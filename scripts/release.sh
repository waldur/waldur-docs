#!/bin/bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

if [ $# -lt 1 ]; then
    echo "Usage: $0 <VERSION>"
    echo "Example: $0 8.0.4"
    exit 1
fi

VERSION=$1

IS_RC=false
if [[ "$VERSION" =~ -rc\. ]]; then
  IS_RC=true
  BASE_VERSION="${VERSION%%-rc.*}"
  echo "(RC release — changelog will be generated; stable $BASE_VERSION will replace it)"
fi

PREV_TAG=$(grep "^## " "$PROJECT_DIR/docs/about/CHANGELOG.md" | grep -v "\-rc\." | head -1 | sed 's/^## \([^ ]*\).*/\1/')
DATE=$(date +%Y-%m-%d)

echo "=== Waldur Release $VERSION ==="
echo "Previous version: $PREV_TAG"
echo ""

# Pre-flight: Verify that the new tag does NOT already exist in any repo
echo "[pre-flight] Checking that tag $VERSION does not already exist..."
REPOS=(
    "$PROJECT_DIR/../waldur-mastermind"
    "$PROJECT_DIR/../waldur-homeport"
    "$PROJECT_DIR/../waldur-helm"
    "$PROJECT_DIR/../waldur-docker-compose"
)

TAG_EXISTS_IN=""
for repo_path in "${REPOS[@]}"; do
    repo_name=$(basename "$repo_path")
    if [ -d "$repo_path/.git" ]; then
        if git -C "$repo_path" rev-parse "$VERSION" >/dev/null 2>&1; then
            TAG_EXISTS_IN="$TAG_EXISTS_IN $repo_name"
        fi
    fi
done

if [ -n "$TAG_EXISTS_IN" ]; then
    echo "ERROR: Tag $VERSION already exists in:$TAG_EXISTS_IN"
    echo "Cannot create a release with an existing tag. Aborting."
    exit 1
fi
echo "  Tag $VERSION does not exist in any repository. Good to proceed."
echo ""

# Step 1: Collect commit data from local repos
echo "[1/5] Collecting commit data from local repositories..."
LOCAL_REPOS='{"waldur-mastermind":"'"$PROJECT_DIR"'/../waldur-mastermind","waldur-homeport":"'"$PROJECT_DIR"'/../waldur-homeport","waldur-helm":"'"$PROJECT_DIR"'/../waldur-helm","waldur-docker-compose":"'"$PROJECT_DIR"'/../waldur-docker-compose"}'

python3 "$SCRIPT_DIR/generate-enhanced-changelog-multiRepo.py" "$VERSION" "$PREV_TAG" \
    --json-output --local-repos "$LOCAL_REPOS" > /tmp/waldur-release-data.json

CORE_COMMITS=$(python3 -c "import json,sys; d=json.load(sys.stdin); print(d['summary_stats']['core_commits'])" < /tmp/waldur-release-data.json)
echo "  Collected $CORE_COMMITS core commits"
echo ""

# Step 2: Build prompt and call Claude Code
echo "[2/5] Generating changelog with Claude Code..."

PROMPT_TEMPLATE=$(cat "$SCRIPT_DIR/prompts/changelog-prompt.md")

# Perform placeholder substitution
FULL_PROMPT="${PROMPT_TEMPLATE//\{VERSION\}/$VERSION}"
FULL_PROMPT="${FULL_PROMPT//\{PREV_VERSION\}/$PREV_TAG}"
FULL_PROMPT="${FULL_PROMPT//\{DATE\}/$DATE}"

# For RC releases, append a note to skip the OpenAPI Resources section
if [ "$IS_RC" = "true" ]; then
    FULL_PROMPT="${FULL_PROMPT}

IMPORTANT: This is an RC (release candidate) release. Do NOT include the OpenAPI Resources section (OpenAPI schema links, API changes diff) because no schema is generated for RC releases."
fi

COMMIT_DATA=$(cat /tmp/waldur-release-data.json)

generate_changelog() {
    printf '%s\n\nHere is the commit data:\n\n```json\n%s\n```\n' "$FULL_PROMPT" "$COMMIT_DATA" | \
        env -u CLAUDECODE claude --print > /tmp/waldur-changelog-entry.md
}

generate_changelog

# Show result and ask for confirmation
echo ""
echo "=== Generated Changelog Entry ==="
echo ""
cat /tmp/waldur-changelog-entry.md
echo ""
echo "================================="
echo ""
read -p "Accept this changelog? [y/edit/regenerate/quit] " choice

case $choice in
    y|Y|yes)
        ;;
    edit|e)
        ${EDITOR:-vim} /tmp/waldur-changelog-entry.md
        ;;
    regenerate|r)
        echo "Regenerating..."
        generate_changelog
        echo ""
        cat /tmp/waldur-changelog-entry.md
        echo ""
        read -p "Accept now? [y/edit/quit] " choice2
        case $choice2 in
            edit|e) ${EDITOR:-vim} /tmp/waldur-changelog-entry.md ;;
            y|Y) ;;
            *) echo "Aborted."; exit 1 ;;
        esac
        ;;
    *)
        echo "Aborted."
        exit 1
        ;;
esac

# Step 3: Commit changelog to waldur-docs
echo ""
echo "[3/5] Updating CHANGELOG.md..."

# Remove any existing RC entries for the same base version before prepending
# For RC: removes prior RCs (e.g., 8.0.6-rc.1 when adding 8.0.6-rc.2)
# For stable: removes all RCs (e.g., 8.0.6-rc.* when adding 8.0.6)
if [ "$IS_RC" = "false" ]; then
    BASE_VERSION="$VERSION"
fi
python3 -c "
import re, sys
base = '${BASE_VERSION}'
pattern = re.compile(r'^## ' + re.escape(base) + r'-rc\.\d+\b')
lines = open(sys.argv[1]).readlines()
out, skip = [], False
for line in lines:
    if pattern.match(line):
        skip = True
        continue
    if skip and line.strip() == '---':
        skip = False
        continue
    if skip and line.startswith('## '):
        skip = False
    if not skip:
        out.append(line)
open(sys.argv[1], 'w').writelines(out)
" "$PROJECT_DIR/docs/about/CHANGELOG.md"
echo "  Removed any existing RC entries for $BASE_VERSION"

# Prepend new entry
{
    echo "# Changelog"
    echo ""
    cat /tmp/waldur-changelog-entry.md
    echo ""
    tail -n +3 "$PROJECT_DIR/docs/about/CHANGELOG.md"  # Skip existing "# Changelog\n" header
} > /tmp/final-changelog.md
mv /tmp/final-changelog.md "$PROJECT_DIR/docs/about/CHANGELOG.md"

cd "$PROJECT_DIR"
git add docs/about/CHANGELOG.md
git commit -m "Update changelog for $VERSION"

echo "  Changelog committed."

# Tag and push
echo ""
echo "[4/5] Tagging waldur-docs with $VERSION..."
read -p "Push changelog commit and tag $VERSION to origin? [y/n] " push_choice
if [[ "$push_choice" != "y" && "$push_choice" != "Y" ]]; then
    echo "Aborted. Changelog is committed locally. You can push manually."
    exit 0
fi

git push origin master
cd "$PROJECT_DIR"
git tag -a "$VERSION" -m "Release $VERSION"
git push origin "$VERSION"

echo ""
echo "[5/5] Done!"
echo ""
echo "Tag $VERSION pushed. The CI pipeline will now:"
echo "  - Tag waldur-mastermind, waldur-homeport, waldur-helm, waldur-docker-compose"
echo "  - Bump versions in helm Chart.yaml and docker-compose .env.example"
if [ "$IS_RC" = "false" ]; then
    echo "  - Release SDKs"
    echo "  - Build and deploy documentation"
    echo "  - Generate changelog (if not already committed) and update publiccode.yml"
else
    echo "  - Generate changelog (if not already committed)"
    echo "  (RC release — SDKs, docs deployment, and publiccode.yml are skipped)"
fi

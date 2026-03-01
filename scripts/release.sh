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
  echo "(RC release — changelog generation will be skipped)"
fi

PREV_TAG=$(grep -m 1 "^## " "$PROJECT_DIR/docs/about/CHANGELOG.md" | sed 's/^## \([^ ]*\).*/\1/')
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

if [ "$IS_RC" = "false" ]; then

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

else
echo "[1/2] RC release — skipping changelog generation (steps 1-3)."
fi

# Tag and push
if [ "$IS_RC" = "false" ]; then
    STEP_TAG="4/5"
    STEP_DONE="5/5"
else
    STEP_TAG="2/2"
    STEP_DONE=""
fi

echo ""
echo "[$STEP_TAG] Tagging waldur-docs with $VERSION..."
if [ "$IS_RC" = "false" ]; then
    read -p "Push changelog commit and tag $VERSION to origin? [y/n] " push_choice
else
    read -p "Push tag $VERSION to origin? [y/n] " push_choice
fi
if [[ "$push_choice" != "y" && "$push_choice" != "Y" ]]; then
    if [ "$IS_RC" = "false" ]; then
        echo "Aborted. Changelog is committed locally. You can push manually."
    else
        echo "Aborted. You can tag and push manually."
    fi
    exit 0
fi

if [ "$IS_RC" = "false" ]; then
    git push origin master
fi
cd "$PROJECT_DIR"
git tag -a "$VERSION" -m "Release $VERSION"
git push origin "$VERSION"

echo ""
echo "Done!"
echo ""
echo "Tag $VERSION pushed. The CI pipeline will now:"
echo "  - Tag waldur-mastermind, waldur-homeport, waldur-helm, waldur-docker-compose"
echo "  - Bump versions in helm Chart.yaml and docker-compose .env.example"
if [ "$IS_RC" = "false" ]; then
    echo "  - Release SDKs"
    echo "  - Build and deploy documentation"
    echo "  - Generate changelog and update publiccode.yml"
else
    echo "  (RC release — SDKs, docs deployment, changelog, and publiccode.yml are skipped)"
fi

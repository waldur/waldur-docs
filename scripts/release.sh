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
  echo "(RC release — entry will be added; prior RCs of $BASE_VERSION are kept until stable $BASE_VERSION ships)"
fi

if [ "$IS_RC" = "true" ]; then
    # RC: diff from the most recent prior release — prior RC of the same base if any, otherwise last stable.
    # Exclude the exact current version to make re-runs idempotent.
    PREV_TAG=$(grep "^## " "$PROJECT_DIR/docs/about/CHANGELOG.md" | grep -v "^## $VERSION " | head -1 | sed 's/^## \([^ ]*\).*/\1/')
else
    # Stable: diff from previous stable (skip RCs).
    PREV_TAG=$(grep "^## " "$PROJECT_DIR/docs/about/CHANGELOG.md" | grep -v "\-rc\." | head -1 | sed 's/^## \([^ ]*\).*/\1/')
fi
DATE=$(date +%Y-%m-%d)

CACHE_DIR="$PROJECT_DIR/.cache/release/$VERSION"
mkdir -p "$CACHE_DIR"

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

echo "[pre-flight] Fetching latest from origin in all repositories..."
for repo_path in "${REPOS[@]}"; do
    repo_name=$(basename "$repo_path")
    if [ -d "$repo_path/.git" ]; then
        echo "  Fetching $repo_name..."
        git -C "$repo_path" fetch origin --tags --force --quiet
    else
        echo "  WARNING: $repo_name not found at $repo_path, skipping fetch."
    fi
done
echo ""

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

collect_commit_data() {
    python3 "$SCRIPT_DIR/generate-enhanced-changelog-multiRepo.py" "$VERSION" "$PREV_TAG" \
        --json-output --local-repos "$LOCAL_REPOS" > "$CACHE_DIR/commit-data.json"
}

if [ -f "$CACHE_DIR/commit-data.json" ]; then
    CORE_COMMITS=$(python3 -c "import json,sys; d=json.load(sys.stdin); print(d['summary_stats']['core_commits'])" < "$CACHE_DIR/commit-data.json")
    echo "  Found cached commit data ($CORE_COMMITS core commits)"
    read -p "  Reuse cached commit data? [Y/n] " reuse_data
    if [[ "$reuse_data" =~ ^[Nn] ]]; then
        echo "  Re-collecting..."
        collect_commit_data
    fi
else
    collect_commit_data
fi

CORE_COMMITS=$(python3 -c "import json,sys; d=json.load(sys.stdin); print(d['summary_stats']['core_commits'])" < "$CACHE_DIR/commit-data.json")
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

COMMIT_DATA=$(cat "$CACHE_DIR/commit-data.json")

generate_changelog() {
    printf '%s\n\nHere is the commit data:\n\n```json\n%s\n```\n' "$FULL_PROMPT" "$COMMIT_DATA" | \
        env -u CLAUDECODE claude --print > "$CACHE_DIR/changelog-entry.md"
}

if [ -f "$CACHE_DIR/changelog-entry.md" ]; then
    echo ""
    echo "  Found cached changelog entry:"
    echo ""
    cat "$CACHE_DIR/changelog-entry.md"
    echo ""
    read -p "  Reuse cached changelog? [Y/n/edit] " reuse_cl
    case $reuse_cl in
        [Nn])
            echo "  Regenerating..."
            generate_changelog
            ;;
        edit|e)
            ${EDITOR:-vim} "$CACHE_DIR/changelog-entry.md"
            ;;
    esac
else
    generate_changelog

    # Show result and ask for confirmation
    echo ""
    echo "=== Generated Changelog Entry ==="
    echo ""
    cat "$CACHE_DIR/changelog-entry.md"
    echo ""
    echo "================================="
    echo ""
    read -p "Accept this changelog? [y/edit/regenerate/quit] " choice

    case $choice in
        y|Y|yes)
            ;;
        edit|e)
            ${EDITOR:-vim} "$CACHE_DIR/changelog-entry.md"
            ;;
        regenerate|r)
            echo "Regenerating..."
            generate_changelog
            echo ""
            cat "$CACHE_DIR/changelog-entry.md"
            echo ""
            read -p "Accept now? [y/edit/quit] " choice2
            case $choice2 in
                edit|e) ${EDITOR:-vim} "$CACHE_DIR/changelog-entry.md" ;;
                y|Y) ;;
                *) echo "Aborted."; exit 1 ;;
            esac
            ;;
        *)
            echo "Aborted."
            exit 1
            ;;
    esac
fi

# Step 3: Commit changelog to waldur-docs
echo ""
echo "[3/5] Updating CHANGELOG.md..."

cd "$PROJECT_DIR"

if git log -1 --format="%s" | grep -q "Update changelog for $VERSION"; then
    echo "  Changelog already committed. Skipping commit step."
else
    # Remove any existing entries that this run would duplicate:
    # - The exact $VERSION (in case release.sh was run before for this version
    #   and a later commit broke the git-log guard above).
    # - For stable releases only, also strip RCs of the same base (e.g. 8.0.6-rc.* when adding 8.0.6).
    # - RC releases keep prior RCs of the same base so each RC has its own entry.
    if [ "$IS_RC" = "false" ]; then
        BASE_VERSION="$VERSION"
    fi
    python3 -c "
import re, sys
base = '${BASE_VERSION}'
version = '${VERSION}'
is_rc = '${IS_RC}' == 'true'
patterns = [re.compile(r'^## ' + re.escape(version) + r'\b')]
if not is_rc:
    patterns.append(re.compile(r'^## ' + re.escape(base) + r'-rc\.\d+\b'))
lines = open(sys.argv[1]).readlines()
out, skip = [], False
for line in lines:
    if any(p.match(line) for p in patterns):
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
    if [ "$IS_RC" = "true" ]; then
        echo "  Removed any existing entry for $VERSION (prior RCs of $BASE_VERSION kept)"
    else
        echo "  Removed any existing entries for $VERSION (and RCs of $BASE_VERSION)"
    fi

    # Prepend new entry
    {
        echo "# Changelog"
        echo ""
        cat "$CACHE_DIR/changelog-entry.md"
        echo ""
        tail -n +3 "$PROJECT_DIR/docs/about/CHANGELOG.md"  # Skip existing "# Changelog\n" header
    } > /tmp/final-changelog.md
    mv /tmp/final-changelog.md "$PROJECT_DIR/docs/about/CHANGELOG.md"

    git add docs/about/CHANGELOG.md
    git commit -m "Update changelog for $VERSION"

    echo "  Changelog committed."
fi

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

#!/bin/bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

WATCH=false
ARGS=()
for arg in "$@"; do
    case "$arg" in
        --watch) WATCH=true ;;
        *) ARGS+=("$arg") ;;
    esac
done
set -- "${ARGS[@]+"${ARGS[@]}"}"

if [ $# -lt 1 ]; then
    echo "Usage: $0 [--watch] <VERSION>"
    echo "Example: $0 8.0.4"
    echo ""
    echo "  --watch   after pushing the tag, follow the release pipeline until"
    echo "            it finishes and report which jobs failed. Off by default;"
    echo "            without it the script exits as soon as the tag is pushed."
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

# Most recent NON-RC entry — the true "last stable", independent of whether
# PREV_TAG (used for diffing) is itself a prior RC of the same base. Used as
# --base-stable for assemble_changelog below.
BASE_STABLE=$(grep "^## " "$PROJECT_DIR/docs/about/CHANGELOG.md" | grep -v "\-rc\." | head -1 | sed 's/^## \([^ ]*\).*/\1/')

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

# The structured changelog is assembled by the local mastermind checkout, so
# it must be recent enough to carry entries across RCs. The fetch above only
# moved origin/develop; fast-forward the working tree too, but only when that
# cannot disturb local work (on develop, no tracked changes, no local commits).
echo "[pre-flight] Updating ../waldur-mastermind to origin/develop..."
MM_DIR="$PROJECT_DIR/../waldur-mastermind"
MM_BRANCH=$(git -C "$MM_DIR" symbolic-ref --short -q HEAD || echo "(detached)")
if [ "$MM_BRANCH" != "develop" ]; then
    echo "  WARNING: on branch '$MM_BRANCH', not develop; leaving it as is."
elif [ -n "$(git -C "$MM_DIR" status --porcelain --untracked-files=no)" ]; then
    echo "  WARNING: uncommitted changes to tracked files; leaving it as is."
elif ! git -C "$MM_DIR" merge-base --is-ancestor HEAD origin/develop; then
    echo "  WARNING: local develop has commits not on origin/develop; leaving it as is."
else
    BEHIND=$(git -C "$MM_DIR" rev-list --count HEAD..origin/develop)
    if [ "$BEHIND" -gt 0 ]; then
        git -C "$MM_DIR" merge --ff-only --quiet origin/develop
        echo "  Fast-forwarded $BEHIND commit(s)."
    else
        echo "  Already up to date."
    fi
fi

echo "[pre-flight] Checking that ../waldur-mastermind can assemble the structured changelog..."
ASSEMBLE_HELP=$(cd "$PROJECT_DIR/../waldur-mastermind" && uv run waldur assemble_changelog --help 2>/dev/null || true)
if [[ "$ASSEMBLE_HELP" != *--previous-release* ]]; then
    echo "ERROR: ../waldur-mastermind's assemble_changelog has no --previous-release option."
    echo "Update that checkout to the latest develop (see warning above) and re-run."
    exit 1
fi
echo ""

# Step 1: Collect commit data from local repos
echo "[1/6] Collecting commit data from local repositories..."
LOCAL_REPOS='{"waldur-mastermind":"'"$PROJECT_DIR"'/../waldur-mastermind","waldur-homeport":"'"$PROJECT_DIR"'/../waldur-homeport","waldur-helm":"'"$PROJECT_DIR"'/../waldur-helm","waldur-docker-compose":"'"$PROJECT_DIR"'/../waldur-docker-compose"}'

collect_commit_data() {
    python3 "$SCRIPT_DIR/generate_enhanced_changelog_multi_repo.py" "$VERSION" "$PREV_TAG" \
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
echo "[2/6] Generating changelog with Claude Code..."

PROMPT_TEMPLATE=$(cat "$SCRIPT_DIR/prompts/changelog-prompt.md")

# Perform placeholder substitution
FULL_PROMPT="${PROMPT_TEMPLATE//\{VERSION\}/$VERSION}"
FULL_PROMPT="${FULL_PROMPT//\{PREV_VERSION\}/$PREV_TAG}"
FULL_PROMPT="${FULL_PROMPT//\{DATE\}/$DATE}"

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

# Step 2b: Build the structured JSON changelog from the same commit data.
JSON_PROMPT_TEMPLATE=$(cat "$SCRIPT_DIR/prompts/changelog-json-prompt.md")
FULL_JSON_PROMPT="${JSON_PROMPT_TEMPLATE//\{VERSION\}/$VERSION}"
FULL_JSON_PROMPT="${FULL_JSON_PROMPT//\{PREV_VERSION\}/$PREV_TAG}"
FULL_JSON_PROMPT="${FULL_JSON_PROMPT//\{DATE\}/$DATE}"

MASTERMIND_DIR="$PROJECT_DIR/../waldur-mastermind"
NEXT_DIR="$MASTERMIND_DIR/changelog/next"
RELEASE_TYPE="stable"
[ "$IS_RC" = "true" ] && RELEASE_TYPE="rc"

# One fragment file per entry, descriptive-slug filename purely for
# readability when inspecting next/ — assemble_changelog globs *.json there
# and treats each file as one fragment object regardless of name.
# changelog/next/ is gitignored in waldur-mastermind and populated only by
# this script (not a hand-authored/per-MR contribution path), so clearing
# and rewriting it on every call is always safe. Paths are passed as argv
# (not interpolated into the source) to avoid quoting fragility, matching
# the footer-normalization step below.
split_fragments() {
    python3 - "$CACHE_DIR/changelog-fragments.json" "$NEXT_DIR" <<'PY'
import json, os, glob, re, sys

fragments_path, next_dir = sys.argv[1], sys.argv[2]

def slugify(title):
    s = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')
    return s[:60]

data = json.load(open(fragments_path))
os.makedirs(next_dir, exist_ok=True)
for f in glob.glob(os.path.join(next_dir, '*.json')):
    os.remove(f)

seen = {}
for e in data['entries']:
    slug = slugify(e['title'])
    seen[slug] = seen.get(slug, 0) + 1
    if seen[slug] > 1:
        slug = f'{slug}-{seen[slug]}'
    json.dump(e, open(os.path.join(next_dir, f'{slug}.json'), 'w'), indent=2)

print(f"  Wrote {len(data['entries'])} fragments to {next_dir}")
PY
}

generate_changelog_json() {
    printf '%s\n\nHere is the commit data:\n\n```json\n%s\n```\n' "$FULL_JSON_PROMPT" "$COMMIT_DATA" | \
        env -u CLAUDECODE claude --print > "$CACHE_DIR/changelog-fragments.json"
    # The prompt asks for bare JSON, but the model can still wrap it in a
    # code fence; unwrap it rather than make the operator do it by hand.
    python3 - "$CACHE_DIR/changelog-fragments.json" <<'PY'
import re, sys
path = sys.argv[1]
text = open(path).read().strip()
match = re.fullmatch(r"```[a-z]*\s*\n(.*?)\n?```", text, re.S)
if match:
    open(path, "w").write(match.group(1).strip() + "\n")
PY
}

# Valid JSON of the shape split_fragments needs: an object with an entries list.
json_is_valid() {
    python3 -c "import json,sys; d=json.load(sys.stdin); assert isinstance(d, dict) and isinstance(d.get('entries'), list)" \
        < "$CACHE_DIR/changelog-fragments.json" >/dev/null 2>&1
}

# A high or critical security entry puts a banner on the staff UI of every
# deployment behind this release (critical cannot be dismissed), so it needs
# a deliberate yes rather than slipping through with the rest of the JSON.
confirm_security_entries() {
    local flagged
    flagged=$(python3 - "$CACHE_DIR/changelog-fragments.json" <<'PY'
import json, sys
for e in json.load(open(sys.argv[1]))["entries"]:
    urgency = (e.get("security") or {}).get("urgency")
    if e.get("type") == "security" and urgency in ("high", "critical"):
        print(f"    [{urgency}] {e.get('title')}: {e.get('description')}")
PY
)
    [ -z "$flagged" ] && return 0
    echo ""
    echo "  These security entries will show an alert banner on every deployment behind $VERSION:"
    echo "$flagged"
    read -p "  Type 'yes' to publish them: " security_choice
    [ "$security_choice" = "yes" ]
}

# The version this release directly follows, and its release file if one was
# published: an RC continues the previous RC's cumulative entries, and a stable
# release after RCs gets since_previous relative to the last of them. PREV_TAG
# is the right diff base for the commit data, but for a stable release it is
# the previous stable, not the RC just before it.
PREVIOUS="$PREV_TAG"
if [ "$IS_RC" = "false" ] && [ -f "$PROJECT_DIR/docs/changelog/index.json" ]; then
    LAST_RC=$(python3 - "$PROJECT_DIR/docs/changelog/index.json" "$VERSION" <<'PY'
import json, sys
index, version = json.load(open(sys.argv[1])), sys.argv[2]
prefix = f"{version}-rc."
numbers = [
    int(r["version"][len(prefix):])
    for r in index.get("releases", [])
    if r["version"].startswith(prefix) and r["version"][len(prefix):].isdigit()
]
print(f"{prefix}{max(numbers)}" if numbers else "")
PY
)
    [ -n "$LAST_RC" ] && PREVIOUS="$LAST_RC"
fi
PREVIOUS_FILE="$PROJECT_DIR/docs/changelog/releases/$PREVIOUS.json"

if [ -f "$CACHE_DIR/changelog-fragments.json" ] && json_is_valid; then
    echo ""
    echo "  Found cached structured changelog:"
    echo ""
    cat "$CACHE_DIR/changelog-fragments.json"
    echo ""
    read -p "  Reuse cached structured changelog? [Y/n/edit] " reuse_json
    case $reuse_json in
        [Nn])
            echo "  Regenerating..."
            generate_changelog_json
            ;;
        edit|e)
            ${EDITOR:-vim} "$CACHE_DIR/changelog-fragments.json"
            ;;
    esac
else
    if [ -f "$CACHE_DIR/changelog-fragments.json" ]; then
        echo "  Cached structured changelog is not valid JSON — regenerating."
    fi
    generate_changelog_json

    echo ""
    echo "=== Generated Structured Changelog ==="
    echo ""
    cat "$CACHE_DIR/changelog-fragments.json"
    echo ""
    echo "======================================="
    echo ""
    read -p "Accept this structured changelog? [y/edit/regenerate/quit] " json_choice

    case $json_choice in
        y|Y|yes)
            ;;
        edit|e)
            ${EDITOR:-vim} "$CACHE_DIR/changelog-fragments.json"
            ;;
        regenerate|r)
            echo "Regenerating..."
            generate_changelog_json
            echo ""
            cat "$CACHE_DIR/changelog-fragments.json"
            echo ""
            read -p "Accept now? [y/edit/quit] " json_choice2
            case $json_choice2 in
                edit|e) ${EDITOR:-vim} "$CACHE_DIR/changelog-fragments.json" ;;
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

echo ""

# Guard: validate the fragments against assemble_changelog's own schema rules
# right here, while the edit/regenerate loop is still available — catching a
# bad LLM fragment now beats aborting mid-release at step 3, after the
# CHANGELOG.md track has already been generated and accepted.
echo "  Validating structured changelog fragments..."
while true; do
    if ! json_is_valid; then
        echo "  $CACHE_DIR/changelog-fragments.json is not a JSON object with an entries list."
    else
        SUMMARY=$(python3 -c "import json,sys; print(json.load(sys.stdin).get('summary', ''))" < "$CACHE_DIR/changelog-fragments.json")
        ASSEMBLE_ARGS=(--release-version "$VERSION" --date "$DATE" --release-type "$RELEASE_TYPE" --summary "$SUMMARY")
        [ -n "$PREVIOUS" ] && ASSEMBLE_ARGS+=(--previous "$PREVIOUS")
        [ -n "$PREVIOUS" ] && [ -f "$PREVIOUS_FILE" ] && ASSEMBLE_ARGS+=(--previous-release "$PREVIOUS_FILE")
        [ -n "$BASE_STABLE" ] && ASSEMBLE_ARGS+=(--base-stable "$BASE_STABLE")
        [ "$IS_RC" = "true" ] && ASSEMBLE_ARGS+=(--stable-target "$BASE_VERSION")

        split_fragments
        if (cd "$MASTERMIND_DIR" && uv run waldur assemble_changelog "${ASSEMBLE_ARGS[@]}" --dry-run) >/dev/null; then
            echo "  Fragments are valid."
            if confirm_security_entries; then
                break
            fi
            echo "  Security entries not confirmed."
        else
            echo ""
            echo "  Structured changelog fragments failed validation (see errors above)."
        fi
    fi

    read -p "  [edit/regenerate/quit] " fix_choice
    case $fix_choice in
        edit|e) ${EDITOR:-vim} "$CACHE_DIR/changelog-fragments.json" ;;
        regenerate|r) echo "  Regenerating..."; generate_changelog_json ;;
        *) echo "Aborted."; exit 1 ;;
    esac
done
echo ""

# Step 3: Assemble the structured changelog and publish it into waldur-docs.
# Fragments are already split into $NEXT_DIR and validated above (--dry-run
# reads them but doesn't write the release file or clear next/) — this just
# runs assemble_changelog for real.
echo "[3/6] Assembling structured changelog..."

# Subshell: assemble_changelog's _find_project_root() walks up from CWD
# looking for changelog/ or pyproject.toml — must run inside mastermind, and
# must not change this script's own CWD for the steps that follow.
(cd "$MASTERMIND_DIR" && uv run waldur assemble_changelog "${ASSEMBLE_ARGS[@]}")

mkdir -p "$PROJECT_DIR/docs/changelog/releases"
# waldur-docs is where release files are kept; the copy in waldur-mastermind
# (git-ignored there) is only assemble_changelog's output.
mv "$MASTERMIND_DIR/changelog/releases/$VERSION.json" "$PROJECT_DIR/docs/changelog/releases/$VERSION.json"

python3 "$SCRIPT_DIR/update_changelog_index.py" \
    "$PROJECT_DIR/docs/changelog/releases/$VERSION.json" \
    "$PROJECT_DIR/docs/changelog/index.json"

echo "  Structured changelog assembled and published to docs/changelog/."
echo ""

# Step 4: Commit changelog to waldur-docs
echo ""
echo "[4/6] Updating CHANGELOG.md..."

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

    # Normalize the generated entry's footer deterministically instead of
    # trusting the LLM: strip any "### Resources" / trailing "---" it emitted.
    #
    # The OpenAPI schema link is deliberately NOT added here, for either RC or
    # stable releases. RC releases ship no schema at all. For stable releases
    # the schema file does not exist yet at this point and cannot: the
    # `Generate OpenAPI schema` CI job builds it from waldur-mastermind's tag
    # pipeline, which only comes into being once this tag's `release` stage has
    # run. Committing the link now would leave a dangling relative link on
    # master for the whole release, aborting `mkdocs build --strict` there and
    # in every open MR. That CI job adds the link and the schema file in a
    # single commit instead — see scripts/add-changelog-api-link.py.
    #
    # Idempotent — safe to re-run on a cached entry.
    python3 - "$CACHE_DIR/changelog-entry.md" <<'PY'
import re, sys
path = sys.argv[1]
text = open(path).read()
text = re.split(r'\n###\s+Resources\b', text, maxsplit=1)[0].rstrip()
text = re.sub(r'\n-{3,}\s*$', '', text).rstrip()
text += "\n\n---\n"
open(path, "w").write(text)
PY
    if [ "$IS_RC" = "true" ]; then
        echo "  Entry footer normalized (RC — no OpenAPI schema is built, so no link)."
    else
        echo "  Entry footer normalized (schema link is added by CI alongside the schema file)."
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

    # Commit only if something actually changed. The skip check above looks at
    # the last commit subject alone, so a re-run with any commit on top of the
    # changelog commit lands here and regenerates an identical file — and a
    # bare `git commit` on an empty diff aborts the whole script under `set -e`.
    git add docs/about/CHANGELOG.md \
        "docs/changelog/releases/$VERSION.json" \
        docs/changelog/index.json
    if git diff --cached --quiet; then
        echo "  CHANGELOG.md and json files are already up to date for $VERSION — nothing to commit."
    else
        git commit -m "Update changelog for $VERSION"
        echo "  Changelog committed."
    fi
fi

# Tag and push
echo ""
echo "[5/6] Tagging waldur-docs with $VERSION..."
read -p "Push changelog commit and tag $VERSION to origin? [y/n] " push_choice
if [[ "$push_choice" != "y" && "$push_choice" != "Y" ]]; then
    echo "Aborted. Changelog is committed locally. You can push manually."
    exit 0
fi

# Guard: never push a changelog whose relative OpenAPI schema links dangle —
# that would fail `mkdocs build --strict` and poison master (and every open MR).
echo "  Validating changelog OpenAPI schema links..."
python3 "$SCRIPT_DIR/check-changelog-api-links.py"

# Guard: a tag pipeline runs the .gitlab-ci.yml from the tagged commit, so a
# broken pipeline cannot be repaired once the tag exists — during 8.1.0 a job
# that was missing `git` had to be finished by hand because fixing master had
# no effect on the running pipeline. Everything checkable is checked here,
# while the tag is still cheap to not create.
echo "  Validating .gitlab-ci.yml before the tag freezes it..."
if command -v glab >/dev/null 2>&1; then
    LINT=$(python3 - <<'PY'
import json, os, subprocess, sys
payload = json.dumps({"content": open(".gitlab-ci.yml").read()})
proc = subprocess.run(
    ["glab", "api", "--method", "POST",
     "projects/waldur%2Fwaldur-docs/ci/lint",
     "-H", "Content-Type: application/json", "--input", "-"],
    input=payload, capture_output=True, text=True,
)
try:
    result = json.loads(proc.stdout)
except Exception:
    print("SKIP could not reach the CI lint API")
    sys.exit(0)
# An API error (e.g. 401, or 404 when glab resolves the wrong host) comes
# back as {"message": ...} with no verdict. That says nothing about the
# config, so it must not be reported as an invalid one.
if not isinstance(result, dict) or "valid" not in result:
    message = result.get("message") if isinstance(result, dict) else None
    print(f"SKIP the CI lint API returned no verdict: {message or proc.stdout.strip()}")
    sys.exit(0)
if result.get("valid"):
    print("OK")
else:
    print("INVALID " + "; ".join(result.get("errors") or ["unknown error"]))
PY
)
    case "$LINT" in
        OK) echo "    CI config is valid." ;;
        SKIP*) echo "    WARNING: ${LINT#SKIP }" ;;
        *) echo "ERROR: ${LINT#INVALID }" >&2
           echo "Fix .gitlab-ci.yml before tagging — the tag would freeze this config." >&2
           exit 1 ;;
    esac
else
    echo "    WARNING: glab not installed, skipping CI config validation."
fi

# Guard: never cut a release from a red master. Whatever is broken there will
# be broken in the tag pipeline too, and by then it is unfixable in place.
echo "  Checking the latest master pipeline..."
if command -v glab >/dev/null 2>&1; then
    MASTER_STATUS=$(glab api "projects/waldur%2Fwaldur-docs/pipelines?ref=master&per_page=1" 2>/dev/null \
        | python3 -c "import json,sys; d=json.load(sys.stdin); print(d[0]['status'] if d else 'unknown')" 2>/dev/null || echo "unknown")
    case "$MASTER_STATUS" in
        success) echo "    master is green." ;;
        unknown) echo "    WARNING: could not determine master pipeline status." ;;
        *)
            echo "    WARNING: the latest master pipeline is '$MASTER_STATUS'."
            read -p "    Tag anyway? [y/n] " red_master
            if [[ "$red_master" != "y" && "$red_master" != "Y" ]]; then
                echo "Aborted. Changelog is committed locally."
                exit 1
            fi
            ;;
    esac
fi

git push origin master

cd "$PROJECT_DIR"
git tag -a "$VERSION" -m "Release $VERSION"
git push origin "$VERSION"

echo ""
echo "[6/6] Done!"
echo ""
echo "Structured changelog published: docs/changelog/releases/$VERSION.json"
echo "(reachable at docs.waldur.com/latest/changelog/releases/$VERSION.json once deployed)"
echo ""
echo "Tag $VERSION pushed. The CI pipeline will now:"
echo "  - Tag waldur-mastermind, waldur-homeport, waldur-helm, waldur-docker-compose"
echo "  - Bump versions in helm Chart.yaml and docker-compose .env.example"
if [ "$IS_RC" = "false" ]; then
    echo "  - Release SDKs"
    echo "  - Build and deploy documentation (including docs/changelog/)"
    echo "  - Generate changelog (if not already committed) and update publiccode.yml"
else
    echo "  - Generate changelog (if not already committed)"
    echo "  - Build and deploy documentation via the master-push trigger (including docs/changelog/)"
    echo "  (RC release — SDK release and publiccode.yml are skipped)"
fi

# Everything that went wrong in the 8.1.0 release happened after this point,
# with the operator already looking away. --watch keeps the script attached to
# the pipeline it just started and reports the outcome.
if [ "$WATCH" = "true" ]; then
    echo ""
    echo "[watch] Following the release pipeline for $VERSION..."
    if ! command -v glab >/dev/null 2>&1; then
        echo "  glab is not installed — cannot watch. Follow the pipeline manually."
        exit 0
    fi
    python3 "$SCRIPT_DIR/watch-release-pipeline.py" "$VERSION"
else
    echo ""
    echo "Re-run with --watch to follow the pipeline instead of exiting here."
fi

# waldur-docs

Documentation for Waldur, an open-source hybrid cloud management platform. This repository contains comprehensive documentation for administrators, developers, integrators, and end-users, built using MkDocs with Material theme.

## Documentation Structure

Each top-level directory is one tab of the site, or part of one:

| Tab | Directory | Contents |
|-----|-----------|----------|
| Get started | `get-started/` | Quickstarts: try, use, deploy, call the API, contribute |
| Use Waldur | `user-guide/` | End-user, service provider, call manager and staff tasks in the UI |
| Operate Waldur | `admin-guide/` | Deployment, configuration, identity providers, providers, operations |
| Integrations | `integrations/` | Third-party integrations |
| Build with Waldur | `integrator-guide/`, `developer-guide/` | API, SDK, CLI, Terraform, Ansible; Waldur internals |
| About | `about/` | Concepts, terminology, changelog, governance |

Navigation comes from the `.pages` files, see [CLAUDE.md](CLAUDE.md#navigation).

## Prerequisites

- [uv](https://docs.astral.sh/uv/getting-started/installation/) for Python dependency management
- Node.js (for markdown linting)

## Local Development

1. Install dependencies:

    ```bash
    uv sync
    npm install
    ```

2. Start the development server:

    ```bash
    uv run mkdocs serve
    ```

    The documentation will be available at `http://127.0.0.1:8000`.

## Building and Testing

### Build Documentation

```bash
# Standard build
uv run mkdocs build

# Strict build (catches errors)
uv run mkdocs build --strict --verbose
```

### Lint Markdown Files

```bash
node lint-markdown.mjs
```

### Deploy Versioned Documentation

```bash
# Deploy as latest
uv run mike deploy latest -p

# Deploy specific version
uv run mike deploy 7.8.3 -p
```

## Management Scripts

The `scripts/` directory contains utilities for documentation and changelog management:

### External Documentation Management

```bash
# Sync documentation from external repositories
python3 scripts/sync-external-docs.py

# Validate external documentation sync status
python3 scripts/validate-external-sync.py

# List local documentation files (not imported from external sources)
python3 scripts/list-local-docs.py
python3 scripts/sync-external-docs.py --list-local
```

### Enhanced Changelog Management

```bash
# Generate enhanced changelog entry for a specific version
python3 scripts/generate_enhanced_changelog_multi_repo.py 7.9.0 7.8.9

# Regenerate individual changelog entries with enhanced format
python3 scripts/regenerate-changelog-entry.py 7.9.0 7.8.9
python3 scripts/regenerate-changelog-entry.py 7.9.0  # auto-detect previous version

# Update multiple recent versions
python3 scripts/regenerate-changelog-entry.py --update-recent 5

# List all versions in current changelog
python3 scripts/regenerate-changelog-entry.py --list-versions
```

**Enhanced changelog features:**
- Multi-repository commit analysis across 8 Waldur repositories
- Accurate functional change statistics (excludes tests, auto-generated files)
- Component-level file and line change breakdowns
- Direct commit links for traceability
- Core repository vs SDK separation
- Professional language formatting

## Documentation for the AI assistant

Waldur's AI assistant answers "how do I…" questions from these pages. Every build
splits the site into sections (`hooks/docs_corpus.py`, configured in
`docs-corpus.yml`), and the `Publish docs corpus` CI job publishes them as
`docs-corpus.jsonl.gz` for mastermind to ship.

A portal can switch features off, and the assistant must not walk an end user
through a menu their portal does not have. So a page or section that describes a
feature that can be switched off says what it needs:

```markdown
---
requires:
  - setting:PAT_ENABLED
---

# Personal access tokens
```

A section of a page that is otherwise always available is tagged on its heading,
and the tag covers the headings below it:

```markdown
## 1. Get a token { data-requires="setting:PAT_ENABLED" }
```

- Terms are `setting:<KEY>`, `feature:<section.key>`, `!feature:<section.key>` (the
  flag is off), `offering_type:<type>` and `capability:<name>`. The keys are the ones
  mastermind publishes in
  `docs/admin-guide/mastermind-configuration/docs-requires-vocabulary.json`; a term
  outside it fails the build. Several terms are all required.
- A section that refers to a gated feature without depending on it (a menu listing,
  "if your portal offers…") says so with `{ data-mentions="setting:PAT_ENABLED" }`, or
  for the whole page with `mentions:` in the front matter.
  The build warns about any end-user section that matches one of the phrases under
  `mentions:` in `docs-corpus.yml` and carries neither tag; the strict build in CI
  fails on it.
- `corpus: false` in the front matter, or `{ data-corpus="false" }` on a heading,
  keeps a page or section out of the assistant's search, for pages that only link
  to others.
- Terms that start with `!` must be quoted in front matter (`- "!feature:x"`): unquoted,
  YAML reads them as a tag and MkDocs drops the whole front matter. The build warns
  when that happens.
- Pages synced from other repositories cannot carry front matter here; give them their
  tags under `tags:` in `docs-corpus.yml`, by path and, for one section, by anchor.
  Use the same for a heading that links point to: markdownlint does not read the
  attribute list, so it reports those links as broken.

How the assistant's search finds a section (measured in waldur/waldur-docs!548 on
questions the pages were not written for):

- **One task per heading, named with its verb and object**: "Create a project",
  not "Project management" or "Creation". The search stems words, so "Creating"
  and "Create" match alike, but nouns ("creation", "membership") do not match the
  verbs people type, and "Adding" stems to `ad`, which "add" does not match.
- **A concept question gets its own heading, worded as the question**: "How
  organizations and projects differ". Headings in a how-to page that explain
  ("What happens at a limit", "When the end date arrives") are taken as concept
  sections, which the search weights up for "what is" and "difference" questions.
  Set a page's kind with `type: concept` (or `howto`, `reference`) in front matter,
  or a section's with `{ data-kind="concept" }`, where the rules in
  `docs-corpus.yml` guess wrong.
- **Questions a section answers** are in `docs-questions.yml`, matched by the search
  but never shown, so "invite a colleague" finds "Add project members". After
  changing pages, refresh the entries of new and changed sections with
  `scripts/section_questions.py` (it needs an OpenAI-compatible LLM; see the
  script), and correct any question by hand.

`scripts/lint_docs_structure.py` checks these rules on every pipeline, for the
pages in `questions_scope`:

| Rule | Finds | Instead |
|------|-------|---------|
| DS001 | "Adding …": the search stems it to `ad`, which "add" does not match | "Add …" |
| DS002 | a how-to heading that names a topic: "Project creation" | the task with its verb: "Create a project" |
| DS003 | a heading that says nothing: "Overview", "Details" | what the section is about |
| DS004 | over 450 words before the next heading | a heading per task or topic |
| DS005 | "the table above", "see above": a section is read on its own | name what you refer to |
| DS006 | a concept page with no section worded as its question | "What is an offering", "How X and Y differ" |

Findings that predate the linter are listed in `docs-structure-baseline.txt` and do
not fail the build; new ones do. When you fix a listed one, run
`uv run python scripts/lint_docs_structure.py --update-baseline` to drop its line;
it never adds one. A finding you mean to keep goes in only with `--accept-new`,
where reviewers see it in the diff. `--all` lists the baselined findings as well.

To look at the corpus a build produces:

```bash
DOCS_CORPUS_OUT=/tmp/docs-corpus.jsonl.gz uv run mkdocs build
```

## Releasing a New Version

Releases are driven from this repository. Pushing a version tag here triggers the CI pipeline that tags all child repositories, bumps versions in Helm/Docker Compose, and releases SDKs.

### Local release with Claude Code (recommended)

The `scripts/release.sh` script uses Claude Code to generate a human-quality changelog from local repo checkouts, then lets you review it before committing and tagging.

**Prerequisites:**

- [Claude Code CLI](https://docs.anthropic.com/en/docs/claude-code) installed (`claude` on PATH)
- Sibling checkouts of the Waldur repos (on the branch/commit you want to release):
  ```
  workspace/
  ├── waldur-docs/              # this repo
  ├── waldur-mastermind/
  ├── waldur-homeport/
  ├── waldur-helm/
  └── waldur-docker-compose/
  ```

**Usage:**

```bash
bash scripts/release.sh 8.0.4
```

The script will:

1. Collect commit data from the local repos (commits since the previous tag)
2. Feed the data to Claude Code to generate a changelog entry
3. Show the result for review — you can **accept**, **edit**, **regenerate**, or **quit**
4. Prepend the entry to `docs/about/CHANGELOG.md` and commit
5. Ask for confirmation, then push the commit and tag to origin

The CI pipeline detects that the changelog entry already exists and skips auto-generation.

### CI-only release (fallback)

If Claude Code is not available, you can push a tag directly and the CI pipeline will auto-generate the changelog using the regex-based Python script:

```bash
git tag -a 8.0.4 -m "Release 8.0.4"
git push origin 8.0.4
```

### Generating JSON commit data (for scripting)

The changelog Python script supports a `--json-output` mode that emits structured commit data (with bodies and per-commit file lists) instead of markdown:

```bash
python3 scripts/generate_enhanced_changelog_multi_repo.py 8.0.4 8.0.3 \
    --json-output \
    --local-repos '{"waldur-mastermind":"../waldur-mastermind","waldur-homeport":"../waldur-homeport"}'
```

Use `--local-repos` to read from local checkouts instead of cloning from GitHub. Only the repos listed in the JSON mapping are analyzed.

## CI/CD Pipeline

The GitLab CI pipeline handles:
- Markdown linting and MkDocs validation on merge requests
- Automatic deployment to GitHub Pages for master branch
- Enhanced changelog generation with multi-repository analysis (skipped if entry already exists)
- Version tagging and multi-repository release orchestration

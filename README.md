# waldur-docs

Documentation for Waldur, an open-source hybrid cloud management platform. This repository contains comprehensive documentation for administrators, developers, integrators, and end-users, built using MkDocs with Material theme.

## Documentation Structure

- **admin-guide/** - System deployment, configuration, and administration
- **developer-guide/** - Architecture, development setup, and contribution guidelines
- **user-guide/** - End-user functionality and interfaces
- **integrator-guide/** - API documentation and third-party integrations  
- **integrations/** - Specific integration implementations
- **about/** - Project overview, governance, and changelog

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
python3 scripts/generate-enhanced-changelog-multiRepo.py 7.9.0 7.8.9

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
python3 scripts/generate-enhanced-changelog-multiRepo.py 8.0.4 8.0.3 \
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

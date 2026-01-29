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

## CI/CD Pipeline

The GitLab CI pipeline handles:
- Markdown linting and MkDocs validation on merge requests
- Automatic deployment to GitHub Pages for master branch
- Enhanced changelog generation with multi-repository analysis
- Version tagging and multi-repository release orchestration

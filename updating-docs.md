# External Documentation Management Scripts

This directory contains scripts for the **pull-based** external documentation synchronization system.

## Overview

The Waldur documentation repository uses a pull-based approach to aggregate content from multiple source repositories. This system provides better control and visibility over external content by maintaining source mappings in this repository.

## Scripts

### sync-external-docs.py

Main synchronization script that pulls documentation from external repositories based on the configuration in `external-sources.yml`.

**Usage:**
```bash
# Sync all configured sources
python scripts/sync-external-docs.py

# Sync specific sources only
python scripts/sync-external-docs.py --sources homeport-ui mastermind-api

# List all configured sources
python scripts/sync-external-docs.py --list

# Dry run (show what would be synced)
python scripts/sync-external-docs.py --dry-run
```

**Features:**
- Clones external repositories with authentication
- Maps specific remote folders to local directories
- Adds external document markers to pulled files
- Removes obsolete external files
- Preserves local files (index.md, .pages, README.md)
- Warns about untracked local files

### validate-external-sync.py

Validation script that checks sync status and identifies issues with external documentation.

**Usage:**
```bash
# Validate all sources
python scripts/validate-external-sync.py

# Validate specific sources
python scripts/validate-external-sync.py --sources homeport-ui

# Generate detailed report
python scripts/validate-external-sync.py --report validation-report.txt
```

**Checks:**
- External files have proper markers
- Sync timestamps are recent
- Local files without markers are flagged
- Marker information matches configuration

### external_doc_plugin.py

MkDocs plugin that processes external document markers and adds visual indicators to the rendered documentation.

**Features:**
- Removes HTML comment markers from rendered output
- Adds visual notice boxes at the top of external documents
- Adds "External" badges to page titles
- Provides CSS classes for styling external content

## Configuration

### external-sources.yml

Central configuration file that defines all external documentation sources and their mappings:

```yaml
sources:
  homeport-ui:
    name: "Waldur HomePort UI Documentation"
    repository: "https://gitlab.com/waldur/waldur-homeport.git"
    branch: "develop"
    auth:
      token_env: "HOMEPORT_TOKEN"
    mappings:
      - remote: "docs/developers"
        local: "docs/developer-guide/ui"
        description: "UI development documentation"
    excludes:
      - "*.pyc"
      - "__pycache__"

settings:
  preserve_local:
    - "index.md"
    - ".pages" 
    - "README.md"
  max_sync_age_hours: 24
```

## Sync Behavior

### Pull Process
1. **Clone**: Temporarily clone each configured external repository
2. **Map**: Copy files from remote paths to local paths according to mappings
3. **Mark**: Add external document markers to pulled markdown files
4. **Clean**: Remove obsolete external files that no longer exist in remote
5. **Preserve**: Keep local files that match preserve patterns
6. **Warn**: Flag local files without external markers for manual review

### File Types
- **External Files**: Files with `<!-- EXTERNAL DOCUMENT -->` markers - managed by sync
- **Local Files**: Files without markers that match preserve patterns - kept locally
- **Untracked Files**: Local files without markers that don't match preserve patterns - flagged as warnings

## Authentication

External repositories requiring authentication use environment variables:

```bash
export HOMEPORT_TOKEN="your-token-here"
export MASTERMIND_TOKEN="your-token-here"
export INTEGRATIONS_TOKEN="your-token-here"
```

Tokens are inserted into repository URLs automatically during cloning.

## CI/CD Integration

Include `.gitlab-ci-external-sync.yml` in your main GitLab CI configuration:

```yaml
# .gitlab-ci.yml
include:
  - .gitlab-ci-external-sync.yml
```

**Pipeline Jobs:**
- **validate-external-sync**: Runs on all MRs and branches
- **sync-external-docs**: Runs on master branch and manual triggers
- **post-sync-validation**: Validates documentation after sync
- **scheduled-sync**: For automated daily/weekly syncs

## Dependencies

- Python 3.12+
- PyYAML (`pip install pyyaml`)
- Git (for cloning repositories)
- MkDocs and MkDocs Material theme (for the plugin)
---
name: quality-check
description: Run quality assurance checks on Waldur documentation. Use before committing changes or when validating the build.
allowed-tools: Bash(poetry:*), Bash(node:*), Bash(python:*)
---

# Documentation Quality Checks

Run these checks before committing any documentation changes.

## Quick Check (Required)

```bash
# Lint markdown files
node lint-markdown.mjs

# Build with strict validation (catches broken links, missing files)
poetry run mkdocs build --strict
```

## Full Validation

```bash
# 1. Lint markdown
node lint-markdown.mjs

# 2. Generate llms-full.txt
python3 scripts/generate-llms-txt.py

# 3. Strict build
poetry run mkdocs build --strict

# 4. Validate external sync (if external sources modified)
python scripts/validate-external-sync.py
```

## Local Preview

```bash
# Start development server at http://127.0.0.1:8000
poetry run mkdocs serve
```

## Linting Rules

The `lint-markdown.mjs` script enforces:

| Rule | Setting | Reason |
|------|---------|--------|
| MD013 (line length) | Disabled | Documentation has flexible line lengths |
| MD007 (list indent) | Disabled | Flexible indentation allowed |
| MD033 (inline HTML) | Disabled | HTML needed for advanced formatting |
| MD012 (blank lines) | Disabled | Multiple blank lines permitted |

## Common Issues

### Broken Links
- MkDocs strict build will fail on broken links
- Use relative links: `../admin-guide/deployment/helm/`
- Check file paths match actual structure

### Missing Files
- Ensure referenced images exist in `img/` directories
- Verify `.pages` navigation references valid files

### External Document Edits
- Files with `<!-- EXTERNAL DOCUMENT -->` cannot be edited locally
- Use `/sync-external` skill for external content

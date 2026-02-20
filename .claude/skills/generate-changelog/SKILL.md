---
name: generate-changelog
description: Generate or regenerate Waldur changelog entries. Use for release documentation or fixing changelog issues.
disable-model-invocation: true
---

# Enhanced Changelog Generation

Waldur uses multi-repository analysis for professional changelog entries.

## Features

- Analyzes commits across 8 Waldur repositories
- Excludes tests, auto-generated files (template.json, docs, SDK clients)
- Provides component-level breakdowns with file/line changes
- Links directly to GitHub commits
- Separates core development from auto-generated SDK clients

## Commands

```bash
# Generate changelog for a new release
python3 scripts/generate-enhanced-changelog-multiRepo.py <new_version> <previous_version>

# Example: Generate changelog for 7.9.1 from 7.9.0
python3 scripts/generate-enhanced-changelog-multiRepo.py 7.9.1 7.9.0

# Regenerate a specific entry
python3 scripts/regenerate-changelog-entry.py <new_version> <previous_version>

# Update most recent N entries
python3 scripts/regenerate-changelog-entry.py --update-recent 5
```

## Output Format

The script outputs a markdown changelog entry:

```markdown
## 7.9.1

**Release Date:** 2026-01-24

### Notable Changes

- Feature: Description of new feature
- Fix: Description of bug fix
- Improvement: Description of enhancement

### Statistics

| Component | Files Changed | Lines Added | Lines Removed |
|-----------|---------------|-------------|---------------|
| MasterMind | 45 | +1,234 | -567 |
| HomePort | 23 | +456 | -123 |
```

## CI/CD Integration

Changelog generation runs automatically in GitLab CI when a tag is created:
- Triggered by tags matching `^\d+\.\d+\.\d+$`
- Updates `docs/about/CHANGELOG.md`
- Commits and pushes to master
- Rotates old entries (keeps last 20)

## Troubleshooting

If the script fails:
1. Ensure `GITLAB_TOKEN` is set for private repository access
2. Check network connectivity to GitLab
3. Verify tag names are correct semantic versions

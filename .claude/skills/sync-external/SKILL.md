---
name: sync-external
description: Sync documentation from external Waldur repositories. Use when updating externally-sourced docs or checking sync status.
disable-model-invocation: true
---

# External Documentation Sync

Waldur docs pulls content from multiple external repositories. Files marked with `<!-- EXTERNAL DOCUMENT -->` are auto-managed.

## Key Rule

**Never edit external files directly.** Changes will be overwritten on next sync.

## External Sources

Configuration is in `external-sources.yml`. Current sources:

| Source | Repository | Local Path |
|--------|------------|------------|
| MasterMind API | waldur-mastermind | `docs/developer-guide/`, `docs/admin-guide/mastermind-configuration/` |
| HomePort UI | waldur-homeport | `docs/developer-guide/ui/` |
| Docker Compose | waldur-docker-compose | `docs/admin-guide/deployment/docker-compose/` |
| Site Agent | waldur-site-agent | `docs/admin-guide/providers/site-agent/` |
| Keycloak Mapper | waldur-keycloak-mapper | `docs/integrations/waldur-keycloak-mapper/` |
| Ansible Generator | ansible-waldur-generator | `docs/integrator-guide/ansible/` |
| Helm | waldur-helm | `docs/admin-guide/deployment/helm/` |
| SDK Reference | waldur-sdk-docs-generator | `docs/api-reference/` |

## Commands

```bash
# Full sync (requires GITLAB_TOKEN)
python scripts/sync-external-docs.py

# Sync specific sources
python scripts/sync-external-docs.py --sources homeport-ui mastermind-api

# Validate sync status
python scripts/validate-external-sync.py

# Check which files are external vs local
python scripts/list-local-docs.py
```

## Editing External Content

1. Find the source repository URL in the file header
2. Make changes in the source repository
3. Wait for or trigger a sync
4. Run `python scripts/sync-external-docs.py` to pull changes

## Preserved Local Files

Some files are preserved even in external directories (defined in `external-sources.yml`):
- `index.md`
- `.pages`
- Custom images and scripts

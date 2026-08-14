# CLAUDE.md

Waldur Documentation repository - MkDocs Material site for the Waldur hybrid cloud platform.

## Quick Reference

```bash
# Development server
poetry run mkdocs serve

# Quality checks (ALWAYS run before committing)
node lint-markdown.mjs && poetry run mkdocs build --strict
```

## Project Structure

```
docs/
├── admin-guide/        # Deployment, configuration (sysadmins)
├── developer-guide/    # Architecture, contribution (developers)
├── user-guide/         # UI workflows (end users)
├── integrator-guide/   # API, SDK usage (integrators)
├── integrations/       # Third-party integrations
└── about/              # Project info, changelog
```

The generated API reference is **not** in this repository. It lives in
[`waldur/api-docs`](https://code.opennodecloud.com/waldur/api-docs) and is published at
<https://api-docs.waldur.com/> (moved out in `0ed2b1d7f`, WAL-9565).

**Config files:** `mkdocs.yml`, `external-sources.yml`, `pyproject.toml`

## Key Rules

1. **Use relative links** between docs: `../admin-guide/deployment/helm/`
2. **Never edit files with `<!-- EXTERNAL DOCUMENT -->`** - these sync from other repos
3. **Use kebab-case** for filenames: `installation-guide.md`
4. **Place images** in `img/` subdirectories within each guide
5. **Run quality checks** before every commit

## Documentation Style

- MkDocs extensions: `admonition`, `pymdownx.superfences`, `pymdownx.tabbed`
- Use `!!! tip`, `!!! warning`, `!!! danger` for callouts
- Videos need `autoplay` and `muted` attributes
- Screenshots go in `docs/*/img/` directories

## Markdown Linting

Disabled rules (see `lint-markdown.mjs`):
- MD013: Line length (flexible)
- MD007: List indentation (flexible)
- MD033: Inline HTML (allowed)
- MD012: Multiple blank lines (allowed)

## Skills Available

Use `/skill-name` for detailed workflows:

| Skill | Purpose |
|-------|---------|
| `/add-docs` | Add new documentation files |
| `/sync-external` | Sync from external repositories |
| `/generate-changelog` | Generate release changelog |
| `/generate-llms-txt` | Generate LLM documentation files |
| `/quality-check` | Run full QA validation |

## External Documentation

8 repositories sync to this docs site via `external-sources.yml`. Key mappings:

- `waldur-helm` → `docs/admin-guide/deployment/helm/`
- `waldur-docker-compose` → `docs/admin-guide/deployment/docker-compose/`
- `waldur-site-agent` → `docs/admin-guide/providers/site-agent/`

Run `python scripts/sync-external-docs.py` to pull updates.

## Common Tasks

| Task | Command |
|------|---------|
| Preview docs | `poetry run mkdocs serve` |
| Lint markdown | `node lint-markdown.mjs` |
| Strict build | `poetry run mkdocs build --strict` |
| Sync external | `python scripts/sync-external-docs.py` |
| Generate llms.txt | `python3 scripts/generate-llms-txt.py` |
| Deploy version | `poetry run mike deploy <version>` |

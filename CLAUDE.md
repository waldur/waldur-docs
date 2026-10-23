# CLAUDE.md

Waldur Documentation repository - MkDocs Material site for the Waldur hybrid cloud platform.

## Quick Reference

```bash
# Development server
poetry run mkdocs serve

# Quality checks (ALWAYS run before committing)
node lint-markdown.mjs && poetry run mkdocs build --strict
```

A strict build fails when the checkout path contains a dot-directory, such as a `ws env` worktree
under `.worktrees/`: include-markdown's `exclude` glob skips dot-directories, so
`templates.md` is no longer excluded. Build through a path without one, e.g. a symlink:
`mkdocs build --strict -f /path/without/dots/mkdocs.yml`.

## Project Structure

```
docs/
├── get-started/        # Quickstarts (hand-written)
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

## Navigation

Tabs and sidebars come from `.pages` files (the `awesome-pages` plugin), not from `mkdocs.yml`.
A page's URL is its file path, and product code, packaging READMEs and the changelog JSON fetch
link to those URLs, so **restructure navigation by editing `.pages`, never by moving files**.

- `docs/.pages` maps top-level directories to tabs: Get started (`get-started/`), Use Waldur
  (`user-guide/`), Operate Waldur (`admin-guide/`), Integrations, Build with Waldur
  (`integrator-guide/` + `developer-guide/`), About.
- End every `nav:` list with `...`, so pages added by the external sync appear on their own.
  Hide a page deliberately with a filter: `- ... | regex=^(?!page-name)`.
- A tab can only group **top-level** directories. A nested path such as `admin-guide/providers`
  in `docs/.pages` becomes a plain link and drops those pages from the nav; group nested
  directories in their own guide's `.pages` instead.
- `.pages` files inside synced directories are safe: the sync only removes files that carry the
  external-document marker.

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

9 repositories sync to this docs site via `external-sources.yml`. Key mappings:

- `waldur-helm` → `docs/admin-guide/deployment/helm/`
- `waldur-docker-compose` → `docs/admin-guide/deployment/docker-compose/`
- `waldur-site-agent` → `docs/admin-guide/providers/site-agent/`
- `rancher-keycloak-operator` → `docs/admin-guide/providers/rancher-keycloak-operator/` (README and Keycloak setup only)

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

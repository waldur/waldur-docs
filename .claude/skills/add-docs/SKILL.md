---
name: add-docs
description: Add new documentation to Waldur docs. Use when creating new markdown files, adding guides, or documenting features.
---

# Adding New Documentation

Follow these steps when adding new documentation to the Waldur docs repository.

## 1. Identify Target Audience

Choose the appropriate directory based on who will read the documentation:

| Audience | Directory | Content Type |
|----------|-----------|--------------|
| System administrators | `docs/admin-guide/` | Deployment, configuration, maintenance |
| Developers | `docs/developer-guide/` | Architecture, code contributions, plugins |
| End users | `docs/user-guide/` | UI workflows, features, self-service |
| Integrators | `docs/integrator-guide/` | API usage, SDK, third-party integration |
| General | `docs/about/` | Project info, governance, changelog |

## 2. Create the File

- Use **kebab-case** for filenames: `installation-guide.md`, `api-authentication.md`
- Place in the appropriate subdirectory
- Create `img/` subdirectory if screenshots are needed

## 3. Write Content

Use these MkDocs Material extensions:

```markdown
# Page Title

Brief introduction paragraph.

## Section with Admonition

!!! tip
    Helpful tip content here.

!!! warning
    Important warning content.

## Code Examples

```bash
poetry run mkdocs serve
```

## Tabbed Content

=== "Option A"
    Content for option A

=== "Option B"
    Content for option B
```

## 4. Add Navigation

Edit the `.pages` file in the directory to control ordering:

```yaml
nav:
  - index.md
  - your-new-file.md
  - ...
```

## 5. Validate

Run quality checks before committing:

```bash
# Preview locally
poetry run mkdocs serve

# Lint markdown
node lint-markdown.mjs

# Build with strict validation
poetry run mkdocs build --strict
```

## Style Guidelines

- Use relative links between documents: `../admin-guide/deployment/helm/`
- Add screenshots to `img/` subdirectories
- Videos need `autoplay` and `muted` attributes
- Keep paragraphs concise and scannable

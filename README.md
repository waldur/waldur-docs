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

- [Poetry](https://python-poetry.org/docs/#installation) for Python dependency management
- Node.js (for markdown linting)

## Local Development

1. Install dependencies:

    ```bash
    poetry install
    npm install
    ```

2. Start the development server:

    ```bash
    poetry run mkdocs serve
    ```

    The documentation will be available at `http://127.0.0.1:8000`.

## Building and Testing

### Build Documentation

```bash
# Standard build
poetry run mkdocs build

# Strict build (catches errors)
poetry run mkdocs build --strict --verbose
```

### Lint Markdown Files

```bash
node lint-markdown.mjs
```

### Deploy Versioned Documentation

```bash
# Deploy as latest
poetry run mike deploy latest -p

# Deploy specific version
poetry run mike deploy 7.8.3 -p
```

## CI/CD Pipeline

The GitLab CI pipeline handles:
- Markdown linting and MkDocs validation on merge requests
- Automatic deployment to GitHub Pages for master branch
- Version tagging and multi-repository release orchestration

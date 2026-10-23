# Contribute to Waldur

Waldur is open source under the MIT license. Fixes, features, documentation and translations are welcome. Read the [contribution guidelines](../about/contributing.md) first: keep each merge request to one clear scope, follow the code conventions, and make sure linters and tests pass.

## Set up a development environment

- **Backend (MasterMind):** [Installation guide](../developer-guide/guides/install-from-src.md), either with Dev Containers or from source with `uv`.
- **Frontend (HomePort):** [Development setup](../developer-guide/ui/development-setup.md).

## Before you open a merge request

- [Build, test and lint commands](../developer-guide/guides/build-commands.md)
- [Code style](../developer-guide/guides/waldur-code-style.md)
- [Testing guide](../developer-guide/guides/waldur-testing-guide.md)

## Code repositories

| Repository | What it is |
| ---------- | ---------- |
| [waldur-mastermind](https://github.com/waldur/waldur-mastermind) | Backend: REST API, orchestration, marketplace, billing |
| [waldur-homeport](https://github.com/waldur/waldur-homeport) | Web interface |
| [waldur-site-agent](https://github.com/waldur/waldur-site-agent) | Agent that connects service provider backends such as SLURM to Waldur |
| [waldur-helm](https://github.com/waldur/waldur-helm) | Helm chart for Kubernetes |
| [waldur-docker-compose](https://github.com/waldur/waldur-docker-compose) | Docker Compose deployment |
| [py-client](https://github.com/waldur/py-client) | Python SDK (`waldur-api-client` on PyPI) |
| [ansible-waldur-module](https://github.com/waldur/ansible-waldur-module) | Ansible modules for the Waldur API |

## Where to go next

- [Developer guide](../developer-guide/index.md): architecture, core concepts and internals
- [Governance](../about/governance.md)
- [Reporting issues](../about/reporting-issues.md)

---
hide:
  - navigation
  - toc
---

# Waldur introduction

Waldur is a platform for managing hybrid cloud resources. It is used both for controlling internal enterprise IT resources and
for selling cloud services. It includes a rich functionality for managing service catalogues and supports integration
of services managed by other Waldur deployments.

Waldur is composed of the following main components:

- [Waldur MasterMind](https://github.com/waldur/waldur-mastermind/) - broker and orchestrator of cloud services. Responsible for technical service delivery and
    connected matters. Exposes REST API for management
- [Waldur HomePort](https://github.com/waldur/waldur-homeport/) - web-based self-service portal. Talks REST to MasterMind.

Waldur is open-source, extendable and comes with a [professional support](about/support.md).

To get a quick feeling what Waldur is, take a look at some [screenshots](about/screenshots.md).

If you are interested in deploying, check the [getting started](about/getting-started.md) section!

![Overview](assets/waldur_overview.png)

# Getting started

Installing Waldur is a simple and straightforward process.

## Pick method of installation

There are 2 supported methods:

- [Using Docker Compose](../admin-guide/deployment/docker-compose/index.md). Fastest but runs on a single server.
- [Using Helm](../admin-guide/deployment/helm/index.md). For deploying on Kubernetes clusters.

## Configure Waldur

Tune Waldur configuration to match your deployment. Majority of the configuration is done on Mastermind side.
Exact method of configuration depends on the chosen method of installation.
Settings are grouped by modules, you can see all available ones in
the [configuration guide](../admin-guide/mastermind-configuration/configuration-guide.md).

The most typical aspects for configuration are:

- Configuring [identity providers](../admin-guide/identities/summary.md). Waldur supports a range of OIDC and SAML based IdPs.
- [Adding offerings](../user-guide/service-provider-organization/adding-an-offering.md) for sharing among Waldur users.

!!! tip
    For easier management of Waldur deployments and configuration we
    provide [Ansible playbooks](../admin-guide/managing-with-ansible.md).

## Profit

You are done! If you are happy and want to support the project, make sure you check the [support page](support.md).

!!! danger
    Before going to production, make sure you have completed
    the [go-live checklist](../admin-guide/checklist-for-production.md).

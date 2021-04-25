# Getting started

Installing Waldur is a simple and straightforward process.

## Pick method of installation

There are 2 supported methods:

- [Using docker-compose](admin-guide/deployment/docker-compose.md). Fastest but runs on a single server.
- [Using Helm](admin-guide/deployment/kubernetes.md). For deploying on Kubernetes clusters.

## Configure Waldur

Tune Waldur configuration to match your deployment. Majority of the configuration is done on Mastermind side.
Exact method of configuration depends on the chosen method of installation.
Settings are grouped by modules, you can see all available ones in
the [configuration guide](admin-guide/mastermind-configuration/configuration-guide.md).

The most typical aspects for configuration are:

- [White-labelling](admin-guide/whitelabelling.md). Setting custom logos and terms of usage.
- [Identity providers](admin-guide/identity-providers.md). Waldur supports a wide range of OIDC and SAML based IdPs.
- [FreeIPA configuration](admin-guide/freeipa.md) for integrating Waldur users with external services.


!!! tip
    For easier management of Waldur deployments and configuration we 
    provide [Ansible playbooks](admin-guide/managing-with-ansible.md). 

## Profit!

You are done! If you are happy and want to support the project, make sure you check the [support page](about/support.md).

!!! danger
    Before going to production, make sure you have completed 
    the [go-live checklist](admin-guide/checklist-for-production.md).


# Operate Waldur

This guide is for the people who deploy and run a Waldur instance.

## Deploy

Check the [hardware requirements](hardware-requirements.md), then install with [Docker Compose](deployment/docker-compose/index.md) on a single server or [Helm](deployment/helm/index.md) on Kubernetes. Before going live, work through the [go-live checklist](checklist-for-production.md).

## Configure

The [configuration options](mastermind-configuration/configuration-guide.md) list every setting; [general configuration](mastermind-configuration/general.md), [email](mastermind-configuration/email.md) and [notifications](mastermind-configuration/notifications.md) are where most deployments start. Optional features such as the [AI assistant](ai-assistant.md), [Matrix chat](matrix-chat.md) and the [web shell](web-shell.md) are configured here too.

## Identity and access

Connect identity providers such as [Keycloak](identities/keycloak.md), [eduTEAMS](identities/eduTEAMS.md), [MyAccessID](identities/MyAccessID.md) or [LDAP](identities/LDAP.md). The [summary](identities/summary.md) lists the supported providers and their protocols.

## Providers

Connect the systems that deliver resources: [OpenStack](providers/openstack.md), [VMware vSphere](providers/vmware.md), [Azure](providers/azure.md), HPC clusters through the [site agent](providers/site-agent/index.md), other Waldur instances through [remote offerings](providers/remote-waldur.md), or anything else with [custom scripts](providers/custom-scripts.md).

## Run

Understand the [architecture](architecture.md), set up [backups](backups.md) and [monitoring](grafana.md), and use the [debugging guide](debugging.md) and [Waldur shell](waldur-shell.md) when something goes wrong. [Billing and accounting](billing-and-accounting.md) explains how usage is tracked, priced and invoiced.

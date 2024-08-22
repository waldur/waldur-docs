# Remote Offering

!!! warning
    Documentation is in progress. Plugin development is in progress.

## Introduction

It is possible to import into a Waldur offerings from a remote Waldur.

## Pre-requisites

- An organization in the remote Waldur, which will contain requests and projects from the local Waldur.
- Account with owner role that will be used for integration.
- Access to APIs of remote Waldur.

## High level process

- In local Waldur, make sure that you have a [service provider](/docs/user-guide/adding-an-offering.md) organization available.
- Click on "Import offering".
- Input remote Waldur API and authentication token.
- Select the remote organization and offering to be imported.
- Review and activate the offering.

## eduTEAMS account SYNC

In case both local and remote Waldurs are relying on a common set of identities
from [eduTEAMS](../identities/eduTEAMS.md), it is possible to configure synchronisation of the identities as well,
i.e. when a resource is provisioned in a remote Waldur, local accounts from organization and project are pushed and
mapped to the remote project.

!!! note
    For this to work, remote Waldur must be integrated with eduTEAMS registry and integration user must have
    `identity_manager` role.

## Remote offering actions

Remote offering actions are available in the integration section of the offering edit page.

[![Remote Offering Actions](img/remote-offering-actions.png)](img/remote-offering-actions.png)

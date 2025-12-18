# Azure

## Overview

This guide will help you set up Azure integration with Waldur by creating a service principal and collecting the necessary credentials. You can use either the **Azure CLI** (recommended) or the **Azure Portal**.

## Prerequisites

- An Azure account with an active subscription
- One of the following:
  - **Azure CLI installed** (for CLI method) - [Install Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)
  - **Sufficient Azure permissions** (for either method):
    - To create service principals: **Cloud Application Administrator** role or higher in Microsoft Entra ID
    - To assign roles: **Owner** or **User Access Administrator** role on the subscription

## Login to Azure CLI

```bash
az login
```

This will open a browser window for authentication. Complete the login process.

## Get Your Subscription ID

```bash
az account show --query id --output tsv
```

Save this value - you'll need it for Waldur configuration.

## Register Resource Providers

To avoid errors when creating Virtual Machines and related resources, register the necessary resource providers:

```bash
# Register Network
az provider register --namespace Microsoft.Network

# Register Compute
az provider register --namespace Microsoft.Compute

# Register Storage
az provider register --namespace Microsoft.Storage
```

**Verify registration:**

```bash
az provider show -n Microsoft.Network --query "registrationState"
# Should output: "Registered"
```

## Create Service Principal with Role Assignment

Run the following command to create a service principal with **Contributor** access to your subscription:

```bash
az ad sp create-for-rbac \
  --name "waldur-integration" \
  --role Contributor \
  --scopes /subscriptions/<YOUR_SUBSCRIPTION_ID>
```

Replace `<YOUR_SUBSCRIPTION_ID>` with the subscription ID from Step 2.

!!! tip
    You can use a different role if needed. See [Azure built-in roles](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles) for other options.

## Save the Output

The command will output JSON containing all the credentials you need:

```json
{
  "appId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "displayName": "waldur-integration",
  "password": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "tenant": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
}
```

**Map these values for Waldur:**

- `appId` → **Client ID**
- `password` → **Client Secret**
- `tenant` → **Tenant ID**
- Subscription ID from Step 2 → **Subscription ID**

!!! warning
    The `password` (Client Secret) is only shown once. Save it immediately in a secure location.

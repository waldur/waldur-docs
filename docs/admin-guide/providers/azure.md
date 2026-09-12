# Azure

## Overview

Waldur offers Microsoft Azure virtual machines through the Azure plugin of the
[Waldur Site Agent](site-agent/index.md). The agent runs at the provider site, holds the Azure
service principal credentials and talks to Azure Resource Manager; Waldur itself does not
connect to Azure. Customers order machines from a Site Agent offering in the marketplace.

| Action in Waldur | Effect on Azure |
|---|---|
| Create a resource | A running virtual machine, with its own resource group, virtual network, subnet, public IP address and network interface |
| Terminate the resource | The virtual machine and its network objects are deleted |
| Pause or downscale (staff actions) | The virtual machine is deallocated, so compute is no longer billed; its disks remain |
| Restore the resource | The virtual machine is started again |

There are no start, stop or restart actions, and a plan change does not resize a machine.
Usage is reported as allocation: the cores, memory and disk of the machine's size, for as long
as the machine exists.

Setting up the integration takes three steps:

1. [Create a service principal](#prepare-azure) in the Azure subscription the machines run in.
2. [Create a Site Agent offering](#create-the-offering) in Waldur.
3. [Configure and run the agent](#configure-the-agent) with the credentials and the offering's UUID.

## Prerequisites

- An Azure account with an active subscription
- **Azure CLI installed** - [Install Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli).
  The steps below use the CLI; the same can be done in the Azure Portal.
- **Sufficient Azure permissions**:
    - To create service principals: **Cloud Application Administrator** role or higher in Microsoft Entra ID
    - To assign roles: **Owner** or **User Access Administrator** role on the subscription
- A host at the provider site for the Waldur Site Agent, with HTTPS access to Waldur and to Azure

## Prepare Azure

### Log in to the Azure CLI

```bash
az login
```

This will open a browser window for authentication. Complete the login process.

### Get your subscription ID

```bash
az account show --query id --output tsv
```

Save this value - you'll need it for the agent configuration.

### Register resource providers

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

### Create a service principal with a role assignment

Run the following command to create a service principal with **Contributor** access to your subscription:

```bash
az ad sp create-for-rbac \
  --name "waldur-integration" \
  --role Contributor \
  --scopes /subscriptions/<YOUR_SUBSCRIPTION_ID>
```

Replace `<YOUR_SUBSCRIPTION_ID>` with the subscription ID from [Get your subscription ID](#get-your-subscription-id).

!!! tip
    You can use a different role if needed. See [Azure built-in roles](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles) for other options.

### Save the output

The command will output JSON containing all the credentials you need:

```json
{
  "appId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "displayName": "waldur-integration",
  "password": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "tenant": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
}
```

**Map these values to the agent's backend settings:**

- `appId` → `client_id`
- `password` → `client_secret`
- `tenant` → `tenant_id`
- Subscription ID → `subscription_id`

!!! warning
    The `password` (Client Secret) is only shown once. Save it immediately in a secure location.

## Create the offering

Create a Site Agent offering (offering type `Marketplace.Slurm`) as described in the
[Site Agent documentation](site-agent/index.md), and note its UUID: the agent is bound to the
offering by it.

### Components

Give the offering the components the plugin reports: `cpu`, `ram` and `disk`, matching the
`backend_components` of the agent configuration below. The plugin also recognises `cores`,
`memory` and `storage`, or any name mapped with `backend_name`.

### Order options

The order form is the Site Agent order form. Define the machine's parameters as the offering's
order options so that the form asks for them; each overrides the agent's default for one
machine:

| Option | Type | Meaning |
|---|---|---|
| `location` | select | Azure region, e.g. `westeurope` |
| `size` | select | Machine size, e.g. `Standard_B1s` |
| `image` | select | Image as `publisher:offer:sku:version` |
| `ssh_public_key` | text | SSH public key for the administrator account |

The key is the only way into a machine: the administrator password is generated and never
shown. An order without a key is refused before anything is created on Azure.

### Pausing and downscaling

Set the offering's `supports_pausing` and `supports_downscaling` plugin options to let staff
pause and downscale its resources. Both deallocate the machine; restoring the resource starts it.

## Configure the agent

Install the agent as described in the [Site Agent documentation](site-agent/index.md), and
add the offering to its configuration with the Azure backend:

```yaml
offerings:
  - name: Azure VM
    waldur_api_url: https://waldur.example.com/api/
    waldur_api_token: <TOKEN>
    waldur_offering_uuid: <OFFERING_UUID>
    backend_type: azure
    order_processing_backend: azure
    reporting_backend: azure
    backend_settings:
      subscription_id: <SUBSCRIPTION_ID>
      tenant_id: <TENANT_ID>
      client_id: <CLIENT_ID>
      client_secret: <CLIENT_SECRET>
      default_location: westeurope
      default_size: Standard_B1s
      default_image: Canonical:0001-com-ubuntu-server-jammy:22_04-lts:latest
      # Without any range a machine accepts no SSH connections.
      allowed_ssh_ranges:
        - 203.0.113.0/24
    backend_components:
      cpu:
        measured_unit: Cores
        unit_factor: 1
        accounting_type: limit
        label: CPU
      ram:
        measured_unit: MiB
        unit_factor: 1
        accounting_type: limit
        label: RAM
      disk:
        measured_unit: MiB
        unit_factor: 1
        accounting_type: limit
        label: Disk
```

- The four credentials are the values collected in [Save the output](#save-the-output).
- `allowed_ssh_ranges` lists the CIDR prefixes that may reach the machines over SSH. The plugin
  opens port 22 only to these ranges; with none configured, no SSH connections are admitted.
- `default_location`, `default_size` and `default_image` apply when an order does not set the
  corresponding order option.

Run the agent for order processing and usage reporting. The full list of backend settings
(including `default_resource_group`, `network_cidr` and `subnet_cidr`) is in the
[Azure plugin README](https://code.opennodecloud.com/waldur/waldur-site-agent/-/blob/main/plugins/azure/README.md).

## Upgrading from Waldur's built-in Azure integration

Upgrading Waldur converts existing Azure offerings into Site Agent offerings. Their resources
are kept, and the plugin manages the existing machines under their current names and ARM ids.
The upgrade deletes the offerings' Azure service settings, which hold the service principal
credentials.

!!! warning
    Copy the credentials before upgrading. The upgrade deletes them from Waldur.

1. For each Azure offering, copy `subscription_id`, `tenant_id`, `client_id` and
   `client_secret` from its Azure service settings into the agent's `backend_settings`. The
   settings carry the same names in both places.
2. Upgrade Waldur.
3. Run an agent with each offering's UUID as `waldur_offering_uuid`, configured as in
   [Configure the agent](#configure-the-agent).

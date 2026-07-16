# Terraform Provider for Waldur

The Waldur Terraform Provider allows you to automate the provisioning and management of Waldur resources using HashiCorp Terraform. The source code and repository for the provider are available on GitHub at [waldur/terraform-provider-waldur](https://github.com/waldur/terraform-provider-waldur).

This guide covers how to set up the provider and use it to manage projects, users, OpenStack tenants, networks, and virtual machines.

## Provider Configuration

To begin, define the required Waldur provider and configure its settings. You need a Waldur API URL and an API token for authentication.

```hcl
terraform {
  required_providers {
    waldur = {
      source  = "waldur/waldur"
      version = "0.0.10" # Replace with the latest version
    }
  }
}

variable "waldur_api_url" {
  type        = string
  description = "Waldur API base URL (e.g., http://localhost:8080)"
}

variable "waldur_api_token" {
  type        = string
  description = "Waldur API Token"
  sensitive   = true
}

provider "waldur" {
  endpoint = var.waldur_api_url
  token    = var.waldur_api_token
}
```

## Data Sources

Before creating resources, you often need to fetch existing objects from Waldur, such as organizations (customers) or marketplace offerings.

```hcl
# Fetch an organization by name
data "waldur_structure_customer" "org" {
  filters = {
    name_exact = "E2E Organization"
  }
}

# Fetch a marketplace offering for a VPC (OpenStack Tenant)
data "waldur_marketplace_offering" "openstack_vpc" {
  filters = {
    name = "E2E OpenStack Tenant"
  }
}
```

## Creating Resources

The following example demonstrates a comprehensive end-to-end workflow: creating a project, setting up a user, provisioning a VPC, configuring a network, and launching a virtual machine.

### 1. Project Creation

Create a new project under the fetched organization:

```hcl
resource "waldur_structure_project" "project" {
  name        = "terraform-e2e-project"
  customer    = data.waldur_structure_customer.org.url
  description = "Project managed by Terraform"
  backend_id  = "e2e-backend-project-id"
}
```

### 2. User Management & Permissions

Link a new user via Identity Bridge and grant them project manager permissions:

```hcl
# Create user via identity bridge
resource "waldur_identity_bridge_link" "bridge_user" {
  source   = "test:idp"
  username = "e2e-terraform-user"
  email    = "e2e-terraform-user@example.com"
}

# Grant user PROJECT.MANAGER role in the project
resource "waldur_project_permission" "user_access" {
  project = waldur_structure_project.project.id
  user    = waldur_identity_bridge_link.bridge_user.user_uuid
  role    = "PROJECT.MANAGER"
}
```

### 3. Provisioning an OpenStack Tenant (VPC)

Provision a new OpenStack Tenant (VPC) based on the offering fetched earlier.

```hcl
resource "waldur_openstack_tenant" "vpc" {
  name     = "terraform-e2e-vpc"
  project  = waldur_structure_project.project.url
  offering = data.waldur_marketplace_offering.openstack_vpc.url
  plan     = data.waldur_marketplace_offering.openstack_vpc.plans[0].url

  limits = {
    cores   = 4
    ram     = 4096
    storage = 51200
  }

  skip_connection_extnet          = true
  skip_creation_of_default_router = true
}
```

### 4. Network Configuration

Define an SSH key, a network, and a subnet for your instances.

```hcl
resource "waldur_core_ssh_public_key" "ssh_key" {
  name       = "terraform-e2e-key"
  public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDDURXDP5YhOQUYoDuTxJ84DuzqMJYJqJ8+SZT28TtLm5yBDRLKAERqtlbH2gkrQ3US58gd2r8H9jAmQOydfvgwauxuJUE4eDpaMWupqquMYsYLB5f+vVGhdZbbzfc6DTQ2rYdknWoMoArlG7MvRMA/xQ0ye1muTv+mYMipnd7Z+WH0uVArYI9QBpqC/gpZRRIouQ4VIQIVWGoT6M4Kat5ZBXEa9yP+9duD2C05GX3gumoSAVyAcDHn/xgej9pYRXGha4l+LKkFdGwAoXdV1z79EG1+9ns7wXuqMJFHM2KDpxAizV0GkZcojISvDwuhvEAFdOJcqjyyH40000000001 test"
}

resource "waldur_openstack_network" "network" {
  name   = "terraform-e2e-net"
  tenant = waldur_openstack_tenant.vpc.url
}

resource "waldur_openstack_subnet" "subnet" {
  name       = "terraform-e2e-subnet"
  network    = waldur_openstack_network.network.url
  cidr       = "10.0.1.0/24"
  gateway_ip = "10.0.1.1"
  allocation_pools = [
    {
      start = "10.0.1.10"
      end   = "10.0.1.100"
    }
  ]
}
```

### 5. Launching an Instance

Fetch the necessary flavor and image from the provisioned tenant, then launch the virtual machine.

```hcl
# Fetch instance offering in the created VPC
data "waldur_marketplace_offering" "instance_offering" {
  filters = {
    name         = "Virtual machine in ${waldur_openstack_tenant.vpc.name}"
    project_uuid = waldur_structure_project.project.id
  }
}

# Fetch desired flavor
data "waldur_openstack_flavor" "flavor" {
  filters = {
    name        = "m1.tiny"
    tenant_uuid = waldur_openstack_tenant.vpc.id
  }
}

# Fetch desired image
data "waldur_openstack_image" "image" {
  filters = {
    name        = "cirros"
    tenant_uuid = waldur_openstack_tenant.vpc.id
  }
}

# Create the instance
resource "waldur_openstack_instance" "instance" {
  name               = "terraform-e2e-instance"
  project            = waldur_structure_project.project.url
  offering           = data.waldur_marketplace_offering.instance_offering.url
  flavor             = data.waldur_openstack_flavor.flavor.url
  image              = data.waldur_openstack_image.image.url
  ssh_public_key     = waldur_core_ssh_public_key.ssh_key.url
  system_volume_size = 1024
  data_volume_size   = 1024

  ports = [
    {
      subnet = waldur_openstack_subnet.subnet.url
    }
  ]
}
```

### 6. Provisioning a SLURM Allocation

You can also request other marketplace offerings, such as a SLURM HPC allocation, using the generic `waldur_marketplace_order` resource.

First, fetch the SLURM marketplace offering:

```hcl
# Fetch SLURM marketplace offering
data "waldur_marketplace_offering" "slurm_offering" {
  filters = {
    name = "SLURM HPC Allocation"
  }
}
```

Then, create a SLURM allocation order:

```hcl
# Create a SLURM allocation order
resource "waldur_marketplace_order" "slurm_order" {
  offering = data.waldur_marketplace_offering.slurm_offering.url
  project  = waldur_structure_project.project.url
  plan     = data.waldur_marketplace_offering.slurm_offering.plans[0].url

  attributes = {
    name        = "terraform-e2e-slurm"
    description = "SLURM allocation created by Terraform"
  }

  limits = {
    cpu = 10
    ram = 20
    gpu = 2
  }
}
```

## Outputs

You can output the UUIDs and URLs of the created resources to use them elsewhere or reference them in scripts.

```hcl
output "project_uuid" {
  value = waldur_structure_project.project.id
}

output "vpc_uuid" {
  value = waldur_openstack_tenant.vpc.id
}

output "user_uuid" {
  value = waldur_identity_bridge_link.bridge_user.user_uuid
}

output "permission_uuid" {
  value = waldur_project_permission.user_access.id
}

output "instance_uuid" {
  value = waldur_openstack_instance.instance.id
}

output "slurm_order_uuid" {
  value = waldur_marketplace_order.slurm_order.id
}
```

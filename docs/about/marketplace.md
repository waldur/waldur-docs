# Marketplace concept

The **Marketplace** is a central module in Waldur designed for the provisioning and lifecycle management of various resources. It provides a unified interface where users can browse, request, and manage services offered by different service providers within the platform.

Each **offering** in the Marketplace is published by a **Service Provider**, which is a specialized type of organization in Waldur. Offerings may include anything from virtual machines (via OpenStack), HPC compute time (via SLURM), container environments (via Rancher), and more — depending on the enabled plugins.

The Marketplace streamlines complex backend processes and enables:
- Discovery of services through categorized offerings
- Resource provisioning through a request-based model (orders & plans)
- Monitoring of resource usage
- Support for accounting and invoicing based on consumption

The core logic of the Marketplace relies on several interconnected modules in Waldur: the **Structure**, **Service Catalog**, and **Provisioning** modules. These modules work together to ensure secure access control, service configuration, and automated resource delivery.


## Architecture Breakdown

The Marketplace module operates through the collaboration of three core modules in Waldur: **Structure**, **Service Catalog**, and **Provisioning**. Each module plays a distinct role in enabling the end-to-end service delivery process.

- **Structure module**  
  Defines the organizational context by managing **Organizations** and **Projects**. Users operate within projects, and access rights are enforced at this level.

- **Service Catalog module**  
  Allows **Service Providers** to create and configure **Offerings**, including pricing models (**Plans**), resource components, and custom request forms. Offerings are categorized and structured using sections and attributes.

- **Provisioning module**  
  Handles the service lifecycle. When a user places an order, it creates an **Order Item**, which leads to the provisioning of a **Resource**. The module also tracks **Component Usage** for accounting and monitoring purposes.


The architecture below illustrates the interaction between these modules

![Diagram of marketplace concepts](img/marketplace-structure.png)


## What Makes an Offering Marketplace-ready?

To be listed in the Waldur Marketplace, an offering must be properly configured and published by a service provider. While technical steps and plugin-specific instructions (e.g. SLURM, OpenStack) are detailed in separate offering creation guides, the following elements are essential for any offering to become Marketplace-ready:

- **Category**  
  Defines where the offering appears in the Marketplace and helps users browse available services by type (e.g. HPC, Virtual Machines, Storage).

- **Offering**  
  Represents the actual service available to users. It must include a name, description, associated plugin type, and linked service settings.

- **Plan**  
  Specifies resource limits and pricing. A single offering can include one or more plans, allowing service providers to define different resource tiers or pricing models.

- **Plan Components**  
  Identify what is being measured or billed (e.g. CPU hours, memory, GPU usage). These components are especially important for usage-based billing.

- **Visibility and Project Permissions**  
  The offering must be marked as *shared* and made visible to selected customers or projects for it to appear in the Marketplace.

- **Attributes and Request Form (optional)**  
  Providers may configure custom attributes to collect additional parameters from users when they place an order.

An offering becomes Marketplace-ready once these elements are correctly configured and saved. Only then will it appear to users in the Marketplace interface.

## Supported Backends and Marketplace Plugins

Each plugin enables resource provisioning and lifecycle management for a specific type of infrastructure or service.

The following plugins are currently supported and documented:

- **[OpenStack](https://docs.waldur.com/latest/user-guide/service-provider-organization/adding-an-offering/#openstack-offering-creation)**  
  Enables users to provision virtual machines, volumes, networks, and floating IPs. Typically used for IaaS environments.

- **[SLURM](https://docs.waldur.com/latest/user-guide/service-provider-organization/adding-an-offering/#slurm-offering-creation)**  
  Allows users to request and consume compute time on HPC clusters. Usage is typically measured in CPU or GPU hours.

Each plugin may have specific configuration requirements, input fields, or resource models. Service providers should consult the relevant plugin documentation when creating offerings for these backends.

## Lifecycle of a Resource in the Marketplace

Once an offering is published in the Marketplace, users can begin interacting with it by placing orders. The process from ordering to resource provisioning follows a clear, structured lifecycle:

1. **Offering is created and published**  
   A service provider defines an offering, including category, plans, components, and visibility settings.

2. **User places an order**  
   A user selects the offering and plan, fills in any required attributes, and submits an order within a project.

3. **Order approval (if required)**  
   Depending on configuration, orders may require approval by a project or customer owner before provisioning.

4. **Resource provisioning**  
   Once approved, the provisioning process is triggered automatically via the connected plugin (e.g. OpenStack, SLURM). A resource is created and becomes visible in the project.

5. **Resource usage tracking**  
   Usage of resource components (such as CPU, memory, storage) is monitored and logged for accounting and reporting.

6. **Resource management**  
   Users can manage the lifecycle of the resource — update, pause, terminate — depending on the plugin and permissions.

This flow is handled seamlessly by the Provisioning module, ensuring consistency across different service types and plugins.

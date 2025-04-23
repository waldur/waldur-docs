# Marketplace concept

## Overview

The Waldur Marketplace serves as a centralized platform for requesting, provisioning, and managing resources from various service providers. This guide explains key concepts and workflows in the Marketplace to help you effectively navigate and utilize its features.

## Core concepts

### Marketplace framework

The Marketplace operates through four integrated modules:

1. **Structure module**: Establishes organizational hierarchy through Organizations and Projects, with access controls enforced at the project level.

2. **Service catalogue module**: Enables Service providers to configure Offerings with pricing models (Plans), resource components, and customized request forms.

3. **Provisioning module**: Manages the complete resource lifecycle from order placement to resource creation, usage tracking, and termination.

4. **Billing module**: Handles financial tracking, invoicing, and cost management for resources provisioned through the Marketplace.


### Key components

- **Service provider**: An organization authorized to publish and deliver services through Waldur.
- **Offering**: A specific service available for provisioning (e.g., virtual machines, HPC compute time).
- **Plan**: A pricing and resource allocation model for an offering.
- **Component**: A measurable resource unit (e.g., CPU hours, storage space) used for tracking consumption.
- **Order**: A formal request for resource provisioning submitted by a user.
- **Resource**: The provisioned service instance that results from a fulfilled order.
- **Invoice**: A financial document detailing resource usage costs for an organization.
- **Invoice item**: An individual billing entry for a specific resource's consumption.

## Architectural framework

```mermaid
flowchart TD
    %% Structure module
    subgraph Structure[Structure module]
        Org[Organization]
        User[User]
        Proj[Project]
        ProjMember[Project member]
        ServiceProvider[Service provider]
    end
    
    %% Service catalogue module
    subgraph Catalog[Service catalogue module]
        Offering[Offering]
        Plan[Plan]
        PluginReg[Plugin registry]
    end
    
    %% Provisioning module
    subgraph Provisioning[Provisioning module]
        Order[Order]
        Resource[Resource]
        MarketplacePlugin[Marketplace plugin]
    end
    
    %% Billing module
    subgraph Billing[Billing module]
        Invoice[Invoice]
        InvoiceItem[Invoice item]
    end
    
    %% Key Relationships
    Org -- has --> Proj
    Org -- becomes --> ServiceProvider
    User -- belongs to --> Proj
    User -- creates --> ProjMember
    ServiceProvider -- provides --> Offering
    Offering -- connects to --> PluginReg
    Offering -- defines --> Plan
    
    ProjMember -- submits --> Order
    Order -- approved by --> ServiceProvider
    Order -- creates --> Resource
    MarketplacePlugin -- processes --> Resource
    
    Resource -- generates --> InvoiceItem
    InvoiceItem -- belongs to --> Invoice
    Invoice -- billed to --> Org
    Resource -- instantiated from --> Offering
    Proj -- contains --> Resource
    
    classDef structureModule fill:#5BAD60,stroke:#333,stroke-width:1px
    classDef catalogModule fill:#5BAD60,stroke:#333,stroke-width:1px
    classDef provisioningModule fill:#5BAD60,stroke:#333,stroke-width:1px
    classDef billingModule fill:#5BAD60,stroke:#333,stroke-width:1px
    
    class Org,User,Proj,ProjMember,ServiceProvider structureModule
    class Offering,Plan,PluginReg catalogModule
    class Order,Resource,MarketplacePlugin provisioningModule
    class Invoice,InvoiceItem billingModule
```

## Offering requirements

For an offering to appear in the Marketplace, it must include:

- **Category assignment**: Determines the offering's location in the Marketplace browsing hierarchy.
- **Basic information**: Name, description, plugin type, and service settings.
- **Plan configuration**: At least one plan defining resource limits and pricing structure.
- **Component definitions**: Specific resources being measured or billed.
- **Visibility settings**: Configuring which customers or projects can access the offering.
- **Optional attributes**: Custom parameters that users must provide when ordering.

## Supported integration plugins

The Marketplace supports various backend systems through dedicated plugins:

- **OpenStack plugin**: Provisions virtual infrastructure including VMs, storage volumes, networks, and IP addresses.
- **SLURM plugin**: Facilitates access to HPC cluster resources with consumption typically measured in CPU or GPU hours.

Each plugin has specific configuration requirements detailed in its dedicated documentation section.

## Resource lifecycle

Resources in the Marketplace follow a defined lifecycle:

1. **Publication**: Service Provider creates and publishes an offering with associated plans.
2. **Order placement**: User selects an offering, chooses a plan, and submits an order within a project context.
3. **Approval process**: Orders may require authorization by project or customer owners based on configured policies.
4. **Provisioning**: Upon approval, the system automatically provisions the requested resource via the appropriate plugin.
5. **Usage monitoring**: The system tracks resource consumption for accounting and reporting purposes.
6. **Management operations**: Users can perform lifecycle operations (update, pause, terminate) as permitted by the plugin and their access rights.
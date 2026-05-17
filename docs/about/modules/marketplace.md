# Marketplace

## Overview

The Waldur Marketplace is the catalog and order pipeline through which projects request resources from service providers. It connects the [platform primitives](platform.md) (users, organizations, projects) to backend systems (OpenStack, SLURM, Rancher, remote Waldur instances, and others) through a uniform offering → order → resource flow.

## Architecture

```d2
direction: down
classes: {
  structure:    { style: { fill: "#e8f5e8"; stroke: "#2e7d32" } }
  catalog:      { style: { fill: "#e1f5fe"; stroke: "#0277bd" } }
  provisioning: { style: { fill: "#fff3e0"; stroke: "#ef6c00" } }
  billing:      { style: { fill: "#f3e5f5"; stroke: "#7b1fa2" } }
}

structure: Structure {
  org: Organization { class: structure }
  project: Project { class: structure }
  user: User { class: structure }
  org -> project: owns
  user -> project: member of
}

catalog: Service catalogue {
  offering: Offering { class: catalog }
  plan: Plan { class: catalog }
  plugin: Plugin { class: catalog }
  offering -> plan: priced by
  offering -> plugin: backed by
}

provisioning: Provisioning {
  order: Order { class: provisioning }
  resource: Resource { class: provisioning }
  order -> resource: creates
}

billing: Billing {
  invoice_item: Invoice item { class: billing }
  invoice: Invoice { class: billing }
  invoice_item -> invoice: rolls up to
}

structure.project -> provisioning.order: submits
catalog.offering -> provisioning.order: ordered
provisioning.resource -> billing.invoice_item: usage
billing.invoice -> structure.org: billed to
```

The four boxes correspond to four Django apps: `structure`, `marketplace`, `marketplace.processors`, and `invoices`.

## Key concepts

| Concept | One-liner | Reference |
|---|---|---|
| Offering | A service published by a service provider (VM family, HPC allocation, ticket queue, ...). | [Glossary](../terminology/glossary.md) |
| Plan | One pricing and limits option attached to an offering. | [Glossary](../terminology/glossary.md) |
| Order | A request to provision, modify, or terminate a resource. | [Lifecycle](lifecycle.md) |
| Resource | The provisioned instance produced by a fulfilled order. | [Lifecycle](lifecycle.md) |
| Plugin | The backend integration that an offering binds to (OpenStack, SLURM, ...). | [Plugins](#plugins) |
| Invoice item | The billing record generated from a resource's usage. | [Billing](../../admin-guide/billing-and-accounting.md) |

## Offering requirements

An offering becomes orderable once it has:

- A **category** (controls where it appears in the catalogue).
- One or more **plans** (defines pricing and limits).
- **Components** (the metered or billed units — vCPU, GB-month, CPU-hours, ...).
- A **plugin type** and matching service settings.
- **Visibility** rules (public, per-customer, per-project).

Custom request-form attributes are optional.

## Plugins

The Marketplace is plugin-driven. Plugins shipped with Waldur include:

| Plugin | What it provisions |
|---|---|
| `openstack` | Tenants, VMs, volumes, networks, floating IPs |
| `slurm` | HPC allocations (CPU/GPU hours, storage) |
| `rancher` | Kubernetes clusters via Rancher |
| `azure`, `vmware` | VMs on the respective backend |
| `openportal` | Federated HPC accounts via the OpenPortal protocol |
| `remote` | Resources hosted on another Waldur instance |
| `support` | Ticket-backed offerings |
| `script` | Arbitrary scripted provisioning |
| `site-agent` | Anything brokered by `waldur-site-agent` |

Service providers can add new plugins by implementing the marketplace processor interface — see the [developer guide](../../developer-guide/core-concepts/marketplace.md).

## Approval and policies

Orders may be auto-approved, gated by an organization owner, or vetoed by a [policy](policies.md) (cost limit, usage limit, blacklist). Per-project auto-approval is configurable.

## Resource lifecycle

Orders and resources have their own state machines — see the dedicated [Lifecycle page](lifecycle.md).

## Related concepts

- [Platform](platform.md) — users, organizations, projects.
- [Call management](call-management.md) — proposal-driven allocation that ends in marketplace orders.
- [Lifecycle](lifecycle.md) — order and resource state machines.

## Examples

!!! example "Requesting a VM"
    1. Open the Marketplace and filter by **Virtual Machines**.
    2. Pick an OpenStack offering and a plan.
    3. Fill in the request form (name, SSH key, flavor).
    4. Submit. After approval, the VM appears in the project.

!!! example "HPC allocation"
    1. Open the SLURM allocation under the project.
    2. Check current CPU-hour and storage usage.
    3. Modify the resource to request more hours if needed.

!!! tip "Cost control"
    Use [policies](policies.md) to cap monthly spend per project rather than relying on after-the-fact invoice review.

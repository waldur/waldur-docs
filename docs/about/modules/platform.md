# Platform

## Overview

Waldur organizes everything around three primitives: **users**, **organizations**, and **projects**. Users get roles inside organizations or projects; resources are grouped under projects; organizations carry the contractual and financial responsibility. Every other Waldur concept — marketplace orders, calls, invoices, policies, quotas — binds to one of these three.

## Structure

```d2
direction: right
classes: {
  primitive: { style: { fill: "#e8f5e8"; stroke: "#2e7d32" } }
  derived: { style: { fill: "#fff8e1"; stroke: "#f57f17" } }
}

user: User { class: primitive; shape: person }
org: Organization { class: primitive }
project: Project { class: primitive }
role: Role { class: derived }
resource: Resource { class: derived }
invoice: Invoice { class: derived }

user -> role: assigned
role -> org: scoped to
role -> project: scoped to
org -> project: owns
project -> resource: contains
org -> invoice: billed
resource -> invoice: charged via items
```

## Key concepts

| Concept | One-liner | Reference |
|---|---|---|
| User | A person or robot account; may hold global roles (staff, support). | [Glossary](../terminology/glossary.md) |
| Organization | A legal entity acting as a customer, a service provider, or both. | [Glossary](../terminology/glossary.md) |
| Project | An access-controlled container for resources inside an organization. | [Glossary](../terminology/glossary.md) |
| Role | A named bundle of permissions, scoped to an organization or a project. | [Roles & permissions](../terminology/roles_and_permissions.md) |
| Resource | A provisioned service instance (VM, HPC allocation, storage volume, ...). | [Marketplace](marketplace.md) |
| Quota | An enforced upper bound on a measurable property within a scope. | [Admin guide](../../admin-guide/mastermind-configuration/configuration-guide.md) |

## Installation types

Waldur reuses the same primitives across three common installation types:

| Type | Typical operator | What an Organization is | What a Project is |
|---|---|---|---|
| Cloud | Commercial or government IaaS | Customer company or agency | Tenant or environment |
| Academic | Single university or research infra | Department or institute | Research group, lab, course |
| Academic shared | Multi-institution federation | Always also a service provider | Allocation granted by a federated allocator |

The role matrix for each shape — Owner, PI, Service Manager, etc. — is documented in [Roles & permissions](../terminology/roles_and_permissions.md).

## Related concepts

- [Marketplace](marketplace.md) — how a project obtains a resource.
- [Call management](call-management.md) — how allocations are awarded through a structured proposal process.

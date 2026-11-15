# Platform

## Overview

Waldur organizes everything around three primitives: **users**, **organizations**, and **projects**. Users get roles inside organizations or projects; resources are grouped under projects; organizations carry the contractual and financial responsibility. Every other Waldur concept — marketplace orders, calls, invoices, policies, quotas — binds to one of these three.

## How organizations and projects differ

An **organization** is the customer: a company, department, faculty or research infrastructure that
holds the contract and is invoiced for what its projects use. Its owners create its projects, manage
its team and see its invoices. An organization can also be a service provider, offering services to
other organizations.

A **project** belongs to one organization and groups the resources a team works with and the people
who use them. Resources are always ordered into a project. A project has its own team — managers,
administrators and members — and its own start and end dates; what its resources cost appears on its
organization's invoice.

In short, the organization is who owns and pays, the project is what is used and by whom. An
organization usually has many projects, and a user can have roles in several organizations and
projects. See [Roles and permissions](../terminology/roles_and_permissions.md) for what each role
may do.

## Structure

```d2
direction: right
classes: {
  primitive: { style: { fill: "#e8f5e8"; font-color: "#1f2328"; stroke: "#2e7d32" } }
  derived: { style: { fill: "#fff8e1"; font-color: "#1f2328"; stroke: "#f57f17" } }
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

## Related concepts { data-corpus="false" }

- [Marketplace](marketplace.md) — how a project obtains a resource.
- [Lifecycle](lifecycle.md) — what happens to that resource over time.
- [Billing](billing.md) — what the organization is invoiced for.
- [Quotas](quotas.md) — up-front bounds on usage per scope.
- [Policies](policies.md) — automated reactions when limits are crossed.
- [Identity](identity.md) — how users get into Waldur.
- [Support](support.md) — how tickets reach the right team.
- [Call management](call-management.md) — how allocations are awarded through a structured proposal process.

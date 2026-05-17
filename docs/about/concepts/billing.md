# Billing & invoicing

## Overview

Waldur tracks the consumption of every [marketplace](marketplace.md) resource and turns it into invoice items, which roll up into monthly invoices per [organization](platform.md). Operators decide pricing in the offering's [plan](marketplace.md); consumers see what they will be charged before they order. Credits, compensations, and prepaid charges are first-class — they are extra invoice items, not a separate billing pipeline.

## How a charge flows

```d2
direction: down
classes: {
  source:  { style: { fill: "#e8f5e8"; stroke: "#2e7d32" } }
  derived: { style: { fill: "#fff8e1"; stroke: "#f57f17" } }
  output:  { style: { fill: "#e1f5fe"; stroke: "#0277bd" } }
}

plan: Plan\n(price per unit) { class: source }
component: Component\n(metered unit) { class: source }
usage: Component usage\n(reported by plugin) { class: source }

item: Invoice item\n(price × usage × period) { class: derived }
credit: Credit\n(prepaid balance) { class: derived }
compensation: Compensation\n(adjustment) { class: derived }

invoice: Monthly invoice { class: output }
org: Organization { class: output; shape: person }

plan -> item: rate
component -> usage: meters
usage -> item: quantity
item -> invoice: appended
credit -> invoice: offset
compensation -> invoice: offset
invoice -> org: billed
```

## Key concepts

| Concept | One-liner | Reference |
|---|---|---|
| Invoice item | A single line on an invoice — one resource, one component, one period. | [Glossary](../terminology/glossary.md) |
| Invoice | A monthly statement aggregating all invoice items for one organization. | [Admin guide](../../admin-guide/billing-and-accounting.md) |
| Billing model | How an offering charges: monthly (limit-based) or prepaid (one-time + recurring). | [Admin guide](../../admin-guide/billing-and-accounting.md#billing-models) |
| Period | The window an invoice item covers — month, quarter, year, or total. | [Glossary](../terminology/glossary.md) |
| Credit | A prepaid balance attached to an organization or project that offsets future invoice items. | [User guide](../../user-guide/customer-organization/credit-management.md) |
| Compensation | An ad-hoc adjustment (refund, discount) applied to an invoice. | — |

## Billing models

Two models cover almost every offering and can be mixed within a single offering:

- **Monthly (limit-based)** — billed each month based on reserved limits; limits can change anytime and the current invoice is adjusted accordingly. Default for OpenStack tenants.
- **Prepaid (one-time + recurring)** — billed upfront for the full subscription period (`price × limit × months`). An end date is required; mid-period limit changes create supplementary charges for the remaining time.

A "Maximum total" limit period exists for flat one-time charges (consultancy hours, setup fees).

## Lifecycle

1. Provider creates an offering with components and a plan.
2. Consumer orders a resource — see [Lifecycle](lifecycle.md).
3. Plugin reports component usage on a schedule.
4. Waldur creates or updates invoice items for the current period.
5. At month end the invoice is closed; credits and compensations are applied.
6. Operator exports the invoice (PDF/CSV/XLSX) or integrates with a payment provider via the API.

## Related concepts

- [Marketplace](marketplace.md) — where pricing is defined.
- [Lifecycle](lifecycle.md) — what state changes trigger billing events.
- [Policies](policies.md) — cap spend before the invoice is closed.
- [Platform](platform.md) — who gets billed.

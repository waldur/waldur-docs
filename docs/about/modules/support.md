# Support

## Overview

Waldur exposes a "Support" interface so consumers and providers can raise tickets without leaving the portal. Tickets can live entirely inside Waldur or be brokered to an external service desk (Jira Service Management, Zammad, SMAX). The ticket lifecycle is the same regardless of backend — what changes is where the canonical record lives.

## Topology

```d2
direction: down
classes: {
  ui:      { style: { fill: "#e8f5e8"; stroke: "#2e7d32" } }
  waldur:  { style: { fill: "#dae8fc"; stroke: "#6c8ebf" } }
  ext:     { style: { fill: "#fff8e1"; stroke: "#f57f17" } }
}

user: User { class: ui; shape: person }
homeport: Homeport\nSupport view { class: ui }

waldur_support: Waldur support backend { class: waldur }

jira: Jira Service Management { class: ext }
zammad: Zammad { class: ext }
smax: SMAX { class: ext }
builtin: Built-in tickets\n(stored in Waldur) { class: ext }

user -> homeport
homeport -> waldur_support: create / comment / close
waldur_support -> jira: sync (configurable)
waldur_support -> zammad: sync
waldur_support -> smax: sync
waldur_support -> builtin: store locally
```

## Key concepts

| Concept | One-liner |
|---|---|
| Issue | A single ticket, with a type (incident, request, change, ...). |
| Comment | A reply on an issue, by the reporter or staff. |
| Attachment | A file attached to an issue or comment. |
| Backend | The system of record — built-in, Jira, Zammad, or SMAX. |
| Mapping | How Waldur issue types and statuses translate to the backend's. |

## Backends at a glance

| Backend | When to use | Where data lives |
|---|---|---|
| Built-in | Small deployments; no existing service desk. | Waldur DB. |
| Jira SM | Existing Atlassian estate; rich SLA tooling. | Jira. |
| Zammad | Open-source preference; multi-channel support. | Zammad. |
| SMAX | Enterprise ITSM integration. | SMAX. |

Setup lives in [admin-guide / service-desk](../../user-guide/staff-users/service-desk/service-desk-config.md) and the [integrations/service-desk](../../integrations/service-desk/service-desk-integrations.md) area for SMAX specifics.

## Lifecycle

1. User opens **Support** in the portal and creates an issue.
2. Waldur posts the issue to the configured backend; the backend assigns an ID and returns it.
3. Comments and status changes sync bidirectionally on the configured cadence.
4. When the backend marks the issue resolved, Waldur reflects it in the portal.

A status mismatch usually means the type/status mapping is out of date — see the per-backend configuration page.

## Related concepts

- [Platform](platform.md) — who can see which tickets (role-scoped).
- [Marketplace](marketplace.md) — "support" can also be an offering type, with each order opening a ticket.

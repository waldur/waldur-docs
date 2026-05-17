# Policies

## Overview

Policies are automated reactions to events on [marketplace](marketplace.md) resources — typically to cap cost, cap usage, or terminate a misbehaving resource. They run alongside [quotas](quotas.md): a quota refuses an action up front, a policy reacts to facts after the fact within a period (this month's spend, this quarter's CPU-hours, this year's storage).

## Model

```d2
direction: right
classes: {
  scope:   { style: { fill: "#e8f5e8"; stroke: "#2e7d32" } }
  policy:  { style: { fill: "#fff8e1"; stroke: "#f57f17" } }
  action:  { style: { fill: "#e1f5fe"; stroke: "#0277bd" } }
}

org: Organization { class: scope }
project: Project { class: scope }
offering: Offering { class: scope }

policy: Policy { class: policy }
trigger: Trigger\n(invoice item, usage report) { class: policy }
period: Period\n(month / quarter / year / total) { class: policy }

notify: Notify { class: action }
block: Block further orders { class: action }
terminate: Terminate resources { class: action }

org -> policy: attached to
project -> policy
offering -> policy
trigger -> policy: evaluated by
period -> policy: scoped to
policy -> notify
policy -> block
policy -> terminate
```

## Key concepts

| Concept | One-liner |
|---|---|
| Policy | A rule attached to a project, customer, or offering scope. |
| Trigger | The signal that evaluates the policy — typically a new invoice item or usage report. |
| Period | The window the trigger sums data over — month, quarter, year, or total. |
| Action | What happens when the policy fires. |
| Action type | **Threshold** (warn at N%, fire at 100%) or **immediate** (act the moment a condition is met). |

## Action catalogue

| Action | Effect |
|---|---|
| Notify project / customer | Email the project members or organization owners. |
| Block creation of new resources | Refuse new orders on the affected scope. |
| Terminate resources | Cancel running resources to stop the bleeding. |
| Block SLURM jobs | (HPC) Pause new job submissions until consumption drops. |
| Custom | Any action wired in via the policy plugin interface. |

A single policy can attach multiple actions.

## Lifecycle

1. Staff (or organization owner, for project-scoped policies) defines a policy: scope, trigger, limit, period, actions.
2. Waldur evaluates the policy each time a new trigger arrives (e.g. an invoice item is written, a SLURM usage report is ingested).
3. When the threshold is crossed, the configured actions execute. A `has_fired` flag prevents repeated firing in the same period.
4. At the next period boundary the flag resets.

## Related concepts

- [Quotas](quotas.md) — up-front bounds; pair with policies for defence in depth.
- [Marketplace](marketplace.md) — what policies guard.
- [Billing](billing.md) — invoice items are the primary trigger for cost policies.
- [Lifecycle](lifecycle.md) — the resource state transitions an "immediate" policy can drive.

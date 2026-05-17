# Quotas

## Overview

Quotas are hard upper bounds on a measurable property within a scope — e.g. "this project can hold at most 20 VMs" or "this organization can use at most 500 vCPU". A quota refuses an action up front when the new value would exceed the limit. Quotas complement [policies](policies.md): a policy reacts after the fact (notify, terminate, block further orders), a quota stops the action before it happens.

## Model

```d2
direction: right
classes: {
  scope: { style: { fill: "#e8f5e8"; stroke: "#2e7d32" } }
  q:     { style: { fill: "#fff8e1"; stroke: "#f57f17" } }
}

org: Organization { class: scope }
project: Project { class: scope }
offering: Offering { class: scope }

q1: vCPU quota { class: q }
q2: VM count quota { class: q }
q3: Project count quota { class: q }

org -> q1: limit + usage
project -> q2: limit + usage
org -> q3: limit + usage
offering -> q1: contributes usage
```

A quota record is `(scope, name, limit, usage)`. Usage is recomputed from the current state of resources; the limit is set by an operator.

## Key concepts

| Concept | One-liner |
|---|---|
| Scope | The object the quota attaches to — organization, project, or offering. |
| Limit | The maximum permitted value. `-1` means unlimited. |
| Usage | The current measured value, derived from resources in scope. |
| Enforcement point | The view or service action that calls `validate_quota_change()` before mutating state. |
| Soft / hard | Some quotas allow brief overage (soft); most refuse the change (hard). |

## Quotas vs. policies vs. plan limits

| Mechanism | Decides when | Failure mode |
|---|---|---|
| **Plan limit** | At order time — what the user can request from this offering. | Order request rejected by the marketplace form. |
| **Quota** | At resource mutation — would this push the scope's usage over the limit? | Action refused with a 400; no state change. |
| **Policy** | After the fact — has usage / cost crossed a threshold within a period? | Notification, block further orders, terminate, or other configured action. |

All three can be in play at once. The order of operations is plan → quota → action → policy.

## Operating quotas

- Set per-organization defaults at offering time (provider) or organization onboarding (operator).
- Override per project to give a team more headroom without inflating the organization-wide cap.
- Quota usage is exposed in the API and on every project / organization dashboard.

## Related concepts

- [Policies](policies.md) — post-hoc enforcement on cost or usage.
- [Marketplace](marketplace.md) — where plan limits originate.
- [Platform](platform.md) — the scopes a quota can attach to.

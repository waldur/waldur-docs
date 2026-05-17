# Policies

!!! note "Draft"
    This page is a placeholder. Full content arrives with the next concept-page batch.

## Overview

Policies are rules that automatically react to events on [marketplace](marketplace.md) resources — typically to cap cost, cap usage, or terminate a misbehaving resource. They run alongside [quotas](platform.md#key-concepts): a quota refuses an action up front, a policy reacts to facts after the fact.

## Key concepts

| Concept | One-liner |
|---|---|
| Policy | A rule attached to a project, customer, or offering scope. |
| Trigger | The signal that evaluates the policy (e.g. an invoice item being written). |
| Action | What happens when the policy fires — threshold notification or immediate enforcement (block, terminate, ...). |
| Period | The window over which the trigger sums data — monthly, quarterly, annual, or total. |

## Related concepts

- [Marketplace](marketplace.md) — what policies guard.
- [Lifecycle](lifecycle.md) — the resource state transitions a policy can drive.

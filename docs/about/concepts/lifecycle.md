# Resource lifecycle

## Overview

Every [marketplace](marketplace.md) order moves through a fixed state machine; once an order succeeds, the resource it creates has its own state machine. Operators and integrators rely on these two state machines to interpret webhook events, debug stuck provisioning, and write [policies](policies.md).

## Order states

```d2
direction: right

pending_consumer: pending\nconsumer
pending_provider: pending\nprovider
pending_project: pending\nproject
pending_start: pending\nstart date
executing
done: done { style: { fill: "#c8e6c9" } }
erred: erred { style: { fill: "#ffcdd2" } }
canceled: canceled { style: { fill: "#eeeeee" } }
rejected: rejected { style: { fill: "#ffcdd2" } }

pending_consumer -> pending_provider: consumer approves
pending_consumer -> rejected: consumer rejects
pending_provider -> pending_project: provider approves
pending_provider -> rejected: provider rejects
pending_project -> pending_start: project approves
pending_project -> rejected
pending_start -> executing: start date reached
executing -> done
executing -> erred
pending_consumer -> canceled: user cancels
pending_provider -> canceled
```

| State | Code | Meaning |
|---|---|---|
| pending-consumer | 1 | Awaiting approval from the consumer organization. |
| executing | 2 | Backend provisioning in progress. |
| done | 3 | Resource provisioned successfully. |
| erred | 4 | Provisioning failed; admin or retry needed. |
| canceled | 5 | User canceled before processing. |
| rejected | 6 | Approval denied. |
| pending-provider | 7 | Awaiting approval from the service provider. |
| pending-project | 8 | Awaiting in-project approval (when configured). |
| pending-start-date | 9 | Approved but waiting for the configured start date. |

## Resource states

```d2
direction: right

creating: Creating
ok: OK { style: { fill: "#c8e6c9" } }
erred: Erred { style: { fill: "#ffcdd2" } }
updating: Updating
terminating: Terminating
terminated: Terminated { style: { fill: "#eeeeee" } }

creating -> ok
creating -> erred
ok -> updating: modify order
updating -> ok
updating -> erred
ok -> terminating: terminate order
terminating -> terminated
terminating -> erred
erred -> updating: retry
erred -> terminating
```

| State | Code | Meaning |
|---|---|---|
| Creating | 1 | Initial provisioning underway. |
| OK | 2 | Steady state; usage being reported. |
| Erred | 3 | Last operation failed; resource is in an inconsistent state. |
| Updating | 4 | A modify order is being applied. |
| Terminating | 5 | Cleanup in progress. |
| Terminated | 6 | Resource removed from the backend; record retained for billing. |

## Recovering an erred order

A staff user can retry an erred order from the UI or via the API. Retry locks the row, re-checks the state inside a transaction, and re-enqueues the backend operation — see the [backend concurrency guidance](../../developer-guide/core-concepts/marketplace-orders.md) for the implementation detail.

## Related concepts

- [Marketplace](marketplace.md) — where orders originate.
- [Policies](policies.md) — automated reactions to state changes (e.g. terminate on overspend).
- [Call management](call-management.md) — proposals that produce orders on approval.

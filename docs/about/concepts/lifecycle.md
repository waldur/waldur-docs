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
done: done { style: { fill: "#c8e6c9"; font-color: "#1f2328" } }
erred: erred { style: { fill: "#ffcdd2"; font-color: "#1f2328" } }
canceled: canceled { style: { fill: "#eeeeee"; font-color: "#1f2328" } }
rejected: rejected { style: { fill: "#ffcdd2"; font-color: "#1f2328" } }

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
ok: OK { style: { fill: "#c8e6c9"; font-color: "#1f2328" } }
erred: Erred { style: { fill: "#ffcdd2"; font-color: "#1f2328" } }
updating: Updating
terminating: Terminating
terminated: Terminated { style: { fill: "#eeeeee"; font-color: "#1f2328" } }

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

## Resource status badge

Resource lists and the resource page show a status badge next to each resource's name. The
badge draws on up to three sources:

| Source | Set for | Values |
|---|---|---|
| Resource state | Every resource | The states in the table above. |
| Backend state | Resources managed through a built-in plugin, such as OpenStack, VMware and Rancher | Waldur's record of the provider-side object: `OK`, `ERRED`, `CREATING` and so on, or `Deleted` once the object is gone. |
| Runtime state | The same resources | What the provider reports, in its own words: `ACTIVE`, `SHUTOFF` or `ERROR` for an OpenStack instance, `in-use` or `error_extending` for a volume, `POWERED_OFF` for a VMware VM. |

Resources managed through a site agent have no backend or runtime state, so their badge shows
the resource state.

The badge shows the first of these that applies:

1. **Erred**, in red, when any source reports a failure.
2. **Terminated**, or **Deleted** when the provider-side object has been removed.
3. The runtime state, such as **Active**, **Shutoff** or **Powered off**: grey for a stopped
   resource, green otherwise. Without a runtime state, the badge shows the backend or resource
   state, for example **OK**.

Hover over an Erred badge to see which source failed:

| Tooltip | Cause |
|---|---|
| The provider reports this resource as *state*. | The runtime state is an error, such as an instance in `ERROR` or a volume in `error_extending`. |
| An operation on the provider side failed. | The backend state is `ERRED`. |
| The last operation on this resource failed. | The resource state is Erred, for example after a failed order. |

When more than one source has failed, the tooltip names the first in this table. The
resource's error message follows, when there is one.

Erred takes precedence even when the provider reports the resource as running: the last
operation failed, so the resource may not match what was ordered. If the provider-side object
recovers, Waldur's next sync with the provider returns the resource to OK. Otherwise, retry the
failed operation, or a staff user or the service provider can set the resource back to OK.

A spinner on the badge means Waldur is still working on the resource: an order is creating,
updating or terminating it, or a provider-side operation has not finished. When the provider
reports which operation it is running, the tooltip names it.

## Recovering an erred order

A staff user can retry an erred order from the UI or via the API. Retry locks the row, re-checks the state inside a transaction, and re-enqueues the backend operation — see the [backend concurrency guidance](../../developer-guide/core-concepts/marketplace-orders.md) for the implementation detail.

## Related concepts

- [Marketplace](marketplace.md) — where orders originate.
- [Policies](policies.md) — automated reactions to state changes (e.g. terminate on overspend).
- [Call management](call-management.md) — proposals that produce orders on approval.

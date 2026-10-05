# Service Desk offerings

A **Service Desk** offering (type `Support.OfferingTemplate`) is a marketplace offering that has no
automated backend: every order becomes an issue in the operator service desk, and a person fulfils it.
Resolving the issue completes the order. Use it for services that are provisioned by hand — consulting,
hardware, accounts in systems Waldur cannot drive.

For the service desk itself, see [Service Desk integrations](service-desk-integrations.md).

## Orders

```d2
direction: right
classes: {
  frontend: { style: { fill: "#d5e8d4"; stroke: "#82b366" } }
  backend:  { style: { fill: "#dae8fc"; stroke: "#6c8ebf" } }
  external: { style: { fill: "#f8cecc"; stroke: "#b85450" } }
}

user: User { class: frontend; shape: person }
order: Order\n(executing) { class: backend }
issue: Issue\n(linked to the order) { class: backend }
desk: Service desk { class: external }
agent: Support agent { class: external; shape: person }
result: Order done or failed,\nresource state updated { class: backend }

user -> order: create / update /\nterminate / restore
order -> issue: open issue
issue -> desk: push
agent -> desk: fulfil, then resolve\nor reject the issue
desk -> issue: webhook: status
issue -> result: status mapped to\nresolved or canceled
```

Each order opens one issue, raised on behalf of the user who created the order. If that user is inactive or
has no email address, the first project manager, administrator or member with one is used, then an
organization owner. Issues of earlier orders for the same resource are linked
to it, and the order's attachment (for example a purchase order) is attached.

| Order | Issue summary |
|---|---|
| Create | Request for *offering* |
| Update — plan switch | Request to switch plan for *resource* |
| Update — limits | Request to update limits for *resource* |
| Update — renewal | Renewal request for *resource* |
| Terminate | Request to terminate resource *resource* |
| Restore | Request to restore resource *resource* |

An order that waits for its start date or for its project to start gets its issue straight away, so the
provider can prepare in advance.

### How the issue completes the order

The order stays *executing* until the issue reaches a status that the service desk configuration maps to
**resolved** or **canceled** — see
[which statuses close a ticket](../../user-guide/staff-users/service-desk/service-desk-config.md#which-statuses-close-a-ticket).

| Order | Issue resolved | Issue canceled |
|---|---|---|
| Create | Resource becomes OK | Order canceled, resource terminated |
| Update | Change is applied | Order and resource erred |
| Terminate | Resource is terminated | Order erred, resource back to OK |
| Restore | Resource is restored | Order canceled, resource stays terminated |

!!! warning
    A status that is mapped to neither outcome leaves the order unchanged. If an order is stuck in
    *executing* although its issue is closed in the service desk, check the status mapping first.

If the issue cannot be created — no project member with an email address, the caller is inactive in the
service desk, or the service desk returns an error — the resource is marked *erred*.

## Membership changes

When **Enable issues for membership changes** is set on the offering, Waldur opens an issue whenever a
user is added to or removed from:

- a project that has an active resource of the offering, or
- a resource of the offering (or one of its resource projects).

The issue names the user, the role, the affected resources and the user's offering username, so the
provider can grant or revoke access in its own systems. One issue is opened per change, raised on behalf of
the affected user. Terminated resources are ignored.

## SSH key changes

When the `ENABLE_ISSUES_FOR_USER_SSH_KEY_CHANGES` setting is on, Waldur opens an issue whenever a user adds
or removes an SSH public key. The issue lists the user's active Service Desk resources, so the provider
can update the key on them. This is a deployment-wide setting, not an offering option.

## Offering options

Set in the offering's **Integration** tab, under **Provisioning configuration**:

| Option | API field | Effect |
|---|---|---|
| Confirmation notification template | `secret_options.template_confirmation_comment` | Posted as the first comment on the issue of a create order |
| Enable issues for membership changes | `plugin_options.enable_issues_for_membership_changes` | See [Membership changes](#membership-changes) |

All automatic issues go to the operator service desk. Provider routing applies to them only as described
in [Provider Helpdesk System](../../developer-guide/provider-helpdesk.md#ticket-routing).

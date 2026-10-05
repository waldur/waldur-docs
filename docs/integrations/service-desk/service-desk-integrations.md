# Service Desk integrations

Waldur supports integrations with several widely used service desk solutions. Integration allows creation of
support requests directly from Waldur. In addition, replies from the support personnel are synchronised with
Waldur so that the end users are never directly exposed to the service desk software. Users can see the
issues' history, current status of active tickets as well as are able to interact with tickets
from within Waldur.

Currently supported service desk solutions:

- [Atlassian ServiceDesk](https://www.atlassian.com/software/jira/service-management) (on-prem and cloud);
- [Zammad](https://zammad.com/en);
- [Microfocus SMAX](https://www.microfocus.com/en-us/smax/predictable-it-service-management).

Without an external system, Waldur's **built-in** service desk ("Basic") keeps tickets in its own database and
lets support staff handle them in the Waldur UI.

## Architecture

A deployment has one **operator service desk** — the built-in one or one of the external systems above. In
addition, each service provider can register its own **provider helpdesk**, to which tickets about that
provider's offerings are routed.

```d2
direction: right
classes: {
  frontend: { style: { fill: "#d5e8d4"; stroke: "#82b366" } }
  backend:  { style: { fill: "#dae8fc"; stroke: "#6c8ebf" } }
  infra:    { style: { fill: "#fff2cc"; stroke: "#d6b656" } }
  external: { style: { fill: "#f8cecc"; stroke: "#b85450" } }
}

user: User { class: frontend; shape: person }
homeport: Homeport\n(Support pages) { class: frontend }

waldur: Waldur {
  api: Mastermind API\n(support module) { class: backend }
  worker: Celery worker { class: backend }
  beat: Celery beat { class: backend }
  db: PostgreSQL { class: infra; shape: cylinder }
}

desk: Operator service desk\nJira SM | Zammad | SMAX\n(or built-in) { class: external }
agent: Support agent { class: external; shape: person }
provider: Provider helpdesk\nJira SM | Zammad | SMAX | email { class: external }
smtp: SMTP { class: infra }

user -> homeport
homeport -> waldur.api: issues, comments,\nattachments
waldur.api -> waldur.db
waldur.beat -> waldur.worker: periodic sync,\nSLA checks
waldur.worker -> desk: create issue,\nadd comment
desk -> waldur.api: webhook
agent -> desk
waldur.worker -> provider: route child issue
provider -> waldur.api: provider webhook
waldur.worker -> smtp: notifications
smtp -> user
```

- **Outbound.** Creating an issue, a comment or an attachment in Waldur is pushed to the service desk by a
  Celery worker. Users never talk to the service desk directly.
- **Inbound.** The service desk calls a Waldur webhook when an agent changes an issue, so status changes
  and replies show up in Waldur. See
  [Synchronising changes back to Waldur](../../user-guide/staff-users/service-desk/service-desk-config.md#synchronising-changes-back-to-waldur-webhooks).
- **Periodic.** Celery beat refreshes reference data from the service desk and evaluates SLAs.
- **Notifications.** Waldur emails the reporter about status changes and replies, and asks for feedback once
  an issue is resolved.
- **Provider routing.** An issue about an offering, or about a resource of one, is copied as a child issue
  to the provider helpdesk of that offering's service provider; comments are forwarded between the two. See
  [Provider Helpdesk System](../../developer-guide/provider-helpdesk.md).

## What is synchronised

| Direction | Mechanism | What |
|---|---|---|
| Waldur → service desk | Celery task on change | Issues, comments, attachments, feedback |
| Service desk → Waldur | Webhook (`/api/support-jira-webhook/`, `/api/support-zammad-webhook/`, `/api/support-smax-webhook/`) | Status, assignee, comments, attachments |
| Provider helpdesk → Waldur | Webhook (`/api/support-provider-webhook/<provider>/<backend>/`) | Same, for the child issue |
| Service desk → Waldur | Every 6 hours | Support users |
| Service desk → Waldur | Daily | Priorities, request types |
| Service desk → Waldur | On demand by staff (`/api/sync-issues/`; Jira SM and SMAX) | All issues — recovers updates missed while webhooks were down |
| Within Waldur | Every 15 and 30 minutes | SLA breaches and warnings |

The built-in service desk needs no synchronisation: Waldur is the system of record.

## When issues are created

Most issues are opened by users in the **Support** section of Waldur. Waldur also opens issues on its own:

| Trigger | Condition | Details |
|---|---|---|
| A user creates an issue | Support is enabled | — |
| An order for a Service Desk offering is created, updated, terminated or restored | Always for that offering type | [Service Desk offerings](service-desk-offerings.md#orders) |
| A Service Desk order waits for its start date or for the project | Always for that offering type | [Service Desk offerings](service-desk-offerings.md#orders) |
| A user is added to or removed from a project or resource | The project has a Service Desk resource whose offering enables membership issues | [Service Desk offerings](service-desk-offerings.md#membership-changes) |
| A user adds or removes an SSH key | `ENABLE_ISSUES_FOR_USER_SSH_KEY_CHANGES` | [Service Desk offerings](service-desk-offerings.md#ssh-key-changes) |
| An issue refers to an offering whose provider has a helpdesk | An active provider helpdesk | [Provider Helpdesk System](../../developer-guide/provider-helpdesk.md#ticket-routing) |

## Related

- [Support concepts](../../about/concepts/support.md) — issues, comments, backends at a glance.
- [Service desk configuration](../../user-guide/staff-users/service-desk/service-desk-config.md) — choosing
  and configuring a backend, status mapping, webhooks.
- [Service Desk offerings](service-desk-offerings.md) — marketplace offerings fulfilled through the service
  desk.
- [Provider Helpdesk System](../../developer-guide/provider-helpdesk.md) — routing, escalation, SLA.

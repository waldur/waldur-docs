# OpenPortal integration

## Overview

OpenPortal is a distributed agent-based infrastructure management protocol that enables Waldur to integrate with remote HPC centres and resource providers. The integration supports award/project management, user provisioning, resource allocation, and usage reporting across institutional boundaries.

!!! note
    OpenPortal is developed by the University of Bristol's Isambard Supercomputing Centre. Source code and documentation: [github.com/isambard-sc/openportal](https://github.com/isambard-sc/openportal)

## Architecture

Waldur talks to the OpenPortal network through the `openportal` Python
library, which connects over local HTTP to a **bridge agent**. The bridge
relays to the portal agent, and from there instructions travel through the
agent chain to the infrastructure provider.

Traffic flows both ways:

- **Outgoing** — Waldur submits an instruction (for example
  `create_project` or `get_usage_report`) as a job through the library and
  polls it until it completes.
- **Incoming** — when a job or notification addressed to Waldur arrives, the
  bridge calls Waldur's signal endpoints (`/api/openportal/fetch_job/` and
  `/api/openportal/fetch_notification/`). Waldur then fetches the job from the
  bridge, processes it in a Celery worker and sends the result back.

```d2
direction: down
classes: {
  waldur: { style: { fill: "#dae8fc"; stroke: "#6c8ebf" } }
  agent:  { style: { fill: "#f8cecc"; stroke: "#b85450" } }
}

portal_side: Portal side {
  waldur: Waldur\n(Mastermind API + Celery) { class: waldur }
  lib: openportal\nPython library { class: waldur }
  bridge: op-bridge\nbridge agent { class: agent }
  portal: op-portal\nportal agent { class: agent }

  waldur -> lib: run jobs
  lib -> bridge: local HTTP
  bridge -> waldur: signal URLs\n(fetch_job, fetch_notification) { style.stroke-dash: 3 }
  bridge <-> portal
}

provider_side: Infrastructure provider {
  provider: op-provider\nprovider agent { class: agent }
  platform: op-clusters\nplatform agent { class: agent }
  instance: op-cluster\ninstance agent { class: agent }
  leaf: Account / scheduler agents\n(FreeIPA, Slurm, filesystem) { class: agent }

  provider <-> platform
  platform <-> instance
  instance <-> leaf
}

portal_side.portal <-> provider_side.provider
```

### Components

| Component | Location | Purpose |
|---|---|---|
| OpenPortal core module | `waldur_openportal/` | Protocol client, job board, award tracking, usage and storage reports, notifications |
| Marketplace OpenPortal | `marketplace_openportal/` | Marketplace processors for allocations on an OpenPortal-managed instance (`OpenPortal` offering type) |
| Marketplace OpenPortal Remote | `marketplace_openportal_remote/` | Marketplace processors for allocations on a remote portal (`OpenPortal Remote` offering type) |
| Bridge agent | Alongside Waldur | Connects the Python library to the OpenPortal network and signals Waldur about incoming jobs |
| Provider-side agents | HPC centre | Manage local accounts, quotas, and usage |

## Capabilities

### Supported operations

Instructions Waldur **sends** to a remote instance or portal:

| Operation | OpenPortal instruction |
|---|---|
| **Create project / award** | `add_project` (instance), `create_project` (remote portal) |
| **Update award** | `update_project` |
| **Delete project** | `remove_project` |
| **Add user to project** | `add_user` |
| **Remove user** | `remove_user` |
| **Set resource limits** | `set_limit` |
| **Get resource limits** | `get_limit` |
| **Get usage report** | `get_usage_report` |
| **Get storage report** | `get_storage_report` |
| **List users / projects / award** | `get_users`, `get_projects`, `get_award` |

Instructions Waldur **answers** when it is the receiving portal for awards
made elsewhere:

| Operation | OpenPortal instruction |
|---|---|
| **Receive / update / remove award** | `create_award`, `update_award`, `remove_award` (or the `*_project` aliases) |
| **Describe awards** | `get_award`, `get_projects`, `get_project_mapping` |
| **Report usage** | `get_usage_report`, `get_usage_reports` |
| **Report storage** | `get_storage_report`, `get_storage_reports` |

### Award metadata (AwardDetails)

When creating or updating projects, the following metadata is transmitted:

- **name**, **description**: Project identification
- **start_date**, **end_date**: Project timeline
- **members**: Map of email → role
- **allocation**: Resource allocation amount with units (CPU-HR, GPU-HR, NHR, etc.)
- **breakdown**: Component-level allocation (e.g., `gpu_hours`, `interactive_cpu_hours`, `project_storage`)
- **award**: Link to award record on funding body system
- **call**: Link to the funding call
- **project_link**: Link to project page on awarding portal
- **renewal**: Link to renewal/extension request page
- **notes**: Append-only timestamped messages between portals
- **membership_control**: Policy for membership changes (`open`, `members_only`, `roles_only`, `locked`)
- **allowed_domains**: Email domain glob patterns permitted to join the project on the remote portal, e.g. `['*.ac.uk']`. An empty list allows no domains; omitting the field places no restriction
- **earliest_approve**: Earliest UTC time the remote portal may approve the award, giving the sender a window to make corrections before provisioning begins

#### Membership control

`membership_control` decides which side is authoritative when the two portals
disagree about who belongs to a project:

| Value | Meaning |
|---|---|
| `open` | The receiving portal manages membership freely |
| `members_only` | Roles are authoritative; membership is not |
| `roles_only` | Membership is authoritative; roles are not |
| `locked` | Both membership and roles are authoritative |

### Usage reporting

The integration supports pulling compute and storage usage:

- **Compute usage**: Daily per-user CPU/GPU/node usage
- **Storage usage**: Quota and consumption snapshots per volume
- **Date range filtering**: Query specific time periods
- **Report remapping**: Translate component names between systems

## Outgoing award lifecycle

Each award Waldur sends to a remote portal is tracked locally as a remote
project record, so that an operator can see what was sent, what the remote
portal confirmed, and what is still outstanding.

| State | Meaning |
|---|---|
| **Pending** | Award details have been sent but not yet confirmed. The remote portal may be awaiting human review |
| **Active** | The award was approved, the project exists on the remote portal, and confirmation was received |
| **Stale** | Nothing has been heard from the remote portal for an unexpectedly long time, so the local view may be out of date |
| **Error** | The request was rejected, or the connection to the remote portal is definitively broken |
| **Deleted** | The local resource was deleted. The record is kept for history and can be revived if a future resource is reconnected |

An **Active** record moves to **Stale** automatically once nothing has been
heard about it for 12 hours, and returns to **Active** on its own the next time
the remote portal answers, for example on a successful usage report fetch.
Pending records are not marked stale. Stale is a warning that the local view
may be wrong, not that anything has failed — it usually points at a
connectivity problem somewhere in the agent chain rather than at the award
itself.

Every award keeps an audit trail of what was sent, what came back, and who
changed what locally, alongside the last set of details sent and the last set
the remote portal confirmed. When those two disagree, the difference is what is
still in flight.

### Managing an award

Organisation owners, support and staff can act on an award directly. Ordinary
project members can see awards for projects they have access to but cannot
change them.

| Action | Effect |
|---|---|
| **Add note** | Appends a timestamped message and sends it to the remote portal in an award update |
| **Set links** | Sets or clears the award, call, project and renewal links |
| **Set allowed domains** | Changes which email domains may join the project remotely |
| **Set membership control** | Changes which side is authoritative for membership and roles |
| **Set earliest approve** | Sets the embargo time before which the remote portal may not approve |
| **Approve now** | Removes the embargo so the remote portal may approve immediately |
| **Hold indefinitely** | Pushes the embargo far into the future, parking the award until released with *Approve now* |
| **Reset to pending** | Clears a rejection locally and returns the award to Pending so changes or a resend can proceed. Sends nothing to the remote portal |
| **Resend request** | Sends the current award details to the remote portal again |

!!! note
    *Reset to pending* only changes local state. If the remote portal rejected
    the award for a reason that still applies, resending it will be rejected
    again — fix the underlying cause first.

## Incoming awards (managed projects)

Waldur can also be the **receiving** portal: another portal, such as an
allocation or review platform, sends an award, and Waldur creates and manages
the corresponding project locally. Each incoming award is tracked as a
**managed project**, identified by the sending portal's project identifier and
the destination it arrived on.

### Project templates

A remote portal can only create projects for which a **project template**
exists. A template is matched on three values — template name, offering and
the sending portal — and defines how its awards land in Waldur:

| Field | Meaning |
|---|---|
| `name` | Template name the sending portal puts in the award's `project_template`, e.g. `ukri` |
| `offering` | Name of the OpenPortal offering the award arrives on — the last agent in the bridge destination, e.g. `isambard-ai`. Free text, not a marketplace offering |
| `portal` | Name of the remote portal allowed to use this template |
| `key` | Optional shared key; when set, the award's `key` must match it |
| `provider` | Service provider organisation that owns the template |
| `customer` | Organisation in which projects are created |
| `shortname` | Naming scheme for project short names. `{year}` becomes the last digit of the year and `{count}` a sequence of letters, so `a{year}{count}` gives `a6a`, `a6b`, … |
| `offerings` | Marketplace offerings whose resources are created automatically once the project is approved |
| `approval_limit` | Credits above which an allocation needs local approval. Empty: never; `0`: every request, including creating the project |
| `max_credit_limit` | Credits above which a request is rejected outright. Empty: no limit; `0`: no projects at all |
| `role_mapping` | Remote role names mapped to local project roles |
| `allocation_units_mapping` | Allocation units per credit, by unit name. An award's allocation is **divided** by this value to give project credits, so `{"GPU-HR": 10}` turns 100 GPU-HR into 10 credits. Units missing from the mapping convert 1:1 |

An award that names no template, an unknown template, or a template not
allowed for the sending portal, or that carries the wrong key, is rejected and
its managed project record is deleted. An award whose end date is more than 30
days in the past is rejected as well.

### What happens to an incoming award

1. **Template check** — the template is resolved and the allocation converted
   to credits. Above `max_credit_limit`, the award is rejected.
2. **Linking** — if the template's organisation already has an active project
   with the same name and no managed project of its own, Waldur links to it,
   but always asks for local approval first.
3. **Approval of creation** — only when `approval_limit` is `0` does creating
   the project wait in **Pending** for a local reviewer. Otherwise the request
   is approved automatically.
4. **Provisioning** — Waldur creates the project in the template's
   organisation and creates resources for the template's default offerings.
   With a non-zero `approval_limit` the project is therefore created straight
   away, and only an allocation above the limit waits for approval (see below).
5. **Synchronisation** — on every update Waldur applies the award's name,
   description, start and end dates, sets the project's credits from the
   allocation, and synchronises members according to
   [membership control](#membership-control) and the
   [membership sync mode](#membership-sync-mode).

Credits follow the same rules on creation and on every later update. An
**increase** above `approval_limit` puts the managed project into Pending until
a reviewer approves it; a decrease is applied straight away. Updates to an
expired project are rejected unless it is still in its grace period, or the
update moves the end date to today or later, which reactivates the project. An
allocation change during the grace period is recorded but not applied to the
project's credits.

When the sending portal removes the award, Waldur deletes only the managed
project record. The local project itself is kept.

### Reviewing managed projects

Staff can always act on a managed project. Other users need both of:

- owner or manager role in the template's `provider` organisation, and
- owner role in the template's `customer` organisation.

If the template has no provider or customer set, only staff can act. Adding a
note is restricted to staff.


| Action | Effect |
|---|---|
| **Approve** | Approves a pending request and provisions or updates the project. Refused before the award's `earliest_approve` time |
| **Reject** | Rejects the request, tells the sending portal, and emails the project's managers and admins |
| **Attach** | Links the managed project to an existing local project, unless that project is already managed |
| **Detach** | Removes the link to the local project, tells the sending portal, and returns the managed project to Pending, so further updates wait for a new approval |
| **Add note** | Appends a note to the managed project (staff only) |
| **Delete** | Deletes the managed project record and tells the sending portal. The local project is kept |

Every received request, approval, rejection, note and change of details is
kept in the managed project's audit trail. Local projects that are not linked
to any managed project are listed separately, which helps when choosing a
project to attach.

## Configuration

### Prerequisites

1. A bridge agent registered in your OpenPortal network
2. The client configuration file exported from that bridge agent (see below)
3. The bridge agent's `signal_url` pointing at Waldur's
   `/api/openportal/fetch_job/` endpoint, so that incoming jobs reach Waldur
4. The bridge agent's `notification_url` pointing at Waldur's
   `/api/openportal/fetch_notification/` endpoint. Without it, changes to
   outgoing awards only reach Waldur on the six-hourly refresh

### Client configuration

Waldur connects to the bridge agent using the client configuration file that
the bridge agent generates, for example:

```bash
openportal-bridge bridge --config python_config.toml
```

The file contains the secrets the client uses to authenticate to the bridge,
so treat it as a credential. Waldur reads it from the path in the
`OPENPORTAL_CONFIG` environment variable. If the variable is unset or the
file cannot be loaded, OpenPortal operations fail with
`OpenPortal is not enabled or configuration is not available` — orders on
OpenPortal offerings error out and incoming jobs are not processed. Some
periodic tasks check first and skip quietly, so a quiet log is not proof that
the configuration is in place.

### Helm configuration

Store the client configuration in a Kubernetes secret under the key
`config.toml`:

```bash
kubectl create secret generic waldur-openportal-config \
  --from-file=config.toml=python_config.toml
```

Then enable the plugin and reference the secret in your Waldur Helm values:

```yaml
waldur:
  features:
    - openportal
  openportal:
    existingSecret:
      name: waldur-openportal-config
```

The `openportal` feature sets `WALDUR_OPENPORTAL["ENABLED"]`. The secret is
mounted at `/etc/waldur/openportal` in the API, worker and web-shell pods, and
`OPENPORTAL_CONFIG` is set to `/etc/waldur/openportal/config.toml`.

### Plugin settings

| Setting | Default | Meaning |
|---|---|---|
| `WALDUR_OPENPORTAL["ENABLED"]` | `False` | Enables the OpenPortal plugin |
| `WALDUR_OPENPORTAL["DEFAULT_LIMITS"]` | `{"NODE": 1000}` | Default node-hour limit for a newly provisioned allocation |

### Membership sync mode

When an incoming award lists someone as a member, Waldur can either invite them
or add them straight away. Which is right depends on the site's own onboarding
process, so it is a runtime setting, `OPENPORTAL_MEMBERSHIP_SYNC_MODE`, under
**Administration → Settings → Project**:

| Value | Behaviour |
|---|---|
| `invitation` (default) | Create a pending invitation. The user accepts, agrees to the terms and is provisioned locally before gaining access |
| `direct` | Create the account if needed and grant the role immediately |

Choose `invitation` where users must authenticate, accept an invitation and
agree to terms and privacy policies before local accounts are provisioned.
Choose `direct` where accounts are provisioned automatically and quickly, and a
second invitation at the receiving site would only confuse someone who has
already been invited by the awarding portal.

!!! warning
    The default is `invitation`. A site that relies on members being added
    directly must set this explicitly, otherwise members from incoming awards
    will sit as pending invitations instead of gaining access.

Either way the award converges immediately: a pending invitation is reported
back to the awarding portal as membership, so it stops resending the update
rather than waiting for the person to accept. Re-running the sync does not
create a second invitation.

### Creating an allocation offering

1. Navigate to **Service Provider** settings
2. Create a new offering with type **OpenPortal** (an instance reached through
   the agent network) or **OpenPortal Remote** (another portal)
3. Configure the offering options:

| Option | Meaning |
|---|---|
| `instance_name` | Full path name of the OpenPortal agent managing this instance, e.g. `portal.provider.platform.instance` |
| `project_template` | Class for projects created on the remote OpenPortal instance |
| `allocation_unit` | Unit for allocation limits (default `NHR`) |
| `default_allocation` | Default allocation for new projects on this resource |
| `max_allocation` | Maximum allocation for new projects on this resource |

Both offering types expose a single `NODE` component, measured in node-hours.

## Monitoring

### Scheduled tasks

Synchronisation runs as periodic Celery tasks. Most of them take a lock so
that only one copy runs at a time; the remote tasks (`sync_remote`,
`sync_remote_usage`, `sync_remote_users`) fan out to one subtask per
destination, and each subtask holds its own lock. `send_notifications`,
`sync_offering_agents`, `fix_total_allocation` and `clean_stale_jobs` are not
locked, so avoid triggering them by hand while a scheduled run is in progress.

| Task | Interval | Purpose |
|---|---|---|
| `waldur_openportal.sync_usage` | 7 min | Pull usage for local allocations |
| `waldur_openportal.sync_remote_usage` | 9 min | Pull usage for remote allocations |
| `waldur_openportal.sync_allocation_limits` | 17 min | Push resource limits for all allocations |
| `waldur_openportal.sync_local_users` | 19 min | Retry failed user additions and removals on instances |
| `waldur_openportal.sync_offering_agents` | 19 min | Synchronise offering agents |
| `waldur_openportal.sync_remote_users` | 23 min | Retry failed user additions and removals on remote portals |
| `waldur_openportal.sync_remote` | 29 min | Retry creating or updating remote projects, e.g. while awaiting approval |
| `waldur_openportal.send_notifications` | 47 min | Send project spending and end-date emails that are due |
| `waldur_openportal.mark_stale_remote_projects` | 1 h | Mark active awards with no contact for 12 hours as Stale |
| `waldur_openportal.refresh_remote_projects` | 6 h | Refresh every remote award, in case a notification was missed |
| `waldur_openportal.sync_storage` | 8 h | Take storage snapshots for local allocations |
| `waldur_openportal.sync_remote_storage` | 8 h | Fetch storage reports for remote allocations |
| `waldur_openportal.fix_total_allocation` | 23 h | Correct drift between project credit and the managed award |
| `waldur_openportal.clean_stale_jobs` | 25 h | Remove stale OpenPortal jobs from the database |

### Health

When Waldur checks an OpenPortal service, it asks the bridge agent for its
health. An unreachable or unhealthy bridge is logged as
`OpenPortal is not available`. Failed instructions appear in the worker log as
`Failed to run '<instruction>'` or `Job '<instruction>' timed out`, and the
next scheduled run retries them.

### Notification frequency

Project members receive periodic emails about the project's current spending
and end date. The interval is set per project, defaults to 14 days, and `0`
turns the emails off. The date of the last email is tracked per project, so
restarting workers does not send duplicates.

## Data flow for marketplace orders

1. **User creates order** → `CreateRemoteAllocationProcessor` → `create_allocation()` on bridge
2. **Limits change** → `UpdateRemoteAllocationLimitsProcessor` → `set_resource_limits()` on bridge
3. **User added** → Signal handler → `sync_users()` → `add_user()` on bridge
4. **Usage sync** → Periodic task → `get_usage_report()` from bridge → `ComponentUsage` update

## Version compatibility

Waldur requires OpenPortal 0.91.0 or later.

| OpenPortal Version | Waldur Module | Key Features |
|---|---|---|
| 0.91.x | Current | Award lifecycle tracking with audit history, allowed domains, approval embargo |
| 0.27.x | Superseded | AwardDetails with links, notes, membership control |
| 0.26.x | Superseded | Date range filtering on reports |
| 0.25.x | Superseded | Report remapping |

!!! tip
    Upgrade every agent in the chain together — bridge, portal, provider,
    clusters, cluster and the leaf agents. A chain running mixed versions is
    not a supported configuration, and the resulting failures usually surface
    as authentication or protocol errors far from the agent that is actually
    out of date.

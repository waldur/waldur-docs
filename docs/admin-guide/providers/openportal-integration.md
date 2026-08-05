# OpenPortal integration

## Overview

OpenPortal is a distributed agent-based infrastructure management protocol that enables Waldur to integrate with remote HPC centres and resource providers. The integration supports award/project management, user provisioning, resource allocation, and usage reporting across institutional boundaries.

!!! note
    OpenPortal is developed by the University of Bristol's Isambard Supercomputing Centre. Source code and documentation: [github.com/isambard-sc/openportal](https://github.com/isambard-sc/openportal)

## Architecture

```text
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  Waldur Portal   │────│  OpenPortal       │────│  Remote HPC      │
│  (Waldur)        │    │  Bridge Agent     │    │  Cluster Agent   │
│                  │    │                   │    │                  │
│  marketplace_    │    │  HTTP API         │    │  SLURM/PBS/etc   │
│  openportal_     │    │  Job queuing      │    │  Account mgmt    │
│  remote module   │    │  Signal URLs      │    │  Usage reporting │
└─────────────────┘     └──────────────────┘     └─────────────────┘
```

### Components

| Component | Location | Purpose |
|---|---|---|
| Waldur OpenPortal module | `waldur_openportal/` | Backend integration with OpenPortal protocol |
| Marketplace OpenPortal Remote | `marketplace_openportal_remote/` | Marketplace processors for order/resource lifecycle |
| OpenPortal Bridge | External service | HTTP bridge between Waldur and OpenPortal network |
| Cluster Agent | HPC centre | Manages local accounts, quotas, and usage |

## Capabilities

### Supported operations

| Operation | Direction | OpenPortal Instruction |
|---|---|---|
| **Create project/award** | Waldur → Remote | `create_project` / `create_award` |
| **Update project** | Waldur → Remote | `update_project` / `update_award` |
| **Delete project** | Waldur → Remote | `remove_project` |
| **Add user to project** | Waldur → Remote | `add_user` |
| **Remove user** | Waldur → Remote | `remove_user` |
| **Set resource limits** | Waldur → Remote | `set_limit` |
| **Get resource limits** | Remote → Waldur | `get_limit` |
| **Get usage reports** | Remote → Waldur | `get_usage_report` / `get_usage_reports` |
| **Get storage reports** | Remote → Waldur | `get_storage_report` / `get_storage_reports` |
| **Set project quota** | Waldur → Remote | `set_project_quota` |
| **Sync offerings** | Remote → Waldur | `sync_offerings` |

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

## Award lifecycle

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

A record moves to **Stale** automatically once nothing has been heard about it
for 12 hours. This is a warning that the local view may be wrong, not that
anything has failed — it usually points at a connectivity problem somewhere in
the agent chain rather than at the award itself.

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
| **Add note** | Appends a timestamped message that travels to the remote portal with the next update |
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

## Configuration

### Prerequisites

1. OpenPortal Bridge deployed and accessible via HTTP
2. Cluster agent(s) configured on remote HPC centres
3. Waldur `waldur_openportal` module enabled

### Helm configuration

Add the following to your Waldur Helm values:

```yaml
waldur:
  openportal:
    enabled: true
    bridge_url: "https://bridge.example.com"
    bridge_token: "your-bridge-api-token"
```

### Membership sync mode

When an incoming award lists someone as a member, Waldur can either invite them
or add them straight away. Which is right depends on the site's own onboarding
process, so it is a deployment setting,
`OPENPORTAL_MEMBERSHIP_SYNC_MODE`:

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

### Creating a remote allocation offering

1. Navigate to **Service Provider** settings
2. Create a new offering with type **OpenPortal Remote**
3. Configure:
    - Bridge URL and authentication
    - Remote project identifier mapping
    - Component definitions (CPU, GPU, RAM, storage)

## Monitoring

### Health checks

The integration includes a health check endpoint:

```bash
# Check bridge connectivity
curl -H "Authorization: Token YOUR_TOKEN" \
  https://waldur.example.com/api/openportal-remote-allocations/health/
```

### Usage synchronization

Usage data is pulled periodically via Celery tasks:

- `sync_usage`: Pulls latest usage reports from remote clusters
- `pull_allocation`: Full synchronization of single allocation
- `send_notifications`: Sends project expiration notifications

### Notification frequency

Per-project notification frequency is configurable to avoid notification fatigue:

- Notifications tracked per project with last-sent timestamps
- Configurable minimum interval between notifications

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

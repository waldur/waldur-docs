# OpenPortal integration

## Overview

OpenPortal is a distributed agent-based infrastructure management protocol that enables Waldur to integrate with remote HPC centres and resource providers. The integration supports award/project management, user provisioning, resource allocation, and usage reporting across institutional boundaries.

!!! note
    OpenPortal is developed by the University of Bristol's Isambard Supercomputing Centre. Source code and documentation: [github.com/isambard-sc/openportal](https://github.com/isambard-sc/openportal)

## Architecture

```
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

### Usage reporting

The integration supports pulling compute and storage usage:

- **Compute usage**: Daily per-user CPU/GPU/node usage
- **Storage usage**: Quota and consumption snapshots per volume
- **Date range filtering**: Query specific time periods
- **Report remapping**: Translate component names between systems

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

| OpenPortal Version | Waldur Module | Key Features |
|---|---|---|
| 0.27.x | Current | AwardDetails with links, notes, membership control |
| 0.26.x | Supported | Date range filtering on reports |
| 0.25.x | Supported | Report remapping |

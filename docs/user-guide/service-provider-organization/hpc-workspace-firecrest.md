# HPC workspace with FirecREST

The HPC workspace lets the members of a SLURM allocation work on the cluster
from Waldur: submit and cancel jobs, read their output, browse and preview
files, see the queue and partitions, find software, and review their job
history and job performance. Waldur does none of this itself. It calls
[FirecREST v2](https://eth-cscs.github.io/firecrest-v2/) **as the signed-in
user**, so every job runs, and every file is read, under that person's own
cluster account.

The workspace is **optional and configured per offering**. An offering without
FirecREST settings behaves exactly as before; nothing on this page is needed to
run a SLURM offering through the site agent.

## What users get

When an offering is connected, each of its allocations shows these extra tabs to
members of the allocation's project:

| Tab | What it does | Comes from |
|---|---|---|
| **Jobs** | Submit a batch job, follow its state, read stdout/stderr, cancel it | FirecREST |
| **Files** | Browse the user's home directory and preview files | FirecREST |
| **Insights** | Job counts, wait times, CPU/GPU hours and efficiency for up to 7 days | FirecREST job history |
| **Cluster** | Partitions the provider publishes, with live node and queue state, and planned maintenance | FirecREST + Waldur |
| **Software** | Modules from the [software catalogs](software-catalogs.md) linked to the offering, as lines to paste into a job | Waldur |

With a [cluster monitor](#job-performance-optional) configured, each finished job
also gets a **performance** view (GPU, CPU and memory over time) and a
downloadable PDF report.

Every job operation is scoped to the allocation's SLURM account
(`resource.backend_id`): a workspace never lists or touches the user's jobs
under other allocations.

## Before you start

The workspace adds a layer on top of an ordinary site-agent SLURM offering. It
needs:

- **A SLURM offering managed by the site agent** (offering type
  `Marketplace.Slurm`), with allocations that already exist on the cluster.
  An allocation without a backend ID, i.e. not yet created by the agent, shows
  "The allocation has not been created on the cluster yet."
- **FirecREST v2** in front of the cluster, reachable from the Waldur backend.
- **One identity provider for Waldur and FirecREST.** Users must sign in to
  Waldur through an OIDC identity provider (for example Keycloak) whose tokens
  FirecREST accepts. Waldur stores the user's access and refresh tokens at sign
  in and forwards the access token to FirecREST; users who signed in another way
  (local password, SAML) see "Sign in again to use HPC services".
- **The same username everywhere.** FirecREST takes the POSIX username from a
  token claim, and Waldur addresses the user's home directory and jobs by the
  user's offering username. Both must be the same account on the cluster.
  [POSIX identity with OpenLDAP and FirecREST](firecrest-posix-identity.md)
  describes a setup that guarantees this.

Configuration then happens in two places, by two different people.

## 1. Staff: allow the FirecREST endpoint

Waldur sends each user's identity provider token to the FirecREST URL that an
offering names. So that a service provider cannot point an offering at a server
of its own and collect those tokens, **only URLs that staff have allowed are
used**.

In **Administration → Marketplace → Settings → HPC workspace**, set:

| Setting | Value |
|---|---|
| `FIRECREST_ALLOWED_API_URLS` | FirecREST API URLs offerings may use, one per line or comma-separated, e.g. `https://firecrest.hpc.example.org` |
| `SLURM_MONITOR_ALLOWED_API_URLS` | Only if job performance is used: slurm-monitor API URLs ending in `/api/v2` |

An offering whose URL is not on the list simply has no workspace: its
allocations show no extra tabs, and the API answers "This offering is not
connected to an allowed FirecREST endpoint."

## 2. Service provider: connect the offering

In **Provider dashboard → Offerings →** *your offering* **→ Integration →
Advanced → HPC workspace (FirecREST)**, set:

| Field | Plugin option | Value |
|---|---|---|
| FirecREST API URL | `firecrest_api_url` | The FirecREST v2 URL, exactly as staff allowed it (a trailing `/` does not matter) |
| FirecREST system name | `firecrest_system_name` | The cluster's name in FirecREST's systems list (`GET /status/systems`) |

Both are required; with either one empty the offering has no workspace. To turn
the workspace off again, clear the URL.

The same settings over the API:

```bash
curl -X POST "$WALDUR/api/marketplace-provider-offerings/$OFFERING_UUID/update_integration/" \
  -H "Authorization: Token $TOKEN" -H "Content-Type: application/json" \
  -d '{"plugin_options": {
        "firecrest_api_url": "https://firecrest.hpc.example.org",
        "firecrest_system_name": "cluster-a"
      }}'
```

### Job performance (optional)

If the cluster runs [Sonar](https://github.com/NordicHPC/sonar) with
**slurm-monitor**, Waldur can show per-job time series (GPU utilisation and
memory, CPU, RSS, top processes) and put them into the job's PDF report. In the
same tab, under **Job performance**, set:

| Field | Plugin option | Value |
|---|---|---|
| slurm-monitor API URL | `slurm_monitor_api_url` | The slurm-monitor URL ending in `/api/v2`, allowed by staff in `SLURM_MONITOR_ALLOWED_API_URLS` |
| slurm-monitor cluster name | `slurm_monitor_cluster_name` | The cluster's name in slurm-monitor (Sonar's cluster name) |

Waldur reads it with the same user token, after checking with FirecREST that the
job belongs to the allocation. Without a monitor, the PDF report still contains
the job's accounting data.

### Related settings

These are independent of the workspace but show up in it when set:

- **Partitions** published on the offering are the ones the Cluster tab and the
  job form offer; FirecREST adds their live state.
- **Software catalogs** linked to the offering fill the Software tab and the
  job form's module picker — see [Software catalogs](software-catalogs.md).
- **Sync maintenance with SLURM reservations** (Integration → Operations →
  Resource lifecycle) makes planned maintenance hold back jobs on the cluster; the Cluster tab
  shows the upcoming maintenance and whether the cluster holds its reservation.

## Checking the result

1. Sign in as a member of an allocation's project, through the identity
   provider FirecREST trusts.
2. Open the allocation. The **Jobs**, **Files**, **Insights**, **Cluster** and
   **Software** tabs appear next to the usual ones.
3. The **Cluster** tab shows the system's health as FirecREST reports it.

If the tabs do not appear or show an error:

| Message | Cause |
|---|---|
| No HPC tabs at all | URL or system name empty, URL not on `FIRECREST_ALLOWED_API_URLS`, or the allocation is not in state OK, Updating or Erred |
| "This offering is not connected to an allowed FirecREST endpoint." | The offering's URL is not on the staff allowlist |
| "The allocation has not been created on the cluster yet." | The site agent has not created the SLURM account (no backend ID) |
| "You do not have an account on this cluster yet." | The user has no offering username on this offering yet; it is created once they are a member of the project |
| "Sign in again to use HPC services." | The user did not sign in through OIDC, or the refresh token has expired |
| "FirecREST does not serve the system '…'." | `firecrest_system_name` does not match a system in FirecREST |

## A runnable reference

The slurm-emulator repository contains a complete stack (Waldur, Keycloak,
FirecREST v2, an emulated SLURM cluster, Sonar and slurm-monitor) with an
offering configured as described here: see `examples/firecrest/waldur/` in
[slurm-emulator](https://github.com/waldur/slurm-emulator).

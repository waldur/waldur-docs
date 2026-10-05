# Service access modes

Waldur hands out services in two ways: users **order** offerings from the marketplace, or they **apply**
through calls for proposals, where a proposal is reviewed and, once accepted, turned into orders. How users
reach either is set by one deployment-wide setting, `SERVICE_ACCESS_MODE`. Three feature flags then decide
what each of those paths can do.

For what users see in each mode, see [How you reach services](../../user-guide/end-users/service-access-modes.md).

## The setting

`SERVICE_ACCESS_MODE` is a runtime setting under **Marketplace visibility & access**. In Helm deployments set
it in `waldur.settingsOverrides` — see [Configuration overrides](../deployment/helm/docs/configuration-overrides.md).

| Value | Marketplace in navigation | Calls section in navigation | Apply through an offering | Applicant wording |
|---|---|---|---|---|
| `both` (default) | Yes | Yes | Yes | Calls, rounds, proposals |
| `calls` | No | Yes | No | Calls, rounds, proposals |
| `marketplace` | Yes | Operators only | Yes | Access requests, submission deadlines |

- **Apply through an offering** — an offering that is open for proposals shows **Apply for access** next to
  **Order now**. In `calls` mode there is no offering page to apply from.
- In `marketplace` mode applicants never meet a call: their proposals are listed as access requests in their
  profile, and the proposal notifications are sent with the `access_request_*` templates instead — see
  [Notifications](notifications.md). Reviewers, call managers and service providers keep the call vocabulary
  and, if call management is on, a sidebar section to work from.

The setting changes navigation and wording only. The API serves the same data in every mode, and a proposal
submitted in one mode keeps working after the mode changes.

## Feature flags that combine with it

These are toggled under **Administration → User interface → Features**, and are independent of the mode.

| Flag | What it does |
|---|---|
| `marketplace.show_call_management_functionality` | Turns on call management: the call-managing organization's workspace, service providers' requests for offerings, and proposal reports. Without it those screens are hidden, whatever the mode. |
| `marketplace.call_only` | The calls are run **outside** Waldur. Each call requires an external URL, and **Apply** sends the user there. The rounds tab, the call managers' proposal and review lists, the reviewers tab and **My proposals** are hidden. A call without an external URL offers no way to apply. |
| `marketplace.catalogue_only` | Offerings can be browsed but not ordered; order lists and the pricing tab are hidden, and anonymous visitors land on the marketplace instead of the login page. See [Catalogue mode](../../user-guide/staff-users/catalogue_mode.md). |

### Typical setups

| Deployment | Mode | Call management | `call_only` | `catalogue_only` |
|---|---|---|---|---|
| Self-service cloud, no calls | `marketplace` | Off | Off | Off |
| Marketplace plus calls for proposals | `both` | On | Off | Off |
| Allocation portal, all access through calls | `calls` | On | Off | Off |
| Offerings granted only after review, without exposing calls | `marketplace` | On | Off | On |
| Directory of services and of calls run elsewhere | `calls` or `both` | On | On | On |

In the fourth row, ordering is disabled but the offering page still offers **Apply for access** when the
offering is open for proposals, so review is the only way in.

## Upgrading from the feature flags

Before `SERVICE_ACCESS_MODE` existed, the same choice was spread over feature flags. On upgrade a migration
derives the mode from what the deployment was showing:

| Before the upgrade | Mode after the upgrade |
|---|---|
| `call_only` on | `calls` |
| `call_only` off, call management on | `both` |
| Both off | `marketplace` |

The flags themselves are kept and keep the meaning described above. Check the derived value after
upgrading: a deployment that had neither flag on is now in `marketplace` mode, so any proposals its applicants
made are shown to them as access requests.

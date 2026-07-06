# Managing POSIX ID pools

Linux and HPC offerings provision local accounts and groups for their users —
for example through GLAuth (LDAP) and the Waldur site agent that feeds SLURM
clusters. Each such account needs a numeric POSIX **UID** (user id) and
**GID** (group id). A POSIX ID pool lets a service provider reserve the number
blocks Waldur allocates from, so that user and group identifiers stay unique
and predictable across all of the provider's offerings.

!!! note
    POSIX ID pools are how Waldur allocates UIDs and GIDs — an offering only
    hands out identifiers when a pool resolves for it. If you do not see the
    **POSIX ID pools** menu under your provider workspace, ask the platform
    operator to make it visible (the `marketplace.show_posix_id_pools` feature
    flag).

## How a pool works

A pool holds **two independent number ranges** — one for UIDs and one for GIDs —
each defined by a minimum and a maximum. UIDs and GIDs are separate namespaces,
so a UID and a GID may share the same number, but no two accounts ever share a
UID, and no two groups ever share a GID.

A pool must define **at least one** of the two ranges, but either may be left
empty to source that identifier **externally** instead of from the pool. The
common case is a federated deployment where each user's UID is a property of
their identity (delivered as an OIDC/SAML `uidNumber` claim and the same on every
site), while project and role **GIDs** are allocated per provider by Waldur: give
such an offering a **GID-only** pool (leave the UID range empty) and set its
UID source to the user attribute (see
[GLAuth user accounts → sourcing UID/GID](glauth-user-accounts.md#sourcing-uid-and-gid)).
Pairing a GID-only pool with externally-sourced UIDs guarantees a Waldur-allocated
UID can never collide with the identity provider's.

A pool is attached to one of two scopes:

| Scope | Use it when… |
|-------|--------------|
| **Service provider** (default) | One identifier space shared by all of your offerings. Most providers need only this. |
| **Offering** (override) | A single offering needs its own isolated number space — for example a separate cluster with its own LDAP directory. |

When Waldur needs an identifier for an offering, it uses the offering's own pool
if one is defined, otherwise the service-provider pool. If neither resolves, the
affected accounts are left without a UID/GID and are excluded from the GLAuth
output until a pool is configured.

## Creating a pool

1. Open your provider workspace, go to **Marketplace → POSIX ID pools** and
    click **Add**.

    ![POSIX ID pools list](../img/posix-pools-list.png)

2. Choose the **Scope**. Keep **Service provider (default)** for a provider-wide
    pool, or pick **Offering (override)** and select the offering for an
    isolated per-offering pool.

3. Enter the **Minimum** and **Maximum** for the **UID** and/or the **GID**
    range (all inclusive). Define at least one range; leave a range empty only
    when that identifier is sourced externally (see the note above). Each range
    is all-or-nothing — set both its bounds or neither. Optionally add a
    description, and click **Create**.

    ![Creating a POSIX ID pool](../img/posix-pool-create.png)

!!! warning "Pools of one provider may not overlap within a namespace"
    Across a provider's pools, UID ranges must not overlap each other and GID
    ranges must not overlap each other — one provider is treated as one POSIX
    identifier space per namespace. A UID range *may* share numbers with a GID
    range (the two namespaces are independent). If you try to save an
    overlapping pool, Waldur rejects it and names the conflicting pool, so an
    offering override must use a number band disjoint from the provider default
    (for example provider UIDs `100000–199999`, an isolated offering's UIDs
    `300000–399999`).

## Which pool applies to an offering

Resolution is simple: an offering uses its **own** pool if it has one, otherwise
the **service-provider** pool. To check, open the offering and go to **Edit →
Integration → User management** — the panel shows the pool in effect for that
offering, with a link to manage the provider's pools.

## Monitoring utilisation

The pools list shows the UID and GID utilisation of every pool at a glance.
Expand a pool row for the full per-namespace breakdown — capacity, the number of
identifiers in use, and the next value the allocator will hand out for each
namespace. A namespace that the pool does not manage (an empty range) is shown
as **Not managed by this pool — sourced externally** rather than a utilisation
bar.

![POSIX ID pool utilisation](../img/posix-pool-utilization.png)

The utilisation bar turns amber as a namespace fills and red once it crosses the
threshold (90% by default), so you can widen the range before it runs out. An
exhausted namespace stops account creation with a clear error until more numbers
are available.

## How identifiers are assigned

Identifiers are handed out sequentially from the resolved pool as offering
users, robot accounts and groups are created — a high-water mark advances per
namespace. The assigned values are stored on each account, so you can review the
**UID** and **GID** in the provider's **Offering users** list.

![Offering users with UID and GID columns](../img/posix-offering-users-uid-gid.png)

When an offering user or group is deleted, its identifiers are **released** and
recycled automatically: the next account created from the same pool reuses the
lowest released value before the high-water mark advances further. Released
records are kept as an audit trail and are visible in a pool's **identities**
view.

## Pinning specific UIDs/GIDs

Sometimes an account must keep a **specific** UID or GID — for example to match
an identity that already exists on the backend. Set it from **Edit POSIX
attributes** on the offering user (see
[Per-user overrides](glauth-user-accounts.md#per-user-overrides)). The value
must fall **within the offering's pool** and must not already be in use; the
allocator then skips it when handing out sequential numbers, so a pinned value
never collides with an automatically assigned one.

!!! note
    Valid POSIX ids run from `1000` (below is reserved for system accounts) to
    `4294967294`. If an offering needs a number band entirely separate from the
    provider default — for instance a block reserved for manually pinned
    identities — give that offering its own **offering-override pool** rather
    than pinning outside the provider pool's range.

# Permissions

A permission in Waldur is a **role granted to a user over a scope**. Roles are named
`SCOPE.ROLE` — `CUSTOMER.OWNER`, `PROJECT.ADMIN`, `OFFERING.MANAGER` — and every grant,
whatever its scope, is exposed through a single endpoint: `/api/user-permissions/`.

!!! warning
    Earlier versions of Waldur exposed one endpoint per scope, `/api/customer-permissions/`
    and `/api/project-permissions/`, and returned `customer_permissions` / `project_permissions`
    fields on `/api/users/`. **All of these have been removed.** The endpoints return 404, and
    requesting the old fields on `/api/users/` still returns 200 with those fields silently
    absent — so a client written against the old shape fails quietly rather than loudly.
    Use `/api/user-permissions/` instead.

## Listing permissions

```bash
GET /api/user-permissions/
Accept: application/json
Authorization: Token <API_TOKEN>
```

Each entry describes one grant: who holds it, which role, over which scope, and whether it is
still active.

| Field | Description |
|-------|-------------|
| `uuid` | Identifier of the grant itself |
| `user_uuid`, `user_username`, `user_name`, `user_email`, `user_slug` | The user holding the role |
| `role_name`, `role_description`, `role_uuid` | The role granted, e.g. `CUSTOMER.OWNER` |
| `scope_type` | `customer`, `project`, `offering`, `call`, `proposal`, … |
| `scope_uuid`, `scope_name` | The object the role applies to |
| `scope_is_removed` | Whether the scope has since been soft-deleted |
| `created`, `expiration_time` | When the role was granted, and when it lapses (`null` = no expiry) |
| `is_active` | `false` once revoked or expired |
| `revoked_by_username`, `revoked_by_full_name`, `revoke_reason` | Populated when the grant was revoked |
| `project_uuid`, `resource_uuid` | Set for project- and resource-scoped grants |

## Filtering

| Filter | Matching |
|--------|----------|
| `?username=<username>` | Exact |
| `?user=<UUID>`, `?user_url=<URL>` | Exact |
| `?full_name=<name>`, `?native_name=<name>`, `?user_slug=<slug>` | Case-insensitive partial |
| `?scope_type=<type>` | Exact — `customer`, `project`, `offering`, `call`, `proposal` |
| `?scope_uuid=<UUID>`, `?scope_name=<name>` | Exact / case-insensitive partial |
| `?role_name=<name>`, `?role_uuid=<UUID>` | Case-insensitive partial / exact |
| `?customer_uuid=<UUID>` | Every grant within an organization — the organization scope **and** its projects |
| `?is_active=true` | Excludes revoked and expired grants |

Ordering uses `?o=<field>`, prefixed with `-` for descending. Supported fields are
`username`, `full_name`, `native_name`, `email`, `expiration_time`, `created` and `role`.

## Fetching a user's permissions

To find everything a given user may do, filter by their username. The same call works with an
eduTEAMS or MyAccessID CUID, since the CUID is stored as the username for federated accounts.

```bash
> http -v GET https://waldur.example.com/api/user-permissions/ username==bsc-operator \
    Authorization:"Token 154f2c6984b5992928b62f87950ac529f1f906ca"

GET /api/user-permissions/?username=bsc-operator HTTP/1.1
Accept: */*
Authorization: Token 154f2c6984b5992928b62f87950ac529f1f906ca
Host: waldur.example.com

HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
X-Result-Count: 1

[
    {
        "uuid": "83000000000000000000000000000001",
        "user_uuid": "00000000000000000000000000000010",
        "user_name": "BSC Operator",
        "user_slug": "bsc-operat",
        "user_username": "bsc-operator",
        "user_email": "operator@bsc.demo",
        "created": "2026-08-19T16:22:56.700721+00:00",
        "expiration_time": null,
        "is_active": true,
        "revoked_by_full_name": null,
        "revoked_by_username": null,
        "revoke_reason": "",
        "role_name": "CUSTOMER.OWNER",
        "role_description": "Organization owner",
        "role_uuid": "961e7d86898d4faf9154f12288acfcc5",
        "scope_type": "customer",
        "scope_uuid": "a3000000000000000000000000000001",
        "scope_name": "Barcelona Supercomputing Center",
        "scope_is_removed": false,
        "resource_uuid": null,
        "project_uuid": null
    }
]
```

The total number of matches is returned in the `X-Result-Count` header, and `Link` carries the
pagination cursors.

## Listing the available roles

`/api/roles/` enumerates the roles a deployment defines, together with the scope each applies to
and the permissions it carries. Staff can add custom roles alongside the system ones — see
[user role management](../../user-guide/staff-users/user_role_management.md).

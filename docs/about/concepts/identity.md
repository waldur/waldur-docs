# Identity

## Overview

Waldur ships its own [user](platform.md) directory but is almost always fronted by an external identity provider (IdP) — SAML2 federation, an OIDC provider like Keycloak, an LDAP service, or a national auth service. SCIM provisioning lets the IdP push users and groups into Waldur, and outbound entitlement sync lets Waldur push group membership to downstream systems. Pick the topology that matches your federation; the [platform](platform.md) role model is the same regardless.

## Topology

```d2
direction: down
classes: {
  ext:    { style: { fill: "#e8f5e8"; stroke: "#2e7d32" } }
  waldur: { style: { fill: "#dae8fc"; stroke: "#6c8ebf" } }
  down:   { style: { fill: "#fff8e1"; stroke: "#f57f17" } }
}

idp: Identity provider\n(SAML / OIDC / LDAP) { class: ext }
scim_in: SCIM source\n(IdP-side) { class: ext }

waldur_auth: Waldur auth { class: waldur }
waldur_users: Waldur user directory { class: waldur }
waldur_groups: Roles & memberships { class: waldur }

scim_out: SCIM consumer\n(downstream system) { class: down }
freeipa: FreeIPA / LDAP\n(allocation backend) { class: down }

idp -> waldur_auth: SSO login
scim_in -> waldur_users: provision users & groups
waldur_auth -> waldur_users: just-in-time create
waldur_users -> waldur_groups: assigned roles
waldur_groups -> scim_out: push entitlements
waldur_groups -> freeipa: account / project sync
```

## Key concepts

| Concept | One-liner | Reference |
|---|---|---|
| Identity provider | The external system a user authenticates against (SAML2, OIDC, LDAP). | [Admin guide](../../admin-guide/identities/summary.md) |
| Just-in-time provisioning | Waldur creates a user record on first successful login. | — |
| SCIM (inbound) | The IdP pushes user / group changes into Waldur. | [Admin guide](../../admin-guide/mastermind-configuration/scim-identity-provider.md) |
| SCIM (outbound) | Waldur pushes role / group entitlements to downstream systems. | [Admin guide](../../admin-guide/mastermind-configuration/scim-integration.md) |
| Offering user | A backend-specific account Waldur creates on the provider side (e.g. a FreeIPA user for SLURM). | [Admin guide](../../admin-guide/offering-users.md) |
| Role mapping | Translation of IdP groups / claims into Waldur roles. | [Roles](../terminology/roles_and_permissions.md) |

## Supported providers

| Provider | Protocol | Typical use |
|---|---|---|
| eduGAIN | SAML2 | Research-and-education federation. |
| eduTEAMS | OIDC | Group management for research collaborations. |
| Keycloak | OIDC / SAML2 | Open-source IdP; common standalone choice. |
| TARA | OIDC | Estonian state authentication. |
| MyAccessID | OIDC | European HPC federation gateway. |
| LDAP / LDAPS | LDAP | Existing enterprise directories. |
| FreeIPA | REST | Identity sync to a FreeIPA-backed allocation system. |
| Valimo, social | OIDC / proprietary | National mobile-ID and social logins. |

Per-provider setup lives in [admin-guide / identities](../../admin-guide/identities/summary.md).

## Choosing the right combination

- **Single corporate IdP**: front Waldur with Keycloak or your SAML IdP; let JIT handle user creation.
- **Federated research access**: front with eduGAIN or MyAccessID; consider SCIM inbound if the federation supports it.
- **Sync to allocation backends**: enable outbound SCIM (for SaaS targets) or FreeIPA sync (for SLURM/HPC clusters).
- **Hybrid**: combine inbound SCIM (authoritative user list) with SAML SSO (authoritative login) and outbound entitlement sync.

## Related concepts

- [Platform](platform.md) — what a Waldur user looks like once authenticated.
- [Roles and permissions](../terminology/roles_and_permissions.md) — what role mapping resolves to.

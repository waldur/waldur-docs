# Organization-scoped roles

## Overview

In addition to the deployment-wide [roles](../../about/terminology/roles_and_permissions.md),
staff can give a single organization its own roles:

- **Clone** a system role into an organization. The copy keeps the original's
  permissions but can only be used within that organization and its projects.
- **Conceal** a system role within an organization so it can no longer be
  granted there — usually so a cloned, organization-specific role replaces it.

Standard roles are unaffected in every organization where they are not concealed.

## Accessing organization roles

1. Open the organization (**Organizations** → select one).
2. Go to **Manage** (the organization edit page) and select the **Roles** tab,
   next to **Access control**.

!!! note
    The **Roles** tab and all actions on this page are visible to staff users
    only.

The page lists the roles that can be managed for this organization — the
organization- and project-scoped system roles plus the organization's own
clones. Roles for other scopes (offering, service provider, call) are not shown
here: they cannot be concealed or cloned into an organization and are managed in
the global role administration instead. *Organization role* and *System role*
badges distinguish clones from system roles.

Use the **Filters** to narrow the list by **Scope**, by **Type** (system or
organization role), or to enable **Show concealed roles** so the roles concealed
for this organization are listed too. The search box matches role names and
descriptions, and the columns sort by name, scope, and origin. Expanding a role
row shows the users currently assigned that role.

## Cloning a role into an organization

1. Click **Clone role**.
2. Select a **Template role** — a system organization or project role to copy.
3. Leave **Conceal the original role in this organization** checked (default) so
   the clone replaces the system role in this organization's pickers, or uncheck
   it to keep both.
4. Click **Clone**.

The new role appears marked *Organization role*, with its origin shown as
*Cloned from …*. Selecting a template in the dialog shows the permissions that
will be copied. To adjust a clone's permissions afterwards, use **Edit** on its
row (this reuses the same editor as the global
[User roles](user_role_management.md) screen).

!!! tip
    Keeping the conceal option checked avoids two identically named entries
    (for example two "Project member" options) appearing in the role pickers.

!!! note
    A cloned role's internal name includes the organization slug (for example
    `CUSTOMER.acme.OWNER`). If you later change the organization's slug, its
    custom roles are renamed automatically to match — the slug field warns you
    when the organization has custom roles.

## Concealing and revealing roles

- To hide a system role in this organization, use **Conceal** on its row. It can
  no longer be granted here (existing assignments are kept) and is marked with a
  *Concealed* badge.
- To restore it, enable **Show concealed roles** in the filters, then use
  **Reveal** on the concealed role's row.

!!! warning
    A role cannot be concealed if it is the last one able to grant access at its
    scope (for example the last owner-capable role), so an organization cannot be
    left ungovernable.

## Deleting an organization role

Use **Delete** on an organization role's row to remove it. A role that is still
assigned to users cannot be deleted — remove those assignments first.

## What members see

Members of the organization see its available roles wherever roles are chosen
(team management, invitations). A concealed system role is no longer offered
there; its organization clone appears in its place. Members of other
organizations never see this organization's private roles.

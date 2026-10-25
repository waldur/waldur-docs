# User role management

## Overview

Staff users can manage user roles through the platform's role management interface. This includes configuring existing roles, creating new ones, and adjusting role permissions to ensure appropriate access levels across different organizational contexts.

## Accessing role management

Open **Administration → Configuration → User roles**.

![User role management](../img/user_role_management.png)

## Managing existing roles

### Viewing roles

The roles interface displays all existing roles with their associated types and descriptions.

### Role actions

For each role, administrators can:

1. **Edit role**
    - Modify role name
    - Change role type
    - Adjust permissions

2. **Edit description**
    - Update role description
    - Add clarifying information

3. **Disable role**
    - Temporarily deactivate role
    - Prevent new assignments

## Creating new roles

1. Click **Add**
2. Complete the required fields:
    - **Name** - Descriptive title for the role
    - **Type** - Select role context
    - **Permissions** - Configure permissions

### Available role types

- Organization
- Project
- Offering
- Call
- Proposal
- Service provider organization
- Call managing organization
- Site-wide

### Site-wide roles

A site-wide role's permissions apply on every object, without making the holder staff or support:
an order desk with **List order** and **Approve order**, for example, sees and approves every
order in every organization.

- Choose **Site-wide** as the type. The three organization team permissions under
  **Team members** (create, update and delete permission customer) are greyed out: held on every
  organization, they would let the holder make themselves owner of any of them.
- Grant the role from the user's page: **Support → Users → user → Roles and permissions → Add**,
  scope type **Site-wide**. There is no scope to pick. The grant is listed with scope
  **Entire site** and is revoked from the same row.

Only staff create and grant site-wide roles. A deployment can also define them with
`scope: global` in `custom-roles.yaml`. What each permission opens is described in
[site-wide roles](../../developer-guide/guides/waldur-permissions.md#site-wide-roles).

## Permission configuration

Permissions in Waldur are extensively categorized to provide granular access control across different functional areas. Each permission category contains multiple specific actions that can be enabled or disabled.

### Offering permissions

- Controls the complete lifecycle of offerings
- Includes creation, modification, and deletion capabilities
- Manages offering components like endpoints, screenshots, and plans
- Controls offering states (pause/unpause/archive)
- Manages offering-specific user groups and campaigns
- Configures offering attributes, location, and description

### Order permissions

- Manages the order workflow process
- Controls order visibility and listing
- Handles order approval processes (both public and private)
- Manages order cancellation and rejection
- Controls order destruction capabilities

### Provider actions

- Manages service provider operations
- Controls resource management and reporting
- Handles API and robot account management
- Provides access to service provider statistics and revenue
- Manages provider-customer relationships
- Controls backend integration settings

### Customer actions for resources

- Controls resource visibility and management
- Handles resource lifecycle operations
- Manages booking requests and plan switching
- Controls resource limitations and options
- Manages importable resources

### Team member permissions

- Controls invitation management
- Manages permission assignments across projects, customers, and offerings
- Handles creation, updating, and deletion of various permission types
- Controls access level modifications

### Project permissions

- Manages project lifecycle
- Controls project creation and modification
- Handles project listing and deletion
- Sets project-level access controls

### Call management

- Controls call and round management
- Handles proposal workflows
- Manages permission assignments for calls
- Controls proposal approval processes
- Manages round closures

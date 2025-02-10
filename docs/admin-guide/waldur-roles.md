# Waldur roles and permissions

## Overview

Waldur provides a flexible Role-Based Access Control (RBAC) system, enabling administrators to manage user permissions efficiently. Roles define the actions users can perform within the system, ensuring structured and secure access to resources.

This guide outlines Waldur's roles, their associated permissions, and how they govern access within the platform.

## Managing roles in Waldur

Roles in Waldur are structured to define user access within specific scopes. The key attributes of a role include:

- **Name** – A unique identifier for the role
- **Scope** – The context in which the role is applicable (e.g., Organization, Project, Call, etc.)
- **Description** – A brief explanation of the role's purpose and responsibilities
- **Active** – Indicates whether the role is currently available for assignment

Users can be assigned one or more roles within an Organization, Project, Call, Offering, Service Provider, Proposal, or Call Managing Organization scope.

## Default roles and permissions

Waldur provides predefined roles to streamline access management across different scopes. Below is an overview of available roles, grouped by scope.

### Organization roles

**Scope**: Organization

| Name | Description | Active |
|------|-------------|--------|
| Customer owner | The highest-level role in an organization, granting full administrative control | Yes |
| Customer manager | A managerial role for service providers within an organization | Yes |
| Customer support | Provides limited support access within an organization | No |

### Project roles

**Scope**: Project

| Name | Description | Active |
|------|-------------|--------|
| Project administrator | Grants full control over a project, including resource and order management | Yes |
| Project manager | Similar to the administrator role but includes additional permission management capabilities | Yes |
| Project member | A limited role with basic project access | No |

### Offering Roles

**Scope**: Offering

| Name | Description | Active |
|------|-------------|--------|
| Offering manager | Manages an offering's configuration and associated resources | Yes |

### Call managing organization roles

**Scope**: Call managing organization

| Name | Description | Active |
|------|-------------|--------|
| Customer call organizer | An organization-specific role for handling calls | Yes |

### Call roles

**Scope**: Call

| Name | Description | Active |
|------|-------------|--------|
| Call manager  | Oversees calls and proposal approvals | Yes |
| Call reviewer  | A role dedicated to reviewing submitted proposals | Yes |


### Proposal roles

**Scope**: Proposal

| Name | Description | Active |
|------|-------------|--------|
| Proposal manager | Responsible for managing proposals within a call | Yes |

### Service provider roles

**Scope**: Service provider

| Name | Description | Active |
|------|-------------|--------|
| Service provider manager  | Manages service provider-specific settings and operations | Yes |

## Role assignment and management

Roles are assigned to users based on their responsibilities and required access levels. Administrators can:

- Add or remove user roles
- Modify permissions associated with roles
- Revoke roles manually or set expiration times for temporary access

## Managing roles via the interface

The Waldur administration interface offers an intuitive way to manage user roles. Staff users can:

1. Navigate to the Administration panel
2. Select the User roles section under Settings menu
3. Modify existing roles by updating permissions or changing their status
4. Disable roles as needed

Using the administration interface simplifies role management and ensures a structured approach to access control.

⚠️ **Important notes**:

- Roles should follow the principle of least privilege
- Some roles are disabled by default (e.g., CUSTOMER.SUPPORT)
- Regular audits of role assignments are recommended
- Certain roles are scope-restricted (e.g., CUSTOMER.CALL_ORGANIZER)
- Changes to role permissions should be carefully considered
- Document any custom role configurations

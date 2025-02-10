# Waldur roles and permissions

## Overview

Waldur provides a flexible Role-Based Access Control (RBAC) system, enabling administrators to manage user permissions efficiently. Roles define the actions users can perform within the system, ensuring structured and secure access to resources.

This guide outlines Waldur's roles, their associated permissions, and how they govern access within the platform.

## Managing Roles in Waldur

Roles in Waldur are structured to define user access within specific scopes. The key attributes of a role include:

- **Name** – A unique identifier for the role
- **System Role** – Specifies whether the role is a predefined system role
- **Active Status** – Indicates if the role is currently available for assignment
- **Permissions** – A set of actions granted to the role

Users can be assigned one or more roles within an organization, project, or service provider scope.

## Default Roles and Permissions

Waldur provides predefined roles to streamline access management across different scopes. Below is an overview of available roles and their permissions.

### Organization Roles

| Role | Description | Key Permissions |
|------|-------------|----------------|
| Customer Owner (CUSTOMER.OWNER) | The highest-level role in an organization, granting full administrative control | Manage offerings, projects, resources, orders, customers, invitations, access subnets, and service provider settings |
| Customer Manager (CUSTOMER.MANAGER) | A managerial role for service providers within an organization | Manage offerings, service provider API secrets, statistics, and robot accounts |

### Project Roles

| Role | Description | Key Permissions |
|------|-------------|----------------|
| Project Administrator (PROJECT.ADMIN) | Grants full control over a project, including resource and order management | Manage orders, resources, invitations, and projects |
| Project Manager (PROJECT.MANAGER) | Similar to the administrator role but includes additional permission management capabilities | All project administrator permissions plus project permission management |
| Project Member (PROJECT.MEMBER) | A limited role with basic project access | List resources and projects |

### Offering Roles

| Role | Description | Key Permissions |
|------|-------------|----------------|
| Offering Manager (OFFERING.MANAGER) | Manages an offering's configuration and associated resources | Update offerings, manage offering state, set resource usage, and accept/reject booking requests |

### Call Management Roles

| Role | Description | Key Permissions |
|------|-------------|----------------|
| Call Reviewer (CALL.REVIEWER) | A role dedicated to reviewing submitted proposals | List proposals |
| Call Manager (CALL.MANAGER) | Oversees calls and proposal approvals | Approve/reject proposals, close rounds, manage call permissions, and list rounds/proposals |
| Customer Call Organizer (CUSTOMER.CALL_ORGANIZER) | An organization-specific role for handling calls | Same as Call Manager |

### Customer Support Role

| Role | Description | Key Permissions |
|------|-------------|----------------|
| Customer Support (CUSTOMER.SUPPORT) | Provides limited support access within an organization | (Inactive by default) |

## Role Assignment and Management

Roles are assigned to users based on their responsibilities and required access levels. Administrators can:

- Add or remove user roles
- Modify permissions associated with roles
- Revoke roles manually or set expiration times for temporary access

## Managing Roles via the interface

The Waldur administration interface offers an intuitive way to manage user roles. Staff users can:

1. Navigate to the Administration
2. Select the User Roles section
3. Modify existing roles by updating permissions or changing their status
4. Disable roles as needed

Using the administration interface simplifies role management and ensures a structured approach to access control.


Waldur's RBAC system provides granular access control to ensure secure and efficient role management. By leveraging predefined roles or customizing them based on specific needs, organizations can ensure users have appropriate access aligned with their responsibilities.


⚠️ **Important Notes**:

- Roles should follow the principle of least privilege
- Some roles are disabled by default (e.g., CUSTOMER.SUPPORT)
- Regular audit of role assignments is recommended
- Certain roles are scope-restricted (e.g., CUSTOMER.CALL_ORGANIZER)
- Changes to role permissions should be carefully considered
- Document any custom role configurations
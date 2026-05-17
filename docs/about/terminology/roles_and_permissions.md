# Roles and permissions

## Users, Organizations and Projects

Waldur is a service for sharing resources across projects. It is based
on the delegation model where an organization can allocate certain users to
perform technical or non-technical actions in the projects.

The most common types of Waldur installations include:

- **Cloud** - used in commercial or government sectors for providing access to cloud resources like virtual machines, storage and Kubernetes clusters.
- **Academic** - used in research and education. Waldur is deployed for a single university, high school or research infrastructure.
- **Academic Shared** - the same purpose as Academic, but is shared among several universities or infrastructures.

### User

An account in Waldur belonging to a person or a robot. A user can have roles in Organizations and Projects.
Some users - mostly affiliated with Waldur operator - can have global roles, e.g. support or staff.

### Organization

=== "Cloud"

    A company or a department. Organization can be a customer, a service provider or both.

=== "Academic"

    A faculty, department or an institute. Organization can be also a service provider, for example, an HPC center.

=== "Academic Shared"

    In Academic Shared model, all organizations are service providers allocating resources to their users (research groups or classes) through their Projects.

### Project

A project within an Organization. Used for organizing and isolating Resources and Users.

### Service Provider

Organization that provides services to other organizations.

### User types

| | User | Support agent | Staff |
| ---- | :----: | :----: | :----: |
| Web and API access | :material-check: | :material-check: | :material-check: |
| Can create support requests | :material-check:  | :material-check:  | :material-check:  |
| Can provide user support | | :material-check: | :material-check: |
| Can see all projects and resources | | :material-check: | :material-check: |
| Can manage organizations | | | :material-check: |
| Can access admin area | | | :material-check: |

### User roles in Organization

=== "Cloud"

    | | Owner | Service Manager | Project Manager | System Administrator |
    | --- | :----: | :----: | :----: | :----: |
    | Manage Team | :material-check: | | :material-check: (pre-approved users) | |
    | Manage Projects | :material-check: | | | |
    | Request and Manage Resources | :material-check: | | :material-check: | :material-check: |
    | Approves creation of Resource Requests (Orders) | :material-check: | | :material-check: (configurable) | :material-check: |
    | Approves Resource Requests (Orders) | :material-check: | :material-check: | | |
    | Manage Offerings (Service provider-specific) | :material-check: | :material-check: | | |

=== "Academic"

    | | PI | Service Manager | co-PI | Member |
    | --- | :----: | :----: | :----: | :----: |
    | Manage Team | :material-check:  | | :material-check: (pre-approved users) |
    | Manage Projects | :material-check: | | |
    | Request and Manage Resources | :material-check: | | :material-check: | :material-check: |
    | Approves creation of Resource Requests (Orders) | :material-check: | | :material-check: (configurable) | :material-check: |
    | Approves Resource Requests (Orders) | :material-check: | :material-check: | | |
    | Manage Offerings (Service provider-specific) | :material-check: | :material-check: | |

=== "Academic Shared"

    | | Resource allocator | Service Manager | PI | co-PI | Member |
    | --- | :----: | :----: | :----: | :----: | :----: |
    | Manage Team | :material-check:  | | :material-check: (pre-approved users) | | |
    | Manage Projects | :material-check: | | | | |
    | Request and Manage Resources | :material-check: | | :material-check: | :material-check: | |
    | Approves creation of Resource Requests (Orders) | :material-check: | | :material-check: (configurable) | :material-check: |
    | Approves Resource Requests (Orders) | :material-check: | :material-check: | | |
    | Manage Offerings (Service provider-specific) | :material-check: | :material-check: | | | |

### User roles in Call management

| Role name              | Scope           | Description |
|----------------------------|----------------------|-------------------------------------------------|
| **Organization owner**         | Customer            | Has full administrative access to manage organizations, offerings, orders, resources, projects, and call-related permissions. |
| **Call organiser** | Call organizer      | Manages calls at the organization level, similar to Call manager but restricted to a specific customer scope. |
| **Call manager**           | Call                | Oversees the entire call process, including managing proposals, approving/rejecting applications, closing rounds, and handling permissions. |
| **Call reviewer**          | Call                | Reviews and evaluates submitted proposals within a call. |
| **Proposal member**       | Proposal            | Manages individual proposals, controlling their status and related workflows. |

## Default roles by scope (reference)

The role names above are friendly labels for the per-installation matrices.
Internally, Waldur ships a fixed set of roles grouped by the scope they apply to.
Operators see these names in the administration interface and API payloads.

| Scope | Role | Description | Active by default |
|---|---|---|:---:|
| Organization | Customer owner | Highest-level role in an organization; full administrative control. | Yes |
| Organization | Customer manager | Managerial role for service providers within an organization. | Yes |
| Organization | Customer support | Limited support access within an organization. | No |
| Project | Project administrator | Full control over a project, including resource and order management. | Yes |
| Project | Project manager | Adds permission-management capabilities on top of administrator. | Yes |
| Project | Project member | Limited project access. | No |
| Offering | Offering manager | Manages an offering's configuration and associated resources. | Yes |
| Service provider | Service provider manager | Manages service-provider-specific settings and operations. | Yes |
| Call managing organization | Customer call organizer | Organization-specific role for handling calls. | Yes |
| Call | Call manager | Oversees calls and proposal approvals. | Yes |
| Call | Call reviewer | Reviews submitted proposals. | Yes |
| Proposal | Proposal manager | Manages proposals within a call. | Yes |

Every role exposes the same attributes:

- **Name** — unique identifier.
- **Scope** — context in which the role is applicable (Organization, Project, Call, Offering, Service Provider, Proposal, Call managing organization).
- **Description** — brief explanation of the role's purpose.
- **Active** — whether the role is currently available for assignment.

A user can hold one or more roles within any of those scopes simultaneously.

### Managing roles in the administration interface

Staff users can review and modify the defaults from the Waldur administration UI:

1. Open the Administration panel.
2. Select **User roles** under the Settings menu.
3. Edit a role to change its permissions or active status, or disable it entirely.

!!! warning
    Apply the principle of least privilege; some roles are intentionally inactive
    by default (e.g. **Customer support**). Audit role assignments regularly,
    and document any custom role configurations.

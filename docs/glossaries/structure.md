# Users, Organizations and Projects

Waldur is a service for sharing resources across projects. It is based
on the delegation model where an organization can allocate certain users to
perform technical or non-technical actions in the projects.

The most common types of Waldur installations include:

- **Cloud** - used in commercial or government sectors for providing access to cloud resources like virtual machines, storage and Kubernetes clusters.
- **Academic** - used in research and education. Waldur is deployed for a single university, high school or research infrastructure.
- **Academic Shared** - the same purpose as Academic, but is shared among several universities or infrastructures.

## Glossary

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
    | Approve/Reject Resource Orders | :material-check: | | :material-check: (configurable) | :material-check: |
    | Manage Offerings (Service provider-specific) | :material-check: | :material-check: | | |

=== "Academic"

    | | PI | Service Manager | co-PI | Member |
    | --- | :----: | :----: | :----: | :----: |
    | Manage Team | :material-check:  | | :material-check: (pre-approved users) |
    | Manage Projects | :material-check: | | |
    | Request and Manage Resources | :material-check: | | :material-check: | :material-check: |
    | Approve/Reject Resource Orders | :material-check: | | :material-check: (configurable) | :material-check: (configurable) |
    | Manage Offerings (Service provider-specific) | :material-check: | :material-check: | |

=== "Academic Shared"

    | | Resource allocator | Service Manager | PI | co-PI | Member |
    | --- | :----: | :----: | :----: | :----: | :----: |
    | Manage Team | :material-check:  | | :material-check: (pre-approved users) | | |
    | Manage Projects | :material-check: | | | | |
    | Request and Manage Resources | :material-check: | | :material-check: | :material-check: | |
    | Approve/Reject Resource Orders | :material-check: | | :material-check: (configurable) | :material-check: | |
    | Manage Offerings (Service provider-specific) | :material-check: | :material-check: | | | |

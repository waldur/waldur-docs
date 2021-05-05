# Roadmap
 
## Disclaimer
This document is a living document and is used for planning. Plans for the unreleased features can change without
further notice and hence cannot be used as a guaranteed delivery plan, the features can be delivered both
earlier and later.

Roadmap is created based on the backlog and requests from the existing users of Waldur. If you are interested in a
specific topic, please [reach out](./support.md) to us.

Some of the tasks are common and some are functional, listed below.

## Continuous improvements

### Documentation

There is no such thing as a perfect documentation so we are constantly working on improving it.

### CI/CD

We believe that automation is a key to improving quality of code and happiness of developers, so we are
constantly working on improving CI/CD related aspects.

### Tests

A good software is a reliable software, so we are always trying to add more sensible tests.

## Functional

The list below is based on the Epics maintained in Waldur's task manager. They are labelled with  domains, which
have requested them. Domains are:

- **Generic** - Common requirements, no extra label. 
- **Academia** - originating from the research community;
- **Commercial** - originating from the commercial deployments;
- **Government** - originating from the public sector deployments.

### Open or  in progress

| **Code** | **Description** | **Domain** |
| -------- | -------- | --------------- |
| WAL-4000 | Allow to limit visibility of Offering by service provider | Academia Commercial |
| WAL-3999 | Support for customer credits  | Academia Commercial Government|
| WAL-3997 | Add common limit management support to HomePort | Academia Commercial |
| WAL-3987 | Extensions to SLURM module | Academia  |
| WAL-3964 | Implement consolidated approach for remote user accounts management in marketplace offerings | Academia  |
| WAL-3963 | Make order confirmation message a common functionality for all Marketplace | Academia Government |
| WAL-3951 | Implement more fine grained storage of user name |   |
| WAL-3943 | Shared Openstack Tenant provider phase I | Academia  |
| WAL-3934 | Functionality specific to deployment of Waldur in Puhuri project as Core | Academia  |
| WAL-3811 | Improvements to feedback collection | Government  |
| WAL-3805 | Direct LDAP support for Linux identity | Academia  |
| WAL-3793 | Tasks related to simplification of the invoice model | Government  |
| WAL-3788 | Add ability to see popularity of an offering from the list |   |
| WAL-3759 | Add support of versioning for core objects | Government  |
| WAL-3744 | Add support for creating / managing projects and resources through API of external Waldur | Academia  |
| WAL-3736 | Allow protecting resources from accidental deletion | Government  |
| WAL-3689 | Expose list of connected VMs for each security group | Government  |
| WAL-3626 | Add ability to generate API docs for select endpoints | Academia  |
| WAL-3625 | Migrate from Issue types to Request types for Jira support backend | Government  |
| WAL-3606 | Introduce Organization level service manager role | Government  |
| WAL-3596 | Allow logins to Rancher via keycloak | Academia Government |
| WAL-3595 | Expose port management for OpenStack tenant | Government  |
| WAL-3589 | Expose Sankey diagram with costs and Service providers | Academia  |
| WAL-3585 | Rancher access group management | Academia Government |
| WAL-3582 | Allow editing of invoice data for staff users | Government  |
| WAL-3563 | Tasks related for getting Puhuri Core to work | Academia  |
| WAL-3524 | Add support for sending notifications to users | Commercial  |
| WAL-3439 | Add support for bookmarking offerings as favourites | Academia  |
| WAL-3400 | Tasks related to gitlab dev pipelines |   |
| WAL-3339 | Offerings (Reporting) |   |
| WAL-3334 | Introduce vault for storing secret configuration in Waldur |   |
| WAL-3305 | Chart for creating overview of existing organizations |   |
| WAL-3285 | "Some of the services suggest purchasing of connected offerings | To Do  |
| WAL-3272 | Allow setting limit for the maximal size of the total volume type quota | Academia  |
| WAL-3218 | Payment profiles (Phase III) |   |
| WAL-3205 | UX stabilization (phase I) |   |
| WAL-3195 | Improvements to the request-based item UX |   |
| WAL-3136 | Marketplace Checklists (phase II) | Commercial  |
| WAL-3135 | Support for auto-scalability of Waldur running on K8S |   |
| WAL-3103 | Second phase of support for virtual routers in OpenStack. | Academia Government |
| WAL-3076 | Extend current model with ability to attach VMs directly to external networks | Academia Commercial |
| WAL-3072 | Support for operations on multiple objects | Commercial  |
| WAL-3005 | Followup tasks for payment profiles | Government  |
| WAL-2991 | Markeplace Scripts plugin phase I | Academia Commercial |
| WAL-2965 | Enhancements to properly support virtual security gateway use-case | Government  |
| WAL-2961 | Tasks related to Kubernetes ON service development and operation | Government  |
| WAL-2922 | Tasks for exposing Offerings publicly | Academia  |
| WAL-2921 | Extending Organization extended payment options | Government  |
| WAL-2920 | Tasks related for extending Waldur with ability to assess compliancy of organizations |   |
| WAL-2850 | Extending Rancher to support Helm charts | Government  |
| WAL-2843 | Tasks related to building up monitoring for EOSC | Academia  |
| WAL-2780 | Integration of PID services with Waldur models | Academia  |
| WAL-2776 | A visual checklist for making sure that things are done for the project | Government  |
| WAL-2749 | Tasks connected to improving security of Waldur  |   |
| WAL-2748 | Collection of tasks aimed at improving UX of Waldur |   |
| WAL-2747 | Operational tools for Waldur deployments |   |
| WAL-2676 | System for lightweight offering management |   |
| WAL-2637 | Support for creating Rancher clusters | Academia  |
| WAL-2623 | Introduce license support for OpenStack | Commercial  |
| WAL-2519 | Improvements to VMware plugin | Commercial  |
| WAL-2401 | Implement device booking feature | Academia  |
| WAL-2134 | Further developments of Marketplace |   |
| WAL-1442 | Enhancements to Waldur for service provider visibility | Commercial  |
| WAL-1309 | Implement backend and frontend support for managing JIRA as a provider and issues as resources |   |
| WAL-1262 | Efforts for getting Waldur into Redhat container store |   |
| WAL-1212 | Reanimate Zabbix plugin |   |
| WAL-1056 | IPv6 support for OpenStack provider | Academia Commercial Government|
| WAL-868 | Refactor cost tracking |   |
| WAL-842 | On-demand demo environment from waldur.com |   |
| WAL-791 | Stress testing & Profiling (vol 1) |   |
| WAL-500 | Waldur-specifics for ISKE H audit | Government  |
| WAL-198 | Resource retention management | Academia Commercial Government|
| WAL-44 | Navigation FTS |   |
| WAL-30 | Quick alerts |   |


### Finished or discarded

| **Code** | **Description** | **Domain** |
| -------- | -------- | --------------- |
| WAL-3998 | Add i18n support |   |
| WAL-3976 | Allow setting end of life for project |   |
| WAL-3850 | Convert OrderItems and Invoices PDF to on-the-fly generation |   |
| WAL-3833 | Add an intro header to the personal dashboard |   |
| WAL-3804 | Slurm user list |   |
| WAL-3710 | Add support for tracking historical changes to important models |   |
| WAL-3592 | Expose measured units in invoice details |   |
| WAL-3587 | Render component usage as charts in homeport |   |
| WAL-3579 | Support for description for Secgroup Rules |   |
| WAL-3551 | Extensions to request-based item offerings to support Puhuri cases |   |
| WAL-3523 | Add regular reminders for reviewing membership data of users |   |
| WAL-3520 | Add a minimal privilege project member role |   |
| WAL-3497 | Trello integration for feature requests |   |
| WAL-3466 | Support editing of organizations in homeport |   |
| WAL-3407 | Extension of checklists to personalized ones |   |
| WAL-3306 | Growth chart shows changes over time of usage | Academia  |
| WAL-3297 | Financial overview improvements |   |
| WAL-3294 | Actions for setting up Waldur at VU |   |
| WAL-3197 | ITA PKI extension improvements |   |
| WAL-3096 | Add support for OpenStack Router  | Academia Government |
| WAL-3022 | Redesign of slurm module |   |
| WAL-2989 | Reports visible to support |   |
| WAL-2967 | Basic feature to track quality of handling of a ticket |   |
| WAL-2666 | Extending OpenStack integration with separate pricing for different volume types |   |
| WAL-2646 | Tickets related to extension of OpenStack driver |   |
| WAL-2596 | Drop OpenStack packages |   |
| WAL-2590 | Tasks related to VMware that are need additional analysis  |   |
| WAL-2491 | VMware plugin |   |
| WAL-2025 | Tasks related to extension of MasterMind API for BDG SSP |   |
| WAL-1988 | Marketplace (3) |   |
| WAL-1808 | Waldur Marketplace (Phase 2) |   |
| WAL-1640 | Extension of ansible SDK with additional operations |   |
| WAL-1568 | Migrate tables to React |   |
| WAL-1523 | Waldur Marketplace (Phase I) |   |
| WAL-1504 | Implement basic support for Dutch government cloud in Waldur |   |
| WAL-1402 | Add support for MOAB provider |   |
| WAL-1289 | Add support for Jira attachments |   |
| WAL-1288 | Support view of users |   |
| WAL-1286 | Add support for LDAP-based authentication backends |   |
| WAL-1255 | Add support for Staff only VPC management |   |
| WAL-1113 | Paypal support |   |
| WAL-1095 | Basic Azure VM provider |   |
| WAL-1060 | Waldur goes to K8S |   |
| WAL-1058 | Resource import |   |
| WAL-969 | Expert provider extension |   |
| WAL-962 | Add organization self-registration |   |
| WAL-925 | Add eduGain support for authentication  |   |
| WAL-903 | Improvements to invoice / accounting |   |
| WAL-839 | Miration to ES 5.x |   |
| WAL-834 | Migrate to Django 1.11 |   |
| WAL-833 | Create a PoC for Expert provider |   |
| WAL-832 | Ansible module for Waldur |   |
| WAL-793 | 2nd phase of Grafana dashboards |   |
| WAL-790 | Add ability to set cost limit on organization |   |
| WAL-751 | Support for Ansible-playbooks as application providers |   |
| WAL-730 | Waldur Mission Control (central management for Waldurs) |   |
| WAL-722 | LDAP-based SSH access provider |   |
| WAL-713 | Add TaaT authentication provider to Waldur |   |
| WAL-701 | Notifications |   |
| WAL-686 | Add support for smartid.ee IdP |   |
| WAL-604 | Basic support mode |   |
| WAL-597 | /admin improvements |   |
| WAL-596 | HomePort localization |   |
| WAL-595 | API Documentation |   |
| WAL-568 | Grafana dashbord (for operators) |   |
| WAL-566 | Predictive analysis for capacity planning (organization-view) |   |
| WAL-511 | Fixes for a broken network model |   |
| WAL-479 | Price estimation |   |
| WAL-468 | Admin and user guides (initial) |   |
| WAL-463 | Extended backup restoration |   |
| WAL-462 | Extend snapshot management |   |
| WAL-461 | Basic resource usage view |   |
| WAL-454 | R: Update django to 1.9. |   |
| WAL-396 | OpenStack providers pricing info |   |
| WAL-323 | Use neutron for network operations. |   |
| WAL-297 | Project policies |   |
| WAL-289 | Optimizer for IaaS resource selection |   |
| WAL-287 | Renaming of artifacts to Waldur |   |
| WAL-270 | OpenStack Tenant dashboard access |   |
| WAL-262 | OpenStack Tenant Network Management |   |
| WAL-259 | OpenStack Instance Access Management |   |
| WAL-213 | Basic policy support |   |
| WAL-199 | Provider details |   |
| WAL-197 | Customer support |   |
| WAL-169 | API Token management |   |
| WAL-168 | Extended membership management capabilities |   |
| WAL-106 | Refactoring: Update DRF version. |   |
| WAL-88 | Transactional event logs |   |
| WAL-82 | Controls for user profile updates |   |
| WAL-79 | Tenant Management |   |
| WAL-77 | Request-based Offerings |   |
| WAL-76 | Billing |   |
| WAL-75 | Audit log |   |
| WAL-68 | Waldur ServiceStore |   |
| WAL-43 | Waldur white-labelling |   |
| WAL-42 | Resource state display |   |
| WAL-41 | Registration |   |
| WAL-17 | Waldur HomePort L&F |   |
| WAL-15 | Waldur web page |   |
| WAL-9 | OpenStack VM backup management |   |
| WAL-8 | OpenStack Storage management |   |
| WAL-7 | OpenStack Instance management |   |
| WAL-6 | Waldur HomePort navigation |   |
| WAL-4 | VPC / OpenStack Tenant purchase |  |
| WAL-3 | Organization team management |   |
| WAL-2 | I want to be able to manage my SSH keys |   |

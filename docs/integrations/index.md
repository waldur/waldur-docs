# Integrations

Waldur connects with a wide range of resource providers, identity services, and management tools to create a comprehensive orchestration platform. These integrations are continually expanded based on user requirements and can be customized for specific deployments.

## Resource Provider Integrations

### Compute and Cloud Services

* **OpenStack** - Complete integration with OpenStack's core services (Keystone, Nova, Cinder, Glance, and Neutron) enabling management of projects, networks, subnets, floating IPs, instances, and more.

* **MS Azure** - Support for creating, importing, and managing Virtual Machines on Microsoft Azure public cloud.

* **VMware** - Integration with VMware virtualization platform for managing virtual infrastructure resources.

### HPC and Scientific Computing

* **SLURM and MOAB** - Integration with popular HPC workload managers and job scheduling systems through Waldur Site Agent, providing web-based self-service for accounts and allocation management. Site Agent supports both SLURM and MOAB workload managers, allowing efficient management of HPC resources.

* **Open OnDemand** - Web-based portal for accessing HPC resources, integrated with Waldur through KeyCloak and SLURM plugins for unified account and permission management, enabling researchers to access computational resources through a user-friendly interface.

* **LEXIS Integration** - Support for LEXIS (Large-scale EXecution for Industry & Society) platform integration, allowing Waldur resources to be linked with LEXIS workflows for enhanced HPC and data management capabilities.

## Identity Provider Integrations

Waldur supports multiple authentication methods to meet diverse organizational needs:

* **EduGAIN** - Full integration as an EduGAIN Service Provider with support for CoCo extensions, enabling secure federated academic identity management.

* **LDAP/Active Directory** - Connect to existing directory services such as FreeIPA, OpenLDAP, or Active Directory with flexible schema configuration.

* **MyAccessID** - Integration with GEANT's MyAccessID service, including support for Puhuri-specific APIs for enhanced functionality.

* **Keycloak** - Comprehensive support for Keycloak identity servers with advanced features:
  * Group synchronization capability, maintaining alignment between Keycloak groups and Waldur's internal structure
  * Custom Keycloak mappers for Waldur OfferingUser usernames and group access
  * MinIO integration for policy-based access control

* **SAML2** - Support for generic SAML-based identity federations with automated account creation and updates based on SAML attributes.

* **Waldur DB** - Built-in user management with customizable profile fields to adapt to specific deployment requirements.

* **GLAuth** - Lightweight LDAP server integration for simple user directory management with automated config refreshing.

## Service Desk Integrations

Waldur integrates with several service desk solutions to enable end-to-end support ticket management:

* **Atlassian ServiceDesk** - Integration with both on-premises and cloud versions
* **Zammad** - Open-source help desk/customer support system integration
* **Microfocus SMAX** - Enterprise service management integration

These integrations allow users to create support requests directly from Waldur, view ticket history and status, and interact with support personnel without leaving the Waldur interface.

## AI and Automation Integrations

* **Claude Desktop Integration** - Waldur MCP (Model Context Protocol) server enables Claude AI assistant to query Waldur instances for reporting and deep analysis of resources and usage data, enhancing decision-making capabilities.

## Additional Integrations

* **Monitoring & Analytics** - Support for Prometheus and Grafana for metrics collection and visualization.
* **Backup Solutions** - Database backup capabilities with support for S3-compatible storage services.

---

New integrations are continuously being developed based on user requirements. For custom integration needs, please contact the Waldur development team.
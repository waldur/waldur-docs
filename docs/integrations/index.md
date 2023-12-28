# Integrations

Waldur supports integration with various private and public cloud services for delivering of additional functionality.
The list of currently supported integrations is below. New services are integrated following business demand and can be
delivered specifically for your deployment.

* OpenStack - OpenStack is a popular open-source platform for building private and public clouds. Waldur provides full integration with OpenStack clouds, in particular with Keystone, Nova, Cinder, Glance and Neutron services. Waldur can provision and manage OpenStack Projects, networks, subnets, floating IPs, instances and much more.
* MS Azure - Microsoft Azure is a well known public cloud provider. Waldur supports creation, import and management of Virtual Machines on Azure.
* SLURM - SLURM is a popular HPC workload manager and job scheduling system. Waldur supports integration with SLURM to enable web-based self-service for creating and managing accounts and allocations. [More information](https://docs.waldur.com/integrations/waldur-slurm-service/)
* Open OnDemand - Open OnDemand provides a remote web access to supercomputers. Waldur supports integration with Open OnDemand by integrating KeyCloak and SLURM plugins for seamless account and permission management. [More information](https://docs.waldur.com/integrations/open-ondemand/)
* VMware - VMware provides virtualization, networking, and security management tools.

In addition to previously mentioned integration towards resource providers, Waldur also supports several identity providers like:

* EduGAIN - Support for federated academical identity provider EduGAIN. Waldur supports full integration as a EduGAIN Service Provider including CoCo extensions for higher security guarantees. [More information](https://docs.waldur.com/admin-guide/identities/eduGAIN/)
* LDAP - Support for taking identities from an external LDAP-server, e.g. FreeIPA, OpenLDAP or AD. Simple configuration for LDAP schema allows to connect your existing profiles with Waldur. [More information](https://docs.waldur.com/admin-guide/identities/LDAP/)
* MyAccessID - Support for integrating with GEANT's MyAccessID service. Full integration along with support for additional Puhuri-specific APIs.
* Keycloak - Support for integrating with Keycloak identity servers. Waldur is also able to maintain a list of groups in Keycloak that match Waldur's internal structure. [More information](https://docs.waldur.com/admin-guide/identities/keycloak/)
* SAML2 - Support for federated identity providers over SAML-based protocols. Automated account creation and update based on information from SAML-attributes.
* Waldur DB - Support for user profiles managed within local Waldur database. Does not require any additional configuration or setup. Fields of the profile can be tuned to match specifics of deployment (e.g. exposing additional names in national languages).
# OpenStack (Tenant)

## Requirements for OpenStack (Tenant)

OpenStack versions tested:

- Queens
- Rocky
- Stein
- Train
- Ussuri
- Victoria
- Wallaby
- Xena
- Yoga
- Zed
- Antelope

In order to integrate an OpenStack-based cloud as a shared provider, the following data is required:

- URL of Keystone's public endpoint (v3).
- Access to public interfaces of Keystone, Nova, Cinder, Neutron and Glance should be opened to Waldur MasterMind server.
- Admin credentials (username/password) as well as domain name (in case non-default domain is used).
- External network UUID - the network will be by default connected to all created OpenStack Projects (Tenants).

## Advanced settings

It's possible to override some settings for OpenStack in MasterMind admin interface.
To do that, please go to Waldur MasterMind Admin interface with a staff account.

Go to Structure → Shared provider settings and select the one you want to update.

Define specific customisation options. To add an option select append on item block under the object tree. Most typical are:

- external_network_id – external network to connect to when creating a VPC from this provider.
- access_url - a URL to access OpenStack Horizon dashboard from a public network. Typically a reverse proxy URL in production deployments.
- flavor_exclude_regex - flavors matching this regex expression will not be pulled from the backend.
- dns_nameservers - default value for new subnets DNS name servers. Should be defined as list.
- create_ha_routers - create highly available Neutron routers when creating Tenants.

## Support for Organization specific OpenStack networks

You can provide specific external network for all OpenStack Tenants created by Organiztion by providing external
network UUIDs in Organization configuration in Waldur Mastermind admin portal.

[![Organization specific OS networks](img/org-specific-os-network.png)](img/org-specific-os-network.png)

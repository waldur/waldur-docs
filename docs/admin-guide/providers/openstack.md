# OpenStack

Waldur integrates with OpenStack-based clouds through a single OpenStack plugin. It
provisions and manages OpenStack projects (tenants) together with the compute, network and
storage resources inside them, and exposes them for self-service ordering through the Waldur
marketplace.

## Requirements

OpenStack releases known to work:

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

Newer releases are generally compatible, as Waldur talks to OpenStack through the standard
service clients (Keystone v3, Nova, Cinder, Neutron and Glance).

To integrate an OpenStack-based cloud as a shared provider, the following data is required:

- URL of Keystone's public endpoint (v3).
- Network access from the Waldur server to the public interfaces of Keystone, Nova, Cinder,
  Neutron and Glance.
- Admin credentials (username/password) and the domain name (if a non-default domain is used).
- External network UUID — the network connected by default to the OpenStack projects (tenants)
  that Waldur creates.

## Marketplace offerings

OpenStack is exposed to end users through three marketplace offering types:

- **OpenStack.Tenant** — provisions an OpenStack project (tenant) with quotas for cores, RAM and
  storage, an internal network, a subnet and a router, and connects it to the external network.
- **OpenStack.Instance** — provisions a virtual machine inside a tenant.
- **OpenStack.Volume** — provisions a block-storage volume inside a tenant.

### Tenant provisioning options

When ordering a tenant, the following options are available:

- `subnet_cidr` — CIDR of the default private subnet.
- `availability_zone` — default availability zone for the tenant.
- `security_groups` — security groups to create in the tenant.
- `skip_connection_extnet` — do not connect the tenant to the external network.
- `skip_creation_of_default_router` — do not create the default router.
- `skip_creation_of_default_subnet` — do not create the default subnet.

### Offering options

Per-offering settings control how tenants behave:

- `storage_mode` — `fixed` for a single storage quota, or `dynamic` for per-volume-type quotas.
- `max_instances`, `max_volumes`, `max_security_groups` — upper bounds enforced within a tenant.
- `default_internal_network_mtu` — MTU applied to networks created in the tenant (68–9000).

## Supported resources

The plugin discovers and manages the full set of OpenStack resources:

- **Compute** — instances, flavors and server groups (affinity / anti-affinity, including soft
  variants). Instances support cloud-init user data, config drive, SSH key injection, multiple
  network ports and boot-from-volume.
- **Networking** — networks, subnets, ports, routers, floating IPs and security groups (ingress
  and egress rules, TCP/UDP/ICMP, IPv4 and IPv6). Cross-tenant network sharing is supported via
  RBAC policies (`access_as_shared` and `access_as_external`).
- **Storage** — volumes and volume types, with resize, retype and boot-from-image. Snapshots
  and full instance backups are supported, each with a retention period after which they are
  cleaned up automatically.
- **Images and availability zones** — images and per-resource availability zones for instances
  and volumes.

Quotas are enforced and kept in sync at the service, tenant and project levels, and resource
state is reconciled with the backend on a periodic schedule.

## Billing

Tenant offerings are billed on quota limits using monthly components:

- **Cores** — vCPU limit.
- **RAM** — memory limit, in GB.
- **Storage** — total storage limit, in GB.

In `dynamic` storage mode, a separate storage component is created for each OpenStack volume
type (for example `storage_ssd`), so that each volume type can be billed independently.

## Organization-specific external networks

A specific external network can be assigned to all OpenStack tenants created by a given
organization on a given provider. When a tenant is created, Waldur resolves the external
network to connect to in the following order:

1. The external network set on the tenant itself.
2. The external network configured for the organization on that provider.
3. The provider's default external network.

The tenant's default router is then connected to the resolved external network, and the
tenant's external network reference is recorded for floating IP allocation.

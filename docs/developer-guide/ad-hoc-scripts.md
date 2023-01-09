# Ad-hoc scripts

This section describes different ad-hoc scripts used by Waldur developers.

## Usage-related scripts

### Restore CPU/GPU/RAM usages for a month

Sometimes, Waldur can have issues with data correctness. They can be caused by different circumstansies, e.g. problems with data syncronization between Waldur backend and service provider software. In order to resolve these issues, a user can restore usage data with [restore_usages.py](scripts/update_usages.py) script.

### Generate openmetrics file with usages for several months

If a user needs to create openmetrics file with usages, e.g. for [historical data backfilling in Prometheus](https://medium.com/tlvince/prometheus-backfilling-a92573eb712c), the [generate_openmetrics_usages.py](scripts/generate_openmetrics_usages.py) can be used.

### Prolong expired projects

If a user needs to prolong an expired project with remote resources, [this script](scripts/prolong_remote_projects.py) should be used. It can:

1. automatically detect projects with pending update requests
2. approve the requests
3. set state OK for terminating resources both in a local Waldur and remote one

**Note:** the script must be executed in a local Waldur instance

### Wipe tenants and all related resources from OpenStack

If a user needs to remove a tenant with all related objects (instances, volumes, backups, etc.) manually, [this script](scripts/wipe-tenants.py) should be used. It removes all the tenants with names from `tenant_names` list using an OpenStack administrator project. Please, replace `<main-tenant-uuid>` (line 13) with the corresponding UUID of the admin tenant in Waldur.

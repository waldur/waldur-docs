## cleanup_stale_event_types

Cleanup stale event types in all hooks.

## clearquotashistory

Delete quotas versions duplicates.

## copy_category

Copy structure of categories for the Marketplace

```
usage: waldur copy_category source_category_uuid target_category_uuid

positional arguments:
  source_category_uuid  UUID of a category to copy metadata from
  target_category_uuid  UUID of a category to copy metadata to
```

## createstaffuser

Create a user with a specified username and password. User will be created as staff.

```
usage: waldur createstaffuser -u USERNAME -p PASSWORD -e EMAIL

optional arguments:
  -u USERNAME, --username USERNAME
  -p PASSWORD, --password PASSWORD
  -e EMAIL, --email EMAIL
```

## drfdocs

Generate RST docs for DRF API

```
usage: waldur drfdocs [--store PATH] [app_label [app_label ...]]

positional arguments:
  app_label             Application label.

optional arguments:
  --store PATH, -s PATH
                        Where to store docs.
```

## drop_leftover_openstack_projects

Drop leftover projects from remote OpenStack deployment.
  Leftovers are resources marked as terminated in Waldur but still present in the remote OpenStack.
  Such inconsistency may be caused by split brain problem in the distributed database.

```
usage: waldur drop_leftover_openstack_projects [--offering OFFERING]
                                               [--dry-run] [--fuzzy-matching]

optional arguments:
  --offering OFFERING  Target marketplace offering name where leftover
                       projects are located.
  --dry-run            Don't make any changes, instead show what projects
                       would be deleted.
  --fuzzy-matching     Try to detect leftovers by name.
```

## dumpusers

Dumps information about users, their organizations and projects.

```
usage: waldur dumpusers [-o OUTPUT]

optional arguments:
  -o OUTPUT, --output OUTPUT
                        Specifies file to which the output is written. The
                        output will be printed to stdout by default.
```

## export_ami_catalog

Export catalog of Amazon images.

## export_offering

Export an offering from Waldur. Export data includes JSON file with an offering data and a thumbnail. Names of this files include offering ID.

```
usage: waldur export_offering -o OFFERING -p PATH

optional arguments:
  -o OFFERING, --offering OFFERING
                        An offering UUID.
  -p PATH, --path PATH  Path to the folder where the export data will be
                        saved.
```

## import_ami_catalog

Import catalog of Amazon images.

```
usage: waldur import_ami_catalog [-y] FILE

positional arguments:
  FILE       AMI catalog file.

optional arguments:
  -y, --yes  The answer to any question which would be asked will be yes.
```

## import_azure_image

Import Azure image

```
usage: waldur import_azure_image [--sku SKU] [--publisher PUBLISHER]
                                 [--offer OFFER]

optional arguments:
  --sku SKU
  --publisher PUBLISHER
  --offer OFFER
```

## import_marketplace_orders

Create marketplace order for each resource if it does not yet exist.

## import_offering

Import or update an offering in Waldur. You must define offering for updating or category and customer for creating.

```
usage: waldur import_offering -p PATH [-c CUSTOMER] [-ct CATEGORY]
                              [-o OFFERING]

optional arguments:
  -p PATH, --path PATH  File path to offering data.
  -c CUSTOMER, --customer CUSTOMER
                        Customer UUID.
  -ct CATEGORY, --category CATEGORY
                        Category UUID.
  -o OFFERING, --offering OFFERING
                        Updated offering UUID.
```

## import_tenant_quotas

Import OpenStack tenant quotas to marketplace.

```
usage: waldur import_tenant_quotas [--dry-run]

optional arguments:
  --dry-run  Don't make any changes, instead show what objects would be
             created.
```

## init_marketplace_support

Import existing support offerings as marketplace resources.

```
usage: waldur init_marketplace_support --category CATEGORY_UUID --customer
                                       CUSTOMER_UUID

optional arguments:
  --category CATEGORY_UUID
                        Specify a category to create offerings.
  --customer CUSTOMER_UUID
                        Specify a customer to create offerings.
```

## initglobalquotashistory

Recalculate all quotas

## initsecuritygroups

Add default security groups with given names to all tenants.

```
usage: waldur initsecuritygroups names [names ...]

positional arguments:
  names
```

## load_categories

Loads a categories for the Marketplace

```
usage: waldur load_categories category [category ...]

positional arguments:
  category  List of categories to load
```

## move_project

Move Waldur project to a different organization.

```
usage: waldur move_project -p PROJECT_UUID -c CUSTOMER_UUID

optional arguments:
  -p PROJECT_UUID, --project PROJECT_UUID
                        UUID of a project to move.
  -c CUSTOMER_UUID, --customer CUSTOMER_UUID
                        Target organization UUID
```

## move_resource

Move a marketplace resource to a different project.

```
usage: waldur move_resource -p PROJECT_UUID -r RESOURCE_UUID

optional arguments:
  -p PROJECT_UUID, --project PROJECT_UUID
                        Target project UUID
  -r RESOURCE_UUID, --resource RESOURCE_UUID
                        UUID of a marketplace resource to move.
```

## pgmigrate

Load data with disabled signals.

```
usage: waldur pgmigrate [--path PATH]

optional arguments:
  --path PATH, -p PATH  Path to dumped database.
```

## pull_openstack_volume_metadata

Pull OpenStack volumes metadata to marketplace.

```
usage: waldur pull_openstack_volume_metadata [--dry-run]

optional arguments:
  --dry-run  Don't make any changes, instead show what objects would be
             created.
```

## pull_support_priorities

Pull priorities from support backend.

## pull_support_users

Pull users from support backend.

## push_tenant_quotas

Push OpenStack tenant quotas from marketplace to backend.

```
usage: waldur push_tenant_quotas [--dry-run]

optional arguments:
  --dry-run  Don't make any changes, instead show what objects would be
             created.
```

## rebuild_billing

Create or update price estimates based on invoices.

## recalculatequotas

Recalculate all quotas

## removestalect

Remove instances that have FK to stale content types.

## status

Check status of Waldur MasterMind configured services

```
usage: waldur status [--check-api-endpoints-at BASE_URL]

optional arguments:
  --check-api-endpoints-at BASE_URL
                        Runs API endpoints check at specified base URL (i.e.
                        http://example.com). If this argument is not provided,
                        check will be skipped.
```

## switching_backend_server

Backend data update if a server was switched.

## sync_saml2_providers

Synchronize SAML2 identity providers.

## sync_users

Sync users from Waldur to Rancher.


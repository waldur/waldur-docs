# CLI guide

## axes_list_attempts

List access attempts

## axes_reset

Reset all access attempts and lockouts

## axes_reset_failure_logs

Reset access failure log records older than given days.

```bash
usage: waldur axes_reset_failure_logs [--age AGE]

optional arguments:
  --age AGE  Maximum age for records to keep in days
```

## axes_reset_ip

Reset all access attempts and lockouts for given IP addresses

```bash
usage: waldur axes_reset_ip ip [ip ...]

positional arguments:
  ip
```

## axes_reset_logs

Reset access log records older than given days.

```bash
usage: waldur axes_reset_logs [--age AGE]

optional arguments:
  --age AGE  Maximum age for records to keep in days
```

## axes_reset_username

Reset all access attempts and lockouts for given usernames

```bash
usage: waldur axes_reset_username username [username ...]

positional arguments:
  username
```

## clean_settings_cache

Clean API configuration settings cache.

## cleanup_stale_event_types

Cleanup stale event types in all hooks.

## copy_category

Copy structure of categories for the Marketplace

```bash
usage: waldur copy_category source_category_uuid target_category_uuid

positional arguments:
  source_category_uuid  UUID of a category to copy metadata from
  target_category_uuid  UUID of a category to copy metadata to
```

## createstaffuser

Create a user with a specified username and password. User will be created as staff.

```bash
usage: waldur createstaffuser -u USERNAME -p PASSWORD -e EMAIL

optional arguments:
  -u USERNAME, --username USERNAME
  -p PASSWORD, --password PASSWORD
  -e EMAIL, --email EMAIL
```

## drfdocs

Generate RST docs for DRF API

```bash
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

```bash
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

```bash
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

```bash
usage: waldur export_offering -o OFFERING -p PATH

optional arguments:
  -o OFFERING, --offering OFFERING
                        An offering UUID.
  -p PATH, --path PATH  Path to the folder where the export data will be
                        saved.
```

## import_ami_catalog

Import catalog of Amazon images.

```bash
usage: waldur import_ami_catalog [-y] FILE

positional arguments:
  FILE       AMI catalog file.

optional arguments:
  -y, --yes  The answer to any question which would be asked will be yes.
```

## import_azure_image

Import Azure image

```bash
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

```bash
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

```bash
usage: waldur import_tenant_quotas [--dry-run]

optional arguments:
  --dry-run  Don't make any changes, instead show what objects would be
             created.
```

## init_marketplace_support

Import existing support offerings as marketplace resources.

```bash
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

```bash
usage: waldur initsecuritygroups names [names ...]

positional arguments:
  names
```

## load_categories

Loads a categories for the Marketplace

```bash
usage: waldur load_categories category [category ...]

positional arguments:
  category  List of categories to load
```

## load_features

Import features in JSON format

```bash
usage: waldur load_features [--dry-run] features_file

positional arguments:
  features_file  Specifies location of features file.

optional arguments:
  --dry-run      Don't make any changes, instead show what objects would be
                 created.
```

## load_notifications

Import notifications to DB

```bash
usage: waldur load_notifications notifications_file

positional arguments:
  notifications_file  Specifies location of notifications file.
```

## load_user_agreements

Imports privacy policy and terms of service into DB

```bash
usage: waldur load_user_agreements [-tos TOS] [-pp PP] [-f FORCE]

optional arguments:
  -tos TOS, --tos TOS   Path to a Terms of service file
  -pp PP, --pp PP       Path to a Privacy policy file
  -f FORCE, --force FORCE
                        This flag means force loading agreements even if they
                        are already defined in DB.
```

## move_project

Move Waldur project to a different organization.

```bash
usage: waldur move_project -p PROJECT_UUID -c CUSTOMER_UUID

optional arguments:
  -p PROJECT_UUID, --project PROJECT_UUID
                        UUID of a project to move.
  -c CUSTOMER_UUID, --customer CUSTOMER_UUID
                        Target organization UUID
```

## move_resource

Move a marketplace resource to a different project.

```bash
usage: waldur move_resource -p PROJECT_UUID -r RESOURCE_UUID

optional arguments:
  -p PROJECT_UUID, --project PROJECT_UUID
                        Target project UUID
  -r RESOURCE_UUID, --resource RESOURCE_UUID
                        UUID of a marketplace resource to move.
```

## override_templates

Override templates

```bash
usage: waldur override_templates [-c CLEAN] templates_file

positional arguments:
  templates_file        Specifies location of templates file.

optional arguments:
  -c CLEAN, --clean CLEAN
                        This flag means total synchronization with the
                        template file you pass.
```

## pgmigrate

Load data with disabled signals.

```bash
usage: waldur pgmigrate [--path PATH]

optional arguments:
  --path PATH, -p PATH  Path to dumped database.
```

## print_notifications

Prints Mastermind notifications with a description and templates

## pull_openstack_volume_metadata

Pull OpenStack volumes metadata to marketplace.

```bash
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

```bash
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

## set_constance_image

A custom command to set Constance image configs with CLI

```bash
usage: waldur set_constance_image KEY PATH

positional arguments:
  KEY   Constance settings key
  PATH  Path to a logo
```

## status

Check status of Waldur MasterMind configured services

```bash
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


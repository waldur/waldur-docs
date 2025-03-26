# CLI guide

## axes_list_attempts

List access attempts

## axes_reset

Reset all access attempts and lockouts

## axes_reset_failure_logs

Reset access failure log records older than given days.

```bash
usage: waldur axes_reset_failure_logs [--age AGE]

options:
  --age AGE  Maximum age for records to keep in days
```

## axes_reset_ip

Reset all access attempts and lockouts for given IP addresses

```bash
usage: waldur axes_reset_ip ip [ip ...]

positional arguments:
  ip
```

## axes_reset_ip_username

Reset all access attempts and lockouts for a given IP address and username

```bash
usage: waldur axes_reset_ip_username ip username

positional arguments:
  ip
  username
```

## axes_reset_logs

Reset access log records older than given days.

```bash
usage: waldur axes_reset_logs [--age AGE]

options:
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

## create_provider

Create a service provider with a linked customer and load categories

```bash
usage: waldur create_provider [-n N] [-c C [C ...]]

options:
  -n N          Customer name
  -c C [C ...]  List of categories to load
```

## createstaffuser

Create a user with a specified username and password. User will be created as staff.

```bash
usage: waldur createstaffuser -u USERNAME -p PASSWORD -e EMAIL

options:
  -u USERNAME, --username USERNAME
  -p PASSWORD, --password PASSWORD
  -e EMAIL, --email EMAIL
```

## drop_leftover_openstack_projects

Drop leftover projects from remote OpenStack deployment.
  Leftovers are resources marked as terminated in Waldur but still present in the remote OpenStack.
  Such inconsistency may be caused by split brain problem in the distributed database.

```bash
usage: waldur drop_leftover_openstack_projects [--offering OFFERING]
                                               [--dry-run] [--fuzzy-matching]

options:
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

options:
  -o OUTPUT, --output OUTPUT
                        Specifies file to which the output is written. The
                        output will be printed to stdout by default.
```

## export_ami_catalog

Export catalog of Amazon images.

## export_auth_social

Export OIDC auth configuration as YAML format

```bash
usage: waldur export_auth_social [-o OUTPUT]

options:
  -o OUTPUT, --output OUTPUT
                        Specifies file to which the output is written. The
                        output will be printed to stdout by default.
```

## export_model_metadata

Collect and export metadata about Django models

## export_offering

Export an offering from Waldur. Export data includes JSON file with an offering data and a thumbnail. Names of this files include offering ID.

```bash
usage: waldur export_offering -o OFFERING -p PATH

options:
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

options:
  -y, --yes  The answer to any question which would be asked will be yes.
```

## import_auth_social

Import OIDC auth configuration in YAML format. The example of auth.yaml:

    - provider: "keycloak"   # OIDC identity provider in string format. Valid values are: "tara", "eduteams", "keycloak".
      label: "Keycloak"    # Human-readable IdP name.
      client_id: "waldur"   # A string used in OIDC requests for client identification.
      client_secret: OIDC_CLIENT_SECRET
      discovery_url: "http://localhost/auth/realms/YOUR_KEYCLOAK_REALM/.well-known/openid-configuration" # OIDC discovery endpoint.
      management_url: ""   # Endpoint for user details management.
      protected_fields:    # User fields that are imported from IdP.
        - "full_name"
        - "email"

```bash
usage: waldur import_auth_social auth_file

positional arguments:
  auth_file  Specifies location of auth configuration file.
```

## import_azure_image

Import Azure image

```bash
usage: waldur import_azure_image [--sku SKU] [--publisher PUBLISHER]
                                 [--offer OFFER]

options:
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

options:
  -p PATH, --path PATH  File path to offering data.
  -c CUSTOMER, --customer CUSTOMER
                        Customer UUID.
  -ct CATEGORY, --category CATEGORY
                        Category UUID.
  -o OFFERING, --offering OFFERING
                        Updated offering UUID.
```

## import_reppu_usages

Import component usages from Reppu for a specified year and month.

```bash
usage: waldur import_reppu_usages [-m MONTH] [-y YEAR]
                                  [--reppu-api-url REPPU_API_URL]
                                  [--reppu-api-token REPPU_API_TOKEN]
                                  [--dry-run | --no-dry-run]

options:
  -m MONTH, --month MONTH
                        Month for which data is imported.
  -y YEAR, --year YEAR  Year for which data is imported.
  --reppu-api-url REPPU_API_URL
                        Reppu API URL.
  --reppu-api-token REPPU_API_TOKEN
                        Reppu API Token.
  --dry-run, --no-dry-run
                        Dry run mode.
```

## import_roles

Import roles configuration in YAML format

```bash
usage: waldur import_roles roles_file

positional arguments:
  roles_file  Specifies location of roles configuration file.
```

## import_tenant_quotas

Import OpenStack tenant quotas to marketplace.

```bash
usage: waldur import_tenant_quotas [--dry-run]

options:
  --dry-run  Don't make any changes, instead show what objects would be
             created.
```

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

options:
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

options:
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

options:
  -p PROJECT_UUID, --project PROJECT_UUID
                        UUID of a project to move.
  -c CUSTOMER_UUID, --customer CUSTOMER_UUID
                        Target organization UUID
```

## move_resource

Move a marketplace resource to a different project.

```bash
usage: waldur move_resource -p PROJECT_UUID -r RESOURCE_UUID

options:
  -p PROJECT_UUID, --project PROJECT_UUID
                        Target project UUID
  -r RESOURCE_UUID, --resource RESOURCE_UUID
                        UUID of a marketplace resource to move.
```

## organization_access_subnets

Dumps information about organization access subnets, merging adjacent or overlapping networks.

```bash
usage: waldur organization_access_subnets [-o OUTPUT]

options:
  -o OUTPUT, --output OUTPUT
                        Specifies file to which the merged subnets will be
                        written. The output will be printed to stdout by
                        default.
```

## override_constance_settings

Override settings stored in django-constance. The example of .yaml file:

  ```yaml
   - WALDUR_SUPPORT_ENABLED: true # Enables support plugin
    WALDUR_SUPPORT_ACTIVE_BACKEND_TYPE: 'zammad' # Specifies zammad as service desk plugin
    ZAMMAD_API_URL: "https://zammad.example.com/api/" # Specifies zammad API URL
    ZAMMAD_TOKEN: "1282361723491" # Specifies zammad token
    ZAMMAD_GROUP: "default-group" # Specifies zammad group
    ZAMMAD_ARTICLE_TYPE: "email" # Specifies zammad article type
    ZAMMAD_COMMENT_COOLDOWN_DURATION: 7 # Specifies zammad comment cooldown duration
  ```

```bash
usage: waldur override_constance_settings constance_settings_file

positional arguments:
  constance_settings_file
                        Specifies location of file in YAML format containing
                        new settings
```

## override_roles

Override roles configuration in YAML format. The example of roles-override.yaml:

    - role: CUSTOMER.OWNER
     description: "Custom owner role"
     is_active: True
     add_permissions:
      - OFFERING.CREATE
      - OFFERING.DELETE
      - OFFERING.UPDATE
     drop_permissions:
      - OFFERING.UPDATE_THUMBNAIL
      - OFFERING.UPDATE_ATTRIBUTES

```bash
usage: waldur override_roles roles_file

positional arguments:
  roles_file  Specifies location of roles configuration file.
```

## override_templates

Override templates

```bash
usage: waldur override_templates [-c CLEAN] templates_file

positional arguments:
  templates_file        Specifies location of templates file.

options:
  -c CLEAN, --clean CLEAN
                        This flag means total synchronization with the
                        template file you pass.
```

## pgmigrate

Load data with disabled signals.

```bash
usage: waldur pgmigrate [--path PATH]

options:
  --path PATH, -p PATH  Path to dumped database.
```

## print_events_enums

Prints all event types as typescript enums.

## print_features_description

Prints all Waldur feature description as typescript code.

## print_features_docs

Prints all Waldur feature toggles in markdown format.

## print_features_enums

Prints all Waldur feature toggles as typescript enums.

## print_notifications

Prints Mastermind notifications with a description and templates

## print_permissions_description

Prints all Waldur permissions description as typescript code.

## print_settings_description

Prints all Waldur feature description as typescript code.

## pull_openstack_volume_metadata

Pull OpenStack volumes metadata to marketplace.

```bash
usage: waldur pull_openstack_volume_metadata [--dry-run]

options:
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

options:
  --dry-run  Don't make any changes, instead show what objects would be
             created.
```

## rebuild_billing

Create or update price estimates based on invoices.

## removestalect

Remove Django event log records with stale content types.

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

options:
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


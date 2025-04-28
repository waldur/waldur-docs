# Ad-hoc scripts

This section describes different ad-hoc scripts used by Waldur developers.

## Usage-related scripts

### Restore CPU/GPU/RAM usages for a month

Sometimes, Waldur can have issues with data correctness. They can be caused by different circumstansies, e.g. problems with data syncronization between Waldur backend and service provider software. In order to resolve these issues, a user can restore usage data with [restore_usages.py](scripts/update_usages.py) script.

### Generate openmetrics file with usages for several months

If a user needs to create openmetrics file with usages, e.g. for [historical data backfilling in Prometheus](https://medium.com/tlvince/prometheus-backfilling-a92573eb712c), the [generate_openmetrics_usages.py](scripts/generate_openmetrics_usages.py) can be used.

### Wipe tenants and all related resources from OpenStack

If a user needs to remove a tenant with all related objects (instances, volumes, backups, etc.) manually, [this script](scripts/wipe-tenants.py) should be used. It removes all the tenants with names from `tenant_names` list using an OpenStack administrator project. Please, replace `<main-tenant-uuid>` (line 13) with the corresponding UUID of the admin tenant in Waldur.

### Import projects with slug info

A CSV-file with the following format is required:

```csv
"id","unix_gid","valid_from","valid_to","accessible_from","accessible_to"
"abc","10000","01/1/2024","31/3/2024","05/1/2024","28/3/2024"
```

Put this file to the `/tmp/projects-info.csv` location and
execute [this script](scripts/import_projects_with_slug.py) with your Waldur shell.

### Migrate legacy SLURM allocations to a new SLURM-remote offering

```python
from waldur_mastermind.marketplace import models as marketplace_models

COMPONENT_TYPE_MAP = {
    "cpu": "cpu",
    "gpu": "gres/gpu",
    "ram": "mem",
}


def migrate_legacy_allocation(
    resource: marketplace_models.Resource,
    offering_new: marketplace_models.Offering,
    dry_run=True,
):
    plan_old = resource.plan
    if dry_run:
        print("Dry-run migrating legacy allocation %s" % resource)
    else:
        print("Migrating legacy allocation %s" % resource)
        resource.offering = offering_new
        print("Updating resource plan to %s" % plan_new)
        resource.plan = plan_new
        resource.save(update_fields=["offering", "plan"])
    try:
        for usage in resource.usages.all():
            new_component = offering_new.components.get(
                type=COMPONENT_TYPE_MAP[usage.component.type]
            )
            if dry_run:
                print("Dry-run switching component usage %s" % usage)
            else:
                print("Switching usage %s" % usage)
                usage.component = new_component
                usage.save(update_fields=["component"])
    except Exception as e:
        if dry_run:
            print("Dry-run Rolling back resource offering and plan because of %s" % e)
        else:
            print("Rolling back resource offering and plan because of %s" % e)
            resource.offering = offering_old
            resource.plan = plan_old
            resource.save(update_fields=["offering", "plan"])

offering_old_uuid = "<LEGACY_OFFERING_UUID>"
offering_new_uuid = "<NEW_OFFERING_UUID>"
offering_old = marketplace_models.Offering.objects.get(uuid=offering_old_uuid)
offering_new = marketplace_models.Offering.objects.get(uuid=offering_new_uuid)
plan_new = offering_new.plans.first()

legacy_allocations = marketplace_models.Resource.objects.filter(offering=offering_old)

i = 1
legacy_allocations_count = legacy_allocations.count()
for legacy_allocation in legacy_allocations:
    print("Processing resource %s/%s" % (i, legacy_allocations_count))
    try:
        migrate_legacy_allocation(legacy_allocation, offering_new, dry_run=False)
    except Exception as e:
        print("Failed to migrate allocation %s: %s" % (legacy_allocation, e))
    i += 1

```

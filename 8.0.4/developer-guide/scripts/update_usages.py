"""
The script reads a file (usually reported by LUMI) with correct usages per component
and changes the related data in Waldur instance.

The format of the file's name is required to meet "<month_name>.csv" format
The content of the file should be csv formatted as:
"plan_period_uuid","cpu_k_hours","gpu_hours","gb_k_hours"
"<UUID>","<USAGE AMOUNT>","<USAGE AMOUNT>","<USAGE AMOUNT>"
"""

from waldur_mastermind.marketplace import models as mm
from waldur_core.core import utils as core_utils
import csv
from datetime import date

MONTHS = [
    (
        "january",
        1,
        2022,
    ),
    (
        "december",
        12,
        2021,
    ),
    (
        "november",
        11,
        2021,
    ),
    (
        "february",
        2,
        2022,
    ),
    (
        "march",
        3,
        2022,
    ),
]

for m_name, month, year in MONTHS:
    print(f"Processing {m_name} data...")
    with open(f"{m_name}.csv", "r") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            plan_period_uuid = row.pop("plan_period_uuid")
            plan_period: mm.ResourcePlanPeriod = mm.ResourcePlanPeriod.objects.get(
                uuid=plan_period_uuid
            )
            resource: mm.Resource = plan_period.resource
            offering: mm.Offering = resource.offering
            print(f"Resource: {resource}, offering: {offering}")
            components_map = {
                component.type: component for component in offering.components.all()
            }
            print(f"Components map: {components_map}")
            first_day_of_month = date(year=year, month=month, day=1)
            billing_period = core_utils.month_start(first_day_of_month)
            last_day_of_month = core_utils.month_end(first_day_of_month)

            for usage_type, amount in row.items():
                amount = int(amount)
                component = components_map[usage_type]
                comp_usage, created = mm.ComponentUsage.objects.update_or_create(
                    resource=resource,
                    component=component,
                    plan_period=plan_period,
                    billing_period=billing_period,
                    defaults={
                        "usage": amount,
                        "date": last_day_of_month,
                    },
                )
                if created:
                    print(f"Created: {comp_usage}")
                else:
                    print(f"Updated: {comp_usage}")

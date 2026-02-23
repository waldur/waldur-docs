"""
The script fetches usage data from Waldur instance and generates metrics
in openmetrics format with usage distributed eventually with period of 2 minutes.

The output of the script is a set of files each of which named `<month>-metrics.txt`

If you need, you can include kubernetes-related metadata to the output, for example:
cluster="kubernetes",component="services",
environment="skylark",instance="kubernetes.hpc.ut.ee:6443",
job="kubernetes-services",namespace="default",tenant="HPC"
"""

import calendar
from datetime import date, datetime, timedelta
from waldur_mastermind.marketplace import models as mm
from waldur_core.core import utils as core_utils
from django.db.models.aggregates import Sum


MONTHS_MAP = (
    ("november", 11, 2021),
    ("december", 12, 2021),
    ("january", 1, 2022),
    ("february", 2, 2022),
    ("march", 3, 2022),
    ("april", 4, 2022),
)

backend_id_backlist = []


for month_name, month, year in MONTHS_MAP:
    f = open(f"{month_name}-metrics.txt", "w")
    f.write("# HELP aggregated_usages Aggregated usages\n")
    f.write("# TYPE aggregated_usages gauge\n")
    comp_usages = list(
        mm.ComponentUsage.objects.filter(
            billing_period__year=year, billing_period__month=month
        )
        .exclude(resource__backend_id__in=backend_id_backlist)
        .values("resource__offering__uuid", "component__type")
        .annotate(usage=Sum("usage"))
    )
    for comp_usage in comp_usages:
        offering = mm.Offering.objects.get(uuid=comp_usage["resource__offering__uuid"])
        comp_usage["offering_uuid"] = offering.uuid.hex
        comp_usage["offering_country"] = offering.country or offering.customer.country
        division = offering.divisions.first()
        comp_usage["division_name"] = division.name
        comp_usage["division_uuid"] = division.uuid.hex
    month_start = core_utils.month_start(date(year=year, month=month, day=1))
    days_in_month = calendar.monthrange(year, month)[1]
    if month == 4:
        number_of_minutes = 25 * 24 * 60  # 26.04.2022
    else:
        number_of_minutes = (
            days_in_month * 24 * 60
        )  # We split the period with 1 minute timeframe
    # Logging can be disabled
    # print(month_start)
    # print(days_in_month)
    # print(number_of_minutes)
    print(month_name)
    dates = [month_start + timedelta(minutes=i) for i in range(0, number_of_minutes, 2)]
    for fixed_date in dates:
        for comp_usage in comp_usages:
            usage_amount = comp_usage["usage"]
            daily_usage = round(usage_amount / (days_in_month + 1 - fixed_date.day), 1)
            f.write(
                """aggregated_usages{division_name="%s",division_uuid="%s","""
                """offering_country="%s",offering_uuid="%s",type="%s"} %s %s\n"""
                % (
                    comp_usage["division_name"],
                    comp_usage["division_uuid"],
                    comp_usage["offering_country"],
                    comp_usage["offering_uuid"],
                    comp_usage["component__type"],
                    float(daily_usage),
                    int(datetime.timestamp(fixed_date)),
                )
            )
            # print(fixed_date, comp_usage)
    f.close()

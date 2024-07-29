"""
This script reads CSV-file containing projects info
and creates/updates the corresponding projects in Waldur.
"""

#!/bin/python

import csv
import datetime

from waldur_core.structure import models as structure_models


def create_project(project_info):
    project_id = project_info["id"]
    valid_from = datetime.datetime.strptime("25/2/2024", "%d/%m/%Y").date()
    valid_to = datetime.datetime.strptime(project_info["valid_to"], "%d/%m/%Y").date()
    description = project_info.get("description", "")
    project, created = structure_models.Project.objects.update_or_create(
        name=project_id,
        defaults={
            "created": valid_from,
            "description": description,
            "end_date": valid_to,
            "slug": project_id,
        },
    )
    if created:
        print(f"The project {project.name} has been created")
    else:
        print(f"The project {project.name} has been updated")


with open("/tmp/projects-info.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for project_data in reader:
        create_project(project_data)

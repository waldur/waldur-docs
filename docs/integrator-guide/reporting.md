# Reporting

Examples below show how it's possible to use Waldur SDK for generation of custom reports.

## Running the scripts

All of the scripts below should be saved as files and executed in the environment with installed
[Waldur SDK](./Waldur-SDK/waldur-sdk.md). Please make sure that you have python3 and pip installed in your command line.

Make sure that you update ``WALDUR_HOST`` and ``TOKEN`` with values that match your target Waldur deployment.

```bash
pip install https://github.com/waldur/python-waldur-client/archive/master.zip
python <reporting-script-name>.py
```

## Project reporting

The first scenario is report generation about monthly costs of each project.
The name of the output file is `project-report.csv`.

Code example:

```python
import os
import csv
from collections import defaultdict
from datetime import datetime
from waldur_api_client.client import AuthenticatedClient
from waldur_api_client.api.customers import customers_list
from waldur_api_client.api.invoice_items import invoice_items_list

# Constants
CURRENT_YEAR = datetime.now().year
CURRENT_MONTH = datetime.now().month
CSV_FILE_PATH = 'project-report.csv'
HEADER = [
    'Organization name',
    'Organization abbreviation',
    'Project name',
    'Monthly cost of a project',
]

# Initialize client
client = AuthenticatedClient(
    base_url=os.environ.get('WALDUR_API_URL'),
    token=os.environ.get('WALDUR_API_TOKEN'),
)

# Get all customers
customers = customers_list.sync(client=client)
if not customers:
    print("No customers found")
    exit()

with open(CSV_FILE_PATH, 'w', encoding='UTF8') as out_file:
    writer = csv.writer(out_file)
    writer.writerow(HEADER)

    for customer in customers:
        project_reporting = defaultdict(lambda: 0.0)

        # Get invoice items for the customer
        items = invoice_items_list.sync(
            client=client,
            customer_uuid=customer.uuid,
            year=CURRENT_YEAR,
            month=CURRENT_MONTH
        )

        if items:
            for item in items:
                if item.name and item.unit_price:
                    project_reporting[item.name] += float(item.unit_price)
            # Write to CSV file
            for project_name, cost in project_reporting.items():
                writer.writerow([
                    customer.name,
                    customer.abbreviation,
                    project_name,
                    cost,
                ])
```

Example of output file content:

```csv
Organization name,Organization abbreviation,Project name,Monthly cost of a project
Org A,OA,Team1,10
Org B,OB,Demo project,70
Org B,OB,Industrial project,100
Org C,OC,Lab1,110
```

## OpenStack tenant reporting

The second scenario is report generation about quotas and monthly costs of OpenStack tenants.

The name of the output file is `openstack-report.csv`.

Code example:

```python
import os
import csv
from datetime import datetime
from waldur_api_client.client import AuthenticatedClient
from waldur_api_client.api.customers import customers_list
from waldur_api_client.api.invoice_items import invoice_items_list
from waldur_api_client.api.marketplace_resources import marketplace_resources_list
from waldur_api_client.api.openstack_tenants import openstack_tenants_list

# Constants
CURRENT_YEAR = datetime.now().year
CURRENT_MONTH = datetime.now().month
CSV_FILE_PATH = 'openstack-report.csv'
HEADER = [
    'Name of the OpenStack Tenant resource',
    'vCPU limit',
    'RAM limit',
    'Storage limit',
    'Monthly cost of the resource',
    'Project name',
    'Organization name',
    'Organization abbreviation',
]

# Initialize client
client = AuthenticatedClient(
    base_url=os.environ.get('WALDUR_API_URL'),
    token=os.environ.get('WALDUR_API_TOKEN'),
)

# Get all customers
customers = customers_list.sync(client=client)
if not customers:
    print("No customers found")
    exit()

with open(CSV_FILE_PATH, 'w', encoding='UTF8') as out_file:
    writer = csv.writer(out_file)
    writer.writerow(HEADER)

    for customer in customers:
        # Get invoice items for the customer
        items = invoice_items_list.sync(
            client=client,
            customer_uuid=customer.uuid,
            year=CURRENT_YEAR,
            month=CURRENT_MONTH
        )

        # Create resource costs mapping
        resource_costs = {}
        for item in items:
            if item.name and item.unit_price:
                resource_costs[item.name] = float(item.unit_price)


        # Get tenants for the customer
        tenants = openstack_tenants_list.sync(
            client=client,
            customer_uuid=customer.uuid
        )
            
        for tenant in tenants:
            if not tenant.marketplace_resource_uuid:
                continue

            # Get resource details
            resources = marketplace_resources_list.sync(
                client=client,
                uuid=tenant.marketplace_resource_uuid
            )

            if not resources:
                continue

            resource = resources[0]
            limits = resource.limits or {}

            writer.writerow([
                tenant.name,
                limits.get('cores', 0),
                limits.get('ram', 0),
                limits.get('storage', 0),
                resource_costs.get(str(tenant.marketplace_resource_uuid), 0.0),
                tenant.project_name,
                tenant.customer_name,
                tenant.customer_abbreviation
            ])
```

Example of output file content:

```csv
Name of the OpenStack.Tenant resource,vCPU limit,RAM limit,Storage limit,Monthly cost of the resource,Project name,Organization name,Organization abbreviation
HPC_resource,2.0,4096.0,61440.0,2.18,Team1,Org A,OA
OpenStack Cloud for testing,1,1024,102400,5.17,Demo project,Org B,OB
OpenStack Cloud,12,51200,614400,21.77,Industrial project,Org B,OB
Private Cloud,1,1024,102400,5.17,Lab1,Org C,OC
```

## Reporting by provider

To get CSV summary of consumption by provider, the following script can be useful. Output
will be a file per provider with a short summary of invoice items for the defined period.

```python
import csv
from collections import defaultdict
import unicodedata
import re
from decimal import Decimal
from datetime import datetime

from waldur_api_client import AuthenticatedClient
from waldur_api_client.api.customers import customers_list
from waldur_api_client.api.invoices import invoices_list
from waldur_api_client.errors import UnexpectedStatus

# Your Waldur instance data
WALDUR_HOST = 'example.waldur.com'
TOKEN = 'SUPPORT_STAFF_SECRET_TOKEN'

# Date-related constants
CURRENT_YEAR = datetime.now().year
CURRENT_MONTH = datetime.now().month


def slugify(value, allow_unicode=False):
    """
    Taken from https://github.com/django/django/blob/master/django/utils/text.py
    Convert to ASCII if 'allow_unicode' is False. Convert spaces or repeated
    dashes to single dashes. Remove characters that aren't alphanumerics,
    underscores, or hyphens. Convert to lowercase. Also strip leading and
    trailing whitespace, dashes, and underscores.
    """
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize('NFKC', value)
    else:
        value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value.lower())
    return re.sub(r'[-\s]+', '-', value).strip('-_')

# Client instance initialization
client = AuthenticatedClient(
    base_url=WALDUR_HOST,
    token=TOKEN,
)

# Organizations data fetching
customers = customers_list.sync(client=client)

sp = {}

for customer in customers:
    try:
        # Invoices data fetching
        invoices = invoices_list.sync(
            client=client,
            customer_uuid=customer.uuid,
            year=CURRENT_YEAR,
            month=CURRENT_MONTH
        )
        if not invoices:
            continue
        invoice = invoices[0]
    # If customer doesn't have any projects or created after the requested month
    except UnexpectedStatus:
        continue

    for item in invoice.items:
        # allocate to SP
        if hasattr(item.details, 'service_provider_name'):
            provider_name = item.details.service_provider_name
            if provider_name in sp:
                sp[provider_name].append((item, customer.name))
            else:
                sp[provider_name] = [(item, customer.name)]

for provider in sp.keys():
    filename = f'{slugify(provider)}_{CURRENT_YEAR}_{CURRENT_MONTH}.csv'
    print('Generating', filename)
    with open(filename, 'w', encoding='UTF8') as out_file:
        writer = csv.writer(out_file)
        HEADER = [
            'Kood',
            'Nimetus',
            'Klient',
            'Kogus',
            'Hind',
            'Summa',
        ]
        writer.writerow(HEADER)
        for inv, customer_name in sp[provider]:
            code = inv.article_code
            try:
                code = inv.article_code.split('_')[0]
            except:
                # failed to parse custom logic
                pass
            writer.writerow(
                [
                    code,
                    inv.name,
                    customer_name,
                    int(Decimal(str(inv.quantity))),
                    inv.unit_price,
                    inv.price,
                ]
            )
```

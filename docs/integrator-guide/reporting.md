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
from waldur_client import WaldurClient, ObjectDoesNotExist
import csv
from collections import defaultdict

# Your Waldur instance data
WALDUR_HOST = 'example.waldur.com'
TOKEN = 'STAFF_USER_API_TOKEN'

# Date-related constants
CURRENT_YEAR = 2021
CURRENT_MONTH = 10

# Other constants
CSV_FILE_PATH = 'project-report.csv'
HEADER = [
    'Organization name',
    'Organization abbreviation',
    'Project name',
    'Monthly cost of a project',
]

# WaldurClient instance initialisation
client = WaldurClient(
    f'https://{WALDUR_HOST}/api/', TOKEN
)

# Organisations data fetching
customers_data = client.list_customers()

with open(CSV_FILE_PATH, 'w', encoding='UTF8') as out_file:
    writer = csv.writer(out_file)
    writer.writerow(HEADER)

    for customer_data in customers_data:
        project_reporting = defaultdict(lambda: 0.0)

        try:
            # Invoices data fetching
            invoice_data = client.get_invoice_for_customer(
                customer_data['uuid'], CURRENT_YEAR, CURRENT_MONTH
            )
        # If customer doesn't have any projects or created after the requested month
        except ObjectDoesNotExist:
            pass

        invoice_items = [item for item in invoice_data['items']]

        # Cost aggregation per each project
        for item in invoice_items:
            project_reporting[item['project_name']] += float(item['price'])

        for key, val in project_reporting.items():
            writer.writerow(
                [
                    customer_data['name'],
                    customer_data['abbreviation'],
                    key,
                    val,
                ]
            )
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
from waldur_client import WaldurClient, ObjectDoesNotExist
from pprint import pprint
import csv

# Your Waldur instance data
WALDUR_HOST = 'example.waldur.com'
TOKEN = 'STAFF_USER_API_TOKEN'

# Date-related constants
CURRENT_YEAR = 2021
CURRENT_MONTH = 10

# WaldurClient instance initialisation
client = WaldurClient(
    f'https://{WALDUR_HOST}/api/', TOKEN
)

# Other constants
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

# Organisations data fetching
customers_data = client.list_customers()

with open(CSV_FILE_PATH, 'w', encoding='UTF8') as out_file:
    writer = csv.writer(out_file)
    writer.writerow(HEADER)
    for customer_data in customers_data:
        customer_uuid = customer_data['uuid']
        try:
            # Invoices data fetching
            invoice_data = client.get_invoice_for_customer(
                customer_data['uuid'], CURRENT_YEAR, CURRENT_MONTH
            )
        # If customer doesn't have any projects or created after the requested month
        except ObjectDoesNotExist:
            pass

        # Tenants data fetching
        tenants = client.list_tenants({'customer_uuid': customer_uuid})

        resource_costs = {item['resource_uuid']: item['price'] for item in invoice_data['items']}

        for tenant in tenants:
            resource_uuid = tenant['marketplace_resource_uuid']

            # Resource data fetching
            resource = client.get_marketplace_resource(resource_uuid)
            limits = resource['limits']
            try:
                writer.writerow([
                    tenant['name'],
                    limits['cores'],
                    limits['ram'],
                    limits['storage'],
                    resource_costs.get(resource_uuid, 0.0), # if a resource wasn't used during the month
                    tenant['project_name'],
                    tenant['customer_name'],
                    tenant['customer_abbreviation']
                ])
            except KeyError as e:
                pprint(resource_uuid)
                pprint(e)
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

from waldur_client import WaldurClient, ObjectDoesNotExist

# Your Waldur instance data
WALDUR_HOST = 'example.waldur.com'
TOKEN = 'SUPPORT_STAFF_SECRET_TOKEN'

# Date-related constants
CURRENT_YEAR = 2023
CURRENT_MONTH = 4


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

# WaldurClient instance initialisation
client = WaldurClient(
    f'https://{WALDUR_HOST}/api/', TOKEN
)

# Organisations data fetching
customers_data = client.list_customers()

sp = {}

for customer_data in customers_data:
    try:
        # Invoices data fetching
        invoice_data = client.get_invoice_for_customer(
            customer_data['uuid'], CURRENT_YEAR, CURRENT_MONTH
        )
    # If customer doesn't have any projects or created after the requested month
    except ObjectDoesNotExist:
        continue

    invoice_items = [item for item in invoice_data['items']]

    for item in invoice_items:
        # allocate to SP
        if 'service_provider_name' in item['details']:
            if item['details']['service_provider_name'] in sp:
                sp[item['details']['service_provider_name']].append((item, customer_data['name']))
            else:
                sp[item['details']['service_provider_name']] = [(item, customer_data['name'])]

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
            code = inv['article_code']
            try:
                code = inv['article_code'].split('_')[0]
            except:
                # failed to parse custom logic
                pass
            writer.writerow(
                [
                    code,
                    inv['name'],
                    customer_name,
                    int(Decimal(inv['quantity'])),
                    inv['unit_price'],
                    inv['price'],
                ]
            )

```

# Custom scripts

`Custom scripts` is a type of plugin that allows defining custom scripts that are executed
at different lifecycle events of the resource. The scripts are executed in one time containers.
Depending on the deployment type, it can be either a docker container for docker-compose-based, or
Kubernetes Jobs for Helm-based deployments.

The following lifecycle events are supported:

- Creation;
- Update - change of plans or limits;
- Termination;
- Regular updates - executed once per hour, aka pull script.

## Script output format

It is possible to control certain aspects of resource management with outputs of the custom scripts.
Below we list currently supported conventions and their impact.

### Creation script

You can set the the backend_id of the created resource by passing a single string as the last
line of the output.

```python
# for python-based scripts
import uuid

UUID = uuid.uuid4()
print(UUID)
```

If you want to save additional metadata, then last line of output should consist of 2 strings:

- ID of the created resource that will be saved as backend_id;
- Base64 encoded metadata object.

```python
# for python-based scripts
import base64
import uuid

UUID = uuid.uuid4()
metadata = {"backend_metadata": {"cpu": 1}}
print(UUID + ' ' + base64.b64encode(metadata))
```

### Regular updates script

The script for regular updates allows to update usage information as well as provide updates of reporting.
In all cases the last line should include a base64-encoded string containing a dictionary with keywords:

- "usages" for usage reporting;
- "report" for updating resource report.

Examples of Python-based scripts are:

```python
# for python-based scripts
import base64

info = {
  "usages": [
    {
      "type": "cpu",
      "amount": 10
    },
  ]
}

info_json = json.dumps(info)

info_json_encoded = info_json.encode("utf-8")

print(base64.b64encode(info_json_encoded).decode("utf-8"))
```

```python
# for python-based scripts
import base64

info = {
  "report": [
    {
      "header": "header",
      "body": "body"
    },
  ]
}

info_json = json.dumps(info)

info_json_encoded = info_json.encode("utf-8")

print(base64.b64encode(info_json_encoded).decode("utf-8"))
```

## Example scripts

Each of the scripts below require access to remote Waldur instance.
Credentials for this passed as environment variables to the scripts with keys:

- `WALDUR_API_URL` - URL of remote Waldur API including `/api/` path, example: `http://localhost/api/`
- `WALDUR_API_TOKEN` - token for a remote user with permissions of service provider owner

### Script for resource creation

In the remote Waldur site, customer and offering should be pre-created for successful resource creation.
Please, add the necessary variables to the local offering's environment:

- `REMOTE_CUSTOMER_NAME` - name of the pre-created customer in the remote Waldur
- `REMOTE_OFFERING_UUID` - UUID of the remote offering for creation of the remote resource
- `PROJECT_NAME` - name of the remote project to be created
- `PI_EMAILS` - optional comma-separated list of emails receiving invitations to the project after creation of the remote resource
- `REMOTE_PROJECT_CREDIT_AMOUNT` - optional amount of credit applied to the remote project


```python
from waldur_client import WaldurClient
from os import environ
from time import sleep
import uuid
import json

waldur_client = WaldurClient(environ["WALDUR_API_URL"], environ["WALDUR_API_TOKEN"])

CUSTOMER_NAME = environ["REMOTE_CUSTOMER_NAME"]
OFFERING_UUID = environ["REMOTE_OFFERING_UUID"]
PROJECT_NAME = environ["REMOTE_PROJECT_NAME"]
PI_EMAILS = environ.get("PI_EMAILS")
RESOURCE_LIMITS = environ["LIMITS"]
PROJECT_CREDIT_AMOUNT = environ.get("REMOTE_PROJECT_CREDIT_AMOUNT")


def get_or_create_project():
    print(f"Listing customers with name_exact: {CUSTOMER_NAME}")
    existing_customers = waldur_client.list_customers({"name_exact": CUSTOMER_NAME})
    if len(existing_customers) == 0:
        print(f"Customer with name {CUSTOMER_NAME} not found")
        exit(1)
    else:
        print(f"Customer with name {CUSTOMER_NAME} exists")
        customer = existing_customers[0]

    customer_uuid = customer["uuid"]

    print(f"Listing projects with name_exact: {PROJECT_NAME}")
    existing_projects = waldur_client.list_projects({"name_exact": PROJECT_NAME})
    if len(existing_projects) == 0:
        print(f"Project with name {PROJECT_NAME} not found, creating it")
        return waldur_client.create_project(customer_uuid, PROJECT_NAME)
    else:
        print(f"Project with name {PROJECT_NAME} exists")
        return existing_projects[0]


def get_or_create_project_credits():
    print(f"Listing project credits for project_uuid: {project_uuid}")
    project_credits = waldur_client.list_project_credits({"project_uuid": project_uuid})
    if len(project_credits) == 0:
        print(
            f"Project credit for project_uuid {project_uuid} not found, creating it with amount {PROJECT_CREDIT_AMOUNT}"
        )
        return waldur_client.create_project_credit(
            project_uuid, PROJECT_CREDIT_AMOUNT
        )
    else:
        print(f"Project credit for project_uuid {project_uuid} exists")
        return project_credits[0]


def invite_PIs():
    print("Listing active roles")
    roles = waldur_client.get_roles(params={"is_active": True})
    print('Looking up role with name "PROJECT.MANAGER"')
    project_manager_role = [
        role for role in roles if role["name"] == "PROJECT.MANAGER"
    ][0]
    project_manager_role_uuid = project_manager_role["uuid"]

    print("Inviting PIs")
    for pi_email in PI_EMAILS.split(","):
        if not pi_email:
            continue
        print(f"Creating project invitation for email: {pi_email}")
        waldur_client.create_project_invitation(
            pi_email, project_uuid, project_manager_role_uuid
        )


def create_resource(resource_name):
    print(f"Fetching marketplace provider offerings with UUID: {OFFERING_UUID}")
    offering = waldur_client.get_marketplace_provider_offering(OFFERING_UUID)
    print("Getting first plan UUID from offering")
    plan_uuid = offering["plans"][0]["uuid"]
    resource_attributes = {
        "name": resource_name,
    }
    resource_limits = json.loads(RESOURCE_LIMITS)

    print("Submitting order")
    order_metadata = waldur_client.create_resource_via_marketplace(
        project_uuid, OFFERING_UUID, plan_uuid, resource_attributes, resource_limits
    )
    print("Fetching order")
    create_order_uuid = order_metadata["create_order_uuid"]
    resource_uuid = order_metadata["marketplace_resource_uuid"]
    order = waldur_client.get_order(create_order_uuid)

    print("Approving order")
    waldur_client.marketplace_order_approve_by_provider(order["uuid"])
    order = waldur_client.get_order(create_order_uuid)

    max_retries = 10
    retry_count = 0
    print("Waiting for order to be done")
    while order["state"] != "done" and retry_count < max_retries:
        print(f"Order state: {order['state']}")
        order = waldur_client.get_order(order["uuid"])
        sleep(5)
        retry_count += 1

    if order["state"] != "done":
        print(f"Order execution timed out, state is {order['state']}")
        exit(1)

    print("Order is done")

    print(f"Fetching marketplace provider resource with UUID: {resource_uuid}")
    resource = waldur_client.get_marketplace_provider_resource(resource_uuid)

    print(f'Resource state is {resource["state"]}')
    return resource

unique_id = uuid.uuid4().hex
resource_name = f"portal-test-{unique_id}"

project = get_or_create_project()
project_uuid = project["uuid"]

if PROJECT_CREDIT_AMOUNT is not None:
    get_or_create_project_credits()

resource = create_resource(resource_name)

if PI_EMAILS is not None:
    invite_PIs()

print("Execution finished")

print(resource["uuid"])
```

### Script for usage pull

This script periodically pulls usage data of the remote resource and saves it locally.

```python
from waldur_client import WaldurClient
from os import environ
import datetime
import base64
import json

waldur_client = WaldurClient(environ["WALDUR_API_URL"], environ["WALDUR_API_TOKEN"])

RESOURCE_UUID = environ["RESOURCE_BACKEND_ID"]

current_date = datetime.datetime.now()
month_start = datetime.datetime(day=1, month=current_date.month, year=current_date.year).date()

print(f"Fetching resource usages from {month_start.isoformat()}")
resource_usages = waldur_client.list_component_usages(
    RESOURCE_UUID,
    month_start,
)

usages_data = []

for usage in resource_usages:
    usages_data.append(
        {
            "type": usage["type"],
            "amount": usage["usage"],
        }
    )

output = {
    "usages": usages_data,
}

output_json = json.dumps(output)

output_json_encoded = output_json.encode("utf-8")

print(base64.b64encode(output_json_encoded).decode("utf-8"))
```

### Script for resource termination

This script terminates the remote resource.

```python
from waldur_client import WaldurClient
from os import environ
from time import sleep

waldur_client = WaldurClient(environ["WALDUR_API_URL"], environ["WALDUR_API_TOKEN"])

RESOURCE_UUID = environ["RESOURCE_BACKEND_ID"]

print('Creating resource termination order')
order_uuid = waldur_client.marketplace_provider_resource_terminate_order(RESOURCE_UUID)

print('Approving the order')
waldur_client.marketplace_order_approve_by_provider(order_uuid)

order = waldur_client.get_order(order_uuid)
max_retries = 10
retry_count = 0
print("Waiting for order to be done")
while order["state"] != "done" and retry_count < max_retries:
    print(f"Order state: {order['state']}")
    order = waldur_client.get_order(order["uuid"])
    sleep(5)
    retry_count += 1

if order["state"] != "done":
    print(f"Order execution timed out, state is {order['state']}")
    exit(1)
```

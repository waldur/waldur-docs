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

If you want to save additional metadata, then last line of output should consist of 2 space separated strings:

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
from os import environ
from time import sleep
import uuid
import json
from waldur_api_client import AuthenticatedClient
from waldur_api_client.api.customers import customers_list
from waldur_api_client.api.projects import projects_list, projects_create
from waldur_api_client.api.marketplace_provider_offerings import marketplace_provider_offerings_retrieve
from waldur_api_client.api.marketplace_resources import marketplace_resources_create
from waldur_api_client.api.marketplace_orders import marketplace_orders_retrieve,marketplace_orders_create, marketplace_orders_approve_by_provider
from waldur_api_client.api.marketplace_provider_resources import marketplace_provider_resources_retrieve
from waldur_api_client.api.project_credits import project_credits_list, project_credits_create
from waldur_api_client.api.roles import roles_list
from waldur_api_client.api.project_invitations import project_invitations_create
from waldur_api_client.models import ProjectCreditRequest, OrderCreateRequest, InvitationRequest, RequestTypes, OrderState
from waldur_api_client.api.user_invitations import user_invitations_create
from os import environ
from time import sleep


client = AuthenticatedClient(
    base_url=environ["WALDUR_API_URL"],
    token=environ["WALDUR_API_TOKEN"],
    prefix="Token",
)

CUSTOMER_NAME = environ["REMOTE_CUSTOMER_NAME"]
OFFERING_UUID = environ["REMOTE_OFFERING_UUID"]
PROJECT_NAME = environ["REMOTE_PROJECT_NAME"]
PI_EMAILS = environ.get("PI_EMAILS")
RESOURCE_LIMITS = environ["LIMITS"]
PROJECT_CREDIT_AMOUNT = environ.get("REMOTE_PROJECT_CREDIT_AMOUNT")


def get_or_create_project():
    print(f"Listing customers with name_exact: {CUSTOMER_NAME}")
    existing_customers = customers_list.sync(client=client, name_exact=CUSTOMER_NAME)
    if not existing_customers:
        print(f"Customer with name {CUSTOMER_NAME} not found")
        exit(1)
    else:
        print(f"Customer with name {CUSTOMER_NAME} exists")
        customer = existing_customers[0]

    customer_uuid = customer.uuid

    print(f"Listing projects with name_exact: {PROJECT_NAME}")
    existing_projects = projects_list.sync(client=client, name_exact=PROJECT_NAME)
    if not existing_projects:
        print(f"Project with name {PROJECT_NAME} not found, creating it")
        return projects_create.sync(client=client, customer_uuid=customer_uuid, name=PROJECT_NAME)
    else:
        print(f"Project with name {PROJECT_NAME} exists")
        return existing_projects[0]


def get_or_create_project_credits():
    print(f"Listing project credits for project_uuid: {project_uuid}")
    project_credits = project_credits_list.sync(client=client, project_uuid=project_uuid)
    if not project_credits:
        print(f"Project credit for project_uuid {project_uuid} not found, creating it with amount {PROJECT_CREDIT_AMOUNT}")
        return project_credits_create.sync(
            client=client,
            body=ProjectCreditRequest(
                project=project_uuid,
                value=PROJECT_CREDIT_AMOUNT
            )
        )
    else:
        print(f"Project credit for project_uuid {project_uuid} exists")
        return project_credits[0]


def invite_PIs():
    print("Listing active roles")
    roles = roles_list.sync(client=client, is_active=True)
    print('Looking up role with name "PROJECT.MANAGER"')
    project_manager_role = next(role for role in roles if role.name == "PROJECT.MANAGER")
    project_manager_role_uuid = project_manager_role.uuid

    print("Inviting PIs")
    for pi_email in PI_EMAILS.split(","):
        if not pi_email:
            continue
        print(f"Creating project invitation for email: {pi_email}")
        user_invitations_create.sync(
            client=client,
            body=InvitationRequest(
                role=project_manager_role_uuid,
                scope=project_uuid,
                email=pi_email
            )
        )

def create_resource(resource_name):
    print(f"Fetching marketplace provider offerings with UUID: {OFFERING_UUID}")
    offering = marketplace_provider_offerings_retrieve.sync(client=client, uuid=OFFERING_UUID)
    print("Getting first plan UUID from offering")
    plan_uuid = offering.plans[0].uuid
    resource_attributes = {
        "name": resource_name,
    }
    resource_limits = json.loads(RESOURCE_LIMITS)

    print("Submitting order")
    order_request = OrderCreateRequest(
        offering=offering_url,
        project=project_url,
        plan=str(plan_uuid),
        attributes=resource_attributes,
        limits=resource_limits,
        type_=RequestTypes.CREATE,
        accepting_terms_of_service=True
    )

    # Submit order
    order = marketplace_orders_create.sync(client=client, body=order_request)
    print(f"Order created successfully. Order UUID: {order.uuid}")

    print("Fetching order")
    create_order_uuid = order.uuid
    resource_uuid = order.marketplace_resource_uuid
    order = marketplace_orders_retrieve.sync(client=client, uuid=create_order_uuid)

    print("Approving order")
    marketplace_orders_approve_by_provider.sync_detailed(client=client, uuid=order.uuid)
    order = marketplace_orders_retrieve.sync(client=client, uuid=create_order_uuid)

    max_retries = 10
    retry_count = 0
    print("Waiting for order to be done")
    while order.state != OrderState.DONE and retry_count < max_retries:
        print(f"Order state: {order.state}")
        order = marketplace_orders_retrieve.sync(client=client, uuid=order.uuid)
        sleep(5)
        retry_count += 1

    if order.state != OrderState.DONE:
        print(f"Order execution timed out, state is {order.state}")
        exit(1)

    print("Order is done")

    print(f"Fetching marketplace provider resource with UUID: {resource_uuid}")
    resource = marketplace_provider_resources_retrieve.sync(client=client, uuid=resource_uuid)

    print(f'Resource state is {resource.state}')
    return resource

unique_id = uuid.uuid4().hex
resource_name = f"portal-test-{unique_id}"

project = get_or_create_project()
project_uuid = project.uuid

if PROJECT_CREDIT_AMOUNT is not None:
    get_or_create_project_credits()

resource = create_resource(resource_name)

if PI_EMAILS is not None:
    invite_PIs()

print("Execution finished")

print(resource.uuid)
```

### Script for usage pull

This script periodically pulls usage data of the remote resource and saves it locally.

```python
from waldur_api_client import AuthenticatedClient
from waldur_api_client.api.marketplace_component_usages import marketplace_component_usages_list
from os import environ
import datetime
import base64
import json
from uuid import UUID

client = AuthenticatedClient(
    base_url=environ["WALDUR_API_URL"],
    token=environ["WALDUR_API_TOKEN"],
    prefix="Token",
)
RESOURCE_UUID = UUID(environ["RESOURCE_BACKEND_ID"])

current_date = datetime.datetime.now()
month_start = datetime.datetime(day=1, month=current_date.month, year=current_date.year).date()

print(f"Fetching resource usages from {month_start.isoformat()}")
resource_usages = marketplace_component_usages_list.sync(
    client=client,
    resource_uuid=RESOURCE_UUID,
    date_after=month_start,
)

usages_data = []

for usage in resource_usages:
    usages_data.append(
        {
            "type": usage.type,
            "amount": usage.usage,
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
from waldur_api_client import AuthenticatedClient
from waldur_api_client.api.marketplace_resources import marketplace_resources_terminate
from waldur_api_client.api.marketplace_orders import marketplace_orders_approve_by_provider, marketplace_orders_retrieve
from waldur_api_client.models import OrderState
from os import environ
from time import sleep
from uuid import UUID

# Initialize the client
client = AuthenticatedClient(
    base_url=environ["WALDUR_API_URL"],
    token=environ["WALDUR_API_TOKEN"],
    prefix="Token",
)

# Get the resource UUID from environment
RESOURCE_UUID = UUID(environ["RESOURCE_BACKEND_ID"])

print('Creating resource termination order')

# Create termination order
order_uuid = marketplace_resources_terminate.sync(
    uuid=RESOURCE_UUID,
    client=client,
    body={}  # Empty body for termination request
)

print('Approving the order')
# Approve the order
marketplace_orders_approve_by_provider.sync_detailed(
    uuid=order_uuid,
    client=client
)

# Wait for order completion
max_retries = 10
retry_count = 0
print("Waiting for order to be done")
while retry_count < max_retries:
    order = marketplace_orders_retrieve.sync(
        uuid=order_uuid,
        client=client
    )
    print(f"Order state: {order.state}")
    if order.state == OrderState.DONE:
        break
    sleep(5)
    retry_count += 1

if retry_count >= max_retries:
    print(f"Order execution timed out, state is {order.state}")
    exit(1)
print('Order is done, resource is being terminated')
```

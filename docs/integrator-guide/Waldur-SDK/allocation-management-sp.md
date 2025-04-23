# Allocation Lifecycle Management by Service Provider

This page describes operations to be performed by service provider.

## Prerequisites

Please, read [initial setup for Waldur SDK](./waldur-sdk.md).

## Getting a list of users

`list_users` method is used to fetch all users in a Waldur instance.

```python
# The sync function from users_list module is used to fetch all users
from waldur_api_client.api.users import users_list

# Initialize your client first (per the SDK guide)
result = users_list.sync(client=client)

# The result will be a list of User objects with the following attributes:
# - url: str
# - uuid: UUID
# - username: str
# - slug: str
# - full_name: str
# - native_name: str
# - job_title: str
# - email: str
# - phone_number: str
# - organization: str
# - civil_number: str
# - description: str
# - is_staff: bool
# - is_active: bool
# - is_support: bool
# - token: str
# - token_lifetime: int
# - registration_method: str
# - date_joined: datetime
# - agreement_date: datetime
# - preferred_language: str
# - permissions: list[Permission]
# - requested_email: str
# - affiliations: Any
# - first_name: str
# - last_name: str
# - identity_provider_name: str
# - identity_provider_label: str
# - identity_provider_management_url: str
# - identity_provider_fields: list[str]
# - image: str
# - identity_source: str
# - has_active_session: bool
```

## Getting a list of SSH keys

`keys_list` method is used to fetch all SSH keys in Waldur.

```python
from waldur_api_client.api.keys import keys_list

# List all SSH keys
result = keys_list.sync(client=client)

# The result will be a list of SshKey objects with the following attributes:
# - url: str
# - uuid: UUID
# - name: str
# - public_key: str
# - fingerprint_md5: str
# - fingerprint_sha256: str
# - fingerprint_sha512: str
# - user_uuid: UUID
# - is_shared: bool
# - type_: str
```

## Getting a list of resource allocations

`marketplace_resources_list` method is used to fetch resources related to offerings, which belong to user's service provider.

Possible filter options for allocations (each one is optional):

- `provider_uuid` - UUID of a service provider organization;
- `state` - current state of a resource allocation; for valid values please use the associated enum values from MarketplaceResourcesListStateItem;
- `offering_uuid` - UUID of a related resource;
- `fields` - list of fields to return (can be passed as as strings or imported from `MarketplaceResourcesListFieldItem` enum, which includes fields like `name`, `offering`, `state`, `limits`, `plan`, `project`, `url`, and many others). Both examples are provided:

```python

from waldur_api_client.models.marketplace_resources_list_state_item import MarketplaceResourcesListStateItem
from waldur_api_client.models.marketplace_resources_list_field_item import MarketplaceResourcesListFieldItem
from waldur_api_client.api.marketplace_resources import marketplace_resources_list

result = marketplace_resources_list.sync(
    client=client,
    provider_uuid='<provider-uuid>',
    state=[MarketplaceResourcesListStateItem.CREATING],
    offering_uuid='<offering-uuid>',
    field=[
        MarketplaceResourcesListFieldItem.NAME,
        MarketplaceResourcesListFieldItem.STATE,
        MarketplaceResourcesListFieldItem.LIMITS,
        MarketplaceResourcesListFieldItem.PLAN,
        MarketplaceResourcesListFieldItem.PROJECT,
        MarketplaceResourcesListFieldItem.URL
    ]
)


# The result will be a list of Resource objects with the following fields:
# - name: str
# - offering: str
# - state: ResourceState
# - limits: ResourceLimits
# - plan: str
# - project: str
# - url: str
```

## Approving/rejecting allocation order by service provider

The service provider can either approve or reject order using
`marketplace_orders_approve_by_provider` and `marketplace_orders_reject_by_provider` correspondingly.
Both of these methods expect as its only argument UUID of an order for the allocation.

For example, a consumer requested an allocation using `Order` with `CREATE` type. After that, an empty allocation with `CREATING` state has appeared.
A service provider can change the state to `ok` (created successfully) using `marketplace_orders_approve_by_provider` or
`rejected` (creation rejected) using `marketplace_orders_reject_by_provider`.
In order to get a proper order, SP owner can use `marketplace_orders_list` method. This action is for order listing and supports filtering by state and allocation.

```python
from waldur_api_client.api.marketplace_orders import (
    marketplace_orders_approve_by_provider,
    marketplace_orders_reject_by_provider, 
    marketplace_orders_list,
    MarketplaceOrdersListStateItem
)
from waldur_api_client.models.marketplace_orders_list_state_item import MarketplaceOrdersListStateItem

# Service providers can approve or reject orders using:
marketplace_orders_approve_by_provider.sync(
    uuid="<order-uuid>",
    client=client
)
marketplace_orders_reject_by_provider.sync(
    uuid="<order-uuid>",
    client=client
)

# To retreive orders with state "executing" with a specific resource uuid
orders = marketplace_orders_list.sync(
    client=client,
    state=[MarketplaceOrdersListStateItem.EXECUTING],  # List of order states to filter by
    resource_uuid="<resource-uuid>"  # Optional filter by specific resource
)

# Example workflow:
# 1. Get pending orders
orders = marketplace_orders_list.sync(
    client=client,
    state=[MarketplaceOrdersListStateItem.EXECUTING]
)

# 2. Approve orders
for order in orders:
    marketplace_orders_approve_by_provider.sync(
        uuid=order.uuid,
        client=client
    )

# Available order states can be viewed in client's MarketplaceOrdersListStateItem, supported order states:
# - "canceled"
# - "done"
# - "erred"
# - "executing"
# - "pending-consumer"
# - "pending-project"
# - "pending-provider"
# - "rejected"
```

## Cancellation of orders for allocations

A consumer can also cancel created order and subsequently interrupt the requested operation over allocation.
For example, this option is suitable if the customer wants to cancel allocation deletion.
For this, `marketplace_orders_cancel` method should be used.
It changes the state of the order to `canceled`.
**NB**: this transition is possible only if the order's state is equal to `pending-consumer` or `pending-provider` and offering type is basic or support.

```python
from waldur_api_client.api.marketplace_orders import marketplace_orders_list, marketplace_orders_cancel
from waldur_api_client.models.marketplace_orders_list_state_item import MarketplaceOrdersListStateItem
from waldur_api_client.models.marketplace_orders_list_type_item import MarketplaceOrdersListTypeItem

# List orders
orders = marketplace_orders_list.sync(
    client=client,
    state=[MarketplaceOrdersListStateItem.EXECUTING],
    type_=[MarketplaceOrdersListTypeItem.TERMINATE]
)

order = orders[0]

result = marketplace_orders_cancel.sync_detailed(
    client=client,
    uuid=order.uuid
)
```

## Updating resource allocation with local reference (setting `backend_id` field)

Each allocation can have a link to a service provider's internal reference using `backend_id` field. Only users with service provider owner and manager roles can set this value using `marketplace_provider_resources_set_backend_id` method of the client. It requires the following arguments:

- **`uuid`** - UUID of a resource allocation;
- **`body`** - A request parameter of type `ResourceBackendIDRequest` that contains the `backend_id` field, which is the unique identifier of the resource in the external system.

```python
from waldur_api_client.api.marketplace_provider_resources import marketplace_provider_resources_set_backend_id
from waldur_api_client.models import ResourceBackendIDRequest

# Set backend ID for a resource
result = marketplace_provider_resources_set_backend_id.sync_detailed(
    uuid="resource-uuid",  # The UUID of the resource
    client=client,
    body=ResourceBackendIDRequest(
        backend_id="some-backend-id"  # The new backend ID
    )
)

# The response will contain a ResourceBackendID object with the updated backend_id
```

In case if SDK usage is not possible, HTTP request can be sent:

```http
POST <API-URL>/marketplace-resources/<resource-uuid>/

{
    "backend_id": "<some-backend-id>"
}

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

{
    "status": "Resource backend_id has been changed."
}
```

## Providing additional access detail for resource allocation

For additional details related to allocation access, `report` data is used.
In order to provide this information, owners and managers can use `marketplace_resource_submit_report` method. It requires the following arguments:

- **`uuid`** - UUID of a resource allocation;
- **`report`** - A list of `ReportSectionRequest` instances that is wrapped in a `ResourceReportRequest` object. Each `ReportSectionRequest` contains a header and body content. The `ResourceReportRequest` serves as a container for these report sections when submitting the report to the API.

```python
from waldur_api_client.models import ReportSectionRequest, ResourceReportRequest
from waldur_api_client.api.marketplace_provider_resources import marketplace_provider_resources_submit_report

report = [
    ReportSectionRequest(header="Header1", body="Body1"),
    ReportSectionRequest(header="Header2", body="Body2")
]

report_request = ResourceReportRequest(report=report)

result = marketplace_provider_resources_submit_report.sync(
    uuid="your-resource-uuid",
    body=report_request
)

# The result will be a ResourceReport object containing:
# - `report`: List of `ReportSection` objects, each with:
#   - `header`: The section header
#   - `body`: The section content
```

## Pagination

The Waldur API Client SDK supports pagination for list endpoints using `page` and `page_size` parameters.

## Example paginating API results

```python
from waldur_api_client.api.marketplace_provider_offerings import marketplace_provider_offerings_list

# Get first page with 10 items
result = marketplace_provider_offerings_list.sync(
    client=client,
    page=1,
    page_size=10
)
```

## Filtering API Response Fields Using Enum Types

The `marketplace_service_providers_list` endpoint allows you to specify which fields you want to retrieve from the service provider objects. This is done using the `field` parameter with enum values from `MarketplaceServiceProvidersListFieldItem`. The field parameter is present for different API endpoints to allow selective retrieval of specific fields from the response objects.

```python
from waldur_api_client.api.marketplace_service_providers import marketplace_service_providers_list
from waldur_api_client.models.marketplace_service_providers_list_field_item import (
    MarketplaceServiceProvidersListFieldItem,
)


# List service providers with specific fields
result = marketplace_service_providers_list.sync(
    client=client,
    field=[
        MarketplaceServiceProvidersListFieldItem.CUSTOMER_NAME,
        MarketplaceServiceProvidersListFieldItem.CUSTOMER_ABBREVIATION,
        MarketplaceServiceProvidersListFieldItem.DESCRIPTION,
        MarketplaceServiceProvidersListFieldItem.OFFERING_COUNT,
    ]
)
# Result will contain only the data for specified fields for each service provider.
```

## Getting a list of members in a project with active resource allocations

Service provider owners and managers can list project members using a resource allocation with `marketplace_resources_team_list` method.
It requires the following arguments:

- **`resource_uuid`** - UUID of a resource allocation.

```python
from waldur_api_client.api.marketplace_resources import marketplace_resources_team_list

# Get team members for a marketplace resource
team = marketplace_resources_team_list.sync(
    uuid="resource_uuid",
    client=client
)

# Each team member is a ProjectUser object with these fields:
# - url: str
# - uuid: UUID
# - username: str
# - full_name: str
# - role: str
# - expiration_time: Optional[datetime]
# - offering_user_username: Optional[str]
# - email: Optional[str]
```

## Reporting usage for a resource allocation

A usage of a resource allocation can be submitted by a corresponding service provider.
For this, the following methods are used:

- `marketplace_public_offerings_retrieve` - getting offering with components info. Arguments:
  - **`offering_uuid`** - UUID of an offering

- `marketplace_resources_plan_periods_list` - getting current plan periods for resource allocation. Arguments:
  - **`resource_uuid`** - UUID of a resource

- `marketplace_plan_components_list` - retrieves the list of components for a specific offering. Arguments:
  - **`offering_uuid`** - UUID of the offering to get components for
  - **`client`** - API client instance

- `marketplace_component_usages_set_usage` - creates or updates component usage for the current plan. Arguments:
  - **`body`** - parameter of type `ComponentUsageCreateRequest` containing:
    - **`resource_uuid`** - UUID of the resource
    - **`usages`** - list of `ComponentUsage` instances

```python
from waldur_api_client.api.marketplace_public_offerings import marketplace_public_offerings_retrieve
from waldur_api_client.api.marketplace_plan_components import marketplace_plan_components_list
from waldur_api_client.api.marketplace_component_usages import marketplace_component_usages_set_usage
from waldur_api_client.api.marketplace_resources import marketplace_resources_plan_periods_list
from waldur_api_client.models import ComponentUsageCreateRequest, ComponentUsageItemRequest 

# Get offering details
offering = marketplace_public_offerings_retrieve.sync(
    uuid='<offering-uuid>',
    client=client
)

# Get components
components = marketplace_plan_components_list.sync(
    offering_uuid='<offering-uuid>',
    client=client
)

# Create component usages
component_usages = [
    ComponentUsageItemRequest(
        type_=component.component_name,
        amount="10",
        description='Usage'
    )
    for component in components
]

# Submit usages
marketplace_component_usages_set_usage.sync(
    client=client,
    body=ComponentUsageCreateRequest(
        resource="<resource-uuid>,
        usages=component_usages
    )
)

# Get plan periods
plan_periods = marketplace_resources_plan_periods_list.sync(
    uuid='<resource-uuid>',
    client=client
)

# plan_periods:
# [{
#     'components': [{
#         'created': '2021-08-11T15:36:45.562440Z',
#         'date': '2021-08-11T15:37:30.556830Z',
#         'description': 'Usage',
#         'measured_unit': 'units',
#         'name': 'CPU',
#         'type_': 'cpu',
#         'usage': 10,
#         'uuid': 'some-uuid'
#     }],
#     'end': None,
#     'plan_name': 'sample-plan',
#     'plan_uuid': 'uuid',
#     'start': '2021-08-11T15:20:25.762775Z',
#     'uuid': 'uuid'
# }]


```

## Granting user access to resource

An access to a resource can be granted by service provider for a particular user with specification of username.
A result is represented by triplet [user, resource, username].
For this purpose, `marketplace_offering_users_create` should be invoked. This method requires the following arguments:

- `marketplace_offering_users_create` - creates a new offering user mapping. Arguments:
  - **`body`** - parameter of type `OfferingUserRequest` containing:
    - **`offering`** - URL of the target offering
    - **`user`** - URL of the target user
    - **`username`** - username to be associated with the user in the offering context

```python
from waldur_api_client.api.marketplace_offering_users import marketplace_offering_users_create
from waldur_api_client.models import OfferingUserRequest

# Create offering user
result = marketplace_offering_users_create.sync(
    client=client,
    body=OfferingUserRequest(
        user='<user-url>',
        offering='<offering-url>',
        username='<username>'
    )
)

# result => {
#  'created': '2021-08-12T15:22:18.993586Z',
#  'offering': 'offering_url',
#  'offering_name': 'offering_name',
#  'offering_uuid': '<offering-uuid>',
#  'user': 'user_url',
#  'user_uuid': '<user-uuid>',
#  'username': 'user_username'
# }
```

In case if SDK usage is not possible, HTTP request can be sent:

```http
POST <API-URL>/marketplace-offering-users/

{
    "offering": "<offering-url>",
    "user": "<user-url>",
    "username": "<username>"
}

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

{
    "created": "2021-08-12T15:22:18.993586Z",
    "offering": "offering_url",
    "offering_name": "offering_name",
    "offering_uuid": "<offering-uuid>",
    "user": "user_url",
    "user_uuid": "<user-uuid>",
    "username": "user_username"
}
```

## Granting user access to corresponding resources in batch manner

A service provider can grant access mentioned in the previous section to all resources used in projects including a target user.
For such access creation or update, `marketplace_service_providers_set_offerings_username` is used.
The method requires the following arguments:

- `marketplace_service_providers_set_offerings_username` - sets or updates the username for a user across all offerings of a service provider. Arguments:
  - **`uuid`** - UUID of the service provider
  - **`body`** - parameter of type `SetOfferingsUsernameRequest` containing:
    - **`user_uuid`** - UUID of the target user
    - **`username`** - new username to be set for the user across all offerings

```python
from waldur_api_client.api.marketplace_service_providers import marketplace_service_providers_set_offerings_username
from waldur_api_client.models import SetOfferingsUsernameRequest

result = marketplace_service_providers_set_offerings_username.sync(
    uuid='<service-provider-uuid>',
    client=client,
    body=SetOfferingsUsernameRequest(
        user_uuid=UUID('<user-uuid>'),
        username='<username>'
    )
)
# result =>  {
#  'detail': 'Offering users have been set.'
# }
```

## Getting service provider for an organization

A user can get service provider details
using `marketplace_service_providers_list` with corresponding filter.
This method is guaranteed to return a list with at most one service provider record.

```python
from waldur_api_client.api.marketplace_service_providers import marketplace_service_providers_list
from waldur_api_client.models.marketplace_service_providers_list_field_item import MarketplaceServiceProvidersListFieldItem

# List service providers
result = marketplace_service_providers_list.sync(
    client=client,
    customer_uuid="uuid"
)

# Result will be a list of ServiceProvider objects with fields:

# 'created': '2021-09-24T13:42:05.448269Z'
# 'customer': '<customer>'
# 'customer_abbreviation': '<customer_abbreviation>'
# 'customer_country': '<customer_country>'
# 'customer_image': '<customer_image_url>'
# 'customer_name': '<customer_name>'
# 'customer_native_name': '<customer_native_name>'
# 'customer_slug': '<customer_slug>'
# 'customer_uuid': '<customer_uuid>'
# 'description': '<description>'
# 'image': '<image_url>'
# 'offering_count': 5
# 'organization_groups': []  
# 'url': '<service_provider_url>'
# 'uuid': '<service_provider_uuid>'
```

## Listing users of service provider's resources

A service provider owner can list users currently using its resources.
For this, `marketplace_service_providers_users_list` should be used. It accepts **service_provider_uuid**,
which can be fetched using `marketplace_service_providers_list`.

- `marketplace_service_providers_users_list` - retrieves a list of users associated with a service provider's resources. Arguments:
  - **`service_provider_uuid`** - UUID of the service provider
  - **`client`** - API client instance

```python
from waldur_api_client.api.marketplace_service_providers import marketplace_service_providers_users_list
from waldur_api_client.api.marketplace_service_providers import marketplace_service_providers_list


# First, get the service provider UUID (as shown in your example)
service_providers = marketplace_service_providers_list.sync(
    client=client,
    customer_uuid="<customer_uuid>"
)
service_provider = service_providers[0]
service_provider_uuid = service_provider.uuid

# List users of the service provider
result = marketplace_service_providers_users_list.sync(
    service_provider_uuid=service_provider_uuid,
    client=client,
)

# The response will be a list of MarketplaceServiceProviderUser objects with fields:
# uuid: UUID
# username: str
# full_name: str
# first_name: str
# last_name: str
# organization: str
# email: str
# phone_number: str
# projects_count: int
# registration_method: str
# affiliations: Any
# is_active: bool
# additional_properties: dict[str, Any]
```

## Listing ssh key for users of service provider's resources

A service provider owner can list ssh keys of users currently using its resources.
For this, `list_service_provider_ssh_keys` should be used. It accepts **service_provider_uuid**,
which can be fetched using `marketplace_service_providers_list`.

- `marketplace_service_providers_keys_list` - retrieves a list of SSH keys associated with users of a service provider's resources. Arguments:
  - **`service_provider_uuid`** - UUID of the service provider
  - **`client`** - API client instance

```python
from waldur_api_client.api.marketplace_service_providers import (
    marketplace_service_providers_list,
    marketplace_service_providers_keys_list,
)
service_providers = marketplace_service_providers_list.sync(
    client=client,
    customer_uuid="<customer_uuid>"
)
service_provider = service_providers[0]
service_provider_uuid = service_provider.uuid

# List SSH keys of service provider users
result = marketplace_service_providers_keys_list.sync(
    service_provider_uuid=service_provider_uuid,
    client=client,
)

# Reulst will be a list of SshKey objects with fields:
# url: str
# uuid: UUID
# name: str
# public_key: str
# fingerprint_md5: str
# fingerprint_sha256: str
# fingerprint_sha512: str
# user_uuid: UUID
# is_shared: bool
# type_: str

```

## Listing projects with service provider's resources

A service provider owner can list all projects, which have its resources.
For this, `list_service_provider_projects` should be used. It accepts **service_provider_uuid**,
which can be fetched using `marketplace_service_providers_list`.

```python
from waldur_api_client.api.marketplace_service_providers import (
    marketplace_service_providers_list,
    marketplace_service_providers_projects_list,
)

service_providers = marketplace_service_providers_list.sync(
    client=client,
    customer_uuid="<customer_uuid>"
)
service_provider = service_providers[0]
service_provider_uuid = service_provider.uuid

projects = marketplace_service_providers_projects_list.sync(
    service_provider_uuid=service_provider_uuid,
    client=client,
)

# url: str
# uuid: UUID
# name: str
# slug: str
# customer: str
# customer_uuid: UUID
# customer_name: str
# customer_slug: str
# customer_native_name: str
# customer_abbreviation: str
# description: str
# created: datetime.datetime
# type_: str
# type_name: str
# type_uuid: UUID
# backend_id: str
# start_date: datetime.date
# end_date: datetime.date
# end_date_requested_by: str
# oecd_fos_2007_code: OecdFos2007CodeEnum
# oecd_fos_2007_label: str
# is_industry: bool
# image: str
# resources_count: int
# project_credit: float
# marketplace_resource_count: ProjectMarketplaceResourceCount
# billing_price_estimate: NestedPriceEstimate
```

## Listing project permissions in projects using service provider's resources

A service provider owner can also list all active projects permissions in projects, which have its resources.
For this, `marketplace_service_providers_project_permissions_list` should be used. It accepts **service_provider_uuid**,
which can be fetched using `marketplace_service_providers_list`.

```python
from waldur_api_client.api.marketplace_service_providers import (
    marketplace_service_providers_list,
    marketplace_service_providers_project_permissions_list,
)

service_providers = marketplace_service_providers_list.sync(
    client=client,
    customer_uuid="<customer_uuid>"
)
service_provider = service_providers[0]
service_provider_uuid = service_provider.uuid

permissions = marketplace_service_providers_project_permissions_list.sync(
    service_provider_uuid=service_provider_uuid,
    client=client
)

# created: datetime.datetime
# expiration_time: datetime.datetime | None
# created_by: str | None
# created_by_full_name: str
# created_by_username: str
# project: str
# project_uuid: UUID
# project_name: str
# project_created: datetime.datetime
# project_end_date: datetime.datetime
# customer_uuid: UUID
# customer_name: str
# role: str
# role_name: str
# user: str
# user_full_name: str
# user_native_name: str
# user_username: str
# user_uuid: UUID
# user_email: str
```

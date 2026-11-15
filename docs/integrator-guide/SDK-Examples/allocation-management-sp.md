# Allocation Lifecycle Management by Service Provider

This page describes operations to be performed by service provider.

## Prerequisites

Please, read [initial setup for Waldur SDK](../sdk.md). Every example below expects a `client` created as described
there, with the token of a user who is an owner or manager of the service provider's organization.

Values in angle brackets, such as `<resource-uuid>`, are placeholders for your own identifiers.
The fields of the returned objects are the attributes of the corresponding model class in
`waldur_api_client.models`, for example `User`, `SshKey` or `Resource`.

## Getting a list of users

`users_list` is used to fetch the users visible to the caller. `sync_all` follows the pagination and returns every page.

```python
from waldur_api_client.api.users import users_list

users = users_list.sync_all(client=client)
for user in users:
    print(user.username, user.email)
```

## Getting a list of SSH keys

```python
from waldur_api_client.api.keys import keys_list

keys = keys_list.sync_all(client=client)
for key in keys:
    print(key.name, key.fingerprint_sha256)
```

## Getting a list of resource allocations

To get a list of all the resources (allocations) of a service provider, use `marketplace_resources_list`.
`sync_all` follows the pagination and returns every page. It accepts the following filters:

- `provider_uuid` - UUID of the service provider's organization;
- `state` - list of resource states, from the `ResourceState` enum;
- `offering_uuid` - list of offering UUIDs;
- `field` - list of fields to return, from the `ResourceFieldEnum` enum. Without it, every field is returned.

```python
from waldur_api_client.api.marketplace_resources import marketplace_resources_list
from waldur_api_client.models import ResourceFieldEnum, ResourceState

resources = marketplace_resources_list.sync_all(
    client=client,
    provider_uuid="<provider-uuid>",
    state=[ResourceState.CREATING, ResourceState.OK],
    offering_uuid=["<offering-uuid>"],
    field=[
        ResourceFieldEnum.UUID,
        ResourceFieldEnum.NAME,
        ResourceFieldEnum.STATE,
        ResourceFieldEnum.LIMITS,
        ResourceFieldEnum.PLAN,
        ResourceFieldEnum.PROJECT,
    ],
)
for resource in resources:
    print(resource.uuid, resource.name, resource.state)
```

## Approving/rejecting allocation order by service provider

When a consumer requests an allocation, Waldur creates an `Order` of type `CREATE`, and the allocation appears in
`CREATING` state. For an offering that requires the provider's approval, the order waits in `pending-provider` state.
The service provider then either approves it with `marketplace_orders_approve_by_provider`, or rejects it with
`marketplace_orders_reject_by_provider`.

To find orders, use `marketplace_orders_list`. It can filter by `state` (from the `OrderState` enum), by `type_`
(from the `RequestTypes` enum), by `provider_uuid` and by `resource_uuid`.

```python
from waldur_api_client.api.marketplace_orders import (
    marketplace_orders_approve_by_provider,
    marketplace_orders_list,
    marketplace_orders_reject_by_provider,
)
from waldur_api_client.models import (
    OrderApproveByProviderRequest,
    OrderProviderRejectionRequest,
    OrderState,
)

# Orders of this provider that wait for its decision
orders = marketplace_orders_list.sync_all(
    client=client,
    provider_uuid="<provider-uuid>",
    state=[OrderState.PENDING_PROVIDER],
)

# Approve the first order
if len(orders) > 0:
    marketplace_orders_approve_by_provider.sync(
        uuid=orders[0].uuid,
        client=client,
        body=OrderApproveByProviderRequest(),
    )

# Reject the second one, with an optional explanation for the consumer
if len(orders) > 1:
    marketplace_orders_reject_by_provider.sync_detailed(
        uuid=orders[1].uuid,
        client=client,
        body=OrderProviderRejectionRequest(
            provider_rejection_comment="Not enough capacity this quarter",
        ),
    )
```

## Cancellation of orders for allocations

A consumer can also cancel an order and so interrupt the requested operation, for example a request to terminate
an allocation. For this, use `marketplace_orders_cancel`. It changes the state of the order to `canceled`.

**NB**: this is possible only while the order is in `pending-consumer` or `pending-provider` state, and only for
offerings of type basic or support.

```python
from waldur_api_client.api.marketplace_orders import (
    marketplace_orders_cancel,
    marketplace_orders_list,
)
from waldur_api_client.models import OrderState, RequestTypes

orders = marketplace_orders_list.sync_all(
    client=client,
    state=[OrderState.PENDING_CONSUMER, OrderState.PENDING_PROVIDER],
    type_=[RequestTypes.TERMINATE],
)

for order in orders:
    response = marketplace_orders_cancel.sync_detailed(
        uuid=order.uuid,
        client=client,
    )
    print(order.uuid, response.status_code)
```

## Updating resource allocation with local reference (setting `backend_id` field)

Each allocation can have a link to a service provider's internal reference using `backend_id` field.
Only users with service provider owner and manager roles can set it, with
`marketplace_provider_resources_set_backend_id`. It requires the following arguments:

- **`uuid`** - UUID of a resource allocation;
- **`body`** - a `ResourceBackendIDRequest` with the `backend_id` field: the identifier of the resource in the
  external system.

```python
from waldur_api_client.api.marketplace_provider_resources import (
    marketplace_provider_resources_set_backend_id,
)
from waldur_api_client.models import ResourceBackendIDRequest

result = marketplace_provider_resources_set_backend_id.sync(
    uuid="<resource-uuid>",
    client=client,
    body=ResourceBackendIDRequest(backend_id="<some-backend-id>"),
)
print(result.status)
```

In case if SDK usage is not possible, HTTP request can be sent:

```http
POST <API-URL>/api/marketplace-provider-resources/<resource-uuid>/set_backend_id/

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
In order to provide this information, owners and managers can use `marketplace_provider_resources_submit_report`.
It requires the following arguments:

- **`uuid`** - UUID of a resource allocation;
- **`body`** - a `ResourceReportRequest` with a `report`: a list of `ReportSectionRequest` objects, each with a
  `header` and a `body`.

```python
from waldur_api_client.api.marketplace_provider_resources import (
    marketplace_provider_resources_submit_report,
)
from waldur_api_client.models import ReportSectionRequest, ResourceReportRequest

result = marketplace_provider_resources_submit_report.sync(
    uuid="<resource-uuid>",
    client=client,
    body=ResourceReportRequest(
        report=[
            ReportSectionRequest(header="Login node", body="ssh login.example.com"),
            ReportSectionRequest(header="Support", body="support@example.com"),
        ]
    ),
)
print(result.status)
```

## Pagination

List endpoints return one page at a time. The page is selected with the `page` and `page_size` parameters;
`sync_all` follows the pagination and returns every page.

```python
from waldur_api_client.api.marketplace_provider_offerings import (
    marketplace_provider_offerings_list,
)

# The first page, with 10 items
first_page = marketplace_provider_offerings_list.sync(
    client=client,
    page=1,
    page_size=10,
)

# Every offering, page by page
offerings = marketplace_provider_offerings_list.sync_all(client=client)
```

## Filtering API Response Fields Using Enum Types

Most list and retrieve endpoints accept a `field` parameter that selects which fields of each object are returned.
The allowed values are an enum named after the model, for example `ServiceProviderFieldEnum` for
`marketplace_service_providers_list`. Fields that were not requested are left unset on the returned objects.

```python
from waldur_api_client.api.marketplace_service_providers import (
    marketplace_service_providers_list,
)
from waldur_api_client.models import ServiceProviderFieldEnum

service_providers = marketplace_service_providers_list.sync(
    client=client,
    field=[
        ServiceProviderFieldEnum.CUSTOMER_NAME,
        ServiceProviderFieldEnum.CUSTOMER_ABBREVIATION,
        ServiceProviderFieldEnum.DESCRIPTION,
        ServiceProviderFieldEnum.OFFERING_COUNT,
    ],
)
for service_provider in service_providers:
    print(service_provider.customer_name, service_provider.offering_count)
```

## Getting a list of members in a project with active resource allocations

Service provider owners and managers can list the members of the project that uses a resource allocation,
with `marketplace_resources_team_list`. It requires the UUID of the resource allocation.

```python
from waldur_api_client.api.marketplace_resources import marketplace_resources_team_list

team = marketplace_resources_team_list.sync(
    uuid="<resource-uuid>",
    client=client,
)
for member in team:
    print(member.username, member.role, member.offering_user_username)
```

## Reporting usage for a resource allocation

A usage of a resource allocation can be submitted by a corresponding service provider.
For this, the following methods are used:

- `marketplace_public_offerings_retrieve` - gets the offering, including its components. Each component's `type_`
  identifies it when reporting usage.
- `marketplace_component_usages_set_usage` - creates or updates the usage of the components for the current
  billing period. Its `body` is a `ComponentUsageCreateRequest` with:
    - **`resource`** - UUID of the resource;
    - **`usages`** - a list of `ComponentUsageItemRequest` objects, each with the component `type_`, the `amount`
      and an optional `description`.
- `marketplace_resources_plan_periods_list` - gets the plan periods of the resource, with the usages reported in
  each.

Usage can be reported only for components whose billing type is `usage`.

```python
from waldur_api_client.api.marketplace_component_usages import (
    marketplace_component_usages_set_usage,
)
from waldur_api_client.api.marketplace_public_offerings import (
    marketplace_public_offerings_retrieve,
)
from waldur_api_client.api.marketplace_resources import (
    marketplace_resources_plan_periods_list,
)
from waldur_api_client.models import (
    BillingTypeEnum,
    ComponentUsageCreateRequest,
    ComponentUsageItemRequest,
)

offering = marketplace_public_offerings_retrieve.sync(
    uuid="<offering-uuid>",
    client=client,
)

usages = [
    ComponentUsageItemRequest(
        type_=component.type_,
        amount="10",
        description="Usage reported by the provider",
    )
    for component in offering.components
    if component.billing_type == BillingTypeEnum.USAGE
]

response = marketplace_component_usages_set_usage.sync_detailed(
    client=client,
    body=ComponentUsageCreateRequest(
        resource="<resource-uuid>",
        usages=usages,
    ),
)
print(response.status_code)

plan_periods = marketplace_resources_plan_periods_list.sync(
    uuid="<resource-uuid>",
    client=client,
)
for period in plan_periods:
    for usage in period.components:
        print(period.plan_name, usage.type_, usage.usage)
```

## Granting user access to resource

An access to a resource can be granted by service provider for a particular user with specification of username.
A result is represented by triplet [user, resource, username].
For this purpose, `marketplace_offering_users_create` is used. Its `body` is an `OfferingUserRequest` with:

- **`offering_uuid`** - UUID of the target offering
- **`user_uuid`** - UUID of the target user
- **`username`** - username of the user in the offering

Instead of the UUIDs, `offering` and `user` accept the URLs of the offering (`/api/marketplace-provider-offerings/<uuid>/`)
and of the user.

```python
from waldur_api_client.api.marketplace_offering_users import (
    marketplace_offering_users_create,
)
from waldur_api_client.models import OfferingUserRequest

offering_user = marketplace_offering_users_create.sync(
    client=client,
    body=OfferingUserRequest(
        offering_uuid="<offering-uuid>",
        user_uuid="<user-uuid>",
        username="<username>",
    ),
)
print(offering_user.uuid, offering_user.username, offering_user.state)
```

In case if SDK usage is not possible, HTTP request can be sent:

```http
POST <API-URL>/api/marketplace-offering-users/

{
    "offering_uuid": "<offering-uuid>",
    "user_uuid": "<user-uuid>",
    "username": "<username>"
}

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

{
    "uuid": "<offering-user-uuid>",
    "offering": "<offering-url>",
    "offering_uuid": "<offering-uuid>",
    "offering_name": "<offering-name>",
    "user": "<user-url>",
    "user_uuid": "<user-uuid>",
    "username": "<username>",
    ...
}
```

## Granting user access to corresponding resources in batch manner

A service provider can grant the access described in the previous section to all of its offerings that a user's
projects use, in one call: `marketplace_service_providers_set_offerings_username`. It creates the offering users
that are missing and updates the username of the existing ones. It requires the following arguments:

- **`uuid`** - UUID of the service provider
- **`body`** - a `SetOfferingsUsernameRequest` with:
    - **`user_uuid`** - UUID of the target user
    - **`username`** - username to set for the user in all offerings of the service provider

```python
from waldur_api_client.api.marketplace_service_providers import (
    marketplace_service_providers_set_offerings_username,
)
from waldur_api_client.models import SetOfferingsUsernameRequest

response = marketplace_service_providers_set_offerings_username.sync_detailed(
    uuid="<service-provider-uuid>",
    client=client,
    body=SetOfferingsUsernameRequest(
        user_uuid="<user-uuid>",
        username="<username>",
    ),
)
print(response.status_code, response.content)
# 201 b'{"detail":"Offering users have been set."}'
```

## Getting service provider for an organization

A user can get service provider details using `marketplace_service_providers_list` with the `customer_uuid` filter.
An organization has at most one service provider, so the list has at most one item.

```python
from waldur_api_client.api.marketplace_service_providers import (
    marketplace_service_providers_list,
)

service_providers = marketplace_service_providers_list.sync(
    client=client,
    customer_uuid="<customer-uuid>",
)
service_provider = service_providers[0]
print(service_provider.uuid, service_provider.customer_name, service_provider.offering_count)
```

The examples below take the service provider UUID from this call.

## Listing users of service provider's resources

A service provider owner can list users currently using its resources,
with `marketplace_service_providers_users_list`.

```python
from waldur_api_client.api.marketplace_service_providers import (
    marketplace_service_providers_users_list,
)

users = marketplace_service_providers_users_list.sync(
    service_provider_uuid="<service-provider-uuid>",
    client=client,
)
for user in users:
    print(user.username, user.full_name, user.email, user.projects_count)
```

## Listing ssh key for users of service provider's resources

A service provider owner can list ssh keys of users currently using its resources,
with `marketplace_service_providers_keys_list`.

```python
from waldur_api_client.api.marketplace_service_providers import (
    marketplace_service_providers_keys_list,
)

keys = marketplace_service_providers_keys_list.sync(
    service_provider_uuid="<service-provider-uuid>",
    client=client,
)
for key in keys:
    print(key.user_uuid, key.name, key.public_key)
```

## Listing projects with service provider's resources

A service provider owner can list all projects, which have its resources,
with `marketplace_service_providers_projects_list`.

```python
from waldur_api_client.api.marketplace_service_providers import (
    marketplace_service_providers_projects_list,
)

projects = marketplace_service_providers_projects_list.sync(
    service_provider_uuid="<service-provider-uuid>",
    client=client,
)
for project in projects:
    print(project.uuid, project.name, project.customer_name)
```

## Listing project permissions in projects using service provider's resources

A service provider owner can also list all active projects permissions in projects, which have its resources,
with `marketplace_service_providers_project_permissions_list`.

```python
from waldur_api_client.api.marketplace_service_providers import (
    marketplace_service_providers_project_permissions_list,
)

permissions = marketplace_service_providers_project_permissions_list.sync(
    service_provider_uuid="<service-provider-uuid>",
    client=client,
)
for permission in permissions:
    print(permission.project_name, permission.user_username, permission.role_name)
```

## Creating Offerings

Service providers can create new offerings using the Waldur SDK. The following example demonstrates how to create a new offering with components and plans.

```python
import os
import uuid
from typing import Union
from uuid import UUID

from waldur_api_client import AuthenticatedClient
from waldur_api_client.api.customers import customers_list, customers_retrieve
from waldur_api_client.api.marketplace_categories import (
    marketplace_categories_list,
    marketplace_categories_retrieve,
)
from waldur_api_client.api.marketplace_provider_offerings import (
    marketplace_provider_offerings_activate,
    marketplace_provider_offerings_create,
)
from waldur_api_client.errors import UnexpectedStatus
from waldur_api_client.models import (
    BaseProviderPlanRequest,
    BillingTypeEnum,
    BillingUnit,
    CountryEnum,
    Customer,
    LimitPeriodEnum,
    MarketplaceCategory,
    OfferingComponentRequest,
    OfferingCreateRequest,
)


def is_uuid_like(value: Union[str, UUID]) -> bool:
    """Check if value looks like a valid UUID."""
    if isinstance(value, UUID):
        return True
    try:
        uuid.UUID(str(value))
    except (TypeError, ValueError, AttributeError):
        return False
    return True


def get_category(
    client: AuthenticatedClient, category_identifier: Union[str, UUID]
) -> MarketplaceCategory:
    """Get category object from identifier (title or UUID)."""
    if is_uuid_like(category_identifier):
        return marketplace_categories_retrieve.sync(
            client=client, uuid=UUID(str(category_identifier))
        )
    categories = marketplace_categories_list.sync(
        client=client, title=category_identifier
    )
    if not categories:
        raise ValueError(f"Category with title '{category_identifier}' not found")
    return categories[0]


def get_provider(
    client: AuthenticatedClient, provider_identifier: Union[str, UUID]
) -> Customer:
    """Get provider (customer) object from identifier (name or UUID)."""
    if is_uuid_like(provider_identifier):
        return customers_retrieve.sync(
            client=client, uuid=UUID(str(provider_identifier))
        )
    providers = customers_list.sync(client=client, name=provider_identifier)
    if not providers:
        raise ValueError(f"Provider with name '{provider_identifier}' not found")
    return providers[0]


def create_offering(
    client: AuthenticatedClient,
    provider_identifier: Union[str, UUID],
    category_identifier: Union[str, UUID],
    name: str,
    type_: str,
    **kwargs,
) -> UUID:
    """
    Create a new offering for an organization.

    Required arguments:
        client: Authenticated client instance
        provider_identifier: Provider name or UUID
        category_identifier: Category title or UUID
        name: Name of the offering
        type_: Type of the offering

    Optional arguments (pass as kwargs) are the other fields of
    OfferingCreateRequest, for example description, full_description,
    terms_of_service, access_url, shared, billable, country, components
    and plans.
    """
    provider = get_provider(client, provider_identifier)
    category = get_category(client, category_identifier)

    offering = marketplace_provider_offerings_create.sync(
        client=client,
        body=OfferingCreateRequest(
            name=name,
            category=category.url,
            type_=type_,
            customer=provider.url,
            **kwargs,
        ),
    )
    return offering.uuid


# Example usage:
if __name__ == "__main__":
    # Requires the waldur-api-client package and two environment variables:
    # WALDUR_API_URL=https://waldur.example.com
    # WALDUR_API_TOKEN=<your token, of a user with access to the organization>
    api_url = os.getenv("WALDUR_API_URL")
    api_token = os.getenv("WALDUR_API_TOKEN")

    if not api_url or not api_token:
        print(
            "Required environment variables not set. Please set WALDUR_API_URL and WALDUR_API_TOKEN"
        )
        raise SystemExit(1)

    client = AuthenticatedClient(base_url=api_url, token=api_token)

    # A component billed by usage, with a monthly limit
    component = OfferingComponentRequest(
        type_="cpu",
        name="CPU",
        measured_unit="hours",
        billing_type=BillingTypeEnum.USAGE,
        limit_period=LimitPeriodEnum.MONTH,
        limit_amount=1000,
    )

    plan = BaseProviderPlanRequest(
        name="Basic Plan",
        unit_price="10",
        unit=BillingUnit.MONTH,
    )

    try:
        offering_uuid = create_offering(
            client=client,
            provider_identifier="My Org Name",  # The organization name or UUID
            category_identifier="HPC",  # The category title or UUID
            name="New Offering",
            type_="Marketplace.Basic",
            description="Offering description",
            components=[component],
            plans=[plan],
            shared=True,
            billable=True,
            country=CountryEnum.FR,
        )
        print(f"Created offering with UUID: {offering_uuid}")

        # A new offering is a draft until it is activated
        marketplace_provider_offerings_activate.sync(
            client=client,
            uuid=offering_uuid,
        )
        print(f"Offering activated with UUID: {offering_uuid}")
    except (UnexpectedStatus, ValueError) as e:
        print(f"Error: {e}")
```

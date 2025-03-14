# REST API

## Authentication

Waldur uses token-based authentication for REST.

In order to authenticate your requests first obtain token from any of
the supported token backends. Then use the token in all the subsequent
requests putting it into `Authorization` header:

``` http
GET /api/projects/ HTTP/1.1
Accept: application/json
Authorization: Token c84d653b9ec92c6cbac41c706593e66f567a7fa4
Host: example.com
```

Also token can be put as request GET parameter, with key `x-auth-token`:

``` http
GET /api/?x-auth-token=Token%20144325be6f45e1cb1a4e2016c4673edaa44fe986 HTTP/1.1
Accept: application/json
Host: example.com
```

## API version

In order to retrieve current version of the Waldur authenticated user
should send a GET request to **/api/version/**.

Valid request example (token is user specific):

``` http
GET /api/version/ HTTP/1.1
Content-Type: application/json
Accept: application/json
Authorization: Token c84d653b9ec92c6cbac41c706593e66f567a7fa4
Host: example.com
```

Valid response example:

``` http
HTTP/1.0 200 OK
Content-Type: application/json
Vary: Accept
Allow: OPTIONS, GET

{
    "version": "0.3.0"
}
```

## Pagination

Every Waldur REST request supports pagination. Links to the next,
previous, first and last pages are included in the Link header.
*X-Result-Count* contains a count of all entries in the response set.

By default page size is set to 10. Page size can be modified by passing
**?page_size=N** query parameter. The maximum page size is 100.

Example of the header output for user listing:

``` http
HTTP/1.0 200 OK
Vary: Accept
Content-Type: application/json
Link:
 <http://example.com/api/users/?page=1>; rel="first",
 <http://example.com/api/users/?page=3>; rel="next",
 <http://example.com/api/users/?page=1>; rel="prev",
 <http://example.com/api/users/?page=6>; rel="last"
X-Result-Count: 54
Allow: GET, POST, HEAD, OPTIONS
```

## Common operations

If you are integrating a python-based application, you might find useful a [python wrapper](../waldur-sdk.md) for typical operations.

Almost all operations require authentication. Authentication process is a two-step:

1. Generation of authentication token using [Authentication API](authentication.md).
2. Passing that token in the Authorization header along with all other REST API calls.

Please note that all of the responses to the listing are paginated, by default up to 10 elements are returned.
You can request more by passing `page_size=<number>` argument, number up to 200 will be respected. Information
about the whole set is contained in the response headers. Check [example of a "get_all" function](https://github.com/waldur/ansible-waldur-module/blob/6679b6b8f9ca21099eb3a6cb97e846d3e8dd1249/waldur_client.py#L140)
to see how a full traversal can be done.

## Project management

### Customer lookup

Waldur implements a multi-tenant model to allow different organizations to allocate shared resources simultaneously
and independently from each other. Each such organizaton is a customer of Waldur and is able to create its own
projects. Project allows us to create new allocations as well as connect users with the project.

Hence, to create a project, one needs first to have a reference to the customer. The reference is a stable one and
can be cached by a REST API client.

Examples:

- [API call for customer lookup](project-api-examples.md#lookup-allocator-customers-available-to-a-user)

### Project creation

In order to create a new project in an organization, user needs to provide the following fields:

- **`customer`** - URL of the project's organization
- **`name`** - project's name
- `description` - description of a project description
- `end_date` - optional date when the project and all allocations it contains will be scheduled for termination.
- `backend_id` - optional identifier, which is intended to be unique in the resource allocator's project list. Can be used for connecting Waldur projects with the client's project registry.
- `oecd_fos_2007_code` - optional OECD Field of Science code. A code is represented by a string with two numbers separated by dot for a corresponding field of science. For example `"1.1"` is code for Mathematics. More information can be found [here](https://joinup.ec.europa.eu/collection/eu-semantic-interoperability-catalogue/solution/field-science-and-technology-classification/about).

Please note that the project becomes active at the moment of creation!

Examples:

- [API call for project creation](project-api-examples.md#create-a-new-project)
- [Project creation in Waldur](https://github.com/waldur/waldur-mastermind/blob/54689ac472b1a07fa815a5ddebcf35ea888d3dcc/src/waldur_mastermind/marketplace_remote/utils.py#L122).

### Project update

It is possible to update an existing project using its URL link. Name, description and backend_id can be updated.

Examples:

- [API call for project update](project-api-examples.md#update-an-existing-project)

### Project lookup

User can list projects and filter them using the following query parameters:

- `name` - project's name (uses 'contains' logic for lookup)
- `name_exact` - project's exact name
- `description` - project's description (uses 'contains' logic for lookup)
- `backend_id` - project's exact backend ID

In case API user has access to more than one customer, extra filter by customer properties can be added:

- `customer` - exact filter by customer UUID
- `customer_name` - filter by partial match of the full name of a customer
- `abbreviation` - filter by partial match of the abbreviation of a customer

Examples:

- [API call for listing  of projects](project-api-examples.md#list-projects))

## Project membership management

Creating a membership for a user means creating a permission link. While multiple roles of a user per project are allowed,
we recommed for clarity to have one active project role per user in a project.

The list of fields for creation are:

- `user` - a user's UUID, looked up from a previous step.
- `role` - a role of the user. Both role UUID and name are supported. By default the system roles 'PROJECT.MEMBER', 'PROJECT.ADMIN' and 'PROJECT.MANAGER' are supported. TODO: add reference to Puhuri terminology.
- `expiration_time` - an optional field, if provided, it should contain date or ISO 8601 datetime.

To remove the permission, REST API client needs to send a HTTP request using the same payload as for permission creation,
but to `delete_user` endpoint .

It is also possible to list available project permissions along with a `role` filter.

Examples:

- [API call for allocating members to a project](project-api-examples.md#project-members-permissions-allocation)
- [API call for removing members from a project](project-api-examples.md#removal-of-members-from-a-project)
- [API call to listing project permissions](project-api-examples.md#list-project-permissions)

## Resource allocation management

Creating and managing resource allocations in Waldur follows ordering logic.

All operations on resources, which lead to changes in allocations - e.g. creation, modification of allocated limits
or termination - are wrapped in an order.

### Listing offerings

To create a new Allocation, one must first choose a specific Offering from available. Offering corresponds to a specific
part of a shared resource that Resource Allocator can allocate. Offerings can be visible to multiple allocators, however in the first iteration we plan to limit allocators with
access to only their owned shares.

User can fetch offerings and filter them by the following fields:

- `name` - offering's name
- `name_exact` - offering's exact name
- `customer` - organization's URL
- `customer_uuid` - organization's UUID

Generally Offering has a stable UUID, which can be used in Waldur client configuration. Offering defines inputs
that are required to provision an instance of the offering, available accounting plans (at least one should be present)
as well as attributes that can or should be provided with each request.

Each Offering contains one or more plans, you will need to provide a reference (URL) to the plan when creating an
allocation.

API examples:

- [Getting a list of offerings available for allocation](project-api-examples.md#getting-a-list-of-offerings)

### Orders and resources

To create a new allocation, an order must be created with requested attributes: project
as well as details about the allocations.

Order might require additional approvals - in this case upon creation its status will be `pending-consumer` or `pending-provider`, which
can transition to `REJECTED` if order is rejected.
Otherwise it will be switched to `EXECUTING`, ending either in `DONE` if all is good or `ERRED`, if error happens during the processing.

Resource UUID is available as a `marketplace_resource_uuid` field of the creation order.

In addition, ``accepting_terms_of_service`` flag must be provided as a lightweight confirmation that allocator is
aware and agreeing with Terms of services of a specific Offering.

Example of the order payload sent with `POST` to ``https://puhuri-core-beta.neic.no/api/marketplace-orders/``:

```json

{
   "project": "https://puhuri-core-beta.neic.no/api/projects/72fff2b5f09643bdb1fa30684427336b/",
   "offering": "https://puhuri-core-beta.neic.no/api/marketplace-public-offerings/0980e9426d5247a0836ccfd64769d900/",
   "attributes": {
      "name": "test20",
   },
   "limits":{
      "gb_k_hours": 30,
      "cpu_k_hours": 1,
      "gpu_k_hours": 20
   },
   "plan": "https://puhuri-core-beta.neic.no/api/marketplace-public-plans/14b28e3a1cbe44b395bad48de9f934d8/",
   "accepting_terms_of_service": true
}
```

### Change resource limits

Send ``POST`` request to ``https://puhuri-core-beta.neic.no/api/marketplace-resources/<UUID_OF_A_RESOURCE>/update_limits/`` providing
the new values of limits, for example:

```json
{
   "limits": {
      "gb_k_hours": 35,
      "cpu_k_hours": 6,
      "gpu_k_hours": 200
   }
}
```

### Resource termination

Send ``POST`` request to ``https://puhuri-core-beta.neic.no/api/marketplace-resources/<UUID_OF_A_RESOURCE>/terminate/``.

API examples:

- [Creation of a resource allocation](project-api-examples.md#creation-of-a-resource-allocation)
- [Modification of a resource allocation](project-api-examples.md#modification-of-a-resource-allocation)
- [Termination of a resource allocation](project-api-examples.md#termination-of-a-resource-allocation)

Example integrations:

- [Lookup of available offerings in Waldur](https://github.com/waldur/waldur-mastermind/blob/7b2eba62e1e0dab945845f05030c7935e57f0d9c/src/waldur_mastermind/marketplace_remote/views.py#L45).
- [Creation of a resource in Waldur](https://github.com/waldur/waldur-mastermind/blob/7b2eba62e1e0dab945845f05030c7935e57f0d9c/src/waldur_mastermind/marketplace_remote/processors.py#L37).
- [Changing allocated limits in Waldur](https://github.com/waldur/waldur-mastermind/blob/7b2eba62e1e0dab945845f05030c7935e57f0d9c/src/waldur_mastermind/marketplace_remote/processors.py#L53).
- [Deletion of a resource allocation in Waldur](https://github.com/waldur/waldur-mastermind/blob/7b2eba62e1e0dab945845f05030c7935e57f0d9c/src/waldur_mastermind/marketplace_remote/processors.py#L64).

## Reporting

### Getting usage data of a specific resource allocation

To get reported usage for resources, send  ``GET`` request to ``https://puhuri-core-beta.neic.no/api/marketplace-component-usages/``. If you want to get usage data of a specific resource, please add a filter, e.g. ``https://puhuri-core-beta.neic.no/api/marketplace-component-usages/?resource_uuid=<UUID_OF_A_RESOURCE>``. Note that responses are paginated.

Additional filters that can be used:

- `date_before` - date of the returned usage records should be before or equal to provided, format YYYY-MM-DD, e.g. 2021-03-01.
- `date_after` - date of the returned usage records should be later or equal to provided, format YYYY-MM-DD, e.g. 2021-03-01.
- `offering_uuid` - return usage records only for a specified offering.
- `type` - type of the usage record to return, e.g. 'cpu_k_hours'.

Response will contain a list of usage records with a separate record for each component per month, for example:

```json
  {
    "uuid": "15a7a55fc78d44f995a6735b1f0f0c86",
    "created": "2021-11-26T20:30:21.348221Z",
    "description": "",
    "type": "cpu_k_hours",
    "name": "CPU allocation",
    "measured_unit": "CPU kH",
    "usage": 12,
    "date": "2021-11-26T20:30:21.342018Z",
    "resource_name": "Sample allocation",
    "resource_uuid": "4e4b8910b3df4ca0969871922eed8f3d",Waldur
    "offering_name": "LUMI UoI / Fast Track Access for Industry Access",
    "offering_uuid": "abe3c5e7cbe14d97a3208c56a22251f4",
    "project_name": "University of Iceland / Sample project",
    "project_uuid": "e1ffec53fd494d438fcb71daee1ae375",
    "customer_name": "University of Iceland",
    "customer_uuid": "6b4aba63ed47472e9cee84dac500cf11",
    "recurring": false,
    "billing_period": "2021-11-01"
  },
  {
    "uuid": "2b90e7f5f91d41b7838bc0d45093dd23",
    "created": "2021-11-26T20:30:21.383305Z",
    "description": "",
    "type": "gb_k_hours",
    "name": "Storage allocation",
    "measured_unit": "GB kH",
    "usage": 34,
    "date": "2021-11-26T20:30:21.342018Z",
    "resource_name": "Sample allocation",
    "resource_uuid": "4e4b8910b3df4ca0969871922eed8f3d",
    "offering_name": "LUMI UoI / Fast Track Access for Industry Access",
    "offering_uuid": "abe3c5e7cbe14d97a3208c56a22251f4",
    "project_name": "University of Iceland / Sample project",
    "project_uuid": "e1ffec53fd494d438fcb71daee1ae375",
    "customer_name": "University of Iceland",
    "customer_uuid": "6b4aba63ed47472e9cee84dac500cf11",
    "recurring": false,
    "billing_period": "2021-11-01"
  }
```

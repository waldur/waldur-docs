# Permissions

## Listing permissions

Entities of Waldur are grouped into *organisational units*. The
following *organisational units* are supported: customer and project.

Each *organisational unit* has a list of users associated with it.
Getting a list of users connected to a certain *organisational unit* is
done through running a GET request against a corresponding endpoint.

- customer: endpoint `/api/customer-permissions/`
- project: endpoint `/api/project-permissions/`

Filtering by *organisational unit* UUID or URL is supported. Depending
on the type, filter field is one of:

- `?customer=<UUID>`
- `?customer_url=<URL>`
- `?project=<UUID>`
- `?project_url=<URL>`
- `?user_url=<URL>`

In addition, filtering by field names is supported. In all cases
filtering is based on case insensitive partial matching.

- `?username=<username>`
- `?full_name=<full name>`
- `?native_name=<native name>`

Ordering can be done by setting an ordering field with
`?o=<field_name>`. For descending ordering prefix field name with a
dash (-). Supported field names are:

- `?o=user__username`
- `?o=user__full_name`
- `?o=user__native_name`

## Fetch user data from Waldur using username

To fetch user data together with its permissions, you need to perform the following HTTP request.
It requires `username` filter and valid API token.

```http
GET /api/users/?username=<USERNAME>&field=uuid&field=customer_permissions&field=project_permissions
Accept: application/json
Authorization: Token <API_TOKEN>
Host: example.com
```

Example:

```bash
> http -v --pretty all GET  http://example.com:8000/api/users/ username==admin field==uuid field==customer_permissions field==project_permissions Authorization:"Token 154f2c6984b5992928b62f87950ac529f1f906ca"

GET /api/users/?username=admin&field=uuid&field=customer_permissions&field=project_permissions HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Authorization: Token 154f2c6984b5992928b62f87950ac529f1f906ca
Connection: keep-alive
Host: example.com:8000
User-Agent: HTTPie/2.4.0



HTTP/1.1 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Language: en
Content-Length: 702
Content-Type: application/json
Date: Tue, 15 Feb 2022 13:07:10 GMT
Link: <http://example.com:8000/api/users/?field=uuid&field=customer_permissions&field=project_permissions&username=admin>; rel="first", <http://example.com:8000/api/users/?field=uuid&field=customer_permissions&field=project_permissions&username=admin>; rel="last"
Server: WSGIServer/0.2 CPython/3.8.2
Vary: Accept, Accept-Language, Cookie, Origin
X-Frame-Options: DENY
X-Result-Count: 1

[
    {
        "customer_permissions": [
            {
                "customer_abbreviation": "",
                "customer_name": "Admin org",
                "customer_native_name": "",
                "customer_uuid": "c9c8685ad4b1427aab2b6c9d36504f84",
                "pk": 8,
                "role": "owner",
                "url": "http://example.com:8000/api/customer-permissions/8/"
            },
            {
                "customer_abbreviation": "",
                "customer_name": "aaaaa",
                "customer_native_name": "",
                "customer_uuid": "7dd7481695e347a4bc80744b0f894c00",
                "pk": 9,
                "role": "owner",
                "url": "http://example.com:8000/api/customer-permissions/9/"
            }
        ],
        "project_permissions": [
            {
                "customer_name": "aaaaa",
                "pk": 40,
                "project_name": "a project",
                "project_uuid": "17db88c53b894aaca8314a2a0ebfda62",
                "role": "admin",
                "url": "http://example.com:8000/api/project-permissions/40/"
            }
        ],
        "uuid": "3c64889f169442d687490addc2a9de30"
    }
]
```

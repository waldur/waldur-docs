# Project API examples

## Lookup allocator customers available to a user

In most cases integration user can see only one allocating organization, however it is
possible that the same account is used for allocating different shares, e.g. national share and community specific.
Projects are always created in the context of a specific customer, so as a first thing you need to lookup a specific
customer you want to use. Customer is a stable entity, so it's URL / UUID can be cached.

```bash
$ http --pretty=format -v https://waldur.com/api/customers/ field==url field==name Authorization:"Token 787de6b7c581ab6d9d42fe9ec12ac9f1811c5811"
GET /api/customers/?field=url&field=name HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Authorization: Token 787de6b7c581ab6d9d42fe9ec12ac9f1811c5811
Connection: keep-alive
Host: waldur.com
User-Agent: HTTPie/2.4.0



HTTP/1.1 200 OK
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Accept, Accept-Encoding, Authorization, Content-Type, Origin, User-Agent, X-CSRFToken, X-Requested-With
Access-Control-Allow-Methods: DELETE, GET, OPTIONS, PATCH, POST, PUT
Access-Control-Allow-Origin: *
Access-Control-Expose-Headers: Link, X-Result-Count
Allow: GET, POST, HEAD, OPTIONS
Content-Language: en
Content-Length: 1188
Content-Security-Policy: report-uri csp.hpc.ut.ee; form-action 'self';
Content-Type: application/json
Date: Fri, 09 Apr 2021 09:28:42 GMT
Link: <https://waldur.com/api/customers/?field=url&field=name>; rel="first", <https://waldur.com/api/customers/?field=url&field=name>; rel="last"
Referrer-Policy: no-referrer-when-downgrade
Strict-Transport-Security: max-age=31536000; preload
Vary: Accept-Language, Cookie
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
X-Result-Count: 9
X-XSS-Protection: 1; mode=block

[
    {
        "name": "Estonian Scientific Computing Infrastructure",
        "url": "https://waldur.com/api/customers/33541d82c56c4eca8dbb1dabee54b3b9/"
    }
]
```

## Create a new project

```bash
$ http --pretty=format -v POST https://waldur.com/api/projects/ Authorization:"Token 787de6b7c581ab6d9d42fe9ec12ac9f1811c5811" customer=https://waldur.com/api/customers/d42a18b6b8ba4c2bb0591b3ff8fb181d/ name="Project name" description="Project description" backend_id="My unique string" oecd_fos_2007_code="1.1"
POST /api/projects/ HTTP/1.1
Accept: application/json, */*;q=0.5
Accept-Encoding: gzip, deflate
Authorization: Token 787de6b7c581ab6d9d42fe9ec12ac9f1811c5811
Connection: keep-alive
Content-Length: 192
Content-Type: application/json
Host: waldur.com
User-Agent: HTTPie/2.4.0

{
    "backend_id": "My unique string",
    "customer": "https://waldur.com/api/customers/d42a18b6b8ba4c2bb0591b3ff8fb181d/",
    "description": "Project description",
    "name": "Project name",
    "oecd_fos_2007_code": "1.1"
}

HTTP/1.1 201 Created
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Accept, Accept-Encoding, Authorization, Content-Type, Origin, User-Agent, X-CSRFToken, X-Requested-With
Access-Control-Allow-Methods: DELETE, GET, OPTIONS, PATCH, POST, PUT
Access-Control-Allow-Origin: *
Access-Control-Expose-Headers: Link, X-Result-Count
Allow: GET, POST, HEAD, OPTIONS
Content-Language: en
Content-Length: 604
Content-Security-Policy: report-uri csp.hpc.ut.ee; form-action 'self';
Content-Type: application/json
Date: Fri, 09 Apr 2021 09:40:52 GMT
Location: https://waldur.com/api/projects/4475ac77fa3a491aacb3fb3a6dfadadf/
Referrer-Policy: no-referrer-when-downgrade
Strict-Transport-Security: max-age=31536000; preload
Vary: Accept-Language, Cookie
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block

{
    "backend_id": "My unique string",
    "billing_price_estimate": {
        "current": 0,
        "tax": 0,
        "tax_current": 0,
        "total": 0.0
    },
    "created": "2021-04-09T09:40:51.832870Z",
    "customer": "https://waldur.com/api/customers/d42a18b6b8ba4c2bb0591b3ff8fb181d/",
    "customer_abbreviation": "DeiC",
    "customer_name": "Danish e-Infrastructure Cooperation",
    "customer_native_name": "",
    "customer_uuid": "d42a18b6b8ba4c2bb0591b3ff8fb181d",
    "description": "Project description",
    "name": "Project name",
    "oecd_fos_2007_code": "1.1",
    "type": null,
    "url": "https://waldur.com/api/projects/4475ac77fa3a491aacb3fb3a6dfadadf/",
    "uuid": "4475ac77fa3a491aacb3fb3a6dfadadf"
}
```

## Update an existing project

```bash
$ http --pretty=format -v PUT https://waldur.com/api/projects/4475ac77fa3a491aacb3fb3a6dfadadf/ Authorization:"Token 787de6b7c581ab6d9d42fe9ec12ac9f1811c5811" name="New project name" customer=https://waldur.com/api/customers/d42a18b6b8ba4c2bb0591b3ff8fb181d/
PUT /api/projects/4475ac77fa3a491aacb3fb3a6dfadadf/ HTTP/1.1
Accept: application/json, */*;q=0.5
Accept-Encoding: gzip, deflate
Authorization: Token 787de6b7c581ab6d9d42fe9ec12ac9f1811c5811
Connection: keep-alive
Content-Length: 124
Content-Type: application/json
Host: waldur.com
User-Agent: HTTPie/2.4.0

{
    "customer": "https://waldur.com/api/customers/d42a18b6b8ba4c2bb0591b3ff8fb181d/",
    "name": "New project name"
}

HTTP/1.1 200 OK
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Accept, Accept-Encoding, Authorization, Content-Type, Origin, User-Agent, X-CSRFToken, X-Requested-With
Access-Control-Allow-Methods: DELETE, GET, OPTIONS, PATCH, POST, PUT
Access-Control-Allow-Origin: *
Access-Control-Expose-Headers: Link, X-Result-Count
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Language: en
Content-Length: 608
Content-Security-Policy: report-uri csp.hpc.ut.ee; form-action 'self';
Content-Type: application/json
Date: Fri, 09 Apr 2021 09:45:16 GMT
Referrer-Policy: no-referrer-when-downgrade
Strict-Transport-Security: max-age=31536000; preload
Vary: Accept-Language, Cookie
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block

{
    "backend_id": "My unique string",
    "billing_price_estimate": {
        "current": 0,
        "tax": 0,
        "tax_current": 0,
        "total": 0.0
    },
    "created": "2021-04-09T09:40:51.832870Z",
    "customer": "https://waldur.com/api/customers/d42a18b6b8ba4c2bb0591b3ff8fb181d/",
    "customer_abbreviation": "DeiC",
    "customer_name": "Danish e-Infrastructure Cooperation",
    "customer_native_name": "",
    "customer_uuid": "d42a18b6b8ba4c2bb0591b3ff8fb181d",
    "description": "Project description",
    "name": "New project name",
    "type": null,
    "url": "https://waldur.com/api/projects/4475ac77fa3a491aacb3fb3a6dfadadf/",
    "uuid": "4475ac77fa3a491aacb3fb3a6dfadadf"
}
```

## List projects

```bash
$ http --pretty=format -v https://waldur.com/api/projects/ Authorization:"Token 787de6b7c581ab6d9d42fe9ec12ac9f1811c5811"
GET /api/projects/ HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Authorization: Token 787de6b7c581ab6d9d42fe9ec12ac9f1811c5811
Connection: keep-alive
Host: waldur.com
User-Agent: HTTPie/2.4.0



HTTP/1.1 200 OK
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Accept, Accept-Encoding, Authorization, Content-Type, Origin, User-Agent, X-CSRFToken, X-Requested-With
Access-Control-Allow-Methods: DELETE, GET, OPTIONS, PATCH, POST, PUT
Access-Control-Allow-Origin: *
Access-Control-Expose-Headers: Link, X-Result-Count
Allow: GET, POST, HEAD, OPTIONS
Content-Language: en
Content-Length: 7129
Content-Security-Policy: report-uri csp.hpc.ut.ee; form-action 'self';
Content-Type: application/json
Date: Fri, 09 Apr 2021 09:46:41 GMT
Link: <https://waldur.com/api/projects/>; rel="first", <https://waldur.com/api/projects/?page=2>; rel="next", <https://waldur.com/api/projects/?page=2>; rel="last"
Referrer-Policy: no-referrer-when-downgrade
Strict-Transport-Security: max-age=31536000; preload
Vary: Accept-Language, Cookie
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
X-Result-Count: 20
X-XSS-Protection: 1; mode=block

[
    {
        "backend_id": "",
        "billing_price_estimate": {
            "current": 0,
            "tax": 0,
            "tax_current": 0,
            "total": 0.0
        },
        "created": "2021-03-26T10:57:02.640605Z",
        "customer": "https://waldur.com/api/customers/29f29e6b65004bff9e831dec7c953177/",
        "customer_abbreviation": "OD",
        "customer_name": "Office Department",
        "customer_native_name": "",
        "customer_uuid": "29f29e6b65004bff9e831dec7c953177",
        "description": "test project description",
        "name": "test project",
        "type": "https://waldur.com/api/project-types/c588e4bc82fa4cf0b97e545e117c4c21/",
        "type_name": "Name of project type",
        "url": "https://waldur.com/api/projects/8cb53568cbed40c584029cb43cc540f6/",
        "uuid": "8cb53568cbed40c584029cb43cc540f6"
    }
]
```

## Project members permissions allocation

User creates a role for a user in a project.

```bash
$ http --pretty=format -v POST https://waldur.com/api/projects/2477fb6fad594922ac2f5ba195807502/add_user/ Authorization:"Token b0dd9a5eb32a158b2739d57d2b359aeb30aef246" role=PROJECT.ADMIN user=d213b473874c44d0bb5e2588b091160d
POST /api/projects/2477fb6fad594922ac2f5ba195807502/add_user/ HTTP/1.1
Accept: application/json, */*;q=0.5
Accept-Encoding: gzip, deflate
Authorization: Token b0dd9a5eb32a158b2739d57d2b359aeb30aef246
Connection: keep-alive
Content-Length: 69
Content-Type: application/json
Host: waldur.com
User-Agent: HTTPie/3.2.2

{
    "role": "PROJECT.ADMIN",
    "user": "d213b473874c44d0bb5e2588b091160d"
}

HTTP/1.1 201 Created
access-control-allow-credentials: true
access-control-allow-headers: Accept, Accept-Encoding, Authorization, Content-Type, Origin, User-Agent, X-CSRFToken, X-Requested-With, sentry-trace, baggage
access-control-allow-methods: DELETE, GET, OPTIONS, PATCH, POST, PUT
access-control-allow-origin: *
access-control-expose-headers: Link, X-Result-Count
allow: POST, OPTIONS
content-language: en
content-length: 24
content-security-policy: report-uri https://csp.hpc.ut.ee/log; form-action 'self'; frame-ancestors 'self';
content-type: application/json
date: Sun, 08 Oct 2023 17:28:49 GMT
referrer-policy: strict-origin-when-cross-origin
strict-transport-security: max-age=31536000; preload
vary: Accept-Language, Cookie
x-content-type-options: nosniff
x-frame-options: DENY
x-xss-protection: 1; mode=block

{
    "expiration_time": null
}
```

## List project permissions

```bash
$ http --pretty=format -v https://waldur.com/api/projects/2477fb6fad594922ac2f5ba195807502/list_users/ Authorization:"Token b0dd9a5eb32a158b2739d57d2b359aeb30aef246" 
GET /api/projects/2477fb6fad594922ac2f5ba195807502/list_users/ HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Authorization: Token b0dd9a5eb32a158b2739d57d2b359aeb30aef246
Connection: keep-alive
Host: waldur.com
User-Agent: HTTPie/3.2.2



HTTP/1.1 200 OK
access-control-allow-credentials: true
access-control-allow-headers: Accept, Accept-Encoding, Authorization, Content-Type, Origin, User-Agent, X-CSRFToken, X-Requested-With, sentry-trace, baggage
access-control-allow-methods: DELETE, GET, OPTIONS, PATCH, POST, PUT
access-control-allow-origin: *
access-control-expose-headers: Link, X-Result-Count
allow: GET, HEAD, OPTIONS
content-language: en
content-length: 484
content-security-policy: report-uri https://csp.hpc.ut.ee/log; form-action 'self'; frame-ancestors 'self';
content-type: application/json
date: Sun, 08 Oct 2023 17:29:53 GMT
link: <https://waldur.com/api/projects/2477fb6fad594922ac2f5ba195807502/list_users/>; rel="first", <https://waldur.com/api/projects/2477fb6fad594922ac2f5ba195807502/list_users/>; rel="last"
referrer-policy: strict-origin-when-cross-origin
strict-transport-security: max-age=31536000; preload
vary: Accept-Language, Cookie
x-content-type-options: nosniff
x-frame-options: DENY
x-result-count: 1
x-xss-protection: 1; mode=block

[
    {
        "created": "2023-10-08T17:28:49.565755Z",
        "created_by_full_name": "Demo User",
        "created_by_uuid": "d213b473874c44d0bb5e2588b091160d",
        "expiration_time": null,
        "role_name": "PROJECT.ADMIN",
        "role_uuid": "f734dc56c95e4f8880293defef00079e",
        "user_email": "demo.user@example.com",
        "user_full_name": "Demo User",
        "user_image": null,
        "user_username": "1af2bdea-73db-4790-baa5-5b487b6625f5@myaccessid.org",
        "user_uuid": "d213b473874c44d0bb5e2588b091160d",
        "uuid": "afdda66296c9490ebed72fce4a00d27a"
    }
]
```

## Removal of members from a project

User can remove the permissions calling DELETE verb on permission's URL.

```bash
$ http --pretty=format -v POST https://waldur.com/api/projects/2477fb6fad594922ac2f5ba195807502/delete_user/ Authorization:"Token b0dd9a5eb32a158b2739d57d2b359aeb30aef246" role=PROJECT.ADMIN user=d213b473874c44d0bb5e2588b091160d
POST /api/projects/2477fb6fad594922ac2f5ba195807502/delete_user/ HTTP/1.1
Accept: application/json, */*;q=0.5
Accept-Encoding: gzip, deflate
Authorization: Token b0dd9a5eb32a158b2739d57d2b359aeb30aef246
Connection: keep-alive
Content-Length: 69
Content-Type: application/json
Host: waldur.com
User-Agent: HTTPie/3.2.2

{
    "role": "PROJECT.ADMIN",
    "user": "d213b473874c44d0bb5e2588b091160d"
}

HTTP/1.1 200 OK
access-control-allow-credentials: true
access-control-allow-headers: Accept, Accept-Encoding, Authorization, Content-Type, Origin, User-Agent, X-CSRFToken, X-Requested-With, sentry-trace, baggage
access-control-allow-methods: DELETE, GET, OPTIONS, PATCH, POST, PUT
access-control-allow-origin: *
access-control-expose-headers: Link, X-Result-Count
allow: POST, OPTIONS
content-language: en
content-length: 0
content-security-policy: report-uri https://csp.hpc.ut.ee/log; form-action 'self'; frame-ancestors 'self';
date: Sun, 08 Oct 2023 17:31:32 GMT
referrer-policy: strict-origin-when-cross-origin
strict-transport-security: max-age=31536000; preload
vary: Accept-Language, Cookie
x-content-type-options: nosniff
x-frame-options: DENY
x-xss-protection: 1; mode=block
```

## Getting a list of offerings

User can fetch offerings and filter them by the following fields:

- `name` - offering's name
- `name_exact` - offering's exact name
- `customer` - organization's URL
- `customer_uuid` - organization's UUID
- `allowed_customer_uuid` - allowed organization's UUID
- `service_manager_uuid` - service manager's UUID
- `attributes` - a set of attributes (key-value pairs) identifying the allocation.
- `state` - offering's state (`Active`, `Draft`, `Paused`, `Archived`), should be `Active`
- `category_uuid` - category's UUID
- `billable` - signalizing if an offering is billable or not, should be `true`
- `shared` - signalizing if an offering is public or not, should be `true`
- `type` - offering's type

```bash
$ http --pretty=format -v https://waldur.com/api/marketplace-public-offerings/ Authorization:"Token 787de6b7c581ab6d9d42fe9ec12ac9f1811c5811" state==Active shared==true
GET /api/marketplace-public-offerings/?state=Active&shared=true HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Authorization: Token 787de6b7c581ab6d9d42fe9ec12ac9f1811c5811
Connection: keep-alive
Host: waldur.com
User-Agent: HTTPie/2.4.0



HTTP/1.1 200 OK
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Accept, Accept-Encoding, Authorization, Content-Type, Origin, User-Agent, X-CSRFToken, X-Requested-With
Access-Control-Allow-Methods: DELETE, GET, OPTIONS, PATCH, POST, PUT
Access-Control-Allow-Origin: *
Access-Control-Expose-Headers: Link, X-Result-Count
Allow: GET, POST, HEAD, OPTIONS
Content-Language: en
Content-Length: 4779
Content-Security-Policy: report-uri csp.hpc.ut.ee; form-action 'self';
Content-Type: application/json
Date: Fri, 09 Apr 2021 12:49:06 GMT
Link: <https://waldur.com/api/marketplace-public-offerings/?shared=true&state=Active>; rel="first", <https://waldur.com/api/marketplace-public-offerings/?shared=true&state=Active>; rel="last"
Referrer-Policy: no-referrer-when-downgrade
Strict-Transport-Security: max-age=31536000; preload
Vary: Accept-Language, Cookie
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
X-Result-Count: 1
X-XSS-Protection: 1; mode=block

[
    {
        "attributes": {},
        "backend_id": "",
        "billable": true,
        "category": "https://waldur.com/api/marketplace-categories/5b61d0811cfe4ed6a004119795a4c532/",
        "category_title": "HPC",
        "category_uuid": "5b61d0811cfe4ed6a004119795a4c532",
        "citation_count": -1,
        "components": [
            {
                "article_code": "",
                "billing_type": "usage",
                "default_limit": null,
                "description": "",
                "disable_quotas": false,
                "factor": null,
                "is_boolean": false,
                "limit_amount": null,
                "limit_period": null,
                "max_value": null,
                "measured_unit": "CPU kH",
                "min_value": null,
                "name": "CPU allocation",
                "type": "cpu_k_hours",
                "use_limit_for_billing": false
            },
            {
                "article_code": "",
                "billing_type": "usage",
                "default_limit": null,
                "description": "",
                "disable_quotas": false,
                "factor": null,
                "is_boolean": false,
                "limit_amount": null,
                "limit_period": null,
                "max_value": null,
                "measured_unit": "CPU kH",
                "min_value": null,
                "name": "GPU allocation",
                "type": "gpu_k_hours",
                "use_limit_for_billing": false
            },
            {
                "article_code": "",
                "billing_type": "usage",
                "default_limit": null,
                "description": "",
                "disable_quotas": false,
                "factor": null,
                "is_boolean": false,
                "limit_amount": null,
                "limit_period": null,
                "max_value": null,
                "measured_unit": "GB kH",
                "min_value": null,
                "name": "Storage allocation",
                "type": "gb_k_hours",
                "use_limit_for_billing": false
            }
        ],
        "created": "2021-03-09T10:27:47.170024Z",
        "customer": "https://waldur.com/api/customers/d42a18b6b8ba4c2bb0591b3ff8fb181d/",
        "customer_name": "Danish e-Infrastructure Cooperation",
        "customer_uuid": "d42a18b6b8ba4c2bb0591b3ff8fb181d",
        "datacite_doi": "",
        "description": "",
        "files": [],
        "full_description": "<h2>Overview</h2>One of the most powerful supercomputers in the world",
        "google_calendar_is_public": null,
        "latitude": 64.2310486,
        "longitude": 27.7040942,
        "name": " ",
        "native_description": "",
        "native_name": "",
        "options": {},
        "order_count": 1.0,
        "paused_reason": "",
        "plans": [
            {
                "archived": false,
                "article_code": "",
                "description": "Default plan for all ",
                "init_price": 0,
                "is_active": true,
                "max_amount": null,
                "name": " Common",
                "prices": {
                    "cpu_k_hours": 0.1,
                    "gb_k_hours": 0.001,
                    "gpu_k_hours": 0.5
                },
                "quotas": {
                    "cpu_k_hours": 0,
                    "gb_k_hours": 0,
                    "gpu_k_hours": 0
                },
                "switch_price": 0,
                "unit": "month",
                "unit_price": "0.0000000",
                "url": "https://waldur.com/api/marketplace-public-plans/c0fb33c79e9b48f69fcb6da26db5a28b/",
                "uuid": "c0fb33c79e9b48f69fcb6da26db5a28b"
            }
        ],
        "plugin_options": {
            "auto_approve_in_service_provider_projects": true
        },
        "quotas": null,
        "rating": 5,
        "scope": null,
        "screenshots": [],
        "secret_options": {},
        "shared": true,
        "state": "Active",
        "terms_of_service": "",
        "thumbnail": null,
        "type": "Marketplace.Basic",
        "url": "https://waldur.com/api/marketplace-provider-offerings/073a0ddd6eba4ff4a90b943ae3e1b7c9/",
        "uuid": "073a0ddd6eba4ff4a90b943ae3e1b7c9",
        "vendor_details": ""
    }
]
```

## Creation of a resource allocation

User can create an order providing requested allocation parameters.

- **`project`** - project's UUID
- **`offering`** - respectful offering's URL
- **`attributes`** - specific attributes for the offering
- **`plan`** - plan's URL (if offering is billable)
- **`limits`** - a set of resource limits for an allocation

```bash
$ http --pretty=format -v POST https://waldur.com/api/marketplace-orders/ Authorization:"Token 32e7682378fa394b0f8b2538c444b60129ebfb47" <<< '{
    "project": "https://waldur.com/api/projects/4475ac77fa3a491aacb3fb3a6dfadadf/",
    "offering": "https://waldur.com/api/marketplace-public-offerings/073a0ddd6eba4ff4a90b943ae3e1b7c9/",
    "attributes": {
        "name": "Resource allocation1",
        "used_ai_tech": [
            "Deep Learning",
            "Machine Learning"
        ],
        "is_industry": true,
        "is_commercial": false,
        "is_training": false
    },
    "plan": "https://waldur.com/api/marketplace-public-plans/c0fb33c79e9b48f69fcb6da26db5a28b/",
    "limits": {
        "gb_k_hours": 1,
        "gpu_k_hours": 2,
        "cpu_k_hours": 3
    }
}'

POST /api/marketplace-orders/ HTTP/1.1
Accept: application/json, */*;q=0.5
Accept-Encoding: gzip, deflate
Authorization: Token 32e7682378fa394b0f8b2538c444b60129ebfb47
Connection: keep-alive
Content-Length: 730
Content-Type: application/json
Host: waldur.com
User-Agent: HTTPie/2.4.0

{
    "attributes": {
        "name": "Resource allocation1",
        "used_ai_tech": [
            "Deep Learning",
            "Machine Learning"
        ],
        "is_industry": true,
        "is_commercial": false,
        "is_training": false
    },
    "limits": {
        "cpu_k_hours": 3,
        "gb_k_hours": 1,
        "gpu_k_hours": 2
    },
    "offering": "https://waldur.com/api/marketplace-public-offerings/073a0ddd6eba4ff4a90b943ae3e1b7c9/",
    "plan": "https://waldur.com/api/marketplace-public-plans/c0fb33c79e9b48f69fcb6da26db5a28b/",
    "project": "https://waldur.com/api/projects/4475ac77fa3a491aacb3fb3a6dfadadf/",
}

HTTP/1.1 201 Created
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Accept, Accept-Encoding, Authorization, Content-Type, Origin, User-Agent, X-CSRFToken, X-Requested-With
Access-Control-Allow-Methods: DELETE, GET, OPTIONS, PATCH, POST, PUT
Access-Control-Allow-Origin: *
Access-Control-Expose-Headers: Link, X-Result-Count
Allow: GET, POST, HEAD, OPTIONS
Content-Language: en
Content-Length: 2114
Content-Security-Policy: report-uri csp.hpc.ut.ee; form-action 'self';
Content-Type: application/json
Date: Wed, 21 Apr 2021 16:03:08 GMT
Location: https://waldur.com/api/marketplace-orders/d4ba1c23c3de47d6b0ad61bbfbaeed05/
Referrer-Policy: no-referrer-when-downgrade
Strict-Transport-Security: max-age=31536000; preload
Vary: Accept-Language, Cookie
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block

{
    "approved_at": "2021-04-21T16:03:08.430238Z",
    "approved_by": "https://waldur.com/api/users/3f2cadfbb2b145fd8cf18d549dcd7329/",
    "approved_by_full_name": "Demo Staff",
    "approved_by_username": "admin",
    "created": "2021-04-21T16:03:08.389589Z",
    "created_by": "https://waldur.com/api/users/3f2cadfbb2b145fd8cf18d549dcd7329/",
    "created_by_full_name": "Demo Staff",
    "created_by_username": "admin",
    "customer_uuid": "d42a18b6b8ba4c2bb0591b3ff8fb181d",
    "attributes": {
        "name": "Resource allocation1",
        "used_ai_tech": [
            "Deep Learning",
            "Machine Learning"
        ],
        "is_industry": true,
        "is_commercial": false,
        "is_training": false
    },
    "category_title": "HPC",
    "category_uuid": "5b61d0811cfe4ed6a004119795a4c532",
    "cost": "1.3010000000",
    "created": "2021-04-21T16:03:08.402139Z",
    "error_message": "",
    "error_traceback": "",
    "limits": {
        "cpu_k_hours": 3,
        "gb_k_hours": 1,
        "gpu_k_hours": 2
    },
    "modified": "2021-04-21T16:03:08.402139Z",
    "offering": "https://waldur.com/api/marketplace-public-offerings/073a0ddd6eba4ff4a90b943ae3e1b7c9/",
    "offering_billable": true,
    "offering_description": "",
    "offering_name": " ",
    "offering_shared": true,
    "offering_terms_of_service": "",
    "offering_thumbnail": null,
    "offering_type": "Marketplace.Basic",
    "offering_uuid": "073a0ddd6eba4ff4a90b943ae3e1b7c9",
    "output": "",
    "plan": "https://waldur.com/api/marketplace-public-plans/c0fb33c79e9b48f69fcb6da26db5a28b/",
    "plan_description": "Default plan for all ",
    "plan_name": " Common",
    "plan_unit": "month",
    "plan_uuid": "c0fb33c79e9b48f69fcb6da26db5a28b",
    "provider_name": "Danish e-Infrastructure Cooperation",
    "provider_uuid": "d42a18b6b8ba4c2bb0591b3ff8fb181d",
    "state": "pending-provider",
    "type": "Create",
    "uuid": "f980c6ae5dc746c5bf5bbf1e31ff7d7e"
    "project": "https://waldur.com/api/projects/4475ac77fa3a491aacb3fb3a6dfadadf/",
    "project_uuid": "4475ac77fa3a491aacb3fb3a6dfadadf",
    "total_cost": "1.3010000000",
    "url": "https://waldur.com/api/marketplace-orders/d4ba1c23c3de47d6b0ad61bbfbaeed05/",
    "uuid": "d4ba1c23c3de47d6b0ad61bbfbaeed05"
}
```

If a token belongs to a staff user, the order can be approved automatically.
Otherwise, there is additional need for manual approval.

After that, order should be pulled until resource UUID is present (`marketplace_resource_uuid` field).

```bash
$ http --pretty=format -v https://waldur.com/api/marketplace-orders/f980c6ae5dc746c5bf5bbf1e31ff7d7e/ Authorization:"Token 32e7682378fa394b0f8b2538c444b60129ebfb47"
GET /api/marketplace-orders/f980c6ae5dc746c5bf5bbf1e31ff7d7e/ HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Authorization: Token 32e7682378fa394b0f8b2538c444b60129ebfb47
Connection: keep-alive
Host: waldur.com
User-Agent: HTTPie/2.4.0



HTTP/1.1 200 OK
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Accept, Accept-Encoding, Authorization, Content-Type, Origin, User-Agent, X-CSRFToken, X-Requested-With
Access-Control-Allow-Methods: DELETE, GET, OPTIONS, PATCH, POST, PUT
Access-Control-Allow-Origin: *
Access-Control-Expose-Headers: Link, X-Result-Count
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Language: en
Content-Length: 1948
Content-Security-Policy: report-uri csp.hpc.ut.ee; form-action 'self';
Content-Type: application/json
Date: Wed, 21 Apr 2021 16:04:53 GMT
Referrer-Policy: no-referrer-when-downgrade
Strict-Transport-Security: max-age=31536000; preload
Vary: Accept-Language, Cookie
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block

{
    "activation_price": 0,
    "attributes": {
        "name": "Resource allocation1",
        "used_ai_tech": [
            "Deep Learning",
            "Machine Learning"
        ],
        "is_industry": true,
        "is_commercial": false,
        "is_training": false
    },
    "can_terminate": false,
    "category_title": "HPC",
    "category_uuid": "5b61d0811cfe4ed6a004119795a4c532",
    "cost": "1.3010000000",
    "created": "2021-04-21T16:03:08.402139Z",
    "created_by_civil_number": null,
    "created_by_full_name": "Demo Staff",
    "customer_name": "Danish e-Infrastructure Cooperation",
    "customer_uuid": "d42a18b6b8ba4c2bb0591b3ff8fb181d",
    "error_message": "",
    "error_traceback": "",
    "fixed_price": 0,
    "issue": null,
    "limits": {
        "cpu_k_hours": 3,
        "gb_k_hours": 1,
        "gpu_k_hours": 2
    },
    "marketplace_resource_uuid": "7b0dc0323ce94ebda8670d76a40ebe99",
    "modified": "2021-04-21T16:03:08.542428Z",
    "new_cost_estimate": 1.301,
    "new_plan_name": "Common",
    "new_plan_uuid": "c0fb33c79e9b48f69fcb6da26db5a28b",
    "offering": "https://waldur.com/api/marketplace-public-offerings/073a0ddd6eba4ff4a90b943ae3e1b7c9/",
    "offering_billable": true,
    "offering_description": "Description",
    "offering_name": " ",
    "offering_shared": true,
    "offering_terms_of_service": "",
    "offering_thumbnail": null,
    "offering_type": "Marketplace.Basic",
    "offering_uuid": "073a0ddd6eba4ff4a90b943ae3e1b7c9",
    "old_cost_estimate": 1.301,
    "order_approved_at": "2021-04-21T16:03:08.430238Z",
    "order_approved_by": "Demo Staff",
    "output": "",
    "plan": "https://waldur.com/api/marketplace-public-plans/c0fb33c79e9b48f69fcb6da26db5a28b/",
    "plan_description": "Default plan",
    "plan_name": "Common",
    "plan_unit": "month",
    "plan_uuid": "c0fb33c79e9b48f69fcb6da26db5a28b",
    "project_name": "New project name",
    "project_uuid": "4475ac77fa3a491aacb3fb3a6dfadadf",
    "provider_name": "Danish e-Infrastructure Cooperation",
    "provider_uuid": "d42a18b6b8ba4c2bb0591b3ff8fb181d",
    "resource_name": "Resource allocation1",
    "resource_type": null,
    "resource_uuid": null,
    "state": "done",
    "type": "Create",
    "uuid": "f980c6ae5dc746c5bf5bbf1e31ff7d7e"
}
```

### Order approval and rejection

In order to approve order by consumer, you shall issue POST request against `/api/marketplace-orders/{UUID}/approve_by_consumer/` endpoint. Similarly in order to approve order by provider, you shall issue POST request against `/api/marketplace-orders/{UUID}/approve_by_provider/` endpoint. Otherwise, you shall issue POST request against `/api/marketplace-orders/{UUID}/reject_by_consumer/` or `/api/marketplace-orders/{UUID}/reject_by_provider/` endpoint.

Of course, these endpoints are available only if you have service provider or service consumer permission against corresponding offerings.

## Modification of a resource allocation

```bash
$ http --pretty=format -v PUT https://waldur.com/api/marketplace-resources/b97e82d0fc2445d493cf5659a3085608/ Authorization:"Token 787de6b7c581ab6d9d42fe9ec12ac9f1811c5811" name="New resource name" description="New resource description"
PUT /api/marketplace-resources/b97e82d0fc2445d493cf5659a3085608/ HTTP/1.1
Accept: application/json, */*;q=0.5
Accept-Encoding: gzip, deflate
Authorization: Token 787de6b7c581ab6d9d42fe9ec12ac9f1811c5811
Connection: keep-alive
Content-Length: 72
Content-Type: application/json
Host: waldur.com
User-Agent: HTTPie/2.4.0

{
    "description": "New resource description",
    "name": "New resource name"
}

HTTP/1.1 200 OK
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Accept, Accept-Encoding, Authorization, Content-Type, Origin, User-Agent, X-CSRFToken, X-Requested-With
Access-Control-Allow-Methods: DELETE, GET, OPTIONS, PATCH, POST, PUT
Access-Control-Allow-Origin: *
Access-Control-Expose-Headers: Link, X-Result-Count
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Language: en
Content-Length: 69
Content-Security-Policy: report-uri csp.hpc.ut.ee; form-action 'self';
Content-Type: application/json
Date: Fri, 09 Apr 2021 15:21:23 GMT
Referrer-Policy: no-referrer-when-downgrade
Strict-Transport-Security: max-age=31536000; preload
Vary: Accept-Language, Cookie
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block

{
    "description": "New resource description",
    "name": "New resource name"
}
```

## Modification of resource allocation options

As an RA, you can update options of an allocations. Update happens through a special endpoint on a resource.

```bash
http -v POST https://waldur.com/api/marketplace-resources/b97e82d0fc2445d493cf5659a3085608/update_options/ Authorization:"Token 787de6b7c581ab6d9d42fe9ec12ac9f1811c5811" <<< '{
    "options": {
        "used_ai_tech": [
            "Deep Learning",
            "Machine Learning"
        ],
        "is_training": false
    }
}'
POST /api/marketplace-resources/53cb5c0a34cc41f5ad36b74c760e39f6/update_options/ HTTP/1.1
Accept: application/json, */*;q=0.5
Accept-Encoding: gzip, deflate
Authorization: Token 787de6b7c581ab6d9d42fe9ec12ac9f1811c5811
Connection: keep-alive
Content-Length: 153
Content-Type: application/json
Host: waldur-demo.com
User-Agent: HTTPie/3.2.2

{
    "options": {
        "is_training": false,
        "used_ai_tech": [
            "Deep Learning",
            "Machine Learning"
        ]
    }
}


HTTP/1.1 200 OK
access-control-allow-credentials: true
access-control-allow-headers: Accept, Accept-Encoding, Authorization, Content-Type, Origin, User-Agent, X-CSRFToken, X-Requested-With, X-Impersonated-User-Uuid, sentry-trace, baggage
access-control-allow-methods: DELETE, GET, OPTIONS, PATCH, POST, PUT
access-control-allow-origin: *
access-control-expose-headers: Link, X-Result-Count
allow: POST, OPTIONS
content-language: en
content-length: 43
content-security-policy: report-uri https://csp.hpc.ut.ee/log; form-action 'self'; frame-ancestors 'self';
content-type: application/json
date: Tue, 27 Aug 2024 09:18:29 GMT
referrer-policy: strict-origin-when-cross-origin
strict-transport-security: max-age=31536000; preload
vary: Accept-Language, Cookie
x-content-type-options: nosniff
x-frame-options: DENY
x-rate-limit-limit: 500
x-rate-limit-remaining: 488
x-xss-protection: 1; mode=block

{
    "status": "Resource options are submitted"
}

```

## Termination of a resource allocation

Termination uses a special short-cut action ``/terminate`` and returns UUID of a generated order.

```bash
$ http -v POST https://waldur.com/api/marketplace-resources/8887243fa8d0458c970eeb6be28ff4f7/terminate/ Authorization:"Token 32e7682378fa394b0f8b2538c444b60129ebfb47"
POST /api/marketplace-resources/8887243fa8d0458c970eeb6be28ff4f7/terminate/ HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Authorization: Token 32e7682378fa394b0f8b2538c444b60129ebfb47
Connection: keep-alive
Content-Length: 0
Host: waldur.com
User-Agent: HTTPie/2.4.0



HTTP/1.1 200 OK
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Accept, Accept-Encoding, Authorization, Content-Type, Origin, User-Agent, X-CSRFToken, X-Requested-With
Access-Control-Allow-Methods: DELETE, GET, OPTIONS, PATCH, POST, PUT
Access-Control-Allow-Origin: *
Access-Control-Expose-Headers: Link, X-Result-Count
Allow: POST, OPTIONS
Content-Language: en
Content-Length: 49
Content-Security-Policy: report-uri csp.hpc.ut.ee; form-action 'self';
Content-Type: application/json
Date: Wed, 14 Apr 2021 22:28:07 GMT
Referrer-Policy: no-referrer-when-downgrade
Strict-Transport-Security: max-age=31536000; preload
Vary: Accept-Language, Cookie
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block

{
    "order_uuid": "7c73504611d741749b3a3a538979e74a"
}

```

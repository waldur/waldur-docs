# Project API examples

## Lookup allocator customers available to a user

In most cases integration user can see only one allocating organization, however it is
possible that the same account is used for allocating different shares, e.g. national share and community specific.
Projects are always created in the context of a specific customer, so as a first thing you need to lookup a specific
customer you want to use. Customer is a stable entity, so it's URL / UUID can be cached.

```bash
$ http --pretty=format -v https://puhuri-core-beta.neic.no/api/customers/ field==url field==name Authorization:"Token 787de6b7c581ab6d9d42fe9ec12ac9f1811c5811"
GET /api/customers/?field=url&field=name HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Authorization: Token 787de6b7c581ab6d9d42fe9ec12ac9f1811c5811
Connection: keep-alive
Host: puhuri-core-beta.neic.no
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
Link: <https://puhuri-core-beta.neic.no/api/customers/?field=url&field=name>; rel="first", <https://puhuri-core-beta.neic.no/api/customers/?field=url&field=name>; rel="last"
Referrer-Policy: no-referrer-when-downgrade
Strict-Transport-Security: max-age=31536000; preload
Vary: Accept-Language, Cookie
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
X-Result-Count: 9
X-XSS-Protection: 1; mode=block

[
    {
        "name": "Danish e-Infrastructure Cooperation",
        "url": "https://puhuri-core-beta.neic.no/api/customers/d42a18b6b8ba4c2bb0591b3ff8fb181d/"
    },
    {
        "name": "Estonian Scientific Computing Infrastructure",
        "url": "https://puhuri-core-beta.neic.no/api/customers/33541d82c56c4eca8dbb1dabee54b3b9/"
    },
    {
        "name": "IT CENTER FOR SCIENCE LTD",
        "url": "https://puhuri-core-beta.neic.no/api/customers/29f29e6b65004bff9e831dec7c953177/"
    },
    {
        "name": "Swedish National Infrastructure for Computing",
        "url": "https://puhuri-core-beta.neic.no/api/customers/479843b7d15543bba6c0596bf408df63/"
    },
    {
        "name": "Swiss National Supercomputing Centre",
        "url": "https://puhuri-core-beta.neic.no/api/customers/f7b91251f991485999f423529fcdc1ad/"
    },
    {
        "name": "The IT4Innovations",
        "url": "https://puhuri-core-beta.neic.no/api/customers/9a8891e0327b460dbce61f9dda74d679/"
    },
    {
        "name": "The Polish Grid Infrastructure",
        "url": "https://puhuri-core-beta.neic.no/api/customers/c11b0d4e95144bd5964a09a294d30196/"
    },
    {
        "name": "UNINETT Sigma2 AS",
        "url": "https://puhuri-core-beta.neic.no/api/customers/918594bae69449bb8d011a4c5987515d/"
    },
    {
        "name": "VLAAMS SUPERCOMPUTER CENTRUM",
        "url": "https://puhuri-core-beta.neic.no/api/customers/b5fd863c7159484b8b9009aac1833cd3/"
    }
]
```

## Create a new project

```bash
$ http --pretty=format -v POST https://puhuri-core-beta.neic.no/api/projects/ Authorization:"Token 787de6b7c581ab6d9d42fe9ec12ac9f1811c5811" customer=https://puhuri-core-beta.neic.no/api/customers/d42a18b6b8ba4c2bb0591b3ff8fb181d/ name="Project name" description="Project description" backend_id="My unique string" oecd_fos_2007_code="1.1"
POST /api/projects/ HTTP/1.1
Accept: application/json, */*;q=0.5
Accept-Encoding: gzip, deflate
Authorization: Token 787de6b7c581ab6d9d42fe9ec12ac9f1811c5811
Connection: keep-alive
Content-Length: 192
Content-Type: application/json
Host: puhuri-core-beta.neic.no
User-Agent: HTTPie/2.4.0

{
    "backend_id": "My unique string",
    "customer": "https://puhuri-core-beta.neic.no/api/customers/d42a18b6b8ba4c2bb0591b3ff8fb181d/",
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
Location: https://puhuri-core-beta.neic.no/api/projects/4475ac77fa3a491aacb3fb3a6dfadadf/
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
    "customer": "https://puhuri-core-beta.neic.no/api/customers/d42a18b6b8ba4c2bb0591b3ff8fb181d/",
    "customer_abbreviation": "DeiC",
    "customer_name": "Danish e-Infrastructure Cooperation",
    "customer_native_name": "",
    "customer_uuid": "d42a18b6b8ba4c2bb0591b3ff8fb181d",
    "description": "Project description",
    "name": "Project name",
    "oecd_fos_2007_code": "1.1",
    "type": null,
    "url": "https://puhuri-core-beta.neic.no/api/projects/4475ac77fa3a491aacb3fb3a6dfadadf/",
    "uuid": "4475ac77fa3a491aacb3fb3a6dfadadf"
}
```

## Update an existing project

```bash
$ http --pretty=format -v PUT https://puhuri-core-beta.neic.no/api/projects/4475ac77fa3a491aacb3fb3a6dfadadf/ Authorization:"Token 787de6b7c581ab6d9d42fe9ec12ac9f1811c5811" name="New project name" customer=https://puhuri-core-beta.neic.no/api/customers/d42a18b6b8ba4c2bb0591b3ff8fb181d/
PUT /api/projects/4475ac77fa3a491aacb3fb3a6dfadadf/ HTTP/1.1
Accept: application/json, */*;q=0.5
Accept-Encoding: gzip, deflate
Authorization: Token 787de6b7c581ab6d9d42fe9ec12ac9f1811c5811
Connection: keep-alive
Content-Length: 124
Content-Type: application/json
Host: puhuri-core-beta.neic.no
User-Agent: HTTPie/2.4.0

{
    "customer": "https://puhuri-core-beta.neic.no/api/customers/d42a18b6b8ba4c2bb0591b3ff8fb181d/",
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
    "customer": "https://puhuri-core-beta.neic.no/api/customers/d42a18b6b8ba4c2bb0591b3ff8fb181d/",
    "customer_abbreviation": "DeiC",
    "customer_name": "Danish e-Infrastructure Cooperation",
    "customer_native_name": "",
    "customer_uuid": "d42a18b6b8ba4c2bb0591b3ff8fb181d",
    "description": "Project description",
    "name": "New project name",
    "type": null,
    "url": "https://puhuri-core-beta.neic.no/api/projects/4475ac77fa3a491aacb3fb3a6dfadadf/",
    "uuid": "4475ac77fa3a491aacb3fb3a6dfadadf"
}
```


## List projects
```bash
$ http --pretty=format -v https://puhuri-core-beta.neic.no/api/projects/ Authorization:"Token 787de6b7c581ab6d9d42fe9ec12ac9f1811c5811"
GET /api/projects/ HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Authorization: Token 787de6b7c581ab6d9d42fe9ec12ac9f1811c5811
Connection: keep-alive
Host: puhuri-core-beta.neic.no
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
Link: <https://puhuri-core-beta.neic.no/api/projects/>; rel="first", <https://puhuri-core-beta.neic.no/api/projects/?page=2>; rel="next", <https://puhuri-core-beta.neic.no/api/projects/?page=2>; rel="last"
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
        "customer": "https://puhuri-core-beta.neic.no/api/customers/29f29e6b65004bff9e831dec7c953177/",
        "customer_abbreviation": "CSC",
        "customer_name": "IT CENTER FOR SCIENCE LTD",
        "customer_native_name": "",
        "customer_uuid": "29f29e6b65004bff9e831dec7c953177",
        "description": "CSC test project description",
        "name": "CSC test project",
        "type": "https://puhuri-core-beta.neic.no/api/project-types/c588e4bc82fa4cf0b97e545e117c4c21/",
        "type_name": "Name of project type",
        "url": "https://puhuri-core-beta.neic.no/api/projects/8cb53568cbed40c584029cb43cc540f6/",
        "uuid": "8cb53568cbed40c584029cb43cc540f6"
    },
    {
        "backend_id": "",
        "billing_price_estimate": {
            "current": 0,
            "tax": 0,
            "tax_current": 0,
            "total": 0.0
        },
        "created": "2021-03-30T06:06:30.911124Z",
        "customer": "https://puhuri-core-beta.neic.no/api/customers/29f29e6b65004bff9e831dec7c953177/",
        "customer_abbreviation": "CSC",
        "customer_name": "IT CENTER FOR SCIENCE LTD",
        "customer_native_name": "",
        "customer_uuid": "29f29e6b65004bff9e831dec7c953177",
        "description": "CSC test project 10 description",
        "name": "CSC test project 10",
        "type": "https://puhuri-core-beta.neic.no/api/project-types/c588e4bc82fa4cf0b97e545e117c4c21/",
        "type_name": "Name of project type",
        "url": "https://puhuri-core-beta.neic.no/api/projects/a6241bd8342c4fb4b8ea9507ea03d658/",
        "uuid": "a6241bd8342c4fb4b8ea9507ea03d658"
    },
    {
        "backend_id": "",
        "billing_price_estimate": {
            "current": 0,
            "tax": 0,
            "tax_current": 0,
            "total": 0.0
        },
        "created": "2021-03-30T06:06:43.645113Z",
        "customer": "https://puhuri-core-beta.neic.no/api/customers/29f29e6b65004bff9e831dec7c953177/",
        "customer_abbreviation": "CSC",
        "customer_name": "IT CENTER FOR SCIENCE LTD",
        "customer_native_name": "",
        "customer_uuid": "29f29e6b65004bff9e831dec7c953177",
        "description": "CSC test project 11 description",
        "name": "CSC test project 11",
        "type": "https://puhuri-core-beta.neic.no/api/project-types/c588e4bc82fa4cf0b97e545e117c4c21/",
        "type_name": "Name of project type",
        "url": "https://puhuri-core-beta.neic.no/api/projects/d21ccbb0033f49fa928dc6bcc739cd8e/",
        "uuid": "d21ccbb0033f49fa928dc6bcc739cd8e"
    },
    {
        "backend_id": "",
        "billing_price_estimate": {
            "current": 0,
            "tax": 0,
            "tax_current": 0,
            "total": 0.0
        },
        "created": "2021-03-30T06:07:03.472114Z",
        "customer": "https://puhuri-core-beta.neic.no/api/customers/29f29e6b65004bff9e831dec7c953177/",
        "customer_abbreviation": "CSC",
        "customer_name": "IT CENTER FOR SCIENCE LTD",
        "customer_native_name": "",
        "customer_uuid": "29f29e6b65004bff9e831dec7c953177",
        "description": "CSC test project 12 description",
        "name": "CSC test project 12",
        "type": "https://puhuri-core-beta.neic.no/api/project-types/c588e4bc82fa4cf0b97e545e117c4c21/",
        "type_name": "Name of project type",
        "url": "https://puhuri-core-beta.neic.no/api/projects/09119652d1f24a068ec8a6d29da1016a/",
        "uuid": "09119652d1f24a068ec8a6d29da1016a"
    },
    {
        "backend_id": "",
        "billing_price_estimate": {
            "current": 0,
            "tax": 0,
            "tax_current": 0,
            "total": 0.0
        },
        "created": "2021-03-30T06:07:22.023662Z",
        "customer": "https://puhuri-core-beta.neic.no/api/customers/29f29e6b65004bff9e831dec7c953177/",
        "customer_abbreviation": "CSC",
        "customer_name": "IT CENTER FOR SCIENCE LTD",
        "customer_native_name": "",
        "customer_uuid": "29f29e6b65004bff9e831dec7c953177",
        "description": "CSC test project 13 description",
        "name": "CSC test project 13",
        "type": "https://puhuri-core-beta.neic.no/api/project-types/c588e4bc82fa4cf0b97e545e117c4c21/",
        "type_name": "Name of project type",
        "url": "https://puhuri-core-beta.neic.no/api/projects/adf45385e57749c4b636d09b127039ea/",
        "uuid": "adf45385e57749c4b636d09b127039ea"
    },
    {
        "backend_id": "",
        "billing_price_estimate": {
            "current": 0,
            "tax": 0,
            "tax_current": 0,
            "total": 0.0
        },
        "created": "2021-03-30T06:07:37.658803Z",
        "customer": "https://puhuri-core-beta.neic.no/api/customers/29f29e6b65004bff9e831dec7c953177/",
        "customer_abbreviation": "CSC",
        "customer_name": "IT CENTER FOR SCIENCE LTD",
        "customer_native_name": "",
        "customer_uuid": "29f29e6b65004bff9e831dec7c953177",
        "description": "CSC test project 14 description",
        "name": "CSC test project 14",
        "type": "https://puhuri-core-beta.neic.no/api/project-types/c588e4bc82fa4cf0b97e545e117c4c21/",
        "type_name": "Name of project type",
        "url": "https://puhuri-core-beta.neic.no/api/projects/4b3ff8e4dfe84c8ab83834715c757e47/",
        "uuid": "4b3ff8e4dfe84c8ab83834715c757e47"
    },
    {
        "backend_id": "",
        "billing_price_estimate": {
            "current": 0,
            "tax": 0,
            "tax_current": 0,
            "total": 0.0
        },
        "created": "2021-03-30T06:07:52.235226Z",
        "customer": "https://puhuri-core-beta.neic.no/api/customers/29f29e6b65004bff9e831dec7c953177/",
        "customer_abbreviation": "CSC",
        "customer_name": "IT CENTER FOR SCIENCE LTD",
        "customer_native_name": "",
        "customer_uuid": "29f29e6b65004bff9e831dec7c953177",
        "description": "CSC test project 15 description",
        "name": "CSC test project 15",
        "type": "https://puhuri-core-beta.neic.no/api/project-types/c588e4bc82fa4cf0b97e545e117c4c21/",
        "type_name": "Name of project type",
        "url": "https://puhuri-core-beta.neic.no/api/projects/19cb4c0825ec4333adcdf3fce9382fac/",
        "uuid": "19cb4c0825ec4333adcdf3fce9382fac"
    },
    {
        "backend_id": "",
        "billing_price_estimate": {
            "current": 0,
            "tax": 0,
            "tax_current": 0,
            "total": 0.0
        },
        "created": "2021-03-30T05:44:25.730256Z",
        "customer": "https://puhuri-core-beta.neic.no/api/customers/29f29e6b65004bff9e831dec7c953177/",
        "customer_abbreviation": "CSC",
        "customer_name": "IT CENTER FOR SCIENCE LTD",
        "customer_native_name": "",
        "customer_uuid": "29f29e6b65004bff9e831dec7c953177",
        "description": "CSC test project 2 description",
        "name": "CSC test project 2",
        "type": "https://puhuri-core-beta.neic.no/api/project-types/c588e4bc82fa4cf0b97e545e117c4c21/",
        "type_name": "Name of project type",
        "url": "https://puhuri-core-beta.neic.no/api/projects/62808e67ca734d6c9710f7d1dd35a299/",
        "uuid": "62808e67ca734d6c9710f7d1dd35a299"
    },
    {
        "backend_id": "",
        "billing_price_estimate": {
            "current": 0,
            "tax": 0,
            "tax_current": 0,
            "total": 0.0
        },
        "created": "2021-03-30T05:44:50.921959Z",
        "customer": "https://puhuri-core-beta.neic.no/api/customers/29f29e6b65004bff9e831dec7c953177/",
        "customer_abbreviation": "CSC",
        "customer_name": "IT CENTER FOR SCIENCE LTD",
        "customer_native_name": "",
        "customer_uuid": "29f29e6b65004bff9e831dec7c953177",
        "description": "CSC test project 3 description",
        "name": "CSC test project 3",
        "type": "https://puhuri-core-beta.neic.no/api/project-types/c588e4bc82fa4cf0b97e545e117c4c21/",
        "type_name": "Name of project type",
        "url": "https://puhuri-core-beta.neic.no/api/projects/03a57d26bc5c448f96ccaf6e1ce2a91d/",
        "uuid": "03a57d26bc5c448f96ccaf6e1ce2a91d"
    },
    {
        "backend_id": "",
        "billing_price_estimate": {
            "current": 0,
            "tax": 0,
            "tax_current": 0,
            "total": 0.0
        },
        "created": "2021-03-30T05:45:07.739197Z",
        "customer": "https://puhuri-core-beta.neic.no/api/customers/29f29e6b65004bff9e831dec7c953177/",
        "customer_abbreviation": "CSC",
        "customer_name": "IT CENTER FOR SCIENCE LTD",
        "customer_native_name": "",
        "customer_uuid": "29f29e6b65004bff9e831dec7c953177",
        "description": "CSC test project 4 description",
        "name": "CSC test project 4",
        "type": "https://puhuri-core-beta.neic.no/api/project-types/c588e4bc82fa4cf0b97e545e117c4c21/",
        "type_name": "Name of project type",
        "url": "https://puhuri-core-beta.neic.no/api/projects/ed75f213306740588854ea3e973c7fb5/",
        "uuid": "ed75f213306740588854ea3e973c7fb5"
    }
]
```

## Project members permissions allocation
User creates a role for a user in a project.

```bash
$ http --pretty=format -v POST https://puhuri-core-beta.neic.no/api/projects/2477fb6fad594922ac2f5ba195807502/add_user/ Authorization:"Token b0dd9a5eb32a158b2739d57d2b359aeb30aef246" role=PROJECT.ADMIN user=d213b473874c44d0bb5e2588b091160d
POST /api/projects/2477fb6fad594922ac2f5ba195807502/add_user/ HTTP/1.1
Accept: application/json, */*;q=0.5
Accept-Encoding: gzip, deflate
Authorization: Token b0dd9a5eb32a158b2739d57d2b359aeb30aef246
Connection: keep-alive
Content-Length: 69
Content-Type: application/json
Host: puhuri-core-beta.neic.no
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
$ http --pretty=format -v https://puhuri-core-beta.neic.no/api/projects/2477fb6fad594922ac2f5ba195807502/list_users/ Authorization:"Token b0dd9a5eb32a158b2739d57d2b359aeb30aef246" 
GET /api/projects/2477fb6fad594922ac2f5ba195807502/list_users/ HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Authorization: Token b0dd9a5eb32a158b2739d57d2b359aeb30aef246
Connection: keep-alive
Host: puhuri-core-beta.neic.no
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
link: <https://puhuri-core-beta.neic.no/api/projects/2477fb6fad594922ac2f5ba195807502/list_users/>; rel="first", <https://puhuri-core-beta.neic.no/api/projects/2477fb6fad594922ac2f5ba195807502/list_users/>; rel="last"
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
$ http --pretty=format -v POST https://puhuri-core-beta.neic.no/api/projects/2477fb6fad594922ac2f5ba195807502/delete_user/ Authorization:"Token b0dd9a5eb32a158b2739d57d2b359aeb30aef246" role=PROJECT.ADMIN user=d213b473874c44d0bb5e2588b091160d
POST /api/projects/2477fb6fad594922ac2f5ba195807502/delete_user/ HTTP/1.1
Accept: application/json, */*;q=0.5
Accept-Encoding: gzip, deflate
Authorization: Token b0dd9a5eb32a158b2739d57d2b359aeb30aef246
Connection: keep-alive
Content-Length: 69
Content-Type: application/json
Host: puhuri-core-beta.neic.no
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
- `attributes` - a set of attributes (key-value pairs) identifying the allocation. Check [below](#lumi-resource-options) for LUMI specific attributes.
- `state` - offering's state (`Active`, `Draft`, `Paused`, `Archived`), should be `Active`
- `category_uuid` - category's UUID
- `billable` - signalizing if an offering is billable or not, should be `true`
- `shared` - signalizing if an offering is public or not, should be `true`
- `type` - offering's type

```bash
$ http --pretty=format -v https://puhuri-core-beta.neic.no/api/marketplace-public-offerings/ Authorization:"Token 787de6b7c581ab6d9d42fe9ec12ac9f1811c5811" state==Active shared==true
GET /api/marketplace-public-offerings/?state=Active&shared=true HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Authorization: Token 787de6b7c581ab6d9d42fe9ec12ac9f1811c5811
Connection: keep-alive
Host: puhuri-core-beta.neic.no
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
Link: <https://puhuri-core-beta.neic.no/api/marketplace-public-offerings/?shared=true&state=Active>; rel="first", <https://puhuri-core-beta.neic.no/api/marketplace-public-offerings/?shared=true&state=Active>; rel="last"
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
        "category": "https://puhuri-core-beta.neic.no/api/marketplace-categories/5b61d0811cfe4ed6a004119795a4c532/",
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
        "customer": "https://puhuri-core-beta.neic.no/api/customers/d42a18b6b8ba4c2bb0591b3ff8fb181d/",
        "customer_name": "Danish e-Infrastructure Cooperation",
        "customer_uuid": "d42a18b6b8ba4c2bb0591b3ff8fb181d",
        "datacite_doi": "",
        "description": "LUMI share of Denmark",
        "files": [],
        "full_description": "<h2>Overview</h2>One of the most powerful supercomputers in the world, LUMI, will start its operations in CSC’s data center in Kajaani, Finland, next year. The peak performance of LUMI is an astonishing 552 petaflop/s. To date, the world’s fastest computer, Fugaku in Japan, reaches peak performance of 513 petaflop/s. When LUMI’s operations start next year, it will be one of the world’s fastest supercomputers",
        "google_calendar_is_public": null,
        "latitude": 64.2310486,
        "longitude": 27.7040942,
        "name": "LUMI Denmark",
        "native_description": "",
        "native_name": "",
        "options": {},
        "order_count": 1.0,
        "paused_reason": "",
        "plans": [
            {
                "archived": false,
                "article_code": "",
                "description": "Default plan for all LUMI",
                "init_price": 0,
                "is_active": true,
                "max_amount": null,
                "name": "LUMI Common",
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
                "url": "https://puhuri-core-beta.neic.no/api/marketplace-public-plans/c0fb33c79e9b48f69fcb6da26db5a28b/",
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
        "url": "https://puhuri-core-beta.neic.no/api/marketplace-provider-offerings/073a0ddd6eba4ff4a90b943ae3e1b7c9/",
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
$ http --pretty=format -v POST https://puhuri-core-beta.neic.no/api/marketplace-orders/ Authorization:"Token 32e7682378fa394b0f8b2538c444b60129ebfb47" <<< '{
    "project": "https://puhuri-core-beta.neic.no/api/projects/4475ac77fa3a491aacb3fb3a6dfadadf/",
    "offering": "https://puhuri-core-beta.neic.no/api/marketplace-public-offerings/073a0ddd6eba4ff4a90b943ae3e1b7c9/",
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
    "plan": "https://puhuri-core-beta.neic.no/api/marketplace-public-plans/c0fb33c79e9b48f69fcb6da26db5a28b/",
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
Host: puhuri-core-beta.neic.no
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
    "offering": "https://puhuri-core-beta.neic.no/api/marketplace-public-offerings/073a0ddd6eba4ff4a90b943ae3e1b7c9/",
    "plan": "https://puhuri-core-beta.neic.no/api/marketplace-public-plans/c0fb33c79e9b48f69fcb6da26db5a28b/",
    "project": "https://puhuri-core-beta.neic.no/api/projects/4475ac77fa3a491aacb3fb3a6dfadadf/",
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
Location: https://puhuri-core-beta.neic.no/api/marketplace-orders/d4ba1c23c3de47d6b0ad61bbfbaeed05/
Referrer-Policy: no-referrer-when-downgrade
Strict-Transport-Security: max-age=31536000; preload
Vary: Accept-Language, Cookie
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block

{
    "approved_at": "2021-04-21T16:03:08.430238Z",
    "approved_by": "https://puhuri-core-beta.neic.no/api/users/3f2cadfbb2b145fd8cf18d549dcd7329/",
    "approved_by_full_name": "Demo Staff",
    "approved_by_username": "admin",
    "created": "2021-04-21T16:03:08.389589Z",
    "created_by": "https://puhuri-core-beta.neic.no/api/users/3f2cadfbb2b145fd8cf18d549dcd7329/",
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
    "offering": "https://puhuri-core-beta.neic.no/api/marketplace-public-offerings/073a0ddd6eba4ff4a90b943ae3e1b7c9/",
    "offering_billable": true,
    "offering_description": "LUMI share of Denmark",
    "offering_name": "LUMI Denmark",
    "offering_shared": true,
    "offering_terms_of_service": "",
    "offering_thumbnail": null,
    "offering_type": "Marketplace.Basic",
    "offering_uuid": "073a0ddd6eba4ff4a90b943ae3e1b7c9",
    "output": "",
    "plan": "https://puhuri-core-beta.neic.no/api/marketplace-public-plans/c0fb33c79e9b48f69fcb6da26db5a28b/",
    "plan_description": "Default plan for all LUMI",
    "plan_name": "LUMI Common",
    "plan_unit": "month",
    "plan_uuid": "c0fb33c79e9b48f69fcb6da26db5a28b",
    "provider_name": "Danish e-Infrastructure Cooperation",
    "provider_uuid": "d42a18b6b8ba4c2bb0591b3ff8fb181d",
    "state": "pending-provider",
    "type": "Create",
    "uuid": "f980c6ae5dc746c5bf5bbf1e31ff7d7e"
    "project": "https://puhuri-core-beta.neic.no/api/projects/4475ac77fa3a491aacb3fb3a6dfadadf/",
    "project_uuid": "4475ac77fa3a491aacb3fb3a6dfadadf",
    "total_cost": "1.3010000000",
    "url": "https://puhuri-core-beta.neic.no/api/marketplace-orders/d4ba1c23c3de47d6b0ad61bbfbaeed05/",
    "uuid": "d4ba1c23c3de47d6b0ad61bbfbaeed05"
}
```

If a token belongs to a staff user, the order can be approved automatically.
Otherwise, there is additional need for manual approval.

After that, order should be pulled until resource UUID is present (`marketplace_resource_uuid` field).

```bash
$ http --pretty=format -v https://puhuri-core-beta.neic.no/api/marketplace-orders/f980c6ae5dc746c5bf5bbf1e31ff7d7e/ Authorization:"Token 32e7682378fa394b0f8b2538c444b60129ebfb47"
GET /api/marketplace-orders/f980c6ae5dc746c5bf5bbf1e31ff7d7e/ HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Authorization: Token 32e7682378fa394b0f8b2538c444b60129ebfb47
Connection: keep-alive
Host: puhuri-core-beta.neic.no
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
    "new_plan_name": "LUMI Common",
    "new_plan_uuid": "c0fb33c79e9b48f69fcb6da26db5a28b",
    "offering": "https://puhuri-core-beta.neic.no/api/marketplace-public-offerings/073a0ddd6eba4ff4a90b943ae3e1b7c9/",
    "offering_billable": true,
    "offering_description": "LUMI share of Denmark",
    "offering_name": "LUMI Denmark",
    "offering_shared": true,
    "offering_terms_of_service": "",
    "offering_thumbnail": null,
    "offering_type": "Marketplace.Basic",
    "offering_uuid": "073a0ddd6eba4ff4a90b943ae3e1b7c9",
    "old_cost_estimate": 1.301,
    "order_approved_at": "2021-04-21T16:03:08.430238Z",
    "order_approved_by": "Demo Staff",
    "output": "",
    "plan": "https://puhuri-core-beta.neic.no/api/marketplace-public-plans/c0fb33c79e9b48f69fcb6da26db5a28b/",
    "plan_description": "Default plan for all LUMI",
    "plan_name": "LUMI Common",
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
$ http --pretty=format -v PUT https://puhuri-core-beta.neic.no/api/marketplace-resources/b97e82d0fc2445d493cf5659a3085608/ Authorization:"Token 787de6b7c581ab6d9d42fe9ec12ac9f1811c5811" name="New resource name" description="New resource description"
PUT /api/marketplace-resources/b97e82d0fc2445d493cf5659a3085608/ HTTP/1.1
Accept: application/json, */*;q=0.5
Accept-Encoding: gzip, deflate
Authorization: Token 787de6b7c581ab6d9d42fe9ec12ac9f1811c5811
Connection: keep-alive
Content-Length: 72
Content-Type: application/json
Host: puhuri-core-beta.neic.no
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
Check [below](#lumi-resource-options) for LUMI specific attributes.

```bash
http -v POST https://puhuri-core-beta.neic.no/api/marketplace-resources/b97e82d0fc2445d493cf5659a3085608/update_options/ Authorization:"Token 787de6b7c581ab6d9d42fe9ec12ac9f1811c5811" <<< '{
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
Host: puhuri-portal-demo.neic.no
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
$ http -v POST https://puhuri-core-beta.neic.no/api/marketplace-resources/8887243fa8d0458c970eeb6be28ff4f7/terminate/ Authorization:"Token 32e7682378fa394b0f8b2538c444b60129ebfb47"
POST /api/marketplace-resources/8887243fa8d0458c970eeb6be28ff4f7/terminate/ HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Authorization: Token 32e7682378fa394b0f8b2538c444b60129ebfb47
Connection: keep-alive
Content-Length: 0
Host: puhuri-core-beta.neic.no
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

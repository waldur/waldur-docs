# Integrating LEXIS with Waldur

## Creating a LEXIS link for a resource

To create a [LEXIS](https://docs.lexis.tech/) link integration with a Waldur resource the API request shown below can be sent (http refers to HTTPie client).

```bash
http POST https://waldur.example.com/api/lexis-links/ Authorization:"Token e63ffc6408afc4ft874fc5fb4dbcebf1277ca723" resource=https://waldur.example.com/api/marketplace-resources/a5dad412c0d94aeb8cffad3d0ca325ea/
HTTP/1.1 200 OK
Accept: application/json, text/plain, */*
Accept-Language: en
HTTP/1.1 201 Created
Date: Mon, 23 Oct 2023 07:31:08 GMT
Content-Type: application/json
Vary: Accept, Accept-Language, Cookie, Origin
Allow: GET, POST, HEAD, OPTIONS
X-Frame-Options: DENY
Content-Length: 2
Content-Language: en
Access-Control-Allow-Origin: *
Access-Control-Expose-Headers: x-result-count, Link
```

Alternatively this can be done through UI of Waldur as shown below.

**Note: To be able to create a LEXIS link for a resource using Waldur UI, the related to the resource offering has to have `plugin_options` set.**

Namely:

* heappe_url
* heappe_username
* heappe_cluster_id
* heappe_local_base_path

![img.png](images/lexisstep1.png)
![img.png](images/lexisstep2.png)

## Listing all LEXIS links

To view all LEXIS links the API request shown below can be sent.

```bash
http GET https://waldur.example.com/api/lexis-links/ Authorization:"Token e63ffc6408afc4ft874fc5fb4dbcebf1277ca723"
Accept: application/json, text/plain, */*
Accept-Language: en
HTTP/1.1 200 OK
Date: Mon, 23 Oct 2023 08:09:41 GMT
Content-Type: application/json
X-Result-Count: 4
Link: <https://waldur.example.com/api/lexis-links/?page_size=10>; rel="first", <https://waldur.example.com/api/lexis-links/?page_size=10>; rel="last"
Vary: Accept, Accept-Language, Cookie, Origin
Allow: GET, POST, HEAD, OPTIONS
X-Frame-Options: DENY
Content-Length: 2965
Content-Language: en
Access-Control-Allow-Origin: *
Access-Control-Expose-Headers: x-result-count, Link
```

Response example:

```json
[
  {
    "url":"https://waldur.example.com/api/lexis-links/6aaa620c60e14f21bd0817360db005ed/",
    "uuid":"6aaa620c60e14f21bd0817360db005ed",
    "created":"2023-10-23T08:57:44.031155Z",
    "modified":"2023-10-23T08:57:44.031155Z",
    "robot_account":"https://waldur.example.com/api/marketplace-robot-accounts/8ae5711c788f4700aab9480deed9e2bd/",
    "robot_account_username":"",
    "robot_account_type":"hl006",
    "state":"pending",
    "resource_uuid":"a5dad412c0d94aeb8cffad3d0ca325ea",
    "resource_name":"brandturn-keybandwidth",
    "resource_backend_id":"dca3f539-3215-476d-b68b-36d8844502f0",
    "resource_end_date":null,
    "project_uuid":"f5b14e76985349d8b5f91325702fde1b",
    "project_name":"Automated coherent access",
    "customer_uuid":"da90223725c74ee4b02524a3f3732321",
    "customer_name":"Ashley and Sons"
  }
]
```

_Note: A LEXIS link can be in one of the following states:_

1. _Pending_
2. _Executing_
3. _OK_
4. _Erred_

Listing LEXIS links can alternatively be done through Waldur UI by visiting resource details

![img.png](images/resourcedetails.png)

or use administration menu if you are a staff user

![img.png](images/stafflexis.png)

## Listing resources supporting LEXIS links

To list all resources supporting LEXIS links, the following API request can be used:

```bash
http GET https://waldur.example.com/api/marketplace-resources/?lexis_links_supported=true Authorization:"Token 154f2c6984b5992928b62f87950ac529f1f906ca"
```

The main filter is `lexis_links_supported` parameter.

The example response:

```json
HTTP/1.1 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Language: en
Content-Length: 4825
Content-Type: application/json
Date: Wed, 31 Jan 2024 13:48:54 GMT
Link: <https://waldur.example.com/api/marketplace-resources/?lexis_links_supported=true>; rel="first", <https://waldur.example.com/api/marketplace-resources/?lexis_links_supported=true>; rel="last"
Server: WSGIServer/0.2 CPython/3.11.5
Vary: Accept, Accept-Language, Cookie, Origin
X-Frame-Options: DENY
X-Result-Count: 2

[
    {
        "attributes": {
            "name": "br1"
        },
        "available_actions": [
            "LEXIS_LINK.CREATE"
        ],
        "backend_id": "project_000003",
        "backend_metadata": {},
        "can_terminate": true,
        "category_icon": "https://waldur.example.com/api/media-download/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c3IiOiIzYzY0ODg5ZjE2OTQ0MmQ2ODc0OTBhZGRjMmE5ZGUzMCIsImN0IjoibWFya2V0cGxhY2UuY2F0ZWdvcnkiLCJpZCI6IjQ3NDZjYWY4NTk0NzQwYjlhNWM4Y2I3OWE1ZGZkNThjIiwiZmllbGQiOiJpY29uIiwiZXhwIjoxNzA2NzEyNTM0fQ.d1oe4Yn5DcB2nEqHjWp-TQzYt0f2gmkJwO_SS3ArJms/",
        "category_title": "HPC",
        "category_uuid": "4746caf8594740b9a5c8cb79a5dfd58c",
        "created": "2022-12-15T20:35:48.855341Z",
        "current_usages": {},
        "customer_name": "Remote project",
        "customer_uuid": "b559b279ee9f47a788f64ac4b86d1c56",
        "description": "",
        "effective_id": "",
        "end_date": null,
        "end_date_requested_by": null,
        "endpoints": [],
        "error_message": "",
        "error_traceback": "",
        "is_limit_based": false,
        "is_usage_based": false,
        "limit_usage": null,
        "limits": {
          "gb_k_hours": 30,
          "cpu_k_hours": 1,
          "gpu_k_hours": 20
        },
        "modified": "2023-10-09T11:17:30.214126Z",
        "name": "br1",
        "offering": "https://waldur.example.com/api/marketplace-public-offerings/765868848dd943e0baeefdac9a78aeac/",
        "offering_billable": true,
        "offering_customer_uuid": "b559b279ee9f47a788f64ac4b86d1c56",
        "offering_description": "",
        "offering_image": null,
        "offering_name": "Basic",
        "offering_plugin_options": {
            "heappe_cluster_id": 1,
            "heappe_local_base_path": "~/",
            "heappe_url": "https://heappe-1.cloud.ut.ee",
            "heappe_username": "admin"
        },
        "offering_shared": true,
        "offering_terms_of_service": "",
        "offering_thumbnail": null,
        "offering_type": "Marketplace.Basic",
        "offering_uuid": "765868848dd943e0baeefdac9a78aeac",
        "options": null,
        "plan": "https://waldur.example.com/api/marketplace-public-offerings/765868848dd943e0baeefdac9a78aeac/plans/6e08a30d481b4d62a17a2c145d744d9e/",
        "plan_description": "",
        "plan_name": "asd plan",
        "plan_unit": "month",
        "plan_uuid": "6e08a30d481b4d62a17a2c145d744d9e",
        "project": "https://waldur.example.com/api/projects/dcc1e4456ba94f2498cf85dace03d1f4/",
        "project_description": "",
        "project_end_date": null,
        "project_end_date_requested_by": null,
        "project_name": "Local project / Local project 14",
        "project_uuid": "dcc1e4456ba94f2498cf85dace03d1f4",
        "provider_name": "Remote project",
        "provider_uuid": "b559b279ee9f47a788f64ac4b86d1c56",
        "report": null,
        "requested_downscaling": false,
        "resource_type": null,
        "resource_uuid": null,
        "scope": null,
        "state": "OK",
        "url": "https://waldur.example.com/api/marketplace-resources/f70a26bf348348a085d7b1276b473bcc/",
        "username": null,
        "uuid": "f70a26bf348348a085d7b1276b473bcc"
    }
]
```

## Deleting LEXIS links

To delete a LEXIS link the API request shown below can be sent.

```bash
http DELETE https://waldur.example.com/api/lexis-links/3bb9fbdce9aa4602860fbedf94d9fb17/
Accept: application/json, text/plain, */*
Accept-Language: en
Authorization: Token e63ffc6408afc4ft874fc5fb4dbcebf1277ca723
HTTP/1.1 204 No Content
Date: Mon, 23 Oct 2023 08:56:48 GMT
Vary: Accept, Accept-Language, Cookie, Origin
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
X-Frame-Options: DENY
Content-Length: 0
Content-Language: en
Access-Control-Allow-Origin: *
Access-Control-Expose-Headers: x-result-count, Link
```

This can alternatively be done using Waldur UI as shown below:
![img.png](images/lexisdelete.png)

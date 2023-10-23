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

This can alternatively be done through Waldur UI by visiting resource details

![img.png](images/resourcedetails.png)

or use administration menu if you are a staff user

![img.png](images/stafflexis.png)

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

# Service Provider Onboarding

This page describes onboarding steps for a service provider via Waldur REST API.

## Slurm Agent Integration

The following steps are specific for SLURM plugin in Waldur.

### Creation of SLURM Offering in Waldur

This section describes creation of SLURM offering in Waldur, which is managed by [Waldur Site Agent](../admin-guide/providers/site-agent/index.md).

#### Example request

```http
POST https://test-portal.example.com/api/marketplace-provider-offerings/
Authorization: Token <Org Owner Token>
Content-Type: application/json
```

Body:

```json
{
    "name": "Test Cluster",
    "description": "Test Cluster",
    "customer": "https://test-portal.example.com/api/customers/354c1f993eb54228b336046417ffaf39/",
    "category": "https://test-portal.example.com/api/marketplace-categories/4588ff519260461893ab371b8fe83363/",
    "components": [
        {
            "type": "node_hours",
            "name": "Node hours",
            "measured_unit": "Node-hours",
            "billing_type": "usage",
            "limit_period": null
        }
    ],
    "plans": [
        {
            "name": "Default",
            "description": "Default plan",
            "unit": "month"
        }
    ],
    "type": "Marketplace.Slurm",
    "shared": true
}
```

#### Example response

Status code: 201

Body:

```json
{
    "url": "https://test-portal.example.com/api/marketplace-provider-offerings/b52a120a0301434a84571bde0b2b74bf/",
    "uuid": "b52a120a0301434a84571bde0b2b74bf",
    "created": "2025-02-04T08:37:14.715810Z",
    "name": "Test Cluster",
    "slug": "test-clu-1",
    "description": "Test Cluster",
    "full_description": "",
    "terms_of_service": "",
    "terms_of_service_link": "",
    "privacy_policy_link": "",
    "access_url": "",
    "endpoints": [],
    "roles": [],
    "customer": "https://test-portal.example.com/api/customers/354c1f993eb54228b336046417ffaf39/",
    "customer_uuid": "354c1f993eb54228b336046417ffaf39",
    "customer_name": "Test Customer",
    "project": null,
    "category": "https://test-portal.example.com/api/marketplace-categories/4588ff519260461893ab371b8fe83363/",
    "category_uuid": "4588ff519260461893ab371b8fe83363",
    "category_title": "HPC",
    "attributes": {},
    "options": {
        "order": [],
        "options": {}
    },
    "resource_options": {
        "options": {},
        "order": []
    },
    "components": [
        {
            "uuid": "30f86ef120a341dba1b7225cf891c77b",
            "billing_type": "usage",
            "type": "node_hours",
            "name": "Node hours",
            "description": "",
            "measured_unit": "Node-hours",
            "unit_factor": 1,
            "limit_period": null,
            "limit_amount": null,
            "article_code": "",
            "max_value": null,
            "min_value": null,
            "max_available_limit": null,
            "is_boolean": false,
            "default_limit": null,
            "factor": null,
            "is_builtin": false
        }
    ],
    "plugin_options": {},
    "secret_options": {},
    "service_attributes": {},
    "state": "Draft",
    "state_code": 1,
    "native_name": "",
    "native_description": "",
    "vendor_details": "",
    "getting_started": "",
    "integration_guide": "",
    "thumbnail": null,
    "order_count": 0,
    "plans": [
        {
            "url": "https://test-portal.example.com/api/marketplace-plans/8ffd1813ba2449bc928546a1dd94bca9/",
            "uuid": "8ffd1813ba2449bc928546a1dd94bca9",
            "name": "Default",
            "description": "Default plan",
            "article_code": "",
            "max_amount": null,
            "archived": false,
            "is_active": true,
            "unit_price": "0.0000000000",
            "unit": "month",
            "init_price": 0,
            "switch_price": 0,
            "backend_id": "",
            "organization_groups": [],
            "prices": {
                "node_hours": 0.0
            },
            "future_prices": {
                "node_hours": null
            },
            "quotas": {
                "node_hours": 0
            },
            "resources_count": 0
        }
    ],
    "screenshots": [],
    "type": "Marketplace.Slurm",
    "shared": true,
    "billable": true,
    "scope": null,
    "files": [],
    "paused_reason": "",
    "datacite_doi": "",
    "citation_count": -1,
    "latitude": null,
    "longitude": null,
    "country": "",
    "backend_id": "",
    "organization_groups": [],
    "image": null,
    "backend_metadata": {}
}
```

### Setting up integration options of the SLURM Offering

For automated management of the offering-related accounts in Waldur, the service provider should update the integration options for the offering.

#### Example request

```http
POST https://test-portal.example.com/api/marketplace-provider-offerings/b52a120a0301434a84571bde0b2b74bf/update_integration/
Authorization: Token <Org Owner Token>
Content-Type: application/json
```

Body:

```json
    {
        "plugin_options": {
            "homedir_prefix": "/home/",
            "initial_uidnumber": 5000,
            "initial_usergroup_number": 6000,
            "username_anonymized_prefix": "waldur_",
            "username_generation_policy": "waldur_username",
            "initial_primarygroup_number": 5000,
            "account_name_generation_policy": "project_slug",
            "supports_pausing": true,
            "supports_downscaling": true,
            "service_provider_can_create_offering_user": true
        }
    }
```

#### Example response

Status code: 200
Body: empty

### Activation of the SLURM Offering

After creation, the offering is in `Draft` state meaning the service provider can edit it, but it is hidden from Wadlur marketplace.
In order to publish it, the service provider should activate the offering the way described below.

#### Example request

```http
POST https://test-portal.example.com/api/marketplace-provider-offerings/b52a120a0301434a84571bde0b2b74bf/activate/
Authorization: Token <Org Owner Token>
Content-Type: application/json
```

Note: This endpoint doesn't require any body.

After sending this request, the offering becomes activated, its state switched to `Active`
and users of the marketplace can order resources.

#### Example response

Status code: 201

Body: empty

### Creation of a service account user

For further management of the offering, Waldur Site Agent need a service account with access to the offering.
This section describes how to create such a user.

#### Example request

```http
POST https://test-portal.example.com/api/users/
Authorization: Token <Staff Token>
Content-Type: application/json
```

Body:

```json
{
    "username": "test_27dd96e5bbc141b3a49f",
    "email": "test_27dd96e5bbc141b3a49f@example.com",
    "is_staff": false,
    "is_active": true,
    "is_support": false,
    "agree_with_policy": true,
    "first_name": "test",
    "last_name": "27dd96e5bbc141b3a49f"
}
```

#### Example response

Status: 201

Body:

```json
{
    "url": "https://test-portal.example.com/api/users/619d60a1c54f484885dfdf42c1dc5dbe/",
    "uuid": "619d60a1c54f484885dfdf42c1dc5dbe",
    "username": "test_27dd96e5bbc141b3a49f",
    "slug": "test_27d-1",
    "full_name": "test 27dd96e5bbc141b3a49f",
    "native_name": "",
    "job_title": "",
    "email": "test_27dd96e5bbc141b3a49f@example.com",
    "phone_number": "",
    "organization": "",
    "civil_number": null,
    "description": "",
    "is_staff": false,
    "is_active": true,
    "is_support": false,
    "registration_method": "default",
    "date_joined": "2025-02-05T13:43:18.365132Z",
    "agreement_date": null,
    "preferred_language": "",
    "permissions": [],
    "requested_email": null,
    "affiliations": [],
    "first_name": "test",
    "last_name": "27dd96e5bbc141b3a49f",
    "identity_provider_name": "Local DB",
    "identity_provider_label": "Local DB",
    "identity_provider_management_url": "",
    "identity_provider_fields": [],
    "image": null,
    "identity_source": ""
}
```

### Assigning service provider permissions to the user

After user creation, you need to grant them permissions for offering management.
Waldur uses `OFFERING.MANAGER` role for this.

#### Example request

```http
POST https://test-portal.example.com/api/marketplace-provider-offerings/b52a120a0301434a84571bde0b2b74bf/add_user/
Authorization: Token <Service Provider Token>
Content-Type: application/json
```

Body:

```json
{
    "role": "OFFERING.MANAGER",
    "user": "619d60a1c54f484885dfdf42c1dc5dbe"
}
```

#### Example response

Status code: 201

Body: empty

### Service Account Token Retrieval

As a staff user, you can fetch any other user's token. For this, use `token` endpoint on a selected user.

#### Example request

```http
GET https://test-portal.example.com/api/users/619d60a1c54f484885dfdf42c1dc5dbe/token/
Authorization: Token <Staff Token>
```

#### Example response

Status code: 200

Body:

```json
{
    "created": "2025-02-06T12:09:46.296525Z",
    "token": "668bf4c77f81edcb2de181d72df40bf7b4e2a6c2",
    "user_first_name": "test",
    "user_is_active": true,
    "user_last_name": "27dd96e5bbc141b3a49f",
    "user_token_lifetime": "3600",
    "user_username": "test_27dd96e5bbc141b3a49f"
}
```

### Service Account Token Refresh

As a staff user, you can also manually refresh any other user's token.
For this, use `refresh_token` endpoint on a selected user.

#### Example request

```http
POST https://test-portal.example.com/api/users/619d60a1c54f484885dfdf42c1dc5dbe/refresh_token/
Authorization: Token <Staff Token>
Content-Type: application/json
```

Body: not required

#### Example response

Status code: 201

Body:

```json
{
    "created": "2025-02-06T12:14:02.899419Z",
    "token": "1d7e2934d9a158e3046add2869bf63a28cba3b6f",
    "user_first_name": "test",
    "user_is_active": true,
    "user_last_name": "27dd96e5bbc141b3a49f",
    "user_token_lifetime": "3600",
    "user_username": "test_27dd96e5bbc141b3a49f"
}
```

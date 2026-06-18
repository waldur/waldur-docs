# Service Provider Onboarding

This page describes onboarding steps for a service provider via Waldur REST API.

## Slurm Agent Integration

The following steps are specific for the SLURM plugin in Waldur.

### Overview

The onboarding process consists of the following steps:

1. [Create a SLURM offering](#step-1-create-a-slurm-offering)
2. [Configure integration options](#step-2-configure-integration-options)
3. [Activate the offering](#step-3-activate-the-offering)
4. [Create a service account user](#step-4-create-a-service-account-user)
5. [Assign service provider permissions](#step-5-assign-service-provider-permissions)
6. [Retrieve the service account token](#step-6-retrieve-the-service-account-token)

### Step 1: Create a SLURM Offering

This step creates a SLURM offering in Waldur, which is managed by [Waldur Site Agent](../admin-guide/providers/site-agent/index.md).

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
    "customer": "https://test-portal.example.com/api/customers/<customer-uuid>/",
    "category": "https://test-portal.example.com/api/marketplace-categories/<category-uuid>/",
    "components": [
        {
            "type": "node_hours",
            "name": "Node hours",
            "measured_unit": "Node-hours",
            "billing_type": "usage",
            "limit_period": "month",
            "limit_amount": 100,
            "unit_factor": 1
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

#### Component fields

| Field | Required | Description | Valid values |
|-------|----------|-------------|--------------|
| `type` | Yes | Component identifier | Any string (e.g. `node_hours`) |
| `name` | Yes | Display name | Any string |
| `measured_unit` | Yes | Unit label shown in the UI | Any string (e.g. `Node-hours`) |
| `billing_type` | Yes | How the component is billed | `usage`, `limit` |
| `limit_period` | No | Billing period for limits | `month`, `quarterly`, `annual`, `total` |
| `limit_amount` | No | Global limit per resource (only for `usage` billing type) | Positive integer |
| `unit_factor` | No | Conversion factor from backend units to `measured_unit` | Number (default: `1`) |

#### Example response

Status code: `201`

Body (key fields shown):

```json
{
    "url": "https://test-portal.example.com/api/marketplace-provider-offerings/<offering-uuid>/",
    "uuid": "<offering-uuid>",
    "created": "2025-02-04T08:37:14.715810Z",
    "name": "Test Cluster",
    "state": "Draft",
    "type": "Marketplace.Slurm",
    "shared": true,
    "components": [
        {
            "uuid": "<component-uuid>",
            "billing_type": "usage",
            "type": "node_hours",
            "name": "Node hours",
            "measured_unit": "Node-hours"
        }
    ],
    "plans": [
        {
            "uuid": "<plan-uuid>",
            "name": "Default",
            "unit": "month",
            "is_active": true
        }
    ]
}
```

!!! tip
    Save the offering `uuid` from the response — you will need it for subsequent steps.

### Step 2: Configure Integration Options

For automated management of offering-related accounts, the service provider should configure the integration options.

#### Example request

```http
POST https://test-portal.example.com/api/marketplace-provider-offerings/<offering-uuid>/update_integration/
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

#### Integration option fields

| Field | Description |
|-------|-------------|
| `homedir_prefix` | Base path for user home directories |
| `initial_uidnumber` | Starting UID number for new users |
| `initial_usergroup_number` | Starting GID number for user groups |
| `initial_primarygroup_number` | Starting GID number for primary groups |
| `username_anonymized_prefix` | Prefix for anonymized usernames |
| `username_generation_policy` | How usernames are generated (e.g. `waldur_username`) |
| `account_name_generation_policy` | How SLURM account names are generated (e.g. `project_slug`) |
| `supports_pausing` | Whether the offering supports pausing allocations |
| `supports_downscaling` | Whether the offering supports reducing allocation limits |
| `service_provider_can_create_offering_user` | Whether the provider can create offering users directly |

#### Example response

Status code: `200`, empty body.

### Step 3: Activate the Offering

After creation, the offering is in `Draft` state — the service provider can edit it, but it is hidden from the Waldur marketplace. To publish it, the service provider must activate the offering.

!!! note
    After activation, the offering state switches to `Active` and users of the marketplace can order resources.

#### Example request

```http
POST https://test-portal.example.com/api/marketplace-provider-offerings/<offering-uuid>/activate/
Authorization: Token <Org Owner Token>
Content-Type: application/json
```

!!! tip
    This endpoint does not require a request body.

#### Example response

Status code: `201`, empty body.

### Step 4: Create a Service Account User

Waldur Site Agent needs a service account with access to the offering. This step creates a dedicated user for the agent.

!!! warning
    This endpoint requires a **staff token**.

#### Example request

```http
POST https://test-portal.example.com/api/users/
Authorization: Token <Staff Token>
Content-Type: application/json
```

Body:

```json
{
    "username": "site-agent-service-account",
    "email": "site-agent@example.com",
    "is_staff": false,
    "is_active": true,
    "is_support": false,
    "agree_with_policy": true,
    "first_name": "Site Agent",
    "last_name": "Service Account"
}
```

#### Example response

Status code: `201`

Body (key fields shown):

```json
{
    "url": "https://test-portal.example.com/api/users/<user-uuid>/",
    "uuid": "<user-uuid>",
    "username": "site-agent-service-account",
    "full_name": "Site Agent Service Account",
    "email": "site-agent@example.com",
    "is_staff": false,
    "is_active": true,
    "is_support": false,
    "registration_method": "default",
    "date_joined": "2025-02-05T13:43:18.365132Z"
}
```

!!! tip
    Save the `uuid` from the response — you will need it in the following steps.

### Step 5: Assign Service Provider Permissions

Grant the service account permissions for offering management using the `OFFERING.MANAGER` role.

#### Example request

```http
POST https://test-portal.example.com/api/marketplace-provider-offerings/<offering-uuid>/add_user/
Authorization: Token <Org Owner Token>
Content-Type: application/json
```

Body:

```json
{
    "role": "OFFERING.MANAGER",
    "user": "<user-uuid>"
}
```

#### Example response

Status code: `201`, empty body.

### Step 6: Retrieve the Service Account Token

Fetch the service account token to configure [Waldur Site Agent](../admin-guide/providers/site-agent/index.md).

!!! warning
    This endpoint requires a **staff token**.

#### Example request

```http
GET https://test-portal.example.com/api/users/<user-uuid>/token/
Authorization: Token <Staff Token>
```

#### Example response

Status code: `200`

```json
{
    "created": "2025-02-06T12:09:46.296525Z",
    "token": "<auth-token>",
    "user_first_name": "Site Agent",
    "user_is_active": true,
    "user_last_name": "Service Account",
    "user_token_lifetime": "3600",
    "user_username": "site-agent-service-account"
}
```

Use the returned `token` value in the Site Agent configuration.

### Refreshing the Service Account Token

If you need to rotate the token, use the `refresh_token` endpoint.

#### Example request

```http
POST https://test-portal.example.com/api/users/<user-uuid>/refresh_token/
Authorization: Token <Staff Token>
Content-Type: application/json
```

!!! tip
    This endpoint does not require a request body.

#### Example response

Status code: `201`

```json
{
    "created": "2025-02-06T12:14:02.899419Z",
    "token": "<new-auth-token>",
    "user_first_name": "Site Agent",
    "user_is_active": true,
    "user_last_name": "Service Account",
    "user_token_lifetime": "3600",
    "user_username": "site-agent-service-account"
}
```

!!! warning
    After refreshing, the previous token is invalidated. Update the Site Agent configuration with the new token.

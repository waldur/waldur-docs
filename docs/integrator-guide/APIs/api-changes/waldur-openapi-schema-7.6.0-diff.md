# OpenAPI schema diff - 7.6.0

## For version 7.6.0

### New Endpoints: 3

--------------------
GET /api/customer-credits/{uuid}/consumptions/  
GET /api/invoice-items/{uuid}/consumptions/  
POST /api/marketplace-provider-offerings/{uuid}/move_offering/  

### Deleted Endpoints: None

---------------------------

### Modified Endpoints: 24

--------------------------
GET /api/booking-resources/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [service_settings_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: service_settings_uuid
              - Modified property: limit_usage
                - Type changed from 'number' to 'object'
                - Format changed from 'double' to ''
                - Nullable changed from true to false
                - AdditionalProperties changed
                  - Schema added

GET /api/booking-resources/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [service_settings_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: service_settings_uuid
            - Modified property: limit_usage
              - Type changed from 'number' to 'object'
              - Format changed from 'double' to ''
              - Nullable changed from true to false
              - AdditionalProperties changed
                - Schema added

POST /api/marketplace-provider-offerings/{uuid}/import_resource/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: service_settings_uuid
            - Modified property: limit_usage
              - Type changed from 'number' to 'object'
              - Format changed from 'double' to ''
              - Nullable changed from true to false
              - AdditionalProperties changed
                - Schema added

GET /api/marketplace-provider-offerings/{uuid}/list_customer_users/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: notifications_enabled

GET /api/marketplace-provider-resources/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [service_settings_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: service_settings_uuid
              - Modified property: limit_usage
                - Type changed from 'number' to 'object'
                - Format changed from 'double' to ''
                - Nullable changed from true to false
                - AdditionalProperties changed
                  - Schema added

GET /api/marketplace-provider-resources/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [service_settings_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: service_settings_uuid
            - Modified property: limit_usage
              - Type changed from 'number' to 'object'
              - Format changed from 'double' to ''
              - Nullable changed from true to false
              - AdditionalProperties changed
                - Schema added

GET /api/marketplace-provider-resources/{uuid}/details/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [service_settings_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: service_settings_uuid
            - Modified property: limit_usage
              - Type changed from 'number' to 'object'
              - Format changed from 'double' to ''
              - Nullable changed from true to false
              - AdditionalProperties changed
                - Schema added

POST /api/marketplace-provider-resources/{uuid}/move_resource/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: service_settings_uuid
            - Modified property: limit_usage
              - Type changed from 'number' to 'object'
              - Format changed from 'double' to ''
              - Nullable changed from true to false
              - AdditionalProperties changed
                - Schema added

POST /api/marketplace-provider-resources/{uuid}/refresh_last_sync/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: service_settings_uuid
            - Modified property: limit_usage
              - Type changed from 'number' to 'object'
              - Format changed from 'double' to ''
              - Nullable changed from true to false
              - AdditionalProperties changed
                - Schema added

POST /api/marketplace-provider-resources/{uuid}/set_as_ok/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: service_settings_uuid
            - Modified property: limit_usage
              - Type changed from 'number' to 'object'
              - Format changed from 'double' to ''
              - Nullable changed from true to false
              - AdditionalProperties changed
                - Schema added

POST /api/marketplace-provider-resources/{uuid}/set_end_date_by_provider/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: service_settings_uuid
            - Modified property: limit_usage
              - Type changed from 'number' to 'object'
              - Format changed from 'double' to ''
              - Nullable changed from true to false
              - AdditionalProperties changed
                - Schema added

GET /api/marketplace-resources/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [service_settings_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: service_settings_uuid
              - Modified property: limit_usage
                - Type changed from 'number' to 'object'
                - Format changed from 'double' to ''
                - Nullable changed from true to false
                - AdditionalProperties changed
                  - Schema added

GET /api/marketplace-resources/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [service_settings_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: service_settings_uuid
            - Modified property: limit_usage
              - Type changed from 'number' to 'object'
              - Format changed from 'double' to ''
              - Nullable changed from true to false
              - AdditionalProperties changed
                - Schema added

GET /api/marketplace-resources/{uuid}/details/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [service_settings_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: service_settings_uuid
            - Modified property: limit_usage
              - Type changed from 'number' to 'object'
              - Format changed from 'double' to ''
              - Nullable changed from true to false
              - AdditionalProperties changed
                - Schema added

POST /api/marketplace-resources/{uuid}/move_resource/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: service_settings_uuid
            - Modified property: limit_usage
              - Type changed from 'number' to 'object'
              - Format changed from 'double' to ''
              - Nullable changed from true to false
              - AdditionalProperties changed
                - Schema added

GET /api/override-settings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: CALL_MANAGEMENT_HERO_IMAGE
            - New property: MARKETPLACE_HERO_IMAGE

POST /api/override-settings/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: CALL_MANAGEMENT_HERO_IMAGE
          - New property: MARKETPLACE_HERO_IMAGE

GET /api/promotions-campaigns/{uuid}/resources/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: service_settings_uuid
              - Modified property: limit_usage
                - Type changed from 'number' to 'object'
                - Format changed from 'double' to ''
                - Nullable changed from true to false
                - AdditionalProperties changed
                  - Schema added

GET /api/users/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [notifications_enabled]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: notifications_enabled

POST /api/users/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: notifications_enabled
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: notifications_enabled

GET /api/users/me/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [notifications_enabled]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: notifications_enabled

GET /api/users/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [notifications_enabled]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: notifications_enabled

PATCH /api/users/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: notifications_enabled
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: notifications_enabled

PUT /api/users/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: notifications_enabled
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: notifications_enabled

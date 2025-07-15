# OpenAPI schema diff - 7.7.0

## For version 7.7.0

### New Endpoints: 8

--------------------
POST /api/broadcast-messages/{uuid}/schedule/  
GET /api/call-proposal-project-role-mappings/  
POST /api/call-proposal-project-role-mappings/  
DELETE /api/call-proposal-project-role-mappings/{uuid}/  
GET /api/call-proposal-project-role-mappings/{uuid}/  
PATCH /api/call-proposal-project-role-mappings/{uuid}/  
PUT /api/call-proposal-project-role-mappings/{uuid}/  
DELETE /api/marketplace-plans/{uuid}/  

### Deleted Endpoints: 6

------------------------
GET /api/autoprovisioning-rule-plans/  
POST /api/autoprovisioning-rule-plans/  
DELETE /api/autoprovisioning-rule-plans/{uuid}/  
GET /api/autoprovisioning-rule-plans/{uuid}/  
PATCH /api/autoprovisioning-rule-plans/{uuid}/  
PUT /api/autoprovisioning-rule-plans/{uuid}/  

### Modified Endpoints: 36

--------------------------
GET /api/autoprovisioning-rules/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: customer_name
              - New required property: customer_uuid
              - New required property: name
              - New required property: project_role_description
              - New required property: project_role_dispay_name
              - Deleted required property: plans
            - Properties changed
              - New property: customer_name
              - New property: customer_uuid
              - New property: name
              - New property: plan
              - New property: plan_attributes
              - New property: plan_limits
              - New property: project_role_description
              - New property: project_role_dispay_name
              - Deleted property: plans

POST /api/autoprovisioning-rules/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Required changed
          - New required property: name
        - Properties changed
          - New property: name
          - New property: plan
          - New property: plan_attributes
          - New property: plan_limits
          - New property: project_role_name
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: customer_name
            - New required property: customer_uuid
            - New required property: name
            - New required property: project_role_description
            - New required property: project_role_dispay_name
            - Deleted required property: plans
          - Properties changed
            - New property: customer_name
            - New property: customer_uuid
            - New property: name
            - New property: plan
            - New property: plan_attributes
            - New property: plan_limits
            - New property: project_role_description
            - New property: project_role_dispay_name
            - Deleted property: plans

GET /api/autoprovisioning-rules/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: customer_name
            - New required property: customer_uuid
            - New required property: name
            - New required property: project_role_description
            - New required property: project_role_dispay_name
            - Deleted required property: plans
          - Properties changed
            - New property: customer_name
            - New property: customer_uuid
            - New property: name
            - New property: plan
            - New property: plan_attributes
            - New property: plan_limits
            - New property: project_role_description
            - New property: project_role_dispay_name
            - Deleted property: plans

PATCH /api/autoprovisioning-rules/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: name
          - New property: plan
          - New property: plan_attributes
          - New property: plan_limits
          - New property: project_role_name
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: customer_name
            - New required property: customer_uuid
            - New required property: name
            - New required property: project_role_description
            - New required property: project_role_dispay_name
            - Deleted required property: plans
          - Properties changed
            - New property: customer_name
            - New property: customer_uuid
            - New property: name
            - New property: plan
            - New property: plan_attributes
            - New property: plan_limits
            - New property: project_role_description
            - New property: project_role_dispay_name
            - Deleted property: plans

PUT /api/autoprovisioning-rules/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Required changed
          - New required property: name
        - Properties changed
          - New property: name
          - New property: plan
          - New property: plan_attributes
          - New property: plan_limits
          - New property: project_role_name
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: customer_name
            - New required property: customer_uuid
            - New required property: name
            - New required property: project_role_description
            - New required property: project_role_dispay_name
            - Deleted required property: plans
          - Properties changed
            - New property: customer_name
            - New property: customer_uuid
            - New property: name
            - New property: plan
            - New property: plan_attributes
            - New property: plan_limits
            - New property: project_role_description
            - New property: project_role_dispay_name
            - Deleted property: plans

GET /api/hooks-email/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: event_types
                - Items changed
                  - New enum values: [marketplace_plan_deleted]

POST /api/hooks-email/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [marketplace_plan_deleted]
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [marketplace_plan_deleted]

GET /api/hooks-email/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [marketplace_plan_deleted]

PATCH /api/hooks-email/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [marketplace_plan_deleted]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [marketplace_plan_deleted]

PUT /api/hooks-email/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [marketplace_plan_deleted]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [marketplace_plan_deleted]

GET /api/hooks-web/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: event_types
                - Items changed
                  - New enum values: [marketplace_plan_deleted]

POST /api/hooks-web/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [marketplace_plan_deleted]
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [marketplace_plan_deleted]

GET /api/hooks-web/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [marketplace_plan_deleted]

PATCH /api/hooks-web/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [marketplace_plan_deleted]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [marketplace_plan_deleted]

PUT /api/hooks-web/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [marketplace_plan_deleted]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [marketplace_plan_deleted]

GET /api/marketplace-orders/{uuid}/offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: google_calendar_link
              - Description changed from '' to 'Get the Google Calendar link for an offering.'

GET /api/marketplace-provider-offerings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: google_calendar_link
                - Description changed from '' to 'Get the Google Calendar link for an offering.'

GET /api/marketplace-provider-offerings/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: google_calendar_link
              - Description changed from '' to 'Get the Google Calendar link for an offering.'

GET /api/marketplace-provider-offerings/{uuid}/list_customer_service_accounts/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: google_calendar_link
              - Description changed from '' to 'Get the Google Calendar link for an offering.'

GET /api/marketplace-provider-offerings/{uuid}/list_project_service_accounts/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: google_calendar_link
              - Description changed from '' to 'Get the Google Calendar link for an offering.'

POST /api/marketplace-provider-offerings/{uuid}/move_offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: google_calendar_link
              - Description changed from '' to 'Get the Google Calendar link for an offering.'

GET /api/marketplace-provider-offerings/{uuid}/stats/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: google_calendar_link
              - Description changed from '' to 'Get the Google Calendar link for an offering.'

POST /api/marketplace-provider-offerings/{uuid}/update_image/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: google_calendar_link
              - Description changed from '' to 'Get the Google Calendar link for an offering.'

GET /api/marketplace-provider-offerings/{uuid}/user_has_resource_access/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: google_calendar_link
              - Description changed from '' to 'Get the Google Calendar link for an offering.'

GET /api/marketplace-provider-resources/{uuid}/offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: google_calendar_link
              - Description changed from '' to 'Get the Google Calendar link for an offering.'

GET /api/marketplace-public-offerings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: google_calendar_link
                - Description changed from '' to 'Get the Google Calendar link for an offering.'

GET /api/marketplace-public-offerings/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: google_calendar_link
              - Description changed from '' to 'Get the Google Calendar link for an offering.'

GET /api/marketplace-resources/{uuid}/offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: google_calendar_link
              - Description changed from '' to 'Get the Google Calendar link for an offering.'

POST /api/marketplace-script-dry-run/{uuid}/async_run/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: google_calendar_link
              - Description changed from '' to 'Get the Google Calendar link for an offering.'

POST /api/marketplace-script-dry-run/{uuid}/run/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: google_calendar_link
              - Description changed from '' to 'Get the Google Calendar link for an offering.'

GET /api/proposal-protected-calls/

- Modified query param: field
  - Schema changed
    - Items changed
      - Deleted enum values: [default_project_role default_project_role_description default_project_role_name]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Deleted property: default_project_role
              - Deleted property: default_project_role_description
              - Deleted property: default_project_role_name

POST /api/proposal-protected-calls/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Deleted property: default_project_role
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: default_project_role
            - Deleted property: default_project_role_description
            - Deleted property: default_project_role_name

GET /api/proposal-protected-calls/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - Deleted enum values: [default_project_role default_project_role_description default_project_role_name]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: default_project_role
            - Deleted property: default_project_role_description
            - Deleted property: default_project_role_name

PATCH /api/proposal-protected-calls/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Deleted property: default_project_role
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: default_project_role
            - Deleted property: default_project_role_description
            - Deleted property: default_project_role_name

PUT /api/proposal-protected-calls/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Deleted property: default_project_role
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: default_project_role
            - Deleted property: default_project_role_description
            - Deleted property: default_project_role_name

POST /api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/close/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Deleted property: default_project_role
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: default_project_role
            - Deleted property: default_project_role_description
            - Deleted property: default_project_role_name

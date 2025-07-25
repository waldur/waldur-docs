# OpenAPI schema diff - 7.7.3

## For version 7.7.3

### New Endpoints: 3

--------------------
POST /api/marketplace-offering-users/{uuid}/set_pending_account_linking/  
POST /api/marketplace-offering-users/{uuid}/set_pending_additional_validation/  
POST /api/marketplace-offering-users/{uuid}/set_validation_complete/  

### Deleted Endpoints: None

---------------------------

### Modified Endpoints: 39

--------------------------
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
                  - New enum values: [marketplace_offering_user_updated]

POST /api/hooks-email/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [marketplace_offering_user_updated]
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [marketplace_offering_user_updated]

GET /api/hooks-email/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [marketplace_offering_user_updated]

PATCH /api/hooks-email/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [marketplace_offering_user_updated]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [marketplace_offering_user_updated]

PUT /api/hooks-email/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [marketplace_offering_user_updated]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [marketplace_offering_user_updated]

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
                  - New enum values: [marketplace_offering_user_updated]

POST /api/hooks-web/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [marketplace_offering_user_updated]
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [marketplace_offering_user_updated]

GET /api/hooks-web/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [marketplace_offering_user_updated]

PATCH /api/hooks-web/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [marketplace_offering_user_updated]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [marketplace_offering_user_updated]

PUT /api/hooks-web/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [marketplace_offering_user_updated]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [marketplace_offering_user_updated]

GET /api/marketplace-maintenance-announcement-offerings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: impact_level_display
              - New required property: offering_name
            - Properties changed
              - New property: impact_level_display
              - New property: offering_name

POST /api/marketplace-maintenance-announcement-offerings/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: impact_level_display
            - New required property: offering_name
          - Properties changed
            - New property: impact_level_display
            - New property: offering_name

GET /api/marketplace-maintenance-announcement-offerings/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: impact_level_display
            - New required property: offering_name
          - Properties changed
            - New property: impact_level_display
            - New property: offering_name

PATCH /api/marketplace-maintenance-announcement-offerings/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: impact_level_display
            - New required property: offering_name
          - Properties changed
            - New property: impact_level_display
            - New property: offering_name

PUT /api/marketplace-maintenance-announcement-offerings/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: impact_level_display
            - New required property: offering_name
          - Properties changed
            - New property: impact_level_display
            - New property: offering_name

GET /api/marketplace-maintenance-announcements-template/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: affected_offerings
                - Items changed
                  - Required changed
                    - New required property: impact_level_display
                    - New required property: offering_name
                  - Properties changed
                    - New property: impact_level_display
                    - New property: offering_name

POST /api/marketplace-maintenance-announcements-template/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: affected_offerings
              - Items changed
                - Required changed
                  - New required property: impact_level_display
                  - New required property: offering_name
                - Properties changed
                  - New property: impact_level_display
                  - New property: offering_name

GET /api/marketplace-maintenance-announcements-template/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: affected_offerings
              - Items changed
                - Required changed
                  - New required property: impact_level_display
                  - New required property: offering_name
                - Properties changed
                  - New property: impact_level_display
                  - New property: offering_name

PATCH /api/marketplace-maintenance-announcements-template/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: affected_offerings
              - Items changed
                - Required changed
                  - New required property: impact_level_display
                  - New required property: offering_name
                - Properties changed
                  - New property: impact_level_display
                  - New property: offering_name

PUT /api/marketplace-maintenance-announcements-template/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: affected_offerings
              - Items changed
                - Required changed
                  - New required property: impact_level_display
                  - New required property: offering_name
                - Properties changed
                  - New property: impact_level_display
                  - New property: offering_name

GET /api/marketplace-maintenance-announcements/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: service_provider_name
            - Properties changed
              - New property: service_provider_name
              - Modified property: affected_offerings
                - Items changed
                  - Required changed
                    - New required property: impact_level_display
                    - New required property: offering_name
                  - Properties changed
                    - New property: impact_level_display
                    - New property: offering_name
              - Modified property: state
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MaintenanceAnnouncementStateEnum
                    - Type changed from 'integer' to 'string'
                    - New enum values: [Draft Scheduled In progress Completed Cancelled]
                    - Deleted enum values: [1 2 3 4 5]

POST /api/marketplace-maintenance-announcements/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: service_provider_name
          - Properties changed
            - New property: service_provider_name
            - Modified property: affected_offerings
              - Items changed
                - Required changed
                  - New required property: impact_level_display
                  - New required property: offering_name
                - Properties changed
                  - New property: impact_level_display
                  - New property: offering_name
            - Modified property: state
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MaintenanceAnnouncementStateEnum
                  - Type changed from 'integer' to 'string'
                  - New enum values: [Draft Scheduled In progress Completed Cancelled]
                  - Deleted enum values: [1 2 3 4 5]

GET /api/marketplace-maintenance-announcements/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: service_provider_name
          - Properties changed
            - New property: service_provider_name
            - Modified property: affected_offerings
              - Items changed
                - Required changed
                  - New required property: impact_level_display
                  - New required property: offering_name
                - Properties changed
                  - New property: impact_level_display
                  - New property: offering_name
            - Modified property: state
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MaintenanceAnnouncementStateEnum
                  - Type changed from 'integer' to 'string'
                  - New enum values: [Draft Scheduled In progress Completed Cancelled]
                  - Deleted enum values: [1 2 3 4 5]

PATCH /api/marketplace-maintenance-announcements/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: service_provider_name
          - Properties changed
            - New property: service_provider_name
            - Modified property: affected_offerings
              - Items changed
                - Required changed
                  - New required property: impact_level_display
                  - New required property: offering_name
                - Properties changed
                  - New property: impact_level_display
                  - New property: offering_name
            - Modified property: state
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MaintenanceAnnouncementStateEnum
                  - Type changed from 'integer' to 'string'
                  - New enum values: [Draft Scheduled In progress Completed Cancelled]
                  - Deleted enum values: [1 2 3 4 5]

PUT /api/marketplace-maintenance-announcements/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: service_provider_name
          - Properties changed
            - New property: service_provider_name
            - Modified property: affected_offerings
              - Items changed
                - Required changed
                  - New required property: impact_level_display
                  - New required property: offering_name
                - Properties changed
                  - New property: impact_level_display
                  - New property: offering_name
            - Modified property: state
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MaintenanceAnnouncementStateEnum
                  - Type changed from 'integer' to 'string'
                  - New enum values: [Draft Scheduled In progress Completed Cancelled]
                  - Deleted enum values: [1 2 3 4 5]

GET /api/marketplace-offering-users/

- New query param: state
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [service_provider_comment state]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: service_provider_comment
              - New property: state

POST /api/marketplace-offering-users/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: service_provider_comment
            - New property: state

GET /api/marketplace-offering-users/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [service_provider_comment state]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: service_provider_comment
            - New property: state

PATCH /api/marketplace-offering-users/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: service_provider_comment
            - New property: state

PUT /api/marketplace-offering-users/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: service_provider_comment
            - New property: state

POST /api/marketplace-service-providers/{uuid}/set_offerings_username/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: username
            - MinLength changed from 1 to 0

GET /api/user-group-invitations/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: user_affiliations
              - New property: user_email_patterns
              - Modified property: scope_type
                - Nullable changed from false to true

POST /api/user-group-invitations/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: user_affiliations
          - New property: user_email_patterns
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: user_affiliations
            - New property: user_email_patterns
            - Modified property: scope_type
              - Nullable changed from false to true

GET /api/user-group-invitations/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: user_affiliations
            - New property: user_email_patterns
            - Modified property: scope_type
              - Nullable changed from false to true

POST /api/user-group-invitations/{uuid}/submit_request/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: user_affiliations
            - New property: user_email_patterns
            - Modified property: scope_type
              - Nullable changed from false to true

GET /api/user-invitations/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: scope_type
                - Nullable changed from false to true

POST /api/user-invitations/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: scope_type
              - Nullable changed from false to true

GET /api/user-invitations/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: scope_type
              - Nullable changed from false to true

GET /api/user-invitations/{uuid}/details/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: scope_type
              - Nullable changed from false to true

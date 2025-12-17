# OpenAPI schema diff - 7.9.5

## For version 7.9.5

### New Endpoints: None

-----------------------

### Deleted Endpoints: None

---------------------------

### Modified Endpoints: 48

--------------------------
GET /api/booking-offerings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: plugin_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedPluginOptions
                    - Properties changed
                      - New property: enable_display_of_order_actions_for_service_provider

GET /api/booking-offerings/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: enable_display_of_order_actions_for_service_provider

GET /api/marketplace-orders/

- New query param: resource_name

HEAD /api/marketplace-orders/

- New query param: resource_name

GET /api/marketplace-orders/{uuid}/offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: enable_display_of_order_actions_for_service_provider

GET /api/marketplace-provider-offerings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: plugin_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedPluginOptions
                    - Properties changed
                      - New property: enable_display_of_order_actions_for_service_provider

POST /api/marketplace-provider-offerings/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: enable_display_of_order_actions_for_service_provider

GET /api/marketplace-provider-offerings/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: enable_display_of_order_actions_for_service_provider

POST /api/marketplace-provider-offerings/{uuid}/move_offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: enable_display_of_order_actions_for_service_provider

POST /api/marketplace-provider-offerings/{uuid}/update_integration/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: plugin_options
            - Properties changed
              - New property: enable_display_of_order_actions_for_service_provider

GET /api/marketplace-provider-offerings/{uuid}/user_has_resource_access/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: enable_display_of_order_actions_for_service_provider

GET /api/marketplace-provider-resources/{uuid}/offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: enable_display_of_order_actions_for_service_provider

GET /api/marketplace-public-offerings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: plugin_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedPluginOptions
                    - Properties changed
                      - New property: enable_display_of_order_actions_for_service_provider

GET /api/marketplace-public-offerings/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: enable_display_of_order_actions_for_service_provider

GET /api/marketplace-resources/{uuid}/offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: enable_display_of_order_actions_for_service_provider

GET /api/marketplace-robot-accounts/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: offering_plugin_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedPluginOptions
                    - Properties changed
                      - New property: enable_display_of_order_actions_for_service_provider

GET /api/marketplace-robot-accounts/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: offering_plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: enable_display_of_order_actions_for_service_provider

POST /api/marketplace-robot-accounts/{uuid}/set_state_creating/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: offering_plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: enable_display_of_order_actions_for_service_provider

POST /api/marketplace-robot-accounts/{uuid}/set_state_deleted/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: offering_plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: enable_display_of_order_actions_for_service_provider

POST /api/marketplace-robot-accounts/{uuid}/set_state_erred/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: offering_plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: enable_display_of_order_actions_for_service_provider

POST /api/marketplace-robot-accounts/{uuid}/set_state_ok/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: offering_plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: enable_display_of_order_actions_for_service_provider

POST /api/marketplace-robot-accounts/{uuid}/set_state_request_deletion/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: offering_plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: enable_display_of_order_actions_for_service_provider

POST /api/marketplace-script-dry-run/{uuid}/async_run/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: enable_display_of_order_actions_for_service_provider

POST /api/marketplace-script-dry-run/{uuid}/run/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: enable_display_of_order_actions_for_service_provider

GET /api/onboarding-justifications/

- New query param: user_uuid
- New query param: verification_uuid
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: onboarding_metadata
              - New required property: user_full_name
              - New required property: user_submitted_customer_data
            - Properties changed
              - New property: onboarding_metadata
              - New property: user_full_name
              - New property: user_submitted_customer_data

HEAD /api/onboarding-justifications/

- New query param: user_uuid
- New query param: verification_uuid

POST /api/onboarding-justifications/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: onboarding_metadata
            - New required property: user_full_name
            - New required property: user_submitted_customer_data
          - Properties changed
            - New property: onboarding_metadata
            - New property: user_full_name
            - New property: user_submitted_customer_data

POST /api/onboarding-justifications/create_justification/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: onboarding_metadata
            - New required property: user_full_name
            - New required property: user_submitted_customer_data
          - Properties changed
            - New property: onboarding_metadata
            - New property: user_full_name
            - New property: user_submitted_customer_data

GET /api/onboarding-justifications/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: onboarding_metadata
            - New required property: user_full_name
            - New required property: user_submitted_customer_data
          - Properties changed
            - New property: onboarding_metadata
            - New property: user_full_name
            - New property: user_submitted_customer_data

PATCH /api/onboarding-justifications/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: onboarding_metadata
            - New required property: user_full_name
            - New required property: user_submitted_customer_data
          - Properties changed
            - New property: onboarding_metadata
            - New property: user_full_name
            - New property: user_submitted_customer_data

PUT /api/onboarding-justifications/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: onboarding_metadata
            - New required property: user_full_name
            - New required property: user_submitted_customer_data
          - Properties changed
            - New property: onboarding_metadata
            - New property: user_full_name
            - New property: user_submitted_customer_data

POST /api/onboarding-justifications/{uuid}/approve/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: onboarding_metadata
            - New required property: user_full_name
            - New required property: user_submitted_customer_data
          - Properties changed
            - New property: onboarding_metadata
            - New property: user_full_name
            - New property: user_submitted_customer_data

POST /api/onboarding-justifications/{uuid}/reject/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: onboarding_metadata
            - New required property: user_full_name
            - New required property: user_submitted_customer_data
          - Properties changed
            - New property: onboarding_metadata
            - New property: user_full_name
            - New property: user_submitted_customer_data

GET /api/onboarding-verifications/

- New query param: country
- New query param: legal_name
- New query param: legal_person_identifier
- New query param: status
- New query param: user_uuid
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: user_full_name
            - Properties changed
              - New property: user_full_name
              - Modified property: customer
                - Type changed from 'integer' to 'string'
                - Format changed from '' to 'uri'
              - Modified property: user
                - Type changed from 'integer' to 'string'
                - Format changed from '' to 'uri'
                - ReadOnly changed from false to true

HEAD /api/onboarding-verifications/

- New query param: country
- New query param: legal_name
- New query param: legal_person_identifier
- New query param: status
- New query param: user_uuid

POST /api/onboarding-verifications/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Required changed
          - Deleted required property: user
        - Properties changed
          - Deleted property: user
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: user_full_name
          - Properties changed
            - New property: user_full_name
            - Modified property: customer
              - Type changed from 'integer' to 'string'
              - Format changed from '' to 'uri'
            - Modified property: user
              - Type changed from 'integer' to 'string'
              - Format changed from '' to 'uri'
              - ReadOnly changed from false to true

POST /api/onboarding-verifications/start_verification/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: user_full_name
          - Properties changed
            - New property: user_full_name
            - Modified property: customer
              - Type changed from 'integer' to 'string'
              - Format changed from '' to 'uri'
            - Modified property: user
              - Type changed from 'integer' to 'string'
              - Format changed from '' to 'uri'
              - ReadOnly changed from false to true

GET /api/onboarding-verifications/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: user_full_name
          - Properties changed
            - New property: user_full_name
            - Modified property: customer
              - Type changed from 'integer' to 'string'
              - Format changed from '' to 'uri'
            - Modified property: user
              - Type changed from 'integer' to 'string'
              - Format changed from '' to 'uri'
              - ReadOnly changed from false to true

PATCH /api/onboarding-verifications/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Deleted property: user
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: user_full_name
          - Properties changed
            - New property: user_full_name
            - Modified property: customer
              - Type changed from 'integer' to 'string'
              - Format changed from '' to 'uri'
            - Modified property: user
              - Type changed from 'integer' to 'string'
              - Format changed from '' to 'uri'
              - ReadOnly changed from false to true

PUT /api/onboarding-verifications/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Required changed
          - Deleted required property: user
        - Properties changed
          - Deleted property: user
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: user_full_name
          - Properties changed
            - New property: user_full_name
            - Modified property: customer
              - Type changed from 'integer' to 'string'
              - Format changed from '' to 'uri'
            - Modified property: user
              - Type changed from 'integer' to 'string'
              - Format changed from '' to 'uri'
              - ReadOnly changed from false to true

POST /api/onboarding-verifications/{uuid}/run_validation/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: user_full_name
          - Properties changed
            - New property: user_full_name
            - Modified property: customer
              - Type changed from 'integer' to 'string'
              - Format changed from '' to 'uri'
            - Modified property: user
              - Type changed from 'integer' to 'string'
              - Format changed from '' to 'uri'
              - ReadOnly changed from false to true

GET /api/openportal-managed-projects/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: project_template_data
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/ProjectTemplate
                    - Properties changed
                      - Modified property: offerings_data
                        - Items changed
                          - Properties changed
                            - Modified property: plugin_options
                              - Property 'AllOf' changed
                                - Modified schema: #/components/schemas/MergedPluginOptions
                                  - Properties changed
                                    - New property: enable_display_of_order_actions_for_service_provider

GET /api/openportal-managed-projects/{identifier}/{destination}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: project_template_data
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/ProjectTemplate
                  - Properties changed
                    - Modified property: offerings_data
                      - Items changed
                        - Properties changed
                          - Modified property: plugin_options
                            - Property 'AllOf' changed
                              - Modified schema: #/components/schemas/MergedPluginOptions
                                - Properties changed
                                  - New property: enable_display_of_order_actions_for_service_provider

GET /api/openportal-project-template/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: offerings_data
                - Items changed
                  - Properties changed
                    - Modified property: plugin_options
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/MergedPluginOptions
                          - Properties changed
                            - New property: enable_display_of_order_actions_for_service_provider

POST /api/openportal-project-template/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: offerings_data
              - Items changed
                - Properties changed
                  - Modified property: plugin_options
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/MergedPluginOptions
                        - Properties changed
                          - New property: enable_display_of_order_actions_for_service_provider

GET /api/openportal-project-template/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: offerings_data
              - Items changed
                - Properties changed
                  - Modified property: plugin_options
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/MergedPluginOptions
                        - Properties changed
                          - New property: enable_display_of_order_actions_for_service_provider

PATCH /api/openportal-project-template/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: offerings_data
              - Items changed
                - Properties changed
                  - Modified property: plugin_options
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/MergedPluginOptions
                        - Properties changed
                          - New property: enable_display_of_order_actions_for_service_provider

PUT /api/openportal-project-template/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: offerings_data
              - Items changed
                - Properties changed
                  - Modified property: plugin_options
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/MergedPluginOptions
                        - Properties changed
                          - New property: enable_display_of_order_actions_for_service_provider

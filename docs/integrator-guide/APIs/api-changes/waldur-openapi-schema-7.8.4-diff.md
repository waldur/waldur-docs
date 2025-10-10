# OpenAPI schema diff - 7.8.4

## For version 7.8.4

### New Endpoints: 28

---------------------
GET /api/marketplace-offering-users/checklist-template/  
HEAD /api/marketplace-offering-users/checklist-template/  
GET /api/marketplace-provider-offerings/{uuid}/tos_stats/  
POST /api/marketplace-provider-resources/{uuid}/update_options/  
POST /api/marketplace-resources/{uuid}/renew/  
GET /api/onboarding-justifications/  
HEAD /api/onboarding-justifications/  
POST /api/onboarding-justifications/  
POST /api/onboarding-justifications/create_justification/  
DELETE /api/onboarding-justifications/{uuid}/  
GET /api/onboarding-justifications/{uuid}/  
PATCH /api/onboarding-justifications/{uuid}/  
PUT /api/onboarding-justifications/{uuid}/  
POST /api/onboarding-justifications/{uuid}/attach_document/  
GET /api/onboarding-verifications/  
HEAD /api/onboarding-verifications/  
POST /api/onboarding-verifications/  
POST /api/onboarding-verifications/validate_company/  
DELETE /api/onboarding-verifications/{uuid}/  
GET /api/onboarding-verifications/{uuid}/  
PATCH /api/onboarding-verifications/{uuid}/  
PUT /api/onboarding-verifications/{uuid}/  
POST /api/onboarding-verifications/{uuid}/create_customer/  
GET /api/onboarding/supported-countries/  
GET /api/projects/checklist-template/  
HEAD /api/projects/checklist-template/  
GET /api/proposal-proposals/checklist-template/  
HEAD /api/proposal-proposals/checklist-template/  

### Deleted Endpoints: None

---------------------------

### Modified Endpoints: 131

---------------------------
POST /api/backend-resources/{uuid}/import_resource/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: provider_slug
                      - Format changed from 'uuid' to ''
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: provider_slug
                      - Format changed from 'uuid' to ''
            - Modified property: provider_slug
              - Format changed from 'uuid' to ''

GET /api/booking-offerings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: components
                - Items changed
                  - Properties changed
                    - New property: is_prepaid
                    - New property: max_prepaid_duration
                    - New property: min_prepaid_duration
                    - New property: overage_component
              - Modified property: plugin_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedPluginOptions
                    - Properties changed
                      - New property: project_permanent_directory
                      - New property: scratch_project_directory

GET /api/booking-offerings/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: is_prepaid
                  - New property: max_prepaid_duration
                  - New property: min_prepaid_duration
                  - New property: overage_component
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: project_permanent_directory
                    - New property: scratch_project_directory

GET /api/booking-resources/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: creation_order
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - Modified property: provider_slug
                        - Format changed from 'uuid' to ''
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - Modified property: provider_slug
                        - Format changed from 'uuid' to ''
              - Modified property: provider_slug
                - Format changed from 'uuid' to ''

GET /api/booking-resources/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: provider_slug
                      - Format changed from 'uuid' to ''
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: provider_slug
                      - Format changed from 'uuid' to ''
            - Modified property: provider_slug
              - Format changed from 'uuid' to ''

GET /api/call-rounds/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: status
                - Property 'AllOf' changed
                  - Schemas added: #/components/schemas/RoundStatus
                  - Schemas deleted: #/components/schemas/StatusEnum

GET /api/call-rounds/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: status
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/RoundStatus
                - Schemas deleted: #/components/schemas/StatusEnum

GET /api/customers/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [display_billing_info_in_projects]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: display_billing_info_in_projects

POST /api/customers/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: display_billing_info_in_projects

GET /api/customers/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [display_billing_info_in_projects]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: display_billing_info_in_projects

PATCH /api/customers/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: display_billing_info_in_projects

PUT /api/customers/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: display_billing_info_in_projects

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
                  - New enum values: [automatic_credit_adjustment]

POST /api/hooks-email/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [automatic_credit_adjustment]
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [automatic_credit_adjustment]

GET /api/hooks-email/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [automatic_credit_adjustment]

PATCH /api/hooks-email/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [automatic_credit_adjustment]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [automatic_credit_adjustment]

PUT /api/hooks-email/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [automatic_credit_adjustment]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [automatic_credit_adjustment]

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
                  - New enum values: [automatic_credit_adjustment]

POST /api/hooks-web/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [automatic_credit_adjustment]
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [automatic_credit_adjustment]

GET /api/hooks-web/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [automatic_credit_adjustment]

PATCH /api/hooks-web/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [automatic_credit_adjustment]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [automatic_credit_adjustment]

PUT /api/hooks-web/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [automatic_credit_adjustment]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [automatic_credit_adjustment]

GET /api/managed-rancher-cluster-resources/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: creation_order
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - Modified property: provider_slug
                        - Format changed from 'uuid' to ''
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - Modified property: provider_slug
                        - Format changed from 'uuid' to ''
              - Modified property: provider_slug
                - Format changed from 'uuid' to ''

GET /api/managed-rancher-cluster-resources/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: provider_slug
                      - Format changed from 'uuid' to ''
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: provider_slug
                      - Format changed from 'uuid' to ''
            - Modified property: provider_slug
              - Format changed from 'uuid' to ''

GET /api/marketplace-orders/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: provider_slug
                - Format changed from 'uuid' to ''

POST /api/marketplace-orders/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: attributes
            - Property 'OneOf' changed
              - Modified schema: #/components/schemas/OpenStackInstanceCreateOrderAttributes
                - Properties changed
                  - Modified property: floating_ips
                    - Items changed
                      - Properties changed
                        - New property: ip_address
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: provider_slug
              - Format changed from 'uuid' to ''

GET /api/marketplace-orders/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: provider_slug
              - Format changed from 'uuid' to ''

GET /api/marketplace-orders/{uuid}/offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: is_prepaid
                  - New property: max_prepaid_duration
                  - New property: min_prepaid_duration
                  - New property: overage_component
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: project_permanent_directory
                    - New property: scratch_project_directory

GET /api/marketplace-provider-offerings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: components
                - Items changed
                  - Properties changed
                    - New property: is_prepaid
                    - New property: max_prepaid_duration
                    - New property: min_prepaid_duration
                    - New property: overage_component
              - Modified property: plugin_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedPluginOptions
                    - Properties changed
                      - New property: project_permanent_directory
                      - New property: scratch_project_directory

POST /api/marketplace-provider-offerings/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: components
            - Items changed
              - Properties changed
                - New property: is_prepaid
                - New property: max_prepaid_duration
                - New property: min_prepaid_duration
                - New property: overage_component
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Modified property: components
            - Items changed
              - Properties changed
                - New property: is_prepaid
                - New property: max_prepaid_duration
                - New property: min_prepaid_duration
                - New property: overage_component
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Modified property: components
            - Items changed
              - Properties changed
                - New property: is_prepaid
                - New property: max_prepaid_duration
                - New property: min_prepaid_duration
                - New property: overage_component
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: is_prepaid
                  - New property: max_prepaid_duration
                  - New property: min_prepaid_duration
                  - New property: overage_component
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: project_permanent_directory
                    - New property: scratch_project_directory

GET /api/marketplace-provider-offerings/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: is_prepaid
                  - New property: max_prepaid_duration
                  - New property: min_prepaid_duration
                  - New property: overage_component
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: project_permanent_directory
                    - New property: scratch_project_directory

POST /api/marketplace-provider-offerings/{uuid}/create_offering_component/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: is_prepaid
          - New property: max_prepaid_duration
          - New property: min_prepaid_duration
          - New property: overage_component

POST /api/marketplace-provider-offerings/{uuid}/import_resource/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: provider_slug
                      - Format changed from 'uuid' to ''
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: provider_slug
                      - Format changed from 'uuid' to ''
            - Modified property: provider_slug
              - Format changed from 'uuid' to ''

GET /api/marketplace-provider-offerings/{uuid}/list_course_accounts/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: is_prepaid
                  - New property: max_prepaid_duration
                  - New property: min_prepaid_duration
                  - New property: overage_component
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: project_permanent_directory
                    - New property: scratch_project_directory

GET /api/marketplace-provider-offerings/{uuid}/list_customer_projects/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: customer_display_billing_info_in_projects
              - Modified property: end_date
                - Description changed from 'The date is inclusive. Once reached, all project resource will be scheduled for termination.' to ''

GET /api/marketplace-provider-offerings/{uuid}/list_customer_service_accounts/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: is_prepaid
                  - New property: max_prepaid_duration
                  - New property: min_prepaid_duration
                  - New property: overage_component
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: project_permanent_directory
                    - New property: scratch_project_directory

GET /api/marketplace-provider-offerings/{uuid}/list_project_service_accounts/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: is_prepaid
                  - New property: max_prepaid_duration
                  - New property: min_prepaid_duration
                  - New property: overage_component
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: project_permanent_directory
                    - New property: scratch_project_directory

POST /api/marketplace-provider-offerings/{uuid}/move_offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: is_prepaid
                  - New property: max_prepaid_duration
                  - New property: min_prepaid_duration
                  - New property: overage_component
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: project_permanent_directory
                    - New property: scratch_project_directory

GET /api/marketplace-provider-offerings/{uuid}/orders/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: provider_slug
                - Format changed from 'uuid' to ''

GET /api/marketplace-provider-offerings/{uuid}/orders/{order_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: provider_slug
              - Format changed from 'uuid' to ''

GET /api/marketplace-provider-offerings/{uuid}/stats/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: is_prepaid
                  - New property: max_prepaid_duration
                  - New property: min_prepaid_duration
                  - New property: overage_component
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: project_permanent_directory
                    - New property: scratch_project_directory

POST /api/marketplace-provider-offerings/{uuid}/update_image/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: is_prepaid
                  - New property: max_prepaid_duration
                  - New property: min_prepaid_duration
                  - New property: overage_component
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: project_permanent_directory
                    - New property: scratch_project_directory

POST /api/marketplace-provider-offerings/{uuid}/update_integration/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: plugin_options
            - Properties changed
              - New property: project_permanent_directory
              - New property: scratch_project_directory

POST /api/marketplace-provider-offerings/{uuid}/update_offering_component/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: is_prepaid
          - New property: max_prepaid_duration
          - New property: min_prepaid_duration
          - New property: overage_component

GET /api/marketplace-provider-offerings/{uuid}/user_has_resource_access/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: is_prepaid
                  - New property: max_prepaid_duration
                  - New property: min_prepaid_duration
                  - New property: overage_component
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: project_permanent_directory
                    - New property: scratch_project_directory

GET /api/marketplace-provider-resources/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: creation_order
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - Modified property: provider_slug
                        - Format changed from 'uuid' to ''
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - Modified property: provider_slug
                        - Format changed from 'uuid' to ''
              - Modified property: provider_slug
                - Format changed from 'uuid' to ''

GET /api/marketplace-provider-resources/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: provider_slug
                      - Format changed from 'uuid' to ''
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: provider_slug
                      - Format changed from 'uuid' to ''
            - Modified property: provider_slug
              - Format changed from 'uuid' to ''

GET /api/marketplace-provider-resources/{uuid}/details/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: provider_slug
                      - Format changed from 'uuid' to ''
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: provider_slug
                      - Format changed from 'uuid' to ''
            - Modified property: provider_slug
              - Format changed from 'uuid' to ''

POST /api/marketplace-provider-resources/{uuid}/move_resource/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: provider_slug
                      - Format changed from 'uuid' to ''
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: provider_slug
                      - Format changed from 'uuid' to ''
            - Modified property: provider_slug
              - Format changed from 'uuid' to ''

GET /api/marketplace-provider-resources/{uuid}/offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: is_prepaid
                  - New property: max_prepaid_duration
                  - New property: min_prepaid_duration
                  - New property: overage_component
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: project_permanent_directory
                    - New property: scratch_project_directory

POST /api/marketplace-provider-resources/{uuid}/set_end_date_by_provider/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: provider_slug
                      - Format changed from 'uuid' to ''
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: provider_slug
                      - Format changed from 'uuid' to ''
            - Modified property: provider_slug
              - Format changed from 'uuid' to ''

GET /api/marketplace-public-offerings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: components
                - Items changed
                  - Properties changed
                    - New property: is_prepaid
                    - New property: max_prepaid_duration
                    - New property: min_prepaid_duration
                    - New property: overage_component
              - Modified property: plugin_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedPluginOptions
                    - Properties changed
                      - New property: project_permanent_directory
                      - New property: scratch_project_directory

GET /api/marketplace-public-offerings/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: is_prepaid
                  - New property: max_prepaid_duration
                  - New property: min_prepaid_duration
                  - New property: overage_component
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: project_permanent_directory
                    - New property: scratch_project_directory

GET /api/marketplace-resources/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: creation_order
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - Modified property: provider_slug
                        - Format changed from 'uuid' to ''
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - Modified property: provider_slug
                        - Format changed from 'uuid' to ''
              - Modified property: provider_slug
                - Format changed from 'uuid' to ''

GET /api/marketplace-resources/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: provider_slug
                      - Format changed from 'uuid' to ''
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: provider_slug
                      - Format changed from 'uuid' to ''
            - Modified property: provider_slug
              - Format changed from 'uuid' to ''

GET /api/marketplace-resources/{uuid}/details/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: provider_slug
                      - Format changed from 'uuid' to ''
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: provider_slug
                      - Format changed from 'uuid' to ''
            - Modified property: provider_slug
              - Format changed from 'uuid' to ''

POST /api/marketplace-resources/{uuid}/move_resource/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: provider_slug
                      - Format changed from 'uuid' to ''
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: provider_slug
                      - Format changed from 'uuid' to ''
            - Modified property: provider_slug
              - Format changed from 'uuid' to ''

GET /api/marketplace-resources/{uuid}/offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: is_prepaid
                  - New property: max_prepaid_duration
                  - New property: min_prepaid_duration
                  - New property: overage_component
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: project_permanent_directory
                    - New property: scratch_project_directory

POST /api/marketplace-resources/{uuid}/update_options/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/scopes/- with value: 'offering.customer'

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
                      - New property: project_permanent_directory
                      - New property: scratch_project_directory

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
                    - New property: project_permanent_directory
                    - New property: scratch_project_directory

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
                    - New property: project_permanent_directory
                    - New property: scratch_project_directory

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
                    - New property: project_permanent_directory
                    - New property: scratch_project_directory

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
                    - New property: project_permanent_directory
                    - New property: scratch_project_directory

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
                    - New property: project_permanent_directory
                    - New property: scratch_project_directory

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
                    - New property: project_permanent_directory
                    - New property: scratch_project_directory

POST /api/marketplace-script-dry-run/{uuid}/async_run/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: is_prepaid
                  - New property: max_prepaid_duration
                  - New property: min_prepaid_duration
                  - New property: overage_component
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: project_permanent_directory
                    - New property: scratch_project_directory

POST /api/marketplace-script-dry-run/{uuid}/run/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: is_prepaid
                  - New property: max_prepaid_duration
                  - New property: min_prepaid_duration
                  - New property: overage_component
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: project_permanent_directory
                    - New property: scratch_project_directory

GET /api/marketplace-service-providers/{service_provider_uuid}/offerings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: components
                - Items changed
                  - Properties changed
                    - New property: is_prepaid
                    - New property: max_prepaid_duration
                    - New property: min_prepaid_duration
                    - New property: overage_component

GET /api/marketplace-service-providers/{service_provider_uuid}/projects/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_display_billing_info_in_projects]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: customer_display_billing_info_in_projects
              - Modified property: end_date
                - Description changed from 'The date is inclusive. Once reached, all project resource will be scheduled for termination.' to ''

GET /api/notification-messages-templates/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: content
                - Nullable changed from false to true

POST /api/notification-messages-templates/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: content
              - Nullable changed from false to true

GET /api/notification-messages-templates/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: content
              - Nullable changed from false to true

PATCH /api/notification-messages-templates/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: content
              - Nullable changed from false to true

PUT /api/notification-messages-templates/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: content
              - Nullable changed from false to true

GET /api/notification-messages/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: context_schema
              - Deleted required property: context_fields
            - Properties changed
              - New property: context_schema
              - Deleted property: context_fields
              - Modified property: templates
                - Items changed
                  - Properties changed
                    - Modified property: content
                      - Nullable changed from false to true

POST /api/notification-messages/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: context_schema
            - Deleted required property: context_fields
          - Properties changed
            - New property: context_schema
            - Deleted property: context_fields
            - Modified property: templates
              - Items changed
                - Properties changed
                  - Modified property: content
                    - Nullable changed from false to true

GET /api/notification-messages/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: context_schema
            - Deleted required property: context_fields
          - Properties changed
            - New property: context_schema
            - Deleted property: context_fields
            - Modified property: templates
              - Items changed
                - Properties changed
                  - Modified property: content
                    - Nullable changed from false to true

PATCH /api/notification-messages/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: context_schema
            - Deleted required property: context_fields
          - Properties changed
            - New property: context_schema
            - Deleted property: context_fields
            - Modified property: templates
              - Items changed
                - Properties changed
                  - Modified property: content
                    - Nullable changed from false to true

PUT /api/notification-messages/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: context_schema
            - Deleted required property: context_fields
          - Properties changed
            - New property: context_schema
            - Deleted property: context_fields
            - Modified property: templates
              - Items changed
                - Properties changed
                  - Modified property: content
                    - Nullable changed from false to true

POST /api/openstack-backups/{uuid}/restore/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: floating_ips
            - Items changed
              - Properties changed
                - New property: ip_address

POST /api/openstack-instances/{uuid}/update_floating_ips/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: floating_ips
            - Items changed
              - Properties changed
                - New property: ip_address

GET /api/openstack-network-rbac-policies/

- New query param: tenant
- New query param: tenant_uuid

HEAD /api/openstack-network-rbac-policies/

- New query param: tenant
- New query param: tenant_uuid

GET /api/override-settings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: ONBOARDING_ARIREGISTER_BASE_URL
            - New property: ONBOARDING_ARIREGISTER_PASSWORD
            - New property: ONBOARDING_ARIREGISTER_TIMEOUT
            - New property: ONBOARDING_ARIREGISTER_USERNAME
            - New property: ONBOARDING_VERIFICATION_EXPIRY_HOURS

POST /api/override-settings/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: ONBOARDING_ARIREGISTER_BASE_URL
          - New property: ONBOARDING_ARIREGISTER_PASSWORD
          - New property: ONBOARDING_ARIREGISTER_TIMEOUT
          - New property: ONBOARDING_ARIREGISTER_USERNAME
          - New property: ONBOARDING_VERIFICATION_EXPIRY_HOURS
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: ONBOARDING_ARIREGISTER_BASE_URL
          - New property: ONBOARDING_ARIREGISTER_PASSWORD
          - New property: ONBOARDING_ARIREGISTER_TIMEOUT
          - New property: ONBOARDING_ARIREGISTER_USERNAME
          - New property: ONBOARDING_VERIFICATION_EXPIRY_HOURS
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: ONBOARDING_ARIREGISTER_BASE_URL
          - New property: ONBOARDING_ARIREGISTER_PASSWORD
          - New property: ONBOARDING_ARIREGISTER_TIMEOUT
          - New property: ONBOARDING_ARIREGISTER_USERNAME
          - New property: ONBOARDING_VERIFICATION_EXPIRY_HOURS

GET /api/project-credits/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: mark_unused_credit_as_spent_on_project_termination

POST /api/project-credits/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: mark_unused_credit_as_spent_on_project_termination
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: mark_unused_credit_as_spent_on_project_termination

GET /api/project-credits/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: mark_unused_credit_as_spent_on_project_termination

PATCH /api/project-credits/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: mark_unused_credit_as_spent_on_project_termination
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: mark_unused_credit_as_spent_on_project_termination

PUT /api/project-credits/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: mark_unused_credit_as_spent_on_project_termination
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: mark_unused_credit_as_spent_on_project_termination

GET /api/projects/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_display_billing_info_in_projects]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: customer_display_billing_info_in_projects
              - Modified property: end_date
                - Description changed from 'The date is inclusive. Once reached, all project resource will be scheduled for termination.' to ''

POST /api/projects/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: end_date
            - Description changed from 'The date is inclusive. Once reached, all project resource will be scheduled for termination.' to ''
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Modified property: end_date
            - Description changed from 'The date is inclusive. Once reached, all project resource will be scheduled for termination.' to ''
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Modified property: end_date
            - Description changed from 'The date is inclusive. Once reached, all project resource will be scheduled for termination.' to ''
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_display_billing_info_in_projects
            - Modified property: end_date
              - Description changed from 'The date is inclusive. Once reached, all project resource will be scheduled for termination.' to ''

GET /api/projects/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_display_billing_info_in_projects]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_display_billing_info_in_projects
            - Modified property: end_date
              - Description changed from 'The date is inclusive. Once reached, all project resource will be scheduled for termination.' to ''

PATCH /api/projects/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: end_date
            - Description changed from 'The date is inclusive. Once reached, all project resource will be scheduled for termination.' to ''
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Modified property: end_date
            - Description changed from 'The date is inclusive. Once reached, all project resource will be scheduled for termination.' to ''
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Modified property: end_date
            - Description changed from 'The date is inclusive. Once reached, all project resource will be scheduled for termination.' to ''
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_display_billing_info_in_projects
            - Modified property: end_date
              - Description changed from 'The date is inclusive. Once reached, all project resource will be scheduled for termination.' to ''

PUT /api/projects/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: end_date
            - Description changed from 'The date is inclusive. Once reached, all project resource will be scheduled for termination.' to ''
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Modified property: end_date
            - Description changed from 'The date is inclusive. Once reached, all project resource will be scheduled for termination.' to ''
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Modified property: end_date
            - Description changed from 'The date is inclusive. Once reached, all project resource will be scheduled for termination.' to ''
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_display_billing_info_in_projects
            - Modified property: end_date
              - Description changed from 'The date is inclusive. Once reached, all project resource will be scheduled for termination.' to ''

POST /api/projects/{uuid}/move_project/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_display_billing_info_in_projects
            - Modified property: end_date
              - Description changed from 'The date is inclusive. Once reached, all project resource will be scheduled for termination.' to ''

GET /api/promotions-campaigns/{uuid}/orders/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: provider_slug
                - Format changed from 'uuid' to ''

GET /api/promotions-campaigns/{uuid}/resources/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: creation_order
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - Modified property: provider_slug
                        - Format changed from 'uuid' to ''
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - Modified property: provider_slug
                        - Format changed from 'uuid' to ''
              - Modified property: provider_slug
                - Format changed from 'uuid' to ''

GET /api/proposal-proposals/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: round
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/NestedRound
                    - Properties changed
                      - Modified property: status
                        - Property 'AllOf' changed
                          - Schemas added: #/components/schemas/RoundStatus
                          - Schemas deleted: #/components/schemas/StatusEnum

POST /api/proposal-proposals/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: round
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/NestedRound
                  - Properties changed
                    - Modified property: status
                      - Property 'AllOf' changed
                        - Schemas added: #/components/schemas/RoundStatus
                        - Schemas deleted: #/components/schemas/StatusEnum

GET /api/proposal-proposals/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: round
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/NestedRound
                  - Properties changed
                    - Modified property: status
                      - Property 'AllOf' changed
                        - Schemas added: #/components/schemas/RoundStatus
                        - Schemas deleted: #/components/schemas/StatusEnum

GET /api/proposal-proposals/{uuid}/resources/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: requested_offering
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/NestedRequestedOffering
                    - Properties changed
                      - Modified property: components
                        - Items changed
                          - Properties changed
                            - New property: is_prepaid
                            - New property: max_prepaid_duration
                            - New property: min_prepaid_duration
                            - New property: overage_component

POST /api/proposal-proposals/{uuid}/resources/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: requested_offering
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/NestedRequestedOffering
                  - Properties changed
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - New property: is_prepaid
                          - New property: max_prepaid_duration
                          - New property: min_prepaid_duration
                          - New property: overage_component

GET /api/proposal-proposals/{uuid}/resources/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: requested_offering
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/NestedRequestedOffering
                  - Properties changed
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - New property: is_prepaid
                          - New property: max_prepaid_duration
                          - New property: min_prepaid_duration
                          - New property: overage_component

PATCH /api/proposal-proposals/{uuid}/resources/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: requested_offering
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/NestedRequestedOffering
                  - Properties changed
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - New property: is_prepaid
                          - New property: max_prepaid_duration
                          - New property: min_prepaid_duration
                          - New property: overage_component

PUT /api/proposal-proposals/{uuid}/resources/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: requested_offering
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/NestedRequestedOffering
                  - Properties changed
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - New property: is_prepaid
                          - New property: max_prepaid_duration
                          - New property: min_prepaid_duration
                          - New property: overage_component

GET /api/proposal-protected-calls/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: offerings
                - Items changed
                  - Properties changed
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - New property: is_prepaid
                          - New property: max_prepaid_duration
                          - New property: min_prepaid_duration
                          - New property: overage_component
              - Modified property: rounds
                - Items changed
                  - Properties changed
                    - Modified property: status
                      - Property 'AllOf' changed
                        - Schemas added: #/components/schemas/RoundStatus
                        - Schemas deleted: #/components/schemas/StatusEnum

POST /api/proposal-protected-calls/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: offerings
              - Items changed
                - Properties changed
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - New property: is_prepaid
                        - New property: max_prepaid_duration
                        - New property: min_prepaid_duration
                        - New property: overage_component
            - Modified property: rounds
              - Items changed
                - Properties changed
                  - Modified property: status
                    - Property 'AllOf' changed
                      - Schemas added: #/components/schemas/RoundStatus
                      - Schemas deleted: #/components/schemas/StatusEnum

GET /api/proposal-protected-calls/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: offerings
              - Items changed
                - Properties changed
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - New property: is_prepaid
                        - New property: max_prepaid_duration
                        - New property: min_prepaid_duration
                        - New property: overage_component
            - Modified property: rounds
              - Items changed
                - Properties changed
                  - Modified property: status
                    - Property 'AllOf' changed
                      - Schemas added: #/components/schemas/RoundStatus
                      - Schemas deleted: #/components/schemas/StatusEnum

PATCH /api/proposal-protected-calls/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: offerings
              - Items changed
                - Properties changed
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - New property: is_prepaid
                        - New property: max_prepaid_duration
                        - New property: min_prepaid_duration
                        - New property: overage_component
            - Modified property: rounds
              - Items changed
                - Properties changed
                  - Modified property: status
                    - Property 'AllOf' changed
                      - Schemas added: #/components/schemas/RoundStatus
                      - Schemas deleted: #/components/schemas/StatusEnum

PUT /api/proposal-protected-calls/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: offerings
              - Items changed
                - Properties changed
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - New property: is_prepaid
                        - New property: max_prepaid_duration
                        - New property: min_prepaid_duration
                        - New property: overage_component
            - Modified property: rounds
              - Items changed
                - Properties changed
                  - Modified property: status
                    - Property 'AllOf' changed
                      - Schemas added: #/components/schemas/RoundStatus
                      - Schemas deleted: #/components/schemas/StatusEnum

POST /api/proposal-protected-calls/{uuid}/activate/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: offerings
              - Items changed
                - Properties changed
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - New property: is_prepaid
                        - New property: max_prepaid_duration
                        - New property: min_prepaid_duration
                        - New property: overage_component
            - Modified property: rounds
              - Items changed
                - Properties changed
                  - Modified property: status
                    - Property 'AllOf' changed
                      - Schemas added: #/components/schemas/RoundStatus
                      - Schemas deleted: #/components/schemas/StatusEnum

POST /api/proposal-protected-calls/{uuid}/archive/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: offerings
              - Items changed
                - Properties changed
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - New property: is_prepaid
                        - New property: max_prepaid_duration
                        - New property: min_prepaid_duration
                        - New property: overage_component
            - Modified property: rounds
              - Items changed
                - Properties changed
                  - Modified property: status
                    - Property 'AllOf' changed
                      - Schemas added: #/components/schemas/RoundStatus
                      - Schemas deleted: #/components/schemas/StatusEnum

GET /api/proposal-protected-calls/{uuid}/offerings/

- New query param: state
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: components
                - Items changed
                  - Properties changed
                    - New property: is_prepaid
                    - New property: max_prepaid_duration
                    - New property: min_prepaid_duration
                    - New property: overage_component

POST /api/proposal-protected-calls/{uuid}/offerings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: is_prepaid
                  - New property: max_prepaid_duration
                  - New property: min_prepaid_duration
                  - New property: overage_component

GET /api/proposal-protected-calls/{uuid}/offerings/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: is_prepaid
                  - New property: max_prepaid_duration
                  - New property: min_prepaid_duration
                  - New property: overage_component

PATCH /api/proposal-protected-calls/{uuid}/offerings/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: is_prepaid
                  - New property: max_prepaid_duration
                  - New property: min_prepaid_duration
                  - New property: overage_component

PUT /api/proposal-protected-calls/{uuid}/offerings/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: is_prepaid
                  - New property: max_prepaid_duration
                  - New property: min_prepaid_duration
                  - New property: overage_component

GET /api/proposal-protected-calls/{uuid}/rounds/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: status
                - Property 'AllOf' changed
                  - Schemas added: #/components/schemas/RoundStatus
                  - Schemas deleted: #/components/schemas/StatusEnum

POST /api/proposal-protected-calls/{uuid}/rounds/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: status
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/RoundStatus
                - Schemas deleted: #/components/schemas/StatusEnum

GET /api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: status
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/RoundStatus
                - Schemas deleted: #/components/schemas/StatusEnum

PATCH /api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: status
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/RoundStatus
                - Schemas deleted: #/components/schemas/StatusEnum

PUT /api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: status
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/RoundStatus
                - Schemas deleted: #/components/schemas/StatusEnum

POST /api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/close/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: offerings
              - Items changed
                - Properties changed
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - New property: is_prepaid
                        - New property: max_prepaid_duration
                        - New property: min_prepaid_duration
                        - New property: overage_component
            - Modified property: rounds
              - Items changed
                - Properties changed
                  - Modified property: status
                    - Property 'AllOf' changed
                      - Schemas added: #/components/schemas/RoundStatus
                      - Schemas deleted: #/components/schemas/StatusEnum

GET /api/proposal-public-calls/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: offerings
                - Items changed
                  - Properties changed
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - New property: is_prepaid
                          - New property: max_prepaid_duration
                          - New property: min_prepaid_duration
                          - New property: overage_component
              - Modified property: rounds
                - Items changed
                  - Properties changed
                    - Modified property: status
                      - Property 'AllOf' changed
                        - Schemas added: #/components/schemas/RoundStatus
                        - Schemas deleted: #/components/schemas/StatusEnum

GET /api/proposal-public-calls/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: offerings
              - Items changed
                - Properties changed
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - New property: is_prepaid
                        - New property: max_prepaid_duration
                        - New property: min_prepaid_duration
                        - New property: overage_component
            - Modified property: rounds
              - Items changed
                - Properties changed
                  - Modified property: status
                    - Property 'AllOf' changed
                      - Schemas added: #/components/schemas/RoundStatus
                      - Schemas deleted: #/components/schemas/StatusEnum

GET /api/proposal-requested-offerings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: components
                - Items changed
                  - Properties changed
                    - New property: is_prepaid
                    - New property: max_prepaid_duration
                    - New property: min_prepaid_duration
                    - New property: overage_component

GET /api/proposal-requested-offerings/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: is_prepaid
                  - New property: max_prepaid_duration
                  - New property: min_prepaid_duration
                  - New property: overage_component

GET /api/proposal-requested-resources/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: requested_offering
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/NestedRequestedOffering
                    - Properties changed
                      - Modified property: components
                        - Items changed
                          - Properties changed
                            - New property: is_prepaid
                            - New property: max_prepaid_duration
                            - New property: min_prepaid_duration
                            - New property: overage_component

GET /api/proposal-requested-resources/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: requested_offering
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/NestedRequestedOffering
                  - Properties changed
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - New property: is_prepaid
                          - New property: max_prepaid_duration
                          - New property: min_prepaid_duration
                          - New property: overage_component

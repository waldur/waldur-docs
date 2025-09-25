# OpenAPI schema diff - 7.8.1

## For version 7.8.1

### New Endpoints: 5

--------------------
GET /api/marketplace-offering-user-checklist-completions/  
HEAD /api/marketplace-offering-user-checklist-completions/  
GET /api/marketplace-offering-user-checklist-completions/{id}/  
GET /api/marketplace-provider-offerings/{uuid}/list_course_accounts/  
POST /api/marketplace-provider-offerings/{uuid}/update_compliance_checklist/  

### Deleted Endpoints: None

---------------------------

### Modified Endpoints: 72

--------------------------
POST /api/backend-resources/{uuid}/import_resource/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: offering_customer_name
            - New property: offering_customer_slug
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: offering_customer_name
                    - New property: offering_customer_slug
                    - New property: offering_customer_uuid
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: offering_customer_name
                    - New property: offering_customer_slug
                    - New property: offering_customer_uuid

GET /api/booking-offerings/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [compliance_checklist]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: compliance_checklist
              - Modified property: plugin_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedPluginOptions
                    - Properties changed
                      - New property: maximal_resource_count_per_project

GET /api/booking-offerings/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [compliance_checklist]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: compliance_checklist
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: maximal_resource_count_per_project

GET /api/booking-resources/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [offering_customer_name offering_customer_slug]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: offering_customer_name
              - New property: offering_customer_slug
              - Modified property: creation_order
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: offering_customer_name
                      - New property: offering_customer_slug
                      - New property: offering_customer_uuid
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: offering_customer_name
                      - New property: offering_customer_slug
                      - New property: offering_customer_uuid

GET /api/booking-resources/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [offering_customer_name offering_customer_slug]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: offering_customer_name
            - New property: offering_customer_slug
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: offering_customer_name
                    - New property: offering_customer_slug
                    - New property: offering_customer_uuid
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: offering_customer_name
                    - New property: offering_customer_slug
                    - New property: offering_customer_uuid

GET /api/checklists-admin/

- New query param: checklist_type
- New query param: checklist_type__in

HEAD /api/checklists-admin/

- New query param: checklist_type
- New query param: checklist_type__in

GET /api/checklists-admin/{uuid}/questions/

- New query param: checklist_type
- New query param: checklist_type__in

GET /api/managed-rancher-cluster-resources/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [offering_customer_name offering_customer_slug]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: offering_customer_name
              - New property: offering_customer_slug
              - Modified property: creation_order
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: offering_customer_name
                      - New property: offering_customer_slug
                      - New property: offering_customer_uuid
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: offering_customer_name
                      - New property: offering_customer_slug
                      - New property: offering_customer_uuid

GET /api/managed-rancher-cluster-resources/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [offering_customer_name offering_customer_slug]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: offering_customer_name
            - New property: offering_customer_slug
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: offering_customer_name
                    - New property: offering_customer_slug
                    - New property: offering_customer_uuid
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: offering_customer_name
                    - New property: offering_customer_slug
                    - New property: offering_customer_uuid

GET /api/marketplace-course-accounts/

- New query param: o
- New query param: project_end_date_after
- New query param: project_end_date_before
- New query param: project_start_date_after
- New query param: project_start_date_before
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: project_end_date
              - New required property: project_slug
              - New required property: project_start_date
            - Properties changed
              - New property: project_end_date
              - New property: project_slug
              - New property: project_start_date

HEAD /api/marketplace-course-accounts/

- New query param: o
- New query param: project_end_date_after
- New query param: project_end_date_before
- New query param: project_start_date_after
- New query param: project_start_date_before

POST /api/marketplace-course-accounts/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: project_end_date
            - New required property: project_slug
            - New required property: project_start_date
          - Properties changed
            - New property: project_end_date
            - New property: project_slug
            - New property: project_start_date

GET /api/marketplace-course-accounts/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: project_end_date
            - New required property: project_slug
            - New required property: project_start_date
          - Properties changed
            - New property: project_end_date
            - New property: project_slug
            - New property: project_start_date

GET /api/marketplace-orders/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [offering_customer_name offering_customer_slug offering_customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: offering_customer_name
              - New property: offering_customer_slug
              - New property: offering_customer_uuid

GET /api/marketplace-orders/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [offering_customer_name offering_customer_slug offering_customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: offering_customer_name
            - New property: offering_customer_slug
            - New property: offering_customer_uuid

GET /api/marketplace-orders/{uuid}/offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: compliance_checklist
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: maximal_resource_count_per_project

GET /api/marketplace-provider-offerings/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [compliance_checklist]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: compliance_checklist
              - Modified property: integration_status
                - Items changed
                  - Properties changed
                    - New property: service_name
                    - Modified property: agent_type
                      - Property 'AllOf' changed
                        - Schemas added: #/components/schemas/AgentTypeEnum
                      - Type changed from 'string' to ''
              - Modified property: plugin_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedPluginOptions
                    - Properties changed
                      - New property: maximal_resource_count_per_project

POST /api/marketplace-provider-offerings/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: compliance_checklist
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: compliance_checklist
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: maximal_resource_count_per_project

GET /api/marketplace-provider-offerings/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [compliance_checklist]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: compliance_checklist
            - Modified property: integration_status
              - Items changed
                - Properties changed
                  - New property: service_name
                  - Modified property: agent_type
                    - Property 'AllOf' changed
                      - Schemas added: #/components/schemas/AgentTypeEnum
                    - Type changed from 'string' to ''
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: maximal_resource_count_per_project

POST /api/marketplace-provider-offerings/{uuid}/import_resource/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: offering_customer_name
            - New property: offering_customer_slug
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: offering_customer_name
                    - New property: offering_customer_slug
                    - New property: offering_customer_uuid
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: offering_customer_name
                    - New property: offering_customer_slug
                    - New property: offering_customer_uuid

GET /api/marketplace-provider-offerings/{uuid}/list_customer_service_accounts/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [compliance_checklist]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: compliance_checklist
            - Modified property: integration_status
              - Items changed
                - Properties changed
                  - New property: service_name
                  - Modified property: agent_type
                    - Property 'AllOf' changed
                      - Schemas added: #/components/schemas/AgentTypeEnum
                    - Type changed from 'string' to ''
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: maximal_resource_count_per_project

GET /api/marketplace-provider-offerings/{uuid}/list_project_service_accounts/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [compliance_checklist]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: compliance_checklist
            - Modified property: integration_status
              - Items changed
                - Properties changed
                  - New property: service_name
                  - Modified property: agent_type
                    - Property 'AllOf' changed
                      - Schemas added: #/components/schemas/AgentTypeEnum
                    - Type changed from 'string' to ''
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: maximal_resource_count_per_project

POST /api/marketplace-provider-offerings/{uuid}/move_offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: compliance_checklist
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: maximal_resource_count_per_project

GET /api/marketplace-provider-offerings/{uuid}/orders/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: offering_customer_name
              - New property: offering_customer_slug
              - New property: offering_customer_uuid

GET /api/marketplace-provider-offerings/{uuid}/orders/{order_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: offering_customer_name
            - New property: offering_customer_slug
            - New property: offering_customer_uuid

POST /api/marketplace-provider-offerings/{uuid}/refresh_offering_usernames/

- Request body changed

GET /api/marketplace-provider-offerings/{uuid}/stats/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [compliance_checklist]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: compliance_checklist
            - Modified property: integration_status
              - Items changed
                - Properties changed
                  - New property: service_name
                  - Modified property: agent_type
                    - Property 'AllOf' changed
                      - Schemas added: #/components/schemas/AgentTypeEnum
                    - Type changed from 'string' to ''
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: maximal_resource_count_per_project

POST /api/marketplace-provider-offerings/{uuid}/update_image/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: compliance_checklist
            - Modified property: integration_status
              - Items changed
                - Properties changed
                  - New property: service_name
                  - Modified property: agent_type
                    - Property 'AllOf' changed
                      - Schemas added: #/components/schemas/AgentTypeEnum
                    - Type changed from 'string' to ''
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: maximal_resource_count_per_project

POST /api/marketplace-provider-offerings/{uuid}/update_integration/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: plugin_options
            - Properties changed
              - New property: maximal_resource_count_per_project

GET /api/marketplace-provider-offerings/{uuid}/user_has_resource_access/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [compliance_checklist]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: compliance_checklist
            - Modified property: integration_status
              - Items changed
                - Properties changed
                  - New property: service_name
                  - Modified property: agent_type
                    - Property 'AllOf' changed
                      - Schemas added: #/components/schemas/AgentTypeEnum
                    - Type changed from 'string' to ''
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: maximal_resource_count_per_project

GET /api/marketplace-provider-resources/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [offering_customer_name offering_customer_slug]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: offering_customer_name
              - New property: offering_customer_slug
              - Modified property: creation_order
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: offering_customer_name
                      - New property: offering_customer_slug
                      - New property: offering_customer_uuid
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: offering_customer_name
                      - New property: offering_customer_slug
                      - New property: offering_customer_uuid

GET /api/marketplace-provider-resources/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [offering_customer_name offering_customer_slug]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: offering_customer_name
            - New property: offering_customer_slug
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: offering_customer_name
                    - New property: offering_customer_slug
                    - New property: offering_customer_uuid
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: offering_customer_name
                    - New property: offering_customer_slug
                    - New property: offering_customer_uuid

GET /api/marketplace-provider-resources/{uuid}/details/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [offering_customer_name offering_customer_slug]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: offering_customer_name
            - New property: offering_customer_slug
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: offering_customer_name
                    - New property: offering_customer_slug
                    - New property: offering_customer_uuid
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: offering_customer_name
                    - New property: offering_customer_slug
                    - New property: offering_customer_uuid

POST /api/marketplace-provider-resources/{uuid}/move_resource/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: offering_customer_name
            - New property: offering_customer_slug
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: offering_customer_name
                    - New property: offering_customer_slug
                    - New property: offering_customer_uuid
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: offering_customer_name
                    - New property: offering_customer_slug
                    - New property: offering_customer_uuid

GET /api/marketplace-provider-resources/{uuid}/offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: compliance_checklist
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: maximal_resource_count_per_project

POST /api/marketplace-provider-resources/{uuid}/set_end_date_by_provider/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: offering_customer_name
            - New property: offering_customer_slug
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: offering_customer_name
                    - New property: offering_customer_slug
                    - New property: offering_customer_uuid
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: offering_customer_name
                    - New property: offering_customer_slug
                    - New property: offering_customer_uuid

GET /api/marketplace-public-offerings/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [compliance_checklist]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: compliance_checklist
              - Modified property: plugin_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedPluginOptions
                    - Properties changed
                      - New property: maximal_resource_count_per_project

GET /api/marketplace-public-offerings/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [compliance_checklist]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: compliance_checklist
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: maximal_resource_count_per_project

GET /api/marketplace-resources/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [offering_customer_name offering_customer_slug]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: offering_customer_name
              - New property: offering_customer_slug
              - Modified property: creation_order
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: offering_customer_name
                      - New property: offering_customer_slug
                      - New property: offering_customer_uuid
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: offering_customer_name
                      - New property: offering_customer_slug
                      - New property: offering_customer_uuid

GET /api/marketplace-resources/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [offering_customer_name offering_customer_slug]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: offering_customer_name
            - New property: offering_customer_slug
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: offering_customer_name
                    - New property: offering_customer_slug
                    - New property: offering_customer_uuid
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: offering_customer_name
                    - New property: offering_customer_slug
                    - New property: offering_customer_uuid

GET /api/marketplace-resources/{uuid}/details/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [offering_customer_name offering_customer_slug]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: offering_customer_name
            - New property: offering_customer_slug
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: offering_customer_name
                    - New property: offering_customer_slug
                    - New property: offering_customer_uuid
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: offering_customer_name
                    - New property: offering_customer_slug
                    - New property: offering_customer_uuid

POST /api/marketplace-resources/{uuid}/move_resource/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: offering_customer_name
            - New property: offering_customer_slug
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: offering_customer_name
                    - New property: offering_customer_slug
                    - New property: offering_customer_uuid
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: offering_customer_name
                    - New property: offering_customer_slug
                    - New property: offering_customer_uuid

GET /api/marketplace-resources/{uuid}/offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: compliance_checklist
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: maximal_resource_count_per_project

POST /api/marketplace-resources/{uuid}/update_limits/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Deleted property: attachment

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
                      - New property: maximal_resource_count_per_project

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
                    - New property: maximal_resource_count_per_project

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
                    - New property: maximal_resource_count_per_project

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
                    - New property: maximal_resource_count_per_project

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
                    - New property: maximal_resource_count_per_project

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
                    - New property: maximal_resource_count_per_project

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
                    - New property: maximal_resource_count_per_project

POST /api/marketplace-script-dry-run/{uuid}/async_run/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: compliance_checklist
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: maximal_resource_count_per_project

POST /api/marketplace-script-dry-run/{uuid}/run/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: compliance_checklist
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: maximal_resource_count_per_project

GET /api/marketplace-service-providers/{service_provider_uuid}/course_accounts/

- New query param: o
- New query param: project_end_date_after
- New query param: project_end_date_before
- New query param: project_start_date_after
- New query param: project_start_date_before
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: project_end_date
              - New required property: project_slug
              - New required property: project_start_date
            - Properties changed
              - New property: project_end_date
              - New property: project_slug
              - New property: project_start_date

GET /api/marketplace-service-providers/{service_provider_uuid}/offerings/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [thumbnail]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: thumbnail

GET /api/notification-messages/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: context_fields
            - Properties changed
              - New property: context_fields

POST /api/notification-messages/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: context_fields
          - Properties changed
            - New property: context_fields

GET /api/notification-messages/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: context_fields
          - Properties changed
            - New property: context_fields

PATCH /api/notification-messages/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: context_fields
          - Properties changed
            - New property: context_fields

PUT /api/notification-messages/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: context_fields
          - Properties changed
            - New property: context_fields

GET /api/promotions-campaigns/{uuid}/orders/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: offering_customer_name
              - New property: offering_customer_slug
              - New property: offering_customer_uuid

GET /api/promotions-campaigns/{uuid}/resources/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: offering_customer_name
              - New property: offering_customer_slug
              - Modified property: creation_order
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: offering_customer_name
                      - New property: offering_customer_slug
                      - New property: offering_customer_uuid
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: offering_customer_name
                      - New property: offering_customer_slug
                      - New property: offering_customer_uuid

GET /api/user-group-invitations/

- New query param: is_public
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: created_by_image
            - Properties changed
              - New property: created_by_image

HEAD /api/user-group-invitations/

- New query param: is_public

POST /api/user-group-invitations/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: created_by_image
          - Properties changed
            - New property: created_by_image

GET /api/user-group-invitations/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: created_by_image
          - Properties changed
            - New property: created_by_image

GET /api/user-invitations/

- New query param: email_exact
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: created_by_image
            - Properties changed
              - New property: created_by_image

HEAD /api/user-invitations/

- New query param: email_exact

POST /api/user-invitations/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: created_by_image
          - Properties changed
            - New property: created_by_image

GET /api/user-invitations/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: created_by_image
          - Properties changed
            - New property: created_by_image

GET /api/user-invitations/{uuid}/details/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: created_by_image
          - Properties changed
            - New property: created_by_image

# OpenAPI schema diff - 7.8.6

## For version 7.8.6

### New Endpoints: 25

---------------------
GET /api/metadata/events/  
GET /api/metadata/features/  
GET /api/metadata/permissions/  
GET /api/metadata/settings/  
GET /api/onboarding-country-configs/  
HEAD /api/onboarding-country-configs/  
POST /api/onboarding-country-configs/  
DELETE /api/onboarding-country-configs/{uuid}/  
GET /api/onboarding-country-configs/{uuid}/  
PATCH /api/onboarding-country-configs/{uuid}/  
PUT /api/onboarding-country-configs/{uuid}/  
GET /api/onboarding-question-metadata/  
HEAD /api/onboarding-question-metadata/  
POST /api/onboarding-question-metadata/  
DELETE /api/onboarding-question-metadata/{uuid}/  
GET /api/onboarding-question-metadata/{uuid}/  
PATCH /api/onboarding-question-metadata/{uuid}/  
PUT /api/onboarding-question-metadata/{uuid}/  
GET /api/onboarding-verifications/checklist-template/  
HEAD /api/onboarding-verifications/checklist-template/  
POST /api/onboarding-verifications/start_verification/  
GET /api/onboarding-verifications/{uuid}/checklist/  
GET /api/onboarding-verifications/{uuid}/completion_status/  
POST /api/onboarding-verifications/{uuid}/run_validation/  
POST /api/onboarding-verifications/{uuid}/submit_answers/  

### Deleted Endpoints: 1

------------------------
POST /api/onboarding-verifications/validate_company/  

### Modified Endpoints: 247

---------------------------
GET /api/admin-announcements/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [maintenance_external_reference_url]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: maintenance_external_reference_url

POST /api/admin-announcements/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: maintenance_external_reference_url

GET /api/admin-announcements/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [maintenance_external_reference_url]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: maintenance_external_reference_url

PATCH /api/admin-announcements/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: maintenance_external_reference_url

PUT /api/admin-announcements/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: maintenance_external_reference_url

GET /api/aws-instances/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: customer_uuid

POST /api/aws-instances/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

GET /api/aws-instances/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

PATCH /api/aws-instances/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

PUT /api/aws-instances/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

GET /api/aws-volumes/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: customer_uuid

POST /api/aws-volumes/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

GET /api/aws-volumes/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

PATCH /api/aws-volumes/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

PUT /api/aws-volumes/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

GET /api/azure-public-ips/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: customer_uuid

POST /api/azure-public-ips/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

GET /api/azure-public-ips/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

PATCH /api/azure-public-ips/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

PUT /api/azure-public-ips/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

GET /api/azure-resource-groups/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: customer_uuid

GET /api/azure-resource-groups/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

GET /api/azure-sql-databases/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: customer_uuid

POST /api/azure-sql-databases/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

GET /api/azure-sql-databases/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

PATCH /api/azure-sql-databases/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

PUT /api/azure-sql-databases/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

GET /api/azure-sql-servers/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: customer_uuid

POST /api/azure-sql-servers/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

GET /api/azure-sql-servers/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

PATCH /api/azure-sql-servers/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

PUT /api/azure-sql-servers/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

GET /api/azure-virtualmachines/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: customer_uuid

POST /api/azure-virtualmachines/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

GET /api/azure-virtualmachines/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

PATCH /api/azure-virtualmachines/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

PUT /api/azure-virtualmachines/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

GET /api/booking-offerings/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [secret_options service_attributes]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OfferingOptions
                    - Properties changed
                      - Modified property: options
                        - AdditionalProperties changed
                          - Properties changed
                            - New property: cascade_config
                            - New property: component_multiplier_config
                            - Modified property: type
                              - New enum values: [conditional_cascade component_multiplier]
              - Modified property: plugin_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedPluginOptions
                    - Properties changed
                      - New property: max_security_groups
              - Modified property: resource_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OfferingOptions
                    - Properties changed
                      - Modified property: options
                        - AdditionalProperties changed
                          - Properties changed
                            - New property: cascade_config
                            - New property: component_multiplier_config
                            - Modified property: type
                              - New enum values: [conditional_cascade component_multiplier]

GET /api/booking-offerings/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [secret_options service_attributes]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: cascade_config
                          - New property: component_multiplier_config
                          - Modified property: type
                            - New enum values: [conditional_cascade component_multiplier]
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: max_security_groups
            - Modified property: resource_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: cascade_config
                          - New property: component_multiplier_config
                          - Modified property: type
                            - New enum values: [conditional_cascade component_multiplier]

GET /api/booking-resources/

- Modified query param: only_limit_based
  - Description changed from 'Filter out resources with only limit-based components' to 'Filter resources with only limit-based components'
- Modified query param: only_usage_based
  - Description changed from 'Filter out resources with only usage-based components' to 'Filter resources with only usage-based components'

HEAD /api/booking-resources/

- Modified query param: only_limit_based
  - Description changed from 'Filter out resources with only limit-based components' to 'Filter resources with only limit-based components'
- Modified query param: only_usage_based
  - Description changed from 'Filter out resources with only usage-based components' to 'Filter resources with only usage-based components'

GET /api/checklists-admin/

- Modified query param: checklist_type
  - Schema changed
    - New enum values: [customer_onboarding]
- Modified query param: checklist_type__in
  - Schema changed
    - Items changed
      - New enum values: [customer_onboarding]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: checklist_type
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/ChecklistTypeEnum
                    - New enum values: [customer_onboarding]

HEAD /api/checklists-admin/

- Modified query param: checklist_type
  - Schema changed
    - New enum values: [customer_onboarding]
- Modified query param: checklist_type__in
  - Schema changed
    - Items changed
      - New enum values: [customer_onboarding]

POST /api/checklists-admin/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: checklist_type
            - Property 'AllOf' changed
              - Modified schema: #/components/schemas/ChecklistTypeEnum
                - New enum values: [customer_onboarding]
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: checklist_type
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/ChecklistTypeEnum
                  - New enum values: [customer_onboarding]

GET /api/checklists-admin/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: checklist_type
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/ChecklistTypeEnum
                  - New enum values: [customer_onboarding]

PATCH /api/checklists-admin/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: checklist_type
            - Property 'AllOf' changed
              - Modified schema: #/components/schemas/ChecklistTypeEnum
                - New enum values: [customer_onboarding]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: checklist_type
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/ChecklistTypeEnum
                  - New enum values: [customer_onboarding]

PUT /api/checklists-admin/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: checklist_type
            - Property 'AllOf' changed
              - Modified schema: #/components/schemas/ChecklistTypeEnum
                - New enum values: [customer_onboarding]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: checklist_type
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/ChecklistTypeEnum
                  - New enum values: [customer_onboarding]

GET /api/checklists-admin/{uuid}/questions/

- Modified query param: checklist_type
  - Schema changed
    - New enum values: [customer_onboarding]
- Modified query param: checklist_type__in
  - Schema changed
    - Items changed
      - New enum values: [customer_onboarding]

GET /api/digitalocean-droplets/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: customer_uuid

POST /api/digitalocean-droplets/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

GET /api/digitalocean-droplets/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

PATCH /api/digitalocean-droplets/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

PUT /api/digitalocean-droplets/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

POST /api/marketplace-orders/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: start_date
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: error_traceback
          - Properties changed
            - New property: start_date

GET /api/marketplace-orders/{uuid}/offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: cascade_config
                          - New property: component_multiplier_config
                          - Modified property: type
                            - New enum values: [conditional_cascade component_multiplier]
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: max_security_groups
            - Modified property: resource_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: cascade_config
                          - New property: component_multiplier_config
                          - Modified property: type
                            - New enum values: [conditional_cascade component_multiplier]

GET /api/marketplace-provider-offerings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OfferingOptions
                    - Properties changed
                      - Modified property: options
                        - AdditionalProperties changed
                          - Properties changed
                            - New property: cascade_config
                            - New property: component_multiplier_config
                            - Modified property: type
                              - New enum values: [conditional_cascade component_multiplier]
              - Modified property: plugin_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedPluginOptions
                    - Properties changed
                      - New property: max_security_groups
              - Modified property: resource_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OfferingOptions
                    - Properties changed
                      - Modified property: options
                        - AdditionalProperties changed
                          - Properties changed
                            - New property: cascade_config
                            - New property: component_multiplier_config
                            - Modified property: type
                              - New enum values: [conditional_cascade component_multiplier]

POST /api/marketplace-provider-offerings/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: options
            - Properties changed
              - Modified property: options
                - AdditionalProperties changed
                  - Properties changed
                    - New property: cascade_config
                    - New property: component_multiplier_config
                    - Modified property: type
                      - New enum values: [conditional_cascade component_multiplier]
          - Modified property: resource_options
            - Properties changed
              - Modified property: options
                - AdditionalProperties changed
                  - Properties changed
                    - New property: cascade_config
                    - New property: component_multiplier_config
                    - Modified property: type
                      - New enum values: [conditional_cascade component_multiplier]
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Modified property: options
            - Properties changed
              - Modified property: options
                - AdditionalProperties changed
                  - Properties changed
                    - New property: cascade_config
                    - New property: component_multiplier_config
                    - Modified property: type
                      - New enum values: [conditional_cascade component_multiplier]
          - Modified property: resource_options
            - Properties changed
              - Modified property: options
                - AdditionalProperties changed
                  - Properties changed
                    - New property: cascade_config
                    - New property: component_multiplier_config
                    - Modified property: type
                      - New enum values: [conditional_cascade component_multiplier]
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Modified property: options
            - Properties changed
              - Modified property: options
                - AdditionalProperties changed
                  - Properties changed
                    - New property: cascade_config
                    - New property: component_multiplier_config
                    - Modified property: type
                      - New enum values: [conditional_cascade component_multiplier]
          - Modified property: resource_options
            - Properties changed
              - Modified property: options
                - AdditionalProperties changed
                  - Properties changed
                    - New property: cascade_config
                    - New property: component_multiplier_config
                    - Modified property: type
                      - New enum values: [conditional_cascade component_multiplier]
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: secret_options
            - Deleted required property: service_attributes
          - Properties changed
            - Modified property: options
              - Properties changed
                - Modified property: options
                  - AdditionalProperties changed
                    - Properties changed
                      - New property: cascade_config
                      - New property: component_multiplier_config
                      - Modified property: type
                        - New enum values: [conditional_cascade component_multiplier]
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: max_security_groups
            - Modified property: resource_options
              - Properties changed
                - Modified property: options
                  - AdditionalProperties changed
                    - Properties changed
                      - New property: cascade_config
                      - New property: component_multiplier_config
                      - Modified property: type
                        - New enum values: [conditional_cascade component_multiplier]

GET /api/marketplace-provider-offerings/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: cascade_config
                          - New property: component_multiplier_config
                          - Modified property: type
                            - New enum values: [conditional_cascade component_multiplier]
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: max_security_groups
            - Modified property: resource_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: cascade_config
                          - New property: component_multiplier_config
                          - Modified property: type
                            - New enum values: [conditional_cascade component_multiplier]

GET /api/marketplace-provider-offerings/{uuid}/customers/

- New query param: field
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - Deleted required property: name
              - Deleted required property: slug
              - Deleted required property: uuid

GET /api/marketplace-provider-offerings/{uuid}/list_course_accounts/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: cascade_config
                          - New property: component_multiplier_config
                          - Modified property: type
                            - New enum values: [conditional_cascade component_multiplier]
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: max_security_groups
            - Modified property: resource_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: cascade_config
                          - New property: component_multiplier_config
                          - Modified property: type
                            - New enum values: [conditional_cascade component_multiplier]

GET /api/marketplace-provider-offerings/{uuid}/list_customer_projects/

- New query param: field

GET /api/marketplace-provider-offerings/{uuid}/list_customer_service_accounts/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: cascade_config
                          - New property: component_multiplier_config
                          - Modified property: type
                            - New enum values: [conditional_cascade component_multiplier]
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: max_security_groups
            - Modified property: resource_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: cascade_config
                          - New property: component_multiplier_config
                          - Modified property: type
                            - New enum values: [conditional_cascade component_multiplier]

GET /api/marketplace-provider-offerings/{uuid}/list_customer_users/

- New query param: field
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: birth_date

GET /api/marketplace-provider-offerings/{uuid}/list_project_service_accounts/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: cascade_config
                          - New property: component_multiplier_config
                          - Modified property: type
                            - New enum values: [conditional_cascade component_multiplier]
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: max_security_groups
            - Modified property: resource_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: cascade_config
                          - New property: component_multiplier_config
                          - Modified property: type
                            - New enum values: [conditional_cascade component_multiplier]

POST /api/marketplace-provider-offerings/{uuid}/move_offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: cascade_config
                          - New property: component_multiplier_config
                          - Modified property: type
                            - New enum values: [conditional_cascade component_multiplier]
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: max_security_groups
            - Modified property: resource_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: cascade_config
                          - New property: component_multiplier_config
                          - Modified property: type
                            - New enum values: [conditional_cascade component_multiplier]

GET /api/marketplace-provider-offerings/{uuid}/orders/

- New query param: field

GET /api/marketplace-provider-offerings/{uuid}/stats/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: cascade_config
                          - New property: component_multiplier_config
                          - Modified property: type
                            - New enum values: [conditional_cascade component_multiplier]
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: max_security_groups
            - Modified property: resource_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: cascade_config
                          - New property: component_multiplier_config
                          - Modified property: type
                            - New enum values: [conditional_cascade component_multiplier]

POST /api/marketplace-provider-offerings/{uuid}/update_image/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: cascade_config
                          - New property: component_multiplier_config
                          - Modified property: type
                            - New enum values: [conditional_cascade component_multiplier]
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: max_security_groups
            - Modified property: resource_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: cascade_config
                          - New property: component_multiplier_config
                          - Modified property: type
                            - New enum values: [conditional_cascade component_multiplier]

POST /api/marketplace-provider-offerings/{uuid}/update_integration/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: plugin_options
            - Properties changed
              - New property: max_security_groups

POST /api/marketplace-provider-offerings/{uuid}/update_options/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: options
            - Properties changed
              - Modified property: options
                - AdditionalProperties changed
                  - Properties changed
                    - New property: cascade_config
                    - New property: component_multiplier_config
                    - Modified property: type
                      - New enum values: [conditional_cascade component_multiplier]

PATCH /api/marketplace-provider-offerings/{uuid}/update_partition/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: partition_uuid
          - Deleted property: offering

POST /api/marketplace-provider-offerings/{uuid}/update_resource_options/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: resource_options
            - Properties changed
              - Modified property: options
                - AdditionalProperties changed
                  - Properties changed
                    - New property: cascade_config
                    - New property: component_multiplier_config
                    - Modified property: type
                      - New enum values: [conditional_cascade component_multiplier]

GET /api/marketplace-provider-offerings/{uuid}/user_has_resource_access/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: cascade_config
                          - New property: component_multiplier_config
                          - Modified property: type
                            - New enum values: [conditional_cascade component_multiplier]
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: max_security_groups
            - Modified property: resource_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: cascade_config
                          - New property: component_multiplier_config
                          - Modified property: type
                            - New enum values: [conditional_cascade component_multiplier]

GET /api/marketplace-provider-resources/

- Modified query param: only_limit_based
  - Description changed from 'Filter out resources with only limit-based components' to 'Filter resources with only limit-based components'
- Modified query param: only_usage_based
  - Description changed from 'Filter out resources with only usage-based components' to 'Filter resources with only usage-based components'

HEAD /api/marketplace-provider-resources/

- Modified query param: only_limit_based
  - Description changed from 'Filter out resources with only limit-based components' to 'Filter resources with only limit-based components'
- Modified query param: only_usage_based
  - Description changed from 'Filter out resources with only usage-based components' to 'Filter resources with only usage-based components'

GET /api/marketplace-provider-resources/{uuid}/offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: cascade_config
                          - New property: component_multiplier_config
                          - Modified property: type
                            - New enum values: [conditional_cascade component_multiplier]
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: max_security_groups
            - Modified property: resource_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: cascade_config
                          - New property: component_multiplier_config
                          - Modified property: type
                            - New enum values: [conditional_cascade component_multiplier]

GET /api/marketplace-public-offerings/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [secret_options service_attributes]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OfferingOptions
                    - Properties changed
                      - Modified property: options
                        - AdditionalProperties changed
                          - Properties changed
                            - New property: cascade_config
                            - New property: component_multiplier_config
                            - Modified property: type
                              - New enum values: [conditional_cascade component_multiplier]
              - Modified property: plugin_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedPluginOptions
                    - Properties changed
                      - New property: max_security_groups
              - Modified property: resource_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OfferingOptions
                    - Properties changed
                      - Modified property: options
                        - AdditionalProperties changed
                          - Properties changed
                            - New property: cascade_config
                            - New property: component_multiplier_config
                            - Modified property: type
                              - New enum values: [conditional_cascade component_multiplier]

GET /api/marketplace-public-offerings/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [secret_options service_attributes]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: cascade_config
                          - New property: component_multiplier_config
                          - Modified property: type
                            - New enum values: [conditional_cascade component_multiplier]
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: max_security_groups
            - Modified property: resource_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: cascade_config
                          - New property: component_multiplier_config
                          - Modified property: type
                            - New enum values: [conditional_cascade component_multiplier]

GET /api/marketplace-resources/

- Modified query param: only_limit_based
  - Description changed from 'Filter out resources with only limit-based components' to 'Filter resources with only limit-based components'
- Modified query param: only_usage_based
  - Description changed from 'Filter out resources with only usage-based components' to 'Filter resources with only usage-based components'

HEAD /api/marketplace-resources/

- Modified query param: only_limit_based
  - Description changed from 'Filter out resources with only limit-based components' to 'Filter resources with only limit-based components'
- Modified query param: only_usage_based
  - Description changed from 'Filter out resources with only usage-based components' to 'Filter resources with only usage-based components'

GET /api/marketplace-resources/{uuid}/offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: cascade_config
                          - New property: component_multiplier_config
                          - Modified property: type
                            - New enum values: [conditional_cascade component_multiplier]
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: max_security_groups
            - Modified property: resource_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: cascade_config
                          - New property: component_multiplier_config
                          - Modified property: type
                            - New enum values: [conditional_cascade component_multiplier]

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
                      - New property: max_security_groups

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
                    - New property: max_security_groups

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
                    - New property: max_security_groups

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
                    - New property: max_security_groups

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
                    - New property: max_security_groups

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
                    - New property: max_security_groups

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
                    - New property: max_security_groups

POST /api/marketplace-script-dry-run/{uuid}/async_run/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: cascade_config
                          - New property: component_multiplier_config
                          - Modified property: type
                            - New enum values: [conditional_cascade component_multiplier]
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: max_security_groups
            - Modified property: resource_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: cascade_config
                          - New property: component_multiplier_config
                          - Modified property: type
                            - New enum values: [conditional_cascade component_multiplier]

POST /api/marketplace-script-dry-run/{uuid}/run/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: cascade_config
                          - New property: component_multiplier_config
                          - Modified property: type
                            - New enum values: [conditional_cascade component_multiplier]
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: max_security_groups
            - Modified property: resource_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: cascade_config
                          - New property: component_multiplier_config
                          - Modified property: type
                            - New enum values: [conditional_cascade component_multiplier]

GET /api/marketplace-service-providers/{service_provider_uuid}/projects/

- New query param: field

GET /api/onboarding-justifications/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: country
              - New required property: error_message
              - New required property: error_traceback
            - Properties changed
              - New property: country
              - New property: error_message
              - New property: error_traceback

POST /api/onboarding-justifications/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: country
            - New required property: error_message
            - New required property: error_traceback
          - Properties changed
            - New property: country
            - New property: error_message
            - New property: error_traceback

POST /api/onboarding-justifications/create_justification/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: country
            - New required property: error_message
            - New required property: error_traceback
          - Properties changed
            - New property: country
            - New property: error_message
            - New property: error_traceback

GET /api/onboarding-justifications/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: country
            - New required property: error_message
            - New required property: error_traceback
          - Properties changed
            - New property: country
            - New property: error_message
            - New property: error_traceback

PATCH /api/onboarding-justifications/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: country
            - New required property: error_message
            - New required property: error_traceback
          - Properties changed
            - New property: country
            - New property: error_message
            - New property: error_traceback

PUT /api/onboarding-justifications/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: country
            - New required property: error_message
            - New required property: error_traceback
          - Properties changed
            - New property: country
            - New property: error_message
            - New property: error_traceback

POST /api/onboarding-justifications/{uuid}/approve/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: country
            - New required property: error_message
            - New required property: error_traceback
          - Properties changed
            - New property: country
            - New property: error_message
            - New property: error_traceback

POST /api/onboarding-justifications/{uuid}/reject/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: country
            - New required property: error_message
            - New required property: error_traceback
          - Properties changed
            - New property: country
            - New property: error_message
            - New property: error_traceback

GET /api/onboarding-verifications/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: onboarding_metadata
              - New required property: user_submitted_customer_data
              - Deleted required property: legal_person_identifier
            - Properties changed
              - New property: onboarding_metadata
              - New property: user_submitted_customer_data
              - Deleted property: user_submitted_customer_metadata
              - Modified property: legal_name
                - Description changed from 'Claimed company name (optional, for reference)' to 'Company name(optional, for reference)'
              - Modified property: legal_person_identifier
                - Description changed from 'Official company registration code' to 'Official company registration code (required for automatic validation)'
              - Modified property: validation_method
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/ValidationMethodEnum
                    - New enum values: [wirtschaftscompass]

POST /api/onboarding-verifications/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Required changed
          - Deleted required property: legal_person_identifier
        - Properties changed
          - Deleted property: user_submitted_customer_metadata
          - Modified property: legal_name
            - Description changed from 'Claimed company name (optional, for reference)' to 'Company name(optional, for reference)'
          - Modified property: legal_person_identifier
            - Description changed from 'Official company registration code' to 'Official company registration code (required for automatic validation)'
            - MinLength changed from 1 to 0
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: onboarding_metadata
            - New required property: user_submitted_customer_data
            - Deleted required property: legal_person_identifier
          - Properties changed
            - New property: onboarding_metadata
            - New property: user_submitted_customer_data
            - Deleted property: user_submitted_customer_metadata
            - Modified property: legal_name
              - Description changed from 'Claimed company name (optional, for reference)' to 'Company name(optional, for reference)'
            - Modified property: legal_person_identifier
              - Description changed from 'Official company registration code' to 'Official company registration code (required for automatic validation)'
            - Modified property: validation_method
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/ValidationMethodEnum
                  - New enum values: [wirtschaftscompass]

GET /api/onboarding-verifications/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: onboarding_metadata
            - New required property: user_submitted_customer_data
            - Deleted required property: legal_person_identifier
          - Properties changed
            - New property: onboarding_metadata
            - New property: user_submitted_customer_data
            - Deleted property: user_submitted_customer_metadata
            - Modified property: legal_name
              - Description changed from 'Claimed company name (optional, for reference)' to 'Company name(optional, for reference)'
            - Modified property: legal_person_identifier
              - Description changed from 'Official company registration code' to 'Official company registration code (required for automatic validation)'
            - Modified property: validation_method
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/ValidationMethodEnum
                  - New enum values: [wirtschaftscompass]

PATCH /api/onboarding-verifications/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Deleted property: user_submitted_customer_metadata
          - Modified property: legal_name
            - Description changed from 'Claimed company name (optional, for reference)' to 'Company name(optional, for reference)'
          - Modified property: legal_person_identifier
            - Description changed from 'Official company registration code' to 'Official company registration code (required for automatic validation)'
            - MinLength changed from 1 to 0
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: onboarding_metadata
            - New required property: user_submitted_customer_data
            - Deleted required property: legal_person_identifier
          - Properties changed
            - New property: onboarding_metadata
            - New property: user_submitted_customer_data
            - Deleted property: user_submitted_customer_metadata
            - Modified property: legal_name
              - Description changed from 'Claimed company name (optional, for reference)' to 'Company name(optional, for reference)'
            - Modified property: legal_person_identifier
              - Description changed from 'Official company registration code' to 'Official company registration code (required for automatic validation)'
            - Modified property: validation_method
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/ValidationMethodEnum
                  - New enum values: [wirtschaftscompass]

PUT /api/onboarding-verifications/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Required changed
          - Deleted required property: legal_person_identifier
        - Properties changed
          - Deleted property: user_submitted_customer_metadata
          - Modified property: legal_name
            - Description changed from 'Claimed company name (optional, for reference)' to 'Company name(optional, for reference)'
          - Modified property: legal_person_identifier
            - Description changed from 'Official company registration code' to 'Official company registration code (required for automatic validation)'
            - MinLength changed from 1 to 0
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: onboarding_metadata
            - New required property: user_submitted_customer_data
            - Deleted required property: legal_person_identifier
          - Properties changed
            - New property: onboarding_metadata
            - New property: user_submitted_customer_data
            - Deleted property: user_submitted_customer_metadata
            - Modified property: legal_name
              - Description changed from 'Claimed company name (optional, for reference)' to 'Company name(optional, for reference)'
            - Modified property: legal_person_identifier
              - Description changed from 'Official company registration code' to 'Official company registration code (required for automatic validation)'
            - Modified property: validation_method
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/ValidationMethodEnum
                  - New enum values: [wirtschaftscompass]

GET /api/onboarding/supported-countries/

- Responses changed
  - New response: 200
  - Deleted response: supported_countries

GET /api/openstack-backups/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: customer_uuid
              - Modified property: instance_ports
                - Items changed
                  - Properties changed
                    - Modified property: security_groups
                      - Items changed
                        - Properties changed
                          - New property: customer_uuid
              - Modified property: restorations
                - Items changed
                  - Properties changed
                    - Modified property: ports
                      - Items changed
                        - Properties changed
                          - Modified property: security_groups
                            - Items changed
                              - Properties changed
                                - New property: customer_uuid

GET /api/openstack-backups/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid
            - Modified property: instance_ports
              - Items changed
                - Properties changed
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - New property: customer_uuid
            - Modified property: restorations
              - Items changed
                - Properties changed
                  - Modified property: ports
                    - Items changed
                      - Properties changed
                        - Modified property: security_groups
                          - Items changed
                            - Properties changed
                              - New property: customer_uuid

PATCH /api/openstack-backups/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid
            - Modified property: instance_ports
              - Items changed
                - Properties changed
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - New property: customer_uuid
            - Modified property: restorations
              - Items changed
                - Properties changed
                  - Modified property: ports
                    - Items changed
                      - Properties changed
                        - Modified property: security_groups
                          - Items changed
                            - Properties changed
                              - New property: customer_uuid

PUT /api/openstack-backups/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid
            - Modified property: instance_ports
              - Items changed
                - Properties changed
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - New property: customer_uuid
            - Modified property: restorations
              - Items changed
                - Properties changed
                  - Modified property: ports
                    - Items changed
                      - Properties changed
                        - Modified property: security_groups
                          - Items changed
                            - Properties changed
                              - New property: customer_uuid

POST /api/openstack-backups/{uuid}/restore/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid
            - Modified property: ports
              - Items changed
                - Properties changed
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - New property: customer_uuid

GET /api/openstack-floating-ips/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: customer_uuid

GET /api/openstack-floating-ips/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

GET /api/openstack-instances/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: customer_uuid
              - Modified property: ports
                - Items changed
                  - Properties changed
                    - Modified property: security_groups
                      - Items changed
                        - Properties changed
                          - New property: customer_uuid

GET /api/openstack-instances/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid
            - Modified property: ports
              - Items changed
                - Properties changed
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - New property: customer_uuid

PATCH /api/openstack-instances/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid
            - Modified property: ports
              - Items changed
                - Properties changed
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - New property: customer_uuid

PUT /api/openstack-instances/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid
            - Modified property: ports
              - Items changed
                - Properties changed
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - New property: customer_uuid

POST /api/openstack-instances/{uuid}/backup/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid
            - Modified property: instance_ports
              - Items changed
                - Properties changed
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - New property: customer_uuid
            - Modified property: restorations
              - Items changed
                - Properties changed
                  - Modified property: ports
                    - Items changed
                      - Properties changed
                        - Modified property: security_groups
                          - Items changed
                            - Properties changed
                              - New property: customer_uuid

GET /api/openstack-instances/{uuid}/ports/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: security_groups
                - Items changed
                  - Properties changed
                    - New property: customer_uuid

GET /api/openstack-networks/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: customer_uuid

GET /api/openstack-networks/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

PATCH /api/openstack-networks/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

PUT /api/openstack-networks/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

POST /api/openstack-networks/{uuid}/create_subnet/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

GET /api/openstack-ports/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: customer_uuid

POST /api/openstack-ports/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

GET /api/openstack-ports/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

PATCH /api/openstack-ports/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

PUT /api/openstack-ports/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

GET /api/openstack-routers/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: customer_uuid
              - Modified property: ports
                - Items changed
                  - Properties changed
                    - Modified property: security_groups
                      - Items changed
                        - Properties changed
                          - New property: customer_uuid

GET /api/openstack-routers/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid
            - Modified property: ports
              - Items changed
                - Properties changed
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - New property: customer_uuid

GET /api/openstack-security-groups/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: customer_uuid

GET /api/openstack-security-groups/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

GET /api/openstack-server-groups/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: customer_uuid

POST /api/openstack-server-groups/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

GET /api/openstack-server-groups/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

PATCH /api/openstack-server-groups/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

PUT /api/openstack-server-groups/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

GET /api/openstack-snapshots/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: customer_uuid

GET /api/openstack-snapshots/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

PATCH /api/openstack-snapshots/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

PUT /api/openstack-snapshots/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

POST /api/openstack-snapshots/{uuid}/restore/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

GET /api/openstack-subnets/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: customer_uuid

GET /api/openstack-subnets/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

PATCH /api/openstack-subnets/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

PUT /api/openstack-subnets/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

GET /api/openstack-tenants/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_uuid]
      - Deleted enum values: [access_url user_password user_username]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: customer_uuid

POST /api/openstack-tenants/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

GET /api/openstack-tenants/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_uuid]
      - Deleted enum values: [access_url user_password user_username]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

PATCH /api/openstack-tenants/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

PUT /api/openstack-tenants/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

POST /api/openstack-tenants/{uuid}/create_floating_ip/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

POST /api/openstack-tenants/{uuid}/create_network/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

POST /api/openstack-tenants/{uuid}/create_security_group/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

POST /api/openstack-tenants/{uuid}/create_server_group/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

POST /api/openstack-tenants/{uuid}/pull_security_groups/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

POST /api/openstack-tenants/{uuid}/pull_server_groups/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

GET /api/openstack-volumes/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: customer_uuid

GET /api/openstack-volumes/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

PATCH /api/openstack-volumes/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

PUT /api/openstack-volumes/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

POST /api/openstack-volumes/{uuid}/snapshot/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

GET /api/override-settings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: ONBOARDING_WICO_API_URL
            - New property: ONBOARDING_WICO_TOKEN

POST /api/override-settings/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: ONBOARDING_WICO_API_URL
          - New property: ONBOARDING_WICO_TOKEN
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: ONBOARDING_WICO_API_URL
          - New property: ONBOARDING_WICO_TOKEN
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: ONBOARDING_WICO_API_URL
          - New property: ONBOARDING_WICO_TOKEN

POST /api/projects/{uuid}/recover/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: end_date

GET /api/promotions-campaigns/{uuid}/orders/

- New query param: field

GET /api/promotions-campaigns/{uuid}/resources/

- New query param: field

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
                      - Modified property: options
                        - Property 'AllOf' changed
                          - Modified schema: #/components/schemas/OfferingOptions
                            - Properties changed
                              - Modified property: options
                                - AdditionalProperties changed
                                  - Properties changed
                                    - New property: cascade_config
                                    - New property: component_multiplier_config
                                    - Modified property: type
                                      - New enum values: [conditional_cascade component_multiplier]

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
                    - Modified property: options
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/OfferingOptions
                          - Properties changed
                            - Modified property: options
                              - AdditionalProperties changed
                                - Properties changed
                                  - New property: cascade_config
                                  - New property: component_multiplier_config
                                  - Modified property: type
                                    - New enum values: [conditional_cascade component_multiplier]

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
                    - Modified property: options
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/OfferingOptions
                          - Properties changed
                            - Modified property: options
                              - AdditionalProperties changed
                                - Properties changed
                                  - New property: cascade_config
                                  - New property: component_multiplier_config
                                  - Modified property: type
                                    - New enum values: [conditional_cascade component_multiplier]

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
                    - Modified property: options
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/OfferingOptions
                          - Properties changed
                            - Modified property: options
                              - AdditionalProperties changed
                                - Properties changed
                                  - New property: cascade_config
                                  - New property: component_multiplier_config
                                  - Modified property: type
                                    - New enum values: [conditional_cascade component_multiplier]

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
                    - Modified property: options
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/OfferingOptions
                          - Properties changed
                            - Modified property: options
                              - AdditionalProperties changed
                                - Properties changed
                                  - New property: cascade_config
                                  - New property: component_multiplier_config
                                  - Modified property: type
                                    - New enum values: [conditional_cascade component_multiplier]

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
                    - Modified property: options
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/OfferingOptions
                          - Properties changed
                            - Modified property: options
                              - AdditionalProperties changed
                                - Properties changed
                                  - New property: cascade_config
                                  - New property: component_multiplier_config
                                  - Modified property: type
                                    - New enum values: [conditional_cascade component_multiplier]

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
                  - Modified property: options
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/OfferingOptions
                        - Properties changed
                          - Modified property: options
                            - AdditionalProperties changed
                              - Properties changed
                                - New property: cascade_config
                                - New property: component_multiplier_config
                                - Modified property: type
                                  - New enum values: [conditional_cascade component_multiplier]

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
                  - Modified property: options
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/OfferingOptions
                        - Properties changed
                          - Modified property: options
                            - AdditionalProperties changed
                              - Properties changed
                                - New property: cascade_config
                                - New property: component_multiplier_config
                                - Modified property: type
                                  - New enum values: [conditional_cascade component_multiplier]

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
                  - Modified property: options
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/OfferingOptions
                        - Properties changed
                          - Modified property: options
                            - AdditionalProperties changed
                              - Properties changed
                                - New property: cascade_config
                                - New property: component_multiplier_config
                                - Modified property: type
                                  - New enum values: [conditional_cascade component_multiplier]

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
                  - Modified property: options
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/OfferingOptions
                        - Properties changed
                          - Modified property: options
                            - AdditionalProperties changed
                              - Properties changed
                                - New property: cascade_config
                                - New property: component_multiplier_config
                                - Modified property: type
                                  - New enum values: [conditional_cascade component_multiplier]

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
                  - Modified property: options
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/OfferingOptions
                        - Properties changed
                          - Modified property: options
                            - AdditionalProperties changed
                              - Properties changed
                                - New property: cascade_config
                                - New property: component_multiplier_config
                                - Modified property: type
                                  - New enum values: [conditional_cascade component_multiplier]

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
                  - Modified property: options
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/OfferingOptions
                        - Properties changed
                          - Modified property: options
                            - AdditionalProperties changed
                              - Properties changed
                                - New property: cascade_config
                                - New property: component_multiplier_config
                                - Modified property: type
                                  - New enum values: [conditional_cascade component_multiplier]

GET /api/proposal-protected-calls/{uuid}/offerings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OfferingOptions
                    - Properties changed
                      - Modified property: options
                        - AdditionalProperties changed
                          - Properties changed
                            - New property: cascade_config
                            - New property: component_multiplier_config
                            - Modified property: type
                              - New enum values: [conditional_cascade component_multiplier]

POST /api/proposal-protected-calls/{uuid}/offerings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: cascade_config
                          - New property: component_multiplier_config
                          - Modified property: type
                            - New enum values: [conditional_cascade component_multiplier]

GET /api/proposal-protected-calls/{uuid}/offerings/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: cascade_config
                          - New property: component_multiplier_config
                          - Modified property: type
                            - New enum values: [conditional_cascade component_multiplier]

PATCH /api/proposal-protected-calls/{uuid}/offerings/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: cascade_config
                          - New property: component_multiplier_config
                          - Modified property: type
                            - New enum values: [conditional_cascade component_multiplier]

PUT /api/proposal-protected-calls/{uuid}/offerings/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: cascade_config
                          - New property: component_multiplier_config
                          - Modified property: type
                            - New enum values: [conditional_cascade component_multiplier]

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
                  - Modified property: options
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/OfferingOptions
                        - Properties changed
                          - Modified property: options
                            - AdditionalProperties changed
                              - Properties changed
                                - New property: cascade_config
                                - New property: component_multiplier_config
                                - Modified property: type
                                  - New enum values: [conditional_cascade component_multiplier]

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
                    - Modified property: options
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/OfferingOptions
                          - Properties changed
                            - Modified property: options
                              - AdditionalProperties changed
                                - Properties changed
                                  - New property: cascade_config
                                  - New property: component_multiplier_config
                                  - Modified property: type
                                    - New enum values: [conditional_cascade component_multiplier]

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
                  - Modified property: options
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/OfferingOptions
                        - Properties changed
                          - Modified property: options
                            - AdditionalProperties changed
                              - Properties changed
                                - New property: cascade_config
                                - New property: component_multiplier_config
                                - Modified property: type
                                  - New enum values: [conditional_cascade component_multiplier]

GET /api/proposal-requested-offerings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OfferingOptions
                    - Properties changed
                      - Modified property: options
                        - AdditionalProperties changed
                          - Properties changed
                            - New property: cascade_config
                            - New property: component_multiplier_config
                            - Modified property: type
                              - New enum values: [conditional_cascade component_multiplier]

GET /api/proposal-requested-offerings/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: cascade_config
                          - New property: component_multiplier_config
                          - Modified property: type
                            - New enum values: [conditional_cascade component_multiplier]

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
                      - Modified property: options
                        - Property 'AllOf' changed
                          - Modified schema: #/components/schemas/OfferingOptions
                            - Properties changed
                              - Modified property: options
                                - AdditionalProperties changed
                                  - Properties changed
                                    - New property: cascade_config
                                    - New property: component_multiplier_config
                                    - Modified property: type
                                      - New enum values: [conditional_cascade component_multiplier]

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
                    - Modified property: options
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/OfferingOptions
                          - Properties changed
                            - Modified property: options
                              - AdditionalProperties changed
                                - Properties changed
                                  - New property: cascade_config
                                  - New property: component_multiplier_config
                                  - Modified property: type
                                    - New enum values: [conditional_cascade component_multiplier]

GET /api/proposal-reviews/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - Deleted required property: anonymous_reviewer_name
              - Deleted required property: reviewer
              - Deleted required property: reviewer_full_name
              - Deleted required property: reviewer_uuid

POST /api/proposal-reviews/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Required changed
          - Deleted required property: reviewer
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: anonymous_reviewer_name
            - Deleted required property: reviewer
            - Deleted required property: reviewer_full_name
            - Deleted required property: reviewer_uuid

GET /api/proposal-reviews/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: anonymous_reviewer_name
            - Deleted required property: reviewer
            - Deleted required property: reviewer_full_name
            - Deleted required property: reviewer_uuid

PATCH /api/proposal-reviews/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: anonymous_reviewer_name
            - Deleted required property: reviewer
            - Deleted required property: reviewer_full_name
            - Deleted required property: reviewer_uuid

PUT /api/proposal-reviews/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Required changed
          - Deleted required property: reviewer
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: anonymous_reviewer_name
            - Deleted required property: reviewer
            - Deleted required property: reviewer_full_name
            - Deleted required property: reviewer_uuid

GET /api/rancher-apps/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: customer_uuid

POST /api/rancher-apps/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

GET /api/rancher-apps/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

PATCH /api/rancher-apps/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

PUT /api/rancher-apps/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

GET /api/rancher-clusters/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: customer_uuid

GET /api/rancher-clusters/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

PATCH /api/rancher-clusters/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

PUT /api/rancher-clusters/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

POST /api/rancher-clusters/{uuid}/create_management_security_group/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

GET /api/rancher-ingresses/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: customer_uuid

POST /api/rancher-ingresses/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

GET /api/rancher-ingresses/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

PATCH /api/rancher-ingresses/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

PUT /api/rancher-ingresses/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

GET /api/rancher-ingresses/{uuid}/yaml/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

PUT /api/rancher-ingresses/{uuid}/yaml/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

GET /api/rancher-services/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: customer_uuid

POST /api/rancher-services/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: customer_uuid
          - Properties changed
            - New property: customer_uuid

GET /api/rancher-services/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

PATCH /api/rancher-services/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

PUT /api/rancher-services/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

GET /api/rancher-services/{uuid}/yaml/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

PUT /api/rancher-services/{uuid}/yaml/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

GET /api/slurm-allocations/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: customer_uuid

POST /api/slurm-allocations/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

GET /api/slurm-allocations/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

PATCH /api/slurm-allocations/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

PUT /api/slurm-allocations/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

GET /api/slurm-jobs/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: customer_uuid

POST /api/slurm-jobs/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

GET /api/slurm-jobs/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

PATCH /api/slurm-jobs/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

PUT /api/slurm-jobs/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

GET /api/users/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [birth_date]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: birth_date

POST /api/users/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: birth_date
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: birth_date
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: birth_date
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: birth_date

GET /api/users/me/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [birth_date]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: birth_date

GET /api/users/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [birth_date]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: birth_date

PATCH /api/users/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: birth_date
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: birth_date
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: birth_date
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: birth_date

PUT /api/users/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: birth_date
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: birth_date
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: birth_date
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: birth_date

GET /api/vmware-disks/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: customer_uuid

GET /api/vmware-disks/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

GET /api/vmware-ports/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: customer_uuid

GET /api/vmware-ports/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

GET /api/vmware-virtual-machine/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: customer_uuid

POST /api/vmware-virtual-machine/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

GET /api/vmware-virtual-machine/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

PATCH /api/vmware-virtual-machine/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

PUT /api/vmware-virtual-machine/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

POST /api/vmware-virtual-machine/{uuid}/create_disk/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

POST /api/vmware-virtual-machine/{uuid}/create_port/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_uuid

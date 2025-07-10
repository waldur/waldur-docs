# OpenAPI schema diff - 7.6.8

## For version 7.6.8

### New Endpoints: 35

---------------------
GET /api/backend-resource-requests/  
POST /api/backend-resource-requests/  
GET /api/backend-resource-requests/{uuid}/  
POST /api/backend-resource-requests/{uuid}/set_done/  
POST /api/backend-resource-requests/{uuid}/set_erred/  
POST /api/backend-resource-requests/{uuid}/start_processing/  
GET /api/backend-resources/  
POST /api/backend-resources/  
DELETE /api/backend-resources/{uuid}/  
GET /api/backend-resources/{uuid}/  
POST /api/backend-resources/{uuid}/import_resource/  
GET /api/marketplace-maintenance-announcement-offerings/  
POST /api/marketplace-maintenance-announcement-offerings/  
DELETE /api/marketplace-maintenance-announcement-offerings/{uuid}/  
GET /api/marketplace-maintenance-announcement-offerings/{uuid}/  
PATCH /api/marketplace-maintenance-announcement-offerings/{uuid}/  
PUT /api/marketplace-maintenance-announcement-offerings/{uuid}/  
GET /api/marketplace-maintenance-announcement-template-offerings/  
POST /api/marketplace-maintenance-announcement-template-offerings/  
DELETE /api/marketplace-maintenance-announcement-template-offerings/{uuid}/  
GET /api/marketplace-maintenance-announcement-template-offerings/{uuid}/  
PATCH /api/marketplace-maintenance-announcement-template-offerings/{uuid}/  
PUT /api/marketplace-maintenance-announcement-template-offerings/{uuid}/  
GET /api/marketplace-maintenance-announcements-template/  
POST /api/marketplace-maintenance-announcements-template/  
DELETE /api/marketplace-maintenance-announcements-template/{uuid}/  
GET /api/marketplace-maintenance-announcements-template/{uuid}/  
PATCH /api/marketplace-maintenance-announcements-template/{uuid}/  
PUT /api/marketplace-maintenance-announcements-template/{uuid}/  
GET /api/marketplace-maintenance-announcements/  
POST /api/marketplace-maintenance-announcements/  
DELETE /api/marketplace-maintenance-announcements/{uuid}/  
GET /api/marketplace-maintenance-announcements/{uuid}/  
PATCH /api/marketplace-maintenance-announcements/{uuid}/  
PUT /api/marketplace-maintenance-announcements/{uuid}/  

### Deleted Endpoints: None

---------------------------

### Modified Endpoints: 268

---------------------------
GET /api/access-subnets/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/admin-announcements/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/auth-tokens/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/autoprovisioning-rule-plans/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/autoprovisioning-rules/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/aws-images/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/aws-instances/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/aws-regions/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/aws-sizes/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/aws-volumes/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/azure-images/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/azure-locations/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/azure-public-ips/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/azure-resource-groups/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/azure-sizes/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/azure-sql-databases/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/azure-sql-servers/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/azure-virtualmachines/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/booking-offerings/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'
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
                    - Modified property: factor
                      - Nullable changed from false to true
              - Modified property: plans
                - Items changed
                  - Properties changed
                    - Modified property: description
                      - MaxLength changed from 2000 to null
              - Modified property: plugin_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedPluginOptions
                    - Properties changed
                      - New property: minimal_team_count_for_provisioning
                      - New property: required_team_role_for_provisioning

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
                  - Modified property: factor
                    - Nullable changed from false to true
            - Modified property: plans
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to null
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: minimal_team_count_for_provisioning
                    - New property: required_team_role_for_provisioning

GET /api/booking-resources/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'
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
                      - Modified property: attributes
                        - Type changed from 'object' to ''
                        - Description changed from 'Get attributes excluding secret attributes, such as username and password.' to ''
                        - ReadOnly changed from true to false
                        - AdditionalProperties changed
                          - Schema deleted
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - Modified property: attributes
                        - Type changed from 'object' to ''
                        - Description changed from 'Get attributes excluding secret attributes, such as username and password.' to ''
                        - ReadOnly changed from true to false
                        - AdditionalProperties changed
                          - Schema deleted

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
                    - Modified property: attributes
                      - Type changed from 'object' to ''
                      - Description changed from 'Get attributes excluding secret attributes, such as username and password.' to ''
                      - ReadOnly changed from true to false
                      - AdditionalProperties changed
                        - Schema deleted
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: attributes
                      - Type changed from 'object' to ''
                      - Description changed from 'Get attributes excluding secret attributes, such as username and password.' to ''
                      - ReadOnly changed from true to false
                      - AdditionalProperties changed
                        - Schema deleted

GET /api/broadcast-message-templates/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/broadcast-messages/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/call-managing-organisations/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/call-rounds/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/component-user-usage-limits/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/customer-credits/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/customer-permissions-reviews/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/digitalocean-droplets/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/digitalocean-images/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/digitalocean-regions/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/digitalocean-sizes/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/email-logs/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/event-subscriptions/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/events-stats/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/events/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/financial-reports/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/freeipa-profiles/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/google-auth/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/hooks-email/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: event_types
                - Items changed
                  - New enum values: [openstack_security_group_added_remotely openstack_security_group_removed_remotely openstack_security_group_added_locally openstack_security_group_removed_locally]

POST /api/hooks-email/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [openstack_security_group_added_remotely openstack_security_group_removed_remotely openstack_security_group_added_locally openstack_security_group_removed_locally]
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [openstack_security_group_added_remotely openstack_security_group_removed_remotely openstack_security_group_added_locally openstack_security_group_removed_locally]

GET /api/hooks-email/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [openstack_security_group_added_remotely openstack_security_group_removed_remotely openstack_security_group_added_locally openstack_security_group_removed_locally]

PATCH /api/hooks-email/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [openstack_security_group_added_remotely openstack_security_group_removed_remotely openstack_security_group_added_locally openstack_security_group_removed_locally]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [openstack_security_group_added_remotely openstack_security_group_removed_remotely openstack_security_group_added_locally openstack_security_group_removed_locally]

PUT /api/hooks-email/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [openstack_security_group_added_remotely openstack_security_group_removed_remotely openstack_security_group_added_locally openstack_security_group_removed_locally]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [openstack_security_group_added_remotely openstack_security_group_removed_remotely openstack_security_group_added_locally openstack_security_group_removed_locally]

GET /api/hooks-web/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: event_types
                - Items changed
                  - New enum values: [openstack_security_group_added_remotely openstack_security_group_removed_remotely openstack_security_group_added_locally openstack_security_group_removed_locally]

POST /api/hooks-web/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [openstack_security_group_added_remotely openstack_security_group_removed_remotely openstack_security_group_added_locally openstack_security_group_removed_locally]
      - Examples changed
        - Modified example: Webhook-create
          - Value changed from map[destination_url:http://example.com/ event_groups:[users] event_types:[resource_start_succeeded]] to map[destination_url:http://example.com/ event_groups:[users] event_types:[customer_update_succeeded]]
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [openstack_security_group_added_remotely openstack_security_group_removed_remotely openstack_security_group_added_locally openstack_security_group_removed_locally]

GET /api/hooks-web/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [openstack_security_group_added_remotely openstack_security_group_removed_remotely openstack_security_group_added_locally openstack_security_group_removed_locally]

PATCH /api/hooks-web/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [openstack_security_group_added_remotely openstack_security_group_removed_remotely openstack_security_group_added_locally openstack_security_group_removed_locally]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [openstack_security_group_added_remotely openstack_security_group_removed_remotely openstack_security_group_added_locally openstack_security_group_removed_locally]

PUT /api/hooks-web/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [openstack_security_group_added_remotely openstack_security_group_removed_remotely openstack_security_group_added_locally openstack_security_group_removed_locally]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [openstack_security_group_added_remotely openstack_security_group_removed_remotely openstack_security_group_added_locally openstack_security_group_removed_locally]

GET /api/hooks/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/identity-providers/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/invoice-items/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/invoices/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/keycloak-groups/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/keycloak-user-group-memberships/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/keys/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/lexis-links/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/marketplace-categories/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/marketplace-category-columns/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/marketplace-category-component-usages/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/marketplace-category-components/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/marketplace-category-groups/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/marketplace-category-help-articles/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/marketplace-checklists-categories/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/marketplace-checklists-categories/{category_uuid}/checklists/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/marketplace-checklists/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/marketplace-checklists/{checklist_uuid}/answers/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/marketplace-checklists/{checklist_uuid}/questions/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/marketplace-checklists/{checklist_uuid}/user/{user_uuid}/answers/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/marketplace-component-usages/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/marketplace-component-user-usages/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/marketplace-customer-estimated-cost-policies/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/marketplace-customer-service-accounts/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/marketplace-integration-statuses/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/marketplace-offering-estimated-cost-policies/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/marketplace-offering-files/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/marketplace-offering-permissions-log/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'
- Modified query param: scope_uuid
  - Schema changed
    - Format changed from 'uuid' to ''

GET /api/marketplace-offering-permissions/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'
- Modified query param: scope_uuid
  - Schema changed
    - Format changed from 'uuid' to ''

GET /api/marketplace-offering-referrals/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/marketplace-offering-usage-policies/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/marketplace-offering-user-roles/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/marketplace-offering-users/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/marketplace-orders/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: attributes
                - Type changed from 'object' to ''
                - Description changed from 'Get attributes excluding secret attributes, such as username and password.' to ''
                - ReadOnly changed from true to false
                - AdditionalProperties changed
                  - Schema deleted

GET /api/marketplace-orders/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: attributes
              - Type changed from 'object' to ''
              - Description changed from 'Get attributes excluding secret attributes, such as username and password.' to ''
              - ReadOnly changed from true to false
              - AdditionalProperties changed
                - Schema deleted

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
                  - Modified property: factor
                    - Nullable changed from false to true
            - Modified property: plans
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to null
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: minimal_team_count_for_provisioning
                    - New property: required_team_role_for_provisioning

GET /api/marketplace-plan-components/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/marketplace-plans/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to null

POST /api/marketplace-plans/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to null
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to null

GET /api/marketplace-plans/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to null

PATCH /api/marketplace-plans/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to null
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to null

PUT /api/marketplace-plans/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to null
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to null

GET /api/marketplace-project-estimated-cost-policies/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/marketplace-project-service-accounts/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/marketplace-project-update-requests/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/marketplace-provider-offerings/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'
- Modified query param: scope_uuid
  - Schema changed
    - Format changed from 'uuid' to ''
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
                    - Modified property: factor
                      - Nullable changed from false to true
              - Modified property: plans
                - Items changed
                  - Properties changed
                    - Modified property: description
                      - MaxLength changed from 2000 to null
              - Modified property: plugin_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedPluginOptions
                    - Properties changed
                      - New property: minimal_team_count_for_provisioning
                      - New property: required_team_role_for_provisioning

POST /api/marketplace-provider-offerings/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to null
          - Modified property: plans
            - Items changed
              - Properties changed
                - Modified property: description
                  - MaxLength changed from 2000 to null
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Properties changed
                  - Modified property: factor
                    - Nullable changed from false to true
            - Modified property: description
              - MaxLength changed from 2000 to null
            - Modified property: plans
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to null
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: minimal_team_count_for_provisioning
                    - New property: required_team_role_for_provisioning

GET /api/marketplace-provider-offerings/groups/

- Modified query param: scope_uuid
  - Schema changed
    - Format changed from 'uuid' to ''

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
                  - Modified property: factor
                    - Nullable changed from false to true
            - Modified property: plans
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to null
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: minimal_team_count_for_provisioning
                    - New property: required_team_role_for_provisioning

GET /api/marketplace-provider-offerings/{uuid}/component_stats/

- Modified query param: scope_uuid
  - Schema changed
    - Format changed from 'uuid' to ''

GET /api/marketplace-provider-offerings/{uuid}/costs/

- Modified query param: scope_uuid
  - Schema changed
    - Format changed from 'uuid' to ''

GET /api/marketplace-provider-offerings/{uuid}/customers/

- Modified query param: scope_uuid
  - Schema changed
    - Format changed from 'uuid' to ''

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
                    - Modified property: attributes
                      - Type changed from 'object' to ''
                      - Description changed from 'Get attributes excluding secret attributes, such as username and password.' to ''
                      - ReadOnly changed from true to false
                      - AdditionalProperties changed
                        - Schema deleted
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: attributes
                      - Type changed from 'object' to ''
                      - Description changed from 'Get attributes excluding secret attributes, such as username and password.' to ''
                      - ReadOnly changed from true to false
                      - AdditionalProperties changed
                        - Schema deleted

GET /api/marketplace-provider-offerings/{uuid}/list_customer_projects/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to null

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
                  - Modified property: factor
                    - Nullable changed from false to true
            - Modified property: plans
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to null
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: minimal_team_count_for_provisioning
                    - New property: required_team_role_for_provisioning

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
                  - Modified property: factor
                    - Nullable changed from false to true
            - Modified property: plans
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to null
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: minimal_team_count_for_provisioning
                    - New property: required_team_role_for_provisioning

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
                  - Modified property: factor
                    - Nullable changed from false to true
            - Modified property: plans
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to null
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: minimal_team_count_for_provisioning
                    - New property: required_team_role_for_provisioning

GET /api/marketplace-provider-offerings/{uuid}/orders/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: attributes
                - Type changed from 'object' to ''
                - Description changed from 'Get attributes excluding secret attributes, such as username and password.' to ''
                - ReadOnly changed from true to false
                - AdditionalProperties changed
                  - Schema deleted

GET /api/marketplace-provider-offerings/{uuid}/orders/{order_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: attributes
              - Type changed from 'object' to ''
              - Description changed from 'Get attributes excluding secret attributes, such as username and password.' to ''
              - ReadOnly changed from true to false
              - AdditionalProperties changed
                - Schema deleted

POST /api/marketplace-provider-offerings/{uuid}/refresh_offering_usernames/

- Description changed from '' to 'Refresh offering user usernames.'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: plans
            - Items changed
              - Properties changed
                - Modified property: description
                  - MaxLength changed from 2000 to null
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: status
          - Properties changed
            - New property: status
            - Deleted property: access_url
            - Deleted property: attributes
            - Deleted property: backend_id
            - Deleted property: backend_metadata
            - Deleted property: billable
            - Deleted property: category
            - Deleted property: category_title
            - Deleted property: category_uuid
            - Deleted property: citation_count
            - Deleted property: components
            - Deleted property: country
            - Deleted property: created
            - Deleted property: customer
            - Deleted property: customer_name
            - Deleted property: customer_uuid
            - Deleted property: datacite_doi
            - Deleted property: description
            - Deleted property: endpoints
            - Deleted property: files
            - Deleted property: full_description
            - Deleted property: getting_started
            - Deleted property: google_calendar_is_public
            - Deleted property: google_calendar_link
            - Deleted property: image
            - Deleted property: integration_guide
            - Deleted property: integration_status
            - Deleted property: latitude
            - Deleted property: longitude
            - Deleted property: name
            - Deleted property: options
            - Deleted property: order_count
            - Deleted property: organization_groups
            - Deleted property: parent_description
            - Deleted property: parent_name
            - Deleted property: parent_uuid
            - Deleted property: paused_reason
            - Deleted property: plans
            - Deleted property: plugin_options
            - Deleted property: privacy_policy_link
            - Deleted property: project
            - Deleted property: project_name
            - Deleted property: project_uuid
            - Deleted property: quotas
            - Deleted property: resource_options
            - Deleted property: roles
            - Deleted property: scope
            - Deleted property: scope_error_message
            - Deleted property: scope_name
            - Deleted property: scope_state
            - Deleted property: scope_uuid
            - Deleted property: screenshots
            - Deleted property: secret_options
            - Deleted property: service_attributes
            - Deleted property: shared
            - Deleted property: slug
            - Deleted property: state
            - Deleted property: terms_of_service
            - Deleted property: terms_of_service_link
            - Deleted property: thumbnail
            - Deleted property: total_cost
            - Deleted property: total_cost_estimated
            - Deleted property: total_customers
            - Deleted property: type
            - Deleted property: url
            - Deleted property: uuid
            - Deleted property: vendor_details

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
                  - Modified property: factor
                    - Nullable changed from false to true
            - Modified property: plans
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to null
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: minimal_team_count_for_provisioning
                    - New property: required_team_role_for_provisioning

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
                  - Modified property: factor
                    - Nullable changed from false to true
            - Modified property: plans
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to null
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: minimal_team_count_for_provisioning
                    - New property: required_team_role_for_provisioning

POST /api/marketplace-provider-offerings/{uuid}/update_integration/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: plugin_options
            - Properties changed
              - New property: minimal_team_count_for_provisioning
              - New property: required_team_role_for_provisioning

POST /api/marketplace-provider-offerings/{uuid}/update_offering_component/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Required changed
          - New required property: uuid
        - Properties changed
          - New property: uuid

POST /api/marketplace-provider-offerings/{uuid}/update_overview/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to null

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
                  - Modified property: factor
                    - Nullable changed from false to true
            - Modified property: plans
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to null
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: minimal_team_count_for_provisioning
                    - New property: required_team_role_for_provisioning

GET /api/marketplace-provider-resources/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'
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
                      - Modified property: attributes
                        - Type changed from 'object' to ''
                        - Description changed from 'Get attributes excluding secret attributes, such as username and password.' to ''
                        - ReadOnly changed from true to false
                        - AdditionalProperties changed
                          - Schema deleted
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - Modified property: attributes
                        - Type changed from 'object' to ''
                        - Description changed from 'Get attributes excluding secret attributes, such as username and password.' to ''
                        - ReadOnly changed from true to false
                        - AdditionalProperties changed
                          - Schema deleted

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
                    - Modified property: attributes
                      - Type changed from 'object' to ''
                      - Description changed from 'Get attributes excluding secret attributes, such as username and password.' to ''
                      - ReadOnly changed from true to false
                      - AdditionalProperties changed
                        - Schema deleted
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: attributes
                      - Type changed from 'object' to ''
                      - Description changed from 'Get attributes excluding secret attributes, such as username and password.' to ''
                      - ReadOnly changed from true to false
                      - AdditionalProperties changed
                        - Schema deleted

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
                    - Modified property: attributes
                      - Type changed from 'object' to ''
                      - Description changed from 'Get attributes excluding secret attributes, such as username and password.' to ''
                      - ReadOnly changed from true to false
                      - AdditionalProperties changed
                        - Schema deleted
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: attributes
                      - Type changed from 'object' to ''
                      - Description changed from 'Get attributes excluding secret attributes, such as username and password.' to ''
                      - ReadOnly changed from true to false
                      - AdditionalProperties changed
                        - Schema deleted

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
                    - Modified property: attributes
                      - Type changed from 'object' to ''
                      - Description changed from 'Get attributes excluding secret attributes, such as username and password.' to ''
                      - ReadOnly changed from true to false
                      - AdditionalProperties changed
                        - Schema deleted
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: attributes
                      - Type changed from 'object' to ''
                      - Description changed from 'Get attributes excluding secret attributes, such as username and password.' to ''
                      - ReadOnly changed from true to false
                      - AdditionalProperties changed
                        - Schema deleted

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
                  - Modified property: factor
                    - Nullable changed from false to true
            - Modified property: plans
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to null
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: minimal_team_count_for_provisioning
                    - New property: required_team_role_for_provisioning

POST /api/marketplace-provider-resources/{uuid}/set_as_erred/

- Description changed from '' to 'Set the resource as erred.'
- Responses changed
  - Modified response: 200
    - Description changed from '' to 'No response body'
    - Content changed
      - Deleted media type: application/json

POST /api/marketplace-provider-resources/{uuid}/set_backend_id/

- Description changed from '' to 'Set resource backend ID.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: status
          - Properties changed
            - New property: status
            - Deleted property: backend_id

POST /api/marketplace-provider-resources/{uuid}/set_backend_metadata/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: status
            - Deleted required property: backend_metadata
          - Properties changed
            - New property: status
            - Deleted property: backend_metadata

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
                    - Modified property: attributes
                      - Type changed from 'object' to ''
                      - Description changed from 'Get attributes excluding secret attributes, such as username and password.' to ''
                      - ReadOnly changed from true to false
                      - AdditionalProperties changed
                        - Schema deleted
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: attributes
                      - Type changed from 'object' to ''
                      - Description changed from 'Get attributes excluding secret attributes, such as username and password.' to ''
                      - ReadOnly changed from true to false
                      - AdditionalProperties changed
                        - Schema deleted

POST /api/marketplace-provider-resources/{uuid}/set_limits/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: status
            - Deleted required property: limits
          - Properties changed
            - New property: status
            - Deleted property: limits

POST /api/marketplace-provider-resources/{uuid}/submit_report/

- Description changed from '' to 'Submit resource report.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: status
            - Deleted required property: report
          - Properties changed
            - New property: status
            - Deleted property: report

GET /api/marketplace-public-offerings/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'
- Modified query param: scope_uuid
  - Schema changed
    - Format changed from 'uuid' to ''
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
                    - Modified property: factor
                      - Nullable changed from false to true
              - Modified property: plans
                - Items changed
                  - Properties changed
                    - Modified property: description
                      - MaxLength changed from 2000 to null
              - Modified property: plugin_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedPluginOptions
                    - Properties changed
                      - New property: minimal_team_count_for_provisioning
                      - New property: required_team_role_for_provisioning

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
                  - Modified property: factor
                    - Nullable changed from false to true
            - Modified property: plans
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to null
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: minimal_team_count_for_provisioning
                    - New property: required_team_role_for_provisioning

GET /api/marketplace-public-offerings/{uuid}/plans/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to null

GET /api/marketplace-public-offerings/{uuid}/plans/{plan_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to null

GET /api/marketplace-remote-synchronisations/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/marketplace-resource-users/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/marketplace-resources/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'
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
                      - Modified property: attributes
                        - Type changed from 'object' to ''
                        - Description changed from 'Get attributes excluding secret attributes, such as username and password.' to ''
                        - ReadOnly changed from true to false
                        - AdditionalProperties changed
                          - Schema deleted
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - Modified property: attributes
                        - Type changed from 'object' to ''
                        - Description changed from 'Get attributes excluding secret attributes, such as username and password.' to ''
                        - ReadOnly changed from true to false
                        - AdditionalProperties changed
                          - Schema deleted

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
                    - Modified property: attributes
                      - Type changed from 'object' to ''
                      - Description changed from 'Get attributes excluding secret attributes, such as username and password.' to ''
                      - ReadOnly changed from true to false
                      - AdditionalProperties changed
                        - Schema deleted
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: attributes
                      - Type changed from 'object' to ''
                      - Description changed from 'Get attributes excluding secret attributes, such as username and password.' to ''
                      - ReadOnly changed from true to false
                      - AdditionalProperties changed
                        - Schema deleted

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
                    - Modified property: attributes
                      - Type changed from 'object' to ''
                      - Description changed from 'Get attributes excluding secret attributes, such as username and password.' to ''
                      - ReadOnly changed from true to false
                      - AdditionalProperties changed
                        - Schema deleted
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: attributes
                      - Type changed from 'object' to ''
                      - Description changed from 'Get attributes excluding secret attributes, such as username and password.' to ''
                      - ReadOnly changed from true to false
                      - AdditionalProperties changed
                        - Schema deleted

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
                    - Modified property: attributes
                      - Type changed from 'object' to ''
                      - Description changed from 'Get attributes excluding secret attributes, such as username and password.' to ''
                      - ReadOnly changed from true to false
                      - AdditionalProperties changed
                        - Schema deleted
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: attributes
                      - Type changed from 'object' to ''
                      - Description changed from 'Get attributes excluding secret attributes, such as username and password.' to ''
                      - ReadOnly changed from true to false
                      - AdditionalProperties changed
                        - Schema deleted

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
                  - Modified property: factor
                    - Nullable changed from false to true
            - Modified property: plans
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to null
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: minimal_team_count_for_provisioning
                    - New property: required_team_role_for_provisioning

POST /api/marketplace-resources/{uuid}/update_options/

- Description changed from '' to 'Update resource options.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: status
          - Properties changed
            - New property: status
            - Deleted property: options

GET /api/marketplace-robot-accounts/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'
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
                      - New property: minimal_team_count_for_provisioning
                      - New property: required_team_role_for_provisioning

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
                    - New property: minimal_team_count_for_provisioning
                    - New property: required_team_role_for_provisioning

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
                    - New property: minimal_team_count_for_provisioning
                    - New property: required_team_role_for_provisioning

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
                    - New property: minimal_team_count_for_provisioning
                    - New property: required_team_role_for_provisioning

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
                    - New property: minimal_team_count_for_provisioning
                    - New property: required_team_role_for_provisioning

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
                    - New property: minimal_team_count_for_provisioning
                    - New property: required_team_role_for_provisioning

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
                    - New property: minimal_team_count_for_provisioning
                    - New property: required_team_role_for_provisioning

GET /api/marketplace-screenshots/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/marketplace-script-async-dry-run/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

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
                  - Modified property: factor
                    - Nullable changed from false to true
            - Modified property: plans
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to null
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: minimal_team_count_for_provisioning
                    - New property: required_team_role_for_provisioning

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
                  - Modified property: factor
                    - Nullable changed from false to true
            - Modified property: plans
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to null
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: minimal_team_count_for_provisioning
                    - New property: required_team_role_for_provisioning

GET /api/marketplace-sections/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/marketplace-service-providers/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/marketplace-service-providers/{service_provider_uuid}/customer_projects/

- New query param: slug

GET /api/marketplace-service-providers/{service_provider_uuid}/offerings/

- Modified query param: scope_uuid
  - Schema changed
    - Format changed from 'uuid' to ''
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
                    - Modified property: factor
                      - Nullable changed from false to true
              - Modified property: plans
                - Items changed
                  - Properties changed
                    - Modified property: description
                      - MaxLength changed from 2000 to null

GET /api/marketplace-service-providers/{service_provider_uuid}/project_permissions/

- Modified query param: scope_uuid
  - Schema changed
    - Format changed from 'uuid' to ''

GET /api/marketplace-service-providers/{service_provider_uuid}/projects/

- New query param: slug
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to null

GET /api/notification-messages-templates/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/notification-messages/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/openstack-backups/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/openstack-flavors/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'
- New query param: offering_uuid

GET /api/openstack-images/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'
- New query param: offering_uuid

GET /api/openstack-instance-availability-zones/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/openstack-instances/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/openstack-marketplace-tenants/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/openstack-migrations/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/openstack-network-rbac-policies/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/openstack-networks/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/openstack-ports/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/openstack-routers/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/openstack-security-groups/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/openstack-server-groups/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/openstack-snapshots/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/openstack-subnets/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/openstack-tenants/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/openstack-volume-availability-zones/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/openstack-volume-types/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'
- New query param: offering_uuid

GET /api/openstack-volumes/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/organization-groups/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/override-settings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: MAINTENANCE_ANNOUNCEMENT_NOTIFY_BEFORE_MINUTES
            - New property: MAINTENANCE_ANNOUNCEMENT_NOTIFY_SYSTEM

POST /api/override-settings/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: MAINTENANCE_ANNOUNCEMENT_NOTIFY_BEFORE_MINUTES
          - New property: MAINTENANCE_ANNOUNCEMENT_NOTIFY_SYSTEM

GET /api/payment-profiles/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/payments/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/project-credits/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/project-types/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/projects/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'
- New query param: slug
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to null

POST /api/projects/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to null
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to null

GET /api/projects/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to null

PATCH /api/projects/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to null
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to null

PUT /api/projects/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to null
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to null

POST /api/projects/{uuid}/move_project/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to null

GET /api/promotions-campaigns/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/promotions-campaigns/{uuid}/orders/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: attributes
                - Type changed from 'object' to ''
                - Description changed from 'Get attributes excluding secret attributes, such as username and password.' to ''
                - ReadOnly changed from true to false
                - AdditionalProperties changed
                  - Schema deleted

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
                      - Modified property: attributes
                        - Type changed from 'object' to ''
                        - Description changed from 'Get attributes excluding secret attributes, such as username and password.' to ''
                        - ReadOnly changed from true to false
                        - AdditionalProperties changed
                          - Schema deleted
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - Modified property: attributes
                        - Type changed from 'object' to ''
                        - Description changed from 'Get attributes excluding secret attributes, such as username and password.' to ''
                        - ReadOnly changed from true to false
                        - AdditionalProperties changed
                          - Schema deleted

GET /api/proposal-proposals/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to null

POST /api/proposal-proposals/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to null
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to null

GET /api/proposal-proposals/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to null

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
                      - New property: created
                      - Modified property: components
                        - Items changed
                          - Properties changed
                            - Modified property: factor
                              - Nullable changed from false to true
                      - Modified property: plan_details
                        - Property 'AllOf' changed
                          - Modified schema: #/components/schemas/BasePublicPlan
                            - Properties changed
                              - Modified property: description
                                - MaxLength changed from 2000 to null

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
                    - New property: created
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - Modified property: factor
                            - Nullable changed from false to true
                    - Modified property: plan_details
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BasePublicPlan
                          - Properties changed
                            - Modified property: description
                              - MaxLength changed from 2000 to null

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
                    - New property: created
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - Modified property: factor
                            - Nullable changed from false to true
                    - Modified property: plan_details
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BasePublicPlan
                          - Properties changed
                            - Modified property: description
                              - MaxLength changed from 2000 to null

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
                    - New property: created
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - Modified property: factor
                            - Nullable changed from false to true
                    - Modified property: plan_details
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BasePublicPlan
                          - Properties changed
                            - Modified property: description
                              - MaxLength changed from 2000 to null

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
                    - New property: created
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - Modified property: factor
                            - Nullable changed from false to true
                    - Modified property: plan_details
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BasePublicPlan
                          - Properties changed
                            - Modified property: description
                              - MaxLength changed from 2000 to null

GET /api/proposal-protected-calls/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to null
              - Modified property: offerings
                - Items changed
                  - Properties changed
                    - New property: created
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - Modified property: factor
                            - Nullable changed from false to true
                    - Modified property: plan_details
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BasePublicPlan
                          - Properties changed
                            - Modified property: description
                              - MaxLength changed from 2000 to null

POST /api/proposal-protected-calls/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to null
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to null
            - Modified property: offerings
              - Items changed
                - Properties changed
                  - New property: created
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - Modified property: factor
                          - Nullable changed from false to true
                  - Modified property: plan_details
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - Modified property: description
                            - MaxLength changed from 2000 to null

GET /api/proposal-protected-calls/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to null
            - Modified property: offerings
              - Items changed
                - Properties changed
                  - New property: created
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - Modified property: factor
                          - Nullable changed from false to true
                  - Modified property: plan_details
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - Modified property: description
                            - MaxLength changed from 2000 to null

PATCH /api/proposal-protected-calls/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to null
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to null
            - Modified property: offerings
              - Items changed
                - Properties changed
                  - New property: created
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - Modified property: factor
                          - Nullable changed from false to true
                  - Modified property: plan_details
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - Modified property: description
                            - MaxLength changed from 2000 to null

PUT /api/proposal-protected-calls/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to null
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to null
            - Modified property: offerings
              - Items changed
                - Properties changed
                  - New property: created
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - Modified property: factor
                          - Nullable changed from false to true
                  - Modified property: plan_details
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - Modified property: description
                            - MaxLength changed from 2000 to null

GET /api/proposal-protected-calls/{uuid}/offerings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: created
            - Properties changed
              - New property: created
              - Modified property: components
                - Items changed
                  - Properties changed
                    - Modified property: factor
                      - Nullable changed from false to true
              - Modified property: plan_details
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/BasePublicPlan
                    - Properties changed
                      - Modified property: description
                        - MaxLength changed from 2000 to null

POST /api/proposal-protected-calls/{uuid}/offerings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: created
          - Properties changed
            - New property: created
            - Modified property: components
              - Items changed
                - Properties changed
                  - Modified property: factor
                    - Nullable changed from false to true
            - Modified property: plan_details
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BasePublicPlan
                  - Properties changed
                    - Modified property: description
                      - MaxLength changed from 2000 to null

GET /api/proposal-protected-calls/{uuid}/offerings/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: created
          - Properties changed
            - New property: created
            - Modified property: components
              - Items changed
                - Properties changed
                  - Modified property: factor
                    - Nullable changed from false to true
            - Modified property: plan_details
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BasePublicPlan
                  - Properties changed
                    - Modified property: description
                      - MaxLength changed from 2000 to null

PATCH /api/proposal-protected-calls/{uuid}/offerings/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: created
          - Properties changed
            - New property: created
            - Modified property: components
              - Items changed
                - Properties changed
                  - Modified property: factor
                    - Nullable changed from false to true
            - Modified property: plan_details
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BasePublicPlan
                  - Properties changed
                    - Modified property: description
                      - MaxLength changed from 2000 to null

PUT /api/proposal-protected-calls/{uuid}/offerings/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: created
          - Properties changed
            - New property: created
            - Modified property: components
              - Items changed
                - Properties changed
                  - Modified property: factor
                    - Nullable changed from false to true
            - Modified property: plan_details
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BasePublicPlan
                  - Properties changed
                    - Modified property: description
                      - MaxLength changed from 2000 to null

POST /api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/close/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to null
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to null
            - Modified property: offerings
              - Items changed
                - Properties changed
                  - New property: created
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - Modified property: factor
                          - Nullable changed from false to true
                  - Modified property: plan_details
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - Modified property: description
                            - MaxLength changed from 2000 to null

GET /api/proposal-public-calls/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to null
              - Modified property: offerings
                - Items changed
                  - Properties changed
                    - New property: created
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - Modified property: factor
                            - Nullable changed from false to true
                    - Modified property: plan_details
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BasePublicPlan
                          - Properties changed
                            - Modified property: description
                              - MaxLength changed from 2000 to null

GET /api/proposal-public-calls/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to null
            - Modified property: offerings
              - Items changed
                - Properties changed
                  - New property: created
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - Modified property: factor
                          - Nullable changed from false to true
                  - Modified property: plan_details
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - Modified property: description
                            - MaxLength changed from 2000 to null

GET /api/proposal-requested-offerings/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: created
            - Properties changed
              - New property: created
              - Modified property: components
                - Items changed
                  - Properties changed
                    - Modified property: factor
                      - Nullable changed from false to true
              - Modified property: plan_details
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/BasePublicPlan
                    - Properties changed
                      - Modified property: description
                        - MaxLength changed from 2000 to null

GET /api/proposal-requested-offerings/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: created
          - Properties changed
            - New property: created
            - Modified property: components
              - Items changed
                - Properties changed
                  - Modified property: factor
                    - Nullable changed from false to true
            - Modified property: plan_details
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BasePublicPlan
                  - Properties changed
                    - Modified property: description
                      - MaxLength changed from 2000 to null

GET /api/proposal-requested-resources/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'
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
                      - New property: created
                      - Modified property: components
                        - Items changed
                          - Properties changed
                            - Modified property: factor
                              - Nullable changed from false to true
                      - Modified property: plan_details
                        - Property 'AllOf' changed
                          - Modified schema: #/components/schemas/BasePublicPlan
                            - Properties changed
                              - Modified property: description
                                - MaxLength changed from 2000 to null

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
                    - New property: created
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - Modified property: factor
                            - Nullable changed from false to true
                    - Modified property: plan_details
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BasePublicPlan
                          - Properties changed
                            - Modified property: description
                              - MaxLength changed from 2000 to null

GET /api/proposal-reviews/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/provider-invoice-items/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/rancher-apps/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/rancher-catalogs/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/rancher-cluster-security-groups/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/rancher-cluster-templates/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/rancher-clusters/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/rancher-hpas/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/rancher-ingresses/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/rancher-namespaces/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/rancher-nodes/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/rancher-projects/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/rancher-role-templates/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/rancher-services/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/rancher-templates/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/rancher-users/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/rancher-workloads/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/roles/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/service-settings/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'
- Modified query param: scope_uuid
  - Schema changed
    - Format changed from 'uuid' to ''

GET /api/slurm-allocation-user-usage/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/slurm-allocations/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/slurm-associations/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/slurm-jobs/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/support-attachments/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/support-comments/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/support-feedbacks/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/support-issues/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/support-priorities/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/support-templates/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/support-users/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/user-agreements/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: content

POST /api/user-agreements/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Required changed
          - New required property: content
        - Properties changed
          - Modified property: content
            - MinLength changed from 0 to 1
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: content

GET /api/user-agreements/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: content

PATCH /api/user-agreements/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: content
            - MinLength changed from 0 to 1
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: content

PUT /api/user-agreements/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Required changed
          - New required property: content
        - Properties changed
          - Modified property: content
            - MinLength changed from 0 to 1
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: content

GET /api/user-group-invitations/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/user-invitations/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: extra_invitation_text
                - MaxLength changed from null to 250

POST /api/user-invitations/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: extra_invitation_text
            - MaxLength changed from null to 250
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: extra_invitation_text
              - MaxLength changed from null to 250

GET /api/user-invitations/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: extra_invitation_text
              - MaxLength changed from null to 250

GET /api/user-permission-requests/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/user-permissions/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'
- Modified query param: scope_uuid
  - Schema changed
    - Format changed from 'uuid' to ''

GET /api/users/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/vmware-clusters/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/vmware-datastores/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/vmware-disks/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/vmware-folders/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/vmware-networks/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/vmware-ports/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/vmware-templates/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/vmware-virtual-machine/

- Description changed from '' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

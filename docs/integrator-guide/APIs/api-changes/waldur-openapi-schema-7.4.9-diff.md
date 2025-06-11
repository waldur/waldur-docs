# OpenAPI schema diff - 7.4.9

## For version 7.4.9

### New Endpoints: 12

---------------------
GET /api/keycloak-groups/  
GET /api/keycloak-groups/{uuid}/  
GET /api/keycloak-user-group-memberships/  
POST /api/keycloak-user-group-memberships/  
DELETE /api/keycloak-user-group-memberships/{uuid}/  
GET /api/keycloak-user-group-memberships/{uuid}/  
PATCH /api/keycloak-user-group-memberships/{uuid}/  
PUT /api/keycloak-user-group-memberships/{uuid}/  
POST /api/openstack-networks/{uuid}/rbac_policy_create/  
DELETE /api/openstack-networks/{uuid}/rbac_policy_delete/{rbac_policy_uuid}/  
GET /api/rancher-role-templates/  
GET /api/rancher-role-templates/{uuid}/  

### Deleted Endpoints: 10

---------------------
GET /api/icons/favicon/  
GET /api/icons/hero_image/  
GET /api/icons/keycloak_icon/  
GET /api/icons/login_logo/  
GET /api/icons/offering_logo_placeholder/  
GET /api/icons/powered_by_logo/  
GET /api/icons/sidebar_logo/  
GET /api/icons/sidebar_logo_dark/  
GET /api/icons/sidebar_logo_mobile/  
GET /api/icons/site_logo/  

### Modified Endpoints: 141

---------------------
GET /api/aws-instances/

- New query param: can_manage

GET /api/azure-public-ips/

- New query param: can_manage

GET /api/azure-sql-databases/

- New query param: can_manage

GET /api/azure-sql-servers/

- New query param: can_manage

GET /api/azure-virtualmachines/

- New query param: can_manage

GET /api/booking-offerings/

- Modified query param: field
  - Schema changed
    - Items changed
      - Deleted enum values: [state_code]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Deleted property: state_code
              - Modified property: plugin_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedPluginOptions
                    - Properties changed
                      - New property: managed_rancher_server_flavor_name
                      - New property: managed_rancher_server_system_volume_size_gb
                      - New property: managed_rancher_server_system_volume_type_name
                      - Modified property: openstack_offering_uuid_list
                        - Items changed
                          - Format changed from 'uuid' to ''

GET /api/booking-offerings/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - Deleted enum values: [state_code]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: state_code
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: managed_rancher_server_flavor_name
                    - New property: managed_rancher_server_system_volume_size_gb
                    - New property: managed_rancher_server_system_volume_type_name
                    - Modified property: openstack_offering_uuid_list
                      - Items changed
                        - Format changed from 'uuid' to ''

GET /api/booking-resources/

- New query param: offering_shared
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
                      - Modified property: consumer_reviewed_by
                        - Nullable changed from false to true
                      - Modified property: consumer_reviewed_by_full_name
                        - Nullable changed from false to true
                      - Modified property: consumer_reviewed_by_username
                        - Nullable changed from false to true
                      - Modified property: new_plan_name
                        - Nullable changed from false to true
                      - Modified property: new_plan_uuid
                        - Nullable changed from false to true
                      - Modified property: old_plan_name
                        - Nullable changed from false to true
                      - Modified property: old_plan_uuid
                        - Nullable changed from false to true
                      - Modified property: provider_reviewed_by
                        - Nullable changed from false to true
                      - Modified property: provider_reviewed_by_full_name
                        - Nullable changed from false to true
                      - Modified property: provider_reviewed_by_username
                        - Nullable changed from false to true
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - Modified property: consumer_reviewed_by
                        - Nullable changed from false to true
                      - Modified property: consumer_reviewed_by_full_name
                        - Nullable changed from false to true
                      - Modified property: consumer_reviewed_by_username
                        - Nullable changed from false to true
                      - Modified property: new_plan_name
                        - Nullable changed from false to true
                      - Modified property: new_plan_uuid
                        - Nullable changed from false to true
                      - Modified property: old_plan_name
                        - Nullable changed from false to true
                      - Modified property: old_plan_uuid
                        - Nullable changed from false to true
                      - Modified property: provider_reviewed_by
                        - Nullable changed from false to true
                      - Modified property: provider_reviewed_by_full_name
                        - Nullable changed from false to true
                      - Modified property: provider_reviewed_by_username
                        - Nullable changed from false to true

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
                    - Modified property: consumer_reviewed_by
                      - Nullable changed from false to true
                    - Modified property: consumer_reviewed_by_full_name
                      - Nullable changed from false to true
                    - Modified property: consumer_reviewed_by_username
                      - Nullable changed from false to true
                    - Modified property: new_plan_name
                      - Nullable changed from false to true
                    - Modified property: new_plan_uuid
                      - Nullable changed from false to true
                    - Modified property: old_plan_name
                      - Nullable changed from false to true
                    - Modified property: old_plan_uuid
                      - Nullable changed from false to true
                    - Modified property: provider_reviewed_by
                      - Nullable changed from false to true
                    - Modified property: provider_reviewed_by_full_name
                      - Nullable changed from false to true
                    - Modified property: provider_reviewed_by_username
                      - Nullable changed from false to true
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: consumer_reviewed_by
                      - Nullable changed from false to true
                    - Modified property: consumer_reviewed_by_full_name
                      - Nullable changed from false to true
                    - Modified property: consumer_reviewed_by_username
                      - Nullable changed from false to true
                    - Modified property: new_plan_name
                      - Nullable changed from false to true
                    - Modified property: new_plan_uuid
                      - Nullable changed from false to true
                    - Modified property: old_plan_name
                      - Nullable changed from false to true
                    - Modified property: old_plan_uuid
                      - Nullable changed from false to true
                    - Modified property: provider_reviewed_by
                      - Nullable changed from false to true
                    - Modified property: provider_reviewed_by_full_name
                      - Nullable changed from false to true
                    - Modified property: provider_reviewed_by_username
                      - Nullable changed from false to true

POST /api/call-managing-organisations/{uuid}/add_user/

- Responses changed
  - New response: 201
  - Deleted response: 200

POST /api/call-managing-organisations/{uuid}/update_user/

- Responses changed
  - Modified response: 200
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

GET /api/customers/

- New query param: owned_by_current_user

GET /api/customers/countries/

- New query param: owned_by_current_user

POST /api/customers/{uuid}/add_user/

- Responses changed
  - New response: 201
  - Deleted response: 200

POST /api/customers/{uuid}/update_user/

- Responses changed
  - Modified response: 200
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

GET /api/digitalocean-droplets/

- New query param: can_manage

GET /api/financial-reports/

- New query param: owned_by_current_user

GET /api/marketplace-orders/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: consumer_reviewed_by
                - Nullable changed from false to true
              - Modified property: consumer_reviewed_by_full_name
                - Nullable changed from false to true
              - Modified property: consumer_reviewed_by_username
                - Nullable changed from false to true
              - Modified property: new_plan_name
                - Nullable changed from false to true
              - Modified property: new_plan_uuid
                - Nullable changed from false to true
              - Modified property: old_plan_name
                - Nullable changed from false to true
              - Modified property: old_plan_uuid
                - Nullable changed from false to true
              - Modified property: provider_reviewed_by
                - Nullable changed from false to true
              - Modified property: provider_reviewed_by_full_name
                - Nullable changed from false to true
              - Modified property: provider_reviewed_by_username
                - Nullable changed from false to true

POST /api/marketplace-orders/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: consumer_reviewed_by_full_name
              - Nullable changed from false to true
            - Modified property: consumer_reviewed_by_username
              - Nullable changed from false to true

GET /api/marketplace-orders/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: consumer_reviewed_by
              - Nullable changed from false to true
            - Modified property: consumer_reviewed_by_full_name
              - Nullable changed from false to true
            - Modified property: consumer_reviewed_by_username
              - Nullable changed from false to true
            - Modified property: new_plan_name
              - Nullable changed from false to true
            - Modified property: new_plan_uuid
              - Nullable changed from false to true
            - Modified property: old_plan_name
              - Nullable changed from false to true
            - Modified property: old_plan_uuid
              - Nullable changed from false to true
            - Modified property: provider_reviewed_by
              - Nullable changed from false to true
            - Modified property: provider_reviewed_by_full_name
              - Nullable changed from false to true
            - Modified property: provider_reviewed_by_username
              - Nullable changed from false to true

GET /api/marketplace-orders/{uuid}/offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: state_code
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: managed_rancher_server_flavor_name
                    - New property: managed_rancher_server_system_volume_size_gb
                    - New property: managed_rancher_server_system_volume_type_name
                    - Modified property: openstack_offering_uuid_list
                      - Items changed
                        - Format changed from 'uuid' to ''

GET /api/marketplace-provider-offerings/

- Modified query param: field
  - Schema changed
    - Items changed
      - Deleted enum values: [state_code]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Deleted property: state_code
              - Modified property: plugin_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedPluginOptions
                    - Properties changed
                      - New property: managed_rancher_server_flavor_name
                      - New property: managed_rancher_server_system_volume_size_gb
                      - New property: managed_rancher_server_system_volume_type_name
                      - Modified property: openstack_offering_uuid_list
                        - Items changed
                          - Format changed from 'uuid' to ''
              - Modified property: secret_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedSecretOptions
                    - Properties changed
                      - New property: backend_url
                      - New property: cloud_init_template
                      - New property: password
                      - New property: username
                      - Deleted property: rancher_offering_uuid
                      - Modified property: customer_uuid
                        - Format changed from 'uuid' to ''

POST /api/marketplace-provider-offerings/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: state_code
          - Properties changed
            - Deleted property: state_code
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: managed_rancher_server_flavor_name
                    - New property: managed_rancher_server_system_volume_size_gb
                    - New property: managed_rancher_server_system_volume_type_name
                    - Modified property: openstack_offering_uuid_list
                      - Items changed
                        - Format changed from 'uuid' to ''
            - Modified property: secret_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedSecretOptions
                  - Properties changed
                    - New property: backend_url
                    - New property: cloud_init_template
                    - New property: password
                    - New property: username
                    - Deleted property: rancher_offering_uuid
                    - Modified property: customer_uuid
                      - Format changed from 'uuid' to ''

GET /api/marketplace-provider-offerings/groups/

- Modified query param: field
  - Schema changed
    - Items changed
      - Deleted enum values: [state_code]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: state_code
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: managed_rancher_server_flavor_name
                    - New property: managed_rancher_server_system_volume_size_gb
                    - New property: managed_rancher_server_system_volume_type_name
                    - Modified property: openstack_offering_uuid_list
                      - Items changed
                        - Format changed from 'uuid' to ''
            - Modified property: secret_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedSecretOptions
                  - Properties changed
                    - New property: backend_url
                    - New property: cloud_init_template
                    - New property: password
                    - New property: username
                    - Deleted property: rancher_offering_uuid
                    - Modified property: customer_uuid
                      - Format changed from 'uuid' to ''

GET /api/marketplace-provider-offerings/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - Deleted enum values: [state_code]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: state_code
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: managed_rancher_server_flavor_name
                    - New property: managed_rancher_server_system_volume_size_gb
                    - New property: managed_rancher_server_system_volume_type_name
                    - Modified property: openstack_offering_uuid_list
                      - Items changed
                        - Format changed from 'uuid' to ''
            - Modified property: secret_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedSecretOptions
                  - Properties changed
                    - New property: backend_url
                    - New property: cloud_init_template
                    - New property: password
                    - New property: username
                    - Deleted property: rancher_offering_uuid
                    - Modified property: customer_uuid
                      - Format changed from 'uuid' to ''

POST /api/marketplace-provider-offerings/{uuid}/add_endpoint/

- Responses changed
  - New response: 201
  - Deleted response: 200

POST /api/marketplace-provider-offerings/{uuid}/add_user/

- Responses changed
  - New response: 201
  - Deleted response: 200

POST /api/marketplace-provider-offerings/{uuid}/delete_thumbnail/

- Responses changed
  - New response: 204
  - Deleted response: 200

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
                    - Modified property: consumer_reviewed_by
                      - Nullable changed from false to true
                    - Modified property: consumer_reviewed_by_full_name
                      - Nullable changed from false to true
                    - Modified property: consumer_reviewed_by_username
                      - Nullable changed from false to true
                    - Modified property: new_plan_name
                      - Nullable changed from false to true
                    - Modified property: new_plan_uuid
                      - Nullable changed from false to true
                    - Modified property: old_plan_name
                      - Nullable changed from false to true
                    - Modified property: old_plan_uuid
                      - Nullable changed from false to true
                    - Modified property: provider_reviewed_by
                      - Nullable changed from false to true
                    - Modified property: provider_reviewed_by_full_name
                      - Nullable changed from false to true
                    - Modified property: provider_reviewed_by_username
                      - Nullable changed from false to true
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: consumer_reviewed_by
                      - Nullable changed from false to true
                    - Modified property: consumer_reviewed_by_full_name
                      - Nullable changed from false to true
                    - Modified property: consumer_reviewed_by_username
                      - Nullable changed from false to true
                    - Modified property: new_plan_name
                      - Nullable changed from false to true
                    - Modified property: new_plan_uuid
                      - Nullable changed from false to true
                    - Modified property: old_plan_name
                      - Nullable changed from false to true
                    - Modified property: old_plan_uuid
                      - Nullable changed from false to true
                    - Modified property: provider_reviewed_by
                      - Nullable changed from false to true
                    - Modified property: provider_reviewed_by_full_name
                      - Nullable changed from false to true
                    - Modified property: provider_reviewed_by_username
                      - Nullable changed from false to true

GET /api/marketplace-provider-offerings/{uuid}/orders/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: consumer_reviewed_by
                - Nullable changed from false to true
              - Modified property: consumer_reviewed_by_full_name
                - Nullable changed from false to true
              - Modified property: consumer_reviewed_by_username
                - Nullable changed from false to true
              - Modified property: new_plan_name
                - Nullable changed from false to true
              - Modified property: new_plan_uuid
                - Nullable changed from false to true
              - Modified property: old_plan_name
                - Nullable changed from false to true
              - Modified property: old_plan_uuid
                - Nullable changed from false to true
              - Modified property: provider_reviewed_by
                - Nullable changed from false to true
              - Modified property: provider_reviewed_by_full_name
                - Nullable changed from false to true
              - Modified property: provider_reviewed_by_username
                - Nullable changed from false to true

GET /api/marketplace-provider-offerings/{uuid}/orders/{order_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: consumer_reviewed_by
              - Nullable changed from false to true
            - Modified property: consumer_reviewed_by_full_name
              - Nullable changed from false to true
            - Modified property: consumer_reviewed_by_username
              - Nullable changed from false to true
            - Modified property: new_plan_name
              - Nullable changed from false to true
            - Modified property: new_plan_uuid
              - Nullable changed from false to true
            - Modified property: old_plan_name
              - Nullable changed from false to true
            - Modified property: old_plan_uuid
              - Nullable changed from false to true
            - Modified property: provider_reviewed_by
              - Nullable changed from false to true
            - Modified property: provider_reviewed_by_full_name
              - Nullable changed from false to true
            - Modified property: provider_reviewed_by_username
              - Nullable changed from false to true

POST /api/marketplace-provider-offerings/{uuid}/refresh_offering_usernames/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: state_code
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: managed_rancher_server_flavor_name
                    - New property: managed_rancher_server_system_volume_size_gb
                    - New property: managed_rancher_server_system_volume_type_name
                    - Modified property: openstack_offering_uuid_list
                      - Items changed
                        - Format changed from 'uuid' to ''
            - Modified property: secret_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedSecretOptions
                  - Properties changed
                    - New property: backend_url
                    - New property: cloud_init_template
                    - New property: password
                    - New property: username
                    - Deleted property: rancher_offering_uuid
                    - Modified property: customer_uuid
                      - Format changed from 'uuid' to ''

GET /api/marketplace-provider-offerings/{uuid}/stats/

- Modified query param: field
  - Schema changed
    - Items changed
      - Deleted enum values: [state_code]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: state_code
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: managed_rancher_server_flavor_name
                    - New property: managed_rancher_server_system_volume_size_gb
                    - New property: managed_rancher_server_system_volume_type_name
                    - Modified property: openstack_offering_uuid_list
                      - Items changed
                        - Format changed from 'uuid' to ''
            - Modified property: secret_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedSecretOptions
                  - Properties changed
                    - New property: backend_url
                    - New property: cloud_init_template
                    - New property: password
                    - New property: username
                    - Deleted property: rancher_offering_uuid
                    - Modified property: customer_uuid
                      - Format changed from 'uuid' to ''

POST /api/marketplace-provider-offerings/{uuid}/update_description/

- Responses changed
  - Modified response: 200
    - Description changed from '' to 'No response body'
    - Content changed
      - Deleted media type: application/json

POST /api/marketplace-provider-offerings/{uuid}/update_image/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: state_code
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: managed_rancher_server_flavor_name
                    - New property: managed_rancher_server_system_volume_size_gb
                    - New property: managed_rancher_server_system_volume_type_name
                    - Modified property: openstack_offering_uuid_list
                      - Items changed
                        - Format changed from 'uuid' to ''
            - Modified property: secret_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedSecretOptions
                  - Properties changed
                    - New property: backend_url
                    - New property: cloud_init_template
                    - New property: password
                    - New property: username
                    - Deleted property: rancher_offering_uuid
                    - Modified property: customer_uuid
                      - Format changed from 'uuid' to ''

POST /api/marketplace-provider-offerings/{uuid}/update_integration/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: plugin_options
            - Properties changed
              - New property: managed_rancher_server_flavor_name
              - New property: managed_rancher_server_system_volume_size_gb
              - New property: managed_rancher_server_system_volume_type_name
              - Modified property: openstack_offering_uuid_list
                - Items changed
                  - Format changed from 'uuid' to ''
                  - MinLength changed from 0 to 1
          - Modified property: secret_options
            - Properties changed
              - New property: backend_url
              - New property: cloud_init_template
              - New property: password
              - New property: username
              - Deleted property: rancher_offering_uuid
              - Modified property: customer_uuid
                - Format changed from 'uuid' to ''
                - MinLength changed from 0 to 1
- Responses changed
  - Modified response: 200
    - Description changed from '' to 'No response body'
    - Content changed
      - Deleted media type: application/json

POST /api/marketplace-provider-offerings/{uuid}/update_location/

- Responses changed
  - Modified response: 200
    - Description changed from '' to 'No response body'
    - Content changed
      - Deleted media type: application/json

POST /api/marketplace-provider-offerings/{uuid}/update_options/

- Responses changed
  - Modified response: 200
    - Description changed from '' to 'No response body'
    - Content changed
      - Deleted media type: application/json

POST /api/marketplace-provider-offerings/{uuid}/update_organization_groups/

- Responses changed
  - Modified response: 200
    - Description changed from '' to 'No response body'
    - Content changed
      - Deleted media type: application/json

POST /api/marketplace-provider-offerings/{uuid}/update_overview/

- Responses changed
  - Modified response: 200
    - Description changed from '' to 'No response body'
    - Content changed
      - Deleted media type: application/json

POST /api/marketplace-provider-offerings/{uuid}/update_resource_options/

- Responses changed
  - Modified response: 200
    - Description changed from '' to 'No response body'
    - Content changed
      - Deleted media type: application/json

POST /api/marketplace-provider-offerings/{uuid}/update_thumbnail/

- Responses changed
  - Modified response: 200
    - Description changed from '' to 'No response body'
    - Content changed
      - Deleted media type: application/json

POST /api/marketplace-provider-offerings/{uuid}/update_user/

- Responses changed
  - Modified response: 200
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

GET /api/marketplace-provider-offerings/{uuid}/user_has_resource_access/

- Modified query param: field
  - Schema changed
    - Items changed
      - Deleted enum values: [state_code]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: state_code
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: managed_rancher_server_flavor_name
                    - New property: managed_rancher_server_system_volume_size_gb
                    - New property: managed_rancher_server_system_volume_type_name
                    - Modified property: openstack_offering_uuid_list
                      - Items changed
                        - Format changed from 'uuid' to ''
            - Modified property: secret_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedSecretOptions
                  - Properties changed
                    - New property: backend_url
                    - New property: cloud_init_template
                    - New property: password
                    - New property: username
                    - Deleted property: rancher_offering_uuid
                    - Modified property: customer_uuid
                      - Format changed from 'uuid' to ''

GET /api/marketplace-provider-resources/

- New query param: offering_shared
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
                      - Modified property: consumer_reviewed_by
                        - Nullable changed from false to true
                      - Modified property: consumer_reviewed_by_full_name
                        - Nullable changed from false to true
                      - Modified property: consumer_reviewed_by_username
                        - Nullable changed from false to true
                      - Modified property: new_plan_name
                        - Nullable changed from false to true
                      - Modified property: new_plan_uuid
                        - Nullable changed from false to true
                      - Modified property: old_plan_name
                        - Nullable changed from false to true
                      - Modified property: old_plan_uuid
                        - Nullable changed from false to true
                      - Modified property: provider_reviewed_by
                        - Nullable changed from false to true
                      - Modified property: provider_reviewed_by_full_name
                        - Nullable changed from false to true
                      - Modified property: provider_reviewed_by_username
                        - Nullable changed from false to true
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - Modified property: consumer_reviewed_by
                        - Nullable changed from false to true
                      - Modified property: consumer_reviewed_by_full_name
                        - Nullable changed from false to true
                      - Modified property: consumer_reviewed_by_username
                        - Nullable changed from false to true
                      - Modified property: new_plan_name
                        - Nullable changed from false to true
                      - Modified property: new_plan_uuid
                        - Nullable changed from false to true
                      - Modified property: old_plan_name
                        - Nullable changed from false to true
                      - Modified property: old_plan_uuid
                        - Nullable changed from false to true
                      - Modified property: provider_reviewed_by
                        - Nullable changed from false to true
                      - Modified property: provider_reviewed_by_full_name
                        - Nullable changed from false to true
                      - Modified property: provider_reviewed_by_username
                        - Nullable changed from false to true

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
                    - Modified property: consumer_reviewed_by
                      - Nullable changed from false to true
                    - Modified property: consumer_reviewed_by_full_name
                      - Nullable changed from false to true
                    - Modified property: consumer_reviewed_by_username
                      - Nullable changed from false to true
                    - Modified property: new_plan_name
                      - Nullable changed from false to true
                    - Modified property: new_plan_uuid
                      - Nullable changed from false to true
                    - Modified property: old_plan_name
                      - Nullable changed from false to true
                    - Modified property: old_plan_uuid
                      - Nullable changed from false to true
                    - Modified property: provider_reviewed_by
                      - Nullable changed from false to true
                    - Modified property: provider_reviewed_by_full_name
                      - Nullable changed from false to true
                    - Modified property: provider_reviewed_by_username
                      - Nullable changed from false to true
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: consumer_reviewed_by
                      - Nullable changed from false to true
                    - Modified property: consumer_reviewed_by_full_name
                      - Nullable changed from false to true
                    - Modified property: consumer_reviewed_by_username
                      - Nullable changed from false to true
                    - Modified property: new_plan_name
                      - Nullable changed from false to true
                    - Modified property: new_plan_uuid
                      - Nullable changed from false to true
                    - Modified property: old_plan_name
                      - Nullable changed from false to true
                    - Modified property: old_plan_uuid
                      - Nullable changed from false to true
                    - Modified property: provider_reviewed_by
                      - Nullable changed from false to true
                    - Modified property: provider_reviewed_by_full_name
                      - Nullable changed from false to true
                    - Modified property: provider_reviewed_by_username
                      - Nullable changed from false to true

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
                    - Modified property: consumer_reviewed_by
                      - Nullable changed from false to true
                    - Modified property: consumer_reviewed_by_full_name
                      - Nullable changed from false to true
                    - Modified property: consumer_reviewed_by_username
                      - Nullable changed from false to true
                    - Modified property: new_plan_name
                      - Nullable changed from false to true
                    - Modified property: new_plan_uuid
                      - Nullable changed from false to true
                    - Modified property: old_plan_name
                      - Nullable changed from false to true
                    - Modified property: old_plan_uuid
                      - Nullable changed from false to true
                    - Modified property: provider_reviewed_by
                      - Nullable changed from false to true
                    - Modified property: provider_reviewed_by_full_name
                      - Nullable changed from false to true
                    - Modified property: provider_reviewed_by_username
                      - Nullable changed from false to true
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: consumer_reviewed_by
                      - Nullable changed from false to true
                    - Modified property: consumer_reviewed_by_full_name
                      - Nullable changed from false to true
                    - Modified property: consumer_reviewed_by_username
                      - Nullable changed from false to true
                    - Modified property: new_plan_name
                      - Nullable changed from false to true
                    - Modified property: new_plan_uuid
                      - Nullable changed from false to true
                    - Modified property: old_plan_name
                      - Nullable changed from false to true
                    - Modified property: old_plan_uuid
                      - Nullable changed from false to true
                    - Modified property: provider_reviewed_by
                      - Nullable changed from false to true
                    - Modified property: provider_reviewed_by_full_name
                      - Nullable changed from false to true
                    - Modified property: provider_reviewed_by_username
                      - Nullable changed from false to true

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
                    - Modified property: consumer_reviewed_by
                      - Nullable changed from false to true
                    - Modified property: consumer_reviewed_by_full_name
                      - Nullable changed from false to true
                    - Modified property: consumer_reviewed_by_username
                      - Nullable changed from false to true
                    - Modified property: new_plan_name
                      - Nullable changed from false to true
                    - Modified property: new_plan_uuid
                      - Nullable changed from false to true
                    - Modified property: old_plan_name
                      - Nullable changed from false to true
                    - Modified property: old_plan_uuid
                      - Nullable changed from false to true
                    - Modified property: provider_reviewed_by
                      - Nullable changed from false to true
                    - Modified property: provider_reviewed_by_full_name
                      - Nullable changed from false to true
                    - Modified property: provider_reviewed_by_username
                      - Nullable changed from false to true
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: consumer_reviewed_by
                      - Nullable changed from false to true
                    - Modified property: consumer_reviewed_by_full_name
                      - Nullable changed from false to true
                    - Modified property: consumer_reviewed_by_username
                      - Nullable changed from false to true
                    - Modified property: new_plan_name
                      - Nullable changed from false to true
                    - Modified property: new_plan_uuid
                      - Nullable changed from false to true
                    - Modified property: old_plan_name
                      - Nullable changed from false to true
                    - Modified property: old_plan_uuid
                      - Nullable changed from false to true
                    - Modified property: provider_reviewed_by
                      - Nullable changed from false to true
                    - Modified property: provider_reviewed_by_full_name
                      - Nullable changed from false to true
                    - Modified property: provider_reviewed_by_username
                      - Nullable changed from false to true

GET /api/marketplace-provider-resources/{uuid}/offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: state_code
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: managed_rancher_server_flavor_name
                    - New property: managed_rancher_server_system_volume_size_gb
                    - New property: managed_rancher_server_system_volume_type_name
                    - Modified property: openstack_offering_uuid_list
                      - Items changed
                        - Format changed from 'uuid' to ''

POST /api/marketplace-provider-resources/{uuid}/refresh_last_sync/

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
                    - Modified property: consumer_reviewed_by
                      - Nullable changed from false to true
                    - Modified property: consumer_reviewed_by_full_name
                      - Nullable changed from false to true
                    - Modified property: consumer_reviewed_by_username
                      - Nullable changed from false to true
                    - Modified property: new_plan_name
                      - Nullable changed from false to true
                    - Modified property: new_plan_uuid
                      - Nullable changed from false to true
                    - Modified property: old_plan_name
                      - Nullable changed from false to true
                    - Modified property: old_plan_uuid
                      - Nullable changed from false to true
                    - Modified property: provider_reviewed_by
                      - Nullable changed from false to true
                    - Modified property: provider_reviewed_by_full_name
                      - Nullable changed from false to true
                    - Modified property: provider_reviewed_by_username
                      - Nullable changed from false to true
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: consumer_reviewed_by
                      - Nullable changed from false to true
                    - Modified property: consumer_reviewed_by_full_name
                      - Nullable changed from false to true
                    - Modified property: consumer_reviewed_by_username
                      - Nullable changed from false to true
                    - Modified property: new_plan_name
                      - Nullable changed from false to true
                    - Modified property: new_plan_uuid
                      - Nullable changed from false to true
                    - Modified property: old_plan_name
                      - Nullable changed from false to true
                    - Modified property: old_plan_uuid
                      - Nullable changed from false to true
                    - Modified property: provider_reviewed_by
                      - Nullable changed from false to true
                    - Modified property: provider_reviewed_by_full_name
                      - Nullable changed from false to true
                    - Modified property: provider_reviewed_by_username
                      - Nullable changed from false to true

POST /api/marketplace-provider-resources/{uuid}/set_as_ok/

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
                    - Modified property: consumer_reviewed_by
                      - Nullable changed from false to true
                    - Modified property: consumer_reviewed_by_full_name
                      - Nullable changed from false to true
                    - Modified property: consumer_reviewed_by_username
                      - Nullable changed from false to true
                    - Modified property: new_plan_name
                      - Nullable changed from false to true
                    - Modified property: new_plan_uuid
                      - Nullable changed from false to true
                    - Modified property: old_plan_name
                      - Nullable changed from false to true
                    - Modified property: old_plan_uuid
                      - Nullable changed from false to true
                    - Modified property: provider_reviewed_by
                      - Nullable changed from false to true
                    - Modified property: provider_reviewed_by_full_name
                      - Nullable changed from false to true
                    - Modified property: provider_reviewed_by_username
                      - Nullable changed from false to true
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: consumer_reviewed_by
                      - Nullable changed from false to true
                    - Modified property: consumer_reviewed_by_full_name
                      - Nullable changed from false to true
                    - Modified property: consumer_reviewed_by_username
                      - Nullable changed from false to true
                    - Modified property: new_plan_name
                      - Nullable changed from false to true
                    - Modified property: new_plan_uuid
                      - Nullable changed from false to true
                    - Modified property: old_plan_name
                      - Nullable changed from false to true
                    - Modified property: old_plan_uuid
                      - Nullable changed from false to true
                    - Modified property: provider_reviewed_by
                      - Nullable changed from false to true
                    - Modified property: provider_reviewed_by_full_name
                      - Nullable changed from false to true
                    - Modified property: provider_reviewed_by_username
                      - Nullable changed from false to true

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
                    - Modified property: consumer_reviewed_by
                      - Nullable changed from false to true
                    - Modified property: consumer_reviewed_by_full_name
                      - Nullable changed from false to true
                    - Modified property: consumer_reviewed_by_username
                      - Nullable changed from false to true
                    - Modified property: new_plan_name
                      - Nullable changed from false to true
                    - Modified property: new_plan_uuid
                      - Nullable changed from false to true
                    - Modified property: old_plan_name
                      - Nullable changed from false to true
                    - Modified property: old_plan_uuid
                      - Nullable changed from false to true
                    - Modified property: provider_reviewed_by
                      - Nullable changed from false to true
                    - Modified property: provider_reviewed_by_full_name
                      - Nullable changed from false to true
                    - Modified property: provider_reviewed_by_username
                      - Nullable changed from false to true
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: consumer_reviewed_by
                      - Nullable changed from false to true
                    - Modified property: consumer_reviewed_by_full_name
                      - Nullable changed from false to true
                    - Modified property: consumer_reviewed_by_username
                      - Nullable changed from false to true
                    - Modified property: new_plan_name
                      - Nullable changed from false to true
                    - Modified property: new_plan_uuid
                      - Nullable changed from false to true
                    - Modified property: old_plan_name
                      - Nullable changed from false to true
                    - Modified property: old_plan_uuid
                      - Nullable changed from false to true
                    - Modified property: provider_reviewed_by
                      - Nullable changed from false to true
                    - Modified property: provider_reviewed_by_full_name
                      - Nullable changed from false to true
                    - Modified property: provider_reviewed_by_username
                      - Nullable changed from false to true

POST /api/marketplace-provider-resources/{uuid}/terminate/

- Description changed from '' to 'Create marketplace order for resource termination.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: order_uuid
          - Properties changed
            - New property: order_uuid
            - Deleted property: attributes

GET /api/marketplace-public-offerings/

- Modified query param: field
  - Schema changed
    - Items changed
      - Deleted enum values: [state_code]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Deleted property: state_code
              - Modified property: plugin_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedPluginOptions
                    - Properties changed
                      - New property: managed_rancher_server_flavor_name
                      - New property: managed_rancher_server_system_volume_size_gb
                      - New property: managed_rancher_server_system_volume_type_name
                      - Modified property: openstack_offering_uuid_list
                        - Items changed
                          - Format changed from 'uuid' to ''

GET /api/marketplace-public-offerings/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - Deleted enum values: [state_code]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: state_code
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: managed_rancher_server_flavor_name
                    - New property: managed_rancher_server_system_volume_size_gb
                    - New property: managed_rancher_server_system_volume_type_name
                    - Modified property: openstack_offering_uuid_list
                      - Items changed
                        - Format changed from 'uuid' to ''

GET /api/marketplace-resources/

- New query param: offering_shared
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
                      - Modified property: consumer_reviewed_by
                        - Nullable changed from false to true
                      - Modified property: consumer_reviewed_by_full_name
                        - Nullable changed from false to true
                      - Modified property: consumer_reviewed_by_username
                        - Nullable changed from false to true
                      - Modified property: new_plan_name
                        - Nullable changed from false to true
                      - Modified property: new_plan_uuid
                        - Nullable changed from false to true
                      - Modified property: old_plan_name
                        - Nullable changed from false to true
                      - Modified property: old_plan_uuid
                        - Nullable changed from false to true
                      - Modified property: provider_reviewed_by
                        - Nullable changed from false to true
                      - Modified property: provider_reviewed_by_full_name
                        - Nullable changed from false to true
                      - Modified property: provider_reviewed_by_username
                        - Nullable changed from false to true
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - Modified property: consumer_reviewed_by
                        - Nullable changed from false to true
                      - Modified property: consumer_reviewed_by_full_name
                        - Nullable changed from false to true
                      - Modified property: consumer_reviewed_by_username
                        - Nullable changed from false to true
                      - Modified property: new_plan_name
                        - Nullable changed from false to true
                      - Modified property: new_plan_uuid
                        - Nullable changed from false to true
                      - Modified property: old_plan_name
                        - Nullable changed from false to true
                      - Modified property: old_plan_uuid
                        - Nullable changed from false to true
                      - Modified property: provider_reviewed_by
                        - Nullable changed from false to true
                      - Modified property: provider_reviewed_by_full_name
                        - Nullable changed from false to true
                      - Modified property: provider_reviewed_by_username
                        - Nullable changed from false to true

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
                    - Modified property: consumer_reviewed_by
                      - Nullable changed from false to true
                    - Modified property: consumer_reviewed_by_full_name
                      - Nullable changed from false to true
                    - Modified property: consumer_reviewed_by_username
                      - Nullable changed from false to true
                    - Modified property: new_plan_name
                      - Nullable changed from false to true
                    - Modified property: new_plan_uuid
                      - Nullable changed from false to true
                    - Modified property: old_plan_name
                      - Nullable changed from false to true
                    - Modified property: old_plan_uuid
                      - Nullable changed from false to true
                    - Modified property: provider_reviewed_by
                      - Nullable changed from false to true
                    - Modified property: provider_reviewed_by_full_name
                      - Nullable changed from false to true
                    - Modified property: provider_reviewed_by_username
                      - Nullable changed from false to true
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: consumer_reviewed_by
                      - Nullable changed from false to true
                    - Modified property: consumer_reviewed_by_full_name
                      - Nullable changed from false to true
                    - Modified property: consumer_reviewed_by_username
                      - Nullable changed from false to true
                    - Modified property: new_plan_name
                      - Nullable changed from false to true
                    - Modified property: new_plan_uuid
                      - Nullable changed from false to true
                    - Modified property: old_plan_name
                      - Nullable changed from false to true
                    - Modified property: old_plan_uuid
                      - Nullable changed from false to true
                    - Modified property: provider_reviewed_by
                      - Nullable changed from false to true
                    - Modified property: provider_reviewed_by_full_name
                      - Nullable changed from false to true
                    - Modified property: provider_reviewed_by_username
                      - Nullable changed from false to true

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
                    - Modified property: consumer_reviewed_by
                      - Nullable changed from false to true
                    - Modified property: consumer_reviewed_by_full_name
                      - Nullable changed from false to true
                    - Modified property: consumer_reviewed_by_username
                      - Nullable changed from false to true
                    - Modified property: new_plan_name
                      - Nullable changed from false to true
                    - Modified property: new_plan_uuid
                      - Nullable changed from false to true
                    - Modified property: old_plan_name
                      - Nullable changed from false to true
                    - Modified property: old_plan_uuid
                      - Nullable changed from false to true
                    - Modified property: provider_reviewed_by
                      - Nullable changed from false to true
                    - Modified property: provider_reviewed_by_full_name
                      - Nullable changed from false to true
                    - Modified property: provider_reviewed_by_username
                      - Nullable changed from false to true
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: consumer_reviewed_by
                      - Nullable changed from false to true
                    - Modified property: consumer_reviewed_by_full_name
                      - Nullable changed from false to true
                    - Modified property: consumer_reviewed_by_username
                      - Nullable changed from false to true
                    - Modified property: new_plan_name
                      - Nullable changed from false to true
                    - Modified property: new_plan_uuid
                      - Nullable changed from false to true
                    - Modified property: old_plan_name
                      - Nullable changed from false to true
                    - Modified property: old_plan_uuid
                      - Nullable changed from false to true
                    - Modified property: provider_reviewed_by
                      - Nullable changed from false to true
                    - Modified property: provider_reviewed_by_full_name
                      - Nullable changed from false to true
                    - Modified property: provider_reviewed_by_username
                      - Nullable changed from false to true

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
                    - Modified property: consumer_reviewed_by
                      - Nullable changed from false to true
                    - Modified property: consumer_reviewed_by_full_name
                      - Nullable changed from false to true
                    - Modified property: consumer_reviewed_by_username
                      - Nullable changed from false to true
                    - Modified property: new_plan_name
                      - Nullable changed from false to true
                    - Modified property: new_plan_uuid
                      - Nullable changed from false to true
                    - Modified property: old_plan_name
                      - Nullable changed from false to true
                    - Modified property: old_plan_uuid
                      - Nullable changed from false to true
                    - Modified property: provider_reviewed_by
                      - Nullable changed from false to true
                    - Modified property: provider_reviewed_by_full_name
                      - Nullable changed from false to true
                    - Modified property: provider_reviewed_by_username
                      - Nullable changed from false to true
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: consumer_reviewed_by
                      - Nullable changed from false to true
                    - Modified property: consumer_reviewed_by_full_name
                      - Nullable changed from false to true
                    - Modified property: consumer_reviewed_by_username
                      - Nullable changed from false to true
                    - Modified property: new_plan_name
                      - Nullable changed from false to true
                    - Modified property: new_plan_uuid
                      - Nullable changed from false to true
                    - Modified property: old_plan_name
                      - Nullable changed from false to true
                    - Modified property: old_plan_uuid
                      - Nullable changed from false to true
                    - Modified property: provider_reviewed_by
                      - Nullable changed from false to true
                    - Modified property: provider_reviewed_by_full_name
                      - Nullable changed from false to true
                    - Modified property: provider_reviewed_by_username
                      - Nullable changed from false to true

GET /api/marketplace-resources/{uuid}/offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: state_code
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: managed_rancher_server_flavor_name
                    - New property: managed_rancher_server_system_volume_size_gb
                    - New property: managed_rancher_server_system_volume_type_name
                    - Modified property: openstack_offering_uuid_list
                      - Items changed
                        - Format changed from 'uuid' to ''

POST /api/marketplace-resources/{uuid}/switch_plan/

- Description changed from '' to 'Create marketplace order for resource plan switch.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: order_uuid
            - Deleted required property: plan
          - Properties changed
            - New property: order_uuid
            - Deleted property: plan

POST /api/marketplace-resources/{uuid}/terminate/

- Description changed from '' to 'Create marketplace order for resource termination.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: order_uuid
          - Properties changed
            - New property: order_uuid
            - Deleted property: attributes

POST /api/marketplace-resources/{uuid}/update_limits/

- Description changed from '' to 'Create marketplace order for resource limits update.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: order_uuid
            - Deleted required property: limits
          - Properties changed
            - New property: order_uuid
            - Deleted property: limits

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
                      - New property: managed_rancher_server_flavor_name
                      - New property: managed_rancher_server_system_volume_size_gb
                      - New property: managed_rancher_server_system_volume_type_name
                      - Modified property: openstack_offering_uuid_list
                        - Items changed
                          - Format changed from 'uuid' to ''
              - Modified property: responsible_user
                - Nullable changed from false to true

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
                    - New property: managed_rancher_server_flavor_name
                    - New property: managed_rancher_server_system_volume_size_gb
                    - New property: managed_rancher_server_system_volume_type_name
                    - Modified property: openstack_offering_uuid_list
                      - Items changed
                        - Format changed from 'uuid' to ''
            - Modified property: responsible_user
              - Nullable changed from false to true

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
                    - New property: managed_rancher_server_flavor_name
                    - New property: managed_rancher_server_system_volume_size_gb
                    - New property: managed_rancher_server_system_volume_type_name
                    - Modified property: openstack_offering_uuid_list
                      - Items changed
                        - Format changed from 'uuid' to ''
            - Modified property: responsible_user
              - Nullable changed from false to true

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
                    - New property: managed_rancher_server_flavor_name
                    - New property: managed_rancher_server_system_volume_size_gb
                    - New property: managed_rancher_server_system_volume_type_name
                    - Modified property: openstack_offering_uuid_list
                      - Items changed
                        - Format changed from 'uuid' to ''
            - Modified property: responsible_user
              - Nullable changed from false to true

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
                    - New property: managed_rancher_server_flavor_name
                    - New property: managed_rancher_server_system_volume_size_gb
                    - New property: managed_rancher_server_system_volume_type_name
                    - Modified property: openstack_offering_uuid_list
                      - Items changed
                        - Format changed from 'uuid' to ''
            - Modified property: responsible_user
              - Nullable changed from false to true

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
                    - New property: managed_rancher_server_flavor_name
                    - New property: managed_rancher_server_system_volume_size_gb
                    - New property: managed_rancher_server_system_volume_type_name
                    - Modified property: openstack_offering_uuid_list
                      - Items changed
                        - Format changed from 'uuid' to ''
            - Modified property: responsible_user
              - Nullable changed from false to true

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
                    - New property: managed_rancher_server_flavor_name
                    - New property: managed_rancher_server_system_volume_size_gb
                    - New property: managed_rancher_server_system_volume_type_name
                    - Modified property: openstack_offering_uuid_list
                      - Items changed
                        - Format changed from 'uuid' to ''
            - Modified property: responsible_user
              - Nullable changed from false to true

POST /api/marketplace-script-dry-run/{uuid}/async_run/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: state_code
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: managed_rancher_server_flavor_name
                    - New property: managed_rancher_server_system_volume_size_gb
                    - New property: managed_rancher_server_system_volume_type_name
                    - Modified property: openstack_offering_uuid_list
                      - Items changed
                        - Format changed from 'uuid' to ''

POST /api/marketplace-script-dry-run/{uuid}/run/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: state_code
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: managed_rancher_server_flavor_name
                    - New property: managed_rancher_server_system_volume_size_gb
                    - New property: managed_rancher_server_system_volume_type_name
                    - Modified property: openstack_offering_uuid_list
                      - Items changed
                        - Format changed from 'uuid' to ''

GET /api/marketplace-service-providers/{service_provider_uuid}/customers/

- New query param: owned_by_current_user

GET /api/marketplace-service-providers/{service_provider_uuid}/offerings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: secret_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedSecretOptions
                    - Properties changed
                      - New property: backend_url
                      - New property: cloud_init_template
                      - New property: password
                      - New property: username
                      - Deleted property: rancher_offering_uuid
                      - Modified property: customer_uuid
                        - Format changed from 'uuid' to ''

GET /api/marketplace-service-providers/{service_provider_uuid}/user_customers/

- New query param: owned_by_current_user

POST /api/marketplace-service-providers/{uuid}/add_user/

- Responses changed
  - New response: 201
  - Deleted response: 200

POST /api/marketplace-service-providers/{uuid}/update_user/

- Responses changed
  - Modified response: 200
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

GET /api/openstack-backups/

- New query param: can_manage
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: instance_ports
                - Items changed
                  - Properties changed
                    - Modified property: fixed_ips
                      - ReadOnly changed from true to false
              - Modified property: restorations
                - Items changed
                  - Properties changed
                    - Modified property: ports
                      - Items changed
                        - Properties changed
                          - Modified property: fixed_ips
                            - ReadOnly changed from true to false

GET /api/openstack-backups/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: instance_ports
              - Items changed
                - Properties changed
                  - Modified property: fixed_ips
                    - ReadOnly changed from true to false
            - Modified property: restorations
              - Items changed
                - Properties changed
                  - Modified property: ports
                    - Items changed
                      - Properties changed
                        - Modified property: fixed_ips
                          - ReadOnly changed from true to false

PATCH /api/openstack-backups/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: instance_ports
              - Items changed
                - Properties changed
                  - Modified property: fixed_ips
                    - ReadOnly changed from true to false
            - Modified property: restorations
              - Items changed
                - Properties changed
                  - Modified property: ports
                    - Items changed
                      - Properties changed
                        - Modified property: fixed_ips
                          - ReadOnly changed from true to false

PUT /api/openstack-backups/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: instance_ports
              - Items changed
                - Properties changed
                  - Modified property: fixed_ips
                    - ReadOnly changed from true to false
            - Modified property: restorations
              - Items changed
                - Properties changed
                  - Modified property: ports
                    - Items changed
                      - Properties changed
                        - Modified property: fixed_ips
                          - ReadOnly changed from true to false

POST /api/openstack-backups/{uuid}/restore/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: ports
            - Items changed
              - Properties changed
                - New property: fixed_ips
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: ports
              - Items changed
                - Properties changed
                  - Modified property: fixed_ips
                    - ReadOnly changed from true to false

GET /api/openstack-floating-ips/

- New query param: can_manage

GET /api/openstack-instances/

- New query param: can_manage
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: ports
                - Items changed
                  - Properties changed
                    - Modified property: fixed_ips
                      - ReadOnly changed from true to false

GET /api/openstack-instances/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: ports
              - Items changed
                - Properties changed
                  - Modified property: fixed_ips
                    - ReadOnly changed from true to false

PATCH /api/openstack-instances/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: ports
              - Items changed
                - Properties changed
                  - Modified property: fixed_ips
                    - ReadOnly changed from true to false

PUT /api/openstack-instances/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: ports
              - Items changed
                - Properties changed
                  - Modified property: fixed_ips
                    - ReadOnly changed from true to false

POST /api/openstack-instances/{uuid}/backup/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: instance_ports
              - Items changed
                - Properties changed
                  - Modified property: fixed_ips
                    - ReadOnly changed from true to false
            - Modified property: restorations
              - Items changed
                - Properties changed
                  - Modified property: ports
                    - Items changed
                      - Properties changed
                        - Modified property: fixed_ips
                          - ReadOnly changed from true to false

GET /api/openstack-instances/{uuid}/ports/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: fixed_ips
                - ReadOnly changed from true to false

POST /api/openstack-instances/{uuid}/update_ports/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: ports
            - Items changed
              - Properties changed
                - New property: fixed_ips

GET /api/openstack-migrations/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: mappings
                - Properties changed
                  - New property: sync_instance_ports

POST /api/openstack-migrations/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: mappings
            - Properties changed
              - New property: sync_instance_ports
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: mappings
              - Properties changed
                - New property: sync_instance_ports

GET /api/openstack-migrations/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: mappings
              - Properties changed
                - New property: sync_instance_ports

PATCH /api/openstack-migrations/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: mappings
            - Properties changed
              - New property: sync_instance_ports
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: mappings
              - Properties changed
                - New property: sync_instance_ports

PUT /api/openstack-migrations/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: mappings
            - Properties changed
              - New property: sync_instance_ports
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: mappings
              - Properties changed
                - New property: sync_instance_ports

GET /api/openstack-networks/

- New query param: can_manage
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [rbac_policies]
- Modified query param: tenant
  - Description changed from '' to 'Tenant URL'
- Modified query param: tenant_uuid
  - Description changed from '' to 'Tenant UUID'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: rbac_policies

GET /api/openstack-networks/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [rbac_policies]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: rbac_policies

PATCH /api/openstack-networks/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: rbac_policies

PUT /api/openstack-networks/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: rbac_policies

GET /api/openstack-security-groups/

- New query param: can_manage

GET /api/openstack-server-groups/

- New query param: can_manage

GET /api/openstack-snapshots/

- New query param: can_manage

GET /api/openstack-subnets/

- New query param: can_manage
- Modified query param: tenant
  - Description changed from '' to 'Tenant URL'
- Modified query param: tenant_uuid
  - Description changed from '' to 'Tenant UUID'

GET /api/openstack-tenants/

- New query param: can_manage

GET /api/openstack-tenants/{uuid}/backend_instances/

- New query param: can_manage

GET /api/openstack-tenants/{uuid}/backend_volumes/

- New query param: can_manage

POST /api/openstack-tenants/{uuid}/create_network/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: rbac_policies

GET /api/openstack-volumes/

- New query param: can_manage

POST /api/projects/{uuid}/add_user/

- Responses changed
  - New response: 201
  - Deleted response: 200

POST /api/projects/{uuid}/move_project/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Required changed
          - New required property: preserve_permissions
        - Properties changed
          - New property: preserve_permissions

POST /api/projects/{uuid}/update_user/

- Responses changed
  - Modified response: 200
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

GET /api/promotions-campaigns/{uuid}/orders/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: consumer_reviewed_by
                - Nullable changed from false to true
              - Modified property: consumer_reviewed_by_full_name
                - Nullable changed from false to true
              - Modified property: consumer_reviewed_by_username
                - Nullable changed from false to true
              - Modified property: new_plan_name
                - Nullable changed from false to true
              - Modified property: new_plan_uuid
                - Nullable changed from false to true
              - Modified property: old_plan_name
                - Nullable changed from false to true
              - Modified property: old_plan_uuid
                - Nullable changed from false to true
              - Modified property: provider_reviewed_by
                - Nullable changed from false to true
              - Modified property: provider_reviewed_by_full_name
                - Nullable changed from false to true
              - Modified property: provider_reviewed_by_username
                - Nullable changed from false to true

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
                      - Modified property: consumer_reviewed_by
                        - Nullable changed from false to true
                      - Modified property: consumer_reviewed_by_full_name
                        - Nullable changed from false to true
                      - Modified property: consumer_reviewed_by_username
                        - Nullable changed from false to true
                      - Modified property: new_plan_name
                        - Nullable changed from false to true
                      - Modified property: new_plan_uuid
                        - Nullable changed from false to true
                      - Modified property: old_plan_name
                        - Nullable changed from false to true
                      - Modified property: old_plan_uuid
                        - Nullable changed from false to true
                      - Modified property: provider_reviewed_by
                        - Nullable changed from false to true
                      - Modified property: provider_reviewed_by_full_name
                        - Nullable changed from false to true
                      - Modified property: provider_reviewed_by_username
                        - Nullable changed from false to true
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - Modified property: consumer_reviewed_by
                        - Nullable changed from false to true
                      - Modified property: consumer_reviewed_by_full_name
                        - Nullable changed from false to true
                      - Modified property: consumer_reviewed_by_username
                        - Nullable changed from false to true
                      - Modified property: new_plan_name
                        - Nullable changed from false to true
                      - Modified property: new_plan_uuid
                        - Nullable changed from false to true
                      - Modified property: old_plan_name
                        - Nullable changed from false to true
                      - Modified property: old_plan_uuid
                        - Nullable changed from false to true
                      - Modified property: provider_reviewed_by
                        - Nullable changed from false to true
                      - Modified property: provider_reviewed_by_full_name
                        - Nullable changed from false to true
                      - Modified property: provider_reviewed_by_username
                        - Nullable changed from false to true

POST /api/proposal-proposals/{uuid}/add_user/

- Responses changed
  - New response: 201
  - Deleted response: 200

POST /api/proposal-proposals/{uuid}/update_user/

- Responses changed
  - Modified response: 200
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

POST /api/proposal-protected-calls/{uuid}/add_user/

- Responses changed
  - New response: 201
  - Deleted response: 200

POST /api/proposal-protected-calls/{uuid}/update_user/

- Responses changed
  - Modified response: 200
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

GET /api/rancher-apps/

- New query param: can_manage

GET /api/rancher-catalogs/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: scope_type
                - Property 'AllOf' changed
                  - Schemas added: #/components/schemas/RancherCatalogScopeType
                  - Schemas deleted: #/components/schemas/ScopeTypeEnum

POST /api/rancher-catalogs/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: scope_type
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/RancherCatalogScopeType
                - Schemas deleted: #/components/schemas/ScopeTypeEnum

GET /api/rancher-catalogs/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: scope_type
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/RancherCatalogScopeType
                - Schemas deleted: #/components/schemas/ScopeTypeEnum

PATCH /api/rancher-catalogs/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: scope_type
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/RancherCatalogScopeType
                - Schemas deleted: #/components/schemas/ScopeTypeEnum

PUT /api/rancher-catalogs/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: scope_type
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/RancherCatalogScopeType
                - Schemas deleted: #/components/schemas/ScopeTypeEnum

POST /api/rancher-catalogs/{uuid}/refresh/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: scope_type
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/RancherCatalogScopeType
                - Schemas deleted: #/components/schemas/ScopeTypeEnum

GET /api/rancher-clusters/

- New query param: can_manage
- Modified query param: field
  - Schema changed
    - Items changed
      - Deleted enum values: [node_command]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Deleted property: node_command

POST /api/rancher-clusters/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: node_command

GET /api/rancher-clusters/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - Deleted enum values: [node_command]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: node_command

PATCH /api/rancher-clusters/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: node_command

PUT /api/rancher-clusters/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: node_command

POST /api/rancher-clusters/{uuid}/create_management_security_group/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: node_command

GET /api/rancher-clusters/{uuid}/kubeconfig_file/

- Modified query param: field
  - Schema changed
    - Items changed
      - Deleted enum values: [node_command]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: node_command

GET /api/rancher-ingresses/

- New query param: can_manage

GET /api/rancher-nodes/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - Deleted required property: get_node_command
            - Properties changed
              - Deleted property: get_node_command

GET /api/rancher-nodes/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: get_node_command
          - Properties changed
            - Deleted property: get_node_command

GET /api/rancher-services/

- New query param: can_manage

GET /api/rancher-users/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: cluster_roles
                - Items changed
                  - Properties changed
                    - Modified property: role
                      - Format changed from '' to 'uri'
                      - Deleted enum values: [owner member]
              - Modified property: project_roles
                - Items changed
                  - Properties changed
                    - Modified property: role
                      - Format changed from '' to 'uri'
                      - MaxLength changed from 255 to null

GET /api/rancher-users/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: cluster_roles
              - Items changed
                - Properties changed
                  - Modified property: role
                    - Format changed from '' to 'uri'
                    - Deleted enum values: [owner member]
            - Modified property: project_roles
              - Items changed
                - Properties changed
                  - Modified property: role
                    - Format changed from '' to 'uri'
                    - MaxLength changed from 255 to null

GET /api/slurm-allocations/

- New query param: can_manage

GET /api/vmware-disks/

- New query param: can_manage

GET /api/vmware-ports/

- New query param: can_manage

GET /api/vmware-virtual-machine/

- New query param: can_manage

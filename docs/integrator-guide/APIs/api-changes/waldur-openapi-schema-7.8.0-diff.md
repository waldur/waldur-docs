# OpenAPI schema diff - 7.8.0

## For version 7.8.0

### New Endpoints: 2

--------------------
POST /api/marketplace-orders/{uuid}/delete_attachment/  
POST /api/marketplace-orders/{uuid}/update_attachment/  

### Deleted Endpoints: 2

------------------------
POST /api/rancher-clusters/  
DELETE /api/rancher-clusters/{uuid}/  

### Modified Endpoints: 86

--------------------------
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
                    - New property: attachment
                    - New property: error_traceback
                    - New property: request_comment
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: attachment
                    - New property: error_traceback
                    - New property: request_comment
            - Modified property: slug
              - ReadOnly changed from true to false

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
                      - New property: deployment_mode
                      - New property: order_supports_comments_and_metadata

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
                    - New property: deployment_mode
                    - New property: order_supports_comments_and_metadata

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
                      - New property: attachment
                      - New property: error_traceback
                      - New property: request_comment
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: attachment
                      - New property: error_traceback
                      - New property: request_comment

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
                    - New property: attachment
                    - New property: error_traceback
                    - New property: request_comment
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: attachment
                    - New property: error_traceback
                    - New property: request_comment

POST /api/customers/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: slug

PATCH /api/customers/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: slug

PUT /api/customers/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: slug

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
                      - New property: attachment
                      - New property: error_traceback
                      - New property: request_comment
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: attachment
                      - New property: error_traceback
                      - New property: request_comment
              - Modified property: slug
                - ReadOnly changed from true to false

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
                    - New property: attachment
                    - New property: error_traceback
                    - New property: request_comment
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: attachment
                    - New property: error_traceback
                    - New property: request_comment
            - Modified property: slug
              - ReadOnly changed from true to false

GET /api/marketplace-offering-users/

- New query param: has_consent
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [has_consent requires_reconsent]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: has_consent
              - New property: requires_reconsent

HEAD /api/marketplace-offering-users/

- New query param: has_consent

POST /api/marketplace-offering-users/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: has_consent
            - New property: requires_reconsent

GET /api/marketplace-offering-users/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [has_consent requires_reconsent]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: has_consent
            - New property: requires_reconsent

PATCH /api/marketplace-offering-users/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: has_consent
            - New property: requires_reconsent

PUT /api/marketplace-offering-users/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: has_consent
            - New property: requires_reconsent

GET /api/marketplace-orders/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [attachment request_comment]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: attachment
              - New property: error_traceback
              - New property: request_comment

POST /api/marketplace-orders/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: request_comment
          - Modified property: attributes
            - Property 'OneOf' changed
              - Schemas deleted: #/components/schemas/MarketplaceRancherCreateOrderAttributes, #/components/schemas/MarketplaceManagedRancherCreateOrderAttributes
              - Modified schema: #/components/schemas/OpenStackTenantCreateOrderAttributes
                - Properties changed
                  - Deleted property: user_password
                  - Deleted property: user_username
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: attachment
            - New required property: error_traceback
          - Properties changed
            - New property: attachment
            - New property: error_traceback
            - New property: request_comment

GET /api/marketplace-orders/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [attachment request_comment]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: attachment
            - New property: error_traceback
            - New property: request_comment

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
                    - New property: deployment_mode
                    - New property: order_supports_comments_and_metadata
            - Modified property: slug
              - ReadOnly changed from true to false

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
                      - New property: deployment_mode
                      - New property: order_supports_comments_and_metadata

POST /api/marketplace-provider-offerings/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: slug
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: slug
          - Properties changed
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: deployment_mode
                    - New property: order_supports_comments_and_metadata
            - Modified property: slug
              - ReadOnly changed from true to false

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
                    - New property: deployment_mode
                    - New property: order_supports_comments_and_metadata

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
                    - New property: attachment
                    - New property: error_traceback
                    - New property: request_comment
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: attachment
                    - New property: error_traceback
                    - New property: request_comment
            - Modified property: slug
              - ReadOnly changed from true to false

GET /api/marketplace-provider-offerings/{uuid}/list_customer_projects/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: slug
                - ReadOnly changed from true to false

GET /api/marketplace-provider-offerings/{uuid}/list_customer_service_accounts/

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
                    - New property: deployment_mode
                    - New property: order_supports_comments_and_metadata

GET /api/marketplace-provider-offerings/{uuid}/list_customer_users/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: slug
                - ReadOnly changed from true to false

GET /api/marketplace-provider-offerings/{uuid}/list_project_service_accounts/

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
                    - New property: deployment_mode
                    - New property: order_supports_comments_and_metadata

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
                    - New property: deployment_mode
                    - New property: order_supports_comments_and_metadata
            - Modified property: slug
              - ReadOnly changed from true to false

GET /api/marketplace-provider-offerings/{uuid}/orders/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: attachment
              - New property: error_traceback
              - New property: request_comment

GET /api/marketplace-provider-offerings/{uuid}/orders/{order_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: attachment
            - New property: error_traceback
            - New property: request_comment

POST /api/marketplace-provider-offerings/{uuid}/refresh_offering_usernames/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: slug

GET /api/marketplace-provider-offerings/{uuid}/stats/

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
                    - New property: deployment_mode
                    - New property: order_supports_comments_and_metadata

POST /api/marketplace-provider-offerings/{uuid}/update_image/

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
                    - New property: deployment_mode
                    - New property: order_supports_comments_and_metadata

POST /api/marketplace-provider-offerings/{uuid}/update_integration/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: plugin_options
            - Properties changed
              - New property: deployment_mode
              - New property: order_supports_comments_and_metadata

POST /api/marketplace-provider-offerings/{uuid}/update_overview/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: slug

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
                    - New property: deployment_mode
                    - New property: order_supports_comments_and_metadata

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
                      - New property: attachment
                      - New property: error_traceback
                      - New property: request_comment
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: attachment
                      - New property: error_traceback
                      - New property: request_comment
              - Modified property: slug
                - ReadOnly changed from true to false

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
                    - New property: attachment
                    - New property: error_traceback
                    - New property: request_comment
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: attachment
                    - New property: error_traceback
                    - New property: request_comment
            - Modified property: slug
              - ReadOnly changed from true to false

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
                    - New property: attachment
                    - New property: error_traceback
                    - New property: request_comment
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: attachment
                    - New property: error_traceback
                    - New property: request_comment
            - Modified property: slug
              - ReadOnly changed from true to false

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
                    - New property: attachment
                    - New property: error_traceback
                    - New property: request_comment
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: attachment
                    - New property: error_traceback
                    - New property: request_comment
            - Modified property: slug
              - ReadOnly changed from true to false

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
                    - New property: deployment_mode
                    - New property: order_supports_comments_and_metadata
            - Modified property: slug
              - ReadOnly changed from true to false

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
                    - New property: attachment
                    - New property: error_traceback
                    - New property: request_comment
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: attachment
                    - New property: error_traceback
                    - New property: request_comment
            - Modified property: slug
              - ReadOnly changed from true to false

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
                      - New property: deployment_mode
                      - New property: order_supports_comments_and_metadata
              - Modified property: slug
                - ReadOnly changed from true to false

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
                    - New property: deployment_mode
                    - New property: order_supports_comments_and_metadata
            - Modified property: slug
              - ReadOnly changed from true to false

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
                      - New property: attachment
                      - New property: error_traceback
                      - New property: request_comment
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: attachment
                      - New property: error_traceback
                      - New property: request_comment
              - Modified property: slug
                - ReadOnly changed from true to false

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
                    - New property: attachment
                    - New property: error_traceback
                    - New property: request_comment
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: attachment
                    - New property: error_traceback
                    - New property: request_comment
            - Modified property: slug
              - ReadOnly changed from true to false

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
                    - New property: attachment
                    - New property: error_traceback
                    - New property: request_comment
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: attachment
                    - New property: error_traceback
                    - New property: request_comment
            - Modified property: slug
              - ReadOnly changed from true to false

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
                    - New property: attachment
                    - New property: error_traceback
                    - New property: request_comment
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: attachment
                    - New property: error_traceback
                    - New property: request_comment
            - Modified property: slug
              - ReadOnly changed from true to false

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
                    - New property: deployment_mode
                    - New property: order_supports_comments_and_metadata
            - Modified property: slug
              - ReadOnly changed from true to false

POST /api/marketplace-resources/{uuid}/update_limits/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: attachment
          - New property: request_comment

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
                      - New property: deployment_mode
                      - New property: order_supports_comments_and_metadata

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
                    - New property: deployment_mode
                    - New property: order_supports_comments_and_metadata

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
                    - New property: deployment_mode
                    - New property: order_supports_comments_and_metadata

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
                    - New property: deployment_mode
                    - New property: order_supports_comments_and_metadata

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
                    - New property: deployment_mode
                    - New property: order_supports_comments_and_metadata

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
                    - New property: deployment_mode
                    - New property: order_supports_comments_and_metadata

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
                    - New property: deployment_mode
                    - New property: order_supports_comments_and_metadata

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
                    - New property: deployment_mode
                    - New property: order_supports_comments_and_metadata
            - Modified property: slug
              - ReadOnly changed from true to false

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
                    - New property: deployment_mode
                    - New property: order_supports_comments_and_metadata
            - Modified property: slug
              - ReadOnly changed from true to false

POST /api/marketplace-service-providers/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: enable_notifications

GET /api/marketplace-service-providers/{service_provider_uuid}/projects/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: slug
                - ReadOnly changed from true to false

PATCH /api/marketplace-service-providers/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: enable_notifications

PUT /api/marketplace-service-providers/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: enable_notifications

POST /api/openstack-tenants/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: user_password
          - New property: user_username

PUT /api/openstack-tenants/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: user_password
          - New property: user_username

GET /api/projects/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: slug
                - ReadOnly changed from true to false

POST /api/projects/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: slug
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: slug
              - ReadOnly changed from true to false

GET /api/projects/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: slug
              - ReadOnly changed from true to false

PATCH /api/projects/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: slug
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: slug
              - ReadOnly changed from true to false

PUT /api/projects/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: slug
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: slug
              - ReadOnly changed from true to false

POST /api/projects/{uuid}/move_project/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: slug
              - ReadOnly changed from true to false

GET /api/promotions-campaigns/{uuid}/orders/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: attachment
              - New property: error_traceback
              - New property: request_comment

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
                      - New property: attachment
                      - New property: error_traceback
                      - New property: request_comment
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: attachment
                      - New property: error_traceback
                      - New property: request_comment
              - Modified property: slug
                - ReadOnly changed from true to false

POST /api/proposal-protected-calls/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: slug

PATCH /api/proposal-protected-calls/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: slug

PUT /api/proposal-protected-calls/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: slug

POST /api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/close/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: slug

PUT /api/rancher-clusters/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Required changed
          - Deleted required property: nodes
          - Deleted required property: project
          - Deleted required property: service_settings
        - Properties changed
          - Deleted property: nodes
          - Deleted property: project
          - Deleted property: service_settings
          - Deleted property: tenant

POST /api/rancher-clusters/{uuid}/create_management_security_group/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Required changed
          - Deleted required property: nodes
          - Deleted required property: project
          - Deleted required property: service_settings
        - Properties changed
          - Deleted property: nodes
          - Deleted property: project
          - Deleted property: service_settings
          - Deleted property: tenant

GET /api/users/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: slug
                - ReadOnly changed from true to false

POST /api/users/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: slug
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: slug
              - ReadOnly changed from true to false

GET /api/users/me/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: slug
              - ReadOnly changed from true to false

GET /api/users/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: slug
              - ReadOnly changed from true to false

PATCH /api/users/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: slug
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: slug
              - ReadOnly changed from true to false

PUT /api/users/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: slug
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: slug
              - ReadOnly changed from true to false

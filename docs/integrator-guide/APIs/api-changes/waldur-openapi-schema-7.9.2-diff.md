# OpenAPI schema diff - 7.9.2

## For version 7.9.2

### New Endpoints: 9

--------------------
POST /api/marketplace-provider-offerings/import_offering/  
POST /api/marketplace-provider-offerings/{uuid}/export_offering/  
POST /api/marketplace-provider-offerings/{uuid}/make_available/  
POST /api/marketplace-provider-offerings/{uuid}/make_unavailable/  
POST /api/marketplace-provider-resources/{uuid}/restore/  
POST /api/marketplace-resources/{uuid}/restore/  
DELETE /api/user-invitations/{uuid}/  
PATCH /api/user-invitations/{uuid}/  
PUT /api/user-invitations/{uuid}/  

### Deleted Endpoints: None

---------------------------

### Modified Endpoints: 114

---------------------------
POST /api/backend-resources/{uuid}/import_resource/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: order_subtype
                    - Modified property: old_cost_estimate
                      - Type changed from 'string' to 'number'
                      - Format changed from 'decimal' to 'double'
                      - Nullable changed from true to false
                      - Pattern changed from '^-?\d{0,12}(?:\.\d{0,10})?$' to ''
                    - Modified property: type
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/RequestTypes
                          - New enum values: [Restore]
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: order_subtype
                    - Modified property: old_cost_estimate
                      - Type changed from 'string' to 'number'
                      - Format changed from 'decimal' to 'double'
                      - Nullable changed from true to false
                      - Pattern changed from '^-?\d{0,12}(?:\.\d{0,10})?$' to ''
                    - Modified property: type
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/RequestTypes
                          - New enum values: [Restore]

GET /api/booking-offerings/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [billing_type_classification]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: billing_type_classification
              - Modified property: plugin_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedPluginOptions
                    - Properties changed
                      - New property: auto_approve_marketplace_script
                      - New property: can_restore_resource
              - Modified property: state
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OfferingState
                    - New enum values: [Unavailable]

GET /api/booking-offerings/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [billing_type_classification]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: billing_type_classification
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: auto_approve_marketplace_script
                    - New property: can_restore_resource
            - Modified property: state
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingState
                  - New enum values: [Unavailable]

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
                      - New property: order_subtype
                      - Modified property: old_cost_estimate
                        - Type changed from 'string' to 'number'
                        - Format changed from 'decimal' to 'double'
                        - Nullable changed from true to false
                        - Pattern changed from '^-?\d{0,12}(?:\.\d{0,10})?$' to ''
                      - Modified property: type
                        - Property 'AllOf' changed
                          - Modified schema: #/components/schemas/RequestTypes
                            - New enum values: [Restore]
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: order_subtype
                      - Modified property: old_cost_estimate
                        - Type changed from 'string' to 'number'
                        - Format changed from 'decimal' to 'double'
                        - Nullable changed from true to false
                        - Pattern changed from '^-?\d{0,12}(?:\.\d{0,10})?$' to ''
                      - Modified property: type
                        - Property 'AllOf' changed
                          - Modified schema: #/components/schemas/RequestTypes
                            - New enum values: [Restore]

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
                    - New property: order_subtype
                    - Modified property: old_cost_estimate
                      - Type changed from 'string' to 'number'
                      - Format changed from 'decimal' to 'double'
                      - Nullable changed from true to false
                      - Pattern changed from '^-?\d{0,12}(?:\.\d{0,10})?$' to ''
                    - Modified property: type
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/RequestTypes
                          - New enum values: [Restore]
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: order_subtype
                    - Modified property: old_cost_estimate
                      - Type changed from 'string' to 'number'
                      - Format changed from 'decimal' to 'double'
                      - Nullable changed from true to false
                      - Pattern changed from '^-?\d{0,12}(?:\.\d{0,10})?$' to ''
                    - Modified property: type
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/RequestTypes
                          - New enum values: [Restore]

GET /api/customer-credits/

- New query param: query

HEAD /api/customer-credits/

- New query param: query

GET /api/customer-credits/{uuid}/consumptions/

- New query param: query

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
                  - New enum values: [user_invitation_updated user_invitation_deleted]

POST /api/hooks-email/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [user_invitation_updated user_invitation_deleted]
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [user_invitation_updated user_invitation_deleted]

GET /api/hooks-email/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [user_invitation_updated user_invitation_deleted]

PATCH /api/hooks-email/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [user_invitation_updated user_invitation_deleted]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [user_invitation_updated user_invitation_deleted]

PUT /api/hooks-email/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [user_invitation_updated user_invitation_deleted]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [user_invitation_updated user_invitation_deleted]

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
                  - New enum values: [user_invitation_updated user_invitation_deleted]

POST /api/hooks-web/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [user_invitation_updated user_invitation_deleted]
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [user_invitation_updated user_invitation_deleted]

GET /api/hooks-web/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [user_invitation_updated user_invitation_deleted]

PATCH /api/hooks-web/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [user_invitation_updated user_invitation_deleted]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [user_invitation_updated user_invitation_deleted]

PUT /api/hooks-web/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [user_invitation_updated user_invitation_deleted]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [user_invitation_updated user_invitation_deleted]

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
                      - New property: order_subtype
                      - Modified property: old_cost_estimate
                        - Type changed from 'string' to 'number'
                        - Format changed from 'decimal' to 'double'
                        - Nullable changed from true to false
                        - Pattern changed from '^-?\d{0,12}(?:\.\d{0,10})?$' to ''
                      - Modified property: type
                        - Property 'AllOf' changed
                          - Modified schema: #/components/schemas/RequestTypes
                            - New enum values: [Restore]
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: order_subtype
                      - Modified property: old_cost_estimate
                        - Type changed from 'string' to 'number'
                        - Format changed from 'decimal' to 'double'
                        - Nullable changed from true to false
                        - Pattern changed from '^-?\d{0,12}(?:\.\d{0,10})?$' to ''
                      - Modified property: type
                        - Property 'AllOf' changed
                          - Modified schema: #/components/schemas/RequestTypes
                            - New enum values: [Restore]

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
                    - New property: order_subtype
                    - Modified property: old_cost_estimate
                      - Type changed from 'string' to 'number'
                      - Format changed from 'decimal' to 'double'
                      - Nullable changed from true to false
                      - Pattern changed from '^-?\d{0,12}(?:\.\d{0,10})?$' to ''
                    - Modified property: type
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/RequestTypes
                          - New enum values: [Restore]
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: order_subtype
                    - Modified property: old_cost_estimate
                      - Type changed from 'string' to 'number'
                      - Format changed from 'decimal' to 'double'
                      - Nullable changed from true to false
                      - Pattern changed from '^-?\d{0,12}(?:\.\d{0,10})?$' to ''
                    - Modified property: type
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/RequestTypes
                          - New enum values: [Restore]

GET /api/marketplace-categories/

- Modified query param: customers_offerings_state
  - Schema changed
    - Items changed
      - New enum values: [5]

HEAD /api/marketplace-categories/

- Modified query param: customers_offerings_state
  - Schema changed
    - Items changed
      - New enum values: [5]

DELETE /api/marketplace-offering-user-roles/{uuid}/

- Extensions changed
  - New extension: x-permissions

PATCH /api/marketplace-offering-user-roles/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/marketplace-offering-user-roles/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-orders/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [order_subtype]
- Modified query param: type
  - Schema changed
    - Items changed
      - New enum values: [Restore]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: order_subtype
              - Modified property: old_cost_estimate
                - Type changed from 'string' to 'number'
                - Format changed from 'decimal' to 'double'
                - Nullable changed from true to false
                - Pattern changed from '^-?\d{0,12}(?:\.\d{0,10})?$' to ''
              - Modified property: type
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/RequestTypes
                    - New enum values: [Restore]

HEAD /api/marketplace-orders/

- Modified query param: type
  - Schema changed
    - Items changed
      - New enum values: [Restore]

POST /api/marketplace-orders/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: type
            - Property 'AllOf' changed
              - Modified schema: #/components/schemas/RequestTypes
                - New enum values: [Restore]
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: order_subtype
            - Modified property: old_cost_estimate
              - Type changed from 'string' to 'number'
              - Format changed from 'decimal' to 'double'
              - Nullable changed from true to false
              - Pattern changed from '^-?\d{0,12}(?:\.\d{0,10})?$' to ''
            - Modified property: type
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/RequestTypes
                  - New enum values: [Restore]

GET /api/marketplace-orders/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [order_subtype]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: order_subtype
            - Modified property: old_cost_estimate
              - Type changed from 'string' to 'number'
              - Format changed from 'decimal' to 'double'
              - Nullable changed from true to false
              - Pattern changed from '^-?\d{0,12}(?:\.\d{0,10})?$' to ''
            - Modified property: type
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/RequestTypes
                  - New enum values: [Restore]

GET /api/marketplace-orders/{uuid}/offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: billing_type_classification
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: auto_approve_marketplace_script
                    - New property: can_restore_resource
            - Modified property: state
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingState
                  - New enum values: [Unavailable]

GET /api/marketplace-provider-offerings/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [billing_type_classification]
- Modified query param: state
  - Schema changed
    - Items changed
      - New enum values: [Unavailable]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: billing_type_classification
              - Modified property: plugin_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedPluginOptions
                    - Properties changed
                      - New property: auto_approve_marketplace_script
                      - New property: can_restore_resource
              - Modified property: state
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OfferingState
                    - New enum values: [Unavailable]

HEAD /api/marketplace-provider-offerings/

- Modified query param: state
  - Schema changed
    - Items changed
      - New enum values: [Unavailable]

POST /api/marketplace-provider-offerings/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: billing_type_classification
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: auto_approve_marketplace_script
                    - New property: can_restore_resource
            - Modified property: state
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingState
                  - New enum values: [Unavailable]

GET /api/marketplace-provider-offerings/groups/

- Modified query param: state
  - Schema changed
    - Items changed
      - New enum values: [Unavailable]

HEAD /api/marketplace-provider-offerings/groups/

- Modified query param: state
  - Schema changed
    - Items changed
      - New enum values: [Unavailable]

GET /api/marketplace-provider-offerings/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [billing_type_classification]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: billing_type_classification
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: auto_approve_marketplace_script
                    - New property: can_restore_resource
            - Modified property: state
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingState
                  - New enum values: [Unavailable]

GET /api/marketplace-provider-offerings/{uuid}/component_stats/

- Modified query param: state
  - Schema changed
    - Items changed
      - New enum values: [Unavailable]

GET /api/marketplace-provider-offerings/{uuid}/costs/

- Modified query param: state
  - Schema changed
    - Items changed
      - New enum values: [Unavailable]

GET /api/marketplace-provider-offerings/{uuid}/customers/

- Modified query param: state
  - Schema changed
    - Items changed
      - New enum values: [Unavailable]

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
                    - New property: order_subtype
                    - Modified property: old_cost_estimate
                      - Type changed from 'string' to 'number'
                      - Format changed from 'decimal' to 'double'
                      - Nullable changed from true to false
                      - Pattern changed from '^-?\d{0,12}(?:\.\d{0,10})?$' to ''
                    - Modified property: type
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/RequestTypes
                          - New enum values: [Restore]
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: order_subtype
                    - Modified property: old_cost_estimate
                      - Type changed from 'string' to 'number'
                      - Format changed from 'decimal' to 'double'
                      - Nullable changed from true to false
                      - Pattern changed from '^-?\d{0,12}(?:\.\d{0,10})?$' to ''
                    - Modified property: type
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/RequestTypes
                          - New enum values: [Restore]

GET /api/marketplace-provider-offerings/{uuid}/list_course_accounts/

- Modified query param: state
  - Schema changed
    - Items changed
      - New enum values: [Unavailable]

GET /api/marketplace-provider-offerings/{uuid}/list_customer_service_accounts/

- Modified query param: state
  - Schema changed
    - Items changed
      - New enum values: [Unavailable]

GET /api/marketplace-provider-offerings/{uuid}/list_project_service_accounts/

- Modified query param: state
  - Schema changed
    - Items changed
      - New enum values: [Unavailable]

POST /api/marketplace-provider-offerings/{uuid}/move_offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: billing_type_classification
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: auto_approve_marketplace_script
                    - New property: can_restore_resource
            - Modified property: state
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingState
                  - New enum values: [Unavailable]

GET /api/marketplace-provider-offerings/{uuid}/orders/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [order_subtype]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: order_subtype
              - Modified property: old_cost_estimate
                - Type changed from 'string' to 'number'
                - Format changed from 'decimal' to 'double'
                - Nullable changed from true to false
                - Pattern changed from '^-?\d{0,12}(?:\.\d{0,10})?$' to ''
              - Modified property: type
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/RequestTypes
                    - New enum values: [Restore]

GET /api/marketplace-provider-offerings/{uuid}/orders/{order_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: order_subtype
            - Modified property: old_cost_estimate
              - Type changed from 'string' to 'number'
              - Format changed from 'decimal' to 'double'
              - Nullable changed from true to false
              - Pattern changed from '^-?\d{0,12}(?:\.\d{0,10})?$' to ''
            - Modified property: type
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/RequestTypes
                  - New enum values: [Restore]

POST /api/marketplace-provider-offerings/{uuid}/update_integration/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: plugin_options
            - Properties changed
              - New property: auto_approve_marketplace_script
              - New property: can_restore_resource

GET /api/marketplace-provider-offerings/{uuid}/user_has_resource_access/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [billing_type_classification]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: billing_type_classification
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: auto_approve_marketplace_script
                    - New property: can_restore_resource
            - Modified property: state
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingState
                  - New enum values: [Unavailable]

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
                      - New property: order_subtype
                      - Modified property: old_cost_estimate
                        - Type changed from 'string' to 'number'
                        - Format changed from 'decimal' to 'double'
                        - Nullable changed from true to false
                        - Pattern changed from '^-?\d{0,12}(?:\.\d{0,10})?$' to ''
                      - Modified property: type
                        - Property 'AllOf' changed
                          - Modified schema: #/components/schemas/RequestTypes
                            - New enum values: [Restore]
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: order_subtype
                      - Modified property: old_cost_estimate
                        - Type changed from 'string' to 'number'
                        - Format changed from 'decimal' to 'double'
                        - Nullable changed from true to false
                        - Pattern changed from '^-?\d{0,12}(?:\.\d{0,10})?$' to ''
                      - Modified property: type
                        - Property 'AllOf' changed
                          - Modified schema: #/components/schemas/RequestTypes
                            - New enum values: [Restore]

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
                    - New property: order_subtype
                    - Modified property: old_cost_estimate
                      - Type changed from 'string' to 'number'
                      - Format changed from 'decimal' to 'double'
                      - Nullable changed from true to false
                      - Pattern changed from '^-?\d{0,12}(?:\.\d{0,10})?$' to ''
                    - Modified property: type
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/RequestTypes
                          - New enum values: [Restore]
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: order_subtype
                    - Modified property: old_cost_estimate
                      - Type changed from 'string' to 'number'
                      - Format changed from 'decimal' to 'double'
                      - Nullable changed from true to false
                      - Pattern changed from '^-?\d{0,12}(?:\.\d{0,10})?$' to ''
                    - Modified property: type
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/RequestTypes
                          - New enum values: [Restore]

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
                    - New property: order_subtype
                    - Modified property: old_cost_estimate
                      - Type changed from 'string' to 'number'
                      - Format changed from 'decimal' to 'double'
                      - Nullable changed from true to false
                      - Pattern changed from '^-?\d{0,12}(?:\.\d{0,10})?$' to ''
                    - Modified property: type
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/RequestTypes
                          - New enum values: [Restore]
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: order_subtype
                    - Modified property: old_cost_estimate
                      - Type changed from 'string' to 'number'
                      - Format changed from 'decimal' to 'double'
                      - Nullable changed from true to false
                      - Pattern changed from '^-?\d{0,12}(?:\.\d{0,10})?$' to ''
                    - Modified property: type
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/RequestTypes
                          - New enum values: [Restore]

GET /api/marketplace-provider-resources/{uuid}/offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: billing_type_classification
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: auto_approve_marketplace_script
                    - New property: can_restore_resource
            - Modified property: state
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingState
                  - New enum values: [Unavailable]

GET /api/marketplace-public-offerings/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [billing_type_classification]
- Modified query param: state
  - Schema changed
    - Items changed
      - New enum values: [Unavailable]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: billing_type_classification
              - Modified property: plugin_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedPluginOptions
                    - Properties changed
                      - New property: auto_approve_marketplace_script
                      - New property: can_restore_resource
              - Modified property: state
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OfferingState
                    - New enum values: [Unavailable]

HEAD /api/marketplace-public-offerings/

- Modified query param: state
  - Schema changed
    - Items changed
      - New enum values: [Unavailable]

GET /api/marketplace-public-offerings/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [billing_type_classification]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: billing_type_classification
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: auto_approve_marketplace_script
                    - New property: can_restore_resource
            - Modified property: state
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingState
                  - New enum values: [Unavailable]

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
                      - New property: order_subtype
                      - Modified property: old_cost_estimate
                        - Type changed from 'string' to 'number'
                        - Format changed from 'decimal' to 'double'
                        - Nullable changed from true to false
                        - Pattern changed from '^-?\d{0,12}(?:\.\d{0,10})?$' to ''
                      - Modified property: type
                        - Property 'AllOf' changed
                          - Modified schema: #/components/schemas/RequestTypes
                            - New enum values: [Restore]
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: order_subtype
                      - Modified property: old_cost_estimate
                        - Type changed from 'string' to 'number'
                        - Format changed from 'decimal' to 'double'
                        - Nullable changed from true to false
                        - Pattern changed from '^-?\d{0,12}(?:\.\d{0,10})?$' to ''
                      - Modified property: type
                        - Property 'AllOf' changed
                          - Modified schema: #/components/schemas/RequestTypes
                            - New enum values: [Restore]

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
                    - New property: order_subtype
                    - Modified property: old_cost_estimate
                      - Type changed from 'string' to 'number'
                      - Format changed from 'decimal' to 'double'
                      - Nullable changed from true to false
                      - Pattern changed from '^-?\d{0,12}(?:\.\d{0,10})?$' to ''
                    - Modified property: type
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/RequestTypes
                          - New enum values: [Restore]
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: order_subtype
                    - Modified property: old_cost_estimate
                      - Type changed from 'string' to 'number'
                      - Format changed from 'decimal' to 'double'
                      - Nullable changed from true to false
                      - Pattern changed from '^-?\d{0,12}(?:\.\d{0,10})?$' to ''
                    - Modified property: type
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/RequestTypes
                          - New enum values: [Restore]

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
                    - New property: order_subtype
                    - Modified property: old_cost_estimate
                      - Type changed from 'string' to 'number'
                      - Format changed from 'decimal' to 'double'
                      - Nullable changed from true to false
                      - Pattern changed from '^-?\d{0,12}(?:\.\d{0,10})?$' to ''
                    - Modified property: type
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/RequestTypes
                          - New enum values: [Restore]
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: order_subtype
                    - Modified property: old_cost_estimate
                      - Type changed from 'string' to 'number'
                      - Format changed from 'decimal' to 'double'
                      - Nullable changed from true to false
                      - Pattern changed from '^-?\d{0,12}(?:\.\d{0,10})?$' to ''
                    - Modified property: type
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/RequestTypes
                          - New enum values: [Restore]

GET /api/marketplace-resources/{uuid}/offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: billing_type_classification
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: auto_approve_marketplace_script
                    - New property: can_restore_resource
            - Modified property: state
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingState
                  - New enum values: [Unavailable]

POST /api/marketplace-resources/{uuid}/renew/

- Request body changed
  - Content changed
    - New media type: application/x-www-form-urlencoded
    - New media type: multipart/form-data
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
                      - New property: auto_approve_marketplace_script
                      - New property: can_restore_resource
              - Modified property: state
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/RobotAccountStates
                    - Type changed from 'integer' to 'string'
                    - New enum values: [Requested Creating OK Requested deletion Deleted Error]
                    - Deleted enum values: [1 2 3 4 5 6]

POST /api/marketplace-robot-accounts/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: state
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/RobotAccountStates
                  - Type changed from 'integer' to 'string'
                  - New enum values: [Requested Creating OK Requested deletion Deleted Error]
                  - Deleted enum values: [1 2 3 4 5 6]

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
                    - New property: auto_approve_marketplace_script
                    - New property: can_restore_resource
            - Modified property: state
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/RobotAccountStates
                  - Type changed from 'integer' to 'string'
                  - New enum values: [Requested Creating OK Requested deletion Deleted Error]
                  - Deleted enum values: [1 2 3 4 5 6]

PATCH /api/marketplace-robot-accounts/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: state
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/RobotAccountStates
                  - Type changed from 'integer' to 'string'
                  - New enum values: [Requested Creating OK Requested deletion Deleted Error]
                  - Deleted enum values: [1 2 3 4 5 6]

PUT /api/marketplace-robot-accounts/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: state
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/RobotAccountStates
                  - Type changed from 'integer' to 'string'
                  - New enum values: [Requested Creating OK Requested deletion Deleted Error]
                  - Deleted enum values: [1 2 3 4 5 6]

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
                    - New property: auto_approve_marketplace_script
                    - New property: can_restore_resource
            - Modified property: state
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/RobotAccountStates
                  - Type changed from 'integer' to 'string'
                  - New enum values: [Requested Creating OK Requested deletion Deleted Error]
                  - Deleted enum values: [1 2 3 4 5 6]

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
                    - New property: auto_approve_marketplace_script
                    - New property: can_restore_resource
            - Modified property: state
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/RobotAccountStates
                  - Type changed from 'integer' to 'string'
                  - New enum values: [Requested Creating OK Requested deletion Deleted Error]
                  - Deleted enum values: [1 2 3 4 5 6]

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
                    - New property: auto_approve_marketplace_script
                    - New property: can_restore_resource
            - Modified property: state
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/RobotAccountStates
                  - Type changed from 'integer' to 'string'
                  - New enum values: [Requested Creating OK Requested deletion Deleted Error]
                  - Deleted enum values: [1 2 3 4 5 6]

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
                    - New property: auto_approve_marketplace_script
                    - New property: can_restore_resource
            - Modified property: state
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/RobotAccountStates
                  - Type changed from 'integer' to 'string'
                  - New enum values: [Requested Creating OK Requested deletion Deleted Error]
                  - Deleted enum values: [1 2 3 4 5 6]

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
                    - New property: auto_approve_marketplace_script
                    - New property: can_restore_resource
            - Modified property: state
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/RobotAccountStates
                  - Type changed from 'integer' to 'string'
                  - New enum values: [Requested Creating OK Requested deletion Deleted Error]
                  - Deleted enum values: [1 2 3 4 5 6]

POST /api/marketplace-script-dry-run/{uuid}/async_run/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: type
            - Property 'AllOf' changed
              - Modified schema: #/components/schemas/DryRunTypeEnum
                - New enum values: [Restore]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: billing_type_classification
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: auto_approve_marketplace_script
                    - New property: can_restore_resource
            - Modified property: state
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingState
                  - New enum values: [Unavailable]

POST /api/marketplace-script-dry-run/{uuid}/run/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: type
            - Property 'AllOf' changed
              - Modified schema: #/components/schemas/DryRunTypeEnum
                - New enum values: [Restore]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: billing_type_classification
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: auto_approve_marketplace_script
                    - New property: can_restore_resource
            - Modified property: state
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingState
                  - New enum values: [Unavailable]

GET /api/marketplace-service-providers/{service_provider_uuid}/offerings/

- Modified query param: state
  - Schema changed
    - Items changed
      - New enum values: [Unavailable]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: state
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OfferingState
                    - New enum values: [Unavailable]

GET /api/marketplace-software-catalogs/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: catalog_type_display
              - New required property: last_successful_update
              - New required property: last_update_attempt
            - Properties changed
              - New property: auto_update_enabled
              - New property: catalog_type
              - New property: catalog_type_display
              - New property: last_successful_update
              - New property: last_update_attempt
              - New property: metadata
              - New property: update_errors
              - Modified property: name
                - Description changed from 'Catalog name (e.g., EESSI)' to 'Catalog name (e.g., EESSI, Spack)'
              - Modified property: version
                - Description changed from 'Catalog version (e.g., 2023.06)' to 'Catalog version (e.g., 2023.06, 0.21.0)'

POST /api/marketplace-software-catalogs/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: auto_update_enabled
          - New property: catalog_type
          - New property: metadata
          - New property: update_errors
          - Modified property: name
            - Description changed from 'Catalog name (e.g., EESSI)' to 'Catalog name (e.g., EESSI, Spack)'
          - Modified property: version
            - Description changed from 'Catalog version (e.g., 2023.06)' to 'Catalog version (e.g., 2023.06, 0.21.0)'
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: catalog_type_display
            - New required property: last_successful_update
            - New required property: last_update_attempt
          - Properties changed
            - New property: auto_update_enabled
            - New property: catalog_type
            - New property: catalog_type_display
            - New property: last_successful_update
            - New property: last_update_attempt
            - New property: metadata
            - New property: update_errors
            - Modified property: name
              - Description changed from 'Catalog name (e.g., EESSI)' to 'Catalog name (e.g., EESSI, Spack)'
            - Modified property: version
              - Description changed from 'Catalog version (e.g., 2023.06)' to 'Catalog version (e.g., 2023.06, 0.21.0)'

GET /api/marketplace-software-catalogs/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: catalog_type_display
            - New required property: last_successful_update
            - New required property: last_update_attempt
          - Properties changed
            - New property: auto_update_enabled
            - New property: catalog_type
            - New property: catalog_type_display
            - New property: last_successful_update
            - New property: last_update_attempt
            - New property: metadata
            - New property: update_errors
            - Modified property: name
              - Description changed from 'Catalog name (e.g., EESSI)' to 'Catalog name (e.g., EESSI, Spack)'
            - Modified property: version
              - Description changed from 'Catalog version (e.g., 2023.06)' to 'Catalog version (e.g., 2023.06, 0.21.0)'

PATCH /api/marketplace-software-catalogs/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: auto_update_enabled
          - New property: catalog_type
          - New property: metadata
          - New property: update_errors
          - Modified property: name
            - Description changed from 'Catalog name (e.g., EESSI)' to 'Catalog name (e.g., EESSI, Spack)'
          - Modified property: version
            - Description changed from 'Catalog version (e.g., 2023.06)' to 'Catalog version (e.g., 2023.06, 0.21.0)'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: catalog_type_display
            - New required property: last_successful_update
            - New required property: last_update_attempt
          - Properties changed
            - New property: auto_update_enabled
            - New property: catalog_type
            - New property: catalog_type_display
            - New property: last_successful_update
            - New property: last_update_attempt
            - New property: metadata
            - New property: update_errors
            - Modified property: name
              - Description changed from 'Catalog name (e.g., EESSI)' to 'Catalog name (e.g., EESSI, Spack)'
            - Modified property: version
              - Description changed from 'Catalog version (e.g., 2023.06)' to 'Catalog version (e.g., 2023.06, 0.21.0)'

PUT /api/marketplace-software-catalogs/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: auto_update_enabled
          - New property: catalog_type
          - New property: metadata
          - New property: update_errors
          - Modified property: name
            - Description changed from 'Catalog name (e.g., EESSI)' to 'Catalog name (e.g., EESSI, Spack)'
          - Modified property: version
            - Description changed from 'Catalog version (e.g., 2023.06)' to 'Catalog version (e.g., 2023.06, 0.21.0)'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: catalog_type_display
            - New required property: last_successful_update
            - New required property: last_update_attempt
          - Properties changed
            - New property: auto_update_enabled
            - New property: catalog_type
            - New property: catalog_type_display
            - New property: last_successful_update
            - New property: last_update_attempt
            - New property: metadata
            - New property: update_errors
            - Modified property: name
              - Description changed from 'Catalog name (e.g., EESSI)' to 'Catalog name (e.g., EESSI, Spack)'
            - Modified property: version
              - Description changed from 'Catalog version (e.g., 2023.06)' to 'Catalog version (e.g., 2023.06, 0.21.0)'

GET /api/marketplace-software-packages/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: catalog_type
              - New required property: catalog_type_display
              - New required property: extension_count
            - Properties changed
              - New property: catalog_type
              - New property: catalog_type_display
              - New property: categories
              - New property: extension_count
              - New property: is_extension
              - New property: licenses
              - New property: maintainers
              - New property: parent_software
              - Modified property: homepage
                - Nullable changed from false to true
              - Modified property: versions
                - Items changed
                  - Properties changed
                    - Modified property: targets
                      - Items changed
                        - Required changed
                          - Deleted required property: cpu_family
                          - Deleted required property: cpu_microarchitecture
                          - Deleted required property: path
                        - Properties changed
                          - New property: location
                          - New property: metadata
                          - New property: target_name
                          - New property: target_subtype
                          - New property: target_type
                          - Deleted property: cpu_family
                          - Deleted property: cpu_microarchitecture
                          - Deleted property: path

POST /api/marketplace-software-packages/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: categories
          - New property: is_extension
          - New property: licenses
          - New property: maintainers
          - New property: parent_software
          - Modified property: homepage
            - Nullable changed from false to true
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: catalog_type
            - New required property: catalog_type_display
            - New required property: extension_count
          - Properties changed
            - New property: catalog_type
            - New property: catalog_type_display
            - New property: categories
            - New property: extension_count
            - New property: is_extension
            - New property: licenses
            - New property: maintainers
            - New property: parent_software
            - Modified property: homepage
              - Nullable changed from false to true
            - Modified property: versions
              - Items changed
                - Properties changed
                  - Modified property: targets
                    - Items changed
                      - Required changed
                        - Deleted required property: cpu_family
                        - Deleted required property: cpu_microarchitecture
                        - Deleted required property: path
                      - Properties changed
                        - New property: location
                        - New property: metadata
                        - New property: target_name
                        - New property: target_subtype
                        - New property: target_type
                        - Deleted property: cpu_family
                        - Deleted property: cpu_microarchitecture
                        - Deleted property: path

GET /api/marketplace-software-packages/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: catalog_type
            - New required property: catalog_type_display
            - New required property: extension_count
          - Properties changed
            - New property: catalog_type
            - New property: catalog_type_display
            - New property: categories
            - New property: extension_count
            - New property: is_extension
            - New property: licenses
            - New property: maintainers
            - New property: parent_software
            - Modified property: homepage
              - Nullable changed from false to true
            - Modified property: versions
              - Items changed
                - Properties changed
                  - Modified property: targets
                    - Items changed
                      - Required changed
                        - Deleted required property: cpu_family
                        - Deleted required property: cpu_microarchitecture
                        - Deleted required property: path
                      - Properties changed
                        - New property: location
                        - New property: metadata
                        - New property: target_name
                        - New property: target_subtype
                        - New property: target_type
                        - Deleted property: cpu_family
                        - Deleted property: cpu_microarchitecture
                        - Deleted property: path

PATCH /api/marketplace-software-packages/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: categories
          - New property: is_extension
          - New property: licenses
          - New property: maintainers
          - New property: parent_software
          - Modified property: homepage
            - Nullable changed from false to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: catalog_type
            - New required property: catalog_type_display
            - New required property: extension_count
          - Properties changed
            - New property: catalog_type
            - New property: catalog_type_display
            - New property: categories
            - New property: extension_count
            - New property: is_extension
            - New property: licenses
            - New property: maintainers
            - New property: parent_software
            - Modified property: homepage
              - Nullable changed from false to true
            - Modified property: versions
              - Items changed
                - Properties changed
                  - Modified property: targets
                    - Items changed
                      - Required changed
                        - Deleted required property: cpu_family
                        - Deleted required property: cpu_microarchitecture
                        - Deleted required property: path
                      - Properties changed
                        - New property: location
                        - New property: metadata
                        - New property: target_name
                        - New property: target_subtype
                        - New property: target_type
                        - Deleted property: cpu_family
                        - Deleted property: cpu_microarchitecture
                        - Deleted property: path

PUT /api/marketplace-software-packages/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: categories
          - New property: is_extension
          - New property: licenses
          - New property: maintainers
          - New property: parent_software
          - Modified property: homepage
            - Nullable changed from false to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: catalog_type
            - New required property: catalog_type_display
            - New required property: extension_count
          - Properties changed
            - New property: catalog_type
            - New property: catalog_type_display
            - New property: categories
            - New property: extension_count
            - New property: is_extension
            - New property: licenses
            - New property: maintainers
            - New property: parent_software
            - Modified property: homepage
              - Nullable changed from false to true
            - Modified property: versions
              - Items changed
                - Properties changed
                  - Modified property: targets
                    - Items changed
                      - Required changed
                        - Deleted required property: cpu_family
                        - Deleted required property: cpu_microarchitecture
                        - Deleted required property: path
                      - Properties changed
                        - New property: location
                        - New property: metadata
                        - New property: target_name
                        - New property: target_subtype
                        - New property: target_type
                        - Deleted property: cpu_family
                        - Deleted property: cpu_microarchitecture
                        - Deleted property: path

GET /api/marketplace-software-targets/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: location
              - New required property: metadata
              - New required property: target_name
              - New required property: target_subtype
              - New required property: target_type
              - Deleted required property: cpu_family
              - Deleted required property: cpu_microarchitecture
              - Deleted required property: path
            - Properties changed
              - New property: location
              - New property: metadata
              - New property: target_name
              - New property: target_subtype
              - New property: target_type
              - Deleted property: cpu_family
              - Deleted property: cpu_microarchitecture
              - Deleted property: path

POST /api/marketplace-software-targets/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: location
            - New required property: metadata
            - New required property: target_name
            - New required property: target_subtype
            - New required property: target_type
            - Deleted required property: cpu_family
            - Deleted required property: cpu_microarchitecture
            - Deleted required property: path
          - Properties changed
            - New property: location
            - New property: metadata
            - New property: target_name
            - New property: target_subtype
            - New property: target_type
            - Deleted property: cpu_family
            - Deleted property: cpu_microarchitecture
            - Deleted property: path

GET /api/marketplace-software-targets/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: location
            - New required property: metadata
            - New required property: target_name
            - New required property: target_subtype
            - New required property: target_type
            - Deleted required property: cpu_family
            - Deleted required property: cpu_microarchitecture
            - Deleted required property: path
          - Properties changed
            - New property: location
            - New property: metadata
            - New property: target_name
            - New property: target_subtype
            - New property: target_type
            - Deleted property: cpu_family
            - Deleted property: cpu_microarchitecture
            - Deleted property: path

PATCH /api/marketplace-software-targets/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: location
            - New required property: metadata
            - New required property: target_name
            - New required property: target_subtype
            - New required property: target_type
            - Deleted required property: cpu_family
            - Deleted required property: cpu_microarchitecture
            - Deleted required property: path
          - Properties changed
            - New property: location
            - New property: metadata
            - New property: target_name
            - New property: target_subtype
            - New property: target_type
            - Deleted property: cpu_family
            - Deleted property: cpu_microarchitecture
            - Deleted property: path

PUT /api/marketplace-software-targets/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: location
            - New required property: metadata
            - New required property: target_name
            - New required property: target_subtype
            - New required property: target_type
            - Deleted required property: cpu_family
            - Deleted required property: cpu_microarchitecture
            - Deleted required property: path
          - Properties changed
            - New property: location
            - New property: metadata
            - New property: target_name
            - New property: target_subtype
            - New property: target_type
            - Deleted property: cpu_family
            - Deleted property: cpu_microarchitecture
            - Deleted property: path

GET /api/marketplace-software-versions/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: catalog_type
              - New required property: dependencies
              - New required property: metadata
            - Properties changed
              - New property: catalog_type
              - New property: dependencies
              - New property: metadata

POST /api/marketplace-software-versions/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: catalog_type
            - New required property: dependencies
            - New required property: metadata
          - Properties changed
            - New property: catalog_type
            - New property: dependencies
            - New property: metadata

GET /api/marketplace-software-versions/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: catalog_type
            - New required property: dependencies
            - New required property: metadata
          - Properties changed
            - New property: catalog_type
            - New property: dependencies
            - New property: metadata

PATCH /api/marketplace-software-versions/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: catalog_type
            - New required property: dependencies
            - New required property: metadata
          - Properties changed
            - New property: catalog_type
            - New property: dependencies
            - New property: metadata

PUT /api/marketplace-software-versions/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: catalog_type
            - New required property: dependencies
            - New required property: metadata
          - Properties changed
            - New property: catalog_type
            - New property: dependencies
            - New property: metadata

GET /api/metadata/events/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_groups
              - AdditionalProperties changed
                - Items changed
                  - New enum values: [user_invitation_updated user_invitation_deleted]

GET /api/onboarding-verifications/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: validation_method
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/ValidationMethodEnum
                    - New enum values: [breg]

POST /api/onboarding-verifications/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: validation_method
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/ValidationMethodEnum
                  - New enum values: [breg]

POST /api/onboarding-verifications/start_verification/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: validation_method
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/ValidationMethodEnum
                  - New enum values: [breg]

GET /api/onboarding-verifications/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: validation_method
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/ValidationMethodEnum
                  - New enum values: [breg]

PATCH /api/onboarding-verifications/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: validation_method
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/ValidationMethodEnum
                  - New enum values: [breg]

PUT /api/onboarding-verifications/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: validation_method
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/ValidationMethodEnum
                  - New enum values: [breg]

POST /api/onboarding-verifications/{uuid}/run_validation/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: validation_method
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/ValidationMethodEnum
                  - New enum values: [breg]

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
                            - New property: billing_type_classification
                            - Modified property: plugin_options
                              - Property 'AllOf' changed
                                - Modified schema: #/components/schemas/MergedPluginOptions
                                  - Properties changed
                                    - New property: auto_approve_marketplace_script
                                    - New property: can_restore_resource
                            - Modified property: state
                              - Property 'AllOf' changed
                                - Modified schema: #/components/schemas/OfferingState
                                  - New enum values: [Unavailable]

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
                          - New property: billing_type_classification
                          - Modified property: plugin_options
                            - Property 'AllOf' changed
                              - Modified schema: #/components/schemas/MergedPluginOptions
                                - Properties changed
                                  - New property: auto_approve_marketplace_script
                                  - New property: can_restore_resource
                          - Modified property: state
                            - Property 'AllOf' changed
                              - Modified schema: #/components/schemas/OfferingState
                                - New enum values: [Unavailable]

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
                    - New property: billing_type_classification
                    - Modified property: plugin_options
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/MergedPluginOptions
                          - Properties changed
                            - New property: auto_approve_marketplace_script
                            - New property: can_restore_resource
                    - Modified property: state
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/OfferingState
                          - New enum values: [Unavailable]

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
                  - New property: billing_type_classification
                  - Modified property: plugin_options
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/MergedPluginOptions
                        - Properties changed
                          - New property: auto_approve_marketplace_script
                          - New property: can_restore_resource
                  - Modified property: state
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/OfferingState
                        - New enum values: [Unavailable]

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
                  - New property: billing_type_classification
                  - Modified property: plugin_options
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/MergedPluginOptions
                        - Properties changed
                          - New property: auto_approve_marketplace_script
                          - New property: can_restore_resource
                  - Modified property: state
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/OfferingState
                        - New enum values: [Unavailable]

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
                  - New property: billing_type_classification
                  - Modified property: plugin_options
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/MergedPluginOptions
                        - Properties changed
                          - New property: auto_approve_marketplace_script
                          - New property: can_restore_resource
                  - Modified property: state
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/OfferingState
                        - New enum values: [Unavailable]

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
                  - New property: billing_type_classification
                  - Modified property: plugin_options
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/MergedPluginOptions
                        - Properties changed
                          - New property: auto_approve_marketplace_script
                          - New property: can_restore_resource
                  - Modified property: state
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/OfferingState
                        - New enum values: [Unavailable]

GET /api/override-settings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: ONBOARDING_BREG_API_URL
            - New property: SOFTWARE_CATALOG_CLEANUP_ENABLED
            - New property: SOFTWARE_CATALOG_EESSI_API_URL
            - New property: SOFTWARE_CATALOG_EESSI_INCLUDE_EXTENSIONS
            - New property: SOFTWARE_CATALOG_EESSI_UPDATE_ENABLED
            - New property: SOFTWARE_CATALOG_EESSI_VERSION
            - New property: SOFTWARE_CATALOG_RETENTION_DAYS
            - New property: SOFTWARE_CATALOG_SPACK_DATA_URL
            - New property: SOFTWARE_CATALOG_SPACK_UPDATE_ENABLED
            - New property: SOFTWARE_CATALOG_SPACK_VERSION
            - New property: SOFTWARE_CATALOG_UPDATE_EXISTING_PACKAGES

POST /api/override-settings/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: ONBOARDING_BREG_API_URL
          - New property: SOFTWARE_CATALOG_CLEANUP_ENABLED
          - New property: SOFTWARE_CATALOG_EESSI_API_URL
          - New property: SOFTWARE_CATALOG_EESSI_INCLUDE_EXTENSIONS
          - New property: SOFTWARE_CATALOG_EESSI_UPDATE_ENABLED
          - New property: SOFTWARE_CATALOG_EESSI_VERSION
          - New property: SOFTWARE_CATALOG_RETENTION_DAYS
          - New property: SOFTWARE_CATALOG_SPACK_DATA_URL
          - New property: SOFTWARE_CATALOG_SPACK_UPDATE_ENABLED
          - New property: SOFTWARE_CATALOG_SPACK_VERSION
          - New property: SOFTWARE_CATALOG_UPDATE_EXISTING_PACKAGES
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: ONBOARDING_BREG_API_URL
          - New property: SOFTWARE_CATALOG_CLEANUP_ENABLED
          - New property: SOFTWARE_CATALOG_EESSI_API_URL
          - New property: SOFTWARE_CATALOG_EESSI_INCLUDE_EXTENSIONS
          - New property: SOFTWARE_CATALOG_EESSI_UPDATE_ENABLED
          - New property: SOFTWARE_CATALOG_EESSI_VERSION
          - New property: SOFTWARE_CATALOG_RETENTION_DAYS
          - New property: SOFTWARE_CATALOG_SPACK_DATA_URL
          - New property: SOFTWARE_CATALOG_SPACK_UPDATE_ENABLED
          - New property: SOFTWARE_CATALOG_SPACK_VERSION
          - New property: SOFTWARE_CATALOG_UPDATE_EXISTING_PACKAGES
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: ONBOARDING_BREG_API_URL
          - New property: SOFTWARE_CATALOG_CLEANUP_ENABLED
          - New property: SOFTWARE_CATALOG_EESSI_API_URL
          - New property: SOFTWARE_CATALOG_EESSI_INCLUDE_EXTENSIONS
          - New property: SOFTWARE_CATALOG_EESSI_UPDATE_ENABLED
          - New property: SOFTWARE_CATALOG_EESSI_VERSION
          - New property: SOFTWARE_CATALOG_RETENTION_DAYS
          - New property: SOFTWARE_CATALOG_SPACK_DATA_URL
          - New property: SOFTWARE_CATALOG_SPACK_UPDATE_ENABLED
          - New property: SOFTWARE_CATALOG_SPACK_VERSION
          - New property: SOFTWARE_CATALOG_UPDATE_EXISTING_PACKAGES

GET /api/project-credits/

- New query param: query

HEAD /api/project-credits/

- New query param: query

GET /api/promotions-campaigns/{uuid}/orders/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [order_subtype]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: order_subtype
              - Modified property: old_cost_estimate
                - Type changed from 'string' to 'number'
                - Format changed from 'decimal' to 'double'
                - Nullable changed from true to false
                - Pattern changed from '^-?\d{0,12}(?:\.\d{0,10})?$' to ''
              - Modified property: type
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/RequestTypes
                    - New enum values: [Restore]

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
                      - New property: order_subtype
                      - Modified property: old_cost_estimate
                        - Type changed from 'string' to 'number'
                        - Format changed from 'decimal' to 'double'
                        - Nullable changed from true to false
                        - Pattern changed from '^-?\d{0,12}(?:\.\d{0,10})?$' to ''
                      - Modified property: type
                        - Property 'AllOf' changed
                          - Modified schema: #/components/schemas/RequestTypes
                            - New enum values: [Restore]
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: order_subtype
                      - Modified property: old_cost_estimate
                        - Type changed from 'string' to 'number'
                        - Format changed from 'decimal' to 'double'
                        - Nullable changed from true to false
                        - Pattern changed from '^-?\d{0,12}(?:\.\d{0,10})?$' to ''
                      - Modified property: type
                        - Property 'AllOf' changed
                          - Modified schema: #/components/schemas/RequestTypes
                            - New enum values: [Restore]

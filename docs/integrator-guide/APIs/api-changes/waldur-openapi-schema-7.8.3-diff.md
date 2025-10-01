# OpenAPI schema diff - 7.8.3

## For version 7.8.3

### New Endpoints: 5

--------------------
GET /api/marketplace-service-providers/{service_provider_uuid}/compliance/checklists_summary/  
POST /api/openstack-network-rbac-policies/  
DELETE /api/openstack-network-rbac-policies/{uuid}/  
PATCH /api/openstack-network-rbac-policies/{uuid}/  
PUT /api/openstack-network-rbac-policies/{uuid}/  

### Deleted Endpoints: None

---------------------------

### Modified Endpoints: 93

--------------------------
POST /api/backend-resources/{uuid}/import_resource/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: provider_slug
            - Deleted property: offering_customer_name
            - Deleted property: offering_customer_slug
            - Deleted property: offering_customer_uuid
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: provider_slug
                    - Deleted property: offering_customer_name
                    - Deleted property: offering_customer_slug
                    - Deleted property: offering_customer_uuid
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: provider_slug
                    - Deleted property: offering_customer_name
                    - Deleted property: offering_customer_slug
                    - Deleted property: offering_customer_uuid

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
                      - New property: conceal_billing_data

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
                    - New property: conceal_billing_data

GET /api/booking-resources/

- New query param: plan_uuid
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [provider_slug]
      - Deleted enum values: [offering_customer_name offering_customer_slug offering_customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: provider_slug
              - Deleted property: offering_customer_name
              - Deleted property: offering_customer_slug
              - Deleted property: offering_customer_uuid
              - Modified property: creation_order
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: provider_slug
                      - Deleted property: offering_customer_name
                      - Deleted property: offering_customer_slug
                      - Deleted property: offering_customer_uuid
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: provider_slug
                      - Deleted property: offering_customer_name
                      - Deleted property: offering_customer_slug
                      - Deleted property: offering_customer_uuid

HEAD /api/booking-resources/

- New query param: plan_uuid

GET /api/booking-resources/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [provider_slug]
      - Deleted enum values: [offering_customer_name offering_customer_slug offering_customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: provider_slug
            - Deleted property: offering_customer_name
            - Deleted property: offering_customer_slug
            - Deleted property: offering_customer_uuid
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: provider_slug
                    - Deleted property: offering_customer_name
                    - Deleted property: offering_customer_slug
                    - Deleted property: offering_customer_uuid
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: provider_slug
                    - Deleted property: offering_customer_name
                    - Deleted property: offering_customer_slug
                    - Deleted property: offering_customer_uuid

GET /api/hooks-email/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: event_groups
                - Items changed
                  - New enum values: [terms_of_service]
              - Modified property: event_types
                - Items changed
                  - New enum values: [terms_of_service_consent_granted terms_of_service_consent_revoked]

POST /api/hooks-email/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_groups
            - Items changed
              - New enum values: [terms_of_service]
          - Modified property: event_types
            - Items changed
              - New enum values: [terms_of_service_consent_granted terms_of_service_consent_revoked]
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_groups
              - Items changed
                - New enum values: [terms_of_service]
            - Modified property: event_types
              - Items changed
                - New enum values: [terms_of_service_consent_granted terms_of_service_consent_revoked]

GET /api/hooks-email/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_groups
              - Items changed
                - New enum values: [terms_of_service]
            - Modified property: event_types
              - Items changed
                - New enum values: [terms_of_service_consent_granted terms_of_service_consent_revoked]

PATCH /api/hooks-email/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_groups
            - Items changed
              - New enum values: [terms_of_service]
          - Modified property: event_types
            - Items changed
              - New enum values: [terms_of_service_consent_granted terms_of_service_consent_revoked]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_groups
              - Items changed
                - New enum values: [terms_of_service]
            - Modified property: event_types
              - Items changed
                - New enum values: [terms_of_service_consent_granted terms_of_service_consent_revoked]

PUT /api/hooks-email/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_groups
            - Items changed
              - New enum values: [terms_of_service]
          - Modified property: event_types
            - Items changed
              - New enum values: [terms_of_service_consent_granted terms_of_service_consent_revoked]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_groups
              - Items changed
                - New enum values: [terms_of_service]
            - Modified property: event_types
              - Items changed
                - New enum values: [terms_of_service_consent_granted terms_of_service_consent_revoked]

GET /api/hooks-web/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: event_groups
                - Items changed
                  - New enum values: [terms_of_service]
              - Modified property: event_types
                - Items changed
                  - New enum values: [terms_of_service_consent_granted terms_of_service_consent_revoked]

POST /api/hooks-web/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_groups
            - Items changed
              - New enum values: [terms_of_service]
          - Modified property: event_types
            - Items changed
              - New enum values: [terms_of_service_consent_granted terms_of_service_consent_revoked]
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_groups
              - Items changed
                - New enum values: [terms_of_service]
            - Modified property: event_types
              - Items changed
                - New enum values: [terms_of_service_consent_granted terms_of_service_consent_revoked]

GET /api/hooks-web/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_groups
              - Items changed
                - New enum values: [terms_of_service]
            - Modified property: event_types
              - Items changed
                - New enum values: [terms_of_service_consent_granted terms_of_service_consent_revoked]

PATCH /api/hooks-web/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_groups
            - Items changed
              - New enum values: [terms_of_service]
          - Modified property: event_types
            - Items changed
              - New enum values: [terms_of_service_consent_granted terms_of_service_consent_revoked]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_groups
              - Items changed
                - New enum values: [terms_of_service]
            - Modified property: event_types
              - Items changed
                - New enum values: [terms_of_service_consent_granted terms_of_service_consent_revoked]

PUT /api/hooks-web/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_groups
            - Items changed
              - New enum values: [terms_of_service]
          - Modified property: event_types
            - Items changed
              - New enum values: [terms_of_service_consent_granted terms_of_service_consent_revoked]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_groups
              - Items changed
                - New enum values: [terms_of_service]
            - Modified property: event_types
              - Items changed
                - New enum values: [terms_of_service_consent_granted terms_of_service_consent_revoked]

GET /api/managed-rancher-cluster-resources/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [provider_slug]
      - Deleted enum values: [offering_customer_name offering_customer_slug offering_customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: provider_slug
              - Deleted property: offering_customer_name
              - Deleted property: offering_customer_slug
              - Deleted property: offering_customer_uuid
              - Modified property: creation_order
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: provider_slug
                      - Deleted property: offering_customer_name
                      - Deleted property: offering_customer_slug
                      - Deleted property: offering_customer_uuid
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: provider_slug
                      - Deleted property: offering_customer_name
                      - Deleted property: offering_customer_slug
                      - Deleted property: offering_customer_uuid

GET /api/managed-rancher-cluster-resources/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [provider_slug]
      - Deleted enum values: [offering_customer_name offering_customer_slug offering_customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: provider_slug
            - Deleted property: offering_customer_name
            - Deleted property: offering_customer_slug
            - Deleted property: offering_customer_uuid
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: provider_slug
                    - Deleted property: offering_customer_name
                    - Deleted property: offering_customer_slug
                    - Deleted property: offering_customer_uuid
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: provider_slug
                    - Deleted property: offering_customer_name
                    - Deleted property: offering_customer_slug
                    - Deleted property: offering_customer_uuid

GET /api/marketplace-orders/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [provider_slug]
      - Deleted enum values: [offering_customer_name offering_customer_slug offering_customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: provider_slug
              - Deleted property: offering_customer_name
              - Deleted property: offering_customer_slug
              - Deleted property: offering_customer_uuid

POST /api/marketplace-orders/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: attributes
            - Property 'OneOf' changed
              - Modified schema: #/components/schemas/AzureVirtualMachineCreateOrderAttributes
                - Description changed from 'This mixin allows to specify list of fields to be rendered by serializer.
It expects that request is available in serializer's context.

It is disabled for nested serializers (where parent is another serializer)
but remains active for list views (where parent is a ListSerializer).' to ''
              - Modified schema: #/components/schemas/AzureSQLServerCreateOrderAttributes
                - Description changed from 'This mixin allows to specify list of fields to be rendered by serializer.
It expects that request is available in serializer's context.

It is disabled for nested serializers (where parent is another serializer)
but remains active for list views (where parent is a ListSerializer).' to ''
              - Modified schema: #/components/schemas/OpenStackTenantCreateOrderAttributes
                - Description changed from 'This mixin allows to specify list of fields to be rendered by serializer.
It expects that request is available in serializer's context.

It is disabled for nested serializers (where parent is another serializer)
but remains active for list views (where parent is a ListSerializer).' to ''
              - Modified schema: #/components/schemas/OpenStackInstanceCreateOrderAttributes
                - Description changed from 'This mixin allows to specify list of fields to be rendered by serializer.
It expects that request is available in serializer's context.

It is disabled for nested serializers (where parent is another serializer)
but remains active for list views (where parent is a ListSerializer).' to ''
                - Properties changed
                  - New property: server_group
                  - Modified property: floating_ips
                    - WriteOnly changed from false to true
                    - Items changed
                      - Properties changed
                        - New property: url
                  - Modified property: ports
                    - WriteOnly changed from false to true
                    - Items changed
                      - Properties changed
                        - Modified property: port
                          - WriteOnly changed from true to false
                  - Modified property: security_groups
                    - Description changed from 'Security groups to attach to the instance' to 'List of security groups to apply to the instance'
                    - WriteOnly changed from false to true
                    - Items changed
                      - Required changed
                        - New required property: url
              - Modified schema: #/components/schemas/OpenStackVolumeCreateOrderAttributes
                - Description changed from 'This mixin allows to specify list of fields to be rendered by serializer.
It expects that request is available in serializer's context.

It is disabled for nested serializers (where parent is another serializer)
but remains active for list views (where parent is a ListSerializer).' to ''
              - Modified schema: #/components/schemas/SlurmInvoicesSlurmPackageCreateOrderAttributes
                - Description changed from 'This mixin allows to specify list of fields to be rendered by serializer.
It expects that request is available in serializer's context.

It is disabled for nested serializers (where parent is another serializer)
but remains active for list views (where parent is a ListSerializer).' to ''
              - Modified schema: #/components/schemas/VMwareVirtualMachineCreateOrderAttributes
                - Description changed from 'This mixin allows to specify list of fields to be rendered by serializer.
It expects that request is available in serializer's context.

It is disabled for nested serializers (where parent is another serializer)
but remains active for list views (where parent is a ListSerializer).' to ''
              - Modified schema: #/components/schemas/GenericOrderAttributes
                - Description changed from 'A generic JSON object for offerings without a predefined schema. Allows any key-value pairs.' to ''

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: provider_slug
          - Properties changed
            - New property: provider_slug

GET /api/marketplace-orders/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [provider_slug]
      - Deleted enum values: [offering_customer_name offering_customer_slug offering_customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: provider_slug
            - Deleted property: offering_customer_name
            - Deleted property: offering_customer_slug
            - Deleted property: offering_customer_uuid

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
                    - New property: conceal_billing_data

GET /api/marketplace-project-update-requests/

- New query param: provider_uuid
- Deleted query param: offering_customer_uuid

HEAD /api/marketplace-project-update-requests/

- New query param: provider_uuid
- Deleted query param: offering_customer_uuid

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
                      - New property: conceal_billing_data

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
                    - New property: conceal_billing_data

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
                    - New property: conceal_billing_data

POST /api/marketplace-provider-offerings/{uuid}/import_resource/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: provider_slug
            - Deleted property: offering_customer_name
            - Deleted property: offering_customer_slug
            - Deleted property: offering_customer_uuid
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: provider_slug
                    - Deleted property: offering_customer_name
                    - Deleted property: offering_customer_slug
                    - Deleted property: offering_customer_uuid
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: provider_slug
                    - Deleted property: offering_customer_name
                    - Deleted property: offering_customer_slug
                    - Deleted property: offering_customer_uuid

GET /api/marketplace-provider-offerings/{uuid}/list_course_accounts/

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
                    - New property: conceal_billing_data

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
                    - New property: conceal_billing_data

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
                    - New property: conceal_billing_data

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
                    - New property: conceal_billing_data

GET /api/marketplace-provider-offerings/{uuid}/orders/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: provider_slug
              - Deleted property: offering_customer_name
              - Deleted property: offering_customer_slug
              - Deleted property: offering_customer_uuid

GET /api/marketplace-provider-offerings/{uuid}/orders/{order_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: provider_slug
            - Deleted property: offering_customer_name
            - Deleted property: offering_customer_slug
            - Deleted property: offering_customer_uuid

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
                    - New property: conceal_billing_data

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
                    - New property: conceal_billing_data

POST /api/marketplace-provider-offerings/{uuid}/update_integration/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: plugin_options
            - Properties changed
              - New property: conceal_billing_data

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
                    - New property: conceal_billing_data

GET /api/marketplace-provider-resources/

- New query param: plan_uuid
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [provider_slug]
      - Deleted enum values: [offering_customer_name offering_customer_slug offering_customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: provider_slug
              - Deleted property: offering_customer_name
              - Deleted property: offering_customer_slug
              - Deleted property: offering_customer_uuid
              - Modified property: creation_order
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: provider_slug
                      - Deleted property: offering_customer_name
                      - Deleted property: offering_customer_slug
                      - Deleted property: offering_customer_uuid
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: provider_slug
                      - Deleted property: offering_customer_name
                      - Deleted property: offering_customer_slug
                      - Deleted property: offering_customer_uuid

HEAD /api/marketplace-provider-resources/

- New query param: plan_uuid

GET /api/marketplace-provider-resources/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [provider_slug]
      - Deleted enum values: [offering_customer_name offering_customer_slug offering_customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: provider_slug
            - Deleted property: offering_customer_name
            - Deleted property: offering_customer_slug
            - Deleted property: offering_customer_uuid
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: provider_slug
                    - Deleted property: offering_customer_name
                    - Deleted property: offering_customer_slug
                    - Deleted property: offering_customer_uuid
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: provider_slug
                    - Deleted property: offering_customer_name
                    - Deleted property: offering_customer_slug
                    - Deleted property: offering_customer_uuid

GET /api/marketplace-provider-resources/{uuid}/details/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [provider_slug]
      - Deleted enum values: [offering_customer_name offering_customer_slug offering_customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: provider_slug
            - Deleted property: offering_customer_name
            - Deleted property: offering_customer_slug
            - Deleted property: offering_customer_uuid
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: provider_slug
                    - Deleted property: offering_customer_name
                    - Deleted property: offering_customer_slug
                    - Deleted property: offering_customer_uuid
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: provider_slug
                    - Deleted property: offering_customer_name
                    - Deleted property: offering_customer_slug
                    - Deleted property: offering_customer_uuid

POST /api/marketplace-provider-resources/{uuid}/move_resource/

- Request body changed
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: provider_slug
            - Deleted property: offering_customer_name
            - Deleted property: offering_customer_slug
            - Deleted property: offering_customer_uuid
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: provider_slug
                    - Deleted property: offering_customer_name
                    - Deleted property: offering_customer_slug
                    - Deleted property: offering_customer_uuid
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: provider_slug
                    - Deleted property: offering_customer_name
                    - Deleted property: offering_customer_slug
                    - Deleted property: offering_customer_uuid

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
                    - New property: conceal_billing_data

POST /api/marketplace-provider-resources/{uuid}/set_end_date_by_provider/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: provider_slug
            - Deleted property: offering_customer_name
            - Deleted property: offering_customer_slug
            - Deleted property: offering_customer_uuid
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: provider_slug
                    - Deleted property: offering_customer_name
                    - Deleted property: offering_customer_slug
                    - Deleted property: offering_customer_uuid
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: provider_slug
                    - Deleted property: offering_customer_name
                    - Deleted property: offering_customer_slug
                    - Deleted property: offering_customer_uuid

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
                      - New property: conceal_billing_data

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
                    - New property: conceal_billing_data

GET /api/marketplace-resources/

- New query param: plan_uuid
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [provider_slug]
      - Deleted enum values: [offering_customer_name offering_customer_slug offering_customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: provider_slug
              - Deleted property: offering_customer_name
              - Deleted property: offering_customer_slug
              - Deleted property: offering_customer_uuid
              - Modified property: creation_order
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: provider_slug
                      - Deleted property: offering_customer_name
                      - Deleted property: offering_customer_slug
                      - Deleted property: offering_customer_uuid
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: provider_slug
                      - Deleted property: offering_customer_name
                      - Deleted property: offering_customer_slug
                      - Deleted property: offering_customer_uuid

HEAD /api/marketplace-resources/

- New query param: plan_uuid

GET /api/marketplace-resources/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [provider_slug]
      - Deleted enum values: [offering_customer_name offering_customer_slug offering_customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: provider_slug
            - Deleted property: offering_customer_name
            - Deleted property: offering_customer_slug
            - Deleted property: offering_customer_uuid
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: provider_slug
                    - Deleted property: offering_customer_name
                    - Deleted property: offering_customer_slug
                    - Deleted property: offering_customer_uuid
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: provider_slug
                    - Deleted property: offering_customer_name
                    - Deleted property: offering_customer_slug
                    - Deleted property: offering_customer_uuid

GET /api/marketplace-resources/{uuid}/details/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [provider_slug]
      - Deleted enum values: [offering_customer_name offering_customer_slug offering_customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: provider_slug
            - Deleted property: offering_customer_name
            - Deleted property: offering_customer_slug
            - Deleted property: offering_customer_uuid
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: provider_slug
                    - Deleted property: offering_customer_name
                    - Deleted property: offering_customer_slug
                    - Deleted property: offering_customer_uuid
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: provider_slug
                    - Deleted property: offering_customer_name
                    - Deleted property: offering_customer_slug
                    - Deleted property: offering_customer_uuid

POST /api/marketplace-resources/{uuid}/move_resource/

- Request body changed
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: provider_slug
            - Deleted property: offering_customer_name
            - Deleted property: offering_customer_slug
            - Deleted property: offering_customer_uuid
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: provider_slug
                    - Deleted property: offering_customer_name
                    - Deleted property: offering_customer_slug
                    - Deleted property: offering_customer_uuid
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: provider_slug
                    - Deleted property: offering_customer_name
                    - Deleted property: offering_customer_slug
                    - Deleted property: offering_customer_uuid

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
                    - New property: conceal_billing_data

GET /api/marketplace-robot-accounts/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [provider_name provider_uuid]
      - Deleted enum values: [offering_customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: provider_name
              - New property: provider_uuid
              - Deleted property: offering_customer_uuid
              - Modified property: offering_plugin_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedPluginOptions
                    - Properties changed
                      - New property: conceal_billing_data

GET /api/marketplace-robot-accounts/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [provider_name provider_uuid]
      - Deleted enum values: [offering_customer_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: provider_name
            - New property: provider_uuid
            - Deleted property: offering_customer_uuid
            - Modified property: offering_plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: conceal_billing_data

POST /api/marketplace-robot-accounts/{uuid}/set_state_creating/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: provider_name
            - New property: provider_uuid
            - Deleted property: offering_customer_uuid
            - Modified property: offering_plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: conceal_billing_data

POST /api/marketplace-robot-accounts/{uuid}/set_state_deleted/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: provider_name
            - New property: provider_uuid
            - Deleted property: offering_customer_uuid
            - Modified property: offering_plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: conceal_billing_data

POST /api/marketplace-robot-accounts/{uuid}/set_state_erred/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: provider_name
            - New property: provider_uuid
            - Deleted property: offering_customer_uuid
            - Modified property: offering_plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: conceal_billing_data

POST /api/marketplace-robot-accounts/{uuid}/set_state_ok/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: provider_name
            - New property: provider_uuid
            - Deleted property: offering_customer_uuid
            - Modified property: offering_plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: conceal_billing_data

POST /api/marketplace-robot-accounts/{uuid}/set_state_request_deletion/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: provider_name
            - New property: provider_uuid
            - Deleted property: offering_customer_uuid
            - Modified property: offering_plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: conceal_billing_data

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
                    - New property: conceal_billing_data

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
                    - New property: conceal_billing_data

GET /api/openstack-backups/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: restorations
                - Items changed
                  - Properties changed
                    - Modified property: floating_ips
                      - Description changed from 'Floating IPs that will be assigned to the restored instance' to ''
                    - Modified property: ports
                      - Description changed from 'Network ports that will be attached to the restored instance' to ''
                    - Modified property: security_groups
                      - Description changed from 'Security groups that will be assigned to the restored instance' to ''

GET /api/openstack-backups/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: restorations
              - Items changed
                - Properties changed
                  - Modified property: floating_ips
                    - Description changed from 'Floating IPs that will be assigned to the restored instance' to ''
                  - Modified property: ports
                    - Description changed from 'Network ports that will be attached to the restored instance' to ''
                  - Modified property: security_groups
                    - Description changed from 'Security groups that will be assigned to the restored instance' to ''

PATCH /api/openstack-backups/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: restorations
              - Items changed
                - Properties changed
                  - Modified property: floating_ips
                    - Description changed from 'Floating IPs that will be assigned to the restored instance' to ''
                  - Modified property: ports
                    - Description changed from 'Network ports that will be attached to the restored instance' to ''
                  - Modified property: security_groups
                    - Description changed from 'Security groups that will be assigned to the restored instance' to ''

PUT /api/openstack-backups/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: restorations
              - Items changed
                - Properties changed
                  - Modified property: floating_ips
                    - Description changed from 'Floating IPs that will be assigned to the restored instance' to ''
                  - Modified property: ports
                    - Description changed from 'Network ports that will be attached to the restored instance' to ''
                  - Modified property: security_groups
                    - Description changed from 'Security groups that will be assigned to the restored instance' to ''

POST /api/openstack-backups/{uuid}/restore/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: security_groups
          - Modified property: floating_ips
            - Items changed
              - Properties changed
                - New property: url
          - Modified property: ports
            - Items changed
              - Properties changed
                - Modified property: port
                  - WriteOnly changed from true to false
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: floating_ips
              - Description changed from 'Floating IPs to assign to the instance' to ''
            - Modified property: ports
              - Description changed from 'Network ports to attach to the instance' to ''
            - Modified property: security_groups
              - Description changed from 'List of security groups to apply to the instance' to ''
            - Modified property: server_group
              - Property 'AllOf' changed
                - Schemas deleted: #/components/schemas/OpenStackNestedServerGroup
              - Type changed from '' to 'object'
              - Description changed from 'Server group for instance scheduling policy' to ''
              - Nullable changed from true to false
              - Properties changed
                - New property: name
                - New property: policy
                - New property: state
                - New property: url

GET /api/openstack-instances/

- Modified query param: field
  - Schema changed
    - Items changed
      - Deleted enum values: [data_volume_size data_volume_type data_volumes flavor image system_volume_size system_volume_type]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: floating_ips
                - Description changed from 'Floating IPs to assign to the instance' to ''
              - Modified property: ports
                - Description changed from 'Network ports to attach to the instance' to ''
              - Modified property: security_groups
                - Description changed from 'List of security groups to apply to the instance' to ''
              - Modified property: server_group
                - Property 'AllOf' changed
                  - Schemas deleted: #/components/schemas/OpenStackNestedServerGroup
                - Type changed from '' to 'object'
                - Description changed from 'Server group for instance scheduling policy' to ''
                - Nullable changed from true to false
                - Properties changed
                  - New property: name
                  - New property: policy
                  - New property: state
                  - New property: url

GET /api/openstack-instances/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - Deleted enum values: [data_volume_size data_volume_type data_volumes flavor image system_volume_size system_volume_type]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: floating_ips
              - Description changed from 'Floating IPs to assign to the instance' to ''
            - Modified property: ports
              - Description changed from 'Network ports to attach to the instance' to ''
            - Modified property: security_groups
              - Description changed from 'List of security groups to apply to the instance' to ''
            - Modified property: server_group
              - Property 'AllOf' changed
                - Schemas deleted: #/components/schemas/OpenStackNestedServerGroup
              - Type changed from '' to 'object'
              - Description changed from 'Server group for instance scheduling policy' to ''
              - Nullable changed from true to false
              - Properties changed
                - New property: name
                - New property: policy
                - New property: state
                - New property: url

PATCH /api/openstack-instances/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Deleted property: data_volume_type
          - Deleted property: data_volumes
          - Deleted property: system_volume_type
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: floating_ips
              - Description changed from 'Floating IPs to assign to the instance' to ''
            - Modified property: ports
              - Description changed from 'Network ports to attach to the instance' to ''
            - Modified property: security_groups
              - Description changed from 'List of security groups to apply to the instance' to ''
            - Modified property: server_group
              - Property 'AllOf' changed
                - Schemas deleted: #/components/schemas/OpenStackNestedServerGroup
              - Type changed from '' to 'object'
              - Description changed from 'Server group for instance scheduling policy' to ''
              - Nullable changed from true to false
              - Properties changed
                - New property: name
                - New property: policy
                - New property: state
                - New property: url

PUT /api/openstack-instances/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Deleted property: data_volume_type
          - Deleted property: data_volumes
          - Deleted property: system_volume_type
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: floating_ips
              - Description changed from 'Floating IPs to assign to the instance' to ''
            - Modified property: ports
              - Description changed from 'Network ports to attach to the instance' to ''
            - Modified property: security_groups
              - Description changed from 'List of security groups to apply to the instance' to ''
            - Modified property: server_group
              - Property 'AllOf' changed
                - Schemas deleted: #/components/schemas/OpenStackNestedServerGroup
              - Type changed from '' to 'object'
              - Description changed from 'Server group for instance scheduling policy' to ''
              - Nullable changed from true to false
              - Properties changed
                - New property: name
                - New property: policy
                - New property: state
                - New property: url

POST /api/openstack-instances/{uuid}/backup/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: restorations
              - Items changed
                - Properties changed
                  - Modified property: floating_ips
                    - Description changed from 'Floating IPs that will be assigned to the restored instance' to ''
                  - Modified property: ports
                    - Description changed from 'Network ports that will be attached to the restored instance' to ''
                  - Modified property: security_groups
                    - Description changed from 'Security groups that will be assigned to the restored instance' to ''

POST /api/openstack-instances/{uuid}/update_floating_ips/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: floating_ips
            - Items changed
              - Properties changed
                - New property: url

POST /api/openstack-instances/{uuid}/update_ports/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: ports
            - Items changed
              - Properties changed
                - Modified property: port
                  - WriteOnly changed from true to false

GET /api/openstack-network-rbac-policies/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: network
                - ReadOnly changed from true to false

GET /api/openstack-network-rbac-policies/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: network
              - ReadOnly changed from true to false

GET /api/openstack-networks/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: rbac_policies
                - Items changed
                  - Properties changed
                    - Modified property: network
                      - ReadOnly changed from true to false

GET /api/openstack-networks/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: rbac_policies
              - Items changed
                - Properties changed
                  - Modified property: network
                    - ReadOnly changed from true to false

PATCH /api/openstack-networks/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: rbac_policies
              - Items changed
                - Properties changed
                  - Modified property: network
                    - ReadOnly changed from true to false

PUT /api/openstack-networks/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: rbac_policies
              - Items changed
                - Properties changed
                  - Modified property: network
                    - ReadOnly changed from true to false

POST /api/openstack-networks/{uuid}/rbac_policy_create/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Required changed
          - New required property: network
        - Properties changed
          - New property: network
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: network
              - ReadOnly changed from true to false

POST /api/openstack-tenants/{uuid}/create_network/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: rbac_policies
              - Items changed
                - Properties changed
                  - Modified property: network
                    - ReadOnly changed from true to false

GET /api/override-settings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: OIDC_ACCESS_TOKEN_ENABLED

POST /api/override-settings/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: OIDC_ACCESS_TOKEN_ENABLED
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: OIDC_ACCESS_TOKEN_ENABLED
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: OIDC_ACCESS_TOKEN_ENABLED

GET /api/promotions-campaigns/{uuid}/orders/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: provider_slug
              - Deleted property: offering_customer_name
              - Deleted property: offering_customer_slug
              - Deleted property: offering_customer_uuid

GET /api/promotions-campaigns/{uuid}/resources/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: provider_slug
              - Deleted property: offering_customer_name
              - Deleted property: offering_customer_slug
              - Deleted property: offering_customer_uuid
              - Modified property: creation_order
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: provider_slug
                      - Deleted property: offering_customer_name
                      - Deleted property: offering_customer_slug
                      - Deleted property: offering_customer_uuid
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: provider_slug
                      - Deleted property: offering_customer_name
                      - Deleted property: offering_customer_slug
                      - Deleted property: offering_customer_uuid

GET /api/rancher-clusters/

- Modified query param: field
  - Schema changed
    - Items changed
      - Deleted enum values: [security_groups]

GET /api/rancher-clusters/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - Deleted enum values: [security_groups]

POST /api/rancher-services/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: target_workloads
            - Items changed
              - Required changed
                - New required property: url
                - Deleted required property: name
              - Properties changed
                - New property: url
                - Deleted property: name
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: access_url
            - New required property: created
            - New required property: customer
            - New required property: customer_abbreviation
            - New required property: customer_name
            - New required property: customer_native_name
            - New required property: is_limit_based
            - New required property: is_usage_based
            - New required property: marketplace_category_name
            - New required property: marketplace_category_uuid
            - New required property: marketplace_offering_name
            - New required property: marketplace_offering_plugin_options
            - New required property: marketplace_offering_uuid
            - New required property: marketplace_plan_uuid
            - New required property: marketplace_resource_state
            - New required property: marketplace_resource_uuid
            - New required property: modified
            - New required property: name
            - New required property: namespace_name
            - New required property: project
            - New required property: project_name
            - New required property: project_uuid
            - New required property: resource_type
            - New required property: service_name
            - New required property: service_settings
            - New required property: service_settings_error_message
            - New required property: service_settings_state
            - New required property: service_settings_uuid
            - New required property: state
            - New required property: url
            - New required property: uuid
          - Properties changed
            - Modified property: target_workloads
              - Items changed
                - Required changed
                  - New required property: url
                - Properties changed
                  - Deleted property: name
                  - Deleted property: uuid
                  - Modified property: url
                    - ReadOnly changed from true to false

PUT /api/rancher-services/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Required changed
          - New required property: target_workloads

PUT /api/rancher-services/{uuid}/yaml/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Required changed
          - New required property: target_workloads

POST /api/vmware-virtual-machine/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: networks
            - Items changed
              - Required changed
                - New required property: url
                - Deleted required property: name
                - Deleted required property: type
              - Properties changed
                - New property: url
                - Deleted property: name
                - Deleted property: type

PUT /api/vmware-virtual-machine/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: networks
            - Items changed
              - Required changed
                - New required property: url
                - Deleted required property: name
                - Deleted required property: type
              - Properties changed
                - New property: url
                - Deleted property: name
                - Deleted property: type

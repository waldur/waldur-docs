# OpenAPI schema diff - 7.7.7

## For version 7.7.7

### New Endpoints: 26

---------------------
GET /api/customers/{customer_uuid}/project-metadata-compliance-details/  
GET /api/customers/{customer_uuid}/project-metadata-compliance-overview/  
GET /api/customers/{customer_uuid}/project-metadata-compliance-projects/  
GET /api/customers/{customer_uuid}/project-metadata-question-answers/  
GET /api/managed-rancher-cluster-resources/  
HEAD /api/managed-rancher-cluster-resources/  
GET /api/managed-rancher-cluster-resources/{uuid}/  
POST /api/managed-rancher-cluster-resources/{uuid}/add_node/  
GET /api/marketplace-offering-terms-of-service/  
HEAD /api/marketplace-offering-terms-of-service/  
POST /api/marketplace-offering-terms-of-service/  
DELETE /api/marketplace-offering-terms-of-service/{uuid}/  
GET /api/marketplace-offering-terms-of-service/{uuid}/  
PATCH /api/marketplace-offering-terms-of-service/{uuid}/  
PUT /api/marketplace-offering-terms-of-service/{uuid}/  
GET /api/marketplace-user-offering-consents/  
HEAD /api/marketplace-user-offering-consents/  
POST /api/marketplace-user-offering-consents/  
DELETE /api/marketplace-user-offering-consents/{uuid}/  
GET /api/marketplace-user-offering-consents/{uuid}/  
PATCH /api/marketplace-user-offering-consents/{uuid}/  
PUT /api/marketplace-user-offering-consents/{uuid}/  
POST /api/marketplace-user-offering-consents/{uuid}/revoke/  
GET /api/remote-waldur-api/remote_resource_order_status/{resource_uuid}/  
GET /api/remote-waldur-api/remote_resource_status/{resource_uuid}/  
GET /api/remote-waldur-api/remote_resource_team_status/{resource_uuid}/  

### Deleted Endpoints: None

---------------------------

### Modified Endpoints: 116

---------------------------
POST /api/backend-resources/{uuid}/import_resource/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: user_requires_reconsent
            - Deleted property: offering_terms_of_service
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Deleted property: offering_terms_of_service
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Deleted property: offering_terms_of_service

GET /api/booking-offerings/

- Modified query param: field
  - Schema changed
    - Items changed
      - Deleted enum values: [terms_of_service terms_of_service_link]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Deleted property: terms_of_service
              - Deleted property: terms_of_service_link
              - Modified property: slug
                - ReadOnly changed from true to false

GET /api/booking-offerings/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - Deleted enum values: [terms_of_service terms_of_service_link]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: terms_of_service
            - Deleted property: terms_of_service_link
            - Modified property: slug
              - ReadOnly changed from true to false

GET /api/booking-resources/

- New query param: offering_slug
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [user_requires_reconsent]
      - Deleted enum values: [offering_terms_of_service]
- Modified query param: offering_uuid
  - Description changed from '' to 'Multiple values may be separated by commas.'
  - Style changed from '' to 'form'
  - Explode changed from null to false
  - Schema changed
    - Type changed from 'string' to 'array'
    - Format changed from 'uuid' to ''
    - Items changed
      - Schema added
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: user_requires_reconsent
              - Deleted property: offering_terms_of_service
              - Modified property: creation_order
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - Deleted property: offering_terms_of_service
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - Deleted property: offering_terms_of_service
              - Modified property: slug
                - ReadOnly changed from true to false

HEAD /api/booking-resources/

- New query param: offering_slug
- Modified query param: offering_uuid
  - Description changed from '' to 'Multiple values may be separated by commas.'
  - Style changed from '' to 'form'
  - Explode changed from null to false
  - Schema changed
    - Type changed from 'string' to 'array'
    - Format changed from 'uuid' to ''
    - Items changed
      - Schema added

GET /api/booking-resources/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [user_requires_reconsent]
      - Deleted enum values: [offering_terms_of_service]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: user_requires_reconsent
            - Deleted property: offering_terms_of_service
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Deleted property: offering_terms_of_service
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Deleted property: offering_terms_of_service
            - Modified property: slug
              - ReadOnly changed from true to false

GET /api/checklists-admin-questions/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: dependency_logic_operator

POST /api/checklists-admin-questions/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: dependency_logic_operator
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: dependency_logic_operator

GET /api/checklists-admin-questions/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: dependency_logic_operator

PATCH /api/checklists-admin-questions/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: dependency_logic_operator
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: dependency_logic_operator

PUT /api/checklists-admin-questions/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: dependency_logic_operator
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: dependency_logic_operator

GET /api/checklists-admin/{uuid}/questions/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: dependency_logic_operator

GET /api/customers/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [organization_groups project_metadata_checklist projects users_count]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: organization_groups
              - New property: project_metadata_checklist
              - New property: projects
              - New property: users_count
              - Modified property: slug
                - ReadOnly changed from true to false

POST /api/customers/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: organization_groups
            - New property: project_metadata_checklist
            - New property: projects
            - New property: users_count
            - Modified property: slug
              - ReadOnly changed from true to false

GET /api/customers/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [organization_groups project_metadata_checklist projects users_count]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: organization_groups
            - New property: project_metadata_checklist
            - New property: projects
            - New property: users_count
            - Modified property: slug
              - ReadOnly changed from true to false

PATCH /api/customers/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: organization_groups
            - New property: project_metadata_checklist
            - New property: projects
            - New property: users_count
            - Modified property: slug
              - ReadOnly changed from true to false

PUT /api/customers/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: organization_groups
            - New property: project_metadata_checklist
            - New property: projects
            - New property: users_count
            - Modified property: slug
              - ReadOnly changed from true to false

GET /api/google-auth/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [enable_notifications]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: enable_notifications

GET /api/google-auth/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [enable_notifications]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: enable_notifications

GET /api/google-auth/{uuid}/authorize/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [enable_notifications]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: enable_notifications

GET /api/maintenance-announcements/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: backend_id
            - Properties changed
              - New property: backend_id

POST /api/maintenance-announcements/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: backend_id
          - Properties changed
            - New property: backend_id

GET /api/maintenance-announcements/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: backend_id
          - Properties changed
            - New property: backend_id

PATCH /api/maintenance-announcements/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: backend_id
          - Properties changed
            - New property: backend_id

PUT /api/maintenance-announcements/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: backend_id
          - Properties changed
            - New property: backend_id

GET /api/marketplace-integration-statuses/

- New query param: offering_slug
- Modified query param: offering_uuid
  - Description changed from '' to 'Multiple values may be separated by commas.'
  - Style changed from '' to 'form'
  - Explode changed from null to false
  - Schema changed
    - Type changed from 'string' to 'array'
    - Format changed from 'uuid' to ''
    - Items changed
      - Schema added

HEAD /api/marketplace-integration-statuses/

- New query param: offering_slug
- Modified query param: offering_uuid
  - Description changed from '' to 'Multiple values may be separated by commas.'
  - Style changed from '' to 'form'
  - Explode changed from null to false
  - Schema changed
    - Type changed from 'string' to 'array'
    - Format changed from 'uuid' to ''
    - Items changed
      - Schema added

GET /api/marketplace-offering-files/

- New query param: offering_slug
- Modified query param: offering_uuid
  - Description changed from '' to 'Multiple values may be separated by commas.'
  - Style changed from '' to 'form'
  - Explode changed from null to false
  - Schema changed
    - Type changed from 'string' to 'array'
    - Format changed from 'uuid' to ''
    - Items changed
      - Schema added

HEAD /api/marketplace-offering-files/

- New query param: offering_slug
- Modified query param: offering_uuid
  - Description changed from '' to 'Multiple values may be separated by commas.'
  - Style changed from '' to 'form'
  - Explode changed from null to false
  - Schema changed
    - Type changed from 'string' to 'array'
    - Format changed from 'uuid' to ''
    - Items changed
      - Schema added

GET /api/marketplace-offering-user-roles/

- New query param: offering_slug
- Modified query param: offering_uuid
  - Description changed from '' to 'Multiple values may be separated by commas.'
  - Style changed from '' to 'form'
  - Explode changed from null to false
  - Schema changed
    - Type changed from 'string' to 'array'
    - Format changed from 'uuid' to ''
    - Items changed
      - Schema added

HEAD /api/marketplace-offering-user-roles/

- New query param: offering_slug
- Modified query param: offering_uuid
  - Description changed from '' to 'Multiple values may be separated by commas.'
  - Style changed from '' to 'form'
  - Explode changed from null to false
  - Schema changed
    - Type changed from 'string' to 'array'
    - Format changed from 'uuid' to ''
    - Items changed
      - Schema added

GET /api/marketplace-offering-users/

- New query param: offering_slug
- Modified query param: offering_uuid
  - Description changed from '' to 'Multiple values may be separated by commas.'
  - Style changed from '' to 'form'
  - Explode changed from null to false
  - Schema changed
    - Type changed from 'string' to 'array'
    - Format changed from 'uuid' to ''
    - Items changed
      - Schema added

HEAD /api/marketplace-offering-users/

- New query param: offering_slug
- Modified query param: offering_uuid
  - Description changed from '' to 'Multiple values may be separated by commas.'
  - Style changed from '' to 'form'
  - Explode changed from null to false
  - Schema changed
    - Type changed from 'string' to 'array'
    - Format changed from 'uuid' to ''
    - Items changed
      - Schema added

GET /api/marketplace-orders/

- New query param: offering_slug
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [error_traceback]
      - Deleted enum values: [offering_terms_of_service]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Deleted property: offering_terms_of_service

HEAD /api/marketplace-orders/

- New query param: offering_slug

POST /api/marketplace-orders/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: attributes
            - Property 'OneOf' changed
              - Schemas added: #/components/schemas/GenericOrderAttributes
              - Modified schema: #/components/schemas/AzureVirtualMachineCreateOrderAttributes
                - Description changed from 'This mixin allows to specify list of fields to be rendered by serializer.
It expects that request is available in serializer's context.' to 'This mixin allows to specify list of fields to be rendered by serializer.
It expects that request is available in serializer's context.

It is disabled for nested serializers (where parent is another serializer)
but remains active for list views (where parent is a ListSerializer).'
              - Modified schema: #/components/schemas/AzureSQLServerCreateOrderAttributes
                - Description changed from 'This mixin allows to specify list of fields to be rendered by serializer.
It expects that request is available in serializer's context.' to 'This mixin allows to specify list of fields to be rendered by serializer.
It expects that request is available in serializer's context.

It is disabled for nested serializers (where parent is another serializer)
but remains active for list views (where parent is a ListSerializer).'
              - Modified schema: #/components/schemas/OpenStackTenantCreateOrderAttributes
                - Description changed from 'This mixin allows to specify list of fields to be rendered by serializer.
It expects that request is available in serializer's context.' to 'This mixin allows to specify list of fields to be rendered by serializer.
It expects that request is available in serializer's context.

It is disabled for nested serializers (where parent is another serializer)
but remains active for list views (where parent is a ListSerializer).'
                - Properties changed
                  - New property: user_password
                  - New property: user_username
              - Modified schema: #/components/schemas/OpenStackInstanceCreateOrderAttributes
                - Description changed from 'This mixin allows to specify list of fields to be rendered by serializer.
It expects that request is available in serializer's context.' to 'This mixin allows to specify list of fields to be rendered by serializer.
It expects that request is available in serializer's context.

It is disabled for nested serializers (where parent is another serializer)
but remains active for list views (where parent is a ListSerializer).'
                - Properties changed
                  - Modified property: security_groups
                    - Description changed from 'List of security groups to apply to the instance' to 'Security groups to attach to the instance'
                    - Items changed
                      - Properties changed
                        - Modified property: url
                          - Format changed from '' to 'uri'
              - Modified schema: #/components/schemas/OpenStackVolumeCreateOrderAttributes
                - Description changed from 'This mixin allows to specify list of fields to be rendered by serializer.
It expects that request is available in serializer's context.' to 'This mixin allows to specify list of fields to be rendered by serializer.
It expects that request is available in serializer's context.

It is disabled for nested serializers (where parent is another serializer)
but remains active for list views (where parent is a ListSerializer).'
              - Modified schema: #/components/schemas/MarketplaceRancherCreateOrderAttributes
                - Description changed from 'This mixin allows to specify list of fields to be rendered by serializer.
It expects that request is available in serializer's context.' to 'This mixin allows to specify list of fields to be rendered by serializer.
It expects that request is available in serializer's context.

It is disabled for nested serializers (where parent is another serializer)
but remains active for list views (where parent is a ListSerializer).'
              - Modified schema: #/components/schemas/SlurmInvoicesSlurmPackageCreateOrderAttributes
                - Description changed from 'This mixin allows to specify list of fields to be rendered by serializer.
It expects that request is available in serializer's context.' to 'This mixin allows to specify list of fields to be rendered by serializer.
It expects that request is available in serializer's context.

It is disabled for nested serializers (where parent is another serializer)
but remains active for list views (where parent is a ListSerializer).'
              - Modified schema: #/components/schemas/VMwareVirtualMachineCreateOrderAttributes
                - Description changed from 'This mixin allows to specify list of fields to be rendered by serializer.
It expects that request is available in serializer's context.' to 'This mixin allows to specify list of fields to be rendered by serializer.
It expects that request is available in serializer's context.

It is disabled for nested serializers (where parent is another serializer)
but remains active for list views (where parent is a ListSerializer).'
            - Description changed from 'Attributes structure depends on the offering type specified in the parent object' to 'Attributes structure depends on the offering type specified in the parent object. Can also be a generic object for offerings without a specific attributes schema.'

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: offering_terms_of_service
          - Properties changed
            - Deleted property: offering_terms_of_service

GET /api/marketplace-orders/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [error_traceback]
      - Deleted enum values: [offering_terms_of_service]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: offering_terms_of_service

GET /api/marketplace-orders/{uuid}/offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: terms_of_service
            - Deleted property: terms_of_service_link

GET /api/marketplace-plans/

- New query param: offering_slug

HEAD /api/marketplace-plans/

- New query param: offering_slug

GET /api/marketplace-plans/usage_stats/

- New query param: offering_slug

HEAD /api/marketplace-plans/usage_stats/

- New query param: offering_slug

GET /api/marketplace-provider-offerings/

- Modified query param: field
  - Schema changed
    - Items changed
      - Deleted enum values: [terms_of_service terms_of_service_link]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Deleted property: terms_of_service
              - Deleted property: terms_of_service_link
              - Modified property: slug
                - ReadOnly changed from true to false

POST /api/marketplace-provider-offerings/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Deleted property: terms_of_service
          - Deleted property: terms_of_service_link
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: terms_of_service
            - Deleted property: terms_of_service_link

GET /api/marketplace-provider-offerings/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - Deleted enum values: [terms_of_service terms_of_service_link]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: terms_of_service
            - Deleted property: terms_of_service_link
            - Modified property: slug
              - ReadOnly changed from true to false

POST /api/marketplace-provider-offerings/{uuid}/import_resource/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: user_requires_reconsent
            - Deleted property: offering_terms_of_service
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Deleted property: offering_terms_of_service
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Deleted property: offering_terms_of_service

GET /api/marketplace-provider-offerings/{uuid}/list_customer_service_accounts/

- Modified query param: field
  - Schema changed
    - Items changed
      - Deleted enum values: [terms_of_service terms_of_service_link]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: terms_of_service
            - Deleted property: terms_of_service_link
            - Modified property: slug
              - ReadOnly changed from true to false

GET /api/marketplace-provider-offerings/{uuid}/list_project_service_accounts/

- Modified query param: field
  - Schema changed
    - Items changed
      - Deleted enum values: [terms_of_service terms_of_service_link]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: terms_of_service
            - Deleted property: terms_of_service_link
            - Modified property: slug
              - ReadOnly changed from true to false

POST /api/marketplace-provider-offerings/{uuid}/move_offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: terms_of_service
            - Deleted property: terms_of_service_link

GET /api/marketplace-provider-offerings/{uuid}/orders/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Deleted property: offering_terms_of_service

GET /api/marketplace-provider-offerings/{uuid}/orders/{order_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: offering_terms_of_service

POST /api/marketplace-provider-offerings/{uuid}/refresh_offering_usernames/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Deleted property: terms_of_service
          - Deleted property: terms_of_service_link

GET /api/marketplace-provider-offerings/{uuid}/stats/

- Modified query param: field
  - Schema changed
    - Items changed
      - Deleted enum values: [terms_of_service terms_of_service_link]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: terms_of_service
            - Deleted property: terms_of_service_link
            - Modified property: slug
              - ReadOnly changed from true to false

POST /api/marketplace-provider-offerings/{uuid}/update_image/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: terms_of_service
            - Deleted property: terms_of_service_link
            - Modified property: slug
              - ReadOnly changed from true to false

POST /api/marketplace-provider-offerings/{uuid}/update_overview/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Deleted property: terms_of_service
          - Deleted property: terms_of_service_link

GET /api/marketplace-provider-offerings/{uuid}/user_has_resource_access/

- Modified query param: field
  - Schema changed
    - Items changed
      - Deleted enum values: [terms_of_service terms_of_service_link]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: terms_of_service
            - Deleted property: terms_of_service_link
            - Modified property: slug
              - ReadOnly changed from true to false

GET /api/marketplace-provider-resources/

- New query param: offering_slug
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [user_requires_reconsent]
      - Deleted enum values: [offering_terms_of_service]
- Modified query param: offering_uuid
  - Description changed from '' to 'Multiple values may be separated by commas.'
  - Style changed from '' to 'form'
  - Explode changed from null to false
  - Schema changed
    - Type changed from 'string' to 'array'
    - Format changed from 'uuid' to ''
    - Items changed
      - Schema added
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: user_requires_reconsent
              - Deleted property: offering_terms_of_service
              - Modified property: creation_order
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - Deleted property: offering_terms_of_service
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - Deleted property: offering_terms_of_service

HEAD /api/marketplace-provider-resources/

- New query param: offering_slug
- Modified query param: offering_uuid
  - Description changed from '' to 'Multiple values may be separated by commas.'
  - Style changed from '' to 'form'
  - Explode changed from null to false
  - Schema changed
    - Type changed from 'string' to 'array'
    - Format changed from 'uuid' to ''
    - Items changed
      - Schema added

GET /api/marketplace-provider-resources/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [user_requires_reconsent]
      - Deleted enum values: [offering_terms_of_service]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: user_requires_reconsent
            - Deleted property: offering_terms_of_service
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Deleted property: offering_terms_of_service
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Deleted property: offering_terms_of_service

GET /api/marketplace-provider-resources/{uuid}/details/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [user_requires_reconsent]
      - Deleted enum values: [offering_terms_of_service]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: user_requires_reconsent
            - Deleted property: offering_terms_of_service
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Deleted property: offering_terms_of_service
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Deleted property: offering_terms_of_service

POST /api/marketplace-provider-resources/{uuid}/move_resource/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: user_requires_reconsent
            - Deleted property: offering_terms_of_service
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Deleted property: offering_terms_of_service
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Deleted property: offering_terms_of_service

GET /api/marketplace-provider-resources/{uuid}/offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: terms_of_service
            - Deleted property: terms_of_service_link

POST /api/marketplace-provider-resources/{uuid}/set_end_date_by_provider/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: user_requires_reconsent
            - Deleted property: offering_terms_of_service
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Deleted property: offering_terms_of_service
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Deleted property: offering_terms_of_service

GET /api/marketplace-public-offerings/

- Modified query param: field
  - Schema changed
    - Items changed
      - Deleted enum values: [terms_of_service terms_of_service_link]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Deleted property: terms_of_service
              - Deleted property: terms_of_service_link

GET /api/marketplace-public-offerings/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - Deleted enum values: [terms_of_service terms_of_service_link]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: terms_of_service
            - Deleted property: terms_of_service_link

GET /api/marketplace-resources/

- New query param: offering_slug
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [user_requires_reconsent]
      - Deleted enum values: [offering_terms_of_service]
- Modified query param: offering_uuid
  - Description changed from '' to 'Multiple values may be separated by commas.'
  - Style changed from '' to 'form'
  - Explode changed from null to false
  - Schema changed
    - Type changed from 'string' to 'array'
    - Format changed from 'uuid' to ''
    - Items changed
      - Schema added
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: user_requires_reconsent
              - Deleted property: offering_terms_of_service
              - Modified property: creation_order
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - Deleted property: offering_terms_of_service
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - Deleted property: offering_terms_of_service

HEAD /api/marketplace-resources/

- New query param: offering_slug
- Modified query param: offering_uuid
  - Description changed from '' to 'Multiple values may be separated by commas.'
  - Style changed from '' to 'form'
  - Explode changed from null to false
  - Schema changed
    - Type changed from 'string' to 'array'
    - Format changed from 'uuid' to ''
    - Items changed
      - Schema added

GET /api/marketplace-resources/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [user_requires_reconsent]
      - Deleted enum values: [offering_terms_of_service]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: user_requires_reconsent
            - Deleted property: offering_terms_of_service
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Deleted property: offering_terms_of_service
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Deleted property: offering_terms_of_service

GET /api/marketplace-resources/{uuid}/details/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [user_requires_reconsent]
      - Deleted enum values: [offering_terms_of_service]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: user_requires_reconsent
            - Deleted property: offering_terms_of_service
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Deleted property: offering_terms_of_service
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Deleted property: offering_terms_of_service

POST /api/marketplace-resources/{uuid}/move_resource/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: user_requires_reconsent
            - Deleted property: offering_terms_of_service
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Deleted property: offering_terms_of_service
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Deleted property: offering_terms_of_service

GET /api/marketplace-resources/{uuid}/offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: terms_of_service
            - Deleted property: terms_of_service_link

GET /api/marketplace-screenshots/

- New query param: offering_slug
- Modified query param: offering_uuid
  - Description changed from '' to 'Multiple values may be separated by commas.'
  - Style changed from '' to 'form'
  - Explode changed from null to false
  - Schema changed
    - Type changed from 'string' to 'array'
    - Format changed from 'uuid' to ''
    - Items changed
      - Schema added

HEAD /api/marketplace-screenshots/

- New query param: offering_slug
- Modified query param: offering_uuid
  - Description changed from '' to 'Multiple values may be separated by commas.'
  - Style changed from '' to 'form'
  - Explode changed from null to false
  - Schema changed
    - Type changed from 'string' to 'array'
    - Format changed from 'uuid' to ''
    - Items changed
      - Schema added

POST /api/marketplace-script-dry-run/{uuid}/async_run/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: terms_of_service
            - Deleted property: terms_of_service_link

POST /api/marketplace-script-dry-run/{uuid}/run/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: terms_of_service
            - Deleted property: terms_of_service_link

GET /api/marketplace-service-providers/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [enable_notifications]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: enable_notifications

POST /api/marketplace-service-providers/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: enable_notifications

GET /api/marketplace-service-providers/{service_provider_uuid}/offerings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: slug
                - ReadOnly changed from true to false

GET /api/marketplace-service-providers/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [enable_notifications]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: enable_notifications

PATCH /api/marketplace-service-providers/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: enable_notifications

PUT /api/marketplace-service-providers/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: enable_notifications

GET /api/openstack-backups/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: instance_security_groups
                - Items changed
                  - Properties changed
                    - New property: description
                    - New property: name
                    - New property: rules
                    - New property: state
                    - Modified property: url
                      - Format changed from '' to 'uri'
                      - ReadOnly changed from false to true
              - Modified property: restorations
                - Items changed
                  - Properties changed
                    - Modified property: security_groups
                      - Items changed
                        - Properties changed
                          - New property: description
                          - New property: name
                          - New property: rules
                          - New property: state
                          - Modified property: url
                            - Format changed from '' to 'uri'
                            - ReadOnly changed from false to true

GET /api/openstack-backups/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: instance_security_groups
              - Items changed
                - Properties changed
                  - New property: description
                  - New property: name
                  - New property: rules
                  - New property: state
                  - Modified property: url
                    - Format changed from '' to 'uri'
                    - ReadOnly changed from false to true
            - Modified property: restorations
              - Items changed
                - Properties changed
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - New property: description
                        - New property: name
                        - New property: rules
                        - New property: state
                        - Modified property: url
                          - Format changed from '' to 'uri'
                          - ReadOnly changed from false to true

PATCH /api/openstack-backups/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: instance_security_groups
              - Items changed
                - Properties changed
                  - New property: description
                  - New property: name
                  - New property: rules
                  - New property: state
                  - Modified property: url
                    - Format changed from '' to 'uri'
                    - ReadOnly changed from false to true
            - Modified property: restorations
              - Items changed
                - Properties changed
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - New property: description
                        - New property: name
                        - New property: rules
                        - New property: state
                        - Modified property: url
                          - Format changed from '' to 'uri'
                          - ReadOnly changed from false to true

PUT /api/openstack-backups/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: instance_security_groups
              - Items changed
                - Properties changed
                  - New property: description
                  - New property: name
                  - New property: rules
                  - New property: state
                  - Modified property: url
                    - Format changed from '' to 'uri'
                    - ReadOnly changed from false to true
            - Modified property: restorations
              - Items changed
                - Properties changed
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - New property: description
                        - New property: name
                        - New property: rules
                        - New property: state
                        - Modified property: url
                          - Format changed from '' to 'uri'
                          - ReadOnly changed from false to true

POST /api/openstack-backups/{uuid}/restore/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Deleted property: security_groups
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: security_groups
              - Items changed
                - Properties changed
                  - New property: description
                  - New property: name
                  - New property: rules
                  - New property: state
                  - Modified property: url
                    - Format changed from '' to 'uri'
                    - ReadOnly changed from false to true

GET /api/openstack-instances/

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
                    - New property: description
                    - New property: name
                    - New property: rules
                    - New property: state
                    - Modified property: url
                      - Format changed from '' to 'uri'
                      - ReadOnly changed from false to true

GET /api/openstack-instances/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: security_groups
              - Items changed
                - Properties changed
                  - New property: description
                  - New property: name
                  - New property: rules
                  - New property: state
                  - Modified property: url
                    - Format changed from '' to 'uri'
                    - ReadOnly changed from false to true

PATCH /api/openstack-instances/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: security_groups
              - Items changed
                - Properties changed
                  - New property: description
                  - New property: name
                  - New property: rules
                  - New property: state
                  - Modified property: url
                    - Format changed from '' to 'uri'
                    - ReadOnly changed from false to true

PUT /api/openstack-instances/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: security_groups
              - Items changed
                - Properties changed
                  - New property: description
                  - New property: name
                  - New property: rules
                  - New property: state
                  - Modified property: url
                    - Format changed from '' to 'uri'
                    - ReadOnly changed from false to true

POST /api/openstack-instances/{uuid}/backup/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: instance_security_groups
              - Items changed
                - Properties changed
                  - New property: description
                  - New property: name
                  - New property: rules
                  - New property: state
                  - Modified property: url
                    - Format changed from '' to 'uri'
                    - ReadOnly changed from false to true
            - Modified property: restorations
              - Items changed
                - Properties changed
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - New property: description
                        - New property: name
                        - New property: rules
                        - New property: state
                        - Modified property: url
                          - Format changed from '' to 'uri'
                          - ReadOnly changed from false to true

GET /api/openstack-networks/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [segmentation_id]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: segmentation_id

GET /api/openstack-networks/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [segmentation_id]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: segmentation_id

PATCH /api/openstack-networks/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: segmentation_id

PUT /api/openstack-networks/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: segmentation_id

POST /api/openstack-security-groups/{uuid}/set_rules/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Items changed
          - Properties changed
            - Modified property: direction
              - Default changed from null to 'ingress'
            - Modified property: ethertype
              - Default changed from null to 'IPv4'

GET /api/openstack-tenants/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [access_url user_password user_username]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: access_url
              - New property: user_password
              - New property: user_username

POST /api/openstack-tenants/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: access_url
            - New property: user_password
            - New property: user_username

GET /api/openstack-tenants/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [access_url user_password user_username]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: access_url
            - New property: user_password
            - New property: user_username

PATCH /api/openstack-tenants/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: access_url
            - New property: user_password
            - New property: user_username

PUT /api/openstack-tenants/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: access_url
            - New property: user_password
            - New property: user_username

POST /api/openstack-tenants/{uuid}/create_network/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: segmentation_id

POST /api/openstack-tenants/{uuid}/pull_security_groups/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: access_url
            - New property: user_password
            - New property: user_username

POST /api/openstack-tenants/{uuid}/pull_server_groups/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: access_url
            - New property: user_password
            - New property: user_username

GET /api/promotions-campaigns/{uuid}/orders/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Deleted property: offering_terms_of_service

GET /api/promotions-campaigns/{uuid}/resources/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: user_requires_reconsent
              - Deleted property: offering_terms_of_service
              - Modified property: creation_order
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - Deleted property: offering_terms_of_service
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - Deleted property: offering_terms_of_service

GET /api/proposal-protected-calls/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: slug
                - ReadOnly changed from true to false

POST /api/proposal-protected-calls/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: slug
              - ReadOnly changed from true to false

GET /api/proposal-protected-calls/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: slug
              - ReadOnly changed from true to false

PATCH /api/proposal-protected-calls/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: slug
              - ReadOnly changed from true to false

PUT /api/proposal-protected-calls/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: slug
              - ReadOnly changed from true to false

POST /api/proposal-protected-calls/{uuid}/activate/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: slug
              - ReadOnly changed from true to false

POST /api/proposal-protected-calls/{uuid}/archive/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: slug
              - ReadOnly changed from true to false

POST /api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/close/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: slug
              - ReadOnly changed from true to false

GET /api/proposal-public-calls/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: slug
                - ReadOnly changed from true to false

GET /api/proposal-public-calls/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: slug
              - ReadOnly changed from true to false

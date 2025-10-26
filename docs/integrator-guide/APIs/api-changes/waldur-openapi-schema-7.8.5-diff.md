# OpenAPI schema diff - 7.8.5

## For version 7.8.5

### New Endpoints: 71

---------------------
GET /api/marketplace-customer-component-usage-policies/  
HEAD /api/marketplace-customer-component-usage-policies/  
POST /api/marketplace-customer-component-usage-policies/  
GET /api/marketplace-customer-component-usage-policies/actions/  
HEAD /api/marketplace-customer-component-usage-policies/actions/  
DELETE /api/marketplace-customer-component-usage-policies/{uuid}/  
GET /api/marketplace-customer-component-usage-policies/{uuid}/  
PATCH /api/marketplace-customer-component-usage-policies/{uuid}/  
PUT /api/marketplace-customer-component-usage-policies/{uuid}/  
POST /api/marketplace-orders/{uuid}/set_backend_id/  
POST /api/marketplace-plans/{uuid}/update_discounts/  
POST /api/marketplace-provider-offerings/{uuid}/add_partition/  
POST /api/marketplace-provider-offerings/{uuid}/add_software_catalog/  
POST /api/marketplace-provider-offerings/{uuid}/remove_partition/  
POST /api/marketplace-provider-offerings/{uuid}/remove_software_catalog/  
PATCH /api/marketplace-provider-offerings/{uuid}/update_partition/  
PATCH /api/marketplace-provider-offerings/{uuid}/update_software_catalog/  
POST /api/marketplace-provider-resources/{uuid}/set_downscaled/  
POST /api/marketplace-provider-resources/{uuid}/set_paused/  
POST /api/marketplace-provider-resources/{uuid}/set_restrict_member_access/  
POST /api/marketplace-resources/{uuid}/set_downscaled/  
POST /api/marketplace-resources/{uuid}/set_paused/  
POST /api/marketplace-resources/{uuid}/set_restrict_member_access/  
GET /api/marketplace-site-agent-identities/  
HEAD /api/marketplace-site-agent-identities/  
POST /api/marketplace-site-agent-identities/  
DELETE /api/marketplace-site-agent-identities/{uuid}/  
GET /api/marketplace-site-agent-identities/{uuid}/  
PUT /api/marketplace-site-agent-identities/{uuid}/  
POST /api/marketplace-site-agent-identities/{uuid}/register_event_subscription/  
POST /api/marketplace-site-agent-identities/{uuid}/register_service/  
GET /api/marketplace-site-agent-processors/  
HEAD /api/marketplace-site-agent-processors/  
GET /api/marketplace-site-agent-processors/{uuid}/  
GET /api/marketplace-site-agent-services/  
HEAD /api/marketplace-site-agent-services/  
GET /api/marketplace-site-agent-services/{uuid}/  
POST /api/marketplace-site-agent-services/{uuid}/register_processor/  
POST /api/marketplace-site-agent-services/{uuid}/set_statistics/  
GET /api/marketplace-software-catalogs/  
HEAD /api/marketplace-software-catalogs/  
POST /api/marketplace-software-catalogs/  
DELETE /api/marketplace-software-catalogs/{uuid}/  
GET /api/marketplace-software-catalogs/{uuid}/  
PATCH /api/marketplace-software-catalogs/{uuid}/  
PUT /api/marketplace-software-catalogs/{uuid}/  
GET /api/marketplace-software-packages/  
HEAD /api/marketplace-software-packages/  
POST /api/marketplace-software-packages/  
DELETE /api/marketplace-software-packages/{uuid}/  
GET /api/marketplace-software-packages/{uuid}/  
PATCH /api/marketplace-software-packages/{uuid}/  
PUT /api/marketplace-software-packages/{uuid}/  
GET /api/marketplace-software-targets/  
HEAD /api/marketplace-software-targets/  
POST /api/marketplace-software-targets/  
DELETE /api/marketplace-software-targets/{uuid}/  
GET /api/marketplace-software-targets/{uuid}/  
PATCH /api/marketplace-software-targets/{uuid}/  
PUT /api/marketplace-software-targets/{uuid}/  
GET /api/marketplace-software-versions/  
HEAD /api/marketplace-software-versions/  
POST /api/marketplace-software-versions/  
DELETE /api/marketplace-software-versions/{uuid}/  
GET /api/marketplace-software-versions/{uuid}/  
PATCH /api/marketplace-software-versions/{uuid}/  
PUT /api/marketplace-software-versions/{uuid}/  
POST /api/onboarding-justifications/{uuid}/approve/  
POST /api/onboarding-justifications/{uuid}/reject/  
POST /api/projects/{uuid}/recover/  
POST /api/remote-waldur-api/pull_resource_robot_accounts/{uuid}/  

### Deleted Endpoints: None

---------------------------

### Modified Endpoints: 424

---------------------------
GET /api/access-subnets/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to 4096

POST /api/access-subnets/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/access-subnets/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PATCH /api/access-subnets/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PUT /api/access-subnets/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/admin-announcements/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to 4096

POST /api/admin-announcements/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/admin-announcements/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PATCH /api/admin-announcements/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PUT /api/admin-announcements/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/aws-instances/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to 4096

POST /api/aws-instances/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/aws-instances/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PATCH /api/aws-instances/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PUT /api/aws-instances/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/aws-volumes/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to 4096

POST /api/aws-volumes/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/aws-volumes/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PATCH /api/aws-volumes/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PUT /api/aws-volumes/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/azure-public-ips/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to 4096

POST /api/azure-public-ips/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/azure-public-ips/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PATCH /api/azure-public-ips/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PUT /api/azure-public-ips/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/azure-resource-groups/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to 4096

GET /api/azure-resource-groups/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/azure-sql-databases/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to 4096

POST /api/azure-sql-databases/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/azure-sql-databases/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PATCH /api/azure-sql-databases/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PUT /api/azure-sql-databases/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/azure-sql-servers/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to 4096

POST /api/azure-sql-servers/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/azure-sql-servers/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PATCH /api/azure-sql-servers/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PUT /api/azure-sql-servers/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

POST /api/azure-sql-servers/{uuid}/create_database/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/azure-virtualmachines/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to 4096

POST /api/azure-virtualmachines/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/azure-virtualmachines/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PATCH /api/azure-virtualmachines/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PUT /api/azure-virtualmachines/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

POST /api/backend-resources/{uuid}/import_resource/

- Responses changed
  - New response: 201
  - Deleted response: 200

GET /api/booking-offerings/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [partitions software_catalogs]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: partitions
              - New property: software_catalogs
              - Modified property: components
                - Items changed
                  - Properties changed
                    - Modified property: description
                      - MaxLength changed from 2000 to 4096
              - Modified property: description
                - MaxLength changed from 2000 to 4096
              - Modified property: plans
                - Items changed
                  - Properties changed
                    - New property: components
              - Modified property: plugin_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedPluginOptions
                    - Properties changed
                      - New property: backend_id_display_label
                      - New property: create_orders_on_resource_option_change
                      - New property: enable_purchase_order_upload
                      - New property: highlight_backend_id_display
                      - New property: require_purchase_order_upload
                      - Deleted property: order_supports_comments_and_metadata
              - Modified property: screenshots
                - Items changed
                  - Properties changed
                    - Modified property: description
                      - MaxLength changed from 2000 to 4096

GET /api/booking-offerings/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [partitions software_catalogs]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: partitions
            - New property: software_catalogs
            - Modified property: components
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096
            - Modified property: description
              - MaxLength changed from 2000 to 4096
            - Modified property: plans
              - Items changed
                - Properties changed
                  - New property: components
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: backend_id_display_label
                    - New property: create_orders_on_resource_option_change
                    - New property: enable_purchase_order_upload
                    - New property: highlight_backend_id_display
                    - New property: require_purchase_order_upload
                    - Deleted property: order_supports_comments_and_metadata
            - Modified property: screenshots
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096

GET /api/booking-resources/

- New query param: component_count
- New query param: limit_based
- New query param: limit_component_count
- New query param: only_limit_based
- New query param: only_usage_based
- New query param: usage_based
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [renewal_date]
- Modified query param: query
  - Description changed from 'Search by resource UUID, name, backend ID, effective ID, IPs or hypervisor' to 'Search by resource UUID, name, slug, backend ID, effective ID, IPs or hypervisor'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: renewal_date
              - Modified property: creation_order
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: start_date
                      - New property: url
                      - Modified property: state
                        - Property 'AllOf' changed
                          - Modified schema: #/components/schemas/OrderState
                            - New enum values: [pending-start-date]
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: start_date
                      - New property: url
                      - Modified property: state
                        - Property 'AllOf' changed
                          - Modified schema: #/components/schemas/OrderState
                            - New enum values: [pending-start-date]

HEAD /api/booking-resources/

- New query param: component_count
- New query param: limit_based
- New query param: limit_component_count
- New query param: only_limit_based
- New query param: only_usage_based
- New query param: usage_based
- Modified query param: query
  - Description changed from 'Search by resource UUID, name, backend ID, effective ID, IPs or hypervisor' to 'Search by resource UUID, name, slug, backend ID, effective ID, IPs or hypervisor'

GET /api/booking-resources/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [renewal_date]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: renewal_date
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: start_date
                    - New property: url
                    - Modified property: state
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/OrderState
                          - New enum values: [pending-start-date]
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: start_date
                    - New property: url
                    - Modified property: state
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/OrderState
                          - New enum values: [pending-start-date]

GET /api/call-managing-organisations/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to 4096

POST /api/call-managing-organisations/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/call-managing-organisations/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PATCH /api/call-managing-organisations/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PUT /api/call-managing-organisations/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

POST /api/call-managing-organisations/{uuid}/add_user/

- Responses changed
  - New response: 400

GET /api/checklists-admin-categories/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to 4096

POST /api/checklists-admin-categories/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/checklists-admin-categories/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PATCH /api/checklists-admin-categories/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PUT /api/checklists-admin-categories/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/checklists-admin-questions/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to 4096

POST /api/checklists-admin-questions/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/checklists-admin-questions/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PATCH /api/checklists-admin-questions/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PUT /api/checklists-admin-questions/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/checklists-admin/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to 4096

POST /api/checklists-admin/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/checklists-admin/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PATCH /api/checklists-admin/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PUT /api/checklists-admin/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/checklists-admin/{uuid}/questions/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to 4096

GET /api/customers/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to 4096

POST /api/customers/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/customers/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PATCH /api/customers/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PUT /api/customers/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

POST /api/customers/{uuid}/add_user/

- Responses changed
  - New response: 400

GET /api/digitalocean-droplets/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to 4096

POST /api/digitalocean-droplets/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/digitalocean-droplets/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PATCH /api/digitalocean-droplets/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PUT /api/digitalocean-droplets/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/event-subscriptions/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to 4096

POST /api/event-subscriptions/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/event-subscriptions/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/external-links/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to 4096

POST /api/external-links/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/external-links/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PATCH /api/external-links/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PUT /api/external-links/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/google-auth/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to 4096

GET /api/google-auth/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/google-auth/{uuid}/authorize/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

POST /api/lexis-links/

- Extensions changed
  - Deleted extension: x-permissions

GET /api/managed-rancher-cluster-resources/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [renewal_date]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: renewal_date
              - Modified property: creation_order
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: start_date
                      - New property: url
                      - Modified property: state
                        - Property 'AllOf' changed
                          - Modified schema: #/components/schemas/OrderState
                            - New enum values: [pending-start-date]
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: start_date
                      - New property: url
                      - Modified property: state
                        - Property 'AllOf' changed
                          - Modified schema: #/components/schemas/OrderState
                            - New enum values: [pending-start-date]

GET /api/managed-rancher-cluster-resources/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [renewal_date]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: renewal_date
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: start_date
                    - New property: url
                    - Modified property: state
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/OrderState
                          - New enum values: [pending-start-date]
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: start_date
                    - New property: url
                    - Modified property: state
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/OrderState
                          - New enum values: [pending-start-date]

GET /api/marketplace-categories/

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
                    - Modified property: description
                      - MaxLength changed from 2000 to 4096

POST /api/marketplace-categories/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096

GET /api/marketplace-categories/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096

PATCH /api/marketplace-categories/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096

PUT /api/marketplace-categories/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096

GET /api/marketplace-category-components/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to 4096

POST /api/marketplace-category-components/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/marketplace-category-components/{id}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PATCH /api/marketplace-category-components/{id}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PUT /api/marketplace-category-components/{id}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/marketplace-component-usages/

- New query param: billing_period_month
- New query param: billing_period_year
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to 4096

HEAD /api/marketplace-component-usages/

- New query param: billing_period_month
- New query param: billing_period_year

GET /api/marketplace-component-usages/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/marketplace-component-user-usages/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to 4096

GET /api/marketplace-component-user-usages/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/marketplace-course-accounts/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to 4096

POST /api/marketplace-course-accounts/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

POST /api/marketplace-course-accounts/create_bulk/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: course_accounts
            - Items changed
              - Properties changed
                - Modified property: description
                  - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: course_accounts
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096

GET /api/marketplace-course-accounts/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

POST /api/marketplace-offering-terms-of-service/

- Extensions changed
  - Deleted extension: x-permissions

GET /api/marketplace-offering-users/checklist-template/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: initial_visible_questions
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096
            - Modified property: questions
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096

GET /api/marketplace-orders/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [start_date url]
- Modified query param: query
  - Description changed from 'Search by order UUID, project name or resource name' to 'Search by order UUID, slug, project name or resource name'
- Modified query param: state
  - Schema changed
    - Items changed
      - New enum values: [pending-start-date]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: start_date
              - New property: url
              - Modified property: state
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderState
                    - New enum values: [pending-start-date]

HEAD /api/marketplace-orders/

- Modified query param: query
  - Description changed from 'Search by order UUID, project name or resource name' to 'Search by order UUID, slug, project name or resource name'
- Modified query param: state
  - Schema changed
    - Items changed
      - New enum values: [pending-start-date]

POST /api/marketplace-orders/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: attributes
            - Property 'OneOf' changed
              - Modified schema: #/components/schemas/AzureVirtualMachineCreateOrderAttributes
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096
              - Modified schema: #/components/schemas/AzureSQLServerCreateOrderAttributes
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096
              - Modified schema: #/components/schemas/OpenStackTenantCreateOrderAttributes
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096
              - Modified schema: #/components/schemas/OpenStackInstanceCreateOrderAttributes
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096
              - Modified schema: #/components/schemas/OpenStackVolumeCreateOrderAttributes
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096
              - Modified schema: #/components/schemas/SlurmInvoicesSlurmPackageCreateOrderAttributes
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096
              - Modified schema: #/components/schemas/VMwareVirtualMachineCreateOrderAttributes
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: state
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderState
                  - New enum values: [pending-start-date]

GET /api/marketplace-orders/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [start_date url]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: start_date
            - New property: url
            - Modified property: state
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderState
                  - New enum values: [pending-start-date]

GET /api/marketplace-orders/{uuid}/offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: partitions
            - New property: software_catalogs
            - Modified property: components
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096
            - Modified property: description
              - MaxLength changed from 2000 to 4096
            - Modified property: plans
              - Items changed
                - Properties changed
                  - New property: components
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: backend_id_display_label
                    - New property: create_orders_on_resource_option_change
                    - New property: enable_purchase_order_upload
                    - New property: highlight_backend_id_display
                    - New property: require_purchase_order_upload
                    - Deleted property: order_supports_comments_and_metadata
            - Modified property: promotion_campaigns
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096
            - Modified property: screenshots
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096

GET /api/marketplace-plan-components/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: discount_rate
              - New property: discount_threshold

GET /api/marketplace-plan-components/{id}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: discount_rate
            - New property: discount_threshold

GET /api/marketplace-plans/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: components
            - Properties changed
              - New property: components

POST /api/marketplace-plans/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: components
          - Properties changed
            - New property: components

GET /api/marketplace-plans/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: components
          - Properties changed
            - New property: components

PATCH /api/marketplace-plans/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: components
          - Properties changed
            - New property: components

PUT /api/marketplace-plans/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: components
          - Properties changed
            - New property: components

GET /api/marketplace-project-update-requests/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: new_description
                - MaxLength changed from 2000 to 4096
              - Modified property: old_description
                - MaxLength changed from 2000 to 4096

GET /api/marketplace-project-update-requests/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: new_description
              - MaxLength changed from 2000 to 4096
            - Modified property: old_description
              - MaxLength changed from 2000 to 4096

GET /api/marketplace-provider-offerings/

- New query param: query
- New query param: user_has_offering_user
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [partitions software_catalogs]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: partitions
              - New property: software_catalogs
              - Modified property: components
                - Items changed
                  - Properties changed
                    - Modified property: description
                      - MaxLength changed from 2000 to 4096
              - Modified property: description
                - MaxLength changed from 2000 to 4096
              - Modified property: plans
                - Items changed
                  - Properties changed
                    - New property: components
              - Modified property: plugin_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedPluginOptions
                    - Properties changed
                      - New property: backend_id_display_label
                      - New property: create_orders_on_resource_option_change
                      - New property: enable_purchase_order_upload
                      - New property: highlight_backend_id_display
                      - New property: require_purchase_order_upload
                      - Deleted property: order_supports_comments_and_metadata
              - Modified property: screenshots
                - Items changed
                  - Properties changed
                    - Modified property: description
                      - MaxLength changed from 2000 to 4096

HEAD /api/marketplace-provider-offerings/

- New query param: query
- New query param: user_has_offering_user

POST /api/marketplace-provider-offerings/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: components
            - Items changed
              - Properties changed
                - Modified property: description
                  - MaxLength changed from 2000 to 4096
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Modified property: components
            - Items changed
              - Properties changed
                - Modified property: description
                  - MaxLength changed from 2000 to 4096
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Modified property: components
            - Items changed
              - Properties changed
                - Modified property: description
                  - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: partitions
            - New required property: software_catalogs
          - Properties changed
            - New property: partitions
            - New property: software_catalogs
            - Modified property: components
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096
            - Modified property: plans
              - Items changed
                - Properties changed
                  - New property: components
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: backend_id_display_label
                    - New property: create_orders_on_resource_option_change
                    - New property: enable_purchase_order_upload
                    - New property: highlight_backend_id_display
                    - New property: require_purchase_order_upload
                    - Deleted property: order_supports_comments_and_metadata
            - Modified property: screenshots
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096

GET /api/marketplace-provider-offerings/groups/

- New query param: query
- New query param: user_has_offering_user

HEAD /api/marketplace-provider-offerings/groups/

- New query param: query
- New query param: user_has_offering_user

GET /api/marketplace-provider-offerings/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [partitions software_catalogs]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: partitions
            - New property: software_catalogs
            - Modified property: components
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096
            - Modified property: description
              - MaxLength changed from 2000 to 4096
            - Modified property: plans
              - Items changed
                - Properties changed
                  - New property: components
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: backend_id_display_label
                    - New property: create_orders_on_resource_option_change
                    - New property: enable_purchase_order_upload
                    - New property: highlight_backend_id_display
                    - New property: require_purchase_order_upload
                    - Deleted property: order_supports_comments_and_metadata
            - Modified property: screenshots
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096

POST /api/marketplace-provider-offerings/{uuid}/add_user/

- Responses changed
  - New response: 400

GET /api/marketplace-provider-offerings/{uuid}/component_stats/

- New query param: query
- New query param: user_has_offering_user

GET /api/marketplace-provider-offerings/{uuid}/costs/

- New query param: query
- New query param: user_has_offering_user

POST /api/marketplace-provider-offerings/{uuid}/create_offering_component/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - New response: 201
  - Deleted response: 200

GET /api/marketplace-provider-offerings/{uuid}/customers/

- New query param: query
- New query param: user_has_offering_user

POST /api/marketplace-provider-offerings/{uuid}/import_resource/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: renewal_date
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: start_date
                    - New property: url
                    - Modified property: state
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/OrderState
                          - New enum values: [pending-start-date]
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: start_date
                    - New property: url
                    - Modified property: state
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/OrderState
                          - New enum values: [pending-start-date]

GET /api/marketplace-provider-offerings/{uuid}/list_course_accounts/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [partitions software_catalogs]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: partitions
            - New property: software_catalogs
            - Modified property: components
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096
            - Modified property: description
              - MaxLength changed from 2000 to 4096
            - Modified property: plans
              - Items changed
                - Properties changed
                  - New property: components
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: backend_id_display_label
                    - New property: create_orders_on_resource_option_change
                    - New property: enable_purchase_order_upload
                    - New property: highlight_backend_id_display
                    - New property: require_purchase_order_upload
                    - Deleted property: order_supports_comments_and_metadata
            - Modified property: screenshots
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096

GET /api/marketplace-provider-offerings/{uuid}/list_customer_projects/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: is_removed
              - New property: staff_notes
              - New property: termination_metadata

GET /api/marketplace-provider-offerings/{uuid}/list_customer_service_accounts/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [partitions software_catalogs]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: partitions
            - New property: software_catalogs
            - Modified property: components
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096
            - Modified property: description
              - MaxLength changed from 2000 to 4096
            - Modified property: plans
              - Items changed
                - Properties changed
                  - New property: components
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: backend_id_display_label
                    - New property: create_orders_on_resource_option_change
                    - New property: enable_purchase_order_upload
                    - New property: highlight_backend_id_display
                    - New property: require_purchase_order_upload
                    - Deleted property: order_supports_comments_and_metadata
            - Modified property: screenshots
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096

GET /api/marketplace-provider-offerings/{uuid}/list_customer_users/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: ip_address
              - Modified property: description
                - MaxLength changed from 2000 to 4096

GET /api/marketplace-provider-offerings/{uuid}/list_project_service_accounts/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [partitions software_catalogs]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: partitions
            - New property: software_catalogs
            - Modified property: components
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096
            - Modified property: description
              - MaxLength changed from 2000 to 4096
            - Modified property: plans
              - Items changed
                - Properties changed
                  - New property: components
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: backend_id_display_label
                    - New property: create_orders_on_resource_option_change
                    - New property: enable_purchase_order_upload
                    - New property: highlight_backend_id_display
                    - New property: require_purchase_order_upload
                    - Deleted property: order_supports_comments_and_metadata
            - Modified property: screenshots
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096

POST /api/marketplace-provider-offerings/{uuid}/move_offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: partitions
            - New property: software_catalogs
            - Modified property: components
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096
            - Modified property: description
              - MaxLength changed from 2000 to 4096
            - Modified property: plans
              - Items changed
                - Properties changed
                  - New property: components
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: backend_id_display_label
                    - New property: create_orders_on_resource_option_change
                    - New property: enable_purchase_order_upload
                    - New property: highlight_backend_id_display
                    - New property: require_purchase_order_upload
                    - Deleted property: order_supports_comments_and_metadata
            - Modified property: promotion_campaigns
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096
            - Modified property: screenshots
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096

GET /api/marketplace-provider-offerings/{uuid}/orders/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: start_date
              - New property: url
              - Modified property: state
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderState
                    - New enum values: [pending-start-date]

GET /api/marketplace-provider-offerings/{uuid}/orders/{order_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: start_date
            - New property: url
            - Modified property: state
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderState
                  - New enum values: [pending-start-date]

GET /api/marketplace-provider-offerings/{uuid}/stats/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [partitions software_catalogs]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: partitions
            - New property: software_catalogs
            - Modified property: components
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096
            - Modified property: description
              - MaxLength changed from 2000 to 4096
            - Modified property: plans
              - Items changed
                - Properties changed
                  - New property: components
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: backend_id_display_label
                    - New property: create_orders_on_resource_option_change
                    - New property: enable_purchase_order_upload
                    - New property: highlight_backend_id_display
                    - New property: require_purchase_order_upload
                    - Deleted property: order_supports_comments_and_metadata
            - Modified property: screenshots
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096

POST /api/marketplace-provider-offerings/{uuid}/update_image/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: partitions
            - New property: software_catalogs
            - Modified property: components
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096
            - Modified property: description
              - MaxLength changed from 2000 to 4096
            - Modified property: plans
              - Items changed
                - Properties changed
                  - New property: components
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: backend_id_display_label
                    - New property: create_orders_on_resource_option_change
                    - New property: enable_purchase_order_upload
                    - New property: highlight_backend_id_display
                    - New property: require_purchase_order_upload
                    - Deleted property: order_supports_comments_and_metadata
            - Modified property: screenshots
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096

POST /api/marketplace-provider-offerings/{uuid}/update_integration/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: plugin_options
            - Properties changed
              - New property: backend_id_display_label
              - New property: create_orders_on_resource_option_change
              - New property: enable_purchase_order_upload
              - New property: highlight_backend_id_display
              - New property: require_purchase_order_upload
              - Deleted property: order_supports_comments_and_metadata

POST /api/marketplace-provider-offerings/{uuid}/update_offering_component/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096

GET /api/marketplace-provider-offerings/{uuid}/user_has_resource_access/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [partitions software_catalogs]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: partitions
            - New property: software_catalogs
            - Modified property: components
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096
            - Modified property: description
              - MaxLength changed from 2000 to 4096
            - Modified property: plans
              - Items changed
                - Properties changed
                  - New property: components
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: backend_id_display_label
                    - New property: create_orders_on_resource_option_change
                    - New property: enable_purchase_order_upload
                    - New property: highlight_backend_id_display
                    - New property: require_purchase_order_upload
                    - Deleted property: order_supports_comments_and_metadata
            - Modified property: screenshots
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096

GET /api/marketplace-provider-resources/

- New query param: component_count
- New query param: limit_based
- New query param: limit_component_count
- New query param: only_limit_based
- New query param: only_usage_based
- New query param: usage_based
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [renewal_date]
- Modified query param: query
  - Description changed from 'Search by resource UUID, name, backend ID, effective ID, IPs or hypervisor' to 'Search by resource UUID, name, slug, backend ID, effective ID, IPs or hypervisor'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: renewal_date
              - Modified property: creation_order
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: start_date
                      - New property: url
                      - Modified property: state
                        - Property 'AllOf' changed
                          - Modified schema: #/components/schemas/OrderState
                            - New enum values: [pending-start-date]
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: start_date
                      - New property: url
                      - Modified property: state
                        - Property 'AllOf' changed
                          - Modified schema: #/components/schemas/OrderState
                            - New enum values: [pending-start-date]

HEAD /api/marketplace-provider-resources/

- New query param: component_count
- New query param: limit_based
- New query param: limit_component_count
- New query param: only_limit_based
- New query param: only_usage_based
- New query param: usage_based
- Modified query param: query
  - Description changed from 'Search by resource UUID, name, backend ID, effective ID, IPs or hypervisor' to 'Search by resource UUID, name, slug, backend ID, effective ID, IPs or hypervisor'

GET /api/marketplace-provider-resources/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [renewal_date]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: renewal_date
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: start_date
                    - New property: url
                    - Modified property: state
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/OrderState
                          - New enum values: [pending-start-date]
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: start_date
                    - New property: url
                    - Modified property: state
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/OrderState
                          - New enum values: [pending-start-date]

PATCH /api/marketplace-provider-resources/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PUT /api/marketplace-provider-resources/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/marketplace-provider-resources/{uuid}/details/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [renewal_date]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: renewal_date
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: start_date
                    - New property: url
                    - Modified property: state
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/OrderState
                          - New enum values: [pending-start-date]
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: start_date
                    - New property: url
                    - Modified property: state
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/OrderState
                          - New enum values: [pending-start-date]

POST /api/marketplace-provider-resources/{uuid}/move_resource/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: renewal_date
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: start_date
                    - New property: url
                    - Modified property: state
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/OrderState
                          - New enum values: [pending-start-date]
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: start_date
                    - New property: url
                    - Modified property: state
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/OrderState
                          - New enum values: [pending-start-date]

GET /api/marketplace-provider-resources/{uuid}/offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: partitions
            - New property: software_catalogs
            - Modified property: components
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096
            - Modified property: description
              - MaxLength changed from 2000 to 4096
            - Modified property: plans
              - Items changed
                - Properties changed
                  - New property: components
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: backend_id_display_label
                    - New property: create_orders_on_resource_option_change
                    - New property: enable_purchase_order_upload
                    - New property: highlight_backend_id_display
                    - New property: require_purchase_order_upload
                    - Deleted property: order_supports_comments_and_metadata
            - Modified property: promotion_campaigns
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096
            - Modified property: screenshots
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096

GET /api/marketplace-provider-resources/{uuid}/plan_periods/

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
                    - Modified property: description
                      - MaxLength changed from 2000 to 4096

POST /api/marketplace-provider-resources/{uuid}/set_end_date_by_provider/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: renewal_date
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: start_date
                    - New property: url
                    - Modified property: state
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/OrderState
                          - New enum values: [pending-start-date]
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: start_date
                    - New property: url
                    - Modified property: state
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/OrderState
                          - New enum values: [pending-start-date]

GET /api/marketplace-provider-resources/{uuid}/team/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: offering_user_state
                - Property 'OneOf' changed
                  - Schemas added: #/components/schemas/OfferingUserState, #/components/schemas/NullEnum
                - Property 'AllOf' changed
                  - Schemas deleted: #/components/schemas/OfferingUserState
                - Nullable changed from false to true

GET /api/marketplace-public-offerings/

- New query param: query
- New query param: user_has_offering_user
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [partitions software_catalogs]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: partitions
              - New property: software_catalogs
              - Modified property: components
                - Items changed
                  - Properties changed
                    - Modified property: description
                      - MaxLength changed from 2000 to 4096
              - Modified property: description
                - MaxLength changed from 2000 to 4096
              - Modified property: plans
                - Items changed
                  - Properties changed
                    - New property: components
              - Modified property: plugin_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedPluginOptions
                    - Properties changed
                      - New property: backend_id_display_label
                      - New property: create_orders_on_resource_option_change
                      - New property: enable_purchase_order_upload
                      - New property: highlight_backend_id_display
                      - New property: require_purchase_order_upload
                      - Deleted property: order_supports_comments_and_metadata
              - Modified property: promotion_campaigns
                - Items changed
                  - Properties changed
                    - Modified property: description
                      - MaxLength changed from 2000 to 4096
              - Modified property: screenshots
                - Items changed
                  - Properties changed
                    - Modified property: description
                      - MaxLength changed from 2000 to 4096

HEAD /api/marketplace-public-offerings/

- New query param: query
- New query param: user_has_offering_user

GET /api/marketplace-public-offerings/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [partitions software_catalogs]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: partitions
            - New property: software_catalogs
            - Modified property: components
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096
            - Modified property: description
              - MaxLength changed from 2000 to 4096
            - Modified property: plans
              - Items changed
                - Properties changed
                  - New property: components
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: backend_id_display_label
                    - New property: create_orders_on_resource_option_change
                    - New property: enable_purchase_order_upload
                    - New property: highlight_backend_id_display
                    - New property: require_purchase_order_upload
                    - Deleted property: order_supports_comments_and_metadata
            - Modified property: promotion_campaigns
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096
            - Modified property: screenshots
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096

GET /api/marketplace-public-offerings/{uuid}/plans/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: components

GET /api/marketplace-public-offerings/{uuid}/plans/{plan_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: components

GET /api/marketplace-resources/

- New query param: component_count
- New query param: limit_based
- New query param: limit_component_count
- New query param: only_limit_based
- New query param: only_usage_based
- New query param: usage_based
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [renewal_date]
- Modified query param: query
  - Description changed from 'Search by resource UUID, name, backend ID, effective ID, IPs or hypervisor' to 'Search by resource UUID, name, slug, backend ID, effective ID, IPs or hypervisor'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: renewal_date
              - Modified property: creation_order
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: start_date
                      - New property: url
                      - Modified property: state
                        - Property 'AllOf' changed
                          - Modified schema: #/components/schemas/OrderState
                            - New enum values: [pending-start-date]
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: start_date
                      - New property: url
                      - Modified property: state
                        - Property 'AllOf' changed
                          - Modified schema: #/components/schemas/OrderState
                            - New enum values: [pending-start-date]

HEAD /api/marketplace-resources/

- New query param: component_count
- New query param: limit_based
- New query param: limit_component_count
- New query param: only_limit_based
- New query param: only_usage_based
- New query param: usage_based
- Modified query param: query
  - Description changed from 'Search by resource UUID, name, backend ID, effective ID, IPs or hypervisor' to 'Search by resource UUID, name, slug, backend ID, effective ID, IPs or hypervisor'

GET /api/marketplace-resources/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [renewal_date]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: renewal_date
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: start_date
                    - New property: url
                    - Modified property: state
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/OrderState
                          - New enum values: [pending-start-date]
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: start_date
                    - New property: url
                    - Modified property: state
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/OrderState
                          - New enum values: [pending-start-date]

PATCH /api/marketplace-resources/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PUT /api/marketplace-resources/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/marketplace-resources/{uuid}/details/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [renewal_date]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: renewal_date
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: start_date
                    - New property: url
                    - Modified property: state
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/OrderState
                          - New enum values: [pending-start-date]
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: start_date
                    - New property: url
                    - Modified property: state
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/OrderState
                          - New enum values: [pending-start-date]

POST /api/marketplace-resources/{uuid}/move_resource/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: renewal_date
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: start_date
                    - New property: url
                    - Modified property: state
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/OrderState
                          - New enum values: [pending-start-date]
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: start_date
                    - New property: url
                    - Modified property: state
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/OrderState
                          - New enum values: [pending-start-date]

GET /api/marketplace-resources/{uuid}/offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: partitions
            - New property: software_catalogs
            - Modified property: components
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096
            - Modified property: description
              - MaxLength changed from 2000 to 4096
            - Modified property: plans
              - Items changed
                - Properties changed
                  - New property: components
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: backend_id_display_label
                    - New property: create_orders_on_resource_option_change
                    - New property: enable_purchase_order_upload
                    - New property: highlight_backend_id_display
                    - New property: require_purchase_order_upload
                    - Deleted property: order_supports_comments_and_metadata
            - Modified property: promotion_campaigns
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096
            - Modified property: screenshots
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096

GET /api/marketplace-resources/{uuid}/plan_periods/

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
                    - Modified property: description
                      - MaxLength changed from 2000 to 4096

GET /api/marketplace-resources/{uuid}/team/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: offering_user_state
                - Property 'OneOf' changed
                  - Schemas added: #/components/schemas/OfferingUserState, #/components/schemas/NullEnum
                - Property 'AllOf' changed
                  - Schemas deleted: #/components/schemas/OfferingUserState
                - Nullable changed from false to true

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
                      - New property: backend_id_display_label
                      - New property: create_orders_on_resource_option_change
                      - New property: enable_purchase_order_upload
                      - New property: highlight_backend_id_display
                      - New property: require_purchase_order_upload
                      - Deleted property: order_supports_comments_and_metadata

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
                    - New property: backend_id_display_label
                    - New property: create_orders_on_resource_option_change
                    - New property: enable_purchase_order_upload
                    - New property: highlight_backend_id_display
                    - New property: require_purchase_order_upload
                    - Deleted property: order_supports_comments_and_metadata

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
                    - New property: backend_id_display_label
                    - New property: create_orders_on_resource_option_change
                    - New property: enable_purchase_order_upload
                    - New property: highlight_backend_id_display
                    - New property: require_purchase_order_upload
                    - Deleted property: order_supports_comments_and_metadata

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
                    - New property: backend_id_display_label
                    - New property: create_orders_on_resource_option_change
                    - New property: enable_purchase_order_upload
                    - New property: highlight_backend_id_display
                    - New property: require_purchase_order_upload
                    - Deleted property: order_supports_comments_and_metadata

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
                    - New property: backend_id_display_label
                    - New property: create_orders_on_resource_option_change
                    - New property: enable_purchase_order_upload
                    - New property: highlight_backend_id_display
                    - New property: require_purchase_order_upload
                    - Deleted property: order_supports_comments_and_metadata

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
                    - New property: backend_id_display_label
                    - New property: create_orders_on_resource_option_change
                    - New property: enable_purchase_order_upload
                    - New property: highlight_backend_id_display
                    - New property: require_purchase_order_upload
                    - Deleted property: order_supports_comments_and_metadata

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
                    - New property: backend_id_display_label
                    - New property: create_orders_on_resource_option_change
                    - New property: enable_purchase_order_upload
                    - New property: highlight_backend_id_display
                    - New property: require_purchase_order_upload
                    - Deleted property: order_supports_comments_and_metadata

GET /api/marketplace-screenshots/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to 4096

POST /api/marketplace-screenshots/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/marketplace-screenshots/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PATCH /api/marketplace-screenshots/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PUT /api/marketplace-screenshots/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

POST /api/marketplace-script-dry-run/{uuid}/async_run/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: partitions
            - New property: software_catalogs
            - Modified property: components
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096
            - Modified property: description
              - MaxLength changed from 2000 to 4096
            - Modified property: plans
              - Items changed
                - Properties changed
                  - New property: components
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: backend_id_display_label
                    - New property: create_orders_on_resource_option_change
                    - New property: enable_purchase_order_upload
                    - New property: highlight_backend_id_display
                    - New property: require_purchase_order_upload
                    - Deleted property: order_supports_comments_and_metadata
            - Modified property: promotion_campaigns
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096
            - Modified property: screenshots
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096

POST /api/marketplace-script-dry-run/{uuid}/run/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: partitions
            - New property: software_catalogs
            - Modified property: components
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096
            - Modified property: description
              - MaxLength changed from 2000 to 4096
            - Modified property: plans
              - Items changed
                - Properties changed
                  - New property: components
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: backend_id_display_label
                    - New property: create_orders_on_resource_option_change
                    - New property: enable_purchase_order_upload
                    - New property: highlight_backend_id_display
                    - New property: require_purchase_order_upload
                    - Deleted property: order_supports_comments_and_metadata
            - Modified property: promotion_campaigns
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096
            - Modified property: screenshots
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096

GET /api/marketplace-service-providers/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to 4096

POST /api/marketplace-service-providers/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/marketplace-service-providers/{service_provider_uuid}/course_accounts/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to 4096

GET /api/marketplace-service-providers/{service_provider_uuid}/customer_projects/

- New query param: is_removed
- Modified query param: query
  - Description changed from 'Filter by name, UUID, backend ID or resource effective ID' to 'Filter by name, slug, UUID, backend ID or resource effective ID'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to 4096

GET /api/marketplace-service-providers/{service_provider_uuid}/offerings/

- New query param: query
- New query param: user_has_offering_user
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
                    - Modified property: description
                      - MaxLength changed from 2000 to 4096
              - Modified property: plans
                - Items changed
                  - Properties changed
                    - New property: components

GET /api/marketplace-service-providers/{service_provider_uuid}/projects/

- New query param: is_removed
- Deleted query param: field
- Modified query param: query
  - Description changed from 'Filter by name, UUID, backend ID or resource effective ID' to 'Filter by name, slug, UUID, backend ID or resource effective ID'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: is_removed
              - New property: staff_notes
              - New property: termination_metadata

GET /api/marketplace-service-providers/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PATCH /api/marketplace-service-providers/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PUT /api/marketplace-service-providers/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

POST /api/marketplace-service-providers/{uuid}/add_user/

- Responses changed
  - New response: 400

POST /api/marketplace-service-providers/{uuid}/set_offerings_username/

- Responses changed
  - New response: 201
  - Deleted response: 200

GET /api/notification-messages/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to 4096

POST /api/notification-messages/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/notification-messages/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PATCH /api/notification-messages/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PUT /api/notification-messages/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/onboarding-justifications/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: legal_name
              - New required property: legal_person_identifier
              - Deleted required property: user_justification
            - Properties changed
              - New property: legal_name
              - New property: legal_person_identifier
              - Modified property: user_justification
                - Nullable changed from false to true

POST /api/onboarding-justifications/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Required changed
          - Deleted required property: user_justification
        - Properties changed
          - Modified property: user_justification
            - Nullable changed from false to true
            - MinLength changed from 1 to 0
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: legal_name
            - New required property: legal_person_identifier
            - Deleted required property: user_justification
          - Properties changed
            - New property: legal_name
            - New property: legal_person_identifier
            - Modified property: user_justification
              - Nullable changed from false to true

POST /api/onboarding-justifications/create_justification/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Required changed
          - Deleted required property: user_justification
        - Properties changed
          - Modified property: user_justification
            - MinLength changed from 1 to 0
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: legal_name
            - New required property: legal_person_identifier
            - Deleted required property: user_justification
          - Properties changed
            - New property: legal_name
            - New property: legal_person_identifier
            - Modified property: user_justification
              - Nullable changed from false to true

GET /api/onboarding-justifications/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: legal_name
            - New required property: legal_person_identifier
            - Deleted required property: user_justification
          - Properties changed
            - New property: legal_name
            - New property: legal_person_identifier
            - Modified property: user_justification
              - Nullable changed from false to true

PATCH /api/onboarding-justifications/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: user_justification
            - Nullable changed from false to true
            - MinLength changed from 1 to 0
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: legal_name
            - New required property: legal_person_identifier
            - Deleted required property: user_justification
          - Properties changed
            - New property: legal_name
            - New property: legal_person_identifier
            - Modified property: user_justification
              - Nullable changed from false to true

PUT /api/onboarding-justifications/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Required changed
          - Deleted required property: user_justification
        - Properties changed
          - Modified property: user_justification
            - Nullable changed from false to true
            - MinLength changed from 1 to 0
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: legal_name
            - New required property: legal_person_identifier
            - Deleted required property: user_justification
          - Properties changed
            - New property: legal_name
            - New property: legal_person_identifier
            - Modified property: user_justification
              - Nullable changed from false to true

POST /api/onboarding-verifications/{uuid}/create_customer/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/openstack-backups/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to 4096
              - Modified property: instance_ports
                - Items changed
                  - Properties changed
                    - Modified property: security_groups
                      - Items changed
                        - Properties changed
                          - Modified property: description
                            - MaxLength changed from 2000 to 4096
                          - Modified property: rules
                            - Items changed
                              - Properties changed
                                - Modified property: description
                                  - MaxLength changed from 2000 to 4096
              - Modified property: instance_security_groups
                - Items changed
                  - Properties changed
                    - Modified property: rules
                      - Items changed
                        - Properties changed
                          - Modified property: description
                            - MaxLength changed from 2000 to 4096
              - Modified property: restorations
                - Items changed
                  - Properties changed
                    - Modified property: ports
                      - Items changed
                        - Properties changed
                          - Modified property: security_groups
                            - Items changed
                              - Properties changed
                                - Modified property: description
                                  - MaxLength changed from 2000 to 4096
                                - Modified property: rules
                                  - Items changed
                                    - Properties changed
                                      - Modified property: description
                                        - MaxLength changed from 2000 to 4096
                    - Modified property: security_groups
                      - Items changed
                        - Properties changed
                          - Modified property: rules
                            - Items changed
                              - Properties changed
                                - Modified property: description
                                  - MaxLength changed from 2000 to 4096

GET /api/openstack-backups/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096
            - Modified property: instance_ports
              - Items changed
                - Properties changed
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - Modified property: description
                          - MaxLength changed from 2000 to 4096
                        - Modified property: rules
                          - Items changed
                            - Properties changed
                              - Modified property: description
                                - MaxLength changed from 2000 to 4096
            - Modified property: instance_security_groups
              - Items changed
                - Properties changed
                  - Modified property: rules
                    - Items changed
                      - Properties changed
                        - Modified property: description
                          - MaxLength changed from 2000 to 4096
            - Modified property: restorations
              - Items changed
                - Properties changed
                  - Modified property: ports
                    - Items changed
                      - Properties changed
                        - Modified property: security_groups
                          - Items changed
                            - Properties changed
                              - Modified property: description
                                - MaxLength changed from 2000 to 4096
                              - Modified property: rules
                                - Items changed
                                  - Properties changed
                                    - Modified property: description
                                      - MaxLength changed from 2000 to 4096
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - Modified property: rules
                          - Items changed
                            - Properties changed
                              - Modified property: description
                                - MaxLength changed from 2000 to 4096

PATCH /api/openstack-backups/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096
            - Modified property: instance_ports
              - Items changed
                - Properties changed
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - Modified property: description
                          - MaxLength changed from 2000 to 4096
                        - Modified property: rules
                          - Items changed
                            - Properties changed
                              - Modified property: description
                                - MaxLength changed from 2000 to 4096
            - Modified property: instance_security_groups
              - Items changed
                - Properties changed
                  - Modified property: rules
                    - Items changed
                      - Properties changed
                        - Modified property: description
                          - MaxLength changed from 2000 to 4096
            - Modified property: restorations
              - Items changed
                - Properties changed
                  - Modified property: ports
                    - Items changed
                      - Properties changed
                        - Modified property: security_groups
                          - Items changed
                            - Properties changed
                              - Modified property: description
                                - MaxLength changed from 2000 to 4096
                              - Modified property: rules
                                - Items changed
                                  - Properties changed
                                    - Modified property: description
                                      - MaxLength changed from 2000 to 4096
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - Modified property: rules
                          - Items changed
                            - Properties changed
                              - Modified property: description
                                - MaxLength changed from 2000 to 4096

PUT /api/openstack-backups/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096
            - Modified property: instance_ports
              - Items changed
                - Properties changed
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - Modified property: description
                          - MaxLength changed from 2000 to 4096
                        - Modified property: rules
                          - Items changed
                            - Properties changed
                              - Modified property: description
                                - MaxLength changed from 2000 to 4096
            - Modified property: instance_security_groups
              - Items changed
                - Properties changed
                  - Modified property: rules
                    - Items changed
                      - Properties changed
                        - Modified property: description
                          - MaxLength changed from 2000 to 4096
            - Modified property: restorations
              - Items changed
                - Properties changed
                  - Modified property: ports
                    - Items changed
                      - Properties changed
                        - Modified property: security_groups
                          - Items changed
                            - Properties changed
                              - Modified property: description
                                - MaxLength changed from 2000 to 4096
                              - Modified property: rules
                                - Items changed
                                  - Properties changed
                                    - Modified property: description
                                      - MaxLength changed from 2000 to 4096
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - Modified property: rules
                          - Items changed
                            - Properties changed
                              - Modified property: description
                                - MaxLength changed from 2000 to 4096

POST /api/openstack-backups/{uuid}/restore/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096
            - Modified property: ports
              - Items changed
                - Properties changed
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - Modified property: description
                          - MaxLength changed from 2000 to 4096
                        - Modified property: rules
                          - Items changed
                            - Properties changed
                              - Modified property: description
                                - MaxLength changed from 2000 to 4096
            - Modified property: security_groups
              - Items changed
                - Properties changed
                  - Modified property: rules
                    - Items changed
                      - Properties changed
                        - Modified property: description
                          - MaxLength changed from 2000 to 4096

GET /api/openstack-instances/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to 4096
              - Modified property: ports
                - Items changed
                  - Properties changed
                    - Modified property: security_groups
                      - Items changed
                        - Properties changed
                          - Modified property: description
                            - MaxLength changed from 2000 to 4096
                          - Modified property: rules
                            - Items changed
                              - Properties changed
                                - Modified property: description
                                  - MaxLength changed from 2000 to 4096
              - Modified property: security_groups
                - Items changed
                  - Properties changed
                    - Modified property: rules
                      - Items changed
                        - Properties changed
                          - Modified property: description
                            - MaxLength changed from 2000 to 4096

GET /api/openstack-instances/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096
            - Modified property: ports
              - Items changed
                - Properties changed
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - Modified property: description
                          - MaxLength changed from 2000 to 4096
                        - Modified property: rules
                          - Items changed
                            - Properties changed
                              - Modified property: description
                                - MaxLength changed from 2000 to 4096
            - Modified property: security_groups
              - Items changed
                - Properties changed
                  - Modified property: rules
                    - Items changed
                      - Properties changed
                        - Modified property: description
                          - MaxLength changed from 2000 to 4096

PATCH /api/openstack-instances/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096
            - Modified property: ports
              - Items changed
                - Properties changed
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - Modified property: description
                          - MaxLength changed from 2000 to 4096
                        - Modified property: rules
                          - Items changed
                            - Properties changed
                              - Modified property: description
                                - MaxLength changed from 2000 to 4096
            - Modified property: security_groups
              - Items changed
                - Properties changed
                  - Modified property: rules
                    - Items changed
                      - Properties changed
                        - Modified property: description
                          - MaxLength changed from 2000 to 4096

PUT /api/openstack-instances/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096
            - Modified property: ports
              - Items changed
                - Properties changed
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - Modified property: description
                          - MaxLength changed from 2000 to 4096
                        - Modified property: rules
                          - Items changed
                            - Properties changed
                              - Modified property: description
                                - MaxLength changed from 2000 to 4096
            - Modified property: security_groups
              - Items changed
                - Properties changed
                  - Modified property: rules
                    - Items changed
                      - Properties changed
                        - Modified property: description
                          - MaxLength changed from 2000 to 4096

POST /api/openstack-instances/{uuid}/backup/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096
            - Modified property: instance_ports
              - Items changed
                - Properties changed
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - Modified property: description
                          - MaxLength changed from 2000 to 4096
                        - Modified property: rules
                          - Items changed
                            - Properties changed
                              - Modified property: description
                                - MaxLength changed from 2000 to 4096
            - Modified property: instance_security_groups
              - Items changed
                - Properties changed
                  - Modified property: rules
                    - Items changed
                      - Properties changed
                        - Modified property: description
                          - MaxLength changed from 2000 to 4096
            - Modified property: restorations
              - Items changed
                - Properties changed
                  - Modified property: ports
                    - Items changed
                      - Properties changed
                        - Modified property: security_groups
                          - Items changed
                            - Properties changed
                              - Modified property: description
                                - MaxLength changed from 2000 to 4096
                              - Modified property: rules
                                - Items changed
                                  - Properties changed
                                    - Modified property: description
                                      - MaxLength changed from 2000 to 4096
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - Modified property: rules
                          - Items changed
                            - Properties changed
                              - Modified property: description
                                - MaxLength changed from 2000 to 4096

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
                    - Modified property: description
                      - MaxLength changed from 2000 to 4096
                    - Modified property: rules
                      - Items changed
                        - Properties changed
                          - Modified property: description
                            - MaxLength changed from 2000 to 4096

GET /api/openstack-networks/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to 4096
              - Modified property: subnets
                - Items changed
                  - Properties changed
                    - Modified property: description
                      - MaxLength changed from 2000 to 4096

GET /api/openstack-networks/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096
            - Modified property: subnets
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096

PATCH /api/openstack-networks/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096
            - Modified property: subnets
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096

PUT /api/openstack-networks/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096
            - Modified property: subnets
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096

POST /api/openstack-networks/{uuid}/create_subnet/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/openstack-ports/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to 4096

POST /api/openstack-ports/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/openstack-ports/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PATCH /api/openstack-ports/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PUT /api/openstack-ports/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/openstack-routers/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to 4096
              - Modified property: ports
                - Items changed
                  - Properties changed
                    - Modified property: security_groups
                      - Items changed
                        - Properties changed
                          - Modified property: description
                            - MaxLength changed from 2000 to 4096
                          - Modified property: rules
                            - Items changed
                              - Properties changed
                                - Modified property: description
                                  - MaxLength changed from 2000 to 4096

GET /api/openstack-routers/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096
            - Modified property: ports
              - Items changed
                - Properties changed
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - Modified property: description
                          - MaxLength changed from 2000 to 4096
                        - Modified property: rules
                          - Items changed
                            - Properties changed
                              - Modified property: description
                                - MaxLength changed from 2000 to 4096

GET /api/openstack-security-groups/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to 4096
              - Modified property: rules
                - Items changed
                  - Properties changed
                    - Modified property: description
                      - MaxLength changed from 2000 to 4096

GET /api/openstack-security-groups/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096
            - Modified property: rules
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096

PATCH /api/openstack-security-groups/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PUT /api/openstack-security-groups/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

POST /api/openstack-security-groups/{uuid}/set_rules/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Items changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/openstack-server-groups/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to 4096

POST /api/openstack-server-groups/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/openstack-server-groups/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PATCH /api/openstack-server-groups/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PUT /api/openstack-server-groups/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/openstack-snapshots/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to 4096

GET /api/openstack-snapshots/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PATCH /api/openstack-snapshots/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PUT /api/openstack-snapshots/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

POST /api/openstack-snapshots/{uuid}/restore/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/openstack-subnets/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to 4096

GET /api/openstack-subnets/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PATCH /api/openstack-subnets/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PUT /api/openstack-subnets/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/openstack-tenants/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to 4096

POST /api/openstack-tenants/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/openstack-tenants/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PATCH /api/openstack-tenants/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PUT /api/openstack-tenants/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/openstack-tenants/{uuid}/backend_volumes/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to 4096

POST /api/openstack-tenants/{uuid}/create_network/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096
            - Modified property: subnets
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096

POST /api/openstack-tenants/{uuid}/create_security_group/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
          - Modified property: rules
            - Items changed
              - Properties changed
                - Modified property: description
                  - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096
            - Modified property: rules
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096

POST /api/openstack-tenants/{uuid}/create_server_group/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

POST /api/openstack-tenants/{uuid}/pull_security_groups/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

POST /api/openstack-tenants/{uuid}/pull_server_groups/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/openstack-volume-types/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to 4096

GET /api/openstack-volume-types/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/openstack-volumes/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to 4096

GET /api/openstack-volumes/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PATCH /api/openstack-volumes/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PUT /api/openstack-volumes/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

POST /api/openstack-volumes/{uuid}/snapshot/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/override-settings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: ATLASSIAN_OAUTH2_ACCESS_TOKEN
            - New property: ATLASSIAN_OAUTH2_CLIENT_ID
            - New property: ATLASSIAN_OAUTH2_TOKEN_TYPE
            - New property: ATLASSIAN_PERSONAL_ACCESS_TOKEN
            - New property: ATLASSIAN_SUPPORT_TYPE_MAPPING
            - New property: ATLASSIAN_WALDUR_BACKEND_ID_FIELD
            - New property: ENABLE_ORDER_START_DATE
            - New property: PROJECT_END_DATE_MANDATORY
            - Deleted property: ATLASSIAN_PULL_PRIORITIES
            - Deleted property: ATLASSIAN_STRANGE_SETTING
            - Deleted property: ATLASSIAN_USE_AUTOMATIC_REQUEST_MAPPING
            - Deleted property: ATLASSIAN_USE_TEENAGE_API

POST /api/override-settings/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: ATLASSIAN_OAUTH2_ACCESS_TOKEN
          - New property: ATLASSIAN_OAUTH2_CLIENT_ID
          - New property: ATLASSIAN_OAUTH2_TOKEN_TYPE
          - New property: ATLASSIAN_PERSONAL_ACCESS_TOKEN
          - New property: ATLASSIAN_SUPPORT_TYPE_MAPPING
          - New property: ATLASSIAN_WALDUR_BACKEND_ID_FIELD
          - New property: ENABLE_ORDER_START_DATE
          - New property: PROJECT_END_DATE_MANDATORY
          - Deleted property: ATLASSIAN_PULL_PRIORITIES
          - Deleted property: ATLASSIAN_STRANGE_SETTING
          - Deleted property: ATLASSIAN_USE_AUTOMATIC_REQUEST_MAPPING
          - Deleted property: ATLASSIAN_USE_TEENAGE_API
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: ATLASSIAN_OAUTH2_ACCESS_TOKEN
          - New property: ATLASSIAN_OAUTH2_CLIENT_ID
          - New property: ATLASSIAN_OAUTH2_TOKEN_TYPE
          - New property: ATLASSIAN_PERSONAL_ACCESS_TOKEN
          - New property: ATLASSIAN_SUPPORT_TYPE_MAPPING
          - New property: ATLASSIAN_WALDUR_BACKEND_ID_FIELD
          - New property: ENABLE_ORDER_START_DATE
          - New property: PROJECT_END_DATE_MANDATORY
          - Deleted property: ATLASSIAN_PULL_PRIORITIES
          - Deleted property: ATLASSIAN_STRANGE_SETTING
          - Deleted property: ATLASSIAN_USE_AUTOMATIC_REQUEST_MAPPING
          - Deleted property: ATLASSIAN_USE_TEENAGE_API
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: ATLASSIAN_OAUTH2_ACCESS_TOKEN
          - New property: ATLASSIAN_OAUTH2_CLIENT_ID
          - New property: ATLASSIAN_OAUTH2_TOKEN_TYPE
          - New property: ATLASSIAN_PERSONAL_ACCESS_TOKEN
          - New property: ATLASSIAN_SUPPORT_TYPE_MAPPING
          - New property: ATLASSIAN_WALDUR_BACKEND_ID_FIELD
          - New property: ENABLE_ORDER_START_DATE
          - New property: PROJECT_END_DATE_MANDATORY
          - Deleted property: ATLASSIAN_PULL_PRIORITIES
          - Deleted property: ATLASSIAN_STRANGE_SETTING
          - Deleted property: ATLASSIAN_USE_AUTOMATIC_REQUEST_MAPPING
          - Deleted property: ATLASSIAN_USE_TEENAGE_API

GET /api/project-types/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to 4096

GET /api/project-types/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/projects/

- New query param: include_terminated
- New query param: is_removed
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [is_removed staff_notes termination_metadata]
- Modified query param: query
  - Description changed from 'Filter by name, UUID, backend ID or resource effective ID' to 'Filter by name, slug, UUID, backend ID or resource effective ID'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: is_removed
              - New property: staff_notes
              - New property: termination_metadata

HEAD /api/projects/

- New query param: include_terminated
- New query param: is_removed
- Modified query param: query
  - Description changed from 'Filter by name, UUID, backend ID or resource effective ID' to 'Filter by name, slug, UUID, backend ID or resource effective ID'

POST /api/projects/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: staff_notes
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: staff_notes
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: staff_notes
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: is_removed
            - New property: staff_notes
            - New property: termination_metadata

GET /api/projects/checklist-template/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: initial_visible_questions
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096
            - Modified property: questions
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096

GET /api/projects/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [is_removed staff_notes termination_metadata]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: is_removed
            - New property: staff_notes
            - New property: termination_metadata

PATCH /api/projects/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: staff_notes
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: staff_notes
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: staff_notes
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: is_removed
            - New property: staff_notes
            - New property: termination_metadata

PUT /api/projects/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: staff_notes
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: staff_notes
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: staff_notes
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: is_removed
            - New property: staff_notes
            - New property: termination_metadata

POST /api/projects/{uuid}/add_user/

- Responses changed
  - New response: 400

POST /api/projects/{uuid}/move_project/

- Responses changed
  - New response: 400
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: is_removed
            - New property: staff_notes
            - New property: termination_metadata

GET /api/promotions-campaigns/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to 4096

POST /api/promotions-campaigns/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/promotions-campaigns/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PUT /api/promotions-campaigns/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/promotions-campaigns/{uuid}/orders/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: start_date
              - New property: url
              - Modified property: state
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderState
                    - New enum values: [pending-start-date]

GET /api/promotions-campaigns/{uuid}/resources/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: renewal_date
              - Modified property: creation_order
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: start_date
                      - New property: url
                      - Modified property: state
                        - Property 'AllOf' changed
                          - Modified schema: #/components/schemas/OrderState
                            - New enum values: [pending-start-date]
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: start_date
                      - New property: url
                      - Modified property: state
                        - Property 'AllOf' changed
                          - Modified schema: #/components/schemas/OrderState
                            - New enum values: [pending-start-date]

GET /api/proposal-proposals/checklist-template/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: initial_visible_questions
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096
            - Modified property: questions
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096

POST /api/proposal-proposals/{uuid}/add_user/

- Responses changed
  - New response: 400

GET /api/proposal-proposals/{uuid}/resources/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to 4096
              - Modified property: requested_offering
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/NestedRequestedOffering
                    - Properties changed
                      - Modified property: components
                        - Items changed
                          - Properties changed
                            - Modified property: description
                              - MaxLength changed from 2000 to 4096
                      - Modified property: plan_details
                        - Property 'AllOf' changed
                          - Modified schema: #/components/schemas/BasePublicPlan
                            - Properties changed
                              - New property: components

POST /api/proposal-proposals/{uuid}/resources/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096
            - Modified property: requested_offering
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/NestedRequestedOffering
                  - Properties changed
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - Modified property: description
                            - MaxLength changed from 2000 to 4096
                    - Modified property: plan_details
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BasePublicPlan
                          - Properties changed
                            - New property: components

GET /api/proposal-proposals/{uuid}/resources/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096
            - Modified property: requested_offering
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/NestedRequestedOffering
                  - Properties changed
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - Modified property: description
                            - MaxLength changed from 2000 to 4096
                    - Modified property: plan_details
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BasePublicPlan
                          - Properties changed
                            - New property: components

PATCH /api/proposal-proposals/{uuid}/resources/{obj_uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096
            - Modified property: requested_offering
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/NestedRequestedOffering
                  - Properties changed
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - Modified property: description
                            - MaxLength changed from 2000 to 4096
                    - Modified property: plan_details
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BasePublicPlan
                          - Properties changed
                            - New property: components

PUT /api/proposal-proposals/{uuid}/resources/{obj_uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096
            - Modified property: requested_offering
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/NestedRequestedOffering
                  - Properties changed
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - Modified property: description
                            - MaxLength changed from 2000 to 4096
                    - Modified property: plan_details
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BasePublicPlan
                          - Properties changed
                            - New property: components

POST /api/proposal-proposals/{uuid}/update_project_details/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096

GET /api/proposal-protected-calls/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: documents
                - Items changed
                  - Properties changed
                    - Modified property: description
                      - MaxLength changed from 2000 to 4096
              - Modified property: offerings
                - Items changed
                  - Properties changed
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - Modified property: description
                            - MaxLength changed from 2000 to 4096
                    - Modified property: plan_details
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BasePublicPlan
                          - Properties changed
                            - New property: components
              - Modified property: resource_templates
                - Items changed
                  - Properties changed
                    - Modified property: description
                      - MaxLength changed from 2000 to 4096
                    - Modified property: requested_offering_plan
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BasePublicPlan
                          - Properties changed
                            - New property: components

POST /api/proposal-protected-calls/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: documents
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096
            - Modified property: offerings
              - Items changed
                - Properties changed
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - Modified property: description
                          - MaxLength changed from 2000 to 4096
                  - Modified property: plan_details
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - New property: components
            - Modified property: resource_templates
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096
                  - Modified property: requested_offering_plan
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - New property: components

GET /api/proposal-protected-calls/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: documents
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096
            - Modified property: offerings
              - Items changed
                - Properties changed
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - Modified property: description
                          - MaxLength changed from 2000 to 4096
                  - Modified property: plan_details
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - New property: components
            - Modified property: resource_templates
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096
                  - Modified property: requested_offering_plan
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - New property: components

PATCH /api/proposal-protected-calls/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: documents
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096
            - Modified property: offerings
              - Items changed
                - Properties changed
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - Modified property: description
                          - MaxLength changed from 2000 to 4096
                  - Modified property: plan_details
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - New property: components
            - Modified property: resource_templates
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096
                  - Modified property: requested_offering_plan
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - New property: components

PUT /api/proposal-protected-calls/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: documents
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096
            - Modified property: offerings
              - Items changed
                - Properties changed
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - Modified property: description
                          - MaxLength changed from 2000 to 4096
                  - Modified property: plan_details
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - New property: components
            - Modified property: resource_templates
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096
                  - Modified property: requested_offering_plan
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - New property: components

POST /api/proposal-protected-calls/{uuid}/activate/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: documents
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096
            - Modified property: offerings
              - Items changed
                - Properties changed
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - Modified property: description
                          - MaxLength changed from 2000 to 4096
                  - Modified property: plan_details
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - New property: components
            - Modified property: resource_templates
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096
                  - Modified property: requested_offering_plan
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - New property: components

POST /api/proposal-protected-calls/{uuid}/add_user/

- Responses changed
  - New response: 400

POST /api/proposal-protected-calls/{uuid}/archive/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: documents
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096
            - Modified property: offerings
              - Items changed
                - Properties changed
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - Modified property: description
                          - MaxLength changed from 2000 to 4096
                  - Modified property: plan_details
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - New property: components
            - Modified property: resource_templates
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096
                  - Modified property: requested_offering_plan
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - New property: components

GET /api/proposal-protected-calls/{uuid}/offerings/

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
                    - Modified property: description
                      - MaxLength changed from 2000 to 4096
              - Modified property: description
                - MaxLength changed from 2000 to 4096
              - Modified property: plan_details
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/BasePublicPlan
                    - Properties changed
                      - New property: components

POST /api/proposal-protected-calls/{uuid}/offerings/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096
            - Modified property: description
              - MaxLength changed from 2000 to 4096
            - Modified property: plan_details
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BasePublicPlan
                  - Properties changed
                    - New property: components

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
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096
            - Modified property: description
              - MaxLength changed from 2000 to 4096
            - Modified property: plan_details
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BasePublicPlan
                  - Properties changed
                    - New property: components

PATCH /api/proposal-protected-calls/{uuid}/offerings/{obj_uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096
            - Modified property: description
              - MaxLength changed from 2000 to 4096
            - Modified property: plan_details
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BasePublicPlan
                  - Properties changed
                    - New property: components

PUT /api/proposal-protected-calls/{uuid}/offerings/{obj_uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096
            - Modified property: description
              - MaxLength changed from 2000 to 4096
            - Modified property: plan_details
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BasePublicPlan
                  - Properties changed
                    - New property: components

GET /api/proposal-protected-calls/{uuid}/resource_templates/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to 4096
              - Modified property: requested_offering_plan
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/BasePublicPlan
                    - Properties changed
                      - New property: components

POST /api/proposal-protected-calls/{uuid}/resource_templates/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096
            - Modified property: requested_offering_plan
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BasePublicPlan
                  - Properties changed
                    - New property: components

GET /api/proposal-protected-calls/{uuid}/resource_templates/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096
            - Modified property: requested_offering_plan
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BasePublicPlan
                  - Properties changed
                    - New property: components

PATCH /api/proposal-protected-calls/{uuid}/resource_templates/{obj_uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096
            - Modified property: requested_offering_plan
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BasePublicPlan
                  - Properties changed
                    - New property: components

PUT /api/proposal-protected-calls/{uuid}/resource_templates/{obj_uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096
            - Modified property: requested_offering_plan
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BasePublicPlan
                  - Properties changed
                    - New property: components

POST /api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/close/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: documents
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096
            - Modified property: offerings
              - Items changed
                - Properties changed
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - Modified property: description
                          - MaxLength changed from 2000 to 4096
                  - Modified property: plan_details
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - New property: components
            - Modified property: resource_templates
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096
                  - Modified property: requested_offering_plan
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - New property: components

GET /api/proposal-public-calls/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: documents
                - Items changed
                  - Properties changed
                    - Modified property: description
                      - MaxLength changed from 2000 to 4096
              - Modified property: offerings
                - Items changed
                  - Properties changed
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - Modified property: description
                            - MaxLength changed from 2000 to 4096
                    - Modified property: plan_details
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BasePublicPlan
                          - Properties changed
                            - New property: components
              - Modified property: resource_templates
                - Items changed
                  - Properties changed
                    - Modified property: description
                      - MaxLength changed from 2000 to 4096
                    - Modified property: requested_offering_plan
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BasePublicPlan
                          - Properties changed
                            - New property: components

GET /api/proposal-public-calls/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: documents
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096
            - Modified property: offerings
              - Items changed
                - Properties changed
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - Modified property: description
                          - MaxLength changed from 2000 to 4096
                  - Modified property: plan_details
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - New property: components
            - Modified property: resource_templates
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096
                  - Modified property: requested_offering_plan
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - New property: components

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
                    - Modified property: description
                      - MaxLength changed from 2000 to 4096
              - Modified property: plan_details
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/BasePublicPlan
                    - Properties changed
                      - New property: components

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
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096
            - Modified property: plan_details
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BasePublicPlan
                  - Properties changed
                    - New property: components

GET /api/proposal-requested-resources/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to 4096
              - Modified property: requested_offering
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/NestedRequestedOffering
                    - Properties changed
                      - Modified property: components
                        - Items changed
                          - Properties changed
                            - Modified property: description
                              - MaxLength changed from 2000 to 4096
                      - Modified property: plan_details
                        - Property 'AllOf' changed
                          - Modified schema: #/components/schemas/BasePublicPlan
                            - Properties changed
                              - New property: components

GET /api/proposal-requested-resources/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096
            - Modified property: requested_offering
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/NestedRequestedOffering
                  - Properties changed
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - Modified property: description
                            - MaxLength changed from 2000 to 4096
                    - Modified property: plan_details
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BasePublicPlan
                          - Properties changed
                            - New property: components

GET /api/rancher-apps/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to 4096

POST /api/rancher-apps/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/rancher-apps/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PATCH /api/rancher-apps/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PUT /api/rancher-apps/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/rancher-catalogs/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to 4096

POST /api/rancher-catalogs/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/rancher-catalogs/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PATCH /api/rancher-catalogs/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PUT /api/rancher-catalogs/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

POST /api/rancher-catalogs/{uuid}/refresh/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/rancher-cluster-security-groups/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: rules
                - Items changed
                  - Properties changed
                    - Modified property: description
                      - MaxLength changed from 2000 to 4096

GET /api/rancher-cluster-security-groups/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: rules
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096

PATCH /api/rancher-cluster-security-groups/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: rules
            - Items changed
              - Properties changed
                - Modified property: description
                  - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: rules
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096

PUT /api/rancher-cluster-security-groups/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: rules
            - Items changed
              - Properties changed
                - Modified property: description
                  - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: rules
              - Items changed
                - Properties changed
                  - Modified property: description
                    - MaxLength changed from 2000 to 4096

GET /api/rancher-cluster-templates/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to 4096

GET /api/rancher-cluster-templates/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/rancher-clusters/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to 4096

GET /api/rancher-clusters/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PATCH /api/rancher-clusters/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PUT /api/rancher-clusters/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

POST /api/rancher-clusters/{uuid}/create_management_security_group/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/rancher-hpas/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to 4096

POST /api/rancher-hpas/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/rancher-hpas/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PATCH /api/rancher-hpas/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PUT /api/rancher-hpas/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/rancher-hpas/{uuid}/yaml/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PUT /api/rancher-hpas/{uuid}/yaml/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/rancher-ingresses/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to 4096

POST /api/rancher-ingresses/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/rancher-ingresses/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PATCH /api/rancher-ingresses/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PUT /api/rancher-ingresses/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/rancher-ingresses/{uuid}/yaml/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PUT /api/rancher-ingresses/{uuid}/yaml/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/rancher-projects/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to 4096

GET /api/rancher-projects/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/rancher-projects/{uuid}/secrets/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/rancher-services/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to 4096

POST /api/rancher-services/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/rancher-services/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PATCH /api/rancher-services/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PUT /api/rancher-services/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/rancher-services/{uuid}/yaml/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PUT /api/rancher-services/{uuid}/yaml/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/rancher-templates/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to 4096

GET /api/rancher-templates/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

POST /api/remote-waldur-api/remote_categories/

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
                    - Modified property: description
                      - MaxLength changed from 2000 to 4096

GET /api/remote-waldur-api/remote_resource_order_status/{resource_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: local_state
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderState
                  - New enum values: [pending-start-date]
            - Modified property: remote_state
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/RemoteResourceOrderRemoteStateEnum
                  - New enum values: [9]

GET /api/roles/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to 4096
              - Modified property: description_ar
                - MaxLength changed from 2000 to 4096
              - Modified property: description_cs
                - MaxLength changed from 2000 to 4096
              - Modified property: description_da
                - MaxLength changed from 2000 to 4096
              - Modified property: description_de
                - MaxLength changed from 2000 to 4096
              - Modified property: description_en
                - MaxLength changed from 2000 to 4096
              - Modified property: description_es
                - MaxLength changed from 2000 to 4096
              - Modified property: description_et
                - MaxLength changed from 2000 to 4096
              - Modified property: description_fr
                - MaxLength changed from 2000 to 4096
              - Modified property: description_it
                - MaxLength changed from 2000 to 4096
              - Modified property: description_lt
                - MaxLength changed from 2000 to 4096
              - Modified property: description_lv
                - MaxLength changed from 2000 to 4096
              - Modified property: description_nb
                - MaxLength changed from 2000 to 4096
              - Modified property: description_ru
                - MaxLength changed from 2000 to 4096
              - Modified property: description_sv
                - MaxLength changed from 2000 to 4096

POST /api/roles/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
          - Modified property: description_ar
            - MaxLength changed from 2000 to 4096
          - Modified property: description_cs
            - MaxLength changed from 2000 to 4096
          - Modified property: description_da
            - MaxLength changed from 2000 to 4096
          - Modified property: description_de
            - MaxLength changed from 2000 to 4096
          - Modified property: description_en
            - MaxLength changed from 2000 to 4096
          - Modified property: description_es
            - MaxLength changed from 2000 to 4096
          - Modified property: description_et
            - MaxLength changed from 2000 to 4096
          - Modified property: description_fr
            - MaxLength changed from 2000 to 4096
          - Modified property: description_it
            - MaxLength changed from 2000 to 4096
          - Modified property: description_lt
            - MaxLength changed from 2000 to 4096
          - Modified property: description_lv
            - MaxLength changed from 2000 to 4096
          - Modified property: description_nb
            - MaxLength changed from 2000 to 4096
          - Modified property: description_ru
            - MaxLength changed from 2000 to 4096
          - Modified property: description_sv
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096
            - Modified property: description_ar
              - MaxLength changed from 2000 to 4096
            - Modified property: description_cs
              - MaxLength changed from 2000 to 4096
            - Modified property: description_da
              - MaxLength changed from 2000 to 4096
            - Modified property: description_de
              - MaxLength changed from 2000 to 4096
            - Modified property: description_en
              - MaxLength changed from 2000 to 4096
            - Modified property: description_es
              - MaxLength changed from 2000 to 4096
            - Modified property: description_et
              - MaxLength changed from 2000 to 4096
            - Modified property: description_fr
              - MaxLength changed from 2000 to 4096
            - Modified property: description_it
              - MaxLength changed from 2000 to 4096
            - Modified property: description_lt
              - MaxLength changed from 2000 to 4096
            - Modified property: description_lv
              - MaxLength changed from 2000 to 4096
            - Modified property: description_nb
              - MaxLength changed from 2000 to 4096
            - Modified property: description_ru
              - MaxLength changed from 2000 to 4096
            - Modified property: description_sv
              - MaxLength changed from 2000 to 4096

GET /api/roles/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096
            - Modified property: description_ar
              - MaxLength changed from 2000 to 4096
            - Modified property: description_cs
              - MaxLength changed from 2000 to 4096
            - Modified property: description_da
              - MaxLength changed from 2000 to 4096
            - Modified property: description_de
              - MaxLength changed from 2000 to 4096
            - Modified property: description_en
              - MaxLength changed from 2000 to 4096
            - Modified property: description_es
              - MaxLength changed from 2000 to 4096
            - Modified property: description_et
              - MaxLength changed from 2000 to 4096
            - Modified property: description_fr
              - MaxLength changed from 2000 to 4096
            - Modified property: description_it
              - MaxLength changed from 2000 to 4096
            - Modified property: description_lt
              - MaxLength changed from 2000 to 4096
            - Modified property: description_lv
              - MaxLength changed from 2000 to 4096
            - Modified property: description_nb
              - MaxLength changed from 2000 to 4096
            - Modified property: description_ru
              - MaxLength changed from 2000 to 4096
            - Modified property: description_sv
              - MaxLength changed from 2000 to 4096

PATCH /api/roles/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
          - Modified property: description_ar
            - MaxLength changed from 2000 to 4096
          - Modified property: description_cs
            - MaxLength changed from 2000 to 4096
          - Modified property: description_da
            - MaxLength changed from 2000 to 4096
          - Modified property: description_de
            - MaxLength changed from 2000 to 4096
          - Modified property: description_en
            - MaxLength changed from 2000 to 4096
          - Modified property: description_es
            - MaxLength changed from 2000 to 4096
          - Modified property: description_et
            - MaxLength changed from 2000 to 4096
          - Modified property: description_fr
            - MaxLength changed from 2000 to 4096
          - Modified property: description_it
            - MaxLength changed from 2000 to 4096
          - Modified property: description_lt
            - MaxLength changed from 2000 to 4096
          - Modified property: description_lv
            - MaxLength changed from 2000 to 4096
          - Modified property: description_nb
            - MaxLength changed from 2000 to 4096
          - Modified property: description_ru
            - MaxLength changed from 2000 to 4096
          - Modified property: description_sv
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096
            - Modified property: description_ar
              - MaxLength changed from 2000 to 4096
            - Modified property: description_cs
              - MaxLength changed from 2000 to 4096
            - Modified property: description_da
              - MaxLength changed from 2000 to 4096
            - Modified property: description_de
              - MaxLength changed from 2000 to 4096
            - Modified property: description_en
              - MaxLength changed from 2000 to 4096
            - Modified property: description_es
              - MaxLength changed from 2000 to 4096
            - Modified property: description_et
              - MaxLength changed from 2000 to 4096
            - Modified property: description_fr
              - MaxLength changed from 2000 to 4096
            - Modified property: description_it
              - MaxLength changed from 2000 to 4096
            - Modified property: description_lt
              - MaxLength changed from 2000 to 4096
            - Modified property: description_lv
              - MaxLength changed from 2000 to 4096
            - Modified property: description_nb
              - MaxLength changed from 2000 to 4096
            - Modified property: description_ru
              - MaxLength changed from 2000 to 4096
            - Modified property: description_sv
              - MaxLength changed from 2000 to 4096

PUT /api/roles/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
          - Modified property: description_ar
            - MaxLength changed from 2000 to 4096
          - Modified property: description_cs
            - MaxLength changed from 2000 to 4096
          - Modified property: description_da
            - MaxLength changed from 2000 to 4096
          - Modified property: description_de
            - MaxLength changed from 2000 to 4096
          - Modified property: description_en
            - MaxLength changed from 2000 to 4096
          - Modified property: description_es
            - MaxLength changed from 2000 to 4096
          - Modified property: description_et
            - MaxLength changed from 2000 to 4096
          - Modified property: description_fr
            - MaxLength changed from 2000 to 4096
          - Modified property: description_it
            - MaxLength changed from 2000 to 4096
          - Modified property: description_lt
            - MaxLength changed from 2000 to 4096
          - Modified property: description_lv
            - MaxLength changed from 2000 to 4096
          - Modified property: description_nb
            - MaxLength changed from 2000 to 4096
          - Modified property: description_ru
            - MaxLength changed from 2000 to 4096
          - Modified property: description_sv
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096
            - Modified property: description_ar
              - MaxLength changed from 2000 to 4096
            - Modified property: description_cs
              - MaxLength changed from 2000 to 4096
            - Modified property: description_da
              - MaxLength changed from 2000 to 4096
            - Modified property: description_de
              - MaxLength changed from 2000 to 4096
            - Modified property: description_en
              - MaxLength changed from 2000 to 4096
            - Modified property: description_es
              - MaxLength changed from 2000 to 4096
            - Modified property: description_et
              - MaxLength changed from 2000 to 4096
            - Modified property: description_fr
              - MaxLength changed from 2000 to 4096
            - Modified property: description_it
              - MaxLength changed from 2000 to 4096
            - Modified property: description_lt
              - MaxLength changed from 2000 to 4096
            - Modified property: description_lv
              - MaxLength changed from 2000 to 4096
            - Modified property: description_nb
              - MaxLength changed from 2000 to 4096
            - Modified property: description_ru
              - MaxLength changed from 2000 to 4096
            - Modified property: description_sv
              - MaxLength changed from 2000 to 4096

PUT /api/roles/{uuid}/update_descriptions/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
          - Modified property: description_ar
            - MaxLength changed from 2000 to 4096
          - Modified property: description_cs
            - MaxLength changed from 2000 to 4096
          - Modified property: description_da
            - MaxLength changed from 2000 to 4096
          - Modified property: description_de
            - MaxLength changed from 2000 to 4096
          - Modified property: description_en
            - MaxLength changed from 2000 to 4096
          - Modified property: description_es
            - MaxLength changed from 2000 to 4096
          - Modified property: description_et
            - MaxLength changed from 2000 to 4096
          - Modified property: description_fr
            - MaxLength changed from 2000 to 4096
          - Modified property: description_it
            - MaxLength changed from 2000 to 4096
          - Modified property: description_lt
            - MaxLength changed from 2000 to 4096
          - Modified property: description_lv
            - MaxLength changed from 2000 to 4096
          - Modified property: description_nb
            - MaxLength changed from 2000 to 4096
          - Modified property: description_ru
            - MaxLength changed from 2000 to 4096
          - Modified property: description_sv
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096
            - Modified property: description_ar
              - MaxLength changed from 2000 to 4096
            - Modified property: description_cs
              - MaxLength changed from 2000 to 4096
            - Modified property: description_da
              - MaxLength changed from 2000 to 4096
            - Modified property: description_de
              - MaxLength changed from 2000 to 4096
            - Modified property: description_en
              - MaxLength changed from 2000 to 4096
            - Modified property: description_es
              - MaxLength changed from 2000 to 4096
            - Modified property: description_et
              - MaxLength changed from 2000 to 4096
            - Modified property: description_fr
              - MaxLength changed from 2000 to 4096
            - Modified property: description_it
              - MaxLength changed from 2000 to 4096
            - Modified property: description_lt
              - MaxLength changed from 2000 to 4096
            - Modified property: description_lv
              - MaxLength changed from 2000 to 4096
            - Modified property: description_nb
              - MaxLength changed from 2000 to 4096
            - Modified property: description_ru
              - MaxLength changed from 2000 to 4096
            - Modified property: description_sv
              - MaxLength changed from 2000 to 4096

GET /api/slurm-allocations/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to 4096

POST /api/slurm-allocations/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/slurm-allocations/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PATCH /api/slurm-allocations/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PUT /api/slurm-allocations/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/slurm-jobs/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to 4096

POST /api/slurm-jobs/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/slurm-jobs/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PATCH /api/slurm-jobs/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PUT /api/slurm-jobs/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/support-issues/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - Deleted required property: first_response_sla
            - Properties changed
              - Deleted property: first_response_sla

POST /api/support-issues/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: first_response_sla
          - Properties changed
            - Deleted property: first_response_sla

GET /api/support-issues/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: first_response_sla
          - Properties changed
            - Deleted property: first_response_sla

PATCH /api/support-issues/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: first_response_sla
          - Properties changed
            - Deleted property: first_response_sla

PUT /api/support-issues/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: first_response_sla
          - Properties changed
            - Deleted property: first_response_sla

POST /api/support-issues/{uuid}/sync/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: first_response_sla
          - Properties changed
            - Deleted property: first_response_sla

GET /api/support-priorities/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to 4096

GET /api/support-priorities/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/users/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [ip_address]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: ip_address
              - Modified property: description
                - MaxLength changed from 2000 to 4096

POST /api/users/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: ip_address
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/users/me/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [ip_address]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: ip_address
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/users/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [ip_address]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: ip_address
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PATCH /api/users/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: ip_address
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PUT /api/users/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: ip_address
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/vmware-disks/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to 4096

GET /api/vmware-disks/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/vmware-ports/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to 4096

GET /api/vmware-ports/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/vmware-templates/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to 4096

GET /api/vmware-templates/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/vmware-virtual-machine/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from 2000 to 4096

POST /api/vmware-virtual-machine/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

GET /api/vmware-virtual-machine/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PATCH /api/vmware-virtual-machine/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

PUT /api/vmware-virtual-machine/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

POST /api/vmware-virtual-machine/{uuid}/create_disk/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

POST /api/vmware-virtual-machine/{uuid}/create_port/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from 2000 to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from 2000 to 4096

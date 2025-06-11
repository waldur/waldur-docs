# OpenAPI schema diff - 7.5.2

## For version 7.5.2

### New Endpoints: 1

--------------------
POST /api/openstack-ports/{uuid}/update_port_ip/  

### Deleted Endpoints: None

---------------------------

### Modified Endpoints: 82

--------------------------
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
                      - Modified property: plan_description
                        - Nullable changed from false to true
                      - Modified property: plan_name
                        - Nullable changed from false to true
                      - Modified property: plan_unit
                        - Nullable changed from false to true
                      - Modified property: plan_uuid
                        - Nullable changed from false to true
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - Modified property: plan_description
                        - Nullable changed from false to true
                      - Modified property: plan_name
                        - Nullable changed from false to true
                      - Modified property: plan_unit
                        - Nullable changed from false to true
                      - Modified property: plan_uuid
                        - Nullable changed from false to true
              - Modified property: plan_description
                - Nullable changed from false to true
              - Modified property: plan_name
                - Nullable changed from false to true
              - Modified property: plan_unit
                - Nullable changed from false to true
              - Modified property: plan_uuid
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
                    - Modified property: plan_description
                      - Nullable changed from false to true
                    - Modified property: plan_name
                      - Nullable changed from false to true
                    - Modified property: plan_unit
                      - Nullable changed from false to true
                    - Modified property: plan_uuid
                      - Nullable changed from false to true
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: plan_description
                      - Nullable changed from false to true
                    - Modified property: plan_name
                      - Nullable changed from false to true
                    - Modified property: plan_unit
                      - Nullable changed from false to true
                    - Modified property: plan_uuid
                      - Nullable changed from false to true
            - Modified property: plan_description
              - Nullable changed from false to true
            - Modified property: plan_name
              - Nullable changed from false to true
            - Modified property: plan_unit
              - Nullable changed from false to true
            - Modified property: plan_uuid
              - Nullable changed from false to true

GET /api/customer-permissions-reviews/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: reviewer_full_name
                - Nullable changed from false to true
              - Modified property: reviewer_uuid
                - Nullable changed from false to true

GET /api/customer-permissions-reviews/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: reviewer_full_name
              - Nullable changed from false to true
            - Modified property: reviewer_uuid
              - Nullable changed from false to true

GET /api/keycloak-groups/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: scope_name
                - Nullable changed from false to true

GET /api/keycloak-groups/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: scope_name
              - Nullable changed from false to true

GET /api/marketplace-orders/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: plan_description
                - Nullable changed from false to true
              - Modified property: plan_name
                - Nullable changed from false to true
              - Modified property: plan_unit
                - Nullable changed from false to true
              - Modified property: plan_uuid
                - Nullable changed from false to true

POST /api/marketplace-orders/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: plan_description
              - Nullable changed from false to true
            - Modified property: plan_name
              - Nullable changed from false to true
            - Modified property: plan_unit
              - Nullable changed from false to true
            - Modified property: plan_uuid
              - Nullable changed from false to true

GET /api/marketplace-orders/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: plan_description
              - Nullable changed from false to true
            - Modified property: plan_name
              - Nullable changed from false to true
            - Modified property: plan_unit
              - Nullable changed from false to true
            - Modified property: plan_uuid
              - Nullable changed from false to true

GET /api/marketplace-provider-offerings/

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
                      - New property: base_image_name
                      - New property: dns_nameservers

POST /api/marketplace-provider-offerings/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: secret_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedSecretOptions
                  - Properties changed
                    - New property: base_image_name
                    - New property: dns_nameservers

GET /api/marketplace-provider-offerings/groups/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: secret_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedSecretOptions
                  - Properties changed
                    - New property: base_image_name
                    - New property: dns_nameservers

GET /api/marketplace-provider-offerings/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: secret_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedSecretOptions
                  - Properties changed
                    - New property: base_image_name
                    - New property: dns_nameservers

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
                    - Modified property: plan_description
                      - Nullable changed from false to true
                    - Modified property: plan_name
                      - Nullable changed from false to true
                    - Modified property: plan_unit
                      - Nullable changed from false to true
                    - Modified property: plan_uuid
                      - Nullable changed from false to true
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: plan_description
                      - Nullable changed from false to true
                    - Modified property: plan_name
                      - Nullable changed from false to true
                    - Modified property: plan_unit
                      - Nullable changed from false to true
                    - Modified property: plan_uuid
                      - Nullable changed from false to true
            - Modified property: plan_description
              - Nullable changed from false to true
            - Modified property: plan_name
              - Nullable changed from false to true
            - Modified property: plan_unit
              - Nullable changed from false to true
            - Modified property: plan_uuid
              - Nullable changed from false to true

GET /api/marketplace-provider-offerings/{uuid}/list_customer_projects/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: type_name
                - Nullable changed from false to true
              - Modified property: type_uuid
                - Nullable changed from false to true

GET /api/marketplace-provider-offerings/{uuid}/orders/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: plan_description
                - Nullable changed from false to true
              - Modified property: plan_name
                - Nullable changed from false to true
              - Modified property: plan_unit
                - Nullable changed from false to true
              - Modified property: plan_uuid
                - Nullable changed from false to true

GET /api/marketplace-provider-offerings/{uuid}/orders/{order_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: plan_description
              - Nullable changed from false to true
            - Modified property: plan_name
              - Nullable changed from false to true
            - Modified property: plan_unit
              - Nullable changed from false to true
            - Modified property: plan_uuid
              - Nullable changed from false to true

POST /api/marketplace-provider-offerings/{uuid}/refresh_offering_usernames/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: secret_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedSecretOptions
                  - Properties changed
                    - New property: base_image_name
                    - New property: dns_nameservers

GET /api/marketplace-provider-offerings/{uuid}/stats/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: secret_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedSecretOptions
                  - Properties changed
                    - New property: base_image_name
                    - New property: dns_nameservers

POST /api/marketplace-provider-offerings/{uuid}/update_image/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: secret_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedSecretOptions
                  - Properties changed
                    - New property: base_image_name
                    - New property: dns_nameservers

POST /api/marketplace-provider-offerings/{uuid}/update_integration/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: secret_options
            - Properties changed
              - New property: base_image_name
              - New property: dns_nameservers

GET /api/marketplace-provider-offerings/{uuid}/user_has_resource_access/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: secret_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedSecretOptions
                  - Properties changed
                    - New property: base_image_name
                    - New property: dns_nameservers

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
                      - Modified property: plan_description
                        - Nullable changed from false to true
                      - Modified property: plan_name
                        - Nullable changed from false to true
                      - Modified property: plan_unit
                        - Nullable changed from false to true
                      - Modified property: plan_uuid
                        - Nullable changed from false to true
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - Modified property: plan_description
                        - Nullable changed from false to true
                      - Modified property: plan_name
                        - Nullable changed from false to true
                      - Modified property: plan_unit
                        - Nullable changed from false to true
                      - Modified property: plan_uuid
                        - Nullable changed from false to true
              - Modified property: plan_description
                - Nullable changed from false to true
              - Modified property: plan_name
                - Nullable changed from false to true
              - Modified property: plan_unit
                - Nullable changed from false to true
              - Modified property: plan_uuid
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
                    - Modified property: plan_description
                      - Nullable changed from false to true
                    - Modified property: plan_name
                      - Nullable changed from false to true
                    - Modified property: plan_unit
                      - Nullable changed from false to true
                    - Modified property: plan_uuid
                      - Nullable changed from false to true
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: plan_description
                      - Nullable changed from false to true
                    - Modified property: plan_name
                      - Nullable changed from false to true
                    - Modified property: plan_unit
                      - Nullable changed from false to true
                    - Modified property: plan_uuid
                      - Nullable changed from false to true
            - Modified property: plan_description
              - Nullable changed from false to true
            - Modified property: plan_name
              - Nullable changed from false to true
            - Modified property: plan_unit
              - Nullable changed from false to true
            - Modified property: plan_uuid
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
                    - Modified property: plan_description
                      - Nullable changed from false to true
                    - Modified property: plan_name
                      - Nullable changed from false to true
                    - Modified property: plan_unit
                      - Nullable changed from false to true
                    - Modified property: plan_uuid
                      - Nullable changed from false to true
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: plan_description
                      - Nullable changed from false to true
                    - Modified property: plan_name
                      - Nullable changed from false to true
                    - Modified property: plan_unit
                      - Nullable changed from false to true
                    - Modified property: plan_uuid
                      - Nullable changed from false to true
            - Modified property: plan_description
              - Nullable changed from false to true
            - Modified property: plan_name
              - Nullable changed from false to true
            - Modified property: plan_unit
              - Nullable changed from false to true
            - Modified property: plan_uuid
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
                    - Modified property: plan_description
                      - Nullable changed from false to true
                    - Modified property: plan_name
                      - Nullable changed from false to true
                    - Modified property: plan_unit
                      - Nullable changed from false to true
                    - Modified property: plan_uuid
                      - Nullable changed from false to true
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: plan_description
                      - Nullable changed from false to true
                    - Modified property: plan_name
                      - Nullable changed from false to true
                    - Modified property: plan_unit
                      - Nullable changed from false to true
                    - Modified property: plan_uuid
                      - Nullable changed from false to true
            - Modified property: plan_description
              - Nullable changed from false to true
            - Modified property: plan_name
              - Nullable changed from false to true
            - Modified property: plan_unit
              - Nullable changed from false to true
            - Modified property: plan_uuid
              - Nullable changed from false to true

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
                    - Modified property: plan_description
                      - Nullable changed from false to true
                    - Modified property: plan_name
                      - Nullable changed from false to true
                    - Modified property: plan_unit
                      - Nullable changed from false to true
                    - Modified property: plan_uuid
                      - Nullable changed from false to true
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: plan_description
                      - Nullable changed from false to true
                    - Modified property: plan_name
                      - Nullable changed from false to true
                    - Modified property: plan_unit
                      - Nullable changed from false to true
                    - Modified property: plan_uuid
                      - Nullable changed from false to true
            - Modified property: plan_description
              - Nullable changed from false to true
            - Modified property: plan_name
              - Nullable changed from false to true
            - Modified property: plan_unit
              - Nullable changed from false to true
            - Modified property: plan_uuid
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
                    - Modified property: plan_description
                      - Nullable changed from false to true
                    - Modified property: plan_name
                      - Nullable changed from false to true
                    - Modified property: plan_unit
                      - Nullable changed from false to true
                    - Modified property: plan_uuid
                      - Nullable changed from false to true
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: plan_description
                      - Nullable changed from false to true
                    - Modified property: plan_name
                      - Nullable changed from false to true
                    - Modified property: plan_unit
                      - Nullable changed from false to true
                    - Modified property: plan_uuid
                      - Nullable changed from false to true
            - Modified property: plan_description
              - Nullable changed from false to true
            - Modified property: plan_name
              - Nullable changed from false to true
            - Modified property: plan_unit
              - Nullable changed from false to true
            - Modified property: plan_uuid
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
                    - Modified property: plan_description
                      - Nullable changed from false to true
                    - Modified property: plan_name
                      - Nullable changed from false to true
                    - Modified property: plan_unit
                      - Nullable changed from false to true
                    - Modified property: plan_uuid
                      - Nullable changed from false to true
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: plan_description
                      - Nullable changed from false to true
                    - Modified property: plan_name
                      - Nullable changed from false to true
                    - Modified property: plan_unit
                      - Nullable changed from false to true
                    - Modified property: plan_uuid
                      - Nullable changed from false to true
            - Modified property: plan_description
              - Nullable changed from false to true
            - Modified property: plan_name
              - Nullable changed from false to true
            - Modified property: plan_unit
              - Nullable changed from false to true
            - Modified property: plan_uuid
              - Nullable changed from false to true

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
                      - Modified property: plan_description
                        - Nullable changed from false to true
                      - Modified property: plan_name
                        - Nullable changed from false to true
                      - Modified property: plan_unit
                        - Nullable changed from false to true
                      - Modified property: plan_uuid
                        - Nullable changed from false to true
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - Modified property: plan_description
                        - Nullable changed from false to true
                      - Modified property: plan_name
                        - Nullable changed from false to true
                      - Modified property: plan_unit
                        - Nullable changed from false to true
                      - Modified property: plan_uuid
                        - Nullable changed from false to true
              - Modified property: plan_description
                - Nullable changed from false to true
              - Modified property: plan_name
                - Nullable changed from false to true
              - Modified property: plan_unit
                - Nullable changed from false to true
              - Modified property: plan_uuid
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
                    - Modified property: plan_description
                      - Nullable changed from false to true
                    - Modified property: plan_name
                      - Nullable changed from false to true
                    - Modified property: plan_unit
                      - Nullable changed from false to true
                    - Modified property: plan_uuid
                      - Nullable changed from false to true
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: plan_description
                      - Nullable changed from false to true
                    - Modified property: plan_name
                      - Nullable changed from false to true
                    - Modified property: plan_unit
                      - Nullable changed from false to true
                    - Modified property: plan_uuid
                      - Nullable changed from false to true
            - Modified property: plan_description
              - Nullable changed from false to true
            - Modified property: plan_name
              - Nullable changed from false to true
            - Modified property: plan_unit
              - Nullable changed from false to true
            - Modified property: plan_uuid
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
                    - Modified property: plan_description
                      - Nullable changed from false to true
                    - Modified property: plan_name
                      - Nullable changed from false to true
                    - Modified property: plan_unit
                      - Nullable changed from false to true
                    - Modified property: plan_uuid
                      - Nullable changed from false to true
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: plan_description
                      - Nullable changed from false to true
                    - Modified property: plan_name
                      - Nullable changed from false to true
                    - Modified property: plan_unit
                      - Nullable changed from false to true
                    - Modified property: plan_uuid
                      - Nullable changed from false to true
            - Modified property: plan_description
              - Nullable changed from false to true
            - Modified property: plan_name
              - Nullable changed from false to true
            - Modified property: plan_unit
              - Nullable changed from false to true
            - Modified property: plan_uuid
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
                    - Modified property: plan_description
                      - Nullable changed from false to true
                    - Modified property: plan_name
                      - Nullable changed from false to true
                    - Modified property: plan_unit
                      - Nullable changed from false to true
                    - Modified property: plan_uuid
                      - Nullable changed from false to true
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: plan_description
                      - Nullable changed from false to true
                    - Modified property: plan_name
                      - Nullable changed from false to true
                    - Modified property: plan_unit
                      - Nullable changed from false to true
                    - Modified property: plan_uuid
                      - Nullable changed from false to true
            - Modified property: plan_description
              - Nullable changed from false to true
            - Modified property: plan_name
              - Nullable changed from false to true
            - Modified property: plan_unit
              - Nullable changed from false to true
            - Modified property: plan_uuid
              - Nullable changed from false to true

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
                      - New property: base_image_name
                      - New property: dns_nameservers

GET /api/marketplace-service-providers/{service_provider_uuid}/project_permissions/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: created_by_full_name
                - Nullable changed from false to true
              - Modified property: created_by_username
                - Nullable changed from false to true

GET /api/marketplace-service-providers/{service_provider_uuid}/projects/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: type_name
                - Nullable changed from false to true
              - Modified property: type_uuid
                - Nullable changed from false to true

GET /api/openstack-backups/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: instance_floating_ips
                - Items changed
                  - Properties changed
                    - Modified property: port_mac_address
                      - Nullable changed from false to true
              - Modified property: instance_ports
                - Items changed
                  - Properties changed
                    - Modified property: subnet_cidr
                      - Nullable changed from false to true
                    - Modified property: subnet_description
                      - Nullable changed from false to true
                    - Modified property: subnet_name
                      - Nullable changed from false to true
                    - Modified property: subnet_uuid
                      - Nullable changed from false to true
              - Modified property: restorations
                - Items changed
                  - Properties changed
                    - Modified property: floating_ips
                      - Items changed
                        - Properties changed
                          - Modified property: port_mac_address
                            - Nullable changed from false to true
                    - Modified property: ports
                      - Items changed
                        - Properties changed
                          - Modified property: subnet_cidr
                            - Nullable changed from false to true
                          - Modified property: subnet_description
                            - Nullable changed from false to true
                          - Modified property: subnet_name
                            - Nullable changed from false to true
                          - Modified property: subnet_uuid
                            - Nullable changed from false to true

GET /api/openstack-backups/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: instance_floating_ips
              - Items changed
                - Properties changed
                  - Modified property: port_mac_address
                    - Nullable changed from false to true
            - Modified property: instance_ports
              - Items changed
                - Properties changed
                  - Modified property: subnet_cidr
                    - Nullable changed from false to true
                  - Modified property: subnet_description
                    - Nullable changed from false to true
                  - Modified property: subnet_name
                    - Nullable changed from false to true
                  - Modified property: subnet_uuid
                    - Nullable changed from false to true
            - Modified property: restorations
              - Items changed
                - Properties changed
                  - Modified property: floating_ips
                    - Items changed
                      - Properties changed
                        - Modified property: port_mac_address
                          - Nullable changed from false to true
                  - Modified property: ports
                    - Items changed
                      - Properties changed
                        - Modified property: subnet_cidr
                          - Nullable changed from false to true
                        - Modified property: subnet_description
                          - Nullable changed from false to true
                        - Modified property: subnet_name
                          - Nullable changed from false to true
                        - Modified property: subnet_uuid
                          - Nullable changed from false to true

PATCH /api/openstack-backups/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: instance_floating_ips
              - Items changed
                - Properties changed
                  - Modified property: port_mac_address
                    - Nullable changed from false to true
            - Modified property: instance_ports
              - Items changed
                - Properties changed
                  - Modified property: subnet_cidr
                    - Nullable changed from false to true
                  - Modified property: subnet_description
                    - Nullable changed from false to true
                  - Modified property: subnet_name
                    - Nullable changed from false to true
                  - Modified property: subnet_uuid
                    - Nullable changed from false to true
            - Modified property: restorations
              - Items changed
                - Properties changed
                  - Modified property: floating_ips
                    - Items changed
                      - Properties changed
                        - Modified property: port_mac_address
                          - Nullable changed from false to true
                  - Modified property: ports
                    - Items changed
                      - Properties changed
                        - Modified property: subnet_cidr
                          - Nullable changed from false to true
                        - Modified property: subnet_description
                          - Nullable changed from false to true
                        - Modified property: subnet_name
                          - Nullable changed from false to true
                        - Modified property: subnet_uuid
                          - Nullable changed from false to true

PUT /api/openstack-backups/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: instance_floating_ips
              - Items changed
                - Properties changed
                  - Modified property: port_mac_address
                    - Nullable changed from false to true
            - Modified property: instance_ports
              - Items changed
                - Properties changed
                  - Modified property: subnet_cidr
                    - Nullable changed from false to true
                  - Modified property: subnet_description
                    - Nullable changed from false to true
                  - Modified property: subnet_name
                    - Nullable changed from false to true
                  - Modified property: subnet_uuid
                    - Nullable changed from false to true
            - Modified property: restorations
              - Items changed
                - Properties changed
                  - Modified property: floating_ips
                    - Items changed
                      - Properties changed
                        - Modified property: port_mac_address
                          - Nullable changed from false to true
                  - Modified property: ports
                    - Items changed
                      - Properties changed
                        - Modified property: subnet_cidr
                          - Nullable changed from false to true
                        - Modified property: subnet_description
                          - Nullable changed from false to true
                        - Modified property: subnet_name
                          - Nullable changed from false to true
                        - Modified property: subnet_uuid
                          - Nullable changed from false to true

POST /api/openstack-backups/{uuid}/restore/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: floating_ips
              - Items changed
                - Properties changed
                  - Modified property: port_mac_address
                    - Nullable changed from false to true
            - Modified property: ports
              - Items changed
                - Properties changed
                  - Modified property: subnet_cidr
                    - Nullable changed from false to true
                  - Modified property: subnet_description
                    - Nullable changed from false to true
                  - Modified property: subnet_name
                    - Nullable changed from false to true
                  - Modified property: subnet_uuid
                    - Nullable changed from false to true

GET /api/openstack-instances/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: floating_ips
                - Items changed
                  - Properties changed
                    - Modified property: port_mac_address
                      - Nullable changed from false to true
              - Modified property: ports
                - Items changed
                  - Properties changed
                    - Modified property: subnet_cidr
                      - Nullable changed from false to true
                    - Modified property: subnet_description
                      - Nullable changed from false to true
                    - Modified property: subnet_name
                      - Nullable changed from false to true
                    - Modified property: subnet_uuid
                      - Nullable changed from false to true

GET /api/openstack-instances/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: floating_ips
              - Items changed
                - Properties changed
                  - Modified property: port_mac_address
                    - Nullable changed from false to true
            - Modified property: ports
              - Items changed
                - Properties changed
                  - Modified property: subnet_cidr
                    - Nullable changed from false to true
                  - Modified property: subnet_description
                    - Nullable changed from false to true
                  - Modified property: subnet_name
                    - Nullable changed from false to true
                  - Modified property: subnet_uuid
                    - Nullable changed from false to true

PATCH /api/openstack-instances/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: floating_ips
              - Items changed
                - Properties changed
                  - Modified property: port_mac_address
                    - Nullable changed from false to true
            - Modified property: ports
              - Items changed
                - Properties changed
                  - Modified property: subnet_cidr
                    - Nullable changed from false to true
                  - Modified property: subnet_description
                    - Nullable changed from false to true
                  - Modified property: subnet_name
                    - Nullable changed from false to true
                  - Modified property: subnet_uuid
                    - Nullable changed from false to true

PUT /api/openstack-instances/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: floating_ips
              - Items changed
                - Properties changed
                  - Modified property: port_mac_address
                    - Nullable changed from false to true
            - Modified property: ports
              - Items changed
                - Properties changed
                  - Modified property: subnet_cidr
                    - Nullable changed from false to true
                  - Modified property: subnet_description
                    - Nullable changed from false to true
                  - Modified property: subnet_name
                    - Nullable changed from false to true
                  - Modified property: subnet_uuid
                    - Nullable changed from false to true

POST /api/openstack-instances/{uuid}/backup/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: instance_floating_ips
              - Items changed
                - Properties changed
                  - Modified property: port_mac_address
                    - Nullable changed from false to true
            - Modified property: instance_ports
              - Items changed
                - Properties changed
                  - Modified property: subnet_cidr
                    - Nullable changed from false to true
                  - Modified property: subnet_description
                    - Nullable changed from false to true
                  - Modified property: subnet_name
                    - Nullable changed from false to true
                  - Modified property: subnet_uuid
                    - Nullable changed from false to true
            - Modified property: restorations
              - Items changed
                - Properties changed
                  - Modified property: floating_ips
                    - Items changed
                      - Properties changed
                        - Modified property: port_mac_address
                          - Nullable changed from false to true
                  - Modified property: ports
                    - Items changed
                      - Properties changed
                        - Modified property: subnet_cidr
                          - Nullable changed from false to true
                        - Modified property: subnet_description
                          - Nullable changed from false to true
                        - Modified property: subnet_name
                          - Nullable changed from false to true
                        - Modified property: subnet_uuid
                          - Nullable changed from false to true

GET /api/openstack-instances/{uuid}/floating_ips/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: port_mac_address
                - Nullable changed from false to true

GET /api/openstack-instances/{uuid}/ports/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: subnet_cidr
                - Nullable changed from false to true
              - Modified property: subnet_description
                - Nullable changed from false to true
              - Modified property: subnet_name
                - Nullable changed from false to true
              - Modified property: subnet_uuid
                - Nullable changed from false to true

GET /api/projects/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: type_name
                - Nullable changed from false to true
              - Modified property: type_uuid
                - Nullable changed from false to true

POST /api/projects/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: type_name
              - Nullable changed from false to true
            - Modified property: type_uuid
              - Nullable changed from false to true

GET /api/projects/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: type_name
              - Nullable changed from false to true
            - Modified property: type_uuid
              - Nullable changed from false to true

PATCH /api/projects/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: type_name
              - Nullable changed from false to true
            - Modified property: type_uuid
              - Nullable changed from false to true

PUT /api/projects/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: type_name
              - Nullable changed from false to true
            - Modified property: type_uuid
              - Nullable changed from false to true

POST /api/projects/{uuid}/move_project/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: type_name
              - Nullable changed from false to true
            - Modified property: type_uuid
              - Nullable changed from false to true

GET /api/promotions-campaigns/{uuid}/orders/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: plan_description
                - Nullable changed from false to true
              - Modified property: plan_name
                - Nullable changed from false to true
              - Modified property: plan_unit
                - Nullable changed from false to true
              - Modified property: plan_uuid
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
                      - Modified property: plan_description
                        - Nullable changed from false to true
                      - Modified property: plan_name
                        - Nullable changed from false to true
                      - Modified property: plan_unit
                        - Nullable changed from false to true
                      - Modified property: plan_uuid
                        - Nullable changed from false to true
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - Modified property: plan_description
                        - Nullable changed from false to true
                      - Modified property: plan_name
                        - Nullable changed from false to true
                      - Modified property: plan_unit
                        - Nullable changed from false to true
                      - Modified property: plan_uuid
                        - Nullable changed from false to true
              - Modified property: plan_description
                - Nullable changed from false to true
              - Modified property: plan_name
                - Nullable changed from false to true
              - Modified property: plan_unit
                - Nullable changed from false to true
              - Modified property: plan_uuid
                - Nullable changed from false to true

GET /api/proposal-reviews/

- New query param: proposal_name

GET /api/rancher-cluster-templates/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: nodes
                - Items changed
                  - Required changed
                    - New required property: role
                    - Deleted required property: roles
                  - Properties changed
                    - New property: role
                    - Deleted property: roles

GET /api/rancher-cluster-templates/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: nodes
              - Items changed
                - Required changed
                  - New required property: role
                  - Deleted required property: roles
                - Properties changed
                  - New property: role
                  - Deleted property: roles

GET /api/rancher-clusters/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: nodes
                - Items changed
                  - Properties changed
                    - New property: role
                    - Deleted property: controlplane_role
                    - Deleted property: etcd_role
                    - Deleted property: worker_role

POST /api/rancher-clusters/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: nodes
            - Items changed
              - Required changed
                - New required property: role
                - Deleted required property: roles
              - Properties changed
                - New property: role
                - Deleted property: controlplane_role
                - Deleted property: roles
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: nodes
              - Items changed
                - Properties changed
                  - New property: role
                  - Deleted property: controlplane_role
                  - Deleted property: etcd_role
                  - Deleted property: worker_role

GET /api/rancher-clusters/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: nodes
              - Items changed
                - Properties changed
                  - New property: role
                  - Deleted property: controlplane_role
                  - Deleted property: etcd_role
                  - Deleted property: worker_role

PATCH /api/rancher-clusters/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: nodes
              - Items changed
                - Properties changed
                  - New property: role
                  - Deleted property: controlplane_role
                  - Deleted property: etcd_role
                  - Deleted property: worker_role

PUT /api/rancher-clusters/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: nodes
            - Items changed
              - Required changed
                - New required property: role
                - Deleted required property: roles
              - Properties changed
                - New property: role
                - Deleted property: controlplane_role
                - Deleted property: roles
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: nodes
              - Items changed
                - Properties changed
                  - New property: role
                  - Deleted property: controlplane_role
                  - Deleted property: etcd_role
                  - Deleted property: worker_role

POST /api/rancher-clusters/{uuid}/create_management_security_group/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: nodes
            - Items changed
              - Required changed
                - New required property: role
                - Deleted required property: roles
              - Properties changed
                - New property: role
                - Deleted property: controlplane_role
                - Deleted property: roles
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: nodes
              - Items changed
                - Properties changed
                  - New property: role
                  - Deleted property: controlplane_role
                  - Deleted property: etcd_role
                  - Deleted property: worker_role

GET /api/rancher-nodes/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: role
            - Properties changed
              - New property: role
              - Deleted property: controlplane_role
              - Deleted property: etcd_role
              - Deleted property: worker_role

POST /api/rancher-nodes/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Required changed
          - New required property: role
          - Deleted required property: roles
        - Properties changed
          - New property: role
          - Deleted property: roles
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: role
          - Properties changed
            - New property: role

GET /api/rancher-nodes/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: role
          - Properties changed
            - New property: role
            - Deleted property: controlplane_role
            - Deleted property: etcd_role
            - Deleted property: worker_role

GET /api/rancher-template-versions/{template_uuid}/{version}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: questions
              - Items changed
                - Properties changed
                  - New property: validate_
                  - Deleted property: validate
                  - Modified property: subquestions
                    - Items changed
                      - Properties changed
                        - New property: validate_
                        - Deleted property: validate

GET /api/service-settings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: customer_name
                - Nullable changed from false to true

GET /api/service-settings/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: customer_name
              - Nullable changed from false to true

GET /api/slurm-jobs/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: user_username
                - Nullable changed from false to true
              - Modified property: user_uuid
                - Nullable changed from false to true

POST /api/slurm-jobs/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: user_username
              - Nullable changed from false to true
            - Modified property: user_uuid
              - Nullable changed from false to true

GET /api/slurm-jobs/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: user_username
              - Nullable changed from false to true
            - Modified property: user_uuid
              - Nullable changed from false to true

PATCH /api/slurm-jobs/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: user_username
              - Nullable changed from false to true
            - Modified property: user_uuid
              - Nullable changed from false to true

PUT /api/slurm-jobs/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: user_username
              - Nullable changed from false to true
            - Modified property: user_uuid
              - Nullable changed from false to true

GET /api/support-issues/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: assignee_name
                - Nullable changed from false to true
              - Modified property: assignee_uuid
                - Nullable changed from false to true
              - Modified property: caller_full_name
                - Nullable changed from false to true
              - Modified property: caller_uuid
                - Nullable changed from false to true
              - Modified property: customer_name
                - Nullable changed from false to true
              - Modified property: customer_uuid
                - Nullable changed from false to true
              - Modified property: project_name
                - Nullable changed from false to true
              - Modified property: project_uuid
                - Nullable changed from false to true
              - Modified property: reporter_name
                - Nullable changed from false to true
              - Modified property: reporter_uuid
                - Nullable changed from false to true

POST /api/support-issues/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: assignee_name
              - Nullable changed from false to true
            - Modified property: assignee_uuid
              - Nullable changed from false to true
            - Modified property: caller_full_name
              - Nullable changed from false to true
            - Modified property: caller_uuid
              - Nullable changed from false to true
            - Modified property: customer_name
              - Nullable changed from false to true
            - Modified property: customer_uuid
              - Nullable changed from false to true
            - Modified property: project_name
              - Nullable changed from false to true
            - Modified property: project_uuid
              - Nullable changed from false to true
            - Modified property: reporter_name
              - Nullable changed from false to true
            - Modified property: reporter_uuid
              - Nullable changed from false to true

GET /api/support-issues/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: assignee_name
              - Nullable changed from false to true
            - Modified property: assignee_uuid
              - Nullable changed from false to true
            - Modified property: caller_full_name
              - Nullable changed from false to true
            - Modified property: caller_uuid
              - Nullable changed from false to true
            - Modified property: customer_name
              - Nullable changed from false to true
            - Modified property: customer_uuid
              - Nullable changed from false to true
            - Modified property: project_name
              - Nullable changed from false to true
            - Modified property: project_uuid
              - Nullable changed from false to true
            - Modified property: reporter_name
              - Nullable changed from false to true
            - Modified property: reporter_uuid
              - Nullable changed from false to true

PATCH /api/support-issues/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: assignee_name
              - Nullable changed from false to true
            - Modified property: assignee_uuid
              - Nullable changed from false to true
            - Modified property: caller_full_name
              - Nullable changed from false to true
            - Modified property: caller_uuid
              - Nullable changed from false to true
            - Modified property: customer_name
              - Nullable changed from false to true
            - Modified property: customer_uuid
              - Nullable changed from false to true
            - Modified property: project_name
              - Nullable changed from false to true
            - Modified property: project_uuid
              - Nullable changed from false to true
            - Modified property: reporter_name
              - Nullable changed from false to true
            - Modified property: reporter_uuid
              - Nullable changed from false to true

PUT /api/support-issues/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: assignee_name
              - Nullable changed from false to true
            - Modified property: assignee_uuid
              - Nullable changed from false to true
            - Modified property: caller_full_name
              - Nullable changed from false to true
            - Modified property: caller_uuid
              - Nullable changed from false to true
            - Modified property: customer_name
              - Nullable changed from false to true
            - Modified property: customer_uuid
              - Nullable changed from false to true
            - Modified property: project_name
              - Nullable changed from false to true
            - Modified property: project_uuid
              - Nullable changed from false to true
            - Modified property: reporter_name
              - Nullable changed from false to true
            - Modified property: reporter_uuid
              - Nullable changed from false to true

POST /api/support-issues/{uuid}/sync/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: assignee_name
              - Nullable changed from false to true
            - Modified property: assignee_uuid
              - Nullable changed from false to true
            - Modified property: caller_full_name
              - Nullable changed from false to true
            - Modified property: caller_uuid
              - Nullable changed from false to true
            - Modified property: customer_name
              - Nullable changed from false to true
            - Modified property: customer_uuid
              - Nullable changed from false to true
            - Modified property: project_name
              - Nullable changed from false to true
            - Modified property: project_uuid
              - Nullable changed from false to true
            - Modified property: reporter_name
              - Nullable changed from false to true
            - Modified property: reporter_uuid
              - Nullable changed from false to true

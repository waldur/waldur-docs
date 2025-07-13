# OpenAPI schema diff - 7.6.9

## For version 7.6.9

### New Endpoints: 1

--------------------
GET /api/openstack-volume-types/names/  

### Deleted Endpoints: None

---------------------------

### Modified Endpoints: 28

--------------------------
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
                      - Modified property: managed_rancher_tenant_max_ram
                        - Description changed from 'Max number of RAM for tenants' to 'Max number of RAM for tenants (GB)'

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
                    - Modified property: managed_rancher_tenant_max_ram
                      - Description changed from 'Max number of RAM for tenants' to 'Max number of RAM for tenants (GB)'

GET /api/invoices/

- Deleted query param: max_sum
- Deleted query param: min_sum

GET /api/invoices/{uuid}/stats/

- Deleted query param: max_sum
- Deleted query param: min_sum

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
                    - Modified property: managed_rancher_tenant_max_ram
                      - Description changed from 'Max number of RAM for tenants' to 'Max number of RAM for tenants (GB)'

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
                      - Modified property: managed_rancher_tenant_max_ram
                        - Description changed from 'Max number of RAM for tenants' to 'Max number of RAM for tenants (GB)'

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
                    - Modified property: managed_rancher_tenant_max_ram
                      - Description changed from 'Max number of RAM for tenants' to 'Max number of RAM for tenants (GB)'

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
                    - Modified property: managed_rancher_tenant_max_ram
                      - Description changed from 'Max number of RAM for tenants' to 'Max number of RAM for tenants (GB)'

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
                    - Modified property: managed_rancher_tenant_max_ram
                      - Description changed from 'Max number of RAM for tenants' to 'Max number of RAM for tenants (GB)'

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
                    - Modified property: managed_rancher_tenant_max_ram
                      - Description changed from 'Max number of RAM for tenants' to 'Max number of RAM for tenants (GB)'

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
                    - Modified property: managed_rancher_tenant_max_ram
                      - Description changed from 'Max number of RAM for tenants' to 'Max number of RAM for tenants (GB)'

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
                    - Modified property: managed_rancher_tenant_max_ram
                      - Description changed from 'Max number of RAM for tenants' to 'Max number of RAM for tenants (GB)'

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
                    - Modified property: managed_rancher_tenant_max_ram
                      - Description changed from 'Max number of RAM for tenants' to 'Max number of RAM for tenants (GB)'

POST /api/marketplace-provider-offerings/{uuid}/update_integration/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: plugin_options
            - Properties changed
              - Modified property: managed_rancher_tenant_max_ram
                - Description changed from 'Max number of RAM for tenants' to 'Max number of RAM for tenants (GB)'

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
                    - Modified property: managed_rancher_tenant_max_ram
                      - Description changed from 'Max number of RAM for tenants' to 'Max number of RAM for tenants (GB)'

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
                    - Modified property: managed_rancher_tenant_max_ram
                      - Description changed from 'Max number of RAM for tenants' to 'Max number of RAM for tenants (GB)'

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
                      - Modified property: managed_rancher_tenant_max_ram
                        - Description changed from 'Max number of RAM for tenants' to 'Max number of RAM for tenants (GB)'

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
                    - Modified property: managed_rancher_tenant_max_ram
                      - Description changed from 'Max number of RAM for tenants' to 'Max number of RAM for tenants (GB)'

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
                    - Modified property: managed_rancher_tenant_max_ram
                      - Description changed from 'Max number of RAM for tenants' to 'Max number of RAM for tenants (GB)'

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
                      - Modified property: managed_rancher_tenant_max_ram
                        - Description changed from 'Max number of RAM for tenants' to 'Max number of RAM for tenants (GB)'

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
                    - Modified property: managed_rancher_tenant_max_ram
                      - Description changed from 'Max number of RAM for tenants' to 'Max number of RAM for tenants (GB)'

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
                    - Modified property: managed_rancher_tenant_max_ram
                      - Description changed from 'Max number of RAM for tenants' to 'Max number of RAM for tenants (GB)'

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
                    - Modified property: managed_rancher_tenant_max_ram
                      - Description changed from 'Max number of RAM for tenants' to 'Max number of RAM for tenants (GB)'

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
                    - Modified property: managed_rancher_tenant_max_ram
                      - Description changed from 'Max number of RAM for tenants' to 'Max number of RAM for tenants (GB)'

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
                    - Modified property: managed_rancher_tenant_max_ram
                      - Description changed from 'Max number of RAM for tenants' to 'Max number of RAM for tenants (GB)'

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
                    - Modified property: managed_rancher_tenant_max_ram
                      - Description changed from 'Max number of RAM for tenants' to 'Max number of RAM for tenants (GB)'

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
                    - Modified property: managed_rancher_tenant_max_ram
                      - Description changed from 'Max number of RAM for tenants' to 'Max number of RAM for tenants (GB)'

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
                    - Modified property: managed_rancher_tenant_max_ram
                      - Description changed from 'Max number of RAM for tenants' to 'Max number of RAM for tenants (GB)'

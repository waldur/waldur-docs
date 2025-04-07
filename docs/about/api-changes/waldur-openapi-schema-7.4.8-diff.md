# Waldur OpenAPI Schema Diff

## For version 7.4.8

### New Endpoints: 5

--------------------
POST /api/marketplace-robot-accounts/{uuid}/set_state_creating/  
POST /api/marketplace-robot-accounts/{uuid}/set_state_deleted/  
POST /api/marketplace-robot-accounts/{uuid}/set_state_erred/  
POST /api/marketplace-robot-accounts/{uuid}/set_state_ok/  
POST /api/marketplace-robot-accounts/{uuid}/set_state_request_deletion/  

### Deleted Endpoints: None

--------------------

### Modified Endpoints: 429

--------------------
POST /api-auth/password/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api-auth/saml2/login/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api-auth/saml2/login/complete/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api-auth/saml2/logout/complete/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/access-subnets/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PATCH /api/access-subnets/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/access-subnets/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/admin-announcements/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PATCH /api/admin-announcements/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/admin-announcements/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/auth-valimo/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/auth-valimo/result/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/aws-instances/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PATCH /api/aws-instances/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/aws-instances/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/aws-instances/{uuid}/resize/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/aws-volumes/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/aws-volumes/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/aws-volumes/{uuid}/attach/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/azure-public-ips/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PATCH /api/azure-public-ips/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/azure-public-ips/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/azure-sql-databases/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PATCH /api/azure-sql-databases/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/azure-sql-databases/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/azure-sql-servers/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PATCH /api/azure-sql-servers/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/azure-sql-servers/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/azure-sql-servers/{uuid}/create_database/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/azure-virtualmachines/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PATCH /api/azure-virtualmachines/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/azure-virtualmachines/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

GET /api/booking-offerings/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [scope_error_message]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: scope_error_message
              - Modified property: customer_name
                - Nullable changed from false to true
              - Modified property: customer_uuid
                - Nullable changed from false to true
              - Modified property: parent_description
                - Nullable changed from false to true
              - Modified property: parent_name
                - Nullable changed from false to true
              - Modified property: parent_uuid
                - Nullable changed from false to true
              - Modified property: plugin_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedPluginOptions
                    - Properties changed
                      - New property: openstack_offering_uuid_list
              - Modified property: project_name
                - Nullable changed from false to true
              - Modified property: project_uuid
                - Nullable changed from false to true

GET /api/booking-offerings/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [scope_error_message]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: scope_error_message
            - Modified property: customer_name
              - Nullable changed from false to true
            - Modified property: customer_uuid
              - Nullable changed from false to true
            - Modified property: parent_description
              - Nullable changed from false to true
            - Modified property: parent_name
              - Nullable changed from false to true
            - Modified property: parent_uuid
              - Nullable changed from false to true
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: openstack_offering_uuid_list
            - Modified property: project_name
              - Nullable changed from false to true
            - Modified property: project_uuid
              - Nullable changed from false to true

POST /api/broadcast-message-templates/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PATCH /api/broadcast-message-templates/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/broadcast-message-templates/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/broadcast-messages/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PATCH /api/broadcast-messages/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/broadcast-messages/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/call-managing-organisations/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PATCH /api/call-managing-organisations/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/call-managing-organisations/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/call-managing-organisations/{uuid}/add_user/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/call-managing-organisations/{uuid}/delete_user/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/call-managing-organisations/{uuid}/update_user/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/component-user-usage-limits/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PATCH /api/component-user-usage-limits/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/component-user-usage-limits/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/customer-credits/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PATCH /api/customer-credits/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/customer-credits/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/customer-credits/{uuid}/apply_compensations/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/customer-credits/{uuid}/clear_compensations/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

GET /api/customers/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: call_managing_organization_uuid
                - Nullable changed from false to true
              - Modified property: service_provider
                - Nullable changed from false to true
              - Modified property: service_provider_uuid
                - Nullable changed from false to true

POST /api/customers/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: call_managing_organization_uuid
              - Nullable changed from false to true
            - Modified property: service_provider
              - Nullable changed from false to true
            - Modified property: service_provider_uuid
              - Nullable changed from false to true

POST /api/customers/{customer_uuid}/marketplace-checklists/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

GET /api/customers/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: call_managing_organization_uuid
              - Nullable changed from false to true
            - Modified property: service_provider
              - Nullable changed from false to true
            - Modified property: service_provider_uuid
              - Nullable changed from false to true

PATCH /api/customers/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: call_managing_organization_uuid
              - Nullable changed from false to true
            - Modified property: service_provider
              - Nullable changed from false to true
            - Modified property: service_provider_uuid
              - Nullable changed from false to true

PUT /api/customers/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: call_managing_organization_uuid
              - Nullable changed from false to true
            - Modified property: service_provider
              - Nullable changed from false to true
            - Modified property: service_provider_uuid
              - Nullable changed from false to true

POST /api/customers/{uuid}/add_user/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/customers/{uuid}/delete_user/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

GET /api/customers/{uuid}/stats/

- New query param: for_current_month

POST /api/customers/{uuid}/update_organization_groups/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/customers/{uuid}/update_user/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/digitalocean-droplets/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PATCH /api/digitalocean-droplets/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/digitalocean-droplets/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/digitalocean-droplets/{uuid}/resize/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/event-subscriptions/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/feature-values/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/freeipa-profiles/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/freeipa-profiles/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

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
                  - New enum values: [resource_robot_account_state_changed]

POST /api/hooks-email/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [resource_robot_account_state_changed]
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [resource_robot_account_state_changed]

GET /api/hooks-email/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [resource_robot_account_state_changed]

PATCH /api/hooks-email/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [resource_robot_account_state_changed]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [resource_robot_account_state_changed]

PUT /api/hooks-email/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [resource_robot_account_state_changed]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [resource_robot_account_state_changed]

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
                  - New enum values: [resource_robot_account_state_changed]

POST /api/hooks-web/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [resource_robot_account_state_changed]
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [resource_robot_account_state_changed]

GET /api/hooks-web/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [resource_robot_account_state_changed]

PATCH /api/hooks-web/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [resource_robot_account_state_changed]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [resource_robot_account_state_changed]

PUT /api/hooks-web/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [resource_robot_account_state_changed]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [resource_robot_account_state_changed]

POST /api/identity-providers/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PATCH /api/identity-providers/{provider}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/identity-providers/{provider}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PATCH /api/invoice-items/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/invoice-items/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/invoice-items/{uuid}/create_compensation/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/invoice-items/{uuid}/migrate_to/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/invoice/send-financial-report-by-mail/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

GET /api/invoices/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [compensations incurred_costs]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: compensations
              - New property: incurred_costs

GET /api/invoices/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [compensations incurred_costs]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: compensations
            - New property: incurred_costs

POST /api/invoices/{uuid}/paid/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: compensations
            - New property: incurred_costs

POST /api/invoices/{uuid}/set_backend_id/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/invoices/{uuid}/set_payment_url/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/invoices/{uuid}/set_reference_number/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/keys/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/lexis-links/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PATCH /api/lexis-links/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/lexis-links/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/marketplace-categories/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PATCH /api/marketplace-categories/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/marketplace-categories/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/marketplace-category-columns/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PATCH /api/marketplace-category-columns/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/marketplace-category-columns/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/marketplace-category-components/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PATCH /api/marketplace-category-components/{id}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/marketplace-category-components/{id}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/marketplace-category-groups/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PATCH /api/marketplace-category-groups/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/marketplace-category-groups/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/marketplace-category-help-articles/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PATCH /api/marketplace-category-help-articles/{id}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/marketplace-category-help-articles/{id}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/marketplace-checklists/{checklist_uuid}/answers/submit/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/marketplace-component-usages/set_usage/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/marketplace-component-usages/{uuid}/set_user_usage/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/marketplace-customer-estimated-cost-policies/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PATCH /api/marketplace-customer-estimated-cost-policies/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/marketplace-customer-estimated-cost-policies/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/marketplace-offering-estimated-cost-policies/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PATCH /api/marketplace-offering-estimated-cost-policies/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/marketplace-offering-estimated-cost-policies/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/marketplace-offering-files/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/marketplace-offering-usage-policies/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PATCH /api/marketplace-offering-usage-policies/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/marketplace-offering-usage-policies/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/marketplace-offering-user-roles/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PATCH /api/marketplace-offering-user-roles/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/marketplace-offering-user-roles/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/marketplace-offering-users/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PATCH /api/marketplace-offering-users/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/marketplace-offering-users/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/marketplace-offering-users/{uuid}/update_restricted/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/marketplace-orders/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

GET /api/marketplace-orders/{uuid}/offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: scope_error_message
            - Modified property: customer_name
              - Nullable changed from false to true
            - Modified property: customer_uuid
              - Nullable changed from false to true
            - Modified property: google_calendar_is_public
              - Nullable changed from false to true
            - Modified property: parent_description
              - Nullable changed from false to true
            - Modified property: parent_name
              - Nullable changed from false to true
            - Modified property: parent_uuid
              - Nullable changed from false to true
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: openstack_offering_uuid_list
            - Modified property: project_name
              - Nullable changed from false to true
            - Modified property: project_uuid
              - Nullable changed from false to true

POST /api/marketplace-orders/{uuid}/set_state_erred/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/marketplace-plans/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PATCH /api/marketplace-plans/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/marketplace-plans/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/marketplace-plans/{uuid}/update_organization_groups/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/marketplace-plans/{uuid}/update_prices/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/marketplace-plans/{uuid}/update_quotas/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/marketplace-project-estimated-cost-policies/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PATCH /api/marketplace-project-estimated-cost-policies/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/marketplace-project-estimated-cost-policies/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/marketplace-project-update-requests/{uuid}/approve/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/marketplace-project-update-requests/{uuid}/reject/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

GET /api/marketplace-provider-offerings/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [scope_error_message]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: scope_error_message
              - Modified property: customer_name
                - Nullable changed from false to true
              - Modified property: customer_uuid
                - Nullable changed from false to true
              - Modified property: google_calendar_is_public
                - Nullable changed from false to true
              - Modified property: integration_status
                - Nullable changed from false to true
              - Modified property: parent_description
                - Nullable changed from false to true
              - Modified property: parent_name
                - Nullable changed from false to true
              - Modified property: parent_uuid
                - Nullable changed from false to true
              - Modified property: plugin_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedPluginOptions
                    - Properties changed
                      - New property: openstack_offering_uuid_list
              - Modified property: project_name
                - Nullable changed from false to true
              - Modified property: project_uuid
                - Nullable changed from false to true
              - Modified property: secret_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedSecretOptions
                    - Properties changed
                      - New property: rancher_offering_uuid

POST /api/marketplace-provider-offerings/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: scope_error_message
          - Properties changed
            - New property: scope_error_message
            - Modified property: customer_name
              - Nullable changed from false to true
            - Modified property: customer_uuid
              - Nullable changed from false to true
            - Modified property: parent_description
              - Nullable changed from false to true
            - Modified property: parent_name
              - Nullable changed from false to true
            - Modified property: parent_uuid
              - Nullable changed from false to true
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: openstack_offering_uuid_list
            - Modified property: project_name
              - Nullable changed from false to true
            - Modified property: project_uuid
              - Nullable changed from false to true
            - Modified property: secret_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedSecretOptions
                  - Properties changed
                    - New property: rancher_offering_uuid

GET /api/marketplace-provider-offerings/groups/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [scope_error_message]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: scope_error_message
            - Modified property: customer_name
              - Nullable changed from false to true
            - Modified property: customer_uuid
              - Nullable changed from false to true
            - Modified property: google_calendar_is_public
              - Nullable changed from false to true
            - Modified property: integration_status
              - Nullable changed from false to true
            - Modified property: parent_description
              - Nullable changed from false to true
            - Modified property: parent_name
              - Nullable changed from false to true
            - Modified property: parent_uuid
              - Nullable changed from false to true
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: openstack_offering_uuid_list
            - Modified property: project_name
              - Nullable changed from false to true
            - Modified property: project_uuid
              - Nullable changed from false to true
            - Modified property: secret_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedSecretOptions
                  - Properties changed
                    - New property: rancher_offering_uuid

GET /api/marketplace-provider-offerings/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [scope_error_message]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: scope_error_message
            - Modified property: customer_name
              - Nullable changed from false to true
            - Modified property: customer_uuid
              - Nullable changed from false to true
            - Modified property: google_calendar_is_public
              - Nullable changed from false to true
            - Modified property: integration_status
              - Nullable changed from false to true
            - Modified property: parent_description
              - Nullable changed from false to true
            - Modified property: parent_name
              - Nullable changed from false to true
            - Modified property: parent_uuid
              - Nullable changed from false to true
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: openstack_offering_uuid_list
            - Modified property: project_name
              - Nullable changed from false to true
            - Modified property: project_uuid
              - Nullable changed from false to true
            - Modified property: secret_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedSecretOptions
                  - Properties changed
                    - New property: rancher_offering_uuid

POST /api/marketplace-provider-offerings/{uuid}/add_endpoint/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/marketplace-provider-offerings/{uuid}/add_user/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/marketplace-provider-offerings/{uuid}/create_offering_component/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/marketplace-provider-offerings/{uuid}/delete_endpoint/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/marketplace-provider-offerings/{uuid}/delete_user/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/marketplace-provider-offerings/{uuid}/import_resource/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/marketplace-provider-offerings/{uuid}/pause/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/marketplace-provider-offerings/{uuid}/refresh_offering_usernames/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: scope_error_message
            - Modified property: customer_name
              - Nullable changed from false to true
            - Modified property: customer_uuid
              - Nullable changed from false to true
            - Modified property: google_calendar_is_public
              - Nullable changed from false to true
            - Modified property: integration_status
              - Nullable changed from false to true
            - Modified property: parent_description
              - Nullable changed from false to true
            - Modified property: parent_name
              - Nullable changed from false to true
            - Modified property: parent_uuid
              - Nullable changed from false to true
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: openstack_offering_uuid_list
            - Modified property: project_name
              - Nullable changed from false to true
            - Modified property: project_uuid
              - Nullable changed from false to true
            - Modified property: secret_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedSecretOptions
                  - Properties changed
                    - New property: rancher_offering_uuid

POST /api/marketplace-provider-offerings/{uuid}/remove_offering_component/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/marketplace-provider-offerings/{uuid}/set_backend_metadata/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

GET /api/marketplace-provider-offerings/{uuid}/stats/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [scope_error_message]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: scope_error_message
            - Modified property: customer_name
              - Nullable changed from false to true
            - Modified property: customer_uuid
              - Nullable changed from false to true
            - Modified property: google_calendar_is_public
              - Nullable changed from false to true
            - Modified property: integration_status
              - Nullable changed from false to true
            - Modified property: parent_description
              - Nullable changed from false to true
            - Modified property: parent_name
              - Nullable changed from false to true
            - Modified property: parent_uuid
              - Nullable changed from false to true
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: openstack_offering_uuid_list
            - Modified property: project_name
              - Nullable changed from false to true
            - Modified property: project_uuid
              - Nullable changed from false to true
            - Modified property: secret_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedSecretOptions
                  - Properties changed
                    - New property: rancher_offering_uuid

POST /api/marketplace-provider-offerings/{uuid}/update_attributes/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/marketplace-provider-offerings/{uuid}/update_description/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/marketplace-provider-offerings/{uuid}/update_image/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: scope_error_message
            - Modified property: customer_name
              - Nullable changed from false to true
            - Modified property: customer_uuid
              - Nullable changed from false to true
            - Modified property: google_calendar_is_public
              - Nullable changed from false to true
            - Modified property: integration_status
              - Nullable changed from false to true
            - Modified property: parent_description
              - Nullable changed from false to true
            - Modified property: parent_name
              - Nullable changed from false to true
            - Modified property: parent_uuid
              - Nullable changed from false to true
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: openstack_offering_uuid_list
            - Modified property: project_name
              - Nullable changed from false to true
            - Modified property: project_uuid
              - Nullable changed from false to true
            - Modified property: secret_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedSecretOptions
                  - Properties changed
                    - New property: rancher_offering_uuid

POST /api/marketplace-provider-offerings/{uuid}/update_integration/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: plugin_options
            - Properties changed
              - New property: openstack_offering_uuid_list
          - Modified property: secret_options
            - Properties changed
              - New property: rancher_offering_uuid
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: plugin_options
              - Properties changed
                - New property: openstack_offering_uuid_list
            - Modified property: secret_options
              - Properties changed
                - New property: rancher_offering_uuid

POST /api/marketplace-provider-offerings/{uuid}/update_location/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/marketplace-provider-offerings/{uuid}/update_offering_component/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/marketplace-provider-offerings/{uuid}/update_options/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/marketplace-provider-offerings/{uuid}/update_organization_groups/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: scope_error_message
            - Modified property: customer_name
              - Nullable changed from false to true
            - Modified property: customer_uuid
              - Nullable changed from false to true
            - Modified property: google_calendar_is_public
              - Nullable changed from false to true
            - Modified property: integration_status
              - Nullable changed from false to true
            - Modified property: parent_description
              - Nullable changed from false to true
            - Modified property: parent_name
              - Nullable changed from false to true
            - Modified property: parent_uuid
              - Nullable changed from false to true
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: openstack_offering_uuid_list
            - Modified property: project_name
              - Nullable changed from false to true
            - Modified property: project_uuid
              - Nullable changed from false to true
            - Modified property: secret_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedSecretOptions
                  - Properties changed
                    - New property: rancher_offering_uuid

POST /api/marketplace-provider-offerings/{uuid}/update_overview/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/marketplace-provider-offerings/{uuid}/update_resource_options/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/marketplace-provider-offerings/{uuid}/update_thumbnail/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: scope_error_message
            - Modified property: customer_name
              - Nullable changed from false to true
            - Modified property: customer_uuid
              - Nullable changed from false to true
            - Modified property: google_calendar_is_public
              - Nullable changed from false to true
            - Modified property: integration_status
              - Nullable changed from false to true
            - Modified property: parent_description
              - Nullable changed from false to true
            - Modified property: parent_name
              - Nullable changed from false to true
            - Modified property: parent_uuid
              - Nullable changed from false to true
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: openstack_offering_uuid_list
            - Modified property: project_name
              - Nullable changed from false to true
            - Modified property: project_uuid
              - Nullable changed from false to true
            - Modified property: secret_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedSecretOptions
                  - Properties changed
                    - New property: rancher_offering_uuid

POST /api/marketplace-provider-offerings/{uuid}/update_user/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

GET /api/marketplace-provider-offerings/{uuid}/user_has_resource_access/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [scope_error_message]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: scope_error_message
            - Modified property: customer_name
              - Nullable changed from false to true
            - Modified property: customer_uuid
              - Nullable changed from false to true
            - Modified property: google_calendar_is_public
              - Nullable changed from false to true
            - Modified property: integration_status
              - Nullable changed from false to true
            - Modified property: parent_description
              - Nullable changed from false to true
            - Modified property: parent_name
              - Nullable changed from false to true
            - Modified property: parent_uuid
              - Nullable changed from false to true
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: openstack_offering_uuid_list
            - Modified property: project_name
              - Nullable changed from false to true
            - Modified property: project_uuid
              - Nullable changed from false to true
            - Modified property: secret_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedSecretOptions
                  - Properties changed
                    - New property: rancher_offering_uuid

PATCH /api/marketplace-provider-resources/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/marketplace-provider-resources/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

GET /api/marketplace-provider-resources/{uuid}/offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: scope_error_message
            - Modified property: customer_name
              - Nullable changed from false to true
            - Modified property: customer_uuid
              - Nullable changed from false to true
            - Modified property: google_calendar_is_public
              - Nullable changed from false to true
            - Modified property: parent_description
              - Nullable changed from false to true
            - Modified property: parent_name
              - Nullable changed from false to true
            - Modified property: parent_uuid
              - Nullable changed from false to true
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: openstack_offering_uuid_list
            - Modified property: project_name
              - Nullable changed from false to true
            - Modified property: project_uuid
              - Nullable changed from false to true

POST /api/marketplace-provider-resources/{uuid}/refresh_last_sync/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/marketplace-provider-resources/{uuid}/set_as_erred/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/marketplace-provider-resources/{uuid}/set_as_ok/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/marketplace-provider-resources/{uuid}/set_backend_id/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/marketplace-provider-resources/{uuid}/set_backend_metadata/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/marketplace-provider-resources/{uuid}/set_end_date_by_provider/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/marketplace-provider-resources/{uuid}/set_end_date_by_staff/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/marketplace-provider-resources/{uuid}/set_limits/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/marketplace-provider-resources/{uuid}/set_slug/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/marketplace-provider-resources/{uuid}/submit_report/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/marketplace-provider-resources/{uuid}/terminate/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/marketplace-public-api/check_signature/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/marketplace-public-api/set_usage/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

GET /api/marketplace-public-offerings/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [scope_error_message]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: scope_error_message
              - Modified property: customer_name
                - Nullable changed from false to true
              - Modified property: customer_uuid
                - Nullable changed from false to true
              - Modified property: google_calendar_is_public
                - Nullable changed from false to true
              - Modified property: parent_description
                - Nullable changed from false to true
              - Modified property: parent_name
                - Nullable changed from false to true
              - Modified property: parent_uuid
                - Nullable changed from false to true
              - Modified property: plugin_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedPluginOptions
                    - Properties changed
                      - New property: openstack_offering_uuid_list
              - Modified property: project_name
                - Nullable changed from false to true
              - Modified property: project_uuid
                - Nullable changed from false to true

GET /api/marketplace-public-offerings/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [scope_error_message]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: scope_error_message
            - Modified property: customer_name
              - Nullable changed from false to true
            - Modified property: customer_uuid
              - Nullable changed from false to true
            - Modified property: google_calendar_is_public
              - Nullable changed from false to true
            - Modified property: parent_description
              - Nullable changed from false to true
            - Modified property: parent_name
              - Nullable changed from false to true
            - Modified property: parent_uuid
              - Nullable changed from false to true
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: openstack_offering_uuid_list
            - Modified property: project_name
              - Nullable changed from false to true
            - Modified property: project_uuid
              - Nullable changed from false to true

POST /api/marketplace-remote-synchronisations/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PATCH /api/marketplace-remote-synchronisations/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/marketplace-remote-synchronisations/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/marketplace-resource-users/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/marketplace-resources/suggest_name/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PATCH /api/marketplace-resources/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/marketplace-resources/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

GET /api/marketplace-resources/{uuid}/offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: scope_error_message
            - Modified property: customer_name
              - Nullable changed from false to true
            - Modified property: customer_uuid
              - Nullable changed from false to true
            - Modified property: google_calendar_is_public
              - Nullable changed from false to true
            - Modified property: parent_description
              - Nullable changed from false to true
            - Modified property: parent_name
              - Nullable changed from false to true
            - Modified property: parent_uuid
              - Nullable changed from false to true
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: openstack_offering_uuid_list
            - Modified property: project_name
              - Nullable changed from false to true
            - Modified property: project_uuid
              - Nullable changed from false to true

POST /api/marketplace-resources/{uuid}/set_end_date_by_staff/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/marketplace-resources/{uuid}/set_slug/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/marketplace-resources/{uuid}/switch_plan/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/marketplace-resources/{uuid}/terminate/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/marketplace-resources/{uuid}/update_limits/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/marketplace-resources/{uuid}/update_options/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

GET /api/marketplace-robot-accounts/

- New query param: state
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: error_message
              - New required property: error_traceback
              - New required property: state
            - Properties changed
              - New property: error_message
              - New property: error_traceback
              - New property: state
              - Modified property: offering_plugin_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedPluginOptions
                    - Properties changed
                      - New property: openstack_offering_uuid_list

POST /api/marketplace-robot-accounts/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: error_message
            - New required property: error_traceback
            - New required property: state
          - Properties changed
            - New property: error_message
            - New property: error_traceback
            - New property: state

GET /api/marketplace-robot-accounts/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: error_message
            - New required property: error_traceback
            - New required property: state
          - Properties changed
            - New property: error_message
            - New property: error_traceback
            - New property: state
            - Modified property: offering_plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: openstack_offering_uuid_list

PATCH /api/marketplace-robot-accounts/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: error_message
            - New required property: error_traceback
            - New required property: state
          - Properties changed
            - New property: error_message
            - New property: error_traceback
            - New property: state

PUT /api/marketplace-robot-accounts/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: error_message
            - New required property: error_traceback
            - New required property: state
          - Properties changed
            - New property: error_message
            - New property: error_traceback
            - New property: state

POST /api/marketplace-screenshots/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PATCH /api/marketplace-screenshots/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/marketplace-screenshots/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/marketplace-script-dry-run/{uuid}/async_run/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: scope_error_message
            - Modified property: customer_name
              - Nullable changed from false to true
            - Modified property: customer_uuid
              - Nullable changed from false to true
            - Modified property: google_calendar_is_public
              - Nullable changed from false to true
            - Modified property: parent_description
              - Nullable changed from false to true
            - Modified property: parent_name
              - Nullable changed from false to true
            - Modified property: parent_uuid
              - Nullable changed from false to true
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: openstack_offering_uuid_list
            - Modified property: project_name
              - Nullable changed from false to true
            - Modified property: project_uuid
              - Nullable changed from false to true

POST /api/marketplace-script-dry-run/{uuid}/run/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: scope_error_message
            - Modified property: customer_name
              - Nullable changed from false to true
            - Modified property: customer_uuid
              - Nullable changed from false to true
            - Modified property: google_calendar_is_public
              - Nullable changed from false to true
            - Modified property: parent_description
              - Nullable changed from false to true
            - Modified property: parent_name
              - Nullable changed from false to true
            - Modified property: parent_uuid
              - Nullable changed from false to true
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: openstack_offering_uuid_list
            - Modified property: project_name
              - Nullable changed from false to true
            - Modified property: project_uuid
              - Nullable changed from false to true

POST /api/marketplace-script-sync-resource/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/marketplace-sections/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PATCH /api/marketplace-sections/{key}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/marketplace-sections/{key}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/marketplace-service-providers/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

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
                      - New property: rancher_offering_uuid

PATCH /api/marketplace-service-providers/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/marketplace-service-providers/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/marketplace-service-providers/{uuid}/add_user/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/marketplace-service-providers/{uuid}/delete_user/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/marketplace-service-providers/{uuid}/set_offerings_username/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/marketplace-service-providers/{uuid}/update_user/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/notification-messages-templates/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PATCH /api/notification-messages-templates/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/notification-messages-templates/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/notification-messages-templates/{uuid}/override/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/notification-messages/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PATCH /api/notification-messages/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/notification-messages/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PATCH /api/openstack-backups/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/openstack-backups/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/openstack-backups/{uuid}/restore/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: volumes
              - Items changed
                - Properties changed
                  - Modified property: marketplace_resource_uuid
                    - Nullable changed from false to true

GET /api/openstack-floating-ips/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: instance_name
                - Nullable changed from false to true
              - Modified property: instance_url
                - Nullable changed from false to true
              - Modified property: instance_uuid
                - Nullable changed from false to true

GET /api/openstack-floating-ips/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: instance_name
              - Nullable changed from false to true
            - Modified property: instance_url
              - Nullable changed from false to true
            - Modified property: instance_uuid
              - Nullable changed from false to true

POST /api/openstack-floating-ips/{uuid}/attach_to_port/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/openstack-floating-ips/{uuid}/update_description/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

GET /api/openstack-instances/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: volumes
                - Items changed
                  - Properties changed
                    - Modified property: marketplace_resource_uuid
                      - Nullable changed from false to true

GET /api/openstack-instances/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: volumes
              - Items changed
                - Properties changed
                  - Modified property: marketplace_resource_uuid
                    - Nullable changed from false to true

PATCH /api/openstack-instances/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: volumes
              - Items changed
                - Properties changed
                  - Modified property: marketplace_resource_uuid
                    - Nullable changed from false to true

PUT /api/openstack-instances/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: volumes
              - Items changed
                - Properties changed
                  - Modified property: marketplace_resource_uuid
                    - Nullable changed from false to true

POST /api/openstack-instances/{uuid}/backup/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/openstack-instances/{uuid}/change_flavor/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/openstack-instances/{uuid}/update_allowed_address_pairs/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/openstack-instances/{uuid}/update_floating_ips/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/openstack-instances/{uuid}/update_ports/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/openstack-instances/{uuid}/update_security_groups/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/openstack-migrations/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PATCH /api/openstack-migrations/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/openstack-migrations/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PATCH /api/openstack-networks/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/openstack-networks/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/openstack-networks/{uuid}/create_port/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/openstack-networks/{uuid}/create_subnet/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/openstack-networks/{uuid}/set_mtu/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/openstack-routers/{uuid}/set_routes/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PATCH /api/openstack-security-groups/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/openstack-security-groups/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/openstack-security-groups/{uuid}/set_rules/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/openstack-server-groups/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PATCH /api/openstack-server-groups/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/openstack-server-groups/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PATCH /api/openstack-snapshots/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/openstack-snapshots/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/openstack-snapshots/{uuid}/restore/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PATCH /api/openstack-subnets/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/openstack-subnets/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/openstack-tenants/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PATCH /api/openstack-tenants/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/openstack-tenants/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/openstack-tenants/{uuid}/change_password/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/openstack-tenants/{uuid}/create_floating_ip/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: instance_name
              - Nullable changed from false to true
            - Modified property: instance_url
              - Nullable changed from false to true
            - Modified property: instance_uuid
              - Nullable changed from false to true

POST /api/openstack-tenants/{uuid}/create_network/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/openstack-tenants/{uuid}/create_security_group/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/openstack-tenants/{uuid}/create_server_group/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/openstack-tenants/{uuid}/set_quotas/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PATCH /api/openstack-volumes/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/openstack-volumes/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/openstack-volumes/{uuid}/attach/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/openstack-volumes/{uuid}/extend/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/openstack-volumes/{uuid}/retype/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/openstack-volumes/{uuid}/snapshot/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/organization-groups/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PATCH /api/organization-groups/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/organization-groups/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/override-settings/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/payment-profiles/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PATCH /api/payment-profiles/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/payment-profiles/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/payments/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PATCH /api/payments/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/payments/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/payments/{uuid}/link_to_invoice/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/project-credits/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PATCH /api/project-credits/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/project-credits/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/projects/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PATCH /api/projects/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/projects/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/projects/{uuid}/add_user/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/projects/{uuid}/delete_user/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/projects/{uuid}/move_project/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

GET /api/projects/{uuid}/stats/

- Description changed from '' to 'Return statistics about project resources usage'
- New query param: for_current_month

POST /api/projects/{uuid}/update_user/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/promotions-campaigns/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/promotions-campaigns/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/proposal-proposals/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/proposal-proposals/{uuid}/add_user/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/proposal-proposals/{uuid}/approve/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/proposal-proposals/{uuid}/attach_document/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/proposal-proposals/{uuid}/delete_user/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/proposal-proposals/{uuid}/reject/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/proposal-proposals/{uuid}/resources/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PATCH /api/proposal-proposals/{uuid}/resources/{obj_uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/proposal-proposals/{uuid}/resources/{obj_uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/proposal-proposals/{uuid}/update_project_details/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/proposal-proposals/{uuid}/update_user/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/proposal-protected-calls/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PATCH /api/proposal-protected-calls/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/proposal-protected-calls/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/proposal-protected-calls/{uuid}/add_user/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/proposal-protected-calls/{uuid}/attach_documents/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/proposal-protected-calls/{uuid}/delete_user/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/proposal-protected-calls/{uuid}/detach_documents/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/proposal-protected-calls/{uuid}/offerings/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PATCH /api/proposal-protected-calls/{uuid}/offerings/{obj_uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/proposal-protected-calls/{uuid}/offerings/{obj_uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/proposal-protected-calls/{uuid}/rounds/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PATCH /api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/close/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/proposal-protected-calls/{uuid}/update_user/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/proposal-reviews/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PATCH /api/proposal-reviews/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/proposal-reviews/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/proposal-reviews/{uuid}/submit/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/query/

- Description changed from '' to 'Execute SQL query against readonly database'
- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data
- Responses changed
  - New response: 400
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Type changed from 'object' to 'array'
          - Items changed
            - Schema added
          - Required changed
            - Deleted required property: query
          - Properties changed
            - Deleted property: query

POST /api/rancher-apps/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PATCH /api/rancher-apps/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/rancher-apps/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/rancher-catalogs/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PATCH /api/rancher-catalogs/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/rancher-catalogs/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/rancher-catalogs/{uuid}/refresh/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/rancher-clusters/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PATCH /api/rancher-clusters/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/rancher-clusters/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/rancher-clusters/{uuid}/create_management_security_group/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/rancher-clusters/{uuid}/import_yaml/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/rancher-hpas/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PATCH /api/rancher-hpas/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/rancher-hpas/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/rancher-hpas/{uuid}/yaml/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/rancher-ingresses/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PATCH /api/rancher-ingresses/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/rancher-ingresses/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/rancher-ingresses/{uuid}/yaml/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/rancher-nodes/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/rancher-nodes/{uuid}/link_openstack/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/rancher-services/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PATCH /api/rancher-services/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/rancher-services/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/rancher-services/{uuid}/yaml/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/rancher-workloads/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PATCH /api/rancher-workloads/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/rancher-workloads/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/rancher-workloads/{uuid}/yaml/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/remote-eduteams/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/remote-waldur-api/import_offering/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/remote-waldur-api/remote_categories/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/remote-waldur-api/remote_customers/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/remote-waldur-api/shared_offerings/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/roles/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PATCH /api/roles/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/roles/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/roles/{uuid}/update_descriptions/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/slurm-allocations/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PATCH /api/slurm-allocations/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/slurm-allocations/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/slurm-allocations/{uuid}/set_limits/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/slurm-jobs/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PATCH /api/slurm-jobs/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/slurm-jobs/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/support-attachments/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PATCH /api/support-comments/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/support-comments/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/support-feedbacks/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/support-issues/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PATCH /api/support-issues/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/support-issues/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/support-issues/{uuid}/comment/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/support-issues/{uuid}/sync/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/support-jira-webhook/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/support-smax-webhook/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/support-templates/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PATCH /api/support-templates/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/support-templates/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/support-templates/{uuid}/create_attachments/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/support-templates/{uuid}/delete_attachments/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/user-agreements/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PATCH /api/user-agreements/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/user-agreements/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/user-group-invitations/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/user-invitations/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/user-invitations/approve/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/user-invitations/reject/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/user-permission-requests/{uuid}/approve/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/user-permission-requests/{uuid}/reject/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/users/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/users/confirm_email/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PATCH /api/users/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/users/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/users/{uuid}/change_email/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/users/{uuid}/change_password/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/vmware-disks/{uuid}/extend/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/vmware-virtual-machine/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PATCH /api/vmware-virtual-machine/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

PUT /api/vmware-virtual-machine/{uuid}/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/vmware-virtual-machine/{uuid}/create_disk/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

POST /api/vmware-virtual-machine/{uuid}/create_port/

- Request body changed
  - Content changed
    - Deleted media type: application/x-www-form-urlencoded
    - Deleted media type: multipart/form-data

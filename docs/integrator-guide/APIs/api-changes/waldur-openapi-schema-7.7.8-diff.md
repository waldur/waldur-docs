# OpenAPI schema diff - 7.7.8

## For version 7.7.8

### New Endpoints: 20

---------------------
GET /api/marketplace-course-accounts/  
HEAD /api/marketplace-course-accounts/  
POST /api/marketplace-course-accounts/  
POST /api/marketplace-course-accounts/create_bulk/  
DELETE /api/marketplace-course-accounts/{uuid}/  
GET /api/marketplace-course-accounts/{uuid}/  
GET /api/marketplace-service-providers/{service_provider_uuid}/course_accounts/  
GET /api/project-permissions-reviews/  
HEAD /api/project-permissions-reviews/  
GET /api/project-permissions-reviews/{uuid}/  
POST /api/project-permissions-reviews/{uuid}/close/  
GET /api/support-issue-statuses/  
HEAD /api/support-issue-statuses/  
POST /api/support-issue-statuses/  
DELETE /api/support-issue-statuses/{uuid}/  
GET /api/support-issue-statuses/{uuid}/  
PATCH /api/support-issue-statuses/{uuid}/  
PUT /api/support-issue-statuses/{uuid}/  
POST /api/user-permission-requests/{uuid}/cancel_request/  
POST /projects/{uuid}/sync_user_roles/  

### Deleted Endpoints: 1

------------------------
POST /api/projects/{uuid}/sync_user_roles/  

### Modified Endpoints: 133

---------------------------
GET /api/customer-permissions-reviews/

- New query param: closed
- Modified query param: customer_uuid
  - Description changed from '' to 'Customer UUID'
- Modified query param: is_pending
  - Description changed from '' to 'Is pending'
- Modified query param: reviewer_uuid
  - Description changed from '' to 'Reviewer UUID'

HEAD /api/customer-permissions-reviews/

- New query param: closed
- Modified query param: customer_uuid
  - Description changed from '' to 'Customer UUID'
- Modified query param: is_pending
  - Description changed from '' to 'Is pending'
- Modified query param: reviewer_uuid
  - Description changed from '' to 'Reviewer UUID'

GET /api/customers/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [description]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: description

POST /api/customers/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: description
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: description

GET /api/customers/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [description]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: description

PATCH /api/customers/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: description
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: description

PUT /api/customers/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: description
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: description

GET /api/customers/{uuid}/users/

- New query param: agreement_date
- New query param: date_joined
- New query param: modified
- Modified path param: uuid
  - Name changed from 'uuid' to 'customer_uuid'
  - Description changed from '' to 'UUID of the customer'
- Modified query param: full_name
  - Description changed from '' to 'Full name'
- Modified query param: is_active
  - Schema changed
    - Type changed from 'string' to 'boolean'
- Modified query param: o
  - Description changed from '' to 'Ordering. Sort by a combination of first name, last name, and username.'
  - Schema changed
    - New enum values: [concatenated_name -concatenated_name]
- Modified query param: organization_role
  - Description changed from '' to 'Filter by one or more organization roles. Select a standard role or provide a custom role string. Can be specified multiple times.'
  - Schema changed
    - Type changed from 'string' to 'array'
    - Items changed
      - Schema added
- Modified query param: project_role
  - Description changed from '' to 'Filter by one or more project roles. Select a standard role or provide a custom role string. Can be specified multiple times.'
  - Schema changed
    - Type changed from 'string' to 'array'
    - Items changed
      - Schema added
- Modified query param: user_keyword
  - Description changed from '' to 'User keyword'

GET /api/event-subscriptions/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: source_ip
                - Property 'OneOf' changed
                  - Schemas added: subschema #1, subschema #2
                - Type changed from 'string' to ''
                - Description changed from '' to 'An IPv4 or IPv6 address.'

POST /api/event-subscriptions/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: source_ip
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''
              - Description changed from '' to 'An IPv4 or IPv6 address.'

GET /api/event-subscriptions/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: source_ip
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''
              - Description changed from '' to 'An IPv4 or IPv6 address.'

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
                  - New enum values: [customer_permission_review_created customer_permission_review_closed project_permission_review_created project_permission_review_closed]

POST /api/hooks-email/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [customer_permission_review_created customer_permission_review_closed project_permission_review_created project_permission_review_closed]
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [customer_permission_review_created customer_permission_review_closed project_permission_review_created project_permission_review_closed]

GET /api/hooks-email/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [customer_permission_review_created customer_permission_review_closed project_permission_review_created project_permission_review_closed]

PATCH /api/hooks-email/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [customer_permission_review_created customer_permission_review_closed project_permission_review_created project_permission_review_closed]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [customer_permission_review_created customer_permission_review_closed project_permission_review_created project_permission_review_closed]

PUT /api/hooks-email/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [customer_permission_review_created customer_permission_review_closed project_permission_review_created project_permission_review_closed]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [customer_permission_review_created customer_permission_review_closed project_permission_review_created project_permission_review_closed]

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
                  - New enum values: [customer_permission_review_created customer_permission_review_closed project_permission_review_created project_permission_review_closed]

POST /api/hooks-web/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [customer_permission_review_created customer_permission_review_closed project_permission_review_created project_permission_review_closed]
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [customer_permission_review_created customer_permission_review_closed project_permission_review_created project_permission_review_closed]

GET /api/hooks-web/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [customer_permission_review_created customer_permission_review_closed project_permission_review_created project_permission_review_closed]

PATCH /api/hooks-web/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [customer_permission_review_created customer_permission_review_closed project_permission_review_created project_permission_review_closed]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [customer_permission_review_created customer_permission_review_closed project_permission_review_created project_permission_review_closed]

PUT /api/hooks-web/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [customer_permission_review_created customer_permission_review_closed project_permission_review_created project_permission_review_closed]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [customer_permission_review_created customer_permission_review_closed project_permission_review_created project_permission_review_closed]

GET /api/invoices/{uuid}/items/

- New query param: o

GET /api/marketplace-customer-service-accounts/

- New query param: state
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: state
            - Properties changed
              - New property: state

HEAD /api/marketplace-customer-service-accounts/

- New query param: state

POST /api/marketplace-customer-service-accounts/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: state
          - Properties changed
            - New property: state

GET /api/marketplace-customer-service-accounts/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: state
          - Properties changed
            - New property: state

PATCH /api/marketplace-customer-service-accounts/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: state
          - Properties changed
            - New property: state

PUT /api/marketplace-customer-service-accounts/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: state
          - Properties changed
            - New property: state

POST /api/marketplace-customer-service-accounts/{uuid}/rotate_api_key/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: state
          - Properties changed
            - New property: state

GET /api/marketplace-offering-users/{uuid}/checklist/

- Extensions changed
  - Deleted extension: x-permissions

GET /api/marketplace-offering-users/{uuid}/completion_status/

- Extensions changed
  - Deleted extension: x-permissions

POST /api/marketplace-offering-users/{uuid}/submit_answers/

- Extensions changed
  - Deleted extension: x-permissions

POST /api/marketplace-orders/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: attributes
            - Property 'OneOf' changed
              - Modified schema: #/components/schemas/OpenStackInstanceCreateOrderAttributes
                - Properties changed
                  - Modified property: ports
                    - Items changed
                      - Properties changed
                        - Modified property: fixed_ips
                          - Items changed
                            - Properties changed
                              - Modified property: ip_address
                                - Property 'OneOf' changed
                                  - Schemas added: subschema #1, subschema #2
                                - Type changed from 'string' to ''

GET /api/marketplace-project-service-accounts/

- New query param: state
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: state
            - Properties changed
              - New property: state

HEAD /api/marketplace-project-service-accounts/

- New query param: state

POST /api/marketplace-project-service-accounts/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: state
          - Properties changed
            - New property: state

GET /api/marketplace-project-service-accounts/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: state
          - Properties changed
            - New property: state

PATCH /api/marketplace-project-service-accounts/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: state
          - Properties changed
            - New property: state

PUT /api/marketplace-project-service-accounts/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: state
          - Properties changed
            - New property: state

POST /api/marketplace-project-service-accounts/{uuid}/rotate_api_key/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: state
          - Properties changed
            - New property: state

GET /api/marketplace-provider-offerings/{uuid}/list_customer_projects/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: kind

GET /api/marketplace-robot-accounts/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: state
                - Property 'AllOf' changed
                  - Schemas deleted: #/components/schemas/RobotAccountStates
                - Type changed from '' to 'string'

POST /api/marketplace-robot-accounts/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: state
              - Property 'AllOf' changed
                - Schemas deleted: #/components/schemas/RobotAccountStates
              - Type changed from '' to 'string'

GET /api/marketplace-robot-accounts/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: state
              - Property 'AllOf' changed
                - Schemas deleted: #/components/schemas/RobotAccountStates
              - Type changed from '' to 'string'

PATCH /api/marketplace-robot-accounts/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: state
              - Property 'AllOf' changed
                - Schemas deleted: #/components/schemas/RobotAccountStates
              - Type changed from '' to 'string'

PUT /api/marketplace-robot-accounts/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: state
              - Property 'AllOf' changed
                - Schemas deleted: #/components/schemas/RobotAccountStates
              - Type changed from '' to 'string'

POST /api/marketplace-robot-accounts/{uuid}/set_state_creating/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: state
              - Property 'AllOf' changed
                - Schemas deleted: #/components/schemas/RobotAccountStates
              - Type changed from '' to 'string'

POST /api/marketplace-robot-accounts/{uuid}/set_state_deleted/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: state
              - Property 'AllOf' changed
                - Schemas deleted: #/components/schemas/RobotAccountStates
              - Type changed from '' to 'string'

POST /api/marketplace-robot-accounts/{uuid}/set_state_erred/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: state
              - Property 'AllOf' changed
                - Schemas deleted: #/components/schemas/RobotAccountStates
              - Type changed from '' to 'string'

POST /api/marketplace-robot-accounts/{uuid}/set_state_ok/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: state
              - Property 'AllOf' changed
                - Schemas deleted: #/components/schemas/RobotAccountStates
              - Type changed from '' to 'string'

POST /api/marketplace-robot-accounts/{uuid}/set_state_request_deletion/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: state
              - Property 'AllOf' changed
                - Schemas deleted: #/components/schemas/RobotAccountStates
              - Type changed from '' to 'string'

GET /api/marketplace-service-providers/{service_provider_uuid}/project_service_accounts/

- New query param: state
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: state
            - Properties changed
              - New property: state

GET /api/marketplace-service-providers/{service_provider_uuid}/projects/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [kind]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: kind

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
                    - Modified property: address
                      - Property 'OneOf' changed
                        - Schemas added: subschema #1, subschema #2
                      - Type changed from 'string' to ''
                    - Modified property: port_fixed_ips
                      - Items changed
                        - Properties changed
                          - Modified property: ip_address
                            - Property 'OneOf' changed
                              - Schemas added: subschema #1, subschema #2
                            - Type changed from 'string' to ''
              - Modified property: instance_ports
                - Items changed
                  - Properties changed
                    - Modified property: fixed_ips
                      - Items changed
                        - Properties changed
                          - Modified property: ip_address
                            - Property 'OneOf' changed
                              - Schemas added: subschema #1, subschema #2
                            - Type changed from 'string' to ''
              - Modified property: restorations
                - Items changed
                  - Properties changed
                    - Modified property: floating_ips
                      - Items changed
                        - Properties changed
                          - Modified property: address
                            - Property 'OneOf' changed
                              - Schemas added: subschema #1, subschema #2
                            - Type changed from 'string' to ''
                          - Modified property: port_fixed_ips
                            - Items changed
                              - Properties changed
                                - Modified property: ip_address
                                  - Property 'OneOf' changed
                                    - Schemas added: subschema #1, subschema #2
                                  - Type changed from 'string' to ''
                    - Modified property: ports
                      - Items changed
                        - Properties changed
                          - Modified property: fixed_ips
                            - Items changed
                              - Properties changed
                                - Modified property: ip_address
                                  - Property 'OneOf' changed
                                    - Schemas added: subschema #1, subschema #2
                                  - Type changed from 'string' to ''

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
                  - Modified property: address
                    - Property 'OneOf' changed
                      - Schemas added: subschema #1, subschema #2
                    - Type changed from 'string' to ''
                  - Modified property: port_fixed_ips
                    - Items changed
                      - Properties changed
                        - Modified property: ip_address
                          - Property 'OneOf' changed
                            - Schemas added: subschema #1, subschema #2
                          - Type changed from 'string' to ''
            - Modified property: instance_ports
              - Items changed
                - Properties changed
                  - Modified property: fixed_ips
                    - Items changed
                      - Properties changed
                        - Modified property: ip_address
                          - Property 'OneOf' changed
                            - Schemas added: subschema #1, subschema #2
                          - Type changed from 'string' to ''
            - Modified property: restorations
              - Items changed
                - Properties changed
                  - Modified property: floating_ips
                    - Items changed
                      - Properties changed
                        - Modified property: address
                          - Property 'OneOf' changed
                            - Schemas added: subschema #1, subschema #2
                          - Type changed from 'string' to ''
                        - Modified property: port_fixed_ips
                          - Items changed
                            - Properties changed
                              - Modified property: ip_address
                                - Property 'OneOf' changed
                                  - Schemas added: subschema #1, subschema #2
                                - Type changed from 'string' to ''
                  - Modified property: ports
                    - Items changed
                      - Properties changed
                        - Modified property: fixed_ips
                          - Items changed
                            - Properties changed
                              - Modified property: ip_address
                                - Property 'OneOf' changed
                                  - Schemas added: subschema #1, subschema #2
                                - Type changed from 'string' to ''

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
                  - Modified property: address
                    - Property 'OneOf' changed
                      - Schemas added: subschema #1, subschema #2
                    - Type changed from 'string' to ''
                  - Modified property: port_fixed_ips
                    - Items changed
                      - Properties changed
                        - Modified property: ip_address
                          - Property 'OneOf' changed
                            - Schemas added: subschema #1, subschema #2
                          - Type changed from 'string' to ''
            - Modified property: instance_ports
              - Items changed
                - Properties changed
                  - Modified property: fixed_ips
                    - Items changed
                      - Properties changed
                        - Modified property: ip_address
                          - Property 'OneOf' changed
                            - Schemas added: subschema #1, subschema #2
                          - Type changed from 'string' to ''
            - Modified property: restorations
              - Items changed
                - Properties changed
                  - Modified property: floating_ips
                    - Items changed
                      - Properties changed
                        - Modified property: address
                          - Property 'OneOf' changed
                            - Schemas added: subschema #1, subschema #2
                          - Type changed from 'string' to ''
                        - Modified property: port_fixed_ips
                          - Items changed
                            - Properties changed
                              - Modified property: ip_address
                                - Property 'OneOf' changed
                                  - Schemas added: subschema #1, subschema #2
                                - Type changed from 'string' to ''
                  - Modified property: ports
                    - Items changed
                      - Properties changed
                        - Modified property: fixed_ips
                          - Items changed
                            - Properties changed
                              - Modified property: ip_address
                                - Property 'OneOf' changed
                                  - Schemas added: subschema #1, subschema #2
                                - Type changed from 'string' to ''

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
                  - Modified property: address
                    - Property 'OneOf' changed
                      - Schemas added: subschema #1, subschema #2
                    - Type changed from 'string' to ''
                  - Modified property: port_fixed_ips
                    - Items changed
                      - Properties changed
                        - Modified property: ip_address
                          - Property 'OneOf' changed
                            - Schemas added: subschema #1, subschema #2
                          - Type changed from 'string' to ''
            - Modified property: instance_ports
              - Items changed
                - Properties changed
                  - Modified property: fixed_ips
                    - Items changed
                      - Properties changed
                        - Modified property: ip_address
                          - Property 'OneOf' changed
                            - Schemas added: subschema #1, subschema #2
                          - Type changed from 'string' to ''
            - Modified property: restorations
              - Items changed
                - Properties changed
                  - Modified property: floating_ips
                    - Items changed
                      - Properties changed
                        - Modified property: address
                          - Property 'OneOf' changed
                            - Schemas added: subschema #1, subschema #2
                          - Type changed from 'string' to ''
                        - Modified property: port_fixed_ips
                          - Items changed
                            - Properties changed
                              - Modified property: ip_address
                                - Property 'OneOf' changed
                                  - Schemas added: subschema #1, subschema #2
                                - Type changed from 'string' to ''
                  - Modified property: ports
                    - Items changed
                      - Properties changed
                        - Modified property: fixed_ips
                          - Items changed
                            - Properties changed
                              - Modified property: ip_address
                                - Property 'OneOf' changed
                                  - Schemas added: subschema #1, subschema #2
                                - Type changed from 'string' to ''

POST /api/openstack-backups/{uuid}/restore/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: ports
            - Items changed
              - Properties changed
                - Modified property: fixed_ips
                  - Items changed
                    - Properties changed
                      - Modified property: ip_address
                        - Property 'OneOf' changed
                          - Schemas added: subschema #1, subschema #2
                        - Type changed from 'string' to ''
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: floating_ips
              - Items changed
                - Properties changed
                  - Modified property: address
                    - Property 'OneOf' changed
                      - Schemas added: subschema #1, subschema #2
                    - Type changed from 'string' to ''
                  - Modified property: port_fixed_ips
                    - Items changed
                      - Properties changed
                        - Modified property: ip_address
                          - Property 'OneOf' changed
                            - Schemas added: subschema #1, subschema #2
                          - Type changed from 'string' to ''
            - Modified property: ports
              - Items changed
                - Properties changed
                  - Modified property: fixed_ips
                    - Items changed
                      - Properties changed
                        - Modified property: ip_address
                          - Property 'OneOf' changed
                            - Schemas added: subschema #1, subschema #2
                          - Type changed from 'string' to ''

GET /api/openstack-floating-ips/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: address
                - Property 'OneOf' changed
                  - Schemas added: subschema #1, subschema #2
                - Type changed from 'string' to ''
              - Modified property: external_address
                - Property 'OneOf' changed
                  - Schemas added: subschema #1, subschema #2
                - Type changed from 'string' to ''
              - Modified property: port_fixed_ips
                - Items changed
                  - Properties changed
                    - Modified property: ip_address
                      - Property 'OneOf' changed
                        - Schemas added: subschema #1, subschema #2
                      - Type changed from 'string' to ''

GET /api/openstack-floating-ips/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: address
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''
            - Modified property: external_address
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''
            - Modified property: port_fixed_ips
              - Items changed
                - Properties changed
                  - Modified property: ip_address
                    - Property 'OneOf' changed
                      - Schemas added: subschema #1, subschema #2
                    - Type changed from 'string' to ''

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
                    - Modified property: address
                      - Property 'OneOf' changed
                        - Schemas added: subschema #1, subschema #2
                      - Type changed from 'string' to ''
                    - Modified property: port_fixed_ips
                      - Items changed
                        - Properties changed
                          - Modified property: ip_address
                            - Property 'OneOf' changed
                              - Schemas added: subschema #1, subschema #2
                            - Type changed from 'string' to ''
              - Modified property: ports
                - Items changed
                  - Properties changed
                    - Modified property: fixed_ips
                      - Items changed
                        - Properties changed
                          - Modified property: ip_address
                            - Property 'OneOf' changed
                              - Schemas added: subschema #1, subschema #2
                            - Type changed from 'string' to ''

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
                  - Modified property: address
                    - Property 'OneOf' changed
                      - Schemas added: subschema #1, subschema #2
                    - Type changed from 'string' to ''
                  - Modified property: port_fixed_ips
                    - Items changed
                      - Properties changed
                        - Modified property: ip_address
                          - Property 'OneOf' changed
                            - Schemas added: subschema #1, subschema #2
                          - Type changed from 'string' to ''
            - Modified property: ports
              - Items changed
                - Properties changed
                  - Modified property: fixed_ips
                    - Items changed
                      - Properties changed
                        - Modified property: ip_address
                          - Property 'OneOf' changed
                            - Schemas added: subschema #1, subschema #2
                          - Type changed from 'string' to ''

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
                  - Modified property: address
                    - Property 'OneOf' changed
                      - Schemas added: subschema #1, subschema #2
                    - Type changed from 'string' to ''
                  - Modified property: port_fixed_ips
                    - Items changed
                      - Properties changed
                        - Modified property: ip_address
                          - Property 'OneOf' changed
                            - Schemas added: subschema #1, subschema #2
                          - Type changed from 'string' to ''
            - Modified property: ports
              - Items changed
                - Properties changed
                  - Modified property: fixed_ips
                    - Items changed
                      - Properties changed
                        - Modified property: ip_address
                          - Property 'OneOf' changed
                            - Schemas added: subschema #1, subschema #2
                          - Type changed from 'string' to ''

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
                  - Modified property: address
                    - Property 'OneOf' changed
                      - Schemas added: subschema #1, subschema #2
                    - Type changed from 'string' to ''
                  - Modified property: port_fixed_ips
                    - Items changed
                      - Properties changed
                        - Modified property: ip_address
                          - Property 'OneOf' changed
                            - Schemas added: subschema #1, subschema #2
                          - Type changed from 'string' to ''
            - Modified property: ports
              - Items changed
                - Properties changed
                  - Modified property: fixed_ips
                    - Items changed
                      - Properties changed
                        - Modified property: ip_address
                          - Property 'OneOf' changed
                            - Schemas added: subschema #1, subschema #2
                          - Type changed from 'string' to ''

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
                  - Modified property: address
                    - Property 'OneOf' changed
                      - Schemas added: subschema #1, subschema #2
                    - Type changed from 'string' to ''
                  - Modified property: port_fixed_ips
                    - Items changed
                      - Properties changed
                        - Modified property: ip_address
                          - Property 'OneOf' changed
                            - Schemas added: subschema #1, subschema #2
                          - Type changed from 'string' to ''
            - Modified property: instance_ports
              - Items changed
                - Properties changed
                  - Modified property: fixed_ips
                    - Items changed
                      - Properties changed
                        - Modified property: ip_address
                          - Property 'OneOf' changed
                            - Schemas added: subschema #1, subschema #2
                          - Type changed from 'string' to ''
            - Modified property: restorations
              - Items changed
                - Properties changed
                  - Modified property: floating_ips
                    - Items changed
                      - Properties changed
                        - Modified property: address
                          - Property 'OneOf' changed
                            - Schemas added: subschema #1, subschema #2
                          - Type changed from 'string' to ''
                        - Modified property: port_fixed_ips
                          - Items changed
                            - Properties changed
                              - Modified property: ip_address
                                - Property 'OneOf' changed
                                  - Schemas added: subschema #1, subschema #2
                                - Type changed from 'string' to ''
                  - Modified property: ports
                    - Items changed
                      - Properties changed
                        - Modified property: fixed_ips
                          - Items changed
                            - Properties changed
                              - Modified property: ip_address
                                - Property 'OneOf' changed
                                  - Schemas added: subschema #1, subschema #2
                                - Type changed from 'string' to ''

GET /api/openstack-instances/{uuid}/floating_ips/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: address
                - Property 'OneOf' changed
                  - Schemas added: subschema #1, subschema #2
                - Type changed from 'string' to ''
              - Modified property: port_fixed_ips
                - Items changed
                  - Properties changed
                    - Modified property: ip_address
                      - Property 'OneOf' changed
                        - Schemas added: subschema #1, subschema #2
                      - Type changed from 'string' to ''

GET /api/openstack-instances/{uuid}/ports/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: fixed_ips
                - Items changed
                  - Properties changed
                    - Modified property: ip_address
                      - Property 'OneOf' changed
                        - Schemas added: subschema #1, subschema #2
                      - Type changed from 'string' to ''

POST /api/openstack-instances/{uuid}/update_ports/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: ports
            - Items changed
              - Properties changed
                - Modified property: fixed_ips
                  - Items changed
                    - Properties changed
                      - Modified property: ip_address
                        - Property 'OneOf' changed
                          - Schemas added: subschema #1, subschema #2
                        - Type changed from 'string' to ''

GET /api/openstack-networks/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: subnets
                - Items changed
                  - Properties changed
                    - Modified property: allocation_pools
                      - Items changed
                        - Properties changed
                          - Modified property: end
                            - Property 'OneOf' changed
                              - Schemas added: subschema #1, subschema #2
                            - Type changed from 'string' to ''
                            - Description changed from '' to 'An IPv4 or IPv6 address.'
                          - Modified property: start
                            - Property 'OneOf' changed
                              - Schemas added: subschema #1, subschema #2
                            - Type changed from 'string' to ''
                            - Description changed from '' to 'An IPv4 or IPv6 address.'
                    - Modified property: gateway_ip
                      - Property 'OneOf' changed
                        - Schemas added: subschema #1, subschema #2
                      - Type changed from 'string' to ''

GET /api/openstack-networks/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: subnets
              - Items changed
                - Properties changed
                  - Modified property: allocation_pools
                    - Items changed
                      - Properties changed
                        - Modified property: end
                          - Property 'OneOf' changed
                            - Schemas added: subschema #1, subschema #2
                          - Type changed from 'string' to ''
                          - Description changed from '' to 'An IPv4 or IPv6 address.'
                        - Modified property: start
                          - Property 'OneOf' changed
                            - Schemas added: subschema #1, subschema #2
                          - Type changed from 'string' to ''
                          - Description changed from '' to 'An IPv4 or IPv6 address.'
                  - Modified property: gateway_ip
                    - Property 'OneOf' changed
                      - Schemas added: subschema #1, subschema #2
                    - Type changed from 'string' to ''

PATCH /api/openstack-networks/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: subnets
              - Items changed
                - Properties changed
                  - Modified property: allocation_pools
                    - Items changed
                      - Properties changed
                        - Modified property: end
                          - Property 'OneOf' changed
                            - Schemas added: subschema #1, subschema #2
                          - Type changed from 'string' to ''
                          - Description changed from '' to 'An IPv4 or IPv6 address.'
                        - Modified property: start
                          - Property 'OneOf' changed
                            - Schemas added: subschema #1, subschema #2
                          - Type changed from 'string' to ''
                          - Description changed from '' to 'An IPv4 or IPv6 address.'
                  - Modified property: gateway_ip
                    - Property 'OneOf' changed
                      - Schemas added: subschema #1, subschema #2
                    - Type changed from 'string' to ''

PUT /api/openstack-networks/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: subnets
              - Items changed
                - Properties changed
                  - Modified property: allocation_pools
                    - Items changed
                      - Properties changed
                        - Modified property: end
                          - Property 'OneOf' changed
                            - Schemas added: subschema #1, subschema #2
                          - Type changed from 'string' to ''
                          - Description changed from '' to 'An IPv4 or IPv6 address.'
                        - Modified property: start
                          - Property 'OneOf' changed
                            - Schemas added: subschema #1, subschema #2
                          - Type changed from 'string' to ''
                          - Description changed from '' to 'An IPv4 or IPv6 address.'
                  - Modified property: gateway_ip
                    - Property 'OneOf' changed
                      - Schemas added: subschema #1, subschema #2
                    - Type changed from 'string' to ''

POST /api/openstack-networks/{uuid}/create_subnet/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: allocation_pools
            - Items changed
              - Properties changed
                - Modified property: end
                  - Property 'OneOf' changed
                    - Schemas added: subschema #1, subschema #2
                  - Type changed from 'string' to ''
                  - Description changed from '' to 'An IPv4 or IPv6 address.'
                - Modified property: start
                  - Property 'OneOf' changed
                    - Schemas added: subschema #1, subschema #2
                  - Type changed from 'string' to ''
                  - Description changed from '' to 'An IPv4 or IPv6 address.'
          - Modified property: dns_nameservers
            - Items changed
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''
              - Description changed from '' to 'An IPv4 or IPv6 address.'
          - Modified property: gateway_ip
            - Property 'OneOf' changed
              - Schemas added: subschema #1, subschema #2
            - Type changed from 'string' to ''
          - Modified property: host_routes
            - Items changed
              - Properties changed
                - Modified property: nexthop
                  - Property 'OneOf' changed
                    - Schemas added: subschema #1, subschema #2
                  - Type changed from 'string' to ''
                  - Description changed from '' to 'An IPv4 or IPv6 address.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: allocation_pools
              - Items changed
                - Properties changed
                  - Modified property: end
                    - Property 'OneOf' changed
                      - Schemas added: subschema #1, subschema #2
                    - Type changed from 'string' to ''
                    - Description changed from '' to 'An IPv4 or IPv6 address.'
                  - Modified property: start
                    - Property 'OneOf' changed
                      - Schemas added: subschema #1, subschema #2
                    - Type changed from 'string' to ''
                    - Description changed from '' to 'An IPv4 or IPv6 address.'
            - Modified property: dns_nameservers
              - Items changed
                - Property 'OneOf' changed
                  - Schemas added: subschema #1, subschema #2
                - Type changed from 'string' to ''
                - Description changed from '' to 'An IPv4 or IPv6 address.'
            - Modified property: gateway_ip
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''
            - Modified property: host_routes
              - Items changed
                - Properties changed
                  - Modified property: nexthop
                    - Property 'OneOf' changed
                      - Schemas added: subschema #1, subschema #2
                    - Type changed from 'string' to ''
                    - Description changed from '' to 'An IPv4 or IPv6 address.'

GET /api/openstack-ports/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: fixed_ips
                - Items changed
                  - Properties changed
                    - Modified property: ip_address
                      - Property 'OneOf' changed
                        - Schemas added: subschema #1, subschema #2
                      - Type changed from 'string' to ''

POST /api/openstack-ports/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: fixed_ips
            - Items changed
              - Properties changed
                - Modified property: ip_address
                  - Property 'OneOf' changed
                    - Schemas added: subschema #1, subschema #2
                  - Type changed from 'string' to ''
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: fixed_ips
              - Items changed
                - Properties changed
                  - Modified property: ip_address
                    - Property 'OneOf' changed
                      - Schemas added: subschema #1, subschema #2
                    - Type changed from 'string' to ''

GET /api/openstack-ports/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: fixed_ips
              - Items changed
                - Properties changed
                  - Modified property: ip_address
                    - Property 'OneOf' changed
                      - Schemas added: subschema #1, subschema #2
                    - Type changed from 'string' to ''

PATCH /api/openstack-ports/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: fixed_ips
              - Items changed
                - Properties changed
                  - Modified property: ip_address
                    - Property 'OneOf' changed
                      - Schemas added: subschema #1, subschema #2
                    - Type changed from 'string' to ''

PUT /api/openstack-ports/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: fixed_ips
            - Items changed
              - Properties changed
                - Modified property: ip_address
                  - Property 'OneOf' changed
                    - Schemas added: subschema #1, subschema #2
                  - Type changed from 'string' to ''
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: fixed_ips
              - Items changed
                - Properties changed
                  - Modified property: ip_address
                    - Property 'OneOf' changed
                      - Schemas added: subschema #1, subschema #2
                    - Type changed from 'string' to ''

POST /api/openstack-ports/{uuid}/update_port_ip/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: ip_address
            - Property 'OneOf' changed
              - Schemas added: subschema #1, subschema #2
            - Type changed from 'string' to ''

GET /api/openstack-routers/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: fixed_ips
                - Items changed
                  - Properties changed
                    - Modified property: ip_address
                      - Property 'OneOf' changed
                        - Schemas added: subschema #1, subschema #2
                      - Type changed from 'string' to ''
              - Modified property: ports
                - Items changed
                  - Properties changed
                    - Modified property: fixed_ips
                      - Items changed
                        - Properties changed
                          - Modified property: ip_address
                            - Property 'OneOf' changed
                              - Schemas added: subschema #1, subschema #2
                            - Type changed from 'string' to ''
              - Modified property: routes
                - Items changed
                  - Properties changed
                    - Modified property: nexthop
                      - Property 'OneOf' changed
                        - Schemas added: subschema #1, subschema #2
                      - Type changed from 'string' to ''
                      - Description changed from '' to 'An IPv4 or IPv6 address.'

GET /api/openstack-routers/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: fixed_ips
              - Items changed
                - Properties changed
                  - Modified property: ip_address
                    - Property 'OneOf' changed
                      - Schemas added: subschema #1, subschema #2
                    - Type changed from 'string' to ''
            - Modified property: ports
              - Items changed
                - Properties changed
                  - Modified property: fixed_ips
                    - Items changed
                      - Properties changed
                        - Modified property: ip_address
                          - Property 'OneOf' changed
                            - Schemas added: subschema #1, subschema #2
                          - Type changed from 'string' to ''
            - Modified property: routes
              - Items changed
                - Properties changed
                  - Modified property: nexthop
                    - Property 'OneOf' changed
                      - Schemas added: subschema #1, subschema #2
                    - Type changed from 'string' to ''
                    - Description changed from '' to 'An IPv4 or IPv6 address.'

POST /api/openstack-routers/{uuid}/set_routes/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: routes
            - Items changed
              - Properties changed
                - Modified property: nexthop
                  - Property 'OneOf' changed
                    - Schemas added: subschema #1, subschema #2
                  - Type changed from 'string' to ''
                  - Description changed from '' to 'An IPv4 or IPv6 address.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: routes
              - Items changed
                - Properties changed
                  - Modified property: nexthop
                    - Property 'OneOf' changed
                      - Schemas added: subschema #1, subschema #2
                    - Type changed from 'string' to ''
                    - Description changed from '' to 'An IPv4 or IPv6 address.'

GET /api/openstack-subnets/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: allocation_pools
                - Items changed
                  - Properties changed
                    - Modified property: end
                      - Property 'OneOf' changed
                        - Schemas added: subschema #1, subschema #2
                      - Type changed from 'string' to ''
                      - Description changed from '' to 'An IPv4 or IPv6 address.'
                    - Modified property: start
                      - Property 'OneOf' changed
                        - Schemas added: subschema #1, subschema #2
                      - Type changed from 'string' to ''
                      - Description changed from '' to 'An IPv4 or IPv6 address.'
              - Modified property: dns_nameservers
                - Items changed
                  - Property 'OneOf' changed
                    - Schemas added: subschema #1, subschema #2
                  - Type changed from 'string' to ''
                  - Description changed from '' to 'An IPv4 or IPv6 address.'
              - Modified property: gateway_ip
                - Property 'OneOf' changed
                  - Schemas added: subschema #1, subschema #2
                - Type changed from 'string' to ''
              - Modified property: host_routes
                - Items changed
                  - Properties changed
                    - Modified property: nexthop
                      - Property 'OneOf' changed
                        - Schemas added: subschema #1, subschema #2
                      - Type changed from 'string' to ''
                      - Description changed from '' to 'An IPv4 or IPv6 address.'

GET /api/openstack-subnets/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: allocation_pools
              - Items changed
                - Properties changed
                  - Modified property: end
                    - Property 'OneOf' changed
                      - Schemas added: subschema #1, subschema #2
                    - Type changed from 'string' to ''
                    - Description changed from '' to 'An IPv4 or IPv6 address.'
                  - Modified property: start
                    - Property 'OneOf' changed
                      - Schemas added: subschema #1, subschema #2
                    - Type changed from 'string' to ''
                    - Description changed from '' to 'An IPv4 or IPv6 address.'
            - Modified property: dns_nameservers
              - Items changed
                - Property 'OneOf' changed
                  - Schemas added: subschema #1, subschema #2
                - Type changed from 'string' to ''
                - Description changed from '' to 'An IPv4 or IPv6 address.'
            - Modified property: gateway_ip
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''
            - Modified property: host_routes
              - Items changed
                - Properties changed
                  - Modified property: nexthop
                    - Property 'OneOf' changed
                      - Schemas added: subschema #1, subschema #2
                    - Type changed from 'string' to ''
                    - Description changed from '' to 'An IPv4 or IPv6 address.'

PATCH /api/openstack-subnets/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: allocation_pools
            - Items changed
              - Properties changed
                - Modified property: end
                  - Property 'OneOf' changed
                    - Schemas added: subschema #1, subschema #2
                  - Type changed from 'string' to ''
                  - Description changed from '' to 'An IPv4 or IPv6 address.'
                - Modified property: start
                  - Property 'OneOf' changed
                    - Schemas added: subschema #1, subschema #2
                  - Type changed from 'string' to ''
                  - Description changed from '' to 'An IPv4 or IPv6 address.'
          - Modified property: dns_nameservers
            - Items changed
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''
              - Description changed from '' to 'An IPv4 or IPv6 address.'
          - Modified property: gateway_ip
            - Property 'OneOf' changed
              - Schemas added: subschema #1, subschema #2
            - Type changed from 'string' to ''
          - Modified property: host_routes
            - Items changed
              - Properties changed
                - Modified property: nexthop
                  - Property 'OneOf' changed
                    - Schemas added: subschema #1, subschema #2
                  - Type changed from 'string' to ''
                  - Description changed from '' to 'An IPv4 or IPv6 address.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: allocation_pools
              - Items changed
                - Properties changed
                  - Modified property: end
                    - Property 'OneOf' changed
                      - Schemas added: subschema #1, subschema #2
                    - Type changed from 'string' to ''
                    - Description changed from '' to 'An IPv4 or IPv6 address.'
                  - Modified property: start
                    - Property 'OneOf' changed
                      - Schemas added: subschema #1, subschema #2
                    - Type changed from 'string' to ''
                    - Description changed from '' to 'An IPv4 or IPv6 address.'
            - Modified property: dns_nameservers
              - Items changed
                - Property 'OneOf' changed
                  - Schemas added: subschema #1, subschema #2
                - Type changed from 'string' to ''
                - Description changed from '' to 'An IPv4 or IPv6 address.'
            - Modified property: gateway_ip
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''
            - Modified property: host_routes
              - Items changed
                - Properties changed
                  - Modified property: nexthop
                    - Property 'OneOf' changed
                      - Schemas added: subschema #1, subschema #2
                    - Type changed from 'string' to ''
                    - Description changed from '' to 'An IPv4 or IPv6 address.'

PUT /api/openstack-subnets/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: allocation_pools
            - Items changed
              - Properties changed
                - Modified property: end
                  - Property 'OneOf' changed
                    - Schemas added: subschema #1, subschema #2
                  - Type changed from 'string' to ''
                  - Description changed from '' to 'An IPv4 or IPv6 address.'
                - Modified property: start
                  - Property 'OneOf' changed
                    - Schemas added: subschema #1, subschema #2
                  - Type changed from 'string' to ''
                  - Description changed from '' to 'An IPv4 or IPv6 address.'
          - Modified property: dns_nameservers
            - Items changed
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''
              - Description changed from '' to 'An IPv4 or IPv6 address.'
          - Modified property: gateway_ip
            - Property 'OneOf' changed
              - Schemas added: subschema #1, subschema #2
            - Type changed from 'string' to ''
          - Modified property: host_routes
            - Items changed
              - Properties changed
                - Modified property: nexthop
                  - Property 'OneOf' changed
                    - Schemas added: subschema #1, subschema #2
                  - Type changed from 'string' to ''
                  - Description changed from '' to 'An IPv4 or IPv6 address.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: allocation_pools
              - Items changed
                - Properties changed
                  - Modified property: end
                    - Property 'OneOf' changed
                      - Schemas added: subschema #1, subschema #2
                    - Type changed from 'string' to ''
                    - Description changed from '' to 'An IPv4 or IPv6 address.'
                  - Modified property: start
                    - Property 'OneOf' changed
                      - Schemas added: subschema #1, subschema #2
                    - Type changed from 'string' to ''
                    - Description changed from '' to 'An IPv4 or IPv6 address.'
            - Modified property: dns_nameservers
              - Items changed
                - Property 'OneOf' changed
                  - Schemas added: subschema #1, subschema #2
                - Type changed from 'string' to ''
                - Description changed from '' to 'An IPv4 or IPv6 address.'
            - Modified property: gateway_ip
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''
            - Modified property: host_routes
              - Items changed
                - Properties changed
                  - Modified property: nexthop
                    - Property 'OneOf' changed
                      - Schemas added: subschema #1, subschema #2
                    - Type changed from 'string' to ''
                    - Description changed from '' to 'An IPv4 or IPv6 address.'

POST /api/openstack-tenants/{uuid}/create_floating_ip/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: address
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''
            - Modified property: external_address
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''
            - Modified property: port_fixed_ips
              - Items changed
                - Properties changed
                  - Modified property: ip_address
                    - Property 'OneOf' changed
                      - Schemas added: subschema #1, subschema #2
                    - Type changed from 'string' to ''

POST /api/openstack-tenants/{uuid}/create_network/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: subnets
              - Items changed
                - Properties changed
                  - Modified property: allocation_pools
                    - Items changed
                      - Properties changed
                        - Modified property: end
                          - Property 'OneOf' changed
                            - Schemas added: subschema #1, subschema #2
                          - Type changed from 'string' to ''
                          - Description changed from '' to 'An IPv4 or IPv6 address.'
                        - Modified property: start
                          - Property 'OneOf' changed
                            - Schemas added: subschema #1, subschema #2
                          - Type changed from 'string' to ''
                          - Description changed from '' to 'An IPv4 or IPv6 address.'
                  - Modified property: gateway_ip
                    - Property 'OneOf' changed
                      - Schemas added: subschema #1, subschema #2
                    - Type changed from 'string' to ''

GET /api/override-settings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: ENFORCE_USER_CONSENT_FOR_OFFERINGS

POST /api/override-settings/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: ENFORCE_USER_CONSENT_FOR_OFFERINGS

GET /api/projects/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [kind]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: kind

POST /api/projects/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: kind
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: kind

GET /api/projects/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [kind]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: kind

PATCH /api/projects/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: kind
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: kind

PUT /api/projects/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: kind
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: kind

POST /api/projects/{uuid}/move_project/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: kind

GET /api/projects/{uuid}/other_users/

- New query param: agreement_date
- New query param: date_joined
- New query param: modified
- New query param: o
- Modified path param: uuid
  - Name changed from 'uuid' to 'project_uuid'
  - Description changed from '' to 'UUID of the project'
- Modified query param: full_name
  - Description changed from '' to 'Full name'
- Modified query param: is_active
  - Schema changed
    - Type changed from 'string' to 'boolean'
- Modified query param: user_keyword
  - Description changed from '' to 'User keyword'

GET /api/proposal-proposals/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: call_managing_organisation_uuid
            - Properties changed
              - New property: call_managing_organisation_uuid

POST /api/proposal-proposals/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: call_managing_organisation_uuid
          - Properties changed
            - New property: call_managing_organisation_uuid

GET /api/proposal-proposals/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: call_managing_organisation_uuid
          - Properties changed
            - New property: call_managing_organisation_uuid

POST /api/proposal-proposals/{uuid}/approve/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/scopes/- with value: 'round.call.manager'

POST /api/proposal-proposals/{uuid}/reject/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/scopes/- with value: 'round.call.manager'

GET /api/proposal-reviews/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: call_managing_organisation_uuid
            - Properties changed
              - New property: call_managing_organisation_uuid

POST /api/proposal-reviews/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: call_managing_organisation_uuid
          - Properties changed
            - New property: call_managing_organisation_uuid

GET /api/proposal-reviews/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: call_managing_organisation_uuid
          - Properties changed
            - New property: call_managing_organisation_uuid

PATCH /api/proposal-reviews/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: call_managing_organisation_uuid
          - Properties changed
            - New property: call_managing_organisation_uuid

PUT /api/proposal-reviews/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: call_managing_organisation_uuid
          - Properties changed
            - New property: call_managing_organisation_uuid

GET /api/rabbitmq-user-stats/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: connections
                - Items changed
                  - Properties changed
                    - Modified property: source_ip
                      - Property 'OneOf' changed
                        - Schemas added: subschema #1, subschema #2
                      - Type changed from 'string' to ''
                      - Description changed from '' to 'An IPv4 or IPv6 address.'

GET /api/rabbitmq-vhost-stats/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: subscriptions
                - Items changed
                  - Properties changed
                    - Modified property: source_ip
                      - Property 'OneOf' changed
                        - Schemas added: subschema #1, subschema #2
                      - Type changed from 'string' to ''
                      - Description changed from '' to 'An IPv4 or IPv6 address.'

GET /api/rancher-clusters/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: public_ips
                - Items changed
                  - Properties changed
                    - Modified property: external_ip_address
                      - Property 'OneOf' changed
                        - Schemas added: subschema #1, subschema #2
                      - Type changed from 'string' to ''
                      - Description changed from '' to 'An IPv4 or IPv6 address.'
                    - Modified property: ip_address
                      - Property 'OneOf' changed
                        - Schemas added: subschema #1, subschema #2
                      - Type changed from 'string' to ''
                      - Description changed from '' to 'An IPv4 or IPv6 address.'

POST /api/rancher-clusters/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: public_ips
              - Items changed
                - Properties changed
                  - Modified property: external_ip_address
                    - Property 'OneOf' changed
                      - Schemas added: subschema #1, subschema #2
                    - Type changed from 'string' to ''
                    - Description changed from '' to 'An IPv4 or IPv6 address.'
                  - Modified property: ip_address
                    - Property 'OneOf' changed
                      - Schemas added: subschema #1, subschema #2
                    - Type changed from 'string' to ''
                    - Description changed from '' to 'An IPv4 or IPv6 address.'

GET /api/rancher-clusters/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: public_ips
              - Items changed
                - Properties changed
                  - Modified property: external_ip_address
                    - Property 'OneOf' changed
                      - Schemas added: subschema #1, subschema #2
                    - Type changed from 'string' to ''
                    - Description changed from '' to 'An IPv4 or IPv6 address.'
                  - Modified property: ip_address
                    - Property 'OneOf' changed
                      - Schemas added: subschema #1, subschema #2
                    - Type changed from 'string' to ''
                    - Description changed from '' to 'An IPv4 or IPv6 address.'

PATCH /api/rancher-clusters/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: public_ips
              - Items changed
                - Properties changed
                  - Modified property: external_ip_address
                    - Property 'OneOf' changed
                      - Schemas added: subschema #1, subschema #2
                    - Type changed from 'string' to ''
                    - Description changed from '' to 'An IPv4 or IPv6 address.'
                  - Modified property: ip_address
                    - Property 'OneOf' changed
                      - Schemas added: subschema #1, subschema #2
                    - Type changed from 'string' to ''
                    - Description changed from '' to 'An IPv4 or IPv6 address.'

PUT /api/rancher-clusters/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: public_ips
              - Items changed
                - Properties changed
                  - Modified property: external_ip_address
                    - Property 'OneOf' changed
                      - Schemas added: subschema #1, subschema #2
                    - Type changed from 'string' to ''
                    - Description changed from '' to 'An IPv4 or IPv6 address.'
                  - Modified property: ip_address
                    - Property 'OneOf' changed
                      - Schemas added: subschema #1, subschema #2
                    - Type changed from 'string' to ''
                    - Description changed from '' to 'An IPv4 or IPv6 address.'

POST /api/rancher-clusters/{uuid}/create_management_security_group/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: public_ips
              - Items changed
                - Properties changed
                  - Modified property: external_ip_address
                    - Property 'OneOf' changed
                      - Schemas added: subschema #1, subschema #2
                    - Type changed from 'string' to ''
                    - Description changed from '' to 'An IPv4 or IPv6 address.'
                  - Modified property: ip_address
                    - Property 'OneOf' changed
                      - Schemas added: subschema #1, subschema #2
                    - Type changed from 'string' to ''
                    - Description changed from '' to 'An IPv4 or IPv6 address.'

GET /api/rancher-services/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: cluster_ip
                - Property 'OneOf' changed
                  - Schemas added: subschema #1, subschema #2
                - Type changed from 'string' to ''
                - Description changed from '' to 'An IPv4 or IPv6 address.'

POST /api/rancher-services/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: cluster_ip
            - Property 'OneOf' changed
              - Schemas added: subschema #1, subschema #2
            - Type changed from 'string' to ''
            - Description changed from '' to 'An IPv4 or IPv6 address.'
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: cluster_ip
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''
              - Description changed from '' to 'An IPv4 or IPv6 address.'

GET /api/rancher-services/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: cluster_ip
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''
              - Description changed from '' to 'An IPv4 or IPv6 address.'

PATCH /api/rancher-services/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: cluster_ip
            - Property 'OneOf' changed
              - Schemas added: subschema #1, subschema #2
            - Type changed from 'string' to ''
            - Description changed from '' to 'An IPv4 or IPv6 address.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: cluster_ip
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''
              - Description changed from '' to 'An IPv4 or IPv6 address.'

PUT /api/rancher-services/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: cluster_ip
            - Property 'OneOf' changed
              - Schemas added: subschema #1, subschema #2
            - Type changed from 'string' to ''
            - Description changed from '' to 'An IPv4 or IPv6 address.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: cluster_ip
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''
              - Description changed from '' to 'An IPv4 or IPv6 address.'

GET /api/rancher-services/{uuid}/yaml/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: cluster_ip
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''
              - Description changed from '' to 'An IPv4 or IPv6 address.'

PUT /api/rancher-services/{uuid}/yaml/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: cluster_ip
            - Property 'OneOf' changed
              - Schemas added: subschema #1, subschema #2
            - Type changed from 'string' to ''
            - Description changed from '' to 'An IPv4 or IPv6 address.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: cluster_ip
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''
              - Description changed from '' to 'An IPv4 or IPv6 address.'

GET /api/user-group-invitations/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: scope_description
            - Properties changed
              - New property: scope_description

POST /api/user-group-invitations/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: scope_description
          - Properties changed
            - New property: scope_description

GET /api/user-group-invitations/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: scope_description
          - Properties changed
            - New property: scope_description

POST /api/user-group-invitations/{uuid}/submit_request/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: created
            - Deleted required property: created_by_full_name
            - Deleted required property: created_by_username
            - Deleted required property: customer_name
            - Deleted required property: customer_uuid
            - Deleted required property: expires
            - Deleted required property: is_active
            - Deleted required property: role
            - Deleted required property: role_description
            - Deleted required property: role_name
            - Deleted required property: scope_image
            - Deleted required property: scope_type
            - Deleted required property: url
          - Properties changed
            - Deleted property: auto_create_project
            - Deleted property: created
            - Deleted property: created_by_full_name
            - Deleted property: created_by_username
            - Deleted property: customer_name
            - Deleted property: customer_uuid
            - Deleted property: expires
            - Deleted property: is_active
            - Deleted property: is_public
            - Deleted property: project_name_template
            - Deleted property: project_role
            - Deleted property: role
            - Deleted property: role_description
            - Deleted property: role_name
            - Deleted property: scope_image
            - Deleted property: scope_type
            - Deleted property: url
            - Deleted property: user_affiliations
            - Deleted property: user_email_patterns
            - Modified property: scope_name
              - Description changed from '' to 'Name of the invitation scope'
              - ReadOnly changed from true to false
            - Modified property: scope_uuid
              - Format changed from 'uuid' to ''
              - Description changed from '' to 'UUID of the invitation scope'
              - ReadOnly changed from true to false
            - Modified property: uuid
              - Format changed from 'uuid' to ''
              - Description changed from '' to 'UUID of the created permission request'
              - ReadOnly changed from true to false

GET /api/user-invitations/

- New query param: scope_description
- New query param: scope_name
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: scope_description
            - Properties changed
              - New property: scope_description

HEAD /api/user-invitations/

- New query param: scope_description
- New query param: scope_name

POST /api/user-invitations/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: scope_description
          - Properties changed
            - New property: scope_description

GET /api/user-invitations/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: scope_description
          - Properties changed
            - New property: scope_description

GET /api/user-invitations/{uuid}/details/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: scope_description
          - Properties changed
            - New property: scope_description

GET /api/user-permission-requests/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: created_by_email
              - New required property: project_name_template
            - Properties changed
              - New property: created_by_email
              - New property: project_name_template

GET /api/user-permission-requests/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: created_by_email
            - New required property: project_name_template
          - Properties changed
            - New property: created_by_email
            - New property: project_name_template

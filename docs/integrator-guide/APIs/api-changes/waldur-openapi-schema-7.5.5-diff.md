# OpenAPI schema diff - 7.5.5

## For version 7.5.5

### New Endpoints: 7

--------------------
POST /api/openstack-routers/{uuid}/add_router_interface/  
POST /api/openstack-routers/{uuid}/remove_router_interface/  
GET /api/projects/{uuid}/other_users/  
GET /api/rancher-cluster-security-groups/  
GET /api/rancher-cluster-security-groups/{uuid}/  
PATCH /api/rancher-cluster-security-groups/{uuid}/  
PUT /api/rancher-cluster-security-groups/{uuid}/  

### Deleted Endpoints: None

---------------------------

### Modified Endpoints: 40

--------------------------
GET /api/booking-resources/

- New query param: has_terminate_date

PATCH /api/invoice-items/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: unit_price
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: unit_price

PUT /api/invoice-items/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: unit_price
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: unit_price

GET /api/marketplace-component-user-usages/

- New query param: billing_period_month
- New query param: billing_period_year
- New query param: o
- New query param: username

GET /api/marketplace-customer-service-accounts/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: customer_name
              - New required property: customer_uuid
            - Properties changed
              - New property: customer_name
              - New property: customer_uuid

POST /api/marketplace-customer-service-accounts/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: customer_name
            - New required property: customer_uuid
          - Properties changed
            - New property: customer_name
            - New property: customer_uuid

GET /api/marketplace-customer-service-accounts/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: customer_name
            - New required property: customer_uuid
          - Properties changed
            - New property: customer_name
            - New property: customer_uuid

PATCH /api/marketplace-customer-service-accounts/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: customer_name
            - New required property: customer_uuid
          - Properties changed
            - New property: customer_name
            - New property: customer_uuid

PUT /api/marketplace-customer-service-accounts/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: customer_name
            - New required property: customer_uuid
          - Properties changed
            - New property: customer_name
            - New property: customer_uuid

POST /api/marketplace-customer-service-accounts/{uuid}/rotate_api_key/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: customer_name
            - New required property: customer_uuid
          - Properties changed
            - New property: customer_name
            - New property: customer_uuid

GET /api/marketplace-project-service-accounts/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: customer_abbreviation
              - New required property: customer_name
              - New required property: customer_uuid
              - New required property: project_name
              - New required property: project_uuid
            - Properties changed
              - New property: customer_abbreviation
              - New property: customer_name
              - New property: customer_uuid
              - New property: project_name
              - New property: project_uuid

POST /api/marketplace-project-service-accounts/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: customer_abbreviation
            - New required property: customer_name
            - New required property: customer_uuid
            - New required property: project_name
            - New required property: project_uuid
          - Properties changed
            - New property: customer_abbreviation
            - New property: customer_name
            - New property: customer_uuid
            - New property: project_name
            - New property: project_uuid

GET /api/marketplace-project-service-accounts/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: customer_abbreviation
            - New required property: customer_name
            - New required property: customer_uuid
            - New required property: project_name
            - New required property: project_uuid
          - Properties changed
            - New property: customer_abbreviation
            - New property: customer_name
            - New property: customer_uuid
            - New property: project_name
            - New property: project_uuid

PATCH /api/marketplace-project-service-accounts/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: customer_abbreviation
            - New required property: customer_name
            - New required property: customer_uuid
            - New required property: project_name
            - New required property: project_uuid
          - Properties changed
            - New property: customer_abbreviation
            - New property: customer_name
            - New property: customer_uuid
            - New property: project_name
            - New property: project_uuid

PUT /api/marketplace-project-service-accounts/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: customer_abbreviation
            - New required property: customer_name
            - New required property: customer_uuid
            - New required property: project_name
            - New required property: project_uuid
          - Properties changed
            - New property: customer_abbreviation
            - New property: customer_name
            - New property: customer_uuid
            - New property: project_name
            - New property: project_uuid

POST /api/marketplace-project-service-accounts/{uuid}/rotate_api_key/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: customer_abbreviation
            - New required property: customer_name
            - New required property: customer_uuid
            - New required property: project_name
            - New required property: project_uuid
          - Properties changed
            - New property: customer_abbreviation
            - New property: customer_name
            - New property: customer_uuid
            - New property: project_name
            - New property: project_uuid

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
                      - New property: k8s_version
                      - New property: private_registry_password
                      - New property: private_registry_url
                      - New property: private_registry_user

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
                    - New property: k8s_version
                    - New property: private_registry_password
                    - New property: private_registry_url
                    - New property: private_registry_user

GET /api/marketplace-provider-offerings/groups/

- OperationID changed from 'marketplace_provider_offerings_groups_retrieve' to 'marketplace_provider_offerings_groups_list'
- New query param: accessible_via_calls
- New query param: allowed_customer_uuid
- New query param: attributes
- New query param: billable
- New query param: category_group_uuid
- New query param: category_uuid
- New query param: created
- New query param: customer
- New query param: customer_uuid
- New query param: description
- New query param: keyword
- New query param: modified
- New query param: name
- New query param: name_exact
- New query param: o
- New query param: organization_group_uuid
- New query param: page
- New query param: page_size
- New query param: parent_uuid
- New query param: project_uuid
- New query param: resource_customer_uuid
- New query param: resource_project_uuid
- New query param: scope_uuid
- New query param: service_manager_uuid
- New query param: shared
- New query param: state
- New query param: type
- Deleted query param: field
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Type changed from 'object' to 'array'
          - Items changed
            - Schema added
          - Properties changed
            - Deleted property: access_url
            - Deleted property: attributes
            - Deleted property: backend_id
            - Deleted property: backend_metadata
            - Deleted property: billable
            - Deleted property: category
            - Deleted property: category_title
            - Deleted property: category_uuid
            - Deleted property: citation_count
            - Deleted property: components
            - Deleted property: country
            - Deleted property: created
            - Deleted property: customer
            - Deleted property: customer_name
            - Deleted property: customer_uuid
            - Deleted property: datacite_doi
            - Deleted property: description
            - Deleted property: endpoints
            - Deleted property: files
            - Deleted property: full_description
            - Deleted property: getting_started
            - Deleted property: google_calendar_is_public
            - Deleted property: google_calendar_link
            - Deleted property: image
            - Deleted property: integration_guide
            - Deleted property: integration_status
            - Deleted property: latitude
            - Deleted property: longitude
            - Deleted property: name
            - Deleted property: options
            - Deleted property: order_count
            - Deleted property: organization_groups
            - Deleted property: parent_description
            - Deleted property: parent_name
            - Deleted property: parent_uuid
            - Deleted property: paused_reason
            - Deleted property: plans
            - Deleted property: plugin_options
            - Deleted property: privacy_policy_link
            - Deleted property: project
            - Deleted property: project_name
            - Deleted property: project_uuid
            - Deleted property: quotas
            - Deleted property: resource_options
            - Deleted property: roles
            - Deleted property: scope
            - Deleted property: scope_error_message
            - Deleted property: scope_name
            - Deleted property: scope_state
            - Deleted property: scope_uuid
            - Deleted property: screenshots
            - Deleted property: secret_options
            - Deleted property: service_attributes
            - Deleted property: shared
            - Deleted property: slug
            - Deleted property: state
            - Deleted property: terms_of_service
            - Deleted property: terms_of_service_link
            - Deleted property: thumbnail
            - Deleted property: total_cost
            - Deleted property: total_cost_estimated
            - Deleted property: total_customers
            - Deleted property: type
            - Deleted property: url
            - Deleted property: uuid
            - Deleted property: vendor_details

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
                    - New property: k8s_version
                    - New property: private_registry_password
                    - New property: private_registry_url
                    - New property: private_registry_user

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
                    - New property: k8s_version
                    - New property: private_registry_password
                    - New property: private_registry_url
                    - New property: private_registry_user

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
                    - New property: k8s_version
                    - New property: private_registry_password
                    - New property: private_registry_url
                    - New property: private_registry_user

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
                    - New property: k8s_version
                    - New property: private_registry_password
                    - New property: private_registry_url
                    - New property: private_registry_user

POST /api/marketplace-provider-offerings/{uuid}/update_integration/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: secret_options
            - Properties changed
              - New property: k8s_version
              - New property: private_registry_password
              - New property: private_registry_url
              - New property: private_registry_user

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
                    - New property: k8s_version
                    - New property: private_registry_password
                    - New property: private_registry_url
                    - New property: private_registry_user

GET /api/marketplace-provider-resources/

- New query param: has_terminate_date

GET /api/marketplace-resources/

- New query param: has_terminate_date

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
                      - New property: k8s_version
                      - New property: private_registry_password
                      - New property: private_registry_url
                      - New property: private_registry_user

POST /api/openstack-backups/{uuid}/restore/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: ports
            - Items changed
              - Properties changed
                - New property: port

POST /api/openstack-instances/{uuid}/update_ports/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: ports
            - Items changed
              - Properties changed
                - New property: port

GET /api/openstack-ports/

- New query param: admin_state_up
- New query param: backend_id
- New query param: device_id
- New query param: device_owner
- New query param: has_device_owner
- New query param: mac_address
- New query param: status
- Modified query param: query
  - Description changed from '' to 'Query'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: admin_state_up
                - Type changed from 'string' to 'boolean'

POST /api/openstack-ports/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: admin_state_up
              - Type changed from 'string' to 'boolean'

GET /api/openstack-ports/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: admin_state_up
              - Type changed from 'string' to 'boolean'

PATCH /api/openstack-ports/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: admin_state_up
              - Type changed from 'string' to 'boolean'

PUT /api/openstack-ports/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: admin_state_up
              - Type changed from 'string' to 'boolean'

POST /api/rancher-clusters/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: nodes
            - Items changed
              - Properties changed
                - Modified property: data_volumes
                  - Items changed
                    - Required changed
                      - New required property: mount_point
                    - Properties changed
                      - Modified property: mount_point
                        - Deleted enum values: [/var/lib/docker /var/lib/etcd /opt/media01 /opt/rke2_storage]
                        - MinLength changed from 0 to 1

PUT /api/rancher-clusters/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: nodes
            - Items changed
              - Properties changed
                - Modified property: data_volumes
                  - Items changed
                    - Required changed
                      - New required property: mount_point
                    - Properties changed
                      - Modified property: mount_point
                        - Deleted enum values: [/var/lib/docker /var/lib/etcd /opt/media01 /opt/rke2_storage]
                        - MinLength changed from 0 to 1

POST /api/rancher-clusters/{uuid}/create_management_security_group/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: nodes
            - Items changed
              - Properties changed
                - Modified property: data_volumes
                  - Items changed
                    - Required changed
                      - New required property: mount_point
                    - Properties changed
                      - Modified property: mount_point
                        - Deleted enum values: [/var/lib/docker /var/lib/etcd /opt/media01 /opt/rke2_storage]
                        - MinLength changed from 0 to 1

POST /api/rancher-nodes/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: data_volumes
            - Items changed
              - Required changed
                - New required property: mount_point
              - Properties changed
                - Modified property: mount_point
                  - Deleted enum values: [/var/lib/docker /var/lib/etcd /opt/media01 /opt/rke2_storage]
                  - MinLength changed from 0 to 1

GET /api/rancher-role-templates/

- New query param: o

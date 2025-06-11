# OpenAPI schema diff - 7.5.1

## For version 7.5.1

### New Endpoints: 21

---------------------
GET /api/marketplace-customer-service-accounts/  
POST /api/marketplace-customer-service-accounts/  
DELETE /api/marketplace-customer-service-accounts/{uuid}/  
GET /api/marketplace-customer-service-accounts/{uuid}/  
PATCH /api/marketplace-customer-service-accounts/{uuid}/  
PUT /api/marketplace-customer-service-accounts/{uuid}/  
POST /api/marketplace-customer-service-accounts/{uuid}/rotate_api_key/  
GET /api/marketplace-project-service-accounts/  
POST /api/marketplace-project-service-accounts/  
DELETE /api/marketplace-project-service-accounts/{uuid}/  
GET /api/marketplace-project-service-accounts/{uuid}/  
PATCH /api/marketplace-project-service-accounts/{uuid}/  
PUT /api/marketplace-project-service-accounts/{uuid}/  
POST /api/marketplace-project-service-accounts/{uuid}/rotate_api_key/  
POST /api/openstack-ports/  
PATCH /api/openstack-ports/{uuid}/  
PUT /api/openstack-ports/{uuid}/  
POST /api/openstack-ports/{uuid}/disable_port/  
POST /api/openstack-ports/{uuid}/disable_port_security/  
POST /api/openstack-ports/{uuid}/enable_port/  
POST /api/openstack-ports/{uuid}/enable_port_security/  

### Deleted Endpoints: 2

------------------------
POST /api/openstack-networks/{uuid}/create_port/  
GET /api/rancher-clusters/{uuid}/kubeconfig_file/  

### Modified Endpoints: 43

--------------------------
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
                  - New enum values: [openstack_port_updated service_account_created service_account_deleted service_account_updated]

POST /api/hooks-email/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [openstack_port_updated service_account_created service_account_deleted service_account_updated]
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [openstack_port_updated service_account_created service_account_deleted service_account_updated]

GET /api/hooks-email/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [openstack_port_updated service_account_created service_account_deleted service_account_updated]

PATCH /api/hooks-email/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [openstack_port_updated service_account_created service_account_deleted service_account_updated]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [openstack_port_updated service_account_created service_account_deleted service_account_updated]

PUT /api/hooks-email/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [openstack_port_updated service_account_created service_account_deleted service_account_updated]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [openstack_port_updated service_account_created service_account_deleted service_account_updated]

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
                  - New enum values: [openstack_port_updated service_account_created service_account_deleted service_account_updated]

POST /api/hooks-web/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [openstack_port_updated service_account_created service_account_deleted service_account_updated]
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [openstack_port_updated service_account_created service_account_deleted service_account_updated]

GET /api/hooks-web/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [openstack_port_updated service_account_created service_account_deleted service_account_updated]

PATCH /api/hooks-web/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [openstack_port_updated service_account_created service_account_deleted service_account_updated]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [openstack_port_updated service_account_created service_account_deleted service_account_updated]

PUT /api/hooks-web/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [openstack_port_updated service_account_created service_account_deleted service_account_updated]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [openstack_port_updated service_account_created service_account_deleted service_account_updated]

GET /api/keycloak-user-group-memberships/

- New query param: state

GET /api/marketplace-provider-offerings/

- New query param: resource_customer_uuid
- New query param: resource_project_uuid
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
                      - New property: argocd_k8s_kubeconfig
                      - New property: argocd_k8s_namespace
                      - New property: keycloak_password
                      - New property: keycloak_realm
                      - New property: keycloak_ssl_verify
                      - New property: keycloak_sync_frequency
                      - New property: keycloak_url
                      - New property: keycloak_user_realm
                      - New property: keycloak_username
                      - New property: vault_host
                      - New property: vault_port
                      - New property: vault_tls_verify
                      - New property: vault_token

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
                    - New property: argocd_k8s_kubeconfig
                    - New property: argocd_k8s_namespace
                    - New property: keycloak_password
                    - New property: keycloak_realm
                    - New property: keycloak_ssl_verify
                    - New property: keycloak_sync_frequency
                    - New property: keycloak_url
                    - New property: keycloak_user_realm
                    - New property: keycloak_username
                    - New property: vault_host
                    - New property: vault_port
                    - New property: vault_tls_verify
                    - New property: vault_token

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
                    - New property: argocd_k8s_kubeconfig
                    - New property: argocd_k8s_namespace
                    - New property: keycloak_password
                    - New property: keycloak_realm
                    - New property: keycloak_ssl_verify
                    - New property: keycloak_sync_frequency
                    - New property: keycloak_url
                    - New property: keycloak_user_realm
                    - New property: keycloak_username
                    - New property: vault_host
                    - New property: vault_port
                    - New property: vault_tls_verify
                    - New property: vault_token

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
                    - New property: argocd_k8s_kubeconfig
                    - New property: argocd_k8s_namespace
                    - New property: keycloak_password
                    - New property: keycloak_realm
                    - New property: keycloak_ssl_verify
                    - New property: keycloak_sync_frequency
                    - New property: keycloak_url
                    - New property: keycloak_user_realm
                    - New property: keycloak_username
                    - New property: vault_host
                    - New property: vault_port
                    - New property: vault_tls_verify
                    - New property: vault_token

GET /api/marketplace-provider-offerings/{uuid}/component_stats/

- New query param: resource_customer_uuid
- New query param: resource_project_uuid

GET /api/marketplace-provider-offerings/{uuid}/costs/

- New query param: resource_customer_uuid
- New query param: resource_project_uuid

GET /api/marketplace-provider-offerings/{uuid}/customers/

- New query param: resource_customer_uuid
- New query param: resource_project_uuid

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
                    - New property: argocd_k8s_kubeconfig
                    - New property: argocd_k8s_namespace
                    - New property: keycloak_password
                    - New property: keycloak_realm
                    - New property: keycloak_ssl_verify
                    - New property: keycloak_sync_frequency
                    - New property: keycloak_url
                    - New property: keycloak_user_realm
                    - New property: keycloak_username
                    - New property: vault_host
                    - New property: vault_port
                    - New property: vault_tls_verify
                    - New property: vault_token

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
                    - New property: argocd_k8s_kubeconfig
                    - New property: argocd_k8s_namespace
                    - New property: keycloak_password
                    - New property: keycloak_realm
                    - New property: keycloak_ssl_verify
                    - New property: keycloak_sync_frequency
                    - New property: keycloak_url
                    - New property: keycloak_user_realm
                    - New property: keycloak_username
                    - New property: vault_host
                    - New property: vault_port
                    - New property: vault_tls_verify
                    - New property: vault_token

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
                    - New property: argocd_k8s_kubeconfig
                    - New property: argocd_k8s_namespace
                    - New property: keycloak_password
                    - New property: keycloak_realm
                    - New property: keycloak_ssl_verify
                    - New property: keycloak_sync_frequency
                    - New property: keycloak_url
                    - New property: keycloak_user_realm
                    - New property: keycloak_username
                    - New property: vault_host
                    - New property: vault_port
                    - New property: vault_tls_verify
                    - New property: vault_token

POST /api/marketplace-provider-offerings/{uuid}/update_integration/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: secret_options
            - Properties changed
              - New property: argocd_k8s_kubeconfig
              - New property: argocd_k8s_namespace
              - New property: keycloak_password
              - New property: keycloak_realm
              - New property: keycloak_ssl_verify
              - New property: keycloak_sync_frequency
              - New property: keycloak_url
              - New property: keycloak_user_realm
              - New property: keycloak_username
              - New property: vault_host
              - New property: vault_port
              - New property: vault_tls_verify
              - New property: vault_token

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
                    - New property: argocd_k8s_kubeconfig
                    - New property: argocd_k8s_namespace
                    - New property: keycloak_password
                    - New property: keycloak_realm
                    - New property: keycloak_ssl_verify
                    - New property: keycloak_sync_frequency
                    - New property: keycloak_url
                    - New property: keycloak_user_realm
                    - New property: keycloak_username
                    - New property: vault_host
                    - New property: vault_port
                    - New property: vault_tls_verify
                    - New property: vault_token

GET /api/marketplace-public-offerings/

- New query param: resource_customer_uuid
- New query param: resource_project_uuid

GET /api/marketplace-robot-accounts/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - Deleted required property: error_message
              - Deleted required property: error_traceback
            - Properties changed
              - New property: description
              - Modified property: state
                - Property 'AllOf' changed
                  - Schemas added: #/components/schemas/RobotAccountStates
                - Type changed from 'string' to ''
              - Modified property: type
                - Description changed from '' to 'Type of the robot account.'

POST /api/marketplace-robot-accounts/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: description
          - Modified property: type
            - Description changed from '' to 'Type of the robot account.'
          - Modified property: users
            - Description changed from '' to 'Users who have access to this robot account.'
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: error_message
            - Deleted required property: error_traceback
          - Properties changed
            - New property: description
            - Modified property: state
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/RobotAccountStates
              - Type changed from 'string' to ''
            - Modified property: type
              - Description changed from '' to 'Type of the robot account.'
            - Modified property: users
              - Description changed from '' to 'Users who have access to this robot account.'

GET /api/marketplace-robot-accounts/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: error_message
            - Deleted required property: error_traceback
          - Properties changed
            - New property: description
            - Modified property: state
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/RobotAccountStates
              - Type changed from 'string' to ''
            - Modified property: type
              - Description changed from '' to 'Type of the robot account.'

PATCH /api/marketplace-robot-accounts/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: description
          - New property: resource
          - Modified property: type
            - Description changed from '' to 'Type of the robot account.'
          - Modified property: users
            - Description changed from '' to 'Users who have access to this robot account.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: error_message
            - Deleted required property: error_traceback
          - Properties changed
            - New property: description
            - Modified property: state
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/RobotAccountStates
              - Type changed from 'string' to ''
            - Modified property: type
              - Description changed from '' to 'Type of the robot account.'
            - Modified property: users
              - Description changed from '' to 'Users who have access to this robot account.'

PUT /api/marketplace-robot-accounts/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: description
          - Modified property: type
            - Description changed from '' to 'Type of the robot account.'
          - Modified property: users
            - Description changed from '' to 'Users who have access to this robot account.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: error_message
            - Deleted required property: error_traceback
          - Properties changed
            - New property: description
            - Modified property: state
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/RobotAccountStates
              - Type changed from 'string' to ''
            - Modified property: type
              - Description changed from '' to 'Type of the robot account.'
            - Modified property: users
              - Description changed from '' to 'Users who have access to this robot account.'

POST /api/marketplace-robot-accounts/{uuid}/set_state_creating/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: error_message
            - Deleted required property: error_traceback
          - Properties changed
            - New property: description
            - Modified property: state
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/RobotAccountStates
              - Type changed from 'string' to ''
            - Modified property: type
              - Description changed from '' to 'Type of the robot account.'

POST /api/marketplace-robot-accounts/{uuid}/set_state_deleted/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: error_message
            - Deleted required property: error_traceback
          - Properties changed
            - New property: description
            - Modified property: state
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/RobotAccountStates
              - Type changed from 'string' to ''
            - Modified property: type
              - Description changed from '' to 'Type of the robot account.'

POST /api/marketplace-robot-accounts/{uuid}/set_state_erred/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: error_message
            - Deleted required property: error_traceback
          - Properties changed
            - New property: description
            - Modified property: state
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/RobotAccountStates
              - Type changed from 'string' to ''
            - Modified property: type
              - Description changed from '' to 'Type of the robot account.'

POST /api/marketplace-robot-accounts/{uuid}/set_state_ok/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: error_message
            - Deleted required property: error_traceback
          - Properties changed
            - New property: description
            - Modified property: state
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/RobotAccountStates
              - Type changed from 'string' to ''
            - Modified property: type
              - Description changed from '' to 'Type of the robot account.'

POST /api/marketplace-robot-accounts/{uuid}/set_state_request_deletion/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: error_message
            - Deleted required property: error_traceback
          - Properties changed
            - New property: description
            - Modified property: state
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/RobotAccountStates
              - Type changed from 'string' to ''
            - Modified property: type
              - Description changed from '' to 'Type of the robot account.'

GET /api/marketplace-service-providers/{service_provider_uuid}/offerings/

- New query param: resource_customer_uuid
- New query param: resource_project_uuid
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
                      - New property: argocd_k8s_kubeconfig
                      - New property: argocd_k8s_namespace
                      - New property: keycloak_password
                      - New property: keycloak_realm
                      - New property: keycloak_ssl_verify
                      - New property: keycloak_sync_frequency
                      - New property: keycloak_url
                      - New property: keycloak_user_realm
                      - New property: keycloak_username
                      - New property: vault_host
                      - New property: vault_port
                      - New property: vault_tls_verify
                      - New property: vault_token

GET /api/openstack-ports/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [admin_state_up]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: admin_state_up
              - Modified property: allowed_address_pairs
                - ReadOnly changed from true to false
              - Modified property: port_security_enabled
                - ReadOnly changed from true to false
              - Modified property: security_groups
                - ReadOnly changed from true to false

GET /api/openstack-ports/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [admin_state_up]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: admin_state_up
            - Modified property: allowed_address_pairs
              - ReadOnly changed from true to false
            - Modified property: port_security_enabled
              - ReadOnly changed from true to false
            - Modified property: security_groups
              - ReadOnly changed from true to false

GET /api/rancher-apps/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: external_url
                - Nullable changed from false to true

POST /api/rancher-apps/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: external_url
              - Nullable changed from false to true

GET /api/rancher-apps/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: external_url
              - Nullable changed from false to true

PATCH /api/rancher-apps/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: external_url
              - Nullable changed from false to true

PUT /api/rancher-apps/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: external_url
              - Nullable changed from false to true

GET /api/rancher-role-templates/

- New query param: name
- New query param: scope_type
- New query param: settings_uuid

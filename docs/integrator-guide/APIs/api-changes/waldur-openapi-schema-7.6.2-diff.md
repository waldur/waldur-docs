# OpenAPI schema diff - 7.6.2

## For version 7.6.2

### New Endpoints: 7

--------------------
POST /api/openstack-ports/{uuid}/update_security_groups/  
GET /api/proposal-protected-calls/{uuid}/resource_templates/  
POST /api/proposal-protected-calls/{uuid}/resource_templates/  
DELETE /api/proposal-protected-calls/{uuid}/resource_templates/{obj_uuid}/  
GET /api/proposal-protected-calls/{uuid}/resource_templates/{obj_uuid}/  
PATCH /api/proposal-protected-calls/{uuid}/resource_templates/{obj_uuid}/  
PUT /api/proposal-protected-calls/{uuid}/resource_templates/{obj_uuid}/  

### Deleted Endpoints: None

---------------------------

### Modified Endpoints: 51

--------------------------
GET /api/customers/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [max_service_accounts]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: max_service_accounts

POST /api/customers/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: max_service_accounts

GET /api/customers/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [max_service_accounts]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: max_service_accounts

PATCH /api/customers/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: max_service_accounts

PUT /api/customers/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: max_service_accounts

POST /api/marketplace-component-usages/set_usage/

- Responses changed
  - New response: 201
  - Deleted response: 200

POST /api/marketplace-component-usages/{uuid}/set_user_usage/

- Responses changed
  - New response: 201
  - Deleted response: 200

GET /api/marketplace-provider-offerings/{uuid}/list_customer_projects/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: max_service_accounts

GET /api/marketplace-service-providers/{service_provider_uuid}/projects/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [max_service_accounts]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: max_service_accounts

GET /api/openstack-backups/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: instance_ports
                - Items changed
                  - Properties changed
                    - New property: security_groups
              - Modified property: restorations
                - Items changed
                  - Properties changed
                    - Modified property: ports
                      - Items changed
                        - Properties changed
                          - New property: security_groups

GET /api/openstack-backups/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: instance_ports
              - Items changed
                - Properties changed
                  - New property: security_groups
            - Modified property: restorations
              - Items changed
                - Properties changed
                  - Modified property: ports
                    - Items changed
                      - Properties changed
                        - New property: security_groups

PATCH /api/openstack-backups/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: instance_ports
              - Items changed
                - Properties changed
                  - New property: security_groups
            - Modified property: restorations
              - Items changed
                - Properties changed
                  - Modified property: ports
                    - Items changed
                      - Properties changed
                        - New property: security_groups

PUT /api/openstack-backups/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: instance_ports
              - Items changed
                - Properties changed
                  - New property: security_groups
            - Modified property: restorations
              - Items changed
                - Properties changed
                  - Modified property: ports
                    - Items changed
                      - Properties changed
                        - New property: security_groups

POST /api/openstack-backups/{uuid}/restore/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: ports
              - Items changed
                - Properties changed
                  - New property: security_groups

GET /api/openstack-instances/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: ports
                - Items changed
                  - Properties changed
                    - New property: security_groups

GET /api/openstack-instances/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: ports
              - Items changed
                - Properties changed
                  - New property: security_groups

PATCH /api/openstack-instances/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: ports
              - Items changed
                - Properties changed
                  - New property: security_groups

PUT /api/openstack-instances/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: ports
              - Items changed
                - Properties changed
                  - New property: security_groups

POST /api/openstack-instances/{uuid}/backup/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: instance_ports
              - Items changed
                - Properties changed
                  - New property: security_groups
            - Modified property: restorations
              - Items changed
                - Properties changed
                  - Modified property: ports
                    - Items changed
                      - Properties changed
                        - New property: security_groups

GET /api/openstack-instances/{uuid}/ports/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: security_groups

GET /api/openstack-ports/

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
                    - New property: url

POST /api/openstack-ports/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: security_groups
              - Items changed
                - Properties changed
                  - New property: url

GET /api/openstack-ports/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: security_groups
              - Items changed
                - Properties changed
                  - New property: url

PATCH /api/openstack-ports/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: security_groups
              - Items changed
                - Properties changed
                  - New property: url

PUT /api/openstack-ports/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: security_groups
              - Items changed
                - Properties changed
                  - New property: url

GET /api/openstack-routers/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: ports
                - Items changed
                  - Properties changed
                    - New property: security_groups

GET /api/openstack-routers/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: ports
              - Items changed
                - Properties changed
                  - New property: security_groups

POST /api/openstack-tenants/{uuid}/create_security_group/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Required changed
          - Deleted required property: rules
        - Properties changed
          - Deleted property: rules

GET /api/override-settings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: ENABLE_MOCK_SERVICE_ACCOUNT_BACKEND

POST /api/override-settings/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: ENABLE_MOCK_SERVICE_ACCOUNT_BACKEND

GET /api/projects/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [max_service_accounts]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: max_service_accounts

POST /api/projects/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: max_service_accounts

GET /api/projects/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [max_service_accounts]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: max_service_accounts

PATCH /api/projects/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: max_service_accounts

PUT /api/projects/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: max_service_accounts

POST /api/projects/{uuid}/move_project/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: max_service_accounts

GET /api/proposal-proposals/{uuid}/resources/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: call_resource_template
              - New required property: call_resource_template_name
            - Properties changed
              - New property: call_resource_template
              - New property: call_resource_template_name

POST /api/proposal-proposals/{uuid}/resources/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Required changed
          - Deleted required property: requested_offering_uuid
        - Properties changed
          - New property: call_resource_template_uuid
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: call_resource_template
            - New required property: call_resource_template_name
          - Properties changed
            - New property: call_resource_template
            - New property: call_resource_template_name

GET /api/proposal-proposals/{uuid}/resources/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: call_resource_template
            - New required property: call_resource_template_name
          - Properties changed
            - New property: call_resource_template
            - New property: call_resource_template_name

PATCH /api/proposal-proposals/{uuid}/resources/{obj_uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: call_resource_template_uuid
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: call_resource_template
            - New required property: call_resource_template_name
          - Properties changed
            - New property: call_resource_template
            - New property: call_resource_template_name

PUT /api/proposal-proposals/{uuid}/resources/{obj_uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Required changed
          - Deleted required property: requested_offering_uuid
        - Properties changed
          - New property: call_resource_template_uuid
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: call_resource_template
            - New required property: call_resource_template_name
          - Properties changed
            - New property: call_resource_template
            - New property: call_resource_template_name

GET /api/proposal-protected-calls/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [fixed_duration_in_days resource_templates]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: fixed_duration_in_days
              - New property: resource_templates

POST /api/proposal-protected-calls/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: fixed_duration_in_days
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: fixed_duration_in_days
            - New property: resource_templates

GET /api/proposal-protected-calls/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [fixed_duration_in_days resource_templates]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: fixed_duration_in_days
            - New property: resource_templates

PATCH /api/proposal-protected-calls/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: fixed_duration_in_days
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: fixed_duration_in_days
            - New property: resource_templates

PUT /api/proposal-protected-calls/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: fixed_duration_in_days
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: fixed_duration_in_days
            - New property: resource_templates

POST /api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/close/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: fixed_duration_in_days
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: fixed_duration_in_days
            - New property: resource_templates

GET /api/proposal-public-calls/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [fixed_duration_in_days resource_templates]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: fixed_duration_in_days
              - New property: resource_templates

GET /api/proposal-public-calls/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [fixed_duration_in_days resource_templates]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: fixed_duration_in_days
            - New property: resource_templates

GET /api/proposal-requested-resources/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: call_resource_template
              - New required property: call_resource_template_name
            - Properties changed
              - New property: call_resource_template
              - New property: call_resource_template_name

GET /api/proposal-requested-resources/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: call_resource_template
            - New required property: call_resource_template_name
          - Properties changed
            - New property: call_resource_template
            - New property: call_resource_template_name

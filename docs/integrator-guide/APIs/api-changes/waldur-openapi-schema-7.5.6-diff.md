# OpenApi Schema Diff - 7.5.6

## For version 7.5.6

### New Endpoints: 2

--------------------
GET /api/marketplace-provider-offerings/{uuid}/list_customer_service_accounts/  
GET /api/marketplace-provider-offerings/{uuid}/list_project_service_accounts/  

### Deleted Endpoints: None

---------------------------

### Modified Endpoints: 17

--------------------------
GET /api/marketplace-component-usages/

- New query param: o

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
                    - New property: url
              - Modified property: restorations
                - Items changed
                  - Properties changed
                    - Modified property: ports
                      - Items changed
                        - Properties changed
                          - New property: url

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
                  - New property: url
            - Modified property: restorations
              - Items changed
                - Properties changed
                  - Modified property: ports
                    - Items changed
                      - Properties changed
                        - New property: url

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
                  - New property: url
            - Modified property: restorations
              - Items changed
                - Properties changed
                  - Modified property: ports
                    - Items changed
                      - Properties changed
                        - New property: url

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
                  - New property: url
            - Modified property: restorations
              - Items changed
                - Properties changed
                  - Modified property: ports
                    - Items changed
                      - Properties changed
                        - New property: url

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
                  - New property: url

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
                    - New property: url

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
                  - New property: url

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
                  - New property: url

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
                  - New property: url

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
                  - New property: url
            - Modified property: restorations
              - Items changed
                - Properties changed
                  - Modified property: ports
                    - Items changed
                      - Properties changed
                        - New property: url

GET /api/openstack-instances/{uuid}/ports/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: url

GET /api/openstack-ports/

- New query param: exclude_subnet_uuids

GET /api/openstack-routers/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [ports]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: ports

GET /api/openstack-routers/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [ports]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: ports

GET /api/override-settings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: RANCHER_USERNAME_INPUT_LABEL

POST /api/override-settings/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: RANCHER_USERNAME_INPUT_LABEL

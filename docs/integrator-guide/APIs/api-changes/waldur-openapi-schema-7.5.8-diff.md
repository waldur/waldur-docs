# OpenApi Schema Diff - 7.5.8

## For version 7.5.8

### New Endpoints: None

-----------------------

### Deleted Endpoints: None

---------------------------

### Modified Endpoints: 6

-------------------------
GET /api/rancher-clusters/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [public_ips]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: public_ips

POST /api/rancher-clusters/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: public_ips

GET /api/rancher-clusters/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [public_ips]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: public_ips

PATCH /api/rancher-clusters/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: public_ips

PUT /api/rancher-clusters/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: public_ips

POST /api/rancher-clusters/{uuid}/create_management_security_group/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: public_ips

# OpenAPI schema diff - 7.9.0

## For version 7.9.0

### New Endpoints: 3

--------------------
POST /api/marketplace-provider-offerings/{uuid}/check_unique_backend_id/  
GET /api/proposal-protected-calls/available_compliance_checklists/  
HEAD /api/proposal-protected-calls/available_compliance_checklists/  

### Deleted Endpoints: None

---------------------------

### Modified Endpoints: 5

-------------------------
GET /api/invoice-items/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: offering_component_type
              - New required property: offering_uuid
            - Properties changed
              - New property: offering_component_type
              - New property: offering_uuid

GET /api/invoice-items/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: offering_component_type
            - New required property: offering_uuid
          - Properties changed
            - New property: offering_component_type
            - New property: offering_uuid

GET /api/invoice-items/{uuid}/consumptions/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: offering_component_type
            - New required property: offering_uuid
          - Properties changed
            - New property: offering_component_type
            - New property: offering_uuid

POST /api/marketplace-component-usages/set_usage/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: date

POST /api/marketplace-component-usages/{uuid}/set_user_usage/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: date

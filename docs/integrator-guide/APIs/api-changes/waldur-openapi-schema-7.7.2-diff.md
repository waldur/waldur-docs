# OpenAPI schema diff - 7.7.2

## For version 7.7.2

### New Endpoints: 25

---------------------
GET /api/marketplace-checklists-admin-question-dependencies/  
POST /api/marketplace-checklists-admin-question-dependencies/  
DELETE /api/marketplace-checklists-admin-question-dependencies/{uuid}/  
GET /api/marketplace-checklists-admin-question-dependencies/{uuid}/  
PATCH /api/marketplace-checklists-admin-question-dependencies/{uuid}/  
PUT /api/marketplace-checklists-admin-question-dependencies/{uuid}/  
GET /api/marketplace-checklists-admin-question-options/  
POST /api/marketplace-checklists-admin-question-options/  
DELETE /api/marketplace-checklists-admin-question-options/{uuid}/  
GET /api/marketplace-checklists-admin-question-options/{uuid}/  
PATCH /api/marketplace-checklists-admin-question-options/{uuid}/  
PUT /api/marketplace-checklists-admin-question-options/{uuid}/  
GET /api/marketplace-checklists-admin-questions/  
POST /api/marketplace-checklists-admin-questions/  
DELETE /api/marketplace-checklists-admin-questions/{uuid}/  
GET /api/marketplace-checklists-admin-questions/{uuid}/  
PATCH /api/marketplace-checklists-admin-questions/{uuid}/  
PUT /api/marketplace-checklists-admin-questions/{uuid}/  
GET /api/marketplace-checklists-admin/  
POST /api/marketplace-checklists-admin/  
DELETE /api/marketplace-checklists-admin/{uuid}/  
GET /api/marketplace-checklists-admin/{uuid}/  
PATCH /api/marketplace-checklists-admin/{uuid}/  
PUT /api/marketplace-checklists-admin/{uuid}/  
GET /api/marketplace-checklists-admin/{uuid}/questions/  

### Deleted Endpoints: None

---------------------------

### Modified Endpoints: 41

--------------------------
POST /api/backend-resources/{uuid}/import_resource/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: offering_slug
            - New property: parent_offering_slug

GET /api/booking-resources/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [offering_slug parent_offering_slug]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: offering_slug
              - New property: parent_offering_slug

GET /api/booking-resources/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [offering_slug parent_offering_slug]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: offering_slug
            - New property: parent_offering_slug

GET /api/marketplace-checklists-categories/{category_uuid}/checklists/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: url
            - Properties changed
              - New property: url

GET /api/marketplace-checklists/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: url
            - Properties changed
              - New property: url

GET /api/marketplace-checklists/{checklist_uuid}/

- Modified path param: checklist_uuid
  - Name changed from 'checklist_uuid' to 'uuid'
  - Schema changed
    - Format changed from '' to 'uuid'
    - Pattern changed from '^[a-f0-9]+$' to ''
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: url
          - Properties changed
            - New property: url

GET /api/marketplace-checklists/{checklist_uuid}/answers/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: answer_data
              - Deleted property: value

POST /api/marketplace-checklists/{checklist_uuid}/answers/submit/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Items changed
          - Required changed
            - New required property: answer_data
            - Deleted required property: value
          - Properties changed
            - New property: answer_data
            - Deleted property: value
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: answer_data
              - Deleted required property: value
            - Properties changed
              - New property: answer_data
              - Deleted property: value

GET /api/marketplace-checklists/{checklist_uuid}/questions/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Return questions available for current user.'
- Modified path param: checklist_uuid
  - Name changed from 'checklist_uuid' to 'uuid'
  - Schema changed
    - Format changed from '' to 'uuid'
    - Pattern changed from '^[a-f0-9]+$' to ''
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: question_options
            - Properties changed
              - New property: question_options
              - Deleted property: correct_answer
              - Modified property: solution
                - Description changed from 'It is shown when incorrect or N/A answer is chosen' to 'Guidance shown when answer needs clarification'

GET /api/marketplace-checklists/{checklist_uuid}/user/{user_uuid}/answers/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: answer_data
              - Deleted property: value

POST /api/marketplace-provider-offerings/{uuid}/import_resource/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: offering_slug
            - New property: parent_offering_slug

GET /api/marketplace-provider-resources/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [offering_slug parent_offering_slug]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: offering_slug
              - New property: parent_offering_slug

GET /api/marketplace-provider-resources/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [offering_slug parent_offering_slug]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: offering_slug
            - New property: parent_offering_slug

GET /api/marketplace-provider-resources/{uuid}/details/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [offering_slug parent_offering_slug]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: offering_slug
            - New property: parent_offering_slug

POST /api/marketplace-provider-resources/{uuid}/move_resource/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: offering_slug
            - New property: parent_offering_slug

POST /api/marketplace-provider-resources/{uuid}/set_end_date_by_provider/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: offering_slug
            - New property: parent_offering_slug

GET /api/marketplace-resources/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [offering_slug parent_offering_slug]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: offering_slug
              - New property: parent_offering_slug

GET /api/marketplace-resources/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [offering_slug parent_offering_slug]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: offering_slug
            - New property: parent_offering_slug

GET /api/marketplace-resources/{uuid}/details/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [offering_slug parent_offering_slug]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: offering_slug
            - New property: parent_offering_slug

POST /api/marketplace-resources/{uuid}/move_resource/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: offering_slug
            - New property: parent_offering_slug

GET /api/openstack-ports/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: backend_id
                - Nullable changed from false to true

POST /api/openstack-ports/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: backend_id
              - Nullable changed from false to true

GET /api/openstack-ports/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: backend_id
              - Nullable changed from false to true

PATCH /api/openstack-ports/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: backend_id
              - Nullable changed from false to true

PUT /api/openstack-ports/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: backend_id
              - Nullable changed from false to true

GET /api/openstack-routers/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: backend_id
                - Nullable changed from false to true

GET /api/openstack-routers/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: backend_id
              - Nullable changed from false to true

GET /api/promotions-campaigns/{uuid}/resources/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: offering_slug
              - New property: parent_offering_slug

GET /api/proposal-protected-calls/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: resource_templates
                - Items changed
                  - Properties changed
                    - New property: requested_offering_plan

POST /api/proposal-protected-calls/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: resource_templates
              - Items changed
                - Properties changed
                  - New property: requested_offering_plan

GET /api/proposal-protected-calls/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: resource_templates
              - Items changed
                - Properties changed
                  - New property: requested_offering_plan

PATCH /api/proposal-protected-calls/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: resource_templates
              - Items changed
                - Properties changed
                  - New property: requested_offering_plan

PUT /api/proposal-protected-calls/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: resource_templates
              - Items changed
                - Properties changed
                  - New property: requested_offering_plan

GET /api/proposal-protected-calls/{uuid}/resource_templates/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: requested_offering_plan

POST /api/proposal-protected-calls/{uuid}/resource_templates/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: requested_offering_plan

GET /api/proposal-protected-calls/{uuid}/resource_templates/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: requested_offering_plan

PATCH /api/proposal-protected-calls/{uuid}/resource_templates/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: requested_offering_plan

PUT /api/proposal-protected-calls/{uuid}/resource_templates/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: requested_offering_plan

POST /api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/close/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: resource_templates
              - Items changed
                - Properties changed
                  - New property: requested_offering_plan

GET /api/proposal-public-calls/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: resource_templates
                - Items changed
                  - Properties changed
                    - New property: requested_offering_plan

GET /api/proposal-public-calls/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: resource_templates
              - Items changed
                - Properties changed
                  - New property: requested_offering_plan

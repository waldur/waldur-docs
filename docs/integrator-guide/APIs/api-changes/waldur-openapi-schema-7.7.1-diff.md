# OpenAPI schema diff - 7.7.1

## For version 7.7.1

### New Endpoints: None

-----------------------

### Deleted Endpoints: None

---------------------------

### Modified Endpoints: 18

--------------------------
GET /api/autoprovisioning-rules/

- Tags changed from 'autoprovisioning-rules' to 'Autoprovisioning Rules'
- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Manage autoprovisioning rules.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: category_title
              - New required property: category_url
              - New required property: offering_name
              - New required property: offering_uuid
              - New required property: plan_name
              - New required property: project_role_display_name
              - Deleted required property: project_role_dispay_name
            - Properties changed
              - New property: category_title
              - New property: category_url
              - New property: offering_name
              - New property: offering_uuid
              - New property: plan_name
              - New property: project_role_display_name
              - Deleted property: project_role_dispay_name

POST /api/autoprovisioning-rules/

- Tags changed from 'autoprovisioning-rules' to 'Autoprovisioning Rules'
- Description changed from '' to 'Manage autoprovisioning rules.'
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: category_title
            - New required property: category_url
            - New required property: offering_name
            - New required property: offering_uuid
            - New required property: plan_name
            - New required property: project_role_display_name
            - Deleted required property: project_role_dispay_name
          - Properties changed
            - New property: category_title
            - New property: category_url
            - New property: offering_name
            - New property: offering_uuid
            - New property: plan_name
            - New property: project_role_display_name
            - Deleted property: project_role_dispay_name

DELETE /api/autoprovisioning-rules/{uuid}/

- Tags changed from 'autoprovisioning-rules' to 'Autoprovisioning Rules'
- Description changed from '' to 'Manage autoprovisioning rules.'

GET /api/autoprovisioning-rules/{uuid}/

- Tags changed from 'autoprovisioning-rules' to 'Autoprovisioning Rules'
- Description changed from '' to 'Manage autoprovisioning rules.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: category_title
            - New required property: category_url
            - New required property: offering_name
            - New required property: offering_uuid
            - New required property: plan_name
            - New required property: project_role_display_name
            - Deleted required property: project_role_dispay_name
          - Properties changed
            - New property: category_title
            - New property: category_url
            - New property: offering_name
            - New property: offering_uuid
            - New property: plan_name
            - New property: project_role_display_name
            - Deleted property: project_role_dispay_name

PATCH /api/autoprovisioning-rules/{uuid}/

- Tags changed from 'autoprovisioning-rules' to 'Autoprovisioning Rules'
- Description changed from '' to 'Manage autoprovisioning rules.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: category_title
            - New required property: category_url
            - New required property: offering_name
            - New required property: offering_uuid
            - New required property: plan_name
            - New required property: project_role_display_name
            - Deleted required property: project_role_dispay_name
          - Properties changed
            - New property: category_title
            - New property: category_url
            - New property: offering_name
            - New property: offering_uuid
            - New property: plan_name
            - New property: project_role_display_name
            - Deleted property: project_role_dispay_name

PUT /api/autoprovisioning-rules/{uuid}/

- Tags changed from 'autoprovisioning-rules' to 'Autoprovisioning Rules'
- Description changed from '' to 'Manage autoprovisioning rules.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: category_title
            - New required property: category_url
            - New required property: offering_name
            - New required property: offering_uuid
            - New required property: plan_name
            - New required property: project_role_display_name
            - Deleted required property: project_role_dispay_name
          - Properties changed
            - New property: category_title
            - New property: category_url
            - New property: offering_name
            - New property: offering_uuid
            - New property: plan_name
            - New property: project_role_display_name
            - Deleted property: project_role_dispay_name

GET /api/customers/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: default_tax_percent
                - Pattern changed from '^-?\d{0,2}(?:\.\d{0,2})?$' to '^-?\d{0,3}(?:\.\d{0,2})?$'

POST /api/customers/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: default_tax_percent
              - Pattern changed from '^-?\d{0,2}(?:\.\d{0,2})?$' to '^-?\d{0,3}(?:\.\d{0,2})?$'

GET /api/customers/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: default_tax_percent
              - Pattern changed from '^-?\d{0,2}(?:\.\d{0,2})?$' to '^-?\d{0,3}(?:\.\d{0,2})?$'

PATCH /api/customers/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: default_tax_percent
              - Pattern changed from '^-?\d{0,2}(?:\.\d{0,2})?$' to '^-?\d{0,3}(?:\.\d{0,2})?$'

PUT /api/customers/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: default_tax_percent
              - Pattern changed from '^-?\d{0,2}(?:\.\d{0,2})?$' to '^-?\d{0,3}(?:\.\d{0,2})?$'

GET /api/openstack-floating-ips/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [port_fixed_ips]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: port_fixed_ips

GET /api/openstack-floating-ips/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [port_fixed_ips]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: port_fixed_ips

POST /api/openstack-tenants/{uuid}/create_floating_ip/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: port_fixed_ips

GET /api/user-group-invitations/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: project_name_template
                - Nullable changed from false to true

POST /api/user-group-invitations/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: project_name_template
            - Nullable changed from false to true
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: project_name_template
              - Nullable changed from false to true

GET /api/user-group-invitations/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: project_name_template
              - Nullable changed from false to true

POST /api/user-group-invitations/{uuid}/submit_request/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: project_name_template
              - Nullable changed from false to true

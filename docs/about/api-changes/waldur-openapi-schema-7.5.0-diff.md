# OpenApi Schema Diff - 7.5.0

## For version 7.5.0

### New Endpoints: 2

--------------------
GET /api/openstack-network-rbac-policies/  
GET /api/openstack-network-rbac-policies/{uuid}/  

### Deleted Endpoints: None

--------------------

### Modified Endpoints: 34

--------------------
GET /api/customers/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_unallocated_credit]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: customer_unallocated_credit

POST /api/customers/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_unallocated_credit

GET /api/customers/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_unallocated_credit]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_unallocated_credit

PATCH /api/customers/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_unallocated_credit

PUT /api/customers/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_unallocated_credit

GET /api/marketplace-robot-accounts/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - Deleted required property: state

POST /api/marketplace-robot-accounts/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: state

GET /api/marketplace-robot-accounts/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: state

PATCH /api/marketplace-robot-accounts/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: state

PUT /api/marketplace-robot-accounts/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: state

POST /api/marketplace-robot-accounts/{uuid}/set_state_creating/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: state

POST /api/marketplace-robot-accounts/{uuid}/set_state_deleted/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: state

POST /api/marketplace-robot-accounts/{uuid}/set_state_erred/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: state

POST /api/marketplace-robot-accounts/{uuid}/set_state_ok/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: state

POST /api/marketplace-robot-accounts/{uuid}/set_state_request_deletion/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: state

GET /api/openstack-networks/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: rbac_policies
                - Items changed
                  - Properties changed
                    - New property: network_name
                    - New property: target_tenant_name
                    - New property: url

GET /api/openstack-networks/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: rbac_policies
              - Items changed
                - Properties changed
                  - New property: network_name
                  - New property: target_tenant_name
                  - New property: url

PATCH /api/openstack-networks/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: rbac_policies
              - Items changed
                - Properties changed
                  - New property: network_name
                  - New property: target_tenant_name
                  - New property: url

PUT /api/openstack-networks/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: rbac_policies
              - Items changed
                - Properties changed
                  - New property: network_name
                  - New property: target_tenant_name
                  - New property: url

POST /api/openstack-networks/{uuid}/rbac_policy_create/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: network_name
            - New property: target_tenant_name
            - New property: url

POST /api/openstack-tenants/{uuid}/create_network/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: rbac_policies
              - Items changed
                - Properties changed
                  - New property: network_name
                  - New property: target_tenant_name
                  - New property: url

GET /api/proposal-proposals/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: project_name
            - Properties changed
              - New property: project_name

POST /api/proposal-proposals/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: project_name
          - Properties changed
            - New property: project_name

GET /api/proposal-proposals/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: project_name
          - Properties changed
            - New property: project_name

GET /api/proposal-protected-calls/{uuid}/rounds/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: proposals
                - Items changed
                  - Properties changed
                    - Modified property: reviews
                      - Items changed
                        - Required changed
                          - New required property: proposal_uuid
                        - Properties changed
                          - New property: proposal_uuid

POST /api/proposal-protected-calls/{uuid}/rounds/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: proposals
              - Items changed
                - Properties changed
                  - Modified property: reviews
                    - Items changed
                      - Required changed
                        - New required property: proposal_uuid
                      - Properties changed
                        - New property: proposal_uuid

GET /api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: proposals
              - Items changed
                - Properties changed
                  - Modified property: reviews
                    - Items changed
                      - Required changed
                        - New required property: proposal_uuid
                      - Properties changed
                        - New property: proposal_uuid

PATCH /api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: proposals
              - Items changed
                - Properties changed
                  - Modified property: reviews
                    - Items changed
                      - Required changed
                        - New required property: proposal_uuid
                      - Properties changed
                        - New property: proposal_uuid

PUT /api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: proposals
              - Items changed
                - Properties changed
                  - Modified property: reviews
                    - Items changed
                      - Required changed
                        - New required property: proposal_uuid
                      - Properties changed
                        - New property: proposal_uuid

GET /api/proposal-reviews/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: proposal_uuid
            - Properties changed
              - New property: proposal_uuid

POST /api/proposal-reviews/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: proposal_uuid
          - Properties changed
            - New property: proposal_uuid

GET /api/proposal-reviews/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: proposal_uuid
          - Properties changed
            - New property: proposal_uuid

PATCH /api/proposal-reviews/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: proposal_uuid
          - Properties changed
            - New property: proposal_uuid

PUT /api/proposal-reviews/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: proposal_uuid
          - Properties changed
            - New property: proposal_uuid

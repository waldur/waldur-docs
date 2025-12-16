# OpenAPI schema diff - 7.9.4

## For version 7.9.4

### New Endpoints: 2

--------------------
POST /api/chat/invoke/  
POST /api/chat/stream/  

### Deleted Endpoints: None

---------------------------

### Modified Endpoints: 20

--------------------------
POST /api/backend-resources/{uuid}/import_resource/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: offering_state
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/OfferingState
                - Schemas deleted: #/components/schemas/ResourceState

GET /api/booking-resources/

- New query param: visible_to_providers
- Deleted query param: exclude_pending_transitional
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: offering_state
                - Property 'AllOf' changed
                  - Schemas added: #/components/schemas/OfferingState
                  - Schemas deleted: #/components/schemas/ResourceState

HEAD /api/booking-resources/

- New query param: visible_to_providers
- Deleted query param: exclude_pending_transitional

GET /api/booking-resources/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: offering_state
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/OfferingState
                - Schemas deleted: #/components/schemas/ResourceState

GET /api/managed-rancher-cluster-resources/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: offering_state
                - Property 'AllOf' changed
                  - Schemas added: #/components/schemas/OfferingState
                  - Schemas deleted: #/components/schemas/ResourceState

GET /api/managed-rancher-cluster-resources/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: offering_state
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/OfferingState
                - Schemas deleted: #/components/schemas/ResourceState

POST /api/marketplace-provider-offerings/{uuid}/import_resource/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: offering_state
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/OfferingState
                - Schemas deleted: #/components/schemas/ResourceState

GET /api/marketplace-provider-resources/

- New query param: visible_to_providers
- Deleted query param: exclude_pending_transitional
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: offering_state
                - Property 'AllOf' changed
                  - Schemas added: #/components/schemas/OfferingState
                  - Schemas deleted: #/components/schemas/ResourceState

HEAD /api/marketplace-provider-resources/

- New query param: visible_to_providers
- Deleted query param: exclude_pending_transitional

GET /api/marketplace-provider-resources/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: offering_state
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/OfferingState
                - Schemas deleted: #/components/schemas/ResourceState

POST /api/marketplace-provider-resources/{uuid}/move_resource/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: offering_state
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/OfferingState
                - Schemas deleted: #/components/schemas/ResourceState

POST /api/marketplace-provider-resources/{uuid}/restore/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: offering_state
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/OfferingState
                - Schemas deleted: #/components/schemas/ResourceState

GET /api/marketplace-resources/

- New query param: visible_to_providers
- Deleted query param: exclude_pending_transitional
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: offering_state
                - Property 'AllOf' changed
                  - Schemas added: #/components/schemas/OfferingState
                  - Schemas deleted: #/components/schemas/ResourceState

HEAD /api/marketplace-resources/

- New query param: visible_to_providers
- Deleted query param: exclude_pending_transitional

GET /api/marketplace-resources/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: offering_state
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/OfferingState
                - Schemas deleted: #/components/schemas/ResourceState

POST /api/marketplace-resources/{uuid}/move_resource/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: offering_state
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/OfferingState
                - Schemas deleted: #/components/schemas/ResourceState

POST /api/marketplace-resources/{uuid}/restore/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: offering_state
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/OfferingState
                - Schemas deleted: #/components/schemas/ResourceState

GET /api/override-settings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: WALDUR_AUTH_SOCIAL_ROLE_CLAIM

POST /api/override-settings/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: WALDUR_AUTH_SOCIAL_ROLE_CLAIM
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: WALDUR_AUTH_SOCIAL_ROLE_CLAIM
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: WALDUR_AUTH_SOCIAL_ROLE_CLAIM

GET /api/promotions-campaigns/{uuid}/resources/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: offering_state
                - Property 'AllOf' changed
                  - Schemas added: #/components/schemas/OfferingState
                  - Schemas deleted: #/components/schemas/ResourceState

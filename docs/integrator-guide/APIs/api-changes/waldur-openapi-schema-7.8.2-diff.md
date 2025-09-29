# OpenAPI schema diff - 7.8.2

## For version 7.8.2

### New Endpoints: None

-----------------------

### Deleted Endpoints: None

---------------------------

### Modified Endpoints: 104

---------------------------
GET /api/booking-offerings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: compliance_checklist
                - Description changed from 'Checklist that offering users must complete for compliance' to ''

GET /api/booking-offerings/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: compliance_checklist
              - Description changed from 'Checklist that offering users must complete for compliance' to ''

GET /api/booking-resources/

- Modified query param: offering_billable
  - Schema changed
    - Type changed from 'string' to 'boolean'
    - Format changed from 'uuid' to ''

HEAD /api/booking-resources/

- Modified query param: offering_billable
  - Schema changed
    - Type changed from 'string' to 'boolean'
    - Format changed from 'uuid' to ''

POST /api/call-managing-organisations/

- Request body changed
  - Content changed
    - New media type: application/x-www-form-urlencoded
    - New media type: multipart/form-data

PATCH /api/call-managing-organisations/{uuid}/

- Request body changed
  - Content changed
    - New media type: application/x-www-form-urlencoded
    - New media type: multipart/form-data

PUT /api/call-managing-organisations/{uuid}/

- Request body changed
  - Content changed
    - New media type: application/x-www-form-urlencoded
    - New media type: multipart/form-data

GET /api/call-rounds/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: slug

GET /api/call-rounds/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: slug

POST /api/checklists-admin-categories/

- Request body changed
  - Content changed
    - New media type: application/x-www-form-urlencoded
    - New media type: multipart/form-data

PATCH /api/checklists-admin-categories/{uuid}/

- Request body changed
  - Content changed
    - New media type: application/x-www-form-urlencoded
    - New media type: multipart/form-data

PUT /api/checklists-admin-categories/{uuid}/

- Request body changed
  - Content changed
    - New media type: application/x-www-form-urlencoded
    - New media type: multipart/form-data

GET /api/customers/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [notification_emails]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: notification_emails

POST /api/customers/

- Request body changed
  - Content changed
    - New media type: application/x-www-form-urlencoded
    - New media type: multipart/form-data
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: notification_emails
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: notification_emails

GET /api/customers/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [notification_emails]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: notification_emails

PATCH /api/customers/{uuid}/

- Request body changed
  - Content changed
    - New media type: application/x-www-form-urlencoded
    - New media type: multipart/form-data
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: notification_emails
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: notification_emails

PUT /api/customers/{uuid}/

- Request body changed
  - Content changed
    - New media type: application/x-www-form-urlencoded
    - New media type: multipart/form-data
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: notification_emails
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: notification_emails

POST /api/external-links/

- Request body changed
  - Content changed
    - New media type: application/x-www-form-urlencoded
    - New media type: multipart/form-data

PATCH /api/external-links/{uuid}/

- Request body changed
  - Content changed
    - New media type: application/x-www-form-urlencoded
    - New media type: multipart/form-data

PUT /api/external-links/{uuid}/

- Request body changed
  - Content changed
    - New media type: application/x-www-form-urlencoded
    - New media type: multipart/form-data

POST /api/invoices/{uuid}/paid/

- Request body changed
  - Content changed
    - New media type: application/x-www-form-urlencoded
    - New media type: multipart/form-data

POST /api/marketplace-categories/

- Request body changed
  - Content changed
    - New media type: application/x-www-form-urlencoded
    - New media type: multipart/form-data

PATCH /api/marketplace-categories/{uuid}/

- Request body changed
  - Content changed
    - New media type: application/x-www-form-urlencoded
    - New media type: multipart/form-data

PUT /api/marketplace-categories/{uuid}/

- Request body changed
  - Content changed
    - New media type: application/x-www-form-urlencoded
    - New media type: multipart/form-data

POST /api/marketplace-category-groups/

- Request body changed
  - Content changed
    - New media type: application/x-www-form-urlencoded
    - New media type: multipart/form-data

PATCH /api/marketplace-category-groups/{uuid}/

- Request body changed
  - Content changed
    - New media type: application/x-www-form-urlencoded
    - New media type: multipart/form-data

PUT /api/marketplace-category-groups/{uuid}/

- Request body changed
  - Content changed
    - New media type: application/x-www-form-urlencoded
    - New media type: multipart/form-data

POST /api/marketplace-offering-files/

- Request body changed
  - Content changed
    - New media type: application/x-www-form-urlencoded
    - New media type: multipart/form-data

GET /api/marketplace-offering-user-checklist-completions/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: offering_user
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OfferingUser
                    - Properties changed
                      - Modified property: state
                        - Property 'AllOf' changed
                          - Schemas added: #/components/schemas/OfferingUserState
                          - Schemas deleted: #/components/schemas/OfferingUserStateEnum

GET /api/marketplace-offering-user-checklist-completions/{id}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: offering_user
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingUser
                  - Properties changed
                    - Modified property: state
                      - Property 'AllOf' changed
                        - Schemas added: #/components/schemas/OfferingUserState
                        - Schemas deleted: #/components/schemas/OfferingUserStateEnum

GET /api/marketplace-offering-users/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: state
                - Property 'AllOf' changed
                  - Schemas added: #/components/schemas/OfferingUserState
                  - Schemas deleted: #/components/schemas/OfferingUserStateEnum

POST /api/marketplace-offering-users/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: state
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/OfferingUserState
                - Schemas deleted: #/components/schemas/OfferingUserStateEnum

GET /api/marketplace-offering-users/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: state
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/OfferingUserState
                - Schemas deleted: #/components/schemas/OfferingUserStateEnum

PATCH /api/marketplace-offering-users/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: state
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/OfferingUserState
                - Schemas deleted: #/components/schemas/OfferingUserStateEnum

PUT /api/marketplace-offering-users/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: state
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/OfferingUserState
                - Schemas deleted: #/components/schemas/OfferingUserStateEnum

GET /api/marketplace-orders/{uuid}/offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: compliance_checklist
              - Description changed from 'Checklist that offering users must complete for compliance' to ''

POST /api/marketplace-orders/{uuid}/update_attachment/

- Request body changed
  - Content changed
    - New media type: application/x-www-form-urlencoded
    - New media type: multipart/form-data

GET /api/marketplace-provider-offerings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: compliance_checklist
                - Description changed from 'Checklist that offering users must complete for compliance' to ''

POST /api/marketplace-provider-offerings/

- Request body changed
  - Content changed
    - New media type: application/x-www-form-urlencoded
    - New media type: multipart/form-data
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: compliance_checklist
            - Description changed from 'Checklist that offering users must complete for compliance' to ''
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: compliance_checklist
              - Description changed from 'Checklist that offering users must complete for compliance' to ''

GET /api/marketplace-provider-offerings/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: compliance_checklist
              - Description changed from 'Checklist that offering users must complete for compliance' to ''

GET /api/marketplace-provider-offerings/{uuid}/list_course_accounts/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: compliance_checklist
              - Description changed from 'Checklist that offering users must complete for compliance' to ''

GET /api/marketplace-provider-offerings/{uuid}/list_customer_service_accounts/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: compliance_checklist
              - Description changed from 'Checklist that offering users must complete for compliance' to ''

GET /api/marketplace-provider-offerings/{uuid}/list_project_service_accounts/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: compliance_checklist
              - Description changed from 'Checklist that offering users must complete for compliance' to ''

POST /api/marketplace-provider-offerings/{uuid}/move_offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: compliance_checklist
              - Description changed from 'Checklist that offering users must complete for compliance' to ''

GET /api/marketplace-provider-offerings/{uuid}/stats/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: compliance_checklist
              - Description changed from 'Checklist that offering users must complete for compliance' to ''

POST /api/marketplace-provider-offerings/{uuid}/update_image/

- Request body changed
  - Content changed
    - New media type: application/x-www-form-urlencoded
    - New media type: multipart/form-data
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: compliance_checklist
              - Description changed from 'Checklist that offering users must complete for compliance' to ''

POST /api/marketplace-provider-offerings/{uuid}/update_thumbnail/

- Request body changed
  - Content changed
    - New media type: application/x-www-form-urlencoded
    - New media type: multipart/form-data

GET /api/marketplace-provider-offerings/{uuid}/user_has_resource_access/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: compliance_checklist
              - Description changed from 'Checklist that offering users must complete for compliance' to ''

GET /api/marketplace-provider-resources/

- Modified query param: offering_billable
  - Schema changed
    - Type changed from 'string' to 'boolean'
    - Format changed from 'uuid' to ''

HEAD /api/marketplace-provider-resources/

- Modified query param: offering_billable
  - Schema changed
    - Type changed from 'string' to 'boolean'
    - Format changed from 'uuid' to ''

GET /api/marketplace-provider-resources/{uuid}/offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: compliance_checklist
              - Description changed from 'Checklist that offering users must complete for compliance' to ''

GET /api/marketplace-provider-resources/{uuid}/team/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: offering_user_state
            - Properties changed
              - New property: offering_user_state

GET /api/marketplace-public-offerings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: compliance_checklist
                - Description changed from 'Checklist that offering users must complete for compliance' to ''

GET /api/marketplace-public-offerings/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: compliance_checklist
              - Description changed from 'Checklist that offering users must complete for compliance' to ''

GET /api/marketplace-resources/

- Modified query param: offering_billable
  - Schema changed
    - Type changed from 'string' to 'boolean'
    - Format changed from 'uuid' to ''

HEAD /api/marketplace-resources/

- Modified query param: offering_billable
  - Schema changed
    - Type changed from 'string' to 'boolean'
    - Format changed from 'uuid' to ''

GET /api/marketplace-resources/{uuid}/offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: compliance_checklist
              - Description changed from 'Checklist that offering users must complete for compliance' to ''

GET /api/marketplace-resources/{uuid}/team/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: offering_user_state
            - Properties changed
              - New property: offering_user_state

POST /api/marketplace-screenshots/

- Request body changed
  - Content changed
    - New media type: application/x-www-form-urlencoded
    - New media type: multipart/form-data

PUT /api/marketplace-screenshots/{uuid}/

- Request body changed
  - Content changed
    - New media type: application/x-www-form-urlencoded
    - New media type: multipart/form-data

POST /api/marketplace-script-dry-run/{uuid}/async_run/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: compliance_checklist
              - Description changed from 'Checklist that offering users must complete for compliance' to ''

POST /api/marketplace-script-dry-run/{uuid}/run/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: compliance_checklist
              - Description changed from 'Checklist that offering users must complete for compliance' to ''

POST /api/marketplace-service-providers/

- Request body changed
  - Content changed
    - New media type: application/x-www-form-urlencoded
    - New media type: multipart/form-data

PATCH /api/marketplace-service-providers/{uuid}/

- Request body changed
  - Content changed
    - New media type: application/x-www-form-urlencoded
    - New media type: multipart/form-data

PUT /api/marketplace-service-providers/{uuid}/

- Request body changed
  - Content changed
    - New media type: application/x-www-form-urlencoded
    - New media type: multipart/form-data

GET /api/override-settings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: OIDC_BLOCK_CREATION_OF_UNINVITED_USERS

POST /api/override-settings/

- Request body changed
  - Content changed
    - New media type: application/x-www-form-urlencoded
    - New media type: multipart/form-data
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: OIDC_BLOCK_CREATION_OF_UNINVITED_USERS

POST /api/payments/

- Request body changed
  - Content changed
    - New media type: application/x-www-form-urlencoded
    - New media type: multipart/form-data

PATCH /api/payments/{uuid}/

- Request body changed
  - Content changed
    - New media type: application/x-www-form-urlencoded
    - New media type: multipart/form-data

PUT /api/payments/{uuid}/

- Request body changed
  - Content changed
    - New media type: application/x-www-form-urlencoded
    - New media type: multipart/form-data

POST /api/projects/

- Request body changed
  - Content changed
    - New media type: application/x-www-form-urlencoded
    - New media type: multipart/form-data

PATCH /api/projects/{uuid}/

- Request body changed
  - Content changed
    - New media type: application/x-www-form-urlencoded
    - New media type: multipart/form-data

PUT /api/projects/{uuid}/

- Request body changed
  - Content changed
    - New media type: application/x-www-form-urlencoded
    - New media type: multipart/form-data

GET /api/proposal-proposals/

- Modified query param: o
  - Schema changed
    - Items changed
      - New enum values: [-slug slug]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: slug
            - Properties changed
              - New property: slug
              - Modified property: round
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/NestedRound
                    - Properties changed
                      - New property: slug

HEAD /api/proposal-proposals/

- Modified query param: o
  - Schema changed
    - Items changed
      - New enum values: [-slug slug]

POST /api/proposal-proposals/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: slug
          - Properties changed
            - New property: slug
            - Modified property: round
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/NestedRound
                  - Properties changed
                    - New property: slug

GET /api/proposal-proposals/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: slug
          - Properties changed
            - New property: slug
            - Modified property: round
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/NestedRound
                  - Properties changed
                    - New property: slug

POST /api/proposal-proposals/{uuid}/attach_document/

- Request body changed
  - Content changed
    - New media type: application/x-www-form-urlencoded
    - New media type: multipart/form-data

GET /api/proposal-protected-calls/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: rounds
                - Items changed
                  - Properties changed
                    - New property: slug

POST /api/proposal-protected-calls/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: rounds
              - Items changed
                - Properties changed
                  - New property: slug

GET /api/proposal-protected-calls/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: rounds
              - Items changed
                - Properties changed
                  - New property: slug

PATCH /api/proposal-protected-calls/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: rounds
              - Items changed
                - Properties changed
                  - New property: slug

PUT /api/proposal-protected-calls/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: rounds
              - Items changed
                - Properties changed
                  - New property: slug

POST /api/proposal-protected-calls/{uuid}/activate/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: rounds
              - Items changed
                - Properties changed
                  - New property: slug

POST /api/proposal-protected-calls/{uuid}/archive/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: rounds
              - Items changed
                - Properties changed
                  - New property: slug

GET /api/proposal-protected-calls/{uuid}/rounds/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: slug
            - Properties changed
              - New property: slug
              - Modified property: proposals
                - Items changed
                  - Required changed
                    - New required property: slug
                  - Properties changed
                    - New property: slug

POST /api/proposal-protected-calls/{uuid}/rounds/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: slug
          - Properties changed
            - New property: slug
            - Modified property: proposals
              - Items changed
                - Required changed
                  - New required property: slug
                - Properties changed
                  - New property: slug

GET /api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: slug
          - Properties changed
            - New property: slug
            - Modified property: proposals
              - Items changed
                - Required changed
                  - New required property: slug
                - Properties changed
                  - New property: slug

PATCH /api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: slug
          - Properties changed
            - New property: slug
            - Modified property: proposals
              - Items changed
                - Required changed
                  - New required property: slug
                - Properties changed
                  - New property: slug

PUT /api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: slug
          - Properties changed
            - New property: slug
            - Modified property: proposals
              - Items changed
                - Required changed
                  - New required property: slug
                - Properties changed
                  - New property: slug

POST /api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/close/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: rounds
              - Items changed
                - Properties changed
                  - New property: slug

GET /api/proposal-public-calls/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: rounds
                - Items changed
                  - Properties changed
                    - New property: slug

GET /api/proposal-public-calls/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: rounds
              - Items changed
                - Properties changed
                  - New property: slug

GET /api/proposal-reviews/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: call_slug
              - New required property: created
              - New required property: modified
              - New required property: proposal_slug
              - New required property: round_slug
            - Properties changed
              - New property: call_slug
              - New property: created
              - New property: modified
              - New property: proposal_slug
              - New property: round_slug

POST /api/proposal-reviews/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: call_slug
            - New required property: created
            - New required property: modified
            - New required property: proposal_slug
            - New required property: round_slug
          - Properties changed
            - New property: call_slug
            - New property: created
            - New property: modified
            - New property: proposal_slug
            - New property: round_slug

GET /api/proposal-reviews/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: call_slug
            - New required property: created
            - New required property: modified
            - New required property: proposal_slug
            - New required property: round_slug
          - Properties changed
            - New property: call_slug
            - New property: created
            - New property: modified
            - New property: proposal_slug
            - New property: round_slug

PATCH /api/proposal-reviews/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: call_slug
            - New required property: created
            - New required property: modified
            - New required property: proposal_slug
            - New required property: round_slug
          - Properties changed
            - New property: call_slug
            - New property: created
            - New property: modified
            - New property: proposal_slug
            - New property: round_slug

PUT /api/proposal-reviews/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: call_slug
            - New required property: created
            - New required property: modified
            - New required property: proposal_slug
            - New required property: round_slug
          - Properties changed
            - New property: call_slug
            - New property: created
            - New property: modified
            - New property: proposal_slug
            - New property: round_slug

POST /api/slurm-jobs/

- Request body changed
  - Content changed
    - New media type: application/x-www-form-urlencoded
    - New media type: multipart/form-data

PUT /api/slurm-jobs/{uuid}/

- Request body changed
  - Content changed
    - New media type: application/x-www-form-urlencoded
    - New media type: multipart/form-data

POST /api/support-attachments/

- Request body changed
  - Content changed
    - New media type: application/x-www-form-urlencoded
    - New media type: multipart/form-data

POST /api/users/

- Request body changed
  - Content changed
    - New media type: application/x-www-form-urlencoded
    - New media type: multipart/form-data

PATCH /api/users/{uuid}/

- Request body changed
  - Content changed
    - New media type: application/x-www-form-urlencoded
    - New media type: multipart/form-data

PUT /api/users/{uuid}/

- Request body changed
  - Content changed
    - New media type: application/x-www-form-urlencoded
    - New media type: multipart/form-data

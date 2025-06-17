# OpenAPI schema diff - 7.6.4

## For version 7.6.4

### New Endpoints: None

-----------------------

### Deleted Endpoints: 1

------------------------
POST /api/openstack-migrations/{uuid}/run/  

### Modified Endpoints: 42

--------------------------
GET /api/booking-resources/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_slug project_slug]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: customer_slug
              - New property: project_slug

GET /api/booking-resources/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_slug project_slug]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_slug
            - New property: project_slug

POST /api/marketplace-provider-offerings/{uuid}/import_resource/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_slug
            - New property: project_slug

GET /api/marketplace-provider-offerings/{uuid}/list_customer_users/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: token_expires_at

GET /api/marketplace-provider-resources/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_slug project_slug]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: customer_slug
              - New property: project_slug

GET /api/marketplace-provider-resources/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_slug project_slug]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_slug
            - New property: project_slug

GET /api/marketplace-provider-resources/{uuid}/details/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_slug project_slug]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_slug
            - New property: project_slug

POST /api/marketplace-provider-resources/{uuid}/move_resource/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_slug
            - New property: project_slug

POST /api/marketplace-provider-resources/{uuid}/refresh_last_sync/

- Description changed from '' to 'Refresh the last sync time for a resource.'
- Request body changed
- Responses changed
  - Modified response: 200
    - Description changed from '' to 'No response body'
    - Content changed
      - Deleted media type: application/json

POST /api/marketplace-provider-resources/{uuid}/set_as_ok/

- Description changed from '' to 'Set the resource as OK.'
- Request body changed
- Responses changed
  - Modified response: 200
    - Description changed from '' to 'No response body'
    - Content changed
      - Deleted media type: application/json

POST /api/marketplace-provider-resources/{uuid}/set_end_date_by_provider/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_slug
            - New property: project_slug

GET /api/marketplace-resources/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_slug project_slug]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: customer_slug
              - New property: project_slug

GET /api/marketplace-resources/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_slug project_slug]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_slug
            - New property: project_slug

GET /api/marketplace-resources/{uuid}/details/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_slug project_slug]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_slug
            - New property: project_slug

POST /api/marketplace-resources/{uuid}/move_resource/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_slug
            - New property: project_slug

POST /api/openstack-tenants/{uuid}/create_security_group/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Required changed
          - New required property: rules
        - Properties changed
          - New property: rules

GET /api/promotions-campaigns/{uuid}/resources/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: customer_slug
              - New property: project_slug

GET /api/proposal-protected-calls/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [reviewer_identity_visible_to_submitters reviews_visible_to_submitters]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: reviewer_identity_visible_to_submitters
              - New property: reviews_visible_to_submitters

POST /api/proposal-protected-calls/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: reviewer_identity_visible_to_submitters
          - New property: reviews_visible_to_submitters
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: reviewer_identity_visible_to_submitters
            - New property: reviews_visible_to_submitters

GET /api/proposal-protected-calls/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [reviewer_identity_visible_to_submitters reviews_visible_to_submitters]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: reviewer_identity_visible_to_submitters
            - New property: reviews_visible_to_submitters

PATCH /api/proposal-protected-calls/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: reviewer_identity_visible_to_submitters
          - New property: reviews_visible_to_submitters
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: reviewer_identity_visible_to_submitters
            - New property: reviews_visible_to_submitters

PUT /api/proposal-protected-calls/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: reviewer_identity_visible_to_submitters
          - New property: reviews_visible_to_submitters
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: reviewer_identity_visible_to_submitters
            - New property: reviews_visible_to_submitters

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
                      - Description changed from '' to 'Return serialized reviews based on user permissions and visibility settings.
- Staff, call managers, and reviewers see all reviews.
- Submitters see submitted reviews if visibility is enabled.'
                      - Items changed
                        - Type changed from 'object' to ''
                        - Required changed
                          - Deleted required property: call_name
                          - Deleted required property: call_uuid
                          - Deleted required property: proposal
                          - Deleted required property: proposal_name
                          - Deleted required property: proposal_uuid
                          - Deleted required property: review_end_date
                          - Deleted required property: reviewer
                          - Deleted required property: reviewer_full_name
                          - Deleted required property: reviewer_uuid
                          - Deleted required property: round_cutoff_time
                          - Deleted required property: round_name
                          - Deleted required property: round_start_time
                          - Deleted required property: round_uuid
                          - Deleted required property: state
                          - Deleted required property: url
                          - Deleted required property: uuid
                        - Properties changed
                          - Deleted property: call_name
                          - Deleted property: call_uuid
                          - Deleted property: comment_project_description
                          - Deleted property: comment_project_duration
                          - Deleted property: comment_project_has_civilian_purpose
                          - Deleted property: comment_project_is_confidential
                          - Deleted property: comment_project_summary
                          - Deleted property: comment_project_supporting_documentation
                          - Deleted property: comment_project_title
                          - Deleted property: comment_resource_requests
                          - Deleted property: comment_team
                          - Deleted property: proposal
                          - Deleted property: proposal_name
                          - Deleted property: proposal_uuid
                          - Deleted property: review_end_date
                          - Deleted property: reviewer
                          - Deleted property: reviewer_full_name
                          - Deleted property: reviewer_uuid
                          - Deleted property: round_cutoff_time
                          - Deleted property: round_name
                          - Deleted property: round_start_time
                          - Deleted property: round_uuid
                          - Deleted property: state
                          - Deleted property: summary_private_comment
                          - Deleted property: summary_public_comment
                          - Deleted property: summary_score
                          - Deleted property: url
                          - Deleted property: uuid

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
                    - Description changed from '' to 'Return serialized reviews based on user permissions and visibility settings.
- Staff, call managers, and reviewers see all reviews.
- Submitters see submitted reviews if visibility is enabled.'
                    - Items changed
                      - Type changed from 'object' to ''
                      - Required changed
                        - Deleted required property: call_name
                        - Deleted required property: call_uuid
                        - Deleted required property: proposal
                        - Deleted required property: proposal_name
                        - Deleted required property: proposal_uuid
                        - Deleted required property: review_end_date
                        - Deleted required property: reviewer
                        - Deleted required property: reviewer_full_name
                        - Deleted required property: reviewer_uuid
                        - Deleted required property: round_cutoff_time
                        - Deleted required property: round_name
                        - Deleted required property: round_start_time
                        - Deleted required property: round_uuid
                        - Deleted required property: state
                        - Deleted required property: url
                        - Deleted required property: uuid
                      - Properties changed
                        - Deleted property: call_name
                        - Deleted property: call_uuid
                        - Deleted property: comment_project_description
                        - Deleted property: comment_project_duration
                        - Deleted property: comment_project_has_civilian_purpose
                        - Deleted property: comment_project_is_confidential
                        - Deleted property: comment_project_summary
                        - Deleted property: comment_project_supporting_documentation
                        - Deleted property: comment_project_title
                        - Deleted property: comment_resource_requests
                        - Deleted property: comment_team
                        - Deleted property: proposal
                        - Deleted property: proposal_name
                        - Deleted property: proposal_uuid
                        - Deleted property: review_end_date
                        - Deleted property: reviewer
                        - Deleted property: reviewer_full_name
                        - Deleted property: reviewer_uuid
                        - Deleted property: round_cutoff_time
                        - Deleted property: round_name
                        - Deleted property: round_start_time
                        - Deleted property: round_uuid
                        - Deleted property: state
                        - Deleted property: summary_private_comment
                        - Deleted property: summary_public_comment
                        - Deleted property: summary_score
                        - Deleted property: url
                        - Deleted property: uuid

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
                    - Description changed from '' to 'Return serialized reviews based on user permissions and visibility settings.
- Staff, call managers, and reviewers see all reviews.
- Submitters see submitted reviews if visibility is enabled.'
                    - Items changed
                      - Type changed from 'object' to ''
                      - Required changed
                        - Deleted required property: call_name
                        - Deleted required property: call_uuid
                        - Deleted required property: proposal
                        - Deleted required property: proposal_name
                        - Deleted required property: proposal_uuid
                        - Deleted required property: review_end_date
                        - Deleted required property: reviewer
                        - Deleted required property: reviewer_full_name
                        - Deleted required property: reviewer_uuid
                        - Deleted required property: round_cutoff_time
                        - Deleted required property: round_name
                        - Deleted required property: round_start_time
                        - Deleted required property: round_uuid
                        - Deleted required property: state
                        - Deleted required property: url
                        - Deleted required property: uuid
                      - Properties changed
                        - Deleted property: call_name
                        - Deleted property: call_uuid
                        - Deleted property: comment_project_description
                        - Deleted property: comment_project_duration
                        - Deleted property: comment_project_has_civilian_purpose
                        - Deleted property: comment_project_is_confidential
                        - Deleted property: comment_project_summary
                        - Deleted property: comment_project_supporting_documentation
                        - Deleted property: comment_project_title
                        - Deleted property: comment_resource_requests
                        - Deleted property: comment_team
                        - Deleted property: proposal
                        - Deleted property: proposal_name
                        - Deleted property: proposal_uuid
                        - Deleted property: review_end_date
                        - Deleted property: reviewer
                        - Deleted property: reviewer_full_name
                        - Deleted property: reviewer_uuid
                        - Deleted property: round_cutoff_time
                        - Deleted property: round_name
                        - Deleted property: round_start_time
                        - Deleted property: round_uuid
                        - Deleted property: state
                        - Deleted property: summary_private_comment
                        - Deleted property: summary_public_comment
                        - Deleted property: summary_score
                        - Deleted property: url
                        - Deleted property: uuid

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
                    - Description changed from '' to 'Return serialized reviews based on user permissions and visibility settings.
- Staff, call managers, and reviewers see all reviews.
- Submitters see submitted reviews if visibility is enabled.'
                    - Items changed
                      - Type changed from 'object' to ''
                      - Required changed
                        - Deleted required property: call_name
                        - Deleted required property: call_uuid
                        - Deleted required property: proposal
                        - Deleted required property: proposal_name
                        - Deleted required property: proposal_uuid
                        - Deleted required property: review_end_date
                        - Deleted required property: reviewer
                        - Deleted required property: reviewer_full_name
                        - Deleted required property: reviewer_uuid
                        - Deleted required property: round_cutoff_time
                        - Deleted required property: round_name
                        - Deleted required property: round_start_time
                        - Deleted required property: round_uuid
                        - Deleted required property: state
                        - Deleted required property: url
                        - Deleted required property: uuid
                      - Properties changed
                        - Deleted property: call_name
                        - Deleted property: call_uuid
                        - Deleted property: comment_project_description
                        - Deleted property: comment_project_duration
                        - Deleted property: comment_project_has_civilian_purpose
                        - Deleted property: comment_project_is_confidential
                        - Deleted property: comment_project_summary
                        - Deleted property: comment_project_supporting_documentation
                        - Deleted property: comment_project_title
                        - Deleted property: comment_resource_requests
                        - Deleted property: comment_team
                        - Deleted property: proposal
                        - Deleted property: proposal_name
                        - Deleted property: proposal_uuid
                        - Deleted property: review_end_date
                        - Deleted property: reviewer
                        - Deleted property: reviewer_full_name
                        - Deleted property: reviewer_uuid
                        - Deleted property: round_cutoff_time
                        - Deleted property: round_name
                        - Deleted property: round_start_time
                        - Deleted property: round_uuid
                        - Deleted property: state
                        - Deleted property: summary_private_comment
                        - Deleted property: summary_public_comment
                        - Deleted property: summary_score
                        - Deleted property: url
                        - Deleted property: uuid

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
                    - Description changed from '' to 'Return serialized reviews based on user permissions and visibility settings.
- Staff, call managers, and reviewers see all reviews.
- Submitters see submitted reviews if visibility is enabled.'
                    - Items changed
                      - Type changed from 'object' to ''
                      - Required changed
                        - Deleted required property: call_name
                        - Deleted required property: call_uuid
                        - Deleted required property: proposal
                        - Deleted required property: proposal_name
                        - Deleted required property: proposal_uuid
                        - Deleted required property: review_end_date
                        - Deleted required property: reviewer
                        - Deleted required property: reviewer_full_name
                        - Deleted required property: reviewer_uuid
                        - Deleted required property: round_cutoff_time
                        - Deleted required property: round_name
                        - Deleted required property: round_start_time
                        - Deleted required property: round_uuid
                        - Deleted required property: state
                        - Deleted required property: url
                        - Deleted required property: uuid
                      - Properties changed
                        - Deleted property: call_name
                        - Deleted property: call_uuid
                        - Deleted property: comment_project_description
                        - Deleted property: comment_project_duration
                        - Deleted property: comment_project_has_civilian_purpose
                        - Deleted property: comment_project_is_confidential
                        - Deleted property: comment_project_summary
                        - Deleted property: comment_project_supporting_documentation
                        - Deleted property: comment_project_title
                        - Deleted property: comment_resource_requests
                        - Deleted property: comment_team
                        - Deleted property: proposal
                        - Deleted property: proposal_name
                        - Deleted property: proposal_uuid
                        - Deleted property: review_end_date
                        - Deleted property: reviewer
                        - Deleted property: reviewer_full_name
                        - Deleted property: reviewer_uuid
                        - Deleted property: round_cutoff_time
                        - Deleted property: round_name
                        - Deleted property: round_start_time
                        - Deleted property: round_uuid
                        - Deleted property: state
                        - Deleted property: summary_private_comment
                        - Deleted property: summary_public_comment
                        - Deleted property: summary_score
                        - Deleted property: url
                        - Deleted property: uuid

POST /api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/close/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: reviewer_identity_visible_to_submitters
          - New property: reviews_visible_to_submitters
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: reviewer_identity_visible_to_submitters
            - New property: reviews_visible_to_submitters

GET /api/proposal-public-calls/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [reviewer_identity_visible_to_submitters reviews_visible_to_submitters]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: reviewer_identity_visible_to_submitters
              - New property: reviews_visible_to_submitters

GET /api/proposal-public-calls/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [reviewer_identity_visible_to_submitters reviews_visible_to_submitters]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: reviewer_identity_visible_to_submitters
            - New property: reviews_visible_to_submitters

GET /api/proposal-reviews/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: anonymous_reviewer_name
            - Properties changed
              - New property: anonymous_reviewer_name

POST /api/proposal-reviews/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: anonymous_reviewer_name
          - Properties changed
            - New property: anonymous_reviewer_name

GET /api/proposal-reviews/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: anonymous_reviewer_name
          - Properties changed
            - New property: anonymous_reviewer_name

PATCH /api/proposal-reviews/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: anonymous_reviewer_name
          - Properties changed
            - New property: anonymous_reviewer_name

PUT /api/proposal-reviews/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: anonymous_reviewer_name
          - Properties changed
            - New property: anonymous_reviewer_name

GET /api/user-invitations/

- Modified query param: o
  - Schema changed
    - Items changed
      - New enum values: [-created_by created_by]

GET /api/users/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [token_expires_at]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: token_expires_at

POST /api/users/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: token_expires_at

GET /api/users/me/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [token_expires_at]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: token_expires_at

GET /api/users/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [token_expires_at]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: token_expires_at

PATCH /api/users/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: token_expires_at

PUT /api/users/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: token_expires_at

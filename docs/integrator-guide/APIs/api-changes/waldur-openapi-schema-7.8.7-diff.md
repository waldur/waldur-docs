# OpenAPI schema diff - 7.8.7

## For version 7.8.7

### New Endpoints: 2

--------------------
POST /api/marketplace-provider-resources/{uuid}/update_options_direct/  
POST /api/projects/{uuid}/sync_user_roles/  

### Deleted Endpoints: 1

------------------------
POST /projects/{uuid}/sync_user_roles/  

### Modified Endpoints: 66

--------------------------
GET /api/autoprovisioning-rules/

- Tags changed from 'Autoprovisioning Rules' to 'autoprovisioning-rules'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - Deleted required property: customer
            - Properties changed
              - New property: use_user_organization_as_customer_name
              - Modified property: customer
                - Nullable changed from false to true

HEAD /api/autoprovisioning-rules/

- Tags changed from 'Autoprovisioning Rules' to 'autoprovisioning-rules'

POST /api/autoprovisioning-rules/

- Tags changed from 'Autoprovisioning Rules' to 'autoprovisioning-rules'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Required changed
          - Deleted required property: customer
        - Properties changed
          - New property: use_user_organization_as_customer_name
          - Modified property: customer
            - Nullable changed from false to true
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: customer
          - Properties changed
            - New property: use_user_organization_as_customer_name
            - Modified property: customer
              - Nullable changed from false to true

DELETE /api/autoprovisioning-rules/{uuid}/

- Tags changed from 'Autoprovisioning Rules' to 'autoprovisioning-rules'

GET /api/autoprovisioning-rules/{uuid}/

- Tags changed from 'Autoprovisioning Rules' to 'autoprovisioning-rules'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: customer
          - Properties changed
            - New property: use_user_organization_as_customer_name
            - Modified property: customer
              - Nullable changed from false to true

PATCH /api/autoprovisioning-rules/{uuid}/

- Tags changed from 'Autoprovisioning Rules' to 'autoprovisioning-rules'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: use_user_organization_as_customer_name
          - Modified property: customer
            - Nullable changed from false to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: customer
          - Properties changed
            - New property: use_user_organization_as_customer_name
            - Modified property: customer
              - Nullable changed from false to true

PUT /api/autoprovisioning-rules/{uuid}/

- Tags changed from 'Autoprovisioning Rules' to 'autoprovisioning-rules'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Required changed
          - Deleted required property: customer
        - Properties changed
          - New property: use_user_organization_as_customer_name
          - Modified property: customer
            - Nullable changed from false to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: customer
          - Properties changed
            - New property: use_user_organization_as_customer_name
            - Modified property: customer
              - Nullable changed from false to true

GET /api/checklists-admin-questions/

- New query param: checklist_type

HEAD /api/checklists-admin-questions/

- New query param: checklist_type

GET /api/customers/

- Description changed from 'To get a list of customers, run GET against /api/customers/ as authenticated user. Note that a user can
only see connected customers:

- customers that the user owns
- customers that have a project where user has a role

Staff also can filter customers by user UUID, for example /api/customers/?user_uuid=<UUID>

Staff also can filter customers by exists accounting_start_date, for example:

The first category:
/api/customers/?accounting_is_running=True
    has accounting_start_date empty (i.e. accounting starts at once)
    has accounting_start_date in the past (i.e. has already started).

Those that are not in the first:
/api/customers/?accounting_is_running=False # exists accounting_start_date' to 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing'

GET /api/marketplace-offering-terms-of-service/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: grace_period_days

POST /api/marketplace-offering-terms-of-service/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: grace_period_days
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: grace_period_days

GET /api/marketplace-offering-terms-of-service/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: grace_period_days

PATCH /api/marketplace-offering-terms-of-service/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: grace_period_days
          - Deleted property: requires_reconsent
          - Deleted property: version
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: grace_period_days

PUT /api/marketplace-offering-terms-of-service/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: grace_period_days
          - Deleted property: requires_reconsent
          - Deleted property: version
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: grace_period_days

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
                      - New property: has_compliance_checklist

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
                    - New property: has_compliance_checklist

GET /api/marketplace-offering-users/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [has_compliance_checklist]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: has_compliance_checklist

POST /api/marketplace-offering-users/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: has_compliance_checklist

GET /api/marketplace-offering-users/checklist-template/

- New query param: parent_uuid
- Responses changed
  - New response: 404
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: initial_visible_questions
              - Items changed
                - Properties changed
                  - New property: required
            - Modified property: questions
              - Items changed
                - Properties changed
                  - New property: required

HEAD /api/marketplace-offering-users/checklist-template/

- New query param: parent_uuid

GET /api/marketplace-offering-users/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [has_compliance_checklist]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: has_compliance_checklist

PATCH /api/marketplace-offering-users/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: has_compliance_checklist

PUT /api/marketplace-offering-users/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: has_compliance_checklist

POST /api/marketplace-site-agent-identities/{uuid}/register_event_subscription/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: observable_object_type
            - Property 'AllOf' changed
              - Modified schema: #/components/schemas/ObservableObjectTypeEnum
                - New enum values: [resource_periodic_limits]

GET /api/metadata/events/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: event_groups
          - Properties changed
            - Modified property: event_groups
              - Description changed from '' to 'Map of event group keys to lists of event type enums from EventType'
              - AdditionalProperties changed
                - Schema added

GET /api/metadata/features/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: feature_enums
            - New required property: features
          - Properties changed
            - Modified property: feature_enums
              - Description changed from '' to 'Nested feature enum values by section'
              - AdditionalProperties changed
                - Schema added
            - Modified property: features
              - Description changed from '' to 'List of feature sections with descriptions'
              - Items changed
                - Schema added

GET /api/metadata/permissions/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: permission_descriptions
            - New required property: permission_map
            - New required property: permissions
            - New required property: roles
          - Properties changed
            - Modified property: permission_descriptions
              - Description changed from '' to 'Grouped permission descriptions for UI'
              - Items changed
                - Schema added
            - Modified property: permission_map
              - Description changed from '' to 'Map of resource types to create permission enums'
              - AdditionalProperties changed
                - Schema added
            - Modified property: permissions
              - Description changed from '' to 'Map of permission keys to permission enum values from PermissionEnum'
              - AdditionalProperties changed
                - Schema added
            - Modified property: roles
              - Description changed from '' to 'Map of role keys to role enum values from RoleEnum'
              - AdditionalProperties changed
                - Schema added

GET /api/metadata/settings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: settings
          - Properties changed
            - Modified property: settings
              - Description changed from '' to 'List of settings sections with configuration items'
              - Items changed
                - Schema added

GET /api/onboarding-country-configs/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: questions
            - Properties changed
              - New property: questions

POST /api/onboarding-country-configs/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: questions
          - Properties changed
            - New property: questions

GET /api/onboarding-country-configs/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: questions
          - Properties changed
            - New property: questions

PATCH /api/onboarding-country-configs/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: questions
          - Properties changed
            - New property: questions

PUT /api/onboarding-country-configs/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: questions
          - Properties changed
            - New property: questions

GET /api/onboarding-justifications/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: verification_uuid
            - Properties changed
              - New property: verification_uuid
              - Modified property: user
                - Type changed from 'integer' to 'string'
                - Format changed from '' to 'uri'
                - ReadOnly changed from false to true
              - Modified property: validated_by
                - Type changed from 'integer' to 'string'
                - Format changed from '' to 'uri'
              - Modified property: verification
                - Type changed from 'integer' to 'string'
                - Format changed from '' to 'uri'

POST /api/onboarding-justifications/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Required changed
          - Deleted required property: user
        - Properties changed
          - Deleted property: user
          - Modified property: verification
            - Type changed from 'integer' to 'string'
            - Format changed from '' to 'uri'
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: verification_uuid
          - Properties changed
            - New property: verification_uuid
            - Modified property: user
              - Type changed from 'integer' to 'string'
              - Format changed from '' to 'uri'
              - ReadOnly changed from false to true
            - Modified property: validated_by
              - Type changed from 'integer' to 'string'
              - Format changed from '' to 'uri'
            - Modified property: verification
              - Type changed from 'integer' to 'string'
              - Format changed from '' to 'uri'

POST /api/onboarding-justifications/create_justification/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: verification_uuid
          - Properties changed
            - New property: verification_uuid
            - Modified property: user
              - Type changed from 'integer' to 'string'
              - Format changed from '' to 'uri'
              - ReadOnly changed from false to true
            - Modified property: validated_by
              - Type changed from 'integer' to 'string'
              - Format changed from '' to 'uri'
            - Modified property: verification
              - Type changed from 'integer' to 'string'
              - Format changed from '' to 'uri'

GET /api/onboarding-justifications/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: verification_uuid
          - Properties changed
            - New property: verification_uuid
            - Modified property: user
              - Type changed from 'integer' to 'string'
              - Format changed from '' to 'uri'
              - ReadOnly changed from false to true
            - Modified property: validated_by
              - Type changed from 'integer' to 'string'
              - Format changed from '' to 'uri'
            - Modified property: verification
              - Type changed from 'integer' to 'string'
              - Format changed from '' to 'uri'

PATCH /api/onboarding-justifications/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Deleted property: user
          - Modified property: verification
            - Type changed from 'integer' to 'string'
            - Format changed from '' to 'uri'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: verification_uuid
          - Properties changed
            - New property: verification_uuid
            - Modified property: user
              - Type changed from 'integer' to 'string'
              - Format changed from '' to 'uri'
              - ReadOnly changed from false to true
            - Modified property: validated_by
              - Type changed from 'integer' to 'string'
              - Format changed from '' to 'uri'
            - Modified property: verification
              - Type changed from 'integer' to 'string'
              - Format changed from '' to 'uri'

PUT /api/onboarding-justifications/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Required changed
          - Deleted required property: user
        - Properties changed
          - Deleted property: user
          - Modified property: verification
            - Type changed from 'integer' to 'string'
            - Format changed from '' to 'uri'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: verification_uuid
          - Properties changed
            - New property: verification_uuid
            - Modified property: user
              - Type changed from 'integer' to 'string'
              - Format changed from '' to 'uri'
              - ReadOnly changed from false to true
            - Modified property: validated_by
              - Type changed from 'integer' to 'string'
              - Format changed from '' to 'uri'
            - Modified property: verification
              - Type changed from 'integer' to 'string'
              - Format changed from '' to 'uri'

POST /api/onboarding-justifications/{uuid}/approve/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: verification_uuid
          - Properties changed
            - New property: verification_uuid
            - Modified property: user
              - Type changed from 'integer' to 'string'
              - Format changed from '' to 'uri'
              - ReadOnly changed from false to true
            - Modified property: validated_by
              - Type changed from 'integer' to 'string'
              - Format changed from '' to 'uri'
            - Modified property: verification
              - Type changed from 'integer' to 'string'
              - Format changed from '' to 'uri'

POST /api/onboarding-justifications/{uuid}/reject/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: verification_uuid
          - Properties changed
            - New property: verification_uuid
            - Modified property: user
              - Type changed from 'integer' to 'string'
              - Format changed from '' to 'uri'
              - ReadOnly changed from false to true
            - Modified property: validated_by
              - Type changed from 'integer' to 'string'
              - Format changed from '' to 'uri'
            - Modified property: verification
              - Type changed from 'integer' to 'string'
              - Format changed from '' to 'uri'

GET /api/onboarding-question-metadata/

- New query param: question_description
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: checklist_name
            - Properties changed
              - New property: checklist_name
              - Modified property: question
                - Description changed from 'Question this metadata applies to' to ''

HEAD /api/onboarding-question-metadata/

- New query param: question_description

POST /api/onboarding-question-metadata/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: question
            - Description changed from 'Question this metadata applies to' to ''
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: checklist_name
          - Properties changed
            - New property: checklist_name
            - Modified property: question
              - Description changed from 'Question this metadata applies to' to ''

GET /api/onboarding-question-metadata/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: checklist_name
          - Properties changed
            - New property: checklist_name
            - Modified property: question
              - Description changed from 'Question this metadata applies to' to ''

PATCH /api/onboarding-question-metadata/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: question
            - Description changed from 'Question this metadata applies to' to ''
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: checklist_name
          - Properties changed
            - New property: checklist_name
            - Modified property: question
              - Description changed from 'Question this metadata applies to' to ''

PUT /api/onboarding-question-metadata/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: question
            - Description changed from 'Question this metadata applies to' to ''
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: checklist_name
          - Properties changed
            - New property: checklist_name
            - Modified property: question
              - Description changed from 'Question this metadata applies to' to ''

GET /api/onboarding-verifications/checklist-template/

- New query param: parent_uuid
- Responses changed
  - New response: 404
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: initial_visible_questions
              - Items changed
                - Properties changed
                  - New property: required
            - Modified property: questions
              - Items changed
                - Properties changed
                  - New property: required

HEAD /api/onboarding-verifications/checklist-template/

- New query param: parent_uuid

POST /api/onboarding-verifications/start_verification/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: is_manual_validation

POST /api/openstack-backups/{uuid}/restore/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: ports
            - Items changed
              - Properties changed
                - New property: tenant

POST /api/openstack-instances/{uuid}/update_ports/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: ports
            - Items changed
              - Properties changed
                - New property: tenant

GET /api/openstack-ports/

- New query param: fixed_ips
- New query param: network_name
- New query param: network_uuid
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [target_tenant]
- Modified query param: o
  - Schema changed
    - Items changed
      - New enum values: [-admin_state_up -created -device_owner -instance_name -mac_address -name -status -subnet_name admin_state_up created device_owner instance_name mac_address name status subnet_name]

HEAD /api/openstack-ports/

- New query param: fixed_ips
- New query param: network_name
- New query param: network_uuid
- Modified query param: o
  - Schema changed
    - Items changed
      - New enum values: [-admin_state_up -created -device_owner -instance_name -mac_address -name -status -subnet_name admin_state_up created device_owner instance_name mac_address name status subnet_name]

POST /api/openstack-ports/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: target_tenant

GET /api/openstack-ports/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [target_tenant]

PATCH /api/openstack-ports/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: target_tenant

PUT /api/openstack-ports/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: target_tenant

GET /api/override-settings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: DISABLED_OFFERING_TYPES

POST /api/override-settings/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: DISABLED_OFFERING_TYPES
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: DISABLED_OFFERING_TYPES
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: DISABLED_OFFERING_TYPES

GET /api/projects/checklist-template/

- New query param: parent_uuid
- Responses changed
  - New response: 404
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: initial_visible_questions
              - Items changed
                - Properties changed
                  - New property: required
            - Modified property: questions
              - Items changed
                - Properties changed
                  - New property: required

HEAD /api/projects/checklist-template/

- New query param: parent_uuid

GET /api/proposal-proposals/checklist-template/

- New query param: parent_uuid
- Responses changed
  - New response: 404
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: initial_visible_questions
              - Items changed
                - Properties changed
                  - New property: required
            - Modified property: questions
              - Items changed
                - Properties changed
                  - New property: required

HEAD /api/proposal-proposals/checklist-template/

- New query param: parent_uuid

POST /api/proposal-proposals/{uuid}/submit_answers/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: completion
              - Required changed
                - New required property: requires_review
                - New required property: review_trigger_summary
                - New required property: reviewed_by_name
              - Properties changed
                - New property: requires_review
                - New property: review_notes
                - New property: review_trigger_summary
                - New property: reviewed_at
                - New property: reviewed_by
                - New property: reviewed_by_name

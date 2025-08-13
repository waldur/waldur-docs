# OpenAPI schema diff - 7.7.5

## For version 7.7.5

### New Endpoints: 95

---------------------
GET /api/checklists-admin-categories/  
HEAD /api/checklists-admin-categories/  
POST /api/checklists-admin-categories/  
DELETE /api/checklists-admin-categories/{uuid}/  
GET /api/checklists-admin-categories/{uuid}/  
PATCH /api/checklists-admin-categories/{uuid}/  
PUT /api/checklists-admin-categories/{uuid}/  
GET /api/checklists-admin-question-dependencies/  
HEAD /api/checklists-admin-question-dependencies/  
POST /api/checklists-admin-question-dependencies/  
DELETE /api/checklists-admin-question-dependencies/{uuid}/  
GET /api/checklists-admin-question-dependencies/{uuid}/  
PATCH /api/checklists-admin-question-dependencies/{uuid}/  
PUT /api/checklists-admin-question-dependencies/{uuid}/  
GET /api/checklists-admin-question-options/  
HEAD /api/checklists-admin-question-options/  
POST /api/checklists-admin-question-options/  
DELETE /api/checklists-admin-question-options/{uuid}/  
GET /api/checklists-admin-question-options/{uuid}/  
PATCH /api/checklists-admin-question-options/{uuid}/  
PUT /api/checklists-admin-question-options/{uuid}/  
GET /api/checklists-admin-questions/  
HEAD /api/checklists-admin-questions/  
POST /api/checklists-admin-questions/  
DELETE /api/checklists-admin-questions/{uuid}/  
GET /api/checklists-admin-questions/{uuid}/  
PATCH /api/checklists-admin-questions/{uuid}/  
PUT /api/checklists-admin-questions/{uuid}/  
GET /api/checklists-admin/  
HEAD /api/checklists-admin/  
POST /api/checklists-admin/  
DELETE /api/checklists-admin/{uuid}/  
GET /api/checklists-admin/{uuid}/  
PATCH /api/checklists-admin/{uuid}/  
PUT /api/checklists-admin/{uuid}/  
GET /api/checklists-admin/{uuid}/questions/  
GET /api/external-links/  
HEAD /api/external-links/  
POST /api/external-links/  
DELETE /api/external-links/{uuid}/  
GET /api/external-links/{uuid}/  
PATCH /api/external-links/{uuid}/  
PUT /api/external-links/{uuid}/  
GET /api/maintenance-announcement-offerings/  
HEAD /api/maintenance-announcement-offerings/  
POST /api/maintenance-announcement-offerings/  
DELETE /api/maintenance-announcement-offerings/{uuid}/  
GET /api/maintenance-announcement-offerings/{uuid}/  
PATCH /api/maintenance-announcement-offerings/{uuid}/  
PUT /api/maintenance-announcement-offerings/{uuid}/  
GET /api/maintenance-announcement-template-offerings/  
HEAD /api/maintenance-announcement-template-offerings/  
POST /api/maintenance-announcement-template-offerings/  
DELETE /api/maintenance-announcement-template-offerings/{uuid}/  
GET /api/maintenance-announcement-template-offerings/{uuid}/  
PATCH /api/maintenance-announcement-template-offerings/{uuid}/  
PUT /api/maintenance-announcement-template-offerings/{uuid}/  
GET /api/maintenance-announcements-template/  
HEAD /api/maintenance-announcements-template/  
POST /api/maintenance-announcements-template/  
DELETE /api/maintenance-announcements-template/{uuid}/  
GET /api/maintenance-announcements-template/{uuid}/  
PATCH /api/maintenance-announcements-template/{uuid}/  
PUT /api/maintenance-announcements-template/{uuid}/  
GET /api/maintenance-announcements/  
HEAD /api/maintenance-announcements/  
POST /api/maintenance-announcements/  
DELETE /api/maintenance-announcements/{uuid}/  
GET /api/maintenance-announcements/{uuid}/  
PATCH /api/maintenance-announcements/{uuid}/  
PUT /api/maintenance-announcements/{uuid}/  
POST /api/maintenance-announcements/{uuid}/cancel_maintenance/  
POST /api/maintenance-announcements/{uuid}/complete_maintenance/  
POST /api/maintenance-announcements/{uuid}/schedule/  
POST /api/maintenance-announcements/{uuid}/start_maintenance/  
POST /api/maintenance-announcements/{uuid}/unschedule/  
POST /api/marketplace-offering-users/{uuid}/request_deletion/  
POST /api/marketplace-offering-users/{uuid}/set_deleted/  
POST /api/marketplace-offering-users/{uuid}/set_deleting/  
POST /api/marketplace-offering-users/{uuid}/set_error_creating/  
POST /api/marketplace-offering-users/{uuid}/set_error_deleting/  
PATCH /api/marketplace-offering-users/{uuid}/update_comments/  
POST /api/marketplace-provider-resources/{uuid}/pull/  
POST /api/marketplace-resources/{uuid}/pull/  
GET /api/projects/{uuid}/checklist/  
GET /api/projects/{uuid}/completion_status/  
POST /api/projects/{uuid}/submit_answers/  
GET /api/proposal-proposals/{uuid}/checklist/  
GET /api/proposal-proposals/{uuid}/checklist_review/  
GET /api/proposal-proposals/{uuid}/completion_review_status/  
GET /api/proposal-proposals/{uuid}/completion_status/  
POST /api/proposal-proposals/{uuid}/submit_answers/  
GET /api/proposal-protected-calls/{uuid}/compliance_overview/  
GET /api/proposal-protected-calls/{uuid}/proposals/{proposal_uuid}/compliance-answers/  
POST /api/proposal-protected-calls/{uuid}/review_proposal_compliance/  

### Deleted Endpoints: 73

-------------------------
GET /api/customers/{customer_uuid}/marketplace-checklists/  
POST /api/customers/{customer_uuid}/marketplace-checklists/  
GET /api/customers/{customer_uuid}/marketplace-checklists/{checklist_uuid}/  
GET /api/marketplace-checklists-admin-question-dependencies/  
HEAD /api/marketplace-checklists-admin-question-dependencies/  
POST /api/marketplace-checklists-admin-question-dependencies/  
DELETE /api/marketplace-checklists-admin-question-dependencies/{uuid}/  
GET /api/marketplace-checklists-admin-question-dependencies/{uuid}/  
PATCH /api/marketplace-checklists-admin-question-dependencies/{uuid}/  
PUT /api/marketplace-checklists-admin-question-dependencies/{uuid}/  
GET /api/marketplace-checklists-admin-question-options/  
HEAD /api/marketplace-checklists-admin-question-options/  
POST /api/marketplace-checklists-admin-question-options/  
DELETE /api/marketplace-checklists-admin-question-options/{uuid}/  
GET /api/marketplace-checklists-admin-question-options/{uuid}/  
PATCH /api/marketplace-checklists-admin-question-options/{uuid}/  
PUT /api/marketplace-checklists-admin-question-options/{uuid}/  
GET /api/marketplace-checklists-admin-questions/  
HEAD /api/marketplace-checklists-admin-questions/  
POST /api/marketplace-checklists-admin-questions/  
DELETE /api/marketplace-checklists-admin-questions/{uuid}/  
GET /api/marketplace-checklists-admin-questions/{uuid}/  
PATCH /api/marketplace-checklists-admin-questions/{uuid}/  
PUT /api/marketplace-checklists-admin-questions/{uuid}/  
GET /api/marketplace-checklists-admin/  
HEAD /api/marketplace-checklists-admin/  
POST /api/marketplace-checklists-admin/  
DELETE /api/marketplace-checklists-admin/{uuid}/  
GET /api/marketplace-checklists-admin/{uuid}/  
PATCH /api/marketplace-checklists-admin/{uuid}/  
PUT /api/marketplace-checklists-admin/{uuid}/  
GET /api/marketplace-checklists-admin/{uuid}/questions/  
GET /api/marketplace-checklists-categories/  
GET /api/marketplace-checklists-categories/{category_uuid}/checklists/  
GET /api/marketplace-checklists-categories/{uuid}/  
GET /api/marketplace-checklists/  
HEAD /api/marketplace-checklists/  
GET /api/marketplace-checklists/{checklist_uuid}/answers/  
POST /api/marketplace-checklists/{checklist_uuid}/answers/submit/  
GET /api/marketplace-checklists/{checklist_uuid}/stats/  
GET /api/marketplace-checklists/{checklist_uuid}/user/{user_uuid}/answers/  
GET /api/marketplace-checklists/{uuid}/  
GET /api/marketplace-checklists/{uuid}/questions/  
GET /api/marketplace-maintenance-announcement-offerings/  
HEAD /api/marketplace-maintenance-announcement-offerings/  
POST /api/marketplace-maintenance-announcement-offerings/  
DELETE /api/marketplace-maintenance-announcement-offerings/{uuid}/  
GET /api/marketplace-maintenance-announcement-offerings/{uuid}/  
PATCH /api/marketplace-maintenance-announcement-offerings/{uuid}/  
PUT /api/marketplace-maintenance-announcement-offerings/{uuid}/  
GET /api/marketplace-maintenance-announcement-template-offerings/  
HEAD /api/marketplace-maintenance-announcement-template-offerings/  
POST /api/marketplace-maintenance-announcement-template-offerings/  
DELETE /api/marketplace-maintenance-announcement-template-offerings/{uuid}/  
GET /api/marketplace-maintenance-announcement-template-offerings/{uuid}/  
PATCH /api/marketplace-maintenance-announcement-template-offerings/{uuid}/  
PUT /api/marketplace-maintenance-announcement-template-offerings/{uuid}/  
GET /api/marketplace-maintenance-announcements-template/  
HEAD /api/marketplace-maintenance-announcements-template/  
POST /api/marketplace-maintenance-announcements-template/  
DELETE /api/marketplace-maintenance-announcements-template/{uuid}/  
GET /api/marketplace-maintenance-announcements-template/{uuid}/  
PATCH /api/marketplace-maintenance-announcements-template/{uuid}/  
PUT /api/marketplace-maintenance-announcements-template/{uuid}/  
GET /api/marketplace-maintenance-announcements/  
HEAD /api/marketplace-maintenance-announcements/  
POST /api/marketplace-maintenance-announcements/  
DELETE /api/marketplace-maintenance-announcements/{uuid}/  
GET /api/marketplace-maintenance-announcements/{uuid}/  
PATCH /api/marketplace-maintenance-announcements/{uuid}/  
PUT /api/marketplace-maintenance-announcements/{uuid}/  
GET /api/projects/{project_uuid}/marketplace-checklists/  
GET /api/users/{user_uuid}/marketplace-checklist-stats/  

### Modified Endpoints: 337

---------------------------
HEAD /api/access-subnets/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'access_subnets_head' to 'access_subnets_count'

HEAD /api/admin-announcements/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'admin_announcements_head' to 'admin_announcements_count'

HEAD /api/auth-tokens/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'auth_tokens_head' to 'auth_tokens_count'

HEAD /api/autoprovisioning-rules/

- Description changed from 'Manage autoprovisioning rules.' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'autoprovisioning_rules_head' to 'autoprovisioning_rules_count'

HEAD /api/aws-images/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'aws_images_head' to 'aws_images_count'

HEAD /api/aws-instances/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'aws_instances_head' to 'aws_instances_count'

HEAD /api/aws-regions/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'aws_regions_head' to 'aws_regions_count'

HEAD /api/aws-sizes/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'aws_sizes_head' to 'aws_sizes_count'

HEAD /api/aws-volumes/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'aws_volumes_head' to 'aws_volumes_count'

HEAD /api/azure-images/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'azure_images_head' to 'azure_images_count'

HEAD /api/azure-locations/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'azure_locations_head' to 'azure_locations_count'

HEAD /api/azure-public-ips/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'azure_public_ips_head' to 'azure_public_ips_count'

HEAD /api/azure-resource-groups/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'azure_resource_groups_head' to 'azure_resource_groups_count'

HEAD /api/azure-sizes/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'azure_sizes_head' to 'azure_sizes_count'

HEAD /api/azure-sql-databases/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'azure_sql_databases_head' to 'azure_sql_databases_count'

HEAD /api/azure-sql-servers/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'azure_sql_servers_head' to 'azure_sql_servers_count'

HEAD /api/azure-virtualmachines/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'azure_virtualmachines_head' to 'azure_virtualmachines_count'

GET /api/backend-resource-requests/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: error_message
              - New required property: error_traceback
            - Properties changed
              - New property: error_message
              - New property: error_traceback

HEAD /api/backend-resource-requests/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'backend_resource_requests_head' to 'backend_resource_requests_count'

POST /api/backend-resource-requests/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: error_message
            - New required property: error_traceback
          - Properties changed
            - New property: error_message
            - New property: error_traceback

GET /api/backend-resource-requests/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: error_message
            - New required property: error_traceback
          - Properties changed
            - New property: error_message
            - New property: error_traceback

HEAD /api/backend-resources/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'backend_resources_head' to 'backend_resources_count'

POST /api/backend-resources/{uuid}/import_resource/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: plan_unit
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BillingUnit
                          - New enum values: [quarter]
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: plan_unit
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BillingUnit
                          - New enum values: [quarter]
            - Modified property: plan_unit
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BillingUnit
                  - New enum values: [quarter]

GET /api/booking-offerings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: components
                - Items changed
                  - Properties changed
                    - Modified property: limit_period
                      - Property 'OneOf' changed
                        - Modified schema: #/components/schemas/LimitPeriodEnum
                          - New enum values: [quarterly]
              - Modified property: plans
                - Items changed
                  - Properties changed
                    - Modified property: unit
                      - New enum values: [quarter]

HEAD /api/booking-offerings/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'booking_offerings_head' to 'booking_offerings_count'

GET /api/booking-offerings/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Properties changed
                  - Modified property: limit_period
                    - Property 'OneOf' changed
                      - Modified schema: #/components/schemas/LimitPeriodEnum
                        - New enum values: [quarterly]
            - Modified property: plans
              - Items changed
                - Properties changed
                  - Modified property: unit
                    - New enum values: [quarter]

GET /api/booking-resources/

- Modified query param: query
  - Description changed from 'Query' to 'Search by resource UUID, name, backend ID, effective ID, IPs or hypervisor'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: creation_order
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - Modified property: plan_unit
                        - Property 'AllOf' changed
                          - Modified schema: #/components/schemas/BillingUnit
                            - New enum values: [quarter]
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - Modified property: plan_unit
                        - Property 'AllOf' changed
                          - Modified schema: #/components/schemas/BillingUnit
                            - New enum values: [quarter]
              - Modified property: plan_unit
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/BillingUnit
                    - New enum values: [quarter]

HEAD /api/booking-resources/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'booking_resources_head' to 'booking_resources_count'
- Modified query param: query
  - Description changed from 'Query' to 'Search by resource UUID, name, backend ID, effective ID, IPs or hypervisor'

GET /api/booking-resources/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: plan_unit
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BillingUnit
                          - New enum values: [quarter]
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: plan_unit
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BillingUnit
                          - New enum values: [quarter]
            - Modified property: plan_unit
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BillingUnit
                  - New enum values: [quarter]

HEAD /api/broadcast-message-templates/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'broadcast_message_templates_head' to 'broadcast_message_templates_count'

HEAD /api/broadcast-messages/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'broadcast_messages_head' to 'broadcast_messages_count'

HEAD /api/broadcast-messages/recipients/

- Description changed from '' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'broadcast_messages_recipients_head' to 'broadcast_messages_recipients_count'

HEAD /api/call-managing-organisations/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'call_managing_organisations_head' to 'call_managing_organisations_count'

HEAD /api/call-proposal-project-role-mappings/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'call_proposal_project_role_mappings_head' to 'call_proposal_project_role_mappings_count'

HEAD /api/call-rounds/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'call_rounds_head' to 'call_rounds_count'

HEAD /api/component-user-usage-limits/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'component_user_usage_limits_head' to 'component_user_usage_limits_count'

HEAD /api/customer-credits/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'customer_credits_head' to 'customer_credits_count'

HEAD /api/customer-permissions-reviews/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'customer_permissions_reviews_head' to 'customer_permissions_reviews_count'

HEAD /api/customer-quotas/

- Description changed from 'List customer quotas.' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'customer_quotas_head' to 'customer_quotas_count'

GET /api/customers/

- Modified query param: query
  - Description changed from '' to 'Filter by name, native name, abbreviation, domain, UUID, registration code or agreement number'

HEAD /api/customers/

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
/api/customers/?accounting_is_running=False # exists accounting_start_date' to 'Get number of items in the collection matching the request parameters.'

- OperationID changed from 'customers_head' to 'customers_count'
- Modified query param: query
  - Description changed from '' to 'Filter by name, native name, abbreviation, domain, UUID, registration code or agreement number'

GET /api/customers/countries/

- Modified query param: query
  - Description changed from '' to 'Filter by name, native name, abbreviation, domain, UUID, registration code or agreement number'

HEAD /api/customers/countries/

- Description changed from 'Return list of countries' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'customers_countries_head' to 'customers_countries_count'
- Modified query param: query
  - Description changed from '' to 'Filter by name, native name, abbreviation, domain, UUID, registration code or agreement number'

HEAD /api/digitalocean-droplets/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'digitalocean_droplets_head' to 'digitalocean_droplets_count'

HEAD /api/digitalocean-images/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'digitalocean_images_head' to 'digitalocean_images_count'

HEAD /api/digitalocean-regions/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'digitalocean_regions_head' to 'digitalocean_regions_count'

HEAD /api/digitalocean-sizes/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'digitalocean_sizes_head' to 'digitalocean_sizes_count'

HEAD /api/email-logs/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'email_logs_head' to 'email_logs_count'

HEAD /api/event-subscriptions/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'event_subscriptions_head' to 'event_subscriptions_count'

HEAD /api/events-stats/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'events_stats_head' to 'events_stats_count'

HEAD /api/events/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'events_head' to 'events_count'

HEAD /api/events/count/

- Description changed from '' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'events_count_head' to 'events_count_count'

HEAD /api/events/event_groups/

- Description changed from 'Returns a list of groups with event types.
Group is used in exclude_features query param.' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'events_event_groups_head' to 'events_event_groups_count'

HEAD /api/events/scope_types/

- Description changed from 'Returns a list of scope types acceptable by events filter.' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'events_scope_types_head' to 'events_scope_types_count'

GET /api/financial-reports/

- Modified query param: query
  - Description changed from '' to 'Filter by name, native name, abbreviation, domain, UUID, registration code or agreement number'

HEAD /api/financial-reports/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'financial_reports_head' to 'financial_reports_count'
- Modified query param: query
  - Description changed from '' to 'Filter by name, native name, abbreviation, domain, UUID, registration code or agreement number'

GET /api/freeipa-profiles/

- Modified query param: query
  - Description changed from '' to 'Filter by username, user UUID, first name or last name'

HEAD /api/freeipa-profiles/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'freeipa_profiles_head' to 'freeipa_profiles_count'
- Modified query param: query
  - Description changed from '' to 'Filter by username, user UUID, first name or last name'

HEAD /api/google-auth/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'google_auth_head' to 'google_auth_count'

HEAD /api/google-auth/callback/

- Description changed from 'Callback endpoint for Google authorization.' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'google_auth_callback_head' to 'google_auth_callback_count'

GET /api/hooks-email/

- Modified query param: query
  - Description changed from '' to 'Filter by author name, username and email'

HEAD /api/hooks-email/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'hooks_email_head' to 'hooks_email_count'
- Modified query param: query
  - Description changed from '' to 'Filter by author name, username and email'

GET /api/hooks-web/

- Modified query param: query
  - Description changed from '' to 'Filter by author name, username and email'

HEAD /api/hooks-web/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'hooks_web_head' to 'hooks_web_count'
- Modified query param: query
  - Description changed from '' to 'Filter by author name, username and email'

HEAD /api/hooks/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'hooks_head' to 'hooks_count'

HEAD /api/identity-providers/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'identity_providers_head' to 'identity_providers_count'

GET /api/invoice-items/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: unit
                - New enum values: [quarter]

HEAD /api/invoice-items/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'invoice_items_head' to 'invoice_items_count'

HEAD /api/invoice-items/costs/

- Description changed from 'Get costs breakdown for a project by year and month.' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'invoice_items_costs_head' to 'invoice_items_costs_count'

HEAD /api/invoice-items/customer_costs_for_period/

- Description changed from '' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'invoice_items_customer_costs_for_period_head' to 'invoice_items_customer_costs_for_period_count'

HEAD /api/invoice-items/project_costs_for_period/

- Description changed from 'Get resource cost breakdown for a project over a specified period.' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'invoice_items_project_costs_for_period_head' to 'invoice_items_project_costs_for_period_count'

HEAD /api/invoice-items/total_price/

- Description changed from 'Calculate total price for filtered invoice items.' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'invoice_items_total_price_head' to 'invoice_items_total_price_count'

GET /api/invoice-items/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: unit
              - New enum values: [quarter]

GET /api/invoice-items/{uuid}/consumptions/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: unit
              - New enum values: [quarter]

GET /api/invoices/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: items
                - Items changed
                  - Properties changed
                    - Modified property: unit
                      - New enum values: [quarter]

HEAD /api/invoices/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'invoices_head' to 'invoices_count'

HEAD /api/invoices/growth/

- Description changed from 'Analyze invoice trends over time by comparing monthly totals for major customers versus others over the past year.' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'invoices_growth_head' to 'invoices_growth_count'

GET /api/invoices/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: items
              - Items changed
                - Properties changed
                  - Modified property: unit
                    - New enum values: [quarter]

GET /api/invoices/{uuid}/items/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: unit
              - New enum values: [quarter]

POST /api/invoices/{uuid}/paid/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: items
              - Items changed
                - Properties changed
                  - Modified property: unit
                    - New enum values: [quarter]

HEAD /api/keycloak-groups/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'keycloak_groups_head' to 'keycloak_groups_count'

HEAD /api/keycloak-user-group-memberships/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'keycloak_user_group_memberships_head' to 'keycloak_user_group_memberships_count'

HEAD /api/keys/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'keys_head' to 'keys_count'

GET /api/lexis-links/

- Modified query param: query
  - Description changed from '' to 'Filter by robot account username or type'

HEAD /api/lexis-links/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'lexis_links_head' to 'lexis_links_count'
- Modified query param: query
  - Description changed from '' to 'Filter by robot account username or type'

HEAD /api/marketplace-categories/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'marketplace_categories_head' to 'marketplace_categories_count'

HEAD /api/marketplace-category-columns/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'marketplace_category_columns_head' to 'marketplace_category_columns_count'

HEAD /api/marketplace-category-component-usages/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'marketplace_category_component_usages_head' to 'marketplace_category_component_usages_count'

HEAD /api/marketplace-category-components/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'marketplace_category_components_head' to 'marketplace_category_components_count'

HEAD /api/marketplace-category-groups/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'marketplace_category_groups_head' to 'marketplace_category_groups_count'

HEAD /api/marketplace-category-help-articles/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'marketplace_category_help_articles_head' to 'marketplace_category_help_articles_count'

HEAD /api/marketplace-component-usages/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'marketplace_component_usages_head' to 'marketplace_component_usages_count'

HEAD /api/marketplace-component-user-usages/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'marketplace_component_user_usages_head' to 'marketplace_component_user_usages_count'

HEAD /api/marketplace-customer-estimated-cost-policies/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'marketplace_customer_estimated_cost_policies_head' to 'marketplace_customer_estimated_cost_policies_count'

HEAD /api/marketplace-customer-estimated-cost-policies/actions/

- Description changed from '' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'marketplace_customer_estimated_cost_policies_actions_head' to 'marketplace_customer_estimated_cost_policies_actions_count'

HEAD /api/marketplace-customer-service-accounts/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'marketplace_customer_service_accounts_head' to 'marketplace_customer_service_accounts_count'

HEAD /api/marketplace-integration-statuses/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'marketplace_integration_statuses_head' to 'marketplace_integration_statuses_count'

HEAD /api/marketplace-offering-estimated-cost-policies/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'marketplace_offering_estimated_cost_policies_head' to 'marketplace_offering_estimated_cost_policies_count'

HEAD /api/marketplace-offering-estimated-cost-policies/actions/

- Description changed from 'List available actions for OfferingEstimatedCostPolicy' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'marketplace_offering_estimated_cost_policies_actions_head' to 'marketplace_offering_estimated_cost_policies_actions_count'

HEAD /api/marketplace-offering-files/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'marketplace_offering_files_head' to 'marketplace_offering_files_count'

HEAD /api/marketplace-offering-permissions-log/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'marketplace_offering_permissions_log_head' to 'marketplace_offering_permissions_log_count'

HEAD /api/marketplace-offering-permissions/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'marketplace_offering_permissions_head' to 'marketplace_offering_permissions_count'

HEAD /api/marketplace-offering-referrals/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'marketplace_offering_referrals_head' to 'marketplace_offering_referrals_count'

HEAD /api/marketplace-offering-usage-policies/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'marketplace_offering_usage_policies_head' to 'marketplace_offering_usage_policies_count'

HEAD /api/marketplace-offering-usage-policies/actions/

- Description changed from '' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'marketplace_offering_usage_policies_actions_head' to 'marketplace_offering_usage_policies_actions_count'

HEAD /api/marketplace-offering-user-roles/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'marketplace_offering_user_roles_head' to 'marketplace_offering_user_roles_count'

GET /api/marketplace-offering-users/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [service_provider_comment_url]
- Modified query param: query
  - Description changed from '' to 'Search by offering name, username or user name'
- Modified query param: state
  - Schema changed
    - Items changed
      - New enum values: [Error creating Error deleting]
      - Deleted enum values: [Error]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: service_provider_comment_url
              - Modified property: state
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OfferingUserStateEnum
                    - New enum values: [Error creating Error deleting]
                    - Deleted enum values: [Error]

HEAD /api/marketplace-offering-users/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'marketplace_offering_users_head' to 'marketplace_offering_users_count'
- Modified query param: query
  - Description changed from '' to 'Search by offering name, username or user name'
- Modified query param: state
  - Schema changed
    - Items changed
      - New enum values: [Error creating Error deleting]
      - Deleted enum values: [Error]

POST /api/marketplace-offering-users/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: service_provider_comment_url
            - Modified property: state
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingUserStateEnum
                  - New enum values: [Error creating Error deleting]
                  - Deleted enum values: [Error]

GET /api/marketplace-offering-users/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [service_provider_comment_url]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: service_provider_comment_url
            - Modified property: state
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingUserStateEnum
                  - New enum values: [Error creating Error deleting]
                  - Deleted enum values: [Error]

PATCH /api/marketplace-offering-users/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: service_provider_comment_url
            - Modified property: state
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingUserStateEnum
                  - New enum values: [Error creating Error deleting]
                  - Deleted enum values: [Error]

PUT /api/marketplace-offering-users/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: service_provider_comment_url
            - Modified property: state
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingUserStateEnum
                  - New enum values: [Error creating Error deleting]
                  - Deleted enum values: [Error]

POST /api/marketplace-offering-users/{uuid}/set_pending_account_linking/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: comment_url

POST /api/marketplace-offering-users/{uuid}/set_pending_additional_validation/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: comment_url

GET /api/marketplace-orders/

- Modified query param: query
  - Description changed from '' to 'Search by order UUID, project name or resource name'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: plan_unit
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/BillingUnit
                    - New enum values: [quarter]

HEAD /api/marketplace-orders/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'marketplace_orders_head' to 'marketplace_orders_count'
- Modified query param: query
  - Description changed from '' to 'Search by order UUID, project name or resource name'

POST /api/marketplace-orders/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: plan_unit
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BillingUnit
                  - New enum values: [quarter]

GET /api/marketplace-orders/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: plan_unit
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BillingUnit
                  - New enum values: [quarter]

GET /api/marketplace-orders/{uuid}/offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Properties changed
                  - Modified property: limit_period
                    - Property 'OneOf' changed
                      - Modified schema: #/components/schemas/LimitPeriodEnum
                        - New enum values: [quarterly]
            - Modified property: plans
              - Items changed
                - Properties changed
                  - Modified property: unit
                    - New enum values: [quarter]

GET /api/marketplace-plan-components/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: plan_unit
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/BillingUnit
                    - New enum values: [quarter]

HEAD /api/marketplace-plan-components/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'marketplace_plan_components_head' to 'marketplace_plan_components_count'

GET /api/marketplace-plan-components/{id}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: plan_unit
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BillingUnit
                  - New enum values: [quarter]

GET /api/marketplace-plans/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: unit
                - New enum values: [quarter]

HEAD /api/marketplace-plans/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'marketplace_plans_head' to 'marketplace_plans_count'

POST /api/marketplace-plans/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: unit
            - New enum values: [quarter]
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: unit
              - New enum values: [quarter]

HEAD /api/marketplace-plans/usage_stats/

- Description changed from '' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'marketplace_plans_usage_stats_head' to 'marketplace_plans_usage_stats_count'

GET /api/marketplace-plans/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: unit
              - New enum values: [quarter]

PATCH /api/marketplace-plans/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: unit
            - New enum values: [quarter]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: unit
              - New enum values: [quarter]

PUT /api/marketplace-plans/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: unit
            - New enum values: [quarter]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: unit
              - New enum values: [quarter]

HEAD /api/marketplace-project-estimated-cost-policies/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'marketplace_project_estimated_cost_policies_head' to 'marketplace_project_estimated_cost_policies_count'

HEAD /api/marketplace-project-estimated-cost-policies/actions/

- Description changed from '' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'marketplace_project_estimated_cost_policies_actions_head' to 'marketplace_project_estimated_cost_policies_actions_count'

HEAD /api/marketplace-project-service-accounts/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'marketplace_project_service_accounts_head' to 'marketplace_project_service_accounts_count'

HEAD /api/marketplace-project-update-requests/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'marketplace_project_update_requests_head' to 'marketplace_project_update_requests_count'

GET /api/marketplace-provider-offerings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: components
                - Items changed
                  - Properties changed
                    - Modified property: limit_period
                      - Property 'OneOf' changed
                        - Modified schema: #/components/schemas/LimitPeriodEnum
                          - New enum values: [quarterly]
              - Modified property: plans
                - Items changed
                  - Properties changed
                    - Modified property: unit
                      - New enum values: [quarter]

HEAD /api/marketplace-provider-offerings/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'marketplace_provider_offerings_head' to 'marketplace_provider_offerings_count'

POST /api/marketplace-provider-offerings/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: components
            - Items changed
              - Properties changed
                - Modified property: limit_period
                  - Property 'OneOf' changed
                    - Modified schema: #/components/schemas/LimitPeriodEnum
                      - New enum values: [quarterly]
          - Modified property: plans
            - Items changed
              - Properties changed
                - Modified property: unit
                  - New enum values: [quarter]
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Properties changed
                  - Modified property: limit_period
                    - Property 'OneOf' changed
                      - Modified schema: #/components/schemas/LimitPeriodEnum
                        - New enum values: [quarterly]
            - Modified property: plans
              - Items changed
                - Properties changed
                  - Modified property: unit
                    - New enum values: [quarter]

HEAD /api/marketplace-provider-offerings/groups/

- Description changed from '' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'marketplace_provider_offerings_groups_head' to 'marketplace_provider_offerings_groups_count'

GET /api/marketplace-provider-offerings/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Properties changed
                  - Modified property: limit_period
                    - Property 'OneOf' changed
                      - Modified schema: #/components/schemas/LimitPeriodEnum
                        - New enum values: [quarterly]
            - Modified property: plans
              - Items changed
                - Properties changed
                  - Modified property: unit
                    - New enum values: [quarter]

POST /api/marketplace-provider-offerings/{uuid}/create_offering_component/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: limit_period
            - Property 'OneOf' changed
              - Modified schema: #/components/schemas/LimitPeriodEnum
                - New enum values: [quarterly]

POST /api/marketplace-provider-offerings/{uuid}/import_resource/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: additional_details
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: plan_unit
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BillingUnit
                          - New enum values: [quarter]
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: plan_unit
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BillingUnit
                          - New enum values: [quarter]
            - Modified property: plan_unit
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BillingUnit
                  - New enum values: [quarter]

GET /api/marketplace-provider-offerings/{uuid}/list_customer_projects/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: end_date_requested_by
                - ReadOnly changed from false to true

GET /api/marketplace-provider-offerings/{uuid}/list_customer_service_accounts/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Properties changed
                  - Modified property: limit_period
                    - Property 'OneOf' changed
                      - Modified schema: #/components/schemas/LimitPeriodEnum
                        - New enum values: [quarterly]
            - Modified property: plans
              - Items changed
                - Properties changed
                  - Modified property: unit
                    - New enum values: [quarter]

GET /api/marketplace-provider-offerings/{uuid}/list_project_service_accounts/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Properties changed
                  - Modified property: limit_period
                    - Property 'OneOf' changed
                      - Modified schema: #/components/schemas/LimitPeriodEnum
                        - New enum values: [quarterly]
            - Modified property: plans
              - Items changed
                - Properties changed
                  - Modified property: unit
                    - New enum values: [quarter]

POST /api/marketplace-provider-offerings/{uuid}/move_offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Properties changed
                  - Modified property: limit_period
                    - Property 'OneOf' changed
                      - Modified schema: #/components/schemas/LimitPeriodEnum
                        - New enum values: [quarterly]
            - Modified property: plans
              - Items changed
                - Properties changed
                  - Modified property: unit
                    - New enum values: [quarter]

GET /api/marketplace-provider-offerings/{uuid}/orders/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: plan_unit
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/BillingUnit
                    - New enum values: [quarter]

GET /api/marketplace-provider-offerings/{uuid}/orders/{order_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: plan_unit
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BillingUnit
                  - New enum values: [quarter]

POST /api/marketplace-provider-offerings/{uuid}/refresh_offering_usernames/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: components
            - Items changed
              - Properties changed
                - Modified property: limit_period
                  - Property 'OneOf' changed
                    - Modified schema: #/components/schemas/LimitPeriodEnum
                      - New enum values: [quarterly]
          - Modified property: plans
            - Items changed
              - Properties changed
                - Modified property: unit
                  - New enum values: [quarter]

GET /api/marketplace-provider-offerings/{uuid}/stats/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Properties changed
                  - Modified property: limit_period
                    - Property 'OneOf' changed
                      - Modified schema: #/components/schemas/LimitPeriodEnum
                        - New enum values: [quarterly]
            - Modified property: plans
              - Items changed
                - Properties changed
                  - Modified property: unit
                    - New enum values: [quarter]

POST /api/marketplace-provider-offerings/{uuid}/update_image/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Properties changed
                  - Modified property: limit_period
                    - Property 'OneOf' changed
                      - Modified schema: #/components/schemas/LimitPeriodEnum
                        - New enum values: [quarterly]
            - Modified property: plans
              - Items changed
                - Properties changed
                  - Modified property: unit
                    - New enum values: [quarter]

POST /api/marketplace-provider-offerings/{uuid}/update_offering_component/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: limit_period
            - Property 'OneOf' changed
              - Modified schema: #/components/schemas/LimitPeriodEnum
                - New enum values: [quarterly]

GET /api/marketplace-provider-offerings/{uuid}/user_has_resource_access/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Properties changed
                  - Modified property: limit_period
                    - Property 'OneOf' changed
                      - Modified schema: #/components/schemas/LimitPeriodEnum
                        - New enum values: [quarterly]
            - Modified property: plans
              - Items changed
                - Properties changed
                  - Modified property: unit
                    - New enum values: [quarter]

GET /api/marketplace-provider-resources/

- Modified query param: query
  - Description changed from 'Query' to 'Search by resource UUID, name, backend ID, effective ID, IPs or hypervisor'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: creation_order
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - Modified property: plan_unit
                        - Property 'AllOf' changed
                          - Modified schema: #/components/schemas/BillingUnit
                            - New enum values: [quarter]
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - Modified property: plan_unit
                        - Property 'AllOf' changed
                          - Modified schema: #/components/schemas/BillingUnit
                            - New enum values: [quarter]
              - Modified property: plan_unit
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/BillingUnit
                    - New enum values: [quarter]

HEAD /api/marketplace-provider-resources/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'marketplace_provider_resources_head' to 'marketplace_provider_resources_count'
- Modified query param: query
  - Description changed from 'Query' to 'Search by resource UUID, name, backend ID, effective ID, IPs or hypervisor'

GET /api/marketplace-provider-resources/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: plan_unit
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BillingUnit
                          - New enum values: [quarter]
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: plan_unit
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BillingUnit
                          - New enum values: [quarter]
            - Modified property: plan_unit
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BillingUnit
                  - New enum values: [quarter]

GET /api/marketplace-provider-resources/{uuid}/details/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: plan_unit
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BillingUnit
                          - New enum values: [quarter]
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: plan_unit
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BillingUnit
                          - New enum values: [quarter]
            - Modified property: plan_unit
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BillingUnit
                  - New enum values: [quarter]

POST /api/marketplace-provider-resources/{uuid}/move_resource/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: plan_unit
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BillingUnit
                          - New enum values: [quarter]
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: plan_unit
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BillingUnit
                          - New enum values: [quarter]
            - Modified property: plan_unit
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BillingUnit
                  - New enum values: [quarter]

GET /api/marketplace-provider-resources/{uuid}/offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Properties changed
                  - Modified property: limit_period
                    - Property 'OneOf' changed
                      - Modified schema: #/components/schemas/LimitPeriodEnum
                        - New enum values: [quarterly]
            - Modified property: plans
              - Items changed
                - Properties changed
                  - Modified property: unit
                    - New enum values: [quarter]

POST /api/marketplace-provider-resources/{uuid}/set_end_date_by_provider/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: plan_unit
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BillingUnit
                          - New enum values: [quarter]
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: plan_unit
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BillingUnit
                          - New enum values: [quarter]
            - Modified property: plan_unit
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BillingUnit
                  - New enum values: [quarter]

GET /api/marketplace-public-offerings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: components
                - Items changed
                  - Properties changed
                    - Modified property: limit_period
                      - Property 'OneOf' changed
                        - Modified schema: #/components/schemas/LimitPeriodEnum
                          - New enum values: [quarterly]
              - Modified property: plans
                - Items changed
                  - Properties changed
                    - Modified property: unit
                      - New enum values: [quarter]

HEAD /api/marketplace-public-offerings/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'marketplace_public_offerings_head' to 'marketplace_public_offerings_count'

GET /api/marketplace-public-offerings/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Properties changed
                  - Modified property: limit_period
                    - Property 'OneOf' changed
                      - Modified schema: #/components/schemas/LimitPeriodEnum
                        - New enum values: [quarterly]
            - Modified property: plans
              - Items changed
                - Properties changed
                  - Modified property: unit
                    - New enum values: [quarter]

GET /api/marketplace-public-offerings/{uuid}/plans/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: unit
                - New enum values: [quarter]

GET /api/marketplace-public-offerings/{uuid}/plans/{plan_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: unit
              - New enum values: [quarter]

HEAD /api/marketplace-remote-synchronisations/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'marketplace_remote_synchronisations_head' to 'marketplace_remote_synchronisations_count'

HEAD /api/marketplace-resource-users/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'marketplace_resource_users_head' to 'marketplace_resource_users_count'

GET /api/marketplace-resources/

- Modified query param: query
  - Description changed from 'Query' to 'Search by resource UUID, name, backend ID, effective ID, IPs or hypervisor'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: creation_order
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - Modified property: plan_unit
                        - Property 'AllOf' changed
                          - Modified schema: #/components/schemas/BillingUnit
                            - New enum values: [quarter]
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - Modified property: plan_unit
                        - Property 'AllOf' changed
                          - Modified schema: #/components/schemas/BillingUnit
                            - New enum values: [quarter]
              - Modified property: plan_unit
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/BillingUnit
                    - New enum values: [quarter]

HEAD /api/marketplace-resources/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'marketplace_resources_head' to 'marketplace_resources_count'
- Modified query param: query
  - Description changed from 'Query' to 'Search by resource UUID, name, backend ID, effective ID, IPs or hypervisor'

GET /api/marketplace-resources/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: plan_unit
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BillingUnit
                          - New enum values: [quarter]
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: plan_unit
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BillingUnit
                          - New enum values: [quarter]
            - Modified property: plan_unit
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BillingUnit
                  - New enum values: [quarter]

GET /api/marketplace-resources/{uuid}/details/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: plan_unit
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BillingUnit
                          - New enum values: [quarter]
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: plan_unit
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BillingUnit
                          - New enum values: [quarter]
            - Modified property: plan_unit
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BillingUnit
                  - New enum values: [quarter]

POST /api/marketplace-resources/{uuid}/move_resource/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: plan_unit
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BillingUnit
                          - New enum values: [quarter]
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Modified property: plan_unit
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BillingUnit
                          - New enum values: [quarter]
            - Modified property: plan_unit
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BillingUnit
                  - New enum values: [quarter]

GET /api/marketplace-resources/{uuid}/offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Properties changed
                  - Modified property: limit_period
                    - Property 'OneOf' changed
                      - Modified schema: #/components/schemas/LimitPeriodEnum
                        - New enum values: [quarterly]
            - Modified property: plans
              - Items changed
                - Properties changed
                  - Modified property: unit
                    - New enum values: [quarter]

HEAD /api/marketplace-robot-accounts/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'marketplace_robot_accounts_head' to 'marketplace_robot_accounts_count'

HEAD /api/marketplace-screenshots/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'marketplace_screenshots_head' to 'marketplace_screenshots_count'

HEAD /api/marketplace-script-async-dry-run/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'marketplace_script_async_dry_run_head' to 'marketplace_script_async_dry_run_count'

POST /api/marketplace-script-dry-run/{uuid}/async_run/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Properties changed
                  - Modified property: limit_period
                    - Property 'OneOf' changed
                      - Modified schema: #/components/schemas/LimitPeriodEnum
                        - New enum values: [quarterly]
            - Modified property: plans
              - Items changed
                - Properties changed
                  - Modified property: unit
                    - New enum values: [quarter]

POST /api/marketplace-script-dry-run/{uuid}/run/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Properties changed
                  - Modified property: limit_period
                    - Property 'OneOf' changed
                      - Modified schema: #/components/schemas/LimitPeriodEnum
                        - New enum values: [quarterly]
            - Modified property: plans
              - Items changed
                - Properties changed
                  - Modified property: unit
                    - New enum values: [quarter]

HEAD /api/marketplace-sections/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'marketplace_sections_head' to 'marketplace_sections_count'

HEAD /api/marketplace-service-providers/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'marketplace_service_providers_head' to 'marketplace_service_providers_count'

GET /api/marketplace-service-providers/{service_provider_uuid}/customer_projects/

- Modified query param: query
  - Description changed from '' to 'Filter by name, UUID, backend ID or resource effective ID'

GET /api/marketplace-service-providers/{service_provider_uuid}/customers/

- Modified query param: query
  - Description changed from '' to 'Filter by name, native name, abbreviation, domain, UUID, registration code or agreement number'

GET /api/marketplace-service-providers/{service_provider_uuid}/offerings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: components
                - Items changed
                  - Properties changed
                    - Modified property: limit_period
                      - Property 'OneOf' changed
                        - Modified schema: #/components/schemas/LimitPeriodEnum
                          - New enum values: [quarterly]
              - Modified property: plans
                - Items changed
                  - Properties changed
                    - Modified property: unit
                      - New enum values: [quarter]

GET /api/marketplace-service-providers/{service_provider_uuid}/projects/

- Modified query param: query
  - Description changed from '' to 'Filter by name, UUID, backend ID or resource effective ID'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: end_date_requested_by
                - ReadOnly changed from false to true

GET /api/marketplace-service-providers/{service_provider_uuid}/user_customers/

- Modified query param: query
  - Description changed from '' to 'Filter by name, native name, abbreviation, domain, UUID, registration code or agreement number'

GET /api/marketplace-service-providers/{service_provider_uuid}/users/

- Modified query param: query
  - Description changed from '' to 'Filter by first name, last name, civil number, username or email'

HEAD /api/marketplace-stats/component_usages/

- Description changed from 'Return component usages for current month.' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'marketplace_stats_component_usages_head' to 'marketplace_stats_component_usages_count'

HEAD /api/marketplace-stats/component_usages_per_month/

- Description changed from 'Return component usages per month.' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'marketplace_stats_component_usages_per_month_head' to 'marketplace_stats_component_usages_per_month_count'

HEAD /api/marketplace-stats/component_usages_per_project/

- Description changed from 'Return component usages per project.' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'marketplace_stats_component_usages_per_project_head' to 'marketplace_stats_component_usages_per_project_count'

HEAD /api/marketplace-stats/count_active_resources_grouped_by_offering/

- Description changed from 'Count active resources grouped by offering.' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'marketplace_stats_count_active_resources_grouped_by_offering_head' to 'marketplace_stats_count_active_resources_grouped_by_offering_count'

HEAD /api/marketplace-stats/count_active_resources_grouped_by_offering_country/

- Description changed from 'Count active resources grouped by offering country.' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'marketplace_stats_count_active_resources_grouped_by_offering_country_head' to 'marketplace_stats_count_active_resources_grouped_by_offering_country_count'

HEAD /api/marketplace-stats/count_active_resources_grouped_by_organization_group/

- Description changed from 'Count active resources grouped by organization group.' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'marketplace_stats_count_active_resources_grouped_by_organization_group_head' to 'marketplace_stats_count_active_resources_grouped_by_organization_group_count'

HEAD /api/marketplace-stats/count_projects_grouped_by_provider_and_industry_flag/

- Description changed from 'Count projects grouped by provider and industry flag' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'marketplace_stats_count_projects_grouped_by_provider_and_industry_flag_head' to 'marketplace_stats_count_projects_grouped_by_provider_and_industry_flag_count'

HEAD /api/marketplace-stats/count_projects_grouped_by_provider_and_oecd/

- Description changed from 'Count projects grouped by provider and OECD code' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'marketplace_stats_count_projects_grouped_by_provider_and_oecd_head' to 'marketplace_stats_count_projects_grouped_by_provider_and_oecd_count'

HEAD /api/marketplace-stats/count_projects_of_service_providers/

- Description changed from 'Count projects of service providers.' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'marketplace_stats_count_projects_of_service_providers_head' to 'marketplace_stats_count_projects_of_service_providers_count'

HEAD /api/marketplace-stats/count_projects_of_service_providers_grouped_by_oecd/

- Description changed from 'Count projects of service providers grouped by OECD.' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'marketplace_stats_count_projects_of_service_providers_grouped_by_oecd_head' to 'marketplace_stats_count_projects_of_service_providers_grouped_by_oecd_count'

HEAD /api/marketplace-stats/count_unique_users_connected_with_active_resources_of_service_provider/

- Description changed from 'Count unique users connected with active resources of service provider.' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'marketplace_stats_count_unique_users_connected_with_active_resources_of_service_provider_head' to 'marketplace_stats_count_unique_users_connected_with_active_resources_of_service_provider_count'

HEAD /api/marketplace-stats/count_users_of_service_providers/

- Description changed from 'Count users of service providers.' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'marketplace_stats_count_users_of_service_providers_head' to 'marketplace_stats_count_users_of_service_providers_count'

HEAD /api/marketplace-stats/customer_member_count/

- Description changed from 'Return count of customer members.' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'marketplace_stats_customer_member_count_head' to 'marketplace_stats_customer_member_count_count'

HEAD /api/marketplace-stats/offerings_counter_stats/

- Description changed from 'Retrieve statistics about the number of offerings, grouped by category and service provider.' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'marketplace_stats_offerings_counter_stats_head' to 'marketplace_stats_offerings_counter_stats_count'

HEAD /api/marketplace-stats/organization_project_count/

- Description changed from 'Return project count per organization.' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'marketplace_stats_organization_project_count_head' to 'marketplace_stats_organization_project_count_count'

HEAD /api/marketplace-stats/organization_resource_count/

- Description changed from 'Return resource count per organization.' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'marketplace_stats_organization_resource_count_head' to 'marketplace_stats_organization_resource_count_count'

HEAD /api/marketplace-stats/projects_limits_grouped_by_industry_flag/

- Description changed from 'Group project limits by industry flag.' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'marketplace_stats_projects_limits_grouped_by_industry_flag_head' to 'marketplace_stats_projects_limits_grouped_by_industry_flag_count'

HEAD /api/marketplace-stats/projects_limits_grouped_by_oecd/

- Description changed from 'Group project limits by OECD code.' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'marketplace_stats_projects_limits_grouped_by_oecd_head' to 'marketplace_stats_projects_limits_grouped_by_oecd_count'

HEAD /api/marketplace-stats/projects_usages_grouped_by_industry_flag/

- Description changed from 'Group project usages by industry flag.' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'marketplace_stats_projects_usages_grouped_by_industry_flag_head' to 'marketplace_stats_projects_usages_grouped_by_industry_flag_count'

HEAD /api/marketplace-stats/projects_usages_grouped_by_oecd/

- Description changed from 'Group project usages by OECD code.' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'marketplace_stats_projects_usages_grouped_by_oecd_head' to 'marketplace_stats_projects_usages_grouped_by_oecd_count'

HEAD /api/marketplace-stats/resources_limits/

- Description changed from 'Return resources limits per offering.' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'marketplace_stats_resources_limits_head' to 'marketplace_stats_resources_limits_count'

HEAD /api/marketplace-stats/total_cost_of_active_resources_per_offering/

- Description changed from 'Total cost of active resources per offering.' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'marketplace_stats_total_cost_of_active_resources_per_offering_head' to 'marketplace_stats_total_cost_of_active_resources_per_offering_count'

HEAD /api/notification-messages-templates/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'notification_messages_templates_head' to 'notification_messages_templates_count'

GET /api/notification-messages/

- Modified query param: query
  - Description changed from '' to 'Filter by key or description'

HEAD /api/notification-messages/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'notification_messages_head' to 'notification_messages_count'
- Modified query param: query
  - Description changed from '' to 'Filter by key or description'

HEAD /api/openstack-backups/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'openstack_backups_head' to 'openstack_backups_count'

HEAD /api/openstack-flavors/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'openstack_flavors_head' to 'openstack_flavors_count'

HEAD /api/openstack-flavors/usage_stats/

- Description changed from '' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'openstack_flavors_usage_stats_head' to 'openstack_flavors_usage_stats_count'

HEAD /api/openstack-floating-ips/

- Description changed from 'Status *DOWN* means that floating IP is not linked to a VM, status *ACTIVE* means that it is in use.' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'openstack_floating_ips_head' to 'openstack_floating_ips_count'

HEAD /api/openstack-images/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'openstack_images_head' to 'openstack_images_count'

HEAD /api/openstack-images/usage_stats/

- Description changed from '' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'openstack_images_usage_stats_head' to 'openstack_images_usage_stats_count'

HEAD /api/openstack-instance-availability-zones/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'openstack_instance_availability_zones_head' to 'openstack_instance_availability_zones_count'

GET /api/openstack-instances/

- Modified query param: query
  - Description changed from '' to 'Search by name, internal IP, or external IP'

HEAD /api/openstack-instances/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'openstack_instances_head' to 'openstack_instances_count'
- Modified query param: query
  - Description changed from '' to 'Search by name, internal IP, or external IP'

HEAD /api/openstack-marketplace-tenants/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'openstack_marketplace_tenants_head' to 'openstack_marketplace_tenants_count'

HEAD /api/openstack-migrations/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'openstack_migrations_head' to 'openstack_migrations_count'

HEAD /api/openstack-network-rbac-policies/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'openstack_network_rbac_policies_head' to 'openstack_network_rbac_policies_count'

HEAD /api/openstack-networks/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'openstack_networks_head' to 'openstack_networks_count'

GET /api/openstack-ports/

- Modified query param: query
  - Description changed from 'Query' to 'Search by name, MAC address or backend ID'

HEAD /api/openstack-ports/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'openstack_ports_head' to 'openstack_ports_count'
- Modified query param: query
  - Description changed from 'Query' to 'Search by name, MAC address or backend ID'

HEAD /api/openstack-routers/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'openstack_routers_head' to 'openstack_routers_count'

GET /api/openstack-security-groups/

- Modified query param: query
  - Description changed from '' to 'Search by name or description'

HEAD /api/openstack-security-groups/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'openstack_security_groups_head' to 'openstack_security_groups_count'
- Modified query param: query
  - Description changed from '' to 'Search by name or description'

HEAD /api/openstack-server-groups/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'openstack_server_groups_head' to 'openstack_server_groups_count'

HEAD /api/openstack-snapshots/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'openstack_snapshots_head' to 'openstack_snapshots_count'

HEAD /api/openstack-subnets/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'openstack_subnets_head' to 'openstack_subnets_count'

HEAD /api/openstack-tenants/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'openstack_tenants_head' to 'openstack_tenants_count'

HEAD /api/openstack-volume-availability-zones/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'openstack_volume_availability_zones_head' to 'openstack_volume_availability_zones_count'

HEAD /api/openstack-volume-types/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'openstack_volume_types_head' to 'openstack_volume_types_count'

HEAD /api/openstack-volume-types/names/

- Description changed from 'Return a list of unique volume type names.' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'openstack_volume_types_names_head' to 'openstack_volume_types_names_count'

HEAD /api/openstack-volumes/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'openstack_volumes_head' to 'openstack_volumes_count'

HEAD /api/organization-groups/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'organization_groups_head' to 'organization_groups_count'

HEAD /api/payment-profiles/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'payment_profiles_head' to 'payment_profiles_count'

HEAD /api/payments/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'payments_head' to 'payments_count'

HEAD /api/project-credits/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'project_credits_head' to 'project_credits_count'

HEAD /api/project-quotas/

- Description changed from 'List project quotas.' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'project_quotas_head' to 'project_quotas_count'

HEAD /api/project-types/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'project_types_head' to 'project_types_count'

GET /api/projects/

- Modified query param: query
  - Description changed from '' to 'Filter by name, UUID, backend ID or resource effective ID'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: end_date_requested_by
                - ReadOnly changed from false to true

HEAD /api/projects/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'projects_head' to 'projects_count'
- Modified query param: query
  - Description changed from '' to 'Filter by name, UUID, backend ID or resource effective ID'

POST /api/projects/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Deleted property: end_date_requested_by
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: end_date_requested_by
              - ReadOnly changed from false to true

GET /api/projects/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: end_date_requested_by
              - ReadOnly changed from false to true

PATCH /api/projects/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: end_date_requested_by
              - ReadOnly changed from false to true

PUT /api/projects/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Deleted property: end_date_requested_by
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: end_date_requested_by
              - ReadOnly changed from false to true

POST /api/projects/{uuid}/move_project/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: end_date_requested_by
              - ReadOnly changed from false to true

GET /api/promotions-campaigns/

- Modified query param: query
  - Description changed from '' to 'Search by name or coupon code'

HEAD /api/promotions-campaigns/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'promotions_campaigns_head' to 'promotions_campaigns_count'
- Modified query param: query
  - Description changed from '' to 'Search by name or coupon code'

GET /api/promotions-campaigns/{uuid}/orders/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: plan_unit
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/BillingUnit
                    - New enum values: [quarter]

GET /api/promotions-campaigns/{uuid}/resources/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: creation_order
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - Modified property: plan_unit
                        - Property 'AllOf' changed
                          - Modified schema: #/components/schemas/BillingUnit
                            - New enum values: [quarter]
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - Modified property: plan_unit
                        - Property 'AllOf' changed
                          - Modified schema: #/components/schemas/BillingUnit
                            - New enum values: [quarter]
              - Modified property: plan_unit
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/BillingUnit
                    - New enum values: [quarter]

GET /api/proposal-proposals/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: can_submit
              - New required property: compliance_status
            - Properties changed
              - New property: can_submit
              - New property: compliance_status

HEAD /api/proposal-proposals/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'proposal_proposals_head' to 'proposal_proposals_count'

POST /api/proposal-proposals/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: can_submit
            - New required property: compliance_status
          - Properties changed
            - New property: can_submit
            - New property: compliance_status

GET /api/proposal-proposals/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: can_submit
            - New required property: compliance_status
          - Properties changed
            - New property: can_submit
            - New property: compliance_status

GET /api/proposal-proposals/{uuid}/resources/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: requested_offering
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/NestedRequestedOffering
                    - Properties changed
                      - Modified property: components
                        - Items changed
                          - Properties changed
                            - Modified property: limit_period
                              - Property 'OneOf' changed
                                - Modified schema: #/components/schemas/LimitPeriodEnum
                                  - New enum values: [quarterly]
                      - Modified property: plan_details
                        - Property 'AllOf' changed
                          - Modified schema: #/components/schemas/BasePublicPlan
                            - Properties changed
                              - Modified property: unit
                                - New enum values: [quarter]

POST /api/proposal-proposals/{uuid}/resources/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: requested_offering
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/NestedRequestedOffering
                  - Properties changed
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - Modified property: limit_period
                            - Property 'OneOf' changed
                              - Modified schema: #/components/schemas/LimitPeriodEnum
                                - New enum values: [quarterly]
                    - Modified property: plan_details
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BasePublicPlan
                          - Properties changed
                            - Modified property: unit
                              - New enum values: [quarter]

GET /api/proposal-proposals/{uuid}/resources/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: requested_offering
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/NestedRequestedOffering
                  - Properties changed
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - Modified property: limit_period
                            - Property 'OneOf' changed
                              - Modified schema: #/components/schemas/LimitPeriodEnum
                                - New enum values: [quarterly]
                    - Modified property: plan_details
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BasePublicPlan
                          - Properties changed
                            - Modified property: unit
                              - New enum values: [quarter]

PATCH /api/proposal-proposals/{uuid}/resources/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: requested_offering
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/NestedRequestedOffering
                  - Properties changed
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - Modified property: limit_period
                            - Property 'OneOf' changed
                              - Modified schema: #/components/schemas/LimitPeriodEnum
                                - New enum values: [quarterly]
                    - Modified property: plan_details
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BasePublicPlan
                          - Properties changed
                            - Modified property: unit
                              - New enum values: [quarter]

PUT /api/proposal-proposals/{uuid}/resources/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: requested_offering
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/NestedRequestedOffering
                  - Properties changed
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - Modified property: limit_period
                            - Property 'OneOf' changed
                              - Modified schema: #/components/schemas/LimitPeriodEnum
                                - New enum values: [quarterly]
                    - Modified property: plan_details
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BasePublicPlan
                          - Properties changed
                            - Modified property: unit
                              - New enum values: [quarter]

GET /api/proposal-protected-calls/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [compliance_checklist compliance_checklist_name]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: compliance_checklist
              - New property: compliance_checklist_name
              - Modified property: offerings
                - Items changed
                  - Properties changed
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - Modified property: limit_period
                            - Property 'OneOf' changed
                              - Modified schema: #/components/schemas/LimitPeriodEnum
                                - New enum values: [quarterly]
                    - Modified property: plan_details
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BasePublicPlan
                          - Properties changed
                            - Modified property: unit
                              - New enum values: [quarter]
              - Modified property: resource_templates
                - Items changed
                  - Properties changed
                    - Modified property: requested_offering_plan
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BasePublicPlan
                          - Properties changed
                            - Modified property: unit
                              - New enum values: [quarter]

HEAD /api/proposal-protected-calls/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'proposal_protected_calls_head' to 'proposal_protected_calls_count'

POST /api/proposal-protected-calls/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: compliance_checklist
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: compliance_checklist
            - New property: compliance_checklist_name
            - Modified property: offerings
              - Items changed
                - Properties changed
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - Modified property: limit_period
                          - Property 'OneOf' changed
                            - Modified schema: #/components/schemas/LimitPeriodEnum
                              - New enum values: [quarterly]
                  - Modified property: plan_details
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - Modified property: unit
                            - New enum values: [quarter]
            - Modified property: resource_templates
              - Items changed
                - Properties changed
                  - Modified property: requested_offering_plan
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - Modified property: unit
                            - New enum values: [quarter]

GET /api/proposal-protected-calls/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [compliance_checklist compliance_checklist_name]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: compliance_checklist
            - New property: compliance_checklist_name
            - Modified property: offerings
              - Items changed
                - Properties changed
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - Modified property: limit_period
                          - Property 'OneOf' changed
                            - Modified schema: #/components/schemas/LimitPeriodEnum
                              - New enum values: [quarterly]
                  - Modified property: plan_details
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - Modified property: unit
                            - New enum values: [quarter]
            - Modified property: resource_templates
              - Items changed
                - Properties changed
                  - Modified property: requested_offering_plan
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - Modified property: unit
                            - New enum values: [quarter]

PATCH /api/proposal-protected-calls/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: compliance_checklist
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: compliance_checklist
            - New property: compliance_checklist_name
            - Modified property: offerings
              - Items changed
                - Properties changed
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - Modified property: limit_period
                          - Property 'OneOf' changed
                            - Modified schema: #/components/schemas/LimitPeriodEnum
                              - New enum values: [quarterly]
                  - Modified property: plan_details
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - Modified property: unit
                            - New enum values: [quarter]
            - Modified property: resource_templates
              - Items changed
                - Properties changed
                  - Modified property: requested_offering_plan
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - Modified property: unit
                            - New enum values: [quarter]

PUT /api/proposal-protected-calls/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: compliance_checklist
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: compliance_checklist
            - New property: compliance_checklist_name
            - Modified property: offerings
              - Items changed
                - Properties changed
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - Modified property: limit_period
                          - Property 'OneOf' changed
                            - Modified schema: #/components/schemas/LimitPeriodEnum
                              - New enum values: [quarterly]
                  - Modified property: plan_details
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - Modified property: unit
                            - New enum values: [quarter]
            - Modified property: resource_templates
              - Items changed
                - Properties changed
                  - Modified property: requested_offering_plan
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - Modified property: unit
                            - New enum values: [quarter]

POST /api/proposal-protected-calls/{uuid}/activate/

- Responses changed
  - Modified response: 200
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

POST /api/proposal-protected-calls/{uuid}/archive/

- Responses changed
  - Modified response: 200
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

GET /api/proposal-protected-calls/{uuid}/offerings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: components
                - Items changed
                  - Properties changed
                    - Modified property: limit_period
                      - Property 'OneOf' changed
                        - Modified schema: #/components/schemas/LimitPeriodEnum
                          - New enum values: [quarterly]
              - Modified property: plan_details
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/BasePublicPlan
                    - Properties changed
                      - Modified property: unit
                        - New enum values: [quarter]

POST /api/proposal-protected-calls/{uuid}/offerings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Properties changed
                  - Modified property: limit_period
                    - Property 'OneOf' changed
                      - Modified schema: #/components/schemas/LimitPeriodEnum
                        - New enum values: [quarterly]
            - Modified property: plan_details
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BasePublicPlan
                  - Properties changed
                    - Modified property: unit
                      - New enum values: [quarter]

GET /api/proposal-protected-calls/{uuid}/offerings/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Properties changed
                  - Modified property: limit_period
                    - Property 'OneOf' changed
                      - Modified schema: #/components/schemas/LimitPeriodEnum
                        - New enum values: [quarterly]
            - Modified property: plan_details
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BasePublicPlan
                  - Properties changed
                    - Modified property: unit
                      - New enum values: [quarter]

PATCH /api/proposal-protected-calls/{uuid}/offerings/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Properties changed
                  - Modified property: limit_period
                    - Property 'OneOf' changed
                      - Modified schema: #/components/schemas/LimitPeriodEnum
                        - New enum values: [quarterly]
            - Modified property: plan_details
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BasePublicPlan
                  - Properties changed
                    - Modified property: unit
                      - New enum values: [quarter]

PUT /api/proposal-protected-calls/{uuid}/offerings/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Properties changed
                  - Modified property: limit_period
                    - Property 'OneOf' changed
                      - Modified schema: #/components/schemas/LimitPeriodEnum
                        - New enum values: [quarterly]
            - Modified property: plan_details
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BasePublicPlan
                  - Properties changed
                    - Modified property: unit
                      - New enum values: [quarter]

GET /api/proposal-protected-calls/{uuid}/resource_templates/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: requested_offering_plan
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/BasePublicPlan
                    - Properties changed
                      - Modified property: unit
                        - New enum values: [quarter]

POST /api/proposal-protected-calls/{uuid}/resource_templates/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: requested_offering_plan
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BasePublicPlan
                  - Properties changed
                    - Modified property: unit
                      - New enum values: [quarter]

GET /api/proposal-protected-calls/{uuid}/resource_templates/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: requested_offering_plan
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BasePublicPlan
                  - Properties changed
                    - Modified property: unit
                      - New enum values: [quarter]

PATCH /api/proposal-protected-calls/{uuid}/resource_templates/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: requested_offering_plan
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BasePublicPlan
                  - Properties changed
                    - Modified property: unit
                      - New enum values: [quarter]

PUT /api/proposal-protected-calls/{uuid}/resource_templates/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: requested_offering_plan
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BasePublicPlan
                  - Properties changed
                    - Modified property: unit
                      - New enum values: [quarter]

POST /api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/close/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: compliance_checklist
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: compliance_checklist
            - New property: compliance_checklist_name
            - Modified property: offerings
              - Items changed
                - Properties changed
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - Modified property: limit_period
                          - Property 'OneOf' changed
                            - Modified schema: #/components/schemas/LimitPeriodEnum
                              - New enum values: [quarterly]
                  - Modified property: plan_details
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - Modified property: unit
                            - New enum values: [quarter]
            - Modified property: resource_templates
              - Items changed
                - Properties changed
                  - Modified property: requested_offering_plan
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - Modified property: unit
                            - New enum values: [quarter]

GET /api/proposal-public-calls/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: offerings
                - Items changed
                  - Properties changed
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - Modified property: limit_period
                            - Property 'OneOf' changed
                              - Modified schema: #/components/schemas/LimitPeriodEnum
                                - New enum values: [quarterly]
                    - Modified property: plan_details
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BasePublicPlan
                          - Properties changed
                            - Modified property: unit
                              - New enum values: [quarter]
              - Modified property: resource_templates
                - Items changed
                  - Properties changed
                    - Modified property: requested_offering_plan
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BasePublicPlan
                          - Properties changed
                            - Modified property: unit
                              - New enum values: [quarter]

HEAD /api/proposal-public-calls/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'proposal_public_calls_head' to 'proposal_public_calls_count'

GET /api/proposal-public-calls/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: offerings
              - Items changed
                - Properties changed
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - Modified property: limit_period
                          - Property 'OneOf' changed
                            - Modified schema: #/components/schemas/LimitPeriodEnum
                              - New enum values: [quarterly]
                  - Modified property: plan_details
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - Modified property: unit
                            - New enum values: [quarter]
            - Modified property: resource_templates
              - Items changed
                - Properties changed
                  - Modified property: requested_offering_plan
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - Modified property: unit
                            - New enum values: [quarter]

GET /api/proposal-requested-offerings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: components
                - Items changed
                  - Properties changed
                    - Modified property: limit_period
                      - Property 'OneOf' changed
                        - Modified schema: #/components/schemas/LimitPeriodEnum
                          - New enum values: [quarterly]
              - Modified property: plan_details
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/BasePublicPlan
                    - Properties changed
                      - Modified property: unit
                        - New enum values: [quarter]

HEAD /api/proposal-requested-offerings/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'proposal_requested_offerings_head' to 'proposal_requested_offerings_count'

GET /api/proposal-requested-offerings/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Properties changed
                  - Modified property: limit_period
                    - Property 'OneOf' changed
                      - Modified schema: #/components/schemas/LimitPeriodEnum
                        - New enum values: [quarterly]
            - Modified property: plan_details
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BasePublicPlan
                  - Properties changed
                    - Modified property: unit
                      - New enum values: [quarter]

GET /api/proposal-requested-resources/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: requested_offering
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/NestedRequestedOffering
                    - Properties changed
                      - Modified property: components
                        - Items changed
                          - Properties changed
                            - Modified property: limit_period
                              - Property 'OneOf' changed
                                - Modified schema: #/components/schemas/LimitPeriodEnum
                                  - New enum values: [quarterly]
                      - Modified property: plan_details
                        - Property 'AllOf' changed
                          - Modified schema: #/components/schemas/BasePublicPlan
                            - Properties changed
                              - Modified property: unit
                                - New enum values: [quarter]

HEAD /api/proposal-requested-resources/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'proposal_requested_resources_head' to 'proposal_requested_resources_count'

GET /api/proposal-requested-resources/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: requested_offering
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/NestedRequestedOffering
                  - Properties changed
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - Modified property: limit_period
                            - Property 'OneOf' changed
                              - Modified schema: #/components/schemas/LimitPeriodEnum
                                - New enum values: [quarterly]
                    - Modified property: plan_details
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BasePublicPlan
                          - Properties changed
                            - Modified property: unit
                              - New enum values: [quarter]

HEAD /api/proposal-reviews/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'proposal_reviews_head' to 'proposal_reviews_count'

GET /api/provider-invoice-items/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: unit
                - New enum values: [quarter]

HEAD /api/provider-invoice-items/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'provider_invoice_items_head' to 'provider_invoice_items_count'

GET /api/provider-invoice-items/{id}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: unit
              - New enum values: [quarter]

HEAD /api/rancher-apps/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'rancher_apps_head' to 'rancher_apps_count'

HEAD /api/rancher-catalogs/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'rancher_catalogs_head' to 'rancher_catalogs_count'

HEAD /api/rancher-cluster-security-groups/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'rancher_cluster_security_groups_head' to 'rancher_cluster_security_groups_count'

HEAD /api/rancher-cluster-templates/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'rancher_cluster_templates_head' to 'rancher_cluster_templates_count'

HEAD /api/rancher-clusters/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'rancher_clusters_head' to 'rancher_clusters_count'

HEAD /api/rancher-hpas/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'rancher_hpas_head' to 'rancher_hpas_count'

HEAD /api/rancher-ingresses/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'rancher_ingresses_head' to 'rancher_ingresses_count'

HEAD /api/rancher-namespaces/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'rancher_namespaces_head' to 'rancher_namespaces_count'

HEAD /api/rancher-nodes/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'rancher_nodes_head' to 'rancher_nodes_count'

HEAD /api/rancher-projects/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'rancher_projects_head' to 'rancher_projects_count'

HEAD /api/rancher-role-templates/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'rancher_role_templates_head' to 'rancher_role_templates_count'

HEAD /api/rancher-services/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'rancher_services_head' to 'rancher_services_count'

HEAD /api/rancher-templates/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'rancher_templates_head' to 'rancher_templates_count'

HEAD /api/rancher-users/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'rancher_users_head' to 'rancher_users_count'

HEAD /api/rancher-workloads/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'rancher_workloads_head' to 'rancher_workloads_count'

HEAD /api/roles/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'roles_head' to 'roles_count'

HEAD /api/service-settings/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'service_settings_head' to 'service_settings_count'

HEAD /api/slurm-allocation-user-usage/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'slurm_allocation_user_usage_head' to 'slurm_allocation_user_usage_count'

HEAD /api/slurm-allocations/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'slurm_allocations_head' to 'slurm_allocations_count'

HEAD /api/slurm-associations/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'slurm_associations_head' to 'slurm_associations_count'

HEAD /api/slurm-jobs/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'slurm_jobs_head' to 'slurm_jobs_count'

HEAD /api/support-attachments/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'support_attachments_head' to 'support_attachments_count'

HEAD /api/support-comments/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'support_comments_head' to 'support_comments_count'

HEAD /api/support-feedbacks/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'support_feedbacks_head' to 'support_feedbacks_count'

HEAD /api/support-issues/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'support_issues_head' to 'support_issues_count'

HEAD /api/support-priorities/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'support_priorities_head' to 'support_priorities_count'

HEAD /api/support-templates/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'support_templates_head' to 'support_templates_count'

HEAD /api/support-users/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'support_users_head' to 'support_users_count'

HEAD /api/user-agreements/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'user_agreements_head' to 'user_agreements_count'

HEAD /api/user-group-invitations/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'user_group_invitations_head' to 'user_group_invitations_count'

HEAD /api/user-invitations/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'user_invitations_head' to 'user_invitations_count'

HEAD /api/user-permission-requests/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'user_permission_requests_head' to 'user_permission_requests_count'

HEAD /api/user-permissions/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'user_permissions_head' to 'user_permissions_count'

GET /api/users/

- Modified query param: query
  - Description changed from '' to 'Filter by first name, last name, civil number, username or email'

HEAD /api/users/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'users_head' to 'users_count'
- Modified query param: query
  - Description changed from '' to 'Filter by first name, last name, civil number, username or email'

HEAD /api/users/me/

- Description changed from 'Get current user details, including authentication token.' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'users_me_head' to 'users_me_count'

HEAD /api/vmware-clusters/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'vmware_clusters_head' to 'vmware_clusters_count'

HEAD /api/vmware-datastores/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'vmware_datastores_head' to 'vmware_datastores_count'

HEAD /api/vmware-disks/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'vmware_disks_head' to 'vmware_disks_count'

HEAD /api/vmware-folders/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'vmware_folders_head' to 'vmware_folders_count'

HEAD /api/vmware-networks/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'vmware_networks_head' to 'vmware_networks_count'

HEAD /api/vmware-ports/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'vmware_ports_head' to 'vmware_ports_count'

HEAD /api/vmware-templates/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'vmware_templates_head' to 'vmware_templates_count'

HEAD /api/vmware-virtual-machine/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get number of items in the collection matching the request parameters.'
- OperationID changed from 'vmware_virtual_machine_head' to 'vmware_virtual_machine_count'

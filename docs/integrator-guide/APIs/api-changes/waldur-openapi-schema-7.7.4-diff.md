# OpenAPI schema diff - 7.7.4

## For version 7.7.4

### New Endpoints: 221

----------------------
HEAD /api/access-subnets/  
HEAD /api/admin-announcements/  
HEAD /api/auth-tokens/  
HEAD /api/autoprovisioning-rules/  
HEAD /api/aws-images/  
HEAD /api/aws-instances/  
HEAD /api/aws-regions/  
HEAD /api/aws-sizes/  
HEAD /api/aws-volumes/  
HEAD /api/azure-images/  
HEAD /api/azure-locations/  
HEAD /api/azure-public-ips/  
HEAD /api/azure-resource-groups/  
HEAD /api/azure-sizes/  
HEAD /api/azure-sql-databases/  
HEAD /api/azure-sql-servers/  
HEAD /api/azure-virtualmachines/  
HEAD /api/backend-resource-requests/  
HEAD /api/backend-resources/  
HEAD /api/booking-offerings/  
HEAD /api/booking-resources/  
HEAD /api/broadcast-message-templates/  
HEAD /api/broadcast-messages/  
HEAD /api/broadcast-messages/recipients/  
HEAD /api/call-managing-organisations/  
HEAD /api/call-proposal-project-role-mappings/  
HEAD /api/call-rounds/  
HEAD /api/component-user-usage-limits/  
HEAD /api/customer-credits/  
HEAD /api/customer-permissions-reviews/  
HEAD /api/customer-quotas/  
HEAD /api/customers/  
HEAD /api/customers/countries/  
HEAD /api/digitalocean-droplets/  
HEAD /api/digitalocean-images/  
HEAD /api/digitalocean-regions/  
HEAD /api/digitalocean-sizes/  
HEAD /api/email-logs/  
HEAD /api/event-subscriptions/  
HEAD /api/events-stats/  
HEAD /api/events/  
HEAD /api/events/count/  
HEAD /api/events/event_groups/  
HEAD /api/events/scope_types/  
HEAD /api/financial-reports/  
HEAD /api/freeipa-profiles/  
HEAD /api/google-auth/  
HEAD /api/google-auth/callback/  
HEAD /api/hooks-email/  
HEAD /api/hooks-web/  
HEAD /api/hooks/  
HEAD /api/identity-providers/  
HEAD /api/invoice-items/  
HEAD /api/invoice-items/costs/  
HEAD /api/invoice-items/customer_costs_for_period/  
HEAD /api/invoice-items/project_costs_for_period/  
HEAD /api/invoice-items/total_price/  
HEAD /api/invoices/  
HEAD /api/invoices/growth/  
HEAD /api/keycloak-groups/  
HEAD /api/keycloak-user-group-memberships/  
HEAD /api/keys/  
HEAD /api/lexis-links/  
HEAD /api/marketplace-categories/  
HEAD /api/marketplace-category-columns/  
HEAD /api/marketplace-category-component-usages/  
HEAD /api/marketplace-category-components/  
HEAD /api/marketplace-category-groups/  
HEAD /api/marketplace-category-help-articles/  
HEAD /api/marketplace-checklists-admin-question-dependencies/  
HEAD /api/marketplace-checklists-admin-question-options/  
HEAD /api/marketplace-checklists-admin-questions/  
HEAD /api/marketplace-checklists-admin/  
HEAD /api/marketplace-checklists/  
HEAD /api/marketplace-component-usages/  
HEAD /api/marketplace-component-user-usages/  
HEAD /api/marketplace-customer-estimated-cost-policies/  
HEAD /api/marketplace-customer-estimated-cost-policies/actions/  
HEAD /api/marketplace-customer-service-accounts/  
HEAD /api/marketplace-integration-statuses/  
HEAD /api/marketplace-maintenance-announcement-offerings/  
HEAD /api/marketplace-maintenance-announcement-template-offerings/  
HEAD /api/marketplace-maintenance-announcements-template/  
HEAD /api/marketplace-maintenance-announcements/  
HEAD /api/marketplace-offering-estimated-cost-policies/  
HEAD /api/marketplace-offering-estimated-cost-policies/actions/  
HEAD /api/marketplace-offering-files/  
HEAD /api/marketplace-offering-permissions-log/  
HEAD /api/marketplace-offering-permissions/  
HEAD /api/marketplace-offering-referrals/  
HEAD /api/marketplace-offering-usage-policies/  
HEAD /api/marketplace-offering-usage-policies/actions/  
HEAD /api/marketplace-offering-user-roles/  
HEAD /api/marketplace-offering-users/  
POST /api/marketplace-offering-users/{uuid}/begin_creating/  
POST /api/marketplace-offering-users/{uuid}/set_ok/  
HEAD /api/marketplace-orders/  
HEAD /api/marketplace-plan-components/  
HEAD /api/marketplace-plans/  
HEAD /api/marketplace-plans/usage_stats/  
HEAD /api/marketplace-project-estimated-cost-policies/  
HEAD /api/marketplace-project-estimated-cost-policies/actions/  
HEAD /api/marketplace-project-service-accounts/  
HEAD /api/marketplace-project-update-requests/  
HEAD /api/marketplace-provider-offerings/  
HEAD /api/marketplace-provider-offerings/groups/  
HEAD /api/marketplace-provider-resources/  
HEAD /api/marketplace-public-offerings/  
HEAD /api/marketplace-remote-synchronisations/  
HEAD /api/marketplace-resource-users/  
HEAD /api/marketplace-resources/  
HEAD /api/marketplace-robot-accounts/  
HEAD /api/marketplace-screenshots/  
HEAD /api/marketplace-script-async-dry-run/  
HEAD /api/marketplace-sections/  
HEAD /api/marketplace-service-providers/  
HEAD /api/marketplace-stats/component_usages/  
HEAD /api/marketplace-stats/component_usages_per_month/  
HEAD /api/marketplace-stats/component_usages_per_project/  
HEAD /api/marketplace-stats/count_active_resources_grouped_by_offering/  
HEAD /api/marketplace-stats/count_active_resources_grouped_by_offering_country/  
HEAD /api/marketplace-stats/count_active_resources_grouped_by_organization_group/  
HEAD /api/marketplace-stats/count_projects_grouped_by_provider_and_industry_flag/  
HEAD /api/marketplace-stats/count_projects_grouped_by_provider_and_oecd/  
HEAD /api/marketplace-stats/count_projects_of_service_providers/  
HEAD /api/marketplace-stats/count_projects_of_service_providers_grouped_by_oecd/  
HEAD /api/marketplace-stats/count_unique_users_connected_with_active_resources_of_service_provider/  
HEAD /api/marketplace-stats/count_users_of_service_providers/  
HEAD /api/marketplace-stats/customer_member_count/  
HEAD /api/marketplace-stats/offerings_counter_stats/  
HEAD /api/marketplace-stats/organization_project_count/  
HEAD /api/marketplace-stats/organization_resource_count/  
HEAD /api/marketplace-stats/projects_limits_grouped_by_industry_flag/  
HEAD /api/marketplace-stats/projects_limits_grouped_by_oecd/  
HEAD /api/marketplace-stats/projects_usages_grouped_by_industry_flag/  
HEAD /api/marketplace-stats/projects_usages_grouped_by_oecd/  
HEAD /api/marketplace-stats/resources_limits/  
HEAD /api/marketplace-stats/total_cost_of_active_resources_per_offering/  
HEAD /api/notification-messages-templates/  
HEAD /api/notification-messages/  
HEAD /api/openstack-backups/  
HEAD /api/openstack-flavors/  
HEAD /api/openstack-flavors/usage_stats/  
HEAD /api/openstack-floating-ips/  
HEAD /api/openstack-images/  
HEAD /api/openstack-images/usage_stats/  
HEAD /api/openstack-instance-availability-zones/  
HEAD /api/openstack-instances/  
HEAD /api/openstack-marketplace-tenants/  
HEAD /api/openstack-migrations/  
HEAD /api/openstack-network-rbac-policies/  
HEAD /api/openstack-networks/  
HEAD /api/openstack-ports/  
HEAD /api/openstack-routers/  
HEAD /api/openstack-security-groups/  
HEAD /api/openstack-server-groups/  
HEAD /api/openstack-snapshots/  
HEAD /api/openstack-subnets/  
HEAD /api/openstack-tenants/  
HEAD /api/openstack-volume-availability-zones/  
HEAD /api/openstack-volume-types/  
HEAD /api/openstack-volume-types/names/  
HEAD /api/openstack-volumes/  
HEAD /api/organization-groups/  
HEAD /api/payment-profiles/  
HEAD /api/payments/  
HEAD /api/project-credits/  
HEAD /api/project-quotas/  
HEAD /api/project-types/  
HEAD /api/projects/  
HEAD /api/promotions-campaigns/  
HEAD /api/proposal-proposals/  
HEAD /api/proposal-protected-calls/  
HEAD /api/proposal-public-calls/  
HEAD /api/proposal-requested-offerings/  
HEAD /api/proposal-requested-resources/  
HEAD /api/proposal-reviews/  
HEAD /api/provider-invoice-items/  
HEAD /api/rancher-apps/  
HEAD /api/rancher-catalogs/  
HEAD /api/rancher-cluster-security-groups/  
HEAD /api/rancher-cluster-templates/  
HEAD /api/rancher-clusters/  
HEAD /api/rancher-hpas/  
HEAD /api/rancher-ingresses/  
HEAD /api/rancher-namespaces/  
HEAD /api/rancher-nodes/  
HEAD /api/rancher-projects/  
HEAD /api/rancher-role-templates/  
HEAD /api/rancher-services/  
HEAD /api/rancher-templates/  
HEAD /api/rancher-users/  
HEAD /api/rancher-workloads/  
HEAD /api/roles/  
HEAD /api/service-settings/  
HEAD /api/slurm-allocation-user-usage/  
HEAD /api/slurm-allocations/  
HEAD /api/slurm-associations/  
HEAD /api/slurm-jobs/  
HEAD /api/support-attachments/  
HEAD /api/support-comments/  
HEAD /api/support-feedbacks/  
HEAD /api/support-issues/  
HEAD /api/support-priorities/  
HEAD /api/support-templates/  
HEAD /api/support-users/  
HEAD /api/user-agreements/  
HEAD /api/user-group-invitations/  
HEAD /api/user-invitations/  
HEAD /api/user-permission-requests/  
HEAD /api/user-permissions/  
HEAD /api/users/  
HEAD /api/users/me/  
HEAD /api/vmware-clusters/  
HEAD /api/vmware-datastores/  
HEAD /api/vmware-disks/  
HEAD /api/vmware-folders/  
HEAD /api/vmware-networks/  
HEAD /api/vmware-ports/  
HEAD /api/vmware-templates/  
HEAD /api/vmware-virtual-machine/  

### Deleted Endpoints: None

---------------------------

### Modified Endpoints: 371

---------------------------
GET /api-auth/saml2/providers/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/access-subnets/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

DELETE /api/access-subnets/{uuid}/

- Extensions changed
  - New extension: x-permissions

PATCH /api/access-subnets/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/access-subnets/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/admin-announcements/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/auth-tokens/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/autoprovisioning-rules/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/aws-images/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/aws-instances/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/aws-regions/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/aws-sizes/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/aws-volumes/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/azure-images/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/azure-locations/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/azure-public-ips/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/azure-resource-groups/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/azure-sizes/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/azure-sql-databases/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/azure-sql-servers/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/azure-virtualmachines/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/backend-resource-requests/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: uuid
            - Properties changed
              - New property: uuid
    - Headers changed
      - New header: x-result-count

POST /api/backend-resource-requests/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: uuid
          - Properties changed
            - New property: uuid

GET /api/backend-resource-requests/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: uuid
          - Properties changed
            - New property: uuid

POST /api/backend-resource-requests/{uuid}/set_done/

- Extensions changed
  - New extension: x-permissions

POST /api/backend-resource-requests/{uuid}/set_erred/

- Extensions changed
  - New extension: x-permissions

POST /api/backend-resource-requests/{uuid}/start_processing/

- Extensions changed
  - New extension: x-permissions

GET /api/backend-resources/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

DELETE /api/backend-resources/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/backend-resources/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/booking-offerings/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/booking-resources/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

POST /api/booking-resources/{uuid}/accept/

- Extensions changed
  - New extension: x-permissions

GET /api/broadcast-message-templates/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/broadcast-messages/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/call-managing-organisations/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/call-managing-organisations/{uuid}/list_users/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/call-proposal-project-role-mappings/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/call-rounds/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/call-rounds/{uuid}/reviewers/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/component-user-usage-limits/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

DELETE /api/component-user-usage-limits/{uuid}/

- Extensions changed
  - New extension: x-permissions

PATCH /api/component-user-usage-limits/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/component-user-usage-limits/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/customer-credits/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/customer-credits/{uuid}/consumptions/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/customer-permissions-reviews/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/customer-quotas/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/customers/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/customers/countries/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/customers/{uuid}/list_users/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/customers/{uuid}/users/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/database-stats/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/digitalocean-droplets/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/digitalocean-images/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/digitalocean-regions/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/digitalocean-sizes/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/email-logs/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/event-subscriptions/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/events-stats/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/events/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/financial-reports/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/freeipa-profiles/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/google-auth/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/hooks-email/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/hooks-web/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/identity-providers/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/invoice-items/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/invoice-items/costs/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/invoices/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/invoices/{uuid}/stats/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/keycloak-groups/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/keycloak-user-group-memberships/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/keys/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/lexis-links/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

POST /api/lexis-links/

- Extensions changed
  - New extension: x-permissions

DELETE /api/lexis-links/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-bookings/{uuid}/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-categories/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-category-columns/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-category-component-usages/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-category-components/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-category-groups/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-category-help-articles/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-checklists-admin-question-dependencies/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-checklists-admin-question-options/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-checklists-admin-questions/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-checklists-admin/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-checklists-categories/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-checklists-categories/{category_uuid}/checklists/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-checklists/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-checklists/{checklist_uuid}/answers/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-checklists/{checklist_uuid}/stats/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-checklists/{checklist_uuid}/user/{user_uuid}/answers/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-checklists/{uuid}/questions/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-component-usages/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

POST /api/marketplace-component-usages/{uuid}/set_user_usage/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-component-user-usages/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-customer-estimated-cost-policies/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-customer-service-accounts/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

DELETE /api/marketplace-customer-service-accounts/{uuid}/

- Extensions changed
  - New extension: x-permissions

PATCH /api/marketplace-customer-service-accounts/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/marketplace-customer-service-accounts/{uuid}/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-customer-service-accounts/{uuid}/rotate_api_key/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-integration-statuses/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-maintenance-announcement-offerings/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-maintenance-announcement-template-offerings/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-maintenance-announcements-template/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-maintenance-announcements/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-offering-estimated-cost-policies/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-offering-files/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-offering-permissions-log/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-offering-permissions/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-offering-referrals/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-offering-usage-policies/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-offering-user-roles/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-offering-users/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [user_email]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: user_email
    - Headers changed
      - New header: x-result-count

POST /api/marketplace-offering-users/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: user_email

GET /api/marketplace-offering-users/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [user_email]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: user_email

PATCH /api/marketplace-offering-users/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: user_email

PUT /api/marketplace-offering-users/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: user_email

POST /api/marketplace-offering-users/{uuid}/set_pending_account_linking/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-offering-users/{uuid}/set_pending_additional_validation/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-offering-users/{uuid}/set_validation_complete/

- Extensions changed
  - New extension: x-permissions
- Request body changed

GET /api/marketplace-orders/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

DELETE /api/marketplace-orders/{uuid}/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-orders/{uuid}/approve_by_consumer/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-orders/{uuid}/approve_by_provider/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-orders/{uuid}/cancel/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-orders/{uuid}/reject_by_provider/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-orders/{uuid}/set_state_done/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-orders/{uuid}/set_state_erred/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-orders/{uuid}/set_state_executing/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-plan-components/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-plans/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-plans/usage_stats/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

PATCH /api/marketplace-plans/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/marketplace-plans/{uuid}/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-plans/{uuid}/archive/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-plans/{uuid}/delete_organization_groups/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-plans/{uuid}/update_organization_groups/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-plans/{uuid}/update_prices/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-plans/{uuid}/update_quotas/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-plugins/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-project-estimated-cost-policies/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-project-service-accounts/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

DELETE /api/marketplace-project-service-accounts/{uuid}/

- Extensions changed
  - New extension: x-permissions

PATCH /api/marketplace-project-service-accounts/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/marketplace-project-service-accounts/{uuid}/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-project-service-accounts/{uuid}/rotate_api_key/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-project-update-requests/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-provider-offerings/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-provider-offerings/groups/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

DELETE /api/marketplace-provider-offerings/{uuid}/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-provider-offerings/{uuid}/add_endpoint/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-provider-offerings/{uuid}/archive/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-provider-offerings/{uuid}/component_stats/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-provider-offerings/{uuid}/costs/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

POST /api/marketplace-provider-offerings/{uuid}/create_offering_component/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-provider-offerings/{uuid}/customers/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

POST /api/marketplace-provider-offerings/{uuid}/delete_endpoint/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-provider-offerings/{uuid}/importable_resources/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-provider-offerings/{uuid}/list_customer_projects/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-provider-offerings/{uuid}/list_customer_users/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: permissions
                - Items changed
                  - Properties changed
                    - Modified property: scope_type
                      - Nullable changed from false to true
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-provider-offerings/{uuid}/list_users/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-provider-offerings/{uuid}/orders/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

POST /api/marketplace-provider-offerings/{uuid}/pause/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-provider-offerings/{uuid}/refresh_offering_usernames/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-provider-offerings/{uuid}/remove_offering_component/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-provider-offerings/{uuid}/set_backend_metadata/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-provider-offerings/{uuid}/sync/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-provider-offerings/{uuid}/unpause/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-provider-offerings/{uuid}/update_attributes/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-provider-offerings/{uuid}/update_description/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-provider-offerings/{uuid}/update_integration/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-provider-offerings/{uuid}/update_location/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-provider-offerings/{uuid}/update_offering_component/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-provider-offerings/{uuid}/update_options/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-provider-offerings/{uuid}/update_resource_options/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-provider-resources/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-provider-resources/{uuid}/offering_for_subresources/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-provider-resources/{uuid}/plan_periods/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

POST /api/marketplace-provider-resources/{uuid}/refresh_last_sync/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-provider-resources/{uuid}/set_as_erred/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-provider-resources/{uuid}/set_backend_id/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-provider-resources/{uuid}/set_backend_metadata/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-provider-resources/{uuid}/submit_report/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-provider-resources/{uuid}/team/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

POST /api/marketplace-provider-resources/{uuid}/terminate/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-public-offerings/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-public-offerings/{uuid}/plans/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-related-customers/{customer_uuid}/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-remote-synchronisations/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-resource-offerings/{category_uuid}/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-resource-users/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-resources/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-resources/{uuid}/offering_for_subresources/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-resources/{uuid}/plan_periods/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

POST /api/marketplace-resources/{uuid}/switch_plan/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-resources/{uuid}/team/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

POST /api/marketplace-resources/{uuid}/terminate/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-resources/{uuid}/update_limits/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-resources/{uuid}/update_options/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-robot-accounts/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

DELETE /api/marketplace-robot-accounts/{uuid}/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-robot-accounts/{uuid}/set_state_creating/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-robot-accounts/{uuid}/set_state_deleted/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-robot-accounts/{uuid}/set_state_erred/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-robot-accounts/{uuid}/set_state_ok/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-robot-accounts/{uuid}/set_state_request_deletion/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-runtime-states/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-screenshots/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

DELETE /api/marketplace-screenshots/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-script-async-dry-run/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

POST /api/marketplace-script-dry-run/{uuid}/async_run/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-script-dry-run/{uuid}/run/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-sections/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-service-providers/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-service-providers/{service_provider_uuid}/customer_projects/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-service-providers/{service_provider_uuid}/customers/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-service-providers/{service_provider_uuid}/keys/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-service-providers/{service_provider_uuid}/offerings/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-service-providers/{service_provider_uuid}/project_permissions/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-service-providers/{service_provider_uuid}/projects/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-service-providers/{service_provider_uuid}/user_customers/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-service-providers/{service_provider_uuid}/users/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-service-providers/{uuid}/list_users/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-service-providers/{uuid}/revenue/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-service-providers/{uuid}/robot_account_customers/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-service-providers/{uuid}/robot_account_projects/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

POST /api/marketplace-service-providers/{uuid}/set_offerings_username/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-service-providers/{uuid}/stat/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-stats/component_usages/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-stats/component_usages_per_month/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-stats/component_usages_per_project/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-stats/count_active_resources_grouped_by_offering/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-stats/count_active_resources_grouped_by_offering_country/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-stats/count_active_resources_grouped_by_organization_group/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-stats/count_projects_grouped_by_provider_and_industry_flag/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-stats/count_projects_grouped_by_provider_and_oecd/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-stats/count_projects_of_service_providers/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-stats/count_projects_of_service_providers_grouped_by_oecd/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-stats/count_unique_users_connected_with_active_resources_of_service_provider/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-stats/count_users_of_service_providers/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-stats/customer_member_count/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-stats/offerings_counter_stats/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-stats/organization_project_count/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-stats/organization_resource_count/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-stats/resources_limits/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-stats/total_cost_of_active_resources_per_offering/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/notification-messages-templates/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/notification-messages/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/openstack-backups/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/openstack-flavors/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/openstack-floating-ips/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/openstack-images/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/openstack-instance-availability-zones/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/openstack-instances/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/openstack-instances/{uuid}/floating_ips/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/openstack-instances/{uuid}/ports/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/openstack-marketplace-tenants/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/openstack-migrations/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/openstack-network-rbac-policies/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/openstack-networks/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/openstack-ports/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/openstack-routers/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/openstack-security-groups/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/openstack-server-groups/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/openstack-snapshots/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/openstack-snapshots/{uuid}/restorations/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/openstack-subnets/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/openstack-tenants/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/openstack-tenants/{uuid}/backend_instances/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/openstack-tenants/{uuid}/backend_volumes/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/openstack-volume-availability-zones/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/openstack-volume-types/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/openstack-volumes/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/organization-groups/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/payment-profiles/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/payments/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/project-credits/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/project-quotas/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/project-types/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/projects/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/projects/{project_uuid}/marketplace-checklists/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

DELETE /api/projects/{uuid}/

- Extensions changed
  - New extension: x-permissions

PATCH /api/projects/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/projects/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/projects/{uuid}/list_users/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/projects/{uuid}/other_users/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/promotions-campaigns/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

DELETE /api/promotions-campaigns/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/promotions-campaigns/{uuid}/

- Extensions changed
  - New extension: x-permissions

POST /api/promotions-campaigns/{uuid}/activate/

- Extensions changed
  - New extension: x-permissions

GET /api/promotions-campaigns/{uuid}/orders/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/promotions-campaigns/{uuid}/resources/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

POST /api/promotions-campaigns/{uuid}/terminate/

- Extensions changed
  - New extension: x-permissions

GET /api/proposal-proposals/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

POST /api/proposal-proposals/{uuid}/approve/

- Extensions changed
  - New extension: x-permissions

GET /api/proposal-proposals/{uuid}/list_users/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

POST /api/proposal-proposals/{uuid}/reject/

- Extensions changed
  - New extension: x-permissions

GET /api/proposal-proposals/{uuid}/resources/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/proposal-protected-calls/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [manager_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: manager_uuid
    - Headers changed
      - New header: x-result-count

POST /api/proposal-protected-calls/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: manager_uuid

GET /api/proposal-protected-calls/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [manager_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: manager_uuid

PATCH /api/proposal-protected-calls/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: manager_uuid

PUT /api/proposal-protected-calls/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: manager_uuid

GET /api/proposal-protected-calls/{uuid}/list_users/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/proposal-protected-calls/{uuid}/offerings/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/proposal-protected-calls/{uuid}/resource_templates/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/proposal-protected-calls/{uuid}/rounds/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

POST /api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/close/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: manager_uuid

GET /api/proposal-public-calls/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [manager_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: manager_uuid
    - Headers changed
      - New header: x-result-count

GET /api/proposal-public-calls/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [manager_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: manager_uuid

GET /api/proposal-requested-offerings/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

POST /api/proposal-requested-offerings/{uuid}/accept/

- Extensions changed
  - New extension: x-permissions

POST /api/proposal-requested-offerings/{uuid}/cancel/

- Extensions changed
  - New extension: x-permissions

GET /api/proposal-requested-resources/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/proposal-reviews/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/provider-invoice-items/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/rabbitmq-user-stats/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/rabbitmq-vhost-stats/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/rancher-apps/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/rancher-catalogs/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/rancher-cluster-security-groups/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/rancher-cluster-templates/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/rancher-clusters/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/rancher-hpas/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/rancher-ingresses/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/rancher-namespaces/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/rancher-nodes/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/rancher-projects/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/rancher-role-templates/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/rancher-services/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/rancher-templates/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/rancher-users/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/rancher-workloads/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/roles/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/service-settings/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/slurm-allocation-user-usage/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/slurm-allocations/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/slurm-associations/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/slurm-jobs/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/support-attachments/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/support-comments/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/support-feedbacks/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/support-issues/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/support-priorities/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/support-templates/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/support-users/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/user-agreements/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/user-group-invitations/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/user-group-invitations/{uuid}/projects/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/user-invitations/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/user-permission-requests/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/user-permissions/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: scope_type
                - Nullable changed from false to true
    - Headers changed
      - New header: x-result-count

GET /api/user-permissions/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: scope_type
              - Nullable changed from false to true

GET /api/users/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: permissions
                - Items changed
                  - Properties changed
                    - Modified property: scope_type
                      - Nullable changed from false to true
    - Headers changed
      - New header: x-result-count

POST /api/users/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: permissions
              - Items changed
                - Properties changed
                  - Modified property: scope_type
                    - Nullable changed from false to true

GET /api/users/me/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: permissions
              - Items changed
                - Properties changed
                  - Modified property: scope_type
                    - Nullable changed from false to true

GET /api/users/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: permissions
              - Items changed
                - Properties changed
                  - Modified property: scope_type
                    - Nullable changed from false to true

PATCH /api/users/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: permissions
              - Items changed
                - Properties changed
                  - Modified property: scope_type
                    - Nullable changed from false to true

PUT /api/users/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: permissions
              - Items changed
                - Properties changed
                  - Modified property: scope_type
                    - Nullable changed from false to true

GET /api/vmware-clusters/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/vmware-datastores/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/vmware-disks/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/vmware-folders/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/vmware-networks/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/vmware-ports/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/vmware-templates/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

GET /api/vmware-virtual-machine/

- Responses changed
  - Modified response: 200
    - Headers changed
      - New header: x-result-count

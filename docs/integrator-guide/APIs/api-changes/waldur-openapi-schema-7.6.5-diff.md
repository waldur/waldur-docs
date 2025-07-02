# OpenAPI schema diff - 7.6.5

## For version 7.6.5

### New Endpoints: 17

---------------------
GET /api/autoprovisioning-rule-plans/  
POST /api/autoprovisioning-rule-plans/  
DELETE /api/autoprovisioning-rule-plans/{uuid}/  
GET /api/autoprovisioning-rule-plans/{uuid}/  
PATCH /api/autoprovisioning-rule-plans/{uuid}/  
PUT /api/autoprovisioning-rule-plans/{uuid}/  
GET /api/autoprovisioning-rules/  
POST /api/autoprovisioning-rules/  
DELETE /api/autoprovisioning-rules/{uuid}/  
GET /api/autoprovisioning-rules/{uuid}/  
PATCH /api/autoprovisioning-rules/{uuid}/  
PUT /api/autoprovisioning-rules/{uuid}/  
GET /api/openstack-marketplace-tenants/  
GET /api/openstack-marketplace-tenants/{uuid}/  
POST /api/openstack-marketplace-tenants/{uuid}/create_image/  
POST /api/openstack-marketplace-tenants/{uuid}/upload_image_data/{image_id}/  
POST /api/projects/{uuid}/sync_user_roles/  

### Deleted Endpoints: None

---------------------------

### Modified Endpoints: 1168

----------------------------
POST /api-auth/logout/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api-auth/password/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api-auth/saml2/providers/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/access-subnets/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/access-subnets/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/access-subnets/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/access-subnets/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/access-subnets/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/access-subnets/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/admin-announcements/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/admin-announcements/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/admin-announcements/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/admin-announcements/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/admin-announcements/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/admin-announcements/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/auth-tokens/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/auth-tokens/{user_id}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/auth-tokens/{user_id}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/auth-valimo/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/auth-valimo/result/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/aws-images/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/aws-images/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/aws-instances/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/aws-instances/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/aws-instances/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/aws-instances/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/aws-instances/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/aws-instances/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/aws-instances/{uuid}/pull/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/aws-instances/{uuid}/resize/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/aws-instances/{uuid}/restart/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/aws-instances/{uuid}/start/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/aws-instances/{uuid}/stop/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/aws-instances/{uuid}/unlink/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/aws-regions/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/aws-regions/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/aws-sizes/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/aws-sizes/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/aws-volumes/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/aws-volumes/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/aws-volumes/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/aws-volumes/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/aws-volumes/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/aws-volumes/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/aws-volumes/{uuid}/attach/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/aws-volumes/{uuid}/detach/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/aws-volumes/{uuid}/pull/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/aws-volumes/{uuid}/unlink/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/azure-images/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/azure-images/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/azure-locations/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/azure-locations/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/azure-public-ips/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/azure-public-ips/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/azure-public-ips/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/azure-public-ips/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/azure-public-ips/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/azure-public-ips/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/azure-public-ips/{uuid}/pull/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/azure-public-ips/{uuid}/unlink/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/azure-resource-groups/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/azure-resource-groups/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/azure-sizes/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/azure-sizes/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/azure-sql-databases/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/azure-sql-databases/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/azure-sql-databases/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/azure-sql-databases/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/azure-sql-databases/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/azure-sql-databases/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/azure-sql-databases/{uuid}/pull/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/azure-sql-databases/{uuid}/unlink/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/azure-sql-servers/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/azure-sql-servers/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/azure-sql-servers/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/azure-sql-servers/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/azure-sql-servers/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/azure-sql-servers/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/azure-sql-servers/{uuid}/create_database/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/azure-sql-servers/{uuid}/pull/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/azure-sql-servers/{uuid}/unlink/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/azure-virtualmachines/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/azure-virtualmachines/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/azure-virtualmachines/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/azure-virtualmachines/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/azure-virtualmachines/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/azure-virtualmachines/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/azure-virtualmachines/{uuid}/pull/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/azure-virtualmachines/{uuid}/restart/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/azure-virtualmachines/{uuid}/start/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/azure-virtualmachines/{uuid}/stop/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/azure-virtualmachines/{uuid}/unlink/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/billing-total-cost/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/booking-offerings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: plugin_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedPluginOptions
                    - Properties changed
                      - New property: managed_rancher_tenant_max_cpu
                      - New property: managed_rancher_tenant_max_disk
                      - New property: managed_rancher_tenant_max_ram
                      - Deleted property: managed_rancher_load_balancer_cloud_init_template
- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/booking-offerings/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: managed_rancher_tenant_max_cpu
                    - New property: managed_rancher_tenant_max_disk
                    - New property: managed_rancher_tenant_max_ram
                    - Deleted property: managed_rancher_load_balancer_cloud_init_template
- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/booking-offerings/{uuid}/google_calendar_sync/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/booking-offerings/{uuid}/share_google_calendar/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/booking-offerings/{uuid}/unshare_google_calendar/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/booking-resources/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/booking-resources/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/booking-resources/{uuid}/accept/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/booking-resources/{uuid}/reject/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/broadcast-message-templates/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/broadcast-message-templates/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/broadcast-message-templates/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/broadcast-message-templates/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/broadcast-message-templates/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/broadcast-message-templates/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/broadcast-messages/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/broadcast-messages/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/broadcast-messages/recipients/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/broadcast-messages/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/broadcast-messages/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/broadcast-messages/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/broadcast-messages/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/broadcast-messages/{uuid}/send/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/call-managing-organisations/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/call-managing-organisations/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/call-managing-organisations/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/call-managing-organisations/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/call-managing-organisations/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/call-managing-organisations/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/call-managing-organisations/{uuid}/add_user/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/call-managing-organisations/{uuid}/delete_user/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/call-managing-organisations/{uuid}/list_users/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/call-managing-organisations/{uuid}/stats/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/call-managing-organisations/{uuid}/update_user/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/call-rounds/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/call-rounds/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/call-rounds/{uuid}/reviewers/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/celery-stats/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/component-user-usage-limits/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/component-user-usage-limits/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/component-user-usage-limits/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/component-user-usage-limits/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/component-user-usage-limits/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/component-user-usage-limits/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/configuration/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/customer-credits/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/customer-credits/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/customer-credits/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/customer-credits/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/customer-credits/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/customer-credits/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/customer-credits/{uuid}/apply_compensations/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/customer-credits/{uuid}/clear_compensations/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/customer-credits/{uuid}/consumptions/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/customer-permissions-reviews/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/customer-permissions-reviews/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/customer-permissions-reviews/{uuid}/close/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/customer-quotas/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/customers/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/customers/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/customers/countries/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/customers/{customer_uuid}/marketplace-checklists/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/customers/{customer_uuid}/marketplace-checklists/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/customers/{customer_uuid}/marketplace-checklists/{checklist_uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/customers/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/customers/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/customers/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/customers/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/customers/{uuid}/add_user/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/customers/{uuid}/delete_user/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/customers/{uuid}/list_users/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/customers/{uuid}/stats/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/customers/{uuid}/update_organization_groups/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/customers/{uuid}/update_user/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/customers/{uuid}/users/

- Modified query param: field
  - Schema changed
    - Items changed
      - Deleted enum values: [role]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Deleted property: role
              - Modified property: expiration_time
                - Nullable changed from false to true
              - Modified property: role_name
                - Nullable changed from false to true
- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/daily-quotas/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/database-stats/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/digitalocean-droplets/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/digitalocean-droplets/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/digitalocean-droplets/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/digitalocean-droplets/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/digitalocean-droplets/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/digitalocean-droplets/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/digitalocean-droplets/{uuid}/pull/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/digitalocean-droplets/{uuid}/resize/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/digitalocean-droplets/{uuid}/restart/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/digitalocean-droplets/{uuid}/start/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/digitalocean-droplets/{uuid}/stop/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/digitalocean-droplets/{uuid}/unlink/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/digitalocean-images/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/digitalocean-images/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/digitalocean-regions/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/digitalocean-regions/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/digitalocean-sizes/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/digitalocean-sizes/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/email-logs/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/email-logs/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/event-subscriptions/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/event-subscriptions/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/event-subscriptions/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/event-subscriptions/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/events-stats/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/events/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/events/count/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/events/event_groups/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/events/scope_types/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/events/{id}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/feature-values/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/financial-reports/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/financial-reports/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/freeipa-profiles/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/freeipa-profiles/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/freeipa-profiles/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/freeipa-profiles/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/freeipa-profiles/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/freeipa-profiles/{uuid}/update_ssh_keys/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/google-auth/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/google-auth/callback/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/google-auth/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/google-auth/{uuid}/authorize/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/hooks-email/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/hooks-email/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/hooks-email/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/hooks-email/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/hooks-email/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/hooks-email/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/hooks-web/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/hooks-web/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/hooks-web/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/hooks-web/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/hooks-web/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/hooks-web/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/hooks/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/identity-providers/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: extra_scope
- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/identity-providers/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: extra_scope
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: extra_scope
- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/identity-providers/{provider}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/identity-providers/{provider}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: extra_scope
- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/identity-providers/{provider}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: extra_scope
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: extra_scope
- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/identity-providers/{provider}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: extra_scope
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: extra_scope
- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/invoice-items/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/invoice-items/costs/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/invoice-items/customer_costs_for_period/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/invoice-items/project_costs_for_period/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/invoice-items/total_price/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/invoice-items/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/invoice-items/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/invoice-items/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/invoice-items/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/invoice-items/{uuid}/consumptions/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/invoice-items/{uuid}/create_compensation/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/invoice-items/{uuid}/migrate_to/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/invoice/send-financial-report-by-mail/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/invoices/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/invoices/growth/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/invoices/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/invoices/{uuid}/items/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/invoices/{uuid}/paid/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/invoices/{uuid}/send_notification/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/invoices/{uuid}/set_backend_id/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/invoices/{uuid}/set_payment_url/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/invoices/{uuid}/set_reference_number/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/invoices/{uuid}/stats/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/keycloak-groups/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/keycloak-groups/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/keycloak-user-group-memberships/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/keycloak-user-group-memberships/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/keycloak-user-group-memberships/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/keycloak-user-group-memberships/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/keycloak-user-group-memberships/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/keycloak-user-group-memberships/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/keys/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/keys/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/keys/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/keys/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/lexis-links/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/lexis-links/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/lexis-links/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/lexis-links/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/lexis-links/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/lexis-links/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-bookings/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-categories/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-categories/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/marketplace-categories/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-categories/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/marketplace-categories/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/marketplace-categories/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-category-columns/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-category-columns/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/marketplace-category-columns/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-category-columns/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/marketplace-category-columns/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/marketplace-category-columns/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-category-component-usages/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-category-component-usages/{id}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-category-components/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-category-components/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/marketplace-category-components/{id}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-category-components/{id}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/marketplace-category-components/{id}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/marketplace-category-components/{id}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-category-groups/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-category-groups/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/marketplace-category-groups/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-category-groups/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/marketplace-category-groups/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/marketplace-category-groups/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-category-help-articles/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-category-help-articles/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/marketplace-category-help-articles/{id}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-category-help-articles/{id}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/marketplace-category-help-articles/{id}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/marketplace-category-help-articles/{id}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-checklists-categories/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-checklists-categories/{category_uuid}/checklists/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-checklists-categories/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-checklists/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-checklists/{checklist_uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-checklists/{checklist_uuid}/answers/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-checklists/{checklist_uuid}/answers/submit/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-checklists/{checklist_uuid}/questions/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-checklists/{checklist_uuid}/stats/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-checklists/{checklist_uuid}/user/{user_uuid}/answers/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-component-usages/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-component-usages/set_usage/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-component-usages/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-component-usages/{uuid}/set_user_usage/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-component-user-usages/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-component-user-usages/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-customer-estimated-cost-policies/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-customer-estimated-cost-policies/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-customer-estimated-cost-policies/actions/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/marketplace-customer-estimated-cost-policies/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-customer-estimated-cost-policies/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/marketplace-customer-estimated-cost-policies/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/marketplace-customer-estimated-cost-policies/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-customer-service-accounts/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-customer-service-accounts/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/marketplace-customer-service-accounts/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-customer-service-accounts/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/marketplace-customer-service-accounts/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/marketplace-customer-service-accounts/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-customer-service-accounts/{uuid}/rotate_api_key/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-global-categories/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-integration-statuses/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-integration-statuses/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-offering-estimated-cost-policies/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-offering-estimated-cost-policies/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-offering-estimated-cost-policies/actions/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/marketplace-offering-estimated-cost-policies/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-offering-estimated-cost-policies/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/marketplace-offering-estimated-cost-policies/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/marketplace-offering-estimated-cost-policies/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-offering-files/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-offering-files/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/marketplace-offering-files/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-offering-files/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-offering-permissions-log/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: role
                - Format changed from '' to 'uri'
                - ReadOnly changed from true to false
- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-offering-permissions-log/{id}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: role
              - Format changed from '' to 'uri'
              - ReadOnly changed from true to false
- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-offering-permissions/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: role
                - Format changed from '' to 'uri'
                - ReadOnly changed from true to false
- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-offering-permissions/{id}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: role
              - Format changed from '' to 'uri'
              - ReadOnly changed from true to false
- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-offering-referrals/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-offering-referrals/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-offering-usage-policies/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-offering-usage-policies/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-offering-usage-policies/actions/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/marketplace-offering-usage-policies/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-offering-usage-policies/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/marketplace-offering-usage-policies/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/marketplace-offering-usage-policies/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-offering-user-roles/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-offering-user-roles/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/marketplace-offering-user-roles/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-offering-user-roles/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/marketplace-offering-user-roles/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/marketplace-offering-user-roles/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-offering-users/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: offering_uuid
                - ReadOnly changed from true to false
              - Modified property: user_uuid
                - ReadOnly changed from true to false
- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-offering-users/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Required changed
          - Deleted required property: offering
          - Deleted required property: user
        - Properties changed
          - New property: offering_uuid
          - New property: user_uuid
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: offering_uuid
              - ReadOnly changed from true to false
            - Modified property: user_uuid
              - ReadOnly changed from true to false
- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/marketplace-offering-users/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-offering-users/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: offering_uuid
              - ReadOnly changed from true to false
            - Modified property: user_uuid
              - ReadOnly changed from true to false
- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/marketplace-offering-users/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: offering_uuid
          - New property: user_uuid
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: offering_uuid
              - ReadOnly changed from true to false
            - Modified property: user_uuid
              - ReadOnly changed from true to false
- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/marketplace-offering-users/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Required changed
          - Deleted required property: offering
          - Deleted required property: user
        - Properties changed
          - New property: offering_uuid
          - New property: user_uuid
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: offering_uuid
              - ReadOnly changed from true to false
            - Modified property: user_uuid
              - ReadOnly changed from true to false
- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-offering-users/{uuid}/update_restricted/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-orders/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-orders/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Deleted property: output
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: output
          - Properties changed
            - Modified property: output
              - ReadOnly changed from false to true
- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/marketplace-orders/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-orders/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-orders/{uuid}/approve_by_consumer/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-orders/{uuid}/approve_by_provider/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-orders/{uuid}/cancel/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-orders/{uuid}/offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: managed_rancher_tenant_max_cpu
                    - New property: managed_rancher_tenant_max_disk
                    - New property: managed_rancher_tenant_max_ram
                    - Deleted property: managed_rancher_load_balancer_cloud_init_template
- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-orders/{uuid}/reject_by_consumer/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-orders/{uuid}/reject_by_provider/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-orders/{uuid}/set_state_done/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-orders/{uuid}/set_state_erred/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-orders/{uuid}/set_state_executing/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-orders/{uuid}/unlink/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-plan-components/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-plan-components/{id}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-plans/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-plans/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-plans/usage_stats/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-plans/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/marketplace-plans/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/marketplace-plans/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-plans/{uuid}/archive/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-plans/{uuid}/delete_organization_groups/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-plans/{uuid}/update_organization_groups/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-plans/{uuid}/update_prices/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-plans/{uuid}/update_quotas/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-project-estimated-cost-policies/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-project-estimated-cost-policies/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-project-estimated-cost-policies/actions/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/marketplace-project-estimated-cost-policies/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-project-estimated-cost-policies/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/marketplace-project-estimated-cost-policies/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/marketplace-project-estimated-cost-policies/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-project-service-accounts/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-project-service-accounts/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/marketplace-project-service-accounts/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-project-service-accounts/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/marketplace-project-service-accounts/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/marketplace-project-service-accounts/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-project-service-accounts/{uuid}/rotate_api_key/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-project-update-requests/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-project-update-requests/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-project-update-requests/{uuid}/approve/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-project-update-requests/{uuid}/reject/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-provider-offerings/

- New query param: uuid_list
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: plugin_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedPluginOptions
                    - Properties changed
                      - New property: managed_rancher_tenant_max_cpu
                      - New property: managed_rancher_tenant_max_disk
                      - New property: managed_rancher_tenant_max_ram
                      - Deleted property: managed_rancher_load_balancer_cloud_init_template
              - Modified property: secret_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedSecretOptions
                    - Properties changed
                      - New property: managed_rancher_load_balancer_cloud_init_template
- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-provider-offerings/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: managed_rancher_tenant_max_cpu
                    - New property: managed_rancher_tenant_max_disk
                    - New property: managed_rancher_tenant_max_ram
                    - Deleted property: managed_rancher_load_balancer_cloud_init_template
            - Modified property: secret_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedSecretOptions
                  - Properties changed
                    - New property: managed_rancher_load_balancer_cloud_init_template
- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-provider-offerings/groups/

- New query param: uuid_list
- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/marketplace-provider-offerings/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-provider-offerings/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: managed_rancher_tenant_max_cpu
                    - New property: managed_rancher_tenant_max_disk
                    - New property: managed_rancher_tenant_max_ram
                    - Deleted property: managed_rancher_load_balancer_cloud_init_template
            - Modified property: secret_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedSecretOptions
                  - Properties changed
                    - New property: managed_rancher_load_balancer_cloud_init_template
- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-provider-offerings/{uuid}/activate/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-provider-offerings/{uuid}/add_endpoint/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-provider-offerings/{uuid}/add_user/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-provider-offerings/{uuid}/archive/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-provider-offerings/{uuid}/component_stats/

- New query param: uuid_list
- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-provider-offerings/{uuid}/costs/

- New query param: uuid_list
- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-provider-offerings/{uuid}/create_offering_component/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-provider-offerings/{uuid}/customers/

- New query param: uuid_list
- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-provider-offerings/{uuid}/delete_endpoint/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-provider-offerings/{uuid}/delete_image/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-provider-offerings/{uuid}/delete_organization_groups/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-provider-offerings/{uuid}/delete_thumbnail/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-provider-offerings/{uuid}/delete_user/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-provider-offerings/{uuid}/draft/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-provider-offerings/{uuid}/glauth_users_config/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-provider-offerings/{uuid}/import_resource/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-provider-offerings/{uuid}/importable_resources/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-provider-offerings/{uuid}/list_customer_projects/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-provider-offerings/{uuid}/list_customer_service_accounts/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: managed_rancher_tenant_max_cpu
                    - New property: managed_rancher_tenant_max_disk
                    - New property: managed_rancher_tenant_max_ram
                    - Deleted property: managed_rancher_load_balancer_cloud_init_template
            - Modified property: secret_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedSecretOptions
                  - Properties changed
                    - New property: managed_rancher_load_balancer_cloud_init_template
- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-provider-offerings/{uuid}/list_customer_users/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-provider-offerings/{uuid}/list_project_service_accounts/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: managed_rancher_tenant_max_cpu
                    - New property: managed_rancher_tenant_max_disk
                    - New property: managed_rancher_tenant_max_ram
                    - Deleted property: managed_rancher_load_balancer_cloud_init_template
            - Modified property: secret_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedSecretOptions
                  - Properties changed
                    - New property: managed_rancher_load_balancer_cloud_init_template
- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-provider-offerings/{uuid}/list_users/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-provider-offerings/{uuid}/move_offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: managed_rancher_tenant_max_cpu
                    - New property: managed_rancher_tenant_max_disk
                    - New property: managed_rancher_tenant_max_ram
                    - Deleted property: managed_rancher_load_balancer_cloud_init_template
- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-provider-offerings/{uuid}/orders/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-provider-offerings/{uuid}/orders/{order_uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-provider-offerings/{uuid}/pause/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-provider-offerings/{uuid}/refresh_offering_usernames/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: managed_rancher_tenant_max_cpu
                    - New property: managed_rancher_tenant_max_disk
                    - New property: managed_rancher_tenant_max_ram
                    - Deleted property: managed_rancher_load_balancer_cloud_init_template
            - Modified property: secret_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedSecretOptions
                  - Properties changed
                    - New property: managed_rancher_load_balancer_cloud_init_template
- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-provider-offerings/{uuid}/remove_offering_component/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-provider-offerings/{uuid}/set_backend_metadata/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-provider-offerings/{uuid}/stats/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: managed_rancher_tenant_max_cpu
                    - New property: managed_rancher_tenant_max_disk
                    - New property: managed_rancher_tenant_max_ram
                    - Deleted property: managed_rancher_load_balancer_cloud_init_template
            - Modified property: secret_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedSecretOptions
                  - Properties changed
                    - New property: managed_rancher_load_balancer_cloud_init_template
- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-provider-offerings/{uuid}/sync/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-provider-offerings/{uuid}/unpause/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-provider-offerings/{uuid}/update_attributes/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-provider-offerings/{uuid}/update_description/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-provider-offerings/{uuid}/update_image/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: managed_rancher_tenant_max_cpu
                    - New property: managed_rancher_tenant_max_disk
                    - New property: managed_rancher_tenant_max_ram
                    - Deleted property: managed_rancher_load_balancer_cloud_init_template
            - Modified property: secret_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedSecretOptions
                  - Properties changed
                    - New property: managed_rancher_load_balancer_cloud_init_template
- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-provider-offerings/{uuid}/update_integration/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: plugin_options
            - Properties changed
              - New property: managed_rancher_tenant_max_cpu
              - New property: managed_rancher_tenant_max_disk
              - New property: managed_rancher_tenant_max_ram
              - Deleted property: managed_rancher_load_balancer_cloud_init_template
          - Modified property: secret_options
            - Properties changed
              - New property: managed_rancher_load_balancer_cloud_init_template
- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-provider-offerings/{uuid}/update_location/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-provider-offerings/{uuid}/update_offering_component/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-provider-offerings/{uuid}/update_options/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-provider-offerings/{uuid}/update_organization_groups/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-provider-offerings/{uuid}/update_overview/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-provider-offerings/{uuid}/update_resource_options/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-provider-offerings/{uuid}/update_thumbnail/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-provider-offerings/{uuid}/update_user/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-provider-offerings/{uuid}/user_has_resource_access/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: managed_rancher_tenant_max_cpu
                    - New property: managed_rancher_tenant_max_disk
                    - New property: managed_rancher_tenant_max_ram
                    - Deleted property: managed_rancher_load_balancer_cloud_init_template
            - Modified property: secret_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedSecretOptions
                  - Properties changed
                    - New property: managed_rancher_load_balancer_cloud_init_template
- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-provider-resources/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-provider-resources/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/marketplace-provider-resources/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/marketplace-provider-resources/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-provider-resources/{uuid}/details/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-provider-resources/{uuid}/glauth_users_config/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-provider-resources/{uuid}/move_resource/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-provider-resources/{uuid}/offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: managed_rancher_tenant_max_cpu
                    - New property: managed_rancher_tenant_max_disk
                    - New property: managed_rancher_tenant_max_ram
                    - Deleted property: managed_rancher_load_balancer_cloud_init_template
- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-provider-resources/{uuid}/offering_for_subresources/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-provider-resources/{uuid}/plan_periods/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-provider-resources/{uuid}/refresh_last_sync/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-provider-resources/{uuid}/set_as_erred/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-provider-resources/{uuid}/set_as_ok/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-provider-resources/{uuid}/set_backend_id/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-provider-resources/{uuid}/set_backend_metadata/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-provider-resources/{uuid}/set_end_date_by_provider/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-provider-resources/{uuid}/set_end_date_by_staff/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-provider-resources/{uuid}/set_limits/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-provider-resources/{uuid}/set_slug/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-provider-resources/{uuid}/submit_report/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-provider-resources/{uuid}/team/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-provider-resources/{uuid}/terminate/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-provider-resources/{uuid}/unlink/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-public-api/check_signature/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-public-api/set_usage/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-public-offerings/

- New query param: uuid_list
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: plugin_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedPluginOptions
                    - Properties changed
                      - New property: managed_rancher_tenant_max_cpu
                      - New property: managed_rancher_tenant_max_disk
                      - New property: managed_rancher_tenant_max_ram
                      - Deleted property: managed_rancher_load_balancer_cloud_init_template
- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-public-offerings/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: managed_rancher_tenant_max_cpu
                    - New property: managed_rancher_tenant_max_disk
                    - New property: managed_rancher_tenant_max_ram
                    - Deleted property: managed_rancher_load_balancer_cloud_init_template
- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-public-offerings/{uuid}/plans/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-public-offerings/{uuid}/plans/{plan_uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-related-customers/{customer_uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-remote-synchronisations/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-remote-synchronisations/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/marketplace-remote-synchronisations/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-remote-synchronisations/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/marketplace-remote-synchronisations/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/marketplace-remote-synchronisations/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-remote-synchronisations/{uuid}/run_synchronisation/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-resource-offerings/{category_uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-resource-users/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-resource-users/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/marketplace-resource-users/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-resource-users/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-resources/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-resources/suggest_name/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-resources/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/marketplace-resources/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/marketplace-resources/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-resources/{uuid}/details/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-resources/{uuid}/glauth_users_config/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-resources/{uuid}/move_resource/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-resources/{uuid}/offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: managed_rancher_tenant_max_cpu
                    - New property: managed_rancher_tenant_max_disk
                    - New property: managed_rancher_tenant_max_ram
                    - Deleted property: managed_rancher_load_balancer_cloud_init_template
- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-resources/{uuid}/offering_for_subresources/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-resources/{uuid}/plan_periods/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-resources/{uuid}/set_end_date_by_staff/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-resources/{uuid}/set_slug/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-resources/{uuid}/switch_plan/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-resources/{uuid}/team/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-resources/{uuid}/terminate/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-resources/{uuid}/unlink/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-resources/{uuid}/update_limits/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-resources/{uuid}/update_options/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-robot-accounts/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: offering_plugin_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedPluginOptions
                    - Properties changed
                      - New property: managed_rancher_tenant_max_cpu
                      - New property: managed_rancher_tenant_max_disk
                      - New property: managed_rancher_tenant_max_ram
                      - Deleted property: managed_rancher_load_balancer_cloud_init_template
- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-robot-accounts/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/marketplace-robot-accounts/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-robot-accounts/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: offering_plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: managed_rancher_tenant_max_cpu
                    - New property: managed_rancher_tenant_max_disk
                    - New property: managed_rancher_tenant_max_ram
                    - Deleted property: managed_rancher_load_balancer_cloud_init_template
- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/marketplace-robot-accounts/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/marketplace-robot-accounts/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-robot-accounts/{uuid}/set_state_creating/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: offering_plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: managed_rancher_tenant_max_cpu
                    - New property: managed_rancher_tenant_max_disk
                    - New property: managed_rancher_tenant_max_ram
                    - Deleted property: managed_rancher_load_balancer_cloud_init_template
- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-robot-accounts/{uuid}/set_state_deleted/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: offering_plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: managed_rancher_tenant_max_cpu
                    - New property: managed_rancher_tenant_max_disk
                    - New property: managed_rancher_tenant_max_ram
                    - Deleted property: managed_rancher_load_balancer_cloud_init_template
- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-robot-accounts/{uuid}/set_state_erred/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: offering_plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: managed_rancher_tenant_max_cpu
                    - New property: managed_rancher_tenant_max_disk
                    - New property: managed_rancher_tenant_max_ram
                    - Deleted property: managed_rancher_load_balancer_cloud_init_template
- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-robot-accounts/{uuid}/set_state_ok/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: offering_plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: managed_rancher_tenant_max_cpu
                    - New property: managed_rancher_tenant_max_disk
                    - New property: managed_rancher_tenant_max_ram
                    - Deleted property: managed_rancher_load_balancer_cloud_init_template
- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-robot-accounts/{uuid}/set_state_request_deletion/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: offering_plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: managed_rancher_tenant_max_cpu
                    - New property: managed_rancher_tenant_max_disk
                    - New property: managed_rancher_tenant_max_ram
                    - Deleted property: managed_rancher_load_balancer_cloud_init_template
- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-runtime-states/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-screenshots/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-screenshots/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/marketplace-screenshots/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-screenshots/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/marketplace-screenshots/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/marketplace-screenshots/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-script-async-dry-run/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-script-async-dry-run/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-script-dry-run/{uuid}/async_run/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: managed_rancher_tenant_max_cpu
                    - New property: managed_rancher_tenant_max_disk
                    - New property: managed_rancher_tenant_max_ram
                    - Deleted property: managed_rancher_load_balancer_cloud_init_template
- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-script-dry-run/{uuid}/run/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: managed_rancher_tenant_max_cpu
                    - New property: managed_rancher_tenant_max_disk
                    - New property: managed_rancher_tenant_max_ram
                    - Deleted property: managed_rancher_load_balancer_cloud_init_template
- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-script-sync-resource/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-sections/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-sections/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/marketplace-sections/{key}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-sections/{key}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/marketplace-sections/{key}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/marketplace-sections/{key}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-service-providers/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-service-providers/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-service-providers/{service_provider_uuid}/customer_projects/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-service-providers/{service_provider_uuid}/customers/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-service-providers/{service_provider_uuid}/keys/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-service-providers/{service_provider_uuid}/offerings/

- New query param: uuid_list
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: secret_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedSecretOptions
                    - Properties changed
                      - New property: managed_rancher_load_balancer_cloud_init_template
- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-service-providers/{service_provider_uuid}/project_permissions/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-service-providers/{service_provider_uuid}/projects/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-service-providers/{service_provider_uuid}/user_customers/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-service-providers/{service_provider_uuid}/users/

- New query param: username_list
- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/marketplace-service-providers/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-service-providers/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/marketplace-service-providers/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/marketplace-service-providers/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-service-providers/{uuid}/add_user/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-service-providers/{uuid}/api_secret_code/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-service-providers/{uuid}/api_secret_code/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-service-providers/{uuid}/delete_user/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-service-providers/{uuid}/list_users/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-service-providers/{uuid}/revenue/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-service-providers/{uuid}/robot_account_customers/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-service-providers/{uuid}/robot_account_projects/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-service-providers/{uuid}/set_offerings_username/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-service-providers/{uuid}/stat/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/marketplace-service-providers/{uuid}/update_user/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-stats/component_usages/

- OperationID changed from 'marketplace_stats_component_usages_retrieve' to 'marketplace_stats_component_usages_list'
- New query param: page
- New query param: page_size
- Responses changed
  - Modified response: 200
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json
- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-stats/component_usages_per_month/

- OperationID changed from 'marketplace_stats_component_usages_per_month_retrieve' to 'marketplace_stats_component_usages_per_month_list'
- New query param: page
- New query param: page_size
- Responses changed
  - Modified response: 200
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json
- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-stats/component_usages_per_project/

- OperationID changed from 'marketplace_stats_component_usages_per_project_retrieve' to 'marketplace_stats_component_usages_per_project_list'
- New query param: page
- New query param: page_size
- Responses changed
  - Modified response: 200
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json
- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-stats/count_active_resources_grouped_by_offering/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-stats/count_active_resources_grouped_by_offering_country/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-stats/count_active_resources_grouped_by_organization_group/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-stats/count_projects_grouped_by_provider_and_industry_flag/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-stats/count_projects_grouped_by_provider_and_oecd/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-stats/count_projects_of_service_providers/

- OperationID changed from 'marketplace_stats_count_projects_of_service_providers_retrieve' to 'marketplace_stats_count_projects_of_service_providers_list'
- New query param: page
- New query param: page_size
- Responses changed
  - Modified response: 200
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json
- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-stats/count_projects_of_service_providers_grouped_by_oecd/

- OperationID changed from 'marketplace_stats_count_projects_of_service_providers_grouped_by_oecd_retrieve' to 'marketplace_stats_count_projects_of_service_providers_grouped_by_oecd_list'
- New query param: page
- New query param: page_size
- Responses changed
  - Modified response: 200
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json
- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-stats/count_unique_users_connected_with_active_resources_of_service_provider/

- OperationID changed from 'marketplace_stats_count_unique_users_connected_with_active_resources_of_service_provider_retrieve' to 'marketplace_stats_count_unique_users_connected_with_active_resources_of_service_provider_list'
- New query param: page
- New query param: page_size
- Responses changed
  - Modified response: 200
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json
- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-stats/count_users_of_service_providers/

- OperationID changed from 'marketplace_stats_count_users_of_service_providers_retrieve' to 'marketplace_stats_count_users_of_service_providers_list'
- New query param: page
- New query param: page_size
- Responses changed
  - Modified response: 200
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json
- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-stats/customer_member_count/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-stats/offerings_counter_stats/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-stats/organization_project_count/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-stats/organization_resource_count/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-stats/projects_limits_grouped_by_industry_flag/

- Responses changed
  - Modified response: 200
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json
- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-stats/projects_limits_grouped_by_oecd/

- Responses changed
  - Modified response: 200
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json
- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-stats/projects_usages_grouped_by_industry_flag/

- Responses changed
  - Modified response: 200
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json
- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-stats/projects_usages_grouped_by_oecd/

- Responses changed
  - Modified response: 200
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json
- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-stats/resources_limits/

- OperationID changed from 'marketplace_stats_resources_limits_retrieve' to 'marketplace_stats_resources_limits_list'
- New query param: page
- New query param: page_size
- Responses changed
  - Modified response: 200
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json
- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/marketplace-stats/total_cost_of_active_resources_per_offering/

- OperationID changed from 'marketplace_stats_total_cost_of_active_resources_per_offering_retrieve' to 'marketplace_stats_total_cost_of_active_resources_per_offering_list'
- New query param: page
- New query param: page_size
- Responses changed
  - Modified response: 200
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json
- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/media/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/notification-messages-templates/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/notification-messages-templates/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/notification-messages-templates/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/notification-messages-templates/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/notification-messages-templates/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/notification-messages-templates/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/notification-messages-templates/{uuid}/override/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/notification-messages/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/notification-messages/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/notification-messages/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/notification-messages/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/notification-messages/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/notification-messages/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/notification-messages/{uuid}/disable/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/notification-messages/{uuid}/enable/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/openstack-backups/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/openstack-backups/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/openstack-backups/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/openstack-backups/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/openstack-backups/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-backups/{uuid}/pull/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-backups/{uuid}/restore/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-backups/{uuid}/unlink/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/openstack-flavors/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/openstack-flavors/usage_stats/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/openstack-flavors/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/openstack-floating-ips/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/openstack-floating-ips/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/openstack-floating-ips/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-floating-ips/{uuid}/attach_to_port/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-floating-ips/{uuid}/detach_from_port/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-floating-ips/{uuid}/pull/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-floating-ips/{uuid}/unlink/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-floating-ips/{uuid}/update_description/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/openstack-images/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/openstack-images/usage_stats/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/openstack-images/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/openstack-instance-availability-zones/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/openstack-instance-availability-zones/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/openstack-instances/

- New query param: query
- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/openstack-instances/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/openstack-instances/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/openstack-instances/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-instances/{uuid}/backup/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-instances/{uuid}/change_flavor/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/openstack-instances/{uuid}/console/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/openstack-instances/{uuid}/console_log/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/openstack-instances/{uuid}/floating_ips/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/openstack-instances/{uuid}/ports/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-instances/{uuid}/pull/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-instances/{uuid}/restart/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-instances/{uuid}/start/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-instances/{uuid}/stop/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-instances/{uuid}/unlink/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-instances/{uuid}/update_allowed_address_pairs/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-instances/{uuid}/update_floating_ips/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-instances/{uuid}/update_ports/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-instances/{uuid}/update_security_groups/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/openstack-migrations/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-migrations/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/openstack-migrations/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/openstack-migrations/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/openstack-migrations/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/openstack-migrations/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/openstack-network-rbac-policies/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/openstack-network-rbac-policies/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/openstack-networks/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/openstack-networks/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/openstack-networks/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/openstack-networks/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/openstack-networks/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-networks/{uuid}/create_subnet/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-networks/{uuid}/pull/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-networks/{uuid}/rbac_policy_create/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/openstack-networks/{uuid}/rbac_policy_delete/{rbac_policy_uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-networks/{uuid}/set_mtu/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-networks/{uuid}/unlink/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/openstack-ports/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-ports/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/openstack-ports/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/openstack-ports/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/openstack-ports/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/openstack-ports/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-ports/{uuid}/disable_port/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-ports/{uuid}/disable_port_security/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-ports/{uuid}/enable_port/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-ports/{uuid}/enable_port_security/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-ports/{uuid}/pull/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-ports/{uuid}/unlink/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-ports/{uuid}/update_port_ip/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-ports/{uuid}/update_security_groups/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/openstack-routers/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-routers/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/openstack-routers/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/openstack-routers/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-routers/{uuid}/add_router_interface/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-routers/{uuid}/remove_router_interface/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-routers/{uuid}/set_routes/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/openstack-security-groups/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/openstack-security-groups/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/openstack-security-groups/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/openstack-security-groups/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/openstack-security-groups/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-security-groups/{uuid}/pull/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-security-groups/{uuid}/set_rules/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-security-groups/{uuid}/unlink/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/openstack-server-groups/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-server-groups/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/openstack-server-groups/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/openstack-server-groups/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/openstack-server-groups/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/openstack-server-groups/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-server-groups/{uuid}/pull/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-server-groups/{uuid}/unlink/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/openstack-snapshots/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/openstack-snapshots/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/openstack-snapshots/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/openstack-snapshots/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/openstack-snapshots/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-snapshots/{uuid}/pull/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/openstack-snapshots/{uuid}/restorations/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-snapshots/{uuid}/restore/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-snapshots/{uuid}/unlink/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/openstack-subnets/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/openstack-subnets/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/openstack-subnets/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/openstack-subnets/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/openstack-subnets/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-subnets/{uuid}/connect/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-subnets/{uuid}/disconnect/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-subnets/{uuid}/pull/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-subnets/{uuid}/unlink/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/openstack-tenants/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-tenants/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/openstack-tenants/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/openstack-tenants/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/openstack-tenants/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/openstack-tenants/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/openstack-tenants/{uuid}/backend_instances/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/openstack-tenants/{uuid}/backend_volumes/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-tenants/{uuid}/change_password/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-tenants/{uuid}/create_floating_ip/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-tenants/{uuid}/create_network/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-tenants/{uuid}/create_security_group/

- Responses changed
  - New response: 201
  - Deleted response: 200
- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-tenants/{uuid}/create_server_group/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-tenants/{uuid}/pull/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-tenants/{uuid}/pull_floating_ips/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-tenants/{uuid}/pull_quotas/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-tenants/{uuid}/pull_security_groups/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-tenants/{uuid}/pull_server_groups/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-tenants/{uuid}/set_quotas/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-tenants/{uuid}/unlink/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/openstack-volume-availability-zones/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/openstack-volume-availability-zones/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/openstack-volume-types/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/openstack-volume-types/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/openstack-volumes/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/openstack-volumes/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/openstack-volumes/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/openstack-volumes/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-volumes/{uuid}/attach/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-volumes/{uuid}/detach/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-volumes/{uuid}/extend/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-volumes/{uuid}/pull/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-volumes/{uuid}/retype/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-volumes/{uuid}/snapshot/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/openstack-volumes/{uuid}/unlink/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/organization-groups/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/organization-groups/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/organization-groups/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/organization-groups/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/organization-groups/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/organization-groups/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/override-settings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: OIDC_AUTH_URL
            - New property: OIDC_CACHE_TIMEOUT
            - New property: OIDC_CLIENT_ID
            - New property: OIDC_CLIENT_SECRET
            - New property: OIDC_INTROSPECTION_URL
            - New property: OIDC_USER_FIELD
- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/override-settings/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: OIDC_AUTH_URL
          - New property: OIDC_CACHE_TIMEOUT
          - New property: OIDC_CLIENT_ID
          - New property: OIDC_CLIENT_SECRET
          - New property: OIDC_INTROSPECTION_URL
          - New property: OIDC_USER_FIELD
- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/payment-profiles/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/payment-profiles/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/payment-profiles/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/payment-profiles/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/payment-profiles/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/payment-profiles/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/payment-profiles/{uuid}/enable/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/payments/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/payments/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/payments/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/payments/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/payments/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/payments/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/payments/{uuid}/link_to_invoice/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/payments/{uuid}/unlink_from_invoice/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/project-credits/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/project-credits/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/project-credits/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/project-credits/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/project-credits/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/project-credits/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/project-quotas/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/project-types/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/project-types/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/projects/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/projects/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/projects/{project_uuid}/marketplace-checklists/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/projects/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/projects/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/projects/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/projects/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/projects/{uuid}/add_user/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/projects/{uuid}/delete_user/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/projects/{uuid}/list_users/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/projects/{uuid}/move_project/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/projects/{uuid}/other_users/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/projects/{uuid}/stats/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/projects/{uuid}/update_user/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/promotions-campaigns/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/promotions-campaigns/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/promotions-campaigns/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/promotions-campaigns/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/promotions-campaigns/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/promotions-campaigns/{uuid}/activate/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/promotions-campaigns/{uuid}/orders/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/promotions-campaigns/{uuid}/resources/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/promotions-campaigns/{uuid}/terminate/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/proposal-proposals/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/proposal-proposals/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/proposal-proposals/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/proposal-proposals/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/proposal-proposals/{uuid}/add_user/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/proposal-proposals/{uuid}/approve/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/proposal-proposals/{uuid}/attach_document/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/proposal-proposals/{uuid}/delete_user/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/proposal-proposals/{uuid}/list_users/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/proposal-proposals/{uuid}/reject/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/proposal-proposals/{uuid}/resources/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/proposal-proposals/{uuid}/resources/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/proposal-proposals/{uuid}/resources/{obj_uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/proposal-proposals/{uuid}/resources/{obj_uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/proposal-proposals/{uuid}/resources/{obj_uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/proposal-proposals/{uuid}/resources/{obj_uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/proposal-proposals/{uuid}/submit/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/proposal-proposals/{uuid}/update_project_details/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/proposal-proposals/{uuid}/update_user/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/proposal-protected-calls/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/proposal-protected-calls/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/proposal-protected-calls/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/proposal-protected-calls/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/proposal-protected-calls/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/proposal-protected-calls/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/proposal-protected-calls/{uuid}/activate/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/proposal-protected-calls/{uuid}/add_user/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/proposal-protected-calls/{uuid}/archive/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/proposal-protected-calls/{uuid}/attach_documents/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/proposal-protected-calls/{uuid}/delete_user/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/proposal-protected-calls/{uuid}/detach_documents/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/proposal-protected-calls/{uuid}/list_users/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/proposal-protected-calls/{uuid}/offerings/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/proposal-protected-calls/{uuid}/offerings/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/proposal-protected-calls/{uuid}/offerings/{obj_uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/proposal-protected-calls/{uuid}/offerings/{obj_uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/proposal-protected-calls/{uuid}/offerings/{obj_uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/proposal-protected-calls/{uuid}/offerings/{obj_uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/proposal-protected-calls/{uuid}/resource_templates/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/proposal-protected-calls/{uuid}/resource_templates/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/proposal-protected-calls/{uuid}/resource_templates/{obj_uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/proposal-protected-calls/{uuid}/resource_templates/{obj_uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/proposal-protected-calls/{uuid}/resource_templates/{obj_uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/proposal-protected-calls/{uuid}/resource_templates/{obj_uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/proposal-protected-calls/{uuid}/rounds/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/proposal-protected-calls/{uuid}/rounds/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/close/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/proposal-protected-calls/{uuid}/update_user/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/proposal-public-calls/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/proposal-public-calls/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/proposal-requested-offerings/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/proposal-requested-offerings/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/proposal-requested-offerings/{uuid}/accept/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/proposal-requested-offerings/{uuid}/cancel/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/proposal-requested-resources/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/proposal-requested-resources/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/proposal-reviews/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/proposal-reviews/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/proposal-reviews/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/proposal-reviews/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/proposal-reviews/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/proposal-reviews/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/proposal-reviews/{uuid}/accept/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/proposal-reviews/{uuid}/reject/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/proposal-reviews/{uuid}/submit/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/provider-invoice-items/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/provider-invoice-items/{id}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/query/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/rabbitmq-user-stats/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/rabbitmq-vhost-stats/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/rancher-apps/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/rancher-apps/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/rancher-apps/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/rancher-apps/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/rancher-apps/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/rancher-apps/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/rancher-apps/{uuid}/pull/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/rancher-apps/{uuid}/unlink/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/rancher-catalogs/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/rancher-catalogs/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/rancher-catalogs/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/rancher-catalogs/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/rancher-catalogs/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/rancher-catalogs/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/rancher-catalogs/{uuid}/refresh/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/rancher-cluster-security-groups/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/rancher-cluster-security-groups/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/rancher-cluster-security-groups/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/rancher-cluster-security-groups/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/rancher-cluster-templates/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/rancher-cluster-templates/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/rancher-clusters/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [capacity kubernetes_version requested router_ips]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: capacity
              - New property: kubernetes_version
              - New property: requested
              - New property: router_ips
              - Modified property: public_ips
                - Items changed
                  - Properties changed
                    - New property: external_ip_address
                    - New property: floating_ip_uuid
                    - Deleted property: cluster
                    - Modified property: floating_ip
                      - Nullable changed from true to false
                      - ReadOnly changed from false to true
- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/rancher-clusters/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: capacity
            - New property: kubernetes_version
            - New property: requested
            - New property: router_ips
            - Modified property: public_ips
              - Items changed
                - Properties changed
                  - New property: external_ip_address
                  - New property: floating_ip_uuid
                  - Deleted property: cluster
                  - Modified property: floating_ip
                    - Nullable changed from true to false
                    - ReadOnly changed from false to true
- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/rancher-clusters/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/rancher-clusters/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [capacity kubernetes_version requested router_ips]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: capacity
            - New property: kubernetes_version
            - New property: requested
            - New property: router_ips
            - Modified property: public_ips
              - Items changed
                - Properties changed
                  - New property: external_ip_address
                  - New property: floating_ip_uuid
                  - Deleted property: cluster
                  - Modified property: floating_ip
                    - Nullable changed from true to false
                    - ReadOnly changed from false to true
- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/rancher-clusters/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: capacity
            - New property: kubernetes_version
            - New property: requested
            - New property: router_ips
            - Modified property: public_ips
              - Items changed
                - Properties changed
                  - New property: external_ip_address
                  - New property: floating_ip_uuid
                  - Deleted property: cluster
                  - Modified property: floating_ip
                    - Nullable changed from true to false
                    - ReadOnly changed from false to true
- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/rancher-clusters/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: capacity
            - New property: kubernetes_version
            - New property: requested
            - New property: router_ips
            - Modified property: public_ips
              - Items changed
                - Properties changed
                  - New property: external_ip_address
                  - New property: floating_ip_uuid
                  - Deleted property: cluster
                  - Modified property: floating_ip
                    - Nullable changed from true to false
                    - ReadOnly changed from false to true
- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/rancher-clusters/{uuid}/create_management_security_group/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: capacity
            - New property: kubernetes_version
            - New property: requested
            - New property: router_ips
            - Modified property: public_ips
              - Items changed
                - Properties changed
                  - New property: external_ip_address
                  - New property: floating_ip_uuid
                  - Deleted property: cluster
                  - Modified property: floating_ip
                    - Nullable changed from true to false
                    - ReadOnly changed from false to true
- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/rancher-clusters/{uuid}/import_yaml/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/rancher-clusters/{uuid}/pull/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/rancher-clusters/{uuid}/unlink/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/rancher-hpas/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/rancher-hpas/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/rancher-hpas/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/rancher-hpas/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/rancher-hpas/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/rancher-hpas/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/rancher-hpas/{uuid}/pull/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/rancher-hpas/{uuid}/unlink/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/rancher-hpas/{uuid}/yaml/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/rancher-hpas/{uuid}/yaml/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/rancher-ingresses/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/rancher-ingresses/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/rancher-ingresses/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/rancher-ingresses/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/rancher-ingresses/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/rancher-ingresses/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/rancher-ingresses/{uuid}/pull/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/rancher-ingresses/{uuid}/unlink/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/rancher-ingresses/{uuid}/yaml/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/rancher-ingresses/{uuid}/yaml/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/rancher-namespaces/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/rancher-namespaces/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/rancher-nodes/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/rancher-nodes/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/rancher-nodes/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/rancher-nodes/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/rancher-nodes/{uuid}/console/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/rancher-nodes/{uuid}/console_log/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/rancher-nodes/{uuid}/link_openstack/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/rancher-nodes/{uuid}/pull/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/rancher-nodes/{uuid}/unlink/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/rancher-nodes/{uuid}/unlink_openstack/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/rancher-projects/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/rancher-projects/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/rancher-projects/{uuid}/secrets/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/rancher-role-templates/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/rancher-role-templates/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/rancher-services/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/rancher-services/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/rancher-services/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/rancher-services/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/rancher-services/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/rancher-services/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/rancher-services/{uuid}/pull/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/rancher-services/{uuid}/unlink/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/rancher-services/{uuid}/yaml/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/rancher-services/{uuid}/yaml/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/rancher-template-versions/{template_uuid}/{version}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/rancher-templates/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/rancher-templates/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/rancher-users/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/rancher-users/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/rancher-workloads/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/rancher-workloads/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/rancher-workloads/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/rancher-workloads/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/rancher-workloads/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/rancher-workloads/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/rancher-workloads/{uuid}/redeploy/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/rancher-workloads/{uuid}/yaml/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/rancher-workloads/{uuid}/yaml/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/remote-eduteams/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/remote-waldur-api/cancel_termination/{uuid}

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/remote-waldur-api/import_offering/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/remote-waldur-api/pull_offering_details/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/remote-waldur-api/pull_offering_invoices/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/remote-waldur-api/pull_offering_orders/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/remote-waldur-api/pull_offering_resources/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/remote-waldur-api/pull_offering_robot_accounts/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/remote-waldur-api/pull_offering_usage/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/remote-waldur-api/pull_offering_users/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/remote-waldur-api/pull_order/{uuid}

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/remote-waldur-api/push_project_data/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/remote-waldur-api/remote_categories/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/remote-waldur-api/remote_customers/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/remote-waldur-api/shared_offerings/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/remote-waldur-api/sync_resource/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/remote-waldur-api/sync_resource_project_permissions/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/roles/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [users_count]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: users_count
- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/roles/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: users_count
- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/roles/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/roles/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [users_count]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: users_count
- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/roles/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: users_count
- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/roles/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: users_count
- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/roles/{uuid}/disable/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/roles/{uuid}/enable/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/roles/{uuid}/update_descriptions/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/service-settings/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/service-settings/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/slurm-allocation-user-usage/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/slurm-allocation-user-usage/{id}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/slurm-allocations/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/slurm-allocations/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/slurm-allocations/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/slurm-allocations/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/slurm-allocations/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/slurm-allocations/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/slurm-allocations/{uuid}/pull/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/slurm-allocations/{uuid}/set_limits/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/slurm-allocations/{uuid}/unlink/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/slurm-associations/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/slurm-associations/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/slurm-jobs/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/slurm-jobs/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/slurm-jobs/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/slurm-jobs/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/slurm-jobs/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/slurm-jobs/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/slurm-jobs/{uuid}/pull/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/slurm-jobs/{uuid}/unlink/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/support-attachments/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/support-attachments/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/support-attachments/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/support-attachments/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/support-comments/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/support-comments/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/support-comments/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/support-comments/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/support-comments/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/support-feedback-average-report/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/support-feedback-report/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/support-feedbacks/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/support-feedbacks/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/support-feedbacks/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/support-issues/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/support-issues/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/support-issues/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/support-issues/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/support-issues/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/support-issues/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/support-issues/{uuid}/comment/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/support-issues/{uuid}/sync/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/support-priorities/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/support-priorities/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/support-statistics/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/support-templates/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/support-templates/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/support-templates/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/support-templates/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/support-templates/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/support-templates/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/support-templates/{uuid}/create_attachments/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/support-templates/{uuid}/delete_attachments/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/support-users/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/support-users/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/sync-issues/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/sync-issues/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/user-agreements/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/user-agreements/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/user-agreements/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/user-agreements/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/user-agreements/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/user-agreements/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/user-group-invitations/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: auto_create_project
              - New property: project_name_template
              - New property: project_role
- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/user-group-invitations/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: auto_create_project
          - New property: project_name_template
          - New property: project_role
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: auto_create_project
            - New property: project_name_template
            - New property: project_role
- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/user-group-invitations/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: auto_create_project
            - New property: project_name_template
            - New property: project_role
- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/user-group-invitations/{uuid}/cancel/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/user-group-invitations/{uuid}/projects/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/user-group-invitations/{uuid}/submit_request/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: auto_create_project
            - New property: project_name_template
            - New property: project_role
- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/user-invitations/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/user-invitations/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/user-invitations/approve/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/user-invitations/reject/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/user-invitations/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/user-invitations/{uuid}/accept/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/user-invitations/{uuid}/cancel/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/user-invitations/{uuid}/check/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/user-invitations/{uuid}/delete/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/user-invitations/{uuid}/details/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/user-invitations/{uuid}/send/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/user-permission-requests/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/user-permission-requests/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/user-permission-requests/{uuid}/approve/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/user-permission-requests/{uuid}/reject/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/user-permissions/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/user-permissions/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/users/

- New query param: username_list
- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/users/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/users/confirm_email/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/users/me/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/users/{user_uuid}/marketplace-checklist-stats/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/users/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/users/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/users/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/users/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/users/{uuid}/cancel_change_email/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/users/{uuid}/change_email/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/users/{uuid}/change_password/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/users/{uuid}/pull_remote_user/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/users/{uuid}/refresh_token/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/users/{uuid}/token/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/version/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/vmware-clusters/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/vmware-clusters/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/vmware-datastores/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/vmware-datastores/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/vmware-disks/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/vmware-disks/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/vmware-disks/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/vmware-disks/{uuid}/extend/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/vmware-disks/{uuid}/pull/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/vmware-disks/{uuid}/unlink/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/vmware-folders/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/vmware-folders/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/vmware-limits/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/vmware-networks/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/vmware-networks/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/vmware-ports/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/vmware-ports/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/vmware-ports/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/vmware-ports/{uuid}/pull/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/vmware-ports/{uuid}/unlink/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/vmware-templates/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/vmware-templates/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/vmware-virtual-machine/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/vmware-virtual-machine/

- Security changed
  - New security requirements: waldurOIDCAuth

DELETE /api/vmware-virtual-machine/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/vmware-virtual-machine/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PATCH /api/vmware-virtual-machine/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

PUT /api/vmware-virtual-machine/{uuid}/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/vmware-virtual-machine/{uuid}/console/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/vmware-virtual-machine/{uuid}/create_disk/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/vmware-virtual-machine/{uuid}/create_port/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/vmware-virtual-machine/{uuid}/pull/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/vmware-virtual-machine/{uuid}/reboot_guest/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/vmware-virtual-machine/{uuid}/reset/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/vmware-virtual-machine/{uuid}/shutdown_guest/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/vmware-virtual-machine/{uuid}/start/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/vmware-virtual-machine/{uuid}/stop/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/vmware-virtual-machine/{uuid}/suspend/

- Security changed
  - New security requirements: waldurOIDCAuth

POST /api/vmware-virtual-machine/{uuid}/unlink/

- Security changed
  - New security requirements: waldurOIDCAuth

GET /api/vmware-virtual-machine/{uuid}/web_console/

- Security changed
  - New security requirements: waldurOIDCAuth

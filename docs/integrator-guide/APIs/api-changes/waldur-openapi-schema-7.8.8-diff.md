# OpenAPI schema diff - 7.8.8

## For version 7.8.8

### New Endpoints: 95

---------------------
POST /api/marketplace-resources/{uuid}/reallocate_limits/  
GET /api/marketplace-slurm-periodic-usage-policies/  
HEAD /api/marketplace-slurm-periodic-usage-policies/  
POST /api/marketplace-slurm-periodic-usage-policies/  
GET /api/marketplace-slurm-periodic-usage-policies/actions/  
HEAD /api/marketplace-slurm-periodic-usage-policies/actions/  
DELETE /api/marketplace-slurm-periodic-usage-policies/{uuid}/  
GET /api/marketplace-slurm-periodic-usage-policies/{uuid}/  
PATCH /api/marketplace-slurm-periodic-usage-policies/{uuid}/  
PUT /api/marketplace-slurm-periodic-usage-policies/{uuid}/  
GET /api/openportal-allocation-user-usage/  
HEAD /api/openportal-allocation-user-usage/  
GET /api/openportal-allocation-user-usage/{id}/  
GET /api/openportal-allocations/  
HEAD /api/openportal-allocations/  
POST /api/openportal-allocations/  
DELETE /api/openportal-allocations/{uuid}/  
GET /api/openportal-allocations/{uuid}/  
PATCH /api/openportal-allocations/{uuid}/  
PUT /api/openportal-allocations/{uuid}/  
POST /api/openportal-allocations/{uuid}/pull/  
POST /api/openportal-allocations/{uuid}/set_limits/  
POST /api/openportal-allocations/{uuid}/unlink/  
GET /api/openportal-associations/  
HEAD /api/openportal-associations/  
GET /api/openportal-associations/{uuid}/  
GET /api/openportal-managed-projects/  
HEAD /api/openportal-managed-projects/  
GET /api/openportal-managed-projects/{identifier}/{destination}/  
HEAD /api/openportal-managed-projects/{identifier}/{destination}/  
POST /api/openportal-managed-projects/{identifier}/{destination}/approve/  
POST /api/openportal-managed-projects/{identifier}/{destination}/attach/  
DELETE /api/openportal-managed-projects/{identifier}/{destination}/delete/  
POST /api/openportal-managed-projects/{identifier}/{destination}/detach/  
POST /api/openportal-managed-projects/{identifier}/{destination}/reject/  
GET /api/openportal-project-template/  
HEAD /api/openportal-project-template/  
POST /api/openportal-project-template/  
DELETE /api/openportal-project-template/{uuid}/  
GET /api/openportal-project-template/{uuid}/  
PATCH /api/openportal-project-template/{uuid}/  
PUT /api/openportal-project-template/{uuid}/  
DELETE /api/openportal-project-template/{uuid}/delete/  
GET /api/openportal-projectinfo/  
HEAD /api/openportal-projectinfo/  
POST /api/openportal-projectinfo/  
DELETE /api/openportal-projectinfo/{project}/  
GET /api/openportal-projectinfo/{project}/  
PATCH /api/openportal-projectinfo/{project}/  
PUT /api/openportal-projectinfo/{project}/  
PUT /api/openportal-projectinfo/{project}/set_allowed_destinations/  
PUT /api/openportal-projectinfo/{project}/set_shortname/  
GET /api/openportal-remote-allocations/  
HEAD /api/openportal-remote-allocations/  
POST /api/openportal-remote-allocations/  
DELETE /api/openportal-remote-allocations/{uuid}/  
GET /api/openportal-remote-allocations/{uuid}/  
PATCH /api/openportal-remote-allocations/{uuid}/  
PUT /api/openportal-remote-allocations/{uuid}/  
POST /api/openportal-remote-allocations/{uuid}/pull/  
POST /api/openportal-remote-allocations/{uuid}/set_limits/  
POST /api/openportal-remote-allocations/{uuid}/unlink/  
GET /api/openportal-remote-associations/  
HEAD /api/openportal-remote-associations/  
GET /api/openportal-remote-associations/{uuid}/  
GET /api/openportal-unmanaged-projects/  
HEAD /api/openportal-unmanaged-projects/  
POST /api/openportal-unmanaged-projects/  
GET /api/openportal-unmanaged-projects/checklist-template/  
HEAD /api/openportal-unmanaged-projects/checklist-template/  
DELETE /api/openportal-unmanaged-projects/{uuid}/  
GET /api/openportal-unmanaged-projects/{uuid}/  
PATCH /api/openportal-unmanaged-projects/{uuid}/  
PUT /api/openportal-unmanaged-projects/{uuid}/  
POST /api/openportal-unmanaged-projects/{uuid}/add_user/  
GET /api/openportal-unmanaged-projects/{uuid}/checklist/  
GET /api/openportal-unmanaged-projects/{uuid}/completion_status/  
POST /api/openportal-unmanaged-projects/{uuid}/delete_user/  
GET /api/openportal-unmanaged-projects/{uuid}/list_users/  
POST /api/openportal-unmanaged-projects/{uuid}/move_project/  
POST /api/openportal-unmanaged-projects/{uuid}/recover/  
GET /api/openportal-unmanaged-projects/{uuid}/stats/  
POST /api/openportal-unmanaged-projects/{uuid}/submit_answers/  
POST /api/openportal-unmanaged-projects/{uuid}/update_user/  
GET /api/openportal-userinfo/  
HEAD /api/openportal-userinfo/  
POST /api/openportal-userinfo/  
GET /api/openportal-userinfo/me/  
HEAD /api/openportal-userinfo/me/  
DELETE /api/openportal-userinfo/{user}/  
GET /api/openportal-userinfo/{user}/  
PATCH /api/openportal-userinfo/{user}/  
PUT /api/openportal-userinfo/{user}/  
PUT /api/openportal-userinfo/{user}/set_shortname/  
POST /api/openstack-tenants/{uuid}/push_security_groups/  

### Deleted Endpoints: None

---------------------------

### Modified Endpoints: 904

---------------------------
POST /api-auth/logout/

- Summary changed from '' to 'Log out'
- Description changed from 'Logout from the system. If single logout is supported, returns logout URL.' to 'Logs out the current user by deleting their authentication token. If single logout (SLO) is supported for the current authentication method (e.g., SAML2 or OIDC), this endpoint may return a logout URL to which the user should be redirected to complete the logout process on the identity provider side.'

POST /api-auth/password/

- Summary changed from '' to 'Obtain authentication token'
- Description changed from '' to 'Authenticates a user with username and password and returns an authentication token.'

GET /api/access-subnets/

- Summary changed from '' to 'List access subnets'
- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Retrieve a list of access subnets. Staff and support users can see all subnets, while other users can only see subnets associated with customers they have a role in.'

HEAD /api/access-subnets/

- Summary changed from '' to 'List access subnets'

POST /api/access-subnets/

- Summary changed from '' to 'Create an access subnet'
- Description changed from '' to 'Create a new access subnet for a customer.'

DELETE /api/access-subnets/{uuid}/

- Summary changed from '' to 'Delete an access subnet'
- Description changed from '' to 'Delete an existing access subnet.'

GET /api/access-subnets/{uuid}/

- Summary changed from '' to 'Retrieve access subnet'
- Description changed from '' to 'Fetch the details of a specific access subnet by its UUID.'

PATCH /api/access-subnets/{uuid}/

- Summary changed from '' to 'Partially update an access subnet'
- Description changed from '' to 'Partially update an existing access subnet.'

PUT /api/access-subnets/{uuid}/

- Summary changed from '' to 'Update an access subnet'
- Description changed from '' to 'Update an existing access subnet.'

GET /api/admin-announcements/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/auth-tokens/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/aws-images/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/aws-instances/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

POST /api/aws-instances/{uuid}/pull/

- Summary changed from '' to 'Synchronize resource state'
- Description changed from '' to 'Schedule an asynchronous pull operation to synchronize resource state from the backend. Returns 202 if the pull was scheduled successfully, or 409 if the pull operation is not implemented for this resource type.'
- Responses changed
  - New response: 202
  - New response: 409
  - Deleted response: 200

POST /api/aws-instances/{uuid}/unlink/

- Summary changed from '' to 'Unlink resource'
- Description changed from 'Delete resource from the database without scheduling operations on backend
and without checking current state of the resource. It is intended to be used
for removing resource stuck in transitioning state.' to 'Delete resource from the database without scheduling operations on backend
        and without checking current state of the resource. It is intended to be used
        for removing resource stuck in transitioning state.'
- Responses changed
  - New response: 204
  - Deleted response: 200

GET /api/aws-regions/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/aws-sizes/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/aws-volumes/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

POST /api/aws-volumes/{uuid}/pull/

- Summary changed from '' to 'Synchronize resource state'
- Description changed from '' to 'Schedule an asynchronous pull operation to synchronize resource state from the backend. Returns 202 if the pull was scheduled successfully, or 409 if the pull operation is not implemented for this resource type.'
- Responses changed
  - New response: 202
  - New response: 409
  - Deleted response: 200

POST /api/aws-volumes/{uuid}/unlink/

- Summary changed from '' to 'Unlink resource'
- Description changed from 'Delete resource from the database without scheduling operations on backend
and without checking current state of the resource. It is intended to be used
for removing resource stuck in transitioning state.' to 'Delete resource from the database without scheduling operations on backend
        and without checking current state of the resource. It is intended to be used
        for removing resource stuck in transitioning state.'
- Responses changed
  - New response: 204
  - Deleted response: 200

GET /api/azure-images/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/azure-locations/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/azure-public-ips/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

POST /api/azure-public-ips/{uuid}/pull/

- Summary changed from '' to 'Synchronize resource state'
- Description changed from '' to 'Schedule an asynchronous pull operation to synchronize resource state from the backend. Returns 202 if the pull was scheduled successfully, or 409 if the pull operation is not implemented for this resource type.'
- Responses changed
  - New response: 202
  - New response: 409
  - Deleted response: 200

POST /api/azure-public-ips/{uuid}/unlink/

- Summary changed from '' to 'Unlink resource'
- Description changed from 'Delete resource from the database without scheduling operations on backend
and without checking current state of the resource. It is intended to be used
for removing resource stuck in transitioning state.' to 'Delete resource from the database without scheduling operations on backend
        and without checking current state of the resource. It is intended to be used
        for removing resource stuck in transitioning state.'
- Responses changed
  - New response: 204
  - Deleted response: 200

GET /api/azure-resource-groups/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/azure-sizes/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/azure-sql-databases/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

POST /api/azure-sql-databases/{uuid}/pull/

- Summary changed from '' to 'Synchronize resource state'
- Description changed from '' to 'Schedule an asynchronous pull operation to synchronize resource state from the backend. Returns 202 if the pull was scheduled successfully, or 409 if the pull operation is not implemented for this resource type.'
- Responses changed
  - New response: 202
  - New response: 409
  - Deleted response: 200

POST /api/azure-sql-databases/{uuid}/unlink/

- Summary changed from '' to 'Unlink resource'
- Description changed from 'Delete resource from the database without scheduling operations on backend
and without checking current state of the resource. It is intended to be used
for removing resource stuck in transitioning state.' to 'Delete resource from the database without scheduling operations on backend
        and without checking current state of the resource. It is intended to be used
        for removing resource stuck in transitioning state.'
- Responses changed
  - New response: 204
  - Deleted response: 200

GET /api/azure-sql-servers/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

POST /api/azure-sql-servers/{uuid}/pull/

- Summary changed from '' to 'Synchronize resource state'
- Description changed from '' to 'Schedule an asynchronous pull operation to synchronize resource state from the backend. Returns 202 if the pull was scheduled successfully, or 409 if the pull operation is not implemented for this resource type.'
- Responses changed
  - New response: 202
  - New response: 409
  - Deleted response: 200

POST /api/azure-sql-servers/{uuid}/unlink/

- Summary changed from '' to 'Unlink resource'
- Description changed from 'Delete resource from the database without scheduling operations on backend
and without checking current state of the resource. It is intended to be used
for removing resource stuck in transitioning state.' to 'Delete resource from the database without scheduling operations on backend
        and without checking current state of the resource. It is intended to be used
        for removing resource stuck in transitioning state.'
- Responses changed
  - New response: 204
  - Deleted response: 200

GET /api/azure-virtualmachines/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

POST /api/azure-virtualmachines/{uuid}/pull/

- Summary changed from '' to 'Synchronize resource state'
- Description changed from '' to 'Schedule an asynchronous pull operation to synchronize resource state from the backend. Returns 202 if the pull was scheduled successfully, or 409 if the pull operation is not implemented for this resource type.'
- Responses changed
  - New response: 202
  - New response: 409
  - Deleted response: 200

POST /api/azure-virtualmachines/{uuid}/unlink/

- Summary changed from '' to 'Unlink resource'
- Description changed from 'Delete resource from the database without scheduling operations on backend
and without checking current state of the resource. It is intended to be used
for removing resource stuck in transitioning state.' to 'Delete resource from the database without scheduling operations on backend
        and without checking current state of the resource. It is intended to be used
        for removing resource stuck in transitioning state.'
- Responses changed
  - New response: 204
  - Deleted response: 200

GET /api/backend-resource-requests/

- Summary changed from '' to 'List backend resource requests'
- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Returns a paginated list of requests for backend resources.'

HEAD /api/backend-resource-requests/

- Summary changed from '' to 'List backend resource requests'

POST /api/backend-resource-requests/

- Summary changed from '' to 'Create a backend resource request'
- Description changed from '' to 'Creates a new request to fetch a list of importable resources from a backend. This is typically used by staff to trigger a site agent to report available resources.'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Examples changed
        - New example: RequestResourcesForAnOffering
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Examples changed
          - New example: RequestResourcesForAnOffering

GET /api/backend-resource-requests/{uuid}/

- Summary changed from '' to 'Retrieve a backend resource request'
- Description changed from '' to 'Returns the details of a specific backend resource request.'

POST /api/backend-resource-requests/{uuid}/set_done/

- Summary changed from '' to 'Mark a request as done'
- Description changed from '' to 'Transitions the request state from 'Processing' to 'Done'. This is used by a site agent to signal that it has successfully reported all available resources.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: status
          - AdditionalProperties changed
            - Schema deleted

POST /api/backend-resource-requests/{uuid}/set_erred/

- Summary changed from '' to 'Mark a request as erred'
- Description changed from '' to 'Transitions the request state to 'Erred'. This is used by a site agent to report a failure during the resource fetching process. An error message and traceback should be provided.'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Examples changed
        - New example: ReportAnError
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: status
          - AdditionalProperties changed
            - Schema deleted
        - Examples changed
          - New example: ReportAnError

POST /api/backend-resource-requests/{uuid}/start_processing/

- Summary changed from '' to 'Start processing a request'
- Description changed from '' to 'Transitions the request state from 'Sent' to 'Processing'. This is used by a site agent to acknowledge that it has started fetching the resource list.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: status
          - AdditionalProperties changed
            - Schema deleted

GET /api/backend-resources/

- Summary changed from '' to 'List backend resources'
- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Returns a paginated list of backend resources that are available for import. This endpoint is typically used by site agents to see which resources they have reported.'

HEAD /api/backend-resources/

- Summary changed from '' to 'List backend resources'

POST /api/backend-resources/

- Summary changed from '' to 'Create a backend resource'
- Description changed from '' to 'Creates a new backend resource record. This is typically done by a site agent to report a resource that is available for import into the marketplace.'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Examples changed
        - New example: CreateABackendResource
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Examples changed
          - New example: CreateABackendResource

DELETE /api/backend-resources/{uuid}/

- Summary changed from '' to 'Delete a backend resource'
- Description changed from '' to 'Deletes a backend resource record. This is typically done when the resource is no longer available for import.'

GET /api/backend-resources/{uuid}/

- Summary changed from '' to 'Retrieve a backend resource'
- Description changed from '' to 'Returns the details of a specific backend resource.'

POST /api/backend-resources/{uuid}/import_resource/

- Summary changed from '' to 'Import a backend resource (staff only)'
- Description changed from '' to '
        Converts a backend resource into a full marketplace resource. This action is restricted to staff users.
        Upon successful import, the original backend resource record is deleted. A fake order in the 'done'
        state is created to represent the import event.
        '
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Examples changed
        - New example: ImportWithASpecificPlan
        - New example: ImportWithoutAPlan(forPrivateOfferings)
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: slug
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: slug
        - Examples changed
          - New example: ImportWithASpecificPlan
          - New example: ImportWithoutAPlan(forPrivateOfferings)

GET /api/booking-offerings/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/booking-resources/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''
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
                      - New property: slug
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: slug

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
                    - New property: slug
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: slug

GET /api/broadcast-message-templates/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/broadcast-messages/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/call-managing-organisations/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

POST /api/call-managing-organisations/{uuid}/add_user/

- Summary changed from '' to 'Grant a role to a user'
- Description changed from '' to 'Assigns a specific role to a user within the current scope. An optional expiration time for the role can be set.'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Examples changed
        - New example: GrantProjectAdminRoleUntilEndOfYear
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Examples changed
          - New example: SuccessfulRoleGrantResponse
  - Modified response: 400
    - Description changed from '' to 'Validation error, for example when trying to add a user to a terminated project.'
    - Content changed
      - Deleted media type: application/json

POST /api/call-managing-organisations/{uuid}/delete_user/

- Summary changed from '' to 'Revoke a role from a user'
- Description changed from '' to 'Removes a specific role from a user within the current scope. This effectively revokes their permissions associated with that role.'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Examples changed
        - New example: RevokeProjectAdminRoleFromUser
- Responses changed
  - Modified response: 200
    - Description changed from 'No response body' to 'Role revoked successfully.'

GET /api/call-managing-organisations/{uuid}/list_users/

- Summary changed from '' to 'List users and their roles in a scope'
- Description changed from '' to 'Retrieves a list of users who have a role within a specific scope (e.g., a project or an organization). The list can be filtered by user details or role.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Examples changed
          - New example: ExampleUserRoleListResponse

POST /api/call-managing-organisations/{uuid}/update_user/

- Summary changed from '' to 'Update a user's role expiration'
- Description changed from '' to 'Updates the expiration time for a user's existing role in the current scope. This is useful for extending or shortening the duration of a permission. To make a role permanent, set expiration_time to null.'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Examples changed
        - New example: ExtendRoleUntilMid-2025
        - New example: MakeARolePermanent
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Examples changed
          - New example: SuccessfulRoleUpdateResponse

GET /api/call-proposal-project-role-mappings/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/call-rounds/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/celery-stats/

- Summary changed from '' to 'Get Celery worker statistics'
- Description changed from '' to 'Provides a snapshot of the Celery workers' status, including active, scheduled, reserved, and revoked tasks, as well as worker-specific statistics. Requires support user permissions.'
- Responses changed
  - Modified response: 200
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

GET /api/checklists-admin-categories/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/checklists-admin-question-dependencies/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/checklists-admin-question-options/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/checklists-admin-questions/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: allowed_file_types
              - New property: allowed_mime_types
              - New property: max_file_size_mb
              - New property: max_files_count
              - Modified property: question_type
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/QuestionTypeEnum
                    - New enum values: [multiple_files]

POST /api/checklists-admin-questions/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: allowed_file_types
          - New property: allowed_mime_types
          - New property: max_file_size_mb
          - New property: max_files_count
          - Modified property: question_type
            - Property 'AllOf' changed
              - Modified schema: #/components/schemas/QuestionTypeEnum
                - New enum values: [multiple_files]
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: allowed_file_types
            - New property: allowed_mime_types
            - New property: max_file_size_mb
            - New property: max_files_count
            - Modified property: question_type
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/QuestionTypeEnum
                  - New enum values: [multiple_files]

GET /api/checklists-admin-questions/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: allowed_file_types
            - New property: allowed_mime_types
            - New property: max_file_size_mb
            - New property: max_files_count
            - Modified property: question_type
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/QuestionTypeEnum
                  - New enum values: [multiple_files]

PATCH /api/checklists-admin-questions/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: allowed_file_types
          - New property: allowed_mime_types
          - New property: max_file_size_mb
          - New property: max_files_count
          - Modified property: question_type
            - Property 'AllOf' changed
              - Modified schema: #/components/schemas/QuestionTypeEnum
                - New enum values: [multiple_files]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: allowed_file_types
            - New property: allowed_mime_types
            - New property: max_file_size_mb
            - New property: max_files_count
            - Modified property: question_type
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/QuestionTypeEnum
                  - New enum values: [multiple_files]

PUT /api/checklists-admin-questions/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: allowed_file_types
          - New property: allowed_mime_types
          - New property: max_file_size_mb
          - New property: max_files_count
          - Modified property: question_type
            - Property 'AllOf' changed
              - Modified schema: #/components/schemas/QuestionTypeEnum
                - New enum values: [multiple_files]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: allowed_file_types
            - New property: allowed_mime_types
            - New property: max_file_size_mb
            - New property: max_files_count
            - Modified property: question_type
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/QuestionTypeEnum
                  - New enum values: [multiple_files]

GET /api/checklists-admin/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/checklists-admin/{uuid}/questions/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: allowed_file_types
              - New property: allowed_mime_types
              - New property: max_file_size_mb
              - New property: max_files_count
              - Modified property: question_type
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/QuestionTypeEnum
                    - New enum values: [multiple_files]

GET /api/component-user-usage-limits/

- Summary changed from '' to 'List component usage limits for users'
- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Returns a paginated list of usage limits set for specific users on resource components.'

HEAD /api/component-user-usage-limits/

- Summary changed from '' to 'List component usage limits for users'

POST /api/component-user-usage-limits/

- Summary changed from '' to 'Create a component usage limit for a user'
- Description changed from '' to 'Sets a usage limit for a specific user on a resource's component. This is only applicable for offerings that support per-user consumption limitation.'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Examples changed
        - New example: SetACPUUsageLimitForAUser
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Examples changed
          - New example: SetACPUUsageLimitForAUser

DELETE /api/component-user-usage-limits/{uuid}/

- Summary changed from '' to 'Delete a component usage limit'
- Description changed from '' to 'Removes a usage limit for a user on a component.'

GET /api/component-user-usage-limits/{uuid}/

- Summary changed from '' to 'Retrieve a component usage limit'
- Description changed from '' to 'Returns the details of a specific user's usage limit for a component.'

PATCH /api/component-user-usage-limits/{uuid}/

- Summary changed from '' to 'Partially update a component usage limit'
- Description changed from '' to 'Partially updates an existing usage limit for a user on a component.'

PUT /api/component-user-usage-limits/{uuid}/

- Summary changed from '' to 'Update a component usage limit'
- Description changed from '' to 'Updates an existing usage limit for a user on a component.'

GET /api/configuration/

- Summary changed from '' to 'Get public configuration'
- Description changed from 'Retrieve public settings' to 'Returns a dictionary of public settings for the Waldur deployment. This includes feature flags, authentication methods, and other configuration details that are safe to expose to any user.'

GET /api/customer-credits/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/customer-permissions-reviews/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

POST /api/customer-permissions-reviews/{uuid}/close/

- Summary changed from '' to 'Close customer permission review'
- Description changed from 'Close customer permission review.' to ''

GET /api/customers/

- Summary changed from '' to 'List customers'
- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Retrieve a list of customers. The list is filtered based on the user's permissions.'
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [grace_period_days]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: grace_period_days
              - Modified property: access_subnets
                - ReadOnly changed from true to false
              - Modified property: accounting_start_date
                - ReadOnly changed from true to false
              - Modified property: agreement_number
                - ReadOnly changed from true to false
              - Modified property: archived
                - ReadOnly changed from true to false
              - Modified property: blocked
                - ReadOnly changed from true to false
              - Modified property: default_tax_percent
                - ReadOnly changed from true to false
              - Modified property: display_billing_info_in_projects
                - ReadOnly changed from true to false
              - Modified property: domain
                - ReadOnly changed from true to false
              - Modified property: max_service_accounts
                - ReadOnly changed from true to false
              - Modified property: project_metadata_checklist
                - ReadOnly changed from true to false
              - Modified property: sponsor_number
                - ReadOnly changed from true to false

HEAD /api/customers/

- Summary changed from '' to 'List customers'

POST /api/customers/

- Summary changed from '' to 'Create a new customer'
- Description changed from 'A new customer can only be created by users with staff privilege' to 'A new customer can only be created by users with staff privilege.'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: access_subnets
          - New property: accounting_start_date
          - New property: agreement_number
          - New property: archived
          - New property: blocked
          - New property: default_tax_percent
          - New property: display_billing_info_in_projects
          - New property: domain
          - New property: grace_period_days
          - New property: max_service_accounts
          - New property: project_metadata_checklist
          - New property: sponsor_number
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: access_subnets
          - New property: accounting_start_date
          - New property: agreement_number
          - New property: archived
          - New property: blocked
          - New property: default_tax_percent
          - New property: display_billing_info_in_projects
          - New property: domain
          - New property: grace_period_days
          - New property: max_service_accounts
          - New property: project_metadata_checklist
          - New property: sponsor_number
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: access_subnets
          - New property: accounting_start_date
          - New property: agreement_number
          - New property: archived
          - New property: blocked
          - New property: default_tax_percent
          - New property: display_billing_info_in_projects
          - New property: domain
          - New property: grace_period_days
          - New property: max_service_accounts
          - New property: project_metadata_checklist
          - New property: sponsor_number
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: grace_period_days
            - Modified property: access_subnets
              - ReadOnly changed from true to false
            - Modified property: accounting_start_date
              - ReadOnly changed from true to false
            - Modified property: agreement_number
              - ReadOnly changed from true to false
            - Modified property: archived
              - ReadOnly changed from true to false
            - Modified property: blocked
              - ReadOnly changed from true to false
            - Modified property: default_tax_percent
              - ReadOnly changed from true to false
            - Modified property: display_billing_info_in_projects
              - ReadOnly changed from true to false
            - Modified property: domain
              - ReadOnly changed from true to false
            - Modified property: max_service_accounts
              - ReadOnly changed from true to false
            - Modified property: project_metadata_checklist
              - ReadOnly changed from true to false
            - Modified property: sponsor_number
              - ReadOnly changed from true to false

GET /api/customers/countries/

- Summary changed from '' to 'Get list of available countries'
- Description changed from 'Return list of countries' to 'Returns a list of countries that can be used when creating or updating a customer. The list can be configured by the service provider.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Examples changed
          - New example: CountryListResponse

HEAD /api/customers/countries/

- Summary changed from '' to 'Get list of available countries'

GET /api/customers/{customer_uuid}/project-metadata-compliance-details/

- Summary changed from '' to 'Get detailed project metadata compliance'
- Description changed from 'Get detailed project compliance information with database-level pagination.' to 'Provides detailed compliance status for all projects within a customer, including individual answers and completion status.'

GET /api/customers/{customer_uuid}/project-metadata-compliance-overview/

- Summary changed from '' to 'Get project metadata compliance overview'
- Description changed from 'Get compliance overview statistics for all projects.' to 'Provides aggregated statistics about project metadata compliance for all projects within a customer.'

GET /api/customers/{customer_uuid}/project-metadata-compliance-projects/

- Summary changed from '' to 'List projects with compliance data'
- Description changed from 'List project checklist answer data with database-level pagination.' to 'Provides a paginated list of projects with their checklist completion status and answer details.'

GET /api/customers/{customer_uuid}/project-metadata-question-answers/

- Summary changed from '' to 'List questions with project answers'
- Description changed from 'List questions with project answers, paginated by question at database level.' to 'Provides a paginated list of all questions from the customer's compliance checklist, including the answers given in each project.'

GET /api/customers/{customer_uuid}/users/

- Summary changed from '' to 'List users of a customer'
- Description changed from 'A list of users connected to the customer.' to 'Lists all users who have a role in the specified customer or any of its projects. Requires permissions to list customer users.'

DELETE /api/customers/{uuid}/

- Summary changed from '' to 'Delete a customer'
- Description changed from 'If a customer has connected projects, deletion request will fail with 409 response code.' to 'Delete a customer. This action is only available to staff users. If a customer has any active projects, the deletion request will fail with a 409 Conflict response.'

GET /api/customers/{uuid}/

- Summary changed from '' to 'Retrieve customer details'
- Description changed from '' to 'Fetch the details of a specific customer by its UUID.'
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [grace_period_days]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: grace_period_days
            - Modified property: access_subnets
              - ReadOnly changed from true to false
            - Modified property: accounting_start_date
              - ReadOnly changed from true to false
            - Modified property: agreement_number
              - ReadOnly changed from true to false
            - Modified property: archived
              - ReadOnly changed from true to false
            - Modified property: blocked
              - ReadOnly changed from true to false
            - Modified property: default_tax_percent
              - ReadOnly changed from true to false
            - Modified property: display_billing_info_in_projects
              - ReadOnly changed from true to false
            - Modified property: domain
              - ReadOnly changed from true to false
            - Modified property: max_service_accounts
              - ReadOnly changed from true to false
            - Modified property: project_metadata_checklist
              - ReadOnly changed from true to false
            - Modified property: sponsor_number
              - ReadOnly changed from true to false

PATCH /api/customers/{uuid}/

- Summary changed from '' to 'Partially update a customer'
- Description changed from '' to 'Partially update the details of an existing customer. Requires customer owner or staff permissions.'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: access_subnets
          - New property: accounting_start_date
          - New property: agreement_number
          - New property: archived
          - New property: blocked
          - New property: default_tax_percent
          - New property: display_billing_info_in_projects
          - New property: domain
          - New property: grace_period_days
          - New property: max_service_accounts
          - New property: project_metadata_checklist
          - New property: sponsor_number
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: access_subnets
          - New property: accounting_start_date
          - New property: agreement_number
          - New property: archived
          - New property: blocked
          - New property: default_tax_percent
          - New property: display_billing_info_in_projects
          - New property: domain
          - New property: grace_period_days
          - New property: max_service_accounts
          - New property: project_metadata_checklist
          - New property: sponsor_number
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: access_subnets
          - New property: accounting_start_date
          - New property: agreement_number
          - New property: archived
          - New property: blocked
          - New property: default_tax_percent
          - New property: display_billing_info_in_projects
          - New property: domain
          - New property: grace_period_days
          - New property: max_service_accounts
          - New property: project_metadata_checklist
          - New property: sponsor_number
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: grace_period_days
            - Modified property: access_subnets
              - ReadOnly changed from true to false
            - Modified property: accounting_start_date
              - ReadOnly changed from true to false
            - Modified property: agreement_number
              - ReadOnly changed from true to false
            - Modified property: archived
              - ReadOnly changed from true to false
            - Modified property: blocked
              - ReadOnly changed from true to false
            - Modified property: default_tax_percent
              - ReadOnly changed from true to false
            - Modified property: display_billing_info_in_projects
              - ReadOnly changed from true to false
            - Modified property: domain
              - ReadOnly changed from true to false
            - Modified property: max_service_accounts
              - ReadOnly changed from true to false
            - Modified property: project_metadata_checklist
              - ReadOnly changed from true to false
            - Modified property: sponsor_number
              - ReadOnly changed from true to false

PUT /api/customers/{uuid}/

- Summary changed from '' to 'Update a customer'
- Description changed from '' to 'Update the details of an existing customer. Requires customer owner or staff permissions.'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: access_subnets
          - New property: accounting_start_date
          - New property: agreement_number
          - New property: archived
          - New property: blocked
          - New property: default_tax_percent
          - New property: display_billing_info_in_projects
          - New property: domain
          - New property: grace_period_days
          - New property: max_service_accounts
          - New property: project_metadata_checklist
          - New property: sponsor_number
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: access_subnets
          - New property: accounting_start_date
          - New property: agreement_number
          - New property: archived
          - New property: blocked
          - New property: default_tax_percent
          - New property: display_billing_info_in_projects
          - New property: domain
          - New property: grace_period_days
          - New property: max_service_accounts
          - New property: project_metadata_checklist
          - New property: sponsor_number
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: access_subnets
          - New property: accounting_start_date
          - New property: agreement_number
          - New property: archived
          - New property: blocked
          - New property: default_tax_percent
          - New property: display_billing_info_in_projects
          - New property: domain
          - New property: grace_period_days
          - New property: max_service_accounts
          - New property: project_metadata_checklist
          - New property: sponsor_number
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: grace_period_days
            - Modified property: access_subnets
              - ReadOnly changed from true to false
            - Modified property: accounting_start_date
              - ReadOnly changed from true to false
            - Modified property: agreement_number
              - ReadOnly changed from true to false
            - Modified property: archived
              - ReadOnly changed from true to false
            - Modified property: blocked
              - ReadOnly changed from true to false
            - Modified property: default_tax_percent
              - ReadOnly changed from true to false
            - Modified property: display_billing_info_in_projects
              - ReadOnly changed from true to false
            - Modified property: domain
              - ReadOnly changed from true to false
            - Modified property: max_service_accounts
              - ReadOnly changed from true to false
            - Modified property: project_metadata_checklist
              - ReadOnly changed from true to false
            - Modified property: sponsor_number
              - ReadOnly changed from true to false

POST /api/customers/{uuid}/add_user/

- Summary changed from '' to 'Grant a role to a user'
- Description changed from '' to 'Assigns a specific role to a user within the current scope. An optional expiration time for the role can be set.'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Examples changed
        - New example: GrantProjectAdminRoleUntilEndOfYear
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Examples changed
          - New example: SuccessfulRoleGrantResponse
  - Modified response: 400
    - Description changed from '' to 'Validation error, for example when trying to add a user to a terminated project.'
    - Content changed
      - Deleted media type: application/json

POST /api/customers/{uuid}/delete_user/

- Summary changed from '' to 'Revoke a role from a user'
- Description changed from '' to 'Removes a specific role from a user within the current scope. This effectively revokes their permissions associated with that role.'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Examples changed
        - New example: RevokeProjectAdminRoleFromUser
- Responses changed
  - Modified response: 200
    - Description changed from 'No response body' to 'Role revoked successfully.'

GET /api/customers/{uuid}/list_users/

- Summary changed from '' to 'List users and their roles in a scope'
- Description changed from '' to 'Retrieves a list of users who have a role within a specific scope (e.g., a project or an organization). The list can be filtered by user details or role.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Examples changed
          - New example: ExampleUserRoleListResponse

GET /api/customers/{uuid}/stats/

- Summary changed from '' to 'Get customer resource usage statistics'
- Description changed from 'Return statistics about customer resources usage' to 'Provides statistics about the resource usage (e.g., CPU, RAM, storage) for all projects within a customer. Can be filtered to show usage for the current month only.'
- Modified query param: for_current_month
  - Description changed from '' to 'If true, returns usage data for the current month only. Otherwise, returns total usage.'

POST /api/customers/{uuid}/update_organization_groups/

- Summary changed from '' to 'Update organization groups for a customer'
- Description changed from 'Update organization groups for customer' to 'Assigns a customer to one or more organization groups. This action is restricted to staff users.'

POST /api/customers/{uuid}/update_user/

- Summary changed from '' to 'Update a user's role expiration'
- Description changed from '' to 'Updates the expiration time for a user's existing role in the current scope. This is useful for extending or shortening the duration of a permission. To make a role permanent, set expiration_time to null.'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Examples changed
        - New example: ExtendRoleUntilMid-2025
        - New example: MakeARolePermanent
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Examples changed
          - New example: SuccessfulRoleUpdateResponse

GET /api/database-stats/

- Summary changed from '' to 'Get database table statistics'
- Description changed from '' to 'Retrieves statistics about the database, including the top 10 largest tables by total size. This information is useful for monitoring and maintenance. Requires support user permissions.'

GET /api/digitalocean-droplets/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

POST /api/digitalocean-droplets/{uuid}/pull/

- Summary changed from '' to 'Synchronize resource state'
- Description changed from '' to 'Schedule an asynchronous pull operation to synchronize resource state from the backend. Returns 202 if the pull was scheduled successfully, or 409 if the pull operation is not implemented for this resource type.'
- Responses changed
  - New response: 202
  - New response: 409
  - Deleted response: 200

POST /api/digitalocean-droplets/{uuid}/unlink/

- Summary changed from '' to 'Unlink resource'
- Description changed from 'Delete resource from the database without scheduling operations on backend
and without checking current state of the resource. It is intended to be used
for removing resource stuck in transitioning state.' to 'Delete resource from the database without scheduling operations on backend
        and without checking current state of the resource. It is intended to be used
        for removing resource stuck in transitioning state.'
- Responses changed
  - New response: 204
  - Deleted response: 200

GET /api/digitalocean-images/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/digitalocean-regions/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/digitalocean-sizes/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/email-logs/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/event-subscriptions/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/events-stats/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/events/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/external-links/

- Summary changed from '' to 'List external links'
- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Retrieve a list of external links available in the system.'

HEAD /api/external-links/

- Summary changed from '' to 'List external links'

POST /api/external-links/

- Summary changed from '' to 'Create an external link'
- Description changed from '' to 'Create a new external link. This action is restricted to staff users.'

DELETE /api/external-links/{uuid}/

- Summary changed from '' to 'Delete an external link'
- Description changed from '' to 'Delete an existing external link. This action is restricted to staff users.'

GET /api/external-links/{uuid}/

- Summary changed from '' to 'Retrieve external link'
- Description changed from '' to 'Fetch the details of a specific external link by its UUID.'

PATCH /api/external-links/{uuid}/

- Summary changed from '' to 'Partially update an external link'
- Description changed from '' to 'Partially update an existing external link. This action is restricted to staff users.'

PUT /api/external-links/{uuid}/

- Summary changed from '' to 'Update an external link'
- Description changed from '' to 'Update an existing external link. This action is restricted to staff users.'

POST /api/feature-values/

- Summary changed from '' to 'Update feature flags'
- Description changed from 'Override feature values' to 'Allows administrators to enable or disable specific feature flags in the system. The request should be a dictionary where keys are feature sections and values are dictionaries of feature keys and their boolean state.'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Examples changed
        - New example: UpdateUserAndMarketplaceFeatures
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Examples changed
          - New example: SuccessfulResponse

GET /api/financial-reports/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/freeipa-profiles/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/google-auth/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/hooks-email/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/hooks-web/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/hooks/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/identity-providers/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/invoice-items/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/invoices/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/keycloak-groups/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/keycloak-user-group-memberships/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/keys/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/lexis-links/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/maintenance-announcement-offerings/

- Summary changed from '' to 'List affected offerings for maintenance'
- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Returns a paginated list of offerings affected by maintenance announcements.'

HEAD /api/maintenance-announcement-offerings/

- Summary changed from '' to 'List affected offerings for maintenance'

POST /api/maintenance-announcement-offerings/

- Summary changed from '' to 'Link an offering to a maintenance announcement'
- Description changed from '' to 'Creates a new association between an offering and a maintenance announcement, specifying the expected impact.'

DELETE /api/maintenance-announcement-offerings/{uuid}/

- Summary changed from '' to 'Unlink an offering from a maintenance announcement'
- Description changed from '' to 'Removes the association between an offering and a maintenance announcement.'

GET /api/maintenance-announcement-offerings/{uuid}/

- Summary changed from '' to 'Retrieve an affected offering link'
- Description changed from '' to 'Returns the details of a specific link between a maintenance announcement and an offering, including the impact level and description.'

PATCH /api/maintenance-announcement-offerings/{uuid}/

- Summary changed from '' to 'Partially update an affected offering link'
- Description changed from '' to 'Partially updates the impact level or description for an offering linked to a maintenance announcement.'

PUT /api/maintenance-announcement-offerings/{uuid}/

- Summary changed from '' to 'Update an affected offering link'
- Description changed from '' to 'Updates the impact level or description for an offering linked to a maintenance announcement.'

GET /api/maintenance-announcement-template-offerings/

- Summary changed from '' to 'List affected offering templates'
- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Returns a paginated list of associations between maintenance announcement templates and offerings.'

HEAD /api/maintenance-announcement-template-offerings/

- Summary changed from '' to 'List affected offering templates'

POST /api/maintenance-announcement-template-offerings/

- Summary changed from '' to 'Link an offering to a maintenance template'
- Description changed from '' to 'Creates a reusable association between an offering and a maintenance announcement template, specifying a default impact level and description.'

DELETE /api/maintenance-announcement-template-offerings/{uuid}/

- Summary changed from '' to 'Unlink an offering from a maintenance template'
- Description changed from '' to 'Removes the association between an offering and a maintenance announcement template.'

GET /api/maintenance-announcement-template-offerings/{uuid}/

- Summary changed from '' to 'Retrieve an affected offering template link'
- Description changed from '' to 'Returns the details of a specific link between a maintenance announcement template and an offering.'

PATCH /api/maintenance-announcement-template-offerings/{uuid}/

- Summary changed from '' to 'Partially update an affected offering template link'
- Description changed from '' to 'Partially updates the default impact level or description for an offering linked to a maintenance template.'

PUT /api/maintenance-announcement-template-offerings/{uuid}/

- Summary changed from '' to 'Update an affected offering template link'
- Description changed from '' to 'Updates the default impact level or description for an offering linked to a maintenance template.'

GET /api/maintenance-announcements-template/

- Summary changed from '' to 'List maintenance announcement templates'
- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Returns a paginated list of reusable templates for maintenance announcements.'

HEAD /api/maintenance-announcements-template/

- Summary changed from '' to 'List maintenance announcement templates'

POST /api/maintenance-announcements-template/

- Summary changed from '' to 'Create a maintenance announcement template'
- Description changed from '' to 'Creates a new reusable template for maintenance announcements, including a default message and type.'

DELETE /api/maintenance-announcements-template/{uuid}/

- Summary changed from '' to 'Delete a maintenance announcement template'
- Description changed from '' to 'Deletes a maintenance announcement template.'

GET /api/maintenance-announcements-template/{uuid}/

- Summary changed from '' to 'Retrieve a maintenance announcement template'
- Description changed from '' to 'Returns the details of a specific maintenance announcement template.'

PATCH /api/maintenance-announcements-template/{uuid}/

- Summary changed from '' to 'Partially update a maintenance announcement template'
- Description changed from '' to 'Partially updates an existing maintenance announcement template.'

PUT /api/maintenance-announcements-template/{uuid}/

- Summary changed from '' to 'Update a maintenance announcement template'
- Description changed from '' to 'Updates an existing maintenance announcement template.'

GET /api/maintenance-announcements/

- Summary changed from '' to 'List maintenance announcements'
- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Returns a paginated list of maintenance announcements.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: internal_notes

HEAD /api/maintenance-announcements/

- Summary changed from '' to 'List maintenance announcements'

POST /api/maintenance-announcements/

- Summary changed from '' to 'Create a maintenance announcement'
- Description changed from '' to 'Creates a new maintenance announcement in the 'Draft' state.'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: internal_notes
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: internal_notes

DELETE /api/maintenance-announcements/{uuid}/

- Summary changed from '' to 'Delete a maintenance announcement'
- Description changed from '' to 'Deletes a maintenance announcement.'

GET /api/maintenance-announcements/{uuid}/

- Summary changed from '' to 'Retrieve a maintenance announcement'
- Description changed from '' to 'Returns the details of a specific maintenance announcement.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: internal_notes

PATCH /api/maintenance-announcements/{uuid}/

- Summary changed from '' to 'Partially update a maintenance announcement'
- Description changed from '' to 'Partially updates an existing maintenance announcement.'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: internal_notes
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: internal_notes

PUT /api/maintenance-announcements/{uuid}/

- Summary changed from '' to 'Update a maintenance announcement'
- Description changed from '' to 'Updates an existing maintenance announcement.'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: internal_notes
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: internal_notes

POST /api/maintenance-announcements/{uuid}/cancel_maintenance/

- Summary changed from '' to 'Cancel the maintenance announcement'
- Description changed from 'Cancel the maintenance announcement' to 'Transitions a 'Draft' or 'Scheduled' maintenance announcement to 'Cancelled'.'

POST /api/maintenance-announcements/{uuid}/complete_maintenance/

- Summary changed from '' to 'Complete the maintenance announcement'
- Description changed from 'Complete the maintenance announcement' to 'Transitions an 'In progress' maintenance announcement to 'Completed', indicating that the maintenance work has finished.'

POST /api/maintenance-announcements/{uuid}/schedule/

- Summary changed from '' to 'Schedule/publish the maintenance announcement'
- Description changed from 'Schedule/publish the maintenance announcement' to 'Transitions a 'Draft' maintenance announcement to the 'Scheduled' state, making it publicly visible.'

POST /api/maintenance-announcements/{uuid}/start_maintenance/

- Summary changed from '' to 'Start the maintenance announcement'
- Description changed from 'Start the maintenance announcement' to 'Transitions a 'Scheduled' maintenance announcement to 'In progress', indicating that the maintenance work has begun.'

POST /api/maintenance-announcements/{uuid}/unschedule/

- Summary changed from '' to 'Unschedule/unpublish the maintenance announcement'
- Description changed from 'Unschedule/unpublish the maintenance announcement' to 'Transitions a 'Scheduled' maintenance announcement back to the 'Draft' state, hiding it from public view.'

GET /api/managed-rancher-cluster-resources/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''
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
                      - New property: slug
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: slug

GET /api/managed-rancher-cluster-resources/{uuid}/

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
                    - New property: slug
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: slug

GET /api/marketplace-categories/

- Summary changed from '' to 'List categories'
- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Returns a paginated list of marketplace categories.'

HEAD /api/marketplace-categories/

- Summary changed from '' to 'List categories'

POST /api/marketplace-categories/

- Summary changed from '' to 'Create a category'
- Description changed from '' to 'Creates a new marketplace category. Requires staff permissions.'

DELETE /api/marketplace-categories/{uuid}/

- Summary changed from '' to 'Delete a category'
- Description changed from '' to 'Deletes a marketplace category. Requires staff permissions.'

GET /api/marketplace-categories/{uuid}/

- Summary changed from '' to 'Retrieve a category'
- Description changed from '' to 'Returns details of a specific marketplace category.'

PATCH /api/marketplace-categories/{uuid}/

- Summary changed from '' to 'Partially update a category'
- Description changed from '' to 'Partially updates an existing marketplace category. Requires staff permissions.'

PUT /api/marketplace-categories/{uuid}/

- Summary changed from '' to 'Update a category'
- Description changed from '' to 'Updates an existing marketplace category. Requires staff permissions.'

GET /api/marketplace-category-columns/

- Summary changed from '' to 'List category columns'
- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Returns a paginated list of category columns used for resource table rendering.'

HEAD /api/marketplace-category-columns/

- Summary changed from '' to 'List category columns'

POST /api/marketplace-category-columns/

- Summary changed from '' to 'Create a category column'
- Description changed from '' to 'Creates a new category column. Requires staff permissions.'

DELETE /api/marketplace-category-columns/{uuid}/

- Summary changed from '' to 'Delete a category column'
- Description changed from '' to 'Deletes a category column. Requires staff permissions.'

GET /api/marketplace-category-columns/{uuid}/

- Summary changed from '' to 'Retrieve a category column'
- Description changed from '' to 'Returns details of a specific category column.'

PATCH /api/marketplace-category-columns/{uuid}/

- Summary changed from '' to 'Partially update a category column'
- Description changed from '' to 'Partially updates an existing category column. Requires staff permissions.'

PUT /api/marketplace-category-columns/{uuid}/

- Summary changed from '' to 'Update a category column'
- Description changed from '' to 'Updates an existing category column. Requires staff permissions.'

GET /api/marketplace-category-component-usages/

- Summary changed from '' to 'List aggregated category component usages'
- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to '
        Returns a paginated list of aggregated component usages for marketplace categories.
        This data is scoped to either a customer or a project and represents the total usage
        of a component type (e.g., total 'CPU hours' used across all resources of a certain category
        within a project).

        The list **must** be filtered by a `scope` parameter (either a customer or project URL).
        '

HEAD /api/marketplace-category-component-usages/

- Summary changed from '' to 'List aggregated category component usages'

GET /api/marketplace-category-component-usages/{id}/

- Summary changed from '' to 'Retrieve an aggregated category component usage record'
- Description changed from '' to 'Returns the details of a single aggregated usage record for a category component, identified by its database ID.'

GET /api/marketplace-category-components/

- Summary changed from '' to 'List category components'
- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Returns a paginated list of all components defined at the category level. These act as templates for components in offerings.'

HEAD /api/marketplace-category-components/

- Summary changed from '' to 'List category components'

POST /api/marketplace-category-components/

- Summary changed from '' to 'Create a category component'
- Description changed from '' to 'Creates a new component for a category. Requires staff permissions.'

DELETE /api/marketplace-category-components/{id}/

- Summary changed from '' to 'Delete a category component'
- Description changed from '' to 'Deletes a category component. Requires staff permissions.'

GET /api/marketplace-category-components/{id}/

- Summary changed from '' to 'Retrieve a category component'
- Description changed from '' to 'Returns the details of a specific category component, identified by its ID.'

PATCH /api/marketplace-category-components/{id}/

- Summary changed from '' to 'Partially update a category component'
- Description changed from '' to 'Partially updates an existing category component. Requires staff permissions.'

PUT /api/marketplace-category-components/{id}/

- Summary changed from '' to 'Update a category component'
- Description changed from '' to 'Updates an existing category component. Requires staff permissions.'

GET /api/marketplace-category-groups/

- Summary changed from '' to 'List category groups'
- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Returns a paginated list of category groups.'

HEAD /api/marketplace-category-groups/

- Summary changed from '' to 'List category groups'

POST /api/marketplace-category-groups/

- Summary changed from '' to 'Create a category group'
- Description changed from '' to 'Creates a new category group. Requires staff permissions.'

DELETE /api/marketplace-category-groups/{uuid}/

- Summary changed from '' to 'Delete a category group'
- Description changed from '' to 'Deletes a category group. Requires staff permissions.'

GET /api/marketplace-category-groups/{uuid}/

- Summary changed from '' to 'Retrieve a category group'
- Description changed from '' to 'Returns details of a specific category group.'

PATCH /api/marketplace-category-groups/{uuid}/

- Summary changed from '' to 'Partially update a category group'
- Description changed from '' to 'Partially updates an existing category group. Requires staff permissions.'

PUT /api/marketplace-category-groups/{uuid}/

- Summary changed from '' to 'Update a category group'
- Description changed from '' to 'Updates an existing category group. Requires staff permissions.'

GET /api/marketplace-category-help-articles/

- Summary changed from '' to 'List category help articles'
- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Returns a paginated list of all help articles associated with marketplace categories.'

HEAD /api/marketplace-category-help-articles/

- Summary changed from '' to 'List category help articles'

POST /api/marketplace-category-help-articles/

- Summary changed from '' to 'Create a category help article'
- Description changed from '' to 'Creates a new help article and associates it with one or more categories. Requires staff permissions.'

DELETE /api/marketplace-category-help-articles/{id}/

- Summary changed from '' to 'Delete a category help article'
- Description changed from '' to 'Deletes a help article. Requires staff permissions.'

GET /api/marketplace-category-help-articles/{id}/

- Summary changed from '' to 'Retrieve a category help article'
- Description changed from '' to 'Returns the details of a specific help article, identified by its ID.'

PATCH /api/marketplace-category-help-articles/{id}/

- Summary changed from '' to 'Partially update a category help article'
- Description changed from '' to 'Partially updates an existing help article. Requires staff permissions.'

PUT /api/marketplace-category-help-articles/{id}/

- Summary changed from '' to 'Update a category help article'
- Description changed from '' to 'Updates an existing help article. Requires staff permissions.'

GET /api/marketplace-component-usages/

- Summary changed from '' to 'List component usage records'
- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Returns a paginated list of component usage records for resources. This data is used for billing and usage tracking.'

HEAD /api/marketplace-component-usages/

- Summary changed from '' to 'List component usage records'

POST /api/marketplace-component-usages/set_usage/

- Summary changed from '' to 'Set component usage for a resource'
- Description changed from '' to '
        Allows a service provider to report usage for one or more components of a specific resource.
        This endpoint is typically used by backend systems or agents to submit periodic usage data.

        - If a `plan_period` is provided, the usage is associated with that period.
        - If only a `resource` is provided, the system will determine the correct plan period based on the current date.
        - If a usage record for the same resource, component, and billing period already exists, it will be updated. Otherwise, a new record is created.
        '
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Examples changed
        - New example: ReportUsageForMultipleComponents

GET /api/marketplace-component-usages/{uuid}/

- Summary changed from '' to 'Retrieve a component usage record'
- Description changed from '' to 'Returns the details of a specific component usage record.'

POST /api/marketplace-component-usages/{uuid}/set_user_usage/

- Summary changed from '' to 'Set user-specific component usage'
- Description changed from '' to '
        Allows a service provider to report usage for a specific user associated with a resource's component.
        This is used for detailed, per-user usage tracking within a single resource.

        - If a user-specific usage record already exists for the given component usage, it will be updated.
        - Otherwise, a new record is created.
        '
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Examples changed
        - New example: ReportUsageForASpecificUser

GET /api/marketplace-component-user-usages/

- Summary changed from '' to 'List user-specific component usages'
- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to '
        Returns a paginated list of component usage records attributed to specific users.
        This provides a granular view of resource consumption, breaking down the total usage of a component
        by individual users.
        '

HEAD /api/marketplace-component-user-usages/

- Summary changed from '' to 'List user-specific component usages'

GET /api/marketplace-component-user-usages/{uuid}/

- Summary changed from '' to 'Retrieve a user-specific component usage record'
- Description changed from '' to 'Returns the details of a single user-specific component usage record.'

GET /api/marketplace-course-accounts/

- Summary changed from '' to 'List course accounts'
- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Returns a paginated list of course accounts accessible to the current user.'

HEAD /api/marketplace-course-accounts/

- Summary changed from '' to 'List course accounts'

POST /api/marketplace-course-accounts/

- Summary changed from '' to 'Create a course account'
- Description changed from '' to 'Creates a new temporary course account within a specified course project.'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Examples changed
        - New example: CreateACourseAccount
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Examples changed
          - New example: CreateACourseAccount

POST /api/marketplace-course-accounts/create_bulk/

- Summary changed from '' to 'Bulk create course accounts'
- Description changed from '' to 'Creates multiple course accounts within a specified course project in a single request.'
- New query param: email
- New query param: o
- New query param: page
- New query param: page_size
- New query param: project_end_date_after
- New query param: project_end_date_before
- New query param: project_start_date_after
- New query param: project_start_date_before
- New query param: project_uuid
- New query param: state
- New query param: username
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Examples changed
        - New example: BulkCreateThreeCourseAccounts
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Type changed from 'object' to 'array'
          - Items changed
            - Schema added
          - Required changed
            - Deleted required property: course_accounts
            - Deleted required property: project
          - Properties changed
            - Deleted property: course_accounts
            - Deleted property: project
        - Examples changed
          - New example: BulkCreateThreeCourseAccounts

DELETE /api/marketplace-course-accounts/{uuid}/

- Summary changed from '' to 'Delete (close) a course account'
- Description changed from '' to 'Deletes a course account, which triggers a 'close' operation in the backend.'

GET /api/marketplace-course-accounts/{uuid}/

- Summary changed from '' to 'Retrieve a course account'
- Description changed from '' to 'Returns the details of a specific course account.'

GET /api/marketplace-customer-component-usage-policies/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/marketplace-customer-estimated-cost-policies/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/marketplace-customer-service-accounts/

- Summary changed from '' to 'List service accounts'
- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

HEAD /api/marketplace-customer-service-accounts/

- Summary changed from '' to 'List service accounts'

POST /api/marketplace-customer-service-accounts/

- Summary changed from '' to 'Create a customer service account'
- Description changed from '' to 'Creates a new service account scoped to a specific customer (organization). This generates an API key that can be used for automated access to resources across all projects within that customer.'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Examples changed
        - New example: CreateACustomerServiceAccount
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Examples changed
          - New example: CreateACustomerServiceAccount

DELETE /api/marketplace-customer-service-accounts/{uuid}/

- Summary changed from '' to 'Close a customer service account'
- Description changed from '' to 'Deactivates a customer service account and revokes its API key.'

GET /api/marketplace-customer-service-accounts/{uuid}/

- Summary changed from '' to 'Retrieve a service account'

PATCH /api/marketplace-customer-service-accounts/{uuid}/

- Summary changed from '' to 'Partially update a service account'

PUT /api/marketplace-customer-service-accounts/{uuid}/

- Summary changed from '' to 'Update a service account'

POST /api/marketplace-customer-service-accounts/{uuid}/rotate_api_key/

- Summary changed from '' to 'Rotate API key for a customer service account'
- Description changed from '' to 'Generates a new API key for the service account, immediately invalidating the old one. The new key is returned in the response.'

GET /api/marketplace-global-categories/

- Summary changed from '' to 'Get resource counts by category'
- Description changed from 'Count of resource categories for all resources accessible by user.' to '
        Returns a dictionary mapping marketplace category UUIDs to the count of active (non-terminated)
        resources the current user has access to within that category. This is primarily used for UI
        dashboards or sidebars to display the number of resources in each category filter.

        The counts can be further filtered by providing a `project_uuid` or `customer_uuid`.
        '
- Modified query param: customer_uuid
  - Description changed from 'UUID of the customer to filter resources by.' to 'Filter counts by resources within a specific customer.'
- Modified query param: project_uuid
  - Description changed from 'UUID of the project to filter resources by.' to 'Filter counts by resources within a specific project.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - AdditionalProperties changed
            - Type changed from 'integer' to ''
        - Examples changed
          - New example: ExampleOfCategoryResourceCounts

GET /api/marketplace-integration-statuses/

- Summary changed from '' to 'List integration statuses'
- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Returns a paginated list of integration statuses for offerings. This is used to monitor the connectivity and health of backend agents (e.g., site agents) associated with offerings.'

HEAD /api/marketplace-integration-statuses/

- Summary changed from '' to 'List integration statuses'

GET /api/marketplace-integration-statuses/{uuid}/

- Summary changed from '' to 'Retrieve an integration status'
- Description changed from '' to 'Returns the details of a specific integration status, including the agent type, status, and last request timestamp.'

GET /api/marketplace-offering-estimated-cost-policies/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - Deleted required property: organization_groups
            - Properties changed
              - New property: apply_to_all

POST /api/marketplace-offering-estimated-cost-policies/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Required changed
          - Deleted required property: organization_groups
        - Properties changed
          - New property: apply_to_all
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: organization_groups
          - Properties changed
            - New property: apply_to_all

GET /api/marketplace-offering-estimated-cost-policies/actions/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: organization_groups
          - Properties changed
            - New property: apply_to_all

GET /api/marketplace-offering-estimated-cost-policies/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: organization_groups
          - Properties changed
            - New property: apply_to_all

PATCH /api/marketplace-offering-estimated-cost-policies/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: apply_to_all
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: organization_groups
          - Properties changed
            - New property: apply_to_all

PUT /api/marketplace-offering-estimated-cost-policies/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Required changed
          - Deleted required property: organization_groups
        - Properties changed
          - New property: apply_to_all
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: organization_groups
          - Properties changed
            - New property: apply_to_all

GET /api/marketplace-offering-files/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/marketplace-offering-permissions-log/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/marketplace-offering-permissions/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/marketplace-offering-referrals/

- Summary changed from '' to 'List Datacite referrals for offerings'
- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Returns a paginated list of Datacite referrals associated with marketplace offerings. Referrals represent relationships between an offering (identified by a DOI) and other research outputs, such as publications or datasets. The list must be filtered by the offering's scope.'

HEAD /api/marketplace-offering-referrals/

- Summary changed from '' to 'List Datacite referrals for offerings'

GET /api/marketplace-offering-referrals/{uuid}/

- Summary changed from '' to 'Retrieve a specific Datacite referral'
- Description changed from '' to 'Returns the details of a single Datacite referral record, identified by its UUID. Details include the related identifier (PID), the type of relationship, and metadata about the related work.'

GET /api/marketplace-offering-terms-of-service/

- Summary changed from '' to 'List Terms of Service configurations'
- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Returns a paginated list of Terms of Service configurations for offerings. Visibility depends on user permissions: staff/support see all; service providers see their own; regular users see ToS for offerings they have consented to or shared offerings.'

HEAD /api/marketplace-offering-terms-of-service/

- Summary changed from '' to 'List Terms of Service configurations'

POST /api/marketplace-offering-terms-of-service/

- Summary changed from '' to 'Create a Terms of Service configuration'
- Description changed from '' to 'Creates a new Terms of Service configuration for an offering. Only one active ToS configuration is allowed per offering.'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Examples changed
        - New example: CreateANewActiveToSForAnOffering
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Examples changed
          - New example: CreateANewActiveToSForAnOffering

DELETE /api/marketplace-offering-terms-of-service/{uuid}/

- Summary changed from '' to 'Delete a Terms of Service configuration'
- Description changed from '' to 'Deletes a Terms of Service configuration. This is a hard delete and should be used with caution.'

GET /api/marketplace-offering-terms-of-service/{uuid}/

- Summary changed from '' to 'Retrieve a Terms of Service configuration'
- Description changed from '' to 'Returns the details of a specific Terms of Service configuration.'

PATCH /api/marketplace-offering-terms-of-service/{uuid}/

- Summary changed from '' to 'Partially update a Terms of Service configuration'
- Description changed from '' to 'Partially updates an existing Terms of Service configuration.'

PUT /api/marketplace-offering-terms-of-service/{uuid}/

- Summary changed from '' to 'Update a Terms of Service configuration'
- Description changed from '' to 'Updates an existing Terms of Service configuration. Note that some fields like `version` and `requires_reconsent` are protected and cannot be changed after creation.'

GET /api/marketplace-offering-usage-policies/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - Deleted required property: organization_groups
            - Properties changed
              - New property: apply_to_all

POST /api/marketplace-offering-usage-policies/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Required changed
          - Deleted required property: organization_groups
        - Properties changed
          - New property: apply_to_all
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: organization_groups
          - Properties changed
            - New property: apply_to_all

GET /api/marketplace-offering-usage-policies/actions/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: organization_groups
          - Properties changed
            - New property: apply_to_all

GET /api/marketplace-offering-usage-policies/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: organization_groups
          - Properties changed
            - New property: apply_to_all

PATCH /api/marketplace-offering-usage-policies/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: apply_to_all
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: organization_groups
          - Properties changed
            - New property: apply_to_all

PUT /api/marketplace-offering-usage-policies/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Required changed
          - Deleted required property: organization_groups
        - Properties changed
          - New property: apply_to_all
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: organization_groups
          - Properties changed
            - New property: apply_to_all

GET /api/marketplace-offering-user-checklist-completions/

- Summary changed from '' to 'List checklist completions for offering users'
- Description changed from 'Override list to add OfferingUser data optimization.' to '
        Returns a paginated list of all checklist completions for offering users that the current user is allowed to see.
        This endpoint is used by service providers to monitor compliance status and by users to see their own required checklists.
        Visibility follows the same rules as the `OfferingUsers` endpoint.
        '

HEAD /api/marketplace-offering-user-checklist-completions/

- Summary changed from '' to 'List checklist completions for offering users'

GET /api/marketplace-offering-user-checklist-completions/{id}/

- Summary changed from '' to 'Retrieve a checklist completion'
- Description changed from '' to 'Returns the details of a specific checklist completion for an offering user.'

GET /api/marketplace-offering-user-roles/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/marketplace-offering-users/

- Summary changed from '' to 'List offering users'
- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Returns a paginated list of users associated with offerings. The visibility of users depends on the role of the authenticated user. Staff and support can see all users. Service providers can see users of their offerings if the user has consented. Regular users can only see their own offering-user records.'

HEAD /api/marketplace-offering-users/

- Summary changed from '' to 'List offering users'

POST /api/marketplace-offering-users/

- Summary changed from '' to 'Create an offering user'
- Description changed from '' to 'Associates a user with a specific offering, creating an offering-specific user account. This is typically done by a service provider.'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Examples changed
        - New example: CreateAnOfferingUserLink
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Examples changed
          - New example: CreateAnOfferingUserLink

GET /api/marketplace-offering-users/checklist-template/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: initial_visible_questions
              - Items changed
                - Properties changed
                  - New property: allowed_file_types
                  - New property: allowed_mime_types
                  - New property: always_requires_review
                  - New property: always_show_guidance
                  - New property: dependency_logic_operator
                  - New property: guidance_answer_value
                  - New property: guidance_operator
                  - New property: max_file_size_mb
                  - New property: max_files_count
                  - New property: max_value
                  - New property: min_value
                  - New property: operator
                  - New property: order
                  - New property: question_type
                  - New property: review_answer_value
            - Modified property: questions
              - Items changed
                - Properties changed
                  - New property: allowed_file_types
                  - New property: allowed_mime_types
                  - New property: always_requires_review
                  - New property: always_show_guidance
                  - New property: dependency_logic_operator
                  - New property: guidance_answer_value
                  - New property: guidance_operator
                  - New property: max_file_size_mb
                  - New property: max_files_count
                  - New property: max_value
                  - New property: min_value
                  - New property: operator
                  - New property: order
                  - New property: question_type
                  - New property: review_answer_value

DELETE /api/marketplace-offering-users/{uuid}/

- Summary changed from '' to 'Delete an offering user'
- Description changed from '' to 'Removes the association between a user and an offering. This action may trigger backend cleanup processes depending on the offering type.'

GET /api/marketplace-offering-users/{uuid}/

- Summary changed from '' to 'Retrieve an offering user'
- Description changed from '' to 'Returns the details of a specific offering-user link. Visibility follows the same rules as the list view.'

POST /api/marketplace-offering-users/{uuid}/begin_creating/

- Summary changed from '' to 'Begin creation process'
- Description changed from '' to 'Transitions the offering user state from 'Requested' or 'Error Creating' to 'Creating'. This is typically used by an agent to signal that the creation process has started.'

GET /api/marketplace-offering-users/{uuid}/checklist/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: questions
              - Items changed
                - Required changed
                  - New required property: allowed_file_types
                  - New required property: allowed_mime_types
                  - New required property: max_file_size_mb
                  - New required property: max_files_count
                - Properties changed
                  - New property: allowed_file_types
                  - New property: allowed_mime_types
                  - New property: max_file_size_mb
                  - New property: max_files_count
                  - Modified property: question_type
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/QuestionTypeEnum
                        - New enum values: [multiple_files]

GET /api/marketplace-offering-users/{uuid}/checklist_review/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: questions
              - Items changed
                - Required changed
                  - New required property: allowed_file_types
                  - New required property: allowed_mime_types
                  - New required property: max_file_size_mb
                  - New required property: max_files_count
                - Properties changed
                  - New property: allowed_file_types
                  - New property: allowed_mime_types
                  - New property: max_file_size_mb
                  - New property: max_files_count
                  - Modified property: question_type
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/QuestionTypeEnum
                        - New enum values: [multiple_files]

POST /api/marketplace-offering-users/{uuid}/request_deletion/

- Summary changed from '' to 'Request deletion of an offering user'
- Description changed from 'Action to request deletion of an offering user account.' to 'Initiates the deletion process for an offering user account by transitioning it to the 'Deletion Requested' state.'

POST /api/marketplace-offering-users/{uuid}/set_deleted/

- Summary changed from '' to 'Set state to Deleted'
- Description changed from 'Action to mark an offering user as successfully deleted.' to 'Transitions the offering user to the 'Deleted' state, marking the successful completion of the deletion process.'

POST /api/marketplace-offering-users/{uuid}/set_deleting/

- Summary changed from '' to 'Begin deletion process'
- Description changed from 'Action to begin the deletion process for an offering user.' to 'Transitions the offering user to the 'Deleting' state. This is typically used by an agent to signal that the deletion process has started.'

POST /api/marketplace-offering-users/{uuid}/set_error_creating/

- Summary changed from '' to 'Set state to Error Creating'
- Description changed from '' to 'Manually moves the offering user into the 'Error Creating' state. This is typically used by an agent to report a failure during the creation process.'

POST /api/marketplace-offering-users/{uuid}/set_error_deleting/

- Summary changed from '' to 'Set state to Error Deleting'
- Description changed from '' to 'Manually moves the offering user into the 'Error Deleting' state. This is typically used by an agent to report a failure during the deletion process.'

POST /api/marketplace-offering-users/{uuid}/set_ok/

- Summary changed from '' to 'Set state to OK'
- Description changed from '' to 'Manually sets the offering user state to 'OK'. This can be used to recover from an error state or to complete a manual creation process.'

POST /api/marketplace-offering-users/{uuid}/set_pending_account_linking/

- Summary changed from '' to 'Set state to Pending Account Linking'
- Description changed from '' to 'Transitions the state to 'Pending Account Linking' and allows a service provider to add a comment and a URL to guide the user.'

POST /api/marketplace-offering-users/{uuid}/set_pending_additional_validation/

- Summary changed from '' to 'Set state to Pending Additional Validation'
- Description changed from '' to 'Transitions the state to 'Pending Additional Validation' and allows a service provider to add a comment and a URL for the user to follow.'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Examples changed
        - New example: RequestAdditionalValidation

POST /api/marketplace-offering-users/{uuid}/set_validation_complete/

- Summary changed from '' to 'Set state to Validation Complete'
- Description changed from '' to 'Transitions the state from a pending validation state to 'OK', indicating that the user has completed the required steps. This clears any service provider comments.'

PATCH /api/marketplace-offering-users/{uuid}/update_comments/

- Summary changed from '' to 'Update service provider comments'
- Description changed from 'Action for service providers to update comment and comment URL fields.' to 'Allows a service provider to update the `service_provider_comment` and `service_provider_comment_url` fields for an offering user. This is often used to provide feedback or instructions during a pending state.'

POST /api/marketplace-offering-users/{uuid}/update_restricted/

- Summary changed from '' to 'Update restriction status'
- Description changed from '' to 'Allows a service provider to mark an offering user as restricted or unrestricted. A restricted user may have limited access to the resource.'

GET /api/marketplace-orders/

- Summary changed from '' to 'List orders'
- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Returns a paginated list of orders accessible to the current user. Orders are visible to service consumers (project/customer members with appropriate permissions) and service providers.'
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [slug]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: slug

HEAD /api/marketplace-orders/

- Summary changed from '' to 'List orders'

POST /api/marketplace-orders/

- Summary changed from '' to 'Create an order'
- Description changed from '' to 'Creates a new order to provision a resource. The order will be placed in a pending state and may require approval depending on the offering and user permissions.'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: slug
          - Modified property: attributes
            - Property 'OneOf' changed
              - Schemas added: #/components/schemas/MarketplaceOpenPortalCreateOrderAttributes, #/components/schemas/MarketplaceOpenPortalRemoteCreateOrderAttributes
              - Modified schema: #/components/schemas/OpenStackTenantCreateOrderAttributes
                - Properties changed
                  - New property: security_groups
      - Examples changed
        - New example: CreateAResourceFromAPublicOffering
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: attachment
            - Deleted required property: category_icon
            - Deleted required property: category_title
            - Deleted required property: category_uuid
            - Deleted required property: completed_at
            - Deleted required property: consumer_reviewed_at
            - Deleted required property: consumer_reviewed_by
            - Deleted required property: consumer_reviewed_by_full_name
            - Deleted required property: consumer_reviewed_by_username
            - Deleted required property: cost
            - Deleted required property: created
            - Deleted required property: created_by
            - Deleted required property: created_by_full_name
            - Deleted required property: created_by_username
            - Deleted required property: customer_name
            - Deleted required property: customer_uuid
            - Deleted required property: error_message
            - Deleted required property: marketplace_resource_uuid
            - Deleted required property: modified
            - Deleted required property: offering
            - Deleted required property: offering_billable
            - Deleted required property: offering_description
            - Deleted required property: offering_image
            - Deleted required property: offering_name
            - Deleted required property: offering_plugin_options
            - Deleted required property: offering_shared
            - Deleted required property: offering_thumbnail
            - Deleted required property: offering_type
            - Deleted required property: offering_uuid
            - Deleted required property: output
            - Deleted required property: plan_description
            - Deleted required property: plan_name
            - Deleted required property: plan_unit
            - Deleted required property: plan_uuid
            - Deleted required property: project
            - Deleted required property: project_description
            - Deleted required property: project_name
            - Deleted required property: project_uuid
            - Deleted required property: provider_name
            - Deleted required property: provider_slug
            - Deleted required property: provider_uuid
            - Deleted required property: resource_name
            - Deleted required property: resource_type
            - Deleted required property: resource_uuid
            - Deleted required property: state
            - Deleted required property: url
            - Deleted required property: uuid
          - Properties changed
            - New property: activation_price
            - New property: backend_id
            - New property: can_terminate
            - New property: created_by_civil_number
            - New property: customer_slug
            - New property: fixed_price
            - New property: issue
            - New property: new_cost_estimate
            - New property: new_plan_name
            - New property: new_plan_uuid
            - New property: old_cost_estimate
            - New property: old_plan_name
            - New property: old_plan_uuid
            - New property: project_slug
            - New property: provider_reviewed_at
            - New property: provider_reviewed_by
            - New property: provider_reviewed_by_full_name
            - New property: provider_reviewed_by_username
            - New property: slug
            - New property: termination_comment
            - Deleted property: created_by
            - Deleted property: project
            - Modified property: attachment
              - ReadOnly changed from true to false
            - Modified property: consumer_reviewed_by
              - Format changed from 'uri' to ''
              - Description changed from '' to 'Required. 128 characters or fewer. Lowercase letters, numbers and @/./+/-/_ characters'
        - Examples changed
          - New example: CreateAResourceFromAPublicOffering

DELETE /api/marketplace-orders/{uuid}/

- Summary changed from '' to 'Delete a pending order'
- Description changed from '' to 'Deletes an order that is still in a pending state (e.g., `pending-consumer` or `pending-provider`). Executing or completed orders cannot be deleted.'

GET /api/marketplace-orders/{uuid}/

- Summary changed from '' to 'Retrieve an order'
- Description changed from '' to 'Returns the details of a specific order.'
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [slug]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: slug

POST /api/marketplace-orders/{uuid}/approve_by_consumer/

- Summary changed from '' to 'Approve an order (consumer)'
- Description changed from '' to 'Approves a pending order from the consumer's side (e.g., project manager, customer owner). This transitions the order to the next state, which could be pending provider approval or executing.'
- Responses changed
  - Modified response: 200
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

POST /api/marketplace-orders/{uuid}/approve_by_provider/

- Summary changed from '' to 'Approve an order (provider)'
- Description changed from '' to 'Approves a pending order from the provider's side. This typically transitions the order to the executing state.'
- Responses changed
  - Modified response: 200
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

POST /api/marketplace-orders/{uuid}/cancel/

- Summary changed from '' to 'Cancel an order'
- Description changed from '' to 'Cancels an order. This is typically only possible for certain offering types (e.g., basic support) and in specific states (pending or executing).'
- Responses changed
  - New response: 202
  - Deleted response: 200

POST /api/marketplace-orders/{uuid}/delete_attachment/

- Summary changed from '' to 'Delete order attachment'
- Description changed from 'Delete the attachment from a pending order.' to 'Allows deleting an attachment from a pending order.'

GET /api/marketplace-orders/{uuid}/offering/

- Summary changed from '' to 'Get offering details'
- Description changed from '' to 'Returns details of the offering connected to the requested object.'

POST /api/marketplace-orders/{uuid}/reject_by_consumer/

- Summary changed from '' to 'Reject an order (consumer)'
- Description changed from '' to 'Rejects a pending order from the consumer's side. This moves the order to the 'rejected' state.'

POST /api/marketplace-orders/{uuid}/reject_by_provider/

- Summary changed from '' to 'Reject an order (provider)'
- Description changed from '' to 'Rejects a pending order from the provider's side. This moves the order to the 'rejected' state.'

POST /api/marketplace-orders/{uuid}/set_backend_id/

- Summary changed from '' to 'Set order backend ID'
- Description changed from '' to 'Allows a service provider or staff to set or update the backend ID associated with an order. This is useful for linking the order to an external system's identifier.'
- Responses changed
  - Modified response: 200
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

POST /api/marketplace-orders/{uuid}/set_state_done/

- Summary changed from '' to 'Set order state to done (agent)'
- Description changed from '' to 'Used by external agents (e.g., site agent) to manually transition the order state to 'done'. This is only applicable for specific offering types.'

POST /api/marketplace-orders/{uuid}/set_state_erred/

- Summary changed from '' to 'Set order state to erred (agent)'
- Description changed from '' to 'Used by external agents to report a failure during order processing. An error message and traceback can be provided.'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Examples changed
        - New example: ReportAnError

POST /api/marketplace-orders/{uuid}/set_state_executing/

- Summary changed from '' to 'Set order state to executing (agent)'
- Description changed from '' to 'Used by external agents (e.g., site agent) to manually transition the order state to 'executing'. This is only applicable for specific offering types.'

POST /api/marketplace-orders/{uuid}/unlink/

- Summary changed from '' to 'Unlink an order (staff only)'
- Description changed from '' to 'Forcefully deletes an order from the database without affecting the backend resource. This is a staff-only administrative action used to clean up stuck or invalid orders.'

POST /api/marketplace-orders/{uuid}/update_attachment/

- Summary changed from '' to 'Update order attachment'
- Description changed from 'Update the attachment for a pending order.' to 'Allows uploading or replacing a file attachment (e.g., a purchase order) for a pending order.'

GET /api/marketplace-plan-components/

- Summary changed from '' to 'List plan components'
- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Returns a paginated list of all plan components. A plan component defines the pricing and quotas for an offering component within a billing plan. The list is filtered based on the current user's access permissions and organization group memberships.'

HEAD /api/marketplace-plan-components/

- Summary changed from '' to 'List plan components'

GET /api/marketplace-plan-components/{id}/

- Summary changed from '' to 'Retrieve a plan component'
- Description changed from '' to 'Returns the details of a specific plan component, including its pricing, quotas, and associated offering and plan information.'

GET /api/marketplace-plans/

- Summary changed from '' to 'List provider plans'
- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Returns a paginated list of plans managed by the provider. The list is filtered based on the current user's access to the offering's customer.'

HEAD /api/marketplace-plans/

- Summary changed from '' to 'List provider plans'

POST /api/marketplace-plans/

- Summary changed from '' to 'Create a provider plan'
- Description changed from '' to 'Creates a new billing plan for an offering.'

GET /api/marketplace-plans/usage_stats/

- Summary changed from '' to 'Get plan usage statistics'
- Description changed from '' to 'Returns aggregated statistics on how many resources are currently using each plan. Can be filtered by offering or service provider.'
- Modified query param: customer_provider_uuid
  - Description changed from '' to 'Filter by service provider's customer UUID.'
  - Schema changed
    - Format changed from '' to 'uuid'
- Modified query param: o
  - Description changed from '' to 'Ordering field. Available options: `usage`, `limit`, `remaining`, and their descending counterparts (e.g., `-usage`).'
- Modified query param: offering_uuid
  - Description changed from '' to 'Filter by offering UUID.'
  - Schema changed
    - Format changed from '' to 'uuid'

HEAD /api/marketplace-plans/usage_stats/

- Summary changed from '' to 'Get plan usage statistics'
- Modified query param: customer_provider_uuid
  - Description changed from '' to 'Filter by service provider's customer UUID.'
  - Schema changed
    - Format changed from '' to 'uuid'
- Modified query param: o
  - Description changed from '' to 'Ordering field. Available options: `usage`, `limit`, `remaining`, and their descending counterparts (e.g., `-usage`).'
- Modified query param: offering_uuid
  - Description changed from '' to 'Filter by offering UUID.'
  - Schema changed
    - Format changed from '' to 'uuid'

DELETE /api/marketplace-plans/{uuid}/

- Summary changed from '' to 'Delete a provider plan'
- Description changed from '' to 'Deletes a plan. This is a hard delete and should be used with caution.'

GET /api/marketplace-plans/{uuid}/

- Summary changed from '' to 'Retrieve a provider plan'
- Description changed from '' to 'Returns details of a specific plan.'

PATCH /api/marketplace-plans/{uuid}/

- Summary changed from '' to 'Partially update a provider plan'
- Description changed from '' to 'Partially updates an existing plan. Note: A plan cannot be updated if it is already used by resources.'

PUT /api/marketplace-plans/{uuid}/

- Summary changed from '' to 'Update a provider plan'
- Description changed from '' to 'Updates an existing plan. Note: A plan cannot be updated if it is already used by resources.'

POST /api/marketplace-plans/{uuid}/archive/

- Summary changed from '' to 'Archive a plan'
- Description changed from '' to 'Marks a plan as archived. Archived plans cannot be used for provisioning new resources, but existing resources will continue to be billed according to this plan.'

POST /api/marketplace-plans/{uuid}/delete_organization_groups/

- Summary changed from '' to 'Remove all organization groups from a plan'
- Description changed from '' to 'Removes all organization group associations from this plan, making it accessible to all users (subject to offering-level restrictions).'
- Responses changed
  - New response: 204
  - Deleted response: 200

POST /api/marketplace-plans/{uuid}/update_discounts/

- Summary changed from '' to 'Update plan component discounts'
- Description changed from 'Update volume discount configuration for plan components.

This endpoint allows updating discount thresholds and rates for multiple
plan components in a single request. Discounts are applied automatically
when limit quantities meet or exceed the threshold.

The discount configuration affects future billing:

- Creates separate invoice items showing the discount
- Can be enabled or disabled per component' to '
        Update volume discount configuration for plan components.

        This endpoint allows updating discount thresholds and rates for multiple
        plan components in a single request. Discounts are applied automatically
        when limit quantities meet or exceed the threshold.

        The discount configuration affects future billing:
        - Creates separate invoice items showing the discount.
        - Can be enabled or disabled per component.
        '

POST /api/marketplace-plans/{uuid}/update_organization_groups/

- Summary changed from '' to 'Update organization groups for a plan'
- Description changed from '' to 'Sets the list of organization groups that are allowed to access this plan. If the list is empty, the plan is accessible to all.'

POST /api/marketplace-plans/{uuid}/update_prices/

- Summary changed from '' to 'Update plan component prices'
- Description changed from '' to 'Updates the prices for one or more components of a specific plan. If the plan is already in use by resources, this action updates the `future_price`, which will be applied from the next billing period. Otherwise, the current `price` is updated directly.'

POST /api/marketplace-plans/{uuid}/update_quotas/

- Summary changed from '' to 'Update plan component quotas'
- Description changed from '' to 'Updates the quotas (fixed amounts) for one or more components of a specific plan. This is only applicable for components with a 'fixed-price' billing type.'

GET /api/marketplace-plugins/

- Summary changed from '' to 'List available marketplace plugins and their components'
- Description changed from '' to '
        Returns a list of all registered marketplace plugins (offering types) and the components
        associated with each. This endpoint is public and does not require authentication.

        Each plugin entry includes:
        - `offering_type`: A unique identifier for the plugin.
        - `components`: A list of components provided by the plugin, each with its `type`, `name`, `measured_unit`, and `billing_type`.
        - `available_limits`: A list of component types that support user-defined limits for this plugin.
        '
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Examples changed
          - New example: ExampleResponseForMarketplacePlugins

GET /api/marketplace-project-estimated-cost-policies/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/marketplace-project-service-accounts/

- Summary changed from '' to 'List service accounts'
- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

HEAD /api/marketplace-project-service-accounts/

- Summary changed from '' to 'List service accounts'

POST /api/marketplace-project-service-accounts/

- Summary changed from '' to 'Create a project service account'
- Description changed from '' to 'Creates a new service account scoped to a specific project. This generates an API key that can be used for automated access to resources within that project.'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Examples changed
        - New example: CreateAProjectServiceAccount
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Examples changed
          - New example: CreateAProjectServiceAccount

DELETE /api/marketplace-project-service-accounts/{uuid}/

- Summary changed from '' to 'Close a project service account'
- Description changed from '' to 'Deactivates a project service account and revokes its API key.'

GET /api/marketplace-project-service-accounts/{uuid}/

- Summary changed from '' to 'Retrieve a service account'

PATCH /api/marketplace-project-service-accounts/{uuid}/

- Summary changed from '' to 'Partially update a service account'

PUT /api/marketplace-project-service-accounts/{uuid}/

- Summary changed from '' to 'Update a service account'

POST /api/marketplace-project-service-accounts/{uuid}/rotate_api_key/

- Summary changed from '' to 'Rotate API key for a project service account'
- Description changed from '' to 'Generates a new API key for the service account, immediately invalidating the old one. The new key is returned in the response.'

GET /api/marketplace-project-update-requests/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/marketplace-provider-offerings/

- Summary changed from '' to 'List provider offerings'
- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Returns a paginated list of offerings for the provider.'
- New query param: can_create_offering_user

HEAD /api/marketplace-provider-offerings/

- Summary changed from '' to 'List provider offerings'
- New query param: can_create_offering_user

POST /api/marketplace-provider-offerings/

- Summary changed from '' to 'Create a provider offering'
- Description changed from '' to 'Creates a new provider offering.'
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: category
            - Deleted required property: category_title
            - Deleted required property: category_uuid
            - Deleted required property: citation_count
            - Deleted required property: created
            - Deleted required property: customer_name
            - Deleted required property: customer_uuid
            - Deleted required property: endpoints
            - Deleted required property: files
            - Deleted required property: has_compliance_requirements
            - Deleted required property: name
            - Deleted required property: order_count
            - Deleted required property: organization_groups
            - Deleted required property: parent_description
            - Deleted required property: parent_name
            - Deleted required property: parent_uuid
            - Deleted required property: partitions
            - Deleted required property: paused_reason
            - Deleted required property: plugin_options
            - Deleted required property: project
            - Deleted required property: project_name
            - Deleted required property: project_uuid
            - Deleted required property: quotas
            - Deleted required property: roles
            - Deleted required property: scope
            - Deleted required property: scope_error_message
            - Deleted required property: scope_name
            - Deleted required property: scope_state
            - Deleted required property: scope_uuid
            - Deleted required property: screenshots
            - Deleted required property: software_catalogs
            - Deleted required property: state
            - Deleted required property: total_cost
            - Deleted required property: total_cost_estimated
            - Deleted required property: total_customers
            - Deleted required property: type
            - Deleted required property: url
            - Deleted required property: uuid
          - Properties changed
            - New property: google_calendar_is_public
            - New property: google_calendar_link
            - New property: integration_status
            - Modified property: attributes
              - Type changed from '' to 'object'
              - ReadOnly changed from false to true
              - AdditionalProperties changed
                - Schema added
            - Modified property: components
              - ReadOnly changed from false to true
            - Modified property: description
              - MaxLength changed from null to 4096
            - Modified property: options
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/OfferingOptions
              - Type changed from 'object' to ''
              - ReadOnly changed from false to true
              - Properties changed
                - Deleted property: options
                - Deleted property: order
            - Modified property: plans
              - ReadOnly changed from false to true
            - Modified property: resource_options
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/OfferingOptions
              - Type changed from 'object' to ''
              - ReadOnly changed from false to true
              - Properties changed
                - Deleted property: options
                - Deleted property: order

GET /api/marketplace-provider-offerings/groups/

- Summary changed from '' to 'List offerings grouped by provider'
- Description changed from '' to 'Returns a paginated list of active, shared offerings grouped by their service provider.'
- New query param: can_create_offering_user

HEAD /api/marketplace-provider-offerings/groups/

- Summary changed from '' to 'List offerings grouped by provider'
- New query param: can_create_offering_user

DELETE /api/marketplace-provider-offerings/{uuid}/

- Summary changed from '' to 'Delete a provider offering'
- Description changed from '' to 'Deletes a provider offering. Only possible for offerings in a Draft state with no associated resources.'

GET /api/marketplace-provider-offerings/{uuid}/

- Summary changed from '' to 'Retrieve a provider offering'
- Description changed from '' to 'Returns details of a specific provider offering.'

POST /api/marketplace-provider-offerings/{uuid}/activate/

- Summary changed from '' to 'Activate an offering'
- Description changed from '' to 'Activates a draft or paused offering, making it available for ordering.'

POST /api/marketplace-provider-offerings/{uuid}/add_endpoint/

- Summary changed from '' to 'Add an access endpoint to an offering'
- Description changed from 'Add endpoint to offering.' to 'Adds a new access endpoint (URL) to an offering.'

POST /api/marketplace-provider-offerings/{uuid}/add_partition/

- Summary changed from '' to 'Add a partition to an offering'
- Description changed from 'Add SLURM partition configuration to offering.' to 'Adds a new partition configuration to an offering.'

POST /api/marketplace-provider-offerings/{uuid}/add_software_catalog/

- Summary changed from '' to 'Add a software catalog to an offering'
- Description changed from 'Add software catalog to offering.' to 'Associates a software catalog with an offering and configures enabled CPU architectures.'

POST /api/marketplace-provider-offerings/{uuid}/add_user/

- Summary changed from '' to 'Grant a role to a user'
- Description changed from '' to 'Assigns a specific role to a user within the current scope. An optional expiration time for the role can be set.'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Examples changed
        - New example: GrantProjectAdminRoleUntilEndOfYear
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Examples changed
          - New example: SuccessfulRoleGrantResponse
  - Modified response: 400
    - Description changed from '' to 'Validation error, for example when trying to add a user to a terminated project.'
    - Content changed
      - Deleted media type: application/json

POST /api/marketplace-provider-offerings/{uuid}/archive/

- Summary changed from '' to 'Archive an offering'
- Description changed from '' to 'Archives an offering, making it permanently unavailable for new orders.'

GET /api/marketplace-provider-offerings/{uuid}/component_stats/

- Summary changed from '' to 'Get statistics for offering components'
- Description changed from 'Get statistics for offering components.' to 'Returns monthly usage statistics for the components of an offering within a specified date range.'
- New query param: can_create_offering_user

GET /api/marketplace-provider-offerings/{uuid}/costs/

- Summary changed from '' to 'Get costs for an offering'
- Description changed from 'Get costs for offering.' to 'Returns monthly cost data for an offering within a specified date range.'
- New query param: can_create_offering_user

POST /api/marketplace-provider-offerings/{uuid}/create_offering_component/

- Summary changed from '' to 'Create an offering component'
- Description changed from '' to 'Adds a new custom component to an offering.'

GET /api/marketplace-provider-offerings/{uuid}/customers/

- Summary changed from '' to 'Get customers for an offering'
- Description changed from 'Get customers for offering.' to 'Returns a paginated list of customers who have resources for this offering.'
- New query param: can_create_offering_user

POST /api/marketplace-provider-offerings/{uuid}/delete_endpoint/

- Summary changed from '' to 'Delete an access endpoint from an offering'
- Description changed from 'Delete endpoint from offering.' to 'Deletes an existing access endpoint from an offering by its UUID.'

POST /api/marketplace-provider-offerings/{uuid}/delete_image/

- Summary changed from '' to 'Delete offering image'
- Description changed from 'Delete offering image.' to 'Deletes the main image of an offering.'
- Responses changed
  - New response: 204
  - Deleted response: 200

POST /api/marketplace-provider-offerings/{uuid}/delete_organization_groups/

- Summary changed from '' to 'Delete organization groups for offering'
- Description changed from 'Delete organization groups for offering.' to 'Removes all organization group associations from this offering, making it accessible to all.'
- Responses changed
  - New response: 204
  - Deleted response: 200

POST /api/marketplace-provider-offerings/{uuid}/delete_thumbnail/

- Summary changed from '' to 'Delete offering thumbnail'
- Description changed from 'Delete offering thumbnail.' to 'Deletes the thumbnail image of an offering.'

POST /api/marketplace-provider-offerings/{uuid}/delete_user/

- Summary changed from '' to 'Revoke a role from a user'
- Description changed from '' to 'Removes a specific role from a user within the current scope. This effectively revokes their permissions associated with that role.'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Examples changed
        - New example: RevokeProjectAdminRoleFromUser
- Responses changed
  - Modified response: 200
    - Description changed from 'No response body' to 'Role revoked successfully.'

POST /api/marketplace-provider-offerings/{uuid}/draft/

- Summary changed from '' to 'Move an offering to draft'
- Description changed from '' to 'Moves an active or paused offering back to the draft state for editing.'

GET /api/marketplace-provider-offerings/{uuid}/glauth_users_config/

- Summary changed from '' to 'Get GLauth user configuration'
- Description changed from 'This endpoint provides a config file for GLauth
Example: <https://github.com/glauth/glauth/blob/master/v2/sample-simple.cfg>
It is assumed that the config is used by an external agent,
which synchronizes data from Waldur to GLauth' to '
        This endpoint provides a configuration file for GLauth.
        It is intended to be used by an external agent to synchronize user data from Waldur to GLauth.

        Example output format:
        ```
        [[users]]
          name = "johndoe"
          givenname="John"
          sn="Doe"
          mail = "john.doe@example.com"
          ...
        [[groups]]
          name = "group1"
          gidnumber = 1001
        ```
        '

POST /api/marketplace-provider-offerings/{uuid}/import_resource/

- Summary changed from '' to 'Import a resource'
- Description changed from '' to 'Imports a backend resource into the marketplace.'
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
                    - New property: slug
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: slug

GET /api/marketplace-provider-offerings/{uuid}/importable_resources/

- Summary changed from '' to 'List importable resources'
- Description changed from 'List importable resources for offering.' to 'Returns a paginated list of resources that can be imported for this offering.'

GET /api/marketplace-provider-offerings/{uuid}/list_course_accounts/

- Summary changed from '' to 'List course accounts for an offering'
- Description changed from '' to 'Returns a paginated list of course accounts for projects that have resources of this offering.'
- OperationID changed from 'marketplace_provider_offerings_list_course_accounts_retrieve' to 'marketplace_provider_offerings_list_course_accounts_list'
- New query param: accessible_via_calls
- New query param: allowed_customer_uuid
- New query param: attributes
- New query param: billable
- New query param: can_create_offering_user
- New query param: category_group_uuid
- New query param: category_uuid
- New query param: created
- New query param: customer
- New query param: customer_uuid
- New query param: description
- New query param: has_active_terms_of_service
- New query param: has_terms_of_service
- New query param: keyword
- New query param: modified
- New query param: name
- New query param: name_exact
- New query param: o
- New query param: organization_group_uuid
- New query param: page
- New query param: page_size
- New query param: parent_uuid
- New query param: project_uuid
- New query param: query
- New query param: resource_customer_uuid
- New query param: resource_project_uuid
- New query param: scope_uuid
- New query param: service_manager_uuid
- New query param: shared
- New query param: state
- New query param: type
- New query param: user_has_consent
- New query param: user_has_offering_user
- New query param: uuid_list
- Deleted query param: field
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Type changed from 'object' to 'array'
          - Items changed
            - Schema added
          - Properties changed
            - Deleted property: access_url
            - Deleted property: attributes
            - Deleted property: backend_id
            - Deleted property: backend_metadata
            - Deleted property: billable
            - Deleted property: category
            - Deleted property: category_title
            - Deleted property: category_uuid
            - Deleted property: citation_count
            - Deleted property: compliance_checklist
            - Deleted property: components
            - Deleted property: country
            - Deleted property: created
            - Deleted property: customer
            - Deleted property: customer_name
            - Deleted property: customer_uuid
            - Deleted property: datacite_doi
            - Deleted property: description
            - Deleted property: endpoints
            - Deleted property: files
            - Deleted property: full_description
            - Deleted property: getting_started
            - Deleted property: google_calendar_is_public
            - Deleted property: google_calendar_link
            - Deleted property: has_compliance_requirements
            - Deleted property: image
            - Deleted property: integration_guide
            - Deleted property: integration_status
            - Deleted property: latitude
            - Deleted property: longitude
            - Deleted property: name
            - Deleted property: options
            - Deleted property: order_count
            - Deleted property: organization_groups
            - Deleted property: parent_description
            - Deleted property: parent_name
            - Deleted property: parent_uuid
            - Deleted property: partitions
            - Deleted property: paused_reason
            - Deleted property: plans
            - Deleted property: plugin_options
            - Deleted property: privacy_policy_link
            - Deleted property: project
            - Deleted property: project_name
            - Deleted property: project_uuid
            - Deleted property: quotas
            - Deleted property: resource_options
            - Deleted property: roles
            - Deleted property: scope
            - Deleted property: scope_error_message
            - Deleted property: scope_name
            - Deleted property: scope_state
            - Deleted property: scope_uuid
            - Deleted property: screenshots
            - Deleted property: secret_options
            - Deleted property: service_attributes
            - Deleted property: shared
            - Deleted property: slug
            - Deleted property: software_catalogs
            - Deleted property: state
            - Deleted property: thumbnail
            - Deleted property: total_cost
            - Deleted property: total_cost_estimated
            - Deleted property: total_customers
            - Deleted property: type
            - Deleted property: url
            - Deleted property: uuid
            - Deleted property: vendor_details
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-provider-offerings/{uuid}/list_customer_projects/

- Summary changed from '' to 'List customer projects for an offering'
- Description changed from '' to 'Returns a paginated list of projects that have consumed resources of this offering.'
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [grace_period_days]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: grace_period_days

GET /api/marketplace-provider-offerings/{uuid}/list_customer_service_accounts/

- Summary changed from '' to 'List customer service accounts for an offering'
- Description changed from '' to 'Returns a paginated list of customer-level service accounts for customers who have resources of this offering.'
- OperationID changed from 'marketplace_provider_offerings_list_customer_service_accounts_retrieve' to 'marketplace_provider_offerings_list_customer_service_accounts_list'
- New query param: accessible_via_calls
- New query param: allowed_customer_uuid
- New query param: attributes
- New query param: billable
- New query param: can_create_offering_user
- New query param: category_group_uuid
- New query param: category_uuid
- New query param: created
- New query param: customer
- New query param: customer_uuid
- New query param: description
- New query param: has_active_terms_of_service
- New query param: has_terms_of_service
- New query param: keyword
- New query param: modified
- New query param: name
- New query param: name_exact
- New query param: o
- New query param: organization_group_uuid
- New query param: page
- New query param: page_size
- New query param: parent_uuid
- New query param: project_uuid
- New query param: query
- New query param: resource_customer_uuid
- New query param: resource_project_uuid
- New query param: scope_uuid
- New query param: service_manager_uuid
- New query param: shared
- New query param: state
- New query param: type
- New query param: user_has_consent
- New query param: user_has_offering_user
- New query param: uuid_list
- Deleted query param: field
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Type changed from 'object' to 'array'
          - Items changed
            - Schema added
          - Properties changed
            - Deleted property: access_url
            - Deleted property: attributes
            - Deleted property: backend_id
            - Deleted property: backend_metadata
            - Deleted property: billable
            - Deleted property: category
            - Deleted property: category_title
            - Deleted property: category_uuid
            - Deleted property: citation_count
            - Deleted property: compliance_checklist
            - Deleted property: components
            - Deleted property: country
            - Deleted property: created
            - Deleted property: customer
            - Deleted property: customer_name
            - Deleted property: customer_uuid
            - Deleted property: datacite_doi
            - Deleted property: description
            - Deleted property: endpoints
            - Deleted property: files
            - Deleted property: full_description
            - Deleted property: getting_started
            - Deleted property: google_calendar_is_public
            - Deleted property: google_calendar_link
            - Deleted property: has_compliance_requirements
            - Deleted property: image
            - Deleted property: integration_guide
            - Deleted property: integration_status
            - Deleted property: latitude
            - Deleted property: longitude
            - Deleted property: name
            - Deleted property: options
            - Deleted property: order_count
            - Deleted property: organization_groups
            - Deleted property: parent_description
            - Deleted property: parent_name
            - Deleted property: parent_uuid
            - Deleted property: partitions
            - Deleted property: paused_reason
            - Deleted property: plans
            - Deleted property: plugin_options
            - Deleted property: privacy_policy_link
            - Deleted property: project
            - Deleted property: project_name
            - Deleted property: project_uuid
            - Deleted property: quotas
            - Deleted property: resource_options
            - Deleted property: roles
            - Deleted property: scope
            - Deleted property: scope_error_message
            - Deleted property: scope_name
            - Deleted property: scope_state
            - Deleted property: scope_uuid
            - Deleted property: screenshots
            - Deleted property: secret_options
            - Deleted property: service_attributes
            - Deleted property: shared
            - Deleted property: slug
            - Deleted property: software_catalogs
            - Deleted property: state
            - Deleted property: thumbnail
            - Deleted property: total_cost
            - Deleted property: total_cost_estimated
            - Deleted property: total_customers
            - Deleted property: type
            - Deleted property: url
            - Deleted property: uuid
            - Deleted property: vendor_details
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-provider-offerings/{uuid}/list_customer_users/

- Summary changed from '' to 'List customer users for an offering'
- Description changed from '' to 'Returns a paginated list of users who have access to resources of this offering.'

GET /api/marketplace-provider-offerings/{uuid}/list_project_service_accounts/

- Summary changed from '' to 'List project service accounts for an offering'
- Description changed from '' to 'Returns a paginated list of project-level service accounts for projects that have resources of this offering.'
- OperationID changed from 'marketplace_provider_offerings_list_project_service_accounts_retrieve' to 'marketplace_provider_offerings_list_project_service_accounts_list'
- New query param: accessible_via_calls
- New query param: allowed_customer_uuid
- New query param: attributes
- New query param: billable
- New query param: can_create_offering_user
- New query param: category_group_uuid
- New query param: category_uuid
- New query param: created
- New query param: customer
- New query param: customer_uuid
- New query param: description
- New query param: has_active_terms_of_service
- New query param: has_terms_of_service
- New query param: keyword
- New query param: modified
- New query param: name
- New query param: name_exact
- New query param: o
- New query param: organization_group_uuid
- New query param: page
- New query param: page_size
- New query param: parent_uuid
- New query param: project_uuid
- New query param: query
- New query param: resource_customer_uuid
- New query param: resource_project_uuid
- New query param: scope_uuid
- New query param: service_manager_uuid
- New query param: shared
- New query param: state
- New query param: type
- New query param: user_has_consent
- New query param: user_has_offering_user
- New query param: uuid_list
- Deleted query param: field
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Type changed from 'object' to 'array'
          - Items changed
            - Schema added
          - Properties changed
            - Deleted property: access_url
            - Deleted property: attributes
            - Deleted property: backend_id
            - Deleted property: backend_metadata
            - Deleted property: billable
            - Deleted property: category
            - Deleted property: category_title
            - Deleted property: category_uuid
            - Deleted property: citation_count
            - Deleted property: compliance_checklist
            - Deleted property: components
            - Deleted property: country
            - Deleted property: created
            - Deleted property: customer
            - Deleted property: customer_name
            - Deleted property: customer_uuid
            - Deleted property: datacite_doi
            - Deleted property: description
            - Deleted property: endpoints
            - Deleted property: files
            - Deleted property: full_description
            - Deleted property: getting_started
            - Deleted property: google_calendar_is_public
            - Deleted property: google_calendar_link
            - Deleted property: has_compliance_requirements
            - Deleted property: image
            - Deleted property: integration_guide
            - Deleted property: integration_status
            - Deleted property: latitude
            - Deleted property: longitude
            - Deleted property: name
            - Deleted property: options
            - Deleted property: order_count
            - Deleted property: organization_groups
            - Deleted property: parent_description
            - Deleted property: parent_name
            - Deleted property: parent_uuid
            - Deleted property: partitions
            - Deleted property: paused_reason
            - Deleted property: plans
            - Deleted property: plugin_options
            - Deleted property: privacy_policy_link
            - Deleted property: project
            - Deleted property: project_name
            - Deleted property: project_uuid
            - Deleted property: quotas
            - Deleted property: resource_options
            - Deleted property: roles
            - Deleted property: scope
            - Deleted property: scope_error_message
            - Deleted property: scope_name
            - Deleted property: scope_state
            - Deleted property: scope_uuid
            - Deleted property: screenshots
            - Deleted property: secret_options
            - Deleted property: service_attributes
            - Deleted property: shared
            - Deleted property: slug
            - Deleted property: software_catalogs
            - Deleted property: state
            - Deleted property: thumbnail
            - Deleted property: total_cost
            - Deleted property: total_cost_estimated
            - Deleted property: total_customers
            - Deleted property: type
            - Deleted property: url
            - Deleted property: uuid
            - Deleted property: vendor_details
    - Headers changed
      - New header: x-result-count

GET /api/marketplace-provider-offerings/{uuid}/list_users/

- Summary changed from '' to 'List users and their roles in a scope'
- Description changed from '' to 'Retrieves a list of users who have a role within a specific scope (e.g., a project or an organization). The list can be filtered by user details or role.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Examples changed
          - New example: ExampleUserRoleListResponse

POST /api/marketplace-provider-offerings/{uuid}/move_offering/

- Summary changed from '' to 'Move an offering'
- Description changed from '' to 'Moves an offering to a different service provider. Requires staff permissions.'

GET /api/marketplace-provider-offerings/{uuid}/orders/

- Summary changed from '' to 'List orders for an offering'
- Description changed from '' to 'Returns a paginated list of orders associated with a specific offering.'
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [slug]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: slug

GET /api/marketplace-provider-offerings/{uuid}/orders/{order_uuid}/

- Summary changed from '' to 'Retrieve a specific order for an offering'
- Description changed from '' to 'Returns details of a specific order associated with an offering.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: slug

POST /api/marketplace-provider-offerings/{uuid}/pause/

- Summary changed from '' to 'Pause an offering'
- Description changed from '' to 'Pauses an active offering, preventing new orders from being created.'

POST /api/marketplace-provider-offerings/{uuid}/refresh_offering_usernames/

- Summary changed from '' to 'Refresh offering user usernames'
- Description changed from 'Refresh offering user usernames.' to 'Triggers a refresh of usernames for all non-restricted users associated with this offering, based on the current username generation policy.'

POST /api/marketplace-provider-offerings/{uuid}/remove_offering_component/

- Summary changed from '' to 'Remove an offering component'
- Description changed from '' to 'Removes a custom component from an offering. Built-in components cannot be removed.'

POST /api/marketplace-provider-offerings/{uuid}/remove_partition/

- Summary changed from '' to 'Remove a partition from an offering'
- Description changed from 'Remove partition from offering.' to 'Removes a partition configuration from an offering.'
- Responses changed
  - New response: 204
  - Deleted response: 200

POST /api/marketplace-provider-offerings/{uuid}/remove_software_catalog/

- Summary changed from '' to 'Remove a software catalog from an offering'
- Description changed from 'Remove software catalog from offering.' to 'Disassociates a software catalog from an offering.'
- Responses changed
  - New response: 204
  - Deleted response: 200

POST /api/marketplace-provider-offerings/{uuid}/set_backend_metadata/

- Summary changed from '' to 'Set offering backend metadata'
- Description changed from '' to 'Updates the backend-specific metadata for an offering.'

GET /api/marketplace-provider-offerings/{uuid}/stats/

- Summary changed from '' to 'Get offering statistics'
- Description changed from '' to 'Returns basic statistics for an offering, such as the number of active resources and customers.'
- Deleted query param: field
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customers_count
            - New property: resources_count
            - Deleted property: access_url
            - Deleted property: attributes
            - Deleted property: backend_id
            - Deleted property: backend_metadata
            - Deleted property: billable
            - Deleted property: category
            - Deleted property: category_title
            - Deleted property: category_uuid
            - Deleted property: citation_count
            - Deleted property: compliance_checklist
            - Deleted property: components
            - Deleted property: country
            - Deleted property: created
            - Deleted property: customer
            - Deleted property: customer_name
            - Deleted property: customer_uuid
            - Deleted property: datacite_doi
            - Deleted property: description
            - Deleted property: endpoints
            - Deleted property: files
            - Deleted property: full_description
            - Deleted property: getting_started
            - Deleted property: google_calendar_is_public
            - Deleted property: google_calendar_link
            - Deleted property: has_compliance_requirements
            - Deleted property: image
            - Deleted property: integration_guide
            - Deleted property: integration_status
            - Deleted property: latitude
            - Deleted property: longitude
            - Deleted property: name
            - Deleted property: options
            - Deleted property: order_count
            - Deleted property: organization_groups
            - Deleted property: parent_description
            - Deleted property: parent_name
            - Deleted property: parent_uuid
            - Deleted property: partitions
            - Deleted property: paused_reason
            - Deleted property: plans
            - Deleted property: plugin_options
            - Deleted property: privacy_policy_link
            - Deleted property: project
            - Deleted property: project_name
            - Deleted property: project_uuid
            - Deleted property: quotas
            - Deleted property: resource_options
            - Deleted property: roles
            - Deleted property: scope
            - Deleted property: scope_error_message
            - Deleted property: scope_name
            - Deleted property: scope_state
            - Deleted property: scope_uuid
            - Deleted property: screenshots
            - Deleted property: secret_options
            - Deleted property: service_attributes
            - Deleted property: shared
            - Deleted property: slug
            - Deleted property: software_catalogs
            - Deleted property: state
            - Deleted property: thumbnail
            - Deleted property: total_cost
            - Deleted property: total_cost_estimated
            - Deleted property: total_customers
            - Deleted property: type
            - Deleted property: url
            - Deleted property: uuid
            - Deleted property: vendor_details

POST /api/marketplace-provider-offerings/{uuid}/sync/

- Summary changed from '' to 'Synchronize offering service settings'
- Description changed from '' to 'Schedules a synchronization task to pull the latest data for the offering's service settings from the backend.'
- Responses changed
  - New response: 202
  - Deleted response: 200

GET /api/marketplace-provider-offerings/{uuid}/tos_stats/

- Summary changed from '' to 'Get Terms of Service consent statistics'
- Description changed from 'Return comprehensive ToS consent statistics for this offering.' to 'Returns comprehensive Terms of Service consent statistics for this offering, including user counts, consent rates, and historical data.'

POST /api/marketplace-provider-offerings/{uuid}/unpause/

- Summary changed from '' to 'Unpause an offering'
- Description changed from '' to 'Resumes a paused offering, making it available for ordering again.'

POST /api/marketplace-provider-offerings/{uuid}/update_attributes/

- Summary changed from '' to 'Update offering attributes'
- Description changed from 'Update offering attributes.' to 'Updates the attributes of an offering.'

POST /api/marketplace-provider-offerings/{uuid}/update_compliance_checklist/

- Summary changed from '' to 'Update offering compliance checklist'
- Description changed from '' to 'Associates a compliance checklist with an offering.'

POST /api/marketplace-provider-offerings/{uuid}/update_description/

- Summary changed from '' to 'Update offering category'
- Description changed from '' to 'Updates the category of an offering.'

POST /api/marketplace-provider-offerings/{uuid}/update_image/

- Summary changed from '' to 'Update offering image'
- Description changed from 'Update offering image.' to 'Uploads or replaces the main image for an offering.'
- Responses changed
  - Modified response: 200
    - Description changed from '' to 'No response body'
    - Content changed
      - Deleted media type: application/json

POST /api/marketplace-provider-offerings/{uuid}/update_integration/

- Summary changed from '' to 'Update offering integration settings'
- Description changed from '' to 'Updates the backend integration settings for an offering, including plugin options, secret options, and service attributes.'

POST /api/marketplace-provider-offerings/{uuid}/update_location/

- Summary changed from '' to 'Update offering location'
- Description changed from '' to 'Updates the geographical location (latitude and longitude) of an offering.'

POST /api/marketplace-provider-offerings/{uuid}/update_offering_component/

- Summary changed from '' to 'Update an offering component'
- Description changed from '' to 'Updates the properties of a specific component within an offering.'

POST /api/marketplace-provider-offerings/{uuid}/update_options/

- Summary changed from '' to 'Update offering options'
- Description changed from '' to 'Updates the order form options for an offering.'

POST /api/marketplace-provider-offerings/{uuid}/update_organization_groups/

- Summary changed from '' to 'Update organization groups for offering'
- Description changed from 'Update organization groups for offering.' to 'Sets the list of organization groups that can access this offering.'

POST /api/marketplace-provider-offerings/{uuid}/update_overview/

- Summary changed from '' to 'Update offering overview'
- Description changed from '' to 'Updates the overview fields of an offering, such as name, description, and getting started guide.'

PATCH /api/marketplace-provider-offerings/{uuid}/update_partition/

- Summary changed from '' to 'Update a partition of an offering'
- Description changed from 'Update partition configuration for offering.' to 'Updates the configuration of an existing partition associated with an offering.'

POST /api/marketplace-provider-offerings/{uuid}/update_resource_options/

- Summary changed from '' to 'Update offering resource options'
- Description changed from '' to 'Updates the resource report form options for an offering.'

PATCH /api/marketplace-provider-offerings/{uuid}/update_software_catalog/

- Summary changed from '' to 'Update software catalog configuration'
- Description changed from 'Update software catalog configuration for offering.' to 'Updates the configuration of a software catalog associated with an offering, such as enabled architectures or partition.'

POST /api/marketplace-provider-offerings/{uuid}/update_thumbnail/

- Summary changed from '' to 'Update offering thumbnail'
- Description changed from 'Update offering thumbnail.' to 'Uploads or replaces the thumbnail image for an offering.'

POST /api/marketplace-provider-offerings/{uuid}/update_user/

- Summary changed from '' to 'Update a user's role expiration'
- Description changed from '' to 'Updates the expiration time for a user's existing role in the current scope. This is useful for extending or shortening the duration of a permission. To make a role permanent, set expiration_time to null.'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Examples changed
        - New example: ExtendRoleUntilMid-2025
        - New example: MakeARolePermanent
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Examples changed
          - New example: SuccessfulRoleUpdateResponse

GET /api/marketplace-provider-offerings/{uuid}/user_has_resource_access/

- Summary changed from '' to 'Check user access to offering resources'
- Description changed from 'Check if user has access to offering.' to 'Checks if a specified user has access to any non-terminated resource of this offering.'

GET /api/marketplace-provider-resources/

- Summary changed from '' to 'List provider resources'
- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Returns a paginated list of resources for offerings managed by the current user as a service provider.'
- Modified query param: o
  - Schema changed
    - Items changed
      - New enum values: [-end_date end_date]
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
                      - New property: slug
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: slug

HEAD /api/marketplace-provider-resources/

- Summary changed from '' to 'List provider resources'
- Modified query param: o
  - Schema changed
    - Items changed
      - New enum values: [-end_date end_date]

GET /api/marketplace-provider-resources/{uuid}/

- Summary changed from '' to 'Retrieve a provider resource'
- Description changed from '' to 'Returns details of a specific resource from a provider's perspective.'
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
                    - New property: slug
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: slug

PATCH /api/marketplace-provider-resources/{uuid}/

- Summary changed from '' to 'Partially update a provider resource'
- Description changed from '' to 'Partially updates the name or description of a resource. Requires provider permissions.'

PUT /api/marketplace-provider-resources/{uuid}/

- Summary changed from '' to 'Update a provider resource'
- Description changed from '' to 'Updates the name or description of a resource. Requires provider permissions.'

GET /api/marketplace-provider-resources/{uuid}/details/

- Summary changed from '' to 'Get resource details'
- Description changed from '' to 'Returns the detailed representation of the backend resource associated with the marketplace resource. The format of the response depends on the resource type.'
- Deleted query param: field
- Responses changed
  - New response: 204
  - New response: 404
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: attributes
            - Deleted property: available_actions
            - Deleted property: backend_id
            - Deleted property: backend_metadata
            - Deleted property: can_terminate
            - Deleted property: category_icon
            - Deleted property: category_title
            - Deleted property: category_uuid
            - Deleted property: created
            - Deleted property: creation_order
            - Deleted property: current_usages
            - Deleted property: customer_name
            - Deleted property: customer_slug
            - Deleted property: customer_uuid
            - Deleted property: description
            - Deleted property: downscaled
            - Deleted property: effective_id
            - Deleted property: end_date
            - Deleted property: end_date_requested_by
            - Deleted property: endpoints
            - Deleted property: error_message
            - Deleted property: error_traceback
            - Deleted property: is_limit_based
            - Deleted property: is_usage_based
            - Deleted property: last_sync
            - Deleted property: limit_usage
            - Deleted property: limits
            - Deleted property: modified
            - Deleted property: name
            - Deleted property: offering
            - Deleted property: offering_billable
            - Deleted property: offering_description
            - Deleted property: offering_image
            - Deleted property: offering_name
            - Deleted property: offering_plugin_options
            - Deleted property: offering_shared
            - Deleted property: offering_slug
            - Deleted property: offering_thumbnail
            - Deleted property: offering_type
            - Deleted property: offering_uuid
            - Deleted property: options
            - Deleted property: order_in_progress
            - Deleted property: parent_name
            - Deleted property: parent_offering_name
            - Deleted property: parent_offering_slug
            - Deleted property: parent_offering_uuid
            - Deleted property: parent_uuid
            - Deleted property: paused
            - Deleted property: plan
            - Deleted property: plan_description
            - Deleted property: plan_name
            - Deleted property: plan_unit
            - Deleted property: plan_uuid
            - Deleted property: project
            - Deleted property: project_description
            - Deleted property: project_end_date
            - Deleted property: project_end_date_requested_by
            - Deleted property: project_name
            - Deleted property: project_slug
            - Deleted property: project_uuid
            - Deleted property: provider_name
            - Deleted property: provider_slug
            - Deleted property: provider_uuid
            - Deleted property: renewal_date
            - Deleted property: report
            - Deleted property: resource_type
            - Deleted property: resource_uuid
            - Deleted property: restrict_member_access
            - Deleted property: scope
            - Deleted property: service_settings_uuid
            - Deleted property: slug
            - Deleted property: state
            - Deleted property: url
            - Deleted property: user_requires_reconsent
            - Deleted property: username
            - Deleted property: uuid
          - AdditionalProperties changed
            - Schema added

GET /api/marketplace-provider-resources/{uuid}/glauth_users_config/

- Summary changed from '' to 'Get GLauth user configuration for a resource'
- Description changed from '
        This endpoint provides a config file for GLauth.
        Example: <https://github.com/glauth/glauth/blob/master/v2/sample-simple.cfg>
        It is assumed that the config is used by an external agent,
        which synchronizes data from Waldur to GLauth.
        ' to '
        This endpoint provides a GLauth configuration file for the users associated with the project of this resource.
        It is intended for use by an external agent to synchronize user data from Waldur to GLauth.
        '

POST /api/marketplace-provider-resources/{uuid}/move_resource/

- Summary changed from '' to 'Move a resource to another project'
- Description changed from 'Move resource to another project.' to 'Moves a resource and its associated data to a different project. Requires staff permissions.'
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
                    - New property: slug
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: slug

GET /api/marketplace-provider-resources/{uuid}/offering/

- Summary changed from '' to 'Get offering details'
- Description changed from '' to 'Returns details of the offering connected to the requested object.'

GET /api/marketplace-provider-resources/{uuid}/offering_for_subresources/

- Summary changed from '' to 'List offerings for sub-resources'
- Description changed from '' to 'Returns a list of offerings that can be provisioned as sub-resources of the current resource.'

GET /api/marketplace-provider-resources/{uuid}/plan_periods/

- Summary changed from '' to 'List resource plan periods'
- Description changed from '' to 'Returns a list of active and future plan periods for the resource. Each period includes the plan details and current component usage.'

POST /api/marketplace-provider-resources/{uuid}/pull/

- Summary changed from '' to 'Pull resource data'
- Description changed from 'Starts process of pulling a resource' to 'Schedules a task to pull the latest data for the resource from its backend.'
- Responses changed
  - New response: 202
  - Deleted response: 200

POST /api/marketplace-provider-resources/{uuid}/refresh_last_sync/

- Summary changed from '' to 'Refresh last sync time'
- Description changed from 'Refresh the last sync time for a resource.' to 'Updates the 'last_sync' timestamp for a resource to the current time. This is useful for backend agents to signal that a resource is being actively monitored.'

POST /api/marketplace-provider-resources/{uuid}/set_as_erred/

- Summary changed from '' to 'Set resource state to erred'
- Description changed from 'Set the resource as erred.' to 'Allows a service provider to manually set the state of a resource to 'erred'. An error message and traceback can be provided.'

POST /api/marketplace-provider-resources/{uuid}/set_as_ok/

- Extensions changed
  - New extension: x-permissions
- Summary changed from '' to 'Set resource state to OK'
- Description changed from 'Set the resource as OK.' to 'Allows a service provider to manually set the state of a resource to 'OK', clearing any previous error messages.'

POST /api/marketplace-provider-resources/{uuid}/set_backend_id/

- Summary changed from '' to 'Set resource backend ID'
- Description changed from 'Set resource backend ID.' to 'Allows a service provider to set or update the backend ID for a resource, linking it to an external system's identifier.'

POST /api/marketplace-provider-resources/{uuid}/set_backend_metadata/

- Summary changed from '' to 'Set resource backend metadata'
- Description changed from '' to 'Allows a service provider to set or update the backend-specific metadata for a resource.'

POST /api/marketplace-provider-resources/{uuid}/set_downscaled/

- Summary changed from '' to 'Set downscaled flag for resource'
- Description changed from 'Set downscaled flag for resource.' to 'Sets the 'downscaled' flag for a resource. Requires staff permissions.'
- Responses changed
  - Modified response: 200
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

POST /api/marketplace-provider-resources/{uuid}/set_end_date_by_provider/

- Summary changed from '' to 'Set end date by provider'
- Description changed from '' to 'Allows a service provider to set or update the end date for a resource, scheduling it for termination. A notification is sent to the consumer.'
- Responses changed
  - Modified response: 200
    - Description changed from '' to 'No response body'
    - Content changed
      - Deleted media type: application/json

POST /api/marketplace-provider-resources/{uuid}/set_end_date_by_staff/

- Summary changed from '' to 'Set end date of the resource by staff'
- Description changed from 'Set end date of the resource by staff.' to 'Allows a staff user to set or update the end date for a resource, which will schedule it for termination.'

POST /api/marketplace-provider-resources/{uuid}/set_limits/

- Extensions changed
  - New extension: x-permissions
- Summary changed from '' to 'Set resource limits'
- Description changed from '' to 'Allows a service provider to directly set the limits for a resource. This is typically used for administrative changes or backend synchronization, bypassing the normal order process.'

POST /api/marketplace-provider-resources/{uuid}/set_paused/

- Summary changed from '' to 'Set paused flag for resource'
- Description changed from 'Set paused flag for resource.' to 'Sets the 'paused' flag for a resource. Requires staff permissions.'
- Responses changed
  - Modified response: 200
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

POST /api/marketplace-provider-resources/{uuid}/set_restrict_member_access/

- Summary changed from '' to 'Set restrict member access flag'
- Description changed from 'Set restrict_member_access flag for resource.' to 'Sets the 'restrict_member_access' flag for a resource. Requires staff permissions.'
- Responses changed
  - Modified response: 200
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

POST /api/marketplace-provider-resources/{uuid}/set_slug/

- Summary changed from '' to 'Set resource slug'
- Description changed from 'Set slug for resource.' to 'Updates the slug for a resource. Requires staff permissions.'
- Responses changed
  - Modified response: 200
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

POST /api/marketplace-provider-resources/{uuid}/submit_report/

- Summary changed from '' to 'Submit a report for a resource'
- Description changed from 'Submit resource report.' to 'Allows a service provider to submit a report (e.g., usage or status report) for a resource.'

GET /api/marketplace-provider-resources/{uuid}/team/

- Summary changed from '' to 'Get resource team'
- Description changed from 'Return users connected to the project.' to 'Returns a list of users connected to the project of this resource, including their project roles and offering-specific usernames.'

POST /api/marketplace-provider-resources/{uuid}/terminate/

- Summary changed from '' to 'Terminate a resource'
- Description changed from 'Create marketplace order for resource termination.' to 'Creates a marketplace order to terminate the resource. This action is asynchronous and may require approval.'

POST /api/marketplace-provider-resources/{uuid}/unlink/

- Summary changed from '' to 'Unlink a resource (staff only)'
- Description changed from 'Delete marketplace resource and related plugin resource from the database without scheduling operations on backend
and without checking current state of the resource. It is intended to be used
for removing resource stuck in transitioning state.' to 'Forcefully deletes a marketplace resource and its related plugin resource from the database. This action does not schedule operations on the backend and is intended for cleaning up resources stuck in transitioning states. Requires staff permissions.'
- Responses changed
  - New response: 204
  - New response: 403
  - Deleted response: 200

POST /api/marketplace-provider-resources/{uuid}/update_options/

- Summary changed from '' to 'Update resource options'
- Description changed from 'Update resource options.' to 'Updates the options of a resource. If the offering is configured to create orders for option changes, a new UPDATE order will be created. Otherwise, the options are updated directly.'
- Responses changed
  - New response: 201

POST /api/marketplace-provider-resources/{uuid}/update_options_direct/

- Summary changed from '' to 'Update resource options directly'
- Description changed from 'Update resource options directly without creating orders.' to 'Allows a service provider to directly update the options of a resource without creating an order. This is typically used for administrative changes or backend synchronization.'

POST /api/marketplace-public-api/check_signature/

- Summary changed from '' to 'Check service provider signature'
- Description changed from '' to '
        Validates a signed payload from a service provider. The payload is a JWT token
        signed with the provider's API secret code. This endpoint is used to verify the
        authenticity of a request before processing it.

        The `data` field should contain the JWT token.
        '
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Examples changed
        - New example: ExampleSignatureCheckRequest
- Responses changed
  - Modified response: 200
    - Description changed from '' to 'No response body'
    - Content changed
      - Deleted media type: application/json

POST /api/marketplace-public-api/set_usage/

- Summary changed from '' to 'Set component usage with signature'
- Description changed from '' to '
        Allows a service provider to report usage for resource components using a signed JWT payload.
        This provides a secure way for external systems to submit billing data.

        The `data` field must contain a JWT token that, when decoded, matches the structure of the
        `ComponentUsageCreateSerializer`.
        '
- Responses changed
  - New response: 201
  - Deleted response: 200

GET /api/marketplace-public-offerings/

- Summary changed from '' to 'List public offerings'
- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Returns a paginated list of public offerings. The list is filtered to show only offerings that are active or paused and available for ordering by the current user. If anonymous access is enabled, it shows shared offerings available to unauthenticated users.'
- New query param: can_create_offering_user

HEAD /api/marketplace-public-offerings/

- Summary changed from '' to 'List public offerings'
- New query param: can_create_offering_user

GET /api/marketplace-public-offerings/{uuid}/

- Summary changed from '' to 'Retrieve a public offering'
- Description changed from '' to 'Returns the details of a specific public offering. Access is granted if the offering is available for ordering by the current user or if anonymous access is enabled.'

GET /api/marketplace-public-offerings/{uuid}/plans/

- Summary changed from '' to 'List plans for an offering'
- Description changed from '' to 'Returns a list of plans available for a specific offering. The plans are filtered based on the current user's permissions and organization group memberships.'

GET /api/marketplace-public-offerings/{uuid}/plans/{plan_uuid}/

- Summary changed from '' to 'Retrieve a specific plan for an offering'
- Description changed from '' to 'Returns the details of a specific plan if it is available to the current user for the given offering.'

GET /api/marketplace-remote-synchronisations/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/marketplace-resource-users/

- Summary changed from '' to 'List resource users'
- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Returns a paginated list of users associated with resources, including their roles. The list is filtered based on the permissions of the current user. Staff and support users can see all resource-user links. Other users can only see links for resources they have access to.'

HEAD /api/marketplace-resource-users/

- Summary changed from '' to 'List resource users'

POST /api/marketplace-resource-users/

- Summary changed from '' to 'Link a user to a resource'
- Description changed from '' to 'Creates a new association between a user and a resource with a specific role. The user must have permission to manage users for the resource (typically service provider staff or owners).'

DELETE /api/marketplace-resource-users/{uuid}/

- Summary changed from '' to 'Unlink a user from a resource'
- Description changed from '' to 'Removes the association between a user and a resource, effectively revoking their role on that resource. The user must have permission to manage users for the resource.'

GET /api/marketplace-resource-users/{uuid}/

- Summary changed from '' to 'Retrieve a resource-user link'
- Description changed from '' to 'Returns details of a specific link between a user and a resource, including their role.'

GET /api/marketplace-resources/

- Summary changed from '' to 'List consumer resources'
- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Returns a paginated list of resources accessible to the current user as a service consumer.'
- Modified query param: o
  - Schema changed
    - Items changed
      - New enum values: [-end_date end_date]
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
                      - New property: slug
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: slug

HEAD /api/marketplace-resources/

- Summary changed from '' to 'List consumer resources'
- Modified query param: o
  - Schema changed
    - Items changed
      - New enum values: [-end_date end_date]

POST /api/marketplace-resources/suggest_name/

- Summary changed from '' to 'Suggest a resource name'
- Description changed from '' to 'Generates a suggested name for a new resource based on the project and offering.'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Examples changed
        - New example: SuggestANameForANewResource
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: offering
            - Deleted required property: project
          - Properties changed
            - New property: name
            - Deleted property: offering
            - Deleted property: project
        - Examples changed
          - New example: ExampleResponseWithSuggestedName

GET /api/marketplace-resources/{uuid}/

- Summary changed from '' to 'Retrieve a consumer resource'
- Description changed from '' to 'Returns details of a specific resource accessible to the consumer.'
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
                    - New property: slug
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: slug

PATCH /api/marketplace-resources/{uuid}/

- Summary changed from '' to 'Partially update a consumer resource'
- Description changed from '' to 'Partially updates the name, description, or end date of a resource.'

PUT /api/marketplace-resources/{uuid}/

- Summary changed from '' to 'Update a consumer resource'
- Description changed from '' to 'Updates the name, description, or end date of a resource.'

GET /api/marketplace-resources/{uuid}/details/

- Summary changed from '' to 'Get resource details'
- Description changed from '' to 'Returns the detailed representation of the backend resource associated with the marketplace resource. The format of the response depends on the resource type.'
- Deleted query param: field
- Responses changed
  - New response: 204
  - New response: 404
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: attributes
            - Deleted property: available_actions
            - Deleted property: backend_id
            - Deleted property: backend_metadata
            - Deleted property: can_terminate
            - Deleted property: category_icon
            - Deleted property: category_title
            - Deleted property: category_uuid
            - Deleted property: created
            - Deleted property: creation_order
            - Deleted property: current_usages
            - Deleted property: customer_name
            - Deleted property: customer_slug
            - Deleted property: customer_uuid
            - Deleted property: description
            - Deleted property: downscaled
            - Deleted property: effective_id
            - Deleted property: end_date
            - Deleted property: end_date_requested_by
            - Deleted property: endpoints
            - Deleted property: error_message
            - Deleted property: error_traceback
            - Deleted property: is_limit_based
            - Deleted property: is_usage_based
            - Deleted property: last_sync
            - Deleted property: limit_usage
            - Deleted property: limits
            - Deleted property: modified
            - Deleted property: name
            - Deleted property: offering
            - Deleted property: offering_billable
            - Deleted property: offering_description
            - Deleted property: offering_image
            - Deleted property: offering_name
            - Deleted property: offering_plugin_options
            - Deleted property: offering_shared
            - Deleted property: offering_slug
            - Deleted property: offering_thumbnail
            - Deleted property: offering_type
            - Deleted property: offering_uuid
            - Deleted property: options
            - Deleted property: order_in_progress
            - Deleted property: parent_name
            - Deleted property: parent_offering_name
            - Deleted property: parent_offering_slug
            - Deleted property: parent_offering_uuid
            - Deleted property: parent_uuid
            - Deleted property: paused
            - Deleted property: plan
            - Deleted property: plan_description
            - Deleted property: plan_name
            - Deleted property: plan_unit
            - Deleted property: plan_uuid
            - Deleted property: project
            - Deleted property: project_description
            - Deleted property: project_end_date
            - Deleted property: project_end_date_requested_by
            - Deleted property: project_name
            - Deleted property: project_slug
            - Deleted property: project_uuid
            - Deleted property: provider_name
            - Deleted property: provider_slug
            - Deleted property: provider_uuid
            - Deleted property: renewal_date
            - Deleted property: report
            - Deleted property: resource_type
            - Deleted property: resource_uuid
            - Deleted property: restrict_member_access
            - Deleted property: scope
            - Deleted property: service_settings_uuid
            - Deleted property: slug
            - Deleted property: state
            - Deleted property: url
            - Deleted property: user_requires_reconsent
            - Deleted property: username
            - Deleted property: uuid
          - AdditionalProperties changed
            - Schema added

GET /api/marketplace-resources/{uuid}/glauth_users_config/

- Summary changed from '' to 'Get GLauth user configuration for a resource'
- Description changed from '
        This endpoint provides a config file for GLauth.
        Example: <https://github.com/glauth/glauth/blob/master/v2/sample-simple.cfg>
        It is assumed that the config is used by an external agent,
        which synchronizes data from Waldur to GLauth.
        ' to '
        This endpoint provides a GLauth configuration file for the users associated with the project of this resource.
        It is intended for use by an external agent to synchronize user data from Waldur to GLauth.
        '

POST /api/marketplace-resources/{uuid}/move_resource/

- Summary changed from '' to 'Move a resource to another project'
- Description changed from 'Move resource to another project.' to 'Moves a resource and its associated data to a different project. Requires staff permissions.'
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
                    - New property: slug
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: slug

GET /api/marketplace-resources/{uuid}/offering/

- Summary changed from '' to 'Get offering details'
- Description changed from '' to 'Returns details of the offering connected to the requested object.'

GET /api/marketplace-resources/{uuid}/offering_for_subresources/

- Summary changed from '' to 'List offerings for sub-resources'
- Description changed from '' to 'Returns a list of offerings that can be provisioned as sub-resources of the current resource.'

GET /api/marketplace-resources/{uuid}/plan_periods/

- Summary changed from '' to 'List resource plan periods'
- Description changed from '' to 'Returns a list of active and future plan periods for the resource. Each period includes the plan details and current component usage.'

POST /api/marketplace-resources/{uuid}/pull/

- Summary changed from '' to 'Pull resource data'
- Description changed from 'Starts process of pulling a resource' to 'Schedules a task to pull the latest data for the resource from its backend.'
- Responses changed
  - New response: 202
  - Deleted response: 200

POST /api/marketplace-resources/{uuid}/renew/

- Summary changed from '' to 'Renew a prepaid resource'
- Description changed from 'Create a renewal order for a prepaid resource.' to 'Creates a renewal order to extend the subscription period of a prepaid resource. Optionally, limits can be upgraded at the same time.'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Examples changed
        - New example: RenewFor12MonthsWithLimitUpgrade
        - New example: RenewFor6MonthsWithoutChangingLimits
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Examples changed
          - New example: RenewFor12MonthsWithLimitUpgrade
          - New example: RenewFor6MonthsWithoutChangingLimits

POST /api/marketplace-resources/{uuid}/set_downscaled/

- Summary changed from '' to 'Set downscaled flag for resource'
- Description changed from 'Set downscaled flag for resource.' to 'Sets the 'downscaled' flag for a resource. Requires staff permissions.'
- Responses changed
  - Modified response: 200
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

POST /api/marketplace-resources/{uuid}/set_end_date_by_staff/

- Summary changed from '' to 'Set end date of the resource by staff'
- Description changed from 'Set end date of the resource by staff.' to 'Allows a staff user to set or update the end date for a resource, which will schedule it for termination.'

POST /api/marketplace-resources/{uuid}/set_paused/

- Summary changed from '' to 'Set paused flag for resource'
- Description changed from 'Set paused flag for resource.' to 'Sets the 'paused' flag for a resource. Requires staff permissions.'
- Responses changed
  - Modified response: 200
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

POST /api/marketplace-resources/{uuid}/set_restrict_member_access/

- Summary changed from '' to 'Set restrict member access flag'
- Description changed from 'Set restrict_member_access flag for resource.' to 'Sets the 'restrict_member_access' flag for a resource. Requires staff permissions.'
- Responses changed
  - Modified response: 200
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

POST /api/marketplace-resources/{uuid}/set_slug/

- Summary changed from '' to 'Set resource slug'
- Description changed from 'Set slug for resource.' to 'Updates the slug for a resource. Requires staff permissions.'
- Responses changed
  - Modified response: 200
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

POST /api/marketplace-resources/{uuid}/switch_plan/

- Summary changed from '' to 'Switch resource plan'
- Description changed from 'Create marketplace order for resource plan switch.' to 'Creates a marketplace order to switch the billing plan for a resource. This action is asynchronous and may require approval.'

GET /api/marketplace-resources/{uuid}/team/

- Summary changed from '' to 'Get resource team'
- Description changed from 'Return users connected to the project.' to 'Returns a list of users connected to the project of this resource, including their project roles and offering-specific usernames.'

POST /api/marketplace-resources/{uuid}/terminate/

- Summary changed from '' to 'Terminate a resource'
- Description changed from 'Create marketplace order for resource termination.' to 'Creates a marketplace order to terminate the resource. This action is asynchronous and may require approval.'

POST /api/marketplace-resources/{uuid}/unlink/

- Summary changed from '' to 'Unlink a resource (staff only)'
- Description changed from 'Delete marketplace resource and related plugin resource from the database without scheduling operations on backend
and without checking current state of the resource. It is intended to be used
for removing resource stuck in transitioning state.' to 'Forcefully deletes a marketplace resource and its related plugin resource from the database. This action does not schedule operations on the backend and is intended for cleaning up resources stuck in transitioning states. Requires staff permissions.'
- Responses changed
  - New response: 204
  - New response: 403
  - Deleted response: 200

POST /api/marketplace-resources/{uuid}/update_limits/

- Summary changed from '' to 'Update resource limits'
- Description changed from 'Create marketplace order for resource limits update.' to 'Creates a marketplace order to update the limits (e.g., CPU, RAM) for a resource. This action is asynchronous and may require approval.'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Examples changed
        - New example: UpdateResourceLimits
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Examples changed
          - New example: UpdateResourceLimits

POST /api/marketplace-resources/{uuid}/update_options/

- Summary changed from '' to 'Update resource options'
- Description changed from 'Update resource options.' to 'Updates the options of a resource. If the offering is configured to create orders for option changes, a new UPDATE order will be created. Otherwise, the options are updated directly.'
- Responses changed
  - New response: 201

GET /api/marketplace-robot-accounts/

- Summary changed from '' to 'List robot accounts'
- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Returns a paginated list of robot accounts accessible to the current user.'

HEAD /api/marketplace-robot-accounts/

- Summary changed from '' to 'List robot accounts'

POST /api/marketplace-robot-accounts/

- Summary changed from '' to 'Create a robot account'
- Description changed from '' to 'Creates a new robot account for a specific resource. This is typically used for automated access to a resource, e.g., for CI/CD pipelines.'

DELETE /api/marketplace-robot-accounts/{uuid}/

- Summary changed from '' to 'Delete a robot account'
- Description changed from '' to 'Deletes a robot account. This is a hard delete and should be used with caution.'

GET /api/marketplace-robot-accounts/{uuid}/

- Summary changed from '' to 'Retrieve a robot account'
- Description changed from '' to 'Returns the details of a specific robot account.'

PATCH /api/marketplace-robot-accounts/{uuid}/

- Summary changed from '' to 'Partially update a robot account'
- Description changed from '' to 'Partially updates the properties of a robot account. Not allowed for synchronized remote accounts.'

PUT /api/marketplace-robot-accounts/{uuid}/

- Summary changed from '' to 'Update a robot account'
- Description changed from '' to 'Updates the properties of a robot account, such as its username or associated users. Not allowed for synchronized remote accounts.'

POST /api/marketplace-robot-accounts/{uuid}/set_state_creating/

- Summary changed from '' to 'Set robot account state to creating'
- Description changed from '' to 'Transitions the robot account state from 'Requested' to 'Creating'. This is typically used by an agent to signal that the creation process has started.'

POST /api/marketplace-robot-accounts/{uuid}/set_state_deleted/

- Summary changed from '' to 'Set robot account state to deleted'
- Description changed from '' to 'Transitions the robot account state from 'Requested deletion' to 'Deleted', marking the successful completion of the deletion process.'
- Responses changed
  - New response: 400

POST /api/marketplace-robot-accounts/{uuid}/set_state_erred/

- Summary changed from '' to 'Set robot account state to erred'
- Description changed from '' to 'Manually moves the robot account into the 'Error' state. An optional error message can be provided.'
- Responses changed
  - New response: 400

POST /api/marketplace-robot-accounts/{uuid}/set_state_ok/

- Summary changed from '' to 'Set robot account state to OK'
- Description changed from '' to 'Manually sets the robot account state to 'OK', indicating that it is fully operational. This can be used to recover from an error state.'
- Responses changed
  - New response: 400

POST /api/marketplace-robot-accounts/{uuid}/set_state_request_deletion/

- Summary changed from '' to 'Request deletion of a robot account'
- Description changed from '' to 'Transitions the robot account state from 'OK' to 'Requested deletion', initiating the deletion process.'
- Responses changed
  - New response: 400

GET /api/marketplace-runtime-states/

- Summary changed from '' to 'List available runtime states for resources'
- Description changed from 'Retrieve available runtime states for resources, optionally filtered by project and category.' to '
        Returns a unique, sorted list of runtime states for all resources accessible to the current user.
        The runtime state is a backend-specific state of a resource (e.g., 'ACTIVE', 'SHUTOFF' for a VM).
        This endpoint is useful for building dynamic filters in a user interface.
        The list can be optionally filtered by project or category.
        '
- Modified query param: category_uuid
  - Description changed from 'UUID of the category to filter runtime states by.' to 'Filter runtime states by resources belonging to a specific category.'
- Modified query param: project_uuid
  - Description changed from 'UUID of the project to filter runtime states by.' to 'Filter runtime states by resources within a specific project.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Examples changed
          - New example: ExampleResponseForRuntimeStates

GET /api/marketplace-screenshots/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/marketplace-script-async-dry-run/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/marketplace-sections/

- Summary changed from '' to 'List sections'
- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Returns a paginated list of all sections. Sections are used to group attributes within a category.'

HEAD /api/marketplace-sections/

- Summary changed from '' to 'List sections'

POST /api/marketplace-sections/

- Summary changed from '' to 'Create a section'
- Description changed from '' to 'Creates a new section within a category. Requires staff permissions.'

DELETE /api/marketplace-sections/{key}/

- Summary changed from '' to 'Delete a section'
- Description changed from '' to 'Deletes a section. Requires staff permissions.'

GET /api/marketplace-sections/{key}/

- Summary changed from '' to 'Retrieve a section'
- Description changed from '' to 'Returns the details of a specific section, identified by its key.'

PATCH /api/marketplace-sections/{key}/

- Summary changed from '' to 'Partially update a section'
- Description changed from '' to 'Partially updates an existing section. Requires staff permissions.'

PUT /api/marketplace-sections/{key}/

- Summary changed from '' to 'Update a section'
- Description changed from '' to 'Updates an existing section. Requires staff permissions.'

GET /api/marketplace-service-providers/

- Summary changed from '' to 'List service providers'
- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Returns a paginated list of service providers.'

HEAD /api/marketplace-service-providers/

- Summary changed from '' to 'List service providers'

POST /api/marketplace-service-providers/

- Summary changed from '' to 'Create a service provider'
- Description changed from '' to 'Creates a new service provider profile for a customer.'

GET /api/marketplace-service-providers/{service_provider_uuid}/compliance/checklists_summary/

- Summary changed from '' to 'Get summary of compliance checklists'
- Description changed from 'Get summary of all compliance checklists used by this service provider with usage counts.' to 'Returns a summary of all compliance checklists used by this service provider with usage counts.'

GET /api/marketplace-service-providers/{service_provider_uuid}/compliance/compliance_overview/

- Summary changed from '' to 'Get compliance overview for a service provider'
- Description changed from 'Get compliance overview statistics for all offerings managed by this service provider.' to 'Returns compliance overview statistics for all offerings managed by this service provider.'

GET /api/marketplace-service-providers/{service_provider_uuid}/compliance/offering_users/

- Summary changed from '' to 'List offering users' compliance status'
- Description changed from 'List offering users with their compliance status for this service provider.' to 'Returns a list of offering users with their compliance status for this service provider. Can be filtered by offering and compliance status.'
- Modified query param: compliance_status
  - Description changed from 'Filter by compliance status: completed, pending, no_checklist' to 'Filter by compliance status: completed, pending, no_checklist.'
- Modified query param: offering_uuid
  - Description changed from 'Filter by offering UUID' to 'Filter by offering UUID.'

GET /api/marketplace-service-providers/{service_provider_uuid}/course_accounts/

- Summary changed from '' to 'List course project accounts for a service provider'
- Description changed from 'Return course project accounts that have access to resources managed by the provider.

        Checks for:
        - Projects with active service provider's resources
        - Course accounts with non-blank users

        ' to 'Returns a paginated list of course project accounts that have access to resources managed by the provider.

        This includes:
        - Projects with active resources of the service provider.
        - Course accounts with non-blank users.
        '

GET /api/marketplace-service-providers/{service_provider_uuid}/customer_projects/

- Summary changed from '' to 'List customer projects of a service provider'
- Description changed from 'Return customer projects of service provider.' to 'Returns a paginated list of projects belonging to a specific customer that have consumed resources from the specified service provider.'
- New query param: project_customer_uuid

GET /api/marketplace-service-providers/{service_provider_uuid}/customers/

- Summary changed from '' to 'List customers of a service provider'
- Description changed from 'Return customers of service provider.' to 'Returns a paginated list of customers who have consumed resources from the specified service provider.'

GET /api/marketplace-service-providers/{service_provider_uuid}/keys/

- Summary changed from '' to 'List SSH keys of a service provider'
- Description changed from 'Return SSH keys of service provider.' to 'Returns a paginated list of SSH public keys for all users who have consumed resources from the specified service provider.'

GET /api/marketplace-service-providers/{service_provider_uuid}/offerings/

- Summary changed from '' to 'List offerings of a service provider'
- Description changed from 'Return offerings of service provider.' to 'Returns a paginated list of all billable, shared offerings provided by the specified service provider.'
- New query param: can_create_offering_user

GET /api/marketplace-service-providers/{service_provider_uuid}/project_permissions/

- Summary changed from '' to 'List project permissions of a service provider'
- Description changed from 'Return project permissions of service provider.' to 'Returns a paginated list of project permissions for all projects that have consumed resources from the specified service provider.'

GET /api/marketplace-service-providers/{service_provider_uuid}/project_service_accounts/

- Summary changed from '' to 'List project service accounts for a service provider'
- Description changed from 'Return project service accounts that have access to resources managed by the provider.

        Checks for:
        - Projects with active service provider's resources
        - Service accounts with non-blank usernames

        ' to 'Returns a paginated list of project service accounts that have access to resources managed by the provider.

        This includes:
        - Projects with active resources of the service provider.
        - Service accounts with non-blank usernames.
        '

GET /api/marketplace-service-providers/{service_provider_uuid}/projects/

- Summary changed from '' to 'List projects of a service provider'
- Description changed from 'Return projects of service provider.' to 'Returns a paginated list of all projects that have consumed resources from the specified service provider.'
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [grace_period_days]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: grace_period_days

GET /api/marketplace-service-providers/{service_provider_uuid}/user_customers/

- Summary changed from '' to 'List customers of a specific user within a service provider's scope'
- Description changed from 'Return customers that have access role for a specified user within service provider's scope.

        Checks for:
        - Customers where user has direct permissions
        - Customers with projects where user has project roles
        - Customers related to service provider's resources

        If user UUID is invalid or missing, returns empty list.' to 'Returns a paginated list of customers that a specified user has access to within the scope of a service provider.

        This includes:
        - Customers where the user has direct permissions.
        - Customers with projects where the user has project roles.
        - Customers related to the service provider's resources that the user can access.
        '
- Modified query param: user_uuid
  - Description changed from 'UUID of user to get related customers for' to 'UUID of the user to get related customers for.'

GET /api/marketplace-service-providers/{service_provider_uuid}/users/

- Summary changed from '' to 'List users of a service provider'
- Description changed from 'Return users of service provider.' to 'Returns a paginated list of all users who have consumed resources from the specified service provider.'

DELETE /api/marketplace-service-providers/{uuid}/

- Summary changed from '' to 'Delete a service provider'
- Description changed from '' to 'Deletes a service provider profile. Only possible if there are no active offerings.'

GET /api/marketplace-service-providers/{uuid}/

- Summary changed from '' to 'Retrieve a service provider'
- Description changed from '' to 'Returns details of a specific service provider.'

PATCH /api/marketplace-service-providers/{uuid}/

- Summary changed from '' to 'Partially update a service provider'
- Description changed from '' to 'Partially updates an existing service provider profile.'

PUT /api/marketplace-service-providers/{uuid}/

- Summary changed from '' to 'Update a service provider'
- Description changed from '' to 'Updates an existing service provider profile.'

POST /api/marketplace-service-providers/{uuid}/add_user/

- Summary changed from '' to 'Grant a role to a user'
- Description changed from '' to 'Assigns a specific role to a user within the current scope. An optional expiration time for the role can be set.'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Examples changed
        - New example: GrantProjectAdminRoleUntilEndOfYear
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Examples changed
          - New example: SuccessfulRoleGrantResponse
  - Modified response: 400
    - Description changed from '' to 'Validation error, for example when trying to add a user to a terminated project.'
    - Content changed
      - Deleted media type: application/json

GET /api/marketplace-service-providers/{uuid}/api_secret_code/

- Summary changed from '' to 'Get service provider API secret code'
- Description changed from 'Return service provider API secret code.' to 'Returns the API secret code for a service provider. Requires service provider owner permission.'

POST /api/marketplace-service-providers/{uuid}/api_secret_code/

- Summary changed from '' to 'Generate new service provider API secret code'
- Description changed from 'Generate new service provider API secret code.' to 'Generates a new API secret code for a service provider, invalidating the old one. Requires service provider owner permission.'

POST /api/marketplace-service-providers/{uuid}/delete_user/

- Summary changed from '' to 'Revoke a role from a user'
- Description changed from '' to 'Removes a specific role from a user within the current scope. This effectively revokes their permissions associated with that role.'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Examples changed
        - New example: RevokeProjectAdminRoleFromUser
- Responses changed
  - Modified response: 200
    - Description changed from 'No response body' to 'Role revoked successfully.'

GET /api/marketplace-service-providers/{uuid}/list_users/

- Summary changed from '' to 'List users and their roles in a scope'
- Description changed from '' to 'Retrieves a list of users who have a role within a specific scope (e.g., a project or an organization). The list can be filtered by user details or role.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Examples changed
          - New example: ExampleUserRoleListResponse

GET /api/marketplace-service-providers/{uuid}/revenue/

- Summary changed from '' to 'Get service provider revenue'
- Description changed from '' to 'Returns monthly revenue data for the last year for the service provider.'

GET /api/marketplace-service-providers/{uuid}/robot_account_customers/

- Summary changed from '' to 'List customers with robot accounts'
- Description changed from '' to 'Returns a paginated list of customers who have robot accounts for resources managed by this service provider.'
- Modified query param: customer_name
  - Description changed from '' to 'Filter by customer name (case-insensitive partial match).'

GET /api/marketplace-service-providers/{uuid}/robot_account_projects/

- Summary changed from '' to 'List projects with robot accounts'
- Description changed from '' to 'Returns a paginated list of projects which have robot accounts for resources managed by this service provider.'
- Modified query param: project_name
  - Description changed from '' to 'Filter by project name (case-insensitive partial match).'

POST /api/marketplace-service-providers/{uuid}/set_offerings_username/

- Summary changed from '' to 'Set offering username for a user'
- Description changed from '' to 'Sets or updates the offering-specific username for a user across all offerings managed by the service provider that the user has access to.'

GET /api/marketplace-service-providers/{uuid}/stat/

- Summary changed from '' to 'Get service provider statistics'
- Description changed from '' to 'Returns various statistics for the service provider, such as number of active campaigns, customers, and resources.'

POST /api/marketplace-service-providers/{uuid}/update_user/

- Summary changed from '' to 'Update a user's role expiration'
- Description changed from '' to 'Updates the expiration time for a user's existing role in the current scope. This is useful for extending or shortening the duration of a permission. To make a role permanent, set expiration_time to null.'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Examples changed
        - New example: ExtendRoleUntilMid-2025
        - New example: MakeARolePermanent
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Examples changed
          - New example: SuccessfulRoleUpdateResponse

GET /api/marketplace-site-agent-identities/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/marketplace-site-agent-processors/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/marketplace-site-agent-services/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/marketplace-software-catalogs/

- Summary changed from '' to 'List software catalogs'
- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Returns a paginated list of available software catalogs, such as EESSI or Spack.'

HEAD /api/marketplace-software-catalogs/

- Summary changed from '' to 'List software catalogs'

POST /api/marketplace-software-catalogs/

- Summary changed from '' to 'Create a software catalog'
- Description changed from '' to 'Creates a new software catalog. Requires staff permissions.'

DELETE /api/marketplace-software-catalogs/{uuid}/

- Summary changed from '' to 'Delete a software catalog'
- Description changed from '' to 'Deletes a software catalog. Requires staff permissions.'

GET /api/marketplace-software-catalogs/{uuid}/

- Summary changed from '' to 'Retrieve a software catalog'
- Description changed from '' to 'Returns the details of a specific software catalog, including its name, version, and the number of packages it contains.'

PATCH /api/marketplace-software-catalogs/{uuid}/

- Summary changed from '' to 'Partially update a software catalog'
- Description changed from '' to 'Partially updates an existing software catalog. Requires staff permissions.'

PUT /api/marketplace-software-catalogs/{uuid}/

- Summary changed from '' to 'Update a software catalog'
- Description changed from '' to 'Updates an existing software catalog. Requires staff permissions.'

GET /api/marketplace-software-packages/

- Summary changed from '' to 'List software packages'
- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Returns a paginated list of software packages available in the catalogs. Can be filtered by catalog, offering, or various package attributes.'

HEAD /api/marketplace-software-packages/

- Summary changed from '' to 'List software packages'

POST /api/marketplace-software-packages/

- Summary changed from '' to 'Create a software package'
- Description changed from '' to 'Creates a new software package within a catalog. Requires staff permissions.'

DELETE /api/marketplace-software-packages/{uuid}/

- Summary changed from '' to 'Delete a software package'
- Description changed from '' to 'Deletes a software package. Requires staff permissions.'

GET /api/marketplace-software-packages/{uuid}/

- Summary changed from '' to 'Retrieve a software package'
- Description changed from '' to 'Returns the details of a specific software package, including its description, homepage, and available versions.'

PATCH /api/marketplace-software-packages/{uuid}/

- Summary changed from '' to 'Partially update a software package'
- Description changed from '' to 'Partially updates an existing software package. Requires staff permissions.'

PUT /api/marketplace-software-packages/{uuid}/

- Summary changed from '' to 'Update a software package'
- Description changed from '' to 'Updates an existing software package. Requires staff permissions.'

GET /api/marketplace-software-targets/

- Summary changed from '' to 'List software targets'
- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Returns a paginated list of software targets, which represent specific builds of a software version for a given CPU architecture.'

HEAD /api/marketplace-software-targets/

- Summary changed from '' to 'List software targets'

POST /api/marketplace-software-targets/

- Summary changed from '' to 'Create a software target'
- Description changed from '' to 'Creates a new target for a software version. Requires staff permissions.'

DELETE /api/marketplace-software-targets/{uuid}/

- Summary changed from '' to 'Delete a software target'
- Description changed from '' to 'Deletes a software target. Requires staff permissions.'

GET /api/marketplace-software-targets/{uuid}/

- Summary changed from '' to 'Retrieve a software target'
- Description changed from '' to 'Returns the details of a specific software target, including its CPU family, microarchitecture, and path.'

PATCH /api/marketplace-software-targets/{uuid}/

- Summary changed from '' to 'Partially update a software target'
- Description changed from '' to 'Partially updates an existing software target. Requires staff permissions.'

PUT /api/marketplace-software-targets/{uuid}/

- Summary changed from '' to 'Update a software target'
- Description changed from '' to 'Updates an existing software target. Requires staff permissions.'

GET /api/marketplace-software-versions/

- Summary changed from '' to 'List software versions'
- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Returns a paginated list of software versions. Can be filtered by package, catalog, offering, or CPU architecture.'

HEAD /api/marketplace-software-versions/

- Summary changed from '' to 'List software versions'

POST /api/marketplace-software-versions/

- Summary changed from '' to 'Create a software version'
- Description changed from '' to 'Creates a new version for a software package. Requires staff permissions.'

DELETE /api/marketplace-software-versions/{uuid}/

- Summary changed from '' to 'Delete a software version'
- Description changed from '' to 'Deletes a software version. Requires staff permissions.'

GET /api/marketplace-software-versions/{uuid}/

- Summary changed from '' to 'Retrieve a software version'
- Description changed from '' to 'Returns the details of a specific software version, including its release date and target count.'

PATCH /api/marketplace-software-versions/{uuid}/

- Summary changed from '' to 'Partially update a software version'
- Description changed from '' to 'Partially updates an existing software version. Requires staff permissions.'

PUT /api/marketplace-software-versions/{uuid}/

- Summary changed from '' to 'Update a software version'
- Description changed from '' to 'Updates an existing software version. Requires staff permissions.'

GET /api/marketplace-user-offering-consents/

- Summary changed from '' to 'List user offering consents'
- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Returns a paginated list of Terms of Service consents for the current user. Staff and support users can see all consents.'

HEAD /api/marketplace-user-offering-consents/

- Summary changed from '' to 'List user offering consents'

POST /api/marketplace-user-offering-consents/

- Summary changed from '' to 'Grant consent to an offering's Terms of Service'
- Description changed from '' to 'Creates a consent record for the current user and a specific offering. This indicates that the user has accepted the active Terms of Service for that offering. If a consent already exists (even if revoked), it will be reactivated and updated with the current ToS version.'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Examples changed
        - New example: GrantConsentToAnOffering
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Examples changed
          - New example: GrantConsentToAnOffering

GET /api/marketplace-user-offering-consents/{uuid}/

- Summary changed from '' to 'Retrieve a user offering consent'
- Description changed from '' to 'Returns the details of a specific consent record.'

POST /api/marketplace-user-offering-consents/{uuid}/revoke/

- Summary changed from '' to 'Revoke consent to Terms of Service'
- Description changed from 'Revoke consent to Terms of Service for an offering.' to 'Revokes a user's consent to the Terms of Service for an offering. The consent record is marked with a revocation date, and the user may lose access to related resources if consent is required.'

GET /api/metadata/events/

- Summary changed from '' to 'Get event metadata'
- Description changed from 'Get event metadata grouped by categories' to 'Retrieves metadata for all available event types, grouped by categories. This endpoint is publicly accessible and is useful for building UIs for event filtering or webhook configuration.'

GET /api/metadata/features/

- Summary changed from '' to 'Get feature flag metadata'
- Description changed from 'Get feature metadata including toggles and descriptions' to 'Retrieves metadata for all available feature flags, including their keys, descriptions, and grouping sections. This endpoint is publicly accessible and helps UIs to dynamically render feature-related settings.'

GET /api/metadata/permissions/

- Summary changed from '' to 'Get permission metadata'
- Description changed from 'Get permission metadata including roles, permissions, and descriptions' to 'Retrieves metadata about roles, permissions, and their descriptions. This endpoint is publicly accessible and provides data needed for UI components, such as role selection dropdowns and permission management interfaces.'

GET /api/metadata/settings/

- Summary changed from '' to 'Get overridable settings metadata'
- Description changed from 'Get settings metadata from Constance configuration' to 'Retrieves metadata for all settings that can be configured via the Constance backend. This includes setting keys, human-readable descriptions, default values, and types. This endpoint is publicly accessible.'

GET /api/notification-messages-templates/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

POST /api/notification-messages-templates/{uuid}/override/

- Summary changed from '' to 'Override notification template content'

GET /api/notification-messages/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

POST /api/notification-messages/{uuid}/disable/

- Summary changed from '' to 'Disable a notification'

POST /api/notification-messages/{uuid}/enable/

- Summary changed from '' to 'Enable a notification'

GET /api/onboarding-country-configs/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: questions
                - Items changed
                  - Properties changed
                    - New property: allowed_file_types
                    - New property: allowed_mime_types
                    - New property: max_file_size_mb
                    - New property: max_files_count
                    - Modified property: question_type
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/QuestionTypeEnum
                          - New enum values: [multiple_files]

POST /api/onboarding-country-configs/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: questions
              - Items changed
                - Properties changed
                  - New property: allowed_file_types
                  - New property: allowed_mime_types
                  - New property: max_file_size_mb
                  - New property: max_files_count
                  - Modified property: question_type
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/QuestionTypeEnum
                        - New enum values: [multiple_files]

GET /api/onboarding-country-configs/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: questions
              - Items changed
                - Properties changed
                  - New property: allowed_file_types
                  - New property: allowed_mime_types
                  - New property: max_file_size_mb
                  - New property: max_files_count
                  - Modified property: question_type
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/QuestionTypeEnum
                        - New enum values: [multiple_files]

PATCH /api/onboarding-country-configs/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: questions
              - Items changed
                - Properties changed
                  - New property: allowed_file_types
                  - New property: allowed_mime_types
                  - New property: max_file_size_mb
                  - New property: max_files_count
                  - Modified property: question_type
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/QuestionTypeEnum
                        - New enum values: [multiple_files]

PUT /api/onboarding-country-configs/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: questions
              - Items changed
                - Properties changed
                  - New property: allowed_file_types
                  - New property: allowed_mime_types
                  - New property: max_file_size_mb
                  - New property: max_files_count
                  - Modified property: question_type
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/QuestionTypeEnum
                        - New enum values: [multiple_files]

GET /api/onboarding-justifications/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/onboarding-question-metadata/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/onboarding-verifications/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: validation_method
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/ValidationMethodEnum
                    - New enum values: [bolagsverket]

POST /api/onboarding-verifications/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: validation_method
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/ValidationMethodEnum
                  - New enum values: [bolagsverket]

GET /api/onboarding-verifications/checklist-template/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: initial_visible_questions
              - Items changed
                - Properties changed
                  - New property: allowed_file_types
                  - New property: allowed_mime_types
                  - New property: always_requires_review
                  - New property: always_show_guidance
                  - New property: dependency_logic_operator
                  - New property: guidance_answer_value
                  - New property: guidance_operator
                  - New property: max_file_size_mb
                  - New property: max_files_count
                  - New property: max_value
                  - New property: min_value
                  - New property: operator
                  - New property: order
                  - New property: question_type
                  - New property: review_answer_value
            - Modified property: questions
              - Items changed
                - Properties changed
                  - New property: allowed_file_types
                  - New property: allowed_mime_types
                  - New property: always_requires_review
                  - New property: always_show_guidance
                  - New property: dependency_logic_operator
                  - New property: guidance_answer_value
                  - New property: guidance_operator
                  - New property: max_file_size_mb
                  - New property: max_files_count
                  - New property: max_value
                  - New property: min_value
                  - New property: operator
                  - New property: order
                  - New property: question_type
                  - New property: review_answer_value

POST /api/onboarding-verifications/start_verification/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: validation_method
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/ValidationMethodEnum
                  - New enum values: [bolagsverket]

GET /api/onboarding-verifications/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: validation_method
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/ValidationMethodEnum
                  - New enum values: [bolagsverket]

PATCH /api/onboarding-verifications/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: validation_method
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/ValidationMethodEnum
                  - New enum values: [bolagsverket]

PUT /api/onboarding-verifications/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: validation_method
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/ValidationMethodEnum
                  - New enum values: [bolagsverket]

GET /api/onboarding-verifications/{uuid}/checklist/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: questions
              - Items changed
                - Required changed
                  - New required property: allowed_file_types
                  - New required property: allowed_mime_types
                  - New required property: max_file_size_mb
                  - New required property: max_files_count
                - Properties changed
                  - New property: allowed_file_types
                  - New property: allowed_mime_types
                  - New property: max_file_size_mb
                  - New property: max_files_count
                  - Modified property: question_type
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/QuestionTypeEnum
                        - New enum values: [multiple_files]

POST /api/onboarding-verifications/{uuid}/create_customer/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: grace_period_days
            - Modified property: access_subnets
              - ReadOnly changed from true to false
            - Modified property: accounting_start_date
              - ReadOnly changed from true to false
            - Modified property: agreement_number
              - ReadOnly changed from true to false
            - Modified property: archived
              - ReadOnly changed from true to false
            - Modified property: blocked
              - ReadOnly changed from true to false
            - Modified property: default_tax_percent
              - ReadOnly changed from true to false
            - Modified property: display_billing_info_in_projects
              - ReadOnly changed from true to false
            - Modified property: domain
              - ReadOnly changed from true to false
            - Modified property: max_service_accounts
              - ReadOnly changed from true to false
            - Modified property: project_metadata_checklist
              - ReadOnly changed from true to false
            - Modified property: sponsor_number
              - ReadOnly changed from true to false

POST /api/onboarding-verifications/{uuid}/run_validation/

- Request body changed
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: validation_method
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/ValidationMethodEnum
                  - New enum values: [bolagsverket]

GET /api/openstack-backups/

- Summary changed from '' to 'List backups'
- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get a list of instance backups.'

HEAD /api/openstack-backups/

- Summary changed from '' to 'List backups'

DELETE /api/openstack-backups/{uuid}/

- Summary changed from '' to 'Delete backup'
- Description changed from '' to 'Delete an instance backup.'

GET /api/openstack-backups/{uuid}/

- Summary changed from '' to 'Get backup details'
- Description changed from '' to 'Retrieve details of a specific instance backup.'

PATCH /api/openstack-backups/{uuid}/

- Summary changed from '' to 'Partially update backup'
- Description changed from '' to 'Update specific fields of an instance backup.'

PUT /api/openstack-backups/{uuid}/

- Summary changed from '' to 'Update backup'
- Description changed from '' to 'Update an existing instance backup.'

POST /api/openstack-backups/{uuid}/pull/

- Summary changed from '' to 'Synchronize resource state'
- Description changed from '' to 'Schedule an asynchronous pull operation to synchronize resource state from the backend. Returns 202 if the pull was scheduled successfully, or 409 if the pull operation is not implemented for this resource type.'
- Responses changed
  - New response: 202
  - New response: 409
  - Deleted response: 200

POST /api/openstack-backups/{uuid}/restore/

- Summary changed from '' to 'Restore instance from backup'

POST /api/openstack-backups/{uuid}/unlink/

- Summary changed from '' to 'Unlink resource'
- Description changed from 'Delete resource from the database without scheduling operations on backend
and without checking current state of the resource. It is intended to be used
for removing resource stuck in transitioning state.' to 'Delete resource from the database without scheduling operations on backend
        and without checking current state of the resource. It is intended to be used
        for removing resource stuck in transitioning state.'
- Responses changed
  - New response: 204
  - Deleted response: 200

GET /api/openstack-flavors/

- Summary changed from '' to 'List flavors'
- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get a list of available VM instance flavors.'

HEAD /api/openstack-flavors/

- Summary changed from '' to 'List flavors'

GET /api/openstack-flavors/usage_stats/

- Summary changed from '' to 'Get flavor usage statistics'
- Description changed from '' to 'Retrieve usage statistics for VM instance flavors, showing running and created instance counts for each flavor.'

HEAD /api/openstack-flavors/usage_stats/

- Summary changed from '' to 'Get flavor usage statistics'

GET /api/openstack-flavors/{uuid}/

- Summary changed from '' to 'Get flavor details'
- Description changed from '' to 'Retrieve details of a specific VM instance flavor.'

GET /api/openstack-floating-ips/

- Summary changed from '' to 'List floating IPs'
- Description changed from 'Status *DOWN* means that floating IP is not linked to a VM, status *ACTIVE* means that it is in use.' to 'Get a list of floating IP addresses. Status *DOWN* means that floating IP is not linked to a VM, status *ACTIVE* means that it is in use.'

HEAD /api/openstack-floating-ips/

- Summary changed from '' to 'List floating IPs'

DELETE /api/openstack-floating-ips/{uuid}/

- Summary changed from '' to 'Delete floating IP'
- Description changed from '' to 'Delete a floating IP address.'

GET /api/openstack-floating-ips/{uuid}/

- Summary changed from '' to 'Get floating IP details'
- Description changed from '' to 'Retrieve details of a specific floating IP address.'

POST /api/openstack-floating-ips/{uuid}/attach_to_port/

- Summary changed from '' to 'Attach floating IP to a port'

POST /api/openstack-floating-ips/{uuid}/detach_from_port/

- Summary changed from '' to 'Detach floating IP from port'

POST /api/openstack-floating-ips/{uuid}/pull/

- Summary changed from '' to 'Synchronize resource state'
- Description changed from '' to 'Schedule an asynchronous pull operation to synchronize resource state from the backend. Returns 202 if the pull was scheduled successfully, or 409 if the pull operation is not implemented for this resource type.'
- Responses changed
  - New response: 202
  - New response: 409
  - Deleted response: 200

POST /api/openstack-floating-ips/{uuid}/unlink/

- Summary changed from '' to 'Unlink resource'
- Description changed from 'Delete resource from the database without scheduling operations on backend
and without checking current state of the resource. It is intended to be used
for removing resource stuck in transitioning state.' to 'Delete resource from the database without scheduling operations on backend
        and without checking current state of the resource. It is intended to be used
        for removing resource stuck in transitioning state.'
- Responses changed
  - New response: 204
  - Deleted response: 200

POST /api/openstack-floating-ips/{uuid}/update_description/

- Summary changed from '' to 'Update floating IP description'

GET /api/openstack-images/

- Summary changed from '' to 'List images'
- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get a list of available VM instance images.'

HEAD /api/openstack-images/

- Summary changed from '' to 'List images'

GET /api/openstack-images/usage_stats/

- Summary changed from '' to 'Get image usage statistics'
- Description changed from '' to 'Retrieve usage statistics for VM instance images, showing running and created instance counts for each image.'

HEAD /api/openstack-images/usage_stats/

- Summary changed from '' to 'Get image usage statistics'

GET /api/openstack-images/{uuid}/

- Summary changed from '' to 'Get image details'
- Description changed from '' to 'Retrieve details of a specific VM instance image.'

GET /api/openstack-instance-availability-zones/

- Summary changed from '' to 'List instance availability zones'
- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get a list of instance availability zones.'

HEAD /api/openstack-instance-availability-zones/

- Summary changed from '' to 'List instance availability zones'

GET /api/openstack-instance-availability-zones/{uuid}/

- Summary changed from '' to 'Get instance availability zone details'
- Description changed from '' to 'Retrieve details of a specific instance availability zone.'

GET /api/openstack-instances/

- Summary changed from '' to 'List instances'
- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get a list of VM instances.'

HEAD /api/openstack-instances/

- Summary changed from '' to 'List instances'

GET /api/openstack-instances/{uuid}/

- Summary changed from '' to 'Get instance details'
- Description changed from '' to 'Retrieve details of a specific VM instance.'

PATCH /api/openstack-instances/{uuid}/

- Summary changed from '' to 'Partially update instance'
- Description changed from '' to 'Update specific fields of a VM instance.'

PUT /api/openstack-instances/{uuid}/

- Summary changed from '' to 'Update instance'
- Description changed from '' to 'Update an existing VM instance.'

POST /api/openstack-instances/{uuid}/backup/

- Summary changed from '' to 'Create instance backup'

POST /api/openstack-instances/{uuid}/change_flavor/

- Summary changed from '' to 'Change instance flavor'

GET /api/openstack-instances/{uuid}/console/

- Summary changed from '' to 'Get console URL'

GET /api/openstack-instances/{uuid}/console_log/

- Summary changed from '' to 'Get console log'

GET /api/openstack-instances/{uuid}/floating_ips/

- Summary changed from '' to 'List instance floating IPs'

GET /api/openstack-instances/{uuid}/ports/

- Summary changed from '' to 'List instance ports'

POST /api/openstack-instances/{uuid}/pull/

- Summary changed from '' to 'Synchronize resource state'
- Description changed from '' to 'Schedule an asynchronous pull operation to synchronize resource state from the backend. Returns 202 if the pull was scheduled successfully, or 409 if the pull operation is not implemented for this resource type.'
- Responses changed
  - New response: 202
  - New response: 409
  - Deleted response: 200

POST /api/openstack-instances/{uuid}/restart/

- Summary changed from '' to 'Restart instance'

POST /api/openstack-instances/{uuid}/start/

- Summary changed from '' to 'Start instance'

POST /api/openstack-instances/{uuid}/stop/

- Summary changed from '' to 'Stop instance'

POST /api/openstack-instances/{uuid}/unlink/

- Summary changed from '' to 'Unlink resource'
- Description changed from 'Delete resource from the database without scheduling operations on backend
and without checking current state of the resource. It is intended to be used
for removing resource stuck in transitioning state.' to 'Delete resource from the database without scheduling operations on backend
        and without checking current state of the resource. It is intended to be used
        for removing resource stuck in transitioning state.'
- Responses changed
  - New response: 204
  - Deleted response: 200

POST /api/openstack-instances/{uuid}/update_allowed_address_pairs/

- Summary changed from '' to 'Update instance allowed address pairs'

POST /api/openstack-instances/{uuid}/update_floating_ips/

- Summary changed from '' to 'Update instance floating IPs'

POST /api/openstack-instances/{uuid}/update_ports/

- Summary changed from '' to 'Update instance ports'

POST /api/openstack-instances/{uuid}/update_security_groups/

- Summary changed from '' to 'Update instance security groups'

GET /api/openstack-marketplace-tenants/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/openstack-migrations/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/openstack-network-rbac-policies/

- Summary changed from '' to 'List network RBAC policies'
- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get a list of network RBAC policies.'

HEAD /api/openstack-network-rbac-policies/

- Summary changed from '' to 'List network RBAC policies'

POST /api/openstack-network-rbac-policies/

- Summary changed from '' to 'Create RBAC policy'

DELETE /api/openstack-network-rbac-policies/{uuid}/

- Summary changed from '' to 'Delete RBAC policy'

GET /api/openstack-network-rbac-policies/{uuid}/

- Summary changed from '' to 'Get network RBAC policy details'
- Description changed from '' to 'Retrieve details of a specific network RBAC policy.'

GET /api/openstack-networks/

- Summary changed from '' to 'List networks'
- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get a list of networks.'

HEAD /api/openstack-networks/

- Summary changed from '' to 'List networks'

DELETE /api/openstack-networks/{uuid}/

- Summary changed from '' to 'Delete network'
- Description changed from '' to 'Delete a network.'

GET /api/openstack-networks/{uuid}/

- Summary changed from '' to 'Get network details'
- Description changed from '' to 'Retrieve details of a specific network.'

PATCH /api/openstack-networks/{uuid}/

- Summary changed from '' to 'Partially update network'
- Description changed from '' to 'Update specific fields of a network.'

PUT /api/openstack-networks/{uuid}/

- Summary changed from '' to 'Update network'
- Description changed from '' to 'Update an existing network.'

POST /api/openstack-networks/{uuid}/create_subnet/

- Summary changed from '' to 'Create subnet'
- Description changed from '' to 'Create a new subnet within the network.'

POST /api/openstack-networks/{uuid}/pull/

- Summary changed from '' to 'Synchronize resource state'
- Description changed from '' to 'Schedule an asynchronous pull operation to synchronize resource state from the backend. Returns 202 if the pull was scheduled successfully, or 409 if the pull operation is not implemented for this resource type.'
- Responses changed
  - New response: 202
  - New response: 409
  - Deleted response: 200

POST /api/openstack-networks/{uuid}/rbac_policy_create/

- Summary changed from '' to 'Create RBAC policy'
- Description changed from 'Create RBAC policy for the network' to 'Create RBAC policy for the network. DEPRECATED: please use the dedicated /api/openstack-network-rbac-policies/ endpoint.'
- Deprecated changed from false to true

DELETE /api/openstack-networks/{uuid}/rbac_policy_delete/{rbac_policy_uuid}/

- Summary changed from '' to 'Delete RBAC policy'
- Description changed from 'Delete RBAC policy for the network' to 'Delete RBAC policy for the network. DEPRECATED: please use the dedicated /api/openstack-network-rbac-policies/ endpoint.'
- Deprecated changed from false to true

POST /api/openstack-networks/{uuid}/set_mtu/

- Summary changed from '' to 'Set network MTU'
- Description changed from '' to 'Update the Maximum Transmission Unit (MTU) for the network.'

POST /api/openstack-networks/{uuid}/unlink/

- Summary changed from '' to 'Unlink resource'
- Description changed from 'Delete resource from the database without scheduling operations on backend
and without checking current state of the resource. It is intended to be used
for removing resource stuck in transitioning state.' to 'Delete resource from the database without scheduling operations on backend
        and without checking current state of the resource. It is intended to be used
        for removing resource stuck in transitioning state.'
- Responses changed
  - New response: 204
  - Deleted response: 200

GET /api/openstack-ports/

- Summary changed from '' to 'List ports'
- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get a list of network ports.'

HEAD /api/openstack-ports/

- Summary changed from '' to 'List ports'

POST /api/openstack-ports/

- Summary changed from '' to 'Create port'
- Description changed from '' to 'Create a new network port.'

DELETE /api/openstack-ports/{uuid}/

- Summary changed from '' to 'Delete port'
- Description changed from '' to 'Delete a network port.'

GET /api/openstack-ports/{uuid}/

- Summary changed from '' to 'Get port details'
- Description changed from '' to 'Retrieve details of a specific network port.'

PATCH /api/openstack-ports/{uuid}/

- Summary changed from '' to 'Partially update port'
- Description changed from '' to 'Update specific fields of a network port.'

PUT /api/openstack-ports/{uuid}/

- Summary changed from '' to 'Update port'
- Description changed from '' to 'Update an existing network port.'

POST /api/openstack-ports/{uuid}/disable_port/

- Summary changed from '' to 'Disable port'

POST /api/openstack-ports/{uuid}/disable_port_security/

- Summary changed from '' to 'Disable port security'

POST /api/openstack-ports/{uuid}/enable_port/

- Summary changed from '' to 'Enable port'

POST /api/openstack-ports/{uuid}/enable_port_security/

- Summary changed from '' to 'Enable port security'

POST /api/openstack-ports/{uuid}/pull/

- Summary changed from '' to 'Synchronize resource state'
- Description changed from '' to 'Schedule an asynchronous pull operation to synchronize resource state from the backend. Returns 202 if the pull was scheduled successfully, or 409 if the pull operation is not implemented for this resource type.'
- Responses changed
  - New response: 202
  - New response: 409
  - Deleted response: 200

POST /api/openstack-ports/{uuid}/unlink/

- Summary changed from '' to 'Unlink resource'
- Description changed from 'Delete resource from the database without scheduling operations on backend
and without checking current state of the resource. It is intended to be used
for removing resource stuck in transitioning state.' to 'Delete resource from the database without scheduling operations on backend
        and without checking current state of the resource. It is intended to be used
        for removing resource stuck in transitioning state.'
- Responses changed
  - New response: 204
  - Deleted response: 200

POST /api/openstack-ports/{uuid}/update_port_ip/

- Summary changed from '' to 'Update port IP address'

POST /api/openstack-ports/{uuid}/update_security_groups/

- Summary changed from '' to 'Update port security groups'

GET /api/openstack-routers/

- Summary changed from '' to 'List routers'
- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get a list of routers.'

HEAD /api/openstack-routers/

- Summary changed from '' to 'List routers'

POST /api/openstack-routers/

- Summary changed from '' to 'Create router'
- Description changed from '' to 'Create a new router.'

DELETE /api/openstack-routers/{uuid}/

- Summary changed from '' to 'Delete router'
- Description changed from '' to 'Delete a router.'

GET /api/openstack-routers/{uuid}/

- Summary changed from '' to 'Get router details'
- Description changed from '' to 'Retrieve details of a specific router.'

POST /api/openstack-routers/{uuid}/add_router_interface/

- Summary changed from '' to 'Add router interface'

POST /api/openstack-routers/{uuid}/remove_router_interface/

- Summary changed from '' to 'Remove router interface'

POST /api/openstack-routers/{uuid}/set_routes/

- Summary changed from '' to 'Set static routes'
- Description changed from '' to 'Define or overwrite the static routes for the router.'

GET /api/openstack-security-groups/

- Summary changed from '' to 'List security groups'
- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get a list of security groups.'

HEAD /api/openstack-security-groups/

- Summary changed from '' to 'List security groups'

DELETE /api/openstack-security-groups/{uuid}/

- Summary changed from '' to 'Delete security group'
- Description changed from '' to 'Delete a security group.'

GET /api/openstack-security-groups/{uuid}/

- Summary changed from '' to 'Get security group details'
- Description changed from '' to 'Retrieve details of a specific security group.'

PATCH /api/openstack-security-groups/{uuid}/

- Summary changed from '' to 'Partially update security group'
- Description changed from '' to 'Update specific fields of a security group.'

POST /api/openstack-security-groups/{uuid}/pull/

- Summary changed from '' to 'Synchronize resource state'
- Description changed from '' to 'Schedule an asynchronous pull operation to synchronize resource state from the backend. Returns 202 if the pull was scheduled successfully, or 409 if the pull operation is not implemented for this resource type.'
- Responses changed
  - New response: 202
  - New response: 409
  - Deleted response: 200

POST /api/openstack-security-groups/{uuid}/set_rules/

- Summary changed from '' to 'Set security group rules'
- Description changed from 'Update security group rules' to 'Update the rules for a specific security group. This overwrites all existing rules.'

POST /api/openstack-security-groups/{uuid}/unlink/

- Summary changed from '' to 'Unlink resource'
- Description changed from 'Delete resource from the database without scheduling operations on backend
and without checking current state of the resource. It is intended to be used
for removing resource stuck in transitioning state.' to 'Delete resource from the database without scheduling operations on backend
        and without checking current state of the resource. It is intended to be used
        for removing resource stuck in transitioning state.'
- Responses changed
  - New response: 204
  - Deleted response: 200

GET /api/openstack-server-groups/

- Summary changed from '' to 'List server groups'
- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get a list of server groups.'

HEAD /api/openstack-server-groups/

- Summary changed from '' to 'List server groups'

DELETE /api/openstack-server-groups/{uuid}/

- Summary changed from '' to 'Delete server group'
- Description changed from '' to 'Delete a server group.'

GET /api/openstack-server-groups/{uuid}/

- Summary changed from '' to 'Get server group details'
- Description changed from '' to 'Retrieve details of a specific server group.'

POST /api/openstack-server-groups/{uuid}/pull/

- Summary changed from '' to 'Synchronize resource state'
- Description changed from '' to 'Schedule an asynchronous pull operation to synchronize resource state from the backend. Returns 202 if the pull was scheduled successfully, or 409 if the pull operation is not implemented for this resource type.'
- Responses changed
  - New response: 202
  - New response: 409
  - Deleted response: 200

POST /api/openstack-server-groups/{uuid}/unlink/

- Summary changed from '' to 'Unlink resource'
- Description changed from 'Delete resource from the database without scheduling operations on backend
and without checking current state of the resource. It is intended to be used
for removing resource stuck in transitioning state.' to 'Delete resource from the database without scheduling operations on backend
        and without checking current state of the resource. It is intended to be used
        for removing resource stuck in transitioning state.'
- Responses changed
  - New response: 204
  - Deleted response: 200

GET /api/openstack-snapshots/

- Summary changed from '' to 'List snapshots'
- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get a list of snapshots.'

HEAD /api/openstack-snapshots/

- Summary changed from '' to 'List snapshots'

DELETE /api/openstack-snapshots/{uuid}/

- Summary changed from '' to 'Delete snapshot'
- Description changed from '' to 'Delete a snapshot.'

GET /api/openstack-snapshots/{uuid}/

- Summary changed from '' to 'Get snapshot details'
- Description changed from '' to 'Retrieve details of a specific snapshot.'

PATCH /api/openstack-snapshots/{uuid}/

- Summary changed from '' to 'Partially update snapshot'
- Description changed from '' to 'Update specific fields of a snapshot.'

PUT /api/openstack-snapshots/{uuid}/

- Summary changed from '' to 'Update snapshot'
- Description changed from '' to 'Update an existing snapshot.'

POST /api/openstack-snapshots/{uuid}/pull/

- Summary changed from '' to 'Synchronize resource state'
- Description changed from '' to 'Schedule an asynchronous pull operation to synchronize resource state from the backend. Returns 202 if the pull was scheduled successfully, or 409 if the pull operation is not implemented for this resource type.'
- Responses changed
  - New response: 202
  - New response: 409
  - Deleted response: 200

GET /api/openstack-snapshots/{uuid}/restorations/

- Summary changed from '' to 'List snapshot restorations'

POST /api/openstack-snapshots/{uuid}/restore/

- Summary changed from '' to 'Restore volume from snapshot'

POST /api/openstack-snapshots/{uuid}/unlink/

- Summary changed from '' to 'Unlink resource'
- Description changed from 'Delete resource from the database without scheduling operations on backend
and without checking current state of the resource. It is intended to be used
for removing resource stuck in transitioning state.' to 'Delete resource from the database without scheduling operations on backend
        and without checking current state of the resource. It is intended to be used
        for removing resource stuck in transitioning state.'
- Responses changed
  - New response: 204
  - Deleted response: 200

GET /api/openstack-subnets/

- Summary changed from '' to 'List subnets'
- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get a list of subnets.'

HEAD /api/openstack-subnets/

- Summary changed from '' to 'List subnets'

DELETE /api/openstack-subnets/{uuid}/

- Summary changed from '' to 'Delete subnet'
- Description changed from '' to 'Delete a subnet.'

GET /api/openstack-subnets/{uuid}/

- Summary changed from '' to 'Get subnet details'
- Description changed from '' to 'Retrieve details of a specific subnet.'

PATCH /api/openstack-subnets/{uuid}/

- Summary changed from '' to 'Partially update subnet'
- Description changed from '' to 'Update specific fields of a subnet.'

PUT /api/openstack-subnets/{uuid}/

- Summary changed from '' to 'Update subnet'
- Description changed from '' to 'Update an existing subnet.'

POST /api/openstack-subnets/{uuid}/connect/

- Summary changed from '' to 'Connect subnet to router'
- Description changed from '' to 'Connect the subnet to the default tenant router.'

POST /api/openstack-subnets/{uuid}/disconnect/

- Summary changed from '' to 'Disconnect subnet from router'
- Description changed from '' to 'Disconnect the subnet from the default tenant router.'

POST /api/openstack-subnets/{uuid}/pull/

- Summary changed from '' to 'Synchronize resource state'
- Description changed from '' to 'Schedule an asynchronous pull operation to synchronize resource state from the backend. Returns 202 if the pull was scheduled successfully, or 409 if the pull operation is not implemented for this resource type.'
- Responses changed
  - New response: 202
  - New response: 409
  - Deleted response: 200

POST /api/openstack-subnets/{uuid}/unlink/

- Summary changed from '' to 'Unlink resource'
- Description changed from 'Delete resource from the database without scheduling operations on backend
and without checking current state of the resource. It is intended to be used
for removing resource stuck in transitioning state.' to 'Delete resource from the database without scheduling operations on backend
        and without checking current state of the resource. It is intended to be used
        for removing resource stuck in transitioning state.'
- Responses changed
  - New response: 204
  - Deleted response: 200

GET /api/openstack-tenants/

- Summary changed from '' to 'List tenants'
- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get a list of OpenStack tenants.'
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [security_groups]

HEAD /api/openstack-tenants/

- Summary changed from '' to 'List tenants'

POST /api/openstack-tenants/

- Summary changed from '' to 'Create tenant'
- Description changed from '' to 'Create a new OpenStack tenant.'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: security_groups

DELETE /api/openstack-tenants/{uuid}/

- Summary changed from '' to 'Delete tenant'
- Description changed from '' to 'Delete an OpenStack tenant and all its resources.'

GET /api/openstack-tenants/{uuid}/

- Summary changed from '' to 'Get tenant details'
- Description changed from '' to 'Retrieve details of a specific OpenStack tenant.'
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [security_groups]

PATCH /api/openstack-tenants/{uuid}/

- Summary changed from '' to 'Partially update tenant'
- Description changed from '' to 'Update specific fields of an OpenStack tenant.'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: security_groups

PUT /api/openstack-tenants/{uuid}/

- Summary changed from '' to 'Update tenant'
- Description changed from '' to 'Update an existing OpenStack tenant.'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: security_groups

GET /api/openstack-tenants/{uuid}/backend_instances/

- Summary changed from '' to 'List backend instances'

GET /api/openstack-tenants/{uuid}/backend_volumes/

- Summary changed from '' to 'List backend volumes'

POST /api/openstack-tenants/{uuid}/change_password/

- Summary changed from '' to 'Change tenant user password'

POST /api/openstack-tenants/{uuid}/create_floating_ip/

- Summary changed from '' to 'Create floating IP for tenant'

POST /api/openstack-tenants/{uuid}/create_network/

- Summary changed from '' to 'Create network for tenant'

POST /api/openstack-tenants/{uuid}/create_security_group/

- Summary changed from '' to 'Create security group'
- Description changed from '' to 'Create a security group for the tenant.'

POST /api/openstack-tenants/{uuid}/create_server_group/

- Summary changed from '' to 'Create server group'
- Description changed from '' to 'Create a new server group for the tenant.'

POST /api/openstack-tenants/{uuid}/pull/

- Summary changed from '' to 'Synchronize resource state'
- Description changed from '' to 'Schedule an asynchronous pull operation to synchronize resource state from the backend. Returns 202 if the pull was scheduled successfully, or 409 if the pull operation is not implemented for this resource type.'
- Responses changed
  - New response: 202
  - New response: 409
  - Deleted response: 200

POST /api/openstack-tenants/{uuid}/pull_floating_ips/

- Summary changed from '' to 'Pull floating IPs'

POST /api/openstack-tenants/{uuid}/pull_quotas/

- Summary changed from '' to 'Pull tenant quotas'

POST /api/openstack-tenants/{uuid}/pull_security_groups/

- Summary changed from '' to 'Pull security groups'

POST /api/openstack-tenants/{uuid}/pull_server_groups/

- Summary changed from '' to 'Pull server groups'

POST /api/openstack-tenants/{uuid}/set_quotas/

- Summary changed from '' to 'Set tenant quotas'
- Description changed from 'A quota can be set for a particular tenant. Only staff users can do that.
In order to set quota submit POST request to /api/openstack-tenants/<uuid>/set_quotas/.
The quota values are propagated to the backend.

The following quotas are supported. All values are expected to be integers:

- instances - maximal number of created instances.
- ram - maximal size of ram for allocation. In MiB_.
- storage - maximal size of storage for allocation. In MiB_.
- vcpu - maximal number of virtual cores for allocation.
- security_group_count - maximal number of created security groups.
- security_group_rule_count - maximal number of created security groups rules.
- volumes - maximal number of created volumes.
- snapshots - maximal number of created snapshots.

It is possible to update quotas by one or by submitting all the fields in one request.
Waldur will attempt to update the provided quotas. Please note, that if provided quotas are
conflicting with the backend (e.g. requested number of instances is below of the already existing ones),
some quotas might not be applied.

.. _MiB: <http://en.wikipedia.org/wiki/Mebibyte>

Response code of a successful request is **202 ACCEPTED**.
In case tenant is in a non-stable status, the response would be **409 CONFLICT**.
In this case REST client is advised to repeat the request after some time.
On successful completion the task will synchronize quotas with the backend.' to 'A quota can be set for a particular tenant. Only staff users can do that.
In order to set quota submit POST request to /api/openstack-tenants/<uuid>/set_quotas/.
The quota values are propagated to the backend.

The following quotas are supported. All values are expected to be integers:

- instances - maximal number of created instances.
- ram - maximal size of ram for allocation. In MiB_.
- storage - maximal size of storage for allocation. In MiB_.
- vcpu - maximal number of virtual cores for allocation.
- security_group_count - maximal number of created security groups.
- security_group_rule_count - maximal number of created security groups rules.
- volumes - maximal number of created volumes.
- snapshots - maximal number of created snapshots.

It is possible to update quotas by one or by submitting all the fields in one request.
Waldur will attempt to update the provided quotas. Please note, that if provided quotas are
conflicting with the backend (e.g. requested number of instances is below of the already existing ones),
some quotas might not be applied.

.. _MiB: <http://en.wikipedia.org/wiki/Mebibyte>

Response code of a successful request is **202 ACCEPTED**.
In case tenant is in a non-stable status, the response would be **409 CONFLICT**.
In this case REST client is advised to repeat the request after some time.
On successful completion the task will synchronize quotas with the backend.
'

POST /api/openstack-tenants/{uuid}/unlink/

- Summary changed from '' to 'Unlink resource'
- Description changed from 'Delete resource from the database without scheduling operations on backend
and without checking current state of the resource. It is intended to be used
for removing resource stuck in transitioning state.' to 'Delete resource from the database without scheduling operations on backend
        and without checking current state of the resource. It is intended to be used
        for removing resource stuck in transitioning state.'
- Responses changed
  - New response: 204
  - Deleted response: 200

GET /api/openstack-volume-availability-zones/

- Summary changed from '' to 'List volume availability zones'
- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get a list of volume availability zones.'

HEAD /api/openstack-volume-availability-zones/

- Summary changed from '' to 'List volume availability zones'

GET /api/openstack-volume-availability-zones/{uuid}/

- Summary changed from '' to 'Get volume availability zone details'
- Description changed from '' to 'Retrieve details of a specific volume availability zone.'

GET /api/openstack-volume-types/

- Summary changed from '' to 'List volume types'
- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get a list of available volume types.'

HEAD /api/openstack-volume-types/

- Summary changed from '' to 'List volume types'

GET /api/openstack-volume-types/names/

- Summary changed from '' to 'List unique volume type names'

HEAD /api/openstack-volume-types/names/

- Summary changed from '' to 'List unique volume type names'

GET /api/openstack-volume-types/{uuid}/

- Summary changed from '' to 'Get volume type details'
- Description changed from '' to 'Retrieve details of a specific volume type.'

GET /api/openstack-volumes/

- Summary changed from '' to 'List volumes'
- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get a list of volumes.'

HEAD /api/openstack-volumes/

- Summary changed from '' to 'List volumes'

GET /api/openstack-volumes/{uuid}/

- Summary changed from '' to 'Get volume details'
- Description changed from '' to 'Retrieve details of a specific volume.'

PATCH /api/openstack-volumes/{uuid}/

- Summary changed from '' to 'Partially update volume'
- Description changed from '' to 'Update specific fields of a volume.'

PUT /api/openstack-volumes/{uuid}/

- Summary changed from '' to 'Update volume'
- Description changed from '' to 'Update an existing volume.'

POST /api/openstack-volumes/{uuid}/attach/

- Summary changed from '' to 'Attach volume to instance'

POST /api/openstack-volumes/{uuid}/detach/

- Summary changed from '' to 'Detach volume from instance'

POST /api/openstack-volumes/{uuid}/extend/

- Summary changed from '' to 'Extend volume size'

POST /api/openstack-volumes/{uuid}/pull/

- Summary changed from '' to 'Synchronize resource state'
- Description changed from '' to 'Schedule an asynchronous pull operation to synchronize resource state from the backend. Returns 202 if the pull was scheduled successfully, or 409 if the pull operation is not implemented for this resource type.'
- Responses changed
  - New response: 202
  - New response: 409
  - Deleted response: 200

POST /api/openstack-volumes/{uuid}/retype/

- Summary changed from '' to 'Change volume type'

POST /api/openstack-volumes/{uuid}/snapshot/

- Summary changed from '' to 'Create volume snapshot'

POST /api/openstack-volumes/{uuid}/unlink/

- Summary changed from '' to 'Unlink resource'
- Description changed from 'Delete resource from the database without scheduling operations on backend
and without checking current state of the resource. It is intended to be used
for removing resource stuck in transitioning state.' to 'Delete resource from the database without scheduling operations on backend
        and without checking current state of the resource. It is intended to be used
        for removing resource stuck in transitioning state.'
- Responses changed
  - New response: 204
  - Deleted response: 200

GET /api/organization-groups/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/override-settings/

- Summary changed from '' to 'Get all overridable settings'
- Description changed from '' to 'Returns all settings that can be overridden in the database via the Constance backend. Requires admin permissions.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: LLM_CHAT_ENABLED
            - New property: LLM_INFERENCES_API_TOKEN
            - New property: LLM_INFERENCES_API_URL
            - New property: LLM_INFERENCES_BACKEND_TYPE
            - New property: LLM_INFERENCES_MODEL
            - New property: ONBOARDING_BOLAGSVERKET_API_URL
            - New property: ONBOARDING_BOLAGSVERKET_CLIENT_ID
            - New property: ONBOARDING_BOLAGSVERKET_CLIENT_SECRET
            - New property: ONBOARDING_BOLAGSVERKET_TOKEN_API_URL
            - New property: ONBOARDING_COUNTRY

POST /api/override-settings/

- Summary changed from '' to 'Update overridable settings'
- Description changed from '' to 'Updates one or more settings in the database via the Constance backend. Requires admin permissions.'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: LLM_CHAT_ENABLED
          - New property: LLM_INFERENCES_API_TOKEN
          - New property: LLM_INFERENCES_API_URL
          - New property: LLM_INFERENCES_BACKEND_TYPE
          - New property: LLM_INFERENCES_MODEL
          - New property: ONBOARDING_BOLAGSVERKET_API_URL
          - New property: ONBOARDING_BOLAGSVERKET_CLIENT_ID
          - New property: ONBOARDING_BOLAGSVERKET_CLIENT_SECRET
          - New property: ONBOARDING_BOLAGSVERKET_TOKEN_API_URL
          - New property: ONBOARDING_COUNTRY
      - Examples changed
        - New example: EnableMarketplaceAndSetACustomTitle
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: LLM_CHAT_ENABLED
          - New property: LLM_INFERENCES_API_TOKEN
          - New property: LLM_INFERENCES_API_URL
          - New property: LLM_INFERENCES_BACKEND_TYPE
          - New property: LLM_INFERENCES_MODEL
          - New property: ONBOARDING_BOLAGSVERKET_API_URL
          - New property: ONBOARDING_BOLAGSVERKET_CLIENT_ID
          - New property: ONBOARDING_BOLAGSVERKET_CLIENT_SECRET
          - New property: ONBOARDING_BOLAGSVERKET_TOKEN_API_URL
          - New property: ONBOARDING_COUNTRY
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: LLM_CHAT_ENABLED
          - New property: LLM_INFERENCES_API_TOKEN
          - New property: LLM_INFERENCES_API_URL
          - New property: LLM_INFERENCES_BACKEND_TYPE
          - New property: LLM_INFERENCES_MODEL
          - New property: ONBOARDING_BOLAGSVERKET_API_URL
          - New property: ONBOARDING_BOLAGSVERKET_CLIENT_ID
          - New property: ONBOARDING_BOLAGSVERKET_CLIENT_SECRET
          - New property: ONBOARDING_BOLAGSVERKET_TOKEN_API_URL
          - New property: ONBOARDING_COUNTRY

GET /api/payment-profiles/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/payments/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/project-credits/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/project-permissions-reviews/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

POST /api/project-permissions-reviews/{uuid}/close/

- Summary changed from '' to 'Close project permission review'

GET /api/project-types/

- Summary changed from '' to 'List project types'
- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Retrieve a list of available project types.'

HEAD /api/project-types/

- Summary changed from '' to 'List project types'

GET /api/project-types/{uuid}/

- Summary changed from '' to 'Retrieve project type details'
- Description changed from '' to 'Fetch details of a specific project type by its UUID.'

GET /api/projects/

- Summary changed from '' to 'List projects'
- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Retrieve a list of projects. The list is filtered based on the user's permissions. By default, only active projects are shown.'
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [grace_period_days]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: grace_period_days

HEAD /api/projects/

- Summary changed from '' to 'List projects'

POST /api/projects/

- Summary changed from '' to 'Create a new project'
- Description changed from 'A new project can be created by users with staff privilege (is_staff=True) or customer owners.
Project resource quota is optional.' to 'A new project can be created by users with staff privilege (is_staff=True) or customer owners. Project resource quota is optional.'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: grace_period_days
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: grace_period_days
    - Modified media type: multipart/form-data
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

GET /api/projects/checklist-template/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: initial_visible_questions
              - Items changed
                - Properties changed
                  - New property: allowed_file_types
                  - New property: allowed_mime_types
                  - New property: always_requires_review
                  - New property: always_show_guidance
                  - New property: dependency_logic_operator
                  - New property: guidance_answer_value
                  - New property: guidance_operator
                  - New property: max_file_size_mb
                  - New property: max_files_count
                  - New property: max_value
                  - New property: min_value
                  - New property: operator
                  - New property: order
                  - New property: question_type
                  - New property: review_answer_value
            - Modified property: questions
              - Items changed
                - Properties changed
                  - New property: allowed_file_types
                  - New property: allowed_mime_types
                  - New property: always_requires_review
                  - New property: always_show_guidance
                  - New property: dependency_logic_operator
                  - New property: guidance_answer_value
                  - New property: guidance_operator
                  - New property: max_file_size_mb
                  - New property: max_files_count
                  - New property: max_value
                  - New property: min_value
                  - New property: operator
                  - New property: order
                  - New property: question_type
                  - New property: review_answer_value

DELETE /api/projects/{uuid}/

- Summary changed from '' to 'Delete a project'
- Description changed from 'If a project has connected instances, deletion request will fail with 409 response code.' to 'Delete a project. If the project has any active resources, the deletion request will fail with a 409 Conflict response. This action performs a soft-delete, and the project can be recovered later.'

GET /api/projects/{uuid}/

- Summary changed from '' to 'Retrieve project details'
- Description changed from '' to 'Fetch the details of a specific project by its UUID. Users can access details of terminated projects they previously had access to.'
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [grace_period_days]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: grace_period_days

PATCH /api/projects/{uuid}/

- Summary changed from '' to 'Partially update project details'
- Description changed from '' to 'Partially update the details of a project. Requires project administrator or customer owner permissions.'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: grace_period_days
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: grace_period_days
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: grace_period_days
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: grace_period_days

PUT /api/projects/{uuid}/

- Summary changed from '' to 'Update project details'
- Description changed from '' to 'Update the details of a project. Requires project administrator or customer owner permissions.'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: grace_period_days
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: grace_period_days
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: grace_period_days
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: grace_period_days

POST /api/projects/{uuid}/add_user/

- Summary changed from '' to 'Grant a role to a user'
- Description changed from '' to 'Assigns a specific role to a user within the current scope. An optional expiration time for the role can be set.'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Examples changed
        - New example: GrantProjectAdminRoleUntilEndOfYear
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Examples changed
          - New example: SuccessfulRoleGrantResponse
  - Modified response: 400
    - Description changed from '' to 'Validation error, for example when trying to add a user to a terminated project.'
    - Content changed
      - Deleted media type: application/json

GET /api/projects/{uuid}/checklist/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: questions
              - Items changed
                - Required changed
                  - New required property: allowed_file_types
                  - New required property: allowed_mime_types
                  - New required property: max_file_size_mb
                  - New required property: max_files_count
                - Properties changed
                  - New property: allowed_file_types
                  - New property: allowed_mime_types
                  - New property: max_file_size_mb
                  - New property: max_files_count
                  - Modified property: question_type
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/QuestionTypeEnum
                        - New enum values: [multiple_files]

POST /api/projects/{uuid}/delete_user/

- Summary changed from '' to 'Revoke a role from a user'
- Description changed from '' to 'Removes a specific role from a user within the current scope. This effectively revokes their permissions associated with that role.'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Examples changed
        - New example: RevokeProjectAdminRoleFromUser
- Responses changed
  - Modified response: 200
    - Description changed from 'No response body' to 'Role revoked successfully.'

GET /api/projects/{uuid}/list_users/

- Summary changed from '' to 'List users and their roles in a scope'
- Description changed from '' to 'Retrieves a list of users who have a role within a specific scope (e.g., a project or an organization). The list can be filtered by user details or role.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Examples changed
          - New example: ExampleUserRoleListResponse

POST /api/projects/{uuid}/move_project/

- Summary changed from '' to 'Move project to another customer'
- Description changed from '' to 'Moves a project and its associated resources to a different customer. This is a staff-only action. You can choose whether to preserve existing project permissions for users.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: grace_period_days

POST /api/projects/{uuid}/recover/

- Summary changed from '' to 'Recover a soft-deleted project'
- Description changed from 'Recover a soft-deleted project with team member restoration' to 'Recovers a soft-deleted (terminated) project, making it active again. Provides options to restore previous team members automatically (staff-only) or send them new invitations.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: grace_period_days

GET /api/projects/{uuid}/stats/

- Summary changed from '' to 'Get project resource usage statistics'
- Description changed from 'Return statistics about project resources usage' to 'Provides statistics about the resource usage (e.g., CPU, RAM, storage) for all resources within a project. Can be filtered to show usage for the current month only.'
- Modified query param: for_current_month
  - Description changed from '' to 'If true, returns usage data for the current month only. Otherwise, returns total usage.'

POST /api/projects/{uuid}/update_user/

- Summary changed from '' to 'Update a user's role expiration'
- Description changed from '' to 'Updates the expiration time for a user's existing role in the current scope. This is useful for extending or shortening the duration of a permission. To make a role permanent, set expiration_time to null.'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Examples changed
        - New example: ExtendRoleUntilMid-2025
        - New example: MakeARolePermanent
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Examples changed
          - New example: SuccessfulRoleUpdateResponse

GET /api/promotions-campaigns/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/promotions-campaigns/{uuid}/orders/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [slug]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: slug

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
                      - New property: slug
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: slug

GET /api/proposal-proposals/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/proposal-proposals/checklist-template/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: initial_visible_questions
              - Items changed
                - Properties changed
                  - New property: allowed_file_types
                  - New property: allowed_mime_types
                  - New property: always_requires_review
                  - New property: always_show_guidance
                  - New property: dependency_logic_operator
                  - New property: guidance_answer_value
                  - New property: guidance_operator
                  - New property: max_file_size_mb
                  - New property: max_files_count
                  - New property: max_value
                  - New property: min_value
                  - New property: operator
                  - New property: order
                  - New property: question_type
                  - New property: review_answer_value
            - Modified property: questions
              - Items changed
                - Properties changed
                  - New property: allowed_file_types
                  - New property: allowed_mime_types
                  - New property: always_requires_review
                  - New property: always_show_guidance
                  - New property: dependency_logic_operator
                  - New property: guidance_answer_value
                  - New property: guidance_operator
                  - New property: max_file_size_mb
                  - New property: max_files_count
                  - New property: max_value
                  - New property: min_value
                  - New property: operator
                  - New property: order
                  - New property: question_type
                  - New property: review_answer_value

POST /api/proposal-proposals/{uuid}/add_user/

- Summary changed from '' to 'Grant a role to a user'
- Description changed from '' to 'Assigns a specific role to a user within the current scope. An optional expiration time for the role can be set.'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Examples changed
        - New example: GrantProjectAdminRoleUntilEndOfYear
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Examples changed
          - New example: SuccessfulRoleGrantResponse
  - Modified response: 400
    - Description changed from '' to 'Validation error, for example when trying to add a user to a terminated project.'
    - Content changed
      - Deleted media type: application/json

GET /api/proposal-proposals/{uuid}/checklist/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: questions
              - Items changed
                - Required changed
                  - New required property: allowed_file_types
                  - New required property: allowed_mime_types
                  - New required property: max_file_size_mb
                  - New required property: max_files_count
                - Properties changed
                  - New property: allowed_file_types
                  - New property: allowed_mime_types
                  - New property: max_file_size_mb
                  - New property: max_files_count
                  - Modified property: question_type
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/QuestionTypeEnum
                        - New enum values: [multiple_files]

GET /api/proposal-proposals/{uuid}/checklist_review/

- Extensions changed
  - Deleted extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: questions
              - Items changed
                - Required changed
                  - New required property: allowed_file_types
                  - New required property: allowed_mime_types
                  - New required property: max_file_size_mb
                  - New required property: max_files_count
                - Properties changed
                  - New property: allowed_file_types
                  - New property: allowed_mime_types
                  - New property: max_file_size_mb
                  - New property: max_files_count
                  - Modified property: question_type
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/QuestionTypeEnum
                        - New enum values: [multiple_files]

GET /api/proposal-proposals/{uuid}/completion_review_status/

- Extensions changed
  - Deleted extension: x-permissions

POST /api/proposal-proposals/{uuid}/delete_user/

- Summary changed from '' to 'Revoke a role from a user'
- Description changed from '' to 'Removes a specific role from a user within the current scope. This effectively revokes their permissions associated with that role.'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Examples changed
        - New example: RevokeProjectAdminRoleFromUser
- Responses changed
  - Modified response: 200
    - Description changed from 'No response body' to 'Role revoked successfully.'

GET /api/proposal-proposals/{uuid}/list_users/

- Summary changed from '' to 'List users and their roles in a scope'
- Description changed from '' to 'Retrieves a list of users who have a role within a specific scope (e.g., a project or an organization). The list can be filtered by user details or role.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Examples changed
          - New example: ExampleUserRoleListResponse

POST /api/proposal-proposals/{uuid}/update_user/

- Summary changed from '' to 'Update a user's role expiration'
- Description changed from '' to 'Updates the expiration time for a user's existing role in the current scope. This is useful for extending or shortening the duration of a permission. To make a role permanent, set expiration_time to null.'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Examples changed
        - New example: ExtendRoleUntilMid-2025
        - New example: MakeARolePermanent
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Examples changed
          - New example: SuccessfulRoleUpdateResponse

GET /api/proposal-protected-calls/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

POST /api/proposal-protected-calls/{uuid}/add_user/

- Summary changed from '' to 'Grant a role to a user'
- Description changed from '' to 'Assigns a specific role to a user within the current scope. An optional expiration time for the role can be set.'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Examples changed
        - New example: GrantProjectAdminRoleUntilEndOfYear
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Examples changed
          - New example: SuccessfulRoleGrantResponse
  - Modified response: 400
    - Description changed from '' to 'Validation error, for example when trying to add a user to a terminated project.'
    - Content changed
      - Deleted media type: application/json

POST /api/proposal-protected-calls/{uuid}/delete_user/

- Summary changed from '' to 'Revoke a role from a user'
- Description changed from '' to 'Removes a specific role from a user within the current scope. This effectively revokes their permissions associated with that role.'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Examples changed
        - New example: RevokeProjectAdminRoleFromUser
- Responses changed
  - Modified response: 200
    - Description changed from 'No response body' to 'Role revoked successfully.'

GET /api/proposal-protected-calls/{uuid}/list_users/

- Summary changed from '' to 'List users and their roles in a scope'
- Description changed from '' to 'Retrieves a list of users who have a role within a specific scope (e.g., a project or an organization). The list can be filtered by user details or role.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Examples changed
          - New example: ExampleUserRoleListResponse

POST /api/proposal-protected-calls/{uuid}/update_user/

- Summary changed from '' to 'Update a user's role expiration'
- Description changed from '' to 'Updates the expiration time for a user's existing role in the current scope. This is useful for extending or shortening the duration of a permission. To make a role permanent, set expiration_time to null.'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Examples changed
        - New example: ExtendRoleUntilMid-2025
        - New example: MakeARolePermanent
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Examples changed
          - New example: SuccessfulRoleUpdateResponse

GET /api/proposal-public-calls/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/proposal-requested-offerings/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/proposal-requested-resources/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/proposal-reviews/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/provider-invoice-items/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/public-maintenance-announcements/

- Summary changed from '' to 'List public maintenance announcements'
- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Returns a paginated list of public maintenance announcements. Only announcements that are 'Scheduled', 'In progress', or 'Completed' are visible. This endpoint is accessible to unauthenticated users.'

HEAD /api/public-maintenance-announcements/

- Summary changed from '' to 'List public maintenance announcements'

GET /api/public-maintenance-announcements/{uuid}/

- Summary changed from '' to 'Retrieve a public maintenance announcement'
- Description changed from '' to 'Returns the details of a specific public maintenance announcement.'

POST /api/query/

- Summary changed from '' to 'Execute read-only SQL query'
- Description changed from 'Execute SQL query against readonly database' to 'Execute a given SQL query against a read-only database replica. This is a powerful tool for diagnostics and reporting, but should be used with caution. Requires support user permissions.'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Examples changed
        - New example: ListAllCustomers
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Examples changed
          - New example: SuccessfulResponse

GET /api/rancher-apps/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

POST /api/rancher-apps/{uuid}/pull/

- Summary changed from '' to 'Synchronize resource state'
- Description changed from '' to 'Schedule an asynchronous pull operation to synchronize resource state from the backend. Returns 202 if the pull was scheduled successfully, or 409 if the pull operation is not implemented for this resource type.'
- Responses changed
  - New response: 202
  - New response: 409
  - Deleted response: 200

POST /api/rancher-apps/{uuid}/unlink/

- Summary changed from '' to 'Unlink resource'
- Description changed from 'Delete resource from the database without scheduling operations on backend
and without checking current state of the resource. It is intended to be used
for removing resource stuck in transitioning state.' to 'Delete resource from the database without scheduling operations on backend
        and without checking current state of the resource. It is intended to be used
        for removing resource stuck in transitioning state.'
- Responses changed
  - New response: 204
  - Deleted response: 200

GET /api/rancher-catalogs/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/rancher-cluster-security-groups/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/rancher-cluster-templates/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/rancher-clusters/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

POST /api/rancher-clusters/{uuid}/pull/

- Summary changed from '' to 'Synchronize resource state'
- Description changed from '' to 'Schedule an asynchronous pull operation to synchronize resource state from the backend. Returns 202 if the pull was scheduled successfully, or 409 if the pull operation is not implemented for this resource type.'
- Responses changed
  - New response: 202
  - New response: 409
  - Deleted response: 200

POST /api/rancher-clusters/{uuid}/unlink/

- Summary changed from '' to 'Unlink resource'
- Description changed from 'Delete resource from the database without scheduling operations on backend
and without checking current state of the resource. It is intended to be used
for removing resource stuck in transitioning state.' to 'Delete resource from the database without scheduling operations on backend
        and without checking current state of the resource. It is intended to be used
        for removing resource stuck in transitioning state.'
- Responses changed
  - New response: 204
  - Deleted response: 200

GET /api/rancher-hpas/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

POST /api/rancher-hpas/{uuid}/pull/

- Summary changed from '' to 'Synchronize resource state'
- Description changed from '' to 'Schedule an asynchronous pull operation to synchronize resource state from the backend. Returns 202 if the pull was scheduled successfully, or 409 if the pull operation is not implemented for this resource type.'
- Responses changed
  - New response: 202
  - New response: 409
  - Deleted response: 200

POST /api/rancher-hpas/{uuid}/unlink/

- Summary changed from '' to 'Unlink resource'
- Description changed from 'Delete resource from the database without scheduling operations on backend
and without checking current state of the resource. It is intended to be used
for removing resource stuck in transitioning state.' to 'Delete resource from the database without scheduling operations on backend
        and without checking current state of the resource. It is intended to be used
        for removing resource stuck in transitioning state.'
- Responses changed
  - New response: 204
  - Deleted response: 200

GET /api/rancher-ingresses/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

POST /api/rancher-ingresses/{uuid}/pull/

- Summary changed from '' to 'Synchronize resource state'
- Description changed from '' to 'Schedule an asynchronous pull operation to synchronize resource state from the backend. Returns 202 if the pull was scheduled successfully, or 409 if the pull operation is not implemented for this resource type.'
- Responses changed
  - New response: 202
  - New response: 409
  - Deleted response: 200

POST /api/rancher-ingresses/{uuid}/unlink/

- Summary changed from '' to 'Unlink resource'
- Description changed from 'Delete resource from the database without scheduling operations on backend
and without checking current state of the resource. It is intended to be used
for removing resource stuck in transitioning state.' to 'Delete resource from the database without scheduling operations on backend
        and without checking current state of the resource. It is intended to be used
        for removing resource stuck in transitioning state.'
- Responses changed
  - New response: 204
  - Deleted response: 200

GET /api/rancher-namespaces/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/rancher-nodes/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

POST /api/rancher-nodes/{uuid}/pull/

- Summary changed from '' to 'Synchronize resource state'
- Description changed from '' to 'Schedule an asynchronous pull operation to synchronize resource state from the backend. Returns 202 if the pull was scheduled successfully, or 409 if the pull operation is not implemented for this resource type.'
- Responses changed
  - New response: 202
  - New response: 409
  - Deleted response: 200

POST /api/rancher-nodes/{uuid}/unlink/

- Summary changed from '' to 'Unlink resource'
- Description changed from 'Delete resource from the database without scheduling operations on backend
and without checking current state of the resource. It is intended to be used
for removing resource stuck in transitioning state.' to 'Delete resource from the database without scheduling operations on backend
        and without checking current state of the resource. It is intended to be used
        for removing resource stuck in transitioning state.'
- Responses changed
  - New response: 204
  - Deleted response: 200

GET /api/rancher-projects/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/rancher-role-templates/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/rancher-services/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

POST /api/rancher-services/{uuid}/pull/

- Summary changed from '' to 'Synchronize resource state'
- Description changed from '' to 'Schedule an asynchronous pull operation to synchronize resource state from the backend. Returns 202 if the pull was scheduled successfully, or 409 if the pull operation is not implemented for this resource type.'
- Responses changed
  - New response: 202
  - New response: 409
  - Deleted response: 200

POST /api/rancher-services/{uuid}/unlink/

- Summary changed from '' to 'Unlink resource'
- Description changed from 'Delete resource from the database without scheduling operations on backend
and without checking current state of the resource. It is intended to be used
for removing resource stuck in transitioning state.' to 'Delete resource from the database without scheduling operations on backend
        and without checking current state of the resource. It is intended to be used
        for removing resource stuck in transitioning state.'
- Responses changed
  - New response: 204
  - Deleted response: 200

GET /api/rancher-templates/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/rancher-users/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/rancher-workloads/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/roles/

- Summary changed from '' to 'List roles'
- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get a list of all available roles.'

HEAD /api/roles/

- Summary changed from '' to 'List roles'

POST /api/roles/

- Summary changed from '' to 'Create a new role'
- Description changed from '' to 'Allows staff users to create a new custom role with a specific set of permissions.'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Examples changed
        - New example: CreateAProject-levelReviewerRole
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Examples changed
          - New example: SuccessfulRoleCreationResponse

DELETE /api/roles/{uuid}/

- Summary changed from '' to 'Delete a role'
- Description changed from '' to 'Allows staff users to delete a custom role. System roles and roles that are currently in use cannot be deleted.'

GET /api/roles/{uuid}/

- Summary changed from '' to 'Get role details'
- Description changed from '' to 'Retrieve the details of a specific role by its UUID.'

PUT /api/roles/{uuid}/

- Summary changed from '' to 'Update a role'
- Description changed from '' to 'Allows staff users to update an existing role's name, description, content type, and permissions. The name of a system role cannot be changed.'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Examples changed
        - New example: AddAPermissionToARole
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Examples changed
          - New example: SuccessfulRoleUpdateResponse

POST /api/roles/{uuid}/disable/

- Summary changed from '' to 'Disable a role'
- Description changed from '' to 'Allows staff users to disable a role, preventing it from being assigned further. Existing assignments are not affected.'
- Responses changed
  - Modified response: 200
    - Description changed from 'No response body' to 'Role disabled successfully.'

POST /api/roles/{uuid}/enable/

- Summary changed from '' to 'Enable a role'
- Description changed from '' to 'Allows staff users to enable a role, making it available for assignment.'
- Responses changed
  - Modified response: 200
    - Description changed from 'No response body' to 'Role enabled successfully.'

PUT /api/roles/{uuid}/update_descriptions/

- Summary changed from '' to 'Update role descriptions'
- Description changed from '' to 'Allows staff users to update the multilingual descriptions of a role.'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Examples changed
        - New example: UpdateEnglishAndEstonianDescriptions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Examples changed
          - New example: UpdateEnglishAndEstonianDescriptions

GET /api/service-settings/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/slurm-allocation-user-usage/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/slurm-allocations/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

POST /api/slurm-allocations/{uuid}/pull/

- Summary changed from '' to 'Synchronize resource state'
- Description changed from '' to 'Schedule an asynchronous pull operation to synchronize resource state from the backend. Returns 202 if the pull was scheduled successfully, or 409 if the pull operation is not implemented for this resource type.'
- Responses changed
  - New response: 202
  - New response: 409
  - Deleted response: 200

POST /api/slurm-allocations/{uuid}/unlink/

- Summary changed from '' to 'Unlink resource'
- Description changed from 'Delete resource from the database without scheduling operations on backend
and without checking current state of the resource. It is intended to be used
for removing resource stuck in transitioning state.' to 'Delete resource from the database without scheduling operations on backend
        and without checking current state of the resource. It is intended to be used
        for removing resource stuck in transitioning state.'
- Responses changed
  - New response: 204
  - Deleted response: 200

GET /api/slurm-associations/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/slurm-jobs/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

POST /api/slurm-jobs/{uuid}/pull/

- Summary changed from '' to 'Synchronize resource state'
- Description changed from '' to 'Schedule an asynchronous pull operation to synchronize resource state from the backend. Returns 202 if the pull was scheduled successfully, or 409 if the pull operation is not implemented for this resource type.'
- Responses changed
  - New response: 202
  - New response: 409
  - Deleted response: 200

POST /api/slurm-jobs/{uuid}/unlink/

- Summary changed from '' to 'Unlink resource'
- Description changed from 'Delete resource from the database without scheduling operations on backend
and without checking current state of the resource. It is intended to be used
for removing resource stuck in transitioning state.' to 'Delete resource from the database without scheduling operations on backend
        and without checking current state of the resource. It is intended to be used
        for removing resource stuck in transitioning state.'
- Responses changed
  - New response: 204
  - Deleted response: 200

GET /api/support-attachments/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/support-comments/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/support-feedbacks/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/support-issue-statuses/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/support-issues/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/support-priorities/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/support-templates/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/support-users/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/user-agreements/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/user-group-invitations/

- Summary changed from '' to 'List group invitations'
- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Retrieve a list of group invitations. Unauthenticated users can only see public invitations.'

HEAD /api/user-group-invitations/

- Summary changed from '' to 'List group invitations'

POST /api/user-group-invitations/

- Summary changed from '' to 'Create group invitation'
- Description changed from '' to 'Create a new group invitation, which acts as a template for users to request permissions.'

GET /api/user-group-invitations/{uuid}/

- Summary changed from '' to 'Retrieve group invitation'
- Description changed from '' to 'Retrieve details of a specific group invitation. Unauthenticated users can only see public invitations.'

POST /api/user-group-invitations/{uuid}/cancel/

- Summary changed from '' to 'Cancel a group invitation'
- Description changed from 'Cancel group invitation' to 'Cancels an active group invitation, preventing new permission requests from being created.'

GET /api/user-group-invitations/{uuid}/projects/

- Summary changed from '' to 'List projects for a customer-scoped group invitation'
- Description changed from 'Return projects for group invitation' to 'For a group invitation scoped to a customer, this endpoint lists all projects within that customer.'

POST /api/user-group-invitations/{uuid}/submit_request/

- Summary changed from '' to 'Submit a permission request'
- Description changed from '' to 'Creates a permission request based on a group invitation for the currently authenticated user.'

GET /api/user-invitations/

- Summary changed from '' to 'List user invitations'
- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Retrieve a list of user invitations visible to the current user.'

HEAD /api/user-invitations/

- Summary changed from '' to 'List user invitations'

POST /api/user-invitations/

- Summary changed from '' to 'Create user invitation'
- Description changed from '' to 'Create a new user invitation to grant a role in a specific scope (e.g., organization or project).'

POST /api/user-invitations/approve/

- Summary changed from '' to 'Approve a requested invitation'
- Description changed from 'For user's convenience invitation approval is performed without authentication.
User UUID and invitation UUID is encoded into cryptographically signed token.' to '
        For user's convenience invitation approval is performed without authentication.
        User UUID and invitation UUID is encoded into cryptographically signed token.
        '

POST /api/user-invitations/reject/

- Summary changed from '' to 'Reject a requested invitation'
- Description changed from 'For user's convenience invitation reject action is performed without authentication.
User UUID and invitation UUID is encoded into cryptographically signed token.' to '
        For user's convenience invitation reject action is performed without authentication.
        User UUID and invitation UUID is encoded into cryptographically signed token.
        '

GET /api/user-invitations/{uuid}/

- Summary changed from '' to 'Retrieve user invitation'
- Description changed from '' to 'Retrieve details of a specific user invitation.'

POST /api/user-invitations/{uuid}/accept/

- Summary changed from '' to 'Accept an invitation'
- Description changed from 'Accept invitation for current user.' to 'Accepts an invitation for the currently authenticated user. This grants the user the specified role in the invitation's scope.'

POST /api/user-invitations/{uuid}/cancel/

- Summary changed from '' to 'Cancel an invitation'
- Description changed from '' to 'Cancels a pending or planned (pending_project) invitation.'
- Responses changed
  - Modified response: 200
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

POST /api/user-invitations/{uuid}/check/

- Summary changed from '' to 'Check invitation validity'
- Description changed from '' to 'Checks if an invitation is pending and returns its email and whether a civil number is required for acceptance. This endpoint is public and does not require authentication.'

POST /api/user-invitations/{uuid}/delete/

- Summary changed from '' to 'Delete an invitation (staff only)'
- Description changed from '' to 'Deletes an invitation. This action is restricted to staff users.'

GET /api/user-invitations/{uuid}/details/

- Summary changed from '' to 'Get public invitation details'
- Description changed from '' to 'Retrieves public-facing details of an invitation. This is used to show information to a user before they accept it.'

POST /api/user-invitations/{uuid}/send/

- Summary changed from '' to 'Resend an invitation'
- Description changed from '' to 'Resends an email for a pending, expired, or canceled invitation. If the invitation was expired or canceled, its state is reset to 'pending' and its creation time is updated.'

GET /api/user-permission-requests/

- Summary changed from '' to 'List permission requests'
- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Retrieve a list of permission requests visible to the user.'

HEAD /api/user-permission-requests/

- Summary changed from '' to 'List permission requests'

GET /api/user-permission-requests/{uuid}/

- Summary changed from '' to 'Retrieve permission request'
- Description changed from '' to 'Retrieve details of a specific permission request.'

POST /api/user-permission-requests/{uuid}/approve/

- Summary changed from '' to 'Approve a permission request'
- Description changed from '' to 'Approves a pending permission request, granting the requesting user the permissions defined in the associated group invitation.'
- Responses changed
  - Modified response: 200
    - Description changed from '' to 'No response body'
    - Content changed
      - Deleted media type: application/json

POST /api/user-permission-requests/{uuid}/cancel_request/

- Summary changed from '' to 'Cancel a permission request'
- Description changed from 'Cancel permission request. Users can cancel their own requests, staff can cancel any request.' to 'Cancels a pending or draft permission request. This can be done by the user who created the request or by a staff member.'

POST /api/user-permission-requests/{uuid}/reject/

- Summary changed from '' to 'Reject a permission request'
- Description changed from '' to 'Rejects a pending permission request.'
- Responses changed
  - Modified response: 200
    - Description changed from '' to 'No response body'
    - Content changed
      - Deleted media type: application/json

GET /api/user-permissions/

- Summary changed from '' to 'List user permissions'
- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to 'Get a list of all permissions for the current user. Staff and support users can view all user permissions. The list can be filtered by user, scope, role, etc.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Examples changed
          - New example: ExampleUserPermissionListResponse

HEAD /api/user-permissions/

- Summary changed from '' to 'List user permissions'

GET /api/user-permissions/{uuid}/

- Summary changed from '' to 'Get permission details'
- Description changed from '' to 'Retrieve the details of a specific user permission grant by its UUID.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Examples changed
          - New example: ExampleUserPermissionDetailResponse

GET /api/users/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

POST /api/users/confirm_email/

- Summary changed from '' to 'Confirm email change'

GET /api/users/me/

- Summary changed from '' to 'Get current user details'

HEAD /api/users/me/

- Summary changed from '' to 'Get current user details'

POST /api/users/{uuid}/cancel_change_email/

- Summary changed from '' to 'Cancel email change request'

POST /api/users/{uuid}/change_email/

- Summary changed from '' to 'Request email change'

POST /api/users/{uuid}/change_password/

- Summary changed from '' to 'Change user password'

POST /api/users/{uuid}/pull_remote_user/

- Summary changed from '' to 'Synchronize user details from eduTEAMS'
- Description changed from 'Pulls remote user data from eduTEAMS.' to ''

POST /api/users/{uuid}/refresh_token/

- Summary changed from '' to 'Refresh user auth token'
- Description changed from 'Allows to refresh user auth token.' to ''

GET /api/users/{uuid}/token/

- Summary changed from '' to 'Get user auth token'

GET /api/version/

- Summary changed from '' to 'Get application version'
- Description changed from 'Retrieve current version of the application and the latest available version from GitHub (if available).' to 'Retrieves the current installed version of the application and the latest available version from GitHub (if available). Requires staff or support user permissions.'

GET /api/vmware-clusters/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/vmware-datastores/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/vmware-disks/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

POST /api/vmware-disks/{uuid}/pull/

- Summary changed from '' to 'Synchronize resource state'
- Description changed from '' to 'Schedule an asynchronous pull operation to synchronize resource state from the backend. Returns 202 if the pull was scheduled successfully, or 409 if the pull operation is not implemented for this resource type.'
- Responses changed
  - New response: 202
  - New response: 409
  - Deleted response: 200

POST /api/vmware-disks/{uuid}/unlink/

- Summary changed from '' to 'Unlink resource'
- Description changed from 'Delete resource from the database without scheduling operations on backend
and without checking current state of the resource. It is intended to be used
for removing resource stuck in transitioning state.' to 'Delete resource from the database without scheduling operations on backend
        and without checking current state of the resource. It is intended to be used
        for removing resource stuck in transitioning state.'
- Responses changed
  - New response: 204
  - Deleted response: 200

GET /api/vmware-folders/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/vmware-networks/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/vmware-ports/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

POST /api/vmware-ports/{uuid}/pull/

- Summary changed from '' to 'Synchronize resource state'
- Description changed from '' to 'Schedule an asynchronous pull operation to synchronize resource state from the backend. Returns 202 if the pull was scheduled successfully, or 409 if the pull operation is not implemented for this resource type.'
- Responses changed
  - New response: 202
  - New response: 409
  - Deleted response: 200

POST /api/vmware-ports/{uuid}/unlink/

- Summary changed from '' to 'Unlink resource'
- Description changed from 'Delete resource from the database without scheduling operations on backend
and without checking current state of the resource. It is intended to be used
for removing resource stuck in transitioning state.' to 'Delete resource from the database without scheduling operations on backend
        and without checking current state of the resource. It is intended to be used
        for removing resource stuck in transitioning state.'
- Responses changed
  - New response: 204
  - Deleted response: 200

GET /api/vmware-templates/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

GET /api/vmware-virtual-machine/

- Description changed from 'Mixin to optimize HEAD requests for DRF views bypassing serializer processing' to ''

POST /api/vmware-virtual-machine/{uuid}/pull/

- Summary changed from '' to 'Synchronize resource state'
- Description changed from '' to 'Schedule an asynchronous pull operation to synchronize resource state from the backend. Returns 202 if the pull was scheduled successfully, or 409 if the pull operation is not implemented for this resource type.'
- Responses changed
  - New response: 202
  - New response: 409
  - Deleted response: 200

POST /api/vmware-virtual-machine/{uuid}/unlink/

- Summary changed from '' to 'Unlink resource'
- Description changed from 'Delete resource from the database without scheduling operations on backend
and without checking current state of the resource. It is intended to be used
for removing resource stuck in transitioning state.' to 'Delete resource from the database without scheduling operations on backend
        and without checking current state of the resource. It is intended to be used
        for removing resource stuck in transitioning state.'
- Responses changed
  - New response: 204
  - Deleted response: 200

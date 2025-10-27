# Registered Handlers

This document lists all registered signal handlers found in the system.

<style>
table {
  table-layout: fixed;
  width: 100%;
}
td:nth-child(1), td:nth-child(2), td:nth-child(3) {
  width: 20%;
  word-wrap: break-word;
}
td:nth-child(4) {
  width: 40%;
  word-wrap: break-word;
}
</style>

## Application: `waldur_auth_saml2`

| Handler Name | Signal Type | Sender | Description |
|--------------|-------------|--------|-------------|
| `update_registration_method` | `Unknown Signal` | `core.User` | Update user's registration method to SAML2. |

## Application: `waldur_autoprovisioning`

| Handler Name | Signal Type | Sender | Description |
|--------------|-------------|--------|-------------|
| `handle_new_user` | `Django Signal (post_save)` | `core.User` | Create project and order for new user based on autoprovisioning rules. |

## Application: `waldur_core`

| Handler Name | Signal Type | Sender | Description |
|--------------|-------------|--------|-------------|
| `change_email_has_been_requested` | `Django Signal (post_save)` | `core.ChangeEmailRequest` | Send a notification when a user requests to change their email. |
| `change_users_quota` | `Custom Signal (role_granted)` | `—` | Update the user count quota for a customer when a user's role is changed. |
| `change_users_quota` | `Custom Signal (role_revoked)` | `—` | Update the user count quota for a customer when a user's role is changed. |
| `constance_updated` | `Custom Signal (config_updated)` | `—` | Clear the API configuration cache when a Constance setting is updated. |
| `create_auth_token` | `Django Signal (post_save)` | `core.User` | Create a token for a new user. |
| `create_existing_projects_completions` | `Django Signal (post_save)` | `structure.Customer` | Create ChecklistCompletion for existing projects when customer checklist is updated. |
| `create_notification_about_permission_request_has_been_submitted` | `Django Signal (post_save)` | `users.PermissionRequest` | Send a notification when a permission request has been submitted. |
| `create_project_metadata_completion` | `Django Signal (post_save)` | `structure.Project` | Create ChecklistCompletion for project metadata when a project is created. |
| `deactivate_user_if_no_roles` | `Custom Signal (role_revoked)` | `—` | Deactivate a user if they no longer have any active roles. |
| `delete_error_message` | `Custom Signal (post_transition)` | `structure.ServiceSettings` | Delete error message if instance state changed from erred |
| `delete_error_message` | `Custom Signal (post_transition)` | `structure.SharedServiceSettings` | Delete error message if instance state changed from erred |
| `delete_error_message` | `Custom Signal (post_transition)` | `structure.PrivateServiceSettings` | Delete error message if instance state changed from erred |
| `delete_error_message` | `Custom Signal (post_transition)` | `waldur_aws.Instance` | Delete error message if instance state changed from erred |
| `delete_error_message` | `Custom Signal (post_transition)` | `waldur_aws.Volume` | Delete error message if instance state changed from erred |
| `delete_error_message` | `Custom Signal (post_transition)` | `waldur_azure.ResourceGroup` | Delete error message if instance state changed from erred |
| `delete_error_message` | `Custom Signal (post_transition)` | `waldur_azure.StorageAccount` | Delete error message if instance state changed from erred |
| `delete_error_message` | `Custom Signal (post_transition)` | `waldur_azure.Network` | Delete error message if instance state changed from erred |
| `delete_error_message` | `Custom Signal (post_transition)` | `waldur_azure.SubNet` | Delete error message if instance state changed from erred |
| `delete_error_message` | `Custom Signal (post_transition)` | `waldur_azure.SecurityGroup` | Delete error message if instance state changed from erred |
| `delete_error_message` | `Custom Signal (post_transition)` | `waldur_azure.NetworkInterface` | Delete error message if instance state changed from erred |
| `delete_error_message` | `Custom Signal (post_transition)` | `waldur_azure.PublicIP` | Delete error message if instance state changed from erred |
| `delete_error_message` | `Custom Signal (post_transition)` | `waldur_azure.VirtualMachine` | Delete error message if instance state changed from erred |
| `delete_error_message` | `Custom Signal (post_transition)` | `waldur_azure.SQLServer` | Delete error message if instance state changed from erred |
| `delete_error_message` | `Custom Signal (post_transition)` | `waldur_azure.SQLDatabase` | Delete error message if instance state changed from erred |
| `delete_error_message` | `Custom Signal (post_transition)` | `waldur_digitalocean.Droplet` | Delete error message if instance state changed from erred |
| `delete_error_message` | `Custom Signal (post_transition)` | `google.GoogleCalendar` | Delete error message if instance state changed from erred |
| `delete_error_message` | `Custom Signal (post_transition)` | `openstack.Tenant` | Delete error message if instance state changed from erred |
| `delete_error_message` | `Custom Signal (post_transition)` | `openstack.ServerGroup` | Delete error message if instance state changed from erred |
| `delete_error_message` | `Custom Signal (post_transition)` | `openstack.SecurityGroup` | Delete error message if instance state changed from erred |
| `delete_error_message` | `Custom Signal (post_transition)` | `openstack.FloatingIP` | Delete error message if instance state changed from erred |
| `delete_error_message` | `Custom Signal (post_transition)` | `openstack.Router` | Delete error message if instance state changed from erred |
| `delete_error_message` | `Custom Signal (post_transition)` | `openstack.Network` | Delete error message if instance state changed from erred |
| `delete_error_message` | `Custom Signal (post_transition)` | `openstack.SubNet` | Delete error message if instance state changed from erred |
| `delete_error_message` | `Custom Signal (post_transition)` | `openstack.Port` | Delete error message if instance state changed from erred |
| `delete_error_message` | `Custom Signal (post_transition)` | `openstack.Volume` | Delete error message if instance state changed from erred |
| `delete_error_message` | `Custom Signal (post_transition)` | `openstack.Snapshot` | Delete error message if instance state changed from erred |
| `delete_error_message` | `Custom Signal (post_transition)` | `openstack.Instance` | Delete error message if instance state changed from erred |
| `delete_error_message` | `Custom Signal (post_transition)` | `openstack.Backup` | Delete error message if instance state changed from erred |
| `delete_error_message` | `Custom Signal (post_transition)` | `waldur_openstack_replication.Migration` | Delete error message if instance state changed from erred |
| `delete_error_message` | `Custom Signal (post_transition)` | `waldur_rancher.Cluster` | Delete error message if instance state changed from erred |
| `delete_error_message` | `Custom Signal (post_transition)` | `waldur_rancher.Node` | Delete error message if instance state changed from erred |
| `delete_error_message` | `Custom Signal (post_transition)` | `waldur_rancher.HPA` | Delete error message if instance state changed from erred |
| `delete_error_message` | `Custom Signal (post_transition)` | `waldur_rancher.Application` | Delete error message if instance state changed from erred |
| `delete_error_message` | `Custom Signal (post_transition)` | `waldur_rancher.Ingress` | Delete error message if instance state changed from erred |
| `delete_error_message` | `Custom Signal (post_transition)` | `waldur_rancher.Service` | Delete error message if instance state changed from erred |
| `delete_error_message` | `Custom Signal (post_transition)` | `waldur_slurm.Allocation` | Delete error message if instance state changed from erred |
| `delete_error_message` | `Custom Signal (post_transition)` | `waldur_vmware.VirtualMachine` | Delete error message if instance state changed from erred |
| `delete_error_message` | `Custom Signal (post_transition)` | `waldur_vmware.Port` | Delete error message if instance state changed from erred |
| `delete_error_message` | `Custom Signal (post_transition)` | `waldur_vmware.Disk` | Delete error message if instance state changed from erred |
| `delete_error_message` | `Custom Signal (post_transition)` | `waldur_firecrest.Job` | Delete error message if instance state changed from erred |
| `delete_error_message` | `Custom Signal (post_transition)` | `support.Issue` | Delete error message if instance state changed from erred |
| `delete_error_message` | `Custom Signal (post_transition)` | `support.Comment` | Delete error message if instance state changed from erred |
| `delete_error_message` | `Custom Signal (post_transition)` | `support.Attachment` | Delete error message if instance state changed from erred |
| `delete_error_message` | `Custom Signal (post_transition)` | `support.Feedback` | Delete error message if instance state changed from erred |
| `delete_project_metadata_completions` | `Django Signal (post_save)` | `structure.Customer` | Delete ChecklistCompletions when customer's project metadata checklist is removed. |
| `delete_quotas_when_model_is_deleted` | `Django Signal (pre_delete)` | `structure.Customer` | Delete all quotas related to a model when it is deleted. |
| `delete_quotas_when_model_is_deleted` | `Django Signal (pre_delete)` | `structure.Project` | Delete all quotas related to a model when it is deleted. |
| `delete_quotas_when_model_is_deleted` | `Django Signal (pre_delete)` | `structure.ServiceSettings` | Delete all quotas related to a model when it is deleted. |
| `delete_quotas_when_model_is_deleted` | `Django Signal (pre_delete)` | `structure.SharedServiceSettings` | Delete all quotas related to a model when it is deleted. |
| `delete_quotas_when_model_is_deleted` | `Django Signal (pre_delete)` | `structure.PrivateServiceSettings` | Delete all quotas related to a model when it is deleted. |
| `delete_quotas_when_model_is_deleted` | `Django Signal (pre_delete)` | `openstack.Tenant` | Delete all quotas related to a model when it is deleted. |
| `delete_quotas_when_model_is_deleted` | `Django Signal (pre_delete)` | `marketplace.Category` | Delete all quotas related to a model when it is deleted. |
| `delete_quotas_when_model_is_deleted` | `Django Signal (pre_delete)` | `marketplace.Offering` | Delete all quotas related to a model when it is deleted. |
| `delete_service_settings_on_scope_delete` | `Django Signal (pre_delete)` | `waldur_aws.Instance` | If VM that contains service settings were deleted - all settings |
| `delete_service_settings_on_scope_delete` | `Django Signal (pre_delete)` | `waldur_aws.Volume` | If VM that contains service settings were deleted - all settings |
| `delete_service_settings_on_scope_delete` | `Django Signal (pre_delete)` | `waldur_azure.ResourceGroup` | If VM that contains service settings were deleted - all settings |
| `delete_service_settings_on_scope_delete` | `Django Signal (pre_delete)` | `waldur_azure.StorageAccount` | If VM that contains service settings were deleted - all settings |
| `delete_service_settings_on_scope_delete` | `Django Signal (pre_delete)` | `waldur_azure.Network` | If VM that contains service settings were deleted - all settings |
| `delete_service_settings_on_scope_delete` | `Django Signal (pre_delete)` | `waldur_azure.SubNet` | If VM that contains service settings were deleted - all settings |
| `delete_service_settings_on_scope_delete` | `Django Signal (pre_delete)` | `waldur_azure.SecurityGroup` | If VM that contains service settings were deleted - all settings |
| `delete_service_settings_on_scope_delete` | `Django Signal (pre_delete)` | `waldur_azure.NetworkInterface` | If VM that contains service settings were deleted - all settings |
| `delete_service_settings_on_scope_delete` | `Django Signal (pre_delete)` | `waldur_azure.PublicIP` | If VM that contains service settings were deleted - all settings |
| `delete_service_settings_on_scope_delete` | `Django Signal (pre_delete)` | `waldur_azure.VirtualMachine` | If VM that contains service settings were deleted - all settings |
| `delete_service_settings_on_scope_delete` | `Django Signal (pre_delete)` | `waldur_azure.SQLServer` | If VM that contains service settings were deleted - all settings |
| `delete_service_settings_on_scope_delete` | `Django Signal (pre_delete)` | `waldur_azure.SQLDatabase` | If VM that contains service settings were deleted - all settings |
| `delete_service_settings_on_scope_delete` | `Django Signal (pre_delete)` | `waldur_digitalocean.Droplet` | If VM that contains service settings were deleted - all settings |
| `delete_service_settings_on_scope_delete` | `Django Signal (pre_delete)` | `openstack.Tenant` | If VM that contains service settings were deleted - all settings |
| `delete_service_settings_on_scope_delete` | `Django Signal (pre_delete)` | `openstack.ServerGroup` | If VM that contains service settings were deleted - all settings |
| `delete_service_settings_on_scope_delete` | `Django Signal (pre_delete)` | `openstack.SecurityGroup` | If VM that contains service settings were deleted - all settings |
| `delete_service_settings_on_scope_delete` | `Django Signal (pre_delete)` | `openstack.FloatingIP` | If VM that contains service settings were deleted - all settings |
| `delete_service_settings_on_scope_delete` | `Django Signal (pre_delete)` | `openstack.Router` | If VM that contains service settings were deleted - all settings |
| `delete_service_settings_on_scope_delete` | `Django Signal (pre_delete)` | `openstack.Network` | If VM that contains service settings were deleted - all settings |
| `delete_service_settings_on_scope_delete` | `Django Signal (pre_delete)` | `openstack.SubNet` | If VM that contains service settings were deleted - all settings |
| `delete_service_settings_on_scope_delete` | `Django Signal (pre_delete)` | `openstack.Port` | If VM that contains service settings were deleted - all settings |
| `delete_service_settings_on_scope_delete` | `Django Signal (pre_delete)` | `openstack.Volume` | If VM that contains service settings were deleted - all settings |
| `delete_service_settings_on_scope_delete` | `Django Signal (pre_delete)` | `openstack.Snapshot` | If VM that contains service settings were deleted - all settings |
| `delete_service_settings_on_scope_delete` | `Django Signal (pre_delete)` | `openstack.Instance` | If VM that contains service settings were deleted - all settings |
| `delete_service_settings_on_scope_delete` | `Django Signal (pre_delete)` | `openstack.Backup` | If VM that contains service settings were deleted - all settings |
| `delete_service_settings_on_scope_delete` | `Django Signal (pre_delete)` | `waldur_rancher.Cluster` | If VM that contains service settings were deleted - all settings |
| `delete_service_settings_on_scope_delete` | `Django Signal (pre_delete)` | `waldur_rancher.Application` | If VM that contains service settings were deleted - all settings |
| `delete_service_settings_on_scope_delete` | `Django Signal (pre_delete)` | `waldur_rancher.Ingress` | If VM that contains service settings were deleted - all settings |
| `delete_service_settings_on_scope_delete` | `Django Signal (pre_delete)` | `waldur_rancher.Service` | If VM that contains service settings were deleted - all settings |
| `delete_service_settings_on_scope_delete` | `Django Signal (pre_delete)` | `waldur_slurm.Allocation` | If VM that contains service settings were deleted - all settings |
| `delete_service_settings_on_scope_delete` | `Django Signal (pre_delete)` | `waldur_vmware.VirtualMachine` | If VM that contains service settings were deleted - all settings |
| `delete_service_settings_on_scope_delete` | `Django Signal (pre_delete)` | `waldur_vmware.Port` | If VM that contains service settings were deleted - all settings |
| `delete_service_settings_on_scope_delete` | `Django Signal (pre_delete)` | `waldur_vmware.Disk` | If VM that contains service settings were deleted - all settings |
| `delete_service_settings_on_scope_delete` | `Django Signal (pre_delete)` | `waldur_firecrest.Job` | If VM that contains service settings were deleted - all settings |
| `delete_stale_event_subscriptions` | `Django Signal (post_delete)` | `authtoken.Token` | Delete stale event subscriptions for a user when their token is deleted. |
| `handle_aggregated_quotas` | `Django Signal (post_save)` | `quotas.QuotaUsage` | Call aggregated quotas fields update methods |
| `handle_aggregated_quotas` | `Django Signal (pre_delete)` | `quotas.QuotaUsage` | Call aggregated quotas fields update methods |
| `log_access_subnet_deletion_succeeded` | `Django Signal (post_delete)` | `structure.AccessSubnet` | Log successful access subnet deletion. |
| `log_access_subnet_save` | `Django Signal (post_save)` | `structure.AccessSubnet` | Log access subnet creation and updates. |
| `log_customer_delete` | `Django Signal (post_delete)` | `structure.Customer` | Log customer deletion. |
| `log_customer_save` | `Django Signal (post_save)` | `structure.Customer` | Log customer creation and updates. |
| `log_project_delete` | `Django Signal (post_delete)` | `structure.Project` | Log project deletion. |
| `log_project_save` | `Django Signal (post_save)` | `structure.Project` | Log project creation and updates. |
| `log_resource_action` | `Custom Signal (post_transition)` | `waldur_aws.Instance` | Log resource state transitions. |
| `log_resource_action` | `Custom Signal (post_transition)` | `waldur_aws.Volume` | Log resource state transitions. |
| `log_resource_action` | `Custom Signal (post_transition)` | `waldur_azure.ResourceGroup` | Log resource state transitions. |
| `log_resource_action` | `Custom Signal (post_transition)` | `waldur_azure.StorageAccount` | Log resource state transitions. |
| `log_resource_action` | `Custom Signal (post_transition)` | `waldur_azure.Network` | Log resource state transitions. |
| `log_resource_action` | `Custom Signal (post_transition)` | `waldur_azure.SubNet` | Log resource state transitions. |
| `log_resource_action` | `Custom Signal (post_transition)` | `waldur_azure.SecurityGroup` | Log resource state transitions. |
| `log_resource_action` | `Custom Signal (post_transition)` | `waldur_azure.NetworkInterface` | Log resource state transitions. |
| `log_resource_action` | `Custom Signal (post_transition)` | `waldur_azure.PublicIP` | Log resource state transitions. |
| `log_resource_action` | `Custom Signal (post_transition)` | `waldur_azure.VirtualMachine` | Log resource state transitions. |
| `log_resource_action` | `Custom Signal (post_transition)` | `waldur_azure.SQLServer` | Log resource state transitions. |
| `log_resource_action` | `Custom Signal (post_transition)` | `waldur_azure.SQLDatabase` | Log resource state transitions. |
| `log_resource_action` | `Custom Signal (post_transition)` | `waldur_digitalocean.Droplet` | Log resource state transitions. |
| `log_resource_action` | `Custom Signal (post_transition)` | `openstack.Tenant` | Log resource state transitions. |
| `log_resource_action` | `Custom Signal (post_transition)` | `openstack.ServerGroup` | Log resource state transitions. |
| `log_resource_action` | `Custom Signal (post_transition)` | `openstack.SecurityGroup` | Log resource state transitions. |
| `log_resource_action` | `Custom Signal (post_transition)` | `openstack.FloatingIP` | Log resource state transitions. |
| `log_resource_action` | `Custom Signal (post_transition)` | `openstack.Router` | Log resource state transitions. |
| `log_resource_action` | `Custom Signal (post_transition)` | `openstack.Network` | Log resource state transitions. |
| `log_resource_action` | `Custom Signal (post_transition)` | `openstack.SubNet` | Log resource state transitions. |
| `log_resource_action` | `Custom Signal (post_transition)` | `openstack.Port` | Log resource state transitions. |
| `log_resource_action` | `Custom Signal (post_transition)` | `openstack.Volume` | Log resource state transitions. |
| `log_resource_action` | `Custom Signal (post_transition)` | `openstack.Snapshot` | Log resource state transitions. |
| `log_resource_action` | `Custom Signal (post_transition)` | `openstack.Instance` | Log resource state transitions. |
| `log_resource_action` | `Custom Signal (post_transition)` | `openstack.Backup` | Log resource state transitions. |
| `log_resource_action` | `Custom Signal (post_transition)` | `waldur_rancher.Cluster` | Log resource state transitions. |
| `log_resource_action` | `Custom Signal (post_transition)` | `waldur_rancher.Application` | Log resource state transitions. |
| `log_resource_action` | `Custom Signal (post_transition)` | `waldur_rancher.Ingress` | Log resource state transitions. |
| `log_resource_action` | `Custom Signal (post_transition)` | `waldur_rancher.Service` | Log resource state transitions. |
| `log_resource_action` | `Custom Signal (post_transition)` | `waldur_slurm.Allocation` | Log resource state transitions. |
| `log_resource_action` | `Custom Signal (post_transition)` | `waldur_vmware.VirtualMachine` | Log resource state transitions. |
| `log_resource_action` | `Custom Signal (post_transition)` | `waldur_vmware.Port` | Log resource state transitions. |
| `log_resource_action` | `Custom Signal (post_transition)` | `waldur_vmware.Disk` | Log resource state transitions. |
| `log_resource_action` | `Custom Signal (post_transition)` | `waldur_firecrest.Job` | Log resource state transitions. |
| `log_resource_creation_scheduled` | `Django Signal (post_save)` | `waldur_aws.Instance` | Log scheduled resource creation. |
| `log_resource_creation_scheduled` | `Django Signal (post_save)` | `waldur_aws.Volume` | Log scheduled resource creation. |
| `log_resource_creation_scheduled` | `Django Signal (post_save)` | `waldur_azure.ResourceGroup` | Log scheduled resource creation. |
| `log_resource_creation_scheduled` | `Django Signal (post_save)` | `waldur_azure.StorageAccount` | Log scheduled resource creation. |
| `log_resource_creation_scheduled` | `Django Signal (post_save)` | `waldur_azure.Network` | Log scheduled resource creation. |
| `log_resource_creation_scheduled` | `Django Signal (post_save)` | `waldur_azure.SubNet` | Log scheduled resource creation. |
| `log_resource_creation_scheduled` | `Django Signal (post_save)` | `waldur_azure.SecurityGroup` | Log scheduled resource creation. |
| `log_resource_creation_scheduled` | `Django Signal (post_save)` | `waldur_azure.NetworkInterface` | Log scheduled resource creation. |
| `log_resource_creation_scheduled` | `Django Signal (post_save)` | `waldur_azure.PublicIP` | Log scheduled resource creation. |
| `log_resource_creation_scheduled` | `Django Signal (post_save)` | `waldur_azure.VirtualMachine` | Log scheduled resource creation. |
| `log_resource_creation_scheduled` | `Django Signal (post_save)` | `waldur_azure.SQLServer` | Log scheduled resource creation. |
| `log_resource_creation_scheduled` | `Django Signal (post_save)` | `waldur_azure.SQLDatabase` | Log scheduled resource creation. |
| `log_resource_creation_scheduled` | `Django Signal (post_save)` | `waldur_digitalocean.Droplet` | Log scheduled resource creation. |
| `log_resource_creation_scheduled` | `Django Signal (post_save)` | `openstack.Tenant` | Log scheduled resource creation. |
| `log_resource_creation_scheduled` | `Django Signal (post_save)` | `openstack.ServerGroup` | Log scheduled resource creation. |
| `log_resource_creation_scheduled` | `Django Signal (post_save)` | `openstack.SecurityGroup` | Log scheduled resource creation. |
| `log_resource_creation_scheduled` | `Django Signal (post_save)` | `openstack.FloatingIP` | Log scheduled resource creation. |
| `log_resource_creation_scheduled` | `Django Signal (post_save)` | `openstack.Router` | Log scheduled resource creation. |
| `log_resource_creation_scheduled` | `Django Signal (post_save)` | `openstack.Network` | Log scheduled resource creation. |
| `log_resource_creation_scheduled` | `Django Signal (post_save)` | `openstack.SubNet` | Log scheduled resource creation. |
| `log_resource_creation_scheduled` | `Django Signal (post_save)` | `openstack.Port` | Log scheduled resource creation. |
| `log_resource_creation_scheduled` | `Django Signal (post_save)` | `openstack.Volume` | Log scheduled resource creation. |
| `log_resource_creation_scheduled` | `Django Signal (post_save)` | `openstack.Snapshot` | Log scheduled resource creation. |
| `log_resource_creation_scheduled` | `Django Signal (post_save)` | `openstack.Instance` | Log scheduled resource creation. |
| `log_resource_creation_scheduled` | `Django Signal (post_save)` | `openstack.Backup` | Log scheduled resource creation. |
| `log_resource_creation_scheduled` | `Django Signal (post_save)` | `waldur_rancher.Cluster` | Log scheduled resource creation. |
| `log_resource_creation_scheduled` | `Django Signal (post_save)` | `waldur_rancher.Application` | Log scheduled resource creation. |
| `log_resource_creation_scheduled` | `Django Signal (post_save)` | `waldur_rancher.Ingress` | Log scheduled resource creation. |
| `log_resource_creation_scheduled` | `Django Signal (post_save)` | `waldur_rancher.Service` | Log scheduled resource creation. |
| `log_resource_creation_scheduled` | `Django Signal (post_save)` | `waldur_slurm.Allocation` | Log scheduled resource creation. |
| `log_resource_creation_scheduled` | `Django Signal (post_save)` | `waldur_vmware.VirtualMachine` | Log scheduled resource creation. |
| `log_resource_creation_scheduled` | `Django Signal (post_save)` | `waldur_vmware.Port` | Log scheduled resource creation. |
| `log_resource_creation_scheduled` | `Django Signal (post_save)` | `waldur_vmware.Disk` | Log scheduled resource creation. |
| `log_resource_creation_scheduled` | `Django Signal (post_save)` | `waldur_firecrest.Job` | Log scheduled resource creation. |
| `log_resource_deleted` | `Django Signal (pre_delete)` | `waldur_aws.Instance` | Log resource deletion. |
| `log_resource_deleted` | `Django Signal (pre_delete)` | `waldur_aws.Volume` | Log resource deletion. |
| `log_resource_deleted` | `Django Signal (pre_delete)` | `waldur_azure.ResourceGroup` | Log resource deletion. |
| `log_resource_deleted` | `Django Signal (pre_delete)` | `waldur_azure.StorageAccount` | Log resource deletion. |
| `log_resource_deleted` | `Django Signal (pre_delete)` | `waldur_azure.Network` | Log resource deletion. |
| `log_resource_deleted` | `Django Signal (pre_delete)` | `waldur_azure.SubNet` | Log resource deletion. |
| `log_resource_deleted` | `Django Signal (pre_delete)` | `waldur_azure.SecurityGroup` | Log resource deletion. |
| `log_resource_deleted` | `Django Signal (pre_delete)` | `waldur_azure.NetworkInterface` | Log resource deletion. |
| `log_resource_deleted` | `Django Signal (pre_delete)` | `waldur_azure.PublicIP` | Log resource deletion. |
| `log_resource_deleted` | `Django Signal (pre_delete)` | `waldur_azure.VirtualMachine` | Log resource deletion. |
| `log_resource_deleted` | `Django Signal (pre_delete)` | `waldur_azure.SQLServer` | Log resource deletion. |
| `log_resource_deleted` | `Django Signal (pre_delete)` | `waldur_azure.SQLDatabase` | Log resource deletion. |
| `log_resource_deleted` | `Django Signal (pre_delete)` | `waldur_digitalocean.Droplet` | Log resource deletion. |
| `log_resource_deleted` | `Django Signal (pre_delete)` | `openstack.Tenant` | Log resource deletion. |
| `log_resource_deleted` | `Django Signal (pre_delete)` | `openstack.ServerGroup` | Log resource deletion. |
| `log_resource_deleted` | `Django Signal (pre_delete)` | `openstack.SecurityGroup` | Log resource deletion. |
| `log_resource_deleted` | `Django Signal (pre_delete)` | `openstack.FloatingIP` | Log resource deletion. |
| `log_resource_deleted` | `Django Signal (pre_delete)` | `openstack.Router` | Log resource deletion. |
| `log_resource_deleted` | `Django Signal (pre_delete)` | `openstack.Network` | Log resource deletion. |
| `log_resource_deleted` | `Django Signal (pre_delete)` | `openstack.SubNet` | Log resource deletion. |
| `log_resource_deleted` | `Django Signal (pre_delete)` | `openstack.Port` | Log resource deletion. |
| `log_resource_deleted` | `Django Signal (pre_delete)` | `openstack.Volume` | Log resource deletion. |
| `log_resource_deleted` | `Django Signal (pre_delete)` | `openstack.Snapshot` | Log resource deletion. |
| `log_resource_deleted` | `Django Signal (pre_delete)` | `openstack.Instance` | Log resource deletion. |
| `log_resource_deleted` | `Django Signal (pre_delete)` | `openstack.Backup` | Log resource deletion. |
| `log_resource_deleted` | `Django Signal (pre_delete)` | `waldur_rancher.Cluster` | Log resource deletion. |
| `log_resource_deleted` | `Django Signal (pre_delete)` | `waldur_rancher.Application` | Log resource deletion. |
| `log_resource_deleted` | `Django Signal (pre_delete)` | `waldur_rancher.Ingress` | Log resource deletion. |
| `log_resource_deleted` | `Django Signal (pre_delete)` | `waldur_rancher.Service` | Log resource deletion. |
| `log_resource_deleted` | `Django Signal (pre_delete)` | `waldur_slurm.Allocation` | Log resource deletion. |
| `log_resource_deleted` | `Django Signal (pre_delete)` | `waldur_vmware.VirtualMachine` | Log resource deletion. |
| `log_resource_deleted` | `Django Signal (pre_delete)` | `waldur_vmware.Port` | Log resource deletion. |
| `log_resource_deleted` | `Django Signal (pre_delete)` | `waldur_vmware.Disk` | Log resource deletion. |
| `log_resource_deleted` | `Django Signal (pre_delete)` | `waldur_firecrest.Job` | Log resource deletion. |
| `log_resource_imported` | `Custom Signal (resource_imported)` | `waldur_aws.Instance` | Log resource import. |
| `log_resource_imported` | `Custom Signal (resource_imported)` | `waldur_aws.Volume` | Log resource import. |
| `log_resource_imported` | `Custom Signal (resource_imported)` | `waldur_azure.ResourceGroup` | Log resource import. |
| `log_resource_imported` | `Custom Signal (resource_imported)` | `waldur_azure.StorageAccount` | Log resource import. |
| `log_resource_imported` | `Custom Signal (resource_imported)` | `waldur_azure.Network` | Log resource import. |
| `log_resource_imported` | `Custom Signal (resource_imported)` | `waldur_azure.SubNet` | Log resource import. |
| `log_resource_imported` | `Custom Signal (resource_imported)` | `waldur_azure.SecurityGroup` | Log resource import. |
| `log_resource_imported` | `Custom Signal (resource_imported)` | `waldur_azure.NetworkInterface` | Log resource import. |
| `log_resource_imported` | `Custom Signal (resource_imported)` | `waldur_azure.PublicIP` | Log resource import. |
| `log_resource_imported` | `Custom Signal (resource_imported)` | `waldur_azure.VirtualMachine` | Log resource import. |
| `log_resource_imported` | `Custom Signal (resource_imported)` | `waldur_azure.SQLServer` | Log resource import. |
| `log_resource_imported` | `Custom Signal (resource_imported)` | `waldur_azure.SQLDatabase` | Log resource import. |
| `log_resource_imported` | `Custom Signal (resource_imported)` | `waldur_digitalocean.Droplet` | Log resource import. |
| `log_resource_imported` | `Custom Signal (resource_imported)` | `openstack.Tenant` | Log resource import. |
| `log_resource_imported` | `Custom Signal (resource_imported)` | `openstack.ServerGroup` | Log resource import. |
| `log_resource_imported` | `Custom Signal (resource_imported)` | `openstack.SecurityGroup` | Log resource import. |
| `log_resource_imported` | `Custom Signal (resource_imported)` | `openstack.FloatingIP` | Log resource import. |
| `log_resource_imported` | `Custom Signal (resource_imported)` | `openstack.Router` | Log resource import. |
| `log_resource_imported` | `Custom Signal (resource_imported)` | `openstack.Network` | Log resource import. |
| `log_resource_imported` | `Custom Signal (resource_imported)` | `openstack.SubNet` | Log resource import. |
| `log_resource_imported` | `Custom Signal (resource_imported)` | `openstack.Port` | Log resource import. |
| `log_resource_imported` | `Custom Signal (resource_imported)` | `openstack.Volume` | Log resource import. |
| `log_resource_imported` | `Custom Signal (resource_imported)` | `openstack.Snapshot` | Log resource import. |
| `log_resource_imported` | `Custom Signal (resource_imported)` | `openstack.Instance` | Log resource import. |
| `log_resource_imported` | `Custom Signal (resource_imported)` | `openstack.Backup` | Log resource import. |
| `log_resource_imported` | `Custom Signal (resource_imported)` | `waldur_rancher.Cluster` | Log resource import. |
| `log_resource_imported` | `Custom Signal (resource_imported)` | `waldur_rancher.Application` | Log resource import. |
| `log_resource_imported` | `Custom Signal (resource_imported)` | `waldur_rancher.Ingress` | Log resource import. |
| `log_resource_imported` | `Custom Signal (resource_imported)` | `waldur_rancher.Service` | Log resource import. |
| `log_resource_imported` | `Custom Signal (resource_imported)` | `waldur_slurm.Allocation` | Log resource import. |
| `log_resource_imported` | `Custom Signal (resource_imported)` | `waldur_vmware.VirtualMachine` | Log resource import. |
| `log_resource_imported` | `Custom Signal (resource_imported)` | `waldur_vmware.Port` | Log resource import. |
| `log_resource_imported` | `Custom Signal (resource_imported)` | `waldur_vmware.Disk` | Log resource import. |
| `log_resource_imported` | `Custom Signal (resource_imported)` | `waldur_firecrest.Job` | Log resource import. |
| `log_role_granted` | `Custom Signal (role_granted)` | `—` | Log the event of a user being granted a role. |
| `log_role_revoked` | `Custom Signal (role_revoked)` | `—` | Log the event of a user having a role revoked. |
| `log_role_updated` | `Custom Signal (role_updated)` | `—` | Log the event of a user's role being updated. |
| `log_ssh_key_delete` | `Django Signal (post_delete)` | `core.SshPublicKey` | Log SSH key deletion events. |
| `log_ssh_key_save` | `Django Signal (post_save)` | `core.SshPublicKey` | Log SSH key creation events. |
| `log_token_create` | `Django Signal (post_save)` | `authtoken.Token` | Log token creation events. |
| `log_user_delete` | `Django Signal (post_delete)` | `core.User` | Log user deletion events. |
| `log_user_save` | `Django Signal (post_save)` | `core.User` | Log user creation, update, and activation/deactivation events. |
| `permissions_request_approved` | `Custom Signal (permissions_request_approved)` | `users.PermissionRequest` | Send a notification when a permission request has been approved. |
| `preserve_fields_before_update` | `Django Signal (pre_save)` | `core.User` | Preserve fields of a user instance before it is updated. |
| `process_hook` | `Django Signal (post_save)` | `logging.Event` | Process a hook for a given event. |
| `projects_customer_has_been_changed` | `Custom Signal (project_moved)` | `structure.Project` | Recalculate quotas when a project's customer has been changed. |
| `recalculate_count_quota` | `Django Signal (post_save)` | `structure.Project` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_save)` | `waldur_aws.Instance` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_save)` | `waldur_aws.Volume` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_save)` | `waldur_azure.ResourceGroup` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_save)` | `waldur_azure.StorageAccount` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_save)` | `waldur_azure.Network` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_save)` | `waldur_azure.SubNet` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_save)` | `waldur_azure.SecurityGroup` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_save)` | `waldur_azure.NetworkInterface` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_save)` | `waldur_azure.PublicIP` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_save)` | `waldur_azure.VirtualMachine` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_save)` | `waldur_azure.SQLServer` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_save)` | `waldur_azure.SQLDatabase` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_save)` | `waldur_digitalocean.Droplet` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_save)` | `openstack.Tenant` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_save)` | `openstack.ServerGroup` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_save)` | `openstack.SecurityGroup` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_save)` | `openstack.FloatingIP` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_save)` | `openstack.Router` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_save)` | `openstack.Network` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_save)` | `openstack.SubNet` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_save)` | `openstack.Port` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_save)` | `openstack.Volume` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_save)` | `openstack.Snapshot` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_save)` | `openstack.Instance` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_save)` | `openstack.Backup` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_save)` | `waldur_rancher.Cluster` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_save)` | `waldur_rancher.Application` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_save)` | `waldur_rancher.Ingress` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_save)` | `waldur_rancher.Service` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_save)` | `waldur_slurm.Allocation` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_save)` | `waldur_vmware.VirtualMachine` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_save)` | `waldur_vmware.Port` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_save)` | `waldur_vmware.Disk` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_save)` | `waldur_firecrest.Job` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_save)` | `marketplace.Order` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_delete)` | `structure.Project` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_delete)` | `waldur_aws.Instance` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_delete)` | `waldur_aws.Volume` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_delete)` | `waldur_azure.ResourceGroup` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_delete)` | `waldur_azure.StorageAccount` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_delete)` | `waldur_azure.Network` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_delete)` | `waldur_azure.SubNet` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_delete)` | `waldur_azure.SecurityGroup` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_delete)` | `waldur_azure.NetworkInterface` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_delete)` | `waldur_azure.PublicIP` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_delete)` | `waldur_azure.VirtualMachine` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_delete)` | `waldur_azure.SQLServer` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_delete)` | `waldur_azure.SQLDatabase` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_delete)` | `waldur_digitalocean.Droplet` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_delete)` | `openstack.Tenant` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_delete)` | `openstack.ServerGroup` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_delete)` | `openstack.SecurityGroup` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_delete)` | `openstack.FloatingIP` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_delete)` | `openstack.Router` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_delete)` | `openstack.Network` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_delete)` | `openstack.SubNet` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_delete)` | `openstack.Port` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_delete)` | `openstack.Volume` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_delete)` | `openstack.Snapshot` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_delete)` | `openstack.Instance` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_delete)` | `openstack.Backup` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_delete)` | `waldur_rancher.Cluster` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_delete)` | `waldur_rancher.Application` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_delete)` | `waldur_rancher.Ingress` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_delete)` | `waldur_rancher.Service` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_delete)` | `waldur_slurm.Allocation` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_delete)` | `waldur_vmware.VirtualMachine` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_delete)` | `waldur_vmware.Port` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_delete)` | `waldur_vmware.Disk` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_delete)` | `waldur_firecrest.Job` | Recalculate count quota when an instance is created or deleted. |
| `recalculate_count_quota` | `Django Signal (post_delete)` | `marketplace.Order` | Recalculate count quota when an instance is created or deleted. |
| `revoke_roles_on_project_deletion` | `Django Signal (pre_delete)` | `structure.Project` | When project is deleted, capture user role snapshots before revoking them. |
| `set_default_token_lifetime` | `Django Signal (post_save)` | `core.User` | Set the default token lifetime for a new user. |
| `update_customer_users_count` | `Custom Signal (recalculate_quotas)` | `—` | Update the user count for all customers. |
| `update_resource_start_time` | `Django Signal (post_save)` | `waldur_aws.Instance` | Update the start time of a resource when its runtime state changes. |
| `update_resource_start_time` | `Django Signal (post_save)` | `waldur_azure.VirtualMachine` | Update the start time of a resource when its runtime state changes. |
| `update_resource_start_time` | `Django Signal (post_save)` | `waldur_digitalocean.Droplet` | Update the start time of a resource when its runtime state changes. |
| `update_resource_start_time` | `Django Signal (post_save)` | `openstack.Instance` | Update the start time of a resource when its runtime state changes. |

## Application: `waldur_freeipa`

| Handler Name | Signal Type | Sender | Description |
|--------------|-------------|--------|-------------|
| `log_profile_deleted` | `Django Signal (pre_delete)` | `waldur_freeipa.Profile` | Log FreeIPA profile deletion events. |
| `log_profile_event` | `Django Signal (pre_save)` | `waldur_freeipa.Profile` | Log FreeIPA profile creation, enable, and disable events. |
| `schedule_ssh_key_sync_when_key_is_created` | `Django Signal (post_save)` | `core.SshPublicKey` | Schedule an SSH key synchronization task when a key is created. |
| `schedule_ssh_key_sync_when_key_is_deleted` | `Django Signal (pre_delete)` | `core.SshPublicKey` | Schedule an SSH key synchronization task when a key is deleted. |
| `schedule_sync` | `Django Signal (post_save)` | `structure.Customer` | Schedule a synchronization task. |
| `schedule_sync` | `Django Signal (post_save)` | `structure.Project` | Schedule a synchronization task. |
| `schedule_sync` | `Django Signal (pre_delete)` | `structure.Customer` | Schedule a synchronization task. |
| `schedule_sync` | `Django Signal (pre_delete)` | `structure.Project` | Schedule a synchronization task. |
| `schedule_sync` | `Custom Signal (role_granted)` | `—` | Schedule a synchronization task. |
| `schedule_sync` | `Custom Signal (role_revoked)` | `—` | Schedule a synchronization task. |
| `schedule_sync_on_quota_change` | `Django Signal (post_save)` | `quotas.QuotaLimit` | Schedule a synchronization task when a quota is changed. |
| `update_user` | `Django Signal (post_save)` | `core.User` | Update a user's FreeIPA profile when their user account is updated. |

## Application: `waldur_lexis`

| Handler Name | Signal Type | Sender | Description |
|--------------|-------------|--------|-------------|
| `request_ssh_key_for_heappe_robot_account` | `Django Signal (post_save)` | `marketplace.RobotAccount` | Request an SSH key for a HEAppE robot account. |

## Application: `waldur_mastermind`

| Handler Name | Signal Type | Sender | Description |
|--------------|-------------|--------|-------------|
| `add_call_managing_organization_uuid` | `Custom Signal (pre_serializer_fields)` | `CustomerSerializer` | Add a call managing organization UUID field to the serializer. |
| `add_customer_credit` | `Custom Signal (pre_serializer_fields)` | `CustomerSerializer` | Add a customer credit field to the serializer. |
| `add_customer_unallocated_credit` | `Custom Signal (pre_serializer_fields)` | `CustomerSerializer` | Add a customer unallocated credit field to the serializer. |
| `add_google_calendar_info` | `Custom Signal (pre_serializer_fields)` | `ProviderOfferingDetailsSerializer` | Add a Google Calendar info field to the serializer. |
| `add_google_calendar_info` | `Custom Signal (pre_serializer_fields)` | `PublicOfferingDetailsSerializer` | Add a Google Calendar info field to the serializer. |
| `add_google_calendar_link` | `Custom Signal (pre_serializer_fields)` | `ProviderOfferingDetailsSerializer` | Add a Google Calendar link field to the serializer. |
| `add_google_calendar_link` | `Custom Signal (pre_serializer_fields)` | `PublicOfferingDetailsSerializer` | Add a Google Calendar link field to the serializer. |
| `add_integration_status` | `Custom Signal (pre_serializer_fields)` | `ProviderOfferingDetailsSerializer` | Add an integration status field to the serializer. |
| `add_issue` | `Custom Signal (pre_serializer_fields)` | `OrderDetailsSerializer` | Add an issue field to the serializer. |
| `add_maintenance_fields_to_admin_announcement_serializer` | `Custom Signal (pre_serializer_fields)` | `AdminAnnouncementSerializer` | Add maintenance-related fields to AdminAnnouncementSerializer when maintenance is scheduled. |
| `add_marketplace_offering` | `Custom Signal (pre_serializer_fields)` | `OpenStackFloatingIPSerializer` | Add marketplace offering related fields to the serializer. |
| `add_marketplace_offering` | `Custom Signal (pre_serializer_fields)` | `OpenStackSecurityGroupSerializer` | Add marketplace offering related fields to the serializer. |
| `add_marketplace_offering` | `Custom Signal (pre_serializer_fields)` | `OpenStackServerGroupSerializer` | Add marketplace offering related fields to the serializer. |
| `add_marketplace_offering` | `Custom Signal (pre_serializer_fields)` | `OpenStackPortSerializer` | Add marketplace offering related fields to the serializer. |
| `add_marketplace_offering` | `Custom Signal (pre_serializer_fields)` | `OpenStackNetworkSerializer` | Add marketplace offering related fields to the serializer. |
| `add_marketplace_offering` | `Custom Signal (pre_serializer_fields)` | `OpenStackSubNetSerializer` | Add marketplace offering related fields to the serializer. |
| `add_marketplace_offering` | `Custom Signal (pre_serializer_fields)` | `OpenStackSnapshotSerializer` | Add marketplace offering related fields to the serializer. |
| `add_marketplace_offering` | `Custom Signal (pre_serializer_fields)` | `OpenStackBackupSerializer` | Add marketplace offering related fields to the serializer. |
| `add_marketplace_offering` | `Custom Signal (pre_serializer_fields)` | `AwsInstanceSerializer` | Add marketplace offering related fields to the serializer. |
| `add_marketplace_offering` | `Custom Signal (pre_serializer_fields)` | `AzureVirtualMachineSerializer` | Add marketplace offering related fields to the serializer. |
| `add_marketplace_offering` | `Custom Signal (pre_serializer_fields)` | `DigitalOceanDropletSerializer` | Add marketplace offering related fields to the serializer. |
| `add_marketplace_offering` | `Custom Signal (pre_serializer_fields)` | `OpenStackInstanceCreateSerializer` | Add marketplace offering related fields to the serializer. |
| `add_marketplace_offering` | `Custom Signal (pre_serializer_fields)` | `OpenStackInstanceSerializer` | Add marketplace offering related fields to the serializer. |
| `add_marketplace_offering` | `Custom Signal (pre_serializer_fields)` | `AwsVolumeSerializer` | Add marketplace offering related fields to the serializer. |
| `add_marketplace_offering` | `Custom Signal (pre_serializer_fields)` | `AzureResourceGroupSerializer` | Add marketplace offering related fields to the serializer. |
| `add_marketplace_offering` | `Custom Signal (pre_serializer_fields)` | `AzureSqlServerSerializer` | Add marketplace offering related fields to the serializer. |
| `add_marketplace_offering` | `Custom Signal (pre_serializer_fields)` | `AzurePublicIPSerializer` | Add marketplace offering related fields to the serializer. |
| `add_marketplace_offering` | `Custom Signal (pre_serializer_fields)` | `AzureSqlDatabaseSerializer` | Add marketplace offering related fields to the serializer. |
| `add_marketplace_offering` | `Custom Signal (pre_serializer_fields)` | `OpenStackTenantSerializer` | Add marketplace offering related fields to the serializer. |
| `add_marketplace_offering` | `Custom Signal (pre_serializer_fields)` | `OpenStackRouterSerializer` | Add marketplace offering related fields to the serializer. |
| `add_marketplace_offering` | `Custom Signal (pre_serializer_fields)` | `OpenStackVolumeSerializer` | Add marketplace offering related fields to the serializer. |
| `add_marketplace_offering` | `Custom Signal (pre_serializer_fields)` | `RancherClusterCreateSerializer` | Add marketplace offering related fields to the serializer. |
| `add_marketplace_offering` | `Custom Signal (pre_serializer_fields)` | `RancherClusterSerializer` | Add marketplace offering related fields to the serializer. |
| `add_marketplace_offering` | `Custom Signal (pre_serializer_fields)` | `RancherApplicationSerializer` | Add marketplace offering related fields to the serializer. |
| `add_marketplace_offering` | `Custom Signal (pre_serializer_fields)` | `RancherIngressSerializer` | Add marketplace offering related fields to the serializer. |
| `add_marketplace_offering` | `Custom Signal (pre_serializer_fields)` | `RancherServiceCreateSerializer` | Add marketplace offering related fields to the serializer. |
| `add_marketplace_offering` | `Custom Signal (pre_serializer_fields)` | `RancherServiceSerializer` | Add marketplace offering related fields to the serializer. |
| `add_marketplace_offering` | `Custom Signal (pre_serializer_fields)` | `SlurmAllocationSerializer` | Add marketplace offering related fields to the serializer. |
| `add_marketplace_offering` | `Custom Signal (pre_serializer_fields)` | `VmwareVirtualMachineSerializer` | Add marketplace offering related fields to the serializer. |
| `add_marketplace_offering` | `Custom Signal (pre_serializer_fields)` | `VmwarePortSerializer` | Add marketplace offering related fields to the serializer. |
| `add_marketplace_offering` | `Custom Signal (pre_serializer_fields)` | `VmwareDiskSerializer` | Add marketplace offering related fields to the serializer. |
| `add_marketplace_resource_count` | `Custom Signal (pre_serializer_fields)` | `ProjectSerializer` | Add a marketplace resource count field to the serializer. |
| `add_marketplace_resource_uuid` | `Custom Signal (pre_serializer_fields)` | `OpenStackNestedVolumeSerializer` | Add a marketplace resource UUID field to the serializer. |
| `add_payment_profile` | `Custom Signal (pre_serializer_fields)` | `CustomerSerializer` | Add a payment profile field to the serializer. |
| `add_price_estimate` | `Custom Signal (pre_serializer_fields)` | `ProjectSerializer` | Add a billing price estimate field to the serializer. |
| `add_price_estimate` | `Custom Signal (pre_serializer_fields)` | `ProjectEstimatedCostPolicySerializer` | Add a billing price estimate field to the serializer. |
| `add_price_estimate` | `Custom Signal (pre_serializer_fields)` | `CustomerSerializer` | Add a billing price estimate field to the serializer. |
| `add_price_estimate` | `Custom Signal (pre_serializer_fields)` | `CustomerEstimatedCostPolicySerializer` | Add a billing price estimate field to the serializer. |
| `add_project_credit` | `Custom Signal (pre_serializer_fields)` | `ProjectSerializer` | Add a project credit field to the serializer. |
| `add_promotion_campaigns` | `Custom Signal (pre_serializer_fields)` | `PublicOfferingDetailsSerializer` | Add promotion campaigns to the serializer. |
| `add_router_external_ips` | `Custom Signal (pre_serializer_fields)` | `OpenStackRouterSerializer` | Add router external IPs to the serializer. |
| `add_service_provider` | `Custom Signal (pre_serializer_fields)` | `CustomerSerializer` | Add a service provider field to the serializer. |
| `add_service_provider_url` | `Custom Signal (pre_serializer_fields)` | `CustomerSerializer` | Add a service provider URL field to the serializer. |
| `add_service_provider_uuid` | `Custom Signal (pre_serializer_fields)` | `CustomerSerializer` | Add a service provider UUID field to the serializer. |
| `apply_campaign_to_pending_invoices` | `Django Signal (post_save)` | `promotions.Campaign` | Apply campaign discounts to pending invoices and create discounted resources. |
| `archive_offering` | `Django Signal (pre_delete)` | `openstack.Tenant` | Archive marketplace offerings when OpenStack tenant is deleted. |
| `change_order_state` | `Django Signal (post_save)` | `waldur_azure.VirtualMachine` | Change the state of an order based on resource state changes. |
| `change_order_state` | `Django Signal (post_save)` | `waldur_azure.SQLServer` | Change the state of an order based on resource state changes. |
| `change_order_state` | `Django Signal (post_save)` | `waldur_azure.SQLDatabase` | Change the state of an order based on resource state changes. |
| `change_order_state` | `Django Signal (post_save)` | `openstack.Instance` | Change the state of an order based on resource state changes. |
| `change_order_state` | `Django Signal (post_save)` | `openstack.Volume` | Change the state of an order based on resource state changes. |
| `change_order_state` | `Django Signal (post_save)` | `openstack.Tenant` | Change the state of an order based on resource state changes. |
| `change_order_state` | `Django Signal (post_save)` | `waldur_rancher.Cluster` | Change the state of an order based on resource state changes. |
| `change_order_state` | `Django Signal (post_save)` | `waldur_slurm.Allocation` | Change the state of an order based on resource state changes. |
| `change_order_state` | `Django Signal (post_save)` | `waldur_vmware.VirtualMachine` | Change the state of an order based on resource state changes. |
| `cleanup_admin_announcement_on_maintenance_deletion` | `Django Signal (pre_delete)` | `marketplace.MaintenanceAnnouncement` | Ensure AdminAnnouncement is cleaned up when MaintenanceAnnouncement is deleted. |
| `close_course_accounts_after_project_removal` | `Django Signal (pre_delete)` | `structure.Project` | No description |
| `close_customer_service_accounts_on_customer_deletion` | `Django Signal (pre_delete)` | `structure.Customer` | Close service accounts associated with a customer when the customer is deleted. |
| `close_resource_plan_period_when_resource_is_terminated` | `Django Signal (post_save)` | `marketplace.Resource` | Handle case when resource has been terminated by service provider. |
| `close_service_accounts_on_project_deletion` | `Django Signal (pre_delete)` | `structure.Project` | Close service accounts associated with a project when the project is deleted. |
| `create_checklist_completion` | `Django Signal (post_save)` | `proposal.Proposal` | Create checklist completion tracking when proposal is created. |
| `create_feedback_if_issue_has_been_resolved` | `Django Signal (post_save)` | `support.Issue` | Create feedback request when support issue transitions to resolved state. |
| `create_issue_if_membership_changed` | `Django Signal (post_save)` | `permissions.UserRole` | Create support issue when user role membership changes in organization. |
| `create_marketplace_resource_for_imported_cluster` | `Custom Signal (resource_imported)` | `waldur_rancher.Cluster` | Create marketplace resource when Rancher cluster is imported from external system. |
| `create_marketplace_resource_for_imported_resources` | `Custom Signal (resource_imported)` | `waldur_azure.VirtualMachine` | No description |
| `create_marketplace_resource_for_imported_resources` | `Custom Signal (resource_imported)` | `openstack.Instance` | No description |
| `create_marketplace_resource_for_imported_resources` | `Custom Signal (resource_imported)` | `openstack.Volume` | No description |
| `create_marketplace_resource_for_imported_resources` | `Custom Signal (resource_imported)` | `openstack.Tenant` | No description |
| `create_offering_component_for_volume_type` | `Django Signal (post_save)` | `openstack.VolumeType` | Create marketplace offering component when OpenStack volume type is created. |
| `create_offering_from_tenant` | `Django Signal (post_save)` | `openstack.Tenant` | No description |
| `create_offering_user_checklist_completions` | `Django Signal (post_save)` | `marketplace.OfferingUser` | Create checklist completions for OfferingUser when created. |
| `create_offering_user_for_new_resource` | `Custom Signal (resource_creation_succeeded)` | `marketplace.Resource` | Create an offering user for a new resource. |
| `create_offering_user_for_rancher_user` | `Django Signal (post_save)` | `waldur_rancher.RancherUser` | No description |
| `create_offering_user_for_slurm_user` | `Custom Signal (slurm_association_created)` | `waldur_slurm.Allocation` | No description |
| `create_offering_users_when_project_role_granted` | `Custom Signal (role_granted)` | `—` | Create offering users when a project role is granted. |
| `create_price_estimate` | `Django Signal (post_save)` | `structure.Project` | Create price estimate when customer or project is created. |
| `create_price_estimate` | `Django Signal (post_save)` | `structure.Customer` | Create price estimate when customer or project is created. |
| `create_public_cluster_ip_for_floating_ip` | `Django Signal (post_save)` | `openstack.FloatingIP` | No description |
| `create_recurring_usage_if_invoice_has_been_created` | `Django Signal (post_save)` | `invoices.Invoice` | No description |
| `create_request_when_project_is_updated` | `Django Signal (post_save)` | `structure.Project` | No description |
| `create_resource_of_volume_if_instance_created` | `Django Signal (post_save)` | `marketplace.Resource` | No description |
| `create_resource_plan_period_when_resource_is_created` | `Django Signal (post_save)` | `marketplace.Resource` | Create a resource plan period when a resource is created. |
| `create_screenshot_thumbnail` | `Django Signal (post_save)` | `marketplace.Screenshot` | Create a thumbnail for a screenshot. |
| `customer_component_usage_policy_trigger_handler` | `Django Signal (post_save)` | `marketplace.ComponentUsage` | Evaluate customer component usage policies when component usage records change. |
| `customer_credit_changed_handler` | `Django Signal (post_save)` | `invoices.CustomerCredit` | Handle customer credit value changes and evaluate related policies. |
| `customer_credit_offerings_list_changed_handler` | `Django Signal (m2m_changed)` | `CustomerCredit_offerings` | No description |
| `customer_estimated_cost_policy_trigger_handler` | `Django Signal (post_save)` | `invoices.InvoiceItem` | Evaluate customer cost policies when invoice items are updated. |
| `delete_checklist_completion` | `Django Signal (pre_delete)` | `proposal.Proposal` | Remove checklist completion tracking when proposal is deleted. |
| `delete_expired_project_if_every_resource_has_been_terminated` | `Django Signal (post_save)` | `marketplace.Resource` | Delete an expired project if all its resources have been terminated. |
| `delete_offering_component_for_volume_type` | `Django Signal (post_delete)` | `openstack.VolumeType` | No description |
| `delete_offering_user_checklist_completions` | `Django Signal (pre_delete)` | `marketplace.OfferingUser` | Delete related checklist completions when OfferingUser is deleted. |
| `delete_remote_project` | `Django Signal (post_delete)` | `structure.Project` | No description |
| `delete_service_setting_when_offering_is_deleted` | `Django Signal (post_delete)` | `marketplace.Offering` | Delete service settings when an offering is deleted. |
| `delete_stale_price_estimate` | `Django Signal (pre_delete)` | `structure.Project` | Delete price estimates when customer or project is deleted. |
| `delete_stale_price_estimate` | `Django Signal (pre_delete)` | `structure.Customer` | Delete price estimates when customer or project is deleted. |
| `disable_archived_service_settings_without_existing_resource` | `Django Signal (post_save)` | `marketplace.Resource` | Disable archived service settings if there are no existing resources. |
| `disable_service_settings_without_existing_resource_when_archived` | `Django Signal (post_save)` | `marketplace.Offering` | Disable service settings without existing resources when an offering is archived. |
| `drop_offering_user_for_rancher_user` | `Django Signal (pre_delete)` | `waldur_rancher.RancherUser` | No description |
| `drop_offering_user_for_slurm_user` | `Custom Signal (slurm_association_deleted)` | `waldur_slurm.Allocation` | No description |
| `emit_invoice_created_event` | `Django Signal (post_save)` | `invoices.Invoice` | Emit invoice created signal when invoice state changes to CREATED. |
| `enable_service_settings_when_not_archived` | `Django Signal (post_save)` | `marketplace.Offering` | Enable service settings when an offering is not archived. |
| `enable_service_settings_with_existing_resource` | `Django Signal (post_save)` | `marketplace.Resource` | Enable service settings if there are existing resources. |
| `handle_openstack_tenant_order_creation` | `Django Signal (post_save)` | `marketplace.Order` | No description |
| `handle_openstack_tenant_order_termination` | `Django Signal (post_save)` | `marketplace.Order` | No description |
| `handler` | `Django Signal (post_save)` | `marketplace.Resource` | No description |
| `handler` | `Django Signal (post_save)` | `invoices.InvoiceItem` | No description |
| `handler` | `Django Signal (post_save)` | `marketplace.ComponentUsage` | No description |
| `import_instances_and_volumes_if_tenant_has_been_imported` | `Custom Signal (resource_imported)` | `openstack.Tenant` | No description |
| `import_instances_and_volumes_if_tenant_has_been_imported` | `Custom Signal (tenant_pull_succeeded)` | `openstack.Tenant` | No description |
| `import_resource_metadata_when_resource_is_created` | `Django Signal (post_save)` | `marketplace.Resource` | Import OpenStack resource metadata when marketplace resource is created. |
| `init_resource_parent` | `Django Signal (post_save)` | `marketplace.Resource` | Initialize the parent resource for a newly created resource. |
| `limit_update_failed` | `Custom Signal (resource_limit_update_failed)` | `marketplace.Resource` | Handle failed limit updates. |
| `limit_update_succeeded` | `Custom Signal (resource_limit_update_succeeded)` | `marketplace.Resource` | Handle successful limit updates. |
| `log_attachment_delete` | `Django Signal (post_delete)` | `support.Attachment` | No description |
| `log_attachment_save` | `Django Signal (post_save)` | `support.Attachment` | No description |
| `log_credit` | `Django Signal (post_save)` | `invoices.CustomerCredit` | No description |
| `log_invoice_item_delete` | `Django Signal (post_delete)` | `invoices.InvoiceItem` | No description |
| `log_invoice_item_save` | `Django Signal (post_save)` | `invoices.InvoiceItem` | No description |
| `log_invoice_state_transition` | `Django Signal (post_save)` | `invoices.Invoice` | No description |
| `log_issue_delete` | `Django Signal (post_delete)` | `support.Issue` | No description |
| `log_issue_save` | `Django Signal (post_save)` | `support.Issue` | No description |
| `log_offering_role_created_or_updated` | `Django Signal (post_save)` | `marketplace.OfferingUserRole` | Log offering role creation and updates. |
| `log_offering_role_deleted` | `Django Signal (post_delete)` | `marketplace.OfferingUserRole` | Log offering role deletion. |
| `log_offering_user_created` | `Django Signal (post_save)` | `marketplace.OfferingUser` | Log offering user creation. |
| `log_offering_user_deleted` | `Django Signal (post_delete)` | `marketplace.OfferingUser` | Log offering user deletion. |
| `log_order_events` | `Django Signal (post_save)` | `marketplace.Order` | Log order creation and state transition events. |
| `log_request_events` | `Django Signal (post_save)` | `marketplace_remote.ProjectUpdateRequest` | No description |
| `log_resource_events` | `Django Signal (post_save)` | `marketplace.Resource` | Log resource creation request events. |
| `log_resource_robot_account_created_or_updated` | `Django Signal (post_save)` | `marketplace.RobotAccount` | Log resource robot account creation and updates. |
| `log_resource_robot_account_deleted` | `Django Signal (post_delete)` | `marketplace.RobotAccount` | Log resource robot account deletion. |
| `log_resource_user_created` | `Django Signal (post_save)` | `marketplace.ResourceUser` | Log resource user creation. |
| `log_resource_user_deleted` | `Django Signal (post_delete)` | `marketplace.ResourceUser` | Log resource user deletion. |
| `log_service_account_created_or_updated` | `Django Signal (post_save)` | `ScopedServiceAccount` | Log service account creation and updates. |
| `log_service_account_deleted` | `Django Signal (post_delete)` | `ScopedServiceAccount` | Log service account deletion. |
| `log_terms_of_service_consent_granted` | `Django Signal (post_save)` | `marketplace.UserOfferingConsent` | Log when a user grants consent to Terms of Service. |
| `log_terms_of_service_consent_revoked` | `Django Signal (post_save)` | `marketplace.UserOfferingConsent` | Log when a user revokes consent to Terms of Service. |
| `manage_maintenance_admin_announcements` | `Django Signal (post_save)` | `marketplace.MaintenanceAnnouncement` | Manage AdminAnnouncement lifecycle based on MaintenanceAnnouncement state changes. |
| `mark_synced_fields_as_read_only` | `Custom Signal (pre_serializer_fields)` | `OfferingOptionsUpdateSerializer` | No description |
| `mark_synced_fields_as_read_only` | `Custom Signal (pre_serializer_fields)` | `OfferingOverviewUpdateSerializer` | No description |
| `notify_about_project_details_update` | `Django Signal (post_save)` | `marketplace_remote.ProjectUpdateRequest` | No description |
| `notify_about_request_based_item_creation` | `Django Signal (post_save)` | `support.Issue` | No description |
| `notify_approvers_when_order_is_created` | `Django Signal (post_save)` | `marketplace.Order` | Notify approvers when an order is created. |
| `notify_offering_user_about_tos_requirement` | `Django Signal (post_save)` | `marketplace.OfferingUser` | Notify user about ToS requirement when OfferingUser is created. |
| `notify_user_about_rejected_order` | `Django Signal (post_save)` | `marketplace.Order` | Notify user about rejected order. |
| `notify_users_about_tos_update_signal` | `Django Signal (post_save)` | `marketplace.OfferingTermsOfService` | Notify users when ToS is updated and requires re-consent. |
| `offering_component_has_been_created_or_updated` | `Django Signal (post_save)` | `marketplace.OfferingComponent` | Log offering component creation and updates. |
| `offering_component_has_been_deleted` | `Django Signal (post_delete)` | `marketplace.OfferingComponent` | Log offering component deletion. |
| `offering_has_been_created_or_updated` | `Django Signal (post_save)` | `marketplace.Offering` | Log offering creation and state updates. |
| `on_resource_post_save` | `Django Signal (post_save)` | `marketplace.Resource` | Handle resource state changes and billing events. |
| `plan_component_has_been_updated` | `Django Signal (post_save)` | `marketplace.PlanComponent` | Log plan component updates. |
| `plan_has_been_created_or_updated` | `Django Signal (post_save)` | `marketplace.Plan` | Log plan creation, update, and archiving events. |
| `process_invitations_and_orders_when_project_start_date_is_unset` | `Django Signal (post_save)` | `structure.Project` | Process pending invitations and orders when a project's start date is unset. |
| `process_invoice_item` | `Django Signal (post_save)` | `invoices.InvoiceItem` | Process invoice item changes and update related price estimates. |
| `project_credit_changed_handler` | `Django Signal (post_save)` | `invoices.ProjectCredit` | No description |
| `project_estimated_cost_policy_trigger_handler` | `Django Signal (post_save)` | `invoices.InvoiceItem` | Evaluate project cost policies when invoice items are updated. |
| `refund_project_credit_on_project_removal` | `Django Signal (pre_delete)` | `structure.Project` | No description |
| `resource_has_been_changed` | `Django Signal (post_save)` | `marketplace.Resource` | Log resource changes. |
| `resource_options_have_been_changed` | `Django Signal (post_save)` | `marketplace.Resource` | Handle script execution when marketplace resource options are changed. |
| `resource_state_has_been_changed` | `Django Signal (post_save)` | `marketplace.Resource` | Handle resource state changes. |
| `run_reset_actions_upon_cost_policy_deletion` | `Django Signal (pre_delete)` | `policy.ProjectEstimatedCostPolicy` | Execute reset actions when a cost policy is deleted. |
| `send_comment_added_notification` | `Django Signal (post_save)` | `support.Comment` | No description |
| `send_course_account_deletion_info` | `Django Signal (post_save)` | `marketplace.CourseAccount` | No description |
| `send_course_account_info` | `Django Signal (post_save)` | `marketplace.CourseAccount` | No description |
| `send_done_order_to_message_queue` | `Django Signal (post_save)` | `marketplace.Order` | Send completed marketplace order to message queue for site agent processing. |
| `send_issue_updated_notification` | `Django Signal (post_save)` | `support.Issue` | No description |
| `send_offering_user_created_message` | `Django Signal (post_save)` | `marketplace.OfferingUser` | Send OfferingUser creation message to message queue for external systems. |
| `send_offering_user_deleted_message` | `Django Signal (post_delete)` | `marketplace.OfferingUser` | Send OfferingUser deletion message to message queue for external systems. |
| `send_offering_user_updated_message` | `Django Signal (post_save)` | `marketplace.OfferingUser` | Send OfferingUser update message to message queue for external systems. |
| `send_offering_user_username_message` | `Django Signal (post_save)` | `marketplace.OfferingUser` | No description |
| `send_pending_order_to_message_queue` | `Django Signal (post_save)` | `marketplace.Order` | Send pending marketplace order to message queue for site agent processing. |
| `send_project_service_account_deletion_info` | `Django Signal (post_save)` | `marketplace.ProjectServiceAccount` | No description |
| `send_project_service_account_info` | `Django Signal (post_save)` | `marketplace.ProjectServiceAccount` | No description |
| `send_resource_update_message_to_queue` | `Django Signal (post_save)` | `marketplace.Resource` | No description |
| `send_role_granted_message_to_queue` | `Custom Signal (role_granted)` | `—` | No description |
| `send_role_revoked_message_to_queue` | `Custom Signal (role_revoked)` | `—` | No description |
| `set_mtu_when_network_has_been_created` | `Django Signal (post_save)` | `openstack.Network` | No description |
| `set_project_name_on_invoice_item_creation` | `Django Signal (post_save)` | `invoices.InvoiceItem` | No description |
| `set_tax_percent_on_invoice_creation` | `Django Signal (pre_save)` | `invoices.Invoice` | No description |
| `switch_resource_plan_period_when_plan_is_updated` | `Django Signal (post_save)` | `marketplace.Resource` | Switch the resource plan period when a resource's plan is updated. |
| `sync_component_user_usage_when_allocation_user_usage_is_submitted` | `Django Signal (post_save)` | `waldur_slurm.AllocationUserUsage` | No description |
| `sync_limits` | `Django Signal (post_save)` | `marketplace.Resource` | Synchronize resource limits. |
| `sync_permission_with_remote` | `Custom Signal (role_granted)` | `—` | No description |
| `sync_permission_with_remote` | `Custom Signal (role_revoked)` | `—` | No description |
| `sync_permission_with_remote` | `Custom Signal (role_updated)` | `—` | No description |
| `sync_remote_project_when_request_is_approved` | `Django Signal (post_save)` | `marketplace_remote.ProjectUpdateRequest` | No description |
| `sync_resource_limit_when_order` | `Django Signal (post_save)` | `marketplace.Order` | Synchronize resource limits when an order is created. |
| `synchronize_directly_connected_ips` | `Django Signal (post_save)` | `openstack.Instance` | No description |
| `synchronize_floating_ips` | `Django Signal (post_save)` | `openstack.FloatingIP` | No description |
| `synchronize_floating_ips_on_delete` | `Django Signal (post_delete)` | `openstack.FloatingIP` | No description |
| `synchronize_instance_after_pull` | `Django Signal (post_save)` | `openstack.Instance` | No description |
| `synchronize_instance_hypervisor_hostname` | `Django Signal (post_save)` | `openstack.Instance` | No description |
| `synchronize_instance_name` | `Django Signal (post_save)` | `openstack.Instance` | No description |
| `synchronize_limits_when_storage_mode_is_switched` | `Django Signal (post_save)` | `marketplace.Offering` | No description |
| `synchronize_nic` | `Django Signal (post_save)` | `waldur_azure.NetworkInterface` | No description |
| `synchronize_ports` | `Django Signal (post_save)` | `openstack.Port` | No description |
| `synchronize_ports_on_delete` | `Django Signal (post_delete)` | `openstack.Port` | No description |
| `synchronize_public_ip` | `Django Signal (post_save)` | `waldur_azure.PublicIP` | No description |
| `synchronize_resource_metadata_on_delete` | `Django Signal (post_delete)` | `waldur_azure.VirtualMachine` | Synchronize resource metadata on delete. |
| `synchronize_resource_metadata_on_delete` | `Django Signal (post_delete)` | `waldur_azure.SQLServer` | Synchronize resource metadata on delete. |
| `synchronize_resource_metadata_on_delete` | `Django Signal (post_delete)` | `waldur_azure.SQLDatabase` | Synchronize resource metadata on delete. |
| `synchronize_resource_metadata_on_delete` | `Django Signal (post_delete)` | `openstack.Instance` | Synchronize resource metadata on delete. |
| `synchronize_resource_metadata_on_delete` | `Django Signal (post_delete)` | `openstack.Volume` | Synchronize resource metadata on delete. |
| `synchronize_resource_metadata_on_delete` | `Django Signal (post_delete)` | `openstack.Tenant` | Synchronize resource metadata on delete. |
| `synchronize_resource_metadata_on_delete` | `Django Signal (post_delete)` | `waldur_rancher.Cluster` | Synchronize resource metadata on delete. |
| `synchronize_resource_metadata_on_delete` | `Django Signal (post_delete)` | `waldur_slurm.Allocation` | Synchronize resource metadata on delete. |
| `synchronize_resource_metadata_on_delete` | `Django Signal (post_delete)` | `waldur_vmware.VirtualMachine` | Synchronize resource metadata on delete. |
| `synchronize_resource_metadata_on_save` | `Django Signal (post_save)` | `waldur_azure.VirtualMachine` | Synchronize resource metadata on save. |
| `synchronize_resource_metadata_on_save` | `Django Signal (post_save)` | `waldur_azure.SQLServer` | Synchronize resource metadata on save. |
| `synchronize_resource_metadata_on_save` | `Django Signal (post_save)` | `waldur_azure.SQLDatabase` | Synchronize resource metadata on save. |
| `synchronize_resource_metadata_on_save` | `Django Signal (post_save)` | `openstack.Instance` | Synchronize resource metadata on save. |
| `synchronize_resource_metadata_on_save` | `Django Signal (post_save)` | `openstack.Volume` | Synchronize resource metadata on save. |
| `synchronize_resource_metadata_on_save` | `Django Signal (post_save)` | `openstack.Tenant` | Synchronize resource metadata on save. |
| `synchronize_resource_metadata_on_save` | `Django Signal (post_save)` | `waldur_rancher.Cluster` | Synchronize resource metadata on save. |
| `synchronize_resource_metadata_on_save` | `Django Signal (post_save)` | `waldur_slurm.Allocation` | Synchronize resource metadata on save. |
| `synchronize_resource_metadata_on_save` | `Django Signal (post_save)` | `waldur_vmware.VirtualMachine` | Synchronize resource metadata on save. |
| `synchronize_router_backend_metadata` | `Django Signal (post_save)` | `openstack.Router` | No description |
| `synchronize_tenant_name` | `Django Signal (post_save)` | `openstack.Tenant` | No description |
| `synchronize_volume_metadata_on_pull` | `Custom Signal (resource_pulled)` | `openstack.Volume` | No description |
| `synchronize_volume_metadata_on_save` | `Django Signal (post_save)` | `openstack.Volume` | No description |
| `tenant_does_not_exist_in_backend` | `Custom Signal (tenant_does_not_exist_in_backend)` | `openstack.Tenant` | No description |
| `terminate_resource` | `Django Signal (pre_delete)` | `waldur_azure.VirtualMachine` | Terminate a resource. |
| `terminate_resource` | `Django Signal (pre_delete)` | `waldur_azure.SQLServer` | Terminate a resource. |
| `terminate_resource` | `Django Signal (pre_delete)` | `waldur_azure.SQLDatabase` | Terminate a resource. |
| `terminate_resource` | `Django Signal (pre_delete)` | `openstack.Instance` | Terminate a resource. |
| `terminate_resource` | `Django Signal (pre_delete)` | `openstack.Volume` | Terminate a resource. |
| `terminate_resource` | `Django Signal (pre_delete)` | `openstack.Tenant` | Terminate a resource. |
| `terminate_resource` | `Django Signal (pre_delete)` | `waldur_rancher.Cluster` | Terminate a resource. |
| `terminate_resource` | `Django Signal (pre_delete)` | `waldur_slurm.Allocation` | Terminate a resource. |
| `terminate_resource` | `Django Signal (pre_delete)` | `waldur_vmware.VirtualMachine` | Terminate a resource. |
| `trigger_order_callback` | `Django Signal (post_save)` | `marketplace.Order` | Trigger HTTP callback when marketplace order state changes. |
| `update_argocd_secret_when_resource_options_changed` | `Django Signal (post_save)` | `marketplace.Resource` | No description |
| `update_cache_when_invoice_item_is_deleted` | `Django Signal (post_delete)` | `invoices.InvoiceItem` | No description |
| `update_cache_when_invoice_item_is_updated` | `Django Signal (post_save)` | `invoices.InvoiceItem` | No description |
| `update_category_offerings_count` | `Custom Signal (recalculate_quotas)` | `—` | Update the count of offerings for each category. |
| `update_category_quota_when_offering_is_created` | `Django Signal (post_save)` | `marketplace.Offering` | Update category quota when an offering is created or its state changes. |
| `update_category_quota_when_offering_is_deleted` | `Django Signal (post_delete)` | `marketplace.Offering` | Update category quota when an offering is deleted. |
| `update_component_quota` | `Django Signal (post_save)` | `waldur_slurm.Allocation` | No description |
| `update_customer_of_offering_if_project_has_been_moved` | `Custom Signal (project_moved)` | `structure.Project` | Update the customer of an offering if the project has been moved. |
| `update_daily_quotas` | `Django Signal (post_save)` | `quotas.QuotaUsage` | No description |
| `update_estimate_when_invoice_is_created` | `Django Signal (post_save)` | `invoices.Invoice` | Update price estimates when new invoice is created for customer. |
| `update_floating_ip_external_addresses` | `Django Signal (post_save)` | `openstack.FloatingIP` | No description |
| `update_google_calendar_name_if_offering_name_has_been_changed` | `Django Signal (post_save)` | `marketplace.Offering` | No description |
| `update_instances_ip_external_addresses` | `Django Signal (post_save)` | `marketplace.Offering` | No description |
| `update_invoice_item_on_project_name_update` | `Django Signal (post_save)` | `structure.Project` | No description |
| `update_invoice_when_usage_is_reported` | `Django Signal (post_save)` | `marketplace.ComponentUsage` | Handles billing when component usage is reported, with integrated prepaid logic. |
| `update_maintenance_announcement_on_offering_change` | `Django Signal (post_save)` | `marketplace.MaintenanceAnnouncementOffering` | Update AdminAnnouncement when affected offerings change. |
| `update_maintenance_announcement_on_offering_change` | `Django Signal (post_delete)` | `marketplace.MaintenanceAnnouncementOffering` | Update AdminAnnouncement when affected offerings change. |
| `update_marketplace_resource_limits_when_vm_is_updated` | `Custom Signal (vm_updated)` | `—` | No description |
| `update_offering_user_username_after_freeipa_profile_update` | `Django Signal (post_save)` | `waldur_freeipa.Profile` | Update offering user usernames after FreeIPA profile update. |
| `update_offering_user_username_after_offering_settings_change` | `Django Signal (post_save)` | `marketplace.Offering` | Update offering user usernames after offering settings change. |
| `update_offering_user_username_after_user_change` | `Django Signal (post_save)` | `core.User` | Set new username for offering users after site_username in user details has been changed. |
| `update_openstack_tenant_usages` | `Django Signal (post_save)` | `quotas.QuotaUsage` | No description |
| `update_order_if_issue_was_complete` | `Django Signal (post_save)` | `support.Issue` | No description |
| `update_remote_resource_options` | `Django Signal (post_save)` | `marketplace.Resource` | No description |
| `update_resource_when_order_is_rejected_or_erred` | `Django Signal (post_save)` | `marketplace.Order` | Update resource state when an order is rejected or erred. |

## Application: `waldur_openstack`

| Handler Name | Signal Type | Sender | Description |
|--------------|-------------|--------|-------------|
| `add_instance_fields` | `Custom Signal (pre_serializer_fields)` | `OpenStackFloatingIPSerializer` | Add instance-related fields to the serializer. |
| `delete_state_service_properties` | `Django Signal (post_delete)` | `openstack.Tenant` | Delete state service properties. |
| `log_action` | `Django Signal (post_save)` | `openstack.Instance` | Log any resource action. |
| `log_action` | `Django Signal (post_save)` | `openstack.Volume` | Log any resource action. |
| `log_action` | `Django Signal (post_save)` | `openstack.Snapshot` | Log any resource action. |
| `log_network_cleaned` | `Django Signal (post_delete)` | `openstack.Network` | Log network cleanup. |
| `log_security_group_cleaned` | `Django Signal (post_delete)` | `openstack.SecurityGroup` | Log security group cleanup. |
| `log_security_group_rule_cleaned` | `Django Signal (post_delete)` | `openstack.SecurityGroupRule` | Log security group rule cleanup. |
| `log_server_group_cleaned` | `Django Signal (post_delete)` | `openstack.ServerGroup` | Log server group cleanup. |
| `log_subnet_cleaned` | `Django Signal (post_delete)` | `openstack.SubNet` | Log subnet cleanup. |
| `log_tenant_quota_update` | `Django Signal (post_save)` | `quotas.QuotaLimit` | Log tenant quota updates. |
| `remove_ssh_key_from_all_tenants_on_it_deletion` | `Django Signal (pre_delete)` | `core.SshPublicKey` | Delete key from all tenants that are accessible for user on key deletion. |
| `remove_ssh_key_from_tenants` | `Custom Signal (role_revoked)` | `—` | Delete user ssh keys from tenants that he does not have access now. |

## Application: `waldur_openstack_replication`

| Handler Name | Signal Type | Sender | Description |
|--------------|-------------|--------|-------------|
| `handle_migration_post_save` | `Django Signal (post_save)` | `waldur_openstack_replication.Migration` | Handle migration post-save events. |

## Application: `waldur_rancher`

| Handler Name | Signal Type | Sender | Description |
|--------------|-------------|--------|-------------|
| `add_group_to_rancher_scope` | `Django Signal (post_save)` | `waldur_rancher.KeycloakGroup` | Add a Keycloak group to Rancher scope. |
| `add_rancher_cluster_to_openstack_instance` | `Custom Signal (pre_serializer_fields)` | `OpenStackInstanceSerializer` | Add Rancher cluster information to OpenStack instance serializer. |
| `delete_catalog_if_scope_has_been_deleted` | `Django Signal (post_delete)` | `waldur_rancher.Project` | Delete a catalog if its scope has been deleted. |
| `delete_catalog_if_scope_has_been_deleted` | `Django Signal (post_delete)` | `waldur_rancher.Cluster` | Delete a catalog if its scope has been deleted. |
| `delete_catalog_if_scope_has_been_deleted` | `Django Signal (post_delete)` | `structure.ServiceSettings` | Delete a catalog if its scope has been deleted. |
| `delete_cluster_if_all_related_nodes_have_been_deleted` | `Django Signal (post_delete)` | `waldur_rancher.Node` | Delete a Rancher cluster if all its related nodes have been deleted. |
| `delete_keycloak_group_from_backend` | `Django Signal (post_delete)` | `waldur_rancher.KeycloakGroup` | Delete a Keycloak group from the backend. |
| `delete_keycloak_user_group_membership_from_backend` | `Django Signal (post_delete)` | `waldur_rancher.KeycloakUserGroupMembership` | Delete a Keycloak user group membership from the backend. |
| `delete_node_if_related_instance_has_been_deleted` | `Django Signal (post_delete)` | `openstack.Instance` | Delete a Rancher node if its related OpenStack instance has been deleted. |
| `remove_group_from_rancher_scope` | `Django Signal (post_delete)` | `waldur_rancher.KeycloakGroup` | Remove a Keycloak group from Rancher scope. |
| `set_error_state_for_cluster_if_related_node_deleting_is_failed` | `Django Signal (post_save)` | `waldur_rancher.Node` | Set error state for a Rancher cluster if a related node deletion fails. |
| `set_error_state_for_node_if_related_instance_deleting_is_failed` | `Django Signal (post_save)` | `openstack.Instance` | Set error state for a Rancher node if its related OpenStack instance deletion fails. |

## Application: `waldur_slurm`

| Handler Name | Signal Type | Sender | Description |
|--------------|-------------|--------|-------------|
| `process_role_granted` | `Custom Signal (role_granted)` | `—` | Process role granted events for FreeIPA synchronization. |
| `process_role_revoked` | `Custom Signal (role_revoked)` | `—` | Process role revoked events for FreeIPA synchronization. |
| `process_user_creation` | `Django Signal (post_save)` | `waldur_freeipa.Profile` | Process user creation for FreeIPA profiles. |
| `process_user_deletion` | `Django Signal (pre_delete)` | `waldur_freeipa.Profile` | Process user deletion for FreeIPA profiles. |
| `update_quotas_on_allocation_usage_update` | `Django Signal (post_save)` | `waldur_slurm.Allocation` | Update quotas on allocation usage update. |

## Application: `waldur_vmware`

| Handler Name | Signal Type | Sender | Description |
|--------------|-------------|--------|-------------|
| `update_vm_total_disk_when_disk_is_created_or_updated` | `Django Signal (post_save)` | `waldur_vmware.Disk` | Update VM total disk size when a disk is created or updated. |
| `update_vm_total_disk_when_disk_is_deleted` | `Django Signal (post_delete)` | `waldur_vmware.Disk` | Update VM total disk size when a disk is deleted. |


## Summary

Total unique handlers found: 646

- **waldur_auth_saml2**: 1 handlers
- **waldur_autoprovisioning**: 1 handlers
- **waldur_core**: 333 handlers
- **waldur_freeipa**: 12 handlers
- **waldur_lexis**: 1 handlers
- **waldur_mastermind**: 265 handlers
- **waldur_openstack**: 13 handlers
- **waldur_openstack_replication**: 1 handlers
- **waldur_rancher**: 12 handlers
- **waldur_slurm**: 5 handlers
- **waldur_vmware**: 2 handlers

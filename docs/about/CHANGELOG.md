# Changelog

## 8.0.7-rc.8 - 2026-03-18

### Highlights

This release candidate brings significant improvements to the AI Assistant, now compatible with the OpenAI API and capable of creating VMs directly from chat. Operators gain new quota usage notifications (75% and 100% thresholds), configurable reporting screens, and OpenStack port security controls. Numerous stability fixes address race conditions, N+1 query performance issues, and marketplace filter synchronization problems in the UI.

### What's New

- **AI Assistant now supports OpenAI-compatible API and VM creation.** Users can ask the assistant to create virtual machines, and operators can connect any OpenAI-compatible LLM provider.
- **Quota usage notifications at 75% and 100% thresholds.** Project owners and managers now receive email notifications when resource quota consumption reaches warning levels.
- **Configurable reporting screens.** Operators can enable or disable specific reporting views through Constance settings, tailoring the UI to their needs.
- **OpenStack port security controls.** Users can now toggle port security when creating instances or ports, with validation that prevents assigning security groups when port security is disabled.
- **Grace period visibility in the UI.** Project and resource APIs now expose grace period fields, and the frontend displays warning bars and improved date fields for projects approaching their end date.
- **Offering documentation and helpdesk URLs.** Service providers can now add documentation and helpdesk links to their offerings, visible on the public offering page.
- **Category structure editing.** Administrators can now edit marketplace category attributes and sections directly from the admin interface.
- **SCIM sync triggers on user state transitions and offering endpoint changes.** Identity provisioning stays in sync automatically when users become active or offering endpoints are modified.
- **Robot account search filters.** New filters make it easier to find and manage robot accounts in the marketplace.
- **Archive offering management command.** Operators can now archive offerings via CLI for bulk lifecycle management.

### Improvements

- **Replaced Cypress with Playwright for E2E testing.** The frontend test infrastructure has been modernized for faster, more reliable end-to-end tests.
- **Marketplace filter synchronization fixed.** Sidebar and toolbar filters now stay in sync correctly, including when removing individual filters or when no organization is selected.
- **Multiple N+1 query fixes.** The course accounts endpoint, service provider users endpoint, and constance settings queries are now properly optimized.
- **SLURM policy period enforcement.** Policy periods are now validated against offering component limit periods, and the preview impact endpoint respects the period setting.
- **Remote offering invoices calculated locally.** Invoice calculation for remote offerings no longer requires pulling data from remote endpoints, improving reliability.
- **Kubernetes resource cleanup for marketplace scripts.** Script-based offerings now properly clean up K8s resources, and the job timeout setting is correctly applied.
- **STOMP notifications enabled for offering consumers.** Consumer-side integrations now receive real-time event notifications.
- **Improved Lithuanian and Estonian translations.**
- **Table UI polish.** Toolbar button sizes are now consistent, and expandable table rows have improved alignment.
- **Added `data-testid` attributes across many UI components** to support automated E2E testing.
- **Added `created_before` and `modified_before` API filters** for more flexible date-range queries.
- **Squashed database migrations** to speed up fresh database setup and E2E test runs.

### Bug Fixes

- **Fixed STOMP circuit breaker never recovering from OPEN state.**
- **Fixed Gunicorn worker timeout when creating offering users** by deferring the operation to Celery.
- **Fixed race condition in offering user creation** that caused duplicate entries.
- **Fixed duplicate key error when importing offering users** with existing (offering, user) pairs.
- **Fixed transaction cascading failures in the `import_structure` command.**
- **Fixed crash in checklist template endpoint** when questions have dependencies.
- **Fixed crash when deleting ERRED course accounts** with no associated user.
- **Fixed IntegrityError when creating course accounts** with existing usernames.
- **Fixed Nova flavor data retrieval** by using microversion 2.47.
- **Fixed URLs with trailing slashes causing 404 errors** in the frontend router.
- **Fixed admin panel logout button.**
- **Fixed navigation to Terms of Service and Privacy pages** for users with incomplete profiles.
- **Fixed measured units display** for OpenStack tenant resource components.
- **Fixed Kubernetes backend fallback** to in-cluster config when kubeconfig is invalid.
- **Exposed identity bridge fields on own user profile.**
- **Docker Compose: upgraded Keycloak setup** and made it optional via Docker profile; removed deprecated FirecREST example configuration.

### Core Component Activity

- **Waldur Mastermind**: [61 commits](https://github.com/waldur/waldur-mastermind/compare/8.0.6...8.0.7-rc.8) - AI Assistant OpenAI compatibility, quota notifications, port security, grace period API, SCIM sync improvements, and numerous stability fixes.
- **Waldur Homeport**: [36 commits](https://github.com/waldur/waldur-homeport/compare/8.0.6...8.0.7-rc.8) - Grace period UI, port security toggle, reporting screen toggles, Playwright migration, marketplace filter fixes, and E2E testability improvements.
- **Waldur Helm**: [9 commits](https://github.com/waldur/waldur-helm/compare/8.0.6...8.0.7-rc.8) - Version bumps and documentation updates.
- **Waldur Docker Compose**: [9 commits](https://github.com/waldur/waldur-docker-compose/compare/8.0.6...8.0.7-rc.8) - Keycloak upgrade, deprecated FirecREST config removal, and version bumps.

---














## 8.0.6 - 2026-03-06

### Highlights

This release delivers major API performance improvements by fixing numerous N+1 query issues across key endpoints, significantly reducing response times for large deployments. OpenStack gains Load Balancer as a Service (LBaaS) support and Application Credentials authentication, while the AI Assistant is hardened with sensitive data detection and injection prevention. Operators also get new feature flags for fine-grained UI visibility control and improved billing credit handling.

### What's New

- **OpenStack Load Balancer as a Service (LBaaS).** Backend support for managing load balancers via the OpenStack Octavia API.
- **OpenStack Application Credentials authentication.** Operators can now connect OpenStack services using application credentials instead of username/password.
- **OpenStack instances reporting page.** Staff users can view aggregate statistics and details for all OpenStack instances from a dedicated reporting page.
- **AI Assistant sensitive data detection.** Chat input is now scanned for PII, credentials, and injection attempts before being sent to the AI model, with warnings displayed to users.
- **GPU architecture fields for software catalogs and partitions.** Software targets and offering partitions now track GPU architectures, with filtering support in the UI.
- **Software catalog: multiple parent packages.** Software extensions can now be linked to multiple parent packages instead of just one.
- **Staff user creation and password management.** Staff users can now create and edit user accounts with password management through a step-by-step wizard.
- **SLURM policy force-period-reset.** Staff can manually trigger a period reset for SLURM usage policies via a new API action.
- **SSH key change notifications.** Optionally create support tickets when users add or remove SSH keys, configurable via Constance settings.
- **SSH key type restrictions.** Operators can restrict which SSH key types (RSA, ED25519, etc.) are accepted, with the UI showing restrictions before import.
- **Feature flags for UI visibility.** New toggles to conceal audit logs from end users, hide resource metadata, and restrict marketplace access to staff.
- **Quarterly usage aggregation.** Resource usage can now be aggregated by quarter in addition to monthly and total periods.
- **Table growth monitoring UI.** Administrators can view database table growth trends and trigger manual samples from a new settings page.
- **Visual login layout selector.** Administrators can preview and select login page layouts from a visual picker in settings.
- **Offering user auto-deletion option.** New plugin option to automatically delete offering users when they are removed, with sync restoration support.
- **Identity management improvements.** ISD managers can create agent identities without offering users, and identity managers can list offering users scoped by ISD overlap.

### Improvements

- **Extensive N+1 query fixes.** Resolved N+1 queries on project list, project list_users, customer projects, robot accounts, service provider project_permissions, component usage, marketplace orders, and stats endpoints.
- **Django upgraded to 6.0.2.** The backend framework has been updated from Django 5.2 to 6.0.2.
- **Structured logging migration.** Mastermind now uses structlog for consistent JSON-formatted logs across API, Celery, and Django request loggers.
- **Bulk course account creation moved to background tasks.** Large CSV uploads no longer time out — processing happens asynchronously.
- **Token refresh DB load reduced.** An adaptive debounce interval prevents excessive database writes during token refreshes.
- **Migration squashing.** 60 migration steps consolidated across 5 apps, speeding up fresh database setup and CI runs.
- **Locale-aware number formatting.** Usage and quota displays now format numbers according to the user's locale.
- **Footer redesign.** Application footer links have been consolidated and redesigned for better organization.
- **Table toolbar alignment.** Search, filters, and action buttons are now consistently aligned in table toolbars.
- **Filter migration to generator.** Multiple batches of hand-written table filters replaced with auto-generated versions for consistency.
- **Offering managers can set order states.** Expanding self-service capabilities for service providers.
- **Invitation text extended to 2000 characters.** Longer custom messages can now be included in invitations.
- **Marketplace resource pull action exposed.** Users can now trigger resource sync from the UI for OpenStack instances, tenants, and volumes.
- **Helm chart supports image digest pulling.** Deployments can now pin images by digest for reproducibility.
- **Dependencies bumped** to address known security vulnerabilities in both Python and npm packages.

### Bug Fixes

- Fixed expired project credits not being zeroed and excluded from linear consumption calculations.
- Fixed duplicate role creation when group invitations are auto-approved.
- Fixed 500 error when `X-Forwarded-For` header contains a hostname instead of an IP address.
- Fixed invalid auth state handling during social authentication flows.
- Fixed resource duplication check incorrectly preventing all resource creation in remote marketplace.
- Fixed corrupt NULL constance values crashing the settings endpoint.
- Fixed GLAuth uidnumber generation to be scoped per offering instead of globally.
- Fixed synchronous subtask call in SLURM policy evaluation causing Celery issues.
- Fixed order unlink AttributeError by relocating `get_order_scopes` to the log module.
- Fixed Atlassian support backend TypeError in `pull_request_types`.
- Fixed image name parsing/grouping and increased flavor page size in instance deployment.
- Fixed resource component quota display showing incorrect units and layout.
- Fixed order details showing pricing when billing info is concealed.
- Fixed stale "No association" warning after auto-approved group invitation.
- Fixed various translation issues across Estonian, Lithuanian, and German locales.

### Core Component Activity

- **Waldur Mastermind**: [92 commits](https://github.com/waldur/waldur-mastermind/compare/8.0.5...8.0.6) - LBaaS backend, N+1 fixes, AI assistant hardening, Django 6.0, structured logging, SLURM policy reset, SSH key management
- **Waldur Homeport**: [56 commits](https://github.com/waldur/waldur-homeport/compare/8.0.5...8.0.6) - OpenStack reporting page, user management wizard, sensitive data detection UI, filter generator migration, footer redesign, feature flag support
- **Waldur Helm**: [9 commits](https://github.com/waldur/waldur-helm/compare/8.0.5...8.0.6) - Docker image digest support, helm-unittest migration
- **Waldur Docker Compose**: [4 commits](https://github.com/waldur/waldur-docker-compose/compare/8.0.5...8.0.6) - Maintenance updates only

### Resources

- [OpenAPI Schema](../API/waldur-openapi-schema-8.0.6.yaml)

---






## 8.0.5 - 2026-02-23

This release strengthens AI Assistant security with prompt injection detection, introduces a hypervisor placement map for OpenStack instances, and adds configurable resource naming patterns for offerings. Operators benefit from several reliability fixes addressing webhook race conditions, Keycloak migration conflicts on upgrades, and billing calculation accuracy for total-period limits.

### What's New

- **Prompt injection detection for AI Assistant.** Incoming messages are now scanned against configurable regex patterns and scored for injection risk. Flagged messages are logged with severity and categories, and administrators can review detection events in the support logs.
- **Hypervisor placement map.** OpenStack tenant instance lists now include a visual placement map showing VM-to-hypervisor distribution, with batch action support for selecting multiple instances.
- **Configurable resource naming patterns.** Offering managers can define naming patterns for the suggest-name endpoint, and suggested names now use hyphens instead of underscores for consistency.
- **Cost breakdown dialog.** Project dashboards now include a detailed cost breakdown dialog showing per-resource rates and usage for the current billing period.
- **Font family selection in branding.** Administrators can choose a custom font family in the theme settings to match organizational branding.
- **Bulk user usage submission.** A new API endpoint allows submitting usage data for multiple users in a single request.
- **OpenStack cloud demo preset.** A new demo preset is available for quickly bootstrapping an OpenStack cloud offering with backend model support.

### Improvements

- Constance settings now support generic enum and multi-select field types in both the backend API and the administration UI.
- Table filter components across the frontend have been migrated to auto-generated components based on the OpenAPI specification, improving consistency and reducing manual maintenance.
- Resource action options are now sorted alphabetically by label.
- Branding configuration modals have been adjusted to a more appropriate size.
- Question mapping fields are now required when configuring onboarding checklists.
- Resource component usage rendering has been refined with clearer limit-period display logic.
- MQTT protocol support has been removed from the Helm chart RabbitMQ configuration, simplifying the messaging setup.

### Bug Fixes

- Fixed EESSI software catalog versions being incorrectly mixed across different catalogs.
- Fixed a webhook dispatch race condition in the event emit handler that could cause missed or duplicate notifications.
- Fixed Keycloak migration conflicts that caused `InconsistentMigrationHistory` errors on databases upgraded from older releases, and made the initial migration idempotent.
- Fixed AI Assistant returning HTTP 400 errors when regenerating or editing responses with chat storage disabled.
- Fixed billing calculation for TOTAL limit period resources that was incorrectly multiplied by the number of days.
- Fixed N+1 query performance issues in course accounts and support comments endpoints.
- Fixed pricing information showing in organization and project cards when the organization has cost display disabled.
- Added missing Lithuanian translations for order metadata labels.
- Fixed remote eduteams configuration and HAproxy redirect annotation in the Helm chart.

### Core Component Activity

- **Waldur Mastermind**: [23 commits](https://github.com/waldur/waldur-mastermind/compare/8.0.4...8.0.5) - injection detection, configurable naming patterns, billing fixes, migration safety improvements.
- **Waldur Homeport**: [24 commits](https://github.com/waldur/waldur-homeport/compare/8.0.4...8.0.5) - placement map, cost breakdown UI, filter generation migration, branding improvements.
- **Waldur Helm**: [3 commits](https://github.com/waldur/waldur-helm/compare/8.0.4...8.0.5) - MQTT removal, eduteams and HAproxy fixes.

### Resources

- [OpenAPI Schema](https://raw.githubusercontent.com/waldur/api-docs/main/docs/API/waldur-openapi-schema-8.0.5.yaml)
- [API Changes](https://api-docs.waldur.com/latest/integrator-guide/APIs/api-changes/waldur-openapi-schema-8.0.5-diff)

---

## 8.0.4 - 2026-02-19

This release introduces Keycloak-based user role management for marketplace offerings, full OpenStack server group policy support, and a new system for auto-generating UI table filters from the OpenAPI schema. Several reliability fixes address invoice proration, resource state transitions, and mobile UI regressions.

### What's New

- **Keycloak user role management.** A new `waldur_keycloak` plugin enables service providers to manage Keycloak group memberships directly from offering settings, including importing remote groups, assigning memberships, and sending notification emails. The frontend provides a full management UI with bulk actions.
- **OpenStack server group policies.** All OpenStack server group policies (affinity, anti-affinity, soft variants) are now supported. Users can create server groups and assign instances to them during deployment via a new scheduling step.
- **AI assistant chat logs.** Support staff can now view AI assistant conversation logs in the support view, with expandable rows showing full chat history. Chat context retrieval has been moved server-side for better reliability.
- **OpenAPI-driven filter generation.** Table filters can now be auto-generated from the OpenAPI specification, ensuring frontend filters stay in sync with backend query parameters. Several list views have been migrated to this approach.
- **User profile completeness tracking.** Service providers can now filter offering users by profile attribute completeness and see field-level warnings. End users see a banner on resource pages when their profile is incomplete.

### Improvements

- **Django upgraded from 4.2 to 5.2.** The backend framework has been updated to the latest LTS release.
- **MQTT protocol support removed.** Message delivery now uses STOMP exclusively, simplifying RabbitMQ configuration across Helm and Docker Compose deployments.
- **Configurable UI font family.** Administrators can now select the portal font via a new `FONT_FAMILY` setting.
- **Sidebar "Match theme" style option.** A new sidebar appearance option automatically matches the current theme colors.
- **Onboarding setup view redesigned.** The admin onboarding question management interface has been refreshed with improved layout.
- **Permission deletion by type.** User affiliation actions now support bulk and row-level permission removal based on permission type.
- **Software package API filters.** New `name_exact` and `is_extension` filters added for more precise software package lookups.
- **OpenAPI schema quality improvements.** View names and operation IDs are now exposed on UUID/URL filter fields, optional request bodies are marked correctly for SDK generators, and a naming collision detector prevents Go SDK build failures.
- **Resource limit validation.** The `update_limits` endpoint now validates min/max bounds before accepting changes.
- **Auto-create default VM/Volume categories.** OpenStack resource import automatically creates marketplace categories when they do not exist.
- **Disclaimer area reordered.** The footer disclaimer now shows text before the logo with increased spacing.
- **Removed unused SITE_LOGO setting.** The deprecated constance setting has been cleaned up from backend and frontend.
- **Header cleanup.** Removed duplicate page title and extra search input from the navigation header.
- **Updated Lithuanian translation** for the sign-in label.

### Bug Fixes

- Fixed `MultipleObjectsReturned` error in usage reporting caused by duplicate `ComponentUsage` records, including a migration to deduplicate existing data.
- Fixed resources getting stuck in "Updating" state after a successful plan switch.
- Fixed quarterly limit change invoice quantity proration calculating incorrect amounts.
- Fixed `Customer.get_owners` raising `AttributeError` and deduplicated usage policy notifications.
- Fixed OpenStack instance image name not being detected during resource pull.
- Fixed mobile table filters not opening the sidebar drawer due to a missing context action.
- Fixed pricing information being visible when billing info is configured to be concealed.
- Fixed `null` `date_created` in the offering revision backfill migration.
- Fixed remote eduteams configuration and HAProxy redirect annotation in Helm charts.
- Fixed docker-logger permission denied error on `docker.sock` in Docker Compose setup.

### Core Component Activity

- **Waldur Mastermind**: [38 commits](https://github.com/waldur/waldur-mastermind/compare/8.0.3...8.0.4) - Keycloak plugin, Django 5.2 upgrade, OpenAPI improvements, billing and state fixes
- **Waldur Homeport**: [24 commits](https://github.com/waldur/waldur-homeport/compare/8.0.3...8.0.4) - Keycloak UI, server groups UI, filter generation, profile completeness, mobile fix
- **Waldur Helm**: [3 commits](https://github.com/waldur/waldur-helm/compare/8.0.3...8.0.4) - MQTT removal, eduteams and HAProxy fixes
- **Waldur Docker Compose**: [3 commits](https://github.com/waldur/waldur-docker-compose/compare/8.0.3...8.0.4) - MQTT removal, docker-logger fix

### Resources

- [OpenAPI Schema](https://raw.githubusercontent.com/waldur/api-docs/main/docs/API/waldur-openapi-schema-8.0.4.yaml)
- [API Changes](https://api-docs.waldur.com/latest/integrator-guide/APIs/api-changes/waldur-openapi-schema-8.0.4-diff)

---

## 8.0.3 - 2026-02-15

This release introduces two-way messaging between providers and consumers on pending orders, a new Identity Bridge API for push-based user attribute synchronization, and a system logs view for administrators. Multiple N+1 query fixes significantly improve API performance on key endpoints, and new feature toggles give operators finer control over marketplace visibility and offering lifecycle management.

### What's New

- **Two-way provider-consumer messaging on pending orders.** Providers and consumers can now exchange messages while an order is pending review, with email notifications for both sides. This allows clarifying order details without rejecting and re-submitting.
- **Identity Bridge API.** A new push-based API enables external identity services to synchronize user profile attributes (organization, registry code) into Waldur without polling.
- **System logs view.** Administrators can now view and filter recent Mastermind system logs directly from the admin panel and support view.
- **Order rejection comments.** When rejecting an order, both providers and consumers can now include a reason, which is shown in the order details.
- **Provider approval with option modification.** Service providers can review and modify resource options when approving an order via a dedicated approval dialog.
- **Renewal cost breakdown.** The resource renewal flow now shows a detailed cost estimate via a new `estimate_renewal` API endpoint before the user confirms.
- **Offering-level backend_id validation rules.** Operators can configure regex-based validation patterns for backend IDs on a per-offering basis.
- **Configurable disclaimer area.** A new footer disclaimer area can display a custom logo and text, controlled via feature toggle and branding settings.
- **Group invitation custom text.** Group invitations now support a custom welcome message, and the creator is hidden on public invitation pages.

### Improvements

- **Service provider offering lifecycle controls.** New configuration options allow operators to gate offering activation, pausing, and archival to service providers via feature flags, including restricting deletion of offerings with active resources.
- **Organization visibility controls.** New feature toggles allow hiding organization-level information from project-level members and disabling the marketplace UI for end users.
- **Permission-aware resource actions.** Frontend resource actions (terminate, change plan, change limits, etc.) are now hidden from users who lack the required permissions, with improved tooltips explaining why actions are unavailable.
- **OIDC email-based failover matching.** When the primary OIDC identifier is missing, Waldur can fall back to email-based user matching.
- **Organization registry code on user profile.** User profiles now include an organization registry code field, synced from identity providers and exposed in the Order API.
- **Duplicate invitation detection.** The invitation form now warns creators when a duplicate invitation already exists for the same email.
- **Onboarding checklist setup.** Administrators have an improved onboarding question management interface with predefined templates and better filtering.
- **Customer detail data scoped to visible projects.** Customer API responses now only include projects visible to the requesting user, and GDPR name filtering now covers all name fields.
- **Service providers can set resource state to OK** to manually recover resources, and SLURM policies are re-evaluated when limits increase on downscaled resources.
- **eduTEAMS refresh token rotation moved to Celery Beat** for improved reliability as a periodic task.
- **Removed legacy django-admin-tools** and django-fluent-dashboard dependencies.
- **Cache-based background task locking** replaces equality-check deduplication for improved reliability.
- **Billing info concealment** now respected in change limits, change plan, and renewal dialogs.
- **Helm chart improvements.** Added secret support for kubeconfig and DataCite password, stomp ingress whitelist configuration, and invoice finalization grace period setting.
- **Lithuanian translations updated** across user profile, invitations, terms of service, and organization fields.

### Bug Fixes

- Fixed N+1 query issues on public offerings, service provider, usage task, and users list endpoints by adding caching and optimized prefetching.
- Fixed cost policy being bypassed for the first resource allocation.
- Fixed Arrow vendor offering mapping serializer not accepting UUIDs, with updated frontend to match.
- Fixed login redirect failing when the auth token is expired.
- Fixed infinite re-render crash when opening drawers on the Resources tab.
- Fixed offering filter not syncing correctly to the URL.
- Fixed pricing display for daily-billed offerings showing incorrect amounts.
- Fixed fractional values being rounded in resource component usage display.
- Fixed ECharts crash when chart container is null after component unmount.
- Fixed FreeIPA existing key handling and UVK ingress path type in Helm chart.

### Core Component Activity

- **Waldur Mastermind**: [59 commits](https://github.com/waldur/waldur-mastermind/compare/8.0.2...8.0.3) - Provider-consumer messaging, Identity Bridge API, system logs, N+1 fixes, offering lifecycle controls
- **Waldur Homeport**: [70 commits](https://github.com/waldur/waldur-homeport/compare/8.0.2...8.0.3) - Messaging UI, system logs view, rejection comments, permission-aware actions, billing display fixes
- **Waldur Helm**: [10 commits](https://github.com/waldur/waldur-helm/compare/8.0.2...8.0.3) - Secret support for kubeconfig and DataCite, FreeIPA fix, invoice finalization grace period
- **Waldur Docker Compose**: [1 commit](https://github.com/waldur/waldur-docker-compose/compare/8.0.2...8.0.3) - Maintenance updates only

### Resources

- [OpenAPI Schema](https://raw.githubusercontent.com/waldur/api-docs/main/docs/API/waldur-openapi-schema-8.0.3.yaml)
- [API Changes](https://api-docs.waldur.com/latest/integrator-guide/APIs/api-changes/waldur-openapi-schema-8.0.3-diff)

---

## 8.0.2 - 2026-02-05

### Highlights

This release introduces an invoice finalization grace period, giving operators a configurable window to adjust invoices before they become final. Marketplace offering owners can now disable specific resource actions per offering, providing fine-grained control over what end users can do. OpenStack infrastructure discovery and software catalog management have been significantly improved with new admin tooling and a guided setup wizard.

### What's New

- **Invoice finalization grace period.** Invoices now enter a "pending finalization" state before becoming final, allowing operators a configurable window to make adjustments. Usage updates on already-finalized invoices are now properly rejected.
- **Disableable resource actions per offering.** Offering owners can now selectively disable specific resource actions (e.g., terminate, change limits, move, synchronize, report usage, and more). Only staff users can modify these settings.
- **OpenStack infrastructure discovery.** A new discovery wizard helps operators configure OpenStack offerings by auto-detecting available infrastructure, including external network support with dedicated models and API endpoints.
- **AI assistant chat session management.** Backend support for logging, persisting, and managing AI assistant chat sessions, including role-based access control and automatic cleanup.
- **Software catalog administration.** New admin UI for managing software catalogs with discovery capabilities, plus management commands for exporting, importing, and cleaning up software catalog structures. Catalog loading is now safer with improved validation.
- **Project move permissions expanded.** Organization owners in both the source and target organizations can now move projects between them.
- **Separate customer contact update permission.** A new `CUSTOMER_CONTACT_UPDATE` permission allows delegating contact information management without granting broader customer editing rights.
- **Event logs for deleted verifications.** Verification deletion events are now logged for audit trail purposes.

### Improvements

- **Version history API reliability.** Fixed empty results for newly created objects and backfilled initial version history entries for existing resources.
- **SCIM entitlements refactored** to use offering user usernames, improving compatibility with identity providers.
- **Customer list filtering** extended with additional filter options.
- **Registration method** is now exposed in the offering serializer by default.
- **Resource options validation** now checks for pending orders before allowing updates.

### Bug Fixes

- Fixed SLURM QoS not updating correctly when downscaling allocations, with improved policy warning display when the site agent queue is misconfigured.
- Fixed N+1 query performance issue on the marketplace orders list endpoint.
- Fixed quarterly and annual billing limit changes creating duplicate invoice items.
- Fixed invoice generation for annual billing periods.
- Fixed TypeError when saving date values in offering plugin_options.
- Fixed nullable partition field in software catalog serializer for SDK compatibility.
- Fixed undefined variable exception in OpenStack backend.
- Added debounce to global search to prevent rate limit errors on fast typing.
- Fixed AI assistant token usage column showing in user list when the feature is disabled.
- Fixed select field rendering in offering edit panel.
- Fixed confirmation dialog input type for onboarding justification actions.
- Fixed invitation translation strings.

### Core Component Activity

- **Waldur Mastermind**: [30 commits](https://github.com/waldur/waldur-mastermind/compare/8.0.1...8.0.2) - Invoice grace period, disableable actions, OpenStack discovery, AI chat management, software catalog tooling, billing and permission fixes.
- **Waldur Homeport**: [17 commits](https://github.com/waldur/waldur-homeport/compare/8.0.1...8.0.2) - Disableable actions UI, invoice state support, OpenStack discovery wizard, software catalog admin UI, search and rendering fixes.
- **Waldur Helm**: [2 commits](https://github.com/waldur/waldur-helm/compare/8.0.1...8.0.2) - Maintenance updates and CI fix for homeport tag setting.
- **Waldur Docker Compose**: [1 commit](https://github.com/waldur/waldur-docker-compose/compare/8.0.1...8.0.2) - Maintenance updates only.

### Resources

- [OpenAPI Schema](https://raw.githubusercontent.com/waldur/api-docs/main/docs/API/waldur-openapi-schema-8.0.2.yaml)
- [API Changes](https://api-docs.waldur.com/latest/integrator-guide/APIs/api-changes/waldur-openapi-schema-8.0.2-diff)

---

## 8.0.1 - 2026-02-03

### Highlights

Waldur 8.0.1 is a major release that introduces Arrow accounting integration for automated license and consumption billing, a comprehensive analytics and reporting suite covering orders, users, provisioning, and resource geography, and a revamped SLURM policy management experience with visual previews and execution logging. Operators gain new tools for database growth monitoring, OIDC identity provider discovery, SCIM user synchronization, and event subscription queues for real-time integrations.

### What's New

- **Arrow accounting integration.** New module for syncing resources, consumption records, and billing data from Arrow, with a full management dashboard including customer mappings, vendor offering mappings, and import wizards.
- **Analytics and reporting suite.** Added reporting pages for orders, user demographics, provisioning statistics, resource geography, usage trends, usage by organization type, project classification, offering costs, maintenance operations, and provider-level analytics.
- **SLURM policy visualization and logging.** SLURM usage policies now include a visual preview, execution log viewer, status summary, and on-demand policy evaluation from the offering management page.
- **OIDC discovery.** Administrators can now configure identity providers via OpenID Connect discovery, with a guided wizard that auto-discovers endpoints and claim mappings.
- **SCIM synchronization.** Initial support for synchronizing user data to external systems via the SCIM protocol.
- **Event subscription queues.** New SubscriptionQueue model enables external systems to subscribe to Waldur events and consume them via a pull-based API.
- **Resource version history.** Resources now track changes via django-reversion, with a timeline UI showing diffs between versions.
- **Offering tag management.** Offerings can be tagged and filtered by tags across the marketplace, with a dedicated admin interface for managing tags.
- **Database table growth monitoring.** New scheduled task tracks table sizes over time with configurable alerts when growth exceeds thresholds, visible in the administration panel.
- **AI assistant usage accounting.** Token consumption by the AI assistant is now tracked per user with configurable quotas, plus an LLM validation management command for quality assurance.
- **Storage folder manager.** Initial skeleton for a new storage folder manager offering option type.
- **Project digest notifications.** Project members can now receive periodic digest emails summarizing team activity, resource usage, and upcoming end dates.

### Improvements

- **Extended user profile attributes.** Users now have fields for country of residence, eduPerson assurance level, nationality, and affiliations parsed from AAI attributes. Administrators can define mandatory profile attributes that users must complete before accessing the platform.
- **Offering visibility modes.** Marketplace offerings can be configured with visibility modes to control which users can see them.
- **Cross-field validators for offering options.** Marketplace offering options now support greater-than, greater-than-or-equal, less-than, and less-than-or-equal validators with cross-field references.
- **Editable pending orders.** Users with approval permissions can now update limits, attributes, and start date on pending orders.
- **Subscription renewal minimum set to 12 months.** The minimum extension period for allocation renewals has been increased from 1 to 12 months.
- **Staff-only set_erred and set_ok actions.** Staff users can now manually transition resources and routers to erred or OK states for troubleshooting.
- **Conditional checklist questions.** Onboarding checklists now support conditional question logic based on previous answers.
- **Support users can manage announcements.** The admin announcements feature is now accessible to support-role users.
- **OpenStack duplicate image handling.** When duplicate image names are retrieved from OpenStack, only the most recently created image is used.
- **Service providers can update OpenStack quotas.** OpenStack tenant quotas can now be updated by the service provider role.
- **Offering pricing tab toggle.** A new feature flag allows hiding the pricing tab on offerings.
- **Unified wizard components.** Wizard dialogs across the application now share a consistent step indicator and layout.
- **Improved pending invitations display.** The user dashboard shows invitations in a more compact format with expiry badges.
- **Onboarding address fetching.** Estonian and Austrian business registry validation now automatically fetches company address data.
- **Improved translations.** Updated localization files for 23 languages.

### Bug Fixes

- Fixed a TransitionNotAllowed error when saving an OfferingUser in DELETED state.
- Fixed RabbitMQ host resolution in the Docker Compose init script that was overwriting pre-set host values.
- Fixed OpenStack network and subnet creation to use non-bulk API calls for better compatibility.
- Fixed group invitation token handling during OAuth login flow.
- Fixed one-time component price calculation returning incorrect values for zero quotas.
- Fixed marketplace script pull and options handler in Kubernetes mode.
- Fixed a 500 error when requesting specific fields via the API.
- Fixed anonymous user filtering by organization in the marketplace.
- Fixed missing pagination on the support page offering users list.
- Fixed the Enter key triggering form submission in search filter bars.
- Fixed the edit end date dialog sizing when many resources are affected.
- Normalized country codes to uppercase when parsing schacPersonalUniqueID attributes.

### Core Component Activity

- **Waldur Mastermind**: [98 commits](https://github.com/waldur/waldur-mastermind/compare/7.9.8...8.0.1) - Arrow integration, SLURM policy overhaul, extended user attributes, reporting endpoints, OIDC discovery, SCIM sync, event subscription queues, resource history API, offering tags, DB growth monitoring
- **Waldur Homeport**: [83 commits](https://github.com/waldur/waldur-homeport/compare/7.9.8...8.0.1) - Arrow management dashboard, comprehensive reporting suite, SLURM policy visualization, OIDC discovery wizard, version history UI, offering tags UI, user profile rework, wizard unification
- **Waldur Helm**: [2 commits](https://github.com/waldur/waldur-helm/compare/7.9.8...8.0.1) - maintenance updates only
- **Waldur Docker Compose**: [2 commits](https://github.com/waldur/waldur-docker-compose/compare/7.9.8...8.0.1) - maintenance updates only

### Resources

- [OpenAPI Schema](https://raw.githubusercontent.com/waldur/api-docs/main/docs/API/waldur-openapi-schema-8.0.1.yaml)
- [API Changes](https://api-docs.waldur.com/latest/integrator-guide/APIs/api-changes/waldur-openapi-schema-8.0.1-diff)

---

## 7.9.8 - 2026-01-21

### Release Summary

- **Release Impact:** Minor release with configuration and documentation updates

### Core Component Activity

- **Waldur Mastermind**: No changes
- **Waldur Homeport**: No changes
- **Waldur Helm**: No changes
- **Waldur Docker Compose**: No changes
- **Waldur Prometheus Exporter**: No changes

### Resources

<!-- - [OpenAPI Schema](../API/waldur-openapi-schema-7.9.8.yaml) -->
<!-- - [API Changes](../integrator-guide/APIs/api-changes/waldur-openapi-schema-7.9.8-diff.md) -->


## 7.9.7 - 2026-01-17

### Release Summary

- **Release Impact:** Minor release with configuration and documentation updates
- **SDK Updates:** 3 auto-generated clients updated

### Core Component Activity

- **Waldur Mastermind**: No changes
- **Waldur Homeport**: No changes
- **Waldur Helm**: No changes
- **Waldur Docker Compose**: No changes
- **Waldur Prometheus Exporter**: No changes

### SDK Updates (Auto-generated)

- **Python Client**: [12 commits](https://github.com/waldur/py-client/compare/7.9.6...7.9.7)
- **JavaScript Client**: [23 commits](https://github.com/waldur/js-client/compare/7.9.6...7.9.7)
- **Go Client**: [11 commits](https://github.com/waldur/go-client/compare/7.9.6...7.9.7)

### Py Client Highlights

- Release: bump version to 7.9.7.
- Update Waldur Python SDK.
- Update Waldur Python SDK.

### Js Client Highlights

- Release: bump version to 7.9.7.
- 7.9.7-dev.10.
- Update Waldur TypeScript SDK.

### Go Client Highlights

- Update Waldur Go SDK.
- Update Waldur Go SDK.
- Update Waldur Go SDK.

<!-- ### Resources

- [OpenAPI Schema](../API/waldur-openapi-schema-7.9.7.yaml)
- [API Changes](../integrator-guide/APIs/api-changes/waldur-openapi-schema-7.9.7-diff.md) -->


## 7.9.6 - 2026-01-07

### Release Summary

- **Release Impact:** Minor release with configuration and documentation updates
- **SDK Updates:** 3 auto-generated clients updated

### Core Component Activity

- **Waldur Mastermind**: No changes
- **Waldur Homeport**: No changes
- **Waldur Helm**: No changes
- **Waldur Docker Compose**: No changes
- **Waldur Prometheus Exporter**: No changes

### SDK Updates (Auto-generated)

- **Python Client**: [25 commits](https://github.com/waldur/py-client/compare/7.9.5...7.9.6)
- **JavaScript Client**: [51 commits](https://github.com/waldur/js-client/compare/7.9.5...7.9.6)
- **Go Client**: [24 commits](https://github.com/waldur/go-client/compare/7.9.5...7.9.6)

### Py Client Highlights

- Release: bump version to 7.9.6.
- Update Waldur Python SDK.
- Update Waldur Python SDK.

### Js Client Highlights

- Release: bump version to 7.9.6.
- 7.9.6-dev.24.
- Update Waldur TypeScript SDK.

### Go Client Highlights

- Update Waldur Go SDK.
- Update Waldur Go SDK.
- Update Waldur Go SDK.

### Resources

- [OpenAPI Schema](https://raw.githubusercontent.com/waldur/api-docs/main/docs/API/waldur-openapi-schema-7.9.6.yaml)
- [API Changes](https://api-docs.waldur.com/latest/integrator-guide/APIs/api-changes/waldur-openapi-schema-7.9.6-diff)


## 7.9.5 - 2025-12-17

### Release Summary

- **Release Impact:** Minor release with configuration and documentation updates

### Core Component Activity

- **Waldur Mastermind**: No changes
- **Waldur Homeport**: No changes
- **Waldur Helm**: No changes
- **Waldur Docker Compose**: No changes
- **Waldur Prometheus Exporter**: No changes

### Resources

- [OpenAPI Schema](https://raw.githubusercontent.com/waldur/api-docs/main/docs/API/waldur-openapi-schema-7.9.5.yaml)
- [API Changes](https://api-docs.waldur.com/latest/integrator-guide/APIs/api-changes/waldur-openapi-schema-7.9.5-diff)


## 7.9.4 - 2025-12-16

### Release Summary

- **Release Impact:** Minor release with configuration and documentation updates
- **SDK Updates:** 3 auto-generated clients updated

### Core Component Activity

- **Waldur Mastermind**: No changes
- **Waldur Homeport**: No changes
- **Waldur Helm**: No changes
- **Waldur Docker Compose**: No changes
- **Waldur Prometheus Exporter**: No changes

### SDK Updates (Auto-generated)

- **Python Client**: [4 commits](https://github.com/waldur/py-client/compare/7.9.3...7.9.4)
- **JavaScript Client**: [7 commits](https://github.com/waldur/js-client/compare/7.9.3...7.9.4)
- **Go Client**: [3 commits](https://github.com/waldur/go-client/compare/7.9.3...7.9.4)

### Js Client Highlights

- Release: bump version to 7.9.4.
- 7.9.4-dev.2.
- Update Waldur TypeScript SDK.

### Resources

- [OpenAPI Schema](https://raw.githubusercontent.com/waldur/api-docs/main/docs/API/waldur-openapi-schema-7.9.4.yaml)
- [API Changes](https://api-docs.waldur.com/latest/integrator-guide/APIs/api-changes/waldur-openapi-schema-7.9.4-diff)


## 7.9.3 - 2025-12-14

### Release Summary

- **Release Impact:** Minor release with configuration and documentation updates

### Core Component Activity

- **Waldur Mastermind**: No changes
- **Waldur Homeport**: No changes
- **Waldur Helm**: No changes
- **Waldur Docker Compose**: No changes
- **Waldur Prometheus Exporter**: No changes

### Resources

- [OpenAPI Schema](https://raw.githubusercontent.com/waldur/api-docs/main/docs/API/waldur-openapi-schema-7.9.3.yaml)
- [API Changes](https://api-docs.waldur.com/latest/integrator-guide/APIs/api-changes/waldur-openapi-schema-7.9.3-diff)


## 7.9.2 - 2025-12-07

### Release Summary

- **Release Impact:** Minor release with configuration and documentation updates
- **SDK Updates:** 3 auto-generated clients updated

### Core Component Activity

- **Waldur Mastermind**: No changes
- **Waldur Homeport**: No changes
- **Waldur Helm**: No changes
- **Waldur Docker Compose**: No changes
- **Waldur Prometheus Exporter**: No changes

### SDK Updates (Auto-generated)

- **Python Client**: [12 commits](https://github.com/waldur/py-client/compare/7.9.1...7.9.2)
- **JavaScript Client**: [19 commits](https://github.com/waldur/js-client/compare/7.9.1...7.9.2)
- **Go Client**: [9 commits](https://github.com/waldur/go-client/compare/7.9.1...7.9.2)

### Py Client Highlights

- Release: bump version to 7.9.2.
- Update Waldur Python SDK.
- Update Waldur Python SDK.

### Js Client Highlights

- Release: bump version to 7.9.2.
- 7.9.2-dev.8.
- Update Waldur TypeScript SDK.

### Go Client Highlights

- Update Waldur Go SDK.
- Update Waldur Go SDK.
- Update Waldur Go SDK.

### Resources

- [OpenAPI Schema](https://raw.githubusercontent.com/waldur/api-docs/main/docs/API/waldur-openapi-schema-7.9.2.yaml)
- [API Changes](https://api-docs.waldur.com/latest/integrator-guide/APIs/api-changes/waldur-openapi-schema-7.9.2-diff)


## 7.9.1 - 2025-11-30

### Release Summary

- **Release Impact:** 23 commits across 4 core repositories
- **Functional Changes:** 82 files changed with +4925/-1030 lines
- **SDK Updates:** 3 auto-generated clients updated from OpenAPI schema

!!! note "Statistics Note"
    Excludes tests, auto-generated files, and SDK client code for accurate development metrics.

### Core Component Activity

- **Waldur Mastermind**: [11 commits](https://github.com/waldur/waldur-mastermind/compare/7.9.0...7.9.1) · 21 files changed (+2791/-557 lines)
- **Waldur Homeport**: [9 commits](https://github.com/waldur/waldur-homeport/compare/7.9.0...7.9.1) · 54 files changed (+2125/-465 lines)
- **Waldur Helm**: [2 commits](https://github.com/waldur/waldur-helm/compare/7.9.0...7.9.1) · 7 files changed (+9/-8 lines)
- **Waldur Docker Compose**: [1 commits](https://github.com/waldur/waldur-docker-compose/compare/7.9.0...7.9.1)
- **Waldur Prometheus Exporter**: No changes

### SDK Updates (Auto-generated)

- **Python Client**: [3 commits](https://github.com/waldur/py-client/compare/7.9.0...7.9.1)
- **JavaScript Client**: [7 commits](https://github.com/waldur/js-client/compare/7.9.0...7.9.1)
- **Go Client**: [3 commits](https://github.com/waldur/go-client/compare/7.9.0...7.9.1)

### Notable Changes

- **Check if WALDUR_OPENPORTAL during routes permission check.** ([349cad4](https://github.com/waldur/waldur-homeport/commit/349cad4) - Waldur Homeport)
- **Allow set of custom cluster issuer name for cert manager.** ([7ee2d14](https://github.com/waldur/waldur-helm/commit/7ee2d14) - Waldur Helm)
- **Workarkound for changed API.** ([23c6904](https://github.com/waldur/waldur-mastermind/commit/23c6904) - Waldur Mastermind)
- **Extend export/import of data.** ([9f50656](https://github.com/waldur/waldur-mastermind/commit/9f50656) - Waldur Mastermind)
- **Set target version to 7.9.1.** ([7fc5104](https://github.com/waldur/waldur-helm/commit/7fc5104) - Waldur Helm)
- **Set target version to 7.9.1.** ([c7dc4e7](https://github.com/waldur/waldur-docker-compose/commit/c7dc4e7) - Waldur Docker Compose)

### Waldur Mastermind Highlights

- Workarkound for changed API.
- Extend export/import of data.
- Add filter to exclude transitional resources with early pending orders.

### Waldur Homeport Highlights

- Fix bad error message when applying for a an available organization with already open request.
- Migrate invitation form to react final form.
- Reallocation limits UI changes.

### Js Client Highlights

- Release: bump version to 7.9.1.
- 7.9.1-dev.2.
- Update Waldur TypeScript SDK.

### Resources

- [OpenAPI Schema](https://raw.githubusercontent.com/waldur/api-docs/main/docs/API/waldur-openapi-schema-7.9.1.yaml)
- [API Changes](https://api-docs.waldur.com/latest/integrator-guide/APIs/api-changes/waldur-openapi-schema-7.9.1-diff)

---

## 7.9.0 - 2025-11-30

### Release Summary

- **Release Impact:** 16 commits across 4 core repositories
- **Functional Changes:** 114 files changed with +1405/-927 lines
- **SDK Updates:** 3 auto-generated clients updated from OpenAPI schema

!!! note "Statistics Note"
    Excludes tests, auto-generated files, and SDK client code for accurate development metrics.

### Core Component Activity

- **Waldur Mastermind**: [8 commits](https://github.com/waldur/waldur-mastermind/compare/7.8.9...7.9.0) · 11 files changed (+377/-7 lines)
- **Waldur Homeport**: [3 commits](https://github.com/waldur/waldur-homeport/compare/7.8.9...7.9.0) · 99 files changed (+1023/-915 lines)
- **Waldur Helm**: [4 commits](https://github.com/waldur/waldur-helm/compare/7.8.9...7.9.0) · 4 files changed (+5/-5 lines)
- **Waldur Docker Compose**: [1 commits](https://github.com/waldur/waldur-docker-compose/compare/7.8.9...7.9.0)
- **Waldur Prometheus Exporter**: No changes

### SDK Updates (Auto-generated)

- **Python Client**: [3 commits](https://github.com/waldur/py-client/compare/7.8.9...7.9.0)
- **JavaScript Client**: [5 commits](https://github.com/waldur/js-client/compare/7.8.9...7.9.0)
- **Go Client**: [2 commits](https://github.com/waldur/go-client/compare/7.8.9...7.9.0)

### Notable Changes

- **[WAl-9443] Show review summary on in review proposals.** ([46b54e2](https://github.com/waldur/waldur-homeport/commit/46b54e2) - Waldur Homeport)
- **Set target version to 7.9.0.** ([9d3756c](https://github.com/waldur/waldur-helm/commit/9d3756c) - Waldur Helm)
- **Revert "Revert "Remove leftover path modifications"".** ([5ee8f11](https://github.com/waldur/waldur-helm/commit/5ee8f11) - Waldur Helm)
- **Fix ingress condition.** ([63903a7](https://github.com/waldur/waldur-helm/commit/63903a7) - Waldur Helm)
- **Revert "Remove leftover path modifications".** ([d8dd890](https://github.com/waldur/waldur-helm/commit/d8dd890) - Waldur Helm)
- **Set target version to 7.9.0.** ([58ceaa9](https://github.com/waldur/waldur-docker-compose/commit/58ceaa9) - Waldur Docker Compose)

### Waldur Mastermind Highlights

- Cleanup unused migration.
- Add readonly viewset to list checklists for call organizers.
- Expose additional fields for invoice items.

### Resources

- [OpenAPI Schema](https://raw.githubusercontent.com/waldur/api-docs/main/docs/API/waldur-openapi-schema-7.9.0.yaml)

---

## 7.8.9 - 2025-11-30

### Release Summary

- **Release Impact:** 4 commits across 3 core repositories
- **Functional Changes:** 8 files changed with +243/-38 lines
- **SDK Updates:** 2 auto-generated clients updated from OpenAPI schema

!!! note "Statistics Note"
    Excludes tests, auto-generated files, and SDK client code for accurate development metrics.

### Core Component Activity

- **Waldur Mastermind**: [2 commits](https://github.com/waldur/waldur-mastermind/compare/7.8.8...7.8.9) · 6 files changed (+240/-35 lines)
- **Waldur Homeport**: No changes
- **Waldur Helm**: [1 commits](https://github.com/waldur/waldur-helm/compare/7.8.8...7.8.9) · 2 files changed (+3/-3 lines)
- **Waldur Docker Compose**: [1 commits](https://github.com/waldur/waldur-docker-compose/compare/7.8.8...7.8.9)
- **Waldur Prometheus Exporter**: No changes

### SDK Updates (Auto-generated)

- **Python Client**: [1 commits](https://github.com/waldur/py-client/compare/7.8.8...7.8.9)
- **JavaScript Client**: [1 commits](https://github.com/waldur/js-client/compare/7.8.8...7.8.9)

### Notable Changes

- **Request deletion of offeringuser upon removal from project.** ([9135636](https://github.com/waldur/waldur-mastermind/commit/9135636) - Waldur Mastermind)
- **Add validation that resources belong to the same offering for limit reallocation.** ([3c8adcd](https://github.com/waldur/waldur-mastermind/commit/3c8adcd) - Waldur Mastermind)
- **Set target version to 7.8.9.** ([39c5fea](https://github.com/waldur/waldur-helm/commit/39c5fea) - Waldur Helm)
- **Set target version to 7.8.9.** ([fad7a57](https://github.com/waldur/waldur-docker-compose/commit/fad7a57) - Waldur Docker Compose)

### Resources

- [API Changes](../integrator-guide/APIs/api-changes/waldur-openapi-schema-7.8.9-diff.md)

---

## 7.8.8 - 2025-11-30

### Release Summary

- **Release Impact:** 123 commits across 4 core repositories
- **Functional Changes:** 667 files changed with +36182/-3236 lines
- **SDK Updates:** 3 auto-generated clients updated from OpenAPI schema

!!! note "Statistics Note"
    Excludes tests, auto-generated files, and SDK client code for accurate development metrics.

### Core Component Activity

- **Waldur Mastermind**: [74 commits](https://github.com/waldur/waldur-mastermind/compare/7.8.7...7.8.8) · 118 files changed (+22512/-916 lines)
- **Waldur Homeport**: [31 commits](https://github.com/waldur/waldur-homeport/compare/7.8.7...7.8.8) · 517 files changed (+13369/-2145 lines)
- **Waldur Helm**: [17 commits](https://github.com/waldur/waldur-helm/compare/7.8.7...7.8.8) · 32 files changed (+301/-175 lines)
- **Waldur Docker Compose**: [1 commits](https://github.com/waldur/waldur-docker-compose/compare/7.8.7...7.8.8)
- **Waldur Prometheus Exporter**: No changes

### SDK Updates (Auto-generated)

- **Python Client**: [19 commits](https://github.com/waldur/py-client/compare/7.8.7...7.8.8)
- **JavaScript Client**: [37 commits](https://github.com/waldur/js-client/compare/7.8.7...7.8.8)
- **Go Client**: [17 commits](https://github.com/waldur/go-client/compare/7.8.7...7.8.8)

### Notable Changes

- **Force migration of queues.** ([202721f](https://github.com/waldur/waldur-mastermind/commit/202721f) - Waldur Mastermind)
- **Fix check for rmq availability.** ([1d4da20](https://github.com/waldur/waldur-mastermind/commit/1d4da20) - Waldur Mastermind)
- **Extend migration to handle both broken and new migrations.** ([6bb3faf](https://github.com/waldur/waldur-mastermind/commit/6bb3faf) - Waldur Mastermind)
- **Fix mermaid typos.** ([2b7c2ca](https://github.com/waldur/waldur-mastermind/commit/2b7c2ca) - Waldur Mastermind)
- **Add orders documentation.** ([65a4924](https://github.com/waldur/waldur-mastermind/commit/65a4924) - Waldur Mastermind)
- **Disable rendering of email vars as they crash ansible installer.** ([9bde6ca](https://github.com/waldur/waldur-helm/commit/9bde6ca) - Waldur Helm)

### Waldur Mastermind Highlights

- Extend migration to handle both broken and new migrations.
- Fix mermaid typos.
- Add orders documentation.

### Waldur Homeport Highlights

- Expose uploaded purchase order in order details [WAL-9356].
- Implement frontend for site agent diagnostics.
- Add form field use_user_organization_as_customer_name.

### Waldur Helm Highlights

- Disable rendering of email vars as they crash ansible installer.
- Set target version to 7.8.8.
- Fix template.

### Py Client Highlights

- Release: bump version to 7.8.8.
- Update Waldur Python SDK.
- Update Waldur Python SDK.

### Js Client Highlights

- Release: bump version to 7.8.8.
- 7.8.8-dev.17.
- Update Waldur TypeScript SDK.

### Go Client Highlights

- Update Waldur Go SDK.
- Update Waldur Go SDK.
- Update Waldur Go SDK.

### Resources

- [API Changes](../integrator-guide/APIs/api-changes/waldur-openapi-schema-7.8.8-diff.md)

---

## 7.8.7 - 2025-11-30

### Release Summary

- **Release Impact:** 78 commits across 4 core repositories
- **Functional Changes:** 186 files changed with +6887/-1416 lines
- **SDK Updates:** 3 auto-generated clients updated from OpenAPI schema

!!! note "Statistics Note"
    Excludes tests, auto-generated files, and SDK client code for accurate development metrics.

### Core Component Activity

- **Waldur Mastermind**: [49 commits](https://github.com/waldur/waldur-mastermind/compare/7.8.6...7.8.7) · 46 files changed (+3070/-210 lines)
- **Waldur Homeport**: [25 commits](https://github.com/waldur/waldur-homeport/compare/7.8.6...7.8.7) · 113 files changed (+3140/-1040 lines)
- **Waldur Helm**: [3 commits](https://github.com/waldur/waldur-helm/compare/7.8.6...7.8.7) · 27 files changed (+677/-166 lines)
- **Waldur Docker Compose**: [1 commits](https://github.com/waldur/waldur-docker-compose/compare/7.8.6...7.8.7)
- **Waldur Prometheus Exporter**: No changes

### SDK Updates (Auto-generated)

- **Python Client**: [15 commits](https://github.com/waldur/py-client/compare/7.8.6...7.8.7)
- **JavaScript Client**: [30 commits](https://github.com/waldur/js-client/compare/7.8.6...7.8.7)
- **Go Client**: [13 commits](https://github.com/waldur/go-client/compare/7.8.6...7.8.7)

### Notable Changes

- **Fix project credit modal crashing issue.** ([b25f336](https://github.com/waldur/waldur-homeport/commit/b25f336) - Waldur Homeport)
- **Improve UI of add component modal.** ([297babe](https://github.com/waldur/waldur-homeport/commit/297babe) - Waldur Homeport)
- **Set target version to 7.8.7.** ([563758c](https://github.com/waldur/waldur-helm/commit/563758c) - Waldur Helm)
- **Cleanup docs.** ([78a0621](https://github.com/waldur/waldur-helm/commit/78a0621) - Waldur Helm)
- **Add support to set external db name and username configuration.** ([eb63a40](https://github.com/waldur/waldur-helm/commit/eb63a40) - Waldur Helm)
- **Set target version to 7.8.7.** ([85107e8](https://github.com/waldur/waldur-docker-compose/commit/85107e8) - Waldur Docker Compose)

### Waldur Mastermind Highlights

- Add autoprovisioning docs.
- Handle adding/removal of offering compliance checklists.
- Add unique constraint on slurm periodic policy.

### Waldur Homeport Highlights

- Implement UI to configure organization-specific component usage limits.
- Fix project credit modal crashing issue.
- Improve UI of add component modal.

### Py Client Highlights

- Release: bump version to 7.8.7.
- Update Waldur Python SDK.
- Update Waldur Python SDK.

### Js Client Highlights

- Release: bump version to 7.8.7.
- 7.8.7-dev.13.
- Update Waldur TypeScript SDK.

### Go Client Highlights

- Update Waldur Go SDK.
- Update Waldur Go SDK.
- Update Waldur Go SDK.

### Resources

- [API Changes](../integrator-guide/APIs/api-changes/waldur-openapi-schema-7.8.7-diff.md)

---

## 7.8.6 - 2025-11-30

### Release Summary

- **Release Impact:** 37 commits across 4 core repositories
- **Functional Changes:** 152 files changed with +6124/-729 lines
- **SDK Updates:** 3 auto-generated clients updated from OpenAPI schema

!!! note "Statistics Note"
    Excludes tests, auto-generated files, and SDK client code for accurate development metrics.

### Core Component Activity

- **Waldur Mastermind**: [5 commits](https://github.com/waldur/waldur-mastermind/compare/7.8.5...7.8.6)
- **Waldur Homeport**: [22 commits](https://github.com/waldur/waldur-homeport/compare/7.8.5...7.8.6) · 129 files changed (+4549/-597 lines)
- **Waldur Helm**: [7 commits](https://github.com/waldur/waldur-helm/compare/7.8.5...7.8.6) · 20 files changed (+1574/-107 lines)
- **Waldur Docker Compose**: [3 commits](https://github.com/waldur/waldur-docker-compose/compare/7.8.5...7.8.6) · 3 files changed (+1/-25 lines)
- **Waldur Prometheus Exporter**: No changes

### SDK Updates (Auto-generated)

- **Python Client**: [13 commits](https://github.com/waldur/py-client/compare/7.8.5...7.8.6)
- **JavaScript Client**: [5 commits](https://github.com/waldur/js-client/compare/7.8.5...7.8.6)
- **Go Client**: [12 commits](https://github.com/waldur/go-client/compare/7.8.5...7.8.6)

### Notable Changes

- **Set target version to 7.8.6.** ([7718ea0](https://github.com/waldur/waldur-docker-compose/commit/7718ea0) - Waldur Docker Compose)
- **Add filter to exclude transitional resources with early pending orders.** ([b216f24](https://github.com/waldur/waldur-mastermind/commit/b216f24) - Waldur Mastermind)
- **Improve filters labels.** ([fc5b9a1](https://github.com/waldur/waldur-mastermind/commit/fc5b9a1) - Waldur Mastermind)
- **Update configuration, CLI and developer guide.** ([0287336](https://github.com/waldur/waldur-mastermind/commit/0287336) - Waldur Mastermind)
- **Workarkound for changed API.** ([23c6904](https://github.com/waldur/waldur-mastermind/commit/23c6904) - Waldur Mastermind)
- **Extend export/import of data.** ([9f50656](https://github.com/waldur/waldur-mastermind/commit/9f50656) - Waldur Mastermind)

### Waldur Homeport Highlights

- Add multiplier configuration options [WAL-9373].
- Add staff notes.
- Add new end date setting to recovery view.

### Waldur Helm Highlights

- Set target version to 7.8.6.
- Update documentation.
- Remove leftover path modifications.

### Py Client Highlights

- Release: bump version to 7.8.6.
- Update Waldur Python SDK.
- Update Waldur Python SDK.

### Go Client Highlights

- Update Waldur Go SDK.
- Update Waldur Go SDK.
- Update Waldur Go SDK.

### Resources

- [API Changes](../integrator-guide/APIs/api-changes/waldur-openapi-schema-7.8.6-diff.md)

---

## 7.8.5 - 2025-11-30

### Release Summary

- **Release Impact:** 65 commits across 3 core repositories
- **Functional Changes:** 502 files changed with +8116/-4035 lines
- **SDK Updates:** 2 auto-generated clients updated from OpenAPI schema

!!! note "Statistics Note"
    Excludes tests, auto-generated files, and SDK client code for accurate development metrics.

### Core Component Activity

- **Waldur Mastermind**: No changes
- **Waldur Homeport**: [59 commits](https://github.com/waldur/waldur-homeport/compare/7.8.4...7.8.5) · 496 files changed (+8027/-4010 lines)
- **Waldur Helm**: [5 commits](https://github.com/waldur/waldur-helm/compare/7.8.4...7.8.5) · 6 files changed (+89/-25 lines)
- **Waldur Docker Compose**: [1 commits](https://github.com/waldur/waldur-docker-compose/compare/7.8.4...7.8.5)
- **Waldur Prometheus Exporter**: No changes

### SDK Updates (Auto-generated)

- **Python Client**: [19 commits](https://github.com/waldur/py-client/compare/7.8.4...7.8.5)
- **Go Client**: [28 commits](https://github.com/waldur/go-client/compare/7.8.4...7.8.5)

### Notable Changes

- **Update enums and descriptions from Waldur Mastermind.** ([ab5581c](https://github.com/waldur/waldur-homeport/commit/ab5581c) - Waldur Homeport)
- **Add JIRA mapping of frontend types to request types.** ([96e94ad](https://github.com/waldur/waldur-homeport/commit/96e94ad) - Waldur Homeport)
- **Add support for display and management of terminated projects [WAL-9212].** ([d9776ed](https://github.com/waldur/waldur-homeport/commit/d9776ed) - Waldur Homeport)
- **Fix sentry crash.** ([bd96857](https://github.com/waldur/waldur-homeport/commit/bd96857) - Waldur Homeport)
- **Set target version to 7.8.5.** ([bc1f90d](https://github.com/waldur/waldur-helm/commit/bc1f90d) - Waldur Helm)
- **Set target version to 7.8.5.** ([943480b](https://github.com/waldur/waldur-docker-compose/commit/943480b) - Waldur Docker Compose)

### Waldur Homeport Highlights

- Add support for display and management of terminated projects [WAL-9212].
- Fix sentry crash.
- Update enums and descriptions from Waldur Mastermind.

### Py Client Highlights

- Release: bump version to 7.8.5.
- Update Waldur Python SDK.
- Update Waldur Python SDK.

### Go Client Highlights

- Update Waldur Go SDK.
- Update Waldur Go SDK.
- Update Waldur Go SDK.

### Resources

- [API Changes](../integrator-guide/APIs/api-changes/waldur-openapi-schema-7.8.5-diff.md)

---

## 7.8.4 - 2025-11-30

### Release Summary

- **Release Impact:** 10 commits across 3 core repositories
- **Functional Changes:** 3 files changed with +67/-52 lines
- **SDK Updates:** 1 auto-generated clients updated from OpenAPI schema

!!! note "Statistics Note"
    Excludes tests, auto-generated files, and SDK client code for accurate development metrics.

### Core Component Activity

- **Waldur Mastermind**: No changes
- **Waldur Homeport**: [5 commits](https://github.com/waldur/waldur-homeport/compare/7.8.3...7.8.4)
- **Waldur Helm**: [3 commits](https://github.com/waldur/waldur-helm/compare/7.8.3...7.8.4) · 2 files changed (+3/-3 lines)
- **Waldur Docker Compose**: [2 commits](https://github.com/waldur/waldur-docker-compose/compare/7.8.3...7.8.4) · 1 files changed (+64/-49 lines)
- **Waldur Prometheus Exporter**: No changes

### SDK Updates (Auto-generated)

- **Python Client**: [12 commits](https://github.com/waldur/py-client/compare/7.8.3...7.8.4)

### Notable Changes

- **Set target version to 7.8.4.** ([fb7f946](https://github.com/waldur/waldur-docker-compose/commit/fb7f946) - Waldur Docker Compose)
- **Fix bad error message when applying for a an available organization with already open request.** ([e035237](https://github.com/waldur/waldur-homeport/commit/e035237) - Waldur Homeport)
- **Migrate invitation form to react final form.** ([264cc02](https://github.com/waldur/waldur-homeport/commit/264cc02) - Waldur Homeport)
- **Reallocation limits UI changes.** ([dc725fb](https://github.com/waldur/waldur-homeport/commit/dc725fb) - Waldur Homeport)
- **Fix either toggle or specific organization can be selected.** ([c506659](https://github.com/waldur/waldur-homeport/commit/c506659) - Waldur Homeport)
- **Check if WALDUR_OPENPORTAL during routes permission check.** ([349cad4](https://github.com/waldur/waldur-homeport/commit/349cad4) - Waldur Homeport)

### Py Client Highlights

- Release: bump version to 7.8.4.
- Update Waldur Python SDK.
- Update Waldur Python SDK.

### Resources

- [API Changes](../integrator-guide/APIs/api-changes/waldur-openapi-schema-7.8.4-diff.md)

---

## 7.8.3 - 2025-11-30

### Release Summary

- **Release Impact:** 2 commits across 2 core repositories
- **Functional Changes:** 2 files changed with +3/-3 lines
- **SDK Updates:** 2 auto-generated clients updated from OpenAPI schema

!!! note "Statistics Note"
    Excludes tests, auto-generated files, and SDK client code for accurate development metrics.

### Core Component Activity

- **Waldur Mastermind**: No changes
- **Waldur Homeport**: No changes
- **Waldur Helm**: [1 commits](https://github.com/waldur/waldur-helm/compare/7.8.2...7.8.3) · 2 files changed (+3/-3 lines)
- **Waldur Docker Compose**: [1 commits](https://github.com/waldur/waldur-docker-compose/compare/7.8.2...7.8.3)
- **Waldur Prometheus Exporter**: No changes

### SDK Updates (Auto-generated)

- **Python Client**: [3 commits](https://github.com/waldur/py-client/compare/7.8.2...7.8.3)
- **Go Client**: [2 commits](https://github.com/waldur/go-client/compare/7.8.2...7.8.3)

### Notable Changes

- **Set target version to 7.8.3.** ([827681b](https://github.com/waldur/waldur-helm/commit/827681b) - Waldur Helm)
- **Set target version to 7.8.3.** ([e32b13b](https://github.com/waldur/waldur-docker-compose/commit/e32b13b) - Waldur Docker Compose)

### Resources

- [API Changes](../integrator-guide/APIs/api-changes/waldur-openapi-schema-7.8.3-diff.md)

---

## 7.8.2 - 2025-11-30

### Release Summary

- **Release Impact:** 2 commits across 2 core repositories
- **Functional Changes:** 2 files changed with +3/-3 lines
- **SDK Updates:** 2 auto-generated clients updated from OpenAPI schema

!!! note "Statistics Note"
    Excludes tests, auto-generated files, and SDK client code for accurate development metrics.

### Core Component Activity

- **Waldur Mastermind**: No changes
- **Waldur Homeport**: No changes
- **Waldur Helm**: [1 commits](https://github.com/waldur/waldur-helm/compare/7.8.1...7.8.2) · 2 files changed (+3/-3 lines)
- **Waldur Docker Compose**: [1 commits](https://github.com/waldur/waldur-docker-compose/compare/7.8.1...7.8.2)
- **Waldur Prometheus Exporter**: No changes

### SDK Updates (Auto-generated)

- **Python Client**: [5 commits](https://github.com/waldur/py-client/compare/7.8.1...7.8.2)
- **Go Client**: [14 commits](https://github.com/waldur/go-client/compare/7.8.1...7.8.2)

### Notable Changes

- **Set target version to 7.8.2.** ([8b9a3c2](https://github.com/waldur/waldur-helm/commit/8b9a3c2) - Waldur Helm)
- **Set target version to 7.8.2.** ([19ef652](https://github.com/waldur/waldur-docker-compose/commit/19ef652) - Waldur Docker Compose)

### Go Client Highlights

- Update Waldur Go SDK.
- Update Waldur Go SDK.
- Update Waldur Go SDK.

### Resources

- [API Changes](../integrator-guide/APIs/api-changes/waldur-openapi-schema-7.8.2-diff.md)

---


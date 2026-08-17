# Changelog

## 8.1.1-rc.1 - 2026-08-17

### Highlights

This release candidate focuses on making OpenStack network port handling and role assignments behave predictably. Pinned IP addresses now actually take effect when ports are updated, failures to reclaim an address come with an explanation instead of an opaque error, and duplicate role assignment requests get a clear conflict response rather than silently proceeding. On the frontend, order approval and review screens are easier to work through, and the first groundwork for the new design system has landed.

### What's New

- Added a credit scenarios demo preset for the project dashboard, so credit history can be showcased with realistic data.
- Added a full-screen toggle to the confirmation drawer for reviewing pending consumer and provider orders in a larger view.

### Improvements

- Approve and reject dialogs for provider orders now clearly identify which order is being acted on.
- The Orders table hides low-signal columns by default, making the list easier to scan.
- Confirmation drawer rows stay on a single line, keeping long lists readable.
- Groundwork for the upcoming Tailwind/shadcn UI migration: shared design tokens and a first reusable button component, with no visible change to the current interface.
- Removed leftover configuration for the retired legacy SLURM plugin from the Helm chart.

### Bug Fixes

- A changed pinned IP address is now correctly applied when updating instance ports.
- Restored validation of the target tenant in OpenStack role assignments, and duplicate assignment requests now return a proper 409 conflict.
- When a port address cannot be reclaimed, the reason is now reported instead of a generic failure.

### Core Component Activity

- **Waldur Mastermind**: [4 commits](https://github.com/waldur/waldur-mastermind/compare/8.1.2...8.1.1-rc.1) - OpenStack port and RBAC fixes, plus a credit scenarios demo preset.
- **Waldur Homeport**: [4 commits](https://github.com/waldur/waldur-homeport/compare/8.1.2...8.1.1-rc.1) - Order review and approval usability work, and design system foundations.
- **Waldur Helm**: [1 commit](https://github.com/waldur/waldur-helm/compare/8.1.2...8.1.1-rc.1) - Dropped configuration for the removed legacy SLURM plugin.

---

## 8.1.2 - 2026-08-15

### Highlights

This release focuses on deployment configuration and operational tuning for both the Helm chart and Docker Compose distributions. Operators can now supply a field encryption key through standard deployment configuration, tailor the country list shown in the marketplace without rebuilding images, and tune mastermind memory behaviour from values or environment variables. API responses are now compressed at the ingress layer, and the Matrix chat networking and CSP settings have been corrected so voice messages and homeserver traffic work as expected.

### What's New

- Field encryption key (`FIELD_ENCRYPTION_KEY`) can now be configured for mastermind services in both the Helm chart and Docker Compose, so encrypted fields no longer require manual wiring.
- The list of countries offered in the marketplace can be customised directly from chart values, alongside the other whitelabeling options.
- New memory tuning knobs for mastermind — the gunicorn preload toggle and the Celery per-child memory ceiling — are exposed as chart values and Compose environment variables, letting operators recycle worker children before they grow too large.

### Improvements

- API and web responses are now compressed at the edge (Traefik middleware for Helm, Caddy for Docker Compose), reducing bandwidth use and improving load times on large payloads.
- Matrix and LiveKit network policies are now controlled by their own gate instead of the chart-wide `networkPolicy` switch, so chat networking can be managed independently; the behaviour is documented in the Matrix chat guide.
- The Prometheus metrics exporter now uses dedicated health check endpoints for its readiness and liveness probes.
- Prepared statements are disabled for psycopg3 connections, avoiding compatibility problems with connection poolers.

### Bug Fixes

- The ingress controller is now explicitly admitted by the Matrix homeserver and LiveKit JWT network policies, fixing blocked inbound traffic to Matrix chat.
- Voice messages in chat now play correctly — `blob:` media sources are permitted by the content security policy in both deployment methods.

### Core Component Activity

- **Waldur Helm**: [38 commits](https://github.com/waldur/waldur-helm/compare/8.1.0...8.1.2) - encryption key wiring, configurable country list, memory tuning values, network policy and ingress fixes.
- **Waldur Docker Compose**: [32 commits](https://github.com/waldur/waldur-docker-compose/compare/8.1.0...8.1.2) - encryption key passthrough, memory tuning environment knobs, and Caddy compression and CSP updates.

### Resources

- [OpenAPI Schema](../API/waldur-openapi-schema-8.1.2.yaml)

---


## 8.1.0 - 2026-08-15

### Highlights

This release makes the marketplace far more controllable for providers and operators. Offerings can now be restricted to specific roles, gated behind IP allow-lists, and made available through calls for proposals, while a new multi-tenant provider helpdesk lets service providers run their own support desks with SLA tracking and ticket routing. Billing gains volume discounts, an affiliate credit ledger and per-project credit attribution, so organizations can finally see where their credit actually goes. Operators also get POSIX UID/GID pool management, rotatable resource API keys with encrypted storage, network-restricted personal access tokens, and a substantially faster, lighter backend.

### What's New

- Service providers can run their own multi-tenant helpdesk: configure a desk per organization, route or re-route tickets to the offering's provider, track SLA and escalations, manage canned responses and a support team, with a full ticket workspace in the web UI.
- Offerings can be restricted to specific user roles, hidden from users who cannot order them, and configured to skip consumer approval for chosen roles.
- Access to resources can be limited by IP subnet: organizations manage one scoped allow-list, providers set defaults per offering, and consumers can add per-resource subnets when the offering opts in.
- Marketplace offerings can now be requested through calls for proposals, with purchase-order requirements, requested subscription periods and cost previews carried through to the allocated resource.
- Resource API keys can be rotated and revealed with encrypted storage at rest, including an inference service view and playground for LLM offerings.
- Personal access tokens support network ACLs, so a token only works from approved subnets, with the changes recorded in the audit log.
- New billing capabilities: volume-based component discounts, an affiliate program with a credit ledger and fee accrual, and credit compensation attributed per project.
- POSIX UID/GID pools can be managed centrally and exposed through GLAuth, SCIM and offering user attributes, including per-project POSIX groups.
- Providers can define SLURM Quality-of-Service levels per offering and allow-list them per partition; users choose a QoS when ordering.
- Resource end dates can be requested and approved as a reviewable change request rather than edited directly, and terminated resources can be restored where the offering allows it.
- Resources can be paused or downscaled automatically when reported usage reaches a component limit.
- An AI assistant is now available to anonymous marketplace visitors, with full-text searchable conversation logs and a KPI dashboard for support staff.
- New scope-aware event pub/sub lets agents and integrations subscribe to exactly the events they are entitled to, with an experimental realtime UI that refreshes views on push.
- Organization-scoped custom roles let owners define and manage roles within their own organization.
- Dun & Bradstreet is available as a company registry backend for onboarding organizations in Nordic countries; Khmer is available as an interface language.

### Improvements

- Maintenance announcements can be extended, ended early or cancelled, start and complete automatically on schedule, remain editable while scheduled, and record overrun metrics.
- Call and proposal management was reworked: checklists per workflow step, technical assessments, conflict-of-interest confirmation, call-manager-driven step completion, and clearer read-only enforcement on archived calls.
- Usage reporting is more forgiving: prepaid components accept usage, corrections can be re-billed after invoice finalization, and mid-month reports resolve the right plan period instead of being skipped.
- Substantially reduced backend memory footprint and removed many N+1 queries across usage billing, cost policies, offering plans, user lists and site-agent tasks.
- Table improvements in the web UI: pinnable columns, filters and sorting on offering resources, filter state scoped per table, and a fix for a multi-second refresh hang.
- Sentry reporting now carries user context and API breadcrumbs, and events group by message instead of raw dictionaries; each deployment gets its own scheduled-job monitors.
- API responses are compressed at the ingress in both Helm and Docker Compose deployments, and a field encryption key is wired through both for encrypted API key storage.
- Numerous dependency upgrades to patch known CVEs across Python and JavaScript dependencies.

### Bug Fixes

- Credit consumption charts plotted net price rather than actual compensation, and the project credit dashboard was rebuilt around credit actually drawn.
- OpenStack fixes: leaked instance ports are now reclaimed, tenant-linked images survive a global image pull, admin-created ports get the right tenant project, port security cannot be disabled while address pairs are set, and a tenant creation race with dependent provisioning was resolved.
- Cost policies deducted credit twice from a policy's cost and reacted slowly when pausing resources; both are fixed, and gate evaluation now reads real invoice data.
- Project and offering descriptions exceeding the length limit returned a server error instead of a validation message.
- Concurrent token refresh no longer fails with an integrity error, and pre-existing accounts are adopted on OIDC login with an audit trail.
- Order forms dropped OpenStack tenant and instance option values on submit, and preselected fields even when the choice was ambiguous.
- Invitations are cancelled when a project is removed, expired invitations show proper details, and project-scoped invitations land on the project dashboard after joining.

### Core Component Activity

- **Waldur Mastermind**: [296 commits](https://github.com/waldur/waldur-mastermind/compare/8.0.9...8.1.0) - provider helpdesk, access subnets, POSIX ID pools, affiliates and volume discounts, proposal workflow engine, performance and memory work
- **Waldur Homeport**: [268 commits](https://github.com/waldur/waldur-homeport/compare/8.0.9...8.1.0) - helpdesk and AI assistant UIs, credit dashboards, call management redesign, table enhancements, extraction of shared packages
- **Waldur Helm**: [38 commits](https://github.com/waldur/waldur-helm/compare/8.0.9...8.1.0) - field encryption key wiring, API response compression, matrix network policies, memory tuning values
- **Waldur Docker Compose**: [32 commits](https://github.com/waldur/waldur-docker-compose/compare/8.0.9...8.1.0) - field encryption key, response compression, memory tuning environment knobs

### Resources

- [OpenAPI Schema](../API/waldur-openapi-schema-8.1.0.yaml)

---






## 8.0.9 - 2026-06-21

### Highlights

This release brings real-time team collaboration to Waldur with an integrated Matrix-based chat — including in-browser voice/video calls — available across projects. It also adds SCIM 2.0 identity provisioning, a structured proposal evaluation workflow, and substantially deeper OpenStack network management (topology views, router gateway control, effective routes, and RBAC sharing). Operators gain finer access control through per-user personal access token gating and entity-scoped tokens, while a broad security pass hardens authentication, webhooks, and API endpoints. The frontend completed a large-scale migration to a modern form and data-fetching architecture for better reliability and performance.

### What's New

- **Team chat for projects** — A new Matrix-based chat lets project members message each other and start fullscreen voice/video calls directly in the browser, with file uploads, drafts, reactions, and message history export. Deployable via the Helm chart and as an optional Docker Compose add-on (LiveKit + Tuwunel homeserver).
- **SCIM 2.0 identity management** — Waldur can now act as a SCIM identity provider and pull users from external directories, enabling automated user lifecycle management with identity systems.
- **Proposal evaluation workflows** — Calls can define multi-step evaluation workflows with manual and automatic transitions, responsible roles, per-step configuration, and a visual status stepper for applicants and reviewers.
- **Offering groups** — Related offerings can be grouped together and managed from a dedicated provider tab.
- **Per-project order auto-approval** — Projects can be configured to automatically approve marketplace orders, with a clear notice surfaced at checkout.
- **Resource limit change requests** — Project members can request resource limit changes, with approval notifications and period-aware pricing shown in the UI.
- **OpenStack network tooling** — New tenant network topology diagram (exportable as PNG), router effective-routes view, external gateway management, inbound RBAC share visibility, per-instance config-drive control, and connectivity diagnostics for instances.
- **Likert and rich-text checklist questions**, plus support for file and multiple-file question types in checklists.
- **Personal access token controls** — Per-user gating of token usage and entity-scoped token bindings that restrict tokens to specific resources.
- **Quick impersonate** action from the global user search for staff.
- **Inference playground** — Chat directly with a resource's vLLM endpoint from the resource view.

### Improvements

- Marketplace orders can require a purchase order on update, and offering descriptions support inline image upload.
- OpenStack `set_quotas` now accepts network, subnet, port, floating-IP, and dynamic storage-type quotas; security group rules support custom IP protocol numbers.
- Resource and project teams gained soft-delete with audit fields, batch end-date actions, and a "sync remote team members" staff action.
- Site Agent diagnostics collection, offering-wide resource synchronization, and broker resilience/health-check tuning improve operational visibility.
- TypeScript SDK generation was centralized with stronger typing across modules, and the frontend migrated forms, tables, and data fetching to react-final-form and React Query for fewer regressions.
- Affiliation handling was redesigned with per-customer defaults and a mandatory-selection option.

### Bug Fixes

- Re-enabled CSRF protection on cookie-session authentication and blocked SSRF on OIDC discovery and webhook destinations; fixed an invoice-cost IDOR and restricted `/api/query/` to staff.
- Fixed OpenStack server-group operations against newer Nova APIs, floating-IP attach failures, and instance-creation race conditions.
- Corrected component usage permissions so authenticated users no longer see all usage data, and fixed total-usage and invoice-period calculations.
- Resolved numerous frontend crashes (floating-IP detach, contact panel, booking details, OIDC bootstrap) and client-side table pagination regressions.
- Hardened auto-deactivation of role-less users and added an admin override.

### Core Component Activity

- **Waldur Mastermind**: [265 commits](https://github.com/waldur/waldur-mastermind/compare/8.0.8...8.0.9) - Matrix chat, SCIM, proposal workflows, OpenStack networking, security hardening, and dependency upgrades.
- **Waldur Homeport**: [300 commits](https://github.com/waldur/waldur-homeport/compare/8.0.8...8.0.9) - Matrix chat UI, workflow steppers, OpenStack topology/routing views, and a large form/data-fetching architecture migration.
- **Waldur Helm**: [42 commits](https://github.com/waldur/waldur-helm/compare/8.0.8...8.0.9) - Matrix chat stack, Traefik ingress support, Bitnami-style extension hooks, and worker health-probe fixes.
- **Waldur Docker Compose**: [39 commits](https://github.com/waldur/waldur-docker-compose/compare/8.0.8...8.0.9) - Optional Matrix chat add-on with LiveKit calls and TURN relay.

### Resources

- [OpenAPI Schema](../API/waldur-openapi-schema-8.0.9.yaml)

---

## 8.0.8 - 2026-05-05

### Highlights

This release introduces resource-level project management through a new ResourceProject system that lets service providers organize and invite users to projects directly on resources, alongside a major expansion of the AI Assistant with an agentic loop, new tools for proposals and reviews, and a public service-discovery chatbot. OpenStack support gets significant upgrades — instance rescue/unrescue, full load balancer (LBaaS) management in the UI, hypervisor capacity tracking via the Placement API, and router gateway management. Operators benefit from usage-based billing for OpenStack offerings, monthly component usage reporting, project affiliations with external organizations, and a science domain registry, while extensive serialization and pagination fixes resolve Go SDK compatibility issues and report performance.

### What's New

- **Resource projects and unified permissions** — Service providers can now create projects under a resource, invite users with specific roles, and apply per-project resource limits. Backed by a unified permission system that consolidates resource user roles (mastermind + homeport).
- **AI Assistant agentic loop and expanded tools** — The AI assistant now runs an agentic loop with tools for marketplace search, proposal research, review workload management, and VM ordering. Includes user feedback collection, configurable system prompts, and a HomePort navigation block.
- **Anonymous service-discovery chatbot** — A new public-facing chatbot for HPC Service Hub helps unauthenticated visitors discover offerings and calls, with rate limiting and PII protections.
- **OpenStack instance rescue/unrescue** — Recover misconfigured instances by booting them from a rescue image without losing the original disk state. Available as a UI action.
- **OpenStack load balancer (LBaaS) management** — Full UI for creating and managing load balancers, listeners, pools, members, and health monitors, with floating IP attachment, security group rules on VIP ports, and algorithm validation against provider capabilities.
- **OpenStack router external gateway management** — New actions for setting and clearing external gateways and managing static routes from the UI.
- **Hypervisor capacity via Placement API** — OpenStack capacity tracking migrated to the Nova Placement API with a new per-instance allocations diagnostic endpoint, allocation-candidates pre-flight check, and a hypervisor summary tab on the tenant page.
- **Usage-based billing for OpenStack offerings** — Operators can now configure OpenStack offerings to bill by actual usage instead of upfront allocation [WAL-9841].
- **Monthly component usage reporting** — Aggregated monthly usage records per offering component, with a new reporting page for service providers showing usage trends [WAL-9823].
- **Project affiliations with external organizations** — Projects can now declare affiliations with external organizations, with admin UI and a project metadata editor [WAL-9846].
- **Science domain registry** — New ScienceDomain/ScienceSubDomain registry with admin UI, preset loading, and editable per-project assignment [HPCMP-476].
- **Custom project slug templates** — Customers and calls can now define project slug templates with live hint preview during project creation.
- **Resource grace period** — Offerings can opt into a grace period before resources are downscaled or terminated; surfaced as a warning bar on projects and a flag on resources [HPCMP-477].
- **Project lifecycle badges** — Projects show lifecycle state (active, ending soon, in grace period) in lists, cards, and resource flags.
- **GDPR-compliant address attribute on User** — User profiles now include an address field that can be exposed selectively via offering attribute config.
- **AI Assistant message feedback collection** — Users can rate assistant responses with a categorized feedback dialog [WAL-9486].
- **Reviewer invitation emails and rejection notifications** — Reviewers receive emails when added to a call pool; requesters and Puhuri portal contacts receive notifications when permission requests or allocations are rejected.
- **Cross-organization notification isolation** — Tests and behavior added to ensure notifications never leak across organization boundaries.
- **Restoring soft-deleted projects** — Project recovery action graduated out of feature flag and available to staff.
- **Order timestamps in error and output logs** — Orders now expose `error_updated_at` and `output_updated_at` for clearer troubleshooting [WAL-7982].
- **`SET_CONSUMER_ORDER_INFO` permission** — Consumer-side users can respond to provider information requests on orders with a dedicated permission [WAL-9872].
- **`ORDER.CREATE` permission** — Restricts order creation so customer readers cannot create orders.
- **Onboarding button on organization page** — Direct access to organization onboarding from the organization list.
- **Usage-based pagination across reports** — Server-side pagination added to offering cost reports, missing usage reports, and resources-by-offering tables for large dataset performance.

### Improvements

- Server-side pagination across reporting tables (offering costs, missing usage, resources-by-offering, usage monitoring) replaces client-side filtering for large datasets.
- Marketplace landing page gets new layouts (carousel, sidebar, classic) with category sidebar, hero section, and configurable card styles.
- AI Assistant drawer now supports expand/collapse, defers runtime mount until opened, and renders a richer resource list block with table data.
- Plan details popup correctly shows the prepaid subscription period and remaining duration; resource change-limits dialog now shows remaining prepaid period instead of annual price.
- Order summary and pending-confirmation drawer get UI polish: cleaner table headers, icon button consistency, hidden actions when empty, and avatar placeholder colors aligned with the design system.
- OpenStack Octavia load balancer sync skips when the service is not in the catalog and is now part of `TenantPullExecutor` [WAL-9387].
- Pending order tickets include prepaid total cost, slugs, and start/end dates in the description.
- Pending order ticket created automatically when an order enters pending state.
- Volume snapshot deletion cascades to delete the connected VM snapshot [WAL-9882].
- Hypervisor summary tab added to OpenStack tenant management view, with capacity charts [WAL-7929].
- Maintenance announcement template API now exposes `affected_offerings`.
- Remaining group invitation tokens are removed when project details dialog is cancelled.
- Resource end-date no longer enforces a 1-week minimum, giving operators full flexibility.
- AI Assistant content saved to the chat history now matches what was displayed in the UI [WAL-9848].
- AI Assistant for staff users can discuss generic, non-Waldur questions [WAL-9811].
- AI Assistant uses keyword-based intent classification to load only relevant tools per query [WAL-9845].
- Service provider chat offering filter correctly matches shared offerings [WAL-9799].
- TOS management UI rewritten for consistency, with a pending TOS consent widget on the user dashboard [WAL-9874, WAL-9877].
- Project slug template now applies when projects are created via API.
- Identity bridge selection allows first/last name as user attribute choices.
- Service desk request type management gets reorder validation and bulk activate/deactivate/delete actions.
- Provider project list now has an expandable team subtable for service providers [WAL-9844].
- Set consumer info action permission moved to the new `SET_CONSUMER_ORDER_INFO` permission [WAL-9872].
- Retry order button now respects permission checks [WAL-9880].
- Resource row actions correctly fetch project UUID for permission evaluation [WAL-9871].
- Project team Details action restricted to staff/support [WAL-9875].
- Apply action on calls table moved into the 3-dots dropdown for cleaner UX.
- Reporting charts use lighter color palettes; summary widgets get improved spacing.
- Pillow upgraded to 12.2.0 (CVE-2026-40192); lxml bumped to fix GHSA-vfmq-68hx-4jfw; dompurify upgraded to 3.4.0 (GHSA-39q2-94rc-95cp); xmldom upgraded to 0.8.13; Keycloak bumped to 26.6.1 (CVE-2026-4366, CVE-2026-4633); waldur-keycloak-mapper bumped to 1.4.0.
- Python runtime upgraded to 3.13 on Debian Bookworm; Docker image switched from Alpine to Debian slim for fastembed/onnxruntime support.
- Resource Add button hidden from users without `CREATE_ORDER` permission.

### Bug Fixes

- Numerous serializer fixes correct Go SDK unmarshal errors: `minimal_price`, plan prices, `get_quotas` return type, `NestedPriceEstimateSerializer`, `scope_name` field type, and `access_url` OpenAPI schema [PUHURI/SDK].
- Fix `IntegrityError` on OpenStack image pull when duplicates are hidden, with regression test.
- Fix N+1 queries in marketplace component usage list endpoint and avoid `M2M JOIN + DISTINCT` on offering-users endpoint [PUHURI-PORTALS-P52, Q1P].
- Fix `PlanComponent.DoesNotExist` crash in `set_limits` for TOTAL limit components.
- Fix quarterly SLURM policies broken by `0226` `limit_period` backfill, with repair migration [WAL-9907].
- Fix prepaid field validation to allow null values on non-prepaid components [WAL-9908].
- Fix volume discount applied to duration-multiplied quantity (frontend threshold check also corrected for prepaid components).
- Fix prepaid duration calculation to use order `start_date`.
- Fix `CourseAccount` serializer crash on null project dates.
- Fix `user_has_consent=false` filter incorrectly excluding offerings with no consent records.
- Fix `IntegrityError` and `InvalidCursorName` crash in `sync_allocation_limits` and SLURM periodic settings sync OOM.
- Fix deactivated users unable to log in via OIDC with pending invitation; group invitations no longer blocked by `OIDC_BLOCK_CREATION_OF_UNINVITED_USERS`.
- Fix `UniqueViolation` in constance key rename migration.
- Fix `verify_ssl` not being passed to `OctaviaClient` connection [WAL-9388].
- Fix user filter incorrectly including users with revoked project/organization roles.
- Fix maintenance announcement `affected_offerings` missing from API response.
- Fix scientific notation display in plan price editing.
- Fix tool-call follow-up path crash and silent content drop in AI Assistant streamer.
- Fix XSS vulnerabilities across markdown/HTML rendering components.
- Fix dropdown pagination in cost policy, credit, issue project/resource, and move-to-project autocompletes [HPCMP-471].
- Fix credit usage dialog showing wrong project name and incorrect filter.
- Fix estimated total price value in plan section.
- Fix permission request rejection notification to use full name as sender [WAL-9906].
- Fix `set_as_erred` action exposure for orders in UI [WAL-9648].

### Core Component Activity

- **Waldur Mastermind**: [184 commits](https://github.com/waldur/waldur-mastermind/compare/8.0.7...8.0.8) - Resource projects, AI assistant tools, OpenStack rescue/Placement API/LBaaS, usage-based billing, science domains, affiliated organizations, Python 3.13 upgrade.
- **Waldur Homeport**: [160 commits](https://github.com/waldur/waldur-homeport/compare/8.0.7...8.0.8) - Resource projects UI, OpenStack LBaaS frontend, AI assistant agentic loop, marketplace layouts, server-side pagination for reports, `useManagedMutation` refactor, extensive UI polish.
- **Waldur Helm**: [15 commits](https://github.com/waldur/waldur-helm/compare/8.0.7...8.0.8) - Pull secret added to cleanup cronjob; release candidate version bumps.
- **Waldur Docker Compose**: [16 commits](https://github.com/waldur/waldur-docker-compose/compare/8.0.7...8.0.8) - Keycloak 26.6.1 (CVE fixes), waldur-keycloak-mapper 1.4.0, release candidate bumps.

### Resources

- [OpenAPI Schema](../API/waldur-openapi-schema-8.0.8.yaml)

---

## 8.0.7 - 2026-04-09

### Highlights

This release introduces Personal Access Tokens (PATs) for programmatic API access, upfront billing with prepaid components, and a fully redesigned reporting and analytics module. Policy enforcement is now more reliable with credit-aware evaluation, debounced month-boundary triggers, and clear attribution of automated actions. The AI Assistant gained VM creation capabilities, role-based access control, OpenAI API compatibility, and improved streaming reliability.

### What's New

- **Personal Access Tokens (PATs)**: Users can now create, rotate, and revoke personal access tokens for programmatic API access, with a dedicated management UI and admin overview.
- **Upfront billing and prepaid components**: Offerings can now use upfront billing with configurable prepaid durations, renewal constraints, and volume discount display in the order form.
- **Project end date change requests**: Project members can request end date modifications through a formal approval workflow with notifications for approvals and rejections.
- **AI Assistant VM creation**: The built-in AI Assistant can now create virtual machines through a guided multi-step flow with offering selection, inline streaming of tool results, and rendered UI blocks.
- **AI Assistant RBAC and customization**: AI Assistant access can now be restricted by role, its name and organization are customizable, and it includes a disclosure statement for users.
- **Reporting and analytics overhaul**: The reporting module has been completely redesigned with a new layout, toggleable report screens, chart export capabilities, proposal analytics, and user demographics dashboards.
- **Quota usage notifications**: Automated email notifications are now sent when resource quota usage reaches 75% and 100%.
- **Batch project operations**: Staff users can now batch-move and batch-delete projects, and batch-activate or batch-deactivate users.
- **Bulk article code updates**: Staff users can find and replace article codes across offerings through a guided wizard.
- **Identity bridge allowed-fields endpoint**: A new API endpoint exposes which identity bridge fields are available, and these fields are now shown on the user's own profile.

### Improvements

- **Cost policy enhancements**: Policies now account for available project/customer credits, include affected resource counts, debounce at month boundaries to prevent false triggers, and track actions with reversion history and event scopes.
- **OpenStack improvements**: Load balancer management now uses the OpenStack SDK (Octavia), port security can be toggled during instance creation, fixed IPs are supported in port updates, and Nova microversion 2.47 is used for reliable flavor data.
- **Marketplace filters and API**: Added resource attribute filters, slug filters on all slug-based endpoints, robot account search filters, and `created_before`/`modified_before` date filters.
- **Offering and resource management**: Offerings now support helpdesk and documentation URLs, extensions lists on software packages, state counters for resource/user distribution, and a provider description field. Billing mode switching is generalized for all offering types.
- **Grace period visibility**: Grace period information is now displayed in project cards, resource lists, resource details, and organization settings.
- **User management**: Added deactivation reason tracking, gender field now uses string values, and OIDC claim parsing includes normalization. Staff can add deactivated users to teams.
- **Proposal system**: Reviewers and proposal creators receive deadline approach notifications, staff can override COI blocks and reviewer invitations, and proposal analytics are available in reporting.
- **SCIM and site agent sync**: SCIM sync now triggers on resource and user state transitions and offering endpoint changes. Site agent message deduplication can be bypassed for user-triggered updates.
- **Notifications default to disabled**: All notifications are now disabled by default and must be explicitly enabled.
- **Marketplace layout customization**: Admins can configure marketplace card style and layout mode, and select login page visual layouts through a preview selector.
- **Rebranded eduTEAMS to MyAccessID** in the authentication UI.
- **E2E testing migrated from Cypress to Playwright**.

### Bug Fixes

- Fixed price estimate fields returning numbers instead of strings.
- Fixed renewal cost calculation not accounting for component factors.
- Fixed ComponentUsage duplicates caused by plan period mismatches.
- Fixed limit usage calculation consistency between panel display and policy enforcement.
- Fixed credit deduction and policy evaluation race conditions.
- Fixed policy actions bypassing Django signals, breaking STOMP notifications.
- Fixed STOMP circuit breaker never recovering from OPEN state.
- Fixed user deactivation sync for course accounts and inactive users.
- Fixed internal comment flag not synced from Jira REST API.
- Fixed N+1 queries on users, course accounts, and service provider users endpoints.
- Fixed offering user creation race conditions and Gunicorn worker timeouts.
- Fixed offering user usernames cleared on plugin options update.
- Fixed duplicate key errors during structure import with existing offering users.
- Fixed AI Assistant persisting full message instead of partial on stop and mid-stream disconnects.
- Fixed resource panel showing stale usage when limit_usage is zero.
- Fixed marketplace sidebar filter synchronization issues.
- Fixed URLs with trailing slashes causing 404 errors.

### Security

- Bumped Django to address GHSA-5mf9-h53q-7mhq.
- Bumped cryptography 46.0.6 to 46.0.7 to fix GHSA-p423-j2cm-9vmq.
- Added osv-scanner dependency vulnerability scanning to CI pipelines.
- Escaped user input in GLauth TOML config to prevent parse errors.
- Added validation that security groups cannot be used with port security disabled.

### Core Component Activity

- **Waldur Mastermind**: [216 commits](https://github.com/waldur/waldur-mastermind/compare/8.0.6...8.0.7) - PATs, upfront billing, policy improvements, AI Assistant enhancements, quota notifications, project end date requests, OpenStack SDK migration
- **Waldur Homeport**: [180 commits](https://github.com/waldur/waldur-homeport/compare/8.0.6...8.0.7) - PAT management UI, prepaid billing forms, reporting overhaul, project end date requests, AI Assistant VM creation, Playwright migration
- **Waldur Helm**: [31 commits](https://github.com/waldur/waldur-helm/compare/8.0.6...8.0.7) - Configurable proxy buffer size, whitelabeling image pull secret, version bumps
- **Waldur Docker Compose**: [28 commits](https://github.com/waldur/waldur-docker-compose/compare/8.0.6...8.0.7) - Keycloak upgrade with optional profile, removed deprecated FirecREST config, version bumps

### Resources

- [OpenAPI Schema](../API/waldur-openapi-schema-8.0.7.yaml)

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
-->

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

---

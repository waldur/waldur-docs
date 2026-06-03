# Changelog

## 8.0.9-rc.20 - 2026-06-03

### Highlights

This release focuses on stability for billing, OpenStack usage tracking, and key UI workflows. Cost policies and usage-based invoicing are more reliable around edge cases, marketplace usage snapshots now stay in sync with every OpenStack tenant quota pull, and several crashes in booking, proposal rounds, and support drawers have been resolved.

### Bug Fixes

- Fixed a datetime/date type mismatch that could prevent usage-triggered invoice creation from succeeding.
- Deferred cost policy publishing until after database commit and removed a recursive save in the project-name handler, eliminating a class of inconsistencies around month boundaries.
- Booking resource details no longer crash when an offering has no schedules defined.
- Round creation wizard no longer crashes when date and timezone fields are not pre-wrapped.

### Improvements

- Marketplace usage snapshots are now refreshed on every OpenStack tenant quota pull, keeping reported usage aligned with backend state.
- Polished the Support requests drawer layout, including issue status presentation, type icons, and the quick-issue table.

### Core Component Activity

- **Waldur Mastermind**: [3 commits](https://github.com/waldur/waldur-mastermind/compare/8.0.9-rc.19...8.0.9-rc.20) - billing/policy reliability fixes and OpenStack usage snapshot refresh.
- **Waldur Homeport**: [3 commits](https://github.com/waldur/waldur-homeport/compare/8.0.9-rc.19...8.0.9-rc.20) - crash fixes in booking and proposal round wizard, plus Support drawer polish.

---

## 8.0.9-rc.19 - 2026-06-03

### Highlights

This release improves the group invitation flow with smarter post-acceptance routing, adds new operational tooling for diagnosing broker and Celery issues, and patches a security vulnerability in JWT handling. Deployments on Kubernetes gain Bitnami-style extension hooks for customizing core workloads without forking the chart.

### What's New

- Operators can now run `audit_broker_config` and `probe_broker_latency` management commands to inspect message broker configuration and measure end-to-end Celery latency for troubleshooting worker issues.
- Helm chart now exposes Bitnami-style extension hooks (extra env vars, volumes, sidecars, init containers, pod annotations) for api, worker, beat, and homeport deployments, enabling customization without modifying the chart.

### Improvements

- Group invitation acceptance now returns the created project in the API response and the frontend routes users to the correct destination based on the acceptance outcome, giving a smoother onboarding experience [WAL-9997].
- Resource project state column now uses the consistent design-system Badge component, aligning visual styling with the rest of the UI.
- Form layouts consolidated under a single FormGroup component across ~90 dialogs and forms, improving visual consistency and reducing duplication.

### Bug Fixes

- Restored `?field=` response projection on API endpoints that override the `responses=` schema, so clients can again request a subset of fields on these endpoints.
- ESLint `no-redundant-vi-mock` rule no longer flags legitimate mock setups in test/mocks directories.

### Security

- Upgraded PyJWT to 2.13.0 to address 4 CVEs.

### Core Component Activity

- **Waldur Mastermind**: [4 commits](https://github.com/waldur/waldur-mastermind/compare/8.0.9-rc.18...8.0.9-rc.19) - broker diagnostic commands, group invitation response improvements, OpenAPI projection fix, PyJWT security bump.
- **Waldur Homeport**: [4 commits](https://github.com/waldur/waldur-homeport/compare/8.0.9-rc.18...8.0.9-rc.19) - invitation acceptance routing, design-system Badge adoption, FormGroup consolidation, ESLint rule fix.
- **Waldur Helm**: [1 commit](https://github.com/waldur/waldur-helm/compare/8.0.9-rc.18...8.0.9-rc.19) - extension hooks for api/worker/beat/homeport deployments.

---

## 8.0.9-rc.18 - 2026-06-03

### Highlights

This release candidate focuses on stability under load and OpenStack capability discovery. Policy evaluation and Celery worker handling have been hardened to prevent timeouts and reduce churn during traffic spikes, while OpenStack now exposes placement traits per hypervisor for finer-grained scheduling decisions. The OpenAPI schema has also been refined to better reflect optional fields across several core models.

### Improvements

- Reduced worker timeouts and stabilised background processing by debouncing all policy trigger handlers and tightening Celery broker resilience with heartbeat, TCP keepalive, and less aggressive worker churn.
- OpenStack now collects placement traits per resource provider into the Hypervisor model, enabling more accurate placement and filtering decisions ([WAL-9894]).
- Improved OpenAPI schema accuracy by marking conditionally-removed User fields as optional and extending the relax-required hook to cover IdentityProvider, Message, and Issue resources.
- Updated developer documentation covering configuration, CLI, events, handlers, and the modern autonomous `*Group` form architecture in Homeport.

### Core Component Activity

- **Waldur Mastermind**: [6 commits](https://github.com/waldur/waldur-mastermind/compare/8.0.9-rc.17...8.0.9-rc.18) - broker and policy resilience improvements, OpenStack hypervisor traits, and OpenAPI schema refinements.
- **Waldur Homeport**: [1 commit](https://github.com/waldur/waldur-homeport/compare/8.0.9-rc.17...8.0.9-rc.18) - developer documentation update for autonomous form group architecture.

---

## 8.0.9-rc.17 - 2026-06-02

### Highlights

This release improves reliability of usage-based billing by moving component usage processing to an asynchronous background task, and quiets noisy policy evaluation events for cleaner audit logs. Administrators get better visibility into offering option changes through extended change logging, and the admin Categories table gains sortable columns and group filtering. Several SDK-related bugs are fixed, including a missing session field and a nullable affiliation issue.

### What's New

- Admin Categories table now supports sortable Title and Group columns plus a Group filter for easier navigation of large category sets.
- Offering change logging now captures changes to offering options, giving administrators a more complete audit trail.

### Improvements

- Component usage billing now runs as an asynchronous Celery task, improving responsiveness and reliability when processing usage reports.
- SLURM policy evaluation no longer emits events for no-op evaluations, reducing noise in audit logs.
- Workflow steps are now seeded as enabled when a call is created, removing the need for manual activation.
- Resource edit actions now preserve an empty description value when the user intentionally clears it.

### Bug Fixes

- Fixed PgBouncer prepared statement errors in the Celery database result backend that could disrupt task result retrieval.
- Fixed `/api/users/me/` to include the `has_active_session` field, restoring expected behavior for SDK clients.
- Allowed the affiliation field to be nullable, resolving an SDK error when the value is not set.

### Internal

- Large frontend refactor migrating forms to HOC-wrapped autonomous field groups, improving form consistency and testability across the application.

### Core Component Activity

- **Waldur Mastermind**: [8 commits](https://github.com/waldur/waldur-mastermind/compare/8.0.9-rc.16...8.0.9-rc.17) - async usage billing, extended offering logging, SDK fixes, and policy event cleanup.
- **Waldur Homeport**: [4 commits](https://github.com/waldur/waldur-homeport/compare/8.0.9-rc.16...8.0.9-rc.17) - admin Categories table enhancements, resource edit fix, and a broad forms refactor.

### Resources

- [OpenAPI Schema](../API/waldur-openapi-schema-8.0.9-rc.17.yaml)

---

## 8.0.9-rc.16 - 2026-06-01

### Highlights

This release tightens OpenStack network security by restricting external gateways and floating IPs to networks the project actually has access to, and extends cost policy pre-flight enforcement across all policy scopes so over-limit orders are blocked before they consume resources. The proposal evaluation workflow gains a full set of UI components including a status stepper, and several papercut bugs in the marketplace, sidebar filters, and invoice tables have been fixed.

### What's New

- New proposal evaluation workflow UI: configurable workflow steps, decision actions, a workflow status stepper on proposals, and supporting widgets across call management and review screens.
- Staff can now create maintenance announcements through a guided flow with an optional provider/offering picker.
- Marketplace categories can now be ordered by title and group.

### Improvements

- External gateway selection on OpenStack routers is now restricted to shared networks or networks granted via RBAC, with the floating-IP create-router argument gated to match. Subnets supplied via `external_fixed_ips` are validated against the chosen network.
- Cost policy pre-flight checks now block over-limit orders for every cost policy scope (project, customer, and offering), not just a subset.
- Project and customer stats now exclude child offerings and report storage in GB instead of MB.
- Invoice items table refreshes automatically after per-row actions so the view always reflects the latest state.
- SAP invoice reports format `cond_value` independently of the operating system locale, avoiding inconsistent decimal separators.
- Helm chart now allows overriding `PROJECT.MEMBER` permissions through `customRolePermissions`.

### Bug Fixes

- Floating-IP request orders no longer crash when offerings expose `select_openstack_*` options, and required validation no longer fires on boolean option fields.
- Provider offerings list no longer hangs when a state filter is applied.
- Resources sidebar links keep the active organization filter, and the sidebar resources filter no longer inherits unrelated query parameters from the host page.
- Marketplace deploy page submits forms from the correct component.
- Fixed Estonian translation for the "Instances count" quota.
- Celery worker health probes in the Helm chart no longer trigger false liveness restarts.

### Core Component Activity

- **Waldur Mastermind**: [10 commits](https://github.com/waldur/waldur-mastermind/compare/8.0.9-rc.15...8.0.9-rc.16) - OpenStack network access hardening, cost policy pre-flight expansion, marketplace stats and ordering tweaks, SAP invoice locale fix.
- **Waldur Homeport**: [11 commits](https://github.com/waldur/waldur-homeport/compare/8.0.9-rc.15...8.0.9-rc.16) - Proposal workflow UI, staff maintenance creation flow, plus a batch of marketplace, sidebar, and invoice fixes.
- **Waldur Helm**: [2 commits](https://github.com/waldur/waldur-helm/compare/8.0.9-rc.15...8.0.9-rc.16) - Configurable project member permissions and Celery worker health probe fix.

---

## 8.0.9-rc.15 - 2026-05-31

### Highlights

This release significantly expands OpenStack tenant network visibility and troubleshooting capabilities. Operators get a new tenant network topology view, router effective-routes inspection, instance connectivity diagnostics, and a network audit timeline — making it much easier to understand and debug complex tenant networking. VM deployment is also more transparent with quota state surfaced for flavors and floating IPs, and several form fixes improve reliability across allocation pools, sidebar filters, and topology export.

### What's New

- Tenant network topology tab: a new visualization (with Mermaid-based rendering, PNG export, and legend) shows the layout of networks, subnets, routers, and ports within a tenant. ([WAL-9971])
- Router effective-routes endpoint and card: see the combined static and learned routes that actually apply to a router, alongside related network and subnet listings. ([WAL-9972])
- Instance connectivity diagnose action: trigger a diagnostic on an OpenStack instance to surface connectivity problems directly from the UI. ([WAL-9976])
- Network audit timeline endpoint on Tenant: review a chronological audit trail of network-related events scoped to a tenant. ([WAL-9975])
- Inbound RBAC shares visible to target tenants: tenants now see RBAC policies shared into them, not just those they share outward. ([WAL-9973])
- Set allowed address pairs as a first-class Port action, with the instance dialog migrated to use the Port endpoint. ([WAL-9977], [WAL-8599])
- Checklist questions now support File and Multiple files question types in the UI. ([WAL-9393])
- Custom IP protocol numbers are supported when authoring security group rules. ([WAL-9828])

### Improvements

- VM deploy flow surfaces flavor and floating IP quota state, so operators can see at a glance which options are blocked by quota. ([WAL-9948])
- External-pool exhaustion is now surfaced clearly when creating a floating IP, instead of failing opaquely. ([WAL-9974])
- Periodic orphan backfill now self-heals on a per-tenant basis, isolating failures to affected tenants. ([ONS-1175])
- Frontend test infrastructure standardized with centralized mocks for more reliable test runs.

### Bug Fixes

- Subnet allocation pool fields now correctly persist user input.
- Resources sidebar links restore the project/customer filter context.
- Topology PNG export no longer fails with a tainted-canvas error.
- `AsyncSelectField` now respects a caller-provided `getOptionLabel`.

### Core Component Activity

- **Waldur Mastermind**: [8 commits](https://github.com/waldur/waldur-mastermind/compare/8.0.9-rc.14...8.0.9-rc.15) — tenant network topology, router effective-routes, instance diagnostics, network audit timeline, inbound RBAC visibility, and Port-based allowed address pairs.
- **Waldur Homeport**: [13 commits](https://github.com/waldur/waldur-homeport/compare/8.0.9-rc.14...8.0.9-rc.15) — topology tab and export, effective-routes card, VM deploy quota surfacing, checklist file question types, custom IP protocols in security rules, and assorted form/test fixes.

---

## 8.0.9-rc.14 - 2026-05-29

### Highlights

This release candidate resolves a startup crash that affected users signing in through OIDC providers. Operators running identity-federated deployments should see reliable application bootstrap restored.

### Bug Fixes

- Fixed an application bootstrap crash that prevented the UI from loading for OIDC-authenticated sessions.

### Core Component Activity

- **Waldur Homeport**: [1 commit](https://github.com/waldur/waldur-homeport/compare/8.0.9-rc.13...8.0.9-rc.14) - OIDC session bootstrap fix.

---

## 8.0.9-rc.13 - 2026-05-29

### Highlights

This release strengthens security with restored CSRF protection on session-authenticated API endpoints and adds a per-user gate for personal access tokens. OpenStack operators gain richer tenant management with router external gateway controls, expanded quota actions, and audit logging. The frontend completes its long-running migration from redux-form to react-final-form and consolidates state management around React Query and hooks.

### What's New

- **OpenStack router external gateways**: Operators can now set, view, and remove external gateways on tenant routers from the UI, with full audit logging of changes.
- **OpenStack tenant quota management**: New "Set quotas" and "Refresh quotas" actions on OpenStack tenants, with marketplace-managed warning badges and an unsaved-changes guard. `set_quotas` now accepts dynamic `gigabytes_<type>` keys plus `floating_ip_count`, `network_count`, `subnet_count`, and `port_count`.
- **Per-user personal access token gate**: Administrators can now enable or disable personal access token creation on a per-user basis from the user form.
- **Custom IP protocol numbers**: Security group rules support arbitrary IP protocol numbers beyond TCP/UDP/ICMP for both OpenStack and Rancher.
- **Inference playground**: Resource view exposes a chat-style playground for talking to a resource's vLLM endpoint, gated by a new `expose_inference_playground` offering display option.
- **Archived calls view**: Proposal call management now has a dedicated archived-calls tab with a banner and disabled actions on closed calls.
- **Manual workflow transitions**: Proposal workflow steps support a manual transition mode with per-call step configuration and internal notes.
- **Marketplace endpoint management**: New `set_endpoints` action lets providers update endpoints on marketplace resources.
- **Offering description image upload**: Markdown editor in offering descriptions now supports inline image upload.
- **VM resource metadata exposure**: VM resource lists show image and flavor names with filter support.
- **Request limit changes for project members**: Project members (not just managers) can now request limit changes on resources.

### Improvements

- **Security — CSRF restored on session auth**: DRF `SessionAuthentication` no longer silently bypasses CSRF; cookie-authenticated state-changing endpoints are protected again. Django admin login continues to work via its own CSRF middleware (covered by regression tests).
- **OIDC reliability**: Deactivated users now receive a clean rejection instead of a 500 error during OIDC login.
- **SCIM reconciliation**: Reconcile now also triggers on recent offering-user and resource changes within the configured timeframe.
- **Service-provider team privacy**: Non-consented users are hidden from SP resource teams when ToS enforcement is on; offering usernames are visible only to direct project members.
- **Remote Waldur sync**: Only project-level permissions are synced to remote Waldur, avoiding unintended customer-level propagation.
- **Termination order acceptance**: Users with appropriate permissions can now accept terminate orders that are pending consumer approval.
- **EESSI catalog**: Duplicate upstream module versions are preserved instead of being silently dropped.
- **Resource lifecycle**: Inactive actors are skipped when scheduling resource termination; system volume bootable flag is preserved during instance creation.
- **Site agent notifications**: The site agent is notified when a project moves between customers.
- **Logout cleanup**: Redirect storage is cleared on logout to prevent stale post-login redirects.
- **SCIM tab fix**: Identity provider settings no longer show an empty SCIM tab.
- **Checklist file answers**: File answers in checklists now process correctly on update and accept already-processed files.
- **Estonian and Lithuanian translations**: Improved coverage; OpenStack "tenant" now renders as "privaatpilv" in Estonian.
- **OpenStack tenant migration**: Subnet dropdown added for the source OpenStack in migration forms.
- **Offering type filter scoping**: Provider offerings table only lists integration types the user can access.
- **Disabled action menus**: Tables show disabled action menus instead of "N/A" text for unavailable actions.
- **Reviewer profile UX**: Multiple UI consistency fixes across project, reviewer profile, user-edit pages, and modals.

### Bug Fixes

- Fix invoice lookup using billing_period instead of UTC date in usage billing.
- Fix wrong resource URL in limit change request notification emails.
- Return 400 (not 500) on ambiguous category title in offering import.
- Bump `js-cookie`, `qs`, `brace-expansion`, and `ws` to patched versions to resolve known vulnerabilities.
- Fix Python dependency vulnerability scan configuration.

### Core Component Activity

- **Waldur Mastermind**: [40 commits](https://github.com/waldur/waldur-mastermind/compare/8.0.9-rc.12...8.0.9-rc.13) - Security hardening (CSRF), OpenStack quota and security-group enhancements, proposal workflow improvements, checklist fixes, and broad OpenAPI typing refactors.
- **Waldur Homeport**: [76 commits](https://github.com/waldur/waldur-homeport/compare/8.0.9-rc.12...8.0.9-rc.13) - Completed redux-form → react-final-form migration, migrated Redux selectors/drawer/notifications/table actions to hooks and React Query, added router external gateway UI, inference playground, archived calls view, and quota management actions.
- **Waldur Helm**: [1 commit](https://github.com/waldur/waldur-helm/compare/8.0.9-rc.12...8.0.9-rc.13) - Metrics exporter image is now overridable.

---

## 8.0.9-rc.12 - 2026-05-19

This release focuses on reliability improvements across OpenStack networking, SLURM policy enforcement, and marketplace offering management. OpenStack floating IP attachment now fails fast and with clear error messages when encountering invalid or missing network port data, preventing silent failures. SLURM periodic policy handling is more stable, and several marketplace API correctness issues have been resolved.

### Bug Fixes

- **OpenStack floating IP attachment error handling**: Improved error handling when attaching floating IPs — the system now fails immediately if a port has no backend ID, and raises a clear error when Neutron reports the port as not found, rather than silently failing or producing confusing state.
- **SLURM periodic policy feedback loops**: Fixed an issue where SLURM periodic policies could trigger unintended feedback loops when updating `resource.limits` or resetting raw usage, causing repeated or conflicting policy evaluations.
- **Offering component limit period preservation**: Fixed a serialization issue where the limit period of an offering component was not preserved correctly when updating the component.
- **Offering `backend_id` field update**: Fixed an issue that prevented updating the `backend_id` field of an offering via API call.

### Core Component Activity

- **Waldur Mastermind**: [5 commits](https://github.com/waldur/waldur-mastermind/compare/8.0.9-rc.11...8.0.9-rc.12) - bug fixes for OpenStack floating IP handling, SLURM policy stability, and marketplace serialization correctness.

### Resources

---

## 8.0.9-rc.11 - 2026-05-19

This release candidate introduces resource limit change requests, allowing users to formally request quota adjustments that go through an approval workflow with email notifications. Authentication has been hardened with a secure one-time token exchange mechanism replacing direct token handling in OAuth/SAML callbacks. OpenStack operators gain per-instance config drive control, and the call management module now supports duplicating existing calls with all their configuration intact.

### What's New

- **Resource limit change requests**: Users can now submit requests to change resource limits, which go through an approval workflow. Notifications are sent to relevant parties when a request is created, approved, or rejected.
- **Per-instance OpenStack config drive**: Each OpenStack instance can now have its config drive setting overridden individually at provisioning time, independent of the offering default. The default is also exposed on public offerings so users can see it before deploying.
- **Duplicate call action**: Protected calls in the proposal/call management module can now be duplicated via a new action and wizard dialog, carrying over rounds, offerings, role mappings, and resource templates.
- **Likert scale and Rich text checklist questions**: Two new question types are available in checklists — Likert scale (for rating-style questions) and Rich text (for formatted free-text answers).
- **Bulk round creation**: Multiple proposal rounds can now be created in a single API call using the new `rounds_bulk_set` action.

### Improvements

- **Secure token exchange for authentication**: OAuth and SAML login callbacks now exchange tokens via short-lived one-time codes rather than passing tokens directly, improving security for SSO flows.
- **Zammad comment detection by author identity**: Waldur-originated Zammad comments are now identified by the author's identity rather than a body marker, making comment tracking more robust.
- **Proposal rounds pagination**: The rounds list endpoint is now paginated, preventing slow responses on calls with many rounds.
- **UX audit fixes**: Seven UX issues were addressed across settings pages, including auto-provisioning rules, cost policies, offering configuration sections, order details, and table toolbar controls.
- **Custom event renderers for OpenStack firewall resources**: Audit log events for OpenStack firewall-like resources now display with richer, contextual detail in the event timeline.
- **Old SLURM module removed**: The legacy standalone SLURM frontend module has been cleaned up; SLURM resources are now handled through the standard marketplace resource flows.

### Bug Fixes

- **Constance admin dropdowns**: Choice and multiple-choice configuration fields now render correctly in the admin interface.
- **Checklist PATCH whitelist bypass**: A security fix prevents per-type field whitelists from being bypassed when updating min/max and file fields via PATCH.
- **Permission deletion for resource-scoped roles**: Deleting permissions for resource-scoped roles now correctly passes the project ID, fixing cases where the delete action was incorrectly blocked.
- **Celery-beat stale DB connection recovery**: Background task locking now recovers gracefully from stale database connections instead of failing silently.
- **Usage-based component validation**: Value checks are skipped for usage-based components, preventing incorrect validation errors during usage reporting.

### Core Component Activity

- **Waldur Mastermind**: [17 commits](https://github.com/waldur/waldur-mastermind/compare/8.0.9-rc.10...8.0.9-rc.11) - resource limit change requests, config drive support, auth token exchange, checklist question types, proposal round improvements, and bug fixes
- **Waldur Homeport**: [10 commits](https://github.com/waldur/waldur-homeport/compare/8.0.9-rc.10...8.0.9-rc.11) - matching UI for all backend features plus UX audit fixes and legacy SLURM module cleanup

### Resources

---

## 8.0.9-rc.10 - 2026-05-16

### Highlights

This release brings several productivity boosts for project teams and service providers: marketplace orders can now be auto-approved on a per-project basis, autoprovisioning rules can be tested before deployment, and personal access tokens can be scoped to specific entities for tighter security. Operators gain better visibility into OpenStack firewall changes through aggregate audit logging, plus several hardening fixes addressing IDOR, SSRF, and privileged endpoint exposure.

### What's New

- **Per-project marketplace order auto-approval (WAL-9936)**: Project administrators can now configure auto-approval rules for marketplace orders directly from project Settings, with corresponding filters and notices added across the orders list, order summary, and deploy pages.
- **Dry-run test-match for autoprovisioning rules (WAL-9930 / WAL-9931)**: Operators can now test autoprovisioning rules against sample users before activating them, with a dedicated diagnostics dialog showing which users would match.
- **Entity-scope bindings for personal access tokens**: Personal access tokens can be restricted to specific entities (projects, organizations, etc.), and list responses are filtered accordingly when accessed via a scoped PAT.
- **Aggregate audit logging for OpenStack firewall resources**: Security group, port, and load balancer changes now emit consolidated audit events, making it easier to track network policy changes.
- **Bidirectional offering type swap (Basic ↔ Slurm)**: Service providers can change an existing offering between Basic and Slurm types via a new row action.
- **Offering groups for service providers (WAL-9759)**: A new offering groups tab and set-group action lets providers organize their offerings into named groups.
- **Paginated user affiliation stats**: The affiliation details table now uses backend pagination, improving load performance for large organizations.
- **Service provider offering types endpoint (WAL-7805)**: New `offering_types` action exposes available offering types per service provider.
- **Site agent diagnostics collection (WAL-9263)**: Offering dashboards now surface diagnostics collected from the site agent.
- **Helm: existing secret for read-only DB password (WAL-9934)**: Helm chart now supports referencing an existing secret for the read-only database password.

### Improvements

- Self-healing of the marketplace model during OpenStack tenant sync recovers from drift automatically (ONS-1175).
- OpenStack instance creation errors are now surfaced with more context, and IP-conflict port creation returns a human-readable message instead of a raw exception.
- STOMP publish-failure logs are deduplicated during outages to reduce log noise.
- DonutChart now expands the "Other" slice with a per-item breakdown in its tooltip.
- "Change limits" action is always shown with an explanatory tooltip when disabled, instead of being hidden.
- Order error dialog now shows a helpful hint when the traceback is hidden from the viewer.
- Experimental "What-if" / "Why-so" analytics actions are hidden behind a feature flag.
- Continued migration of forms (credits, Rancher templates, offering imports, LBaaS dialogs, roles, proposals, and more) to react-final-form for consistency and reliability.

### Bug Fixes

- Fixed IDOR vulnerability allowing unauthorized access to invoice costs (SEC-C5).
- Blocked SSRF attacks via webhook destination URLs (SEC-C9).
- Restricted `/api/query/` endpoint to staff users only (SEC-C10).
- Fixed `refresh_instance_backend_metadata` to correctly iterate OpenStack instances.
- Fixed `AttributeError` in `ProtectedCallViewSet.detach_documents`.
- Fixed missing required-field validation in project metadata checklist.
- Fixed structlog traceback formatting for stdlib loggers.
- Bumped `systeminformation` to address GHSA-hvx9-hwr7-wjj9.

### Core Component Activity

- **Waldur Mastermind**: [22 commits](https://github.com/waldur/waldur-mastermind/compare/8.0.9-rc.9...8.0.9-rc.10) - new auto-approval, autoprovisioning, and PAT scoping features plus security hardening (SEC-C5/C9/C10).
- **Waldur Homeport**: [18 commits](https://github.com/waldur/waldur-homeport/compare/8.0.9-rc.9...8.0.9-rc.10) - UI for new backend features, continued react-final-form migration, and several UX polish items.
- **Waldur Helm**: [1 commit](https://github.com/waldur/waldur-helm/compare/8.0.9-rc.9...8.0.9-rc.10) - support for existing secret reference for read-only DB password.

---

## 8.0.9-rc.9 - 2026-05-12

### Highlights

This release introduces SCIM 2.0 identity management, enabling enterprise customers to provision and synchronize users and groups from external identity providers. Operators gain new batch actions to manage project and resource end dates across multiple items at once, and a new OfferingGroup model lets marketplace administrators organize related offerings together. Several reliability fixes address OpenStack RBAC sync crashes, support backend stability, and noisy error logging.

### What's New

- SCIM 2.0 identity management is now available, with both a server endpoint for external identity providers to push users and groups, and a pull client plus management command for synchronizing users from upstream SCIM sources.
- Marketplace administrators can now group related offerings together using the new OfferingGroup model, with admin, API, and filtering support.
- Operators can batch-set or clear the end date for multiple projects at once from the project list.
- Operators can batch-set or clear the termination date for multiple marketplace resources at once from the resource list.
- User details view now exposes the user's birthdate field.

### Improvements

- External-network and configuration failures during marketplace and Arrow task execution are now logged at WARNING level instead of ERROR, reducing noise from expected transient conditions.

### Bug Fixes

- Fixed a duplicate-key crash during OpenStack RBAC policy synchronization when OpenStack recreates a policy with the same identifier.
- Resolved conflicting marketplace migrations introduced alongside the OfferingGroup model.
- Issue serialization no longer fails when a support issue references a stale resource content type.
- SMAX support backend calls are now guarded against `None` entity_id values, preventing crashes when processing incomplete issue data.

### Core Component Activity

- **Waldur Mastermind**: [7 commits](https://github.com/waldur/waldur-mastermind/compare/8.0.9-rc.8...8.0.9-rc.9) - SCIM 2.0 identity management, OfferingGroup model, support and OpenStack stability fixes.
- **Waldur Homeport**: [4 commits](https://github.com/waldur/waldur-homeport/compare/8.0.9-rc.8...8.0.9-rc.9) - Batch end-date actions for projects and resources, plus user birthdate exposure.

---

## 8.0.9-rc.8 - 2026-05-12

### Highlights

This release introduces an experimental Spending & limits watch section on the project dashboard, giving teams clearer visibility into credit terms, pacing, and cost breakdowns. Resource lifecycle handling is more robust: expired resource terminations are now attributed independently, marketplace actions no longer fail for unlinked plugin resources, and total component usage is reported correctly when user-level usages are populated. Security and stability also improve with urllib3 and mermaid upgrades to address CVEs, plus a fix for an OIDC login edge case.

### What's New

- Project dashboards now include an experimental Spending & limits watch section with credit terms, pacing indicators, and breakdown, health, matrix, spend, and timeline views.
- The hpc_ai_platform demo preset has been extended to cover credits, invoices, and cost policies, making it easier to showcase end-to-end financial workflows.

### Improvements

- Project PATCH requests no longer require mandatory fields when those fields aren't being changed, simplifying partial updates.
- Truncated table cells now show the full value as a tooltip on hover in pending consumer and provider order drawers (WAL-9916).
- Site Agent SLURM partition handling is now documented for marketplace operators (WAL-9925).
- Frontend forms across customer, marketplace, OpenStack, proposals, Rancher, and project management have been migrated to react-final-form for consistency.

### Bug Fixes

- Fixed an attribute error encountered during the first-revision OIDC login path.
- Fixed total component usage incorrectly reporting zero when per-user usages were non-zero.
- Each expired resource termination is now attributed independently, preventing one failure from affecting the whole batch (WAL-9926).
- Marketplace resource actions (edit end date, pull, change limits, renew allocation) no longer return 404 errors for resources without a linked plugin.

### Security

- Bumped urllib3 to 2.7.0 in the backend to address known CVEs.
- Bumped mermaid to ^11.15.0 in the frontend to address OSV-scanner vulnerabilities.

### Core Component Activity

- **Waldur Mastermind**: [7 commits](https://github.com/waldur/waldur-mastermind/compare/8.0.9-rc.7...8.0.9-rc.8) - bug fixes for OIDC login and usage reporting, independent expired-resource termination, expanded HPC AI demo preset, and a urllib3 security bump.
- **Waldur Homeport**: [5 commits](https://github.com/waldur/waldur-homeport/compare/8.0.9-rc.7...8.0.9-rc.8) - new experimental project spending watch section, marketplace action 404 fixes, table tooltip improvement, react-final-form migration, and mermaid security bump.

---

## 8.0.9-rc.7 - 2026-05-11

### Highlights

This release candidate delegates more permission-management authority to customer owners and removes redundant work from remote resource synchronization. Customer owners can now act on project-scoped permission requests without escalating to higher-level admins, and remote resource pulls avoid fetching the same data twice.

### Improvements

- Customer owners can now approve or reject permission requests scoped to projects within their customer, reducing reliance on staff or higher-tier roles for routine access decisions.
- Remote resource pulls no longer fetch the same remote resource twice during a single pull cycle, lowering API load and speeding up synchronization.

### Core Component Activity

- **Waldur Mastermind**: [2 commits](https://github.com/waldur/waldur-mastermind/compare/8.0.9-rc.6...8.0.9-rc.7) - expanded customer owner permissions and optimized remote resource fetching.

---

## 8.0.9-rc.6 - 2026-05-11

### Highlights

This release expands ResourceProject lifecycle management with per-offering auto-approval, soft-delete with restore, and staff tools to adjust prepaid resource dates. Operators get visibility into termination metadata and audit fields, while several stability and security fixes (notification email handling, Django CVE patches, and a hotfix for LDAP-based deployments) make this candidate safer to roll out.

### What's New

- ResourceProjects now support per-offering auto-approval and soft delete, with new UI for the auto-OK toggle, staff-only force-delete, and a restore dialog for terminated projects. Termination metadata and soft-delete audit fields are also exposed on the API so operators can see who terminated what and when. ([WAL-9922])
- Staff can adjust start and end dates of prepaid resources directly from the resource actions menu, via a new staff-only `adjust_dates` API action and matching dialog in the UI. ([WAL-9921])
- Prepaid `ONE_TIME` components can now be selected as ResourceProject limits and are shown as such in the project form.

### Improvements

- Notification email recipients are no longer truncated when saving customer details — all entries are now preserved correctly. ([WAL-9919])
- SAML2 and other extension settings are now re-applied after operator `override.conf.py` files load, so deployment overrides no longer silently lose extension config. ([gh-83])
- ResourceProject member management no longer crashes when event hooks are active. ([WAL-9922])
- Site-agent log cleanup task fixed to use the correct related-name lookup. ([WAL-9263])
- Backend dependency hygiene: replaced `iptools` with the Python standard library `ipaddress`, removed 8 unused dependencies, and restored `django-auth-ldap` to avoid breaking LDAP-based operator deployments.

### Security

- Bumped Django to 6.0.5 to address CVEs flagged by osv-scanner.
- Bumped `fast-uri` in the frontend to address GHSA-q3j6-qgpj-74h6. ([WAL-9920])

### Core Component Activity

- **Waldur Mastermind**: [14 commits](https://github.com/waldur/waldur-mastermind/compare/8.0.9-rc.5...8.0.9-rc.6) - ResourceProject auto-OK and soft delete, prepaid date adjustments, Django CVE patch, and dependency cleanup.
- **Waldur Homeport**: [8 commits](https://github.com/waldur/waldur-homeport/compare/8.0.9-rc.5...8.0.9-rc.6) - UI for ResourceProject auto-OK/restore and prepaid date adjustments, notification email fix, plus form and test framework migrations (redux-form → react-final-form, enzyme → react-testing-library).

---

## 8.0.9-rc.5 - 2026-05-08

### Highlights

This release candidate brings a major redesign of organization affiliations, new proposal workflow step tracking, and substantial improvements to usage visualization across customer and project dashboards. Operators get site-agent diagnostics collection and Traefik ingress support in Helm, while OpenStack users benefit from several reliability fixes around instance creation, server groups, and rescue images. Numerous form modernizations and small UX fixes round out the release.

### What's New

- Affiliation redesign rolls out across the stack: per-customer default affiliations, a single foreign key on projects, optional mandatory enforcement, a new project-create field, and a customer admin panel for managing defaults.
- Proposal workflow step tracking lets call managers define ordered, role-responsible workflow steps and track active step per proposal.
- Site agent diagnostics collection: operators can now request and view diagnostic logs from connected site agents.
- Helpdesk tickets are automatically created on resource and resource-project role changes.
- Traefik ingress class with Middleware CRDs is now supported in the Helm chart.
- New per-offering usage widget overhaul on customer and project dashboards, including aggregate timeline, gauge grid, limit horizon, period-over-period, and treemap views.

### Improvements

- Per-offering usage stats moved fully into the marketplace API, simplifying the data model.
- Project members can now create OpenStack tenants directly via the marketplace.
- Affiliated-organizations list now supports `?field=` projection for lighter responses; project serializer exposes flat `affiliation_name`/`code`.
- Pull tasks are skipped for service settings without live offerings, reducing background load.
- StateMixin `begin_*` transitions are now idempotent from the target state.
- Existing ports beyond `status=DOWN` are accepted on instance create / `update_ports`.
- OfferingUser caching refactored to use ListSerializer context for fewer queries.
- Rescue-tagged OpenStack images are rejected as VM boot images and hidden from the homeport boot-image picker.
- Usage chart y-axis uses compact notation; resource usage history renders as bars with empty limit series hidden.
- Terminate orders fall back to resource name and show project/customer names in the confirmation popup.
- Clarified `HOMEPORT_URL` impact on SSO redirect callbacks in provider configuration.
- Front-end forms continue migration from redux-form to react-final-form (offerings, plans, components, payments, campaigns, broadcasts, attributes, endpoints, payment profiles).
- Security: bumped `uuid` (GHSA-w5hq-g745-h8pq) and `marked` (GHSA-6v9c-7cg6-27q7).

### Bug Fixes

- Fixed OpenStack instance creation race against `pull_tenant_ports`.
- Fixed OpenStack server group creation and pull against newer Nova API.
- Service provider deletion is no longer blocked by auto-created OpenStack child offerings.
- Permission request notification link now points correctly for approvers; customer owners now see approve/reject buttons on permission requests.
- Offering import handles a null TOS link without errors.
- OpenPortal report filters no longer 500 when configuration is unavailable.
- One-time components can be created without enabling the prepaid toggle.
- Order checkout sidebar no longer shows daily totals with a monthly tag.
- Restored the language selector in the logged-in user dropdown.
- Limit-period usage charts no longer render a misleading "Limit: 0" tooltip row.
- Init scripts that depended on missing `wget` are fixed.

### Core Component Activity

- **Waldur Mastermind**: [26 commits](https://github.com/waldur/waldur-mastermind/compare/8.0.8...8.0.9-rc.5) - affiliation redesign, proposal workflow steps, site-agent diagnostics, OpenStack reliability fixes.
- **Waldur Homeport**: [26 commits](https://github.com/waldur/waldur-homeport/compare/8.0.8...8.0.9-rc.5) - usage widget overhaul, affiliation UI, large redux-form to react-final-form migration, several UX fixes.
- **Waldur Helm**: [5 commits](https://github.com/waldur/waldur-helm/compare/8.0.8...8.0.9-rc.5) - Traefik ingress class with Middleware CRDs.
- **Waldur Docker Compose**: [4 commits](https://github.com/waldur/waldur-docker-compose/compare/8.0.8...8.0.9-rc.5) - maintenance updates only.

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


---


# Changelog

## 8.1.4-rc.5 - 2026-10-28

### Highlights

This release tightens calls for proposals. Archived calls stop accepting applications, and calls now enforce their resource templates and required offering options before a proposal can be submitted or awarded. Staff can pay a project's earlier invoices from its credit, cost policies explain why they are over their limit, and credit-aware policies now trigger on the correct amount. Customers can be asked for feedback through surveys shown after login, and OpenStack tenants can use networks shared with every project from the moment the tenant is created.

### What's New

- Staff can create feedback surveys that customers are asked to answer after they log in, and can review the answers in the feedback logs.
- Staff can pay a project's earlier invoices from its credit, with a preview of the invoices that will be covered.
- Cost policies have a details view that explains why a policy is over its limit, which resources it affects and how to resolve it.
- The resource metrics tab shows OpenStack instance and volume metrics, along with how often they are updated.

### Improvements

- Calls that have resource templates require applicants to use them. Call managers can limit a call to one template, and applicants then pick a single template when they add a proposal.
- Proposals must fill in the options an offering requires before they can be submitted or awarded. The chosen options appear in the review, the proposal PDF and the award.
- Archived calls refuse new proposals, are left out of the open calls list and are shown as closed to applications.
- Networks that a provider shares with every project are treated as shared with each OpenStack tenant, starting when the tenant is created. The VM creation form fills the first network with a tenant subnet and marks subnets that the provider shares.
- Webhook certificate errors now list every cause of the failure, including untrusted certificates. The configuration guide and the Helm documentation explain how to trust a private CA through a mounted trust bundle.
- Only the metric roll-ups that new data points affect are recomputed.
- Applied table filters show their values as tags.
- Frequently used forms track only the fields they need, which reduces unnecessary re-rendering.
- More of the UI moved from Bootstrap to Tailwind. This covers spacing, layout and flex utilities, and the Arrow administration tables.
- dnspython, msgpack and qs were updated to fix published security advisories.

### Bug Fixes

- Credit-aware cost policies now trigger on the cost left after credit is applied, not on the remaining credit balance.
- A VM's network interfaces now come up in the same order as its requested ports.
- A call's slug template stays locked when an API request clears it.
- Validating a call that already exists no longer crashes.
- The science domain selector now appears on proposals whose call asks for it.
- Gaps between stacked elements display correctly again. For example, the hypervisor summary charts no longer touch each other.

### Core Component Activity

- **Waldur Mastermind**: [15 commits](https://github.com/waldur/waldur-mastermind/compare/8.1.4-rc.4...8.1.4-rc.5) - Feedback surveys, paying earlier invoices from project credit, credit-aware cost policy fix, stricter call and proposal checks, OpenStack shared network handling and clearer webhook certificate errors.
- **Waldur Homeport**: [19 commits](https://github.com/waldur/waldur-homeport/compare/8.1.4-rc.4...8.1.4-rc.5) - Feedback survey UI, cost policy explanations, required options and templates in proposals, OpenStack metrics display and continued Tailwind migration.
- **Waldur Helm**: [1 commit](https://github.com/waldur/waldur-helm/compare/8.1.4-rc.4...8.1.4-rc.5) - Documentation on trusting a private CA through a mounted trust bundle.

---

## 8.1.4-rc.4 - 2026-10-27

### Highlights

This release adds site-wide roles. Staff can now define and grant permissions that cover the whole deployment instead of a single organization or project. Table and chart PDF exports are now produced on the server, and OpenStack instance and volume metrics are collected on a schedule. The release also hardens authentication (SAML, logout, Mobile ID), Rancher access control and support-user permissions, and removes the Google Calendar integration.

### What's New

- Staff can create roles with a global, site-wide scope and grant them from the role management and user affiliation screens. `scope_type` filters now match the public scope names.
- Table and chart PDF exports are now rendered on the server with Typst instead of in the browser.
- OpenStack instance and volume metrics are read from Nova on a schedule.
- Staff can cap the API token lifetime that non-staff users may choose, and the token lifetime selector offers only the allowed values.
- Resource templates in proposal calls support a single-selection mode.
- The helpdesk is emailed when an organization or project administrator comments on a support request.
- Staff can set another user's email address directly.

### Security and Access Control

- Logging out now ends the server session and revokes the API token.
- SAML responses are verified only with identity provider keys from metadata. A deployment's own `SAML_CONFIG` settings are preserved, and unsolicited SAML responses are accepted by default.
- The Mobile ID client now verifies TLS certificates, applies timeouts and keeps credentials out of logs.
- Terms of Service acceptance is recorded only when users accept it themselves through the Terms checkbox, and each acceptance is logged.
- Managing Rancher Keycloak group memberships requires project administrator access, and Rancher catalog changes are limited to staff and project administrators.
- The Rancher sync binds Keycloak groups only to their own cluster or project, and managed Rancher clusters get public IPs only from their own load balancers.
- Support users have read-only access to other users' hooks and onboarding records, and staff-only pages are hidden from them.
- An onboarding verification's company is locked once it is verified or escalated.
- Register checks go to manual review when the identity was typed in, and the organization creation form tells users so.

### Improvements

- Map location search runs when you press Enter instead of querying Nominatim as you type.
- Issue comments display better on mobile, with more space between comments.
- Destroy-dialog warnings for OpenStack tenants and Rancher clusters can now be translated.
- Dependencies were cleaned up:
  - The admin JSON editor is now a built-in widget.
  - django-fsm was replaced by django-fsm-2.
  - Unused runtime packages were dropped.
  - react-arborist was replaced by a local read-only tree view.
- More of the UI moved from legacy Metronic styles to Tailwind, covering avatars, timelines, icons, flex layouts and tables.

### Bug Fixes

- Fixed staff edits to user email addresses. Locked profile fields now depend on the user being edited.
- Users whose username contains uppercase letters can now be edited.
- A Jira deletion event deletes a support issue only when Jira reports the issue as not found.

### Removed

- The Google Calendar integration is gone, including its publish, sync and unpublish actions and the calendar link on offerings.

### Core Component Activity

- **Waldur Mastermind**: [32 commits](https://github.com/waldur/waldur-mastermind/compare/8.1.4-rc.3...8.1.4-rc.4) - Site-wide roles, server-side PDF export, scheduled OpenStack metrics, authentication, Rancher and onboarding hardening, and removal of Google Calendar.
- **Waldur Homeport**: [26 commits](https://github.com/waldur/waldur-homeport/compare/8.1.4-rc.3...8.1.4-rc.4) - UI for site-wide roles and token lifetime limits, PDF export through the server, staff-only pages hidden from support users, and continued Tailwind migration.

---

## 8.1.4-rc.3 - 2026-10-24

### Highlights

Customers can now cap what a usage-based resource spends per day, week, month, quarter or year, or over its whole lifetime. They can change those caps at any time without placing an order. Resource API keys get the same per-period limits and can now be managed by project managers and administrators. Keys are also handled more safely: a key stays with the person it was issued to, and a deleted user's keys are withdrawn instead of being shared. OpenStack instances gain a hard reboot action, and logging out now revokes the stored identity provider token.

### What's New

- **Per-period spending limits**: Providers choose which periods customers may cap on a usage-based component: day, week, month, quarter, year, or an all-time limit that never resets. Each period can have a default and a maximum. Customers set limits when they order and can change them later with a new "Change spending limits" action, with no order or approval needed. When a limit is reached, the offering's usage-limit action applies until the limit resets. The order form and the dialog say whether that action pauses the resource, downscales it or only reports the overspend.
- **Spending limit status**: The Usage tab and the resource's components panel show usage against the limit for each period, when each limit resets and why access is paused. The API keys tab names the limit that is holding a paused resource and says when access resumes.
- **Daily usage reports**: Integrations can report usage per day, and the month's usage is derived from the daily figures. One report can hold at most 1000 items.
- **API key limits per period**: A resource API key can have its own limit for each period. A key's limit can't be higher than the resource's limit for that period or any longer one. Per offering, providers decide whether consumers may limit keys at all, and whether the site agent reports each key's usage per day. Key limits for periods other than the month are only offered when it does. Keys can also be limited on a component that the plan prices at zero, such as a LiteLLM USD cap.
- **API key management for project roles**: A new permission, RESOURCE.MANAGE_CONSUMER_API_KEY ("Manage API keys of resources used by the project or organization"), is granted to organization owners, project administrators and project managers. These roles can now lower a key's cap, pause a leaked key or delete a departed member's key.
- **OpenStack hard reboot**: OpenStack instances have a new hard reboot action, available from the API and the portal.
- **Role assignment from a user's page**: Staff can grant a user a role directly from the user's affiliations. A role's user listing now also includes users who hold organization copies of that role.

### Improvements

- **API key limit enforcement**: If the site agent fails to apply a limit pause, Waldur retries it, waiting longer after each failure, from 5 minutes up to 6 hours. A key paused at its own limit stays paused while its resource is restricted by the resource's spending limit. Key limits are checked again when they are saved, and audit events record the old and new values.
- **API key usage data**: A key's daily usage reports are limited in size and in how far back they can go. Each key reads only the daily usage its limits need, and old daily usage is deleted. Older clients that send the flat monthly `limits` field get the amount rounded up to the cent instead of an error.
- **API key dialogs**: The key dialogs offer only the periods that the resource's plan allows. A limit the key already holds is accepted only if it is left unchanged. Rotate is blocked once any of the key's limits is reached, and the tooltips name that limit and say when the key resumes.
- **Prepaid components**: Prepaid limits are shown as one total for the whole subscription. Only one-time components can be prepaid, and the component form no longer saves prepaid settings that it hides.
- **Service accounts**: Service accounts are closed only once a project's deletion has completed. Accounts that are already closed are treated as closed, and accounts left over from removed projects are cleaned up.
- **Cost policies and credits**: An organization cost policy now deducts only usage compensation. Changing a credit's offering list now re-evaluates the organizations whose credits changed.
- **Accessibility**: Header and footer link menus open and close from the keyboard. The project filter announces the selected project by name. Focus stays in the tab row when a table tab switches the page.
- **Smaller UI touches**: Revisiting a page no longer flashes a loading spinner. Per-offering usage views choose the component type from a select instead of tabs. Long offering descriptions are truncated in the Add resource dialog. The error page and the order steps fit mobile screens, and on small screens New chat closes the AI assistant history. The unused reason field has been removed from the offering availability dialog.
- **Demo presets**: Each demo preset resource is billed once in the current month, and the tenants in the openstack_cloud preset can now be ordered.
- **Interface migration**: More portal code moved from Bootstrap and lodash to Tailwind and es-toolkit. Form controls moved to a shared waldur-form package, and tables no longer depend on UI-Router.
- **Dependency updates**: Backend packages (Django REST framework, fastmcp-slim, setuptools) and frontend packages (dompurify, zod, fast-uri, undici) were updated to fix security advisories.

### Security

- **Fixed API key holders**: A key's assignee is set when the key is requested and can no longer be changed. To hand a key over, request one for the new holder and delete the old one. The Unassign action and the assignee field have been removed from the portal.
- **Deleted users' keys**: Deleting a user now withdraws their API keys. Before, those keys became shared keys that any project member could reveal.
- **Key reveal**: Staff and support can no longer reveal resource API keys directly, and the portal shows Reveal only where the API allows it.
- **Identity provider tokens**: The stored identity provider token is revoked and removed when a user logs out, is deactivated or is deleted.

### Bug Fixes

- Resources paused by a project grace period or a cost policy are now also marked as restricted by their usage limit. Before, they could be resumed while still over their spending limit.
- OpenStack instance actions stop waiting for completion when Nova reports ERROR.
- Erred resources are labelled Erred instead of OK.
- The Change spending limits dialog highlights the limit the backend refused. Long reset descriptions no longer squeeze the input fields.
- Multi-select fields keep their input when the first value is selected. Table cell padding is restored. Organization credit is formatted correctly in the project credit dialog. Wizard step indicators navigate and display correctly.
- Nested table toolbars no longer show a Filter button that did nothing.
- The specific error messages for duplicate active affiliates and offering Terms of Service are kept after the Django REST framework upgrade.
- Service provider revenue is returned with its fractional part.
- The Helm chart drops the broken PayPal feature and fixes dead documentation links.

### Core Component Activity

- **Waldur Mastermind**: [46 commits](https://github.com/waldur/waldur-mastermind/compare/8.1.4-rc.2...8.1.4-rc.3) - Per-period spending limits and daily usage, per-period API key limits with pause retries and cleanup of old usage data, the consumer API key permission, fixed key assignees, identity provider token revocation, OpenStack hard reboot, and fixes for prepaid components, service accounts and cost policies.
- **Waldur Homeport**: [87 commits](https://github.com/waldur/waldur-homeport/compare/8.1.4-rc.2...8.1.4-rc.3) - UI for spending limits, API key limits and the new key permission, OpenStack hard reboot, staff role assignment, prepaid totals and accessibility fixes. Also the new waldur-form package, the move off lodash and more of the Bootstrap-to-Tailwind migration.
- **Waldur Helm**: [1 commit](https://github.com/waldur/waldur-helm/compare/8.1.4-rc.2...8.1.4-rc.3) - Removed the broken PayPal feature and fixed dead documentation links.

---

## 8.1.4-rc.2 - 2026-10-22

### Highlights

Cost policies now explain themselves. Waldur shows why each policy fires or waits, records what started each evaluation and which gate decided it, and keeps a version history of policy changes. Resource API keys are easier to manage: you can pick "All models" explicitly, the person a key is assigned to can rotate it, and the site agent is told when a key changes hands. Organization owners and readers get access to organization reporting through a new permission, and platform settings now live in a built-in settings store instead of django-constance.

### What's New

- **Cost policy status**: Each cost policy now reports why it fires or is waiting. The policy list shows this as a single status badge and lists the organization credit only once. The project's "what happens next" view says when a credit is holding a policy back.
- **Cost policy audit trail**: Waldur records what started each cost policy evaluation, who started it, and which gate decided the outcome. Project credit changes made by staff now appear in the project's audit log.
- **Version history**: Cost policies and projects now keep a version history. You can open a policy's history from its actions, and staff and support can open a project's history from the project list.
- **Organization reporting permission**: A new permission, CUSTOMER.VIEW_REPORTING, gives access to organization reporting. Organization owners and readers have it.
- **MCP server groundwork**: Waldur now includes an early skeleton of a Model Context Protocol (MCP) server. It authenticates with personal access tokens and is started with the `mcp_server` management command.
- **Project resources at a glance**: You can expand a project in the organization project list to see its resources.
- **SLURM placement in proposals**: Proposal resource requests now show the SLURM QoS and partition.

### Improvements

- **Resource API key models**: An empty model list on an API key now means no models, and `*` means every model. API key dialogs have a new "All models" checkbox.
- **Resource API key management**: The person a key is assigned to can rotate it from the resource page. Each person can hold only one API key per resource. The site agent is notified when a key is reassigned. The API keys tab now appears on managed resources even before they have any keys.
- **Settings store**: Platform settings have moved from django-constance to a built-in settings store, and a migration imports existing settings. The Helm Matrix cleanup now works with whichever settings table is present.
- **AI assistant**: Chat tools now check tool sets and roles themselves. The anonymous marketplace discovery chat has new access-guidance rules, and its KPIs show how often searches return no results.
- **Support requests**: Ticket comments now go to the backend the ticket belongs to, and fail gracefully if that backend can't take them. Support requests opened from an offering no longer use the offering's provider as the organization, and the caller can follow the request.
- **Notification settings**: Notification event groups now have readable titles, descriptions and sections.
- **Maintenance badges**: A maintenance window that is currently open shows as in progress, and its badge sits on its own line in the resource list.
- **Tables**: Tables page through the rows they already hold, and short lists no longer show a pager.
- **Page loading**: A loading bar shows while you move between pages. The startup splash screen is branded and has slow-loading and error states.
- **Privacy and impersonation**: The user Audit log tab and IP column are hidden from viewers who aren't allowed to read them. Staff impersonating a user can see the user's API token even when it is concealed.
- **Smaller UI touches**: OpenStack subnets without a name show their CIDR instead. The project hero bar now works as navigation rather than tabs. The affiliation dialog requires the start date to be before the end date. Onboarding verification statuses are now capitalized.
- **Interface migration**: The header, breadcrumbs, modals and page layout have moved from Metronic and Bootstrap to shared Waldur UI components and Tailwind.
- **Dependency updates**: Backend libraries (aiohttp, Pillow, certifi, pypdf) and frontend tooling (vite, markdown-it, vitest, Storybook) were updated to fix security advisories.

### Bug Fixes

- Marketplace resources return to the OK state when their backend recovers.
- Resource creation is now checked against the credit gates of the cost policy itself.
- Credit compensations no longer count toward a total limit's billed quantity.
- Event filters by UUID now match events filed on a project's or organization's feed. The credit and access subnet history logs are now read through the organization scope.
- The API now declares the OpenStack instance `server_group` field as nullable.
- Bulk invitations no longer stall when the same email is invited to several projects.
- Fixed a landing page crash ("Converting circular structure to JSON"), and a proposal page crash for staff before the call loads.
- The cookie consent dialog no longer reopens after you close or accept it.

### Core Component Activity

- **Waldur Mastermind**: [31 commits](https://github.com/waldur/waldur-mastermind/compare/8.1.4-rc.1...8.1.4-rc.2) - Cost policy status, evaluation records and history, resource API key rules, CUSTOMER.VIEW_REPORTING, project version history, an MCP server skeleton, the built-in settings store and tighter chat tool checks.
- **Waldur Homeport**: [46 commits](https://github.com/waldur/waldur-homeport/compare/8.1.4-rc.1...8.1.4-rc.2) - UI for cost policy status and history, API key "All models" and rotation, organization reporting access and project version history. Also a new boot splash and loading bar, and the move of the header, breadcrumbs, modals and layout to Waldur UI.
- **Waldur Helm**: [1 commit](https://github.com/waldur/waldur-helm/compare/8.1.4-rc.1...8.1.4-rc.2) - Matrix settings cleanup now works with the new settings store.

---

## 8.1.4-rc.1 - 2026-10-18

### Highlights

This release lets teams draft support tickets directly from Matrix chat threads and adds EU VAT calculation to invoices. Operators can now send platform events to their own HTTP webhooks and send invoice notifications to dedicated billing addresses. Login security is stronger: OIDC ID tokens are now validated, and security-relevant actions are recorded as audit events. British English is now available as an interface language.

### What's New

- **Support tickets from Matrix chat**: You can now draft a support ticket from a Matrix chat thread, then review and edit the draft in the chat before submitting it. The chat composer also offers commands with an in-chat help dialog.
- **EU VAT on invoices**: Invoices now calculate EU VAT. Organizations have new VAT fields, including a "private person" flag. New admin settings control VAT, and invoice PDFs show the VAT amounts. A new management command refreshes VAT rates.
- **Webhook delivery for event consumers**: Event consumers can now deliver events to an HTTP webhook. You can create and manage these consumers from the pub/sub admin page.
- **Organization invoice emails**: Organizations can set dedicated invoice email addresses, which receive invoice notifications. You can edit them in the organization contact panel, and a notification is sent when they change.
- **British English**: The interface is now offered in British English (en-GB), generated from the US English source strings. Translatable fields such as category and role descriptions can also have en-GB versions.
- **Security audit events**: Audit events are now emitted for security-relevant actions, including SAML2, OIDC and Valimo logins, offering deletion and policy changes.
- **Offering option transforms**: Service providers can configure how offering option values are transformed before they are stored, and preview the result in the option editor.
- **Option as usage limit**: An integer resource option can now be displayed as the limit of a usage-based component on resource and project views.
- **Editable access endpoints**: Offering access endpoints can now be edited after they are created.
- **Call statistics**: Calls now report the number of proposals, reviews and workflow steps per call and per round.
- **Accept invitations on behalf of users**: Staff can accept a user invitation on behalf of a named user.

### Improvements

- **OIDC login validation**: OIDC ID tokens are now validated against the identity provider's JWKS at login. New issuer and JWKS URL settings are available on identity providers.
- **Accounting permission**: A new permission, CUSTOMER.VIEW_ACCOUNTING, controls access to the Accounting section. It is granted to organization owners and to roles cloned from the owner role.
- **OpenPortal feature toggles**: OpenPortal now has separate feature toggles for the sending and receiving portal. Shared OpenPortal pages are hidden when the portal plays neither role.
- **Date entry**: Date pickers now accept dates typed into a masked input field. The project creation dialog prevents choosing an end date before the start date.
- **Resource end dates**: The API now validates resource end dates, and the termination date pickers follow the same rules.
- **Resource actions**: The "Show all" actions dialog is organized into tabs by action group, and duplicate resource actions were removed.
- **Accessibility**: Shared components now have accessible names, keyboard access and sufficient colour contrast. WCAG target-size and link-in-text-block violations were also fixed.
- **Organization onboarding**: Missing Dun & Bradstreet identity fields are now requested inline during onboarding.
- **OpenStack floating IPs**: Floating IPs are disabled on subnets without a router, and the release option is hidden when there are no floating IPs to release.
- **Pending orders**: Orders waiting for the project start date now show provider approval as pending.
- **Interface refresh**: Form inputs, selects and labels now use the Waldur UI component library. Design tokens are standardized, and unused Bootstrap CSS was removed (32% smaller gzipped). Support buttons and tab count badges have a refreshed look.

### Bug Fixes

- OpenStack synchronization now recovers from stale cached Keystone tokens.
- Backend URL validation for OpenStack, Rancher, VMware and marketplace settings now actually runs.
- Links built from HOMEPORT_URL no longer contain double or missing slashes.
- Plain-text issue descriptions and comments now keep their line breaks.
- The organization dashboard shows the organization profile only once, and managed and remote project detail pages no longer appear as provider tabs.
- The Reviews tab in proposal rows stays visible when reviews fail to load.
- Several visual issues were fixed:
  - Brand colour is restored on search and breadcrumb links.
  - Non-scrollable tab strips now wrap.
  - The date picker caption no longer covers the month arrows.
  - The local login link has the right colour in the dark Neumorphism layout.
  - Unintended font weights were removed.
  - Chart target lines stay inside the plot area.

### Core Component Activity

- **Waldur Mastermind**: [28 commits](https://github.com/waldur/waldur-mastermind/compare/8.1.3...8.1.4-rc.1) - Matrix ticket drafts, EU VAT, webhook event consumers, invoice emails, OIDC token validation, audit events, option transforms and en-GB support.
- **Waldur Homeport**: [60 commits](https://github.com/waldur/waldur-homeport/compare/8.1.3...8.1.4-rc.1) - UI for chat tickets and commands, VAT and invoice emails, webhook consumers and option transforms, plus British English, typed date entry, accessibility work and a form/design-token migration.
- **Waldur Helm**: [1 commit](https://github.com/waldur/waldur-helm/compare/8.1.3...8.1.4-rc.1) - Clearer titles for the Helm install and Matrix documentation pages.
- **Waldur Docker Compose**: [1 commit](https://github.com/waldur/waldur-docker-compose/compare/8.1.3...8.1.4-rc.1) - Matrix chat add-on page retitled to name Docker Compose.

---

## 8.1.3 - 2026-10-13

### Highlights

This release makes team chat secure and quick to set up. Every Matrix room is now end-to-end encrypted, and calls are encrypted too. Helm and Docker Compose deployments configure chat automatically, and users can sign in to Matrix clients with single sign-on. Sign-in also gets stronger: users can log in with passkeys, and privileged accounts can be required to use them. Call managers get a full round lifecycle, awards that can differ from the request, and call export and import. Providers can now share user accounts, POSIX identities and project groups across all their offerings.

### What's New

- **Encrypted team chat**: Every Matrix room is created encrypted, and the chat drawer handles encryption, attachments and recovery keys, including keys made in Element. A Waldur bot in every room exports encrypted history and gives new members the room's earlier keys.
- **Chat messaging and calls**: Users can edit, delete and reply to messages. Calls are encrypted end to end, use call tokens issued by Waldur, and show who joined and when in the chat timeline.
- **Matrix setup and SSO**: Helm and Docker Compose now register the appservice, seed the settings and support token rotation, and can configure single sign-on for Matrix clients. Helm adds opt-in alert rules and a metrics ServiceMonitor, and the docs cover monitoring, backup, restore and capacity.
- **Passkeys**: Users can register passkeys and log in with them. Deployments can require passkeys for privileged accounts, and staff can revoke a user's passkeys if they give a reason.
- **Call and proposal management**:
  - Rounds have a lifecycle after the cut-off, and a round's results are published together.
  - The award can differ from what was requested, and decisions on hold can be reopened.
  - Unsubmitted drafts can carry over to the next round.
  - Call configuration can be exported and imported.
  - Proposals and reviews export as CSV, and a single proposal as PDF.
- **Proposal roles and visibility**: New proposal administrator role, a team that freezes after submission, eligibility rules set from the call UI, and notification rules per workflow step. Applicant identity is hidden from evaluators everywhere.
- **Provider accounts**: User accounts and POSIX identities are shared across a provider's offerings. Each project gets one POSIX group per provider, and offerings can inherit account settings from the provider. Providers can also preview what their account settings produce.
- **Billing**:
  - Plans have a billing mode, including prepaid, and one OpenStack offering can offer both a limit plan and a usage plan.
  - Invoice notification emails now include a PDF of the invoice.
  - Credit drawdown is recorded in a ledger, and credit-funded cost policies check the live credit balance.
- **Custom metrics**: Providers define metrics in a catalogue and send in data. Metrics roll up over time, can have goals and break down per resource, and show on project and offering pages.
- **Resource API keys**: Keys are managed one at a time: request, assign, cap, pause, resume and delete. Each key shows its usage and models.
- **Offering merge**: Staff can merge duplicate offerings with a wizard that previews which rows change, runs in the background and can be undone.
- **In-app changelog**: Admins get a changelog page, a footer badge for new releases and a banner for security releases.
- **Identity integrations**: SRAM pushes users and groups over SCIM. Organization roles can be assigned from OIDC claims, and SCIM users are matched to accounts by a configurable attribute.
- **Organization reporting**: Organization owners get reporting views, including a report by affiliated organization.
- **New languages**: Croatian, Macedonian and Albanian.

### Improvements

- **OpenStack**: IPv6 and dual-stack networking across subnets, routers, security groups, load balancers and floating IPs. Networks shared over RBAC by projects Waldur does not manage are shown, and you can choose the router for a new subnet or skip attaching one.
- **Support**:
  - The built-in service desk is now the default backend, with a configurable ticket key prefix.
  - Staff can open a support request on a user's behalf.
  - Authors can edit and delete their own comments.
  - Notification emails are threaded.
- **Offering options**:
  - Options can be shown only when another option has a given value.
  - Free-form values can be checked against a pattern, or required to be unique across resources.
  - Component limits can be derived from formulas.
- **Permissions**: Service provider managers can review orders and report usage. Organization readers get read access. Support users can read call data and settings, with secret values hidden.
- **Security hardening**: Secret Constance settings and offering secret options are encrypted at rest. Uploaded files can no longer run as pages, and credentials are masked in logs.
- **Deployment**:
  - Helm supports Gateway API alongside Ingress, and CloudPirates charts replace the Bitnami subcharts.
  - Helm and Compose both work on IPv6-only and dual-stack clusters.
  - Telemetry can be switched off when deploying.
  - Compose makes outgoing email configurable.
- **UI modernisation**: Menus, tabs, buttons, badges, selects and the date picker now use Tailwind and Radix components, with better keyboard and screen-reader accessibility throughout.
- **Removed integrations**: The Azure integration and the legacy SLURM plugin are gone. Existing Azure VMs are moved to the site agent.

### Bug Fixes

- OIDC users are now found by email regardless of letter case, and bearer token introspection no longer requires a DRF token.
- Fixed:
  - Celery task locks that were never released.
  - FreeIPA errors when a username is already taken.
  - Sentry log scrubbing that broke audit event inserts.
  - Software catalog cleanup deleting distinct EESSI versions.
- Fixed frontend crashes in the usage report dialog, the profile page and menu items rendered outside a menu, and broken file downloads after media permissions were tightened.

### Core Component Activity

- **Waldur Mastermind**: [568 commits](https://github.com/waldur/waldur-mastermind/compare/8.1.2...8.1.3) - Encrypted Matrix chat with a bot, passkeys, call round lifecycle and awards, provider accounts and project groups, billing modes, custom metrics, OpenStack IPv6
- **Waldur Homeport**: [662 commits](https://github.com/waldur/waldur-homeport/compare/8.1.2...8.1.3) - Encrypted chat and calls, passkey UI, call management and provider account screens, changelog page, move to Tailwind/Radix and accessibility work
- **Waldur Helm**: [69 commits](https://github.com/waldur/waldur-helm/compare/8.1.2...8.1.3) - Matrix setup at deploy time with SSO and alerts, Gateway API, CloudPirates subcharts, IPv6/dual-stack, Matrix bot deployment
- **Waldur Docker Compose**: [139 commits](https://github.com/waldur/waldur-docker-compose/compare/8.1.2...8.1.3) - Automatic Matrix setup, SSO, call tokens from Waldur, Matrix operations docs, configurable email, web shell profile

### Resources

- [OpenAPI Schema](../API/waldur-openapi-schema-8.1.3.yaml)

---


























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

- **Waldur Helm**: [38 commits](https://github.com/waldur/waldur-helm/compare/8.0.9...8.1.2) - encryption key wiring, configurable country list, memory tuning values, network policy and ingress fixes.
- **Waldur Docker Compose**: [32 commits](https://github.com/waldur/waldur-docker-compose/compare/8.0.9...8.1.2) - encryption key passthrough, memory tuning environment knobs, and Caddy compression and CSP updates.

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
- **Waldur Helm**: [38 commits](https://github.com/waldur/waldur-helm/compare/8.0.9...8.1.2) - field encryption key wiring, API response compression, matrix network policies, memory tuning values
- **Waldur Docker Compose**: [32 commits](https://github.com/waldur/waldur-docker-compose/compare/8.0.9...8.1.2) - field encryption key, response compression, memory tuning environment knobs

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

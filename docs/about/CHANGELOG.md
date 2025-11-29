# Changelog

## 7.9.0 - 2025-11-29

**Release Notes:** Multi-repository release with enhanced analysis

📈 **Release Impact:** 16 commits across 4 core repositories
📁 **Functional Changes:** 115 files · +1407/-929 lines *(excludes tests, auto-generated files)*
🔄 **SDK Updates:** 3 auto-generated clients updated

🔗 **Core Component Activity:**
- **Waldur Mastermind**: [8 commits](https://github.com/waldur/waldur-mastermind/compare/7.8.9...7.9.0) · 11 files (+377/-7 lines)
- **Waldur Homeport**: [3 commits](https://github.com/waldur/waldur-homeport/compare/7.8.9...7.9.0) · 99 files (+1023/-915 lines)
- **Waldur Helm**: [4 commits](https://github.com/waldur/waldur-helm/compare/7.8.9...7.9.0) · 4 files (+5/-5 lines)
- **Waldur Docker Compose**: [1 commits](https://github.com/waldur/waldur-docker-compose/compare/7.8.9...7.9.0) · 1 files (+2/-2 lines)
- **Waldur Prometheus Exporter**: No changes

🔄 **SDK Updates (Auto-generated):**
- **Python Client**: [3 commits](https://github.com/waldur/py-client/compare/7.8.9...7.9.0)
- **JavaScript Client**: [5 commits](https://github.com/waldur/js-client/compare/7.8.9...7.9.0)
- **Go Client**: [2 commits](https://github.com/waldur/go-client/compare/7.8.9...7.9.0)

**✨ Notable Changes:**
- Expose additional fields for invoice items. *([7385aa4](https://github.com/waldur/waldur-mastermind/commit/7385aa4) - waldur-mastermind)*
- Batch to Fix 4 (Modals, Charts, Metrics, Breadcrumbs, Tabs). *([4fb3221](https://github.com/waldur/waldur-homeport/commit/4fb3221) - waldur-homeport)*
- [WAl-9443] Show review summary on in review proposals. *([46b54e2](https://github.com/waldur/waldur-homeport/commit/46b54e2) - waldur-homeport)*
- Set target version to 7.9.0. *([9d3756c](https://github.com/waldur/waldur-helm/commit/9d3756c) - waldur-helm)*
- Revert "Revert "Remove leftover path modifications"". *([5ee8f11](https://github.com/waldur/waldur-helm/commit/5ee8f11) - waldur-helm)*
- Fix ingress condition. *([63903a7](https://github.com/waldur/waldur-helm/commit/63903a7) - waldur-helm)*
- Revert "Remove leftover path modifications". *([d8dd890](https://github.com/waldur/waldur-helm/commit/d8dd890) - waldur-helm)*
- Set target version to 7.9.0. *([58ceaa9](https://github.com/waldur/waldur-docker-compose/commit/58ceaa9) - waldur-docker-compose)*

**Waldur Mastermind Highlights:**
- Cleanup unused migration.
- Add readonly viewset to list checklists for call organizers.
- Expose additional fields for invoice items.

**📚 Resources:**
- [API Schema](../API/waldur-openapi-schema-7.9.0.yaml)
- [API Changes](../integrator-guide/APIs/api-changes/waldur-openapi-schema-7.9.0-diff.md)
- [Full Release Comparison](https://github.com/waldur/waldur-mastermind/compare/7.8.9...7.9.0)

**⏱️ Released:** 2025-11-29 17:41 UTC

---

## 7.8.9 - 2025-11-29

**Release Notes:** Multi-repository release with enhanced analysis

📈 **Release Impact:** 4 commits across 3 core repositories
📁 **Functional Changes:** 9 files · +245/-40 lines *(excludes tests, auto-generated files)*
🔄 **SDK Updates:** 2 auto-generated clients updated

🔗 **Core Component Activity:**
- **Waldur Mastermind**: [2 commits](https://github.com/waldur/waldur-mastermind/compare/7.8.8...7.8.9) · 6 files (+240/-35 lines)
- **Waldur Homeport**: No changes
- **Waldur Helm**: [1 commits](https://github.com/waldur/waldur-helm/compare/7.8.8...7.8.9) · 2 files (+3/-3 lines)
- **Waldur Docker Compose**: [1 commits](https://github.com/waldur/waldur-docker-compose/compare/7.8.8...7.8.9) · 1 files (+2/-2 lines)
- **Waldur Prometheus Exporter**: No changes

🔄 **SDK Updates (Auto-generated):**
- **Python Client**: [1 commits](https://github.com/waldur/py-client/compare/7.8.8...7.8.9)
- **JavaScript Client**: [1 commits](https://github.com/waldur/js-client/compare/7.8.8...7.8.9)

**✨ Notable Changes:**
- Request deletion of offeringuser upon removal from project. *([9135636](https://github.com/waldur/waldur-mastermind/commit/9135636) - waldur-mastermind)*
- Add validation that resources belong to the same offering for limit reallocation. *([3c8adcd](https://github.com/waldur/waldur-mastermind/commit/3c8adcd) - waldur-mastermind)*
- Set target version to 7.8.9. *([39c5fea](https://github.com/waldur/waldur-helm/commit/39c5fea) - waldur-helm)*
- Set target version to 7.8.9. *([fad7a57](https://github.com/waldur/waldur-docker-compose/commit/fad7a57) - waldur-docker-compose)*

**📚 Resources:**
- [API Schema](../API/waldur-openapi-schema-7.8.9.yaml)
- [API Changes](../integrator-guide/APIs/api-changes/waldur-openapi-schema-7.8.9-diff.md)
- [Full Release Comparison](https://github.com/waldur/waldur-mastermind/compare/7.8.8...7.8.9)

**⏱️ Released:** 2025-11-29 17:42 UTC

---

## 7.8.8 - 2025-11-29

**Release Notes:** Multi-repository release with enhanced analysis

📈 **Release Impact:** 123 commits across 4 core repositories
📁 **Functional Changes:** 668 files · +36184/-3238 lines *(excludes tests, auto-generated files)*
🔄 **SDK Updates:** 3 auto-generated clients updated

🔗 **Core Component Activity:**
- **Waldur Mastermind**: [74 commits](https://github.com/waldur/waldur-mastermind/compare/7.8.7...7.8.8) · 118 files (+22512/-916 lines)
- **Waldur Homeport**: [31 commits](https://github.com/waldur/waldur-homeport/compare/7.8.7...7.8.8) · 517 files (+13369/-2145 lines)
- **Waldur Helm**: [17 commits](https://github.com/waldur/waldur-helm/compare/7.8.7...7.8.8) · 32 files (+301/-175 lines)
- **Waldur Docker Compose**: [1 commits](https://github.com/waldur/waldur-docker-compose/compare/7.8.7...7.8.8) · 1 files (+2/-2 lines)
- **Waldur Prometheus Exporter**: No changes

🔄 **SDK Updates (Auto-generated):**
- **Python Client**: [19 commits](https://github.com/waldur/py-client/compare/7.8.7...7.8.8)
- **JavaScript Client**: [37 commits](https://github.com/waldur/js-client/compare/7.8.7...7.8.8)
- **Go Client**: [17 commits](https://github.com/waldur/go-client/compare/7.8.7...7.8.8)

**✨ Notable Changes:**
- Handle case for failed migration of queue. *([62bd769](https://github.com/waldur/waldur-mastermind/commit/62bd769) - waldur-mastermind)*
- Better check for rmq admin. *([a6c04a7](https://github.com/waldur/waldur-mastermind/commit/a6c04a7) - waldur-mastermind)*
- Force migration of queues. *([202721f](https://github.com/waldur/waldur-mastermind/commit/202721f) - waldur-mastermind)*
- Fix check for rmq availability. *([1d4da20](https://github.com/waldur/waldur-mastermind/commit/1d4da20) - waldur-mastermind)*
- Extend migration to handle both broken and new migrations. *([6bb3faf](https://github.com/waldur/waldur-mastermind/commit/6bb3faf) - waldur-mastermind)*
- Fix mermaid typos. *([2b7c2ca](https://github.com/waldur/waldur-mastermind/commit/2b7c2ca) - waldur-mastermind)*
- Add orders documentation. *([65a4924](https://github.com/waldur/waldur-mastermind/commit/65a4924) - waldur-mastermind)*
- Disable rendering of email vars as they crash ansible installer. *([9bde6ca](https://github.com/waldur/waldur-helm/commit/9bde6ca) - waldur-helm)*

**Waldur Mastermind Highlights:**
- Extend migration to handle both broken and new migrations.
- Fix mermaid typos.
- Add orders documentation.

**Waldur Homeport Highlights:**
- Expose uploaded purchase order in order details [WAL-9356].
- Implement frontend for site agent diagnostics.
- Add form field use_user_organization_as_customer_name.

**Waldur Helm Highlights:**
- Disable rendering of email vars as they crash ansible installer.
- Set target version to 7.8.8.
- Fix template.

**Py Client Highlights:**
- Release: bump version to 7.8.8.
- Update Waldur Python SDK.
- Update Waldur Python SDK.

**Js Client Highlights:**
- Release: bump version to 7.8.8.
- 7.8.8-dev.17.
- Update Waldur TypeScript SDK.

**Go Client Highlights:**
- Update Waldur Go SDK.
- Update Waldur Go SDK.
- Update Waldur Go SDK.

**📚 Resources:**
- [API Schema](../API/waldur-openapi-schema-7.8.8.yaml)
- [API Changes](../integrator-guide/APIs/api-changes/waldur-openapi-schema-7.8.8-diff.md)
- [Full Release Comparison](https://github.com/waldur/waldur-mastermind/compare/7.8.7...7.8.8)

**⏱️ Released:** 2025-11-29 17:43 UTC

---

## 7.8.7 - 2025-11-29

**Release Notes:** Multi-repository release with enhanced analysis

📈 **Release Impact:** 78 commits across 4 core repositories
📁 **Functional Changes:** 187 files · +6889/-1418 lines *(excludes tests, auto-generated files)*
🔄 **SDK Updates:** 3 auto-generated clients updated

🔗 **Core Component Activity:**
- **Waldur Mastermind**: [49 commits](https://github.com/waldur/waldur-mastermind/compare/7.8.6...7.8.7) · 46 files (+3070/-210 lines)
- **Waldur Homeport**: [25 commits](https://github.com/waldur/waldur-homeport/compare/7.8.6...7.8.7) · 113 files (+3140/-1040 lines)
- **Waldur Helm**: [3 commits](https://github.com/waldur/waldur-helm/compare/7.8.6...7.8.7) · 27 files (+677/-166 lines)
- **Waldur Docker Compose**: [1 commits](https://github.com/waldur/waldur-docker-compose/compare/7.8.6...7.8.7) · 1 files (+2/-2 lines)
- **Waldur Prometheus Exporter**: No changes

🔄 **SDK Updates (Auto-generated):**
- **Python Client**: [15 commits](https://github.com/waldur/py-client/compare/7.8.6...7.8.7)
- **JavaScript Client**: [30 commits](https://github.com/waldur/js-client/compare/7.8.6...7.8.7)
- **Go Client**: [13 commits](https://github.com/waldur/go-client/compare/7.8.6...7.8.7)

**✨ Notable Changes:**
- Handle adding/removal of offering compliance checklists. *([2c57178](https://github.com/waldur/waldur-mastermind/commit/2c57178) - waldur-mastermind)*
- Implement UI to configure organization-specific component usage limits. *([14067d0](https://github.com/waldur/waldur-homeport/commit/14067d0) - waldur-homeport)*
- Fix project credit modal crashing issue. *([b25f336](https://github.com/waldur/waldur-homeport/commit/b25f336) - waldur-homeport)*
- Improve UI of add component modal. *([297babe](https://github.com/waldur/waldur-homeport/commit/297babe) - waldur-homeport)*
- Set target version to 7.8.7. *([563758c](https://github.com/waldur/waldur-helm/commit/563758c) - waldur-helm)*
- Cleanup docs. *([78a0621](https://github.com/waldur/waldur-helm/commit/78a0621) - waldur-helm)*
- Add support to set external db name and username configuration. *([eb63a40](https://github.com/waldur/waldur-helm/commit/eb63a40) - waldur-helm)*
- Set target version to 7.8.7. *([85107e8](https://github.com/waldur/waldur-docker-compose/commit/85107e8) - waldur-docker-compose)*

**Waldur Mastermind Highlights:**
- Add autoprovisioning docs.
- Handle adding/removal of offering compliance checklists.
- Add unique constraint on slurm periodic policy.

**Waldur Homeport Highlights:**
- Implement UI to configure organization-specific component usage limits.
- Fix project credit modal crashing issue.
- Improve UI of add component modal.

**Py Client Highlights:**
- Release: bump version to 7.8.7.
- Update Waldur Python SDK.
- Update Waldur Python SDK.

**Js Client Highlights:**
- Release: bump version to 7.8.7.
- 7.8.7-dev.13.
- Update Waldur TypeScript SDK.

**Go Client Highlights:**
- Update Waldur Go SDK.
- Update Waldur Go SDK.
- Update Waldur Go SDK.

**📚 Resources:**
- [API Schema](../API/waldur-openapi-schema-7.8.7.yaml)
- [API Changes](../integrator-guide/APIs/api-changes/waldur-openapi-schema-7.8.7-diff.md)
- [Full Release Comparison](https://github.com/waldur/waldur-mastermind/compare/7.8.6...7.8.7)

**⏱️ Released:** 2025-11-29 17:44 UTC

---

## 7.8.6 - 2025-11-29

**Release Notes:** Multi-repository release with enhanced analysis

📈 **Release Impact:** 37 commits across 4 core repositories
📁 **Functional Changes:** 153 files · +6126/-731 lines *(excludes tests, auto-generated files)*
🔄 **SDK Updates:** 3 auto-generated clients updated

🔗 **Core Component Activity:**
- **Waldur Mastermind**: [5 commits](https://github.com/waldur/waldur-mastermind/compare/7.8.5...7.8.6)
- **Waldur Homeport**: [22 commits](https://github.com/waldur/waldur-homeport/compare/7.8.5...7.8.6) · 129 files (+4549/-597 lines)
- **Waldur Helm**: [7 commits](https://github.com/waldur/waldur-helm/compare/7.8.5...7.8.6) · 20 files (+1574/-107 lines)
- **Waldur Docker Compose**: [3 commits](https://github.com/waldur/waldur-docker-compose/compare/7.8.5...7.8.6) · 4 files (+3/-27 lines)
- **Waldur Prometheus Exporter**: No changes

🔄 **SDK Updates (Auto-generated):**
- **Python Client**: [13 commits](https://github.com/waldur/py-client/compare/7.8.5...7.8.6)
- **JavaScript Client**: [5 commits](https://github.com/waldur/js-client/compare/7.8.5...7.8.6)
- **Go Client**: [12 commits](https://github.com/waldur/go-client/compare/7.8.5...7.8.6)

**✨ Notable Changes:**
- Add multiplier configuration options [WAL-9373]. *([79cd3e9](https://github.com/waldur/waldur-homeport/commit/79cd3e9) - waldur-homeport)*
- Set target version to 7.8.6. *([2564937](https://github.com/waldur/waldur-helm/commit/2564937) - waldur-helm)*
- Set target version to 7.8.6. *([7718ea0](https://github.com/waldur/waldur-docker-compose/commit/7718ea0) - waldur-docker-compose)*
- Add filter to exclude transitional resources with early pending orders. *([b216f24](https://github.com/waldur/waldur-mastermind/commit/b216f24) - waldur-mastermind)*
- Improve filters labels. *([fc5b9a1](https://github.com/waldur/waldur-mastermind/commit/fc5b9a1) - waldur-mastermind)*
- Update configuration, CLI and developer guide. *([0287336](https://github.com/waldur/waldur-mastermind/commit/0287336) - waldur-mastermind)*
- Improve labels for filters. *([92b4a4c](https://github.com/waldur/waldur-mastermind/commit/92b4a4c) - waldur-mastermind)*
- Export project kind, allow disabling rmq signals. *([67e21b6](https://github.com/waldur/waldur-mastermind/commit/67e21b6) - waldur-mastermind)*

**Waldur Homeport Highlights:**
- Add multiplier configuration options [WAL-9373].
- Add staff notes.
- Add new end date setting to recovery view.

**Waldur Helm Highlights:**
- Set target version to 7.8.6.
- Update documentation.
- Remove leftover path modifications.

**Py Client Highlights:**
- Release: bump version to 7.8.6.
- Update Waldur Python SDK.
- Update Waldur Python SDK.

**Go Client Highlights:**
- Update Waldur Go SDK.
- Update Waldur Go SDK.
- Update Waldur Go SDK.

**📚 Resources:**
- [API Schema](../API/waldur-openapi-schema-7.8.6.yaml)
- [API Changes](../integrator-guide/APIs/api-changes/waldur-openapi-schema-7.8.6-diff.md)
- [Full Release Comparison](https://github.com/waldur/waldur-mastermind/compare/7.8.5...7.8.6)

**⏱️ Released:** 2025-11-29 17:45 UTC

---

## 7.8.5 - 2025-11-29

**Release Notes:** Multi-repository release with enhanced analysis

📈 **Release Impact:** 65 commits across 3 core repositories
📁 **Functional Changes:** 503 files · +8118/-4037 lines *(excludes tests, auto-generated files)*
🔄 **SDK Updates:** 2 auto-generated clients updated

🔗 **Core Component Activity:**
- **Waldur Mastermind**: No changes
- **Waldur Homeport**: [59 commits](https://github.com/waldur/waldur-homeport/compare/7.8.4...7.8.5) · 496 files (+8027/-4010 lines)
- **Waldur Helm**: [5 commits](https://github.com/waldur/waldur-helm/compare/7.8.4...7.8.5) · 6 files (+89/-25 lines)
- **Waldur Docker Compose**: [1 commits](https://github.com/waldur/waldur-docker-compose/compare/7.8.4...7.8.5) · 1 files (+2/-2 lines)
- **Waldur Prometheus Exporter**: No changes

🔄 **SDK Updates (Auto-generated):**
- **Python Client**: [19 commits](https://github.com/waldur/py-client/compare/7.8.4...7.8.5)
- **Go Client**: [28 commits](https://github.com/waldur/go-client/compare/7.8.4...7.8.5)

**✨ Notable Changes:**
- Update enums and descriptions from Waldur Mastermind. *([f920e69](https://github.com/waldur/waldur-homeport/commit/f920e69) - waldur-homeport)*
- Bump dependencies. *([909fd78](https://github.com/waldur/waldur-homeport/commit/909fd78) - waldur-homeport)*
- Update enums and descriptions from Waldur Mastermind. *([ab5581c](https://github.com/waldur/waldur-homeport/commit/ab5581c) - waldur-homeport)*
- Add JIRA mapping of frontend types to request types. *([96e94ad](https://github.com/waldur/waldur-homeport/commit/96e94ad) - waldur-homeport)*
- Add support for display and management of terminated projects [WAL-9212]. *([d9776ed](https://github.com/waldur/waldur-homeport/commit/d9776ed) - waldur-homeport)*
- Fix sentry crash. *([bd96857](https://github.com/waldur/waldur-homeport/commit/bd96857) - waldur-homeport)*
- Set target version to 7.8.5. *([bc1f90d](https://github.com/waldur/waldur-helm/commit/bc1f90d) - waldur-helm)*
- Set target version to 7.8.5. *([943480b](https://github.com/waldur/waldur-docker-compose/commit/943480b) - waldur-docker-compose)*

**Waldur Homeport Highlights:**
- Add support for display and management of terminated projects [WAL-9212].
- Fix sentry crash.
- Update enums and descriptions from Waldur Mastermind.

**Py Client Highlights:**
- Release: bump version to 7.8.5.
- Update Waldur Python SDK.
- Update Waldur Python SDK.

**Go Client Highlights:**
- Update Waldur Go SDK.
- Update Waldur Go SDK.
- Update Waldur Go SDK.

**📚 Resources:**
- [API Schema](../API/waldur-openapi-schema-7.8.5.yaml)
- [API Changes](../integrator-guide/APIs/api-changes/waldur-openapi-schema-7.8.5-diff.md)
- [Full Release Comparison](https://github.com/waldur/waldur-mastermind/compare/7.8.4...7.8.5)

**⏱️ Released:** 2025-11-29 17:46 UTC

---

## 7.8.4 - 2025-11-29

**Release Notes:** Multi-repository release with enhanced analysis

📈 **Release Impact:** 10 commits across 3 core repositories
📁 **Functional Changes:** 4 files · +69/-54 lines *(excludes tests, auto-generated files)*
🔄 **SDK Updates:** 1 auto-generated clients updated

🔗 **Core Component Activity:**
- **Waldur Mastermind**: No changes
- **Waldur Homeport**: [5 commits](https://github.com/waldur/waldur-homeport/compare/7.8.3...7.8.4)
- **Waldur Helm**: [3 commits](https://github.com/waldur/waldur-helm/compare/7.8.3...7.8.4) · 2 files (+3/-3 lines)
- **Waldur Docker Compose**: [2 commits](https://github.com/waldur/waldur-docker-compose/compare/7.8.3...7.8.4) · 2 files (+66/-51 lines)
- **Waldur Prometheus Exporter**: No changes

🔄 **SDK Updates (Auto-generated):**
- **Python Client**: [12 commits](https://github.com/waldur/py-client/compare/7.8.3...7.8.4)

**✨ Notable Changes:**
- Revert "Set CSP using custom headers". *([8160df1](https://github.com/waldur/waldur-helm/commit/8160df1) - waldur-helm)*
- Set target version to 7.8.4. *([48aba0c](https://github.com/waldur/waldur-helm/commit/48aba0c) - waldur-helm)*
- Set target version to 7.8.4. *([fb7f946](https://github.com/waldur/waldur-docker-compose/commit/fb7f946) - waldur-docker-compose)*
- Fix bad error message when applying for a an available organization with already open request. *([e035237](https://github.com/waldur/waldur-homeport/commit/e035237) - waldur-homeport)*
- Migrate invitation form to react final form. *([264cc02](https://github.com/waldur/waldur-homeport/commit/264cc02) - waldur-homeport)*
- Reallocation limits UI changes. *([dc725fb](https://github.com/waldur/waldur-homeport/commit/dc725fb) - waldur-homeport)*
- Fix either toggle or specific organization can be selected. *([c506659](https://github.com/waldur/waldur-homeport/commit/c506659) - waldur-homeport)*
- Check if WALDUR_OPENPORTAL during routes permission check. *([349cad4](https://github.com/waldur/waldur-homeport/commit/349cad4) - waldur-homeport)*

**Py Client Highlights:**
- Release: bump version to 7.8.4.
- Update Waldur Python SDK.
- Update Waldur Python SDK.

**📚 Resources:**
- [API Schema](../API/waldur-openapi-schema-7.8.4.yaml)
- [API Changes](../integrator-guide/APIs/api-changes/waldur-openapi-schema-7.8.4-diff.md)
- [Full Release Comparison](https://github.com/waldur/waldur-mastermind/compare/7.8.3...7.8.4)

**⏱️ Released:** 2025-11-29 17:47 UTC

---

## 7.8.3 - 2025-11-29

**Release Notes:** Multi-repository release with enhanced analysis

📈 **Release Impact:** 2 commits across 2 core repositories
📁 **Functional Changes:** 3 files · +5/-5 lines *(excludes tests, auto-generated files)*
🔄 **SDK Updates:** 2 auto-generated clients updated

🔗 **Core Component Activity:**
- **Waldur Mastermind**: No changes
- **Waldur Homeport**: No changes
- **Waldur Helm**: [1 commits](https://github.com/waldur/waldur-helm/compare/7.8.2...7.8.3) · 2 files (+3/-3 lines)
- **Waldur Docker Compose**: [1 commits](https://github.com/waldur/waldur-docker-compose/compare/7.8.2...7.8.3) · 1 files (+2/-2 lines)
- **Waldur Prometheus Exporter**: No changes

🔄 **SDK Updates (Auto-generated):**
- **Python Client**: [3 commits](https://github.com/waldur/py-client/compare/7.8.2...7.8.3)
- **Go Client**: [2 commits](https://github.com/waldur/go-client/compare/7.8.2...7.8.3)

**✨ Notable Changes:**
- Set target version to 7.8.3. *([827681b](https://github.com/waldur/waldur-helm/commit/827681b) - waldur-helm)*
- Set target version to 7.8.3. *([e32b13b](https://github.com/waldur/waldur-docker-compose/commit/e32b13b) - waldur-docker-compose)*

**📚 Resources:**
- [API Schema](../API/waldur-openapi-schema-7.8.3.yaml)
- [API Changes](../integrator-guide/APIs/api-changes/waldur-openapi-schema-7.8.3-diff.md)
- [Full Release Comparison](https://github.com/waldur/waldur-mastermind/compare/7.8.2...7.8.3)

**⏱️ Released:** 2025-11-29 17:48 UTC

---

## 7.8.2 - 2025-11-29

**Release Notes:** Multi-repository release with enhanced analysis

📈 **Release Impact:** Minor release with configuration and documentation updates

🔗 **Core Component Activity:**
- **Waldur Mastermind**: No changes
- **Waldur Homeport**: No changes
- **Waldur Helm**: No changes
- **Waldur Docker Compose**: No changes
- **Waldur Prometheus Exporter**: No changes

**📚 Resources:**
- [API Schema](../API/waldur-openapi-schema-7.8.2.yaml)
- [API Changes](../integrator-guide/APIs/api-changes/waldur-openapi-schema-7.8.2-diff.md)
- [Full Release Comparison](https://github.com/waldur/waldur-mastermind/compare/7.8.2...7.8.2)

**⏱️ Released:** 2025-11-29 17:50 UTC

---

## 7.8.2 - 2025-11-29

**Release Notes:** Multi-repository release with enhanced analysis

📈 **Release Impact:** Minor release with configuration and documentation updates

🔗 **Core Component Activity:**
- **Waldur Mastermind**: No changes
- **Waldur Homeport**: No changes
- **Waldur Helm**: No changes
- **Waldur Docker Compose**: No changes
- **Waldur Prometheus Exporter**: No changes

**📚 Resources:**
- [API Schema](../API/waldur-openapi-schema-7.8.2.yaml)
- [API Changes](../integrator-guide/APIs/api-changes/waldur-openapi-schema-7.8.2-diff.md)
- [Full Release Comparison](https://github.com/waldur/waldur-mastermind/compare/7.8.2...7.8.2)

**⏱️ Released:** 2025-11-29 17:50 UTC

---

## 7.8.1 - 2025-11-29

**Release Notes:** Multi-repository release with enhanced analysis

📈 **Release Impact:** 2 commits across 2 core repositories
📁 **Functional Changes:** 3 files · +5/-5 lines *(excludes tests, auto-generated files)*

🔗 **Core Component Activity:**
- **Waldur Mastermind**: No changes
- **Waldur Homeport**: No changes
- **Waldur Helm**: [1 commits](https://github.com/waldur/waldur-helm/compare/7.8.0...7.8.1) · 2 files (+3/-3 lines)
- **Waldur Docker Compose**: [1 commits](https://github.com/waldur/waldur-docker-compose/compare/7.8.0...7.8.1) · 1 files (+2/-2 lines)
- **Waldur Prometheus Exporter**: No changes

**✨ Notable Changes:**
- Set target version to 7.8.1. *([df73b4c](https://github.com/waldur/waldur-helm/commit/df73b4c) - waldur-helm)*
- Set target version to 7.8.1. *([4b13d32](https://github.com/waldur/waldur-docker-compose/commit/4b13d32) - waldur-docker-compose)*

**📚 Resources:**
- [API Schema](../API/waldur-openapi-schema-7.8.1.yaml)
- [API Changes](../integrator-guide/APIs/api-changes/waldur-openapi-schema-7.8.1-diff.md)
- [Full Release Comparison](https://github.com/waldur/waldur-mastermind/compare/7.8.0...7.8.1)

**⏱️ Released:** 2025-11-29 17:51 UTC

---

## 7.8.0 - 2025-11-29

**Release Notes:** Multi-repository release with enhanced analysis

📈 **Release Impact:** 4 commits across 2 core repositories
📁 **Functional Changes:** 5 files · +297/-5 lines *(excludes tests, auto-generated files)*
🔄 **SDK Updates:** 1 auto-generated clients updated

🔗 **Core Component Activity:**
- **Waldur Mastermind**: No changes
- **Waldur Homeport**: No changes
- **Waldur Helm**: [3 commits](https://github.com/waldur/waldur-helm/compare/7.7.9...7.8.0) · 4 files (+295/-3 lines)
- **Waldur Docker Compose**: [1 commits](https://github.com/waldur/waldur-docker-compose/compare/7.7.9...7.8.0) · 1 files (+2/-2 lines)
- **Waldur Prometheus Exporter**: No changes

🔄 **SDK Updates (Auto-generated):**
- **Go Client**: [5 commits](https://github.com/waldur/go-client/compare/7.7.9...7.8.0)

**✨ Notable Changes:**
- Add ENABLE_PROJECT_KIND_COURSE field. *([36404b1](https://github.com/waldur/waldur-helm/commit/36404b1) - waldur-helm)*
- Basic overview of helm components. *([0037b29](https://github.com/waldur/waldur-helm/commit/0037b29) - waldur-helm)*
- Set target version to 7.8.0. *([38bbe0d](https://github.com/waldur/waldur-helm/commit/38bbe0d) - waldur-helm)*
- Set target version to 7.8.0. *([e1b89ee](https://github.com/waldur/waldur-docker-compose/commit/e1b89ee) - waldur-docker-compose)*

**📚 Resources:**
- [API Schema](../API/waldur-openapi-schema-7.8.0.yaml)
- [API Changes](../integrator-guide/APIs/api-changes/waldur-openapi-schema-7.8.0-diff.md)
- [Full Release Comparison](https://github.com/waldur/waldur-mastermind/compare/7.7.9...7.8.0)

**⏱️ Released:** 2025-11-29 17:52 UTC

---

## 7.7.9 - 2025-11-29

**Release Notes:** Multi-repository release with enhanced analysis

📈 **Release Impact:** 2 commits across 2 core repositories
📁 **Functional Changes:** 3 files · +5/-5 lines *(excludes tests, auto-generated files)*

🔗 **Core Component Activity:**
- **Waldur Mastermind**: No changes
- **Waldur Homeport**: No changes
- **Waldur Helm**: [1 commits](https://github.com/waldur/waldur-helm/compare/7.7.8...7.7.9) · 2 files (+3/-3 lines)
- **Waldur Docker Compose**: [1 commits](https://github.com/waldur/waldur-docker-compose/compare/7.7.8...7.7.9) · 1 files (+2/-2 lines)
- **Waldur Prometheus Exporter**: No changes

**✨ Notable Changes:**
- Set target version to 7.7.9. *([f2c09cc](https://github.com/waldur/waldur-helm/commit/f2c09cc) - waldur-helm)*
- Set target version to 7.7.9. *([cbdebc3](https://github.com/waldur/waldur-docker-compose/commit/cbdebc3) - waldur-docker-compose)*

**📚 Resources:**
- [API Schema](../API/waldur-openapi-schema-7.7.9.yaml)
- [API Changes](../integrator-guide/APIs/api-changes/waldur-openapi-schema-7.7.9-diff.md)
- [Full Release Comparison](https://github.com/waldur/waldur-mastermind/compare/7.7.8...7.7.9)

**⏱️ Released:** 2025-11-29 17:53 UTC

---

## 7.7.8 - 2025-11-29

**Release Notes:** Multi-repository release with enhanced analysis

📈 **Release Impact:** 8 commits across 2 core repositories
📁 **Functional Changes:** 9 files · +79/-24 lines *(excludes tests, auto-generated files)*

🔗 **Core Component Activity:**
- **Waldur Mastermind**: No changes
- **Waldur Homeport**: No changes
- **Waldur Helm**: [6 commits](https://github.com/waldur/waldur-helm/compare/7.7.7...7.7.8) · 7 files (+75/-21 lines)
- **Waldur Docker Compose**: [2 commits](https://github.com/waldur/waldur-docker-compose/compare/7.7.7...7.7.8) · 2 files (+4/-3 lines)
- **Waldur Prometheus Exporter**: No changes

**✨ Notable Changes:**
- Introduce support for operator-based RabbitMQ deployment. *([f6986cc](https://github.com/waldur/waldur-helm/commit/f6986cc) - waldur-helm)*
- Revert "Merge branch 'feature/add-support-for-rmq-operator' into 'master'". *([4afe521](https://github.com/waldur/waldur-helm/commit/4afe521) - waldur-helm)*
- Implement support for RabbitMQ operator (Season 1, episode 2). *([49d1f0c](https://github.com/waldur/waldur-helm/commit/49d1f0c) - waldur-helm)*
- Add resources settings to initContainers of waldur beat deployment. *([8ea8f0f](https://github.com/waldur/waldur-helm/commit/8ea8f0f) - waldur-helm)*
- Make upgrade instructions more reliable. *([ac45b19](https://github.com/waldur/waldur-docker-compose/commit/ac45b19) - waldur-docker-compose)*
- Set target version to 7.7.8. *([0d827b1](https://github.com/waldur/waldur-helm/commit/0d827b1) - waldur-helm)*
- Add settings for course accounts. *([e9ba76f](https://github.com/waldur/waldur-helm/commit/e9ba76f) - waldur-helm)*
- Set target version to 7.7.8. *([f7cbdf5](https://github.com/waldur/waldur-docker-compose/commit/f7cbdf5) - waldur-docker-compose)*

**Waldur Helm Highlights:**
- Set target version to 7.7.8.
- Add settings for course accounts.
- Add resources settings to initContainers of waldur beat deployment.

**📚 Resources:**
- [API Schema](../API/waldur-openapi-schema-7.7.8.yaml)
- [API Changes](../integrator-guide/APIs/api-changes/waldur-openapi-schema-7.7.8-diff.md)
- [Full Release Comparison](https://github.com/waldur/waldur-mastermind/compare/7.7.7...7.7.8)

**⏱️ Released:** 2025-11-29 17:54 UTC

---

## 7.7.7 - 2025-11-29

**Release Notes:** Multi-repository release with enhanced analysis

📈 **Release Impact:** 7 commits across 2 core repositories
📁 **Functional Changes:** 6 files · +54/-10 lines *(excludes tests, auto-generated files)*

🔗 **Core Component Activity:**
- **Waldur Mastermind**: No changes
- **Waldur Homeport**: No changes
- **Waldur Helm**: [2 commits](https://github.com/waldur/waldur-helm/compare/7.7.6...7.7.7) · 3 files (+7/-7 lines)
- **Waldur Docker Compose**: [5 commits](https://github.com/waldur/waldur-docker-compose/compare/7.7.6...7.7.7) · 3 files (+47/-3 lines)
- **Waldur Prometheus Exporter**: No changes

**✨ Notable Changes:**
- Enable api-auth-browsable forwarding to mastermind APIs. *([5678eb0](https://github.com/waldur/waldur-docker-compose/commit/5678eb0) - waldur-docker-compose)*
- Update docs for readonly setup to include env vars. *([31a51ad](https://github.com/waldur/waldur-docker-compose/commit/31a51ad) - waldur-docker-compose)*
- Add instructions for fixing migration from bitnami DB image to a regular one. *([793bcda](https://github.com/waldur/waldur-docker-compose/commit/793bcda) - waldur-docker-compose)*
- Additional fixes for DB collation. *([78512c9](https://github.com/waldur/waldur-docker-compose/commit/78512c9) - waldur-docker-compose)*
- Set target version to 7.7.7. *([f2c23d6](https://github.com/waldur/waldur-helm/commit/f2c23d6) - waldur-helm)*
- Increase default RMQ resources. *([6520aa1](https://github.com/waldur/waldur-helm/commit/6520aa1) - waldur-helm)*
- Set target version to 7.7.7. *([d0922c7](https://github.com/waldur/waldur-docker-compose/commit/d0922c7) - waldur-docker-compose)*

**📚 Resources:**
- [API Schema](../API/waldur-openapi-schema-7.7.7.yaml)
- [API Changes](../integrator-guide/APIs/api-changes/waldur-openapi-schema-7.7.7-diff.md)
- [Full Release Comparison](https://github.com/waldur/waldur-mastermind/compare/7.7.6...7.7.7)

**⏱️ Released:** 2025-11-29 17:55 UTC

---

## 7.7.6 - 2025-11-29

**Release Notes:** Multi-component release with updates across the Waldur ecosystem

📊 **Changes:** Updates across 3 core components
📈 **Impact:** See component links below for detailed changes

🔗 **Component Updates:**
- **Waldur MasterMind**: [View changes](https://github.com/waldur/waldur-mastermind/compare/7.7.5...7.7.6)
- **Waldur HomePort**: [View changes](https://github.com/waldur/waldur-homeport/compare/7.7.5...7.7.6)
- **Waldur Helm**: [View changes](https://github.com/waldur/waldur-helm/compare/7.7.5...7.7.6)
- **Waldur Docker Compose**: [View changes](https://github.com/waldur/waldur-docker-compose/compare/7.7.5...7.7.6)
- **Waldur Prometheus Exporter**: [View changes](https://github.com/waldur/waldur-prometheus-exporter/compare/7.7.5...7.7.6)
- **Python SDK**: [View changes](https://github.com/waldur/py-client/compare/7.7.5...7.7.6)
- **JavaScript SDK**: [View changes](https://github.com/waldur/js-client/compare/7.7.5...7.7.6)
- **Go SDK**: [View changes](https://github.com/waldur/go-client/compare/7.7.5...7.7.6)

**📚 Resources:**
- [API Schema](/API/waldur-openapi-schema-7.7.6.yaml)
- [API Changes](/integrator-guide/APIs/api-changes/waldur-openapi-schema-7.7.6-diff)
- [Release Comparison](https://github.com/waldur/waldur-mastermind/compare/7.7.5...7.7.6)

**⏱️ Released:** 2025-11-29

---

## Archived Releases

*Older releases have been archived to maintain file size. Historical entries are available in the git history.*

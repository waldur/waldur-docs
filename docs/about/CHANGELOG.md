# Changelog

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

- [OpenAPI Schema](../API/waldur-openapi-schema-7.9.1.yaml)
- [API Changes](../integrator-guide/APIs/api-changes/waldur-openapi-schema-7.9.1-diff.md)

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

- [OpenAPI Schema](../API/waldur-openapi-schema-7.9.0.yaml)
- [API Changes](../integrator-guide/APIs/api-changes/waldur-openapi-schema-7.9.0-diff.md)

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

- [OpenAPI Schema](../API/waldur-openapi-schema-7.8.9.yaml)
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

- [OpenAPI Schema](../API/waldur-openapi-schema-7.8.8.yaml)
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

- [OpenAPI Schema](../API/waldur-openapi-schema-7.8.7.yaml)
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

- [OpenAPI Schema](../API/waldur-openapi-schema-7.8.6.yaml)
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

- [OpenAPI Schema](../API/waldur-openapi-schema-7.8.5.yaml)
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

- [OpenAPI Schema](../API/waldur-openapi-schema-7.8.4.yaml)
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

- [OpenAPI Schema](../API/waldur-openapi-schema-7.8.3.yaml)
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

- [OpenAPI Schema](../API/waldur-openapi-schema-7.8.2.yaml)
- [API Changes](../integrator-guide/APIs/api-changes/waldur-openapi-schema-7.8.2-diff.md)

---

## 7.8.1 - 2025-11-30

### Release Summary

- **Release Impact:** 2 commits across 2 core repositories
- **Functional Changes:** 2 files changed with +3/-3 lines

!!! note "Statistics Note"
    Excludes tests, auto-generated files, and SDK client code for accurate development metrics.

### Core Component Activity

- **Waldur Mastermind**: No changes
- **Waldur Homeport**: No changes
- **Waldur Helm**: [1 commits](https://github.com/waldur/waldur-helm/compare/7.8.0...7.8.1) · 2 files changed (+3/-3 lines)
- **Waldur Docker Compose**: [1 commits](https://github.com/waldur/waldur-docker-compose/compare/7.8.0...7.8.1)
- **Waldur Prometheus Exporter**: No changes

### Notable Changes

- **Set target version to 7.8.1.** ([df73b4c](https://github.com/waldur/waldur-helm/commit/df73b4c) - Waldur Helm)
- **Set target version to 7.8.1.** ([4b13d32](https://github.com/waldur/waldur-docker-compose/commit/4b13d32) - Waldur Docker Compose)

### Resources

- [OpenAPI Schema](../API/waldur-openapi-schema-7.8.1.yaml)
- [API Changes](../integrator-guide/APIs/api-changes/waldur-openapi-schema-7.8.1-diff.md)

---

## 7.8.0 - 2025-11-30

### Release Summary

- **Release Impact:** 4 commits across 2 core repositories
- **Functional Changes:** 4 files changed with +295/-3 lines
- **SDK Updates:** 1 auto-generated clients updated from OpenAPI schema

!!! note "Statistics Note"
    Excludes tests, auto-generated files, and SDK client code for accurate development metrics.

### Core Component Activity

- **Waldur Mastermind**: No changes
- **Waldur Homeport**: No changes
- **Waldur Helm**: [3 commits](https://github.com/waldur/waldur-helm/compare/7.7.9...7.8.0) · 4 files changed (+295/-3 lines)
- **Waldur Docker Compose**: [1 commits](https://github.com/waldur/waldur-docker-compose/compare/7.7.9...7.8.0)
- **Waldur Prometheus Exporter**: No changes

### SDK Updates (Auto-generated)

- **Go Client**: [5 commits](https://github.com/waldur/go-client/compare/7.7.9...7.8.0)

### Notable Changes

- **Add ENABLE_PROJECT_KIND_COURSE field.** ([36404b1](https://github.com/waldur/waldur-helm/commit/36404b1) - Waldur Helm)
- **Basic overview of helm components.** ([0037b29](https://github.com/waldur/waldur-helm/commit/0037b29) - Waldur Helm)
- **Set target version to 7.8.0.** ([38bbe0d](https://github.com/waldur/waldur-helm/commit/38bbe0d) - Waldur Helm)
- **Set target version to 7.8.0.** ([e1b89ee](https://github.com/waldur/waldur-docker-compose/commit/e1b89ee) - Waldur Docker Compose)

### Resources

- [OpenAPI Schema](../API/waldur-openapi-schema-7.8.0.yaml)
- [API Changes](../integrator-guide/APIs/api-changes/waldur-openapi-schema-7.8.0-diff.md)

---

## 7.7.9 - 2025-11-30

### Release Summary

- **Release Impact:** 2 commits across 2 core repositories
- **Functional Changes:** 2 files changed with +3/-3 lines

!!! note "Statistics Note"
    Excludes tests, auto-generated files, and SDK client code for accurate development metrics.

### Core Component Activity

- **Waldur Mastermind**: No changes
- **Waldur Homeport**: No changes
- **Waldur Helm**: [1 commits](https://github.com/waldur/waldur-helm/compare/7.7.8...7.7.9) · 2 files changed (+3/-3 lines)
- **Waldur Docker Compose**: [1 commits](https://github.com/waldur/waldur-docker-compose/compare/7.7.8...7.7.9)
- **Waldur Prometheus Exporter**: No changes

### Notable Changes

- **Set target version to 7.7.9.** ([f2c09cc](https://github.com/waldur/waldur-helm/commit/f2c09cc) - Waldur Helm)
- **Set target version to 7.7.9.** ([cbdebc3](https://github.com/waldur/waldur-docker-compose/commit/cbdebc3) - Waldur Docker Compose)

### Resources

- [OpenAPI Schema](../API/waldur-openapi-schema-7.7.9.yaml)
- [API Changes](../integrator-guide/APIs/api-changes/waldur-openapi-schema-7.7.9-diff.md)

---

## 7.7.8 - 2025-11-30

### Release Summary

- **Release Impact:** 8 commits across 2 core repositories
- **Functional Changes:** 8 files changed with +77/-22 lines

!!! note "Statistics Note"
    Excludes tests, auto-generated files, and SDK client code for accurate development metrics.

### Core Component Activity

- **Waldur Mastermind**: No changes
- **Waldur Homeport**: No changes
- **Waldur Helm**: [6 commits](https://github.com/waldur/waldur-helm/compare/7.7.7...7.7.8) · 7 files changed (+75/-21 lines)
- **Waldur Docker Compose**: [2 commits](https://github.com/waldur/waldur-docker-compose/compare/7.7.7...7.7.8) · 1 files changed (+2/-1 lines)
- **Waldur Prometheus Exporter**: No changes

### Notable Changes

- **Implement support for RabbitMQ operator (Season 1, episode 2).** ([49d1f0c](https://github.com/waldur/waldur-helm/commit/49d1f0c) - Waldur Helm)
- **Add resources settings to initContainers of waldur beat deployment.** ([8ea8f0f](https://github.com/waldur/waldur-helm/commit/8ea8f0f) - Waldur Helm)
- **Make upgrade instructions more reliable.** ([ac45b19](https://github.com/waldur/waldur-docker-compose/commit/ac45b19) - Waldur Docker Compose)
- **Set target version to 7.7.8.** ([0d827b1](https://github.com/waldur/waldur-helm/commit/0d827b1) - Waldur Helm)
- **Add settings for course accounts.** ([e9ba76f](https://github.com/waldur/waldur-helm/commit/e9ba76f) - Waldur Helm)
- **Set target version to 7.7.8.** ([f7cbdf5](https://github.com/waldur/waldur-docker-compose/commit/f7cbdf5) - Waldur Docker Compose)

### Waldur Helm Highlights

- Set target version to 7.7.8.
- Add settings for course accounts.
- Add resources settings to initContainers of waldur beat deployment.

### Resources

- [OpenAPI Schema](../API/waldur-openapi-schema-7.7.8.yaml)
- [API Changes](../integrator-guide/APIs/api-changes/waldur-openapi-schema-7.7.8-diff.md)

---

## 7.7.7 - 2025-11-30

### Release Summary

- **Release Impact:** 7 commits across 2 core repositories
- **Functional Changes:** 5 files changed with +47/-8 lines

!!! note "Statistics Note"
    Excludes tests, auto-generated files, and SDK client code for accurate development metrics.

### Core Component Activity

- **Waldur Mastermind**: No changes
- **Waldur Homeport**: No changes
- **Waldur Helm**: [2 commits](https://github.com/waldur/waldur-helm/compare/7.7.6...7.7.7) · 3 files changed (+7/-7 lines)
- **Waldur Docker Compose**: [5 commits](https://github.com/waldur/waldur-docker-compose/compare/7.7.6...7.7.7) · 2 files changed (+40/-1 lines)
- **Waldur Prometheus Exporter**: No changes

### Notable Changes

- **Update docs for readonly setup to include env vars.** ([31a51ad](https://github.com/waldur/waldur-docker-compose/commit/31a51ad) - Waldur Docker Compose)
- **Add instructions for fixing migration from bitnami DB image to a regular one.** ([793bcda](https://github.com/waldur/waldur-docker-compose/commit/793bcda) - Waldur Docker Compose)
- **Additional fixes for DB collation.** ([78512c9](https://github.com/waldur/waldur-docker-compose/commit/78512c9) - Waldur Docker Compose)
- **Set target version to 7.7.7.** ([f2c23d6](https://github.com/waldur/waldur-helm/commit/f2c23d6) - Waldur Helm)
- **Increase default RMQ resources.** ([6520aa1](https://github.com/waldur/waldur-helm/commit/6520aa1) - Waldur Helm)
- **Set target version to 7.7.7.** ([d0922c7](https://github.com/waldur/waldur-docker-compose/commit/d0922c7) - Waldur Docker Compose)

### Resources

- [OpenAPI Schema](../API/waldur-openapi-schema-7.7.7.yaml)
- [API Changes](../integrator-guide/APIs/api-changes/waldur-openapi-schema-7.7.7-diff.md)

---

## Archived Releases

*Older releases have been archived to maintain file size. Historical entries are available in the git history.*

# API Stability Roadmap

!!! warning "This is a roadmap"
    This document describes **planned improvements**, not current functionality.
    For how API changes work today, see [API Versioning and Change Policy](api-lifecycle.md).

## Motivation

As Waldur's integrator ecosystem grows, we need to provide stronger guarantees around API stability, clearer communication of breaking changes, and better tooling for safe upgrades. This roadmap outlines the planned improvements in three phases.

## Phase 1: Breaking change visibility

**Goal**: Make it impossible for breaking changes to ship without being explicitly acknowledged.

- **OpenAPI schema linting in CI** — Automatically compare the OpenAPI schema in each merge request against the previous release. Flag removals, renames, and type changes as breaking.
- **Breaking change labels in changelog** — Introduce a dedicated "Breaking Changes" section in release changelogs so integrators can scan quickly.
- **Endpoint inventory by domain** — Catalog all API endpoints by functional group (`marketplace`, `openstack`, `rancher`, etc.) to understand the surface area and identify candidates for stabilization.

## Phase 2: Formal deprecation policy

**Goal**: Give integrators predictable timelines for endpoint removal.

- **Defined deprecation windows** — Establish minimum notice periods before deprecated endpoints are removed (e.g., at least 2 releases or 90 days, whichever is longer).
- **`Waldur-API-Version` response header** — Return the current API version in HTTP responses so clients can detect version mismatches programmatically.
- **Deprecation metadata in OpenAPI** — Extend the OpenAPI spec with structured deprecation info: sunset date, replacement endpoint, and migration notes.
- **SDK deprecation warnings** — Surface deprecation warnings in the Python/Go/TypeScript SDKs when calling deprecated endpoints.

## Phase 3: Upgrade impact tooling

**Goal**: Help operators and integrators assess the impact of an upgrade before applying it.

- **Upgrade impact CLI** — A command-line tool that compares two Waldur versions and reports:
    - API breaking changes affecting the deployment
    - Database schema changes and estimated migration time
    - Configuration changes (new/removed/renamed settings)
- **Dry-run mode for migrations** — Allow running database migrations in a preview mode to catch issues before committing.
- **Consolidated impact report** — Generate a machine-readable (JSON) report summarizing all upgrade impacts:

```json
{
  "upgrade_path": "8.0.5 → 8.1.0",
  "breaking_api_changes": [
    {
      "endpoint": "/api/marketplace-resources/",
      "change": "Field 'category' is now required",
      "migration": "Set 'category' on existing resources before upgrading"
    }
  ],
  "database_migrations": 3,
  "config_changes": [
    {
      "setting": "WALDUR_MARKETPLACE.NEW_SETTING",
      "action": "added",
      "default": true
    }
  ]
}
```

## Success criteria

- All breaking changes detected and flagged before release
- No unannounced breaking changes in patch releases
- Deprecated endpoints have documented removal timelines
- Integrators can assess upgrade impact before applying updates

# API Versioning and Change Policy

## Versioning scheme

Waldur uses semantic versioning: **`MAJOR.MINOR.PATCH`** (e.g., `8.0.5`).

- **MAJOR** version increments indicate significant platform changes.
- **MINOR** version increments are not currently used for separate cadence — patches ship as `MAJOR.MINOR.PATCH`.
- **PATCH** releases ship frequently and may contain new features, improvements, bug fixes, and occasionally breaking changes.
- **Release candidates** use the format `MAJOR.MINOR.PATCH-rc.N` (e.g., `8.0.6-rc.1`) for pre-release testing.

Releases are coordinated across all Waldur components (MasterMind, HomePort, Helm charts, Docker Compose, SDKs) — they all share the same version tag.

## How API changes are communicated

### Changelog

Every release includes a changelog entry in the [Changelog](../about/CHANGELOG.md) with categorized sections: features, improvements, bug fixes.

### OpenAPI schema diffs

For each release, an OpenAPI schema diff is auto-generated and published under the API Changes section (see e.g. [8.0.3 diff](APIs/api-changes/waldur-openapi-schema-8.0.3-diff.md)). These diffs show:

- New endpoints added
- Endpoints removed
- Changed parameters, fields, or response structures

For example, `waldur-openapi-schema-8.0.3-diff.md` lists all endpoint additions and removals between 8.0.2 and 8.0.3.

### SDK regeneration

The Python, Go, and TypeScript SDKs are regenerated from the OpenAPI schema on each release. SDK users can pin to a specific version and review the updated schema before upgrading.

## Deprecation

Deprecated endpoints are marked with the `deprecated` flag in the OpenAPI schema. When an endpoint is deprecated:

1. The `deprecated: true` flag is set in the OpenAPI spec.
2. The endpoint description is updated with a migration note (e.g., "DEPRECATED: please use the dedicated `/api/openstack-network-rbac-policies/` endpoint").
3. The change appears in the OpenAPI schema diff for that release.

!!! warning
    Waldur does not currently guarantee a fixed deprecation window. Deprecated endpoints may be removed in any subsequent release. Integrators should migrate promptly when a deprecation notice appears.

## Types of API changes

### Backward-compatible changes

These changes do not break existing clients:

- Adding new endpoints
- Adding optional query parameters
- Adding new fields to responses
- Adding new enum values

### Breaking changes

These changes may require client updates:

- Removing or renaming endpoints
- Removing or renaming request/response fields
- Changing field types
- Making a previously optional field required
- Changing HTTP status codes
- Changing URL patterns

!!! tip
    Review the OpenAPI schema diffs (under API Changes in the navigation) before upgrading to identify any breaking changes that affect your integration.

## Tracking changes as an integrator

1. **Before upgrading**: Review the [Changelog](../about/CHANGELOG.md) and the relevant API schema diff for your target version.
2. **Pin SDK versions**: Use version pinning in your dependencies so upgrades are deliberate.
3. **Watch for deprecation flags**: Periodically check the OpenAPI schema for newly deprecated endpoints.
4. **Test against RC releases**: Release candidates (`-rc.N`) are available for pre-release validation.

## Future improvements

We are working on improving API stability guarantees and change communication. See the [API Stability Roadmap](api-stability-roadmap.md) for planned improvements including formal deprecation windows, breaking change detection in CI, and upgrade impact tooling.

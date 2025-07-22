# Waldur Release Lifecycle and API Stability Guarantees

## Introduction to API Policies

Waldur's API lifecycle management balances innovation with stability through defined policies:

- **Release Cadence**:
   - 2 major releases per year (every 6 months)
   - 4 minor releases per year (every 3 months)

- **API Group Segmentation**:
   - APIs are grouped by functional domains (e.g., `core`, `marketplace`, `openstack`)
   - Groups have independent maturity levels and versioning

- **API Maturity Management**:
   - Three maturity levels: `alpha`, `beta`, `stable`
   - Each level has specific stability guarantees and versioning rules

- **Change Classification**:
   - Backward-compatible (additive changes) and backward-incompatible (breaking changes)
   - API changes, database changes, configuration and deployment changes

- **Change Communication**:
   - For Waldur developers: via commit message and OpenAPI schema linter
   - For release manager: breaking changes in stable APIs trigger policy validation
   - For external developers: via OpenAPI schema, SDK documentation, code transformations and validation tools
   - For external scripts: via OpenAPI schema validation and version validation in HTTP response
   - For Waldur operators: via release impact assesment CLI tooling and Waldur dashboard

Waldur MasterMind lifecycle strategy enables:

- **Rapid Innovation** through alpha/beta channels
- **Enterprise Stability** through backported security patches
- **Risk Mitigation** with pre-upgrade analysis
- **Seamless Upgrades** using migration tooling

## Release Cadence

### Waldur MasterMind Release Timeline

```mermaid
gantt
    dateFormat  YYYY-MM-DD
    axisFormat  %b %Y

    section Releases
    Major 2025.1 : milestone, m1, 2025-01-01, 0d
    Minor 2025.1.1 : milestone, m2, 2025-04-01, 0d
    Minor 2025.1.2 : milestone, m3, 2025-07-01, 0d
    Minor 2025.1.3 : milestone, m4, 2025-10-01, 0d

    section Stable API v1
    Active Support : active_stable1, 2025-01-01, 2025-07-01
    Security Maintenance : maint_stable1, 2025-07-01, 2026-01-01

    section Stable API v2
    Active Support : active_stable2, 2025-07-01, 2026-01-01

    section Beta API v1beta1
    Active Support : active_beta1, 2025-01-01, 2025-04-01
    Maintenance : maint_beta1, 2025-04-01, 2025-07-01

    section Beta API v1beta2
    Active Support : active_beta2, 2025-04-01, 2025-07-01

    section Alpha API v1alpha1
    Unsupported : alpha1, 2025-01-01, 2025-04-01

    section Alpha API v1alpha2
    Unsupported : alpha2, 2025-04-01, 2025-07-01
```

## API Maturity Levels

| Maturity | Breaking Changes | Support Window | Version Format | Recommended Use           |
| -------- | ---------------- | -------------- | -------------- | ------------------------- |
| Alpha    | Daily            | None           | 2025.2-dev.45  | Internal development only |
| Beta     | Quarterly        | 90 days        | 2025.2-beta.3  | Preview environments      |
| Stable   | Bi-annually      | 180 days       | 2025.2.5       | General production        |

### Alpha Level

- **Versioning**: `XalphaY` (e.g., `1alpha1`)
- **Availability**: In main repo, disabled by default (feature flag)
- **Audience**: Developers and expert users
- **Completeness**: Partial implementation expected
- **Upgradeability**: No upgrade path; breaking changes without notice
- **Reliability**: May destabilize deployments
- **Support**: No commitment to completion or long-term support
- **Use Cases**: Short-lived testing environments only

### Beta Level

- **Versioning**: `XbetaY` (e.g., `2beta3`)
- **Availability**: In releases, disabled by default (feature flag)
- **Audience**: Users providing feedback
- **Completeness**: Full implementation with API review
- **Upgradeability**: Breaking changes with documented migration path
- **Reliability**: Minor bugs possible, shouldn't break core functionality
- **Support**: Two concurrent versions supported for ≥1 minor release (3 months)
- **Use Cases**: Evaluation environments and limited production trials

### Stable Level

- **Versioning**: `X` (e.g., `v3`)
- **Availability**: Enabled by default in releases
- **Audience**: All users
- **Completeness**: Full implementation with integration tests
- **Upgradeability**: Only backward-compatible changes allowed
- **Reliability**: High stability guarantee
- **Support**: Maintained for ≥1 major release cycle (6 months) after deprecation
- **Use Cases**: All production environments

## Types of API Changes

### Backward-Incompatible Changes

- URL format changes
- Removing/renaming resources, parameters, properties, or methods
- Changing parameter/property types
- Modifying HTTP status codes
- Changing optional field to mandatory in REST API
- Adding required parameters

### Backward-Compatible Changes

- Adding new resources
- Adding operations to existing resources
- Adding optional parameters
- Adding response fields
- Extending string formats
- Adding enum values

```mermaid
graph TD
    A[Proposed API Change] --> B{Backward Compatible?}
    B -->|Yes| C[Apply to current version]
    B -->|No| D{Maturity Level}
    D -->|Alpha| E[Increment alpha version<br>e.g. v1alpha1 → v1alpha2]
    D -->|Beta| F[Increment beta version<br>e.g. v1beta1 → v1beta2<br>Support both for ≥3 months]
    D -->|Stable| G[Create new major version<br>e.g. v1 → v2<br>Deprecate old version<br>Support for ≥6 months]
```

## Change Communication

### Change Communication Stages

```mermaid
flowchart LR
    %% Merged Development & Pre-Release Phase
    subgraph DevPre[Development & Pre-Release]
        direction TB
        DP1[Commit Messages]
        DP2[OpenAPI Linter]
        DP3[Policy Validation]
        DP4[Breaking Change Review]
        DP1 --> DP2 --> DP3 --> DP4
    end

    subgraph Release[Release Phase]
        direction TB
        R1[OpenAPI Schema]
        R2[SDK Docs]
        R3[Code Tools]
        R1 --> R2 --> R3
    end

    subgraph Runtime[Runtime Phase]
        direction TB
        RT1[HTTP Headers]
        RT2[Schema Validation]
        RT1 --> RT2
    end

    subgraph Upgrade[Upgrade Phase]
        direction TB
        U1[Impact CLI]
        U2[Dashboard]
        U3[Dry-Run]
        U1 --> U2 --> U3
    end

    %% Connections between phases
    DevPre --> Release
    Release --> Runtime
    Runtime --> Upgrade
```

### Change Communication Schedule

```mermaid
gantt
    title Deprecation Schedule for API v2025.1
    dateFormat  YYYY-MM-DD
    section Lifecycle
    Active Development : active, 2025-01-01, 90d
    Deprecation Notice : 2025-04-01, 90d
    Compatibility Mode : 2025-07-01, 90d
    End of Life        : 2025-10-01, 1d
```

| Phase         | Duration  | Communication Channels                                             |
| ------------- | --------- | ------------------------------------------------------------------ |
| Announcement  | 90 days   | API headers, OpenAPI metadata, email notices, developer portal     |
| Compatibility | 180 days  | Support both versions, code transformation tools, migration guides |
| End of Life   | Immediate | Remove deprecated endpoints                                        |

## Impact Preview & Reporting

```mermaid
graph LR
    A[Upgrade Initiated] --> B[Version Comparison]
    B --> C[Database Impact Scan]
    B --> D[Config Change Analysis]
    B --> E[API Compatibility Check]
    C --> F[Migration Preview Report]
    D --> G[Config Diff Report]
    E --> H[Breaking Changes List]
    F --> I[Consolidated Impact Report]
    G --> I
    H --> I
```

### Impact Report Components

- **Database Impact**:

   - Schema changes
   - Data migration requirements
   - Estimated execution time

- **API Compatibility**:

   - Breaking changes
   - Required client updates
   - Deprecation timeline

- **Configuration Changes**:

   - Modified settings
   - New environment variables
   - Security implications

### Impact Report Sample

```json
{
  "upgrade_path": "2025.1 → 2025.2",
  "risk_level": "medium",
  "estimated_downtime": "15 minutes",
  "critical_issues": [
    {
      "type": "schema_change",
      "location": "marketplace/Resources",
      "description": "Required field 'category' added"
    }
  ],
  "actions_required": [
    "Update client code to handle new required field",
    "Execute a management command to migrate data"
  ]
}
```

## Stabilization Action Plan

### Phase 1: Inventory & Classification

- Catalog all API endpoints by functional group
- Assign current maturity level (alpha/beta/stable)
- Identify breaking changes in last 2 releases

### Phase 2: Stabilization Foundations

- Add header-based versioning (`Waldur-Version`)
- Introduce version match validation in SDK
- Introduce standardized error format
- OpenAPI schema validation in pull requests
- Breaking change detection gates
- Automated SDK documentation publishing
- Set up versioning automation for alpha/beta releases

### Phase 3: Impact Analysis Tooling

- Database migration previews
- Configuration change detection
- API compatibility scanning
- Dry-run execution framework
- Risk score calculation
- Data loss probability assessment
- Downtime estimation
- Actionable remediation steps
- Automated customer alerts
- Personalized impact assessments
- Upgrade scheduling dashboard

## Key Metrics for Success

- 100% breaking changes detected in CI
- Zero unannounced breaking changes in stable APIs
- 90%+ deprecated endpoints removed on schedule
- <30 days between beta and stable promotion
- 100% of new features launch behind feature flags

## Example workflows

These examples demonstrate how to apply lifecycle and communication rules in practice.

### Patching and Releasing an Older Supported Release

**Context**: Waldur 2025.1 is in **Security Maintenance** phase.

**Scenario**: A security bug is discovered in the `marketplace` app in version 2025.1.

**Steps**:

1. **Create a branch** from the `release/2025.1` tag.
2. Apply the patch fix (e.g., sanitize input in `marketplace.views.OfferingViewSet`).
3. Bump patch version: `2025.1.4` → `2025.1.5`.
4. Add changelog entry under `SECURITY FIXES`.
5. Create new tag `release/2025.1.5`, trigger CI/CD.

**Communication**:

- Email notification for operators
- Waldur HomePort dashboard warning for operators


### Adding a New Endpoint in a Mature App (e.g., `openstack`, maturity: **stable**)

**Scenario**: Add a new endpoint to list all flavors with extended metadata.

**Constraints**:

- Must be backward-compatible
- Cannot break existing consumers

**Steps**:

1. Create a new action or viewset method: `GET /openstacktenant-flavors/extended/`.
2. Use `@extend_schema` to document new response format in OpenAPI.
3. Add unit and integration tests.
4. Add a changelog entry under `FEATURES`.
5. Merge into `develop`.
6. New version number will be **minor**: e.g., `2025.2.3` → `2025.2.4`.

**Communication**:

- Added to OpenAPI schema
- SDK is regenerated
- Endpoint is announced in changelog


### Adding a New Endpoint in an Experimental App (e.g., `checklist`, maturity: **alpha**)

**Scenario**: Introduce a new endpoint for scoring checklist responses.

**Steps**:

1. Create endpoint: `POST /checklist-items/{uuid}/score/`.
2. No guarantee of stability — endpoint can be renamed/removed later.
3. Version updated in `checklist.VERSION = 2025.2-alpha.7`.
4. No changelog required, but internal commit message must follow pattern:

   ```text
   feat(checklist): add scoring endpoint [alpha]
   ```

**Communication**:

- Only available when feature flag enabled
- Not included in stable OpenAPI documentation
- Optional preview in dev dashboard

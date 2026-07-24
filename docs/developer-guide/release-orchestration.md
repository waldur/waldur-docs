# Release Orchestration

This document describes the automated, decentralized CI/CD release orchestration system that coordinates releases across the entire Waldur ecosystem from the `waldur-docs` repository.

## Overview

The `waldur-docs` repository serves as the central orchestration hub for Waldur releases. To avoid monolithic bottlenecks, Waldur relies on **GitLab CI/CD Multi-Project Triggers** and **Directed Acyclic Graphs (DAG)**.

When a version tag (e.g., `8.0.6`) is pushed to `waldur-docs`, it acts merely as an **orchestrator/router**. It delegates the release authority to the downstream repositories themselves by triggering their native pipelines and passing the target `$RELEASE_VERSION`.

This ensures:

1. **Parallel Execution:** Releases happen concurrently across the ecosystem.
2. **Resilience:** A failure in one downstream pipeline does not halt independent components.
3. **Separation of Concerns:** Repositories own their specific deployment mechanics.

## Coordinated Repositories

### Core components

- **waldur-mastermind** — Backend API and business logic
- **waldur-homeport** — Frontend web application
- **waldur-prometheus-exporter** — Metrics and monitoring

### Deployment & infrastructure

- **waldur-helm** — Kubernetes Helm charts
- **waldur-docker-compose** — Docker Compose configurations

### SDKs & client libraries

- **py-client** — Python SDK
- **js-client** — TypeScript/JavaScript SDK
- **go-client** — Go SDK
- **rs-client** — Rust SDK
- **terraform-provider-waldur-generator** — Terraform Provider
- **ansible-waldur-generator** — Ansible Collection
- **waldur-cli-generator** — scriptable CLI (generates
  [waldur-cli](https://code.opennodecloud.com/waldur/waldur-cli) by parsing the OpenAPI
  schema directly -- the same as the SDKs, and with no dependency on rs-client or any other
  generated client, including for request-body validation). Still triggered from the
  `infrastructure` stage rather than `sdks` in `.gitlab-ci.yml` ("Generate and release
  Waldur CLI" extends `.rules-rc-release`, not `.sdk-trigger-base` like the SDKs below).

## Release Process

### For maintainers

The recommended way to create a release is via the local release script:

```bash
./scripts/release.sh 8.0.6
```

The script performs these steps locally before pushing:

1. **Pre-flight check** — verifies the tag doesn't already exist in any downstream repo
2. **Collect commit data** from local clones of all repositories
3. **Generate changelog** using Claude Code with the commit data
4. **Review** — presents the changelog for approval (accept / edit / regenerate / quit)
5. **Commit changelog** to `docs/about/CHANGELOG.md`
6. **Tag and push** — pushes the changelog commit and the version tag to origin

Once the tag is pushed, the CI pipeline takes over automatically.

Alternatively, you can tag manually (e.g., if the changelog was already committed):

```bash
git tag -a 8.0.6 -m "Release 8.0.6"
git push origin 8.0.6
```

## Pipeline Stages & Execution Flow

The release orchestration pipeline inside `waldur-docs` strictly utilizes sequential pipeline stages to natively enforce the logical flow of a release and its dependency chain.

```mermaid
graph TD
    subgraph 1. Test Stage
        T[Linting, Regex Tests, Code Scans]
    end

    subgraph 2. Release Stage
        C1(Release Mastermind)
    end

    subgraph 3. Schema Stage
        O[Generate OpenAPI Schema]
    end

    subgraph 4. SDKs Stage
        S1(Generate and release API Docs)
        S2(Generate and release Python SDK)
        S3(Generate and release TypeScript SDK)
        S4(Generate and release Go SDK)
        S5(Generate and release Rust SDK)
        S6(Generate and release Terraform Provider)
        S7(Generate and release Ansible Collection)
    end

    subgraph 5. Infrastructure Stage
        D1(Release Homeport)
        D2(Release Prometheus Exporter)
        D3(Release Helm)
        D4(Release Docker Compose)
        D5(Generate and release Waldur CLI)
    end

    subgraph 6. Finalize Stage
        CH[Generate Consolidated Changelog]
        MK[Build Tagged MkDocs Pages]
        SL[Announce on Slack]
    end

    T --> C1
    C1 --> O
    O --> S1 & S2 & S3 & S4 & S5 & S6 & S7
    S1 & S2 & S3 & S4 & S5 & S6 & S7 --> D1 & D2 & D3 & D4 & D5
    D1 & D2 & D3 & D4 & D5 --> CH
    CH --> MK
    CH --> SL
```

### Stage 1: `test`

Performs static analysis, linting, and checks on the orchestration logic itself.

### Stage 2: `release` (Core Component)

The orchestrator fires a multi-project trigger to `waldur-mastermind`. This ensures the core API is tagged and published first.

### Stage 3: `schema` (Schema Generation)

The pipeline fetches the `waldur-openapi-schema.yaml` (and, where needed, `waldur-typescript-schema.yaml`) generated in the preceding `release` stage by `waldur-mastermind`'s pipeline, using the shared `.fetch-openapi-schema` CI template (see [Shared schema-fetch template](#shared-schema-fetch-template) below). It then commits the versioned schema file back to `waldur-docs`.

### Stage 4: `sdks` (First-Layer Consumers)

With the OpenAPI schema generated, the pipeline triggers the first-layer consumers of that schema: SDKs (Python, TypeScript, Go, Rust), Terraform, Ansible, and API Docs. These pipelines ingest the schema (each via the same `.fetch-openapi-schema` template) to generate their codebases and publish to package registries (NPM, PyPI, etc.) where applicable. The Rust SDK does not yet publish to crates.io — it only commits generated code to `rs-client`'s `main` branch (and a tag on stable releases), same as `go-client`.

### Triggering an individual SDK build

Two ways to exercise SDK generation without doing a full release:

- **Orchestrated, all SDKs at once**: on `waldur-docs`, use GitLab's **Run pipeline** with the CI/CD variable `BUILD_SDK=true` on the `master` branch. This satisfies the `.rules-sdk-release` rule shared by every `Generate and release *` job, so it fans out to Python, TypeScript, Go, Rust, Terraform, and Ansible simultaneously — there is no per-SDK toggle.
- **Standalone, a single SDK**: go directly to that SDK's own repository and use **Run pipeline**
  there. Every downstream repository's build/release (and, for `py-client`/`js-client`, publish)
  jobs accept `CI_PIPELINE_SOURCE == "web"` in addition to `"pipeline"`/`"trigger"`, so this works
  uniformly across `rs-client`, `go-client`, `py-client`, `js-client`, and
  `waldur-cli-generator`. No variables are needed for a nightly build: `RELEASE_VERSION` is empty
  on a plain manual run, which takes the nightly-commit (or, for `py-client`/`js-client`,
  publish-to-dev-registry) path rather than tagging a release. Setting `RELEASE_VERSION` to a
  semver string on that same manual run takes the tagged-release path instead, exactly as a
  `pipeline`/`trigger`-sourced run would.

### Shared schema-fetch template

Every downstream repository that needs the OpenAPI schema (`waldur-docs`, `rs-client`, `go-client`, `py-client`, `js-client`, `api-docs`, `ansible-waldur-generator`, `terraform-provider-waldur-generator`) fetches it the same way, via `extends: .fetch-openapi-schema` (defined in `waldur-pipelines/templates/utils/release-utils.yml`). Consumers just declare a `Fetch OpenAPI schema` job and depend on its artifacts:

```yaml
Fetch OpenAPI schema:
  extends: .fetch-openapi-schema

Build My SDK:
  needs:
    - job: Fetch OpenAPI schema
      artifacts: true
```

The template is a self-contained Python script with no bash/curl/jq dependency. It:

1. **For pipeline/trigger/release runs**, looks up a successful `Generate OpenAPI schema` job in `waldur-mastermind`'s pipelines via the GitLab API, downloading and extracting its artifacts. Requests try `CI_JOB_TOKEN` first and fall back to the `GITLAB_TOKEN` CI/CD variable on an auth failure, since a job token's cross-project access is scoped per project and isn't always allow-listed.
2. **Otherwise (or as a fallback)**, resolves the latest published schema version from the **public GitHub mirror** of `waldur-docs` (`api.github.com` + `raw.githubusercontent.com`) and downloads it from there — deliberately not the internal GitLab API, which 404s for repos whose job tokens aren't cross-project allow-listed (GitLab returns 404 rather than 403 on scope violations, to avoid leaking project existence).
3. **Validates** that whatever was downloaded is actually an OpenAPI document before declaring success, rejecting HTML sign-in/error pages that GitLab can return with an HTTP 200.

Set `DOWNLOAD_TYPESCRIPT_SCHEMA: "true"` in the job's `variables` to also produce `waldur-typescript-schema.yaml` as an artifact (used by `js-client`).

### Stage 5: `infrastructure` (Second-Layer Consumers & Infrastructure)

This stage triggers components that rely on the artifacts published in earlier stages:

- **Homeport:** Dynamically updates its `yarn.lock` to install the newly published JS SDK, performs a compilation test, and tags itself.
- **Prometheus Exporter:** Dynamically updates its dependency to point to the newly published Python SDK package.
- **Helm & Docker Compose:** Update their image tags to match the newly released Mastermind and Homeport versions.

### Stage 6: `finalize` (Finalization)

The `Generate consolidated changelog` job acts as the final synchronization barrier. It explicitly waits for all triggers across the `release`, `sdks`, and `infrastructure` stages to finish.

When the entire Waldur ecosystem has successfully released, this job:

- Detects the previous version from `CHANGELOG.md`.
- If a changelog entry for this version doesn't already exist (i.e., not created by the local release script), it auto-generates one using `generate_enhanced_changelog_multi_repo.py`.
- Includes Terraform breaking changes and Ansible collection notes since those downstream repos have been updated.
- Rotates old entries (keeps the last 20).
- Updates `publiccode.yml`.
- Commits and pushes the final documentation commit to master.

### Validation

The release is complete when:

- [ ] All repositories have the new tag
- [ ] Helm chart versions are updated
- [ ] Docker Compose configurations reference new image tags
- [ ] SDK packages are released with new versions
- [ ] Documentation is deployed with the new version
- [ ] Changelog is updated with cross-repository diff links
- [ ] OpenAPI schema is committed

## Shared Release Templates

To avoid duplicating boilerplate git commands across the downstream repositories, we utilize a shared CI template hosted in `waldur-pipelines/templates/release/tag-release.yml`.

Downstream repositories consume this template using `extends: .release-tag-base`.

For repositories that require file modifications prior to tagging (e.g., injecting the new version into Helm charts), they extend the template and leverage the custom `!reference [.release-tag-base, tag_script]` block. This allows them to execute their specific `sed` substitutions and `git commit` commands, then seamlessly hand execution back to the shared template to create and push the git tag.

## Changelog

Each release changelog is generated with cross-repository commit data and includes:

- **Summary** of user-visible changes grouped by theme (What's New, Improvements, Bug Fixes)
- **Cross-repository diff links** for each component:

    ```markdown
    * Waldur MasterMind: [tag diff](https://github.com/waldur/waldur-mastermind/compare/8.0.5...8.0.6)
    ```

- **Resources** section linking to the OpenAPI schema and API changes diff

Changelogs are stored in `docs/about/CHANGELOG.md` with automatic rotation (last 20 entries kept).

## Documentation versioning

Versioned documentation is deployed to GitHub Pages using `mike`:

```bash
# Latest alias (deployed on every master push)
mike deploy latest -p -r github_waldur -b gh-pages

# Tagged versions (deployed in post-deploy stage)
mike deploy $CI_COMMIT_TAG -p -r github_waldur -b gh-pages
```

Each release also includes a versioned OpenAPI schema file at `docs/API/waldur-openapi-schema-{version}.yaml`.

## RC (Release Candidate) releases

RC releases allow testing a full deployment stack before committing to a stable release. An RC tag triggers the tagging and version-update workflow across downstream repos, but skips artifacts that should only be produced for stable releases (like SDKs).

### Tag format

```text
X.Y.Z-rc.N
```

Examples: `8.0.6-rc.1`, `8.0.6-rc.2`, `10.0.0-rc.1`

### Creating an RC release

```bash
# Using the local release script
./scripts/release.sh 8.0.6-rc.1

# Or manually
git tag -a 8.0.6-rc.1 -m "RC 8.0.6-rc.1"
git push origin 8.0.6-rc.1
```

### What RC triggers vs. skips

| Action | Stable release | RC release |
|--------|:-:|:-:|
| Tag downstream repos (mastermind, homeport, helm, docker-compose, prometheus-exporter) | Yes | Yes |
| Update Helm `Chart.yaml` / `values.yaml` | Yes | Yes |
| Update Docker Compose `.env.example` | Yes | Yes |
| Test Docker Compose deployment | Yes | Yes |
| Test Helm deployment | Yes | Yes |
| Generate changelog | Yes | **Yes** (replaced by stable) |
| Generate OpenAPI schema | Yes | **Skipped** |
| Release SDKs & Terraform/Ansible | Yes | **Skipped** |
| Deploy versioned documentation | Yes | **Skipped** |

### Promoting RC to stable

Once an RC has been validated, create the stable tag on the same commit:

```bash
./scripts/release.sh 8.0.6
```

This runs the full stable release workflow — changelog generation, SDK releases, docs deployment, and all other steps that were skipped during the RC.

### Downstream repo compatibility

All downstream repos use `if: $CI_COMMIT_TAG` (without a regex filter) for Docker image builds and chart packaging, so RC tags work out of the box with no changes needed in any downstream repository.

## Emergency procedures

### Rolling back a release

If a release needs to be rolled back:

1. **Remove the git tag** from all repositories
2. **Revert configuration changes** in helm and docker-compose repositories
3. **Update documentation** to remove the problematic version
4. **Coordinate with package repositories** (PyPI, npm) if SDKs were published

### Partial release recovery

If only some repositories were tagged successfully:

1. **Identify missing tags** by checking each repository
2. **Manually tag missing repositories** using the same tag message
3. **Re-run failed CI jobs** if configuration updates are missing

## Security considerations

- **SSH keys** for GitHub authentication are stored as GitLab CI variables
- **GitLab tokens** provide access to private repositories
- **Automated testing** validates deployments before release completion

# Grafana and Prometheus Metrics

Waldur Homeport includes a number of reports, but for cases when additional custom reports need to be created,
it is possible to setup a time-series database, for example, Prometheus, and setup business metrics exporter
for Waldur.

This would allow to create live dashboards exposing, for example, growth of adoption of the platform in terms
of users and offerings, aggregated costs of resource on a daily or weekly basis, total active provisioned resources
on an hourly basis and so on.

To achieve that, [waldur-prometheus-exporter](https://github.com/waldur/waldur-prometheus-exporter) needs to be setup.
In addition, we provide example [Grafana dashboard json](grafana-dashboard.json) for visualising the metrics.

## Creating a database user with restricted permissions

When integrating Grafana with Waldur's database, we will create a dedicated database user with restricted permissions. For this, run the following commands using `psql` under your Waldur database user:

```sql
CREATE USER postgres_stats WITH PASSWORD 'password';

GRANT SELECT ON ALL TABLES IN SCHEMA public TO postgres_stats;

ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO postgres_stats;

```

When setting up Grafana, use the postgres_stats user to connect to your database with the appropriate permissions.

## Prometheus metrics

Prometheus exporter allows to setup export of business metrics and reporting information at the fine-grained
granularity, for example, every 5 minutes or daily. Collected information can then be visualized in Grafana or
other visualisation solutions.

The exporter currently publishes the following metric families.

### Platform totals

| Metric | Description |
|--------|-------------|
| `waldur_users_total` | Total count of users |
| `waldur_customers_total` | Total count of organizations |
| `waldur_projects_total` | Total count of projects |
| `waldur_owners_users_total` | Users with owner permissions |
| `waldur_support_users_total` | Support users |
| `waldur_local_users_total` | Users with local registration method |
| `waldur_marketplace_resources_total` | Total count of active resources |

### User breakdowns

| Metric | Description |
|--------|-------------|
| `waldur_user_auth_method_count` | Users by authentication method (local, saml2, tara, eduteams, …) |
| `waldur_user_identity_source_count` | Users by identity source |
| `waldur_user_organization_count` | Users by organization |
| `waldur_user_organization_type_count` | Users by organisation type (SCHAC URN) |
| `waldur_user_affiliation_count` | Users by affiliation |
| `waldur_user_registration_count` | Monthly count of new user registrations |

### Per-organization

| Metric | Description |
|--------|-------------|
| `organization_project_count` | Projects per organization |
| `organization_resource_count` | Resources per organization |
| `organization_members_count` | Members per organization |

### Usage, limits and cost

| Metric | Description |
|--------|-------------|
| `resources_limits` | Resource limits by offering, organization group and country |
| `aggregated_usages` | Aggregated usages by offering, organization group and country |
| `aggregated_usages_per_month` | Aggregated usages per month |
| `component_usages_per_project` | Component usages per project |
| `total_cost_of_active_resources_per_offering` | Total cost of active resources per offering |
| `resource_usage_by_customer_resources` | Active resources per customer |
| `resource_usage_by_customer_cost` | Cost of active resources per customer |
| `resource_usage_by_customer_component` | Absolute component usage per customer and component type |
| `resource_limit_by_customer_component` | Allocated component limit per customer and component type |
| `resource_utilization_by_customer_component` | Component utilisation (usage / limit × 100) per customer and component |
| `resource_usage_by_organization_type` | Component usage by organisation type and component type |
| `resource_count_by_organization_type` | Active resource count by organisation type and component type |
| `waldur_platform_usage_trend_resource_count` | Monthly count of resources with recorded usage |

### Service provider view

| Metric | Description |
|--------|-------------|
| `count_users_of_service_provider` | Users visible to a service provider |
| `count_projects_of_service_provider` | Projects visible to a service provider |
| `count_projects_of_service_provider_grouped_by_oecd` | …grouped by OECD science code |
| `count_unique_users_connected_with_active_resources_of_service_provider` | Unique users with active resources |
| `count_active_resources_grouped_by_offering` | Active resources by offering |
| `count_active_resources_grouped_by_offering_country` | Active resources by country |
| `count_active_resources_grouped_by_organization_group` | Active resources by organization group |
| `offerings_counter_stats` | Offerings by service provider and category |

### Science-domain and industry classification

| Metric | Description |
|--------|-------------|
| `projects_usages_grouped_by_oecd`, `projects_limits_grouped_by_oecd` | Project usages / limits by OECD science code |
| `projects_usages_grouped_by_industry_flag`, `projects_limits_grouped_by_industry_flag` | Project usages / limits by industry flag |
| `count_projects_grouped_by_provider_and_oecd` | Projects with active resources by provider and OECD code |
| `count_projects_grouped_by_provider_and_industry_flag` | Projects with active resources by provider and industry flag |

### Provisioning health

| Metric | Description |
|--------|-------------|
| `provisioning_count` | Finished provisioning attempts (done + erred) |
| `provisioning_success_count` | Successful provisioning attempts |
| `provisioning_error_count` | Failed provisioning attempts |
| `provisioning_in_progress_count` | Provisioning attempts currently in progress |
| `provisioning_success_rate` | Rate of successful provisioning (0.0–1.0) |
| `avg_provisioning_duration` | Average seconds from Executing to a terminal state |
| `avg_pending_duration` | Average seconds from creation to Executing |

!!! note
    This list tracks the exporter's source. If a metric you need is missing, check
    [`src/app.py`](https://github.com/waldur/waldur-prometheus-exporter/blob/main/src/app.py)
    in the exporter repository — it is the authoritative list.

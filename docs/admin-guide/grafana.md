# Grafana and Prometheus Metrics

Waldur Homeport includes a number of reports, but for cases when additional custom reports need to be created,
it is possible to setup a time-series database, for example, Prometheus, and setup business metrics exporter
for Waldur.

This would allow to create live dashboards exposing, for example, growth of adoption of the platform in terms
of users and offerings, aggregated costs of resource on a daily or weekly basis, total active provisioned resources
on an hourly basis and so on.

To achieve that, [waldur-prometheus-exporter](https://github.com/waldur/waldur-prometheus-exporter) needs to be setup.
In addition, we provide example [Grafana dashboard json](grafana-dashboard.json) for visualising the metrics.

## Prometheus metrics

Prometheus exporter allows to setup export of business metrics and reporting information at the fine-grained
granularity, for example, every 5 minutes or daily. Collected information can then be visualized in Grafana or
other visualisation solutions.

Currently, the following metrics are supported:

- Total count of users;
- Total count of organizations;
- Total count of projects;
- Total count of users with owner permissions;
- Total count of support users;
- Total count of users with local registration method;
- Total count of users with saml2 registration method;
- Total count of users with tara registration method;
- Total count of users with eduteams registration method;
- Total count of active resources;
- Count of projects for each organization;
- Count of resources for every organization;
- Count of members for every organization;
- Resources limits by offerings, customer groups, customer countries;
- Aggregated usages by offerings, customer groups, customer countries;
- Aggregated usages per month;
- Count of users visible to service provider;
- Count of projects visible to service provider;
- Count of projects visible to service provider and grouped by OECD science code;
- Total cost of active resources per offering;
- Projects usages grouped by OECD science code;
- Projects limits grouped by OECD science code;
- Projects usages grouped by industry flag;
- Projects limits grouped by industry flag;
- Count unique users connected with active resources of a service provider;
- Count active resources grouped by offering;
- Count active resources grouped by country;
- Count active resources grouped by organization group;
- Count projects with active resources grouped by provider and OECD science code;
- Count projects with active resources grouped by provider and industry flag.

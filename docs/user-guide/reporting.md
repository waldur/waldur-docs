# Reporting

Marketplace is a central module for provisioning of Waldur resources. Marketplace contains Offerings that
belong to a special type of Organizations - Service Providers. Marketplace provides common functionality
for resource lifecycle management, accounting and invoicing. Specifics are implemented in the Marketplace plugins
(e.g. for OpenStack, SLURM, Rancher, etc).

## HomePort reports

Waldur HomePort includes a number of built-in reports based on the user activity. Reports can be accessed by
staff and support users from the "Reporting" sidebar menu.

<figure markdown="span">
  ![Homeport reports](./img/reporting-homeport.png)
  <figcaption>List of built-in reports in HomePort</figcaption>
</figure>

## Grafana and Prometheus Metrics

Waldur supports exporters to Prometheus of different statistical metrics that can be used for building
business dashboards, for example, in Grafana.

Check out details about the [setup of the exporter](../admin-guide/grafana.md).

<figure markdown="span">
  ![Example of OECD-science code report](./img/grafana-sp-example.png)
  <figcaption>Example of OECD-science code report</figcaption>
</figure>

## Custom reports

It is possible to implement custom metric collection and report generation using Waldur SDK. Several examples are
provided in [the section for integrators](../integrator-guide/reporting.md).
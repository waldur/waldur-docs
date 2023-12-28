# Billing and accounting in Waldur

Accounting and billing components in Waldur are respnsible for gathering the accunting data and representing it to the
end users. Waldur has built-in reporting and accounting functionality. This allows tracking usage information in each
project and resources within that project. During the creation step of the service offering, the provider can define
the accounting components (like CPU-h, GPU-h and storage for HPC, CPU, RAM and storage for VMs) and plans, which set
the price for each defined component. Consumers can see the usage information based on the policies defined by the
provider.

From a provider point of view, Waldur supports invoice generation and exposes enough of information via APIs to
integrate with custom payment providers.

On the consumer side, Waldur provides convenient ways to see resource usage information. User interface shows overall
usage data within the project and monthly usage across resource components (for exammple, CPU, GPU and storage).
End users are  able to export the usage data to PDF, CSV and XLSX formats. Depending on the end user role,
project members are able to  see the specific project information, organization owners are able to see all projects
information within specific organization.

In addition to that, Waldur offers convenient way to export the usage information, so external visualization solutions
(like Grafana) can generate graphs based on that data. More information [about that](grafana.md).

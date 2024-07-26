# Billing and accounting in Waldur

Waldur's accounting and billing components are responsible for collecting accounting data and presenting
it to end users. It features built-in reporting and accounting functionality, enabling the tracking of
usage information for each project and its resources. During the service offering creation process,
providers can define accounting components (such as CPU-h, GPU-h, and storage for HPC; CPU, RAM, and
storage for VMs) and set the pricing plans for each component. Consumers can view usage information
according to the policies established by the provider.

From a provider point of view, Waldur supports invoice generation and exposes enough of information via APIs to
integrate with custom payment providers.

Waldur offers convenient tools for consumers to view resource usage information. The user interface displays
overall usage data within a project and breaks down monthly usage across resource components such as CPU,
GPU, and storage. End users can export this usage data in PDF, CSV, and XLSX formats. Access to information
varies by user role: project members can see details for their specific projects, while organization owners
can view information for all projects within their organization.

In addition to that, Waldur offers convenient way for exporting the usage information for visualization [with
Grafana](grafana.md).

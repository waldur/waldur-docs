# Screenshots

## Desktop view

### Login page

![Landing](img/Login-page.png)

### Organization dashboard

![Organization dashboard](img/Organization-dashboard.png)

### Project dashboard

![Project dashboard](img/Project-dashboard.png)
![Resource list](img/Resource-view1.png)
![HPC details](img/Resource-view2.png)
![OpenStack details](img/Resource-view3.png)

### Provider reporting and support dashboard

![Monthly revenue](img/Provider-reporting1.png)
![Growth reporting](img/Provider-reporting2.png)
![Support view](img/Support-view.png)

### Call management dashboard

![Call management](img/Call-managament-dashboard.png)

### Marketplace

![Marketplace](img/Marketplace-main.png)
![VPC creation](img/Marketplace-vpc.png)
![SLURM creation](img/Marketplace-hpc.png)

### Admin dashboard

![Admin dashboard](img/Admin-dashboard.png)

## Federation views

These screenshots show one Waldur instance serving several providers. They come from a demo
deployment loaded with the `public_sector_accounting` preset, so every organisation in them is
fictional. Each was taken in the light theme in a 1920 px wide window at the same zoom, and
cropped to the panel it shows.

### One catalogue across technologies

An HPC partition, an OpenStack cloud tenant, object storage and an LLM inference service from
two providers, offered side by side in one marketplace.

![Offerings of different kinds in the marketplace catalogue](img/marketplace-catalogue-across-technologies.png)

### One bill across providers

An organisation's monthly invoice. It carries tokens, core-hours, TB-months and GPU-hours from
two service providers on one bill.

![Invoice with components from two providers](img/invoice-components-across-providers.png)

### Components set by each provider

Each provider defines the components of its own offerings: what is metered, in which unit and
within which limits.

![Accounting components of an LLM inference offering](img/offering-components-tokens.png)
![Accounting components of an HPC offering](img/offering-components-hpc.png)
![Editing a component's unit and spending limits](img/offering-component-edit-tokens.png)

### Site agent

The offering dashboard shows the site agent that serves the offering: its identity, version and
uptime, and the services it runs. Each service lists the processor that handles it, when it last
ran, and the backend it talks to: orders, membership and usage reporting.

![Site agent of an HPC offering](img/site-agent-dashboard.png)
![Processor that handles orders](img/site-agent-processes-orders.png)
![Processor that synchronises membership](img/site-agent-processes-membership.png)
![Processor that reports usage](img/site-agent-processes-usage.png)

### AI inference with API keys

An inference resource with an OpenAI-compatible endpoint, and its API keys, each with its own
monthly token quota.

![API keys of an inference resource, with per-key token quotas](img/inference-resource-api-keys.png)
![Endpoint of an inference resource](img/inference-resource-endpoint.png)

### A resource served by a site agent

An HPC allocation served by a site agent. It looks like any other resource.

![HPC allocation served by a site agent](img/resource-served-by-site-agent.png)

### Usage policy set by the provider

A provider's SLURM usage policy: notify at 80% of the allocation, downscale at 100%, and pause
once the 20% grace is used up.

![SLURM periodic usage policy of an offering](img/slurm-policy-editor.png)
![Thresholds of a SLURM usage policy for one allocation](img/slurm-policy-thresholds.png)

## Mobile view

### Login page

![Landing](img/Mob-login-page.png)

### Organization dashboard

![Organization dashboard](img/Mob-organization-dashboard.png)

### Project dashboard

![Project dashboard](img/Mob-project-dashboard.png)
![Resource list](img/Mob-resource-view1.png)
![HPC details](img/Mob-resource-view2.png)
![OpenStack details](img/Mob-resource-view3.png)

### Provider reporting and support dashboard

![Monthly revenue](img/Mob-provider-reporting1.png)
![Growth reporting](img/Mob-provider-reporting2.png)
![Support view](img/Mob-support-view.png)

### Marketplace

![Marketplace](img/Mob-marketplace-main1.png)
![Marketplace](img/Mob-marketplace-main2.png)
![VPC creation](img/Mob-marketplace-vpc.png)
![SLURM creation](img/Mob-marketplace-hpc.png)

### Admin dashboard

![Admin dashboard](img/Mob-admin-dashboard.png)

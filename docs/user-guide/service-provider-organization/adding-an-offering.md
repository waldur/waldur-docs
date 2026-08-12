# Offerings

To create a new Offering in the Marketplace, you need to:

- Assure that categories are configured in the Marketplace.
- Create at least one service provider.
- Create and activate a public offering.

Waldur supports a number of different types of service providers when creating a shared offering. A common way of
creating an offering is through a HomePort.

## OpenStack offering creation

1. Select organization, which will provide the offering.

2. Go to Provider dashboard, click **Marketplace** -> **Offerings** from the top menu and then **Add** from the left.
    ![Adding an offering](../img/Add_offering_main.png)

3. A popup opens, fill in the name for the offering, category (e.g. Private clouds) and type (**OpenStack tenant**) and click **Create**.
    ![Adding details](../img/Add_offering_openstack.png)

4. An offering configuration page opens with an option to edit different attributes.

    ![Adding details](../img/OpenStack_offering_config1.png)

5. For the OpenStack integration, select **Integration** -> **Credentials** from the top menu. Fill in requested parameters.

    - **API URL** - OpenStack deployment keystone URL
    - **Domain name** - OpenStack domain name
    - **Username** - Tenant user username
    - **Password** - Tenant user password
    - **Tenant name** - OpenStack tenant name
    - **External network ID** - OpenStack extnet UUID

    ![Adding details](../img/OpenStack_offering_integration.png)

6. If everything is filled in, click on **Synchronize** in the top left corner. After few seconds, the **State** field will show **OK** if the integration is completed between Waldur and OpenStack.

7. To adjust the accounting, select **Accounting** from the top menu and then **Plans** -> **Edit prices**. Default accounting components are already defined.

    ![Adding details](../img/OpenStack_accounting_config.png)

8. If everything is completed and ready, click on **Activate** in the upper right corner to publish the offering.

### Provisioning configuration

The **Integration** → **Provisioning configuration** card groups options that change how instances and volumes are provisioned on the OpenStack backend. Most operators only need to touch a few of these; defaults are sensible.

The card is split into tabs — Filtering, Console access, Network, **Operations**, Limits, IP mapping.

#### Config drive

The **Operations** tab includes a **Config drive enabled by default** toggle. A config drive is a small read-only disk attached to the instance at boot. Cloud-init reads metadata, the SSH key and any user-supplied start script from it, without going through the OpenStack metadata service on the network (`http://169.254.169.254`).

![Provisioning configuration Operations tab with the Config drive toggle](../img/openstack-config-drive-provider.png)

- Enable this when guests typically cannot reach the metadata service — for example, when tenant networks have no DHCP, or sit on an isolated segment.
- Leave it off when the metadata service is reachable, which is the usual case.

The toggle sets the **provider-wide default**. Users can override it per instance at order time (see [Config drive](../customer-organization/resource_management.md#config-drive) in the customer guide).

## SLURM offering creation

1. Select organization, which will provide the offering.

2. Go to Provider dashboard and click on **Marketplace** -> **Offerings** from the top menu and then click **Add** from the right.
    ![Adding an offering](../img/Add_offering_main.png)

3. A popup opens, fill in the name for the offering, category and type.
    ![Adding details](../img/Add_offering2.jpg)

4. An offering configuration page opens with an option to edit different attributes.
    ![Offering details](../img/Offering_edit.jpg)

5. Under Endpoints section, you can add access endpoints for the offering, for example, management consoles, SSH login nodes or similar.
    ![Offering endpoints](../img/Offering_edit_endpoints.png)

    This configuration will display then to resource of the offering a menu for easier navigation to the corresponding services. For SSH protocol this would trigger
    opening of an SSH client if configured for the browser. Out of the box works on OS X and Linux, requires configuration of the default application on Windows.
    ![Resource endpoints](../img/Resource_endpoints.png)

6. To add accounting components, select "Accounting components" from the top menu and then "Add component" from the right side. Accounting component is a measurable unit of a resource. For example, it can be CPU hours, GPU hours, storage hours, RAM etc.
    ![Accounting components](../img/Accounting_components.jpg)

7. A popup opens with possibility to configure fields and select the accounting type (whether the component is billed by the usage, max limit or it has a fixed price).

    - Usage-based - billing is applied according to the actual usage of the resource during the billing period defined in the accounting plan after the submission of a usage report;
    - Limit-based - billing is applied according to the requested/updated limits of a resource, actual usage can be below the limits and it is not the basis of the billing;
    - Fixed price - billing is applied according to the exact values defined by the service provider in the accounting plan, limits and usage are not the basis for the accounting;
    - One-time - billing is applied once on resource activation;
    - One-time on plan switch - billing is applied once on resource activation and everytime a plan has changed, using pricing of a new plan.

    ![Accounting component details](../img/Add_component.png)

8. To configure accounting frequency and prices, select "Accounting plans" from the top menu and then "Add plan" from the right. Select a name for the plan and accounting frequency.
    ![Accounting frequency](../img/Accounting_plan.png)

9. To define prices for the components, select "Actions" and then "Edit prices". Set new price and save. If there is a need to provide higher priority access to resources with different prices, then it is advised to create another offering for this kind of cases.
    ![Offering prices](../img/Offering_edit_prices1.png)

    ![Offering prices](../img/Offering_edit_prices.png)

10. If all set, click "Activate" on the top-right side to make it visible to everybody.
    ![Activate offering](../img/Offering_activation.png)

!!! tip
    For more advanced cases of management of offerings, take a look at how a SLURM offering can be managed using
    [Ansible module](https://github.com/waldur/ansible-waldur-module/blob/develop/waldur_batch_offering.py).

## Configuring billing model per component

Waldur supports configuring the billing model for each component individually. The same OpenStack Tenant offering type can have different billing configurations depending on the use case:

- **Monthly billing** (default): Components use **Limit-based** accounting type. Customers are billed monthly based on their reserved limits (e.g., 4 cores × €1/core/month).
- **Prepaid billing**: Components use **One-time** accounting type with the **Pre-paid** option enabled. Customers pay upfront for the full duration (e.g., 4 cores × €1/core/month × 3 months = €12 total).

### Default: Limit-based (monthly billing)

By default, OpenStack Tenant offerings come with three built-in components — Cores, RAM, and Storage — all configured as **Limit-based** with monthly billing.

### Switching all components with "Switch modes"

The fastest way to switch between monthly and prepaid billing is the **Switch modes** dropdown on the Accounting → Components tab. It combines both billing mode and storage mode options in one menu:

![Components tab with Switch modes dropdown](../img/openstack-switch-modes-button.png)

Click **Switch modes** → **Billing mode** to open a dialog where you can select the billing model for all infrastructure components at once:

![Switch modes dropdown with Billing mode and Storage mode options](../img/openstack-switch-modes-dropdown.png)

After selecting "Prepaid (One-time)" and saving, all built-in components (Cores, RAM, Storage) switch to "One-time" (prepaid). Custom components like "Consultancy Hours" are not affected.

![All infrastructure components switched to One-time](../img/openstack-all-prepaid-result.png)

### Switching individual components

You can also configure each component individually:

1. Navigate to the offering's **Edit** → **Accounting** → **Components** tab.
2. Click the action menu (⋮) on the component you want to change and select **Edit**.
3. Change the **Accounting type** from "Limit-based" to **"One-time"**.
4. Enable the **Pre-paid component** toggle.
5. Optionally configure duration constraints (min/max duration, renewal settings).
6. Click **Save**.

This allows mixed configurations — for example, CPU and RAM as prepaid while Storage remains monthly.

One-time components also support **Min value** and **Max value** constraints, which limit the quantity a customer can order. These fields appear alongside the Pre-paid toggle in the component edit dialog.

![One-time component with min/max value fields](../img/one-time-component-min-max.png)

!!! note
    For prepaid offerings, the **Termination date** (end date) is required when ordering. The total upfront charge is calculated as `price × limit × months`.

### How billing works for each model

| Billing model | Invoice frequency | Formula | Limit changes |
|---------------|-------------------|---------|---------------|
| **Limit-based** (monthly) | Every month | `price × limit` per month | Adjusted on current month's invoice |
| **One-time + prepaid** (upfront) | Once at creation | `price × limit × months` | Supplementary charge for `(new - old) × remaining months` |
| **Limit-based / Total** (one-time) | Once at creation | `price × limit` | Incremental charge for difference |

## Pausing or downscaling resources on usage limit

For offerings with **limit-based** components, Waldur can automatically restrict a resource once its reported usage reaches the component's limit for the current accounting period — pausing or downscaling the resource until usage drops back below the limit. Use this when a limit should act as a hard ceiling on consumption, not only as a billing basis.

### Prerequisites

- The offering has at least one **limit-based** component with a limit configured for an accounting period (monthly, quarterly, annual or total).
- Usage is reported against that component, either by the service provider or by the backend.

### Enabling it

1. Open the offering's **Edit** page, go to the **Integration** settings and open the **Resource lifecycle** tab.
2. Set **Action on usage limit** to one of:
    - **Pause** — the resource is paused when the limit is reached.
    - **Downscale** — the resource is downscaled when the limit is reached.
3. Leave the field empty to disable the behavior.
4. Click **Save**.

Pause and downscale are mutually exclusive — an offering uses at most one of them.

### How it behaves

- When the reported usage of any limit-based component reaches or exceeds its limit for the current period, the resource is automatically **paused** or **downscaled**, according to the offering setting.
- The restriction is **lifted automatically** when usage drops back below the limit — for example, when a new billing period resets the period's usage, or when the component's limit is raised.
- For the **Total** accounting period, usage accumulates over the whole life of the resource and never resets, so the restriction is lifted only if the limit is increased.
- The feature toggles the same **Paused** / **Downscaled** state shown on the resource page. Only restrictions applied by this feature are lifted automatically — a resource paused manually, by a grace period, or by a cost and usage policy is left untouched.

!!! note
    For provider backends that enforce these states (such as SLURM via the site agent), pausing blocks further usage and downscaling reduces the resource's share. For other backends the state is recorded and visible, but enforcement depends on the backend.

## Adding custom components

Service providers can add custom accounting components to any offering alongside the built-in ones. This is useful for non-infrastructure services like consultancy hours, support packages, or training credits.

To add a custom component:

1. Navigate to the offering's **Edit** → **Accounting** → **Components** tab.
2. Click **Add component**.
3. Fill in:
    - **Internal name**: a machine-readable identifier (e.g., `consultancy_hours`)
    - **Display name**: shown to users (e.g., "Consultancy Hours")
    - **Measured unit**: the unit label (e.g., "hours")
    - **Accounting type**: select the billing model (e.g., "Limit-based" with "Maximum total" for one-time flat charges)
4. Click **Confirm**.

![Custom component added to OpenStack offering](../img/openstack-custom-component-added.png)

Custom components appear alongside built-in components in the order form and pricing views. They are billed according to their configured accounting type but are not pushed to the OpenStack backend as quotas.

!!! tip
    Use **Limit-based** with **Maximum total** period for one-time flat-rate services like consultancy hours. Use **One-time + Pre-paid** for subscription-based add-ons that scale with duration.

## Volume discounts

Service providers can configure volume discounts on a plan's components to reward
larger usage. A discount grants a percentage reduction on a component once the
customer's usage reaches a threshold, and is applied automatically when the
invoice is finalized.

### Configuring discounts

1. Navigate to the offering's **Edit** → **Accounting** → **Plans** tab.
2. Open a plan's **⋮** actions menu and choose **Edit discounts**.
3. For each component, build the discount and pick its scope, then save.

![Edit discounts dialog with the tier builder and scope selector](../img/volume-discount-tier-builder.png)

#### Tier builder

Add one or more **tiers** — each grants a percentage discount once usage reaches
a threshold (*when usage ≥ N → X % off*). Add several tiers for graduated
pricing; higher thresholds take precedence. Use the **Preview** field to check
the resulting discount for a sample usage. Leave a component with no tiers for no
discount.

#### Discount scope

Each component has a **Discount scope**:

- **Aggregated across the customer's resources** (default) — usage is summed
  across all of the customer's resources of the offering before the discount is
  applied, so consolidating usage can reach a higher tier.
- **Per resource** — each resource is discounted on its own usage independently.

#### Advanced formula

For discounts that are not simple tiers (for example a capped continuous
discount such as `MIN(20, usage / 100)`), switch to **Advanced: edit formula**
and enter a formula directly. The formula returns a percentage (clamped to
0–100) as a function of the usage bound to `usage`, and supports the functions
`MIN`, `MAX`, `LN`, `LOG10`, `FLOOR`, `CEIL`, `POW` and `ABS`.

### How discounts appear

Volume discounts are computed at invoice finalization, not at order time, so the
exact saving depends on the customer's actual usage for the month. On the
customer's invoice the discount appears as a separate negative line paired with
each discounted component — see
[volume discounts on invoices](../customer-organization/affiliate-earnings.md#volume-discounts-on-invoices).

!!! tip
    Discounts are configured per plan. When a customer has resources on
    different plans of the same offering, keep a component's discount consistent
    across the plans, since the aggregated discount uses one plan's formula for
    the whole offering component.

## Offering management

It is possible to temporarily unpublish the offering. For example, if the service is down for a longer maintenance. To do that, open the offering edit page and click on **Pause** from the right.

![Offering pause](../img/Offering_pause.png)

If the offering is not needed anymore, then it is possible to archive it by selecting **Archive** from the offering edit page.

![Offering archive](../img/Offering_archive.png)

## Restricting who can see and order an offering

By default a shared offering is visible to everyone in the marketplace catalog. You can restrict an offering so that only users holding specific **project or organization roles** can see and order it.

Open the offering's edit page and go to **Integration → Operations → Orders & approval**. In the **Restrict to roles** field, select one or more roles (for example *Project manager* and *Project administrator*).

![Restrict to roles field](../img/offering-restrict-to-roles.png)

The dropdown lists both project roles and organization roles, so you can combine them (for example *Organization owner* and *Project manager*):

![Selecting roles to restrict the offering](../img/offering-restrict-to-roles-dropdown.png)

When the field is set:

- The offering is **hidden from the marketplace catalog** for users who do not hold one of the selected roles. Existing consumers who already have resources from the offering keep access to it.
- Only users holding one of the selected roles **in the target project or its organization** can create an order for it. Other users get a "restricted to designated project roles" error.
- When the offering is opened from the marketplace, the order form's **organization** and **project** selectors only list the organizations and projects where the user holds one of the required roles, so a user cannot accidentally order into a project where they lack access.
- Staff and support users are not affected and can always see and order the offering.

!!! note
    This setting controls **visibility and ordering** only. Whether a user's order skips consumer-side approval depends on whether their role has the order-approval permission — it is not granted by this restriction. Provider-side review continues to follow the offering's type.

Leave the field empty to remove the restriction and make the offering available to everyone again.

## Embedding images in the offering description

The **Description** and **Full description** fields use a rich Markdown editor. When image support is enabled, you can embed images directly into these descriptions — for example, an architecture diagram or a screenshot of the service.

!!! note
    This feature must be enabled by the platform administrator. Image embedding becomes available only when the `allow_display_of_images_in_markdown` feature is turned on, and uploading from your device additionally requires the `ENABLE_MARKDOWN_IMAGE_UPLOAD` setting. Uploaded images are limited to the size configured in `MARKDOWN_IMAGE_MAX_SIZE_MB` (5 MB by default).

To add an image:

1. On the offering's **Edit** page, find the **Description** or **Full description** field and click its **Edit** button.
2. In the editor toolbar, click the **Insert image** button.

    ![Markdown editor with the Insert image button](../img/offering-description-image-toolbar.png)

3. In the dialog, either choose a file from your device to upload, or paste an image URL. Optionally fill in the **Alt** and **Title** fields, then click **Save**.

    ![Upload an image dialog](../img/offering-description-image-upload-dialog.png)

4. The image is uploaded and embedded in the description. Click **Update** to save your changes to the offering.

    ![Image embedded in the description editor](../img/offering-description-image-embedded.png)

!!! warning
    Images are uploaded to the platform's media storage as soon as you add them, before you save the offering. Keep image sizes reasonable to stay within the configured upload limit.

## Description length limit

Short **description** fields are limited to **4,096 characters**. The limit applies to the offering description, plan descriptions, project descriptions and call descriptions. It is a fixed limit built into Waldur — it is not a deployment setting, and cannot be raised by configuration.

Long-form fields are not affected: the offering's **Full description** and **Vendor details** have no length limit, so a description that has outgrown 4,096 characters usually belongs in Full description instead. Both fields sit next to each other on the offering's **Edit → Public information → Basic info** panel:

![Description and Full description on the offering edit page](../img/offering-description-fields.png)

!!! note "HTML escaping counts toward the limit"
    Descriptions are sanitised before they are stored, which escapes the characters `&`, `<` and `>` into their HTML entities (`&` becomes `&amp;`, five characters instead of one). The **escaped** text is what has to fit within 4,096 characters.

    Text containing many such characters therefore reaches the limit sooner than its visible length suggests — a bibliography full of `&` can be rejected at around 4,000 characters. When this happens, Waldur says the value is too long after sanitisation, so the message can be told apart from an ordinary over-length description.

## Configuring Getting Started Templates

When setting up an offering, you can configure a "Getting Started" guide that will be shown to users after they provision a resource. This guide supports dynamic variables that are automatically replaced with actual resource values.

### Available Template Variables

- `{resource_name}` - The name of the resource
- `{resource_username}` - The username associated with the resource
- `{backend_id}` - The backend identifier (e.g., SLURM account name)
- `{backend_metadata_key}` - Any metadata fields from the backend (e.g., `{backend_metadata_state}`)
- `{options_key}` - Any custom options set for the resource (e.g., `{options_custom_field}`)

### Example Template

For SLURM allocations, you might want to create a comprehensive guide like this:

```markdown
# Getting Started with your SLURM Allocation

Welcome to your new SLURM allocation. Here are your access details:

- Account name: {backend_id}
- Username: {resource_username}
- Resource name: {resource_name}

## Status

Current state: {backend_metadata_state}
```

To configure this template:

1. Go to your offering's page
2. Select "Edit" from the top menu
3. Scroll down and find the "Getting started instructions" and click the "Edit" button
4. Enter your desired template information using the variables above
5. Save the changes

The template will be rendered with retreived values when users access their resources.

## Service offering configuration guide

### Overview

This guide provides a structured approach for integrators to define an Offering. Offerings represent services, resources, or products made available through the platform.

### General information

The General Information section defines the core attributes of an offering, including its identity, accessibility, and governance policies.

#### Required fields

- **Name** – The title of the offering, displayed across the platform
- **Description** – A concise summary outlining the offering's purpose (limited to 4,096 characters — see [Description length limit](#description-length-limit))
- **Full description** – A detailed explanation, including technical aspects and potential use cases (no length limit)
- **Terms of service** – Any contractual obligations or usage restrictions
- **Privacy policy link** – URL linking to the privacy policy
- **Terms of service link** – URL linking to the terms of service
- **Access URL** – The main entry point for users to access the offering
- **Slug** – A unique identifier used in URLs (readonly)
- **Location** – The geographical or virtual location of the offering
- **Access policies** – Defines access control rules and user eligibility
- **Logo** – A graphical representation of the offering
- **Getting started instructions** – Guidelines on how users can begin using the offering

### Public information

The Public Information section ensures visibility and accessibility for end users. It includes Endpoints, Categories, and Images.

#### Endpoints

Endpoints provide connectivity to the offering's services. Each endpoint requires:

- **Name** – A human-readable identifier for the endpoint
- **URL** – The direct link to access the service

#### Images

Images provide visual representation and marketing appeal. Each image requires:

- **Name** – A descriptive title
- **Description** – A brief explanation of the image content
- **Attached image file** – The image file itself

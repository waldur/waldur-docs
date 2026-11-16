---
type: reference
requires:
  - setting:MCP_ENABLED
---

# MCP tools

An AI client connected to Waldur's MCP server can call the tools on this page. To connect
one, see [Connect AI clients over MCP](mcp-clients.md).

Every tool only reads. None of them changes anything in Waldur. A tool sees what you
see in the portal, with your roles in organizations and projects. Your client lists each
tool with its full input and output schemas, so this page only summarizes them.

## Which tools your client lists

Your client may list fewer tools than this page:

- `get_user_overview` is listed only for staff and support users.
- With a personal access token, a tool is listed only if the token holds the
  permissions the same REST call needs. `get_user_overview` needs `SUPPORT.ACCESS`
  or `STAFF.ACCESS`. Every other tool works with any token the server accepts.
- `chart_costs` is not listed when the portal hides prices.
- `search_docs` is not listed when documentation search is turned off, or when no
  documentation is loaded.

## How tools match names and limit results

- An input ending in `_uuid`, or named `uuid`, matches exactly.
- An input ending in `_name`, or named `search`, matches part of the name, ignoring case,
  unless its description says the name must be exact. When a name matches several
  projects or resources, `get_project` and `get_resource` return them in `matches`, so
  your client can ask you which one you mean.
- Most lists return at most 15 items. When more match, `_truncated` is true and
  `_total_count` gives the number. Narrow the request with more inputs to see the rest.
- A result has a one-line summary, the data as JSON text, and the same data as
  structured content that follows the tool's output schema.

## Organizations and projects

### `list_organizations`

Lists the organizations you have access to.

| Input | Type | Description |
|-------|------|-------------|
| `search` | string | Part of the name or abbreviation. |
| `uuid` | string | One organization's UUID. |

**Returns** `organizations`, each with its UUID, name, abbreviation and your role, and
`total`.

### `list_projects`

Lists the projects you have access to.

| Input | Type | Description |
|-------|------|-------------|
| `organization_uuid` | string | Only this organization's projects. |
| `organization_name` | string | The organization's name, when its UUID is not known. |
| `search` | string | Part of the project name. |
| `uuid` | string | One project's UUID. |

**Returns** `projects`, each with its UUID, name, organization and your role, and `total`.

### `get_project`

Shows one project: its organization, dates, and team members with their roles.

| Input | Type | Description |
|-------|------|-------------|
| `project_uuid` | string | The project's UUID. |
| `project_name` | string | The project's name, when its UUID is not known. |

**Returns** `project`, `organization` and `team`. When you may not see the project's
team, `team` is null and `restricted_fields` lists `team`: the team is hidden from you,
which doesn't mean it has no members.

### `get_project_quota`

Shows a project's quota limits and current usage.

| Input | Type | Description |
|-------|------|-------------|
| `project_uuid` | string | The project's UUID. |
| `project_name` | string | The project's name, when its UUID is not known. |

**Returns** `project` and `quotas`, each with its name, limit and usage.

## Resources

### `get_project_resources`

Lists resources with their state, offering and backend ID. Terminated resources are left
out.

| Input | Type | Description |
|-------|------|-------------|
| `project_uuid` | string | Only this project's resources. |
| `project_name` | string | The project's name, when its UUID is not known. |
| `search` | string | Part of the resource name or backend ID. |
| `uuid` | string | One resource's UUID. |

**Returns** `resources`, each with its UUID, name, state, offering, category, project,
backend ID, plan and creation date, and `total`.

### `get_resource`

Shows one resource: its state, offering, plan, limits, project, last error message and
recent events.

| Input | Type | Description |
|-------|------|-------------|
| `resource_uuid` | string | The resource's UUID. |
| `resource_name` | string | The resource's name, when its UUID is not known. Terminated resources are skipped. |
| `project_name` | string | Narrows a `resource_name` search to one project. |

**Returns** `resource`, `offering`, `plan`, `project`, `organization` and
`recent_events`.

### `get_resource_usage`

Shows a resource's usage of each component, such as CPU hours or storage, in the current
billing period.

| Input | Type | Description |
|-------|------|-------------|
| `resource_uuid` | string | The resource's UUID. |
| `resource_name` | string | The resource's name, when its UUID is not known. |

**Returns** `resource`, `components` and the billing `period`. When you may not see the
usage, `components` is null and `restricted_fields` lists `components`.

### `explain_resource_paused_reason`

Explains why a resource is paused: a cost policy, SLURM usage over its grace limit, the
project's grace period, or a manual pause. It also says when the resource is not paused,
and when its project has ended although the resource is not paused.

| Input | Type | Description |
|-------|------|-------------|
| `resource_uuid` | string | The resource's UUID. |
| `resource_name` | string | The resource's name, when its UUID is not known. |
| `project_name` | string | Tells resources with the same name apart. |

**Returns** `resource`, `project` with its end date and grace period, `primary_cause`,
and the numbers behind it in `attribution` and `policy_details`.

## Orders

### `list_orders`

Lists marketplace orders to create, update or terminate resources.

| Input | Type | Description |
|-------|------|-------------|
| `project_uuid` | string | Only orders in this project. |
| `project_name` | string | The project's name, when its UUID is not known. |
| `resource_uuid` | string | Only orders for this resource. |
| `customer_uuid` | string | Only orders placed by this organization. |
| `customer_name` | string | The organization's name, when its UUID is not known. |
| `offering_uuid` | string | Only orders for this offering. |
| `offering_name` | string | The offering's name, when its UUID is not known. |
| `state` | array of strings | Only orders in these states: `pending-consumer`, `pending-provider`, `pending-project`, `pending-start-date`, `executing`, `done`, `erred`, `canceled` or `rejected`. `pending` stands for every `pending-*` state. |

**Returns** `orders`, each with its UUID, type, state, offering, resource, project,
organization, cost, creator, creation date and error message, and `total`.

### `get_order`

Shows one order: its state, error message, who created and reviewed it, and when.

| Input | Type | Description |
|-------|------|-------------|
| `order_uuid` | string | Required. The order's UUID. |

**Returns** `order`, `created_by`, `consumer_reviewed_by`, `provider_reviewed_by`,
`offering`, `plan`, `resource`, `project` and `organization`.

## Costs, invoices and credit

### `chart_costs`

Shows an organization's or a project's monthly costs: the cost incurred, the credit and
compensation applied, and the net cost. The last month is the current one, as an
estimate.

| Input | Type | Description |
|-------|------|-------------|
| `customer_uuid` | string | The organization's UUID. |
| `customer_name` | string | The organization's name, when its UUID is not known. |
| `project_uuid` | string | The project's UUID. |
| `project_name` | string | The project's name, when its UUID is not known. |
| `months` | integer | How many months, from 1 to 24. Default 12. |

With both an organization and a project, the organization only narrows which project is
meant.

**Returns** the organization or project, `currency`, `months` with the costs of each
month, and `total_price`.

### `list_invoices`

Lists monthly invoices with their state and totals.

| Input | Type | Description |
|-------|------|-------------|
| `customer_uuid` | string | Only this organization's invoices. |
| `customer_name` | string | The organization's name, when its UUID is not known. |
| `year` | integer | Only invoices for this year. |
| `month` | integer | Only invoices for this month, from 1 to 12. |
| `state` | array of strings | Only invoices in these states: `pending`, `pending_finalization`, `created`, `paid` or `canceled`. `created` means issued and not paid. |

**Returns** `invoices`, each with its UUID, number, organization, year, month, state,
price, tax, total, invoice date and due date, and `total`.

### `explain_invoice_compensations`

Explains the credit compensations and manual adjustments on a project's invoice, and
counts terminated resources that still added to it.

| Input | Type | Description |
|-------|------|-------------|
| `project_uuid` | string | The project's UUID. |
| `project_name` | string | The project's name, when its UUID is not known. |
| `year` | integer | The invoice's year. Default: the latest invoice. |
| `month` | integer | The invoice's month. Default: the latest invoice. |

**Returns** `project`, `invoice_summary`, `per_resource` with each resource's gross cost,
compensation and net cost, `manual_adjustments` and `concealed_resource_count`.

### `explain_project_credit_balance`

Explains a project's credit: how much was allocated, how much has been spent this month
and in total, and whether the project is overdrawn. It also shows the organization's
credit.

| Input | Type | Description |
|-------|------|-------------|
| `project_uuid` | string | The project's UUID. |
| `project_name` | string | The project's name, when its UUID is not known. |

**Returns** `project`, `customer`, `project_credit` and `customer_credit`.

### `get_customer_credit_overview`

Shows an organization's credit, and each of its projects' credit, spending, balance and
whether it is overdrawn.

| Input | Type | Description |
|-------|------|-------------|
| `customer_uuid` | string | The organization's UUID. |
| `customer_name` | string | The organization's name, when its UUID is not known. |

**Returns** `customer`, `customer_credit`, `projects` and `overdrawn_count`. When the
project list is cut short, `_total_project_count` gives the number of projects.

### `list_overdrawn_projects`

Lists projects that have spent more than their credit.

| Input | Type | Description |
|-------|------|-------------|
| `customer_name` | string | Only this organization's projects. Without it, all the projects you can see. |

**Returns** `overdrawn_projects`, each with its project, organization, credit, spending
to date and the amount it is over by.

## Marketplace

These tools cover the offerings you could order in the portal. For staff and support
users, that is every active or paused offering.

### `list_categories`

Lists the marketplace categories that hold at least one offering you could order. It
takes no inputs, and returns every such category.

**Returns** `categories`, each with its UUID, title and number of offerings.

### `search_offerings`

Searches the marketplace offerings by keyword.

| Input | Type | Description |
|-------|------|-------------|
| `keyword` | string | Required. One word or term, matched against names, descriptions, categories, tags, plans and components. |
| `category_uuid` | string | Only offerings in this category. |
| `category_name` | string | The category's exact title, when its UUID is not known. |
| `type` | string | Only offerings of this type, such as `OpenStack.Tenant`. |
| `limit` | integer | How many offerings to return, up to 15. |

**Returns** `offerings`, each with its name, UUID, category, provider, country,
description, starting price and portal link, and `total`. `has_access_url` marks the
offerings that also publish a direct access link.

### `get_offering`

Shows one offering, with its plans, components, attributes and links.

| Input | Type | Description |
|-------|------|-------------|
| `uuid` | string | The offering's UUID. |
| `name` | string | The offering's exact name, when its UUID is not known. |

**Returns** `offering`, with its description, plans, components, attributes, tags, access
URL, getting-started text, documentation, helpdesk and privacy policy links, and portal
link.

### `compare_offerings`

Compares two or more offerings by provider, category, description and starting price.

| Input | Type | Description |
|-------|------|-------------|
| `uuids` | array of strings | The offerings' UUIDs. |
| `names` | array of strings | The offerings' exact names, when their UUIDs are not known. |

**Returns** `offerings`, and in `missing` the ones it did not find.

## Documentation

### `search_docs`

Searches the Waldur user and administrator documentation, which is this site.

| Input | Type | Description |
|-------|------|-------------|
| `query` | string | Required. English keywords for the feature or task, up to 300 characters. |

**Returns** `sections`, each with its title, breadcrumb, excerpt, link and whether the
feature it describes is on in your portal, and in `switched_off_here` the features that
are off.

## Support

### `get_user_overview`

Shows another user's organizations and projects with their roles, resource counts,
pending orders and recent errors. Only staff and support users get this tool.

| Input | Type | Description |
|-------|------|-------------|
| `user_email` | string | Required. The user's email address. |

**Returns** `user`, `organizations`, `projects`, `resources`, `pending_orders` and
`recent_errors`.

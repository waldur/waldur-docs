# API keys of your offerings

Offerings such as inference gateways and S3 storage give each resource one or
more **API keys**. A consumer manages the keys of their own resource on its
**API keys** tab (see [Resource API keys](../customer-organization/resource-api-keys.md)).
As a service provider you can see the keys of every resource of all your
offerings in one list, for example to find which key is spending the most this
month.

The list is read-only. You never see a key's value, and pausing, resuming,
rotating or deleting a key stays with the consuming project or organization.

## Opening the list

Open your organization, switch to the **Service provider** view, and choose
**Resources** → **API keys**.

You see the keys of the resources the service provider's **Resources** list
shows you: with a role in the service provider organization you see the keys of
all its offerings, and as a manager of an offering you see that offering's
keys. Deleted keys are left out unless you filter by the **Deleted** state.

## What each row shows

- **Key ID** — the identifier the backend knows the key by.
- **Resource** — the resource the key belongs to. Click it to open the
  resource on its **API keys** tab, which shows the key's limits, models and
  history.
- **Offering**, **Client organization** and **Project** — where the key is
  used.
- **Assignee** — the person the key belongs to, or a dash for a key shared by
  the project.
- **State** — **OK**, **Paused**, **Paused at limit**, **Erred**, or a
  transitional state while the site agent carries out a change.
- **Usage this month** — the key's usage per component, against its monthly
  limit where it has one.
- **Estimated cost** — what the key's usage this month costs at the unit prices
  of the resource's plan.
- **Paused by limit** — whether Waldur paused the key because its usage reached
  one of its limits.

The keys are sorted by estimated cost, highest first. Click a column header to
sort by state instead.

Above the list, a summary counts the keys that match your filters, how many of
them a limit has paused, and how many are erred, and adds up their estimated
cost this month.

## Filtering

Use the filter button to narrow the list by offering, client organization,
project, state, paused by limit, or assignee. The summary follows the filters.
You can also filter by a row's offering, organization, project or assignee from
the filter icon in its cell.

As an offering manager you pick organizations, projects and assignees from the
keys on the current page, since you may not list all of the provider's
customers.

## Estimated cost

Offerings measure different things — tokens, a cost in currency, storage — so
raw usage cannot tell you which key spends the most across offerings. The
estimated cost can: it is each component's usage this month multiplied by that
component's price in the resource's plan.

It is an estimate, not an invoice amount:

- discounts, credits and carried-over usage are not applied;
- a component the plan does not price counts as zero;
- it is updated whenever the site agent reports the key's usage, so a plan
  price change shows from the key's next report;
- a key reads zero until its first usage report of the month.

The summary's total also counts keys deleted this month, since their usage up
to the deletion still happened.

## Key counts on the resource list

The **Resources** list of your service provider view has an optional
**API keys** column. Turn it on from the column settings. It shows how many
keys each resource has and how many of them are paused or erred, for example
`4 · 1 paused`. Click the figure to open the API keys list for that resource.

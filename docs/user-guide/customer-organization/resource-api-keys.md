# Resource API keys

Some resources — inference services and other API gateways — are reached with an
**API key**. Waldur lists a resource's keys on its **API keys** tab. There you
can reveal and rotate a key, and, where the provider supports it, request new
keys, hand a key to one person, cap how much it may use, restrict it to some
models, and pause or delete it.

Waldur never generates key material itself. Every change is sent to the
provider's site agent, which carries it out on the backend and reports back. A
key therefore shows a transitional state (**Creating**, **Rotating**,
**Pausing**, **Resuming**, **Updating**, **Deleting**) until the agent confirms the change.

## The API keys tab

Open the resource and select the **API keys** tab.

![API keys tab of a resource](../img/resource-api-keys-tab.png)

Each row is one key:

- **Key ID** — the identifier the backend knows the key by.
- **Assignee** — the person the key belongs to, or a dash for a key shared by
  the project.
- **Limits & usage** — how much of a limit the key has used, for the limit
  closest to being reached, of any component and period.
- **Models** — the models the key may call, or **All models**.
- **State** — **OK**, **Paused**, **Paused at limit**, **Erred**, or a
  transitional state while a change is in progress.
- **Issued** — when the current key value was created or last rotated.

Expand a row to see every component: its usage this month, and each of the
key's limits on a shorter or longer period, such as **Token cost · Daily
limit**. A limit marked *(inherited)* is the resource's own limit: the key has
no monthly limit of its own for that component.

![A key's usage per component](../img/resource-api-keys-row-details.png)

The **Actions** menu at the end of each row offers what the key's state allows.

![Actions available on an active key](../img/resource-api-keys-actions.png)

## Revealing a key

Choose **Reveal** to see the key value. The value is masked until you click the
eye icon, and the copy button puts it on the clipboard.

![Revealing an API key](../img/resource-api-keys-reveal.png)

Any member of the resource's project can reveal a shared key. A key with an
**assignee** can be revealed only by that person (and by staff and support).

!!! tip
    If a key may have been exposed, use **Rotate**. The backend issues a new
    value and the old one stops working. Anything using the key needs the new
    value afterwards.

## Requesting a key

Project managers and organization owners can request additional keys with
**Request key**:

1. Optionally choose an **Assignee** — only project members are offered. Leave
   it empty for a key shared by the project.
2. Optionally set **limits** per component and period (see [Limits](#limits)).
   Leave a field empty for no limit on that period.
3. Optionally tick the **Models** the key may call. Leave all unticked to allow
   every model.
4. Click **Submit**.

![Requesting an API key](../img/resource-api-keys-request.png)

The new key appears as **Creating** and turns **OK** once the provider has
created it. Its key ID is assigned at that point.

![A requested key waiting to be created](../img/resource-api-keys-requested.png)

## Changing a key's assignee, limits and models

Choose **Edit key settings**. **Save** stays disabled until you change
something.

![Editing a key's settings](../img/resource-api-keys-edit.png)

- The **assignee** can be changed at any time, except while the key is being
  deleted.
- **Limits** and **models** can be changed while the key is **OK** or
  **Paused**. On an active key the change is sent to the provider and the key
  shows **Updating** until it is applied. On a paused key the change is stored
  and applied when the key is resumed.

## Limits

A key can have a limit per component for each **period** the provider offers:
daily, weekly, monthly, quarterly or yearly. A research group that puts a
monthly budget into a resource can, for example, give each member's key a daily
and a monthly limit, so one person's run cannot spend the group's month on a
Tuesday.

- **Monthly** is available on every component. The other periods are available
  where the provider lets customers set spending limits on the component for
  its resources.
- Periods are calendar periods in UTC: a day resets at 00:00 UTC, a week on
  Monday, a month on the 1st, a quarter on 1 January, April, July and October,
  and a year on 1 January. The reset time is shown next to each field.
- A key's limit may not exceed the resource's own spending limit for the same
  period ("Up to …" under the field), and a shorter period's limit may not
  exceed a longer one's: daily ≤ weekly ≤ monthly ≤ quarterly ≤ yearly.
- A limit must be above **0**. To stop a key, pause it.

Limits are enforced by Waldur:

- When a key's usage in a period reaches its limit for that period, Waldur
  pauses that key only. The resource and its other keys keep working. The key
  shows **Paused at limit**; hover over it to see which limit stopped it and
  when it resumes.
- A key paused at its limit is resumed automatically once it is under its
  limits again — within a few minutes of the reset of the limit that stopped it,
  or when you raise or remove that limit.
- If you resume such a key by hand while it is still over its limit, it is
  paused again on the next usage report.

!!! note
    Usage is reported by the provider periodically, so a key can go somewhat
    over its limit before it is paused. Daily, weekly, quarterly and yearly
    limits need the provider to report each key's usage per day. With a
    provider that reports only monthly totals, monthly limits are enforced in
    full, and a quarterly or yearly limit counts only the current month.

## Pausing, resuming and deleting

- **Pause** stops the backend accepting the key. The key keeps its value, and
  **Resume** brings it back.
- **Delete** revokes the key at the backend. A deleted key disappears from the
  list, but the usage it reported still counts towards the resource.
- A requested key that has not been created yet can be withdrawn with
  **Delete**. It is removed at once, without waiting for the provider.

![Withdrawing a key request](../img/resource-api-keys-withdraw.png)

## When a change fails

If the provider cannot carry out a change, the key shows **Erred** and the row
keeps the error message. An erred key offers **Retry**, which repeats the failed
change, and **Delete**. A key whose settings update failed can also be corrected
with **Edit key settings**, which sends the update again.

## For service providers

Two options in the offering's **Integration → Resource display options**
control the tab:

![Offering options for API keys](../img/resource-api-keys-offering-options.png)

- **Manage API keys one by one** turns on everything above apart from
  revealing, rotating and resuming: requesting keys, assignees, limits, model
  restrictions, pausing and deleting. It is available on site-agent offerings.
  Turn it on only if the backend behind the site agent supports per-key
  management, such as the Envoy AI Gateway. Other backends, such as Ceph S3,
  fail those actions.
- **Hide API keys tab** removes the tab from the offering's resources.

The models offered in the key dialogs are the choices of the offering's
`models` resource option, narrowed to the resource's own selection when it has
one. Without that option, the key dialogs show no model list.

!!! warning
    Without **Manage API keys one by one**, consumers can only reveal and rotate
    keys, and resume keys that were paused earlier. Per-key usage is not
    recorded, so limits are no longer enforced, but a key keeps its assignee:
    only that person can still reveal it. Project managers and organization
    owners can share such a key with the project again with **Unassign**.

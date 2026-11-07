# Enabling call management

Before an organisation can run calls, staff turn call management on for it, and its owner
appoints the people who create calls. This page covers that one-off setup and the optional
limit on how many proposals one applicant may hold with the organisation.

## Setting up the organisation

**Performed by:** Organization owner

1. **Verify organization type**:
      - Confirm your organization is registered as a **Call managing organization**
      - If not, contact your Waldur administrator: staff turn it on with **Manages calls** under the organization's **Edit → Call manager** tab

2. **Decide on a per-applicant limit** (optional):
      - The same **Call manager** tab holds **Active proposals per applicant** — see [Limiting proposals per applicant](#limiting-proposals-per-applicant)

3. **Review available offerings**:
      - Check that there are **marketplace offerings** available to be requested in calls
      - These offerings will form the resource pool available for allocation

4. **Assign Call organisers**:
      - Open the organization's **Call management** tab and go to **Team** — the tab
        appears only once staff have turned call management on
      - Click on the **Add member** button
      - Search for users to assign as Call organisers
      - Select the **Organization call organizer** role
      - Click **Add** to confirm the assignment

Once the organisation manages calls, its **Call management** tab has the sections
**Dashboard**, **Calls**, **Proposals**, **Reviews**, **Reports** and **Team** (see
[Dashboards and reports](dashboards-and-reports.md)). An owner without a call role lands on
**Calls** and does not see **Dashboard** or **Reports**. On deployments that run their calls
outside Waldur (the `marketplace.call_only` feature), **Proposals**, **Reviews** and **Reports**
are not shown.
Continue with [Creating and configuring a call](creating-a-call.md).

## Limiting proposals per applicant

**Set by:** Staff, on the organization's **Edit → Call manager** tab

**Active proposals per applicant** caps how many proposals one applicant may
hold with the organization at a time, across **all** of its calls. Leave it
empty for no limit (the default).

A proposal holds a place:

- while it is **Submitted** or **In review**, and
- once **Accepted**, for as long as its project runs — until the project is
  completed, removed or past its end date.

Drafts, rejected and cancelled proposals hold none, and an accepted proposal
and its project count as one place, not two. Only the proposal's **creator**
is counted: being a member or co-manager of someone else's proposal team takes
no place.

The limit is checked when a proposal is created and again when it is
submitted, where it holds: a draft takes no place until it is submitted, so an
applicant at the limit cannot submit another one. They are refused with
*You have reached the maximum of N active projects or pending proposals. You
cannot submit another proposal until one of them is completed or closed.*

Once a limit is set, every call of the organization counts as restricting who
may apply (see
[When eligibility is checked](application-form.md#when-eligibility-is-checked)), and an applicant
at the limit sees **Apply to call** disabled with *You are not eligible to
apply to this call.* State the limit in the call descriptions.

What applicants see of the limit is described in the
[Applicant guide](applicant-guide.md#how-many-proposals-you-may-have-at-once).

# Call manager's roadmap

This page walks through the lifecycle of a call from setup to final resource allocation, one
step at a time, and points to the page that covers each step. It ends with troubleshooting and
frequently asked questions. For what calls, rounds and proposals are, see the
[overview](overview.md).

## Detailed process guide

## Step 1: Organization setup

**Performed by:** Organization owner (with staff)

Staff turn call management on for the organisation, optionally set a limit on proposals per
applicant, and the owner appoints call organisers. See
[Enabling call management](organization-setup.md).

### Limiting proposals per applicant

See [Limiting proposals per applicant](organization-setup.md#limiting-proposals-per-applicant).

## Step 2: Call creation

**Performed by:** Call organiser (or staff)

Create the call, blank or from a template, and assign its call managers. See
[Creating and configuring a call](creating-a-call.md).

### Starting from a call template

See [Starting from a call template](creating-a-call.md#starting-from-a-call-template) and the
[Extreme Scale call template](extreme-scale-template.md).

## Step 3: Configure call rounds

**Performed by:** Call manager

Add at least one round with its dates. See [Rounds](call-rounds.md).

### Drafts at the cut-off

See [Drafts at the cut-off](call-rounds.md#drafts-at-the-cut-off).

### When evaluation starts

See [When evaluation starts](call-rounds.md#when-evaluation-starts).

## Step 4: Call configuration and activation

**Performed by:** Call manager

Configure the call on its **Edit** page, then check and activate it:

1. **General settings and configuration** — [Creating and configuring a call](creating-a-call.md#general-configuration)
2. **Application form** — project details fields, applicant eligibility and resource templates: [Application form](application-form.md)
3. **Offerings, role mapping and team** — [Resources, role mapping and team](call-resources-and-team.md)
4. **Workflow steps and evaluator roles** — [Workflow configuration](workflow-configuration.md)
5. **COI settings** — [Conflict of interest management](coi-management.md#configuring-coi-detection)
6. **Matching settings** — [Reviewer management](reviewer-management.md#configuring-matching)
7. **Proposal IDs** — [Proposal ID configuration](proposal-id-configuration.md)
8. **Workflow check and activation** — [Checking and activating a call](call-activation.md)

### How long a granted project runs

See [How long a granted project runs](allocation-decision.md#how-long-a-granted-project-runs).

### Project details fields

See [Project details fields](application-form.md#project-details-fields).

### Applicant eligibility

See [Applicant eligibility](application-form.md#applicant-eligibility) and
[When eligibility is checked](application-form.md#when-eligibility-is-checked).

### Resource templates

See [Resource templates](application-form.md#resource-templates).

### Call activation process

See [Call activation process](call-activation.md#call-activation-process).

### Checking the workflow before activation

See [Checking the workflow before activation](call-activation.md#checking-the-workflow-before-activation).

## Step 5: Submit proposal

**Performed by:** Applicant

Applicants find the active call, create a proposal, fill it in and submit it. See the
[Applicant guide](applicant-guide.md).

## Step 6: Review assignment and process

**Performed by:** Call manager, reviewers and evaluators

1. Build the reviewer pool, generate matches and send assignment batches —
   [Reviewer management](reviewer-management.md).
2. Triage conflicts of interest — [Conflict of interest management](coi-management.md).
3. Drive each proposal through the workflow steps —
   [Running the evaluation](call-manager-workflow.md); committee work on a whole round —
   [Round steps and rankings](round-rankings.md).
4. Reviewers review and score — [Reviewing proposals](reviewer-workflow.md).

### Requesting changes from the applicant

See [Requests for changes and withdrawals](requests-for-changes.md#requesting-changes-from-the-applicant).

### Withdrawn proposals

See [Withdrawn proposals](requests-for-changes.md#withdrawn-proposals).

## Step 7: Decision and allocation

**Performed by:** The responsible role of the **Allocation decision** step (Call manager by default)

Complete the allocation decision for each proposal, adjusting the awarded resources where
needed — [Allocation decision and award](allocation-decision.md). Publish and complete each
round — [Publishing a round's results](round-results.md).

### Round lifecycle after the cut-off

See [Round lifecycle after the cut-off](round-results.md#round-lifecycle-after-the-cut-off).

### Publishing a round's results

See [Publishing a round's results](round-results.md#publishing-a-rounds-results).

### Completing a round

See [Completing a round](round-results.md#completing-a-round).

### Recording adoption

See [Recording adoption](round-results.md#recording-adoption).

## Step 8: Monitoring and reporting

**Performed by:** Call manager and Call organiser

Follow the calls on their dashboards and reports — [Dashboards and reports](dashboards-and-reports.md)
— and export what you need — [Data export](data-export.md).

## Additional tips

- Always check round and call status before making edits.
- Assign enough reviewers early to avoid bottlenecks.
- Communicate with applicants when revisions are needed.
- Keep documentation clear and up to date.

## Troubleshooting

Solutions for common issues encountered during the call management process:

| Issue | Possible Cause | Solution |
| --- | --- | --- |
| Unable to create call | Insufficient permissions | Verify user has Call Organiser role |
| **Activate** is disabled | The call has no round, no enabled workflow step, not exactly one enabled allocation decision, or no accepted offering — or you lack the right to edit the call | Hover over **Activate** for the reason and fix it |
| Offering request pending | Service provider hasn't responded | Contact provider directly or through system notification |
| Reviewer cannot access proposal | Incorrect assignment | Verify the assignment on the call's **Manage → Reviews** and **Reviewer pool** tabs |
| Applicant cannot see or apply to a call | The call is not active, or none of its rounds is open | A call is public only while it is **Active**, and **Apply** needs an open round |
| Resource allocation failed | Insufficient provider capacity | Contact service provider to resolve capacity issue |
| Round cannot be deleted | The round has proposals, in any state | Rounds with proposals stay on record; only an empty round can be deleted (see [Configuring rounds](call-rounds.md#configuring-rounds)) |
| **Activate** is refused or shows a number of errors | The workflow check found errors | Open the call's **Validation → Check** tab and fix each error from its link (see [Checking the workflow before activation](call-activation.md#checking-the-workflow-before-activation)) |
| Applicant refused with *You have reached the maximum of N active projects or pending proposals* | The call-managing organization limits proposals per applicant | The applicant waits until a proposal is decided or a project ends, or staff raise **Active proposals per applicant** (see [Limiting proposals per applicant](organization-setup.md#limiting-proposals-per-applicant)) |
| **Applicants learn the decision** cannot be changed | The call holds decisions that have not been published | Publish the results of the rounds that hold them first |
| **Complete round** is refused | Proposals of the round have no decision, or a held decision failed to publish | Decide them (or set the round's rule to reject them), or publish the results again (see [Completing a round](round-results.md#completing-a-round)) |

## FAQ

**Q: What's the difference between a Call Organiser and a Call Manager?**
A: A Call Organiser is appointed by the Organization Owner to create calls and assign Call Managers. The Call Manager is responsible for the detailed configuration of calls assigned to them including setting up rounds, assigning reviewers, and managing the review process.

**Q: Can a call have multiple rounds running simultaneously?**
A: No. A call can have several rounds, but their submission periods may not overlap.

**Q: What happens if insufficient reviewers complete their evaluations?**
A: **Minimum contributions** on an assessment step (**Minimum reviewers** on a decision) is a completion gate: the step cannot be completed with a positive outcome until that many reviews have been submitted, though declining the proposal is always possible. If the step has a duration and its deadline passes first, the step is marked **Overdue** and the workflow moves on to the next step, or rejects the proposal if it was the last one (see [Deadline handling](workflow-configuration.md#deadline-handling)). To avoid this, assign further reviewers in time, or leave the step's duration unset so it waits.

**Q: Can applicants edit their proposals after submission?**
A: Not on their own. Once a proposal is submitted its requested resources and documents are fixed: what was submitted is what gets evaluated. The exception is a [request for changes](requests-for-changes.md#requesting-changes-from-the-applicant): on a step that allows it, whoever acts on the step can unlock chosen parts for the applicant to change and submit again. Call managers and staff can still adjust a proposal at any time. A draft left open at its round's cut-off is the exception only in that it survives into the next round (see [Drafts at the cut-off](call-rounds.md#drafts-at-the-cut-off)); it is still a draft until the applicant submits it.

**Q: Is it possible to transfer allocated resources between approved projects?**
A: Resource transfer between projects requires administrative approval. Contact your Call manager to request a resource transfer.

**Q: How are applicants notified about proposal decisions?**
A: Waldur automatically sends email notifications to all team members listed in a proposal when a decision (approval or rejection) is announced — when it is made, or, on a call that publishes results together for the whole round, when the round's results are published.

**Q: Can a Call manager override reviewer scores?**
A: Decisions are always made by a person completing a workflow step; scores never decide on their own. A step can be declined regardless of scores, but approving is blocked while a **Minimum contributions**, **Minimum reviewers** or **Minimum score threshold** set on that step is not met. All reviewer feedback remains visible and documented.

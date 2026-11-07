# Calls for proposals overview

A **call for proposals** is how a call-managing organisation hands out resources through
an application and evaluation process instead of direct orders. Applicants write a
**proposal** asking for resources from the offerings the call grants access to; the proposal
is evaluated through the call's workflow; and an accepted proposal becomes a project with the
awarded resources. For the concepts behind the module — calls, rounds, proposals and reviews,
and who triggers which part of the process — see the
[Call management concept page](../../about/concepts/call-management.md).

This section is organised by the job you are doing:

| You want to… | Start with |
|---|---|
| Understand calls, roles and lifecycles | this page |
| Set up and open a call | [Call manager's roadmap](call_management.md) |
| Run the evaluation of submitted proposals | [Workflow configuration](workflow-configuration.md) and [Running the evaluation](call-manager-workflow.md) |
| Decide and award | [Allocation decision and award](allocation-decision.md) |
| Follow progress and export data | [Dashboards and reports](dashboards-and-reports.md) and [Data export](data-export.md) |
| Apply for resources | [Applicant guide](applicant-guide.md) |
| Review or evaluate proposals | [Reviewer profile and invitations](reviewer-guide.md) and [Reviewing proposals](reviewer-workflow.md) |
| Operate calls on a deployment | [Calls on your deployment](operator-settings.md) |

## Calls, rounds and proposals

- A **call** belongs to a call-managing organisation. It names the offerings it grants
  access to, what it asks of applicants, and its **evaluation workflow** — the ordered steps
  every submitted proposal walks, ending in one allocation decision. A call can start blank or
  from a call template that carries a complete process.
- A call has one or more **rounds**. A round schedules submission (a start and a cutoff date),
  review and allocation.
- A **proposal** is submitted to one round of a call by an applicant and their proposal team.
  It holds the project details, the resource requests and, when the call has one, the answers
  to its compliance checklist.
- When a proposal is accepted, Waldur creates a **project** under the call-managing
  organisation, provisions the awarded resources in it and adds the proposal's team with the
  project roles the call maps their proposal roles to.

## Roles

Role definitions and the permission matrix are on
[Roles and permissions](../../about/terminology/roles_and_permissions.md#user-roles-in-call-management).
In the course of a call you will meet:

| Role | Part in the process |
|---|---|
| **Organisation owner** | Owns the call-managing organisation and appoints call organisers |
| **Call organiser** | Creates calls in the organisation and oversees all of them |
| **Call manager** | Configures and runs the calls they are assigned to, drives proposals through the workflow and records the decisions |
| **Panel member**, **Chair**, **Vice-chair** | Members of the call's panel; steps can be completed by them or by the chair or vice-chair |
| **Reviewer** | Member of the call's reviewer pool who reviews the proposals assigned to them |
| **Evaluator role holder** | Holds a role on one proposal, such as rapporteur, defined per call |
| **Offering manager** | Service provider team that accepts the call's offering requests and, on calls that ask for it, assesses each requested offering |
| **Applicant** | Creates and submits a proposal; the proposal's managers (principal investigators) act for its team |
| **Staff** | Enables call management for an organisation, manages call templates and checklists, and can act anywhere |

## Lifecycle of a call

1. **Draft** — the call is created, blank or from a template, and configured: rounds,
   application form, offerings, workflow, team. Nobody can apply yet.
2. **Active** — once the workflow check finds no errors, a call manager activates it and it
   appears in the call catalogue. Applicants submit proposals to its open rounds.
3. **Archived** — the call's workflow steps become read-only.

The calls list groups calls by these states (All / Active / Draft / Archived). See
[Creating and configuring a call](creating-a-call.md) and
[Checking and activating a call](call-activation.md).

Each **round** is **Scheduled** or **Open** before its cutoff, derived from its dates. After the
cutoff it moves through **Evaluating**, optionally **Deciding**, **Results published** and
**Closed** — see [Publishing a round's results](round-results.md).

## Lifecycle of a proposal

| State | Meaning |
|---|---|
| **Draft** | Being written; only the proposal team sees it |
| **Submitted** | Submitted and waiting for evaluation to start — on calls that evaluate at the round cut-off, until the cut-off has passed |
| **In review** | Walking the call's workflow steps — on calls that announce results together for the whole round, until the round's results are published |
| **Accepted** | Approved; a project and its resources have been (or are being) provisioned |
| **Rejected** | Not awarded |
| **Canceled** | Withdrawn, an award the applicant declined, or a draft cancelled at the cut-off |

Each proposal keeps the path of steps it was submitted with, even if the call is reconfigured
later. See [How proposals progress through the workflow](workflow-configuration.md#how-proposals-progress-through-the-workflow).

## Calls mode

How users reach services is a deployment-wide setting, `SERVICE_ACCESS_MODE`:

- `both` (the default) — users browse the marketplace or open calls;
- `calls` — users reach services **only through calls for proposals**. There is no marketplace
  navigation: an offering page is reached from **Calls for proposals → Available offerings**,
  offers applying only, and the marketplace shop itself is for staff only;
- `marketplace` — applicants reach a call through an offering's **Apply for access**, and see
  *access requests* instead of proposals.

Reviewers, call managers and service providers keep the call vocabulary in every mode. See
[How you reach services](../end-users/service-access-modes.md) for what users see, and
[Service access modes](../../admin-guide/mastermind-configuration/service-access-modes.md) for
the setting and the feature flags it combines with.

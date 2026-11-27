---
mentions:
  - feature:marketplace.show_call_management_functionality
---

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
| **Organisation owner** | Owns the call-managing organisation and appoints call organisers; does not create or configure calls without a call role |
| **Call organiser** | Creates calls in the organisation and oversees all of them |
| **Call manager** | Configures and runs the calls they are assigned to, drives proposals through the workflow and records the decisions |
| **Panel member**, **Chair**, **Vice-chair** | Members of the call's panel; steps can be completed by them or by the chair or vice-chair |
| **Reviewer** | Member of the call's reviewer pool who reviews the proposals assigned to them; the **Call reviewer** role can also be granted on the call's **Team** tab |
| **Evaluator role holder** | Holds a role on one proposal, such as rapporteur, defined per call |
| **Offering manager** | Service provider team that accepts the call's offering requests and, on calls that ask for it, assesses each requested offering |
| **Offering evaluator** | Member of an offering's team, without managing the offering, to whom offering managers hand their part of a step |
| **Applicant** | Creates and submits a proposal; the proposal's managers (principal investigators) act for its team |
| **Staff** | Enables call management for an organisation, manages call templates and checklists, and can act anywhere |

## Lifecycle of a call { data-requires="feature:marketplace.show_call_management_functionality" }

1. **Draft** — the call is created, blank or from a template, and configured: rounds,
   application form, offerings, workflow, team. Nobody can apply yet.
2. **Active** — once the workflow check finds no errors, a call manager, call organiser or
   staff activates it and it appears in the call catalogue. Applicants submit proposals to its
   open rounds.
3. **Archived** — the call's evaluation is closed: the call and its proposals' work up to the
   award become read-only, while the award stage goes on. Archiving a call whose proposals are
   still in evaluation asks for confirmation (**Archive anyway**), and those proposals stop where
   they are. An archived call can be activated again.

The calls list groups calls by these states (All / Active / Draft / Archived). See
[Creating and configuring a call](creating-a-call.md) and
[Checking and activating a call](call-activation.md).

### What archiving freezes

Archiving closes the call's evaluation and keeps it exactly as it was. For everyone, staff
included:

- **The call's configuration** — settings, offerings, resource templates, workflow steps, role
  mappings, rounds, documents and notification overrides cannot be changed.
- **Applications** — no proposal can be created or submitted.
- **The evaluation's workflow** — no evaluation step is completed, rejected or advanced, on one
  proposal or for a whole round, and no decision is reopened. Changes cannot be requested from
  applicants, nor submitted by them.
- **Reviews and contributions** — reviews cannot be submitted, sent back or removed; no reviewer
  is assigned, invited, suggested or bids, and assignments cannot be accepted, declined or
  reassigned; the evaluation's contributions and step checklists cannot be submitted, reopened,
  handed on, accepted or declined; evaluator roles cannot be confirmed and conflicts of interest
  are not resolved; offering teams answer no offering requests.
- **Rounds** — round reports cannot be written, submitted or reopened, notes and the ranking
  are not changed, no step is completed, opened or advanced for a round, and no step discussion
  is started.
- **The proposals themselves** — the team, project details, panel, requested resources and
  supporting documents cannot be changed, and a draft cannot be deleted or a proposal withdrawn.
- **The award** — what the allocation decision awards (its items and duration) cannot be edited.
- **Scheduled work of the evaluation** — its overdue steps do not expire, reviews, assignments,
  reviewer pool invitations and requests for changes do not lapse, ended rounds do not start
  their evaluation and held proposals stay held, its open discussions stay as they are, and no
  deadline reminders or digests are sent for it. The evaluation's work leaves everyone's
  **My tasks**. Only drafts are still cancelled once their round ends: never submitted, they no
  longer can be.

### What goes on

The award stage of the call's proposals continues as in an active call:

- the **award response** — the applicant accepts or declines the award;
- **provisioning** the awarded resources, and provisioning them again after a failure;
- **extensions** — the applicant requests one, its steps are assessed, contributed to, decided
  and lapse as usual, and its granted limits are edited;
- the **final report** — it opens at the end of the allocation, is submitted, contributed to and
  approved, and lapses as usual;
- withdrawing a run, the changes a run asks for, the step discussions of these steps, and the
  reminders, tasks and digests of all of the above.

A proposal whose award response leads on to a further evaluation step waits before it while the
call is archived, and enters it once the call is active again.

The pages show the frozen actions as disabled, with the reason in their tooltip; an attempt
through the API is refused with *The call is archived.* (HTTP 409).

Everything stays readable for those who could read it before: the call, its proposals, reviews
and contributions, the exports and the proposal PDF. Activating the call again lifts the freeze,
and the scheduled work picks up from where it stopped. A step whose last open contribution ended
while the call was archived — its holder's role revoked, say — is completed on activation with
the outcome the submitted contributions give, as completed by who submitted the last of them. An
hourly sweep picks up anything the activation itself did not.

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

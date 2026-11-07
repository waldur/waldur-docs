# Calls on your deployment

**Performed by:** Staff and deployment administrators

Most of a call is configured by its call managers. A few things are set for the whole
deployment, or only by staff. This page collects them, with links to where each is described.

## Calls mode

`SERVICE_ACCESS_MODE` decides how users reach services: `both` (the default), `calls` — users
reach services only through calls for proposals, with no marketplace navigation — or
`marketplace`, where applicants apply from an offering and see access requests. See
[Calls mode](overview.md#calls-mode) for a summary,
[Service access modes](../../admin-guide/mastermind-configuration/service-access-modes.md)
for the setting and the feature flags it combines with, and
[How you reach services](../end-users/service-access-modes.md) for what users see.

## Staff settings

| Setting | Where | Described in |
|---|---|---|
| **Manages calls** — turns call management on for an organisation | the organisation's **Edit → Call manager** tab | [Enabling call management](organization-setup.md) |
| **Active proposals per applicant** | the organisation's **Edit → Call manager** tab | [Limiting proposals per applicant](organization-setup.md#limiting-proposals-per-applicant) |
| Call templates — **Load preset**, publish | **Administration → Call templates** | [Starting from a call template](creating-a-call.md#starting-from-a-call-template) |
| Checklists and evaluation forms | **Administration → Compliance → Checklists** | [Managing checklists](checklists-and-forms.md#managing-checklists-administrators) |
| Force-accepting invitations and force-unblocking COI-blocked assignments (call managers can too) | the call's **Reviewer pool** | [Staff override capabilities](coi-management.md#staff-override-capabilities) |
| Reviews and proposals across all calls | the admin reviews and proposals pages | [Admin reviews and proposals](dashboards-and-reports.md#admin-reviews-and-proposals) |

## Constance settings

| Setting | Effect | Described in |
|---|---|---|
| `DEFAULT_PROPOSAL_REQUIRED_FIELDS`, `DEFAULT_PROPOSAL_HIDDEN_FIELDS` (under **Proposal settings**) | The project details fields a new call starts with; applied when the call is created | [Project details fields](application-form.md#project-details-fields) |
| `PROPOSAL_REVIEW_DURATION` (under **Proposal settings**) | The review duration, in days, a new round gets when none is given | [Rounds](call-rounds.md) |
| `PROPOSAL_DASHBOARD_REVIEWS_DUE_WITHIN_DAYS` (under **Proposal settings**) | How many days ahead a deadline counts as due soon, for reviews on the call manager dashboard and for tasks in **My tasks** | [Dashboards and reports](dashboards-and-reports.md) |
| `REVIEWER_PROFILES_ENABLED`, `REVIEWER_PUBLICATION_REQUIRES_APPROVAL` (under **Proposal settings**) | Whether users can create and publish reviewer profiles, and whether publishing a profile needs staff approval | [Reviewer profiles](reviewer-management.md#reviewer-profiles) |
| `COI_DETECTION_ENABLED`, `COI_DISCLOSURE_REQUIRED` (under **Proposal settings**) | Whether call managers can run automated conflict of interest detection, and whether reviewers must file a current conflict of interest disclosure for a call before taking on its reviews | [Conflict of interest management](coi-management.md) |
| `COI_COAUTHORSHIP_LOOKBACK_YEARS`, `COI_COAUTHORSHIP_THRESHOLD_PAPERS`, `COI_INSTITUTIONAL_LOOKBACK_YEARS` (under **Proposal settings**) | Defaults for co-authorship and institutional conflict detection: the years looked back, and the number of co-authored papers that counts as a conflict | [Configuring COI detection](coi-management.md#configuring-coi-detection) |
| `AUTOMATED_MATCHING_ENABLED` (under **Proposal settings**) | Whether automated reviewer matching is available: reviewer suggestions, affinity scores and generated assignments | [Reviewer-proposal matching](reviewer-management.md#reviewer-proposal-matching) |
| `ORCID_*` (under **ORCID integration settings**) | The ORCID client, endpoints and sandbox mode used to connect reviewers' ORCID records to their profiles | [Reviewer profile and invitations](reviewer-guide.md) |
| `ENABLED_USER_PROFILE_ATTRIBUTES` | Which applicant attributes are collected, and so which eligibility rows a call offers | [Entering values](application-form.md#entering-values) |
| `SERVICE_ACCESS_MODE` (under **Marketplace visibility & access**) | Calls mode | [Service access modes](../../admin-guide/mastermind-configuration/service-access-modes.md) |

## Notifications

Several emails of the call workflow are sent only when their notification is enabled on the
deployment:

| Notification | Sent when | Described in |
|---|---|---|
| `proposal.reviewer_assignment_invitation` | An assignment batch is sent to a reviewer | [Sending draft batches](reviewer-management.md#sending-draft-batches) |
| `proposal.assignment_expiry_reminder` | A sent batch approaches its deadline | [Batch lifecycle](reviewer-management.md#batch-lifecycle) |
| `proposal.assignment_batch_expired` | A batch expires with proposals unanswered | [Batch lifecycle](reviewer-management.md#batch-lifecycle) |
| `proposal.reviewer_pool_invitation_expired` | A pool invitation expires | [Invitation expiry and resending](reviewer-management.md#invitation-expiry-and-resending) |
| `proposal.proposal_withdrawn` | An applicant withdraws a proposal | [Withdrawn proposals](requests-for-changes.md#withdrawn-proposals) |

In `marketplace` mode the proposal notifications are sent with the `access_request_*` templates
instead. The notification catalogue and how to enable notifications are described in
[Notifications](../../admin-guide/mastermind-configuration/notifications.md). Step notification
rules are set per call — see [Notification rules](workflow-configuration.md#notification-rules).

## Exporting the platform structure

The `waldur export_structure` management command exports the platform's structure, including
checklists and answers — see [Management command export](data-export.md#management-command-export).

## Upgrading to workflow v2

Upgrading the proposal module converts existing calls and proposals to the configurable call
workflow. The operator's checks and upgrade log are described in
[Upgrading the proposal module to v2](../../admin-guide/proposal-module-v2-migration.md); what
call managers settle afterwards in [After the upgrade to workflow v2](upgrading-to-workflow-v2.md).

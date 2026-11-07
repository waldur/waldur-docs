# After the upgrade to workflow v2

When your Waldur is upgraded to version 2 of the proposal module, existing calls and proposals are
converted to the configurable call workflow. Proposals already in evaluation keep their path, and
most calls need nothing from you. A few situations are left for you to settle, because only the call
manager knows the right answer.

Your operator can tell you which of your calls are affected: they run checks before the upgrade and
keep the upgrade log. The operator's side is described in
[Upgrading the proposal module to v2](../../admin-guide/proposal-module-v2-migration.md).

## Checklist

### Reviewers who declined but hold the reviewer role

Some reviewers declined your call's pool invitation, or let it expire, but were also given the call's
reviewer role directly. In v2 the pool and the role are one list. The upgrade kept both the decline
and the role rather than decide for the reviewer.

For each such reviewer, decide which one stands:

- **They are not reviewing**: revoke their reviewer role. The call's **Team** tab does not list
  reviewers, so ask your operator, or use the API as described in
  [Reviewer pools and roles](../../admin-guide/proposal-module-v2-migration.md#reviewer-pools-and-roles).
  Their pool entry stays declined.
- **They are reviewing after all**: open the call's **Manage → Reviewer pool → Pool**, and choose
  **Force accept invitation** from their row's actions, with a reason. This needs the reviewer to
  have a reviewer profile. A declined invitation cannot be sent again.

### Invitations accepted on a reviewer's behalf

If a reviewer held the reviewer role but had not yet answered the pool invitation, the upgrade
accepted it for them. In **Manage → Reviewer pool → Pool** these entries show the override reason
"Given the call's reviewer role." Check that they still expect to review for the call.

### Pool members who were given the reviewer role

Reviewers who had accepted the pool invitation but did not hold the reviewer role now hold it. The
role lets them be given reviews directly, sends them step notifications, and lets them act on steps
whose responsible role is "reviewer". Have the role revoked from anyone who should not have that
access, as above. Doing so also marks their pool entry declined.

### Calls that had no enabled step

An open call older than the workflow steps may have had no enabled step, so nothing submitted to it
could be evaluated. The upgrade enabled the **Administrative check** and the **Allocation
decision**, the steps a new call starts with. If your call should evaluate proposals differently,
change its workflow under **Edit → Evaluation workflow → Steps & settings** before new proposals
arrive.

### Score thresholds with no review step before them

A score threshold, for example on the **Allocation decision**, now reads the scores of the steps
before it. If no enabled step before it collects reviews, the workflow check (shown above the steps
under **Edit → Evaluation workflow → Steps & settings**) reports an error:

- an active call keeps running, and proposals that already have reviews pass as before;
- a proposal with no reviews stops at the step;
- a draft call cannot be activated.

Either enable a review step, such as **Expert review**, before the threshold, or remove the
threshold.

## What looks different

- **Step forms shared between steps.** Each step now keeps its own copy of the answers. Changing an
  answer at one step no longer changes it at the other.
- **Step order.** Steps are shown in the order proposals go through them. A display order set in v1
  is no longer used. Proposals follow the same path as before.
- **Review scores** run from 1 to 5. Scores above 5 given in v1 are kept as they were, unless your
  operator rescaled them with you.
- **Reviewer statistics** are worked out from the reviews in Waldur. Figures imported from another
  system are no longer shown.
- **Active proposals per applicant.** Staff can now cap how many proposals one applicant may have
  under evaluation or running as a project across all of your organisation's calls. The upgrade
  sets no limit.

# Upgrading the proposal module to v2

Version 2 of the proposal module replaces the fixed six-step evaluation with the configurable call
workflow. Each call has its own steps with their own order, contributors and gates. The upgrade
converts existing calls and proposals in place. Proposals already in evaluation keep the path they
were submitted with.

This page is for operators. It covers what to check before upgrading, what the migration writes to
its log, and what to tell call managers afterwards. Call managers have their own checklist:
[After the upgrade to workflow v2](../user-guide/call-managing-organization/upgrading-to-workflow-v2.md).

## What the upgrade does

The workflow itself comes in three migrations of the `proposal` app, which run in this order as
expand, backfill and contract, after one `checklist` migration they depend on:

| Migration | What it does |
|---|---|
| `checklist.0017_checklist_organization` | Runs first. Lets a checklist belong to an organisation. |
| `proposal.0093_call_workflow_expand` | Adds every new table and column: call steps with their order, contributors and gates, contributions, proposal runs, panels, call templates, per-criterion review scores (review scores now run from 1 to 5), and more. It renames three step fields (`step` to `key`, `responsible_role` to `completer`, `min_reviewers` to `min_contributions`) and changes no data. |
| `proposal.0094_call_workflow_backfill` | Fills them in for existing calls and proposals. Every call gets a row for each of the six former steps, and every proposal's steps a link to their call's row. Reviews become contributions to the call's review step. Answers to step forms move from the proposal to the contributions of the people who gave them. Open calls with no enabled step get the administrative check and the allocation decision. A call's reviewer pool and its reviewer role become one list of reviewers (see [Reviewer pools and roles](#reviewer-pools-and-roles)). Existing roles get this release's new permissions, and the project roles of an awarded proposal's team (Principal investigator, Co-investigator, Collaborator) are created. |
| `proposal.0095_call_workflow_contract` | Makes required and unique what `0094` filled in, and drops the proposal's old step field and the `ReviewerStats` table. Reviewer figures are now computed from the reviews themselves. |

The same release brings smaller migrations around them. None needs a decision:

| Migration | What it does |
|---|---|
| `proposal.0092_delete_empty_proposal_documents` | Deletes proposal document rows that have no file. They could not be shown or downloaded, and broke reading their proposal. |
| `configuration.0004_drop_removed_reporting_screens` | Removes `call-performance`, `review-progress` and `resource-demand` from a stored `ENABLED_REPORTING_SCREENS`. Those screens are replaced by `call-reports` (**Proposals: Call reports**). It is on by default, but a deployment that stored its own list must add it. |
| `proposal.0096`, `proposal.0097` | Record when a review was submitted. Reviews submitted before the upgrade take the time their submission was logged, or else their last change. |
| `proposal.0098_callmanagingorganisation_max_active_proposals` | Adds the per-applicant limit on active proposals, empty (no limit). See [New settings](#new-settings). |
| `proposal.0099_call_image` | Adds an optional logo to calls, empty. |

Expect about 50 seconds for the three workflow migrations on top of the rest of the release, almost all of it
CPU time in Django rather than database work. That time does not grow noticeably with the amount
of data.

!!! note
    Each migration runs in one transaction, and a table it changes stays locked until the
    migration finishes. If the previous release keeps serving requests during the upgrade, as it
    does with the Helm chart's rolling update, call and proposal pages can stall for up to about a
    minute while `proposal.0093` runs. Calls and requested offerings, which pages outside the
    proposal module read too, are changed last, so they are locked only for the last ten seconds
    or so.

## Before you upgrade

1. **Back up the database.** The data migrations cannot be fully reversed: answers copied between
   steps, the reviewer pool changes and the deleted empty documents are not restored by migrating
   backwards.
2. **Run the pre-upgrade checks below** against the production database, or a copy of it, while it
   still runs v1. Each query lists the rows behind one of the decisions or follow-ups on this page.
   An empty result means there is nothing to do.
3. **Settle the two decisions** that only you can make before migrating:
   [review scores above 5](#review-scores-above-5) and
   [imported reviewer statistics](#imported-reviewer-statistics).
4. **Send the call managers the results** of checks 3 to 7, so they know which calls to look at after
   the upgrade.

### Pre-upgrade checks

Run these with `psql` against the v1 database. The first query defines the holders of a call's
reviewer role, which several checks use.

```sql
-- Used by checks 3, 4 and 5: who holds the reviewer role of which call.
create temporary view call_reviewer_role as
select ur.object_id as call_id, ur.user_id
from permissions_userrole ur
join permissions_role r on r.id = ur.role_id
where ur.is_active
  and ur.content_type_id = (
    select id from django_content_type where app_label = 'proposal' and model = 'call'
  )
  and (
    r.name = 'CALL.REVIEWER'
    or r.template_id in (select id from permissions_role where name = 'CALL.REVIEWER')
  );
```

**1. Review scores above 5, and score thresholds above 5.** See
[Review scores above 5](#review-scores-above-5).

```sql
select c.id as call_id, c.name as call, count(*) as reviews, max(r.summary_score) as highest
from proposal_review r
join proposal_proposal p on p.id = r.proposal_id
join proposal_round rd on rd.id = p.round_id
join proposal_call c on c.id = rd.call_id
where r.summary_score > 5
group by c.id, c.name;

select c.id as call_id, c.name as call, s.step, s.min_score_threshold
from proposal_callworkflowstep s
join proposal_call c on c.id = s.call_id
where s.min_score_threshold > 5;
```

**2. Imported reviewer statistics.** See [Imported reviewer statistics](#imported-reviewer-statistics).

```sql
select count(*) from proposal_reviewerstats;
```

**3. Reviewers who declined, yet hold the reviewer role.** The upgrade keeps both. Their call manager
decides which one stands.

```sql
select c.id as call_id, c.name as call, u.username, p.invitation_status, p.decline_reason
from proposal_callreviewerpool p
join proposal_call c on c.id = p.call_id
left join proposal_reviewerprofile rp on rp.id = p.reviewer_id
join core_user u on u.id = coalesce(rp.user_id, p.invited_user_id)
join call_reviewer_role h on h.call_id = p.call_id and h.user_id = u.id
where p.invitation_status in ('declined', 'expired');
```

**4. Unanswered invitations of people who hold the reviewer role.** The upgrade accepts these
invitations on the reviewer's behalf.

```sql
select c.id as call_id, c.name as call, u.username, p.invited_email
from proposal_callreviewerpool p
join proposal_call c on c.id = p.call_id
left join proposal_reviewerprofile rp on rp.id = p.reviewer_id
join core_user u
  on u.id = coalesce(rp.user_id, p.invited_user_id)
  or (p.reviewer_id is null and p.invited_user_id is null and lower(u.email) = lower(p.invited_email))
join call_reviewer_role h on h.call_id = p.call_id and h.user_id = u.id
where p.invitation_status = 'pending';
```

**5. Accepted pool members without the reviewer role.** The upgrade gives them the role, which
widens their access to the call.

```sql
select c.id as call_id, c.name as call, u.username
from proposal_callreviewerpool p
join proposal_call c on c.id = p.call_id
left join proposal_reviewerprofile rp on rp.id = p.reviewer_id
join core_user u on u.id = coalesce(rp.user_id, p.invited_user_id)
where p.invitation_status = 'accepted'
  and not exists (
    select 1 from call_reviewer_role h where h.call_id = p.call_id and h.user_id = u.id
  );
```

**6. Score thresholds with no review step before them.** The new workflow check reports these calls
as errors. See [Score thresholds without a review step](#score-thresholds-without-a-review-step).
Use this list rather than the upgrade log: the log leaves out a call where an enabled technical assessment
without gates of its own comes before the threshold, which the workflow check still reports.

```sql
select c.id as call_id, c.name as call, c.state, s.step, s.min_score_threshold
from proposal_callworkflowstep s
join proposal_call c on c.id = s.call_id
where s.is_enabled
  and s.min_score_threshold is not null
  and s.step <> 'expert_review'
  and c.state in ('draft', 'active')
  and (
    -- the administrative check and the technical assessment come before the expert review
    s.step in ('administrative_check', 'technical_assessment')
    or not exists (
      select 1 from proposal_callworkflowstep e
      where e.call_id = c.id and e.step = 'expert_review' and e.is_enabled
    )
  );
```

**7. Open calls with no enabled step.** The upgrade enables the administrative check and the
allocation decision in them.

```sql
select c.id as call_id, c.name as call, c.state
from proposal_call c
where c.state in ('draft', 'active')
  and not exists (
    select 1 from proposal_callworkflowstep s where s.call_id = c.id and s.is_enabled
  );
```

**8. Step forms shared by several steps, or reusing the compliance form.** No action is needed, but
see [Step forms](#step-forms) for what changes.

```sql
select c.id as call_id, c.name as call, ck.name as form,
       string_agg(s.step, ', ' order by s.step) as steps,
       bool_or(s.checklist_id = c.compliance_checklist_id) as is_compliance_form
from proposal_callworkflowstep s
join proposal_call c on c.id = s.call_id
join checklist_checklist ck on ck.id = s.checklist_id
where s.is_enabled
group by c.id, c.name, ck.name, c.compliance_checklist_id
having count(*) > 1 or bool_or(s.checklist_id = c.compliance_checklist_id);
```

**9. Calls with a custom step display order.** See [Step order](#step-order).

```sql
select c.id as call_id, c.name as call, count(*) as steps_with_display_order
from proposal_callworkflowstep s
join proposal_call c on c.id = s.call_id
where s.display_order is not null
group by c.id, c.name;
```

## Decisions before the upgrade

### Review scores above 5

v1 accepted any whole number as a review's overall score. v2 scores from 1 to 5, and refuses a higher
score when a review is saved. The upgrade does not rescale existing scores, because the scale a call
used is not recorded anywhere.

If check 1 finds nothing, there is nothing to decide. If it finds calls, then after the upgrade:

- averages, rankings, score gates and exports mix the call's old scores with new 1–5 scores;
- a reviewer who reopens and saves an unfinished review with a score above 5 must score it again;
- a score threshold above 5 can never be reached by reviews scored on the new scale.

For each call the check lists, choose one of these:

- **Leave it.** This suits calls that are archived or whose evaluation is finished. Their history
  stays as the reviewers entered it.
- **Rescale it before the upgrade.** This suits calls still in evaluation. Rescale the call's scores
  and its thresholds together, so that gates keep their meaning. For example, for a call that scored
  from 1 to 10:

    ```sql
    -- Call 42 scored 1-10: halve its scores and thresholds. 0 means not yet rated.
    update proposal_review r
    set summary_score = greatest(1, round(r.summary_score / 2.0))
    from proposal_proposal p, proposal_round rd
    where p.id = r.proposal_id and rd.id = p.round_id
      and rd.call_id = 42 and r.summary_score > 0;

    update proposal_callworkflowstep
    set min_score_threshold = min_score_threshold / 2
    where call_id = 42 and min_score_threshold is not null;
    ```

!!! warning
    Rescaling changes what reviewers entered, and results already published to applicants still
    show the old scores. Agree the change with the call's managers first.

### Imported reviewer statistics

v1 kept reviewer statistics in a `ReviewerStats` table. Waldur itself never wrote to it: only
`import_structure` and the `call_management` demo preset filled it. v2 computes the same figures
(completed, declined and timed-out reviews, average score, average review time) live from the reviews
and assignments, and `proposal.0095` drops the table.

- If check 2 returns 0, nothing is lost.
- Otherwise the imported rows describe history from outside this database, and they are lost with
  the table. The quality rating fields have no counterpart in v2. To keep the rows, dump the table
  before the upgrade:

    ```bash
    pg_dump --table=proposal_reviewerstats --format=custom --file=reviewerstats.dump <database>
    ```

`proposal.0094` logs how many rows will be dropped ("Dropping … rows") before `0095` drops them.

## During the upgrade

Run the migrations as usual. They log at `WARNING` level whatever a person has to look at.
Keep the output: call managers will need it.

| Log message | Meaning | Who acts |
|---|---|---|
| `<user> holds the reviewer role of call <id> but its pool invitation is declined; both are left as they are.` (or `expired`) | Check 3. The reviewer declined but still holds the role. | Call manager |
| `Call <id> had no enabled step; enabled administrative_check, allocation_decision.` | Check 7. New proposals to this call now start at the administrative check. | Call manager |
| `Call <id>: the <step> step needs a score of <n>, and no enabled step before it collects reviews. …` | Check 6, which may list more calls. The call cannot be activated again as it stands. | Call manager |
| `Dropping <n> imported reviewer stats rows (reviewer profiles …).` | Check 2. | Operator |
| `Proposal <id> has a <step> step its call had no row for; added it disabled.` | The proposal used a step its call no longer had. It keeps its path. | None |
| `Proposal <id> stood on the <step> step but has no instance of it; it is left outside the workflow.` | Data that v1 could not process either. The proposal is left as it was. | Operator |
| `Answers of proposal <id> to checklist <id> belong to no step of it; left in place.` | The proposal has no step using that form, so its answers stay on the proposal and no step shows them. | Operator |

Call ids in the log are database ids. To find the call:

```sql
select id, uuid, name, state from proposal_call where id in (2, 28);
```

## After the upgrade

Send each call manager the calls from checks 3 to 7 and the log, and point them to
[After the upgrade to workflow v2](../user-guide/call-managing-organization/upgrading-to-workflow-v2.md).
The sections below explain what changed, for answering their questions.

### Reviewer pools and roles

In v1, a call's reviewer pool and its reviewer role (`CALL.REVIEWER`, granted on the call through
the API, an import, or a call manager's **Review this proposal yourself**) were separate lists.
In v2 they are one list, and the upgrade merges them:

- a holder of the reviewer role joins the pool as accepted. An unanswered invitation is accepted on
  their behalf, and an invitation sent to their e-mail address is linked to their account. The pool
  shows these entries with the override reason "Given the call's reviewer role.";
- an accepted pool member who lacked the role is given it. That gives them what the role grants:
  being given reviews directly, step notifications, and acting on steps whose responsible role is
  "reviewer";
- a reviewer who **declined** or let the invitation expire but holds the role keeps both. The upgrade
  does not decide for them.

From then on, granting the role adds the person to the pool, accepting a pool invitation grants the
role, and revoking the role marks the pool entry declined.

The call's **Team** tab lists only call managers and panel members, so call managers cannot revoke
the reviewer role from the UI. A call manager or organisation owner revokes it through the API, or
you do it for them:

```bash
curl -X POST -H "Authorization: Token <token>" -H "Content-Type: application/json" \
  -d '{"user": "<user uuid>", "role": "CALL.REVIEWER"}' \
  https://<waldur>/api/proposal-protected-calls/<call uuid>/delete_user/
```

`GET /api/proposal-protected-calls/<call uuid>/list_users/?role=CALL.REVIEWER` lists who holds it.

### Score thresholds without a review step

In v1, a score threshold on a step such as the allocation decision averaged every submitted review on
the proposal, however the review came about. In v2 the threshold reads the scores of the steps before
it, and the workflow check reports a threshold that nothing scores as an error. Errors block only
activation:

- an active call keeps running. Proposals that already have reviews pass the threshold as before;
- a proposal with no reviews stops at the step, as it did in v1;
- a draft call cannot be activated until its call manager enables a review step before the threshold
  or removes the threshold.

### Open calls with no enabled step

Draft and active calls created before v1 had step rows may have no enabled step, so nothing submitted
to them could be evaluated. The upgrade enables the administrative check and the allocation decision,
the steps a new call starts with. Proposals already submitted keep their path. Archived calls are not
changed.

### Step forms

In v1, answers to a step's form belonged to the proposal, and every step using that form saw the same
answers. In v2 each person's answers belong to their contribution to the step. The upgrade gives each
step that used the form a copy of the answers, so nothing is lost. From then on the copies are
separate: an answer changed at one step does not change at the other.

A copied file answer refers to the same stored file as the original.

A step that uses the call's compliance form still counts the applicant's compliance answers towards
its required questions, as in v1.

### Step order

v1 let call managers set a display order for steps, but proposals always went through the steps in
the fixed order. v2 shows steps in the order proposals go through them, and ignores the display
order. Calls from check 9 will show their steps in a different order than before. Their proposals
follow the same path as before.

### New settings

The upgrade turns on nothing new that limits users. These settings arrive off or empty:

- **Active proposals per applicant** on a call-managing organisation
  (`max_active_proposals_per_applicant`): how many proposals an applicant may have under evaluation
  or running as a project, across all of the organisation's calls, before they may submit another.
  Staff set it under the organisation's **Edit → Call manager** tab; the organisation's owners can set it
  through the API (`PATCH /api/call-managing-organisations/<uuid>/`). Empty means no limit.
- `REVIEWER_PUBLICATION_REQUIRES_APPROVAL` (default off): staff approve a reviewer profile before
  call managers can discover it.
- `call-reports` in `ENABLED_REPORTING_SCREENS`, if you stored your own list of screens: the call
  reports that replace the three removed ones. With the default list it is already on.

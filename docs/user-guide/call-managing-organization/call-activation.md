# Checking and activating a call

**Performed by:** Call manager (or call organiser, or staff)

A call opens for proposals when it is activated. Activation runs the workflow check first, and
refuses a call whose workflow cannot run as configured.

## Call activation process

Once all configurations are complete:

1. **Review all configurations**:
      - Verify general settings are correct
      - Confirm team assignments are complete
      - Check that offerings are properly configured
      - Ensure role mappings are defined — without them the **Activate call** confirmation
        warns **No role mappings**: projects allocated from approved proposals would have
        nobody on them

2. **Run the workflow check** — see [Checking the workflow before activation](#checking-the-workflow-before-activation).

3. **Activate the call**:
      - Choose **Activate** from the call's actions to open it for proposal submissions, and
        confirm in the **Activate call** dialog
      - **Activate** stays disabled, with the reason on hover, while the call has no round, no
        enabled workflow step, not exactly one enabled allocation decision, or no accepted
        offering
      - Once activated, the call becomes visible to potential applicants
      - Applicants can now submit proposals during active rounds

## Checking the workflow before activation

The call's **Validation** tab, between **Manage** and **Edit**, says whether
the call's workflow works as configured. Its **Check** sub-tab lists every
finding with its severity and a link that opens the setting to fix:

- **Errors** mean the call cannot run as configured — for example no round, no
  enabled step, no or several allocation decisions, an award response before
  the decision, a step that nobody can complete, a run condition naming a
  missing or later step, an accepted offering missing, or a notification rule
  that can never reach anyone.
- **Warnings** never block — for example step durations up to the decision
  that exceed the round's time to decision (the allocation date, else **Target
  days from cut-off to decision**), steps without a duration, or an empty
  reviewer pool.
- **Info** lists, for example, the roles the call managers assign by hand and
  the steps that differ from the template the call was created from.

**Activate** runs the same check and refuses the call while there are errors;
the action shows their number (*Activate (2 errors)*), and a refused activation
lists all of them at once. There is no override. The calls list shows the
verdict too, under **Workflow check** in the call's expanded row.

An archived call can be activated again the same way.

The other sub-tabs of **Validation** help confirm that the workflow does what
you intend: **Roles**, **Notifications**, **Diagram**, **Timeline**,
**Paths**, **Dry run**, **Scenarios**, and **Changes** — the call's saved
workflow versions, compared with each other or with the template the call was
created from.

## Changing an active call

Workflow steps stay editable while the call is active, but a reconfigured step applies only to
proposals submitted afterwards: each proposal keeps the path it was submitted with. Make
structural changes before activation wherever you can — see
[Rules across a call's steps](workflow-configuration.md#rules-across-a-calls-steps).

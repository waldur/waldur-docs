# Acting on several offerings at once

**Administration → Marketplace → Offerings** lists every offering on the portal. Select
offerings with the checkboxes in the first column, or every offering on the current page with
the checkbox in the header, and an **Actions** menu appears above the table. Each action runs
on the selected offerings one by one, exactly as if you had used the same action in each
offering's own row menu.

Selection covers the current page only. To act on more offerings, raise the page size or
narrow the list with the filters first.

## What you can do

| Action | Runs on | Notes |
|--------|---------|-------|
| **Activate** | Draft offerings | Skips offerings without a plan, and custom-script offerings without a creation script. |
| **Resume** | Paused offerings | Same checks as Activate. |
| **Pause** | Active offerings | Asks for one pause reason, saved on every paused offering and shown in the marketplace. |
| **Set as down** | Active offerings | The confirmation warns that all operations on the offerings' resources are blocked until the offerings are restored. |
| **Restore** | Offerings that are down | |
| **Set to draft** | Any offering that is not a draft | |
| **Archive** | Any offering that is not archived | |
| **Set offering group** | Offerings of one organization that are not archived | An offering group belongs to an organization, so every selected offering must belong to the same one. Archived offerings cannot be changed and are skipped. Leave the group empty to take the offerings out of their group. |
| **Move offerings** | Any offering | Staff only. Moves the offerings to another service provider organization, optionally keeping their permissions. |
| **Export** | Any offering | Asks for the export parameters once and downloads one ZIP archive with a YAML file per offering. Each file can be imported on its own, just like a single-offering export. |
| **Delete** | Draft offerings; any offering for staff | The portal still refuses an offering that has resources, or active resources when the offering restricts deletion. |

An action that none of the selected offerings can take stays in the menu but is disabled, and
the question mark beside it says why. While an action runs, the others are disabled until it
finishes. Before an action runs, the confirmation or dialog lists
the offerings it will change and says how many of the selected ones it leaves alone.

Actions are shown only to users who may take them. A service provider who opens the list sees
only the actions their roles allow, applied only to the offerings of their own organizations.
State changes and deletion also depend on whether the deployment lets service providers manage
their offerings' lifecycle; otherwise they are for staff only.

## When some offerings fail

Each offering succeeds or fails on its own; one refusal does not stop or undo the rest. When
the action finishes:

- a success message says how many offerings were changed;
- an error message names the offerings that failed (up to five, then how many more) with the
  reason the portal gave for each;
- the list reloads, and the offerings that failed **stay selected**, so you can fix them and run
  the action again without picking them out once more.

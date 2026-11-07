# Proposal ID configuration

Waldur allows call managers to configure custom proposal ID patterns per call. This ensures proposals have meaningful, structured identifiers that follow organizational conventions.

## How proposal IDs work

Each proposal receives a **slug** (identifier) generated from a configurable template. The slug is assigned when the proposal is created in draft state, and is always upper-cased.

## Configuring the ID template

**Performed by:** Call manager (before the call has any proposals)

1. Open the call's **Edit** page
2. Under **Call → General**, set the **Proposal slug template**
3. Use the available template variables to define your pattern

## Available template variables

| Variable | Description | Example Value |
|---|---|---|
| `{call_slug}` | The call's slug identifier | `hpc-call-2026` |
| `{round_slug}` | The round's slug identifier — by default generated as `<organization slug>-<call slug>-<YYYYMM of the round start>`, upper-cased | `RESEARCH-COUNCIL-HPC-CALL-2026-202607` |
| `{org_slug}` | The slug of the call-managing organization | `research-council` |
| `{year}` | Current year | `2026` |
| `{month}` | Current month (2-digit) | `04` |
| `{counter}` | Sequential counter within the round | `7` |
| `{counter_padded}` | Zero-padded counter (3 digits) | `007` |

## Example patterns

| Pattern | Example Output |
|---|---|
| `{call_slug}-{counter_padded}` | `HPC-CALL-2026-001` |
| `{round_slug}-{year}-{counter_padded}` | `RESEARCH-COUNCIL-HPC-CALL-2026-202607-2026-001` |
| `{call_slug}/{org_slug}-{counter}` | `HPC-CALL-2026/RESEARCH-COUNCIL-1` |

!!! note
    The default pattern (if no template is configured) is `{round_slug}-{counter_padded}`, for example `RESEARCH-COUNCIL-HPC-CALL-2026-202607-001`.

## Important considerations

- The template **cannot be changed** once the call has proposals, drafts included
- The counter resets per round — each round starts counting from 1
- The counter counts all proposals in the round (including drafts)

!!! warning
    Plan your ID pattern carefully before activating the call. Once proposals are created, the template is locked to prevent ID inconsistencies.

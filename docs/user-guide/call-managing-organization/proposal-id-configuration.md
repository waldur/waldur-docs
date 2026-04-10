# Proposal ID configuration

Waldur allows call managers to configure custom proposal ID patterns per call. This ensures proposals have meaningful, structured identifiers that follow organizational conventions.

## How proposal IDs work

Each proposal receives a unique **slug** (identifier) generated from a configurable template. The slug is assigned when the proposal is created in draft state.

## Configuring the ID template

**Performed by:** Call manager (before any proposals are submitted)

1. Navigate to the **call configuration**
2. In the **General configuration** section, set the **Proposal slug template**
3. Use the available template variables to define your pattern

## Available template variables

| Variable | Description | Example Value |
|---|---|---|
| `{call_slug}` | The call's slug identifier | `hpc-call-2026` |
| `{round_slug}` | The round's slug identifier | `round-1` |
| `{org_slug}` | The proposing organization's slug | `university-of-tartu` |
| `{year}` | Current year | `2026` |
| `{month}` | Current month (2-digit) | `04` |
| `{counter}` | Sequential counter within the round | `7` |
| `{counter_padded}` | Zero-padded counter (3 digits) | `007` |

## Example patterns

| Pattern | Example Output |
|---|---|
| `{call_slug}-{counter_padded}` | `hpc-call-2026-001` |
| `{round_slug}-{year}-{counter_padded}` | `round-1-2026-001` |
| `{call_slug}/{org_slug}-{counter}` | `hpc-call-2026/university-of-tartu-1` |

!!! note
    The default pattern (if no template is configured) is `{round_slug}-{counter_padded}`.

## Important considerations

- The template **cannot be changed** after proposals have been submitted to the call
- The counter resets per round — each round starts counting from 1
- Proposal slugs are unique within the system
- The counter counts all proposals in the round (including drafts)

!!! warning
    Plan your ID pattern carefully before activating the call. Once proposals are created, the template is locked to prevent ID inconsistencies.

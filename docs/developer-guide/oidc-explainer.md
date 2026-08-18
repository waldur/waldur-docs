---
hide:
  - toc
---

# OIDC login flow, step by step

Waldur delegates authentication to an external identity provider over OpenID
Connect. The walkthrough below plays that flow one hop at a time, showing the
payload on the wire at each step and linking to the code that produces it.

<!--
  Both references below are URL-relative, not source-relative. MkDocs serves
  this page at /developer-guide/oidc-explainer/ (directory URLs) and copies the
  built app to /developer-guide/oidc-explainer/app/, so "app/index.html" is
  correct from the rendered page. Writing "./oidc-explainer/app/..." resolves to
  a doubled path. Kept as raw HTML so MkDocs does not rewrite it against the
  source tree.
-->
<iframe src="app/index.html"
        title="Interactive walkthrough of the Waldur OIDC login flow"
        style="width:100%;height:760px;border:1px solid var(--md-default-fg-color--lightest);border-radius:6px"
        loading="lazy"></iframe>

<a class="md-button" href="app/index.html" target="_blank">Open it full screen</a>

!!! tip "Linking to a specific step"

    Every step has its own URL. `#/flow/step/8` is the back-channel token
    request; `#/scenario/no-pkce/step/3` is where the PKCE branch parts company
    with the normal flow. Handy for pointing at one hop in a review comment.

    Step numbers count the shared prefix too — a branch replays the flow up to
    its divergence point before its own steps begin, so branch step 1 is the
    start of the *whole* run, not of the branch.

    Arrow keys step back and forth and space plays or pauses. Hovering a hop
    line previews its payload; clicking one jumps to that step.

    **Overview & full text** swaps the animation for a sequence diagram of the
    whole flow plus every step as a plain document, with the stepper moving
    through the prose as you go. That view is also the keyboard and
    screen-reader path: the diagram's rows are focusable and selectable, where
    the 3D scene's hop lines are reachable by pointer only.

## The three things worth taking away

**Redirect versus direct call.** Some hops travel *through* the user's browser
as redirects, so their contents land in the address bar, in browser history and
in any proxy log on the way. Others are direct requests whose payload never
appears in a URL. Which of the two a secret travels on decides how much
protection it needs.

Note that "direct" is not the same as "server to server". The Homeport SPA runs
*inside* the browser, so its calls to Mastermind are direct — nothing lands in a
URL — but they still originate in the browser and hold no client secret. Only
the Mastermind-to-provider hops are a true back channel.

**Three different credentials, one login.** The identity provider's access
token, the one-time token-exchange code, and Waldur's own DRF API token are
distinct things with distinct lifetimes. Only the last one authorises API
calls. Conflating them is the most common source of confusion when reading the
auth code.

**Claims become a user.** On first successful login Waldur creates the user
record from the claims it just read: just-in-time provisioning, driven by the
`user_field`, `user_claim` and `attribute_mapping` columns on the identity
provider.

## Bearer token mode

Alongside the default flow there is a **Bearer token mode** branch, covering
the configuration where `OIDC_ACCESS_TOKEN_ENABLED` is on. It diverges at the
point where the exchange code is minted and runs six further steps:

- `TokenExchangeCode` wraps the provider's access token (`external_token`)
  instead of a foreign key to a Waldur token row. The Waldur token is still
  minted a step earlier; it is simply not what gets handed out.
- The SPA therefore ends up holding a credential Waldur did not issue.
- API calls arrive as `Authorization: Bearer <jwt>`, which routes them to
  `OIDCAuthentication` rather than the DRF token backend.
- The JWT is decoded **without verifying its signature** — only `exp` is
  checked locally. Trust is established by the next step, not this one.
- An RFC 7662 introspection call validates the token against the provider,
  authenticated with Waldur's own client credentials over HTTP Basic. Results
  are cached by SHA-256 of the token for `OIDC_CACHE_TIMEOUT` seconds.
- `OIDC_USER_FIELD` picks which introspection field identifies the user. A
  first-time value creates the account; a collision with a pre-existing
  non-OIDC account is *adopted* rather than rejected, with a WARNING log and a
  django-reversion snapshot as the audit trail.

Two consequences worth holding on to: a token revoked at the provider stays
usable until its cache entry expires, and logging out of Waldur deletes the
Waldur token, which is not the credential in play in this mode.

## What the scenarios show

The four **break it** toggles re-run the flow with one guard removed, so the
reason each guard exists is visible rather than asserted:

| Scenario | Guard removed | What an attacker gets |
| --- | --- | --- |
| Drop the state parameter | Session-bound `state` comparison | The victim is silently logged in as the attacker |
| Disable PKCE | `code_verifier` / `code_challenge` binding | A captured authorization code becomes redeemable |
| Replay the exchange code | Single-use redemption under a row lock | A second trade of the same code for an API token |
| Point `return_url` at an attacker | `allowed_redirects` allowlist | The exchange code delivered to a host they control |

Note that PKCE is opt-in per provider: `IdentityProvider.enable_pkce` defaults
to `False`, so the second scenario describes a configuration that really can
exist.

## What this page does not cover

The browser login flow and bearer token mode. Waldur uses OIDC in two further
places, each worth its own read:

- **Machine-to-machine.** The site agent obtains its own token with the
  `client_credentials` grant.
- **Logout and single logout.** Deleting the Waldur token is only half of it;
  the response may carry a `logout_url` for the provider side.

Every "in the code" link points at the public GitHub mirrors of
`waldur-mastermind` and `waldur-homeport`, on the `develop` branch.

Related reading: [Multi-client OIDC authentication](multi-client-oidc.md) for
the `allowed_redirects` rules in full, and
[Identity](../about/concepts/identity.md) for how OIDC sits alongside SAML2,
SCIM and LDAP.

## Working on the explainer

The source is a Vite app in `oidc-explainer/` at the root of this repository.
The content is data, not code: the steps, payloads and code references all live
in `src/data/flow.ts`, `src/data/scenarios.ts` and `src/data/variants.ts`, so
keeping the page honest after a change to the auth flow is an edit to those
files.

```bash
cd oidc-explainer
npm install
npm run dev          # develop against localhost
npm run check-refs   # verify every cited symbol still exists
npm run build        # emits into docs/developer-guide/oidc-explainer/app
```

The build output is gitignored and produced in CI by the **Build OIDC
explainer** job, so `mkdocs serve` on a fresh clone shows an empty frame until
you run `npm run build` once.

`npm run check-refs` reads every code reference in every file under
`src/data/` — it globs the directory, so a new data file cannot slip in
unchecked — and confirms the symbol still exists in the product repositories.
Locally it expects them as siblings of this one, or at
`WALDUR_MASTERMIND_PATH` / `WALDUR_HOMEPORT_PATH`; where it finds no checkout
it reports how many references went unchecked and skips rather than fails.
Set `WALDUR_REFS_STRICT=1` to make an unchecked reference an error instead.

In CI the job clones the two repositories from the public GitHub mirrors and
runs strict, so the check covers exactly the code a reader will land on when
they follow a link from the page.

import { FIXTURES as F } from './flow';
import { SPECS } from './specs';
import type { Scenario } from './types';
import { VARIANTS } from './variants';

/**
 * Each scenario replays the flow with one guard removed. The shared prefix runs
 * normally up to `divergeAfter`, then these steps take over.
 */
export const SCENARIOS: Scenario[] = [
  {
    id: 'no-state',
    label: 'Drop the state parameter',
    kind: 'attack',
    short: 'What the state check is actually for',
    outcome:
      "The victim is silently logged in as the attacker, and everything they upload or configure afterwards lands in the attacker's account.",
    guard: {
      title: 'The guard',
      text: 'OAuthViewComplete compares the state in the callback URL against the value stored in the session, and rejects the request if they differ or if the session has none.',
      code: [
        {
          repo: 'waldur-mastermind',
          path: 'src/waldur_auth_social/views.py',
          symbol: 'def _complete_login',
        },
      ],
    },
    divergeAfter: 'authorize',
    steps: [
      {
        id: 'attacker-starts',
        title: 'The attacker starts a login of their own',
        from: 'idp',
        to: 'idp',
        channel: 'internal',
        credential: 'authcode',
        narration:
          'The attacker runs the flow up to the callback in their own browser, authenticating as themselves, and then simply stops. They now hold a valid, unredeemed authorization code bound to their own identity.',
        wire: {
          kind: 'internal',
          body: `attacker authenticates as mallory@evil.example
IdP issues code = "ATTACKER-CODE-9f2b"
attacker does NOT follow the redirect`,
        },
        code: [],
      },
      {
        id: 'victim-clicks',
        specs: [SPECS.stateCsrf],
        title: "The victim's browser is made to visit the callback",
        from: 'user',
        to: 'mastermind',
        channel: 'front',
        credential: 'authcode',
        narration:
          "A link in an email, an image tag, any cross-site navigation. The victim's browser hits Waldur's callback carrying the attacker's code.",
        wire: {
          kind: 'http',
          method: 'GET',
          url: `${F.api}/api-auth/${F.provider}/complete/?code=ATTACKER-CODE-9f2b`,
          note: 'No state parameter, and with the guard removed nothing objects.',
        },
        code: [],
      },
      {
        id: 'no-state-redeem',
        title: 'Mastermind happily redeems it',
        from: 'mastermind',
        to: 'idp',
        channel: 'back',
        credential: 'idp_token',
        narration:
          "The code is perfectly valid, so the token endpoint returns tokens. The claims describe the attacker, because it was the attacker who authenticated.",
        wire: {
          kind: 'http',
          status: '200 OK',
          body: `{
  "sub": "mallory-sub-0001",
  "email": "mallory@evil.example"
}`,
        },
        code: [],
      },
      {
        id: 'no-state-outcome',
        title: "The victim is now logged in as the attacker",
        from: 'mastermind',
        to: 'spa',
        channel: 'front',
        credential: 'exchange_code',
        narration:
          "The victim's browser receives a session for mallory@evil.example. They see a working Waldur, assume it is theirs, and every document, key or project they create belongs to the attacker.",
        wire: {
          kind: 'redirect',
          status: '302 Found',
          url: `${F.portal}/oauth_login_completed/${F.provider}/?code=...`,
          note: 'Session fixation. The state check exists to bind the callback to the browser that started the flow.',
        },
        code: [],
      },
    ],
  },

  {
    id: 'no-pkce',
    label: 'Disable PKCE',
    kind: 'attack',
    short: 'Why a stolen code should be useless',
    outcome:
      'Anyone who captures the authorization code in transit can redeem it, provided they also hold the client secret.',
    guard: {
      title: 'The guard',
      text: 'With PKCE on, the token request must carry the code_verifier whose SHA-256 the IdP saw at authorization time. A code lifted from a URL is worthless without the verifier, which never left Mastermind\'s session.',
      code: [
        {
          repo: 'waldur-mastermind',
          path: 'src/waldur_auth_social/views.py',
          symbol: 'def generate_code_challenge',
        },
        {
          repo: 'waldur-mastermind',
          path: 'src/waldur_auth_social/models.py',
          symbol: 'enable_pkce',
        },
      ],
    },
    // Diverge before mint-state, not after: that step mints the code_verifier and
    // pins a PKCE badge on Mastermind, which would sit there contradicting a
    // branch whose whole point is that no verifier exists.
    divergeAfter: 'init-nav',
    steps: [
      {
        id: 'no-pkce-mint',
        title: 'The session gets a state, and nothing else',
        from: 'mastermind',
        to: 'mastermind',
        channel: 'internal',
        credential: 'pkce',
        narration:
          'enable_pkce is False for this provider, so the PKCE branch never runs. A state is still minted, so CSRF protection is intact; what is missing is anything binding the eventual code to this particular flow.',
        wire: {
          kind: 'internal',
          body: `session.flush()
session["oidc_state"] = "${F.state}"

# if self.config.enable_pkce:      <- False, so skipped entirely
#     code_verifier = secrets.token_urlsafe(32)
#     params["code_challenge"] = ...`,
          note: 'IdentityProvider.enable_pkce defaults to False, so this is the out-of-the-box behaviour for a newly configured provider.',
        },
        code: [
          {
            repo: 'waldur-mastermind',
            path: 'src/waldur_auth_social/models.py',
            symbol: 'enable_pkce',
          },
        ],
        effects: [
          {
            actor: 'mastermind',
            add: [
              { id: 'state', label: 'state', value: F.state, credential: 'pkce' },
            ],
          },
        ],
      },
      {
        id: 'no-pkce-authorize',
        title: 'The authorization request goes out without a challenge',
        from: 'mastermind',
        to: 'idp',
        channel: 'front',
        credential: 'none',
        narration:
          'enable_pkce is False, so no code_verifier is generated and no code_challenge is sent. Nothing binds the eventual code to this particular flow.',
        wire: {
          kind: 'redirect',
          status: '302 Found',
          url: `${F.idp}/protocol/openid-connect/auth`,
          body: `response_type = code
client_id     = waldur-portal
redirect_uri  = ${F.api}/api-auth/${F.provider}/complete/
scope         = openid profile email
state         = ${F.state}
(no code_challenge)`,
        },
        code: [],
      },
      {
        id: 'no-pkce-leak',
        title: 'The code leaks on the front channel',
        from: 'idp',
        to: 'user',
        channel: 'front',
        credential: 'authcode',
        narration:
          'The code travels in a URL, so it is exposed anywhere a URL is exposed: browser history, a shared machine, a logging proxy, a malicious extension, a Referer header on the next page load.',
        wire: {
          kind: 'redirect',
          url: `${F.api}/api-auth/${F.provider}/complete/?code=${F.authCode}&state=${F.state}`,
          note: 'This exposure is unavoidable and expected. PKCE is what makes it harmless.',
        },
        code: [],
      },
      {
        id: 'no-pkce-replay',
        specs: [SPECS.pkceTokenRequest],
        title: 'Whoever redeems it first wins',
        from: 'idp',
        to: 'mastermind',
        channel: 'back',
        credential: 'idp_token',
        narration:
          "The token endpoint has nothing to check the caller against beyond the client credentials. A captured code plus a leaked client secret is a complete login as the victim.",
        wire: {
          kind: 'http',
          method: 'POST',
          body: `grant_type   = authorization_code
code         = ${F.authCode}
client_id    = waldur-portal
client_secret = ********
(no code_verifier to prove who started this)

-> 200 OK, tokens for ${F.username}`,
        },
        code: [],
      },
    ],
  },

  {
    id: 'replay-exchange',
    label: 'Replay the exchange code',
    kind: 'attack',
    short: 'Single-use, and why that needs a lock',
    outcome:
      'A code read out of browser history or a proxy log could be traded for the API token a second time.',
    guard: {
      title: 'The guard',
      text: 'TokenExchangeView selects the row FOR UPDATE, checks it is younger than TOKEN_EXCHANGE_TTL (10 seconds), resolves the token and deletes the row, all in one transaction. Two concurrent redemptions cannot both succeed.',
      code: [
        {
          repo: 'waldur-mastermind',
          path: 'src/waldur_core/core/views.py',
          symbol: 'class TokenExchangeView',
        },
      ],
    },
    divergeAfter: 'redirect-spa',
    steps: [
      {
        id: 'replay-first',
        title: 'The SPA redeems the code normally',
        from: 'spa',
        to: 'mastermind',
        channel: 'back',
        credential: 'waldur_token',
        narration: 'The legitimate redemption succeeds and the row is deleted.',
        wire: {
          kind: 'http',
          method: 'POST',
          url: `${F.api}/api-auth/token-exchange/`,
          body: `{ "code": "${F.exchangeCode}" }

-> 200 OK
{ "token": "${F.waldurToken}" }`,
        },
        code: [],
        effects: [
          { actor: 'db', remove: ['exchange-row'] },
          {
            actor: 'spa',
            add: [
              {
                id: 'spa-token',
                label: 'Waldur API token',
                value: `${F.waldurToken.slice(0, 12)}...`,
                credential: 'waldur_token',
              },
            ],
          },
        ],
      },
      {
        id: 'replay-second',
        title: 'An attacker replays the same code',
        from: 'user',
        to: 'mastermind',
        channel: 'back',
        credential: 'exchange_code',
        narration:
          'The code was in a URL, so it is recoverable from history or logs. With the guard in place the row is already gone and the answer is a flat 400.',
        wire: {
          kind: 'http',
          method: 'POST',
          url: `${F.api}/api-auth/token-exchange/`,
          body: `{ "code": "${F.exchangeCode}" }

-> 400 Bad Request
{ "code": "Invalid or expired code." }`,
          note: 'Remove the delete, or do it outside the transaction, and a racing second request gets the same token.',
        },
        code: [],
      },
    ],
  },

  {
    id: 'rogue-redirect',
    label: 'Point return_url at an attacker',
    kind: 'attack',
    short: 'The allowlist behind the last redirect',
    outcome:
      'The exchange code, and therefore the API token, is delivered to a host the attacker controls.',
    guard: {
      title: 'The guard',
      text: 'validate_and_get_redirect_url reduces the return_url or Referer to scheme plus host plus port and requires an exact match in IdentityProvider.allowed_redirects. No wildcards, no path matching, HTTPS except for localhost.',
      code: [
        {
          repo: 'waldur-mastermind',
          path: 'src/waldur_auth_social/utils.py',
          symbol: 'def validate_and_get_redirect_url',
        },
      ],
    },
    divergeAfter: 'exchange-code',
    steps: [
      {
        id: 'rogue-start',
        title: 'The flow was started from an attacker-controlled page',
        from: 'user',
        to: 'mastermind',
        channel: 'front',
        credential: 'none',
        narration:
          'The victim clicks a login link on the attacker\'s site, so the Referer header, and the return destination derived from it, points at that site.',
        wire: {
          kind: 'http',
          method: 'GET',
          url: `${F.api}/api-auth/${F.provider}/init/`,
          headers: { Referer: 'https://waldur-login.evil.example/go' },
        },
        code: [],
      },
      {
        id: 'rogue-redirect-out',
        title: 'The final redirect follows it',
        from: 'mastermind',
        to: 'user',
        channel: 'front',
        credential: 'exchange_code',
        narration:
          'With the allowlist removed, the exchange code is handed to the attacker\'s origin. Their page redeems it before the victim\'s browser can, and walks away with a Waldur API token for the victim.',
        wire: {
          kind: 'redirect',
          status: '302 Found',
          url: `https://waldur-login.evil.example/oauth_login_completed/${F.provider}/?code=${F.exchangeCode}`,
          note: 'The 10-second TTL narrows the window but does not close it: the attacker page redeems on load.',
        },
        code: [],
      },
    ],
  },
];

/** Every branch off the main flow, attacks and variants alike. */
export const BRANCHES: Scenario[] = [...VARIANTS, ...SCENARIOS];

export const SCENARIO_BY_ID = Object.fromEntries(
  BRANCHES.map((s) => [s.id, s]),
) as Record<string, Scenario>;

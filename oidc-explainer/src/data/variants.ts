import { FIXTURES as F } from './flow';
import { SPECS } from './specs';
import type { Scenario } from './types';

/**
 * Legitimate alternative configurations, as opposed to the attacks in
 * scenarios.ts. Same branching machinery, different framing.
 */
export const VARIANTS: Scenario[] = [
  {
    id: 'bearer-introspection',
    label: 'Bearer token mode',
    kind: 'variant',
    short: "Hand out the IdP's own token and introspect it on every call",
    outcome:
      "The SPA receives the identity provider's access token instead of a Waldur one, and every later API call is validated against the provider rather than against a local token row.",
    guard: {
      title: 'The switch',
      text: "OIDC_ACCESS_TOKEN_ENABLED. With it on, the completion view wraps the IdP access token in the exchange code instead of Waldur's DRF token, and OIDCAuthentication takes over API authentication. It needs OIDC_INTROSPECTION_URL, OIDC_CLIENT_ID and OIDC_CLIENT_SECRET set, or every request is rejected.",
      code: [
        {
          repo: 'waldur-mastermind',
          path: 'src/waldur_core/server/constance_settings.py',
          symbol: 'OIDC_ACCESS_TOKEN_ENABLED',
        },
        {
          repo: 'waldur-mastermind',
          path: 'src/waldur_core/core/authentication.py',
          symbol: 'class OIDCAuthentication',
        },
      ],
    },
    // The Waldur token is still minted at step 12; it is simply not the one
    // handed out. Divergence starts with what the exchange code wraps.
    divergeAfter: 'waldur-token',
    steps: [
      {
        id: 'bearer-exchange',
        title: 'The exchange code wraps the IdP token, not the Waldur one',
        from: 'mastermind',
        to: 'db',
        channel: 'internal',
        credential: 'exchange_code',
        narration:
          "Same one-time code, different contents. TokenExchangeCode carries either a foreign key to a Waldur token row or a raw external token string, and resolve_token_key returns whichever is set. Note that refresh_token(user) still ran a step ago: the Waldur token exists, it is just not what gets handed out.",
        wire: {
          kind: 'internal',
          body: `if config.OIDC_ACCESS_TOKEN_ENABLED:
    exchange_code = TokenExchangeCode.generate_code(
        user=user, external_token=access_token   # <- the IdP's JWT
    )
else:
    exchange_code = TokenExchangeCode.generate_code(user=user, token=token)

# resolve_token_key():
#   return self.token.key if self.token_id else self.external_token`,
          note: 'external_token is a CharField capped at 500 characters, so a very large JWT will not fit.',
        },
        code: [
          {
            repo: 'waldur-mastermind',
            path: 'src/waldur_core/core/models.py',
            symbol: 'def resolve_token_key',
          },
          {
            repo: 'waldur-mastermind',
            path: 'src/waldur_auth_social/views.py',
            symbol: 'def _complete_login',
          },
        ],
        effects: [
          {
            actor: 'db',
            add: [
              {
                id: 'exchange-row',
                label: 'TokenExchangeCode',
                value: 'wraps external_token',
                credential: 'idp_token',
              },
            ],
          },
        ],
      },

      {
        id: 'bearer-redirect',
        title: 'Back to the SPA, carrying only the code',
        from: 'mastermind',
        to: 'spa',
        channel: 'front',
        credential: 'exchange_code',
        narration:
          'Unchanged from the default flow. The redirect destination is still checked against allowed_redirects, and the code is still what travels, not the token.',
        wire: {
          kind: 'redirect',
          status: '302 Found',
          url: `${F.portal}/oauth_login_completed/${F.provider}/?code=${F.exchangeCode}`,
        },
        code: [
          {
            repo: 'waldur-mastermind',
            path: 'src/waldur_auth_social/utils.py',
            symbol: 'def validate_and_get_redirect_url',
          },
        ],
      },

      {
        id: 'bearer-redeem',
        title: 'The SPA redeems the code and gets a JWT',
        from: 'spa',
        to: 'mastermind',
        channel: 'back',
        credential: 'idp_token',
        narration:
          "Same endpoint, same single-use semantics. What comes back is the identity provider's access token, so from here the SPA holds a credential Waldur did not issue and cannot revoke on its own.",
        wire: {
          kind: 'http',
          method: 'POST',
          url: `${F.api}/api-auth/token-exchange/`,
          body: `{ "code": "${F.exchangeCode}" }

-> 200 OK
{ "token": "${F.idpAccessToken}" }`,
          note: 'Logging out of Waldur deletes the Waldur token, which is not the credential in play here.',
        },
        code: [
          {
            repo: 'waldur-mastermind',
            path: 'src/waldur_core/core/views.py',
            symbol: 'class TokenExchangeView',
          },
        ],
        effects: [
          {
            actor: 'db',
            remove: ['exchange-row'],
          },
          {
            actor: 'spa',
            add: [
              {
                id: 'spa-token',
                label: 'IdP access token',
                value: `${F.idpAccessToken.slice(0, 16)}...`,
                credential: 'idp_token',
              },
            ],
          },
        ],
      },

      {
        id: 'bearer-call',
        title: 'An API call arrives as a bearer token',
        from: 'spa',
        to: 'mastermind',
        channel: 'back',
        credential: 'idp_token',
        narration:
          'The scheme is Bearer rather than Token, which is what routes the request to OIDCAuthentication. Waldur decodes the JWT only to read it: the signature is deliberately not verified here, because the introspection call in the next step is what establishes trust.',
        wire: {
          kind: 'http',
          method: 'GET',
          url: `${F.api}/api/users/me/`,
          headers: { Authorization: `Bearer ${F.idpAccessToken.slice(0, 16)}...` },
          body: `jwt.decode(raw_token, options={
    "verify_signature": False,   # payload is read, not trusted
    "verify_exp": True,          # an expired token is rejected outright
})`,
          note: 'ExpiredSignatureError becomes "Token has expired."; a malformed token becomes "Invalid JWT token."',
        },
        code: [
          {
            repo: 'waldur-mastermind',
            path: 'src/waldur_core/core/authentication.py',
            symbol: 'class OIDCAuthentication',
          },
        ],
      },

      {
        id: 'bearer-introspect',
        specs: [SPECS.introspectRequest, SPECS.introspectResponse, SPECS.introspectCaching],
        title: 'Back channel: is this token still active?',
        from: 'mastermind',
        to: 'idp',
        channel: 'back',
        credential: 'idp_token',
        narration:
          'This is the RFC 7662 introspection call, and it is where the token is actually trusted or rejected. Waldur authenticates to the endpoint with its own client credentials over HTTP Basic; anything other than a 200 with active true fails the request.',
        wire: {
          kind: 'http',
          method: 'POST',
          url: `${F.idp}/protocol/openid-connect/token/introspect`,
          headers: { Authorization: 'Basic <client_id:client_secret>' },
          body: `token=${F.idpAccessToken.slice(0, 16)}...

-> 200 OK
{
  "active": true,
  "username": "${F.username}",
  "sub": "${F.sub}",
  "exp": 1789000000
}`,
          note: 'Successful results are cached under oidc_token:<sha256 of the token> for OIDC_CACHE_TIMEOUT seconds (default 300). Only active tokens are cached, so a revoked token is not held open by the cache — but a token revoked at the provider stays usable until its cache entry expires.',
        },
        code: [
          {
            repo: 'waldur-mastermind',
            path: 'src/waldur_core/server/constance_settings.py',
            symbol: 'OIDC_INTROSPECTION_URL',
          },
          {
            repo: 'waldur-mastermind',
            path: 'src/waldur_core/core/authentication.py',
            symbol: 'class OIDCAuthentication',
          },
        ],
        effects: [
          {
            actor: 'mastermind',
            add: [
              {
                id: 'introspection-cache',
                label: 'Introspection cache',
                value: 'active, 300s',
                credential: 'idp_token',
              },
            ],
          },
        ],
      },

      {
        id: 'bearer-user',
        title: 'The token is resolved to a Waldur user',
        from: 'mastermind',
        to: 'db',
        channel: 'internal',
        credential: 'none',
        narration:
          'OIDC_USER_FIELD names which field of the introspection response identifies the user, and it is matched against User.username. A first-time identifier creates the account; a match against a pre-existing non-OIDC account is adopted rather than rejected, and that adoption is deliberately loud.',
        wire: {
          kind: 'internal',
          body: `user_identifier = data[config.OIDC_USER_FIELD]   # default "username"

User.all_objects.get_or_create(
    username=user_identifier,
    defaults={"registration_method": "oidc"},
)
# all_objects, so a deactivated account is found and rejected
# rather than hidden and re-created into a unique collision

if existing.registration_method != "oidc":
    _adopt_local_account(...)   # WARNING log + reversion snapshot`,
          note: 'Adoption keeps users working across an OIDC rollout, but it is also the shape of a username takeover, which is why every adoption records a revertible snapshot.',
        },
        code: [
          {
            repo: 'waldur-mastermind',
            path: 'src/waldur_core/core/authentication.py',
            symbol: 'def _get_or_provision_user',
          },
          {
            repo: 'waldur-mastermind',
            path: 'src/waldur_core/core/authentication.py',
            symbol: 'def _adopt_local_account',
          },
        ],
        effects: [
          {
            actor: 'db',
            add: [
              {
                id: 'user-row-oidc',
                label: 'User row',
                value: 'registration_method=oidc',
              },
            ],
          },
        ],
        callout: {
          tone: 'warning',
          text: 'A token whose username claim collides with an existing staff account will adopt that account. The WARNING log and the django-reversion snapshot are the audit trail; there is a dedicated regression test covering this.',
        },
      },
    ],
  },
];

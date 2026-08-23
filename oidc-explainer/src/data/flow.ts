import { SPECS } from './specs';
import type { Step } from './types';

/**
 * Fixture values. The PKCE pair is the RFC 7636 appendix B test vector and the
 * authorization code is the RFC 6749 example, so anyone checking the hash by
 * hand gets the documented answer.
 */
export const FIXTURES = {
  portal: 'https://portal.example.com',
  api: 'https://api.example.com',
  idp: 'https://keycloak.example.com/realms/waldur',
  provider: 'keycloak',
  state: 'nVQ2b7yZK1sLp0RmT9xGfA6hCwEuJ3dS',
  codeVerifier: 'dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk',
  codeChallenge: 'E9Melhoa2OwvFrEMTJguCHaoeK1t8URWbuGJSstw-cM',
  authCode: 'SplxlOBeZQQYbYS6WxSbIA',
  idpAccessToken: 'eyJhbGciOiJSUzI1NiIsImtpZCI6Ind2Nk...QssI2Zg',
  exchangeCode: '7f3d2b8c4e5a4f0192ab3c4d5e6f7a8b',
  waldurToken: '9a1c0f7e5b2d4c8a6f3e1b9d7c5a3f1e8d6b4a20',
  sub: 'c1f4a9e2-7b3d-4f61-9a08-2e5d6c7b8a91',
  username: 'j.tamm@example.org',
} as const;

const F = FIXTURES;

export const FLOW: Step[] = [
  {
    id: 'providers',
    title: 'The SPA asks which identity providers are enabled',
    from: 'spa',
    to: 'mastermind',
    channel: 'back',
    credential: 'none',
    narration:
      'Before anything auth-related happens, the login page fetches the list of identity providers and renders one button per provider. Only providers with is_active are returned to anonymous callers.',
    wire: {
      kind: 'http',
      method: 'GET',
      url: `${F.api}/api/identity-providers/`,
      status: '200 OK',
      body: `[
  {
    "provider": "keycloak",
    "label": "Example University",
    "auth_url": "${F.idp}/protocol/openid-connect/auth",
    "is_active": true
  }
]`,
      note: 'Secret fields (client_secret, user_claim, attribute_mapping, ...) are stripped from the serializer for non-staff callers.',
    },
    code: [
      {
        repo: 'waldur-mastermind',
        path: 'src/waldur_auth_social/views.py',
        symbol: 'class IdentityProvidersViewSet',
      },
      {
        repo: 'waldur-homeport',
        path: 'src/auth/OauthLoginButton.tsx',
        symbol: 'OauthLoginButton',
      },
    ],
    effects: [
      {
        actor: 'spa',
        add: [
          {
            id: 'provider-list',
            label: 'Provider list',
            value: '1 active provider',
          },
        ],
      },
    ],
  },

  {
    id: 'init-nav',
    title: 'Clicking the button navigates the whole page away',
    from: 'user',
    to: 'mastermind',
    channel: 'front',
    credential: 'none',
    narration:
      'This is a top-level browser navigation (window.location.href), not an XHR. It has to be: the flow is about to hand control to a different origin, and only the browser itself can carry the user there and back.',
    wire: {
      kind: 'http',
      method: 'GET',
      url: `${F.api}/api-auth/${F.provider}/init/?return_url=${encodeURIComponent(
        F.portal,
      )}&ui_locales=en`,
      headers: { Referer: `${F.portal}/login` },
    },
    code: [
      {
        repo: 'waldur-homeport',
        path: 'src/auth/utils.ts',
        symbol: 'getOauthURL',
      },
    ],
    callout: {
      tone: 'insight',
      text: 'return_url is where the flow will land once it comes back. OAuthViewInit takes it over the Referer header, and only falls back to the header when the parameter is absent — which is what happens for any client that is not Homeport. Either way the value is an origin, and it has to be one the provider already allows.',
    },
  },

  {
    id: 'mint-state',
    specs: [SPECS.pkceChallenge, SPECS.pkceVector],
    title: 'Mastermind flushes the session and mints its secrets',
    from: 'mastermind',
    to: 'mastermind',
    channel: 'internal',
    credential: 'pkce',
    narration:
      'The old session is flushed first, so a fresh session key is issued and a concurrent request cannot overwrite the state that is about to be written. Then a random state and, if the provider has PKCE enabled, a code_verifier are generated and stored server-side.',
    wire: {
      kind: 'internal',
      body: `session.flush()
session["oidc_state"]         = "${F.state}"
session["oidc_code_verifier"] = "${F.codeVerifier}"
session["oidc_return_url"]    = "${F.portal}"

code_challenge = b64url(sha256(code_verifier))
               = "${F.codeChallenge}"`,
      note: 'The verifier never leaves the server. Only its hash is sent to the IdP.',
    },
    code: [
      {
        repo: 'waldur-mastermind',
        path: 'src/waldur_auth_social/views.py',
        symbol: 'class OAuthViewInit',
      },
      {
        repo: 'waldur-mastermind',
        path: 'src/waldur_auth_social/views.py',
        symbol: 'def generate_code_challenge',
      },
    ],
    effects: [
      {
        actor: 'mastermind',
        add: [
          { id: 'state', label: 'state', value: F.state, credential: 'pkce' },
          {
            id: 'verifier',
            label: 'code_verifier',
            value: F.codeVerifier,
            credential: 'pkce',
          },
          { id: 'return-url', label: 'return_url', value: F.portal },
        ],
      },
    ],
    callout: {
      tone: 'warning',
      text: 'PKCE is opt-in per provider: IdentityProvider.enable_pkce defaults to False. A provider configured without it runs the flow with no code_verifier at all.',
    },
  },

  {
    id: 'authorize',
    specs: [SPECS.authRequest, SPECS.stateCsrf],
    title: 'Redirect to the authorization endpoint',
    from: 'mastermind',
    to: 'idp',
    channel: 'front',
    credential: 'pkce',
    narration:
      'Mastermind answers with a 302. The browser carries the authorization request to the IdP, which is why every parameter here is public: anyone watching the address bar sees them.',
    wire: {
      kind: 'redirect',
      status: '302 Found',
      url: `${F.idp}/protocol/openid-connect/auth`,
      body: `response_type       = code
client_id           = waldur-portal
redirect_uri        = ${F.api}/api-auth/${F.provider}/complete/
scope               = openid profile email
state               = ${F.state}
code_challenge      = ${F.codeChallenge}
code_challenge_method = S256
ui_locales          = en`,
      note: 'redirect_uri is built with reverse(), so it always points back at Mastermind and never at whatever the caller asked for.',
    },
    code: [
      {
        repo: 'waldur-mastermind',
        path: 'src/waldur_auth_social/views.py',
        symbol: 'class OAuthViewInit',
      },
    ],
    effects: [
      {
        actor: 'idp',
        add: [
          {
            id: 'pending-auth',
            label: 'Pending authorization',
            value: `challenge ${F.codeChallenge.slice(0, 12)}...`,
            credential: 'pkce',
          },
        ],
      },
    ],
  },

  {
    id: 'authenticate',
    title: 'The user authenticates at the identity provider',
    from: 'user',
    to: 'idp',
    channel: 'front',
    credential: 'none',
    narration:
      'Everything in this step is outside Waldur. Password, MFA, an upstream federation hop, a consent screen: Waldur sees none of it and never receives the password. This is the entire point of delegating authentication.',
    wire: {
      kind: 'internal',
      body: `The IdP does whatever it does:
  - username + password, or
  - passkey / MFA, or
  - another SAML or OIDC hop upstream (eduGAIN, ...)
  - optionally a consent screen for the requested scopes

Waldur is not involved and never sees the credentials.`,
    },
    code: [],
    callout: {
      tone: 'insight',
      text: 'This is why adding a new login method is usually an IdP configuration change, not a Waldur change.',
    },
  },

  {
    id: 'callback',
    specs: [SPECS.authResponse],
    title: 'The IdP redirects back with a code, through the browser',
    from: 'idp',
    to: 'mastermind',
    channel: 'front',
    credential: 'authcode',
    narration:
      'The authorization code arrives on the front channel, in a URL. That is safe only because the code is single-use, short-lived, and cannot be redeemed without the client secret (and the PKCE verifier).',
    wire: {
      kind: 'redirect',
      status: '302 Found',
      url: `${F.api}/api-auth/${F.provider}/complete/?code=${F.authCode}&state=${F.state}`,
      note: 'Both values are visible in the address bar, in browser history, and in any proxy log along the way.',
    },
    code: [
      {
        repo: 'waldur-mastermind',
        path: 'src/waldur_auth_social/views.py',
        symbol: 'class OAuthViewComplete',
      },
    ],
    effects: [
      {
        actor: 'idp',
        remove: ['pending-auth'],
      },
    ],
  },

  {
    id: 'check-state',
    specs: [SPECS.stateCsrf],
    title: 'The returned state is compared with the session',
    from: 'mastermind',
    to: 'mastermind',
    channel: 'internal',
    credential: 'pkce',
    narration:
      'If the state in the URL does not match the state in the session, the request is rejected outright. This is what stops an attacker from feeding their own authorization code into your browser.',
    wire: {
      kind: 'internal',
      body: `stored_state   = session["oidc_state"]   # ${F.state}
returned_state = request.GET["state"]     # ${F.state}

if not stored_state or stored_state != returned_state:
    logger.warning("Invalid auth state for provider %s", provider)
    raise OAuthException(provider, "Invalid auth state.")`,
    },
    code: [
      {
        repo: 'waldur-mastermind',
        path: 'src/waldur_auth_social/views.py',
        symbol: 'def _complete_login',
      },
    ],
  },

  {
    id: 'token',
    specs: [SPECS.tokenRequest, SPECS.pkceTokenRequest],
    title: 'Back channel: redeem the code for an access token',
    from: 'mastermind',
    to: 'idp',
    channel: 'back',
    credential: 'authcode',
    narration:
      'Now the flow leaves the browser entirely. Mastermind calls the token endpoint directly over TLS, presenting the code, its client credentials and the PKCE verifier it kept in the session.',
    wire: {
      kind: 'http',
      method: 'POST',
      url: `${F.idp}/protocol/openid-connect/token`,
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body: `grant_type    = authorization_code
code          = ${F.authCode}
redirect_uri  = ${F.api}/api-auth/${F.provider}/complete/
code_verifier = ${F.codeVerifier}
client_id     = waldur-portal
client_secret = ********`,
      note: 'TARA is the exception: it authenticates with HTTP Basic instead of posting the client secret in the body.',
    },
    code: [
      {
        repo: 'waldur-mastermind',
        path: 'src/waldur_auth_social/views.py',
        symbol: 'def get_token_data',
      },
    ],
  },

  {
    id: 'token-response',
    specs: [SPECS.pkceServerVerify, SPECS.idTokenValidation],
    title: 'The IdP returns its tokens',
    from: 'idp',
    to: 'mastermind',
    channel: 'back',
    credential: 'idp_token',
    narration:
      'The IdP verifies that sha256(code_verifier) equals the challenge it stored at step 4, then issues tokens. Waldur reads access_token and refresh_token and ignores everything else.',
    wire: {
      kind: 'http',
      status: '200 OK',
      body: `{
  "access_token": "${F.idpAccessToken}",
  "refresh_token": "eyJhbGciOiJIUzUxMiIs...Vd8",
  "expires_in": 300,
  "token_type": "Bearer",
  "id_token": "eyJhbGciOiJSUzI1NiIs...ignored"
}`,
    },
    code: [
      {
        repo: 'waldur-mastermind',
        path: 'src/waldur_auth_social/views.py',
        symbol: 'def authenticate_user',
      },
    ],
    effects: [
      {
        actor: 'mastermind',
        add: [
          {
            id: 'idp-token',
            label: 'IdP access token',
            value: `${F.idpAccessToken.slice(0, 18)}...`,
            credential: 'idp_token',
          },
        ],
      },
    ],
    callout: {
      tone: 'insight',
      text: 'Waldur ignores id_token and never sends a nonce; neither appears anywhere in the codebase. That is permitted rather than sloppy: nonce is OPTIONAL in the authorization code flow, and OIDC Core 3.1.3.7 lets TLS server validation stand in for checking the ID token signature when the token comes straight from the token endpoint. Waldur leans on that and reads claims from userinfo instead.',
    },
  },

  {
    id: 'userinfo',
    specs: [SPECS.userinfo],
    title: 'Back channel: read the claims from the userinfo endpoint',
    from: 'mastermind',
    to: 'idp',
    channel: 'back',
    credential: 'idp_token',
    narration:
      'Mastermind presents the access token as a bearer token and gets the claims back as plain JSON. Because this is a direct TLS call to a known endpoint, there is no signature to check.',
    wire: {
      kind: 'http',
      method: 'GET',
      url: `${F.idp}/protocol/openid-connect/userinfo`,
      headers: { Authorization: `Bearer ${F.idpAccessToken.slice(0, 18)}...` },
      status: '200 OK',
      body: `{
  "sub": "${F.sub}",
  "preferred_username": "${F.username}",
  "given_name": "Jaan",
  "family_name": "Tamm",
  "email": "${F.username}",
  "schac_home_organization": "example.org",
  "eduperson_assurance": ["https://refeds.org/assurance/IAP/low"]
}`,
    },
    code: [
      {
        repo: 'waldur-mastermind',
        path: 'src/waldur_auth_social/views.py',
        symbol: 'def get_user_info',
      },
    ],
  },

  {
    id: 'map-user',
    title: 'Claims become a Waldur user',
    from: 'mastermind',
    to: 'db',
    channel: 'internal',
    credential: 'none',
    narration:
      'The provider configuration decides which claim identifies the user (user_claim) and which User field to match it against (user_field). Everything else is copied across by attribute_mapping. If no user matches, one is created on the spot: just-in-time provisioning.',
    wire: {
      kind: 'internal',
      body: `# from IdentityProvider, keycloak defaults
user_field = "username"     <- which User column to look up
user_claim = "sub"          <- which claim holds the value

attribute_mapping = {
  "email":        "email",
  "first_name":   "given_name",
  "last_name":    "family_name",
  "organization": "schac_home_organization affiliation org",
}

User.all_objects.get(username="${F.sub}")  -> DoesNotExist
    -> create user, registration_method="keycloak"

# all_objects, not objects: a deactivated account must be found and
# rejected rather than hidden by the active-only default manager and
# then re-created into a unique-username collision.`,
      note: 'A mapping value can list several claims separated by spaces; the first one present wins.',
    },
    code: [
      {
        repo: 'waldur-mastermind',
        path: 'src/waldur_auth_social/utils.py',
        symbol: 'def create_or_update_oauth_user',
      },
      {
        repo: 'waldur-mastermind',
        path: 'src/waldur_auth_social/const.py',
        symbol: 'PROVIDER_DEFAULTS',
      },
    ],
    effects: [
      {
        actor: 'db',
        add: [
          {
            id: 'user-row',
            label: 'User row',
            value: `${F.username} (created)`,
          },
          {
            id: 'oauth-token-row',
            label: 'OAuthToken row',
            value: 'access + refresh stored',
            credential: 'idp_token',
          },
        ],
      },
    ],
    callout: {
      tone: 'warning',
      text: 'Two Constance settings change this step materially: OIDC_MATCHMAKING_BY_EMAIL falls back to matching on email, and OIDC_BLOCK_CREATION_OF_UNINVITED_USERS refuses to create a user without a matching invitation.',
    },
  },

  {
    id: 'waldur-token',
    title: 'Mastermind mints its own API token',
    from: 'mastermind',
    to: 'db',
    channel: 'internal',
    credential: 'waldur_token',
    narration:
      "From here on the IdP is out of the picture. Waldur issues a DRF token of its own, and that is what authorises API calls. The IdP's token is kept only for later reads, not for API authentication.",
    wire: {
      kind: 'internal',
      body: `token = refresh_token(user)      # get_or_create, rotate if expired
user.last_login = now()
set_authentication_method(request, "${F.provider}")

token.key = "${F.waldurToken}"`,
      note: 'Unless OIDC_ACCESS_TOKEN_ENABLED is on, in which case the IdP access token is handed out instead and every API call is verified by introspection.',
    },
    code: [
      {
        repo: 'waldur-mastermind',
        path: 'src/waldur_core/core/authentication.py',
        symbol: 'def refresh_token',
      },
    ],
    effects: [
      {
        actor: 'db',
        add: [
          {
            id: 'waldur-token-row',
            label: 'Token row',
            value: `${F.waldurToken.slice(0, 12)}...`,
            credential: 'waldur_token',
          },
        ],
      },
    ],
  },

  {
    id: 'exchange-code',
    title: 'A one-time code stands in for the token',
    from: 'mastermind',
    to: 'db',
    channel: 'internal',
    credential: 'exchange_code',
    narration:
      'The SPA needs that token, but the only way back to the SPA is a redirect, and a redirect means a URL. Putting the real token in a URL would leak it into history, logs and Referer headers, so Waldur puts a 10-second single-use code there instead.',
    wire: {
      kind: 'internal',
      body: `exchange_code = TokenExchangeCode.generate_code(user=user, token=token)
exchange_code.uuid.hex = "${F.exchangeCode}"

redirect_base = validate_and_get_redirect_url(
    config, referrer=None, return_url="${F.portal}"
)   # must match IdentityProvider.allowed_redirects`,
      note: 'TOKEN_EXCHANGE_TTL is 10 seconds.',
    },
    code: [
      {
        repo: 'waldur-mastermind',
        path: 'src/waldur_core/core/models.py',
        symbol: 'class TokenExchangeCode',
      },
      {
        repo: 'waldur-mastermind',
        path: 'src/waldur_auth_social/utils.py',
        symbol: 'def validate_and_get_redirect_url',
      },
    ],
    effects: [
      {
        actor: 'db',
        add: [
          {
            id: 'exchange-row',
            label: 'TokenExchangeCode',
            value: `${F.exchangeCode.slice(0, 12)}... (10s)`,
            credential: 'exchange_code',
          },
        ],
      },
    ],
  },

  {
    id: 'redirect-spa',
    title: 'Back to the SPA, carrying only the code',
    from: 'mastermind',
    to: 'spa',
    channel: 'front',
    credential: 'exchange_code',
    narration:
      'The last front-channel hop. The destination was validated against the allowed_redirects allowlist, so an attacker cannot steer this redirect at a host of their choosing.',
    wire: {
      kind: 'redirect',
      status: '302 Found',
      url: `${F.portal}/oauth_login_completed/${F.provider}/?code=${F.exchangeCode}`,
    },
    code: [
      {
        repo: 'waldur-mastermind',
        path: 'src/waldur_auth_social/views.py',
        symbol: 'def _complete_login',
      },
      {
        repo: 'waldur-homeport',
        path: 'src/auth/callbacks/routes.ts',
        symbol: 'home.oauth_login_completed',
      },
    ],
  },

  {
    id: 'redeem',
    title: 'The SPA redeems the code for the real token',
    from: 'spa',
    to: 'mastermind',
    channel: 'back',
    credential: 'waldur_token',
    narration:
      'An ordinary XHR, so the token comes back in a response body rather than a URL. The row is locked, checked for freshness and deleted inside one transaction, which is what makes the code genuinely single-use under concurrency.',
    wire: {
      kind: 'http',
      method: 'POST',
      url: `${F.api}/api-auth/token-exchange/`,
      body: `{ "code": "${F.exchangeCode}" }

-> 200 OK
{ "token": "${F.waldurToken}" }`,
      note: 'select_for_update, then resolve, then delete: a second redemption finds nothing and gets a 400.',
    },
    code: [
      {
        repo: 'waldur-homeport',
        path: 'src/auth/callbacks/OauthLoginCompleted.tsx',
        symbol: 'OauthLoginCompleted',
      },
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
            label: 'Waldur API token',
            value: `${F.waldurToken.slice(0, 12)}...`,
            credential: 'waldur_token',
          },
        ],
      },
    ],
  },

  {
    id: 'authenticated',
    title: 'Every later call carries the Waldur token',
    from: 'spa',
    to: 'mastermind',
    channel: 'back',
    credential: 'waldur_token',
    narration:
      'The login is over. From here the SPA is an ordinary API client holding a DRF token, and nothing it does touches the identity provider again until logout.',
    wire: {
      kind: 'http',
      method: 'GET',
      url: `${F.api}/api/users/me/`,
      headers: { Authorization: `Token ${F.waldurToken.slice(0, 12)}...` },
      status: '200 OK',
      body: `{
  "username": "${F.username}",
  "full_name": "Jaan Tamm",
  "registration_method": "${F.provider}"
}`,
    },
    code: [
      {
        repo: 'waldur-homeport',
        path: 'packages/auth-core/src/authService.ts',
        symbol: 'export async function loginUser',
      },
      {
        repo: 'waldur-mastermind',
        path: 'src/waldur_core/core/authentication.py',
        symbol: 'class ImpersonationAuthentication',
        label: 'ImpersonationAuthentication (the DRF token backend)',
      },
    ],
  },
];

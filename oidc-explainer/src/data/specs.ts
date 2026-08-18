import type { SpecRef } from './types';

/**
 * Normative references, each verified against the published text.
 *
 * Deliberately narrow: only RFC 6749, RFC 7636, RFC 7662 and OpenID Connect
 * Core 1.0 are cited, because those are the four documents whose wording was
 * actually checked. Nothing here is cited from memory.
 */
export const SPECS = {
  pkceVector: {
    label: 'RFC 7636 - Appendix B',
    note: 'The verifier/challenge pair used here is the spec’s own test vector, so the hash can be checked by hand.',
    url: 'https://www.rfc-editor.org/rfc/rfc7636#appendix-B',
  },
  pkceChallenge: {
    label: 'RFC 7636 - 4.2',
    note: 'code_challenge = BASE64URL-ENCODE(SHA256(ASCII(code_verifier))); the verifier is 43 to 128 characters.',
    url: 'https://www.rfc-editor.org/rfc/rfc7636#section-4.2',
  },
  pkceTokenRequest: {
    label: 'RFC 7636 - 4.5',
    note: 'The client sends the authorization code together with the code_verifier to the token endpoint.',
    url: 'https://www.rfc-editor.org/rfc/rfc7636#section-4.5',
  },
  pkceServerVerify: {
    label: 'RFC 7636 - 4.6',
    note: 'The server transforms the received code_verifier and compares it with the challenge it stored before returning tokens.',
    url: 'https://www.rfc-editor.org/rfc/rfc7636#section-4.6',
  },
  authRequest: {
    label: 'OpenID Connect Core 1.0 - 3.1.2.1',
    note: 'The openid scope value is REQUIRED; without it the behaviour is entirely unspecified.',
    url: 'https://openid.net/specs/openid-connect-core-1_0.html#AuthRequest',
  },
  stateCsrf: {
    label: 'RFC 6749 - 10.12',
    note: 'state SHOULD be used to prevent cross-site request forgery on the redirect back.',
    url: 'https://www.rfc-editor.org/rfc/rfc6749#section-10.12',
  },
  authResponse: {
    label: 'RFC 6749 - 4.1.2',
    note: 'The authorization response returns code and the state it was given.',
    url: 'https://www.rfc-editor.org/rfc/rfc6749#section-4.1.2',
  },
  tokenRequest: {
    label: 'RFC 6749 - 4.1.3',
    note: 'grant_type=authorization_code, plus code and the identical redirect_uri.',
    url: 'https://www.rfc-editor.org/rfc/rfc6749#section-4.1.3',
  },
  idTokenValidation: {
    label: 'OpenID Connect Core 1.0 - 3.1.3.7',
    note: 'When the ID token arrives directly from the token endpoint, TLS server validation MAY stand in for checking its signature.',
    url: 'https://openid.net/specs/openid-connect-core-1_0.html#IDTokenValidation',
  },
  userinfo: {
    label: 'OpenID Connect Core 1.0 - 5.3',
    note: 'The UserInfo endpoint returns claims about the end user when presented with the access token.',
    url: 'https://openid.net/specs/openid-connect-core-1_0.html#UserInfo',
  },
  introspectRequest: {
    label: 'RFC 7662 - 2.1',
    note: 'HTTP POST with a token parameter; the endpoint MUST require authorization, such as client authentication.',
    url: 'https://www.rfc-editor.org/rfc/rfc7662#section-2.1',
  },
  introspectResponse: {
    label: 'RFC 7662 - 2.2',
    note: 'active is the required boolean: issued by this server, not revoked, and inside its validity window.',
    url: 'https://www.rfc-editor.org/rfc/rfc7662#section-2.2',
  },
  introspectCaching: {
    label: 'RFC 7662 - 2.2',
    note: 'The response MAY be cached "to improve performance and reduce load on the introspection endpoint, but at the cost of liveness of the information used by the protected resource to make authorization decisions".',
    url: 'https://www.rfc-editor.org/rfc/rfc7662#section-2.2',
  },
} satisfies Record<string, SpecRef>;

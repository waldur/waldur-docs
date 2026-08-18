import type { CredentialId } from './types';

export interface Credential {
  id: CredentialId;
  label: string;
  color: string;
  /** Shown in the legend; explains what this thing actually authorises. */
  blurb: string;
}

export const CREDENTIALS: Credential[] = [
  {
    id: 'none',
    label: 'No credential',
    color: '#94a3b8',
    blurb: 'A plain request that carries nothing secret.',
  },
  {
    id: 'pkce',
    label: 'PKCE verifier / challenge',
    color: '#22d3ee',
    blurb:
      'A random secret Mastermind keeps in its own session, plus its SHA-256 hash sent to the IdP. Proves at the end that the same party that started the flow is finishing it.',
  },
  {
    id: 'authcode',
    label: 'Authorization code',
    color: '#f472b6',
    blurb:
      'Single-use, short-lived, and useless on its own: redeeming it needs the client secret and the PKCE verifier.',
  },
  {
    id: 'idp_token',
    label: 'IdP access token',
    color: '#fb923c',
    blurb:
      "The identity provider's own token. Mastermind uses it to read claims, then stores it on the OAuthToken row.",
  },
  {
    id: 'exchange_code',
    label: 'Token exchange code',
    color: '#c084fc',
    blurb:
      "A Waldur-invented one-time code, valid 10 seconds, that exists purely so the real token never rides in a URL.",
  },
  {
    id: 'waldur_token',
    label: 'Waldur API token',
    color: '#4ade80',
    blurb:
      'A DRF token. This is what the SPA actually sends on every subsequent API call.',
  },
];

export const CREDENTIAL_BY_ID = Object.fromEntries(
  CREDENTIALS.map((c) => [c.id, c]),
) as Record<CredentialId, Credential>;

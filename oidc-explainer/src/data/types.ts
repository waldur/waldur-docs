/**
 * The whole explainer is data-driven: the renderer knows nothing about OIDC,
 * it just plays the steps below. A change in the Waldur auth flow should be a
 * change to `flow.ts` / `scenarios.ts`, never to the scene or panel code.
 */

export type ActorId = 'user' | 'spa' | 'mastermind' | 'idp' | 'db';

/**
 * Front channel  - travels through the user's browser as a redirect, so it is
 *                  visible to anything sitting in the browser or the address bar.
 * Back channel   - direct server-to-server call over TLS, never touches the browser.
 * Internal       - work an actor does to itself (minting, hashing, DB writes).
 */
export type Channel = 'front' | 'back' | 'internal';

/**
 * Three separate credentials exist in a single Waldur login, and confusing them
 * is the most common source of misunderstanding. They are colour-coded
 * consistently everywhere in the app.
 */
export type CredentialId =
  | 'none'
  | 'pkce'
  | 'authcode'
  | 'idp_token'
  | 'exchange_code'
  | 'waldur_token';

export type RepoId = 'waldur-mastermind' | 'waldur-homeport';

export interface CodeRef {
  repo: RepoId;
  /** Path inside the repo, used verbatim by scripts/check-code-refs.mjs. */
  path: string;
  /** Symbol expected to exist in that file. The CI check greps for it. */
  symbol: string;
  /** Optional human label; defaults to the symbol. */
  label?: string;
}

/**
 * A pointer into the normative spec. Every one of these was checked against the
 * published RFC / OIDC text rather than written from memory; the PKCE vector in
 * flow.ts is additionally verified by recomputing the SHA-256.
 */
export interface SpecRef {
  /** e.g. "RFC 7636 - Appendix B" */
  label: string;
  /** What that section actually says, compressed to a line. */
  note: string;
  url: string;
}

export interface Wire {
  kind: 'http' | 'redirect' | 'internal';
  method?: string;
  url?: string;
  status?: string;
  headers?: Record<string, string>;
  body?: string;
  /** Rendered under the payload in a quieter style. */
  note?: string;
}

export interface Holding {
  id: string;
  label: string;
  value: string;
  credential?: CredentialId;
}

export interface Effect {
  actor: ActorId;
  add?: Holding[];
  /** Holding ids to drop. */
  remove?: string[];
}

export interface Callout {
  tone: 'insight' | 'warning';
  text: string;
}

export interface Step {
  id: string;
  title: string;
  from: ActorId;
  to: ActorId;
  channel: Channel;
  credential: CredentialId;
  /** One or two sentences. Shown in the panel and in the text-only view. */
  narration: string;
  wire: Wire;
  code: CodeRef[];
  specs?: SpecRef[];
  effects?: Effect[];
  callout?: Callout;
}

/**
 * A branch off the main flow. Two kinds share the machinery:
 *
 *   attack  - the flow with one guard removed, to show why the guard is there
 *   variant - a legitimate alternative configuration Waldur really supports
 *
 * Both diverge after a shared step and then run their own steps.
 */
export interface Scenario {
  id: string;
  label: string;
  kind: 'attack' | 'variant';
  /** One line, shown on the toggle itself. */
  short: string;
  /** attack: what an attacker gets. variant: what is different about it. */
  outcome: string;
  /** attack: the guard that normally prevents it. variant: the switch that turns it on. */
  guard: {
    title: string;
    text: string;
    code: CodeRef[];
  };
  /** Id of the last shared step; the branch continues from there. */
  divergeAfter: string;
  steps: Step[];
}

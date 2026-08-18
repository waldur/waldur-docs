import type { ActorId } from './types';

export interface Actor {
  id: ActorId;
  name: string;
  subtitle: string;
  /** Scene position, in world units. */
  position: [number, number, number];
  color: string;
  /** Trust boundary the actor sits in; drawn as a ground plate. */
  zone: 'client' | 'waldur' | 'idp';
  /**
   * Which way the holdings badges hang. No two actors sharing a column may
   * hang the same way, or the badges collide.
   */
  holdings: 'above' | 'below';
}

/**
 * The SPA is deliberately docked to the browser rather than given its own
 * column: it *runs inside* the browser, which is exactly why step 2 is a
 * full-page navigation and not an XHR.
 */
export const ACTORS: Actor[] = [
  {
    id: 'user',
    name: "User's browser",
    subtitle: 'Carries redirects; sees every URL',
    position: [-7.4, -1.4, 0],
    color: '#7dd3fc',
    zone: 'client',
    holdings: 'below',
  },
  {
    id: 'spa',
    name: 'Homeport SPA',
    subtitle: 'Runs inside the browser; holds no secret',
    position: [-7.4, 2.9, 0],
    color: '#38bdf8',
    zone: 'client',
    holdings: 'above',
  },
  {
    id: 'mastermind',
    name: 'Mastermind',
    subtitle: 'The OIDC client; holds the client secret',
    position: [0, 1.4, 0],
    color: '#a3e635',
    zone: 'waldur',
    holdings: 'above',
  },
  {
    id: 'db',
    name: 'PostgreSQL',
    subtitle: 'Users, tokens, OIDC session state',
    position: [0, -3.0, 0],
    color: '#86efac',
    zone: 'waldur',
    holdings: 'below',
  },
  {
    id: 'idp',
    name: 'Identity provider',
    subtitle: 'Authenticates the user; issues tokens',
    position: [7.4, 1.4, 0],
    color: '#fbbf24',
    zone: 'idp',
    holdings: 'above',
  },
];

export const ACTOR_BY_ID = Object.fromEntries(
  ACTORS.map((a) => [a.id, a]),
) as Record<ActorId, Actor>;

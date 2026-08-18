import type { ActorId, Step } from './types';

/** Actors that live inside the user's browser. */
const BROWSER_SIDE: ActorId[] = ['user', 'spa'];

export const isBrowserSide = (id: ActorId) => BROWSER_SIDE.includes(id);

/**
 * How a hop is described depends on who is at each end, not only on its channel.
 *
 * "Back channel: direct server to server" was being shown on Homeport SPA ->
 * Mastermind hops, which contradicted the page's own actor subtitle ("runs
 * inside the browser"). In OAuth terms a public SPA has no back channel at all;
 * the distinction that matters to a reader is redirect versus direct call:
 * a redirect puts its parameters in a URL, a direct call does not, regardless
 * of whether it starts in a browser or on a server.
 */
export function channelLabel(step: Step): string {
  if (step.channel === 'front') {
    return 'Front channel: a redirect through the browser, so every parameter is visible in the address bar';
  }
  if (step.channel === 'internal') {
    return step.from === step.to
      ? 'Internal: work an actor does to itself, no network hop'
      : 'Internal: stays inside the Waldur trust boundary';
  }
  return isBrowserSide(step.from) || isBrowserSide(step.to)
    ? 'Direct call: an ordinary request from the browser, not a redirect, so nothing lands in a URL'
    : 'Back channel: direct server to server, never touches the browser';
}

/** Short form, for the linear text view. */
export function channelShort(step: Step): string {
  if (step.channel === 'front') return 'front channel, a redirect through the browser';
  if (step.channel === 'internal') {
    return step.from === step.to
      ? 'internal, no network hop'
      : 'internal, inside the Waldur trust boundary';
  }
  return isBrowserSide(step.from) || isBrowserSide(step.to)
    ? 'direct call from the browser, not a redirect'
    : 'back channel, server to server';
}

/** Drives the colour of the channel chip. */
export function channelKind(step: Step): 'front' | 'back' | 'direct' | 'internal' {
  if (step.channel !== 'back') return step.channel;
  return isBrowserSide(step.from) || isBrowserSide(step.to) ? 'direct' : 'back';
}

import { useEffect } from 'react';

import { hashFor, parseHash, stepsForMode } from './deepLink';
import { useStore } from './store';

/**
 * Keeps the address bar and the store in step.
 *
 * The store is seeded from the URL at creation (see deepLink.initialFromHash),
 * so there is nothing to apply on mount and no race to guard: this hook only
 * handles later hashchange events and mirrors store moves back out.
 */
export function useHashSync() {
  const mode = useStore((s) => s.mode);
  const index = useStore((s) => s.index);

  // Inbound: back/forward, or a pasted link in an already-open tab.
  useEffect(() => {
    const apply = () => {
      const parsed = parseHash(window.location.hash);
      if (!parsed) return;
      const state = useStore.getState();
      const clamped = Math.max(
        0,
        Math.min(parsed.index, stepsForMode(parsed.mode).length - 1),
      );
      if (state.mode !== parsed.mode) state.setMode(parsed.mode);
      state.goTo(clamped);
    };
    window.addEventListener('hashchange', apply);
    return () => window.removeEventListener('hashchange', apply);
  }, []);

  // Outbound: store -> address bar, without stacking history entries.
  useEffect(() => {
    const next = hashFor(mode, index);
    if (window.location.hash !== next) {
      window.history.replaceState(null, '', next);
    }
  }, [mode, index]);
}

import { create } from 'zustand';

import type { ActorId, Holding, Step } from './data/types';
import { initialFromHash, isBranchId, stepsForMode } from './deepLink';

export { isBranchId, stepsForMode };

export type Mode = 'flow' | string;

/** Steps actually played for a given mode: shared prefix + scenario tail. */
/** Cumulative actor holdings after playing `steps` up to and including `index`. */
export function holdingsAt(
  steps: Step[],
  index: number,
): Record<ActorId, Holding[]> {
  const acc: Record<ActorId, Holding[]> = {
    user: [],
    spa: [],
    mastermind: [],
    idp: [],
    db: [],
  };
  steps.slice(0, index + 1).forEach((step) => {
    step.effects?.forEach((effect) => {
      const current = acc[effect.actor];
      const kept = effect.remove
        ? current.filter((h) => !effect.remove!.includes(h.id))
        : current;
      const added = (effect.add ?? []).filter(
        (h) => !kept.some((k) => k.id === h.id),
      );
      acc[effect.actor] = [...kept, ...added];
    });
  });
  return acc;
}

interface ExplainerState {
  mode: Mode;
  index: number;
  playing: boolean;
  textOnly: boolean;
  steps: () => Step[];
  step: () => Step;
  setMode: (mode: Mode) => void;
  goTo: (index: number) => void;
  next: () => void;
  prev: () => void;
  setPlaying: (playing: boolean) => void;
  toggleTextOnly: () => void;
}

const initial = initialFromHash();

export const useStore = create<ExplainerState>((set, get) => ({
  // Seeded from the URL so a deep link is honoured on the very first render.
  mode: initial.mode,
  index: initial.index,
  playing: false,
  textOnly: false,

  steps: () => stepsForMode(get().mode),
  step: () => {
    const steps = stepsForMode(get().mode);
    return steps[Math.min(get().index, steps.length - 1)];
  },

  setMode: (mode) => set({ mode, index: 0, playing: false }),
  goTo: (index) => {
    const steps = stepsForMode(get().mode);
    set({ index: Math.max(0, Math.min(index, steps.length - 1)) });
  },
  next: () => {
    const { index, mode } = get();
    const steps = stepsForMode(mode);
    if (index >= steps.length - 1) set({ playing: false });
    else set({ index: index + 1 });
  },
  prev: () => set({ index: Math.max(0, get().index - 1), playing: false }),
  setPlaying: (playing) => set({ playing }),
  toggleTextOnly: () => set({ textOnly: !get().textOnly }),
}));

/** `prefers-reduced-motion` collapses every animation to a jump cut. */
export const prefersReducedMotion = () =>
  typeof window !== 'undefined' &&
  window.matchMedia?.('(prefers-reduced-motion: reduce)').matches;

export const hasWebGL = () => {
  if (typeof document === 'undefined') return false;
  try {
    const canvas = document.createElement('canvas');
    return Boolean(
      canvas.getContext('webgl2') ??
        canvas.getContext('webgl') ??
        canvas.getContext('experimental-webgl'),
    );
  } catch {
    return false;
  }
};

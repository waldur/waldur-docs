import { FLOW } from './data/flow';
import { SCENARIO_BY_ID } from './data/scenarios';
import type { Step } from './data/types';

/**
 * Deep-link parsing, kept free of any store import so the store can seed itself
 * from the URL at creation time. Reading the link in an effect instead created a
 * race: the outbound effect published the store's initial step 1 over the link
 * the visitor actually arrived on.
 */

/** Guards against inherited keys: "#/scenario/constructor/step/1" must not resolve. */
export function isBranchId(id: string): boolean {
  return Object.hasOwn(SCENARIO_BY_ID, id);
}

/** Steps actually played for a given mode: shared prefix + branch tail. */
export function stepsForMode(mode: string): Step[] {
  if (mode === 'flow' || !isBranchId(mode)) return FLOW;
  const branch = SCENARIO_BY_ID[mode];
  const cut = FLOW.findIndex((s) => s.id === branch.divergeAfter);
  const prefix = cut === -1 ? FLOW : FLOW.slice(0, cut + 1);
  return [...prefix, ...branch.steps];
}

export function parseHash(
  hash: string,
): { mode: string; index: number } | null {
  const flow = hash.match(/^#\/flow\/step\/(\d+)$/);
  if (flow) return { mode: 'flow', index: Number(flow[1]) - 1 };

  const branch = hash.match(/^#\/scenario\/([\w-]+)\/step\/(\d+)$/);
  if (branch && isBranchId(branch[1])) {
    return { mode: branch[1], index: Number(branch[2]) - 1 };
  }
  return null;
}

export function hashFor(mode: string, index: number): string {
  return mode === 'flow'
    ? `#/flow/step/${index + 1}`
    : `#/scenario/${mode}/step/${index + 1}`;
}

/** Initial store state, read straight from the address bar. */
export function initialFromHash(): { mode: string; index: number } {
  if (typeof window === 'undefined') return { mode: 'flow', index: 0 };
  const parsed = parseHash(window.location.hash);
  if (!parsed) return { mode: 'flow', index: 0 };
  const max = stepsForMode(parsed.mode).length - 1;
  return { mode: parsed.mode, index: Math.max(0, Math.min(parsed.index, max)) };
}

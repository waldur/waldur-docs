import { useThree } from '@react-three/fiber';

/**
 * drei's <Html distanceFactor> keeps an element at a constant *screen* size,
 * while the meshes around it shrink as the canvas gets smaller. Embedded in a
 * docs iframe that mismatch makes labels overflow their boxes badly.
 *
 * Scaling the factor by canvas height against the size it was tuned at keeps
 * labels locked to their boxes at any viewport.
 */
const REFERENCE_HEIGHT = 765;

export function useHtmlScale(base: number): number {
  const height = useThree((state) => state.size.height);
  return Math.max(base * (height / REFERENCE_HEIGHT), base * 0.45);
}

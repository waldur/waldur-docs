import * as THREE from 'three';

import { ACTOR_BY_ID } from '../data/actors';
import type { Step } from '../data/types';

const v = (p: [number, number, number]) => new THREE.Vector3(...p);

/**
 * The one visual idea the whole scene rests on:
 *
 *   front channel -> arcs forward (+z), through the browser, out where anyone
 *                    watching the address bar could read it
 *   back channel  -> dips backward (-z), server to server, out of the browser's
 *                    reach entirely
 *   internal      -> stays inside a trust boundary; a loop when an actor is
 *                    working on itself, otherwise drawn like a back-channel hop
 */
export function pathForStep(step: Step): THREE.Curve<THREE.Vector3> {
  const from = v(ACTOR_BY_ID[step.from].position);
  const to = v(ACTOR_BY_ID[step.to].position);

  // Only genuine self-work loops. An internal step between two actors (a DB
  // write, say) is still a hop and gets drawn as one.
  if (step.from === step.to) {
    const centre = from.clone().add(new THREE.Vector3(0, 0, 1.1));
    return new THREE.CatmullRomCurve3(
      [
        centre.clone().add(new THREE.Vector3(0.9, 0.5, 0)),
        centre.clone().add(new THREE.Vector3(0, 1.1, 0.5)),
        centre.clone().add(new THREE.Vector3(-0.9, 0.5, 0)),
        centre.clone().add(new THREE.Vector3(0, -0.1, 0.5)),
        centre.clone().add(new THREE.Vector3(0.9, 0.5, 0)),
      ],
      true,
    );
  }

  const mid = from.clone().lerp(to, 0.5);

  if (step.channel === 'front') {
    // Route through the browser, unless the browser is already an endpoint.
    const browser = v(ACTOR_BY_ID.user.position);
    const throughBrowser =
      step.from !== 'user' && step.to !== 'user' && step.from !== 'spa' && step.to !== 'spa';

    if (throughBrowser) {
      return new THREE.CatmullRomCurve3([
        from,
        from.clone().lerp(browser, 0.55).add(new THREE.Vector3(0, 2.2, 2.8)),
        browser.clone().add(new THREE.Vector3(0, 1.5, 2.4)),
        browser.clone().lerp(to, 0.45).add(new THREE.Vector3(0, 2.2, 2.8)),
        to,
      ]);
    }
    return new THREE.QuadraticBezierCurve3(
      from,
      mid.clone().add(new THREE.Vector3(0, 1.6, 2.8)),
      to,
    );
  }

  // Back channel: dips down and behind the stage, away from the browser.
  return new THREE.QuadraticBezierCurve3(
    from,
    mid.clone().add(new THREE.Vector3(0, -1.9, -2.2)),
    to,
  );
}

export function samplePath(
  curve: THREE.Curve<THREE.Vector3>,
  segments = 64,
): THREE.Vector3[] {
  return curve.getPoints(segments);
}

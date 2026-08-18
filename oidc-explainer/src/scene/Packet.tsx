import { useFrame } from '@react-three/fiber';
import { useMemo, useRef } from 'react';
import * as THREE from 'three';

import { CREDENTIAL_BY_ID } from '../data/credentials';
import type { Step } from '../data/types';
import { pathForStep } from './paths';

interface Props {
  step: Step;
  reducedMotion: boolean;
  /** Changes whenever the shown step changes, to restart the flight.
   *  Must include the branch: switching branch resets the index to 0, so an
   *  index-only key leaves the packet parked at the previous destination. */
  runKey: string;
}

const TRAVEL_SECONDS = 1.9;

export function Packet({ step, reducedMotion, runKey }: Props) {
  const curve = useMemo(() => pathForStep(step), [step]);
  const colour = CREDENTIAL_BY_ID[step.credential].color;

  const packet = useRef<THREE.Group>(null);
  const elapsed = useRef(0);
  const lastRun = useRef(runKey);

  useFrame((_, delta) => {
    if (!packet.current) return;
    if (lastRun.current !== runKey) {
      lastRun.current = runKey;
      elapsed.current = 0;
    }
    elapsed.current = Math.min(elapsed.current + delta, TRAVEL_SECONDS);

    // Reduced motion: park the packet at the destination instead of flying it.
    const t = reducedMotion
      ? 1
      : easeInOutCubic(elapsed.current / TRAVEL_SECONDS);
    const selfWork = step.from === step.to;
    const at = selfWork && !reducedMotion ? (elapsed.current / TRAVEL_SECONDS) % 1 : t;
    packet.current.position.copy(curve.getPointAt(Math.min(at, 1)));
  });

  return (
    <group>
      <group ref={packet}>
        <mesh>
          <icosahedronGeometry args={[0.28, 1]} />
          <meshStandardMaterial
            color={colour}
            emissive={colour}
            emissiveIntensity={1.1}
            roughness={0.3}
          />
        </mesh>
        <pointLight color={colour} intensity={6} distance={4} />
      </group>
    </group>
  );
}

function easeInOutCubic(x: number): number {
  return x < 0.5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2;
}

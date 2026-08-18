import { Html, RoundedBox } from '@react-three/drei';
import { useThree } from '@react-three/fiber';
import { useEffect, useRef } from 'react';
import type * as THREE from 'three';

import type { Actor } from '../data/actors';
import { CREDENTIAL_BY_ID } from '../data/credentials';
import type { Holding } from '../data/types';
import { useHtmlScale } from './useHtmlScale';

interface Props {
  actor: Actor;
  holdings: Holding[];
  active: boolean;
}

export function ActorNode({ actor, holdings, active }: Props) {
  const mesh = useRef<THREE.Mesh>(null);
  const material = useRef<THREE.MeshStandardMaterial>(null);
  const htmlScale = useHtmlScale(13);
  const canvasHeight = useThree((state) => state.size.height);

  // Nine badges accumulate over a full run. Showing them all at once buries the
  // scene, and most are irrelevant to the hop being explained, so only the two
  // actors in the current hop carry their contents. On a short canvas (the docs
  // iframe) the subtitles and badges go entirely - the panel has the detail.
  const compact = canvasHeight < 420;
  const showHoldings = active && !compact && holdings.length > 0;

  // Highlight is a state change, not motion: the emissive level is set
  // directly, with no pulse and no scaling. Breathing geometry made the stage
  // feel restless and competed with the packet, which is the only thing whose
  // movement carries meaning.
  useEffect(() => {
    if (material.current) {
      material.current.emissiveIntensity = active ? 0.8 : 0.12;
    }
  }, [active]);

  return (
    <group position={actor.position}>
      <RoundedBox ref={mesh} args={[2.5, 1.5, 1.1]} radius={0.16} smoothness={4}>
        <meshStandardMaterial
          ref={material}
          color={actor.color}
          emissive={actor.color}
          emissiveIntensity={0.12}
          roughness={0.45}
          metalness={0.15}
        />
      </RoundedBox>

      <Html center position={[0, 0, 0.62]} distanceFactor={htmlScale} zIndexRange={[10, 0]}>
        <div className={`actor-label${active ? ' is-active' : ''}`}>
          <strong>{actor.name}</strong>
          {!compact && <span>{actor.subtitle}</span>}
        </div>
      </Html>

      {showHoldings && (
        <Html
          center
          position={[0, actor.holdings === 'above' ? 1.05 : -1.05, 0.4]}
          distanceFactor={htmlScale}
          zIndexRange={[9, 0]}
        >
          {/*
            The anchor is deliberately zero-height: drei centres whatever it is
            given on the 3D point, so a zero-height box plus an absolutely
            positioned list makes the badges grow strictly away from the actor,
            whatever the count.
          */}
          <div className={`holdings-anchor is-${actor.holdings}`}>
          <ul className="holdings">
            {holdings.map((h) => (
              <li
                key={h.id}
                style={{
                  borderColor: h.credential
                    ? CREDENTIAL_BY_ID[h.credential].color
                    : undefined,
                }}
              >
                <em>{h.label}</em>
                <code>{h.value}</code>
              </li>
            ))}
          </ul>
          </div>
        </Html>
      )}
    </group>
  );
}

import { Html, Line } from '@react-three/drei';
import { useEffect, useMemo, useRef, useState } from 'react';
import * as THREE from 'three';

import { ACTOR_BY_ID } from '../data/actors';
import { CREDENTIAL_BY_ID } from '../data/credentials';
import type { Step } from '../data/types';
import { pathForStep, samplePath } from './paths';

export type HopTone = 'past' | 'current' | 'future';

interface Props {
  step: Step;
  index: number;
  tone: HopTone;
  onSelect: (index: number) => void;
}

const TONE = {
  past: { opacity: 0.22, width: 1.4 },
  current: { opacity: 0.85, width: 2.8 },
  future: { opacity: 0.18, width: 1.4 },
} as const;

/**
 * One hop, drawn and made interactive.
 *
 * The visible line is a drei <Line>, which is thin and unreliable to hit-test.
 * The clickable target is a separate invisible tube swept along the same curve,
 * which raycasts predictably at any zoom.
 */
export function HopLine({ step, index, tone, onSelect }: Props) {
  const [hovered, setHovered] = useState(false);

  // Two independent flags rather than one, because the ordering of the two
  // event systems is not guaranteed: moving from the line onto the card fires
  // the card's mouseenter BEFORE r3f's pointerout, so an open-then-close
  // sequence closed the card every time and made its "click to open"
  // unreachable. The delayed close re-reads both refs when it fires, so
  // whichever order the events arrive in, the result is the same.
  const overLine = useRef(false);
  const overCard = useRef(false);
  const timer = useRef<number>();

  const sync = () => {
    window.clearTimeout(timer.current);
    if (overLine.current || overCard.current) {
      setHovered(true);
      return;
    }
    // Grace period: the pointer crosses empty canvas between the line and the
    // card, which sits above it.
    timer.current = window.setTimeout(() => {
      if (!overLine.current && !overCard.current) setHovered(false);
    }, 220);
  };

  useEffect(() => () => window.clearTimeout(timer.current), []);

  const curve = useMemo(() => pathForStep(step), [step]);
  const points = useMemo(() => samplePath(curve), [curve]);
  const colour = CREDENTIAL_BY_ID[step.credential].color;
  const style = TONE[tone];

  // Lifted off the line so the card does not cover the actors it points at.
  const anchor = useMemo(
    () => curve.getPointAt(0.5).clone().add(new THREE.Vector3(0, 1.5, 0.6)),
    [curve],
  );

  // A preview, not the whole payload: the panel already carries that, and a
  // full body here blankets the stage on a small canvas.
  const preview = useMemo(() => {
    if (!step.wire.body) return null;
    const lines = step.wire.body.split('\n');
    return lines.length > 6
      ? { text: lines.slice(0, 6).join('\n'), more: lines.length - 6 }
      : { text: step.wire.body, more: 0 };
  }, [step.wire.body]);

  return (
    <group>
      <Line
        points={points}
        color={colour}
        lineWidth={hovered ? style.width + 1.6 : style.width}
        transparent
        opacity={hovered ? 1 : style.opacity}
        dashed={step.channel === 'front'}
        dashSize={0.28}
        gapSize={0.18}
      />

      {/* Invisible, generously sized hit target. */}
      <mesh
        onPointerOver={(e) => {
          e.stopPropagation();
          overLine.current = true;
          sync();
          document.body.style.cursor = 'pointer';
        }}
        onPointerOut={() => {
          overLine.current = false;
          sync();
          document.body.style.cursor = '';
        }}
        onClick={(e) => {
          e.stopPropagation();
          document.body.style.cursor = '';
          onSelect(index);
        }}
      >
        <tubeGeometry args={[curve as THREE.Curve<THREE.Vector3>, 48, 0.3, 6, false]} />
        <meshBasicMaterial transparent opacity={0} depthWrite={false} />
      </mesh>

      {hovered && (
        <Html
          center
          position={anchor}
          distanceFactor={12}
          zIndexRange={[30, 20]}
          // The card is interactive: it advertises "click to open", so it has to
          // honour a click on itself, not only on the line under it. Safe to
          // swallow pointer events here because clicking the card and clicking
          // the line do the same thing.
          style={{ pointerEvents: 'auto' }}
        >
          <div
            className="hop-tip"
            role="button"
            tabIndex={0}
            onMouseEnter={() => {
              overCard.current = true;
              sync();
            }}
            onMouseLeave={() => {
              overCard.current = false;
              sync();
            }}
            onClick={(e) => {
              e.stopPropagation();
              overCard.current = false;
              overLine.current = false;
              setHovered(false);
              onSelect(index);
            }}
            onKeyDown={(e) => {
              if (e.key !== 'Enter' && e.key !== ' ') return;
              e.preventDefault();
              e.stopPropagation();
              onSelect(index);
            }}
          >
            <p className="hop-tip-head">
              <span className="n">{index + 1}</span>
              {step.title}
            </p>
            <p className="hop-tip-hop">
              {ACTOR_BY_ID[step.from].name} &rarr; {ACTOR_BY_ID[step.to].name}
            </p>
            {(step.wire.method || step.wire.status) && (
              <p className="hop-tip-wire">
                <b>{step.wire.method ?? step.wire.status}</b>
                {step.wire.url && <span>{step.wire.url}</span>}
              </p>
            )}
            {preview && <pre>{preview.text}</pre>}
            {/* Always present: the card is clickable, so it must always say so.
                Previously a payload of six lines or fewer rendered no footer at
                all and the affordance simply vanished. */}
            <p className="hop-tip-more">
              {preview && preview.more > 0
                ? `+${preview.more} more lines - click to open`
                : 'Click to open'}
            </p>
          </div>
        </Html>
      )}
    </group>
  );
}

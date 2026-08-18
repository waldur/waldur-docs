import { Html } from '@react-three/drei';
import { Canvas } from '@react-three/fiber';
import { useMemo } from 'react';

import { ACTORS } from '../data/actors';
import type { ActorId, Holding, Step } from '../data/types';
import { ActorNode } from './ActorNode';
import { CameraRig } from './CameraRig';
import { HopLine } from './HopLine';
import { Packet } from './Packet';
import { useHtmlScale } from './useHtmlScale';

interface Props {
  steps: Step[];
  index: number;
  step: Step;
  holdings: Record<ActorId, Holding[]>;
  reducedMotion: boolean;
  runKey: string;
  onGoTo: (index: number) => void;
}

/** Trust boundaries, drawn as ground plates under the actors that sit in them. */
function ZoneLabel({ label }: { label: string }) {
  const scale = useHtmlScale(16);
  return (
    <Html center position={[0, 0.05, 4.9]} distanceFactor={scale}>
      <span className="zone-label">{label}</span>
    </Html>
  );
}

const ZONES: { label: string; x: number; width: number; color: string }[] = [
  { label: 'Client', x: -7.4, width: 5.4, color: '#0ea5e9' },
  { label: 'Waldur', x: 0, width: 5.4, color: '#65a30d' },
  { label: 'Identity provider', x: 7.4, width: 5.4, color: '#d97706' },
];

export function Stage({
  steps,
  index,
  step,
  holdings,
  reducedMotion,
  runKey,
  onGoTo,
}: Props) {
  const activeActors = useMemo(
    () => new Set<ActorId>([step.from, step.to]),
    [step],
  );

  // Only the immediate neighbours are drawn alongside the current hop. Drawing
  // every hop turns the stage into a ball of overlapping arcs; drawing only one
  // leaves nothing to click.
  const visibleHops = useMemo(() => {
    const out: { step: Step; index: number; tone: 'past' | 'current' | 'future' }[] = [];
    if (index > 0) out.push({ step: steps[index - 1], index: index - 1, tone: 'past' });
    out.push({ step, index, tone: 'current' });
    if (index < steps.length - 1)
      out.push({ step: steps[index + 1], index: index + 1, tone: 'future' });
    return out;
  }, [steps, index, step]);

  return (
    <Canvas
      camera={{ position: [0, 2.5, 16], fov: 46 }}
      dpr={[1, 2]}
      gl={{ antialias: true }}
    >
      <color attach="background" args={['#0b1220']} />
      <fog attach="fog" args={['#0b1220', 26, 52]} />

      <ambientLight intensity={0.55} />
      <directionalLight position={[6, 12, 10]} intensity={1.1} />
      <directionalLight position={[-8, 4, -6]} intensity={0.35} color="#60a5fa" />

      {ZONES.map((zone) => (
        <group key={zone.label} position={[zone.x, -5.8, 0]}>
          <mesh rotation={[-Math.PI / 2, 0, 0]}>
            <planeGeometry args={[zone.width, 9]} />
            <meshStandardMaterial
              color={zone.color}
              transparent
              opacity={0.1}
              roughness={1}
            />
          </mesh>
          <ZoneLabel label={zone.label} />
        </group>
      ))}

      {ACTORS.map((actor) => (
        <ActorNode
          key={actor.id}
          actor={actor}
          holdings={holdings[actor.id]}
          active={activeActors.has(actor.id)}
        />
      ))}

      {visibleHops.map((hop) => (
        <HopLine
          key={`${hop.index}-${hop.step.id}`}
          step={hop.step}
          index={hop.index}
          tone={hop.tone}
          onSelect={onGoTo}
        />
      ))}

      <Packet step={step} reducedMotion={reducedMotion} runKey={runKey} />
      <CameraRig />
    </Canvas>
  );
}

import { ACTORS } from '../data/actors';
import { CREDENTIAL_BY_ID } from '../data/credentials';
import type { Step } from '../data/types';

interface Props {
  steps: Step[];
  index: number;
  onGoTo: (i: number) => void;
}

const COLUMN = 190;
const TOP = 64;
const ROW = 46;
const MARGIN = 90;

/**
 * Doubles as the no-WebGL fallback and as the "see the whole thing at once"
 * view. Front-channel arrows are dashed, back-channel solid, matching the 3D
 * scene, and both are coloured by the credential they carry.
 */
export function SequenceDiagram({ steps, index, onGoTo }: Props) {
  const width = MARGIN * 2 + COLUMN * (ACTORS.length - 1);
  const height = TOP + ROW * steps.length + 40;
  const x = (id: string) =>
    MARGIN + COLUMN * ACTORS.findIndex((a) => a.id === id);

  return (
    <div className="sequence">
      {/* The scroll lives on an inner wrapper, never on .sequence itself: an
          overflow scroll container as a grid item collapses its row to zero. */}
      <div className="sequence-scroll">
      {/*
        Explicit width/height attributes plus an inline aspect-ratio are load
        bearing. Without a definite intrinsic ratio the SVG's height depends on
        its resolved width, which inside the overflow-x scroll container leaves
        the grid row unable to size and collapses it to zero, so the text view
        lays out on top of the diagram.
      */}
      <svg
        viewBox={`0 0 ${width} ${height}`}
        width={width}
        height={height}
        style={{ aspectRatio: `${width} / ${height}` }}
        role="img"
        aria-label="Sequence diagram of the login flow"
      >
        {ACTORS.map((actor) => (
          <g key={actor.id}>
            <text className="lifeline-label" x={x(actor.id)} y={26} textAnchor="middle">
              {actor.name}
            </text>
            <line
              className="lifeline"
              x1={x(actor.id)}
              y1={TOP - 20}
              x2={x(actor.id)}
              y2={height - 20}
            />
          </g>
        ))}

        {steps.map((step, i) => {
          const y = TOP + ROW * i;
          const colour = CREDENTIAL_BY_ID[step.credential].color;
          const from = x(step.from);
          const to = x(step.to);
          const current = i === index;
          const self = step.from === step.to;

          return (
            <g
              key={step.id}
              className={`seq-step${current ? ' is-current' : ''}`}
              onClick={() => onGoTo(i)}
              role="button"
              tabIndex={0}
              onKeyDown={(e) => {
                if (e.key !== 'Enter' && e.key !== ' ') return;
                // Space also reaches the window-level play/pause handler and
                // scrolls the page; claim it here.
                e.preventDefault();
                e.stopPropagation();
                onGoTo(i);
              }}
            >
              <rect x={0} y={y - 16} width={width} height={ROW} className="seq-hit" />
              {self ? (
                <path
                  d={`M ${from} ${y} h 34 v 18 h -34`}
                  fill="none"
                  stroke={colour}
                  strokeWidth={current ? 3 : 1.8}
                  strokeDasharray="4 3"
                />
              ) : (
                <line
                  x1={from}
                  y1={y}
                  x2={to}
                  y2={y}
                  stroke={colour}
                  strokeWidth={current ? 3 : 1.8}
                  strokeDasharray={step.channel === 'front' ? '7 5' : undefined}
                  markerEnd={`url(#arrow-${current ? 'current' : 'plain'})`}
                />
              )}
              <text
                className="seq-label"
                x={self ? from + 46 : (from + to) / 2}
                y={y - 6}
                textAnchor="middle"
                fill={current ? '#e2e8f0' : '#94a3b8'}
              >
                {i + 1}. {step.title}
              </text>
            </g>
          );
        })}

        <defs>
          <marker id="arrow-plain" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto">
            <path d="M0,0 L0,6 L7,3 z" fill="#94a3b8" />
          </marker>
          <marker id="arrow-current" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto">
            <path d="M0,0 L0,6 L7,3 z" fill="#e2e8f0" />
          </marker>
        </defs>
      </svg>
      </div>
      <p className="sequence-key">
        Dashed arrows are front-channel hops through the browser; solid arrows
        are direct back-channel calls. Colour marks which credential is in
        flight.
      </p>
    </div>
  );
}

import type { Step } from '../data/types';

interface Props {
  steps: Step[];
  index: number;
  playing: boolean;
  onGoTo: (i: number) => void;
  onPlayToggle: () => void;
  onPrev: () => void;
  onNext: () => void;
}

export function Timeline({
  steps,
  index,
  playing,
  onGoTo,
  onPlayToggle,
  onPrev,
  onNext,
}: Props) {
  return (
    <div className="timeline">
      <div className="transport">
        <button type="button" onClick={onPrev} disabled={index === 0}>
          &#8592; Back
        </button>
        <button type="button" className="play" onClick={onPlayToggle}>
          {playing ? 'Pause' : 'Play'}
        </button>
        <button
          type="button"
          onClick={onNext}
          disabled={index === steps.length - 1}
        >
          Next &#8594;
        </button>
      </div>

      <ol className="ticks">
        {steps.map((step, i) => (
          <li key={step.id}>
            <button
              type="button"
              className={`tick channel-${step.channel}${i === index ? ' is-current' : ''}${i < index ? ' is-done' : ''}`}
              onClick={() => onGoTo(i)}
              aria-current={i === index ? 'step' : undefined}
              title={`${i + 1}. ${step.title}`}
            >
              <span className="sr-only">
                {i + 1}. {step.title}
              </span>
            </button>
          </li>
        ))}
      </ol>
    </div>
  );
}

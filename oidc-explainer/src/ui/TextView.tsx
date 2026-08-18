import { useEffect, useRef } from 'react';

import { ACTOR_BY_ID } from '../data/actors';
import { channelShort } from '../data/channels';
import { CREDENTIAL_BY_ID } from '../data/credentials';
import type { Step } from '../data/types';
import { codeRefUrl } from './CodeRefs';

interface Props {
  steps: Step[];
  index: number;
  onGoTo: (i: number) => void;
  reducedMotion: boolean;
}

/**
 * Every step readable without the animation, in one linear document. This is
 * the accessible path, not a lesser one: it carries the same narration,
 * payloads and code references.
 *
 * The current step is marked and scrolled to as the transport moves, so the
 * stepper drives this view rather than only recolouring the diagram above it.
 */
export function TextView({ steps, index, onGoTo, reducedMotion }: Props) {
  const items = useRef<(HTMLLIElement | null)[]>([]);

  useEffect(() => {
    const el = items.current[index];
    const container = el?.closest('.text-main');
    if (!el || !(container instanceof HTMLElement)) return;
    // Deliberately not scrollIntoView: it walks every ancestor scroll container,
    // and this app is embedded in an iframe on the docs page, so it would scroll
    // the host document too on every step.
    const top =
      el.offsetTop - container.clientHeight / 2 + el.clientHeight / 2;
    container.scrollTo({
      top: Math.max(0, top),
      behavior: reducedMotion ? 'auto' : 'smooth',
    });
  }, [index, reducedMotion]);

  return (
    <article className="text-view">
      <ol>
        {steps.map((step, i) => (
          <li
            key={step.id}
            id={`text-step-${i + 1}`}
            ref={(el) => {
              items.current[i] = el;
            }}
            className={i === index ? 'is-current' : undefined}
            aria-current={i === index ? 'step' : undefined}
            onClick={() => onGoTo(i)}
          >
            <h3>
              {i + 1}. {step.title}
            </h3>
            <p className="meta">
              {ACTOR_BY_ID[step.from].name} &rarr; {ACTOR_BY_ID[step.to].name} (
              {channelShort(step)})
              {step.credential !== 'none' &&
                `, carrying the ${CREDENTIAL_BY_ID[step.credential].label.toLowerCase()}`}
            </p>
            <p>{step.narration}</p>
            {step.wire.url && (
              <p className="meta">
                <code>
                  {step.wire.method ?? step.wire.status} {step.wire.url}
                </code>
              </p>
            )}
            {step.wire.body && <pre>{step.wire.body}</pre>}
            {step.wire.note && <p className="note">{step.wire.note}</p>}
            {step.callout && (
              <p className={`note note-${step.callout.tone}`}>
                {step.callout.text}
              </p>
            )}
            {step.specs && step.specs.length > 0 && (
              <p className="meta">
                Spec:{' '}
                {step.specs.map((spec, j) => (
                  <span key={spec.url}>
                    {j > 0 && ', '}
                    <a href={spec.url} target="_blank" rel="noreferrer">
                      {spec.label}
                    </a>
                  </span>
                ))}
              </p>
            )}
            {step.code.length > 0 && (
              <p className="meta">
                Code:{' '}
                {step.code.map((ref, j) => (
                  <span key={ref.symbol}>
                    {j > 0 && ', '}
                    <a href={codeRefUrl(ref)} target="_blank" rel="noreferrer">
                      {ref.path} &middot; {ref.label ?? ref.symbol}
                    </a>
                  </span>
                ))}
              </p>
            )}
          </li>
        ))}
      </ol>
    </article>
  );
}

import { ACTOR_BY_ID } from '../data/actors';
import { channelKind, channelLabel } from '../data/channels';
import { CREDENTIAL_BY_ID } from '../data/credentials';
import type { Step } from '../data/types';
import { useEffect, useRef, useState } from 'react';

import { CodeRefs } from './CodeRefs';
import { SpecRefs } from './SpecRefs';
import { WireView } from './WireView';

interface Props {
  step: Step;
  index: number;
  total: number;
}

export function Panel({ step, index, total }: Props) {
  const credential = CREDENTIAL_BY_ID[step.credential];
  const ref = useRef<HTMLElement>(null);
  const [hasMore, setHasMore] = useState(false);

  // Re-measured per step: some steps fit, some hide the code and spec links.
  useEffect(() => {
    const el = ref.current;
    if (!el) return;
    el.scrollTop = 0;
    const check = () => setHasMore(el.scrollHeight - el.clientHeight > 8);
    check();
    const ro = new ResizeObserver(check);
    ro.observe(el);
    return () => ro.disconnect();
  }, [step]);

  return (
    <aside className={`panel${hasMore ? ' has-more' : ''}`} ref={ref}>
      <header className="panel-header">
        <p className="step-count">
          Step {index + 1} of {total}
        </p>
        <h2>{step.title}</h2>
        <p className={`channel channel-${channelKind(step)}`}>
          {channelLabel(step)}
        </p>
        <p className="hop">
          <span>{ACTOR_BY_ID[step.from].name}</span>
          <span aria-hidden="true"> &rarr; </span>
          <span>{ACTOR_BY_ID[step.to].name}</span>
          {step.credential !== 'none' && (
            <span
              className="credential-chip"
              style={{ '--chip': credential.color } as React.CSSProperties}
              title={credential.blurb}
            >
              {credential.label}
            </span>
          )}
        </p>
      </header>

      <p className="narration">{step.narration}</p>

      <WireView wire={step.wire} />

      {step.callout && (
        <aside className={`callout callout-${step.callout.tone}`}>
          <strong>{step.callout.tone === 'warning' ? 'Watch out' : 'Worth knowing'}</strong>
          <p>{step.callout.text}</p>
        </aside>
      )}

      <CodeRefs refs={step.code} />

      <SpecRefs specs={step.specs} />

      <div className="panel-fade" aria-hidden="true" />
    </aside>
  );
}

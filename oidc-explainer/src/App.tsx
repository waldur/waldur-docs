import { Suspense, useEffect, useMemo, useRef, useState } from 'react';

import { useHashSync } from './hash';
import { Stage } from './scene/Stage';
import {
  hasWebGL,
  holdingsAt,
  prefersReducedMotion,
  stepsForMode,
  useStore,
} from './store';
import { Controls } from './ui/Controls';
import { Panel } from './ui/Panel';
import { SequenceDiagram } from './ui/SequenceDiagram';
import { TextView } from './ui/TextView';
import { Timeline } from './ui/Timeline';

const AUTOPLAY_MS = 4200;

export function App() {
  useHashSync();

  const mode = useStore((s) => s.mode);
  const index = useStore((s) => s.index);
  const playing = useStore((s) => s.playing);
  const textOnly = useStore((s) => s.textOnly);
  const { setMode, goTo, next, prev, setPlaying, toggleTextOnly } = useStore();

  const [webgl] = useState(hasWebGL);
  const [reducedMotion, setReducedMotion] = useState(prefersReducedMotion);

  // Honour a mid-session change of the OS motion preference.
  useEffect(() => {
    // Guarded to match store.ts, which already treats matchMedia as optional:
    // an unguarded call here would throw during mount and render nothing.
    const query = window.matchMedia?.('(prefers-reduced-motion: reduce)');
    if (!query?.addEventListener) return;
    const onChange = () => setReducedMotion(query.matches);
    query.addEventListener('change', onChange);
    return () => query.removeEventListener('change', onChange);
  }, []);

  const steps = useMemo(() => stepsForMode(mode), [mode]);
  const step = steps[Math.min(index, steps.length - 1)];
  const holdings = useMemo(() => holdingsAt(steps, index), [steps, index]);

  // Autoplay.
  const timer = useRef<number>();
  useEffect(() => {
    if (!playing) return;
    timer.current = window.setTimeout(next, AUTOPLAY_MS);
    return () => window.clearTimeout(timer.current);
  }, [playing, index, next]);

  // Keyboard transport.
  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      if (e.target instanceof HTMLElement && e.target.tagName === 'INPUT') return;
      if (e.key === 'ArrowRight') next();
      if (e.key === 'ArrowLeft') prev();
      if (e.key === ' ') {
        e.preventDefault();
        setPlaying(!playing);
      }
    };
    window.addEventListener('keydown', onKey);
    return () => window.removeEventListener('keydown', onKey);
  }, [next, prev, playing, setPlaying]);

  return (
    <div className={`app${textOnly ? ' is-text' : ''}`}>
      <Controls
        mode={mode}
        textOnly={textOnly}
        onMode={setMode}
        onTextOnly={toggleTextOnly}
      />

      {textOnly ? (
        <main className="text-main">
          <SequenceDiagram steps={steps} index={index} onGoTo={goTo} />
          <TextView
            steps={steps}
            index={index}
            onGoTo={goTo}
            reducedMotion={reducedMotion}
          />
        </main>
      ) : (
        <main className="stage-main">
          <div className="viewport">
            {webgl ? (
              <Suspense fallback={<div className="loading">Loading scene...</div>}>
                <Stage
                  steps={steps}
                  index={index}
                  step={step}
                  holdings={holdings}
                  reducedMotion={reducedMotion}
                  runKey={`${mode}:${index}`}
                  onGoTo={goTo}
                />
              </Suspense>
            ) : (
              <div className="no-webgl">
                <p>
                  This browser has no WebGL, so here is the same flow as a
                  sequence diagram.
                </p>
                <SequenceDiagram steps={steps} index={index} onGoTo={goTo} />
              </div>
            )}
          </div>

          <Panel step={step} index={index} total={steps.length} />
        </main>
      )}

      <Timeline
        steps={steps}
        index={index}
        playing={playing}
        onGoTo={goTo}
        onPlayToggle={() => setPlaying(!playing)}
        onPrev={prev}
        onNext={next}
      />
    </div>
  );
}

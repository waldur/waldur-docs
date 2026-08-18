import { CREDENTIALS } from '../data/credentials';
import { BRANCHES, SCENARIOS } from '../data/scenarios';
import { VARIANTS } from '../data/variants';
import type { Mode } from '../store';

interface Props {
  mode: Mode;
  textOnly: boolean;
  onMode: (mode: Mode) => void;
  onTextOnly: () => void;
}

export function Controls({ mode, textOnly, onMode, onTextOnly }: Props) {
  const branch = BRANCHES.find((s) => s.id === mode);

  return (
    <header className="controls">
      <div className="titles">
        <h1>How Waldur logs you in with OIDC</h1>
        <p>
          The authorization code flow, one hop at a time, with the payloads and
          the code that produces them.
        </p>
      </div>

      <div className="mode-picker">
        <button
          type="button"
          className={mode === 'flow' ? 'is-active' : ''}
          onClick={() => onMode('flow')}
        >
          The normal flow
        </button>
        {VARIANTS.map((s) => (
          <button
            key={s.id}
            type="button"
            className={mode === s.id ? 'is-active' : ''}
            onClick={() => onMode(s.id)}
            title={s.short}
          >
            {s.label}
          </button>
        ))}
        <span className="mode-divider">Break it:</span>
        {SCENARIOS.map((s) => (
          <button
            key={s.id}
            type="button"
            className={`danger${mode === s.id ? ' is-active' : ''}`}
            onClick={() => onMode(s.id)}
            title={s.short}
          >
            {s.label}
          </button>
        ))}
        <button
          type="button"
          className={`ghost${textOnly ? ' is-active' : ''}`}
          onClick={onTextOnly}
        >
          {textOnly ? 'Back to the scene' : 'Overview & full text'}
        </button>
      </div>

      {branch && (
        <div className={`scenario-banner is-${branch.kind}`}>
          <p className="outcome">
            <strong>
              {branch.kind === 'attack'
                ? 'If this guard is missing:'
                : 'What is different:'}
            </strong>{' '}
            {branch.outcome}
          </p>
          <p className="guard">
            <strong>{branch.guard.title}:</strong> {branch.guard.text}
          </p>
        </div>
      )}

      <div className="legends">
        <ul className="legend">
          <li className="legend-caption">Carrying</li>
          {CREDENTIALS.filter((c) => c.id !== 'none').map((c) => (
            <li key={c.id} title={c.blurb}>
              <span className="swatch" style={{ background: c.color }} />
              {c.label}
            </li>
          ))}
        </ul>

        {/* The dashed/solid distinction is the whole point of the scene and was
            previously explained only inside the text view's diagram key. */}
        {!textOnly && (
          <ul className="legend legend-lines">
            <li className="legend-caption">Lines</li>
            <li title="A redirect: it travels through the browser and its parameters are visible in the address bar.">
              <span className="line-swatch is-dashed" />
              through the browser
            </li>
            <li title="A direct request: not a redirect, so nothing lands in a URL.">
              <span className="line-swatch" />
              direct call
            </li>
            <li title="The steps immediately before and after the current one.">
              <span className="line-swatch is-faint" />
              previous / next hop
            </li>
            <li className="legend-hint">
              Hover a line for its payload, click to jump to it
            </li>
          </ul>
        )}
      </div>
    </header>
  );
}

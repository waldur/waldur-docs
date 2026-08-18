import type { Wire } from '../data/types';

export function WireView({ wire }: { wire: Wire }) {
  const hasHead = Boolean(wire.method || wire.url || wire.status);
  return (
    <section className="panel-section">
      <h4>{wire.kind === 'internal' ? 'What happens' : 'On the wire'}</h4>
      <div className="wire">
        {hasHead && (
          <p className="wire-head">
            {wire.method && <span className="method">{wire.method}</span>}
            {wire.url && <span className="url">{wire.url}</span>}
            {wire.status && <span className="status">{wire.status}</span>}
          </p>
        )}
        {wire.headers && (
          <dl className="wire-headers">
            {Object.entries(wire.headers).map(([k, v]) => (
              <div key={k}>
                <dt>{k}</dt>
                <dd>{v}</dd>
              </div>
            ))}
          </dl>
        )}
        {wire.body && <pre>{wire.body}</pre>}
        {wire.note && <p className="wire-note">{wire.note}</p>}
      </div>
    </section>
  );
}

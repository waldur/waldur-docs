import type { SpecRef } from '../data/types';

export function SpecRefs({ specs }: { specs?: SpecRef[] }) {
  if (!specs || specs.length === 0) return null;
  return (
    <section className="panel-section">
      <h4>In the spec</h4>
      <ul className="spec-refs">
        {specs.map((spec) => (
          <li key={spec.url}>
            <a href={spec.url} target="_blank" rel="noreferrer">
              {spec.label}
            </a>
            <p>{spec.note}</p>
          </li>
        ))}
      </ul>
    </section>
  );
}

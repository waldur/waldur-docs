import type { CodeRef } from '../data/types';

/**
 * This page is published on the public documentation site, so references point
 * at the GitHub mirrors rather than the GitLab instance the team develops on -
 * code.opennodecloud.com requires an account most readers will not have. Both
 * product repos are public there and both default to `develop`, the same branch
 * the internal remotes use.
 */
const BRANCH = 'develop';
const HOST = 'https://github.com/waldur';

export const codeRefUrl = (ref: CodeRef) =>
  `${HOST}/${ref.repo}/blob/${BRANCH}/${ref.path}`;

export function CodeRefs({ refs }: { refs: CodeRef[] }) {
  if (refs.length === 0) return null;
  return (
    <section className="panel-section">
      <h4>In the code</h4>
      <ul className="code-refs">
        {refs.map((ref) => (
          <li key={`${ref.repo}:${ref.path}:${ref.symbol}`}>
            <a href={codeRefUrl(ref)} target="_blank" rel="noreferrer">
              <span className="repo">{ref.repo}</span>
              <code>{ref.label ?? ref.symbol}</code>
              <span className="path">{ref.path}</span>
            </a>
          </li>
        ))}
      </ul>
    </section>
  );
}

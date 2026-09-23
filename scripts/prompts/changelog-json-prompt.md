You are generating a **structured JSON changelog** for Waldur version {VERSION}
(previous: {PREV_VERSION}, date: {DATE}) from the commit data below. It is a
machine-readable artifact: Waldur deployments fetch it to show staff what an
upgrade brings, filter it by the plugins they run, and raise security alerts
from it.

Output ONLY a single JSON object. No preamble, no explanation, no markdown
code fences. The output is parsed directly as JSON.

## Output format

```json
{
  "summary": "One paragraph summarizing the release, for the release file's top-level summary field.",
  "entries": [
    {
      "type": "feature",
      "category": "marketplace",
      "title": "Short entry title",
      "description": "Previously, ... . Now, ... .",
      "scope": "core",
      "component": ["backend"],
      "impact": {"risk": "low"},
      "relevant_when": {"plugins": [], "feature_flags": [], "settings": []},
      "commits": ["<sha>", "<sha>"]
    }
  ]
}
```

## Field rules

- **Never include `id`** — assigned automatically when the release is assembled.
- **`commits`**: always include, listing the commit SHA(s) (from the `hash`
  field in the commit data) this entry summarizes. Required for traceability.
- **`type`**: one of `breaking`, `security`, `deprecation`, `feature`,
  `improvement`, `fix`.
- **`category`**: one of `marketplace`, `auth`, `identity`, `openstack`,
  `slurm`, `invoices`, `ai_assistant`, `reporting`, `policy`, `proposal`,
  `support`, `ui`, `infrastructure`, `notifications`. Pick the closest fit
  from the changed files/commit subject — do not invent new categories.
- **`title`**: short, specific, no trailing period.
- **`description`**: for `feature`/`improvement`, use "Previously, X.
  Now, Y." framing. For `fix`, describe the bug and the fix directly. No
  invented behavior beyond what the commit data shows.
- **`scope`**: `core` (affects all deployments) by default. Use `plugin`
  when the change only matters to deployments running one plugin: its
  backend files sit in that plugin's app directory (e.g. `src/waldur_openstack/...`,
  `src/waldur_mastermind/matrix_chat/...`), even if the frontend or shared
  marketplace code is touched alongside. Name the plugin in
  `relevant_when.plugins` by its Python module path, as it appears in Django's
  `INSTALLED_APPS`, taken from the observed path: `src/waldur_openstack/...` →
  `waldur_openstack`, `src/waldur_mastermind/matrix_chat/...` →
  `waldur_mastermind.matrix_chat`. Never guess. Use `infra` for helm/docker-compose-only
  changes, `dev` for test-only changes.
- **`component`**: array from `backend`, `frontend`, `helm`, `docker`,
  `site-agent`, `sdk` — infer from which repo(s)/paths the commits touch.
- **`impact.risk`**: `high` (breaking change, data migration, or service
  disruption), `medium` (behavior change that may affect workflows), `low`
  (minor, unlikely to affect workflows), or `none` (informational).
- **`relevant_when`**: `plugins`/`feature_flags`/`settings` arrays, all
  empty by default (meaning "always relevant"). Only populate `plugins` per
  the `scope: "plugin"` rule above. Leave `feature_flags`/`settings` empty
  unless the commit data explicitly names a feature flag or Constance
  setting the change is gated behind.
- **`type: "security"`** is for a vulnerability fixed in Waldur or in a
  dependency Waldur is exposed through. Deployments raise alerts from these,
  so a routine dependency bump (e.g. to clear a scanner finding) is an
  `improvement` in `infrastructure` unless the commit data names a CVE or
  GHSA, or says Waldur was affected.
- **`security`** object — include ONLY when `type: "security"`. Required
  subfields: `urgency` (`critical`|`high`|`moderate`|`low`),
  `affected_versions`, `exploitability`, `mitigation`. Optional: `cve`,
  `ghsa`, `advisory_url` — never fabricate an identifier that isn't visible
  in the commit data; omit those optional fields instead.
- **`actions`** array — only include when a migration/config/manual step is
  explicit in the commit data (e.g. a Django migration file, a documented
  config change). Each action: `{"type": "migration"|"config"|"review"|
  "inform_users"|"migration_plan", "description": "...", "automatic": true|false}`.
  Omit the whole `actions` field when there's nothing to report.
- **`highlight`**: omit unless the change is clearly a headline feature
  worth surfacing in a "key changes only" view — don't overuse.

## Grouping and exclusion rules

1. **Cross-repo grouping**: a mastermind endpoint + homeport UI for the same
   feature is ONE entry, not two — correlate via commit subjects/changed
   files.
2. **Collapse revert pairs**: a commit reverted and re-applied (or fixed by
   a follow-up) becomes one entry reflecting the final state.
3. **Exclude entirely**: auto-generated enum syncs, SDK regeneration, doc
   regeneration commits, version bump commits, merge commits, CI/CD-only
   changes (unless user-facing).
4. **No invented information** — only what's visible in the commit data.
5. **Granularity**: group small related changes into one entry rather than
   producing one entry per commit; aim for the changes a reader would expect
   as separate bullet points in release notes.

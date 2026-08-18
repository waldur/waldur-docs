#!/usr/bin/env node
/**
 * The explainer claims that a given symbol lives at a given path in the product
 * repos. That claim rots silently. This script re-checks every reference in
 * src/data against real checkouts.
 *
 * It needs the product repos as siblings of waldur-docs (the layout the Waldur
 * workspace bootstrap produces) or explicit paths via WALDUR_MASTERMIND_PATH /
 * WALDUR_HOMEPORT_PATH. Where they are absent it skips rather than fails, so a
 * docs-only CI job is not blocked by repos it does not check out.
 */
import { existsSync, readdirSync, readFileSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));
const dataDir = resolve(here, '..', 'src', 'data');
const workspace = resolve(here, '..', '..', '..');

const REPOS = {
  'waldur-mastermind':
    process.env.WALDUR_MASTERMIND_PATH ?? join(workspace, 'waldur-mastermind'),
  'waldur-homeport':
    process.env.WALDUR_HOMEPORT_PATH ?? join(workspace, 'waldur-homeport'),
};

const REF_RE =
  /repo:\s*'([^']+)',\s*(?:\/\*[\s\S]*?\*\/\s*|\/\/[^\n]*\n\s*)*path:\s*'([^']+)',\s*(?:\/\*[\s\S]*?\*\/\s*|\/\/[^\n]*\n\s*)*symbol:\s*'([^']+)'/g;

// Glob the directory rather than list files: a new data file must not be able
// to smuggle in unchecked references by not being on a hand-maintained list.
const sources = readdirSync(dataDir).filter((f) => f.endsWith('.ts'));
const refs = [];

for (const file of sources) {
  const text = readFileSync(join(dataDir, file), 'utf8');
  for (const [, repo, path, symbol] of text.matchAll(REF_RE)) {
    refs.push({ repo, path, symbol, source: file });
  }
}

if (refs.length === 0) {
  console.error('No code references found - has the data format changed?');
  process.exit(1);
}

const problems = [];
const skipped = new Set();
let checked = 0;

for (const ref of refs) {
  const root = REPOS[ref.repo];
  if (!root || !existsSync(root)) {
    skipped.add(ref.repo);
    continue;
  }
  const full = join(root, ref.path);
  if (!existsSync(full)) {
    problems.push(`${ref.source}: ${ref.repo}/${ref.path} does not exist`);
    continue;
  }
  if (!readFileSync(full, 'utf8').includes(ref.symbol)) {
    problems.push(
      `${ref.source}: ${ref.repo}/${ref.path} no longer contains "${ref.symbol}"`,
    );
    continue;
  }
  checked += 1;
}

const skippedRefs = refs.length - checked - problems.length;

for (const repo of skipped) {
  const varName =
    repo === 'waldur-homeport'
      ? 'WALDUR_HOMEPORT_PATH'
      : 'WALDUR_MASTERMIND_PATH';
  console.log(`skipped ${repo}: no checkout found, set ${varName} to check it`);
}

// Skipping used to be invisible: the script printed "N/N verified" counting only
// what it looked at, so a run that checked nothing still looked like a pass.
if (skippedRefs > 0) {
  console.log(
    `${skippedRefs} of ${refs.length} references NOT checked (missing checkouts).`,
  );
  if (process.env.WALDUR_REFS_STRICT === '1') {
    console.error(
      '\nWALDUR_REFS_STRICT=1 but some references could not be checked.',
    );
    process.exit(1);
  }
}

if (problems.length > 0) {
  console.error(`\n${problems.length} stale code reference(s):`);
  problems.forEach((p) => console.error(`  - ${p}`));
  console.error('\nUpdate src/data/flow.ts or src/data/scenarios.ts to match.');
  process.exit(1);
}

console.log(`${checked}/${refs.length} code references verified.`);

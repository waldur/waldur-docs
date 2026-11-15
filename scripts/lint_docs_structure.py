"""Check that user documentation is structured so the AI assistant's search finds it.

The assistant searches the documentation section by section (hooks/docs_corpus.py,
waldur/waldur-docs#37). Each rule here is something measured to cost search
results, or a direct consequence of how the search works:

  DS001 stemmed-gerund      "Adding …": the search stems it to "ad", which "add"
                            does not match. Use "Add …".
  DS002 noun-task-heading   "Project creation": nouns do not match the verbs
                            people type ("creation" is not "create"). Name the
                            task with its verb: "Create a project".
  DS003 generic-heading     "Overview", "Details": the heading is the
                            strongest-weighted part of a section and says
                            nothing. Name what the section is about.
  DS004 long-section        a long section without subheadings: one section
                            ranks for one topic, so split it per task.
  DS005 positional-reference "the table above": a section is read on its own,
                            without what is above it. Name what you refer to.
  DS006 concept-unasked     a concept page with no section worded as the
                            question it answers ("What is an offering",
                            "How organizations and projects differ").

Findings already in docs-structure-baseline.txt are reported but do not fail;
new ones do, and so do baseline entries that no longer occur. After fixing a
baselined finding, --update-baseline removes its line; it never adds one.
Adding needs --accept-new, which a reviewer should see in the diff.

    uv run python scripts/lint_docs_structure.py                    # check
    uv run python scripts/lint_docs_structure.py --all              # also list baselined findings
    uv run python scripts/lint_docs_structure.py --update-baseline  # drop fixed lines
    uv run python scripts/lint_docs_structure.py --update-baseline --accept-new
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "hooks"))

import docs_corpus  # noqa: E402 - the corpus hook decides scope, exclusion and kind

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
CONFIG = ROOT / "docs-corpus.yml"
BASELINE = ROOT / "docs-structure-baseline.txt"

LONG_SECTION_WORDS = 450

_FENCE = re.compile(r"^\s*(```|~~~)")
_HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*(\{[^}]*\})?\s*#*\s*$")
_ATTR = re.compile(r'([\w-]+)="([^"]*)"')
_STEP = re.compile(r"^(step\s+\d+[:.]?|\d+[.)])\s*", re.IGNORECASE)
_WORD = re.compile(r"[A-Za-z][\w'-]*")
_MARKUP = re.compile(r"!\[[^\]]*\]\([^)]*\)|<[^>]+>|\]\([^)]*\)|[*_`#>|]")

# Snowball (the stemmer Postgres's "english" search uses) undoubles a final
# consonant after removing -ing, so the gerund of a verb that itself ends in
# a doubled consonant loses a letter: "adding" -> "ad", while "add" -> "add".
# "Configuring", "Creating" and the rest stem like their verb.
_STEMMED_GERUND = re.compile(r"^(Adding|Staffing|Stuffing|Erring)\b")

# Nouns that name an action. A how-to heading that ends with one and has no
# verb reads as a topic, not a task.
_ACTION_NOUNS = (
    "management|creation|configuration|deletion|removal|modification|"
    "administration|registration|activation|deactivation|installation|"
    "assignment|submission|approval|cancellation|termination|setup|"
    "provisioning|onboarding|invitation|invitations"
)
_NOUN_TASK = re.compile(rf"\b({_ACTION_NOUNS})$", re.IGNORECASE)
# "Defaults on call creation", "After approval": a moment, not a task.
_MOMENT = re.compile(r"\b(at|on|after|before|during|upon)\b", re.IGNORECASE)
# First words that already make the heading a task.
_IMPERATIVES = {
    "add",
    "assign",
    "activate",
    "approve",
    "cancel",
    "change",
    "check",
    "choose",
    "configure",
    "connect",
    "create",
    "deactivate",
    "delete",
    "disable",
    "edit",
    "enable",
    "find",
    "get",
    "give",
    "install",
    "invite",
    "manage",
    "move",
    "open",
    "order",
    "register",
    "remove",
    "rename",
    "request",
    "revoke",
    "review",
    "rotate",
    "run",
    "select",
    "set",
    "share",
    "start",
    "stop",
    "submit",
    "switch",
    "terminate",
    "track",
    "turn",
    "update",
    "upload",
    "use",
    "view",
}

_GENERIC = re.compile(
    r"^(overview|introduction|intro|details|detail|notes?|general|other|"
    r"misc|miscellaneous|usage|examples?|summary|description|more information|"
    r"additional information|information|background|basics|key concepts|"
    r"concepts)$",
    re.IGNORECASE,
)

# References to the page's own layout. "The banner shown above the tabs"
# describes the portal, not the page, so only document objects count.
_POSITIONAL = re.compile(
    r"\b((the|this|these|that) (table|list|steps?|examples?|screenshots?|images?|"
    r"figure|diagram|section|instructions|options) above"
    r"|(see|described|mentioned|listed|explained|outlined) above"
    r"|(the )?previous section)\b",
    re.IGNORECASE,
)
# An image or a table earlier in the same section travels with it.
_OWN_OBJECT = re.compile(r"!\[|^\s*\|", re.MULTILINE)

_QUESTION_HEADING = re.compile(
    r"^(what|when|why|who|how)\b|\bdiffer|\bvs\.?\b|\bversus\b", re.IGNORECASE
)


@dataclass(frozen=True)
class Finding:
    rule: str
    path: str
    line: int
    heading: str
    message: str

    @property
    def key(self) -> str:
        """Baseline key: stable across edits elsewhere on the page."""
        return f"{self.rule}\t{self.path}\t{self.heading}"

    def __str__(self) -> str:
        return f"docs/{self.path}:{self.line}: {self.rule} {self.message}"


@dataclass
class Section:
    level: int
    title: str
    line: int
    attrs: dict
    words: int = 0
    text: str = ""


@dataclass
class Rules:
    """The corpus hook's rules, limited to the pages the assistant is given
    section questions for (`questions_scope`): the user documentation."""

    corpus: docs_corpus.Rules
    scope: list[re.Pattern]

    @classmethod
    def load(cls, path: Path = CONFIG) -> Rules:
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        return cls(
            corpus=docs_corpus.Rules.load(path),
            scope=[re.compile(p) for p in data.get("questions_scope") or []],
        )

    def checks(self, path: str) -> bool:
        return self.corpus.in_scope(path) and any(p.search(path) for p in self.scope)


def split_front_matter(text: str) -> tuple[dict, list[str], int]:
    """(front matter, body lines, line number of the first body line)."""
    lines = text.splitlines()
    if lines and lines[0].strip() == "---":
        for end in range(1, len(lines)):
            if lines[end].strip() == "---":
                try:
                    meta = yaml.safe_load("\n".join(lines[1:end])) or {}
                except yaml.YAMLError:
                    meta = {}
                return (
                    (meta if isinstance(meta, dict) else {}),
                    lines[end + 1 :],
                    end + 2,
                )
    return {}, lines, 1


def sections_of(lines: list[str], first_line: int) -> list[Section]:
    sections: list[Section] = []
    in_fence = False
    prose: list[str] = []

    def close():
        if sections:
            text = "\n".join(prose)
            sections[-1].text = text
            sections[-1].words = len(_WORD.findall(_MARKUP.sub(" ", text)))
        prose.clear()

    for offset, line in enumerate(lines):
        if _FENCE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        match = _HEADING.match(line)
        if match:
            close()
            level = len(match.group(1))
            sections.append(
                Section(
                    level=level,
                    title=match.group(2).strip(),
                    line=first_line + offset,
                    attrs=dict(_ATTR.findall(match.group(3) or "")),
                )
            )
        elif not line.lstrip().startswith(("<!--", "!!!", "???")):
            prose.append(line)
    close()
    return sections


def plain(title: str) -> str:
    """A heading without step numbering, markup or a trailing colon."""
    title = _MARKUP.sub("", title).strip().rstrip(":").strip()
    return _STEP.sub("", title).strip()


def lint_page(path: str, text: str, rules: Rules) -> list[Finding]:
    if "EXTERNAL DOCUMENT" in text[:500]:
        return []
    meta, lines, first_line = split_front_matter(text)
    if "corpus" in meta and docs_corpus.is_false(meta["corpus"]):
        return []
    page_type = str(meta.get("type") or "")
    page_kind = rules.corpus.kind_of(path, "", page_type)
    sections = sections_of(lines, first_line)
    findings = []

    def add(rule, section, message):
        findings.append(Finding(rule, path, section.line, section.title, message))

    excluded_level = None
    # data-kind applies to the headings below, as in the corpus hook.
    kinds: list[tuple[int, str]] = []
    for section in sections:
        if excluded_level is not None and section.level > excluded_level:
            continue
        excluded_level = None
        if docs_corpus.is_false(section.attrs.get("data-corpus", "")):
            excluded_level = section.level
            continue
        while kinds and kinds[-1][0] >= section.level:
            kinds.pop()
        if section.attrs.get("data-kind"):
            kinds.append((section.level, section.attrs["data-kind"]))
        title = plain(section.title)
        kind = (kinds[-1][1] if kinds else "") or rules.corpus.kind_of(
            path, section.title, page_type
        )
        if section.level == 1:
            continue
        if _STEMMED_GERUND.match(title):
            add(
                "DS001",
                section,
                f'stemmed-gerund: "{title}" — the search stems '
                f'"{title.split()[0]}" so that the verb does not match it; '
                f'start with "{title.split()[0][:-3]}"',
            )
        words = title.split()
        if (
            kind == "howto"
            and section.level in (2, 3)
            and _NOUN_TASK.search(title)
            and len(words) <= 4
            and not words[0].lower().endswith("ing")
            and words[0].lower() not in _IMPERATIVES
            and not _QUESTION_HEADING.search(title)
            and not _MOMENT.search(title)
        ):
            add(
                "DS002",
                section,
                f'noun-task-heading: "{title}" — name the task with its verb '
                '("Create a project", not "Project creation")',
            )
        if _GENERIC.match(title):
            add(
                "DS003",
                section,
                f'generic-heading: "{title}" — say what the section is about; '
                'on a concept page, as its question ("How billing works")',
            )
        if section.words > LONG_SECTION_WORDS:
            # The corpus holds a section's own text, up to its first
            # subheading, so a long intro above a short subsection counts.
            add(
                "DS004",
                section,
                f'long-section: "{title}" has {section.words} words before its '
                "next heading — split it per task or topic",
            )
        positional = _POSITIONAL.search(section.text)
        if positional and not _OWN_OBJECT.search(section.text[: positional.start()]):
            add(
                "DS005",
                section,
                f'positional-reference: "{positional.group(0)}" in "{title}" — '
                "a section is read on its own; name what you refer to",
            )
    if page_kind == "concept" and sections:
        asked = [
            s
            for s in sections
            if s.level > 1 and _QUESTION_HEADING.search(plain(s.title))
        ]
        if not asked:
            add(
                "DS006",
                sections[0],
                "concept-unasked: no section is worded as the question the page "
                'answers ("What is …", "How … works", "How X and Y differ")',
            )
    return findings


def lint(docs: Path = DOCS, rules: Rules | None = None) -> list[Finding]:
    rules = rules or Rules.load()
    findings = []
    for file in sorted(docs.rglob("*.md")):
        path = file.relative_to(docs).as_posix()
        if rules.checks(path):
            findings += lint_page(path, file.read_text(encoding="utf-8"), rules)
    return findings


def read_baseline(path: Path = BASELINE) -> Counter:
    if not path.exists():
        return Counter()
    return Counter(
        line
        for line in path.read_text(encoding="utf-8").splitlines()
        if line and not line.startswith("#")
    )


BASELINE_HEADER = """\
# Findings of scripts/lint_docs_structure.py that predate it: rule, page, heading.
# Fix them when you touch the page; `uv run python scripts/lint_docs_structure.py
# --update-baseline` then drops the line. New findings are fixed, not added:
# adding takes --accept-new, and shows in the diff of this file.
"""


def write_baseline(findings: list[Finding], path: Path = BASELINE) -> None:
    lines = sorted(f.key for f in findings)
    path.write_text(BASELINE_HEADER + "\n".join(lines) + "\n", encoding="utf-8")


def compare(findings: list[Finding], baseline: Counter):
    """(new findings, baselined findings, baseline keys that no longer occur)."""
    remaining = Counter(baseline)
    new, known = [], []
    for finding in findings:
        if remaining[finding.key] > 0:
            remaining[finding.key] -= 1
            known.append(finding)
        else:
            new.append(finding)
    gone = sorted(key for key, count in remaining.items() for _ in range(count))
    return new, known, gone


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument(
        "--update-baseline",
        action="store_true",
        help="remove baseline lines that no longer occur",
    )
    parser.add_argument(
        "--accept-new",
        action="store_true",
        help="with --update-baseline, also add the new findings",
    )
    parser.add_argument(
        "--all", action="store_true", help="list baselined findings too"
    )
    args = parser.parse_args(argv)

    findings = lint()
    new, known, gone = compare(findings, read_baseline(BASELINE))
    if args.update_baseline:
        kept = known + new if args.accept_new else known
        write_baseline(kept, BASELINE)
        print(f"{BASELINE.name}: {len(kept)} findings, {len(gone)} removed")
        if new and not args.accept_new:
            for finding in new:
                print(finding)
            print(
                f"{len(new)} new findings were not added: fix them, or add "
                "--accept-new if they are deliberate.",
                file=sys.stderr,
            )
            return 1
        return 0
    for finding in new:
        print(finding)
    if args.all:
        for finding in known:
            print(f"{finding} (baseline)")
    for key in gone:
        rule, path, heading = key.split("\t")
        print(f"docs/{path}: {rule} fixed: remove '{heading}' from {BASELINE.name}")
    counts = Counter(f.rule for f in findings)
    print(
        f"{len(new)} new, {len(known)} in the baseline, {len(gone)} fixed "
        f"({', '.join(f'{r} {n}' for r, n in sorted(counts.items())) or 'no findings'})"
    )
    if new or gone:
        print(
            "Fix new findings; after fixing baselined ones, run with "
            "--update-baseline to drop their lines.",
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

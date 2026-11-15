"""Build the documentation corpus the AI assistant searches.

Mastermind's search_docs tool (waldur/waldur-mastermind#1204) searches the
documentation by section and leaves out, for end users, every section that
describes something switched off on their portal. This hook writes that corpus
(waldur/waldur-docs#37): one JSON line per section of the site's search index,

    {"path": "user-guide/end-users/personal-access-tokens.md",
     "anchor": "prerequisites", "title": ..., "breadcrumb": ..., "text": ...,
     "audience": "all" | "staff_support" | "staff",
     "requires": ["setting:PAT_ENABLED"], "boost": 1.5,
     "kind": "howto" | "concept" | "reference" | "", "context": ...}

and checks the tags on every build. What a section requires comes from, in
union:

- `tags` in docs-corpus.yml, by path and optionally section anchor, for pages
  synced from other repos;
- `requires:` in the page's front matter;
- `data-requires` on a heading (`## Get a token { data-requires="setting:PAT_ENABLED" }`),
  which also covers the headings below it.

What kind of section it is (`kind`) comes from `type:` in front matter or
`data-kind` on a heading, else from the `kind` rules in docs-corpus.yml, where
a heading in a how-to page that explains rather than instructs
(`concept_headings`) makes a concept section. Mastermind weights concept
sections up for questions worded as concept questions ("what is", "difference").

`context` holds the questions a section answers, from the file named by
`questions` in docs-corpus.yml (scripts/section_questions.py writes it). They
are searched but never shown: a user asks "how do I invite a colleague" of a
section titled "Add project members".

`corpus: false` in front matter, or `data-corpus="false"` on a heading, leaves
a page or section out. `mentions:` in front matter, or `data-mentions` on a
heading, says the page or section mentions a feature on purpose without
depending on it.

The corpus is written only when DOCS_CORPUS_OUT names a file, so an ordinary
build is not slowed down and the published site does not change. The checks run
on every build: an unknown term is an error, and an end-user section that
mentions a gated feature without being tagged for it is a warning (an error
under --strict).
"""

from __future__ import annotations

import gzip
import hashlib
import html
import json
import logging
import os
import re
from dataclasses import dataclass, field
from pathlib import Path

import yaml
from mkdocs.exceptions import PluginError

log = logging.getLogger("mkdocs.hooks.docs_corpus")

CONFIG_FILE = "docs-corpus.yml"
AUDIENCES = ("all", "staff_support", "staff")
KINDS = ("howto", "concept", "reference")
TERM_KINDS = ("setting", "feature", "offering_type", "capability")
# Sections shorter than this are headings with a link or two under them.
MIN_TEXT_LENGTH = 40

_HEADING = re.compile(r"<h([1-6])\b([^>]*)>", re.IGNORECASE)
_ATTR = re.compile(r'([\w-]+)="([^"]*)"')
_TAG = re.compile(r"<[^>]+>")


@dataclass
class PathTag:
    """Tags for synced pages, by path and optionally by section anchor."""

    pattern: re.Pattern
    anchor: re.Pattern | None
    requires: set[str]
    mentions: set[str]


@dataclass
class Rules:
    include: list[re.Pattern]
    exclude: list[re.Pattern]
    audience: list[tuple[re.Pattern, str]]
    boost: list[tuple[re.Pattern, float]]
    tags: list[PathTag]
    mentions: list[tuple[str, list[re.Pattern]]]
    vocabulary: str
    mentions_scope: list[re.Pattern] = field(default_factory=list)
    kind: list[tuple[re.Pattern, str]] = field(default_factory=list)
    concept_headings: re.Pattern | None = None
    questions: str = ""

    @classmethod
    def load(cls, path: Path) -> Rules:
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}

        def patterns(key):
            return [re.compile(p) for p in data.get(key) or []]

        return cls(
            include=patterns("include"),
            exclude=patterns("exclude"),
            audience=[
                (re.compile(r["pattern"]), r["audience"])
                for r in data.get("audience") or []
            ],
            boost=[
                (re.compile(r["pattern"]), float(r["boost"]))
                for r in data.get("boost") or []
            ],
            tags=[
                PathTag(
                    pattern=re.compile(r["pattern"]),
                    anchor=re.compile(r["anchor"]) if r.get("anchor") else None,
                    requires=split_terms(r.get("requires")),
                    mentions=split_terms(r.get("mentions")),
                )
                for r in data.get("tags") or []
            ],
            mentions=[
                (r["term"], [re.compile(p, re.IGNORECASE) for p in r["phrases"]])
                for r in data.get("mentions") or []
            ],
            vocabulary=data.get("vocabulary") or "",
            mentions_scope=patterns("mentions_scope"),
            kind=[
                (re.compile(r["pattern"]), r["kind"]) for r in data.get("kind") or []
            ],
            concept_headings=(
                re.compile(data["concept_headings"])
                if data.get("concept_headings")
                else None
            ),
            questions=data.get("questions") or "",
        )

    def in_scope(self, path: str) -> bool:
        return any(p.search(path) for p in self.include) and not any(
            p.search(path) for p in self.exclude
        )

    def checks_mentions(self, path: str) -> bool:
        return not self.mentions_scope or any(
            p.search(path) for p in self.mentions_scope
        )

    def audience_of(self, path: str) -> str:
        return next((a for p, a in self.audience if p.search(path)), "all")

    def kind_of(self, path: str, title: str, page_kind: str = "") -> str:
        """A section's kind: the page's own `type`, else the first `kind` rule
        for its path; in a how-to page, a heading that explains is a concept."""
        kind = page_kind or next((k for p, k in self.kind if p.search(path)), "")
        if (
            kind == "howto"
            and self.concept_headings
            and self.concept_headings.search(title)
        ):
            return "concept"
        return kind

    def boost_of(self, path: str) -> float | None:
        return next((b for p, b in self.boost if p.search(path)), None)

    def tags_of(self, path: str, anchor: str) -> tuple[set[str], set[str]]:
        """The (requires, mentions) the config gives a section of a page."""
        requires, mentions = set(), set()
        for tag in self.tags:
            if tag.pattern.search(path) and (
                tag.anchor is None or tag.anchor.fullmatch(anchor)
            ):
                requires |= tag.requires
                mentions |= tag.mentions
        return requires, mentions


@dataclass
class Heading:
    level: int
    anchor: str
    requires: set[str] = field(default_factory=set)
    mentions: set[str] = field(default_factory=set)
    excluded: bool = False
    kind: str = ""


@dataclass
class PageInfo:
    path: str
    title: str
    breadcrumb: list[str]
    requires: set[str]
    excluded: bool
    mentions: set[str] = field(default_factory=set)
    kind: str = ""
    # Effective tags per heading anchor, inherited from the headings above it.
    sections: dict[str, Heading] = field(default_factory=dict)


def split_terms(value) -> set[str]:
    """Terms from front matter (a list or a string) or a heading attribute."""
    if not value:
        return set()
    if isinstance(value, str):
        value = value.replace(",", " ").split()
    return {str(term).strip() for term in value if str(term).strip()}


def is_false(value) -> bool:
    return value is False or str(value).strip().lower() in ("false", "no", "exclude")


def heading_tags(html_text: str) -> list[Heading]:
    """Each heading with an id, carrying its own `data-*` tags only."""
    headings = []
    for match in _HEADING.finditer(html_text):
        attrs = dict(_ATTR.findall(match.group(2)))
        if "id" not in attrs:
            continue
        headings.append(
            Heading(
                level=int(match.group(1)),
                anchor=attrs["id"],
                requires=split_terms(attrs.get("data-requires")),
                mentions=split_terms(attrs.get("data-mentions")),
                excluded=is_false(attrs.get("data-corpus", "")),
                kind=attrs.get("data-kind", ""),
            )
        )
    return headings


def inherit(headings: list[Heading]) -> dict[str, Heading]:
    """Give each heading the tags of the headings it sits under."""
    stack: list[Heading] = []
    result = {}
    for heading in headings:
        while stack and stack[-1].level >= heading.level:
            stack.pop()
        effective = Heading(
            level=heading.level,
            anchor=heading.anchor,
            requires=set(heading.requires),
            mentions=set(heading.mentions),
            excluded=heading.excluded,
            kind=heading.kind,
        )
        if stack:
            parent = stack[-1]
            effective.requires |= parent.requires
            effective.mentions |= parent.mentions
            effective.excluded |= parent.excluded
            effective.kind = effective.kind or parent.kind
        stack.append(effective)
        result[heading.anchor] = effective
    return result


def clean(text: str) -> str:
    return " ".join(html.unescape(_TAG.sub(" ", text or "")).split())


def text_hash(text: str) -> str:
    """Short hash of a section's text, to tell which questions are stale."""
    return hashlib.sha256(text.encode()).hexdigest()[:8]


def term_error(term: str, vocabulary: dict[str, list[str]]) -> str | None:
    """Why a `requires` term is not valid, or None."""
    negated = term.startswith("!")
    kind, sep, key = term.lstrip("!").partition(":")
    if not sep or not key:
        return "is not of the form kind:key"
    if kind not in TERM_KINDS:
        return f"has an unknown kind {kind!r} (one of {', '.join(TERM_KINDS)})"
    if negated and kind != "feature":
        return "only feature terms can be negated"
    if key not in set(vocabulary.get(kind, [])):
        return f"names a {kind} that mastermind does not know"
    return None


def build_sections(
    index: dict,
    pages: dict[str, PageInfo],
    rules: Rules,
    questions: dict | None = None,
) -> list[dict]:
    """Corpus sections from a search index and the tags collected per page.

    `questions` maps a page path to {anchor: {"for": text hash, "questions": [...]}}.
    """
    questions = questions or {}
    sections = []
    for entry in index.get("docs", []):
        url, _, anchor = entry.get("location", "").partition("#")
        page = pages.get(url)
        if page is None or page.excluded or not anchor:
            continue
        heading = page.sections.get(anchor)
        if heading is not None and heading.excluded:
            continue
        text = clean(entry.get("text"))
        if len(text) < MIN_TEXT_LENGTH:
            continue
        title = clean(entry.get("title")) or page.title
        is_page_title = heading is not None and heading.level == 1
        crumb = page.breadcrumb if is_page_title else [*page.breadcrumb, page.title]
        config_requires, config_mentions = rules.tags_of(page.path, anchor)
        requires = (
            page.requires | config_requires | (heading.requires if heading else set())
        )
        mentions = (
            page.mentions | config_mentions | (heading.mentions if heading else set())
        )
        boost = rules.boost_of(page.path)
        if boost is None:
            boost = float(entry.get("boost", 1.0))
        kind = (heading.kind if heading else "") or rules.kind_of(
            page.path, title, page.kind
        )
        asked = (questions.get(page.path) or {}).get(anchor) or {}
        sections.append(
            {
                "path": page.path,
                "anchor": anchor,
                "title": title,
                "breadcrumb": " > ".join(c for c in crumb if c),
                "text": text,
                "audience": rules.audience_of(page.path),
                "requires": sorted(requires),
                "boost": boost,
                "kind": kind,
                "context": " ".join(asked.get("questions") or []),
                # Not part of the corpus: used by the checks.
                "_mentions": sorted(mentions),
                "_stale": bool(asked) and asked.get("for") != text_hash(text),
            }
        )
    return sections


def check_terms(sections: list[dict], vocabulary: dict) -> list[str]:
    errors = {}
    for section in sections:
        for term in [*section["requires"], *section["_mentions"]]:
            reason = term_error(term, vocabulary)
            if reason:
                errors.setdefault((section["path"], term), reason)
    return [
        f"{path}: requires term {term!r} {why}" for (path, term), why in errors.items()
    ]


def check_kinds(sections: list[dict]) -> list[str]:
    errors = {
        (s["path"], s["kind"]) for s in sections if s["kind"] and s["kind"] not in KINDS
    }
    return [
        f"{path}: kind {kind!r} is not one of {', '.join(KINDS)}"
        for path, kind in sorted(errors)
    ]


def check_mentions(sections: list[dict], rules: Rules) -> list[str]:
    """End-user sections that mention a gated feature they are not tagged for."""
    problems = []
    for section in sections:
        if section["audience"] != "all" or not rules.checks_mentions(section["path"]):
            continue
        tagged = set(section["requires"]) | set(section["_mentions"])
        haystack = f"{section['title']} {section['text']}"
        for term, phrases in rules.mentions:
            if term in tagged:
                continue
            match = next((m for p in phrases if (m := p.search(haystack))), None)
            if match:
                problems.append(
                    f"{section['path']}#{section['anchor']} mentions "
                    f"{match.group(0)!r} but is not tagged {term}: add "
                    f'{{ data-requires="{term}" }} to the heading if the section '
                    f'depends on it, or {{ data-mentions="{term}" }} if it only '
                    "refers to it"
                )
    return problems


def write_corpus(sections: list[dict], out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    # No name and mtime=0 in the gzip header: identical content, identical file.
    with (
        open(out, "wb") as raw,
        gzip.GzipFile(filename="", fileobj=raw, mode="wb", mtime=0) as gz,
    ):
        for section in sections:
            line = {k: v for k, v in section.items() if not k.startswith("_")}
            gz.write(
                (json.dumps(line, ensure_ascii=False, sort_keys=True) + "\n").encode()
            )


# --- MkDocs events ---------------------------------------------------------

_rules: Rules | None = None
_pages: dict[str, PageInfo] = {}


def on_config(config, **kwargs):
    global _rules
    _rules = Rules.load(Path(config.config_file_path).parent / CONFIG_FILE)
    for _, kind in _rules.kind:
        if kind not in KINDS:
            raise PluginError(f"{CONFIG_FILE}: unknown kind {kind!r}")
    _pages.clear()
    for _, audience in _rules.audience:
        if audience not in AUDIENCES:
            raise PluginError(f"{CONFIG_FILE}: unknown audience {audience!r}")
    return config


def on_page_content(html_text, page, **kwargs):
    path = page.file.src_uri
    if _rules is None or not _rules.in_scope(path):
        return html_text
    meta = page.meta or {}
    # MkDocs drops front matter it cannot parse without a word, which would
    # silently untag the page: an unquoted `- !feature:x` is a YAML tag.
    source = page.file.content_string
    if (
        source.startswith("---")
        and "requires:" in source.split("\n---", 2)[0]
        and "requires" not in meta
    ):
        log.warning(
            "docs corpus: %s has `requires:` in front matter that did not parse; "
            'quote terms that start with "!"',
            path,
        )
    _pages[page.url] = PageInfo(
        path=path,
        title=page.title or "",
        breadcrumb=[a.title for a in reversed(page.ancestors) if a.title],
        requires=split_terms(meta.get("requires")),
        excluded="corpus" in meta and is_false(meta["corpus"]),
        mentions=split_terms(meta.get("mentions")),
        kind=str(meta.get("type") or ""),
        sections=inherit(heading_tags(html_text)),
    )
    return html_text


def on_post_build(config, **kwargs):
    if _rules is None:
        return
    site = Path(config.site_dir)
    index_file = site / "search" / "search_index.json"
    if not index_file.exists():
        log.warning("docs corpus: no search index at %s", index_file)
        return
    index = json.loads(index_file.read_text(encoding="utf-8"))
    questions = {}
    if _rules.questions:
        questions_file = Path(config.config_file_path).parent / _rules.questions
        if questions_file.exists():
            questions = yaml.safe_load(questions_file.read_text(encoding="utf-8")) or {}
    sections = build_sections(index, _pages, _rules, questions)
    kind_errors = check_kinds(sections)
    if kind_errors:
        raise PluginError("docs corpus:\n  " + "\n  ".join(kind_errors))

    vocabulary_file = Path(config.docs_dir) / _rules.vocabulary
    if vocabulary_file.exists():
        vocabulary = json.loads(vocabulary_file.read_text(encoding="utf-8"))
        errors = check_terms(sections, vocabulary)
        if errors:
            raise PluginError(
                "docs corpus: unknown requires terms:\n  " + "\n  ".join(errors)
            )
    else:
        log.warning(
            "docs corpus: %s is missing, so requires terms were not checked",
            vocabulary_file,
        )

    for problem in check_mentions(sections, _rules):
        log.warning("docs corpus: %s", problem)

    out = os.environ.get("DOCS_CORPUS_OUT")
    if out:
        write_corpus(sections, Path(out))
        tagged = sum(1 for s in sections if s["requires"])
        if _rules.questions:
            asked = sum(1 for s in sections if s["context"])
            stale = sum(1 for s in sections if s["_stale"])
            log.info(
                "docs corpus: %d sections with questions, %d of them written for "
                "an older text (scripts/section_questions.py refreshes them)",
                asked,
                stale,
            )
        by_audience = {a: sum(s["audience"] == a for s in sections) for a in AUDIENCES}
        log.info(
            "docs corpus: %d sections (%d with requires, %s) written to %s",
            len(sections),
            tagged,
            ", ".join(f"{a} {n}" for a, n in by_audience.items()),
            out,
        )

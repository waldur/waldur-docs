"""Tests for hooks/docs_corpus.py. Run: uv run python -m unittest scripts/test_docs_corpus.py"""

import contextlib
import gzip
import io
import json
import os
import re
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "hooks"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import docs_corpus
import section_questions
from docs_corpus import PageInfo, Rules

VOCABULARY = {
    "setting": ["PAT_ENABLED", "MATRIX_ENABLED"],
    "feature": ["marketplace.show_call_management_functionality"],
    "offering_type": ["OpenStack.Tenant"],
    "capability": ["hpc"],
}

TEXT = "Enough words here to count as a section of the documentation."


def rules(**overrides):
    base = {
        "include": [re.compile(r"^user-guide/"), re.compile(r"^admin-guide/")],
        "exclude": [re.compile(r"(^|/)CHANGELOG\.md$")],
        "audience": [(re.compile(r"^admin-guide/"), "staff")],
        "boost": [],
        "tags": [],
        "mentions": [],
        "vocabulary": "",
    }
    base.update(overrides)
    return Rules(**base)


def page(path, html_text, requires=(), title="Page", excluded=False, kind=""):
    return PageInfo(
        path=path,
        title=title,
        breadcrumb=["Use Waldur"],
        requires=set(requires),
        excluded=excluded,
        kind=kind,
        sections=docs_corpus.inherit(docs_corpus.heading_tags(html_text)),
    )


def index(*entries):
    return {
        "docs": [
            {"location": loc, "title": title, "text": text}
            for loc, title, text in entries
        ]
    }


class HeadingTagsTest(unittest.TestCase):
    def test_section_tags_cover_the_headings_below(self):
        html_text = (
            '<h1 id="tokens">Tokens</h1>'
            '<h2 id="get" data-requires="setting:PAT_ENABLED">Get</h2>'
            '<h3 id="copy">Copy</h3>'
            '<h2 id="other">Other</h2>'
        )
        sections = docs_corpus.inherit(docs_corpus.heading_tags(html_text))
        self.assertEqual(sections["get"].requires, {"setting:PAT_ENABLED"})
        self.assertEqual(sections["copy"].requires, {"setting:PAT_ENABLED"})
        self.assertEqual(sections["other"].requires, set())
        self.assertEqual(sections["tokens"].requires, set())

    def test_excluded_heading_takes_its_subsections(self):
        html_text = (
            '<h2 id="a" data-corpus="false">A</h2><h3 id="b">B</h3><h2 id="c">C</h2>'
        )
        sections = docs_corpus.inherit(docs_corpus.heading_tags(html_text))
        self.assertTrue(sections["b"].excluded)
        self.assertFalse(sections["c"].excluded)

    def test_several_terms_in_one_attribute(self):
        html_text = (
            '<h2 id="a" data-requires="setting:PAT_ENABLED capability:hpc">A</h2>'
        )
        heading = docs_corpus.heading_tags(html_text)[0]
        self.assertEqual(heading.requires, {"setting:PAT_ENABLED", "capability:hpc"})


class BuildSectionsTest(unittest.TestCase):
    def test_page_and_heading_requires_are_combined(self):
        pages = {
            "user-guide/a/": page(
                "user-guide/a.md",
                '<h1 id="a">A</h1><h2 id="b" data-requires="capability:hpc">B</h2>',
                requires=["setting:PAT_ENABLED"],
            )
        }
        sections = docs_corpus.build_sections(
            index(("user-guide/a/#a", "A", TEXT), ("user-guide/a/#b", "B", TEXT)),
            pages,
            rules(),
        )
        by_anchor = {s["anchor"]: s for s in sections}
        self.assertEqual(by_anchor["a"]["requires"], ["setting:PAT_ENABLED"])
        self.assertEqual(
            by_anchor["b"]["requires"], ["capability:hpc", "setting:PAT_ENABLED"]
        )
        self.assertEqual(by_anchor["a"]["breadcrumb"], "Use Waldur")
        self.assertEqual(by_anchor["b"]["breadcrumb"], "Use Waldur > Page")

    def test_config_tags_a_synced_section_by_anchor(self):
        tag = docs_corpus.PathTag(
            pattern=re.compile(r"^user-guide/cli\.md$"),
            anchor=re.compile("token-types"),
            requires={"setting:PAT_ENABLED"},
            mentions=set(),
        )
        pages = {
            "user-guide/cli/": page(
                "user-guide/cli.md",
                '<h2 id="token-types">T</h2><h2 id="install">I</h2>',
            )
        }
        sections = docs_corpus.build_sections(
            index(
                ("user-guide/cli/#token-types", "T", TEXT),
                ("user-guide/cli/#install", "I", TEXT),
            ),
            pages,
            rules(tags=[tag]),
        )
        by_anchor = {s["anchor"]: s["requires"] for s in sections}
        self.assertEqual(
            by_anchor, {"token-types": ["setting:PAT_ENABLED"], "install": []}
        )

    def test_short_excluded_and_unknown_pages_are_left_out(self):
        pages = {
            "user-guide/a/": page(
                "user-guide/a.md",
                '<h2 id="x" data-corpus="false">X</h2><h2 id="y">Y</h2>',
            ),
            "user-guide/hidden/": page("user-guide/hidden.md", "", excluded=True),
        }
        sections = docs_corpus.build_sections(
            index(
                ("user-guide/a/", "A", TEXT),  # page entry without an anchor
                ("user-guide/a/#x", "X", TEXT),
                ("user-guide/a/#y", "Y", "too short"),
                ("user-guide/hidden/#z", "Z", TEXT),
                ("developer-guide/b/#c", "C", TEXT),
            ),
            pages,
            rules(),
        )
        self.assertEqual(sections, [])

    def test_html_is_stripped_and_audience_and_boost_set(self):
        pages = {"admin-guide/a/": page("admin-guide/a.md", '<h2 id="b">B</h2>')}
        sections = docs_corpus.build_sections(
            {
                "docs": [
                    {
                        "location": "admin-guide/a/#b",
                        "title": "<code>B</code>",
                        "text": f"<p>{TEXT} &amp; more</p>",
                        "boost": 0.3,
                    }
                ]
            },
            pages,
            rules(boost=[(re.compile(r"^user-guide/"), 2.0)]),
        )
        self.assertEqual(sections[0]["title"], "B")
        self.assertTrue(sections[0]["text"].endswith("& more"))
        self.assertEqual(sections[0]["audience"], "staff")
        self.assertEqual(sections[0]["boost"], 0.3)


class KindAndQuestionsTest(unittest.TestCase):
    KIND_RULES = [
        (re.compile(r"^about/concepts/"), "concept"),
        (re.compile(r"^user-guide/"), "howto"),
    ]

    def build(self, pages, entries, questions=None):
        return {
            s["anchor"]: s
            for s in docs_corpus.build_sections(
                index(*entries),
                pages,
                rules(
                    include=[re.compile(".")],
                    kind=self.KIND_RULES,
                    concept_headings=re.compile(r"^(What|When)\b"),
                ),
                questions,
            )
        }

    def test_kind_from_path_explaining_headings_page_type_and_heading(self):
        pages = {
            "user-guide/a/": page(
                "user-guide/a.md",
                '<h2 id="add">Add</h2><h2 id="what">What happens</h2>'
                '<h2 id="ref" data-kind="reference">Fields</h2><h3 id="sub">Sub</h3>',
            ),
            "user-guide/b/": page(
                "user-guide/b.md", '<h2 id="b">B</h2>', kind="reference"
            ),
            "about/concepts/c/": page("about/concepts/c.md", '<h2 id="c">C</h2>'),
            "other/d/": page("other/d.md", '<h2 id="d">D</h2>'),
        }
        sections = self.build(
            pages,
            [
                ("user-guide/a/#add", "Add a thing", TEXT),
                ("user-guide/a/#what", "What happens at a limit", TEXT),
                ("user-guide/a/#ref", "Fields", TEXT),
                ("user-guide/a/#sub", "Sub", TEXT),
                ("user-guide/b/#b", "B", TEXT),
                ("about/concepts/c/#c", "C", TEXT),
                ("other/d/#d", "D", TEXT),
            ],
        )
        self.assertEqual(
            {a: s["kind"] for a, s in sections.items()},
            {
                "add": "howto",
                "what": "concept",
                "ref": "reference",
                "sub": "reference",
                "b": "reference",
                "c": "concept",
                "d": "",
            },
        )

    def test_unknown_kind_is_an_error(self):
        sections = [{"path": "a.md", "kind": "tutorial"}, {"path": "b.md", "kind": ""}]
        self.assertEqual(len(docs_corpus.check_kinds(sections)), 1)

    def test_questions_become_context_and_stale_ones_are_marked(self):
        pages = {
            "user-guide/a/": page(
                "user-guide/a.md", '<h2 id="x">X</h2><h2 id="y">Y</h2>'
            )
        }
        questions = {
            "user-guide/a.md": {
                "x": {"for": docs_corpus.text_hash(TEXT), "questions": ["Q1?", "Q2?"]},
                "y": {"for": "00000000", "questions": ["Old?"]},
            }
        }
        sections = self.build(
            pages,
            [("user-guide/a/#x", "X", TEXT), ("user-guide/a/#y", "Y", TEXT)],
            questions,
        )
        self.assertEqual(sections["x"]["context"], "Q1? Q2?")
        self.assertFalse(sections["x"]["_stale"])
        # Stale questions are still used until they are written again.
        self.assertEqual(sections["y"]["context"], "Old?")
        self.assertTrue(sections["y"]["_stale"])


class SectionQuestionsScriptTest(unittest.TestCase):
    def test_plan_keeps_current_entries_and_asks_for_the_rest(self):
        sections = [
            {"path": "user-guide/a.md", "anchor": "x", "text": TEXT},
            {"path": "user-guide/a.md", "anchor": "y", "text": "changed " + TEXT},
            {"path": "user-guide/a.md", "anchor": "z", "text": TEXT},
            {"path": "admin-guide/b.md", "anchor": "w", "text": TEXT},
        ]
        current = {"for": docs_corpus.text_hash(TEXT), "questions": ["Q?"]}
        entries = {
            "user-guide/a.md": {"x": current, "y": current},
            "user-guide/gone.md": {"g": current},
        }
        todo, kept = section_questions.plan(
            sections, entries, [re.compile("^user-guide/")]
        )
        self.assertEqual([s["anchor"] for s in todo], ["y", "z"])
        # y is stale: kept until new questions replace it.
        self.assertEqual(dict(kept), {"user-guide/a.md": {"x": current, "y": current}})

    def test_an_interrupted_run_keeps_every_stale_entry(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "docs-corpus.yml").write_text(
                "questions: q.yml\nquestions_scope: ['^user-guide/']\n"
            )
            stale = {"for": "00000000", "questions": ["Hand-written?"]}
            entries = {a: stale for a in ("x", "y", "z")}
            (root / "q.yml").write_text(yaml.safe_dump({"user-guide/a.md": entries}))
            corpus = root / "c.jsonl.gz"
            with gzip.open(corpus, "wt") as f:
                for anchor in entries:
                    f.write(
                        json.dumps(
                            {
                                "path": "user-guide/a.md",
                                "anchor": anchor,
                                "title": anchor,
                                "breadcrumb": "",
                                "text": TEXT,
                            }
                        )
                        + "\n"
                    )

            def ask(self, prompt):
                raise KeyboardInterrupt

            env = {
                "DOCS_QUESTIONS_LLM_URL": "http://llm",
                "DOCS_QUESTIONS_LLM_MODEL": "m",
            }
            with (
                mock.patch.object(section_questions, "ROOT", root),
                mock.patch.object(
                    section_questions, "CONFIG", root / "docs-corpus.yml"
                ),
                mock.patch.object(section_questions.Client, "ask", ask),
                mock.patch.dict(os.environ, env),
                contextlib.redirect_stdout(io.StringIO()),
                self.assertRaises(KeyboardInterrupt),
            ):
                section_questions.main([str(corpus), "--workers", "1"])
            written = yaml.safe_load((root / "q.yml").read_text())["user-guide/a.md"]
            self.assertEqual(written, entries)

    def test_failed_refresh_keeps_the_stale_entry_and_a_bad_reply_does_not_stop_the_run(
        self,
    ):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "docs-corpus.yml").write_text(
                "questions: q.yml\nquestions_scope: ['^user-guide/']\n"
            )
            stale = {"for": "00000000", "questions": ["Hand-written?"]}
            (root / "q.yml").write_text(
                yaml.safe_dump({"user-guide/a.md": {"x": stale}})
            )
            corpus = root / "c.jsonl.gz"
            with gzip.open(corpus, "wt") as f:
                for anchor in ("x", "y"):
                    f.write(
                        json.dumps(
                            {
                                "path": "user-guide/a.md",
                                "anchor": anchor,
                                "title": anchor,
                                "breadcrumb": "",
                                "text": TEXT,
                            }
                        )
                        + "\n"
                    )

            def ask(self, prompt):
                if "> x" in prompt:
                    raise ValueError("not JSON")
                return '{"questions": ["New?"]}'

            env = {
                "DOCS_QUESTIONS_LLM_URL": "http://llm",
                "DOCS_QUESTIONS_LLM_MODEL": "m",
            }
            with (
                mock.patch.object(section_questions, "ROOT", root),
                mock.patch.object(
                    section_questions, "CONFIG", root / "docs-corpus.yml"
                ),
                mock.patch.object(section_questions.Client, "ask", ask),
                mock.patch.dict(os.environ, env),
                contextlib.redirect_stdout(io.StringIO()),
            ):
                self.assertEqual(section_questions.main([str(corpus)]), 1)
            written = yaml.safe_load((root / "q.yml").read_text())["user-guide/a.md"]
            self.assertEqual(written["x"], stale)
            self.assertEqual(written["y"]["questions"], ["New?"])

    def test_parse_questions(self):
        self.assertEqual(
            section_questions.parse_questions('ok {"questions": ["A?", " ", 3, "B?"]}'),
            ["A?", "B?"],
        )
        self.assertEqual(section_questions.parse_questions("no json"), [])
        self.assertEqual(section_questions.parse_questions(None), [])


class ChecksTest(unittest.TestCase):
    def section(self, **kw):
        base = {
            "path": "user-guide/a.md",
            "anchor": "b",
            "title": "B",
            "text": TEXT,
            "audience": "all",
            "requires": [],
            "_mentions": [],
        }
        base.update(kw)
        return base

    def test_unknown_terms_are_reported_with_the_page(self):
        errors = docs_corpus.check_terms(
            [
                self.section(
                    requires=[
                        "setting:NOPE",
                        "feature:marketplace.show_call_management_functionality",
                        "!setting:PAT_ENABLED",
                        "bogus",
                    ]
                )
            ],
            VOCABULARY,
        )
        self.assertEqual(len(errors), 3)
        self.assertTrue(all(e.startswith("user-guide/a.md:") for e in errors))

    def test_negated_feature_is_valid(self):
        self.assertIsNone(
            docs_corpus.term_error(
                "!feature:marketplace.show_call_management_functionality", VOCABULARY
            )
        )

    def test_untagged_mention_is_flagged_for_end_users_only(self):
        r = rules(
            mentions=[
                (
                    "setting:PAT_ENABLED",
                    [re.compile(r"personal access tokens?", re.IGNORECASE)],
                )
            ]
        )
        text = "Open Personal access tokens from the user menu, which has more words."
        flagged = docs_corpus.check_mentions([self.section(text=text)], r)
        self.assertEqual(len(flagged), 1)
        self.assertIn("setting:PAT_ENABLED", flagged[0])
        self.assertEqual(
            docs_corpus.check_mentions([self.section(text=text, audience="staff")], r),
            [],
        )
        self.assertEqual(
            docs_corpus.check_mentions(
                [self.section(text=text, requires=["setting:PAT_ENABLED"])], r
            ),
            [],
        )
        self.assertEqual(
            docs_corpus.check_mentions(
                [self.section(text=text, _mentions=["setting:PAT_ENABLED"])], r
            ),
            [],
        )


class WriteCorpusTest(unittest.TestCase):
    def test_output_is_reproducible_and_drops_private_keys(self):
        sections = [
            {
                "path": "user-guide/a.md",
                "anchor": "b",
                "_mentions": ["x"],
                "requires": [],
            }
        ]
        with tempfile.TemporaryDirectory() as tmp:
            first, second = Path(tmp, "1.gz"), Path(tmp, "2.gz")
            docs_corpus.write_corpus(sections, first)
            docs_corpus.write_corpus(sections, second)
            self.assertEqual(first.read_bytes(), second.read_bytes())
            with gzip.open(first, "rt") as stream:
                line = json.loads(stream.readline())
            self.assertNotIn("_mentions", line)


class ConceptHeadingsTest(unittest.TestCase):
    def test_explaining_headings_but_not_instructions(self):
        root = Path(__file__).resolve().parent.parent
        pattern = Rules.load(root / docs_corpus.CONFIG_FILE).concept_headings
        for title in (
            "How billing works",
            "How resource slugs work",
            "What happens at a limit",
            "Quotas vs policies",
        ):
            self.assertTrue(pattern.search(title), title)
        for title in (
            "How to work with volumes",
            "How do I work with keys",
            "Create a project",
        ):
            self.assertFalse(pattern.search(title), title)


class ConfigTest(unittest.TestCase):
    def test_repository_config_loads_and_its_terms_are_known(self):
        root = Path(__file__).resolve().parent.parent
        r = Rules.load(root / docs_corpus.CONFIG_FILE)
        vocabulary = json.loads((root / "docs" / r.vocabulary).read_text())
        terms = {t for tag in r.tags for t in tag.requires | tag.mentions} | {
            t for t, _ in r.mentions
        }
        for term in terms:
            self.assertIsNone(docs_corpus.term_error(term, vocabulary), term)


if __name__ == "__main__":
    unittest.main()

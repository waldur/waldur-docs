"""Tests for scripts/lint_docs_structure.py. Run: uv run python -m unittest scripts/test_lint_docs_structure.py"""

import contextlib
import io
import re
import sys
import tempfile
import unittest
from collections import Counter
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "hooks"))

import docs_corpus
import lint_docs_structure as lint
from lint_docs_structure import Finding, Rules

RULES = Rules(
    corpus=docs_corpus.Rules(
        include=[re.compile(".")],
        exclude=[],
        audience=[],
        boost=[],
        tags=[],
        mentions=[],
        vocabulary="",
        kind=[
            (re.compile("^about/concepts/"), "concept"),
            (re.compile("^user-guide/"), "howto"),
        ],
        concept_headings=re.compile(r"^(What|When)\b"),
    ),
    scope=[re.compile("^(user-guide|about)/")],
)
WORDS = "Enough words to make a section. " * 5


def rules_of(path, text):
    return [(f.rule, f.heading) for f in lint.lint_page(path, text, RULES)]


class RulesTest(unittest.TestCase):
    def test_stemmed_gerund(self):
        text = f"# Members\n\n## Adding members\n\n{WORDS}\n\n## Configuring roles\n\n{WORDS}\n"
        self.assertEqual(
            rules_of("user-guide/a.md", text), [("DS001", "Adding members")]
        )

    def test_noun_task_heading_only_in_how_to_pages(self):
        text = (
            f"# Projects\n\n## Project creation\n\n{WORDS}\n\n"
            f"## Create a project\n\n{WORDS}\n\n## Managing project creation\n\n{WORDS}\n\n"
            f"## What happens on submission\n\n{WORDS}\n\n## Defaults on call creation\n\n{WORDS}\n"
        )
        self.assertEqual(
            rules_of("user-guide/a.md", text), [("DS002", "Project creation")]
        )
        self.assertNotIn(
            "DS002", [r for r, _ in rules_of("about/terminology/a.md", text)]
        )

    def test_generic_heading_ignores_step_numbers(self):
        text = f"# Calls\n\n## Overview\n\n{WORDS}\n\n## Step 1: Details\n\n{WORDS}\n"
        self.assertEqual(
            rules_of("user-guide/a.md", text),
            [("DS003", "Overview"), ("DS003", "Step 1: Details")],
        )

    def test_long_section_counts_its_own_text_up_to_the_next_heading(self):
        long = "word " * (lint.LONG_SECTION_WORDS + 1)
        half = "word " * (lint.LONG_SECTION_WORDS // 2)
        flat = f"# P\n\n## Limits\n\n{long}\n"
        long_intro = f"# P\n\n## Limits\n\n{long}\n\n### Daily limits\n\n{WORDS}\n"
        split = f"# P\n\n## Limits\n\n{half}\n\n### Daily limits\n\n{half}\n"
        self.assertEqual(rules_of("user-guide/a.md", flat), [("DS004", "Limits")])
        self.assertEqual(rules_of("user-guide/a.md", long_intro), [("DS004", "Limits")])
        self.assertEqual(rules_of("user-guide/a.md", split), [])

    def test_code_blocks_are_not_headings_or_words(self):
        code = "```\n# Adding a comment\n" + "word " * 600 + "\n```\n"
        self.assertEqual(rules_of("user-guide/a.md", f"# P\n\n## Run it\n\n{code}"), [])

    def test_positional_reference_unless_the_object_is_in_the_section(self):
        across = "# P\n\n## Roles\n\n| a | b |\n|---|---|\n\n## Use\n\nSee the table above.\n"
        within = (
            "# P\n\n## Roles\n\n| a | b |\n|---|---|\n\nThe table above lists roles.\n"
        )
        layout = "# P\n\n## Profile\n\nClick the banner shown above the tabs.\n"
        self.assertEqual(rules_of("user-guide/a.md", across), [("DS005", "Use")])
        self.assertEqual(rules_of("user-guide/a.md", within), [])
        self.assertEqual(rules_of("user-guide/a.md", layout), [])

    def test_concept_page_needs_a_section_worded_as_its_question(self):
        unasked = f"# Offerings\n\n## Plans\n\n{WORDS}\n"
        asked = f"# Offerings\n\n## What is an offering\n\n{WORDS}\n"
        self.assertEqual(
            rules_of("about/concepts/a.md", unasked), [("DS006", "Offerings")]
        )
        self.assertEqual(rules_of("about/concepts/a.md", asked), [])
        self.assertEqual(
            rules_of("user-guide/a.md", "---\ntype: concept\n---\n" + unasked),
            [("DS006", "Offerings")],
        )

    def test_excluded_pages_and_sections_are_skipped(self):
        self.assertEqual(
            rules_of(
                "user-guide/a.md", "---\ncorpus: false\n---\n# P\n\n## Overview\n\nx\n"
            ),
            [],
        )
        text = (
            '# P\n\n## Related { data-corpus="false" }\n\n### Overview\n\nx\n\n'
            "## Notes\n\nx\n"
        )
        self.assertEqual(rules_of("user-guide/a.md", text), [("DS003", "Notes")])
        external = "<!-- EXTERNAL DOCUMENT -->\n# P\n\n## Overview\n\nx\n"
        self.assertEqual(rules_of("user-guide/a.md", external), [])
        # Every value the corpus hook takes as "leave out".
        for value in ("false", "no", "exclude"):
            text = (
                f'# P\n\n## Related {{ data-corpus="{value}" }}\n\n### Overview\n\nx\n'
            )
            self.assertEqual(rules_of("user-guide/a.md", text), [], value)

    def test_kind_follows_the_corpus_hook(self):
        # data-kind covers the headings below; an explaining heading in a
        # how-to page is a concept section; neither is a task heading.
        text = (
            '# P\n\n## Fields { data-kind="reference" }\n\nx\n\n'
            "### Project creation\n\nx\n\n## When registration ends\n\nx\n\n"
            "## Project creation\n\nx\n"
        )
        self.assertEqual(
            rules_of("user-guide/a.md", text), [("DS002", "Project creation")]
        )

    def test_line_numbers_count_front_matter(self):
        text = "---\nrequires:\n  - setting:X\n---\n# P\n\n## Overview\n\nx\n"
        (finding,) = lint.lint_page("user-guide/a.md", text, RULES)
        self.assertEqual(finding.line, 7)


class BaselineTest(unittest.TestCase):
    def finding(self, heading):
        return Finding("DS003", "user-guide/a.md", 1, heading, "")

    def test_new_known_and_fixed(self):
        findings = [self.finding("Overview"), self.finding("Notes")]
        baseline = Counter([self.finding("Overview").key, self.finding("Details").key])
        new, known, gone = lint.compare(findings, baseline)
        self.assertEqual([f.heading for f in new], ["Notes"])
        self.assertEqual([f.heading for f in known], ["Overview"])
        self.assertEqual(gone, [self.finding("Details").key])

    def test_a_second_occurrence_is_new(self):
        findings = [self.finding("Overview"), self.finding("Overview")]
        new, known, _ = lint.compare(findings, Counter([self.finding("Overview").key]))
        self.assertEqual((len(new), len(known)), (1, 1))


class UpdateBaselineTest(unittest.TestCase):
    def run_main(self, findings, baseline_lines, *args):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "baseline.txt"
            path.write_text("\n".join(baseline_lines) + "\n")
            with (
                mock.patch.object(lint, "BASELINE", path),
                mock.patch.object(lint, "lint", return_value=findings),
                contextlib.redirect_stdout(io.StringIO()),
                contextlib.redirect_stderr(io.StringIO()),
            ):
                code = lint.main(["--update-baseline", *args])
            return code, read(path)

    def test_drops_fixed_lines_and_never_adds_new_ones(self):
        old = Finding("DS003", "user-guide/a.md", 1, "Overview", "")
        fixed = Finding("DS003", "user-guide/a.md", 1, "Details", "")
        new = Finding("DS003", "user-guide/a.md", 1, "Notes", "")
        code, lines = self.run_main([old, new], [old.key, fixed.key])
        self.assertEqual((code, lines), (1, [old.key]))
        code, lines = self.run_main([old, new], [old.key], "--accept-new")
        self.assertEqual((code, lines), (0, sorted([old.key, new.key])))


def read(path):
    return [
        line
        for line in path.read_text().splitlines()
        if line and not line.startswith("#")
    ]


class RepositoryTest(unittest.TestCase):
    def test_docs_match_the_baseline(self):
        new, _, gone = lint.compare(lint.lint(), lint.read_baseline())
        self.assertEqual([str(f) for f in new], [])
        self.assertEqual(gone, [])


if __name__ == "__main__":
    unittest.main()

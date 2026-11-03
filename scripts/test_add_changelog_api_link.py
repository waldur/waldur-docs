"""Tests for add-changelog-api-link.py.

Run with: python3 -m unittest scripts/test_add_changelog_api_link.py
"""

import importlib.util
import tempfile
import unittest
from pathlib import Path

_SPEC = importlib.util.spec_from_file_location(
    "add_changelog_api_link",
    Path(__file__).resolve().parent / "add-changelog-api-link.py",
)
link_script = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(link_script)

SCHEMA = "- [OpenAPI Schema](../API/waldur-openapi-schema-8.1.4.yaml)"
CHANGES = (
    "- [API changes](https://api-docs.waldur.com/8.1.4/integrator-guide/APIs/"
    "api-changes/waldur-openapi-schema-8.1.4-diff/)"
)

ENTRY = """\
## 8.1.4 - 2026-11-10

### Highlights

- Something new.

---

## 8.1.3 - 2026-10-13

### Highlights

- Something older.

### Resources

- [OpenAPI Schema](../API/waldur-openapi-schema-8.1.3.yaml)

---
"""


def entry_of(text, version):
    start = text.index(f"## {version}")
    end = text.find("\n## ", start + 1)
    return text[start : end if end != -1 else len(text)]


class AddLinksTest(unittest.TestCase):
    def test_new_release_gets_a_resources_section_with_both_links(self):
        text, added = link_script.add_links(ENTRY, "8.1.4")
        self.assertEqual(added, [SCHEMA, CHANGES])
        entry = entry_of(text, "8.1.4")
        self.assertIn(f"### Resources\n\n{SCHEMA}\n{CHANGES}\n\n---", entry)

    def test_other_entries_are_untouched(self):
        text, _ = link_script.add_links(ENTRY, "8.1.4")
        self.assertEqual(entry_of(text, "8.1.3"), entry_of(ENTRY, "8.1.3"))

    def test_older_release_gets_only_the_missing_link(self):
        text, added = link_script.add_links(ENTRY, "8.1.3")
        changes = CHANGES.replace("8.1.4", "8.1.3")
        self.assertEqual(added, [changes])
        entry = entry_of(text, "8.1.3")
        self.assertIn(
            "- [OpenAPI Schema](../API/waldur-openapi-schema-8.1.3.yaml)\n"
            f"{changes}\n\n---",
            entry,
        )
        self.assertEqual(entry.count("### Resources"), 1)

    def test_site_version_links_through_another_build(self):
        text, added = link_script.add_links(ENTRY, "8.1.3", site_version="latest")
        self.assertEqual(
            added,
            [
                "- [API changes](https://api-docs.waldur.com/latest/integrator-guide/"
                "APIs/api-changes/waldur-openapi-schema-8.1.3-diff/)"
            ],
        )
        # Either form counts as linked: a later run adds no second link.
        _, again = link_script.add_links(text, "8.1.3")
        self.assertEqual(again, [])

    def test_rerun_is_a_no_op(self):
        once, _ = link_script.add_links(ENTRY, "8.1.4")
        twice, added = link_script.add_links(once, "8.1.4")
        self.assertEqual(added, [])
        self.assertEqual(twice, once)

    def test_last_entry_without_a_rule(self):
        text, added = link_script.add_links("## 8.1.4 - 2026-11-10\n\n- x\n", "8.1.4")
        self.assertEqual(added, [SCHEMA, CHANGES])
        self.assertTrue(
            text.endswith(f"- x\n\n### Resources\n\n{SCHEMA}\n{CHANGES}\n\n")
        )

    def test_missing_entry_is_an_error(self):
        with self.assertRaises(link_script.MissingEntry):
            link_script.add_links(ENTRY, "8.1.5")


class VerifyReleaseTest(unittest.TestCase):
    def test_verifier_checks_the_url_this_script_links(self):
        spec = importlib.util.spec_from_file_location(
            "verify_release_complete",
            Path(__file__).resolve().parent / "verify-release-complete.py",
        )
        verify = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(verify)
        self.assertEqual(
            verify.api_changes_url("8.1.4"), link_script.api_changes_url("8.1.4")
        )


class MainTest(unittest.TestCase):
    def test_writes_the_changelog(self):
        with tempfile.TemporaryDirectory() as tmp:
            changelog = Path(tmp) / "CHANGELOG.md"
            changelog.write_text(ENTRY, encoding="utf-8")
            self.assertEqual(link_script.main(["8.1.4"], changelog), 0)
            self.assertIn(CHANGES, changelog.read_text(encoding="utf-8"))

    def test_refuses_release_candidates(self):
        with tempfile.TemporaryDirectory() as tmp:
            changelog = Path(tmp) / "CHANGELOG.md"
            changelog.write_text(ENTRY, encoding="utf-8")
            self.assertEqual(link_script.main(["8.1.4-rc.1"], changelog), 1)
            self.assertEqual(changelog.read_text(encoding="utf-8"), ENTRY)

    def test_missing_entry_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            changelog = Path(tmp) / "CHANGELOG.md"
            changelog.write_text(ENTRY, encoding="utf-8")
            self.assertEqual(link_script.main(["8.1.5"], changelog), 1)


if __name__ == "__main__":
    unittest.main()

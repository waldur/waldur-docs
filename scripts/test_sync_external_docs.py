"""Tests for sync-external-docs.py.

Links and the external marker are the two things the sync writes rather than
copies. Every link rule here exists because a link that made sense in the
source repository did not survive the move into this one.
"""

import contextlib
import importlib.util
import io
import os
import tempfile
import unittest
from pathlib import Path

_spec = importlib.util.spec_from_file_location(
    "sync_external_docs", Path(__file__).parent / "sync-external-docs.py"
)
sync_external_docs = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(sync_external_docs)


class RewriteLinksTest(unittest.TestCase):
    """Exercises ExternalDocSyncer.rewrite_links against a two-mapping source."""

    def setUp(self):
        # __new__ rather than the constructor: rewrite_links needs no config,
        # and the constructor would go looking for external-sources.yml.
        self.syncer = sync_external_docs.ExternalDocSyncer.__new__(
            sync_external_docs.ExternalDocSyncer
        )
        self.docs_mapping = {"remote": "docs/", "local": "docs/developer-guide"}
        self.admin_mapping = {
            "remote": "docs/admin",
            "local": "docs/admin-guide/configuration",
        }
        self.source = {"mappings": [self.docs_mapping, self.admin_mapping]}

        # The out-of-subtree rule consults the local tree, so tests run against
        # a scratch directory rather than the checkout they happen to sit in.
        self._cwd = os.getcwd()
        self._tmp = tempfile.TemporaryDirectory()
        os.chdir(self._tmp.name)

    def tearDown(self):
        os.chdir(self._cwd)
        self._tmp.cleanup()

    def rewrite(self, content, mapping=None, rel_file_path="guide.md"):
        return self.syncer.rewrite_links(
            content, self.source, mapping or self.docs_mapping, rel_file_path
        )

    def touch(self, path):
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        Path(path).write_text("stub")

    def test_link_within_the_same_mapping_is_untouched(self):
        content = "See [the theme](theme.md) for details."
        self.assertEqual(self.rewrite(content), content)

    def test_link_across_mappings_is_repointed_at_the_local_path(self):
        content = "See [config](admin/configuration-guide.md)."
        self.assertEqual(
            self.rewrite(content),
            "See [config](../admin-guide/configuration/configuration-guide.md).",
        )

    def test_link_out_of_the_synced_subtree_keeps_its_text(self):
        # `../apps/...` from a `docs/` mapping: nothing outside docs/ is copied,
        # so no local path can be formed and mkdocs --strict aborts on the link.
        content = "See [`apps/poc/README.md`](../apps/poc/README.md) for more."
        self.assertEqual(self.rewrite(content), "See `apps/poc/README.md` for more.")

    def test_link_out_of_the_subtree_is_kept_when_it_resolves_locally(self):
        # The local tree keeps enough of the source repo's shape that some of
        # these land on a hand-written page. Those links work — leave them.
        self.touch("docs/CHANGELOG.md")
        content = "Check the [CHANGELOG](../CHANGELOG.md) first."
        self.assertEqual(self.rewrite(content), content)

    def test_image_out_of_the_subtree_is_left_as_a_broken_link(self):
        # Alt text is no substitute for the image, so a missing one stays a loud
        # build failure instead of silently vanishing from the page.
        content = "![Architecture](../assets/architecture.png)"
        self.assertEqual(self.rewrite(content), content)

    def test_external_and_absolute_links_are_untouched(self):
        content = (
            "[site](https://example.com/x.md) [root](/index.md) "
            "[anchor](#section) [mail](mailto:x@example.com)"
        )
        self.assertEqual(self.rewrite(content), content)

    def test_anchor_is_preserved_when_repointing_across_mappings(self):
        content = "See [config](admin/configuration-guide.md#plugins)."
        self.assertEqual(
            self.rewrite(content),
            "See [config](../admin-guide/configuration/configuration-guide.md#plugins).",
        )

    def test_single_mapping_source_still_degrades_out_of_subtree_links(self):
        # Regression guard: rewrite_links used to return early whenever a source
        # had fewer than two mappings, which skipped this rule entirely for the
        # single-mapping sources — the case that broke the build.
        source = {"mappings": [self.docs_mapping]}
        content = "See [`apps/poc`](../apps/poc) for a concrete example."
        self.assertEqual(
            self.syncer.rewrite_links(content, source, self.docs_mapping, "guide.md"),
            "See `apps/poc` for a concrete example.",
        )


class ExternalMarkerTest(unittest.TestCase):
    """Exercises where add_external_marker puts the marker and reading it back.

    MkDocs titles a page by its H1 only when the H1 is the page's first
    element; anything above it, this comment included, makes MkDocs fall back
    to a title made from the filename.
    """

    def setUp(self):
        self.syncer = sync_external_docs.ExternalDocSyncer.__new__(
            sync_external_docs.ExternalDocSyncer
        )
        self.syncer.external_marker = "<!-- EXTERNAL DOCUMENT\nSource: {repository}\nLast Sync: {sync_time}\n-->\n"
        self.mapping = {"remote": "docs/", "local": "docs/developer-guide"}
        self.source = {"repository": "https://example.com/repo.git", "branch": "main"}
        self.temp_dir = Path("/checkout")

    def add_marker(self, content):
        return self.syncer.add_external_marker(
            content,
            self.source,
            self.mapping,
            self.temp_dir / "docs" / "guide.md",
            self.temp_dir,
            "2026-10-17T00:00:00",
        )

    def test_marker_goes_below_a_leading_title(self):
        content = self.add_marker("# Matrix chat with Helm\n\nBody.\n")
        self.assertTrue(
            content.startswith("# Matrix chat with Helm\n\n<!-- EXTERNAL DOCUMENT")
        )

    def test_marker_stays_on_top_of_a_page_without_a_leading_title(self):
        content = self.add_marker("Intro.\n\n# Later title\n")
        self.assertTrue(content.startswith("<!-- EXTERNAL DOCUMENT"))

    def test_reading_the_marker_back_gives_the_source_unchanged(self):
        # A page that reads back different from its source counts as changed,
        # so it would be restamped and committed on every sync. How the
        # template ends is up to its YAML block style (`|-`, `|` or `|+`).
        template = self.syncer.external_marker.rstrip("\n")
        for ending in ("", "\n", "\n\n"):
            self.syncer.external_marker = template + ending
            for source in (
                "# Title\n\nBody.\n",
                "# Title\nBody right below.\n",
                "# Title\n\n\nTwo blank lines.\n",
                "Intro without a title.\n",
            ):
                with self.subTest(ending=ending, source=source):
                    marked = self.add_marker(source)
                    self.assertEqual(
                        self.syncer.extract_content_without_marker(marked), source
                    )

    def test_a_page_synced_with_the_marker_on_top_is_still_read(self):
        old = self.syncer.external_marker + "\n\n# Title\n\nBody.\n"
        self.assertEqual(
            self.syncer.extract_content_without_marker(old), "# Title\n\nBody.\n"
        )

    def test_sync_timestamp_is_read_below_the_title(self):
        marked = self.add_marker("# Title\n\nBody.\n")
        self.assertEqual(
            self.syncer.extract_existing_marker_timestamp(marked), "2026-10-17T00:00:00"
        )


class SyncMappingTest(unittest.TestCase):
    """Runs sync_mapping from a scratch checkout into a scratch docs tree."""

    def setUp(self):
        self.syncer = sync_external_docs.ExternalDocSyncer.__new__(
            sync_external_docs.ExternalDocSyncer
        )
        self.syncer.dry_run = False
        self.syncer.preserve_local = []
        self.syncer.external_marker = (
            "<!-- EXTERNAL DOCUMENT\nLast Sync: {sync_time}\n-->\n"
        )
        # The single-file path serves the README.md -> index.md mappings and the
        # directory path the rest; each decides on its own when to write
        self.mappings = (
            {"remote": "docs/", "local": "docs/developer-guide"},
            {"remote": "docs/guide.md", "local": "docs/developer-guide/guide.md"},
        )

        self._cwd = os.getcwd()
        self._tmp = tempfile.TemporaryDirectory()
        os.chdir(self._tmp.name)
        self.checkout = Path("checkout")
        (self.checkout / "docs").mkdir(parents=True)
        (self.checkout / "docs" / "guide.md").write_text("# Title\n\nBody.\n")
        self.page = Path("docs/developer-guide/guide.md")

    def tearDown(self):
        os.chdir(self._cwd)
        self._tmp.cleanup()

    def sync(self, mapping):
        source = {
            "repository": "https://example.com/repo.git",
            "branch": "main",
            "mappings": [mapping],
        }
        with contextlib.redirect_stdout(io.StringIO()):
            self.syncer.sync_mapping(source, mapping, self.checkout)

    def test_a_page_synced_with_the_marker_on_top_moves_it_below_the_title(self):
        # The source did not change, so only the layout tells the sync to write
        old_marker = self.syncer.external_marker.format(sync_time="2026-01-01")
        for mapping in self.mappings:
            with self.subTest(mapping=mapping["remote"]):
                self.page.parent.mkdir(parents=True, exist_ok=True)
                self.page.write_text(old_marker + "\n\n# Title\n\nBody.\n")

                self.sync(mapping)

                self.assertEqual(
                    self.page.read_text(), "# Title\n\n" + old_marker + "\n\nBody.\n"
                )

    def test_a_second_sync_of_an_unchanged_source_leaves_the_page_alone(self):
        for mapping in self.mappings:
            with self.subTest(mapping=mapping["remote"]):
                self.page.unlink(missing_ok=True)
                self.sync(mapping)
                first = self.page.read_text()

                self.sync(mapping)

                self.assertEqual(self.page.read_text(), first)


if __name__ == "__main__":
    unittest.main()

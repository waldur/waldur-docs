"""Tests for relative-link handling in sync-external-docs.py.

Links are the one thing the sync rewrites rather than copies, and every rule
here exists because a link that made sense in the source repository did not
survive the move into this one.
"""

import importlib.util
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


if __name__ == "__main__":
    unittest.main()

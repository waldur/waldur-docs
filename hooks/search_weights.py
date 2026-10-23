"""Weight pages in the search index by what kind of page they are.

Search ranks a section almost entirely on whether its title contains the query
term (titles carry a 1000x boost), so a page made of hundreds of short,
identifier-titled sections outranks the guide a reader is looking for: "invoice"
returned two message templates before any billing page, and "create project"
put the guide 33rd behind CLI reference and configuration constants.

Most of these pages are synced from other repositories, so the weights are set
here by path rather than in each page's front matter. A page that sets
`search:` in its own front matter keeps it.
"""

import re

# Pages that are not documentation a reader searches for.
EXCLUDE = [
    re.compile(r"(^|/)tests/"),
    re.compile(r"(^|/)LICENCE\.md$"),
]

# First match wins. Below 1 sinks a page, above 1 lifts it.
BOOST = [
    (re.compile(r"(^|/)CHANGELOG\.md$"), 0.1),
    # Generated reference: one section per command, template, setting or job
    (re.compile(r"^integrator-guide/waldur-cli/docs/reference/"), 0.3),
    (
        re.compile(
            r"^admin-guide/mastermind-configuration/(templates|notifications|scheduled)\.md$"
        ),
        0.3,
    ),
    (re.compile(r"^developer-guide/(handlers|mixins)\.md$"), 0.3),
    # Task-oriented guides. Kept small: a query matches pages on any of its
    # words, so a larger lift lets a guide sharing one word ("manager" in
    # "cert-manager") outrank the operator page that answers the query.
    (re.compile(r"^user-guide/"), 1.5),
    (re.compile(r"^get-started/"), 1.5),
]


def search_meta(src_uri):
    """Return the `search` page meta for a docs-relative source path, or None."""
    if any(pattern.search(src_uri) for pattern in EXCLUDE):
        return {"exclude": True}
    for pattern, boost in BOOST:
        if pattern.search(src_uri):
            return {"boost": boost}
    return None


def on_page_markdown(markdown, page, **kwargs):
    meta = search_meta(page.file.src_uri)
    if meta and "search" not in page.meta:
        page.meta["search"] = meta
    return markdown

#!/usr/bin/env python3
"""Add the OpenAPI schema and API changes links to a released version's changelog entry.

Run by the `Generate OpenAPI schema` CI job immediately after it writes
docs/API/waldur-openapi-schema-<version>.yaml, so that the schema link and the
file it points at are staged into the SAME commit.

Why it is not done in scripts/release.sh: the schema is built from
waldur-mastermind's tag pipeline, which does not exist until this tag's
`release` stage has run. A link committed alongside the changelog would
therefore dangle for the whole release, and a dangling relative link aborts
`mkdocs build --strict` — on master and, because the entry sits on master, in
every open merge request. See scripts/check-changelog-api-links.py, which
guards against exactly that.

The API changes link points at the release's page on api-docs.waldur.com, which
waldur/api-docs renders from the schema diff once this pipeline's `Generate and
release API docs` trigger has run (waldur-mastermind#399). It is absolute, so
`mkdocs build --strict` does not resolve it, and it is added in the same commit
rather than after the trigger: the commit lands on master, which only reaches
docs.waldur.com on a later master deploy, long after the trigger has finished.
`Verify release completed` fails the release if the page is not served.

RC releases ship no schema, so this script is never run for them (the CI job's
rules match stable tags only) and it refuses to run if asked.

Idempotent: each link is added only if the entry does not carry it yet, so a
retried job commits nothing, and running it for an older release adds just the
link that entry lacks.

Exit status: 0 on success or no-op, 1 on a malformed argument or a missing
changelog entry. A missing entry is deliberately fatal — a stable release must
not ship without a link to its API contract.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
CHANGELOG = PROJECT_DIR / "docs" / "about" / "CHANGELOG.md"

STABLE_VERSION_RE = re.compile(r"^\d+\.\d+\.\d+$")

API_DOCS_URL = "https://api-docs.waldur.com"

RESOURCES_HEADING = "### Resources"


class MissingEntry(Exception):
    pass


def api_changes_url(version: str, site_version: str | None = None) -> str:
    """The release's API changes page on api-docs.waldur.com.

    Served from the release's own versioned build by default. Releases older
    than 8.1.0 have no versioned build there, but every build carries all
    earlier pages, so their entries link through ``site_version="latest"``.
    """
    return (
        f"{API_DOCS_URL}/{site_version or version}/integrator-guide/APIs/"
        f"api-changes/waldur-openapi-schema-{version}-diff/"
    )


def release_links(version: str, site_version: str | None = None) -> list:
    return [
        f"- [OpenAPI Schema](../API/waldur-openapi-schema-{version}.yaml)",
        f"- [API changes]({api_changes_url(version, site_version)})",
    ]


def add_links(text: str, version: str, site_version: str | None = None) -> tuple:
    """Return ``text`` with the release's links added, and the links it added.

    The links go in the entry's `### Resources` section, which is created just
    above the entry's closing `---` rule when the entry has none.
    """
    lines = text.splitlines(keepends=True)

    heading_re = re.compile(r"^## " + re.escape(version) + r"(\s|$)")
    start = next((i for i, line in enumerate(lines) if heading_re.match(line)), None)
    if start is None:
        raise MissingEntry(version)

    # The entry runs until the next version heading, or to the end of file.
    end = next(
        (i for i in range(start + 1, len(lines)) if lines[i].startswith("## ")),
        len(lines),
    )

    entry = "".join(lines[start:end])
    missing = [
        link
        for link in release_links(version, site_version)
        # A link is there if its text is, whichever build it points at.
        if link.split("](")[0] + "](" not in entry
    ]
    if not missing:
        return text, []

    resources = next(
        (i for i in range(start, end) if lines[i].strip() == RESOURCES_HEADING),
        None,
    )
    if resources is not None:
        # After the section's last list item, so links keep their order.
        insert_at = resources + 1
        for i in range(resources + 1, end):
            stripped = lines[i].strip()
            if stripped.startswith(("#", "---")):
                break
            if stripped.startswith("- "):
                insert_at = i + 1
        lines[insert_at:insert_at] = [f"{link}\n" for link in missing]
        return "".join(lines), missing

    section = [f"{RESOURCES_HEADING}\n", "\n"] + [f"{link}\n" for link in missing]
    section.append("\n")

    # Entries are terminated by a '---' rule; insert just above it so the
    # section lands inside the entry rather than after its separator.
    rule = next(
        (i for i in range(end - 1, start, -1) if lines[i].strip() == "---"),
        None,
    )
    if rule is None:
        # No separator (last entry in the file, or a hand-edited one): append
        # to the entry, trimming trailing blank lines first.
        insert_at = end
        while insert_at > start and not lines[insert_at - 1].strip():
            insert_at -= 1
        if insert_at == len(lines) and lines and not lines[-1].endswith("\n"):
            lines[-1] += "\n"
        lines[insert_at:insert_at] = ["\n"] + section
    else:
        lines[rule:rule] = section

    return "".join(lines), missing


def main(argv=None, changelog: Path = CHANGELOG) -> int:
    argv = sys.argv[1:] if argv is None else argv
    site_version = None
    if len(argv) == 3 and argv[1] == "--site-version":
        site_version = argv[2]
    elif len(argv) != 1:
        print(
            f"Usage: {sys.argv[0]} <VERSION> [--site-version <api-docs build>]",
            file=sys.stderr,
        )
        return 1

    version = argv[0]
    if not STABLE_VERSION_RE.match(version):
        print(
            f"ERROR: {version!r} is not a stable version. RC releases ship no "
            "OpenAPI schema, so their changelog entries carry no schema link.",
            file=sys.stderr,
        )
        return 1

    try:
        text, added = add_links(
            changelog.read_text(encoding="utf-8"), version, site_version
        )
    except MissingEntry:
        # Fail rather than ship a stable release whose changelog entry has no
        # link to its API contract. scripts/release.sh commits the entry before
        # it pushes the tag, so by the time this runs the entry must exist; if
        # it does not, the release did not go through release.sh and needs a
        # human to look at it.
        print(
            f"ERROR: no '## {version}' entry in CHANGELOG.md.\n"
            "\n"
            "A stable release must have its changelog entry committed before "
            "the tag is pushed — scripts/release.sh does this in step [3/5]. "
            "Add the entry on master and retry this job.",
            file=sys.stderr,
        )
        return 1

    if not added:
        print(f"OK: '## {version}' already links its OpenAPI schema and API changes.")
        return 0

    changelog.write_text(text, encoding="utf-8")
    for link in added:
        print(f"Added to the '## {version}' changelog entry: {link}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Add the OpenAPI schema link to a released version's changelog entry.

Run by the `Generate OpenAPI schema` CI job immediately after it writes
docs/API/waldur-openapi-schema-<version>.yaml, so that the link and the file it
points at are staged into the SAME commit.

Why it is not done in scripts/release.sh: the schema is built from
waldur-mastermind's tag pipeline, which does not exist until this tag's
`release` stage has run. A link committed alongside the changelog would
therefore dangle for the whole release, and a dangling relative link aborts
`mkdocs build --strict` — on master and, because the entry sits on master, in
every open merge request. See scripts/check-changelog-api-links.py, which
guards against exactly that.

RC releases ship no schema, so this script is never run for them (the CI job's
rules match stable tags only) and it refuses to run if asked.

Idempotent: re-running on an entry that already carries the link is a no-op, so
a retried job commits nothing.

Exit status: 0 on success or no-op, 1 on a malformed argument or a missing
changelog entry. A missing entry is deliberately fatal — a stable release must
not ship without a link to its API contract.
"""

import re
import sys
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
CHANGELOG = PROJECT_DIR / "docs" / "about" / "CHANGELOG.md"

STABLE_VERSION_RE = re.compile(r"^\d+\.\d+\.\d+$")


def main() -> int:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <VERSION>", file=sys.stderr)
        return 1

    version = sys.argv[1]
    if not STABLE_VERSION_RE.match(version):
        print(
            f"ERROR: {version!r} is not a stable version. RC releases ship no "
            "OpenAPI schema, so their changelog entries carry no schema link.",
            file=sys.stderr,
        )
        return 1

    link = f"- [OpenAPI Schema](../API/waldur-openapi-schema-{version}.yaml)"
    lines = CHANGELOG.read_text(encoding="utf-8").splitlines(keepends=True)

    heading_re = re.compile(r"^## " + re.escape(version) + r"(\s|$)")
    start = next((i for i, l in enumerate(lines) if heading_re.match(l)), None)
    if start is None:
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

    # The entry runs until the next version heading, or to the end of file.
    end = next(
        (i for i in range(start + 1, len(lines)) if lines[i].startswith("## ")),
        len(lines),
    )

    if any(link in l for l in lines[start:end]):
        print(f"OK: '## {version}' already links to its OpenAPI schema.")
        return 0

    section = ["### Resources\n", "\n", f"{link}\n", "\n"]

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
        lines[insert_at:insert_at] = ["\n"] + section
    else:
        lines[rule:rule] = section

    CHANGELOG.write_text("".join(lines), encoding="utf-8")
    print(f"Added OpenAPI schema link to the '## {version}' changelog entry.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

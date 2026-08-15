#!/usr/bin/env python3
"""Verify a fetched OpenAPI schema really belongs to the release being tagged.

The `Generate OpenAPI schema` CI job gets its schema from the shared
`.fetch-openapi-schema` template in waldur/waldur-pipelines. That template first
tries waldur-mastermind's pipeline for this tag, and if it finds nothing it
falls back — silently, with exit status 0 — to downloading the latest *already
published* schema from the GitHub mirror of waldur-docs. A fallback therefore
looks exactly like success while yielding the previous release's schema, which
would then be committed under the new version's filename.

The schema carries the release in `info.version`, so compare it against the tag
and fail loudly on a mismatch. Better a red pipeline than a wrong schema
published as the new release's API contract.

Parsed with a small regex rather than PyYAML: the job runs on a
python:3.13-alpine image with no third-party packages installed, and only the
first few lines of the document are needed.

Exit status: 0 when the schema matches, 1 on any mismatch or unreadable file.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

# Only the head of the document is scanned; `info:` is a top-level key that
# appears within the first handful of lines of a generated schema.
HEAD_BYTES = 4096

INFO_RE = re.compile(r"^info:\s*$", re.MULTILINE)
VERSION_RE = re.compile(r"^[ \t]+version:[ \t]*['\"]?([^'\"\s]+)['\"]?[ \t]*$", re.MULTILINE)


def schema_version(path: Path) -> str | None:
    with path.open("r", encoding="utf-8", errors="replace") as f:
        head = f.read(HEAD_BYTES)

    info = INFO_RE.search(head)
    if not info:
        return None

    # Take the first indented `version:` after the `info:` key. A top-level
    # `openapi: 3.0.3` line is not indented, so it cannot be matched here.
    match = VERSION_RE.search(head, info.end())
    return match.group(1) if match else None


def main() -> int:
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <VERSION> <SCHEMA_PATH>", file=sys.stderr)
        return 1

    version, path = sys.argv[1], Path(sys.argv[2])

    if not path.is_file():
        print(f"ERROR: no schema at {path} — the fetch step produced nothing.", file=sys.stderr)
        return 1

    found = schema_version(path)
    if found is None:
        print(
            f"ERROR: could not read info.version from {path}. It may not be an "
            "OpenAPI schema at all (the fetch template can hand back an HTML "
            "error page).",
            file=sys.stderr,
        )
        return 1

    if found != version:
        print(
            f"ERROR: {path} declares info.version {found!r}, but this release "
            f"is {version!r}.\n"
            "\n"
            "This is what the .fetch-openapi-schema fallback looks like: no "
            "waldur-mastermind pipeline was found for this tag, so it silently "
            "downloaded the last published schema instead. Check that "
            "waldur-mastermind was tagged and that its 'Generate OpenAPI "
            "schema' job succeeded, then retry this job.",
            file=sys.stderr,
        )
        return 1

    print(f"OK: {path} is the schema for {version}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

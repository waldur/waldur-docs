#!/usr/bin/env python3
"""Validate relative OpenAPI-schema links in the changelog.

Every `](../API/waldur-openapi-schema-<version>.yaml)` link in
docs/about/CHANGELOG.md must point at a file that actually exists under
docs/API/. RC releases intentionally ship no schema, so an RC entry must not
carry such a link (see scripts/release.sh and the `Tag all repositories` CI
job). A dangling relative link makes `mkdocs build --strict` abort, which
blocks the docs build and — because the entry lands on master — every open MR.

Links inside HTML comments (`<!-- ... -->`) are ignored, matching how mkdocs
treats them: they are not rendered, so they are not validated.

Exit status: 0 when all links resolve, 1 when any target is missing.
"""

import re
import sys
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
CHANGELOG = PROJECT_DIR / "docs" / "about" / "CHANGELOG.md"
API_DIR = PROJECT_DIR / "docs" / "API"

# Matches the target of a relative link, e.g.
#   [OpenAPI Schema](../API/waldur-openapi-schema-8.1.0-rc.7.yaml)
LINK_RE = re.compile(r"\]\((\.\./API/waldur-openapi-schema-[^)]+\.yaml)\)")
# Drop <!-- ... --> comments (including multi-line ones) before scanning.
COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)


def main() -> int:
    text = CHANGELOG.read_text(encoding="utf-8")
    visible = COMMENT_RE.sub("", text)

    missing = []
    for rel in LINK_RE.findall(visible):
        # rel looks like "../API/waldur-openapi-schema-<ver>.yaml"; resolve it
        # against docs/about/ (where CHANGELOG.md lives).
        target = (CHANGELOG.parent / rel).resolve()
        if not target.is_file():
            missing.append(rel)

    if missing:
        print("ERROR: CHANGELOG.md links to OpenAPI schema files that do not exist:")
        for rel in missing:
            print(f"  - {rel}  ->  {(CHANGELOG.parent / rel).resolve()}")
        print()
        print(
            "RC releases ship no schema, so RC changelog entries must omit the "
            "'### Resources' OpenAPI Schema link. Remove the offending link or "
            "add the missing file under docs/API/."
        )
        return 1

    print("OK: all relative OpenAPI schema links in CHANGELOG.md resolve.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

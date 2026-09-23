#!/usr/bin/env python3
"""Upsert a release into docs/changelog/index.json.

Given a just-published `docs/changelog/releases/<version>.json` (assembled by
`waldur assemble_changelog` in waldur-mastermind and copied here by
scripts/release.sh), update the manifest that
`waldur_core.changelog.utils.fetch_changelog_index()` fetches from
`{CHANGELOG_BASE_URL}/index.json`: upsert this version's summary row,
recompute `latest_stable`/`latest_rc`.

Usage:
    python3 scripts/update_changelog_index.py <release-json-path> <index-json-path>
"""

import json
import sys
from pathlib import Path

URGENCY_RANK = {"critical": 4, "high": 3, "moderate": 2, "low": 1}


def _version_key(version: str) -> tuple:
    """Sort key ordering stable releases after their RCs (8.0.7-rc.9 < 8.0.7),
    matching waldur_core.changelog.utils.parse_version()'s RC-before-stable
    ordering without adding a `packaging` dependency to this repo. Release
    components are padded to three so '8.1' and '8.1.0' compare equal, same
    as packaging.version.Version. Unparseable input sorts as 0.0.0 rather
    than crashing the index update mid-release."""
    base, _, rc = version.partition("-rc.")
    try:
        parts = tuple(int(p) for p in base.split("."))
    except ValueError:
        parts = ()
    parts = (parts + (0, 0, 0))[:3]
    if rc:
        try:
            rc_num = int(rc)
        except ValueError:
            rc_num = 0
        is_rc = 0
    else:
        is_rc, rc_num = 1, 0
    return parts + (is_rc, rc_num)


def build_release_row(release: dict) -> dict:
    entries = release.get("entries", [])
    security_entries = [e for e in entries if e.get("type") == "security"]

    row = {
        "version": release["version"],
        "type": release.get("type", "stable"),
        "date": release.get("date"),
        "has_breaking": any(e.get("type") == "breaking" for e in entries),
        "has_security": bool(security_entries),
    }
    if security_entries:
        row["max_security_urgency"] = max(
            (e.get("security", {}).get("urgency", "low") for e in security_entries),
            key=lambda u: URGENCY_RANK.get(u, 0),
        )
    return row


def upsert(index: dict, row: dict) -> dict:
    releases = [r for r in index.get("releases", []) if r["version"] != row["version"]]
    releases.append(row)
    releases.sort(key=lambda r: _version_key(r["version"]))
    index["releases"] = releases

    stables = [r["version"] for r in releases if r["type"] == "stable"]
    rcs = [r["version"] for r in releases if r["type"] == "rc"]

    if stables:
        index["latest_stable"] = max(stables, key=_version_key)
    if rcs:
        index["latest_rc"] = max(rcs, key=_version_key)

    return index


def main() -> int:
    if len(sys.argv) != 3:
        print(
            f"Usage: {sys.argv[0]} <release-json-path> <index-json-path>",
            file=sys.stderr,
        )
        return 1

    release_path = Path(sys.argv[1])
    index_path = Path(sys.argv[2])

    release = json.loads(release_path.read_text(encoding="utf-8"))
    index: dict = (
        json.loads(index_path.read_text(encoding="utf-8"))
        if index_path.exists()
        else {"releases": []}
    )
    index.setdefault("schema_version", "1.0.0")

    row = build_release_row(release)
    index = upsert(index, row)

    index_path.parent.mkdir(parents=True, exist_ok=True)
    index_path.write_text(json.dumps(index, indent=2) + "\n", encoding="utf-8")

    print(f"Updated {index_path} with {row['version']} ({row['type']})")
    return 0


if __name__ == "__main__":
    sys.exit(main())

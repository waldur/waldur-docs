#!/usr/bin/env python3
"""Assert that a stable release actually finished.

Nothing in the pipeline used to check the *outcome* of a release. The 8.1.0 run
left Helm, Docker Compose and the Prometheus exporter unreleased and
docs.waldur.com/8.1.0/ returning 404, and the pipeline reported nothing —
because the jobs that would have done that work were skipped, and a skipped job
is not a failed one. The gap was found by hand, days later.

This runs at the end of a stable tag pipeline and checks what an operator would
otherwise have to check themselves:

  * the OpenAPI schema for the release is committed under docs/API/
  * the changelog entry exists and links that schema
  * the versioned documentation is actually served
  * every repository that takes part in the release carries the tag

Every check runs before anything is reported, so one invocation lists
everything that is wrong rather than failing on the first problem.

Exit status: 0 when the release is complete, 1 when any check fails.
"""

from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
CHANGELOG = PROJECT_DIR / "docs" / "about" / "CHANGELOG.md"
API_DIR = PROJECT_DIR / "docs" / "API"

GITLAB = os.environ.get("CI_SERVER_URL", "https://code.opennodecloud.com") + "/api/v4"
DOCS_URL = "https://docs.waldur.com"

# Repositories tagged as part of a stable release. waldur-docs itself is the
# pipeline running this, so its tag is a given.
TAGGED_REPOS = [
    "waldur/waldur-mastermind",
    "waldur/waldur-homeport",
    "waldur/waldur-helm",
    "waldur/waldur-docker-compose",
]

TIMEOUT = 30


def gitlab_get(path: str):
    """GET a GitLab API path, trying the job token then GITLAB_TOKEN."""
    attempts = []
    if os.environ.get("CI_JOB_TOKEN"):
        attempts.append(("JOB-TOKEN", os.environ["CI_JOB_TOKEN"]))
    if os.environ.get("GITLAB_TOKEN"):
        attempts.append(("PRIVATE-TOKEN", os.environ["GITLAB_TOKEN"]))
    if not attempts:
        attempts.append((None, None))

    last = None
    for header, value in attempts:
        request = urllib.request.Request(f"{GITLAB}/{path}")
        if header:
            request.add_header(header, value)
        try:
            with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
                return json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            last = f"HTTP {exc.code}"
            if exc.code == 404:
                return None
        except Exception as exc:  # noqa: BLE001 - reported as a failed check
            last = str(exc)
    print(f"    (lookup failed: {last})")
    return None


def http_status(url: str) -> int | None:
    request = urllib.request.Request(url, method="GET")
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
            return response.status
    except urllib.error.HTTPError as exc:
        return exc.code
    except Exception:  # noqa: BLE001 - treated as unreachable
        return None


def check_schema_committed(version: str) -> str | None:
    schema = API_DIR / f"waldur-openapi-schema-{version}.yaml"
    if not schema.is_file():
        return (
            f"docs/API/{schema.name} is missing — the Generate OpenAPI schema "
            "job did not commit it."
        )
    return None


def check_changelog(version: str) -> str | None:
    if not CHANGELOG.is_file():
        return "docs/about/CHANGELOG.md is missing."
    text = CHANGELOG.read_text(encoding="utf-8")
    if f"## {version} " not in text and not text.count(f"## {version}\n"):
        return f"CHANGELOG.md has no '## {version}' entry."
    link = f"../API/waldur-openapi-schema-{version}.yaml"
    if link not in text:
        return (
            f"The '## {version}' changelog entry does not link its OpenAPI "
            "schema — add-changelog-api-link.py did not run."
        )
    return None


def check_docs_published(version: str) -> str | None:
    status = http_status(f"{DOCS_URL}/{version}/")
    if status != 200:
        return (
            f"{DOCS_URL}/{version}/ returned {status} — the versioned "
            "documentation was never deployed."
        )
    return None


def check_repo_tag(repo: str, version: str) -> str | None:
    quoted = repo.replace("/", "%2F")
    tag = gitlab_get(f"projects/{quoted}/repository/tags/{version}")
    if not tag:
        return f"{repo} has no {version} tag — it was not released."
    return None


def main() -> int:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <VERSION>", file=sys.stderr)
        return 1

    version = sys.argv[1]
    print(f"Verifying that release {version} completed...\n")

    checks = [
        ("OpenAPI schema committed", lambda: check_schema_committed(version)),
        ("changelog entry links the schema", lambda: check_changelog(version)),
        ("versioned documentation is served", lambda: check_docs_published(version)),
    ]
    for repo in TAGGED_REPOS:
        checks.append((f"{repo} tagged", lambda r=repo: check_repo_tag(r, version)))

    failures = []
    for name, check in checks:
        problem = check()
        if problem:
            print(f"  FAIL  {name}")
            failures.append(problem)
        else:
            print(f"  ok    {name}")

    if failures:
        print(f"\nERROR: release {version} is incomplete:\n", file=sys.stderr)
        for problem in failures:
            print(f"  - {problem}", file=sys.stderr)
        print(
            "\nThe tag is already published, so fix forward: re-run the jobs "
            "that were skipped, or finish the missing steps by hand.",
            file=sys.stderr,
        )
        return 1

    print(f"\nOK: release {version} is complete.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

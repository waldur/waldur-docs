#!/usr/bin/env python3
"""Block until waldur-mastermind has published the schema for this release.

The `Generate OpenAPI schema` job fetches the schema from waldur-mastermind's
pipeline *for this tag*. That pipeline is created by the `release` stage, but
the job inside it that actually builds the schema takes a few more minutes — in
the 8.1.0 release, mastermind's tag pipeline was created 10 seconds before this
job started, and its schema job had not finished.

`.fetch-openapi-schema` reacts to that by falling back to the last published
schema, which used to corrupt the release silently and now (since
waldur-pipelines!127) fails it. Either way the release stalls or breaks on a
race that is purely a matter of waiting, so wait explicitly instead.

Polls the pipelines for the given ref until one has a successful
`Generate OpenAPI schema` job, then exits 0 so the fetch can proceed.

Exit status: 0 once the schema is ready, 1 on timeout or a bad argument.
"""

from __future__ import annotations

import json
import os
import re
import sys
import time
import urllib.error
import urllib.request

API = "https://code.opennodecloud.com/api/v4"
PROJECT = "waldur%2Fwaldur-mastermind"
JOB_NAME = "Generate OpenAPI schema"

POLL_SECONDS = 30
TIMEOUT_SECONDS = 30 * 60
# Only the newest pipelines matter; a ref usually has one.
PIPELINES_CHECKED = 5

STABLE_VERSION_RE = re.compile(r"^\d+\.\d+\.\d+$")


def request(url: str):
    """GET url, trying the job token first and then the broader GITLAB_TOKEN.

    Mirrors the two-tier fallback in `.fetch-openapi-schema`: CI_JOB_TOKEN is
    scoped per-project and may not be allow-listed for cross-project reads.
    """
    attempts = []
    if os.environ.get("CI_JOB_TOKEN"):
        attempts.append(("JOB-TOKEN", os.environ["CI_JOB_TOKEN"]))
    if os.environ.get("GITLAB_TOKEN"):
        attempts.append(("PRIVATE-TOKEN", os.environ["GITLAB_TOKEN"]))
    if not attempts:
        attempts.append((None, None))

    last = None
    for header, value in attempts:
        req = urllib.request.Request(url)
        if header:
            req.add_header(header, value)
        try:
            with urllib.request.urlopen(req, timeout=30) as response:
                return json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            last = f"HTTP {exc.code} {exc.reason}"
        except Exception as exc:  # noqa: BLE001 - network errors are retried
            last = str(exc)
    print(f"  (lookup failed: {last})", flush=True)
    return None


def schema_ready(ref: str) -> bool:
    pipelines = request(f"{API}/projects/{PROJECT}/pipelines?ref={ref}")
    if not pipelines:
        return False
    for pipeline in pipelines[:PIPELINES_CHECKED]:
        jobs = request(f"{API}/projects/{PROJECT}/pipelines/{pipeline['id']}/jobs")
        if not jobs:
            continue
        for job in jobs:
            if job.get("name") == JOB_NAME and job.get("status") == "success":
                print(
                    f"waldur-mastermind job {job['id']} in pipeline "
                    f"{pipeline['id']} has the schema for {ref}."
                )
                return True
    return False


def main() -> int:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <VERSION>", file=sys.stderr)
        return 1

    ref = sys.argv[1]
    if not STABLE_VERSION_RE.match(ref):
        # RC tags never reach this job; treat anything else as nothing to wait
        # for rather than blocking a pipeline for half an hour.
        print(f"{ref!r} is not a stable release — nothing to wait for.")
        return 0

    deadline = time.monotonic() + TIMEOUT_SECONDS
    attempt = 0
    while True:
        attempt += 1
        if schema_ready(ref):
            return 0
        if time.monotonic() >= deadline:
            print(
                f"ERROR: waldur-mastermind still has no successful "
                f"{JOB_NAME!r} job for {ref} after "
                f"{TIMEOUT_SECONDS // 60} minutes.\n"
                "\n"
                "Check that waldur-mastermind was tagged and that its schema "
                "job succeeded, then retry this job. Proceeding without it "
                "would generate the release from the previous release's "
                "schema.",
                file=sys.stderr,
            )
            return 1
        print(
            f"[{attempt}] schema for {ref} not ready yet; "
            f"retrying in {POLL_SECONDS}s...",
            flush=True,
        )
        time.sleep(POLL_SECONDS)


if __name__ == "__main__":
    sys.exit(main())

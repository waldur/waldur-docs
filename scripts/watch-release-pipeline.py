#!/usr/bin/env python3
"""Follow a release pipeline to completion and report what failed.

`release.sh` used to print "[5/5] Done!" the moment the tag was pushed and then
exit. Every failure in the 8.1.0 release happened after that line: the schema
job died, the stages behind it were skipped, three SDK pipelines failed, and
the operator had already looked away.

Run by `release.sh --watch`. Polls the tag pipeline, prints each job and
downstream trigger as it settles, and ends with a verdict. Watching does not
change the release — killing this script leaves the pipeline running.

Exit status: 0 if the pipeline succeeded, 1 if it failed or timed out.
"""

from __future__ import annotations

import json
import subprocess
import sys
import time

PROJECT = "waldur%2Fwaldur-docs"
POLL_SECONDS = 20
TIMEOUT_SECONDS = 90 * 60

TERMINAL = {"success", "failed", "canceled", "skipped", "manual"}
BAD = {"failed", "canceled"}


def api(path: str):
    """Call the GitLab API through glab, which already holds credentials."""
    proc = subprocess.run(
        ["glab", "api", f"projects/{PROJECT}/{path}"],
        capture_output=True,
        text=True,
    )
    if proc.returncode != 0:
        return None
    try:
        return json.loads(proc.stdout)
    except json.JSONDecodeError:
        return None


def find_pipeline(version: str):
    pipelines = api(f"pipelines?ref={version}&per_page=1")
    return pipelines[0] if pipelines else None


def units(pipeline_id: int):
    """Jobs and downstream triggers, which GitLab reports separately."""
    found = []
    for kind, path in (("job", "jobs"), ("trigger", "bridges")):
        items = api(f"pipelines/{pipeline_id}/{path}?per_page=100") or []
        for item in items:
            downstream = (item.get("downstream_pipeline") or {}).get("status")
            found.append(
                {
                    "kind": kind,
                    "name": item.get("name", "?"),
                    "stage": item.get("stage", "?"),
                    "status": item.get("status", "?"),
                    "downstream": downstream,
                }
            )
    return found


def main() -> int:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <VERSION>", file=sys.stderr)
        return 1

    version = sys.argv[1]

    pipeline = None
    for _ in range(15):
        pipeline = find_pipeline(version)
        if pipeline:
            break
        print("  waiting for the pipeline to appear...", flush=True)
        time.sleep(4)

    if not pipeline:
        print(f"ERROR: no pipeline found for {version}.", file=sys.stderr)
        return 1

    print(f"  pipeline {pipeline['id']}: {pipeline.get('web_url', '')}\n", flush=True)

    reported = {}
    deadline = time.monotonic() + TIMEOUT_SECONDS

    while True:
        current = api(f"pipelines/{pipeline['id']}")
        status = current.get("status") if current else None

        for unit in units(pipeline["id"]):
            key = (unit["kind"], unit["name"])
            if unit["status"] in TERMINAL and reported.get(key) != unit["status"]:
                reported[key] = unit["status"]
                mark = {
                    "success": "ok  ",
                    "failed": "FAIL",
                    "canceled": "CANC",
                    "skipped": "skip",
                    "manual": "man ",
                }.get(unit["status"], "??  ")
                extra = ""
                if unit["downstream"] and unit["downstream"] != unit["status"]:
                    extra = f"  (downstream: {unit['downstream']})"
                print(
                    f"  {mark}  {unit['stage']:<14} {unit['name']}{extra}", flush=True
                )

        if status and status not in (
            "running",
            "pending",
            "created",
            "waiting_for_resource",
        ):
            print()
            failed = [name for (_, name), state in reported.items() if state in BAD]
            skipped = [
                name for (_, name), state in reported.items() if state == "skipped"
            ]
            if status == "success":
                print(f"Pipeline {status}. Release {version} ran to completion.")
                return 0
            print(f"ERROR: pipeline {status}.", file=sys.stderr)
            if failed:
                print("  failed: " + ", ".join(sorted(failed)), file=sys.stderr)
            if skipped:
                print(
                    "  skipped (never ran, so their work is missing): "
                    + ", ".join(sorted(skipped)),
                    file=sys.stderr,
                )
            print(
                "\nThe tag is already published — fix forward rather than retagging.",
                file=sys.stderr,
            )
            return 1

        if time.monotonic() >= deadline:
            print(
                f"\nERROR: pipeline still {status} after "
                f"{TIMEOUT_SECONDS // 60} minutes; giving up watching. "
                "The pipeline itself keeps running.",
                file=sys.stderr,
            )
            return 1

        time.sleep(POLL_SECONDS)


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Post a Waldur release announcement to Slack.

Reads docs/about/CHANGELOG.md, extracts the entry for the given VERSION,
and posts a Block Kit message via Slack incoming webhook.

Usage:
    publish-release-slack.py <VERSION> [--dry-run]

Webhook URL is read from $SLACK_WEBHOOK_URL.
For RC releases (e.g. 8.0.9-rc.5), $SLACK_WEBHOOK_URL_RC is preferred if set.

Failures are logged but do not exit non-zero (release announcements should
not fail the pipeline).
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Optional

DOCS_BASE = "https://docs.waldur.com/latest/about/CHANGELOG/"
CHANGELOG_PATH = Path(__file__).resolve().parent.parent / "docs" / "about" / "CHANGELOG.md"

# Slack Block Kit limits
MAX_HEADER_CHARS = 150
MAX_SECTION_CHARS = 3000
MAX_BLOCKS = 50

# Per-subsection bullet preview budget
TOP_BULLETS = 8
# Per-bullet hard cap to keep the message scannable.
MAX_BULLET_CHARS = 280


def extract_entry(version: str, changelog: str) -> Optional[str]:
    """Return the body of '## <version> - <date>' up to the next '## ' or '---'."""
    pattern = re.compile(
        r"^## " + re.escape(version) + r"\b.*?(?=^## |\Z)",
        re.MULTILINE | re.DOTALL,
    )
    m = pattern.search(changelog)
    if not m:
        return None
    block = m.group(0)
    # Drop trailing '---' separator if present.
    block = re.sub(r"\n---\s*\n*\Z", "\n", block)
    return block.strip()


def parse_header_date(entry: str) -> tuple[str, str]:
    """Return (version, date) from the leading '## VERSION - DATE' line."""
    m = re.match(r"^## (\S+)\s*-\s*(\d{4}-\d{2}-\d{2})", entry)
    if not m:
        return "", ""
    return m.group(1), m.group(2)


def split_subsections(entry: str) -> dict[str, str]:
    """Return {subsection_title: body} for each '### Title' block.

    Body excludes the heading line. Order is preserved via dict insertion order.
    """
    sections: dict[str, str] = {}
    parts = re.split(r"^### (.+)$", entry, flags=re.MULTILINE)
    # parts[0] is preamble, then alternating [title, body, title, body, ...]
    for i in range(1, len(parts) - 1, 2):
        title = parts[i].strip()
        body = parts[i + 1].strip()
        sections[title] = body
    return sections


def first_bullets(body: str, n: int) -> tuple[list[str], int]:
    """Return (top_n_bullets, total_count). A bullet starts with '- '."""
    bullets = [
        md_to_mrkdwn(line[2:].strip())
        for line in body.splitlines()
        if line.startswith("- ")
    ]
    return bullets[:n], len(bullets)


def md_to_mrkdwn(text: str) -> str:
    """Convert standard markdown to Slack mrkdwn.

    - **bold** -> *bold*
    - [text](url) -> <url|text>
    Italic with `*` or `_` is left alone (Slack treats underscores as italic).
    """
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"<\2|\1>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"*\1*", text)
    return text


def trim(text: str, limit: int) -> str:
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "…"


def anchor_for(version: str, date: str) -> str:
    """Compute the MkDocs Material anchor for a '## VERSION - DATE' heading.

    Drops dots from version, lowercases, joins with date via '-'.
    Example: ('8.0.9-rc.5', '2026-05-08') -> '809-rc5-2026-05-08'
    """
    v = version.replace(".", "").lower()
    return f"{v}-{date}"


def is_rc(version: str) -> bool:
    return bool(re.search(r"-rc\.\d+$", version))


def build_blocks(entry: str) -> tuple[list[dict], str]:
    """Build Block Kit blocks plus a fallback text string."""
    version, date = parse_header_date(entry)
    rc = is_rc(version)
    suffix = " — release candidate" if rc else " released"
    title = f"Waldur {version}{suffix}"
    if date:
        title += f" — {date}"
    fallback = title

    subs = split_subsections(entry)
    blocks: list[dict] = [
        {"type": "header", "text": {"type": "plain_text", "text": trim(title, MAX_HEADER_CHARS)}}
    ]

    # Each subsection becomes its own section block so each fits within the
    # 3000-char per-section limit.
    first_subsection = True
    for title_key in ("What's New", "Improvements", "Bug Fixes"):
        body = subs.get(title_key)
        if not body:
            continue
        top, total = first_bullets(body, TOP_BULLETS)
        if total == 0:
            continue
        if first_subsection:
            first_subsection = False
        else:
            blocks.append({"type": "divider"})
        lines = [f"*{title_key}* ({total})"]
        lines += [f"• {trim(b, MAX_BULLET_CHARS)}" for b in top]
        if total > len(top):
            lines.append(f"_+ {total - len(top)} more_")
        blocks.append(_section("\n".join(lines)))

    # Footer: activity counts + link.
    activity_line = _activity_summary(subs.get("Core Component Activity", ""))
    url = DOCS_BASE + "#" + anchor_for(version, date)
    context_elements = []
    if activity_line:
        context_elements.append({"type": "mrkdwn", "text": activity_line})
    context_elements.append({"type": "mrkdwn", "text": f"<{url}|Full changelog →>"})

    blocks.append({"type": "divider"})
    blocks.append({"type": "context", "elements": context_elements})

    # Enforce hard limits.
    blocks = blocks[:MAX_BLOCKS]
    return blocks, fallback


def _section(text: str) -> dict:
    return {"type": "section", "text": {"type": "mrkdwn", "text": trim(text, MAX_SECTION_CHARS)}}


def _activity_summary(body: str) -> str:
    """Extract 'Repo N commits' fragments from Core Component Activity bullets."""
    parts: list[str] = []
    for line in body.splitlines():
        m = re.match(r"^-\s+\*\*(.+?)\*\*.*?(\d+)\s+commits?", line)
        if m:
            parts.append(f"{m.group(1)}: {m.group(2)}")
    return "Activity — " + " · ".join(parts) if parts else ""


def post(webhook_url: str, blocks: list[dict], fallback_text: str) -> bool:
    payload = json.dumps({"blocks": blocks, "text": fallback_text}).encode()
    req = urllib.request.Request(
        webhook_url,
        data=payload,
        headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = resp.read().decode().strip()
            if body and body != "ok":
                print(f"slack response: {body}", file=sys.stderr)
            return True
    except urllib.error.HTTPError as e:
        print(f"slack webhook returned {e.code}: {e.read().decode()[:300]}", file=sys.stderr)
    except urllib.error.URLError as e:
        print(f"slack webhook error: {e}", file=sys.stderr)
    return False


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("version")
    ap.add_argument("--dry-run", action="store_true", help="Print payload, do not POST")
    ap.add_argument("--changelog", default=str(CHANGELOG_PATH))
    args = ap.parse_args(argv)

    changelog = Path(args.changelog).read_text()
    entry = extract_entry(args.version, changelog)
    if not entry:
        print(f"No changelog entry found for {args.version}", file=sys.stderr)
        return 0  # do not fail pipeline

    blocks, fallback = build_blocks(entry)

    if args.dry_run:
        print(json.dumps({"text": fallback, "blocks": blocks}, indent=2))
        return 0

    rc = is_rc(args.version)
    webhook = os.environ.get("SLACK_WEBHOOK_URL_RC") if rc else None
    webhook = webhook or os.environ.get("SLACK_WEBHOOK_URL")
    if not webhook:
        print("no webhook URL set (SLACK_WEBHOOK_URL[_RC])", file=sys.stderr)
        return 0

    post(webhook, blocks, fallback)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

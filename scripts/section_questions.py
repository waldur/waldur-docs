"""Write the questions each documentation section answers, for the AI assistant's search.

The corpus hook (hooks/docs_corpus.py) puts a section's questions in the corpus
as `context`, which mastermind searches but never shows. That is how "how do I
invite a colleague" finds a section titled "Add project members"
(measurements in waldur/waldur-docs!548).

The questions live in docs-questions.yml, one entry per section:

    user-guide/customer-organization/project-management.md:
      create-a-project:
        for: 1a2b3c4d          # hash of the section text they were written for
        questions:
          - How do I start a new project?

This script asks an LLM for sections in `questions_scope` that have no entry,
or whose text changed since (`for` no longer matches), and drops entries of
sections that are gone. Entries are plain YAML: correct or add questions by
hand; they are kept until the section's text changes, and also when writing
new ones fails.

    DOCS_CORPUS_OUT=/tmp/corpus.jsonl.gz uv run mkdocs build
    DOCS_QUESTIONS_LLM_URL=https://llm.example.org/v1 DOCS_QUESTIONS_LLM_MODEL=... \\
    DOCS_QUESTIONS_LLM_TOKEN_FILE=~/token uv run python scripts/section_questions.py /tmp/corpus.jsonl.gz

Any OpenAI-compatible endpoint works. DOCS_QUESTIONS_LLM_BACKEND=vllm (the
default) also turns off Qwen3's thinking, which vLLM accepts and OpenAI
rejects; set it to `openai` for an endpoint that takes only the standard
fields. `--dry-run` only counts.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import gzip
import json
import os
import re
import sys
import threading
import urllib.error
import urllib.request
from collections import defaultdict
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "hooks"))

from docs_corpus import text_hash  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / "docs-corpus.yml"
HEADER = """\
# The questions each documentation section answers, in a user's words.
# The AI assistant's search matches them but never shows them (docs-corpus.yml,
# `questions`). `for` is a hash of the section text they were written for; when
# the text changes, scripts/section_questions.py writes them again. Edit freely.
"""

PROMPT = """Below is one section of a page of the user documentation of Waldur, \
a self-service portal for ordering and managing cloud and HPC resources.

Write three short questions a portal user might type that this section answers. \
Use everyday words; do not just repeat the heading.

Reply with JSON only: {{"questions": ["...", "...", "..."]}}

Page: {page}
Section: {crumb} > {title}
Page outline: {outline}

Section text:
{text}"""


def load_entries(path: Path) -> dict:
    if not path.exists():
        return {}
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def dump_entries(entries: dict, path: Path) -> None:
    ordered = {
        page: {anchor: entries[page][anchor] for anchor in sorted(entries[page])}
        for page in sorted(entries)
        if entries[page]
    }
    body = yaml.safe_dump(
        ordered, allow_unicode=True, sort_keys=False, width=1000, indent=2
    )
    path.write_text(HEADER + body, encoding="utf-8")


def plan(sections: list[dict], entries: dict, scope: list[re.Pattern]):
    """(sections to ask about, entries pruned to existing sections).

    A stale entry stays in `kept` until new questions replace it, so a run
    that fails or is stopped leaves every section at least what it had.
    """
    todo, kept = [], defaultdict(dict)
    for section in sections:
        if not any(p.search(section["path"]) for p in scope):
            continue
        entry = (entries.get(section["path"]) or {}).get(section["anchor"])
        if entry:
            kept[section["path"]][section["anchor"]] = entry
        if not entry or entry.get("for") != text_hash(section["text"]):
            todo.append(section)
    return todo, kept


def parse_questions(reply: str | None) -> list[str]:
    match = re.search(r"\{.*\}", reply or "", re.S)
    if not match:
        return []
    try:
        questions = json.loads(match.group(0)).get("questions")
    except (json.JSONDecodeError, AttributeError):
        return []
    if not isinstance(questions, list):
        return []
    return [q.strip() for q in questions if isinstance(q, str) and q.strip()][:5]


class Client:
    def __init__(self, url: str, model: str, token: str, backend: str = "vllm"):
        self.url = url.rstrip("/") + "/chat/completions"
        self.model = model
        self.token = token
        self.backend = backend

    def ask(self, prompt: str) -> str:
        body = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0,
        }
        if self.backend == "vllm":
            body["max_tokens"] = 300
            # Qwen3 on vLLM thinks by default and leaves no room for the answer.
            body["chat_template_kwargs"] = {"enable_thinking": False}
        else:
            body["max_completion_tokens"] = 300
        request = urllib.request.Request(
            self.url,
            json.dumps(body).encode(),
            {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.token}",
            },
        )
        with urllib.request.urlopen(request, timeout=120) as response:
            return json.load(response)["choices"][0]["message"]["content"]


def prompt_for(section: dict, page_sections: list[dict]) -> str:
    page = page_sections[0]["title"]
    outline = "; ".join(s["title"] for s in page_sections)[:600]
    return PROMPT.format(
        page=page,
        crumb=section["breadcrumb"],
        title=section["title"],
        outline=outline,
        text=section["text"][:2500],
    )


def token_from_env() -> str:
    token_file = os.environ.get("DOCS_QUESTIONS_LLM_TOKEN_FILE")
    if token_file:
        return Path(token_file).expanduser().read_text(encoding="utf-8").strip()
    return os.environ.get("DOCS_QUESTIONS_LLM_TOKEN", "")


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument(
        "corpus", type=Path, help="docs-corpus.jsonl.gz of this checkout"
    )
    parser.add_argument("--dry-run", action="store_true", help="only count")
    parser.add_argument("--workers", type=int, default=8)
    args = parser.parse_args(argv)

    config = yaml.safe_load(CONFIG.read_text(encoding="utf-8"))
    out = ROOT / config["questions"]
    scope = [re.compile(p) for p in config.get("questions_scope") or []]
    with gzip.open(args.corpus, "rt", encoding="utf-8") as stream:
        sections = [json.loads(line) for line in stream if line.strip()]
    by_page = defaultdict(list)
    for section in sections:
        by_page[section["path"]].append(section)

    entries = load_entries(out)
    todo, kept = plan(sections, entries, scope)
    before = sum(len(v) for v in entries.values())
    print(
        f"{len(todo)} sections to ask about; "
        f"{before - sum(map(len, kept.values()))} entries of removed sections dropped"
    )
    if args.dry_run or not todo:
        if not args.dry_run:
            dump_entries(kept, out)
        return 0

    client = Client(
        os.environ["DOCS_QUESTIONS_LLM_URL"],
        os.environ["DOCS_QUESTIONS_LLM_MODEL"],
        token_from_env(),
        os.environ.get("DOCS_QUESTIONS_LLM_BACKEND", "vllm"),
    )
    lock = threading.Lock()
    failed = []

    def ask(section):
        reason = "no questions in the reply"
        for _ in range(3):
            try:
                questions = parse_questions(
                    client.ask(prompt_for(section, by_page[section["path"]]))
                )
            except urllib.error.HTTPError as exc:
                # Status only: the response is not printed, the request never.
                reason = f"HTTP {exc.code} {exc.reason}"
                continue
            except Exception as exc:  # noqa: BLE001 - one bad reply must not end the run
                reason = type(exc).__name__
                continue
            if questions:
                with lock:
                    kept[section["path"]][section["anchor"]] = {
                        "for": text_hash(section["text"]),
                        "questions": questions,
                    }
                return
        with lock:
            failed.append(f"{section['path']}#{section['anchor']} ({reason})")

    pool = concurrent.futures.ThreadPoolExecutor(args.workers)
    try:
        list(pool.map(ask, todo))
    except KeyboardInterrupt:
        # Stop at once: sections not started keep what they had.
        pool.shutdown(wait=False, cancel_futures=True)
        raise
    finally:
        # Under the lock, so a worker still finishing cannot change `kept`
        # mid-write; the answers already paid for are kept.
        with lock:
            dump_entries(kept, out)
        pool.shutdown(wait=False)
    print(f"Wrote {out.name}; {len(failed)} sections failed")
    for line in failed[:10]:
        print(f"  {line}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())

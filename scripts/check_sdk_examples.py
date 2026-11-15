#!/usr/bin/env python3
"""Check the Python SDK examples in the docs against the installed waldur-api-client.

Each ```python block in the given Markdown files must compile, every name it
imports from waldur_api_client must exist, and every call to an SDK function or
request model must use keyword arguments that the function or model accepts,
including all required ones. Nothing is sent to a server.

The SDK is regenerated from the API schema, so endpoints, enums and models are
renamed or dropped without anyone touching the docs; this catches examples that
would fail with ImportError, AttributeError or TypeError.

Usage: check_sdk_examples.py [FILE.md ...]
Without arguments, checks every page under docs/integrator-guide/.
"""

from __future__ import annotations

import ast
import importlib
import inspect
import re
import sys
from dataclasses import dataclass
from pathlib import Path

try:
    import attrs
except ImportError:  # attrs is a dependency of waldur-api-client
    attrs = None

DEFAULT_ROOT = Path(__file__).resolve().parent.parent / "docs" / "integrator-guide"
BLOCK_RE = re.compile(r"^```python[^\n]*\n(.*?)^```", re.S | re.M)
SDK_PACKAGE = "waldur_api_client"


@dataclass
class Problem:
    path: str
    line: int
    message: str

    def __str__(self) -> str:
        return f"{self.path}:{self.line}: {self.message}"


def iter_blocks(text: str):
    """Yield (first line number, source) for each python block."""
    for match in BLOCK_RE.finditer(text):
        first_line = text.count("\n", 0, match.start(1)) + 1
        yield first_line, match.group(1)


def resolve_import(module: str, name: str):
    """Return the object `from module import name` would bind."""
    mod = importlib.import_module(module)
    if hasattr(mod, name):
        return getattr(mod, name)
    return importlib.import_module(f"{module}.{name}")


def attrs_fields(cls):
    if attrs is None or not attrs.has(cls):
        return None
    return attrs.fields(cls)


def check_call(call: ast.Call, target, label: str):
    """Return messages for keyword arguments that `target` would reject."""
    given = {kw.arg for kw in call.keywords if kw.arg is not None}
    has_star_kwargs = any(kw.arg is None for kw in call.keywords)
    fields = attrs_fields(target) if inspect.isclass(target) else None
    if fields is not None:
        accepted = {f.alias or f.name for f in fields}
        required = [
            f.alias or f.name for f in fields if f.default is attrs.NOTHING and f.init
        ][len(call.args) :]
        accepts_any = False
    else:
        try:
            signature = inspect.signature(target)
        except (TypeError, ValueError):
            return []
        params = signature.parameters
        accepts_any = any(p.kind is p.VAR_KEYWORD for p in params.values())
        accepted = set(params)
        positional = [
            name
            for name, p in params.items()
            if p.kind in (p.POSITIONAL_ONLY, p.POSITIONAL_OR_KEYWORD)
        ][: len(call.args)]
        required = [
            name
            for name, p in params.items()
            if p.default is p.empty
            and p.kind in (p.POSITIONAL_OR_KEYWORD, p.KEYWORD_ONLY)
            and name not in positional
        ]
    messages = []
    unknown = sorted(given - accepted)
    if unknown and not accepts_any:
        messages.append(f"{label}() got unexpected keyword arguments {unknown}")
    missing = [name for name in required if name not in given]
    if missing and not has_star_kwargs:
        messages.append(f"{label}() is missing required arguments {missing}")
    return messages


def check_block(path: str, first_line: int, source: str) -> list[Problem]:
    def problem(node_line: int, message: str) -> Problem:
        return Problem(path, first_line + node_line - 1, message)

    try:
        tree = ast.parse(source)
    except SyntaxError as e:
        return [problem(e.lineno or 1, f"syntax error: {e.msg}")]

    problems = []
    bound = {}
    for node in ast.walk(tree):
        if not (
            isinstance(node, ast.ImportFrom)
            and node.module
            and node.module.split(".")[0] == SDK_PACKAGE
        ):
            continue
        for alias in node.names:
            try:
                bound[alias.asname or alias.name] = resolve_import(
                    node.module, alias.name
                )
            except (ImportError, AttributeError):
                problems.append(
                    problem(
                        node.lineno, f"cannot import {alias.name} from {node.module}"
                    )
                )

    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        func = node.func
        if isinstance(func, ast.Attribute) and isinstance(func.value, ast.Name):
            owner = bound.get(func.value.id)
            if owner is None or not inspect.ismodule(owner):
                continue
            label = f"{func.value.id}.{func.attr}"
            if not hasattr(owner, func.attr):
                available = sorted(
                    name
                    for name in ("sync", "sync_detailed", "sync_all", "asyncio")
                    if hasattr(owner, name)
                )
                problems.append(
                    problem(node.lineno, f"{label} does not exist (has {available})")
                )
                continue
            target = getattr(owner, func.attr)
        elif isinstance(func, ast.Name) and func.id in bound:
            target, label = bound[func.id], func.id
            if not callable(target) or inspect.ismodule(target):
                continue
        else:
            continue
        for message in check_call(node, target, label):
            problems.append(problem(node.lineno, message))
    return problems


def check_text(path: str, text: str) -> tuple[list[Problem], int]:
    """Return the problems in the page's python blocks and the number of blocks."""
    problems = []
    blocks = 0
    for first_line, source in iter_blocks(text):
        blocks += 1
        problems.extend(check_block(path, first_line, source))
    return problems, blocks


def check_file(path: Path) -> list[Problem]:
    return check_text(str(path), path.read_text(encoding="utf-8"))[0]


def main(argv: list[str]) -> int:
    paths = [Path(arg) for arg in argv] or sorted(DEFAULT_ROOT.rglob("*.md"))
    try:
        sdk = importlib.import_module(SDK_PACKAGE)
    except ImportError:
        print(
            f"{SDK_PACKAGE} is not installed: pip install waldur-api-client",
            file=sys.stderr,
        )
        return 2
    version = getattr(sdk, "__version__", None)
    try:
        from importlib.metadata import version as dist_version

        version = version or dist_version("waldur-api-client")
    except Exception:
        pass

    problems = []
    blocks = 0
    for path in paths:
        file_problems, file_blocks = check_text(
            str(path), path.read_text(encoding="utf-8")
        )
        problems.extend(file_problems)
        blocks += file_blocks
    for p in problems:
        print(p)
    print(
        f"Checked {blocks} Python blocks in {len(paths)} files against "
        f"waldur-api-client {version or '(unknown version)'}: {len(problems)} problems."
    )
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

"""Convert workshop notebooks under notebooks/ to markdown/ for pre-commit."""

from __future__ import annotations

import sys
from pathlib import Path

from nbconvert import MarkdownExporter

REPO_ROOT = Path(__file__).resolve().parent.parent

NOTEBOOK_TO_MARKDOWN: dict[str, str] = {
    "notebooks/python_basics.ipynb": "markdown/Python Basics.md",
    "notebooks/using_packages.ipynb": "markdown/Using Packages.md",
}


def _repo_relative(path: str) -> str:
    p = Path(path)
    if not p.is_absolute():
        return p.as_posix()
    return p.relative_to(REPO_ROOT).as_posix()


def convert(notebook_rel: str) -> None:
    output_rel = NOTEBOOK_TO_MARKDOWN.get(notebook_rel)
    if output_rel is None:
        print(f"Skipping unmapped notebook: {notebook_rel}", file=sys.stderr)
        return

    notebook = REPO_ROOT / notebook_rel
    output = REPO_ROOT / output_rel

    exporter = MarkdownExporter()
    body, _resources = exporter.from_filename(str(notebook))
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(body, encoding="utf-8")
    print(f"Wrote {output_rel}")


def main(argv: list[str]) -> int:
    if len(argv) > 1:
        targets = [_repo_relative(arg) for arg in argv[1:]]
    else:
        targets = list(NOTEBOOK_TO_MARKDOWN.keys())

    unknown = [t for t in targets if t not in NOTEBOOK_TO_MARKDOWN]
    if unknown:
        print(
            "Unknown notebook(s). Expected one of:\n  "
            + "\n  ".join(NOTEBOOK_TO_MARKDOWN),
            file=sys.stderr,
        )
        return 1

    for notebook_rel in targets:
        convert(notebook_rel)

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

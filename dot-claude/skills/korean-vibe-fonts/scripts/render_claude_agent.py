#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]
TEMPLATE_PATH = BASE_DIR / "adapters" / "claude-code-agent.template.md"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Render a Claude Code subagent file for korean-vibe-fonts using absolute resource paths."
    )
    parser.add_argument(
        "--output",
        required=True,
        help="Where to write the Claude Code agent markdown file."
    )
    parser.add_argument(
        "--skill-root",
        default=str(BASE_DIR),
        help="Root path of this skill bundle. Defaults to the current installed location."
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    skill_root = Path(args.skill_root).expanduser().resolve()
    output = Path(args.output).expanduser().resolve()

    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    rendered = template.replace("__SKILL_ROOT__", str(skill_root))

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(rendered, encoding="utf-8")

    print(f"Wrote Claude Code agent to: {output}")
    print(f"Using skill root: {skill_root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Run deterministic structure and contract checks for the candidate Skill."""

from __future__ import annotations

import math
import re
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
SKILL = ROOT / "SKILL.md"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)
    print(f"[OK] {message}")


def main() -> None:
    required = [
        "SKILL.md",
        "INTAKE.md",
        "EVAL.md",
        "TESTS.md",
        "CHANGELOG.md",
        "agents/openai.yaml",
        "assets/parent-intake-card.md",
        "assets/reading-adventure-handbook-template.md",
        "references/activity-library.md",
        "references/content-grounding.md",
        "references/design-principles.md",
        "references/safety-and-tools.md",
        "benchmark/BENCHMARK.md",
    ]
    for relative in required:
        require((ROOT / relative).is_file(), f"required file exists: {relative}")

    text = SKILL.read_text(encoding="utf-8")
    markers = [
        "## Select the smallest sufficient output mode",
        "`ideas`",
        "`plan`",
        "`full`",
        "## Resolve constraints in priority order",
        "Use a standard two-page packet",
        "Add an optional Page C only",
        "### 3a. Protect varied play rhythm in a full handbook",
        "ceil(p × n)",
        "floor(p × n)",
        "references/safety-and-tools.md",
    ]
    for marker in markers:
        require(marker in text, f"contract marker present: {marker}")

    forbidden = [
        "## Produce two coordinated outputs",
        "one- or two-page adventure packet",
        "Use a two- or three-page rhythm",
    ]
    for marker in forbidden:
        require(marker not in text, f"obsolete ambiguous rule absent: {marker}")

    linked = set(re.findall(r"`((?:assets|references)/[^`]+)`", text))
    for relative in sorted(linked):
        require((ROOT / relative).is_file(), f"linked file exists: {relative}")

    metadata = yaml.safe_load((ROOT / "agents/openai.yaml").read_text(encoding="utf-8"))
    require(bool(metadata["interface"]["display_name"]), "openai.yaml interface parses")

    n = 3
    require(math.ceil(0.6 * n) == 2, "three-core toy-like minimum is two")
    require(math.ceil(0.7 * n) == 3, "three-core autonomous minimum is three")
    require(math.floor(0.25 * n) == 0, "three-core organizer maximum is zero")

    print("Contract validation passed.")


if __name__ == "__main__":
    main()

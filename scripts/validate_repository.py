#!/usr/bin/env python3
"""Validate ICE Tech Skills structure without third-party dependencies."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = {
    "code-review",
    "database-change",
    "fix-bug",
    "implement-feature",
    "investigate",
    "refactor",
}
REQUIRED_GROUPS = {
    "governance": 7,
    "standards": 7,
    "stacks": 7,
    "templates": 2,
}


def fail(message: str) -> None:
    raise ValueError(message)


def load_json(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        fail(f"Invalid JSON in {path.relative_to(ROOT)}: {error}")
    if not isinstance(value, dict):
        fail(f"Expected an object in {path.relative_to(ROOT)}")
    return value


def validate_manifests() -> None:
    portable = load_json(ROOT / "plugin.json")
    compatibility = load_json(ROOT / ".codex-plugin" / "plugin.json")

    for path, manifest in (
        ("plugin.json", portable),
        (".codex-plugin/plugin.json", compatibility),
    ):
        if manifest.get("name") != "ice-tech-skills":
            fail(f"Unexpected plugin name in {path}")
        if not re.fullmatch(r"\d+\.\d+\.\d+", str(manifest.get("version", ""))):
            fail(f"Plugin version is not strict semver in {path}")
        if "[TODO:" in json.dumps(manifest):
            fail(f"Unfinished placeholder in {path}")

    if portable.get("$schema") != "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json":
        fail("Portable manifest has an unexpected schema")
    if compatibility.get("skills") != "./skills/":
        fail("Compatibility manifest must expose ./skills/")


def validate_skills() -> None:
    skill_dirs = {path.name for path in (ROOT / "skills").iterdir() if path.is_dir()}
    if skill_dirs != SKILLS:
        fail(f"Unexpected skill set: {sorted(skill_dirs)}")

    for name in sorted(SKILLS):
        path = ROOT / "skills" / name / "SKILL.md"
        text = path.read_text(encoding="utf-8")
        match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
        if not match:
            fail(f"Invalid frontmatter in {path.relative_to(ROOT)}")
        frontmatter = match.group(1)
        if not re.search(rf"^name:\s*{re.escape(name)}\s*$", frontmatter, re.MULTILINE):
            fail(f"Skill name does not match folder: {path.relative_to(ROOT)}")
        if not re.search(r"^description:\s*\S.+$", frontmatter, re.MULTILINE):
            fail(f"Missing skill description: {path.relative_to(ROOT)}")


def validate_required_files() -> None:
    for group, expected in REQUIRED_GROUPS.items():
        base = ROOT / group
        count = sum(1 for path in base.rglob("*") if path.is_file())
        if count != expected:
            fail(f"Expected {expected} files in {group}, found {count}")


def validate_markdown_links() -> None:
    broken: list[str] = []
    pattern = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
    for source in ROOT.rglob("*.md"):
        for target in pattern.findall(source.read_text(encoding="utf-8")):
            relative = target.split("#", 1)[0]
            if not relative or "://" in relative or relative.startswith("mailto:"):
                continue
            if not (source.parent / relative).resolve().exists():
                broken.append(f"{source.relative_to(ROOT)} -> {target}")
    if broken:
        fail("Broken Markdown links:\n" + "\n".join(broken))


def main() -> int:
    try:
        validate_manifests()
        validate_skills()
        validate_required_files()
        validate_markdown_links()
    except (OSError, ValueError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1

    print("PASS: plugin manifests, six skills, required files, and Markdown links")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

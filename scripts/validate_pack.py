#!/usr/bin/env python3
"""Audit CobbleHorizons first-party datapacks and optional Modrinth .mrpack.

Only Python's standard library is required. By default, detected errors return
a non-zero exit code. --audit-only is for an incomplete source recovery, NEVER
for release approval.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import zipfile
from collections import Counter
from pathlib import Path, PurePosixPath


def finding(level: str, code: str, location: str, detail: str) -> dict:
    return {"level": level, "code": code, "location": location, "detail": detail}


def read_json(path: Path, issues: list[dict]):
    try:
        return json.loads(path.read_text(encoding="utf-8-sig"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        issues.append(finding("error", "INVALID_JSON", str(path), str(exc)))
        return None


def advancement_id(path: Path, pack: Path) -> str:
    parts = path.relative_to(pack).parts
    return f"{parts[1]}:{'/'.join(parts[3:])[:-5]}"


def dependency_gate(quest: dict, parent: str) -> bool:
    for criterion in quest.get("criteria", {}).values():
        conditions = criterion.get("conditions", {})
        if not isinstance(conditions, dict):
            continue
        player = conditions.get("player", {})
        if not isinstance(player, dict):
            continue
        type_specific = player.get("type_specific", {})
        if not isinstance(type_specific, dict):
            continue
        advancements = type_specific.get("advancements", {})
        if isinstance(advancements, dict) and advancements.get(parent) is True:
            return True
    return False


def validate_source(source: Path) -> tuple[list[dict], dict]:
    issues: list[dict] = []
    datapacks = source / "datapacks"
    packs = sorted(p for p in datapacks.iterdir() if p.is_dir()) if datapacks.is_dir() else []
    quests: dict[str, tuple[Path, dict]] = {}
    functions: set[str] = set()
    all_json = 0
    for pack in packs:
        meta = pack / "pack.mcmeta"
        if not meta.is_file():
            issues.append(finding("error", "PACK_META_MISSING", str(pack), "Missing pack.mcmeta"))
        else:
            metadata = read_json(meta, issues)
            if isinstance(metadata, dict) and "pack" not in metadata:
                issues.append(finding("error", "PACK_META_INVALID", str(meta), "No pack object"))
        for file in pack.rglob("*.json"):
            all_json += 1
            doc = read_json(file, issues)
            if doc is None:
                continue
            parts = file.relative_to(pack).parts
            if len(parts) >= 4 and parts[0] == "data" and parts[2] == "advancement":
                if not isinstance(doc, dict):
                    issues.append(finding("error", "ADVANCEMENT_INVALID", str(file), "Expected an object"))
                    continue
                ident = advancement_id(file, pack)
                if ident in quests:
                    issues.append(finding("error", "DUPLICATE_ADVANCEMENT", ident, str(file)))
                else:
                    quests[ident] = (file, doc)
            if len(parts) >= 4 and parts[0] == "data" and parts[2] == "function":
                pass
        for fn in pack.rglob("*.mcfunction"):
            parts = fn.relative_to(pack).parts
            if len(parts) >= 4 and parts[0] == "data" and parts[2] == "function":
                functions.add(f"{parts[1]}:{'/'.join(parts[3:])[:-11]}")

    missing_references = 0
    active_count = 0
    parents: dict[str, str] = {}
    for ident, (file, doc) in quests.items():
        parent = doc.get("parent")
        criteria = doc.get("criteria", {})
        disabled = bool(criteria) and all(
            isinstance(c, dict) and c.get("trigger") == "minecraft:impossible"
            for c in criteria.values()
        )
        if not disabled:
            active_count += 1
        if not isinstance(criteria, dict) or not criteria:
            issues.append(finding("error", "CRITERIA_MISSING", ident, str(file)))
        requirements = doc.get("requirements", [])
        if not isinstance(requirements, list) or not requirements:
            issues.append(finding("error", "REQUIREMENTS_MISSING", ident, str(file)))
        else:
            for group in requirements:
                if not isinstance(group, list) or not group or any(c not in criteria for c in group):
                    issues.append(finding("error", "REQUIREMENTS_INVALID", ident, str(file)))
                    break
        if parent:
            parents[ident] = parent
            if parent.startswith("cobblehorizons:") and parent not in quests:
                missing_references += 1
                issues.append(finding("error", "PARENT_MISSING", ident, parent))
            if not disabled and not dependency_gate(doc, parent):
                issues.append(finding("error", "PREREQUISITE_MISSING", ident, parent))
        elif ident != "cobblehorizons:questz/root":
            issues.append(finding("error", "PARENT_REQUIRED", ident, "Active quest/root relationship missing"))
        reward = doc.get("rewards", {})
        if isinstance(reward, dict) and reward.get("function"):
            fn = reward["function"]
            if fn not in functions:
                issues.append(finding("error", "REWARD_FUNCTION_MISSING", ident, fn))
        if disabled and not doc.get("display", {}).get("hidden", False):
            issues.append(finding("warning", "DISABLED_VISIBLE", ident, "Impossible quest is visible"))

    colors: dict[str, int] = {}
    def visit(ident: str, stack: list[str]) -> None:
        state = colors.get(ident, 0)
        if state == 2:
            return
        if state == 1:
            issues.append(finding("error", "PARENT_CYCLE", ident, " -> ".join(stack + [ident])))
            return
        colors[ident] = 1
        parent = parents.get(ident)
        if parent in quests:
            visit(parent, stack + [ident])
        colors[ident] = 2

    for ident in quests:
        visit(ident, [])

    if "cobblehorizons:questz/root" not in quests:
        issues.append(finding("error", "QUEST_ROOT_MISSING", str(datapacks), "QuestZ root not found"))

    progression = datapacks / "CobbleHorizons-Progression"
    if progression.is_dir() and not list(progression.rglob("data/*")):
        issues.append(finding("error", "PROGRESSION_DATA_MISSING", str(progression),
                              "Progression pack contains no data; compare against v1.2.0 release"))
    elif not progression.is_dir():
        issues.append(finding("error", "PROGRESSION_PACK_MISSING", str(progression), "Missing progression pack"))

    return issues, {"packs": len(packs), "json_files": all_json,
                    "advancements": len(quests), "active_advancements": active_count,
                    "missing_parents": missing_references}


def validate_mrpack(file: Path) -> tuple[list[dict], dict]:
    issues: list[dict] = []
    stats: dict = {"archive": str(file)}
    if not file.is_file():
        return [finding("error", "MRPACK_NOT_FOUND", str(file), "Archive not present")], stats
    try:
        with zipfile.ZipFile(file) as archive:
            names = archive.namelist()
            duplicates = [name for name, count in Counter(names).items() if count > 1]
            for name in duplicates:
                issues.append(finding("error", "DUPLICATE_ZIP_ENTRY", name, "Entry occurs more than once"))
            for name in names:
                pp = PurePosixPath(name)
                if pp.is_absolute() or ".." in pp.parts or "\\" in name:
                    issues.append(finding("error", "UNSAFE_ZIP_ENTRY", name, "Unsafe archive path"))
            corrupt = archive.testzip()
            if corrupt:
                issues.append(finding("error", "ZIP_CORRUPT", corrupt, "CRC or extraction error"))
            if "modrinth.index.json" not in names:
                issues.append(finding("error", "MANIFEST_MISSING", str(file), "Missing Modrinth index"))
            else:
                try:
                    manifest = json.loads(archive.read("modrinth.index.json"))
                except (ValueError, UnicodeError) as exc:
                    issues.append(finding("error", "MANIFEST_INVALID", str(file), str(exc)))
                    manifest = {}
                if manifest.get("formatVersion") != 1 or manifest.get("game") != "minecraft":
                    issues.append(finding("error", "MANIFEST_FORMAT_INVALID", str(file), "Expected Modrinth v1/Minecraft"))
                deps = manifest.get("dependencies", {})
                if deps.get("minecraft") != "1.21.1" or "fabric-loader" not in deps:
                    issues.append(finding("error", "DEPENDENCIES_INVALID", str(file),
                                          "Expected Minecraft 1.21.1 + Fabric loader"))
                items = manifest.get("files", [])
                paths = [item.get("path") for item in items if isinstance(item, dict)]
                if len(paths) != len(set(paths)):
                    issues.append(finding("error", "DUPLICATE_MANIFEST_FILE", str(file), "Duplicate manifest paths"))
                for item in items:
                    if not isinstance(item, dict) or not item.get("path") or not item.get("hashes"):
                        issues.append(finding("error", "MANIFEST_FILE_INVALID", str(file), str(item)[:100]))
                stats["manifest_files"] = len(items)
                stats["minecraft"] = deps.get("minecraft")
                stats["fabric_loader"] = deps.get("fabric-loader")
            stats["zip_entries"] = len(names)
    except (OSError, zipfile.BadZipFile, RuntimeError) as exc:
        issues.append(finding("error", "ZIP_INVALID", str(file), str(exc)))
    return issues, stats


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=Path("."))
    parser.add_argument("--mrpack", type=Path, help="Also validate the published .mrpack")
    parser.add_argument("--audit-only", action="store_true",
                        help="Report errors but return success for discovery; never use for a release")
    parser.add_argument("--output", type=Path, help="Write machine-readable JSON report")
    args = parser.parse_args()
    source_issues, source_stats = validate_source(args.source)
    findings = source_issues
    report = {"source": source_stats}
    if args.mrpack:
        archive_issues, archive_stats = validate_mrpack(args.mrpack)
        findings = findings + archive_issues
        report["mrpack"] = archive_stats
    report["findings"] = findings
    report["errors"] = sum(item["level"] == "error" for item in findings)
    report["warnings"] = sum(item["level"] == "warning" for item in findings)
    print(json.dumps(report, indent=2, ensure_ascii=False))
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    if report["errors"] and not args.audit_only:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

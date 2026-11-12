#!/usr/bin/env python3
"""Restore the QuestZ 1.0.1 advancement-backed quest UI to the 1.3 alpha.

QuestZ 1.1.1 expects world/config chapter JSON; CobbleHorizons' authored
campaign still consists of Minecraft advancements and used QuestZ 1.0.1.
Use the exact QuestZ manifest record from the verified v1.2 release.
No other mod file or first-party datapack is changed.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import zipfile
from pathlib import Path
from restore_v1_2_sources import V12_SHA256

PROJECT_ID = "q1Xo6imm"
OLD_VERSION = "1.0.1"
NEW_VERSION = "1.1.1"


def is_questz(entry: dict) -> bool:
    return entry.get("path", "").lower().startswith("mods/questz-") and entry["path"].endswith(".jar")


def patch(source: Path, baseline: Path, dest: Path) -> dict:
    if source.resolve() == dest.resolve() or baseline.resolve() == dest.resolve():
        raise ValueError("Never overwrite an input package")
    if hashlib.sha256(baseline.read_bytes()).hexdigest() != V12_SHA256:
        raise ValueError("Official 1.2.0 baseline checksum differs from known-good SHA-256")
    with zipfile.ZipFile(source) as current, zipfile.ZipFile(baseline) as old:
        if current.testzip() or old.testzip():
            raise ValueError("A ZIP entry failed CRC verification")
        if len(current.namelist()) != len(set(current.namelist())):
            raise ValueError("Duplicate ZIP entry in current alpha")
        current_index = json.loads(current.read("modrinth.index.json"))
        old_index = json.loads(old.read("modrinth.index.json"))
        current_q = [f for f in current_index["files"] if is_questz(f)]
        old_q = [f for f in old_index["files"] if is_questz(f)]
        if len(current_q) != 1 or len(old_q) != 1:
            raise ValueError("Expected exactly one QuestZ file in each package")
        current_entry = current_q[0]
        legacy_entry = old_q[0]
        if NEW_VERSION not in current_entry["path"]:
            raise ValueError("Input is not the known QuestZ 1.1.1 alpha")
        if OLD_VERSION not in legacy_entry["path"]:
            raise ValueError("Baseline does not contain QuestZ 1.0.1")
        if not any(f"/data/{PROJECT_ID}/" in url for url in legacy_entry.get("downloads", [])):
            raise ValueError("Legacy QuestZ record uses an unexpected Modrinth project")
        if current_index.get("dependencies", {}).get("fabric-loader") != "0.19.5":
            raise ValueError("Expected Fabric Loader 0.19.5; do not change other versions")
        if not any("mods/Cobblemon-fabric-1.8.4" in f["path"] for f in current_index["files"]):
            raise ValueError("Expected Cobblemon 1.8.4")
        if not any(name.endswith("/advancement/questz/root.json") for name in current.namelist()):
            raise ValueError("First-party CobbleHorizons advancement source is missing")
        if any(name.startswith("overrides/config/questz/default/") for name in current.namelist()):
            raise ValueError("A native QuestZ 1.1+ chapter pack is already present")
        idx = next(i for i, f in enumerate(current_index["files"]) if is_questz(f))
        current_index["files"][idx] = legacy_entry
        current_index["name"] = "CobbleHorizons 1.3.0 Alpha 2.1 (QuestZ compatibility)"
        current_index["versionId"] = "1.3.0-alpha.2.1-questz-legacy"
        dest.parent.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(dest, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as final:
            for info in current.infolist():
                if info.filename == "modrinth.index.json":
                    data = (json.dumps(current_index, ensure_ascii=False, indent=2) + "\n").encode()
                elif info.is_dir():
                    data = b""
                else:
                    data = current.read(info.filename)
                final.writestr(info, data)
    with zipfile.ZipFile(dest) as check:
        if check.testzip() or len(set(check.namelist())) != len(check.namelist()):
            raise ValueError("Output ZIP integrity failure")
        manifest = json.loads(check.read("modrinth.index.json"))
        q = [f for f in manifest["files"] if is_questz(f)]
        if len(q) != 1 or q[0] != legacy_entry:
            raise ValueError("Legacy QuestZ entry was not preserved")
        return {
            "filename": str(dest),
            "sha256": hashlib.sha256(dest.read_bytes()).hexdigest(),
            "questz_from": current_entry["path"],
            "questz_to": legacy_entry["path"],
            "unchanged_manifest_entries": len(manifest["files"]) - 1,
            "manifest_entries": len(manifest["files"]),
            "zip_entries": len(check.namelist()),
            "minecraft_client_tested": False,
        }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--alpha2", type=Path, required=True)
    parser.add_argument("--baseline", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    result = patch(args.alpha2, args.baseline, args.output)
    text = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    print(text)
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()

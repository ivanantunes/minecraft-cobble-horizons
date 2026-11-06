#!/usr/bin/env python3
"""Build a NOT-FOR-RELEASE CobbleHorizons 1.3.0 alpha MRPack.

Pin the exact v1.2.0 archive, preserve all third-party manifest references and
binary overrides, replace first-party datapack source from this branch, overlay
the PokéMart configuration, and append the official hashed Modrinth Outbreaks
file. No third-party JARs are copied into the archive.

This performs a packaging test, NOT an in-game or migration test.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import zipfile
from pathlib import Path

from restore_v1_2_sources import V12_SHA256

PREFIX = "overrides/datapacks/"
ALLOWED_SOURCE = {".json", ".mcfunction", ".mcmeta"}
PACKS = ("CobbleHorizons-QuestZ", "CobbleHorizons-Progression")


def first_party_overlays(repo: Path) -> dict[str, bytes]:
    payload = {}
    for pack in PACKS:
        folder = repo / "datapacks" / pack
        if not folder.exists():
            raise ValueError(f"Missing required first-party datapack: {folder}")
        for file in folder.rglob("*"):
            if file.is_file():
                relative = file.relative_to(repo).as_posix()
                if file.suffix not in ALLOWED_SOURCE:
                    raise ValueError("Unexpected first-party binary/asset: " + relative)
                payload[f"overrides/{relative}"] = file.read_bytes()
    shop = repo / "config/cobbledollars/default_shop.json"
    if not shop.is_file():
        raise ValueError("Missing CobbleDollars shop source")
    json.loads(shop.read_text(encoding="utf-8"))
    payload["overrides/config/cobbledollars/default_shop.json"] = shop.read_bytes()
    return payload


def pack_addon_entry(spec: dict, manifest: dict) -> dict:
    if spec.get("project_id") != "nxE2RfXE" or spec.get("version_id") != "Rlt9c9kz":
        raise ValueError("Outbreaks candidate must match reviewed Modrinth version 1.1.2")
    if spec.get("version_number") != "1.1.2" or "fabric" not in spec.get("loaders", []):
        raise ValueError("Unexpected mod version or loader")
    baseline_deps = spec.get("baseline_dependencies", {})
    if "missing_required_dependencies" not in baseline_deps:
        raise ValueError("Addon spec must include baseline dependency verification")
    if baseline_deps["missing_required_dependencies"]:
        raise ValueError("Addon has missing required dependencies")
    obj = spec["file"]
    hashes = obj["hashes"]
    if not re.fullmatch(r"[0-9a-f]{128}", hashes["sha512"]):
        raise ValueError("Missing valid SHA-512 from Modrinth")
    if not re.fullmatch(r"[0-9a-f]{40}", hashes["sha1"]):
        raise ValueError("Missing valid SHA-1 from Modrinth")
    if not obj["filename"].endswith(".jar") or "/" in obj["filename"]:
        raise ValueError("Unsafe mod JAR filename")
    if not obj["url"].startswith(
        "https://cdn.modrinth.com/data/nxE2RfXE/versions/Rlt9c9kz/"
    ):
        raise ValueError("Unexpected Modrinth download source")
    path = "mods/" + obj["filename"]
    if path in {item["path"] for item in manifest.get("files", [])}:
        raise ValueError("Outbreaks JAR is already in base manifest")
    return {
        "path": path,
        "hashes": hashes,
        "env": {"client": "required", "server": "required"},
        "downloads": [obj["url"]],
        "fileSize": 0,  # replaced after verifying exact remote file size in future
    }


def build(base: Path, repo: Path, spec: dict, target: Path,
          expected_sha: str = V12_SHA256) -> dict:
    if target.resolve() == base.resolve():
        raise ValueError("Cannot overwrite published baseline")
    sha = hashlib.sha256(base.read_bytes()).hexdigest()
    if sha != expected_sha:
        raise ValueError("Baseline checksum mismatch")
    overlays = first_party_overlays(repo)
    with zipfile.ZipFile(base) as src:
        if src.testzip():
            raise ValueError("Baseline ZIP failed CRC check")
        names = set(src.namelist())
        if len(names) != len(src.namelist()):
            raise ValueError("Duplicate entry in baseline")
        base_pack_entries = {name for name in names if name.startswith(PREFIX)
                             and not name.endswith("/")}
        missing_source = sorted(base_pack_entries.difference(overlays))
        if missing_source:
            raise ValueError(f"First-party source missing for archive entries: {missing_source[:10]}")
        manifest = json.loads(src.read("modrinth.index.json"))
        if (manifest.get("dependencies", {}).get("minecraft") != "1.21.1"
                or manifest.get("dependencies", {}).get("fabric-loader") != "0.19.3"):
            raise ValueError("Unexpected Minecraft/Fabric baseline")
        addition = pack_addon_entry(spec, manifest)
        # Modrinth v1 manifests require a valid size. Candidate workflow
        # obtains the exact size from the official download during packaging.
        if addition["fileSize"] <= 0:
            raise ValueError("Official addon file size not provided")
        manifest["files"].append(addition)
        manifest["versionId"] = "1.3.0-alpha.1"
        manifest["name"] = "CobbleHorizons 1.3.0 Alpha"
        target.parent.mkdir(parents=True, exist_ok=True)
        new_files = sorted(set(overlays) - names)
        with zipfile.ZipFile(target, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as dest:
            for info in src.infolist():
                if info.is_dir():
                    dest.writestr(info, b"")
                elif info.filename == "modrinth.index.json":
                    dest.writestr(info.filename, json.dumps(manifest, indent=2) + "\n")
                else:
                    dest.writestr(info, overlays.get(info.filename, src.read(info.filename)))
            for path in new_files:
                dest.writestr(path, overlays[path])
    return {
        "base_sha256": sha,
        "alpha_sha256": hashlib.sha256(target.read_bytes()).hexdigest(),
        "output": str(target),
        "manifest_files": len(manifest["files"]),
        "new_first_party_overrides": new_files,
        "replaced_first_party_overrides": len(set(overlays) & names),
        "modrinth_addon": spec["version_number"],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline", type=Path, required=True)
    parser.add_argument("--repo", type=Path, default=Path("."))
    parser.add_argument("--addon-spec", type=Path, required=True)
    parser.add_argument("--addon-size", type=int, required=True,
                        help="Exact official file size obtained from Modrinth HEAD or GET")
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--report", type=Path, default=Path("alpha-build-report.json"))
    args = parser.parse_args()
    spec = json.loads(args.addon_spec.read_text(encoding="utf-8"))
    # Exact file length is verified by CI against its downloaded SHA-512 hash.
    spec["file"]["size"] = args.addon_size
    result = build(args.baseline, args.repo.resolve(), spec, args.output)
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Build a test-only CobbleHorizons 1.3 alpha for Cobblemon 1.8.4.

Rebuilds from the SHA-pinned published 1.2.0 MRPack, the 69 exact Modrinth
mod version IDs in the user-provided upgrade inventory, and the first-party
datapack/shop sources in this same branch. No JARs or saves are bundled.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import urllib.parse
import urllib.request
import zipfile
from pathlib import Path, PurePosixPath

from build_alpha_mrpack import first_party_overlays
from restore_v1_2_sources import V12_SHA256

API = "https://api.modrinth.com/v2"
INVENTORY = "docs/migration-1.8.4-upload-inventory.json"
NESTS_VERSION = "e4li5aWm"
OUTBREAKS_PROJECT = "nxE2RfXE"
DROP_CONFIGS = {
    "overrides/config/cobblemonnestsdens.json",
    "overrides/config/cobblemonnestsdens-client.json",
}
HEADERS = {"User-Agent": "CobbleHorizons/1.3.0-alpha.2 (+https://github.com/ivanantunes/minecraft-cobble-horizons)"}


def project_from_url(item: dict) -> str | None:
    for url in item.get("downloads", []):
        split = urllib.parse.urlsplit(url)
        parts = split.path.strip("/").split("/")
        if split.hostname == "cdn.modrinth.com" and len(parts) >= 4 and parts[0] == "data":
            return parts[1]
    return None


def fetch_versions(ids: list[str]) -> dict[str, dict]:
    versions = {}
    for pos in range(0, len(ids), 16):
        batch = ids[pos:pos + 16]
        query = urllib.parse.urlencode({"ids": json.dumps(batch)})
        request = urllib.request.Request(f"{API}/versions?{query}", headers=HEADERS)
        with urllib.request.urlopen(request, timeout=45) as response:
            result = json.load(response)
        for version in result:
            versions[version["id"]] = version
    if set(ids) != set(versions):
        raise ValueError(f"Missing published Modrinth versions: {set(ids)-set(versions)}")
    return versions


def mod_entries(versions: dict[str, dict], ids: list[str], baseline: dict) -> list[dict]:
    existing = {}
    for item in baseline["files"]:
        if not item["path"].startswith("mods/"):
            continue
        pid = project_from_url(item)
        if pid:
            existing[pid] = item
    output = []
    missing = []
    for vid in ids:
        if vid == NESTS_VERSION:
            continue
        version = versions[vid]
        if "1.21.1" not in version.get("game_versions", []) or "fabric" not in version.get("loaders", []):
            raise ValueError(f"Not a Fabric 1.21.1 release: {vid}")
        pid = version["project_id"]
        files = version.get("files", [])
        file = next((f for f in files if f.get("primary")), files[0] if files else None)
        if not file or not file.get("filename", "").endswith(".jar"):
            raise ValueError(f"Missing official JAR for {vid}")
        filename = file["filename"]
        if "/" in filename or "\\" in filename:
            raise ValueError(f"Unsafe addon filename: {filename}")
        url = file.get("url", "")
        if not url.startswith(f"https://cdn.modrinth.com/data/{pid}/versions/{vid}/"):
            raise ValueError(f"Unexpected CDN URL for {vid}: {url}")
        hashes = file.get("hashes", {})
        if len(hashes.get("sha512", "")) != 128 or len(hashes.get("sha1", "")) != 40:
            raise ValueError(f"Missing hashes for {vid}")
        env = existing.get(pid, {}).get("env")
        if env is None and pid == OUTBREAKS_PROJECT:
            env = {"client": "required", "server": "required"}
        if env is None:
            missing.append({"project_id": pid, "version_id": vid, "filename": filename})
            continue
        output.append({"path": "mods/" + filename, "hashes": hashes,
                       "env": env, "downloads": [url], "fileSize": file["size"]})
    if missing:
        raise ValueError(f"No baseline env for updated projects (review manually): {missing}")
    if len(output) != 68 or len({x["path"] for x in output}) != 68:
        raise ValueError(f"Expected 68 distinct compatible mods, found {len(output)}")
    if not any(x["path"].startswith("mods/Cobblemon-fabric-1.8.4+") for x in output):
        raise ValueError("Cobblemon 1.8.4 is missing")
    if not any("fabric-language-kotlin-1.14.2" in x["path"] for x in output):
        raise ValueError("Fabric Language Kotlin 1.14.2 missing")
    if any("cobblemonnestsdens" in x["path"].lower() for x in output):
        raise ValueError("Incompatible Nests & Dens is still present")
    return output


def build(baseline: Path, repo: Path, target: Path) -> dict:
    if hashlib.sha256(baseline.read_bytes()).hexdigest() != V12_SHA256:
        raise ValueError("Incorrect v1.2.0 baseline SHA-256")
    inventory = json.loads((repo / INVENTORY).read_text())
    version_ids = inventory["modrinth_mod_version_ids"].split()
    if len(version_ids) != 69 or len(set(version_ids)) != 69 or NESTS_VERSION not in version_ids:
        raise ValueError("Unexpected source version inventory")
    versions = fetch_versions(version_ids)
    firstparty = first_party_overlays(repo)
    with zipfile.ZipFile(baseline) as src:
        if src.testzip() or len(src.namelist()) != len(set(src.namelist())):
            raise ValueError("Corrupt or duplicate baseline entries")
        manifest = json.loads(src.read("modrinth.index.json"))
        if manifest["dependencies"] != {"minecraft": "1.21.1", "fabric-loader": "0.19.3"}:
            raise ValueError("Unexpected baseline version")
        non_mods = [f for f in manifest["files"] if not f["path"].startswith("mods/")]
        # Preserve the user's ALREADY-TESTED updated shader versions rather
        # than silently restoring v1.2-era shader packs.
        shader_data = json.loads((repo / "docs/alpha2-shaderpack-pins.json").read_text())
        shader_pins = shader_data["shaderpacks"]
        if len(shader_pins) != 3 or len({p["path"] for p in shader_pins}) != 3:
            raise ValueError("Expected exactly three pinned alpha.2 shaderpacks")
        for pin in shader_pins:
            if not pin["path"].startswith("shaderpacks/"):
                raise ValueError("Invalid pinned shader path")
            if not pin["downloads"][0].startswith("https://cdn.modrinth.com/data/"):
                raise ValueError("Invalid pinned shader download URL")
            if len(pin["hashes"]["sha512"]) != 128:
                raise ValueError("Missing SHA-512 in shader pins")
        non_mods = [f for f in non_mods if not f["path"].startswith("shaderpacks/")]
        non_mods.extend(shader_pins)
        manifest["files"] = non_mods + mod_entries(versions, version_ids, manifest)
        if len(manifest["files"]) != 75:
            raise ValueError("Expected 75 Modrinth entries (68 mods + 7 resources)")
        manifest["dependencies"]["fabric-loader"] = "0.19.5"
        manifest["name"] = "CobbleHorizons 1.3.0 Alpha 2 (Cobblemon 1.8.4)"
        manifest["versionId"] = "1.3.0-alpha.2-cobblemon-1.8.4-test"
        manifest["summary"] = "Experimental Minecraft 1.21.1 / Cobblemon 1.8.4 compatibility build."
        included = set(src.namelist())
        for old in included:
            if old.startswith("overrides/datapacks/CobbleHorizons-") and not old.endswith("/") and old not in firstparty:
                raise ValueError(f"Tracked first-party file missing from branch: {old}")
        target.parent.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(target, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as out:
            for info in src.infolist():
                if info.filename in DROP_CONFIGS:
                    continue
                if info.filename == "modrinth.index.json":
                    data = (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode()
                elif info.is_dir():
                    data = b""
                else:
                    data = firstparty.get(info.filename, src.read(info.filename))
                out.writestr(info, data)
            for path in sorted(firstparty.keys() - included):
                out.writestr(path, firstparty[path])
    with zipfile.ZipFile(target) as z:
        if z.testzip():
            raise ValueError("Generated package failed CRC")
        if len(set(z.namelist())) != len(z.namelist()):
            raise ValueError("Duplicate ZIP entries")
        actual = json.loads(z.read("modrinth.index.json"))
        if len(actual["files"]) != 75 or actual["dependencies"]["fabric-loader"] != "0.19.5":
            raise ValueError("Bad alpha.2 manifest")
        return {"output": str(target), "sha256": hashlib.sha256(target.read_bytes()).hexdigest(),
                "entries": len(z.namelist()), "mods": 68, "manifest_files": 75,
                "loader": "0.19.5", "cobblemon": "1.8.4",
                "source_updated_mod_versions": len(version_ids),
                "nests_dens_removed": True, "minecraft_runtime_tested": False}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline", required=True, type=Path)
    parser.add_argument("--repo", type=Path, default=Path("."))
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--report", type=Path, default=Path("dist/alpha2-build-report.json"))
    args = parser.parse_args()
    result = build(args.baseline, args.repo.resolve(), args.output)
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

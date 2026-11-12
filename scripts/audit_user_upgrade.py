#!/usr/bin/env python3
"""Audit an *uploaded* 1.8.4 manifest snapshot against official Modrinth JAR metadata.

Read-only network requests, no redistribution of third-party JARs. This is a
preflight for the experimental upgrade, not proof of successful gameplay.
"""
from __future__ import annotations

import concurrent.futures
import hashlib
import io
import json
import re
import sys
import time
import urllib.parse
import urllib.request
import zipfile
from pathlib import Path

API = "https://api.modrinth.com/v2"
HEADERS = {"User-Agent": "CobbleHorizonsCompatibilityAudit/1.3.0 (+https://github.com/ivanantunes/minecraft-cobble-horizons)"}
INVENTORY = Path("docs/migration-1.8.4-upload-inventory.json")
OUTPUT = Path("docs/migration-1.8.4-audit-results.json")
EXCLUDE_BIG = ("Cobblemon-fabric-", "Mambience-", "fancymenu_", "Cobblemon-fabric-1.8.4")


def request(url):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=90) as response:
        return response.read()


def get_versions(ids):
    versions = []
    for start in range(0, len(ids), 16):
        batch = ids[start:start + 16]
        url = API + "/versions?" + urllib.parse.urlencode({"ids": json.dumps(batch)})
        versions.extend(json.loads(request(url)))
    return versions


def inspect_jar(version):
    files = version.get("files", [])
    if not files:
        return {"mod": version.get("name"), "error": "No files"}
    file = next((f for f in files if f.get("primary")), files[0])
    name = file.get("filename", "")
    if not name.endswith(".jar") or name.startswith(EXCLUDE_BIG):
        return {"mod": name, "skipped": "Large JAR or not a Fabric mod"}
    url = file.get("url", "")
    if not url.startswith("https://cdn.modrinth.com/data/"):
        return {"mod": name, "error": "Unexpected download domain"}
    try:
        data = request(url)
        if file.get("size") != len(data):
            raise ValueError("Size mismatch")
        if file.get("hashes", {}).get("sha512") != hashlib.sha512(data).hexdigest():
            raise ValueError("SHA-512 mismatch")
        with zipfile.ZipFile(io.BytesIO(data)) as archive:
            if archive.testzip():
                raise ValueError("Invalid ZIP CRC")
            meta = {}
            if "fabric.mod.json" in archive.namelist():
                meta = json.loads(archive.read("fabric.mod.json"))
            else:
                return {"mod": name, "warning": "No fabric.mod.json; may be datapack/jar-in-jar"}
        return {"mod": name, "id": meta.get("id"), "version": meta.get("version"),
                "depends": meta.get("depends", {}), "breaks": meta.get("breaks", {}),
                "conflicts": meta.get("conflicts", {}), "hash_verified": True}
    except Exception as exc:
        return {"mod": name, "error": str(exc)}


def main():
    inv = json.loads(INVENTORY.read_text())
    ids = inv["modrinth_mod_version_ids"].split()
    versions = get_versions(ids)
    found = {v["id"]: v for v in versions}
    base_projects = {v["project_id"] for v in versions}
    results = []
    for version_id in ids:
        v = found.get(version_id)
        if not v:
            results.append({"version_id": version_id, "error": "Modrinth version not found"})
            continue
        required_missing = [
            x.get("project_id") for x in v.get("dependencies", [])
            if x.get("dependency_type") == "required" and x.get("project_id")
            and x["project_id"] not in base_projects
        ]
        results.append({
            "project_id": v["project_id"], "version_id": v["id"], "name": v.get("name"),
            "game_versions": v.get("game_versions"), "loaders": v.get("loaders"),
            "required_modrinth_projects_missing": required_missing,
            "fabric_metadata": None,
        })
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        tasks = {pool.submit(inspect_jar, found[vid]): vid for vid in ids if vid in found}
        jars = {vid: future.result() for future, vid in tasks.items()}
    for entry in results:
        if entry.get("version_id") in jars:
            entry["fabric_metadata"] = jars[entry["version_id"]]
    flagged = []
    for entry in results:
        meta = entry.get("fabric_metadata") or {}
        dep = meta.get("depends", {}) if isinstance(meta, dict) else {}
        breaks = meta.get("breaks", {}) if isinstance(meta, dict) else {}
        if isinstance(dep, dict) and ("cobblemon" in dep or "rctmod" in dep or "fabricloader" in dep):
            flagged.append({"mod": meta.get("mod"), "id": meta.get("id"),
                            "cobblemon_requirement": dep.get("cobblemon"),
                            "rct_requirement": dep.get("rctmod"),
                            "fabricloader_requirement": dep.get("fabricloader"),
                            "breaks": breaks})
    report = {
        "cobblemon_installed": inv["cobblemon"],
        "manifest_mods": len(ids),
        "modrinth_versions_found": len(versions),
        "missing_dependencies": [
            {"mod": i.get("name"), "missing": i.get("required_modrinth_projects_missing")}
            for i in results if i.get("required_modrinth_projects_missing")
        ],
        "fabric_dependency_constraints": flagged,
        "jar_errors": [
            {"mod": e.get("name"), "detail": e.get("fabric_metadata")}
            for e in results if (e.get("fabric_metadata") or {}).get("error")
        ],
        "mods": results,
    }
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n")
    print("SUMMARY")
    print(json.dumps({k: v for k, v in report.items() if k != "mods"}, indent=2))
    if len(versions) != len(ids):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Resolve a verified Modrinth Fabric addon file without bundling third-party binaries.

The resolver makes read-only requests to Modrinth. Its JSON output pins the
project/version IDs, hashes, download URL, and declared dependencies for a
candidate alpha build. This does not prove runtime compatibility.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.parse
import urllib.request
from pathlib import Path

API = "https://api.modrinth.com/v2"
USER_AGENT = "CobbleHorizons/1.3.0-alpha (+https://github.com/ivanantunes/minecraft-cobble-horizons)"


def get_json(url: str):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT,
                                                "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.load(response)


def resolve(project_slug: str, version_number: str, game: str, loader: str):
    params = urllib.parse.urlencode({
        "game_versions": json.dumps([game]),
        "loaders": json.dumps([loader]),
    })
    versions = get_json(f"{API}/project/{project_slug}/version?{params}")
    matches = [v for v in versions
               if v.get("version_number") == version_number
               and game in v.get("game_versions", [])
               and loader in v.get("loaders", [])
               and v.get("version_type") == "release"]
    if len(matches) != 1:
        found = sorted({v.get("version_number", "") for v in versions})
        raise ValueError(f"Expected exactly one Fabric release for {version_number}; found "
                         f"{len(matches)}. Available: {found}")
    version = matches[0]
    files = version.get("files", [])
    if not files:
        raise ValueError("Version has no files")
    primary = next((f for f in files if f.get("primary")), files[0])
    hashes = primary.get("hashes", {})
    if not hashes.get("sha512") or not hashes.get("sha1"):
        raise ValueError("Modrinth version missing sha512 or sha1")
    url = primary.get("url", "")
    if not url.startswith("https://cdn.modrinth.com/data/"):
        raise ValueError("Refusing unexpected addon download URL: " + url)
    if not primary.get("filename", "").endswith(".jar"):
        raise ValueError("Expected addon JAR file")
    return {
        "project_slug": project_slug,
        "project_id": version["project_id"],
        "version_id": version["id"],
        "version_number": version["version_number"],
        "date_published": version.get("date_published"),
        "game_versions": version.get("game_versions", []),
        "loaders": version.get("loaders", []),
        "dependencies": version.get("dependencies", []),
        "file": {"filename": primary["filename"], "url": url,
                 "hashes": {"sha512": hashes["sha512"], "sha1": hashes["sha1"]}},
    }


def verify_baseline_dependencies(addon: dict, baseline: Path):
    import zipfile
    with zipfile.ZipFile(baseline) as archive:
        manifest = json.loads(archive.read("modrinth.index.json"))
    installed = set()
    for item in manifest.get("files", []):
        for url in item.get("downloads", []):
            parts = urllib.parse.urlparse(url).path.split("/")
            # cdn.modrinth.com/data/<project_id>/versions/<version_id>/<file>
            if len(parts) > 3 and parts[1] == "data":
                installed.add(parts[2])
    missing = [d for d in addon["dependencies"]
               if d.get("dependency_type") == "required"
               and d.get("project_id")
               and d["project_id"] not in installed]
    return {"existing_modrinth_projects": len(installed),
            "missing_required_dependencies": missing}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--project", default="cobblemon-outbreaks")
    p.add_argument("--version", default="1.1.2")
    p.add_argument("--game", default="1.21.1")
    p.add_argument("--loader", default="fabric")
    p.add_argument("--baseline", type=Path, help="Verify addon required dependencies in this MRPack")
    p.add_argument("--output", type=Path, required=True)
    args = p.parse_args()
    addon = resolve(args.project, args.version, args.game, args.loader)
    if args.baseline:
        addon["baseline_dependencies"] = verify_baseline_dependencies(addon, args.baseline)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(addon, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(addon, indent=2))
    if addon.get("baseline_dependencies", {}).get("missing_required_dependencies"):
        print("ERROR: required addon dependencies are missing from current pack", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Inspect official Modrinth addon JAR metadata without redistributing the JAR.

Downloads only the resolved, pinned Modrinth file; compares SHA-512/SHA-1,
byte length, ZIP CRC and fabric.mod.json. Emits a JSON audit report.
"""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import sys
import urllib.request
import zipfile
from pathlib import Path

USER_AGENT = "CobbleHorizons/1.3.0-alpha (+https://github.com/ivanantunes/minecraft-cobble-horizons)"


def inspect(spec: dict) -> dict:
    f = spec["file"]
    if spec.get("project_id") != "nxE2RfXE" or spec.get("version_id") != "Rlt9c9kz":
        raise ValueError("Unknown or unreviewed Outbreaks version")
    url = f["url"]
    if not url.startswith("https://cdn.modrinth.com/data/nxE2RfXE/versions/Rlt9c9kz/"):
        raise ValueError("Untrusted download source")
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=60) as response:
        data = response.read()
    digest512 = hashlib.sha512(data).hexdigest()
    digest1 = hashlib.sha1(data).hexdigest()
    if digest512 != f["hashes"]["sha512"] or digest1 != f["hashes"]["sha1"]:
        raise ValueError("Official addon hashes do not match the downloaded JAR")
    if len(data) != f["size"]:
        raise ValueError("Official addon size differs from manifest metadata")
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        corrupt = archive.testzip()
        if corrupt:
            raise ValueError("Corrupt JAR content: " + corrupt)
        if "fabric.mod.json" not in archive.namelist():
            raise ValueError("Selected JAR does not contain Fabric metadata")
        metadata = json.loads(archive.read("fabric.mod.json"))
        config_resources = [p for p in archive.namelist()
                            if "config" in p.lower() and (p.endswith(".json") or p.endswith(".json5"))]
    return {
        "project_id": spec["project_id"],
        "version_id": spec["version_id"],
        "file_name": f["filename"],
        "size": len(data),
        "sha512_verified": True,
        "sha1_verified": True,
        "jar_crc_verified": True,
        "fabric_metadata": {
            "id": metadata.get("id"),
            "version": metadata.get("version"),
            "environment": metadata.get("environment"),
            "depends": metadata.get("depends", {}),
            "breaks": metadata.get("breaks", {}),
        },
        "bundled_config_resources": config_resources,
    }


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--addon-spec", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    args = p.parse_args()
    result = inspect(json.loads(args.addon_spec.read_text(encoding="utf-8")))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())

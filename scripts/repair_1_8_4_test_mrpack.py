#!/usr/bin/env python3
"""Patch user-exported 1.3 alpha for Cobblemon 1.8.4 in a separate test instance.

This is a strictly scoped repair: remove Cobblemon Nests & Dens 1.3.3 from
Modrinth's file manifest and its now-unused configs, then declare Fabric Loader
0.19.5 for Fabric Language Kotlin 1.14.2. Not a substitute for runtime testing.
No third-party JARs, worlds, or external data are modified.
"""
import argparse
import hashlib
import json
import zipfile
from pathlib import Path

DROP = "mods/cobblemonnestsdens-fabric-1.3.3.jar"
DROP_CONFIGS = {
    "overrides/config/cobblemonnestsdens-client.json",
    "overrides/config/cobblemonnestsdens.json",
}


def repair(source: Path, target: Path):
    if source.resolve() == target.resolve():
        raise ValueError("Source and target must be different!")
    with zipfile.ZipFile(source) as src:
        if src.testzip() is not None:
            raise ValueError("Invalid original MRPack CRC")
        names = src.namelist()
        if len(names) != len(set(names)):
            raise ValueError("Original MRPack has duplicate entries")
        manifest = json.loads(src.read("modrinth.index.json"))
        assert manifest.get("game") == "minecraft"
        assert manifest.get("formatVersion") == 1
        assert manifest["dependencies"]["minecraft"] == "1.21.1"
        assert manifest["dependencies"]["fabric-loader"] == "0.19.3"
        paths = [f["path"] for f in manifest["files"]]
        if DROP not in paths:
            raise ValueError("Expected Nests & Dens 1.3.3 not found")
        if not any(x.startswith("mods/Cobblemon-fabric-1.8.4+") for x in paths):
            raise ValueError("This patch applies only to Cobblemon 1.8.4")
        if not any("fabric-language-kotlin-1.14.2" in x for x in paths):
            raise ValueError("This patch expects Fabric Language Kotlin 1.14.2")
        manifest["files"] = [f for f in manifest["files"] if f["path"] != DROP]
        manifest["dependencies"]["fabric-loader"] = "0.19.5"
        manifest["name"] = "CobbleHorizons 1.3.0 Alpha - 1.8.4 Compatibility Test"
        manifest["versionId"] = "1.3.0-alpha.1-cobblemon1.8.4-compat1"
        body = (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode()
        target.parent.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(target, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as dest:
            for info in src.infolist():
                if info.filename in DROP_CONFIGS:
                    continue
                content = body if info.filename == "modrinth.index.json" else src.read(info.filename)
                dest.writestr(info, content)
    with zipfile.ZipFile(target) as dest:
        if dest.testzip() is not None:
            raise ValueError("Output MRPack integrity error")
        result = json.loads(dest.read("modrinth.index.json"))
        assert result["dependencies"]["fabric-loader"] == "0.19.5"
        assert DROP not in [f["path"] for f in result["files"]]
        assert len(result["files"]) == len(paths)-1
        return {"path": str(target), "sha256": hashlib.sha256(target.read_bytes()).hexdigest(),
                "modrinth_entries": len(result["files"]), "zip_entries": len(dest.namelist())}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("source", type=Path)
    ap.add_argument("target", type=Path)
    args = ap.parse_args()
    print(json.dumps(repair(args.source, args.target), indent=2))


if __name__ == "__main__":
    main()

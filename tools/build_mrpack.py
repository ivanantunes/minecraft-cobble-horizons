#!/usr/bin/env python3
"""Build and validate a CobbleHorizons Modrinth pack from a known-good manifest."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import tempfile
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RELEASES = ROOT / "releases"


def replace_tree(source: Path, destination: Path) -> None:
    if destination.exists():
        shutil.rmtree(destination)
    shutil.copytree(source, destination)


def build(base_pack: Path, version: str) -> Path:
    output = RELEASES / f"CobbleHorizons-{version}.mrpack"
    if base_pack.resolve() == output.resolve():
        raise ValueError("The base pack and output pack must be different files")

    with tempfile.TemporaryDirectory(prefix="cobblehorizons-mrpack-") as temp_name:
        stage = Path(temp_name)
        with zipfile.ZipFile(base_pack) as archive:
            bad_member = archive.testzip()
            if bad_member:
                raise ValueError(f"Base pack has a corrupt member: {bad_member}")
            archive.extractall(stage)

        index_path = stage / "modrinth.index.json"
        index = json.loads(index_path.read_text(encoding="utf-8"))
        index["name"] = "CobbleHorizons"
        index["versionId"] = version
        index["summary"] = (
            f"CobbleHorizons {version} with 66 English Pokemon quests, "
            "stable Boundless access and Inmis backpacks"
        )
        index_path.write_text(json.dumps(index, indent=2) + "\n", encoding="utf-8")

        overrides = stage / "overrides"
        replace_tree(ROOT / "config", overrides / "config")
        replace_tree(ROOT / "datapacks", overrides / "datapacks")
        shutil.copy2(ROOT / "options.txt", overrides / "options.txt")
        shutil.copy2(ROOT / "icon.png", overrides / "icon.png")

        forbidden = ("justquests", "ftbquests", "ftb-library", "ftb-teams")
        for path in stage.rglob("*"):
            lowered = path.as_posix().lower()
            if any(name in lowered for name in forbidden):
                raise ValueError(f"Forbidden legacy quest content remains: {path}")

        with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
            for path in sorted(stage.rglob("*")):
                if path.is_file():
                    archive.write(path, path.relative_to(stage).as_posix())

    with zipfile.ZipFile(output) as archive:
        bad_member = archive.testzip()
        if bad_member:
            raise ValueError(f"Built pack has a corrupt member: {bad_member}")
        names = set(archive.namelist())
        if "modrinth.index.json" not in names:
            raise ValueError("Built pack is missing modrinth.index.json")
        quest_prefix = (
            "overrides/config/boundless/questpacks/cobblehorizons-adventure/"
            "data/cobblehorizons/quests/"
        )
        quests = [
            name
            for name in names
            if name.startswith(quest_prefix)
            and name.endswith(".json")
            and "/categories/" not in name
            and "/sub-category/" not in name
        ]
        if len(quests) != 66:
            raise ValueError(f"Expected 66 quests, found {len(quests)}")

    digest = hashlib.sha256(output.read_bytes()).hexdigest()
    (RELEASES / "SHA256SUMS.txt").write_text(
        f"{digest}  {output.name}\n", encoding="utf-8"
    )
    print(f"Built {output.name} ({output.stat().st_size} bytes)")
    print(f"SHA-256 {digest}")
    return output


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", type=Path, required=True, help="Known-good source MRPack")
    parser.add_argument("--version", required=True, help="Version ID, e.g. 1.1.0-rc5")
    args = parser.parse_args()
    build(args.base.resolve(), args.version)


if __name__ == "__main__":
    main()

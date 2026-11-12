#!/usr/bin/env python3
"""Restore missing first-party source files from the verified v1.2.0 MRPack.

Only creates absent text files from the two known first-party datapacks. Existing
files are NEVER overwritten. Release hash and ZIP CRC are mandatory checks.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
import zipfile
from pathlib import Path, PurePosixPath

V12_SHA256 = "fccfeb290946191c30f6c5e2783fc90e3564e04b36d3794d8c666d73ce57a40a"
KNOWN_PACKS = ("CobbleHorizons-QuestZ", "CobbleHorizons-Progression")
ALLOWED_SUFFIXES = {".json", ".mcfunction", ".mcmeta"}


def restore(archive_file: Path, repository: Path, apply: bool) -> dict:
    checksum = hashlib.sha256(archive_file.read_bytes()).hexdigest()
    if checksum != V12_SHA256:
        raise ValueError(f"Unexpected 1.2.0 release checksum: {checksum}")
    report = {
        "release_sha256": checksum,
        "apply": apply,
        "new_files": [],
        "identical_files": [],
        "different_existing_files": [],
        "skipped_files": [],
        "pack_entry_counts": {name: 0 for name in KNOWN_PACKS},
    }
    with zipfile.ZipFile(archive_file) as archive:
        corrupt = archive.testzip()
        if corrupt:
            raise ValueError(f"Corrupt release ZIP entry: {corrupt}")
        for entry in archive.infolist():
            if entry.is_dir():
                continue
            for pack in KNOWN_PACKS:
                prefix = f"overrides/datapacks/{pack}/"
                if not entry.filename.startswith(prefix):
                    continue
                relative = entry.filename[len(prefix):]
                posix = PurePosixPath(relative)
                if (not relative or posix.is_absolute() or ".." in posix.parts
                        or "\\" in relative or posix.suffix not in ALLOWED_SUFFIXES):
                    report["skipped_files"].append(entry.filename)
                    break
                content = archive.read(entry)
                try:
                    content.decode("utf-8-sig")
                except UnicodeDecodeError:
                    raise ValueError(f"Non-text first-party source: {entry.filename}")
                destination = repository / "datapacks" / pack / Path(*posix.parts)
                destination_rel = destination.relative_to(repository).as_posix()
                report["pack_entry_counts"][pack] += 1
                if destination.is_file():
                    key = ("identical_files" if destination.read_bytes() == content
                           else "different_existing_files")
                    report[key].append(destination_rel)
                else:
                    report["new_files"].append(destination_rel)
                    if apply:
                        destination.parent.mkdir(parents=True, exist_ok=True)
                        destination.write_bytes(content)
                break
    return report


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("mrpack", type=Path)
    ap.add_argument("--repo", type=Path, default=Path("."))
    ap.add_argument("--apply", action="store_true",
                    help="Restore only absent verified first-party text files")
    ap.add_argument("--output", type=Path, default=Path("baseline-restore-report.json"))
    args = ap.parse_args()
    report = restore(args.mrpack, args.repo.resolve(), args.apply)
    args.output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    summary = {k: len(v) if isinstance(v, list) else v
               for k, v in report.items() if k not in ("new_files", "identical_files",
                                                        "different_existing_files", "skipped_files")}
    summary.update({key: len(report[key]) for key in
                    ("new_files", "identical_files", "different_existing_files", "skipped_files")})
    print(json.dumps(summary, indent=2))
    print("Files restored or pending:", *report["new_files"], sep="\n  ")
    print("Existing files differing from archive:", *report["different_existing_files"], sep="\n  ")
    return 0


if __name__ == "__main__":
    sys.exit(main())

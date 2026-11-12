"""Regression tests for CobbleHorizons' release validator (stdlib only)."""
import json
import tempfile
import unittest
import zipfile
from pathlib import Path

from scripts.validate_pack import validate_mrpack, validate_source


ROOT_ID = "cobblehorizons:questz/root"
BASE = "datapacks/CobbleHorizons-QuestZ/data/cobblehorizons/advancement/questz"


class ValidatorTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.write("datapacks/CobbleHorizons-QuestZ/pack.mcmeta", {"pack": {"pack_format": 48, "description": "test"}})
        self.write("datapacks/CobbleHorizons-Progression/pack.mcmeta", {"pack": {"pack_format": 48, "description": "test"}})
        self.write("datapacks/CobbleHorizons-Progression/data/cobblehorizons/function/progression/test.mcfunction",
                   "say ok\n")
        self.write(f"{BASE}/root.json", {
            "criteria": {"start": {"trigger": "minecraft:tick"}},
            "requirements": [["start"]],
        })

    def write(self, path, data):
        file = self.root / path
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_text(json.dumps(data) if isinstance(data, dict) else data, encoding="utf-8")
        return file

    def child(self, name="child", parent=ROOT_ID, gated=True, reward=None):
        criterion = {"trigger": "minecraft:tick"}
        if gated:
            criterion["conditions"] = {
                "player": {"type_specific": {
                    "type": "minecraft:player", "advancements": {parent: True}
                }}
            }
        quest = {"parent": parent, "criteria": {"complete": criterion},
                 "requirements": [["complete"]]}
        if reward:
            quest["rewards"] = {"function": reward}
        self.write(f"{BASE}/{name}.json", quest)

    def errors(self):
        findings, _ = validate_source(self.root)
        return [issue["code"] for issue in findings if issue["level"] == "error"]

    def test_valid_quest_with_prerequisite(self):
        self.child()
        self.assertEqual([], self.errors())

    def test_missing_parent_is_detected(self):
        self.child(parent="cobblehorizons:questz/nonexistent")
        self.assertIn("PARENT_MISSING", self.errors())

    def test_missing_parent_gate_is_detected(self):
        self.child(gated=False)
        self.assertIn("PREREQUISITE_MISSING", self.errors())

    def test_missing_reward_function_is_detected(self):
        self.child(reward="cobblehorizons:quest_rewards/no_such_function")
        self.assertIn("REWARD_FUNCTION_MISSING", self.errors())

    def test_parent_cycle_is_detected(self):
        self.child("alpha", "cobblehorizons:questz/beta")
        self.child("beta", "cobblehorizons:questz/alpha")
        self.assertIn("PARENT_CYCLE", self.errors())

    def test_invalid_json_is_detected(self):
        self.write(f"{BASE}/broken.json", "{ broken JSON")
        self.assertIn("INVALID_JSON", self.errors())

    def test_missing_progression_data_is_detected(self):
        (self.root / "datapacks/CobbleHorizons-Progression/data/cobblehorizons/function/progression/test.mcfunction").unlink()
        self.assertIn("PROGRESSION_DATA_MISSING", self.errors())

    def test_valid_modrinth_archive(self):
        archive_path = self.root / "working.mrpack"
        manifest = {"formatVersion": 1, "game": "minecraft",
                    "dependencies": {"minecraft": "1.21.1", "fabric-loader": "0.19.3"},
                    "files": [{"path": "mods/example.jar", "hashes": {"sha512": "abc"},
                               "downloads": ["https://example.invalid/test.jar"]}]}
        with zipfile.ZipFile(archive_path, "w") as archive:
            archive.writestr("modrinth.index.json", json.dumps(manifest))
        issues, stats = validate_mrpack(archive_path)
        self.assertEqual([], issues)
        self.assertEqual(1, stats["manifest_files"])

    def test_new_questz_cannot_read_legacy_advancements_without_chapters(self):
        file = self.root / "legacy.mrpack"
        manifest = {
            "formatVersion": 1, "game": "minecraft",
            "dependencies": {"minecraft": "1.21.1", "fabric-loader": "0.19.5"},
            "files": [{
                "path": "mods/questz-1.1.1.jar",
                "hashes": {"sha512": "f" * 128},
                "downloads": ["https://cdn.modrinth.com/data/q1Xo6imm/versions/example/questz-1.1.1.jar"],
            }]
        }
        with zipfile.ZipFile(file, "w") as archive:
            archive.writestr("modrinth.index.json", json.dumps(manifest))
            archive.writestr(
                "overrides/datapacks/CobbleHorizons-QuestZ/data/cobblehorizons/advancement/questz/root.json",
                "{}"
            )
        issues, _ = validate_mrpack(file)
        self.assertIn("QUESTZ_FORMAT_INCOMPATIBLE", [issue["code"] for issue in issues])
        manifest["files"][0]["path"] = "mods/questz-1.0.1+1.21.1.jar"
        with zipfile.ZipFile(file, "w") as archive:
            archive.writestr("modrinth.index.json", json.dumps(manifest))
            archive.writestr(
                "overrides/datapacks/CobbleHorizons-QuestZ/data/cobblehorizons/advancement/questz/root.json",
                "{}"
            )
        issues, _ = validate_mrpack(file)
        self.assertNotIn("QUESTZ_FORMAT_INCOMPATIBLE", [issue["code"] for issue in issues])

    def test_duplicate_zip_entries_are_detected(self):
        import warnings
        archive_path = self.root / "duplicate.mrpack"
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", UserWarning)
            with zipfile.ZipFile(archive_path, "w") as archive:
                archive.writestr("modrinth.index.json", "{}")
                archive.writestr("modrinth.index.json", "{}")
        issues, _ = validate_mrpack(archive_path)
        self.assertIn("DUPLICATE_ZIP_ENTRY", [item["code"] for item in issues])


if __name__ == "__main__":
    unittest.main()

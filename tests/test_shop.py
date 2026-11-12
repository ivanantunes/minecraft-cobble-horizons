"""Guard against malformed CobbleDollars shop entries and accidental price regressions."""
import json
import unittest
from pathlib import Path

SHOP = Path(__file__).resolve().parents[1] / "config/cobbledollars/default_shop.json"


class ShopTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.groups = json.loads(SHOP.read_text(encoding="utf-8"))

    def test_groups_and_prices_valid(self):
        self.assertTrue(self.groups)
        items = []
        for group in self.groups:
            self.assertIsInstance(group["name"], str)
            self.assertTrue(group["offers"])
            for offer in group["offers"]:
                item = offer["item"]
                price = offer["price"]
                self.assertRegex(item, r"^[a-z0-9_.-]+:[a-z0-9_./-]+$")
                self.assertIsInstance(price, str)
                self.assertTrue(price.isdecimal(), (item, price))
                self.assertGreater(int(price), 0)
                items.append(item)
        self.assertEqual(len(items), len(set(items)), "Every shop item should have one price")

    def test_known_legacy_prices_preserved(self):
        indexed = {o["item"]: int(o["price"]) for g in self.groups for o in g["offers"]}
        self.assertEqual(2000, indexed["cobblemon:poke_ball"])
        self.assertEqual(8000, indexed["cobblemon:ultra_ball"])
        self.assertEqual(500, indexed["cobblemon:exp_candy_xs"])
        self.assertEqual(100000, indexed["cobblemon:rare_candy"])

    def test_medicine_and_stones_are_present(self):
        groups = {g["name"]: g for g in self.groups}
        self.assertEqual(6, len(groups["Medicine"]["offers"]))
        self.assertEqual(9, len(groups["Evolution Stones"]["offers"]))


if __name__ == "__main__":
    unittest.main()

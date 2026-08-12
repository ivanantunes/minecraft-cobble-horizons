#!/usr/bin/env python3
"""Normalize the CobbleHorizons Boundless campaign.

This script keeps the quest JSON reproducible: all player-facing text is English,
every objective is Cobblemon/Pokemon-focused, and locked quests remain visible.
Run it from the repository root whenever the campaign source is edited.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QUEST_ROOT = (
    ROOT
    / "config/boundless/questpacks/cobblehorizons-adventure/data/cobblehorizons/quests"
)


QUEST_TEXT = {
    "starter_01": ("01. Apricorn Fieldwork", "Gather eight Red Apricorns, the basic material for a trainer's first supply of Poke Balls."),
    "starter_02": ("02. First Poke Ball Kit", "Carry five Poke Balls so you are ready when the right wild Pokemon appears."),
    "starter_03": ("03. Field Medicine", "Prepare three Potions before traveling far from your first healing station."),
    "starter_04": ("04. Status Treatment", "Keep two Antidotes ready so poison cannot end an early expedition."),
    "starter_05": ("05. Premier Capture", "Obtain two Premier Balls and begin a collection of specialized capture tools."),
    "starter_06": ("06. Partner Care", "Stock two Super Potions for longer routes and tougher trainer battles."),
    "starter_07": ("07. Quick Encounter", "Prepare two Quick Balls for wild Pokemon that are best caught on the first turn."),
    "starter_08": ("08. Cave Capture Kit", "Carry two Dusk Balls before searching caves and other dark habitats."),
    "starter_09": ("09. Training Reserve", "Collect four Small Exp. Candies to help a new team member catch up."),
    "starter_10": ("10. Friendship Training", "Find a Soothe Bell and prepare a Pokemon whose growth depends on friendship."),
    "starter_11": ("11. Begin the Pokedex", "Obtain a red Pokedex and start documenting the species you meet across the horizon."),
    "starter_12": ("12. Pokemon Center Setup", "Build a Healing Machine so your team has a reliable recovery point at home."),
    "capture_01": ("01. Great Ball Supply", "Prepare six Great Balls for species that regularly escape standard Poke Balls."),
    "capture_02": ("02. Aquatic Specialist", "Carry four Dive Balls while researching Pokemon found in rivers, lakes, and oceans."),
    "capture_03": ("03. Bug and Water Specialist", "Prepare four Net Balls for Bug- and Water-type capture expeditions."),
    "capture_04": ("04. Repeat Research", "Obtain four Repeat Balls for species already registered in your collection."),
    "capture_05": ("05. Friendly Arrival", "Prepare three Friend Balls for Pokemon you want to bond with quickly."),
    "capture_06": ("06. Safari Expedition", "Carry three Safari Balls before exploring broad wild habitats."),
    "capture_07": ("07. Moonlit Capture", "Prepare two Moon Balls for Pokemon connected to Moon Stone evolution."),
    "capture_08": ("08. Heavyweight Target", "Carry two Heavy Balls when hunting large and exceptionally heavy Pokemon."),
    "capture_09": ("09. Level Advantage", "Prepare two Level Balls for encounters where your active partner greatly outlevels the target."),
    "capture_10": ("10. Fishing Specialist", "Obtain two Lure Balls before searching for Pokemon with a Poke Rod."),
    "capture_11": ("11. Rare Species Hunt", "Stock four Ultra Balls for rare, powerful, and low-catch-rate Pokemon."),
    "capture_12": ("12. Luxury Partner", "Prepare two Luxury Balls for future partners whose friendship matters."),
    "training_01": ("01. Small Candy Stockpile", "Collect twelve Small Exp. Candies to support newly caught Pokemon."),
    "training_02": ("02. Medium Candy Stockpile", "Collect eight Medium Exp. Candies for the core members of your team."),
    "training_03": ("03. Large Candy Stockpile", "Collect four Large Exp. Candies for advanced training."),
    "training_04": ("04. Rare Candy Reserve", "Secure two Rare Candies for important level thresholds and evolutions."),
    "training_05": ("05. Battle-Ready Medicine", "Carry three Hyper Potions before challenging stronger trainers."),
    "training_06": ("06. Return to Battle", "Prepare two Revives so a fainted partner can return during a long challenge."),
    "training_07": ("07. Complete Recovery", "Obtain a Full Restore for endgame battles that combine damage and status effects."),
    "training_08": ("08. Lucky Egg Training", "Find a Lucky Egg and use it to accelerate the growth of a chosen partner."),
    "training_09": ("09. Move Endurance", "Collect two PP Ups to improve a move used throughout long battles."),
    "training_10": ("10. Maximum Move Endurance", "Obtain a PP Max for a signature move in your competitive team."),
    "training_11": ("11. Defensive Recovery", "Find Leftovers and prepare a Pokemon built to remain in battle."),
    "training_12": ("12. Physical Commitment", "Obtain a Choice Band for a physical attacker with a carefully selected moveset."),
    "evolution_01": ("01. Fire Stone Evolution", "Obtain a Fire Stone for a compatible Fire-linked evolution."),
    "evolution_02": ("02. Water Stone Evolution", "Obtain a Water Stone for a compatible Water-linked evolution."),
    "evolution_03": ("03. Thunder Stone Evolution", "Obtain a Thunder Stone for a compatible Electric-linked evolution."),
    "evolution_04": ("04. Leaf Stone Evolution", "Obtain a Leaf Stone for a compatible Grass-linked evolution."),
    "evolution_05": ("05. Moon Stone Evolution", "Obtain a Moon Stone for a Pokemon influenced by moonlight."),
    "evolution_06": ("06. Sun Stone Evolution", "Obtain a Sun Stone for a Pokemon influenced by sunlight."),
    "evolution_07": ("07. Dawn Stone Evolution", "Obtain a Dawn Stone for one of its specialized evolution paths."),
    "evolution_08": ("08. Dusk Stone Evolution", "Obtain a Dusk Stone for one of its dark evolution paths."),
    "evolution_09": ("09. Shiny Stone Evolution", "Obtain a Shiny Stone for a Pokemon that evolves through radiant energy."),
    "evolution_10": ("10. Held-Item Evolution", "Find a Metal Coat and prepare a Pokemon that uses it to reach a stronger form."),
    "gyms_01": ("01. Gym Defense Plan", "Obtain an Assault Vest and prepare a durable Pokemon for special attacks."),
    "gyms_02": ("02. Special Attack Plan", "Obtain Choice Specs for a special attacker built around one decisive move."),
    "gyms_03": ("03. Speed Control", "Obtain a Choice Scarf for a Pokemon that must move before dangerous opponents."),
    "gyms_04": ("04. Unevolved Potential", "Find an Eviolite and build a strategy around a Pokemon that has not fully evolved."),
    "gyms_05": ("05. Ability Tuning", "Obtain an Ability Capsule and refine one member of your gym challenge team."),
    "gyms_06": ("06. First Gym Badge", "Defeat your first tracked gym leader and prove your team can win an official challenge."),
    "gyms_07": ("07. Rising Challenger", "Defeat three tracked gym leaders using a team that can answer different types."),
    "gyms_08": ("08. Gym Veteran", "Defeat eight tracked gym leaders and complete the full badge campaign."),
    "gyms_09": ("09. Ultra Beast Preparation", "Secure a Beast Ball for the rarest extradimensional capture opportunities."),
    "gyms_10": ("10. Championship Recovery", "Obtain a Max Revive before facing the strongest trainers in the pack."),
    "legend_01": ("01. Master Ball Protocol", "Secure a Master Ball for a legendary encounter where failure is not acceptable."),
    "legend_02": ("02. Dragon Scale Relic", "Find a Dragon Scale while researching rare item-based evolutions."),
    "legend_03": ("03. Reaper Cloth Relic", "Find a Reaper Cloth for a Pokemon linked to spectral evolution."),
    "legend_04": ("04. Protector Relic", "Obtain a Protector for a Pokemon whose final form requires exceptional armor."),
    "legend_05": ("05. Electirizer Relic", "Obtain an Electirizer for a high-voltage evolution path."),
    "legend_06": ("06. Magmarizer Relic", "Obtain a Magmarizer for a high-temperature evolution path."),
    "legend_07": ("07. Prism Scale Relic", "Find a Prism Scale for a rare and beautiful evolution."),
    "legend_08": ("08. King's Rock Relic", "Obtain a King's Rock for evolution research and flinch-based battle strategies."),
    "legend_09": ("09. Hidden Ability Mastery", "Secure an Ability Patch to unlock a Pokemon's hidden competitive potential."),
    "legend_10": ("10. Champion of the Horizon", "Hold two Master Balls as proof that your team is ready for the pack's legendary endgame."),
}


CATEGORY_NAMES = {
    "starter": "Trainer's First Journey",
    "capture": "Capture and Research",
    "training": "Training and Battle",
    "evolution": "Evolution and Forms",
    "gyms": "Gyms and Competition",
    "legend": "Legendary Horizon",
}


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def save(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def update_quests() -> None:
    files = sorted(path for path in QUEST_ROOT.glob("*.json") if path.is_file())
    seen: set[str] = set()
    for path in files:
        data = load(path)
        quest_id = data["id"]
        if quest_id not in QUEST_TEXT:
            raise ValueError(f"Missing English copy for {quest_id} ({path})")
        title, description = QUEST_TEXT[quest_id]
        data["name"] = title
        data["description"] = description
        data["hidden_under_dependency"] = "false"
        seen.add(quest_id)

        if quest_id == "starter_11":
            data["icon"] = "cobblemon:pokedex_red"
            data["completion"] = {"complete": [{"collect": "cobblemon:pokedex_red", "count": 1}]}
            data["reward"] = {"items": [{"item": "cobblemon:poke_ball", "count": 5}], "exp": "points", "count": 43}
        elif quest_id == "starter_12":
            data["icon"] = "cobblemon:healing_machine"
            data["completion"] = {"complete": [{"collect": "cobblemon:healing_machine", "count": 1}]}
            data["reward"] = {"items": [{"item": "cobblemon:great_ball", "count": 3}], "exp": "points", "count": 46}
        elif quest_id == "capture_01":
            data["dependencies"] = "starter_12"

        save(path, data)

    missing = sorted(set(QUEST_TEXT) - seen)
    if missing:
        raise ValueError(f"Quest files are missing for: {', '.join(missing)}")


def update_categories() -> None:
    for folder in ("categories", "sub-category"):
        for path in sorted((QUEST_ROOT / folder).glob("*.json")):
            data = load(path)
            data["name"] = CATEGORY_NAMES[data["id"]]
            save(path, data)


if __name__ == "__main__":
    update_quests()
    update_categories()
    print(f"Updated {len(QUEST_TEXT)} Pokemon-focused Boundless quests in English.")

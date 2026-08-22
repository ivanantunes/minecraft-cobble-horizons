# Balance and Design Rules — CobbleHorizons 1.2.0

This document records deliberate 1.2.0 balance decisions so future fixes do not accidentally undo them.

## Pokémon-first world

CobbleHorizons intentionally suppresses most world-generated vanilla mobs so Pokémon and trainers dominate exploration.

### Allowed vanilla entities

The current Mob Filter allow-list preserves:

- villagers;
- wandering traders;
- iron golems;
- snow golems;
- Ender Dragon;
- Wither;
- cows;
- pigs;
- chickens;
- sheep.

The last four were restored after survival playtesting showed that removing all farm animals made early food and basic materials depend too heavily on finding a village.

### Suppressed spawn sources

The general vanilla suppression rule covers world-generated spawn types including natural spawns, chunk generation, spawners, patrols, reinforcements, jockeys and trial spawners.

Do not broadly remove this policy without a deliberate design decision.

## Trainers

### Normal trainers

Normal RCT trainers remain part of world exploration.

The global RCT spawning configuration is intentionally active and provides route-style encounters.

### League bosses

Gym Leaders, Elite Four variants and Champion Terry are progression bosses. Their first-party overrides use:

`spawnWeightFactor: 0.0`

They should not be random natural encounters.

## Level caps

The League is designed around RCT's next-required-trainer cap system:

`15 → 27 → 34 → 44 → 59 → 68 → 76 → 81 → 85`

`allowOverLeveling = false` is intentional.

Changes to boss teams or required-defeat order must be checked against this cap curve.

## Village and structure loot

Cobblemon itself injects additional loot into vanilla structures. Village-house injection is separate from QuestZ rewards.

Do not nerf a loot table solely because an item was observed in the player's inventory after looting. First establish whether the item was:

1. visibly generated inside the chest; or
2. awarded by a quest when the chest item triggered an `inventory_changed` criterion.

## Quest reward cascades

Inventory quests can legitimately complete as soon as their target item enters the inventory.

The unwanted behavior is a **chain**, where quest A rewards an item that instantly completes quest B, whose reward completes quest C, etc.

Version 1.2.0 breaks the main multi-step cascade by converting 17 reward-sink quests to CobbleDollars.

Future quest edits should preserve this rule:

> Item acquisition may complete its own quest, but a reward should not unintentionally create a long automatic item-reward chain.

## Scope for 1.2.0

1.2.0 is intended as a long-playtest/stable progression release. New systems should generally wait for a later version unless they are necessary to fix a confirmed bug, exploit or severe balance problem.

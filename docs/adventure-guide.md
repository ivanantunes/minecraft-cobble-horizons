# CobbleHorizons Adventure Guide

CobbleHorizons 1.1.0 uses **QuestZ 1.0.1** for its in-game progression system.

Open the quest screen with **`L`** after entering a world.

## Campaign status

The current campaign contains:

- **93 active gameplay quests**;
- **1 root advancement** used to anchor the quest tree;
- **12 Species Hunt quests hidden and disabled** until species-specific capture filtering is reintroduced safely.

All active player-facing quests are in English.

## Opening progression

The beginning of the campaign is deliberately ordered:

1. **Choose Your Partner** — choose a starter Pokémon.
2. **Red Apricorn Research** — carry 8 Red Apricorns.
3. **A New Friend** — catch your first Pokémon.

The campaign then opens into multiple Pokémon-focused branches.

## Main quest branches

| Branch | Examples |
|---|---|
| Apricorn research | Red, Yellow, Green, Blue, Pink, Black and White Apricorns |
| Poké Balls | Poké Ball, Great Ball, Ultra Ball and specialized ball progression |
| Capture milestones | 5, 15, 30 and 60 captures, plus shiny capture |
| Type challenges | Fire, Water, Grass, Electric, Psychic, Ghost, Dragon, Dark, Steel and Fairy capture goals |
| Training | Level milestones, candies and Rare Candy progression |
| Battles | Battle wins and Pokémon defeat milestones |
| Evolution | First evolution, evolution counts, stones and held evolution items |
| Medicine | Potions, restores and revives |
| Held items | Leftovers, Choice items, Lucky Egg, Eviolite and other battle items |
| Fishing | First fishing milestones and Pokémon fishing |
| Utility | Pokédex and Healing Machine progression |
| Endgame preparation | Advanced items and the Horizon Elite objective |

## Prerequisite protection

QuestZ uses Minecraft advancements as the underlying quest data.

CobbleHorizons adds a real prerequisite predicate to every active non-root quest. A later quest cannot complete simply because the player accidentally performs its objective before reaching it.

This is separate from the visual `parent` relationship: the parent organizes the quest tree, while the prerequisite predicate enforces the progression.

## Species Hunt status

The following Species Hunt templates are currently hidden and use `minecraft:impossible`:

- Beldum
- Dratini
- Eevee
- Gastly
- Gible
- Larvitar
- Magikarp
- Pikachu
- Ralts
- Riolu
- Rotom
- Snorlax

They were disabled because a generic capture could incorrectly complete multiple species-specific quests in the previous implementation.

They should only be re-enabled after one species-specific quest is validated against the exact Cobblemon version used by the pack.

## World progress

Quest completion is stored as advancement progress inside the world.

For release validation, use a **fresh world**. Reusing an old test world can preserve completed advancements from an earlier release and make a corrected quest appear to complete immediately.

## Release testing checklist

1. Import the latest MRPack into a new Modrinth instance.
2. Create a new world.
3. Press `L` and confirm the CobbleHorizons quest tree opens.
4. Choose a starter and confirm only **Choose Your Partner** completes.
5. Carry 8 Red Apricorns and confirm **Red Apricorn Research** completes.
6. Catch one Pokémon and confirm only the intended first-capture progression completes.
7. Confirm future capture, type and item quests do not complete early.
8. Confirm the 12 Species Hunt quests are not visible.
9. Confirm quest rewards are delivered without missing-function errors.
10. Report the pack version, operating system, reproduction steps and `latest.log` for any failure.

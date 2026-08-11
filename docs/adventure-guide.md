# CobbleHorizons Adventure Guide

CobbleHorizons 1.1.0 introduces a curated in-game campaign that gives players direction without turning the open world into a fixed linear map.

Press **J** after entering a world, open the **CobbleHorizons Adventure** category, and accept the first available objective. Accept each new stage before completing its requirement so the quest tracker can record the event.

## Campaign

| Stage | Objective | Main lesson |
|---:|---|---|
| 1 | Field Essentials | Choose a starter and obtain a Poké Ball |
| 2 | Your First Catch | Study and capture a wild Pokémon |
| 3 | Begin Field Research | Obtain a Pokédex and begin documenting species |
| 4 | Test Your Strategy | Defeat an NPC trainer |
| 5 | Build a Balanced Team | Assemble a six-Pokémon party with varied roles |
| 6 | A Stronger Form | Evolve a Pokémon |
| 7 | Recovery Routine | Use a fully charged Healing Machine |
| 8 | Your First Gym Badge | Find and defeat any gym leader |
| 9 | Rising Challenger | Collect three gym badges |
| 10 | Gym Veteran | Collect eight gym badges |
| 11 | Mega Breakthrough | Mega Evolve a compatible Pokémon |
| 12 | A Legendary Call | Craft the Arc Phone |
| 13 | Legendary Encounter | Complete a legendary monument ritual |
| 14 | The Elite Gauntlet | Defeat all tracked Elite Four-class trainers |
| 15 | Champion of the Horizon | Defeat all tracked Champion-class trainers |

## Progression philosophy

- Gym order remains open because structures and leaders are discovered through world exploration.
- Rewards provide supplies and small training boosts, not complete teams or free progression.
- The campaign uses achievements already emitted by Cobblemon, Radical Cobblemon Trainers, Mega Showdown and Legendary Monuments.
- Badge objectives recognize every badge supplied by the included RCT Badges datapack.
- The final stage does not end the world. Research, collecting, breeding, building and legendary hunting remain available.

## Important behavior

Quest progression is saved per world. A fresh world is recommended when validating a new release candidate.

If a badge objective was accepted after the badge entered your inventory, drop the badge and pick it up again to refresh the collection event. Advancement-based objectives should be accepted before earning the corresponding advancement.

## RC testing checklist

1. Import the MRPack as a new Modrinth instance.
2. Create a new world and confirm that the Adventure Guide opens with `J`.
3. Confirm that only the **CobbleHorizons Adventure** campaign appears as the primary quest path.
4. Accept **Field Essentials**, obtain a Poké Ball, and verify completion and reward delivery.
5. Continue through **Your First Catch** and **Begin Field Research**.
6. Confirm that the RCT Badges datapack appears under the world's datapack list.
7. Report the pack version, operating system, reproduction steps and a `latest.log` link for any failure.

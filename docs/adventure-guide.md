# CobbleHorizons Adventure Guide — 1.2.0

CobbleHorizons 1.2.0 uses **QuestZ 1.0.1** for the quest UI and **Radical Cobblemon Trainers** for the League series / level-cap progression.

Open the QuestZ screen with **`L`** after entering a world.

## Campaign status

The 1.2.0 campaign contains:

- **107 active gameplay quests**;
- **1 root advancement** used to anchor the quest tree;
- **12 Species Hunt quests hidden and disabled**.

All active player-facing quest text remains in English.

## Main campaign opening

The opening is intentionally ordered:

1. **Choose Your Partner** — choose a starter Pokémon.
2. **Red Apricorn Research** — carry the required Red Apricorns.
3. **A New Friend** — catch the first Pokémon.
4. **Field Pokédex** — enter the field-research phase.
5. **First Challenger** — defeat the first trainer milestone.
6. Enter the **CobbleHorizons League**.

The rest of the quest tree includes capture, type, training, evolution, medicine, held-item, fishing, utility and exploration branches alongside the League campaign.

## CobbleHorizons League

The required order is:

| Stage | Opponent |
|---:|---|
| Gym I | Brock |
| Gym II | Misty |
| Gym III | Lt. Surge |
| Gym IV | Erika |
| Gym V | Sabrina |
| Gym VI | Koga |
| Gym VII | Blaine |
| Gym VIII | Clair |
| Elite Four I | Lorelei |
| Elite Four II | Bruno |
| Elite Four III | Agatha |
| Elite Four IV | Lance |
| Champion | Terry |

After the Champion, the quest campaign points toward **Horizon Elite** as the postgame objective.

## Level-cap rules

RCT is configured with:

- initial level cap: **15**;
- relative level cap: **0**;
- overleveling: **disabled**;
- initial series: `cobblehorizons`.

The designed cap sequence is:

`15 → 27 → 34 → 44 → 59 → 68 → 76 → 81 → 85`

Because the cap is based on the next required trainer, progress through the League is intended to raise the cap naturally instead of requiring manual commands.

## League boss spawning

The Gym Leaders, Elite Four variants and Champion used by the CobbleHorizons series have `spawnWeightFactor = 0` in the first-party progression datapack.

This means they should **not naturally spawn as random world trainers**. Their intended role is progression through the gym / League structures.

Ordinary RCT trainers can still spawn naturally and serve as route/world encounters.

## Prerequisite protection

QuestZ stores its quests as Minecraft advancements.

CobbleHorizons uses actual prerequisite checks, not only visual parent links. A later campaign node should not complete before its required parent/progression state has been reached.

## Reward-chain protection

Some legacy inventory quests use `minecraft:inventory_changed`. An item entering the inventory can therefore satisfy an objective immediately.

In 1.2.0 the main 17 reward-sink quests were changed so their reward does not hand out another chain-triggering item. They now terminate in CobbleDollars, preventing the old multi-step reward cascade while keeping the side objectives usable.

## Species Hunt status

These Species Hunt templates remain hidden and disabled:

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

They use an impossible criterion until species-specific capture filtering is proven reliable for Cobblemon 1.7.3 in this stack.

## World progress and upgrades

Quest progress lives in world advancement data. RCT series/progression also lives with player/world state.

For release validation, use a **fresh world**.

A migration helper is bundled for worlds that need the 1.2 League series selected for online players:

`/function cobblehorizons:progression/migrate_1_2_all_online`

Back up a world before using migration commands.

## 1.2 release test checklist

1. Import the MRPack into a new Modrinth instance.
2. Create a new survival world.
3. Press `L` and confirm the quest tree opens.
4. Choose a starter.
5. Complete Red Apricorn Research.
6. Catch the first Pokémon and verify A New Friend.
7. Reach Field Pokédex and First Challenger.
8. Confirm Brock is the first League requirement.
9. Confirm later League quests do not complete early.
10. Confirm random naturally spawned trainers are normal trainers, not League bosses.
11. Confirm the Species Hunt templates are not visible.
12. Confirm quest rewards do not start an uncontrolled item-reward cascade.

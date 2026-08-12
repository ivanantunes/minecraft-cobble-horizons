# CobbleHorizons Adventure Guide

CobbleHorizons 1.1.0 RC5 introduces a curated in-game campaign that gives players direction without turning the open world into a fixed linear map.

Press **`[`** after entering a world, or use the supplied Quest Book item. The inventory-side button is intentionally disabled because Boundless 1.21.1-Fabric-10 crashes while injecting that widget on Minecraft 1.21.1. The standalone book remains fully available. Open **CobbleHorizons Adventure** and follow the connected path.

## Campaign

The campaign has **66 connected Pokémon objectives in English** grouped into six categories. Every quest is visible in the book; quests with unfinished prerequisites are shown as locked rather than hidden. The objectives cover Poké Balls, healing, Pokédex research, capture specializations, training, evolution items, gym milestones and legendary preparation.

| Category | Difficulty | Focus |
|---:|---|---|
| Primeiros Passos | Fácil | Abrigo, ferramentas, comida e sobrevivência inicial |
| Exploração | Fácil / médio | Navegação, cavernas, biomas, viagem e portal |
| Jornada de Treinador | Médio | Poké Bolas, preparação de batalha, pesquisa e arenas |
| Base e Recursos | Médio | Oficina, armazenamento, encantamentos, fazenda e redstone |
| Desafios | Difícil | Nether, combate, equipamentos e tesouros perigosos |
| Horizonte Lendário | Hardcore | Netherite, End, Dragon, Wither, beacon e legado final |

## Progression philosophy

- The progression begins accessible and becomes demanding only after the player has established a base and team.
- Rewards provide experience bottles and small progression help, not complete teams or free endgame gear.
- Objectives intentionally use stable item IDs, making them reliable in singleplayer and in a Modrinth-imported instance.
- The final stage does not end the world. Research, collecting, breeding, building, gyms and legendary hunting remain available.

## Important behavior

Quest progression is saved per world. A fresh world is recommended when validating a new release candidate. The campaign is shipped at `config/boundless/questpacks/cobblehorizons-adventure`; it is enabled by default and does not depend on FTB mods or CurseForge downloads. The inventory widget is disabled, but the standalone Quest Book is not.

## RC testing checklist

1. Import the MRPack as a new Modrinth instance.
2. Create a new world and confirm that the Quest Book opens with `[`.
3. Confirm that **CobbleHorizons Adventure** contains six English category tabs and 66 visible quests.
4. Complete **Apricorn Fieldwork** with red apricorns and verify the reward delivery.
5. Continue to **First Poke Ball Kit** and confirm the dependency unlocks correctly.
6. Confirm that no FTB Quests, FTB Library, FTB Teams or JustQuests mod is present.
7. Open the player inventory and confirm it does not crash.
8. Report the pack version, operating system, reproduction steps and a `latest.log` link for any failure.

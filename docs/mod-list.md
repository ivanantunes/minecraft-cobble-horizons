# CobbleHorizons Mod List

This document tracks the mods evaluated and approved for CobbleHorizons.

## Status

- 🔎 Researching
- 🧪 Testing
- ✅ Approved
- ❌ Rejected
- ⚠️ Known Issue

---

# Core

| Mod | Version | Status | Purpose |
|---|---|---|---|
| Cobblemon | 1.7.3 | ✅ | Core Pokémon gameplay |
| Fabric API | 0.116.15+1.21.1 | ✅ | Fabric dependency |
| Fabric Language Kotlin | 1.13.13+kotlin.2.4.10 | ✅ | Mod dependency |

---

# Performance

| Mod | Version | Status | Purpose |
|---|---|---|---|
| Sodium | 0.8.13-beta.2 | ✅ | Rendering optimization |
| Lithium | 0.15.4 | ✅ | Game logic optimization |
| ImmediatelyFast | 1.6.11+1.21.1 | ✅ | Rendering optimization |
| FerriteCore | 7.0.3 | ✅ | Memory optimization |
| ModernFix | 5.25.1+mc1.21.1 | ✅ | Memory, loading and stability |

---

# General Quality of Life

| Mod | Version | Status | Purpose |
|---|---|---|---|
| Xaero's Minimap | 26.4.2 | ✅ | Navigation |
| Xaero's World Map | 1.44.2 | ✅ | World exploration |
| EMI | 1.1.24 | ✅ | Recipes and items |
| Jade | 15.10.6 | ✅ | Contextual information |
| Mouse Tweaks | 2.26 | ✅ | Inventory controls |

---

# Pokémon Quality of Life

| Mod | Version | Status | Purpose |
|---|---|---|---|
| Cobblemon Pokedex (Cobbledex) | 1.2.0 | ✅ | Pokémon information |
| Cobblemon Integrations | 1.1.6 | ✅ | Integration with Jade and other systems |

---

# World Generation

| Mod | Version | Status | Purpose |
|---|---|---|---|
| Terralith | 2.6.2 | ✅ | World generation and biome variety |
| Cobblemon: Extra Structures | 1.21.1-1.3.0 | ⚠️ | Pokémon structures |
| Cobblemon: Nests & Dens | 1.3.3 | ✅ | Pokémon nests and dens |
| Lithostitched | 1.7.13-fabric-21.1 | ✅ | World generation dependency |

---

# Pokémon World

| Mod | Version | Status | Purpose |
|---|---|---|---|
| CobbleStructures | 1.1.0+mod | ✅ | PokéCenters, PokéMarts and Pokémon structures |
| CobbleDollars | 2.0.0+Beta-6.1 | ✅ | Pokémon economy |
| Another Furniture | 4.0.2 | ✅ | Furniture and structure content |
| Cobblemon PokéNav | 2.3.3 | ✅ | Pokémon spawn information |
| Cobblemon Repel | 1.7-1.4 | ✅ | Pokémon spawn control |
| Waystones | 21.1.40+fabric-1.21.1 | ✅ | Fast travel |
| Balm | 21.0.64+fabric-1.21.1 | ✅ | Waystones dependency |
| Forge Config API Port | v21.1.6-1.21.1-Fabric | ✅ | Configuration dependency |

---

# Trainers

| Mod | Version | Status | Purpose |
|---|---|---|---|
| Radical Cobblemon Trainers | 0.18.1-beta | ✅ | Main trainer system |
| Radical Cobblemon Trainers API | 0.15.2-beta | ✅ | Trainer battle engine and API |
| Cobblemon Trainer Structures | 1.7.1 | ⚠️ | Trainer structures and battle locations |
| Architectury API | 13.0.11+fabric | ✅ | Required dependency |
| Fix Cobblemon Pokemon Experience | 1.1.1+1.21.1-fabric | ✅ | Improved experience gain during trainer battles |

---

# Progression

| Mod | Version | Status | Purpose |
|---|---|---|---|
| Rad Gyms | 1.7.3_0.4.4 | ✅ | Gym system and gym challenges |
| Radical Gyms & Structures | 0.6 | ✅ | Gym structures, Gym Leaders and Pokémon League |
| Capture Cap - RCT Version | 1.2.0 | ✅ | Capture restrictions integrated with RCT progression |
| CobbleFurnies | 1.2 | ✅ | Structure/content dependency |
| Athena | 4.0.6 | ✅ | Required dependency |
| Cobblemon Pokemon Badges | 0.1.1 | ✅ | Physical Pokémon badge system |
| RCT Badges - Cobblemon Pokemon Badges | 1.1.2 | ✅ | RCT Gym Leader badge integration |

---

# Pokémon Mechanics

| Mod | Version | Status | Purpose |
|---|---|---|---|
| SimpleTMs: TMs and TRs for Cobblemon | 2.3.3 | ✅ | TM and TR system |
| Cobbreeding | 2.2.2 | ✅ | Pokémon breeding |
| Cobblemon Utility+ | 1.7.4 | ✅ | IV, EV and Pokémon training utilities |
| Cobblemon: Mega Showdown | 1.9.3+1.7.3+1.21.1 | ✅ | Mega Evolution and advanced battle gimmicks |
| Myths and Legends | 1.9.0 | ✅ | Legendary and Mythical encounter mechanics |
| Cobblemon: Legendary Monuments | 8.1-Love-for-All | ✅ | Legendary structures and encounters |

---

# V0.5 Dependencies

| Mod | Version | Status | Purpose |
|---|---|---|---|
| Cloth Config API | 15.0.140+fabric | ✅ | Configuration dependency |
| owo-lib | 0.13.0-alpha.15+1.21 | ✅ | Mega Showdown dependency |
| Accessories | 1.1.0-beta.53+1.21.1 | ✅ | Mega Showdown accessory system |
| Resourceful Lib | 3.0.12 | ✅ | Required library |
| Chipped | 4.0.2 | ✅ | Required content/dependency |

---

# Rejected Mods

## Cobblemon Auto Tidy Up PC

Version:

`1.2-SNAPSHOT`

Status:

❌ Rejected

Reason:

- Caused resource reload failure.
- Game failed to load correctly.
- Removing the mod resolved the issue.

---

## Cobblemon UI Tweaks

Version:

`1.0.7`

Status:

❌ Rejected

Reason:

- Client crashed when opening the Pokémon Stats/EV screen.
- Incompatible with the current Cobblemon Stats UI.
- Removing the mod resolved the crash.

---

# Known Issues

## Cobblemon Trainer Structures

Status:

⚠️ Non-critical resource/model issue

Observed:

The mod attempts to load:

`cobblemonopponents:models/block/pokeball_trophy_java.json`

The model contains an invalid resource location referencing a development/local path.

Current impact:

- No observed game crash
- World continues loading
- Trainer gameplay continues functioning

Planned action:

Review during V0.7 cleanup.

---

## Cobblemon: Extra Structures

Status:

⚠️ Non-critical advancement/resource issue

Observed:

The Sprout Tower advancement references:

`cobblemonextrastructures:bellsprout_statue`

The referenced registry item was not available during advancement loading.

Current impact:

- No observed game crash
- World continues loading
- Structure generation remains usable

Planned action:

Review during V0.7 cleanup.

---

# Intentionally Excluded

## Alternative Gym Systems

Alternative gym/progression systems are intentionally avoided while Rad Gyms, RCT and Radical Gyms & Structures provide the primary progression architecture.

## Duplicate Battle Gimmick Systems

Mega Showdown is the primary platform for advanced Pokémon battle gimmicks.

Separate addons implementing overlapping Mega Evolution, Z-Move, Terastallization or Dynamax systems should generally be avoided.

## Excess Legendary Systems

Myths and Legends and Legendary Monuments currently provide the primary expansion for Legendary and Mythical Pokémon.

Additional large legendary systems should only be introduced if they provide substantial unique value without excessive duplication.

---

# Evaluation Rules

Before approving a mod:

1. Minecraft 1.21.1 compatibility
2. Fabric compatibility
3. Cobblemon 1.7.3 compatibility
4. Required dependencies
5. Maintenance status
6. Known incompatibilities
7. Performance impact
8. Singleplayer stability
9. License
10. Contribution to the Pokémon experience
11. Compatibility with existing progression
12. Avoid unnecessary mechanic duplication
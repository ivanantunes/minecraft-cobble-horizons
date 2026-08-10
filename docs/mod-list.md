# CobbleHorizons Mod List

This document tracks every mod evaluated for CobbleHorizons.

A mod being listed here does not necessarily mean it has been approved.

## Status

- 🔎 Researching
- 🧪 Testing
- ✅ Approved
- ❌ Rejected
- ⚠️ Issue
- 🔄 Replacement being evaluated

---

# V0.1 — Foundation

## Core

| Mod | Version | Category | Status | Reason |
|---|---|---|---|---|
| Cobblemon | 1.7.3 | Core | ✅ Approved | Core Pokémon gameplay |
| Fabric API | 0.116.15+1.21.1 | Dependency | ✅ Approved | Required Fabric dependency |

---

## Performance

| Mod | Version | Category | Status | Reason |
|---|---|---|---|---|
| Sodium | 0.8.13-beta.2 | Performance | ✅ Approved | Rendering and FPS optimization |
| Lithium | 0.15.4 | Performance | ✅ Approved | Game logic and tick optimization |
| ImmediatelyFast | 1.6.11+1.21.1 | Performance | ✅ Approved | Immediate-mode rendering optimization |
| FerriteCore | 7.0.3 | Performance | ✅ Approved | Memory usage reduction |
| ModernFix | 5.25.1+mc1.21.1 | Performance | ✅ Approved | Memory, loading and stability optimizations |

---

## General Quality of Life

| Mod | Version | Category | Status | Reason |
|---|---|---|---|---|
| Xaero's Minimap | 26.4.2 | Map | ✅ Approved | Navigation and waypoints |
| Xaero's World Map | 1.44.2 | Map | ✅ Approved | Exploration tracking and world navigation |
| EMI | 1.1.24 | Recipes | ✅ Approved | Item and recipe visualization |
| Jade | 15.10.6 | Information | ✅ Approved | Contextual block and entity information |
| Mouse Tweaks | 2.26 | Inventory | ✅ Approved | Improved inventory controls |

---

## Pokémon Quality of Life

| Mod | Version | Category | Status | Reason |
|---|---|---|---|---|
| Cobblemon Pokedex (Cobbledex) | 1.2.0 | Pokédex | ✅ Approved | Improved Pokémon species information |
| Cobblemon UI Tweaks | 1.0.7 | Interface | ✅ Approved | Improves Cobblemon PC and battle UI |
| Fabric Language Kotlin | 1.13.13+kotlin.2.4.10 | Dependency | ✅ Approved | Required dependency for installed mods |
| Cobblemon Auto Tidy Up PC | 1.2-SNAPSHOT | PC QoL | ❌ Rejected | Caused resource reload failure during V0.1 testing |

---

# Rejected Mods

## Cobblemon Auto Tidy Up PC

Version tested:

`1.2-SNAPSHOT`

Environment:

- Minecraft 1.21.1
- Fabric Loader 0.19.3
- Cobblemon 1.7.3

Issue:

The game displayed a resource reload failure and did not load correctly while the mod was enabled.

Result:

Removing or disabling the mod resolved the issue.

Decision:

❌ Rejected for V0.1.

The mod can be reevaluated if a stable compatible version becomes available.

---

# Future Candidates

These mods or systems are candidates for future milestones and are not currently part of V0.1.

## Pokémon Mechanics

- Mega Showdown
- Cobbreeding
- Pokémon gimmick systems
- IV/EV utility systems

## Trainers

- Radical Cobblemon Trainers
- Trainer APIs
- Gym systems

## World

- Pokémon structures
- Pokémon Centers
- Poké Marts
- World-generation improvements

---

# Evaluation Rules

Before approving a mod, verify:

1. Minecraft compatibility
2. Fabric compatibility
3. Cobblemon compatibility
4. Required dependencies
5. Recent maintenance
6. Known incompatibilities
7. Performance impact
8. Multiplayer compatibility
9. License
10. Whether it actually improves the Pokémon experience
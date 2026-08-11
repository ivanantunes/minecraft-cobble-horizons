# Changelog

All notable changes to CobbleHorizons are documented in this file.

---

## V0.5.0 — Pokémon Mechanics

Status: ✅ Completed

### Added

#### TMs and TRs

- SimpleTMs 2.3.3
- TM system
- TR system
- Expanded Pokémon moveset progression

#### Breeding

- Cobbreeding 2.2.2
- Pokémon breeding
- Egg generation
- Pasture-based breeding mechanics

#### Pokémon Training

- Cobblemon Utility+ 1.7.4
- IV utilities
- EV utilities
- Pokémon training tools
- Additional Pokémon management functionality

#### Advanced Battle Mechanics

- Cobblemon: Mega Showdown 1.9.3+1.7.3+1.21.1
- Mega Evolution
- Z-Moves
- Terastallization
- Dynamax
- Additional battle gimmicks and forms

#### Legendary and Mythical Pokémon

- Myths and Legends 1.9.0
- Cobblemon: Legendary Monuments 8.1-Love-for-All
- Legendary structures
- Legendary encounters
- Mythical encounters
- Special encounter mechanics
- Rare Pokémon exploration

#### Dependencies

- Cloth Config API 15.0.140+fabric
- owo-lib 0.13.0-alpha.15+1.21
- Accessories 1.1.0-beta.53+1.21.1
- Resourceful Lib 3.0.12
- Chipped 4.0.2

### Development

Changed the development validation workflow.

Previous workflow:

- Install small group
- Test
- Install next group
- Test again

New workflow:

- Research milestone
- Install compatible systems in batches
- Start game
- Collect logs
- Resolve critical issues
- Document non-critical warnings

This allows faster development while maintaining visibility into compatibility problems.

### Known Issues

#### Cobblemon Trainer Structures

A trophy model references an invalid development/local resource path.

No game crash has been observed.

#### Cobblemon: Extra Structures

The Sprout Tower advancement references an unavailable Bellsprout statue registry entry.

No game crash has been observed.

Both issues are scheduled for later cleanup unless they become gameplay-breaking.

### Result

✅ V0.5 Pokémon Mechanics completed.

---

## V0.4.0 — Progression

Status: ✅ Completed

### Added

#### Gyms

- Rad Gyms 1.7.3_0.4.4
- Radical Gyms & Structures 0.6

#### Progression

- Capture Cap - RCT Version 1.2.0
- Gym progression
- Gym Leader challenges
- Level-based progression
- Capture restrictions integrated with RCT

#### Badges

- Cobblemon Pokemon Badges 0.1.1
- RCT Badges - Cobblemon Pokemon Badges 1.1.2
- Physical Pokémon badges
- RCT Gym Leader badge integration

#### Pokémon League

- Kanto League content
- Elite Four progression
- Champion progression

#### Dependencies

- CobbleFurnies 1.2
- Athena 4.0.6

### Result

✅ V0.4 Progression completed.

---

## V0.3.0 — Trainers

Status: ✅ Completed

### Added

- Radical Cobblemon Trainers 0.18.1-beta
- Radical Cobblemon Trainers API 0.15.2-beta
- Cobblemon Trainer Structures 1.7.1
- Architectury API 13.0.11+fabric
- Fix Cobblemon Pokemon Experience 1.1.1+1.21.1-fabric

### Features

- NPC Pokémon trainers
- Trainer battles
- Trainer structures
- Varied trainer teams
- Trainer rewards
- Improved experience gain during trainer battles

### Result

✅ V0.3 Trainers completed.

---

## V0.2.0 — Pokémon World

Status: ✅ Completed

### Added

#### World Generation

- Terralith 2.6.2
- Cobblemon: Extra Structures 1.21.1-1.3.0
- Cobblemon: Nests & Dens 1.3.3
- Lithostitched 1.7.13-fabric-21.1

#### Pokémon World

- CobbleStructures 1.1.0+mod
- CobbleDollars 2.0.0+Beta-6.1
- Another Furniture 4.0.2
- Cobblemon PokéNav 2.3.3
- Cobblemon Repel 1.7-1.4
- Waystones 21.1.40+fabric-1.21.1
- Cobblemon Integrations 1.1.6

#### Dependencies

- Balm 21.0.64+fabric-1.21.1
- Forge Config API Port v21.1.6-1.21.1-Fabric

### Compatibility

#### Cobblemon Auto Tidy Up PC

Rejected due to resource reload failure.

#### Cobblemon UI Tweaks

Removed due to crash when opening the Pokémon Stats/EV interface.

### Result

✅ V0.2 Pokémon World completed.

---

## V0.1.0 — Foundation

Status: ✅ Completed

### Added

#### Core

- Minecraft 1.21.1
- Fabric
- Fabric API
- Fabric Language Kotlin
- Cobblemon 1.7.3

#### Performance

- Sodium
- Lithium
- ImmediatelyFast
- FerriteCore
- ModernFix

#### Quality of Life

- Xaero's Minimap
- Xaero's World Map
- EMI
- Jade
- Mouse Tweaks

#### Pokémon Quality of Life

- Cobbledex

### Result

✅ V0.1 Foundation completed.
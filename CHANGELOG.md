# CobbleHorizons Changelog

All notable changes to CobbleHorizons will be documented in this file.

---

## [Unreleased]

### Added

- Initial project repository.
- Project documentation.
- Development roadmap.
- Mod tracking structure.
- Testing structure.

---
## V0.3.0 — Trainers

Status: ✅ Completed

### Added

#### Trainers

- Radical Cobblemon Trainers 0.18.1-beta
- Radical Cobblemon Trainers API 0.15.2-beta
- Cobblemon Trainer Structures 1.7.1

#### Dependencies

- Architectury API 13.0.11+fabric

#### Battle Improvements

- Fix Cobblemon Pokemon Experience 1.1.1+1.21.1-fabric

### Trainer Gameplay

- Added NPC Pokémon trainers throughout the world.
- Added trainer battle encounters.
- Added trainer-related structures.
- Added varied trainer teams.
- Added trainer rewards and battle locations.

### Experience

- Improved Pokémon experience gain during trainer battles.
- Pokémon now receive experience correctly during multi-Pokémon trainer battles.

### Testing

Validated:

- Trainer spawning
- Trainer battles
- Trainer structures
- Trainer rewards
- Pokémon battle compatibility
- Experience gain
- Existing world compatibility
- Singleplayer stability

### Result

✅ V0.3 Trainers completed.

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

### World

- Expanded world generation and biome variety.
- Added Pokémon-related structures.
- Added PokéCenters and PokéMarts.
- Added Pokémon nests and dens.
- Added additional exploration locations.

### Exploration

- Added Pokémon spawn information through PokéNav.
- Added fast travel through Waystones.
- Added Pokémon Repel functionality.
- Added improved Cobblemon integration with existing systems.

### Economy

- Added CobbleDollars.
- Added Pokémon-related merchants and economy functionality.

### Compatibility

#### Removed Cobblemon UI Tweaks 1.0.7

Reason:

- Crashed when opening Pokémon Stats/EV screen.
- Incompatible with the Cobblemon 1.7.3 Stats UI implementation.

#### Cobblemon Auto Tidy Up PC remains rejected

Reason:

- Resource reload failure.

### Testing

Validated:

- World generation
- Biomes
- Pokémon spawning
- Pokémon structures
- PokéCenters
- PokéMarts
- Economy
- PokéNav
- Waystones
- Repel
- Nests & Dens
- Cobblemon integrations
- Existing Cobblemon gameplay
- Singleplayer stability

### Result

✅ V0.2 Pokémon World completed.

## V0.1 — Foundation

Status: ✅ Completed

### Added

#### Core

- Minecraft 1.21.1
- Fabric Loader 0.19.3
- Fabric API 0.116.15+1.21.1
- Cobblemon 1.7.3

#### Performance

- Sodium 0.8.13-beta.2
- Lithium 0.15.4
- ImmediatelyFast 1.6.11+1.21.1
- FerriteCore 7.0.3
- ModernFix 5.25.1+mc1.21.1

#### General Quality of Life

- Xaero's Minimap 26.4.2
- Xaero's World Map 1.44.2
- EMI 1.1.24
- Jade 15.10.6
- Mouse Tweaks 2.26

#### Pokémon Quality of Life

- Cobblemon Pokedex (Cobbledex) 1.2.0
- Cobblemon UI Tweaks 1.0.7
- Fabric Language Kotlin 1.13.13+kotlin.2.4.10

### Tested

- Game startup
- World creation
- Existing world loading
- Starter selection
- Natural Pokémon spawning
- Pokémon battles
- Pokémon capturing
- Pokémon progression
- Exploration
- Performance stack
- General QoL stack
- Pokémon QoL stack
- Extended singleplayer gameplay

### Rejected

#### Cobblemon Auto Tidy Up PC 1.2-SNAPSHOT

Rejected during V0.1 testing.

Reason:

- Caused a resource reload failure on Minecraft 1.21.1 with Cobblemon 1.7.3.
- Game failed to load correctly while the mod was enabled.
- Removing/disabling the mod resolved the issue.

The mod may be reevaluated in a future version if a stable compatible release becomes available.

### Result

✅ V0.1 Foundation completed.

This version establishes the stable singleplayer foundation for future CobbleHorizons development.
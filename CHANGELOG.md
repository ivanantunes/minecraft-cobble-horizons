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

## V0.1 — Foundation

Status: In Development

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
- Exploration
- Performance stack
- General QoL stack
- Pokémon QoL stack

### Rejected

#### Cobblemon Auto Tidy Up PC 1.2-SNAPSHOT

Rejected during V0.1 testing.

Reason:

- Caused a resource reload failure on Minecraft 1.21.1 with Cobblemon 1.7.3.
- Game failed to load correctly while the mod was enabled.
- Removing/disabling the mod resolved the issue.

The mod may be reevaluated in a future version if a stable compatible release becomes available.
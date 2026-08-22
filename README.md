<div align="center">

<img src="imgs/logo.png" alt="CobbleHorizons" width="460">

# CobbleHorizons

### Minecraft is the world. Pokémon is the game.

[![Minecraft](https://img.shields.io/badge/Minecraft-1.21.1-62B47A?style=for-the-badge&logo=minecraft)](https://www.minecraft.net/)
[![Fabric](https://img.shields.io/badge/Fabric-0.19.3-D6B98C?style=for-the-badge)](https://fabricmc.net/)
[![Cobblemon](https://img.shields.io/badge/Cobblemon-1.7.3-42B8C6?style=for-the-badge)](https://modrinth.com/mod/cobblemon)
[![Release](https://img.shields.io/badge/release-1.2.0-F4A261?style=for-the-badge)](CHANGELOG.md)

**Download the latest `.mrpack` from GitHub Releases.**

[Adventure guide](docs/adventure-guide.md) · [Installation](docs/installation.md) · [Mod list](docs/mod-list.md) · [Performance & controls](docs/performance-and-controls.md) · [Troubleshooting](docs/troubleshooting.md)

</div>

![CobbleHorizons world](imgs/fundo2.png)

## Welcome to CobbleHorizons

CobbleHorizons is a Pokémon-first adventure modpack for Minecraft 1.21.1. It combines Cobblemon with a structured League campaign, exploration, trainers, gyms, breeding, Mega Evolution, legendary content, economy, navigation, quests, custom music and a polished interface while keeping Minecraft as the open world around the Pokémon journey.

The project is built around three principles:

- **Pokémon stays at the center of progression.**
- **The official release installs with the intended defaults and minimal manual setup.**
- **Stability, compatibility and long-play usability come before feature count.**

## Current release

| Component | Version / state |
|---|---|
| CobbleHorizons | **1.2.0** |
| Minecraft | 1.21.1 |
| Fabric Loader | 0.19.3 |
| Cobblemon | 1.7.3 |
| Quest system | QuestZ 1.0.1 |
| Java | 21 |
| Default language | English (US) |
| Manifest content | 68 mods, 1 external datapack, 3 external resource packs, 3 shaders |
| First-party content | 2 datapacks + 1 unified resource pack |
| Effective datapack count | 3 |
| Effective resource-pack count | 4 |

## What changed in 1.2.0

### CobbleHorizons League progression

Version 1.2.0 introduces the first-party **CobbleHorizons League** RCT series:

`Brock → Misty → Lt. Surge → Erika → Sabrina → Koga → Blaine → Clair → Lorelei → Bruno → Agatha → Lance → Champion Terry`

The player starts with a level cap of **15**. Overleveling is disabled and the cap follows the next required League opponent. The designed cap progression is:

`15 → 27 → 34 → 44 → 59 → 68 → 76 → 81 → 85`

League bosses no longer spawn naturally around the player. They are reserved for the intended gym / League progression, while normal RCT trainers can still populate the world.

### Quest campaign

The QuestZ campaign now contains:

- **107 active gameplay quests**;
- **1 root advancement**;
- **12 Species Hunt templates hidden and disabled** until species-specific capture filtering is reliable for the exact Cobblemon version.

The main campaign flows through starter selection, Apricorn research, first capture, Pokédex, first trainer, eight gyms, Elite Four, Champion and the **Horizon Elite** postgame objective.

### Presentation and identity

The old separate Branding and Identity packs were merged into one first-party resource pack:

`resourcepacks/CobbleHorizons.zip`

It contains the CobbleHorizons branding, title/UI assets, button theme, foliage/colormap adjustments and six original procedural music tracks:

- Horizon Menu
- Routes and Fields
- Quiet Town
- Starlit Research
- Caves and Ruins
- Beyond the Horizon

Cobblemon Interface and Cobblemon Interface: Modded are distributed through their official Modrinth sources. Faithful 32x is no longer part of the release.

### Curated world spawning

CobbleHorizons remains Pokémon-first, but 1.2.0 restores the four core passive farm animals needed for early survival:

- cow;
- pig;
- chicken;
- sheep.

Villagers, wandering traders, iron/snow golems, the Ender Dragon and Wither also remain allowed. Other world-generated vanilla mobs continue to be suppressed by the curated Mob Filter rules.

## Highlights

| Experience | Included |
|---|---|
| Pokémon adventure | Catching, training, battles, Pokédex, breeding, TMs/TRs, Mega Evolution, legends and badges |
| League progression | Eight Gym Leaders, Elite Four and Champion with RCT level-cap progression |
| Guided campaign | 107 active QuestZ gameplay quests with prerequisite gating |
| Living world | Terralith terrain, Pokémon structures, nests, dens, normal trainers, gyms and legendary monuments |
| Survival baseline | Cow, pig, chicken and sheep restored for food and core vanilla materials |
| Exploration | Xaero's Minimap, Xaero's World Map, Waystones and CobbleNav |
| Presentation | FancyMenu, custom loading flow, unified branding, six original music tracks and Cobblemon Interface packs |
| Performance | Sodium, Lithium, ImmediatelyFast, FerriteCore and ModernFix |
| Visual options | MakeUp Ultra Fast, Complementary Reimagined and BSL shaders |

## Installation

1. Open the repository's **Releases** page.
2. Download the latest `CobbleHorizons-*.mrpack`.
3. Import it into the Modrinth App as a **new instance**.
4. Allocate **6 GB RAM**.
5. Start the game with Java 21.

A fresh import is strongly recommended because Default Options only applies defaults safely to keys/settings that have not already been customized in an older instance.

See [Installation and Updates](docs/installation.md).

## Curated controls

| Action | Key |
|---|---|
| Open QuestZ | `L` |
| Send / recall selected Pokémon | `R` |
| Cobblemon Summary | `V` |
| CobbleNav PokéNav | `N` |
| CobbleNav location screen | `K` |
| Open Inmis backpack | `B` |
| Hide Cobblemon party HUD | `H` |
| Xaero World Map | `M` |
| Create Xaero waypoint | `G` |
| Xaero waypoint list | `Y` |
| Enlarge minimap | `Z` |
| Xaero minimap settings | `F6` |
| Iris shader selection | `F7` |
| Reload shaders | `F8` |
| Toggle shaders | `F9` |
| Jade configuration | `F10` |
| Jade details | `Right Shift` |

Development/debug keybinds that are not needed during normal gameplay are intentionally unbound to reduce conflicts.

## Resource-pack stack

The release requires the following project/interface packs through Global Packs:

- CobbleHorizons;
- Cobblemon Battle Tracks;
- Cobblemon Interface: Modded;
- Cobblemon Interface.

Cobbreeding also exposes its Pasture Fix built-in resources. The exact resolved priority is controlled by the packaged configuration; use a fresh instance when validating it.

## Repository policy

This Git repository stores **CobbleHorizons source/configuration**, not a mirror of third-party binaries.

Tracked here:

- curated `config/` files;
- `CobbleHorizons-QuestZ` datapack;
- `CobbleHorizons-Progression` datapack;
- the first-party `CobbleHorizons.zip` resource pack;
- project assets and documentation;
- validation/build scripts when applicable.

Do not commit:

- third-party mod JARs;
- third-party datapack/resource-pack/shader archives;
- generated `.mrpack` release files;
- worlds, logs, crash reports, caches or personal root `options.txt`.

Generated `.mrpack` files belong on **GitHub Releases**.

See [Repository Structure](docs/repository-structure.md).

## Documentation

- [Installation and updates](docs/installation.md)
- [Adventure Guide and progression](docs/adventure-guide.md)
- [Included content](docs/mod-list.md)
- [Performance and controls](docs/performance-and-controls.md)
- [Balance and design rules](docs/balance-and-design.md)
- [Repository structure](docs/repository-structure.md)
- [Release checklist](docs/release-checklist.md)
- [Troubleshooting](docs/troubleshooting.md)
- [Contributing](CONTRIBUTING.md)
- [Changelog](CHANGELOG.md)
- [Credits](CREDITS.md)
- [Project license](LICENSE.md)

## Support

When reporting a problem, include:

- CobbleHorizons version;
- operating system;
- clear reproduction steps;
- screenshots when relevant;
- a sanitized `latest.log` link from [mclo.gs](https://mclo.gs/).

For progression, spawn or quest issues, reproduce in a **fresh world** before reporting whenever possible.

## Credits and legal notice

CobbleHorizons is an independent community project and is not affiliated with Mojang Studios, Microsoft, Nintendo, Game Freak, The Pokémon Company, Cobblemon, Modrinth or the authors of bundled third-party projects.

Minecraft, Pokémon, Cobblemon, included mods, third-party datapacks, resource packs and shaders remain the property of their respective owners/authors and are subject to their own licenses and terms.

CobbleHorizons branding, original project assets, configuration and documentation are covered by the [project license](LICENSE.md).

---

<div align="center">

### Explore. Capture. Battle. Build your journey.

</div>

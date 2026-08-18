<div align="center">

<img src="imgs/logo.png" alt="CobbleHorizons" width="460">

# CobbleHorizons

### Minecraft is the world. Pokémon is the game.

[![Minecraft](https://img.shields.io/badge/Minecraft-1.21.1-62B47A?style=for-the-badge&logo=minecraft)](https://www.minecraft.net/)
[![Fabric](https://img.shields.io/badge/Fabric-0.19.3-D6B98C?style=for-the-badge)](https://fabricmc.net/)
[![Cobblemon](https://img.shields.io/badge/Cobblemon-1.7.3-42B8C6?style=for-the-badge)](https://modrinth.com/mod/cobblemon)
[![Release](https://img.shields.io/badge/release-1.1.0-F4A261?style=for-the-badge)](CHANGELOG.md)

**Download the latest `.mrpack` from the GitHub Releases page.**

[Adventure guide](docs/adventure-guide.md) · [Installation](docs/installation.md) · [Mod list](docs/mod-list.md) · [Performance & controls](docs/performance-and-controls.md) · [Troubleshooting](docs/troubleshooting.md)

</div>

![CobbleHorizons world](imgs/fundo2.png)

## Welcome to CobbleHorizons

CobbleHorizons is a Pokémon-first adventure modpack for Minecraft 1.21.1. The project combines Cobblemon with exploration, trainers, gyms, breeding, Mega Evolution, legendary content, economy, navigation, custom quests and a polished interface while keeping Minecraft as the open world around the Pokémon journey.

The pack is built around three principles:

- **Pokémon stays at the center of progression.**
- **The official release should install and play with minimal setup.**
- **Performance and compatibility are preferred over unnecessary complexity.**

## Current release

| Component | Version |
|---|---|
| CobbleHorizons | 1.1.0 |
| Minecraft | 1.21.1 |
| Fabric Loader | 0.19.3 |
| Cobblemon | 1.7.3 |
| Quest system | QuestZ 1.0.1 |
| Java | 21 |
| Default language | English (US) |
| Included release content | 68 mods, 2 datapacks, 3 resource packs, 3 shaders |

## Highlights

| Experience | What is included |
|---|---|
| Pokémon adventure | Catching, training, battles, Pokédex, breeding, TMs/TRs, Mega Evolution, legends and badges |
| Guided progression | 93 active English gameplay quests with real prerequisite gating through QuestZ |
| Living world | Terralith terrain, Pokémon structures, nests, dens, trainers, gyms and legendary monuments |
| Pokémon-first world | Naturally generated vanilla mobs are suppressed while progression-critical exceptions remain |
| Exploration | Xaero's Minimap, Xaero's World Map, Waystones and CobbleNav |
| Presentation | Custom loading screen, title screen, buttons, branding, music and sound configuration |
| Performance | Sodium, Lithium, ImmediatelyFast, FerriteCore and ModernFix |
| Visual options | MakeUp Ultra Fast, Complementary Reimagined, BSL and optional Faithful 32x |

## Quest progression

CobbleHorizons 1.1.0 uses **QuestZ** and the first progression steps are intentionally ordered:

`Choose Your Partner → Red Apricorn Research → A New Friend`

That means the player first chooses a starter, carries 8 Red Apricorns, and then catches the first Pokémon.

Every active non-root quest contains a prerequisite check, preventing later objectives from completing before their intended parent quest.

The 12 experimental **Species Hunt** quests are currently hidden and disabled because species-specific capture filtering was not reliable in the tested Cobblemon/QuestZ setup. They remain reserved for a future corrected implementation.

See the full overview in the [Adventure Guide](docs/adventure-guide.md).

## Installation

1. Open the repository's **Releases** page.
2. Download the latest `CobbleHorizons-*.mrpack`.
3. Import it into the Modrinth App as a new instance.
4. Allocate **6 GB RAM**.
5. Start the game.

A fresh import applies the tested configuration, English language, resource-pack stack, controls and performance defaults.

> Existing Minecraft instances can retain old advancement progress and old client settings. Use a fresh instance and preferably a fresh world when validating a new CobbleHorizons release.

## Default controls

| Action | Key |
|---|---|
| Open CobbleHorizons quests (QuestZ) | `L` |
| Send selected Pokémon | `R` |
| Xaero's World Map | `M` |
| Cobblemon Summary | `V` |
| Select shader | `F7` |
| Reload shader | `F8` |
| Toggle shader | `F9` |

## Visual profiles

- **MakeUp Ultra Fast** — recommended for integrated and entry-level graphics.
- **Complementary Reimagined** — recommended balance of quality and performance.
- **BSL** — stronger visual profile for more capable GPUs.
- **Faithful 32x** — optional vanilla-style texture upgrade.

![CobbleHorizons portal](imgs/fundo1.png)

## Repository policy

This repository stores the **first-party CobbleHorizons source and configuration**, not copies of every dependency.

Tracked here:

- CobbleHorizons configuration;
- the CobbleHorizons QuestZ datapack;
- CobbleHorizons branding and project assets;
- documentation.

Not tracked as source:

- third-party mod `.jar` files;
- third-party datapack/resource-pack archives;
- generated `.mrpack` release artifacts;
- local worlds, logs, screenshots and personal `options.txt`.

Third-party content is referenced by the release manifest and remains subject to its original license and distribution terms.

See [Repository Structure](docs/repository-structure.md).

## Documentation

- [Installation and updates](docs/installation.md)
- [Adventure Guide and quests](docs/adventure-guide.md)
- [Complete mod and content list](docs/mod-list.md)
- [Performance, controls and visual profiles](docs/performance-and-controls.md)
- [Repository structure](docs/repository-structure.md)
- [Troubleshooting](docs/troubleshooting.md)
- [Contributing](CONTRIBUTING.md)
- [Changelog](CHANGELOG.md)
- [Project license](LICENSE.md)

## Support

When reporting a problem, include the CobbleHorizons version, operating system, reproduction steps, screenshots when relevant, and a link to `latest.log` uploaded through [mclo.gs](https://mclo.gs/).

## Credits and legal notice

CobbleHorizons is an independent community project and is not affiliated with Mojang Studios, Microsoft, Nintendo, Game Freak, The Pokémon Company, Cobblemon, Modrinth or the authors of bundled third-party projects.

Minecraft, Pokémon, Cobblemon, included mods, third-party datapacks, resource packs and shaders belong to their respective owners and authors. CobbleHorizons branding and original project assets are covered by the [project license](LICENSE.md).

---

<div align="center">

### Explore. Capture. Battle. Build your journey.

</div>

# Performance, Controls and Visual Profiles

## Plug-and-play baseline

| Setting | Default | Purpose |
|---|---:|---|
| Render distance | 12 chunks | Balanced exploration visibility |
| Simulation distance | 8 chunks | Controlled CPU load |
| Frame-rate limit | 120 FPS | Avoids unnecessary GPU usage |
| Graphics | Fancy | Preserves the intended presentation |
| Mipmaps | 4 | Reduces distant texture shimmer |
| Shaders | Disabled | Safest first launch |
| Language | English (US) | Official player-facing baseline |

These defaults are shipped through `config/defaultoptions/extra/options.txt`.

Sodium, Lithium, ImmediatelyFast, FerriteCore and ModernFix use conservative settings intended to prioritize compatibility.

## Curated controls

| Action | Key |
|---|---|
| Open CobbleHorizons quests (QuestZ) | `L` |
| Send selected Pokémon | `R` |
| Xaero's World Map | `M` |
| Cobblemon Summary | `V` |
| Iris shader selection | `F7` |
| Iris shader reload | `F8` |
| Iris shader toggle | `F9` |

QuestZ registers `L` as its default quest-screen key. Personal key changes in an existing instance can override it.

## Shader profiles

Shaders are optional and disabled by default.

| Profile | Best for |
|---|---|
| MakeUp Ultra Fast 9.0c | Integrated and entry-level graphics |
| Complementary Reimagined r5.8.1 | Most gaming PCs |
| BSL 8.3 | Stronger GPUs and cinematic screenshots |

Start with MakeUp Ultra Fast, then try Complementary. Use BSL when performance remains comfortable.

## Resource-pack order

The tested active stack is:

1. CobbleHorizons Branding
2. Cobblemon Battle Tracks
3. Cobbreeding Pasture Fix
4. Fabric resources
5. Vanilla resources

Faithful 32x is installed by the release but optional. Keep CobbleHorizons Branding at higher priority when enabling it.

## Title-screen presentation

CobbleHorizons uses FancyMenu for the main interface and a first-party branding resource pack for Minecraft title textures.

The final 1.1.0 layout does not render the old extra logo element above the buttons, avoiding the duplicated-logo effect.

The branding resource pack also replaces the vanilla yellow rotating splash with an invisible entry.

## Pokémon-first spawn policy

Vanilla mobs created through natural generation, chunk generation, spawners, patrols, reinforcements, jockeys and trial spawners are suppressed.

Cobblemon Pokémon, trainers and modded NPCs remain unaffected.

Villagers, wandering traders, iron and snow golems, the Ender Dragon and the Wither are intentional exceptions. Existing mobs already saved in older worlds are not deleted automatically.

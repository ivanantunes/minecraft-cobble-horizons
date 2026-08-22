# Performance, Controls and Visual Profiles — 1.2.0

## Plug-and-play baseline

| Setting | Default | Purpose |
|---|---:|---|
| Render distance | 12 chunks | Balanced exploration visibility |
| Simulation distance | 8 chunks | Controlled CPU load |
| Frame-rate limit | 120 FPS | Avoid unnecessary GPU load |
| Graphics | Fancy | Intended presentation baseline |
| Mipmaps | 4 | Reduce distant texture shimmer |
| Language | English (US) | Official player-facing baseline |
| Master volume | 70% | Balanced game audio |
| Music volume | 35% | Keeps CobbleHorizons music present without dominating gameplay |

These Minecraft defaults are shipped through:

`config/defaultoptions/options.txt`

Key mappings are shipped separately through:

`config/defaultoptions/keybindings.txt`

## Curated controls

| Action | Key |
|---|---|
| QuestZ | `L` |
| Send / recall selected Pokémon | `R` |
| Cobblemon Summary | `V` |
| CobbleNav PokéNav | `N` |
| CobbleNav location screen | `K` |
| Inmis backpack | `B` |
| Hide party HUD | `H` |
| Previous / next party slot | `↑` / `↓` |
| Xaero World Map | `M` |
| New Xaero waypoint | `G` |
| Xaero waypoint list | `Y` |
| Enlarge minimap | `Z` |
| Xaero minimap settings | `F6` |
| Iris shader selection | `F7` |
| Iris shader reload | `F8` |
| Iris shader toggle | `F9` |
| Jade configuration | `F10` |
| Jade details | `Right Shift` |

The Cobblemon internal PokéNavigator binding is intentionally unbound because CobbleNav owns `N` for the player-facing PokéNav.

Secondary Xaero actions, Cobblemon debug controls, FancyMenu/Drippy development overlays and Iris wireframe are intentionally unbound.

## macOS function keys

On macOS, F6–F10 may map to system/media actions depending on keyboard settings. If needed:

- hold `Fn` while pressing the function key; or
- configure macOS to use F1, F2, etc. as standard function keys.

This is separate from a Minecraft key conflict.

## Shader profiles

| Profile | Best for |
|---|---|
| MakeUp Ultra Fast 9.0c | Integrated / entry-level graphics |
| Complementary Reimagined r5.8.1 | Balanced quality and performance |
| BSL 8.3 | Stronger GPUs and screenshots |

Start without shaders when diagnosing performance or rendering issues.

## Resource packs

CobbleHorizons 1.2.0 no longer uses Faithful 32x.

The packaged visual stack combines:

- first-party CobbleHorizons branding/music/UI assets;
- Cobblemon Battle Tracks;
- Cobblemon Interface: Modded;
- Cobblemon Interface;
- Cobbreeding's built-in Pasture Fix resources.

Global Packs is used so the required release packs do not depend solely on a user's old `options.txt` state.

## Music

The first-party resource pack includes six original tracks for menu/ambient/world identity while the Battle Tracks pack remains available for battles.

If music seems missing:

1. confirm Music volume is above zero;
2. confirm `CobbleHorizons.zip` is loaded;
3. confirm Global Packs configuration is present;
4. test in a fresh instance before changing pack order.

## Performance troubleshooting baseline

Before reporting low FPS:

1. disable shaders with `F9`;
2. keep render distance at 12 or reduce it to 10;
3. keep simulation distance at 8 or reduce it;
4. allocate 6 GB RAM;
5. compare a fresh world and existing world;
6. check `latest.log` for repeated errors.

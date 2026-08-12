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

Sodium, Lithium, ImmediatelyFast, FerriteCore and ModernFix use stable, conservative settings. Experimental rendering flags and aggressive threading changes remain disabled.

## Curated controls

| Action | Key |
|---|---|
| Send selected Pokémon | `R` |
| Xaero's World Map | `M` |
| Cobblemon Summary | `V` |
| CobbleHorizons Quest Book | `[` |
| Iris shader selection | `F7` |
| Iris shader reload | `F8` |
| Iris shader toggle | `F9` |

EMI and Jade retain their context-sensitive recipe and usage shortcuts. These operate inside inventory or overlay contexts.

The Quest Book key does not conflict with the curated defaults. Boundless loads the bundled CobbleHorizons campaign on first launch; the inventory button is also enabled by default.

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

Faithful 32x is installed but optional. Keep CobbleHorizons Branding at higher priority when enabling it.

## Pokémon-first spawn policy

Vanilla mobs created through natural generation, chunk generation, spawners, patrols, reinforcements, jockeys and trial spawners are suppressed. Cobblemon Pokémon, trainers and modded NPCs remain unaffected.

Villagers, wandering traders, iron and snow golems, the Ender Dragon and the Wither are explicit exceptions. Existing mobs in older worlds are not deleted automatically.

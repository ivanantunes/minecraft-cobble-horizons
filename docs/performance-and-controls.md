# Performance, Controls, and Visual Profiles

## Plug-and-play baseline

CobbleHorizons uses a conservative profile intended to behave consistently on Windows, macOS, integrated graphics, and dedicated GPUs.

| Setting | Default | Reason |
|---|---:|---|
| Render distance | 12 chunks | Balanced exploration visibility and frame time |
| Simulation distance | 8 chunks | Limits CPU load without making the world feel inactive |
| Frame-rate limit | 120 FPS | Avoids unnecessary GPU load on high-refresh systems |
| Graphics | Fancy | Preserves the intended presentation |
| Mipmaps | 4 | Reduces texture shimmer |
| Shaders | Disabled | Guarantees the safest first launch |

Sodium, Lithium, ImmediatelyFast, FerriteCore, and ModernFix use stable or conservative options. Experimental rendering flags and aggressive threading changes remain disabled.

## Curated controls

| Action | Key |
|---|---|
| Send selected Pokémon | R |
| Xaero's World Map | M |
| Cobblemon Summary | V |
| Iris shader selection | F7 |
| Iris shader reload | F8 |
| Iris shader toggle | F9 |

The dedicated Iris keys prevent shader reload from competing with Cobblemon's primary `R` action. Moving the Cobblemon Summary to `V` keeps `M` available for the world map.

EMI and Jade retain their context-sensitive recipe and usage shortcuts. Their actions operate in inventory or overlay contexts and do not replace the world controls above.

## Shader profiles

Shaders are optional and disabled by default.

| Profile | Best for | Notes |
|---|---|---|
| MakeUp Ultra Fast 9.0c | Integrated and entry-level graphics | Highest-performance visual option |
| Complementary Reimagined r5.8.1 | Most gaming PCs | Recommended balance |
| BSL 8.3 | Stronger GPUs and screenshots | Rich lighting and cinematic presentation |

Start with MakeUp Ultra Fast, then try Complementary. Use BSL only when frame rate remains comfortable.

## Resource-pack order

The default active stack is:

1. CobbleHorizons Branding
2. Battle Tracks
3. Cobbreeding Pasture Fix
4. Fabric and vanilla resources

Faithful 32x is installed but not enabled by default. If enabled, keep CobbleHorizons Branding above it so menu identity remains intact.

## Memory guidance

Allocate 6 GB for the normal profile and 8 GB when using shaders, high-resolution resource packs, or long sessions. Avoid allocating excessive memory because larger heaps can produce longer garbage-collection pauses.

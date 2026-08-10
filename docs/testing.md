# CobbleHorizons Testing

Every development milestone must be tested before the next major gameplay layer is introduced.

---

# Test Environment

## Game

Minecraft: 1.21.1

Fabric Loader: 0.19.3

Fabric API: 0.116.15+1.21.1

Cobblemon: 1.7.3

---

# V0.1 — Foundation Testing

Status: ✅ Completed

## Launch

- [x] Game launches successfully
- [x] No critical startup errors
- [x] Main menu loads correctly
- [x] Mod list loads correctly

## World

- [x] New world can be created
- [x] Existing world loads correctly
- [x] World loads correctly
- [x] Chunks generate correctly
- [x] No major generation errors detected

## Cobblemon

- [x] Starter selection works
- [x] Pokémon spawn naturally
- [x] Pokémon models load correctly
- [x] Pokémon animations work
- [x] Pokémon can be captured
- [x] Pokémon battles work
- [x] Pokémon gain experience
- [x] Pokémon level up
- [x] Pokémon progression works correctly

## Performance

Installed and tested:

- [x] Sodium
- [x] Lithium
- [x] ImmediatelyFast
- [x] FerriteCore
- [x] ModernFix

Result:

- [x] Game remained stable after performance mods were added
- [x] Existing world continued loading correctly
- [x] Exploration remained functional
- [x] Cobblemon gameplay remained functional

## General Quality of Life

Installed and tested:

- [x] Xaero's Minimap
- [x] Xaero's World Map
- [x] EMI
- [x] Jade
- [x] Mouse Tweaks

Result:

- [x] Game launches correctly
- [x] World loads correctly
- [x] No critical incompatibility detected

## Pokémon Quality of Life

Installed and tested:

- [x] Cobblemon Pokedex (Cobbledex)
- [x] Cobblemon UI Tweaks
- [x] Fabric Language Kotlin

Rejected:

- [x] Cobblemon Auto Tidy Up PC 1.2-SNAPSHOT

### Auto Tidy Up PC Issue

Observed behavior:

- Resource reload failure
- Game failed to load correctly

Resolution:

- Disabling/removing Auto Tidy Up PC resolved the issue

Status:

❌ Rejected for V0.1

---

# V0.1 Scope

V0.1 validation focuses on singleplayer.

Multiplayer and dedicated server compatibility are not part of the acceptance criteria for this milestone.

They may be evaluated in a future development phase.

---

# Final V0.1 Result

- [x] Core baseline approved
- [x] Performance layer approved
- [x] General QoL approved
- [x] Pokémon QoL approved
- [x] Extended singleplayer stability testing
- [x] Final V0.1 validation

Result:

✅ **PASS**

V0.1 — Foundation is considered complete and ready to be tagged as:

`v0.1.0`
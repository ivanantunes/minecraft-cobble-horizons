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

# Current V0.1 Result

Status:

- [x] Core baseline approved
- [x] Performance layer approved
- [x] General QoL approved
- [x] Pokémon QoL approved
- [ ] Multiplayer validation
- [ ] Extended stability testing
- [ ] Final V0.1 validation

Current result:

**PASS WITH REMAINING VALIDATION**

---

# Remaining Tests

Before declaring V0.1 complete:

- [ ] 30-minute continuous session
- [ ] 1-hour continuous session
- [ ] Extended exploration
- [ ] Multiple battles
- [ ] Multiple captures
- [ ] Dedicated server startup
- [ ] Multiplayer connection
- [ ] Multiplayer Pokémon spawning
- [ ] Multiplayer capturing
- [ ] Multiplayer battles
- [ ] Server stability

---

# Test Result

Version:

V0.1 — Foundation

Result:

- [ ] PASS
- [x] PASS WITH REMAINING VALIDATION
- [ ] FAIL
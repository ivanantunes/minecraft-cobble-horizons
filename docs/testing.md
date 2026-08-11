# CobbleHorizons Testing

Every development milestone must be tested before the next major gameplay layer is introduced.

---

# Test Environment

Minecraft: 1.21.1

Fabric Loader: 0.19.3

Fabric API: 0.116.15+1.21.1

Cobblemon: 1.7.3

Primary validation target:

**Singleplayer**

---

# V0.1 — Foundation

Status: ✅ PASS

Validated:

- Game startup
- World creation
- World loading
- Cobblemon startup
- Starter selection
- Pokémon spawning
- Pokémon capturing
- Pokémon battles
- Pokémon progression
- Performance stack
- General QoL
- Pokémon QoL
- Singleplayer stability

---

# V0.2 — Pokémon World

Status: ✅ PASS

## World Generation

- [x] New world creation
- [x] Terralith world generation
- [x] Terrain generation
- [x] Biome generation
- [x] Chunk generation
- [x] Pokémon continue spawning
- [x] Cobblemon gameplay remains functional

## Structures

- [x] Cobblemon Extra Structures loads
- [x] CobbleStructures loads
- [x] Pokémon structures generate
- [x] PokéCenter functionality
- [x] PokéMart functionality
- [x] Nests & Dens loads correctly

## Economy

- [x] CobbleDollars loads
- [x] Pokémon merchants load
- [x] Economy functionality works

## Exploration

- [x] PokéNav loads and works
- [x] Pokémon spawn information works
- [x] Waystones load
- [x] Waystone teleportation works
- [x] Repel loads
- [x] World exploration remains stable

## Integrations

- [x] Cobblemon Integrations loads
- [x] Jade remains functional
- [x] Waystones remain functional
- [x] Cobblemon remains functional

---

# Compatibility Issues Found

## Cobblemon Auto Tidy Up PC

Status:

❌ Rejected

Issue:

Resource reload failure.

Resolution:

Mod removed.

---

## Cobblemon UI Tweaks

Status:

❌ Rejected

Issue:

Client crash when opening Pokémon Stats/EV screen.

Cause:

Incompatible Mixin targeting Cobblemon's StatWidget implementation.

Resolution:

Mod removed.

After removal, the game returned to normal operation.

---

# V0.2 Final Result

- [x] World generation approved
- [x] Pokémon structures approved
- [x] Pokémon civilization systems approved
- [x] Economy approved
- [x] Exploration systems approved
- [x] Integrations approved
- [x] Critical compatibility issues resolved
- [x] Singleplayer validation completed

Result:

✅ **PASS**

V0.2 — Pokémon World is considered complete.

Release:

`v0.2.0`
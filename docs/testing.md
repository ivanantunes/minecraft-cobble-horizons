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

## Result

✅ **PASS**

V0.2 — Pokémon World completed.

Release:

`v0.2.0`

---

# V0.3 — Trainers

Status: ✅ PASS

## Trainer System

- [x] Radical Cobblemon Trainers loads
- [x] Radical Cobblemon Trainers API loads
- [x] Trainer NPCs appear correctly
- [x] Trainer battles start correctly
- [x] Trainer battles finish correctly
- [x] Pokémon can participate normally in trainer battles
- [x] Trainer teams load correctly

## Trainer Structures

- [x] Cobblemon Trainer Structures loads
- [x] Trainer structures generate correctly
- [x] Trainers inside structures function correctly
- [x] Battle locations remain stable

## Experience

- [x] Fix Cobblemon Pokemon Experience loads
- [x] Pokémon receive experience correctly during trainer battles

## Stability

- [x] Existing worlds load correctly
- [x] Pokémon spawning remains functional
- [x] Existing Cobblemon systems remain functional
- [x] No critical trainer-related crashes detected

## Result

✅ **PASS**

V0.3 — Trainers completed.

Release:

`v0.3.0`

---

# V0.4 — Progression

Status: ✅ PASS

## Gym System

- [x] Rad Gyms loads correctly
- [x] Radical Gyms & Structures loads correctly
- [x] Gym structures generate correctly
- [x] Gym-related NPCs load
- [x] Existing trainer system remains functional
- [x] Gym content coexists with Terralith world generation

## Progression

- [x] RCT Trainer Card remains functional
- [x] RCT progression remains functional
- [x] Capture Cap - RCT Version loads correctly
- [x] Level progression systems remain functional
- [x] Existing trainer battles remain functional

## Badges

- [x] Cobblemon Pokemon Badges 0.1.1 loads correctly
- [x] RCT Badges - Cobblemon Pokemon Badges 1.1.2 loads correctly
- [x] Badge integration does not prevent world loading
- [x] RCT remains functional with badge integration

## Pokémon League

- [x] Radical Gyms & Structures League content loads
- [x] Elite Four content is available through the progression system
- [x] Champion content is available through the progression system

## Dependencies

- [x] CobbleFurnies 1.2 loads correctly
- [x] Athena 4.0.6 loads correctly
- [x] Existing Architectury API remains functional
- [x] Existing RCT API remains functional

## Regression Testing

- [x] Existing world loads
- [x] New chunks generate
- [x] Pokémon spawn normally
- [x] Pokémon battles work
- [x] Trainer battles work
- [x] PokéNav works
- [x] Maps work
- [x] Waystones remain functional
- [x] Existing structures remain functional
- [x] No critical progression-related crashes detected

---

# V0.4 Final Result

- [x] Gym system approved
- [x] Gym structures approved
- [x] RCT progression approved
- [x] Capture Cap approved
- [x] Badge system approved
- [x] Badge/RCT integration approved
- [x] Pokémon League content approved
- [x] Singleplayer validation completed

Result:

✅ **PASS**

V0.4 — Progression is considered complete.

Release:

`v0.4.0`

---

# Known Rejected Mods

## Cobblemon Auto Tidy Up PC

Status: ❌ Rejected

Issue:

Resource reload failure.

Resolution:

Mod removed.

---

## Cobblemon UI Tweaks

Status: ❌ Rejected

Issue:

Client crash when opening the Pokémon Stats/EV screen.

Resolution:

Mod removed.

After removal, normal gameplay was restored.

---

# Next Test Phase

## V0.5 — Pokémon Mechanics

Planned testing areas:

- TMs and TRs
- Breeding
- IV/EV systems
- Evolution systems
- Mega Evolution
- Battle gimmicks
- Legendary Pokémon
- Rare encounters
- Pokémon training mechanics
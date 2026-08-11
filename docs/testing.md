# CobbleHorizons Testing

This document tracks technical validation, compatibility issues and the testing strategy used during CobbleHorizons development.

---

# Test Environment

Minecraft: 1.21.1

Fabric Loader: 0.19.3

Fabric API: 0.116.15+1.21.1

Cobblemon: 1.7.3

Primary validation target:

**Singleplayer**

---

# Testing Strategy

## V0.1 – V0.4

Early development used incremental testing.

Mods were installed in small groups and manually validated before additional systems were introduced.

This helped establish a stable technical baseline.

## V0.5+

Starting with V0.5, development moved to a faster batch-integration strategy.

Workflow:

1. Research compatible mods.
2. Install the planned milestone group.
3. Resolve required dependencies.
4. Start Minecraft.
5. Load the development world.
6. Confirm core gameplay remains operational.
7. Collect runtime logs.
8. Investigate crashes and gameplay-breaking errors.
9. Document non-critical warnings.
10. Continue development.

Non-critical log warnings do not automatically block a milestone.

Critical crashes, corrupted worlds or gameplay-breaking incompatibilities must be resolved before release.

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

Result:

✅ PASS

Release:

`v0.1.0`

---

# V0.2 — Pokémon World

Status: ✅ PASS

Validated:

- Terralith world generation
- Terrain generation
- Biome generation
- Pokémon structures
- PokéCenters
- PokéMarts
- Nests & Dens
- CobbleDollars
- Pokémon merchants
- PokéNav
- Waystones
- Repel
- Cobblemon Integrations
- Existing Pokémon gameplay

Result:

✅ PASS

Release:

`v0.2.0`

---

# V0.3 — Trainers

Status: ✅ PASS

Validated:

- Radical Cobblemon Trainers
- RCT API
- Trainer NPCs
- Trainer battles
- Trainer teams
- Trainer structures
- Trainer rewards
- Pokémon experience during trainer battles
- Existing world compatibility
- Existing Pokémon gameplay

Result:

✅ PASS

Release:

`v0.3.0`

---

# V0.4 — Progression

Status: ✅ PASS

Validated:

- Rad Gyms
- Radical Gyms & Structures
- Gym structures
- Gym-related NPCs
- RCT Trainer Card
- Capture Cap
- Pokémon badges
- RCT badge integration
- Trainer battles
- Pokémon League content
- Existing world compatibility
- Existing Pokémon gameplay

Result:

✅ PASS

Release:

`v0.4.0`

---

# V0.5 — Pokémon Mechanics

Status: ✅ PASS — Initial Integration

## Installed

### Moves

- SimpleTMs 2.3.3

### Breeding

- Cobbreeding 2.2.2

### Pokémon Training

- Cobblemon Utility+ 1.7.4

### Battle Mechanics

- Cobblemon: Mega Showdown 1.9.3+1.7.3+1.21.1

### Legendary / Mythical

- Myths and Legends 1.9.0
- Cobblemon: Legendary Monuments 8.1-Love-for-All

### Dependencies

- Cloth Config API 15.0.140+fabric
- owo-lib 0.13.0-alpha.15+1.21
- Accessories 1.1.0-beta.53+1.21.1
- Resourceful Lib 3.0.12
- Chipped 4.0.2

---

# V0.5 Integration Validation

Observed after installation:

- [x] Minecraft starts
- [x] Resource packs enabled
- [x] Existing world loads
- [x] Pokémon continue spawning
- [x] Core Cobblemon gameplay remains operational
- [x] No startup crash observed
- [x] No world-loading crash observed
- [x] New V0.5 mods load
- [x] Runtime logs collected

Full mechanic-by-mechanic validation is intentionally deferred to later full-playthrough testing.

---

# Known Runtime Issues

## Cobblemon Trainer Structures

Observed error:

`Failed to load model cobblemonopponents:models/block/pokeball_trophy_java.json`

Cause indicated by runtime log:

Invalid resource location referencing:

`OneDrive/Desktop/test_trophy/pedesta`

Severity:

⚠️ Non-critical

Observed impact:

No game crash.

Action:

Deferred to V0.7 cleanup unless gameplay impact is discovered earlier.

---

## Cobblemon: Extra Structures

Observed error:

Sprout Tower advancement references an unknown registry item:

`cobblemonextrastructures:bellsprout_statue`

Severity:

⚠️ Non-critical

Observed impact:

No game crash.

Action:

Deferred to V0.7 cleanup unless gameplay impact is discovered earlier.

---

# V0.5 Result

The Pokémon Mechanics integration is considered sufficiently stable to continue development.

Result:

✅ **PASS — INITIAL INTEGRATION**

Release:

`v0.5.0`

More extensive gameplay validation will occur during later balancing, Alpha and full-playthrough testing.

---

# Next Test Phase

## V0.6 — Immersion

Focus:

- Interface
- Music
- Audio
- Visual improvements
- Pokémon interaction
- World atmosphere

Testing continues using the batch-integration and log-analysis workflow.
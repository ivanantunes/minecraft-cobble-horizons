# CobbleHorizons — Testing

Testing history and compatibility notes for CobbleHorizons.

> Primary test environment: Singleplayer  
> Minecraft: 1.21.1  
> Loader: Fabric  
> Cobblemon: 1.7.3

---

# Testing Strategy

CobbleHorizons is currently under active development.

During early development, mods are installed in development batches.

The game is then launched and basic functionality is verified.

If the game:

- launches successfully;
- loads a world;
- keeps the core Cobblemon gameplay functional;
- and does not produce a critical crash;

the development batch is considered provisionally approved.

Warnings and non-critical errors are documented and reviewed during cleanup and stabilization.

---

# v0.1.0 — Foundation

Status: PASSED

Tested:

- Minecraft startup
- Fabric
- Cobblemon
- Starter selection
- World loading
- Basic Pokémon functionality
- Performance mods

Result:

Core environment functional.

---

# v0.2.0 — World & Exploration

Status: PASSED

Tested:

- World generation
- Terralith
- Cobblemon structures
- Maps
- Waystones
- Pokémon structures
- Nests and dens
- Singleplayer gameplay

Result:

World generation and exploration systems functional.

---

# v0.3.0 — Trainers & Battles

Status: PASSED

Tested:

- Trainer structures
- Radical Cobblemon Trainers
- Trainer battles
- Pokémon battles
- Pokémon experience
- Existing world functionality

Result:

Trainer and battle systems functional.

---

# v0.4.0 — Gyms & Progression

Status: PASSED

Tested:

- Gym structures
- Radical Gyms & Structures
- Rad Gyms
- Capture Cap
- Badge system
- RCT badge integration
- Pokémon battles

Result:

Gym and initial progression systems functional.

---

# v0.5.0 — Expanded Pokémon Gameplay

Status: PASSED

Tested:

- Mega Showdown
- Pokémon utilities
- Breeding
- TMs/TRs
- Legendary content
- Legendary monuments
- Decorative content
- Resource packs
- Existing worlds

Result:

Expanded Pokémon gameplay loaded successfully without critical crashes.

---

# v0.6.0 — Immersion & Visuals

Status: PASSED

Tested:

- World startup
- Existing Pokémon
- Environmental audio
- Battle audio
- Battle music
- Cobblemon Intros
- Environmental interactions
- Iris
- Complementary Reimagined
- Entity Model Features
- Entity Texture Features
- Shader rendering

Result:

All primary V0.6 features loaded and operated without a game crash.

---

# Known Non-Critical Issues

The following issues were observed during development but currently do not prevent gameplay.

## Iris / Complementary

An Iris shader exception involving:

`Unknown variable: endFlashIntensity`

was observed in logs.

Complementary Reimagined nevertheless loaded and rendered successfully during gameplay.

Status:

MONITOR

---

## MAmbience

MAmbience reports missing footstep definitions for some blocks from mods including:

- Cobblemon
- Chipped
- Another Furniture

No crash or significant gameplay issue was observed.

Status:

NON-CRITICAL

---

## Cobblemon Extra Structures

A missing/invalid advancement related to:

`bellsprout_statue`

was observed.

No critical gameplay issue was observed.

Status:

MONITOR

---

## Spawn Presets

Some unknown spawn presets have appeared in logs, including:

- water_surface
- freshwater
- underwater
- flowers
- river

No critical crash was associated with these warnings during testing.

Status:

MONITOR

---

# Known Incompatibilities

## Cobblemon Auto Tidy Up PC

Result:

FAILED

Reason:

Caused resource reload failure.

Action:

Removed from CobbleHorizons.

---

## Cobblemon UI

Result:

FAILED

Reason:

Game crashed when opening Pokémon EV/stat information.

Action:

Removed from CobbleHorizons.

---

# Multiplayer

Multiplayer testing is currently outside the development scope.

CobbleHorizons is being developed and validated primarily for singleplayer during the pre-alpha development cycle.

Multiplayer compatibility may be evaluated in a later development phase.

---

## V0.8 — Clean Instance UI Validation

### Boot

- [ ] Título, ícone, wallpaper, logo e barra corretos.
- [ ] Jogo chega ao menu sem crash.

### Main menu

- [ ] Wallpaper e botões personalizados aparecem.
- [ ] Logo vanilla e splash amarelo estão ocultos.
- [ ] Hover, clique e navegação funcionam.
- [ ] Layout permanece legível em GUI Scale 3.

### Internal menus

- [ ] Background e estilos globais aparecem onde compatíveis.
- [ ] Sliders, listas e datasource continuam utilizáveis.
- [ ] Vídeo, áudio, controles e resource packs abrem.

### Gameplay

- [ ] Mundo novo e existente carregam.
- [ ] Captura, batalha e EV/status funcionam.
- [ ] Trainers, ginásios, áudio e shaders funcionam.

### Logs

- [ ] Nenhuma exceção fatal.
- [ ] Nenhum erro de layout ou textura ausente.

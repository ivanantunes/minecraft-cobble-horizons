# CobbleHorizons Changelog

## [Unreleased]

### Repository

- Removed obsolete development MRPack and superseded patch notes.
- Removed unused FancyMenu editor themes and redundant icon sizes.
- Release artifacts are now excluded from the development branch.


- Regenerar o MRPack após o teste limpo.
- Preparar a v0.9.0 Release Candidate.

## [0.8.0] — Configuration & Identity

Status: aguardando validação.

### Added

- FancyMenu, Drippy Loading Screen e Default Options.
- Wallpaper, logo, ícones e texturas de botões.
- Layout dedicado ao menu principal.
- Padrões de vídeo, áudio, idioma e resource packs.

### Fixed

- Caminhos globais dos assets do FancyMenu.
- Estados normal, hover e inativo dos botões.
- Nine-slicing de 8 px.
- Cores globais de texto.
- Ordem de renderização do title screen.

### Validation

- Boot, menu principal e menus internos.
- Mundo, captura, batalha, áudio e shaders.
- Logs sem exceções fatais ou assets ausentes.

---

# Changelog

All notable changes to CobbleHorizons are documented in this file.

---

## [Unreleased]

### Planned

- Balance and cleanup
- Configuration review
- Progression balancing
- Compatibility cleanup

---

## [0.6.0] - 2026-08-10

### Added

- Cobblemon Environment Interactions
- MAmbience
- Ambient Environment
- Sounds
- Cobblemon Intros
- Cobblemon Battle Tracks
- Iris Shaders
- Complementary Shaders - Reimagined
- Entity Model Features (EMF)
- Entity Texture Features (ETF)

### Dependencies

- MRU
- YetAnotherConfigLib (YACL)

### Changed

- Expanded environmental ambience
- Added dynamic environmental sounds
- Added Pokémon battle music
- Added battle music intros
- Added Pokémon environmental interactions
- Added shader support
- Added enhanced entity model support
- Added enhanced entity texture support

### Testing

- Minecraft startup successful
- World loading successful
- Cobblemon gameplay functional
- Environmental audio functional
- Battle audio functional
- Battle music functional
- Iris functional
- Complementary Reimagined functional
- EMF/ETF loaded successfully
- No critical crash observed

### Known Issues

- Iris may log an `endFlashIntensity` shader exception with Complementary Reimagined
- MAmbience reports missing footstep definitions for some modded blocks
- Cobblemon Extra Structures contains an invalid/missing `bellsprout_statue` advancement reference
- Some unknown Cobblemon spawn presets are reported in logs

---

## [0.5.0]

### Added

- Cobblemon: Mega Showdown
- Cobblemon Utility+
- Cobbreeding
- SimpleTMs
- Myths and Legends
- Cobblemon: Legendary Monuments
- Chipped
- Resourceful Lib
- Required dependencies

### Changed

- Expanded Pokémon progression
- Added Mega Evolution support
- Added breeding mechanics
- Added TM/TR mechanics
- Expanded legendary Pokémon content
- Expanded decorative building options

---

## [0.4.0]

### Added

- Capture Cap - RCT Version
- CobbleFurnies
- Radical Gyms & Structures
- Rad Gyms
- Cobblemon Pokemon Badges
- RCT Badges - Cobblemon Pokemon Badges
- Required dependencies

### Changed

- Added gym progression
- Added badge progression
- Added capture progression

---

## [0.3.0]

### Added

- Cobblemon Trainer Structures
- Radical Cobblemon Trainers API
- Radical Cobblemon Trainers
- Fix Cobblemon Pokemon Experience
- Architectury API

### Changed

- Added trainer battles
- Added trainer structures
- Improved Pokémon experience behavior

---

## [0.2.0]

### Added

- Terralith
- Lithostitched
- Cobblemon: Extra Structures
- CobbleStructures
- CobbleDollars
- Another Furniture
- Cobblemon Pokenav
- Cobblemon Repel
- Waystones
- Cobblemon: Nests & Dens
- Cobblemon Integrations
- Required dependencies

### Changed

- Expanded world generation
- Expanded exploration
- Added Pokémon structures
- Added economy systems
- Added fast travel

---

## [0.1.0]

### Added

- Cobblemon
- Fabric API
- Sodium
- Lithium
- ImmediatelyFast
- FerriteCore
- ModernFix
- Jade
- EMI
- Mouse Tweaks
- Xaero's Minimap
- Xaero's World Map
- Cobblemon Pokedex
- Cobblemon UI Tweaks
- Initial dependencies

### Removed

- Cobblemon Auto Tidy Up PC due to resource reload failure
- Cobblemon UI due to crash when accessing Pokémon EV/stat information

### Initial

- CobbleHorizons development environment established
- Minecraft 1.21.1 selected
- Fabric selected
- Cobblemon 1.7.3 selected
# CobbleHorizons Changelog

All notable project changes are documented here.

## [Unreleased]

### Added

- MakeUp Ultra Fast 9.0c as the performance shader profile.
- BSL 8.3 as the cinematic shader profile.
- Faithful 32x for Minecraft 1.21.1 as an optional resource pack.
- A documented plug-and-play performance and controls profile.

### Fixed

- Moved Cobblemon Summary from `M` to `V`, leaving `M` available for Xaero's World Map.
- Moved Iris shortcuts to `F7` (shader selection), `F8` (reload), and `F9` (toggle), preventing collisions with Cobblemon's `R` action.
- Made English (US) the clean-install default language.
- Added an explicit root `options.txt` so Modrinth exports preserve resource-pack defaults.
- Enabled CobbleHorizons Branding, Battle Tracks, and Cobbreeding Pasture Fix by default.
- Updated the FancyMenu title-screen layout to render its custom background above the vanilla panorama.
- Added current FancyMenu background and scroll-layer properties.
- Removed the invalid universal `title_screen` declaration from `customizablemenus.txt`.
- Removed the invalid quoted cloud option that generated a parsing error.

### Changed

- `fundo1` is the official title-screen background.
- The project documentation is now fully maintained in English.
- The title screen uses English labels and hides vanilla title branding and splash text.
- Shaders remain disabled by default for maximum hardware compatibility.
- Faithful 32x is installed but remains optional so the CobbleHorizons branding and Cobblemon assets retain priority.

### Validation

- Version 1.0.1 clean import, English defaults, resource packs, loading screen, and title screen validated on macOS.
- Version 1.0.2 MRPack structure, hashes, nested branding archive, and clean-install defaults validated.

## [0.8.0] — Configuration and Identity

### Added

- FancyMenu, Drippy Loading Screen, and Default Options integration.
- Custom wallpaper, logo, icons, button textures, and loading assets.
- A dedicated title-screen layout and global UI styling.

### Fixed

- Local FancyMenu asset paths.
- Button normal, hover, and inactive states.
- Nine-slice borders and global text colors.

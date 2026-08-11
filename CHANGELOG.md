# CobbleHorizons Changelog

All notable project changes are documented here.

## [Unreleased]

### Fixed

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

### Validation

- Pending one final clean Modrinth import.

## [0.8.0] — Configuration and Identity

### Added

- FancyMenu, Drippy Loading Screen, and Default Options integration.
- Custom wallpaper, logo, icons, button textures, and loading assets.
- A dedicated title-screen layout and global UI styling.

### Fixed

- Local FancyMenu asset paths.
- Button normal, hover, and inactive states.
- Nine-slice borders and global text colors.

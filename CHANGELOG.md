# Changelog

All notable changes to CobbleHorizons are documented here.

## [1.1.0-rc3] — 2026-08-11

### Stable quest migration and menu polish

- Removed JustQuests 0.2.3 after its player mixin prevented Minecraft 1.21.1 from starting.
- Migrated the complete 15-stage Adventure Guide to FTB Quests 2101.1.20.
- Added the matching FTB Library 2101.1.29 and FTB Teams 2101.1.8 dependencies.
- Replaced badge inventory checks with reliable RCT gym-leader milestones for one, three and eight victories.
- Kept Global Packs 21.0.6 because it loads the RCT badge and CobbleHorizons milestone datapacks in every world.
- Added layout-scoped FancyMenu button templates to the title and Options screens.
- Kept global FancyMenu backgrounds and button styles disabled so gameplay and Cobblemon interfaces remain clean.
- Rebuilt and validated the release candidate as `CobbleHorizons-1.1.0-rc3.mrpack`.

## [1.1.0-rc2] — 2026-08-11

### Interface isolation correction

- Restricted the CobbleHorizons wallpaper to the title screen, Options screen and loading screen.
- Removed global FancyMenu backgrounds and button overrides from gameplay and mod interaction screens.
- Added JustQuests 0.2.3 and Global Packs 21.0.6 to the RC2 manifest. JustQuests was removed again in RC3 after startup testing exposed an incompatible mixin.
- Rebuilt the release candidate after the quest interface failed to load in RC1.

## [1.1.0-rc1] — 2026-08-11

### Adventure Guide release candidate

- Added a 15-stage in-game CobbleHorizons campaign, opened with `J`.
- Added guided objectives for Poké Ball crafting, catching, Pokédex research, trainer battles, team building, evolution, healing, gym badges, Mega Evolution, legendary monuments, the Elite Four and Champions.
- Added balanced automatic rewards intended to support progression without replacing exploration or training.
- Added JustQuests 0.2.3 as the lightweight datapack-driven quest interface.
- Added Global Packs 21.0.6 so the Adventure Guide and RCT badge datapacks load automatically in every world.
- Suppressed JustQuests' generic built-in quest set so only the curated CobbleHorizons campaign is presented.
- Added the external Adventure Guide documentation and RC testing checklist.
- Kept Minecraft 1.21.1, Fabric Loader 0.19.3, Cobblemon 1.7.3 and all 1.0.0 gameplay defaults unchanged.

## [1.0.0] — 2026-08-11

### First public release

- Released the complete CobbleHorizons experience for Minecraft 1.21.1, Fabric Loader 0.19.3 and Cobblemon 1.7.3.
- Curated 65 compatible mods covering Pokémon gameplay, progression, exploration, structures, economy, decoration, audio, interface and performance.
- Added a Pokémon-first spawn policy that suppresses world-generated vanilla mobs while preserving villagers, wandering traders, golems, the Ender Dragon and the Wither.
- Added custom CobbleHorizons loading, title-screen, menu, button and resource-pack branding.
- Added three optional shader profiles: MakeUp Ultra Fast 9.0c, Complementary Reimagined r5.8.1 and BSL 8.3.
- Added Faithful 32x as an optional resource pack.
- Enabled CobbleHorizons Branding, Battle Tracks and Cobbreeding Pasture Fix by default.
- Set English (US), balanced video defaults and conflict-free controls for clean installations.
- Added Sodium, Lithium, ImmediatelyFast, FerriteCore and ModernFix with conservative compatibility-first settings.
- Validated MRPack extraction, indexed hashes, macOS installation and the uncompressed nested branding archive.

### Default controls

- Cobblemon Summary: `V`
- Xaero's World Map: `M`
- Iris shader selection: `F7`
- Iris shader reload: `F8`
- Iris shader toggle: `F9`

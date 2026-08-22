# Changelog

All notable changes to CobbleHorizons are documented here.

## [1.2.0] — 2026-08-22

### League progression, identity overhaul, keybind stabilization and long-play balance

#### Progression

- Added the first-party **CobbleHorizons League** RCT series.
- Ordered the League as Brock → Misty → Lt. Surge → Erika → Sabrina → Koga → Blaine → Clair → Lorelei → Bruno → Agatha → Lance → Champion Terry.
- Set the initial player level cap to 15, relative cap to 0 and disabled overleveling.
- Added the designed cap sequence `15 → 27 → 34 → 44 → 59 → 68 → 76 → 81 → 85` as the player advances through the required opponents.
- Added `/function cobblehorizons:progression/migrate_1_2_all_online` as a migration helper for online players/worlds moving to the 1.2 progression series.
- Added League quest nodes through all eight gyms, Elite Four and Champion, followed by the Horizon Elite postgame objective.
- Expanded the QuestZ campaign to **107 active gameplay quests + 1 root advancement**.
- Kept the 12 Species Hunt templates hidden/disabled because species-specific capture filtering is still not reliable enough for the exact Cobblemon 1.7.3 setup.

#### Trainer and world balance

- Prevented the eight Gym Leaders, Elite Four and Champion identities used by CobbleHorizons progression from spawning naturally (`spawnWeightFactor = 0`).
- Kept ordinary RCT trainers available as world encounters.
- Restored natural spawning for **cow, pig, chicken and sheep** so early survival has food, leather, wool and feathers without requiring a village.
- Continued suppressing other world-generated vanilla mobs through Mob Filter while preserving villagers, wandering traders, iron/snow golems, Ender Dragon and Wither.
- Reduced reward-chain side effects from legacy `inventory_changed` quests by converting the 17 main reward-sink quests to CobbleDollars, preventing multi-step item reward cascades.

#### Controls

- Added proper Default Options key defaults through `config/defaultoptions/keybindings.txt` instead of relying on key lines in `options.txt`.
- Resolved gameplay key conflicts between Cobblemon, Inmis, Xaero, Iris, Jade and utility/debug bindings.
- Kept core gameplay keys compact (`R`, `V`, `N`, `K`, `B`, `H`, `M`, `G`, `Y`, `Z`) and moved configuration functions to `F6–F10`.
- Unbound unnecessary Cobblemon debug, FancyMenu/Drippy development, Iris wireframe and secondary Xaero shortcuts.

#### Resource packs, UI and music

- Merged the old `CobbleHorizons-Branding.zip` and `CobbleHorizons-Identity.zip` into one first-party `CobbleHorizons.zip` resource pack.
- Removed Faithful 32x from the release.
- Added Cobblemon Interface v1.6.0 and Cobblemon Interface: Modded v1.9.4 through official Modrinth distribution.
- Fixed Default Options native configuration location to `config/defaultoptions/options.txt`.
- Configured Global Packs to require the intended CobbleHorizons/interface/resource-pack stack.
- Expanded FancyMenu world-loading customization to cover the generic message/loading flow in addition to the existing loading layouts.
- Added six original CobbleHorizons music tracks: Horizon Menu, Routes and Fields, Quiet Town, Starlit Research, Caves and Ruins, and Beyond the Horizon.
- Preserved Cobblemon Battle Tracks for battle music.

#### Validation

- Kept Minecraft 1.21.1, Fabric Loader 0.19.3, Cobblemon 1.7.3 and Java 21 as the release baseline.
- Validated MRPack ZIP integrity after each correction pass.
- Preserved the established progression/quest source except for the explicit 1.2 League, spawn and reward-balance changes described above.

## [1.1.0] — 2026-08-17

### QuestZ stabilization, progression gating and final release packaging

- Replaced the temporary Boundless quest implementation with QuestZ 1.0.1 and a first-party advancement-based CobbleHorizons datapack.
- Finalized 93 active gameplay quests plus the CobbleHorizons root entry, all player-facing content in English.
- Added real prerequisite predicates to active non-root quests so later objectives cannot complete before their intended progression point.
- Standardized the opening progression as **Choose Your Partner → Red Apricorn Research (8) → A New Friend**.
- Audited capture, evolution, battle, inventory and reward criteria for invalid JSON, missing parents, broken reward functions and progression cycles.
- Hid and disabled 12 Species Hunt templates after species-specific capture filtering proved unreliable and could complete multiple future quests from a generic capture.
- Removed the duplicate title-screen logo overlay while preserving the logo already present in the menu artwork.
- Replaced the vanilla yellow rotating splash text with an invisible branding entry.
- Kept the custom FancyMenu button layouts, title screen, loading screen and CobbleHorizons Branding presentation.
- Rebuilt the release using the import-safe MRPack packaging approach after a previous rebuild triggered `Cannot read properties of undefined (reading 'then')` in the Modrinth App.
- Updated repository documentation to reflect QuestZ, the current quest count, the `L` quest key, source-control policy and final 1.1.0 release state.


## [1.1.0-rc5] — 2026-08-12

### Stable inventory, English campaign and scoped button theme

- Disabled Boundless' broken inventory widget integration on Fabric 1.21.1, preventing the `addRenderableWidget` reflection crash when opening the player inventory.
- Kept the standalone Quest Book available through the `[` key and the supplied Quest Book item.
- Rewrote all 66 quests and all six category names in English.
- Replaced the last two vanilla starter objectives with a Pokédex and Healing Machine progression step; every quest objective is now Pokémon/Cobblemon-focused.
- Made dependent quests visible while keeping them locked until their prerequisites are complete.
- Corrected the title-screen render order so custom button textures render above the vanilla button background.
- Hardened the screen-local Options button template without applying it to gameplay or Cobblemon interfaces.
- Added a reproducible campaign normalization tool and rebuilt the release as `CobbleHorizons-1.1.0-rc5.mrpack`.

## [1.1.0-rc4] — 2026-08-11

### Modrinth-native quest campaign and title-screen cleanup

- Added Inmis 2.8.1, a Fabric backpack mod with `B` as the default quick-open key.

- Removed FTB Quests, FTB Library and FTB Teams because those downloads cannot be published as a fully Modrinth-native MRPack.
- Added Boundless: Quests `1.21.1-fabric-10`, distributed from Modrinth for Fabric 1.21.1.
- Rebuilt the Adventure Guide as an enabled Boundless quest pack with 66 linked Pokémon quests across easy, medium, difficult and hardcore progression categories.
- Disabled Boundless' generic built-in quest set; only the CobbleHorizons campaign is shown by default.
- Updated the title and Options layouts to apply their button design at layout scope, preserving unmodified Cobblemon interfaces.
- Disabled the optional ModernFix title-screen branding line to remove the unwanted yellow message.
- Rebuilt the release candidate as `CobbleHorizons-1.1.0-rc4.mrpack`.

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

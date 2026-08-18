# Troubleshooting

## Start with a clean instance

Most release-validation problems come from updating an existing profile in place.

Import the latest MRPack as a new Modrinth instance before reporting a default-setting or interface issue.

## The title screen is not customized

Confirm these files exist in the installed instance:

- `config/fancymenu/customization/cobblehorizons_title_screen.txt`
- `config/fancymenu/assets/menu_background.png`
- `resourcepacks/CobbleHorizons-Branding.zip`

Do not edit FancyMenu layouts while Minecraft is running.

## Two logos appear on the title screen

CobbleHorizons 1.1.0 no longer renders the old extra logo element above the buttons.

If two logos are visible, the instance is probably using an older FancyMenu layout or copied configuration. Import the current MRPack into a fresh instance.

## The yellow Minecraft splash text is visible

The active CobbleHorizons Branding resource pack replaces the vanilla yellow splash list with an invisible entry.

Confirm that **CobbleHorizons Branding** is enabled and has higher priority than packs that replace the same title assets.

## Background appears behind gameplay interfaces

The custom wallpaper is intended for the title/Options presentation and loading flow, not general gameplay interfaces.

If it appears behind unrelated mod screens, replace the old FancyMenu configuration with the current release configuration by using a fresh import.

## Resource packs are not enabled

A clean instance should enable:

- CobbleHorizons Branding;
- Cobblemon Battle Tracks;
- Cobbreeding Pasture Fix.

Faithful 32x is intentionally disabled by default.

Existing profiles can retain their previous resource-pack order.

## The quest screen does not open

Press **`L`** while inside a world.

Confirm:

- QuestZ 1.0.1 is installed;
- `L` has not been rebound;
- the player is fully loaded into a world.

The current release does not use Boundless, FTB Quests or JustQuests.

## The campaign is missing

Confirm this folder exists:

`datapacks/CobbleHorizons-QuestZ`

Also confirm Global Packs is enabled and `config/global_packs.toml` still requires the bundled `datapacks/` directory.

Use `/datapack list` in a world to inspect loaded datapacks.

## A later quest completed too early

CobbleHorizons 1.1.0 adds real prerequisite predicates to every active non-root quest.

If an old test world already contains advancement progress from a previous RC, those completions remain stored in the world.

Validate the problem in a fresh world before reporting it.

## Species Hunt quests are missing

This is intentional in 1.1.0.

The 12 species-specific hunt templates are hidden and disabled because the earlier species filter could behave as a generic capture condition and complete several future quests from one Pokémon capture.

They will remain disabled until a species-specific criterion is validated safely.

## Modrinth import error: `Cannot read properties of undefined (reading 'then')`

Do not manually unzip/re-zip the MRPack.

1. Delete the failed partial instance.
2. Re-download the official MRPack.
3. Restart/update the Modrinth App.
4. Import the official file again.

The final packaging uses the import-safe archive approach validated during the RC12 fix.

## Vanilla mobs still exist

The pack prevents new world-generated vanilla mobs.

Entities already saved in an older world remain present. Villagers, wandering traders, golems, the Ender Dragon and the Wither are intentional exceptions.

## Low frame rate

1. Confirm shaders are disabled with `F9`.
2. Keep render distance at 12 chunks or reduce it to 10.
3. Try MakeUp Ultra Fast before Complementary or BSL.
4. Allocate 6 GB of memory.
5. Update graphics drivers and avoid unnecessary overlays.

## macOS `unexpected BufError`

Use the official release MRPack.

Avoid recompressing nested pack archives manually.

## Crash or severe error

Do not remove random mods from the main instance.

1. Reproduce the issue in a copy or clean instance.
2. Save the exact action that triggered it.
3. Upload `latest.log` to [mclo.gs](https://mclo.gs/).
4. Include operating system, hardware, pack version and screenshots.

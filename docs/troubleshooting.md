# Troubleshooting

## Start with a clean instance

Most default-setting problems come from updating an existing profile. Import the current MRPack as a new Modrinth instance before reporting a problem.

## The title screen is not customized

Confirm these files exist:

- `config/fancymenu/customization/cobblehorizons_title_screen.txt`
- `config/fancymenu/assets/menu_background.png`
- `resourcepacks/CobbleHorizons-Branding.zip`

Do not edit FancyMenu layouts while Minecraft is running.

## Background appears behind gameplay interfaces

RC1 incorrectly applied the FancyMenu wallpaper globally. RC5 restricts it and the custom button theme to the title screen and main Options screen. The loading wallpaper remains controlled by Drippy Loading Screen. Import RC5 into a clean instance; copying only `options.txt` does not replace FancyMenu layouts.

## Resource packs are not enabled

A clean instance should enable CobbleHorizons Branding, Battle Tracks and Cobbreeding Pasture Fix. Existing profiles keep their previous `options.txt`; import a new instance to verify release defaults.

Faithful 32x is intentionally disabled by default.

## The Adventure Guide does not open

Press `[` in a world, not from the title screen. Confirm that **Boundless: Quests** is installed and that no personal key binding has replaced `[`. The Quest Book item is also available. The inventory-side button is intentionally disabled in RC5 to prevent Boundless' `addRenderableWidget` crash on Fabric 1.21.1.

## The campaign is missing or a quest did not update

Confirm `config/boundless/questpacks/cobblehorizons-adventure/pack.mcmeta` exists. Run `/datapack list` to confirm the CobbleHorizons milestone and RCT badge packs are enabled.

RC5 shows all 66 quests immediately. Incomplete dependent quests remain visible but locked. A fresh world remains the recommended RC validation environment.

## Vanilla mobs still exist

The pack prevents new world-generated vanilla mobs. Entities already saved in an older world remain present. Villagers, wandering traders, golems, the Ender Dragon and the Wither are intentional exceptions.

## Low frame rate

1. Confirm shaders are disabled with `F9`.
2. Keep render distance at 12 chunks or reduce it to 10.
3. Try MakeUp Ultra Fast before Complementary or BSL.
4. Allocate 6 GB of memory.
5. Update graphics drivers and avoid running multiple overlays.

## macOS `unexpected BufError`

Use the official release MRPack. It packages the internal branding archive without recompression specifically to avoid this extraction failure.

## Crash or severe error

Do not remove random mods from the main instance.

1. Reproduce the issue in a copy or clean instance.
2. Save the exact action that triggered it.
3. Upload `latest.log` to [mclo.gs](https://mclo.gs/).
4. Include operating system, hardware, pack version and screenshots.

# Troubleshooting

## Start with a clean instance

Most default-setting problems come from updating an existing profile. Import the current MRPack as a new Modrinth instance before reporting a problem.

## The title screen is not customized

Confirm these files exist:

- `config/fancymenu/customization/cobblehorizons_title_screen.txt`
- `config/fancymenu/assets/menu_background.png`
- `resourcepacks/CobbleHorizons-Branding.zip`

Do not edit FancyMenu layouts while Minecraft is running.

## Resource packs are not enabled

A clean instance should enable CobbleHorizons Branding, Battle Tracks and Cobbreeding Pasture Fix. Existing profiles keep their previous `options.txt`; import a new instance to verify release defaults.

Faithful 32x is intentionally disabled by default.

## The Adventure Guide does not open

Press `J` in a world, not from the title screen. Confirm `JustQuests-fabric-1.21.1-0.2.3.jar` is installed and that no personal key binding has replaced `J`.

## The campaign is missing or a quest did not update

Confirm `datapacks/CobbleHorizons-Adventure-Guide.zip` exists and that Global Packs is installed. The guide is designed for a fresh world and each stage must be accepted before its advancement is earned.

For badge collection objectives, drop the relevant badges and pick them up again after accepting the quest. Run `/datapack list` to confirm the CobbleHorizons guide and RCT Badges packs are enabled.

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

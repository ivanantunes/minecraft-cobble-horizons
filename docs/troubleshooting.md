# Troubleshooting — CobbleHorizons 1.2.0

## Start with a clean instance

Default-setting, keybind, UI and resource-pack reports should first be reproduced in a newly imported Modrinth instance.

An older profile may preserve user settings and previous mod defaults.

## Resource packs are not enabled / visuals look old

Confirm:

- `resourcepacks/CobbleHorizons.zip` exists;
- Cobblemon Interface and Cobblemon Interface: Modded were downloaded by the MRPack;
- `config/global_packs.toml` exists;
- the instance is a fresh import.

The old Branding/Identity split and Faithful 32x are not part of 1.2.0.

## The title screen or loading flow is vanilla

Confirm FancyMenu/Drippy configuration from the release is present.

CobbleHorizons customizes title/options/pause/multiplayer/create-world flows and covers the relevant world-loading message/loading screens. A copied older `config/fancymenu/` directory can override the corrected 1.2 layouts.

Use a fresh instance when validating this.

## Music is missing

Confirm:

- Music volume is above zero;
- `CobbleHorizons.zip` is loaded;
- Battle Tracks is available for battle music;
- the required resource packs are being loaded by Global Packs.

The first-party pack contains six CobbleHorizons music tracks.

## Controls are conflicting again

The 1.2 key map is shipped through:

`config/defaultoptions/keybindings.txt`

Do not test key defaults by copying an old root `options.txt` into a new instance.

If a key was manually changed in the current profile, Default Options may preserve that user customization. Validate a clean import before reporting a release conflict.

On macOS, function keys may require `Fn`; this is not itself a Minecraft duplicate binding.

## Quest screen does not open

Press **`L`** in a world.

Confirm QuestZ 1.0.1 is installed and `L` has not been manually rebound.

## Campaign is missing

Confirm the first-party datapack exists:

`datapacks/CobbleHorizons-QuestZ`

Global Packs should load the packaged datapacks. `/datapack list` can help diagnose a world where the pack is missing.

## League progression is missing or wrong

Confirm:

`datapacks/CobbleHorizons-Progression`

and verify RCT's initial series is `cobblehorizons`.

For upgraded worlds, back up first and use the bundled migration helper if required:

`/function cobblehorizons:progression/migrate_1_2_all_online`

## Brock / Gym Leaders spawn randomly in the overworld

The CobbleHorizons League trainer overrides set the League bosses' natural spawn weight to zero.

If a boss is already present in an upgraded world, the configuration does not automatically delete an entity that had already spawned. Test new chunks / a fresh world before reporting the current release as broken.

## No cows, pigs, chickens or sheep spawn

Version 1.2.0 explicitly allows these four core passive animals:

- cow;
- pig;
- chicken;
- sheep.

If none appear in a fresh world after normal exploration, confirm `config/mobfilter.json5` is the 1.2 version and has the four entities in the first `ALLOW_SPAWN` rule.

Other vanilla world-generated mobs are intentionally suppressed.

## Rare Candy / Exp Candy / medicine seems to appear after looting

Cobblemon can inject its own loot into structures and QuestZ inventory objectives can also complete when an item enters the player's inventory.

Version 1.2.0 breaks the main multi-step quest reward cascades, but a single inventory-based quest may still complete when its target item is legitimately obtained.

When reporting suspicious loot:

1. note whether the item was visibly inside the chest before taking it;
2. note any quest-completion notification at the same time;
3. provide the structure type and screenshot if possible.

This distinction tells us whether the source is a loot table or a quest reward.

## Species Hunt quests are missing

Intentional. The 12 species-specific templates remain disabled until reliable species filtering is validated for Cobblemon 1.7.3.

## Old quest completed immediately

Quest progress is stored in world advancement data. Old test worlds can retain completion state from earlier builds.

Reproduce in a fresh world before filing a progression bug.

## Low frame rate

1. Disable shaders with `F9`.
2. Keep render distance at 12 or lower it.
3. Keep simulation distance at 8 or lower it.
4. Allocate 6 GB RAM.
5. Try MakeUp Ultra Fast before heavier shaders.
6. Check for repeated errors in `latest.log`.

## Modrinth import error

Do not manually unzip and re-zip the MRPack unless you are intentionally rebuilding it and can validate the resulting archive.

If an official artifact fails:

1. remove the failed partial instance;
2. re-download the release;
3. restart/update Modrinth App;
4. import again as a new instance;
5. verify the release checksum when one is supplied.

## Crash or severe error

1. Reproduce in a copy or clean instance.
2. Record the exact action that triggered the issue.
3. Upload `latest.log` to [mclo.gs](https://mclo.gs/).
4. Include OS, hardware, pack version and reproduction steps.

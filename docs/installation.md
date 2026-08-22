# Installation and Updates — CobbleHorizons 1.2.0

## Requirements

- Modrinth App (recommended)
- Java 21
- 6 GB of allocated memory
- Minecraft: Java Edition

Use 8 GB only when heavier shader profiles or unusually long sessions justify it. More memory is not automatically better.

## Fresh installation

1. Open the CobbleHorizons GitHub **Releases** page.
2. Download the current `CobbleHorizons-*.mrpack`.
3. Import it into the Modrinth App as a **new instance**.
4. Allocate 6 GB RAM.
5. Confirm Java 21 is selected.
6. Start the game.

A fresh instance is the supported baseline for validating defaults.

## Updating from an older release

Worlds are not stored inside the MRPack.

1. Back up the old instance, especially `saves/`.
2. Import the new MRPack as a separate instance.
3. Start the new instance once and reach the title screen.
4. Close Minecraft.
5. Copy only the worlds you want to keep into the new instance.
6. Keep the new instance's `config`, mods and packaged defaults.

Do not copy the old root `options.txt` into the new instance when validating a release.

## Default Options in 1.2.0

The correct packaged defaults are:

- `config/defaultoptions/options.txt` — regular client options;
- `config/defaultoptions/keybindings.txt` — curated key mappings.

The old `config/defaultoptions/extra/options.txt` layout is no longer used for Minecraft's native `options.txt` defaults.

`defaultoptions.journal.json` is runtime state and must **not** be distributed in the source or release overrides.

## Resource packs

Global Packs requires the release's interface/identity stack so a clean instance does not depend only on a pre-existing personal `options.txt`.

The 1.2.0 release includes:

- first-party `CobbleHorizons.zip`;
- Cobblemon Battle Tracks;
- Cobblemon Interface v1.6.0;
- Cobblemon Interface: Modded v1.9.4;
- Cobbreeding's built-in Pasture Fix resources.

Faithful 32x was removed from the 1.2.0 release.

## Shaders

Shaders are optional.

| Key | Action |
|---|---|
| `F7` | Open shader selection |
| `F8` | Reload shaders |
| `F9` | Toggle shaders |

Bundled profiles:

- MakeUp Ultra Fast 9.0c;
- Complementary Reimagined r5.8.1;
- BSL 8.3.

On macOS, the top-row function keys may require `Fn` depending on system keyboard settings.

## Updating worlds from pre-1.2 progression

The 1.2.0 release uses the `cobblehorizons` RCT series.

For an existing world where players need to be moved onto that series, the pack includes:

`/function cobblehorizons:progression/migrate_1_2_all_online`

Back up the world before migration. A fresh world remains the preferred validation environment.

## Exporting a release from Modrinth App

When exporting the project source/test instance, include only content that belongs in the release. Do not carry runtime state into the MRPack.

Common folders that belong in the export when they contain project content:

- `config/`
- `datapacks/`
- `resourcepacks/`
- `shaderpacks/`

The Modrinth App should handle normally installed mods through the manifest. Include raw `mods/` only when there are manually installed files that cannot be represented by the manifest and you have permission to redistribute them.

Do **not** export runtime/personal state such as:

- `saves/`
- `logs/`
- `crash-reports/`
- `xaero/`
- `showdown/`
- `fancymenu_data/`
- `defaultoptions.journal.json`
- personal root `options.txt`
- `usercache.json`
- local caches/download folders.

## macOS notes

CobbleHorizons has been tested on both Windows and macOS during the 1.2 cycle.

If a function key appears not to work on macOS, test `Fn + F-key` or enable standard F1/F2/etc. behavior in macOS keyboard settings before changing the modpack keybind.

If a fresh instance behaves differently from an upgraded instance, treat the fresh instance as the release baseline and report both results.

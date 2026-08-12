# Installation and Updates

## Requirements

- Modrinth App
- Java 21
- 6 GB of allocated memory
- A legitimate Minecraft: Java Edition account

Use 8 GB when running BSL, high shader presets or long sessions. Allocating substantially more memory is not recommended.

## Fresh installation

1. Download [CobbleHorizons 1.1.0 RC4](../releases/CobbleHorizons-1.1.0-rc4.mrpack).
2. Open the file with the Modrinth App.
3. Confirm the new instance name and start the import.
4. Open the instance settings and allocate 6 GB of memory.
5. Start the game.

A fresh import automatically applies English (US), the official resource-pack order, balanced graphics, curated controls, the in-game Adventure Guide and disabled-by-default shaders.

## Updating

Worlds are not stored inside the MRPack.

1. Back up the `saves` folder from your current instance.
2. Import the new MRPack as a separate instance.
3. Start it once and reach the title screen.
4. Close the game and copy only your backed-up worlds into the new instance.
5. Keep the new instance's `config`, `options.txt`, mods and packs.

Do not copy an old `options.txt` when testing a release because it overrides the official defaults.

## Visual profiles

Press `F7` to open Iris shader selection.

| Profile | Recommendation |
|---|---|
| MakeUp Ultra Fast 9.0c | Integrated graphics and lower-end systems |
| Complementary Reimagined r5.8.1 | Recommended balanced profile |
| BSL 8.3 | Stronger GPUs and screenshots |

Faithful 32x is installed but disabled by default. If enabled, keep CobbleHorizons Branding above it in the resource-pack list.

## macOS installation note

The official MRPack stores the internal CobbleHorizons Branding ZIP without recompression to avoid the Modrinth App `unexpected BufError` extraction failure previously observed on macOS.

## Verifying the download

SHA-256:

`72fb88e5017c4eafdfa25c75b4705cb9a7ed9d3ccd7abe334447a4e91fa40b42`

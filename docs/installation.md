# Installation and Updates

## Requirements

- Modrinth App
- Java 21
- 6 GB of allocated memory
- A legitimate Minecraft: Java Edition account

Use 8 GB only when needed for heavier shader presets or unusually long sessions. Allocating substantially more memory is normally unnecessary.

## Fresh installation

1. Open the CobbleHorizons GitHub **Releases** page.
2. Download the latest `CobbleHorizons-*.mrpack`.
3. Open the file with the Modrinth App.
4. Import it as a **new instance**.
5. Allocate 6 GB of memory.
6. Start the game.

A fresh import applies English (US), the tested resource-pack order, balanced graphics, curated controls, QuestZ progression and disabled-by-default shaders.

## Updating

Worlds are not stored inside the MRPack.

1. Back up the `saves` folder from your current instance.
2. Import the new MRPack as a separate instance.
3. Start it once and reach the title screen.
4. Close Minecraft.
5. Copy only the worlds you want to keep into the new instance.
6. Keep the new instance's mods, config and bundled defaults.

Do not copy an old root `options.txt` when validating a release. CobbleHorizons ships its official client defaults through Default Options.

### Quest update note

QuestZ progress is stored in each world's advancement data. When validating changes to the quest tree, a fresh world is strongly recommended.

An old world can preserve advancement completions from previous release candidates.

## Visual profiles

Press `F7` to open Iris shader selection.

| Profile | Recommendation |
|---|---|
| MakeUp Ultra Fast 9.0c | Integrated graphics and lower-end systems |
| Complementary Reimagined r5.8.1 | Recommended balanced profile |
| BSL 8.3 | Stronger GPUs and screenshots |

Shaders are disabled on first launch.

Faithful 32x is installed by the release but disabled by default. If enabled, keep CobbleHorizons Branding at higher priority.

## Resource-pack defaults

The tested active stack includes:

1. CobbleHorizons Branding
2. Cobblemon Battle Tracks
3. Cobbreeding Pasture Fix
4. Fabric resources
5. Vanilla resources

Faithful 32x remains optional.

## macOS installation note

CobbleHorizons previously encountered a Modrinth App extraction failure involving nested ZIP content (`unexpected BufError`).

Use the official release MRPack rather than manually rebuilding or recompressing the pack if testing on macOS.

## Modrinth import error

A previous rebuild produced:

`Cannot read properties of undefined (reading 'then')`

The working release packaging was rebuilt using the known-good MRPack structure instead of regenerating the archive layout from scratch.

If this error appears with an official release:

1. delete the failed partial instance;
2. re-download the MRPack;
3. update/restart the Modrinth App;
4. import the official file again.

Do not unzip and re-zip the MRPack manually.

## Verifying CobbleHorizons 1.1.0

SHA-256 of the 1.1.0 MRPack included in the source archive used for this documentation update:

`22607851083c015ce5f6beea040269a9f8840ad1aa49094ecdbde77ec6546aa4`

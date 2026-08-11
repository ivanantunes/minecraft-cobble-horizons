# Installation and Distribution

## Requirements

- Modrinth App
- Minecraft 1.21.1
- Java 21
- 6–8 GB of memory allocated to the instance

## Development update

1. Download the repository's `master` branch.
2. Close Minecraft.
3. Open the Modrinth instance folder.
4. Copy `config`, `resourcepacks`, `shaderpacks`, and the root `options.txt` into the instance.
5. Replace existing files when prompted.
6. Start the game without shaders for the first validation.
7. Complete [testing.md](testing.md).

The root `options.txt` is required for export builds. It guarantees the default language and resource-pack selection even when the launcher creates the file before Default Options runs.

## Exporting an MRPack

1. Confirm the updated instance passes the UI smoke test.
2. Choose **Export modpack** in the Modrinth instance menu.
3. Include `config`, `mods`, `resourcepacks`, `shaderpacks`, `datapacks`, and `options.txt`.
4. Exclude worlds, logs, crash reports, screenshots, caches, and account data.
5. Import the exported MRPack into a new instance before publishing it.

## Updating an existing installation

Back up worlds before replacing an instance. Personal controls and video settings may be preserved separately, but release validation must always use the distributed `options.txt`.

## Repository policy

Generated MRPack files are release artifacts. They are attached only to validated releases and are not kept in the development branch.

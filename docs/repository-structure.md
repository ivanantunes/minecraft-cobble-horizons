# Repository Structure

The CobbleHorizons Git repository is the **source of the modpack**, not a mirror of every third-party download.

## Tracked source

```text
CobbleHorizons/
├── config/                         # Curated mod and client defaults
├── datapacks/
│   └── CobbleHorizons-QuestZ/      # First-party quest datapack
├── resourcepacks/
│   └── CobbleHorizons-Branding.zip # First-party branding pack
├── docs/                           # Project documentation
├── imgs/                           # README/project images
├── README.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE.md
├── .gitignore
└── icon.png
```

## Do not commit third-party binaries

The source repository should not contain:

- mod `.jar` files;
- third-party datapack `.zip` files;
- third-party resource-pack `.zip` files;
- shader archives;
- generated `.mrpack` files;
- worlds, logs, screenshots, crash reports or personal client state.

Examples intentionally excluded from source control:

- `RCT-Badges-CobblemonPokemonBadges-0.15+1.1.2.zip`
- `Battle Tracks v1.2.zip`
- `Faithful 32x - 1.21.1.zip`

These are release dependencies and are referenced by the MRPack manifest.

## First-party archive exception

`resourcepacks/CobbleHorizons-Branding.zip` is authored for CobbleHorizons and is therefore allowed in the repository.

A future build pipeline may move this to an unpacked source directory and generate the ZIP automatically.

## Releases

Generated `.mrpack` files belong on **GitHub Releases**, not in normal Git history.

This keeps repository history small and makes source changes reviewable.

## Default client options

Do not commit a personal root-level `options.txt`.

The official CobbleHorizons defaults live at:

`config/defaultoptions/extra/options.txt`

That file is part of the modpack source because Default Options applies it when a fresh instance is created.

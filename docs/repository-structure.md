# Repository Structure — CobbleHorizons 1.2.0

The CobbleHorizons Git repository is the **source/configuration of the modpack**, not a mirror of every third-party download.

## Recommended tracked layout

```text
CobbleHorizons/
├── config/                              # Curated mod/client defaults
│   └── defaultoptions/
│       ├── options.txt                  # Native Minecraft defaults
│       └── keybindings.txt              # Curated key mappings
├── datapacks/
│   ├── CobbleHorizons-QuestZ/           # First-party quest campaign
│   └── CobbleHorizons-Progression/      # First-party RCT League overrides
├── resourcepacks/
│   └── CobbleHorizons.zip               # First-party identity/music/UI pack
├── docs/
├── imgs/
├── README.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── CREDITS.md
├── LICENSE.md
├── .gitignore
└── icon.png
```

The exact repository may include additional first-party scripts/assets, but the same source-control rules apply.

## Track

- curated configuration;
- first-party datapacks;
- first-party resource-pack assets/archive;
- documentation;
- project-owned images/branding;
- validation/build scripts.

## Do not commit third-party binaries

Do not store these in normal Git history:

- `mods/*.jar`;
- third-party datapack ZIPs;
- third-party resource-pack ZIPs;
- shader archives;
- generated `.mrpack` files.

The MRPack manifest should reference third-party content from its proper distribution source.

## Runtime files to exclude

Do not commit:

- `saves/`;
- `logs/`;
- `crash-reports/`;
- `screenshots/`;
- `downloads/`;
- `xaero/`;
- `showdown/`;
- `fancymenu_data/`;
- `moddata/`;
- root `options.txt`;
- `defaultoptions.journal.json`;
- `usercache.json`;
- personal launcher/runtime files.

## Default Options

The project-owned defaults are now correctly stored at:

```text
config/defaultoptions/options.txt
config/defaultoptions/keybindings.txt
```

Do not replace this with a tracked root-level `options.txt`.

`config/defaultoptions/extra/` should only be used for extra third-party configuration files that Default Options needs to copy into the instance root; it is not the location for Minecraft's native options defaults.

## First-party resource pack

Version 1.2.0 uses one unified first-party archive:

`resourcepacks/CobbleHorizons.zip`

The old `CobbleHorizons-Branding.zip` and `CobbleHorizons-Identity.zip` should not be present in the 1.2 source tree.

## GitHub Releases

Put generated `.mrpack` artifacts and optional checksum files on **GitHub Releases**, not in normal source commits.

Recommended release assets:

- `CobbleHorizons-1.2.0.mrpack`
- `CobbleHorizons-1.2.0.sha256.txt` (optional but useful)

This keeps Git history small and reviewable.

# CobbleHorizons 1.3.0-alpha.1 — compatibility snapshot

This document separates **metadata verification** from **Minecraft runtime testing**.

## Pinned baseline

- Published source: [GitHub v1.2.0](https://github.com/ivanantunes/minecraft-cobble-horizons/releases/tag/v1.2.0)
- Release archive SHA-256: `fccfeb290946191c30f6c5e2783fc90e3564e04b36d3794d8c666d73ce57a40a`
- Minecraft `1.21.1`, Fabric Loader `0.19.3`, Java `21`
- Cobblemon `1.7.3`, Architectury `13.0.11` (as listed in `docs/mod-list.md`)
- 75 Modrinth file dependencies in the published v1.2.0 manifest
- The 1.3 alpha builder carries those original manifest entries forward unchanged

## New candidate: Cobblemon Outbreaks 1.1.2

- Modrinth: https://modrinth.com/mod/cobblemon-outbreaks/version/Rlt9c9kz
- Project ID: `nxE2RfXE`; version ID: `Rlt9c9kz`
- Official Fabric JAR: `cobblemon_outbreaks-fabric-1.1.2.jar`
- Official published version date: 2026-04-05
- Minecraft `1.21.1`; Fabric
- Modrinth declared required project IDs: `P7dR8mSH`, `MdwFAVRL`;
  both are present in the 1.2 MRPack manifest
- The verified JAR contains `fabric.mod.json` identifying the mod as
  `cobblemon_outbreaks` version `1.1.2`, environment `*`.
- Exact JAR file size, SHA-512 and SHA-1 matched Modrinth's version metadata;
  JAR ZIP CRC checks passed.

Actual `fabric.mod.json` declared requirements:

| Dependency | Required | Current pack |
|---|---|---|
| Minecraft | `~1.21.1` | `1.21.1` |
| Fabric Loader | `>=0.17.3` | `0.19.3` |
| Java | `>=21` | `21` |
| Architectury API | `>=13.0.8` | `13.0.11` |
| Fabric API | Any compatible version | Included |
| Cobblemon | `>=1.6.0` | `1.7.3` |

All these checks are **static**. They do not prove that Outbreaks behaves
properly alongside Nests & Dens, Legendary Monuments, Myths and Legends,
Mega Showdown, Mob Filter or Radical Gyms. An in-game regression pass is
mandatory before promoting the release.

The 1.3 alpha's manifest adds the official Modrinth JAR URL and hashes,
**not a bundled third-party JAR**, bringing the total to 76 file dependencies.

## Optional Cobblemon 1.8.4 migration

Cobblemon `1.8.4` exists for Minecraft `1.21.1` / Fabric but is **not in
this alpha**. The following require a separate migration compatibility test,
including actual JAR declared dependencies and gameplay trials:

- Radical Cobblemon Trainers API, Radical Cobblemon Trainers, Rad Gyms,
  Radical Gyms & Structures and RCT Capture Cap (League series, level caps)
- Mega Showdown, Legendary Monuments, Myths and Legends
- Cobbreeding, SimpleTMs (review native TM overlap)
- QuestZ triggers and all advancement criteria and rewards
- Cobblemon Environment Interactions, Cobblemon Intros, and CobbleNav

No changes to the Cobblemon base version should be made on the 1.3 stable
branch unless the full table is verified and saved-world migration is tested.

## Evidence and reproducibility

- `scripts/resolve_modrinth_addon.py` reads the Modrinth API and checks
  required project dependencies against the pinned v1.2.0 manifest.
- `scripts/inspect_mod_jar.py` downloads the exact candidate JAR only for
  verifying its hashes, metadata, and ZIP integrity.
- `scripts/build_alpha_mrpack.py` regenerates a 1.3.0-alpha.1 candidate with
  verified `fileSize`, `sha512`, `sha1` and official Modrinth download.
- `.github/workflows/build-alpha.yml` uploads a **test-only** MRPack as
  a GitHub Actions artifact; it does not publish to Modrinth.

**Status:** static metadata/package checks pass; runtime testing pending.

# CobbleHorizons experimental migration to Cobblemon 1.8.4

Status: **test only — do not merge into stable 1.3.0 or publish on Modrinth**.

The user-exported `CobbleHorizons 1.3.0 Alpha 1.0.0.mrpack` was
analyzed on 2026-11-12. Its Modrinth index contains 76 file entries
(69 mods, one external datapack, three resource packs and three shaders).
It carries Cobblemon 1.8.4, many newly updated sidemods, but still has
Fabric Loader 0.19.3.

## Confirmed metadata incompatibilities

1. `Cobblemon Nests & Dens 1.3.3` declares
   `cobblemon: >=1.7.3 <1.8.0`, which rejects installed Cobblemon 1.8.4.
   Published 1.3.3 is the most recent version located; no 1.8-compatible
   Nests & Dens version is verified.
2. `Fabric Language Kotlin 1.14.2+kotlin.2.4.21` declares
   `fabricloader: >=0.19.5`, whereas the uploaded MRPack declares
   `fabric-loader: 0.19.3`.

A GitHub Actions audit of all 69 Modrinth versions on the uploaded
manifest found all 69 versions and **zero missing Modrinth project
dependencies**. It downloaded and SHA-512-verified supported JARs,
inspecting `fabric.mod.json` where possible. The Mega Showdown
`fabric.mod.json` could not be parsed by the standard Python JSON
parser (control-character issue) and requires further review; this
does **not** prove its JAR is broken under Fabric's parser.

### Minimal MRPack patch

`scripts/repair_1_8_4_test_mrpack.py SOURCE.mrpack OUT.mrpack`

- Remove `mods/cobblemonnestsdens-fabric-1.3.3.jar` *from the manifest*
  and the no-longer-applicable Nests & Dens override configuration files.
  Third-party JARs were never embedded in the MRPack.
- Upgrade Fabric Loader declaration from 0.19.3 to **0.19.5**, a
  published version, to satisfy Fabric Language Kotlin.
- Preserve all other Modrinth dependency entries, data packs, QuestZ
  source, RCT trainer series, and project resource packs.
- Give the experimental package a clearly non-release version identifier.
- Check ZIP CRC and absence of duplicate entries before and after.

The resulting MRPack contains 75 Modrinth file entries (68 mods).
It is suitable for **fresh-instance testing**, not a proven release.

## Remaining compatibility work

- Test launching a new Modrinth App instance with Java 21.
- Test the complete League's RCT/Rad Gyms progression and existing
  level-cap series; the alpha source was developed for Cobblemon 1.7.3.
- Test Cobblemon 1.8.4's built-in TMs against legacy
  `SimpleTMs 2.3.3`; remove legacy TMs only with an explicit
  world-migration strategy because existing item IDs may be affected.
- Test Mega Showdown, Cobbreeding, legendary spawns, Outbreaks, QuestZ
  events, loot and shop IDs, and server startup.
- **Do not upgrade existing worlds in place.** Disabling Nests & Dens
  may remove structures, blocks, items or dimension data used in old
  saves. Keep an untouched backup and use a world copy.
- Do not change `feature/1.3.0-living-horizons` or `master` based
  only on static compatibility checks.

## Audit evidence

- `docs/migration-1.8.4-upload-inventory.json`: exact uploaded
  Modrinth mod version identifiers.
- `scripts/audit_user_upgrade.py`: official version and JAR
  metadata inspection.
- `.github/workflows/audit-user-upgrade.yml`: reproducible audit job.
- `scripts/repair_1_8_4_test_mrpack.py`: reproducible minimal repair.

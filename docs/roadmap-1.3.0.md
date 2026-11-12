# CobbleHorizons 1.3.0 — Living Horizons

Status: **in development** on `feature/1.3.0-living-horizons`. Do not publish this
branch as a Modrinth release until all gates below are satisfied.

## Release baseline

- Published baseline: [GitHub v1.2.0](https://github.com/ivanantunes/minecraft-cobble-horizons/releases/tag/v1.2.0).
- Public distribution: [Modrinth CobbleHorizons](https://modrinth.com/modpack/cobblehorizons).
- Current known-good release target: Minecraft 1.21.1, Fabric Loader 0.19.3,
  Java 21, Cobblemon 1.7.3.
- Preserve existing League series ID, advancement IDs, level caps, first-party
  resource-pack identity, and saved-world progression unless migration is
  explicitly tested.
- **Do not assume the GitHub source tree is a complete copy of the 1.2.0
  artifact.** Verify against the actual `.mrpack`.

## Phase 0 — Restore reproducible release sources [blocking]

The `master` tree inspected on 2026-11-06 contains:

- 106 tracked QuestZ advancement JSON files, compared with 120 documented
  advancement records (107 gameplay quests + root + 12 disabled hunts).
- `horizon_elite.json`, which references
  `cobblehorizons:questz/league_champion`, while that advancement is absent
  from the tracked source.
- `CobbleHorizons-Progression/pack.mcmeta`, but no corresponding progression
  `data/` files in the tracked source.
- No tracked build/validator scripts before 1.3 development started.
- A root-unscoped `data/` ignore rule that can suppress new nested datapack data.

**Actions:**

1. Obtain the official `CobbleHorizons.1.2.0.mrpack` asset and save its SHA-256.
2. Unzip to a disposable directory; inspect `modrinth.index.json`,
   `overrides/`, `client-overrides/` and `server-overrides/`.
3. Compare first-party datapacks, first-party resource-pack contents and
   configuration from the artifact against the repository.
4. Restore first-party text/source files exactly, including the League RCT
   series, migrations, trainer overrides, missing quests and reward functions.
   Do not check in third-party JARs, generated archives or personal runtime data.
5. Remove any accidental omissions caused by `.gitignore` and resolve all
   validator findings with a verified source-of-truth.
6. Verify that a build from the repository reproduces the playable behavior of
   the release. Binary-identical ZIP bytes are not required if metadata/order
   changes, but effective content must agree.

**Recovery status (2026-11-06):** complete at source-file level.
The official v1.2.0 release archive has SHA-256
`fccfeb290946191c30f6c5e2783fc90e3564e04b36d3794d8c666d73ce57a40a`.
The verified restore added **47 previously untracked first-party files**:
14 QuestZ advancements, 14 reward functions, and 19 progression files.
The other 213 first-party files were byte-identical to GitHub (0 conflicts).
The restored source now includes the complete League, trainer overrides,
RCT series and migration command. Strict JSON, advancement and archive
validation passes on the recovered baseline.

**Remaining gate:** verify League and RCT behavior *in-game* and confirm that
the release pack imports correctly on a clean Modrinth instance. The strict
source/MRPack CI check is enabled without `--audit-only`.

## Phase 1 — Compatibility and update matrix

Inventory every `modrinth.index.json` file entry by ID, version, dependency,
distribution URL, and client/server environment. Do not assume the docs list is
identical to the released manifest.

Evaluate **Cobblemon 1.8.4 as an opt-in experimental branch**, not a requirement
for 1.3.0. Check RCT/Rad Gyms, Mega Showdown, Cobbreeding, SimpleTMs, Myths and
Legends, Legendary Monuments, RCT Capture Cap, QuestZ triggers, and datapack
schemas. Replace overlapping systems only after compatibility testing.

**Gate:** the stable baseline starts on both singleplayer and dedicated server
without regression. Any 1.8.x migration requires its own proven compatibility
matrix, saved-world migration tests and independent go/no-go decision.

## Phase 2 — Living Horizons gameplay

### Mass Outbreaks (candidate mod)

- Investigate a Cobblemon Outbreaks build for the exact stable Cobblemon/Fabric
  stack; pin its download and file hashes via the MRPack manifest.
- Test biome selection, spawn competition with Nests & Dens and legendary
  encounters, shiny rates, event frequency, world persistence and server load.
- Do not enable highly frequent outbreaks or uncontrolled shiny rewards by
  default. Use a conservative configuration and measure performance.

### Horizon Research postgame (first-party)

**Initial alpha implementation:** `research_champion_first_battle` and
`research_shiny_first` are new QuestZ nodes under `horizon_elite`, each
using an existing Cobblemon trigger and paying CobbleDollars rather than items.
These are structurally checked by CI, but still need gameplay validation for
post-unlock event timing.

- Preserve `horizon_elite` as the existing post-Champion achievement/gate.
- Add new postgame chapters under new IDs; never replace already-granted
  advancement IDs in existing worlds.
- Planned paths: Legendary Research, Mega Mastery, Shiny Research.
- Every quest requires a **verified gameplay trigger**. No generic capture
  event may masquerade as a species-specific capture. For unsupported events,
  use an attainable alternative objective and clearly label it.
- Rewards should not trigger chain completions of inventory objectives.

### Horizon Expeditions (first-party)

- Use Terralith, existing structure mods, nests and legendary monuments.
- Only ship exploration objectives that can detect their criteria reliably.
- Avoid extra world-generation mods unless clearly needed and migration-safe.

### PokéMart balance

- Review `config/cobbledollars/default_shop.json`, incomes and quest rewards.
- Add useful supplies and evolution items only after IDs are confirmed.
- Define earn/spend budgets for early, mid and late game.
- Badge-gated shops are optional and must have a tested implementation; do not
  promise them with plain static JSON alone.

## Alpha 1 technical milestone — completed 2026-11-06

- Restored 47 missing first-party source files from the SHA-256-pinned v1.2.0 MRPack.
- Enabled strict source and archive validation; the historical 1.2.0 baseline passes.
- Added two preliminary Horizon Research quests (Champion battle and Shiny catch).
- Expanded CobbleDollars `default_shop.json` with Medicine (6 offers) and
  Evolution Stones (9 offers); kept original shop offers/prices unchanged.
- Inspected Modrinth Outbreaks `1.1.2` (`nxE2RfXE`, `Rlt9c9kz`) directly
  through both its API version metadata and SHA-verified Fabric JAR.
  All declared required Modrinth projects are present in the 1.2.0 manifest.
- Added a pinned MRPack alpha builder; its first successful candidate contains
  **76 Modrinth manifest files**, 122 advancements (110 active including root),
  397 ZIP entries and **zero strict validator findings**.
- Alpha archives are uploaded to GitHub Actions as test artifacts, not released.
- See `docs/compatibility-1.3.0.md` and `docs/alpha-1.3.0-test-plan.md`.

**Still blocked:** no verified gameplay client/server test, no migration
playtest and no proven spawn/quest semantics for Outbreaks or postgame.
Do not label the alpha as release-ready.

## Phase 3 — Pre-release checks

1. Validate first-party JSONs, advancements, parent references, cycles,
   required progression predicates and reward functions.
2. Run validator unit tests and validate final MRPack ZIP, manifest, hashes,
   override paths and disallowed runtime files.
3. Test fresh Modrinth instance on Java 21, world creation, title/resource
   packs, normal trainers, all eight Gym Leaders, Elite Four, Champion Terry,
   and expected level-cap unlock order.
4. Test outbreaks, postgame milestones, economy, rare spawn rates and duration
   in fresh world and backed-up world from 1.2.0.
5. Validate dedicated server, client-server mod requirements and performance.
6. Update README, CHANGELOG, included mod list, installation and migration
   guide, screenshots, and Modrinth description to reflect the final contents.
7. Publish a release candidate first. Publish GitHub and Modrinth final only
   when those artifacts and release notes match.

## Proposed checkpoints

- **alpha.1:** repaired Git source + release auditor + baseline recovery.
- **alpha.2:** complete compatibility matrix and approved upgrade decisions.
- **beta.1:** functional outbreaks, postgame/expedition quests, economy balancing.
- **rc.1:** stabilization, migration tests and candidate MRPack.
- **1.3.0:** signed-off GitHub Release and Modrinth publication.

## Known constraints

- Binary recovery is performed by the checksum-pinned GitHub Actions
  `restore-v1.2-sources.yml` workflow. The restorer never overwrites existing
  source and records which files matched or were recovered.
- Code-level validation does not prove in-game spawn, progression, economy
  or saved-world migration behavior.
- Avoid altering live 1.2.0 content or uploading a Modrinth file during
  development. Only tested release artifacts belong in a final release.

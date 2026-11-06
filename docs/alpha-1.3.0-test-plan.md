# Manual test plan — CobbleHorizons 1.3.0-alpha.1

**Status:** test build only. Never overwrite an existing world or publish this
artifact directly to Modrinth.

## Getting the alpha

1. Open [GitHub Actions: experimental alpha MRPack](https://github.com/ivanantunes/minecraft-cobble-horizons/actions/workflows/build-alpha.yml).
2. Open the latest **successful** run on `feature/1.3.0-living-horizons`.
3. Download the `CobbleHorizons-1.3.0-alpha.1-NOT-FOR-RELEASE` artifact ZIP.
4. Extract the archive and import only `CobbleHorizons-1.3.0-alpha.1.mrpack`
   into a **new** Modrinth App instance.
5. Use Java 21 and initially allocate 6 GB RAM.

The Actions artifact ZIP itself is **not** the importable MRPack.

## A. Clean installation / world (mandatory)

- [ ] MRPack imports without the previously observed Modrinth import exception.
- [ ] Minecraft starts and opens a brand-new survival world without a crash.
- [ ] Cobblemon 1.7.3, RCT, QuestZ and Outbreaks 1.1.2 are present.
- [ ] All expected resource packs, menus, keybindings, and music work.
- [ ] Press `L` and verify the QuestZ book loads with the existing campaign.
- [ ] Starter → Apricorns → first capture → First Challenger progression works.
- [ ] Brock is the first required League opponent; level cap starts at 15.
- [ ] Later Gym/Elite/Champion quests remain gated and do not autocomplete.
- [ ] League bosses do not spawn randomly; ordinary RCT trainers still do.
- [ ] New Medicine and Evolution Stones categories show in CobbleDollars shop.
- [ ] Bought items have correct IDs/prices and do not cause reward cascades.

## B. Mass Outbreaks (mandatory)

Test at least one event in **plains**, **forest**, and **water/coast** areas.
For fast testing, use an operator account and built-in commands:

- `/outbreak start`
- `/outbreak info`
- `/outbreak stop`
- `/outbreak reload` (if supported on the installed build)

- [ ] Outbreaks spawn a biome-appropriate species on viable terrain.
- [ ] Bossbar, waypoint/chat messages and wave counters are readable.
- [ ] Defeating/capturing outbreak Pokémon advances counts correctly.
- [ ] Outbreak completes or times out; no orphaned Pokémon remain.
- [ ] Stopping an outbreak cleans up without affecting wild Pokémon.
- [ ] Normal wild spawns, legends, monuments, nests and dens still function.
- [ ] No obvious runaway shiny rewards or high-IV economy exploits.
- [ ] Game FPS, server tick rate and memory remain acceptable versus v1.2.0.
- [ ] Restart and reload do not duplicate or stall active outbreaks.

Record number of outbreak Pokémon, duration, environment, peak memory,
server TPS (dedicated), and any unusual log errors. Do **not** ship a
custom config until its schema and semantics are verified in-game.

## C. Horizon Research (mandatory)

Use a test world where the original League is completed legitimately.

- [ ] Finishing Champion Terry grants the old `horizon_elite` achievement.
- [ ] Two new quests appear under `Horizon Elite` in QuestZ.
- [ ] `Champion's First Match` cannot complete before unlocking Horizon Elite.
- [ ] Winning the required post-Champion battle completes it exactly once.
- [ ] Reward is 15,000 CobbleDollars (and the configured XP), not items.
- [ ] `Shiny Field Research` cannot complete before Horizon Elite.
- [ ] Catching a Shiny after the gate completes the quest exactly once.
- [ ] Reward is 20,000 CobbleDollars (and the configured XP), not items.
- [ ] Neither new quest alters old Gym/Elite/Champion advancement data.
- [ ] Reloading after completion does not re-award the currency.

If a player's old battle/shiny statistics cause retroactive completion,
treat it as a **blocker** and adjust the criterion implementation.

## D. Upgrade an existing 1.2.0 world (mandatory)

Back up the entire v1.2.0 instance, especially `saves/`, before starting.

1. Make a new 1.3 alpha instance (do not replace the original).
2. Start it once and close Minecraft.
3. Copy a backed-up v1.2.0 save to the alpha instance.
4. Check player party/PC, held items, structures and saved advancements.
5. Verify League series, existing level cap and Champion completion state.
6. Run the existing progression migration helper **only if needed**:
   `/function cobblehorizons:progression/migrate_1_2_all_online`
7. Repeat the same checks with a world that has *not* defeated Terry.
8. Verify Outbreaks do not corrupt saved world state after shutdown/restart.

- [ ] No level-cap reset, quest loss, incorrect badge unlock or economy wipe.
- [ ] New quests are available only to eligible existing Champions.
- [ ] Player data survives restart and return to v1.2.0 copy unchanged.
- [ ] The new instance does not overwrite the original backup.

## E. Dedicated server and release gates (mandatory)

- [ ] Dedicated server starts with correct server-side dependencies installed.
- [ ] Multiple players can join without incompatible client-only mod failures.
- [ ] Outbreak bossbars/announcements show to appropriate participants.
- [ ] No forced crashes on server stop/start or player dimension changes.
- [ ] Build manifest and ZIP integrity audit pass with **0 errors**.
- [ ] Update changelog, screenshots, installation documentation and migration
      notes after gameplay passes.
- [ ] Build a fresh release candidate from the final commit.
- [ ] Explicit review/approval before merging PR #3 or uploading to Modrinth.

For bugs include OS, Java version, alpha version, exact reproduction steps,
world type (new/upgraded), and a sanitized `latest.log` link.

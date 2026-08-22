# Release Checklist — CobbleHorizons 1.2.x

Use this before publishing an MRPack to GitHub Releases or Modrinth.

## Packaging

- [ ] `modrinth.index.json` reports Minecraft 1.21.1 and Fabric Loader 0.19.3.
- [ ] Third-party mods/packs are represented through their permitted distribution source where possible.
- [ ] `config/` is included.
- [ ] first-party `datapacks/` are included.
- [ ] first-party `resourcepacks/CobbleHorizons.zip` is included.
- [ ] required external resource/shader content resolves through the manifest.
- [ ] no `saves/`, logs, crash reports, caches or personal data are included.
- [ ] no root personal `options.txt` is included as release override state.
- [ ] `defaultoptions.journal.json` is not included.
- [ ] ZIP/MRPack integrity test passes.

## Defaults

- [ ] `config/defaultoptions/options.txt` exists.
- [ ] `config/defaultoptions/keybindings.txt` exists.
- [ ] resource packs load correctly in a fresh instance.
- [ ] title screen / loading flow is customized.
- [ ] six CobbleHorizons music tracks can play.

## Controls

- [ ] `R` sends/recalls selected Pokémon without a shader conflict.
- [ ] `B` opens Inmis backpack.
- [ ] `M` opens world map.
- [ ] `G` creates a waypoint.
- [ ] `N` opens CobbleNav PokéNav.
- [ ] `V` opens Cobblemon Summary.
- [ ] no important active bindings are duplicated in Minecraft Controls.
- [ ] F6–F10 behavior is understood/tested on macOS (`Fn` if required).

## Fresh-world gameplay

- [ ] QuestZ opens with `L`.
- [ ] starter → Apricorn → first catch → Pokédex → first trainer sequence works.
- [ ] Brock is the first League boss.
- [ ] later League nodes stay locked until required.
- [ ] League bosses do not naturally spawn in the overworld.
- [ ] ordinary trainers still spawn.
- [ ] cow, pig, chicken and sheep can naturally appear.
- [ ] unwanted vanilla mobs remain suppressed.
- [ ] no obvious quest item-reward cascade occurs after looting/inventory changes.
- [ ] Species Hunt templates remain hidden.

## Regression

- [ ] server/client starts without new severe log errors.
- [ ] singleplayer world loads.
- [ ] progression validator passes.
- [ ] resource pack archive opens correctly.
- [ ] migration function exists for upgraded worlds.

## Documentation

- [ ] README version is correct.
- [ ] CHANGELOG includes current release.
- [ ] mod list matches manifest.
- [ ] controls documentation matches `keybindings.txt`.
- [ ] repository docs do not instruct users to commit runtime files.
- [ ] release notes are updated.
- [ ] checksum is generated from the final artifact actually published.

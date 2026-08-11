# CobbleHorizons Testing

## Reference environment

- Minecraft 1.21.1
- Fabric Loader 0.19.x
- Cobblemon 1.7.3
- English (US)
- clean Modrinth instance

## Clean-import checklist

### Installation

- [ ] MRPack imports without extraction or filesystem errors.
- [ ] Minecraft, Fabric, and all indexed content resolve correctly.
- [ ] No personal worlds, logs, screenshots, or account files are included.

### Startup

- [ ] Mojang/Drippy loading screen uses the CobbleHorizons artwork.
- [ ] Loading bar and window title are correct.
- [ ] The game reaches the title screen without a crash.

### Title screen

- [ ] `fundo1` replaces the vanilla panorama.
- [ ] Vanilla title logo, edition branding, and yellow splash are hidden.
- [ ] Buttons use the CobbleHorizons visual style.
- [ ] All title-screen actions remain accessible.
- [ ] Layout remains readable at GUI scale 3.

### Defaults

- [ ] Language is English (US).
- [ ] CobbleHorizons Branding is enabled.
- [ ] Battle Tracks is enabled.
- [ ] Cobbreeding Pasture Fix is enabled.
- [ ] A second launch preserves the same selection.
- [ ] Faithful 32x is available but not enabled by default.
- [ ] Shaders are disabled by default; Complementary, MakeUp Ultra Fast, and BSL are selectable.

### Gameplay

- [ ] A new world loads.
- [ ] An existing test world loads.
- [ ] Starter selection, catching, battles, and Pokémon status screens work.
- [ ] Trainers, gyms, breeding, audio, maps, and shaders work.
- [ ] `M` opens Xaero's World Map and `V` opens the Cobblemon Summary.
- [ ] Iris uses `F7` for selection, `F8` for reload, and `F9` for toggle.
- [ ] `R` still sends the selected Pokémon without triggering a shader reload.

### Logs

- [ ] No fatal exception occurs.
- [ ] No FancyMenu illegal identifier is reported.
- [ ] No missing FancyMenu background or button texture is reported.
- [ ] Resource manager lists the three default packs plus optional Faithful 32x.

## Known non-critical log noise

Some optional compatibility mixins, missing optional integrations, sound warnings, and data-fixer messages may appear without affecting gameplay. They must still be reviewed before a stable release.

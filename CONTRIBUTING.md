# Contributing to CobbleHorizons

Thank you for helping improve CobbleHorizons.

## Project standards

- Target Minecraft **1.21.1**, Fabric Loader **0.19.3** and Java **21**.
- Keep Cobblemon **1.7.3** compatibility unless a future release explicitly changes the baseline.
- Keep Pokémon at the center of progression.
- Prefer stability and compatibility over unnecessary complexity.
- Avoid changing progression unless the change is intentional, validated and documented.
- Keep player-facing defaults and repository documentation in English.
- Respect every third-party project's license and distribution requirements.
- Treat the Git repository as source/configuration, not as a binary dependency mirror.

## Source-control policy

Commit:

- CobbleHorizons `config/` files;
- first-party datapacks;
- the first-party `resourcepacks/CobbleHorizons.zip` pack or its maintained source;
- project artwork/assets you have the right to redistribute;
- documentation;
- validation/build scripts.

Do not commit:

- third-party mod `.jar` files;
- third-party datapack/resource-pack/shader archives;
- generated `.mrpack` releases;
- a personal root `options.txt`;
- `defaultoptions.journal.json`;
- worlds, account data, logs, screenshots, caches or crash reports.

See [Repository Structure](docs/repository-structure.md).

## Bug reports

Include:

- CobbleHorizons version;
- operating system and hardware;
- fresh-instance or upgraded-instance status;
- clear reproduction steps;
- expected and actual behavior;
- screenshots when relevant;
- a sanitized `latest.log` link from [mclo.gs](https://mclo.gs/).

For world-generation, quest or progression issues, state whether the problem reproduces in a **new world**.

## Required validation before a change

1. Build or obtain the candidate MRPack using the official project process.
2. Import it into a completely new Modrinth instance.
3. Confirm startup, title screen, loading flow and required resource packs.
4. Confirm `config/defaultoptions/options.txt` and `config/defaultoptions/keybindings.txt` are present.
5. Create a fresh survival world.
6. Press `L` and verify QuestZ opens.
7. Verify the affected gameplay/interface flow.
8. For progression changes, verify the RCT series and required-defeat chain.
9. For trainer changes, verify key League trainers do not spawn naturally.
10. For spawn changes, verify cow/pig/chicken/sheep can appear and suppressed vanilla mobs remain suppressed.
11. Review `latest.log` for new errors.
12. Run the project validator when available.
13. Update README/docs/changelog for player-visible changes.

## Quest changes

Quest data lives in:

`datapacks/CobbleHorizons-QuestZ/data/cobblehorizons/advancement/questz/`

When adding or editing a non-root quest:

- keep a valid `parent`;
- enforce prerequisite gating when the quest belongs to a sequence;
- use criteria supported by Minecraft 1.21.1 / Cobblemon 1.7.3;
- verify the reward function exists;
- check whether an item reward can satisfy another `inventory_changed` quest;
- avoid multi-step automatic item reward cascades;
- test in a fresh world.

Do not re-enable the disabled Species Hunt quests until species-specific capture filtering is validated against the exact release stack.

## League progression changes

First-party RCT overrides live in:

`datapacks/CobbleHorizons-Progression/`

Keep the CobbleHorizons sequence synchronized across:

- trainer `requiredDefeats`;
- trainer `series` membership;
- natural spawn policy;
- QuestZ League nodes;
- intended level-cap progression;
- documentation.

League bosses should remain structure/progression encounters, not random natural spawns.

## Controls

Curated defaults live in:

- `config/defaultoptions/options.txt` — regular Minecraft client defaults;
- `config/defaultoptions/keybindings.txt` — key mapping defaults.

Do not reintroduce keybind lines into `options.txt` as a replacement for `keybindings.txt`.

When adding a mod with keybindings, verify the Controls screen for duplicate active bindings on both Windows and macOS where practical.

## Commit style

- `feat:` new functionality
- `fix:` bug fix
- `config:` gameplay, UI or performance configuration
- `balance:` spawn/reward/progression balancing
- `docs:` documentation
- `chore:` maintenance
- `release:` release preparation

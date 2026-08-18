# Contributing to CobbleHorizons

Thank you for helping improve CobbleHorizons.

## Project standards

- Target Minecraft 1.21.1, Fabric Loader 0.19.3 and Java 21.
- Keep Pokémon at the center of the experience.
- Prefer stability and compatibility over unnecessary complexity.
- Keep player-facing defaults and documentation in English.
- Respect every third-party project's license and distribution requirements.
- Treat the Git repository as source code, not as a binary dependency mirror.

## Source-control policy

Commit:

- CobbleHorizons configuration;
- first-party datapacks;
- first-party branding/assets;
- documentation;
- validation/build scripts when added.

Do not commit:

- third-party mod `.jar` files;
- third-party datapack/resource-pack/shader ZIPs;
- generated `.mrpack` releases;
- root `options.txt`;
- worlds, accounts, logs, screenshots, caches or crash reports.

The first-party `resourcepacks/CobbleHorizons-Branding.zip` is currently an intentional exception.

See [Repository Structure](docs/repository-structure.md).

## Bug reports

Include:

- CobbleHorizons version;
- operating system and hardware;
- clear reproduction steps;
- expected and actual behavior;
- screenshots when relevant;
- a sanitized `latest.log` link from [mclo.gs](https://mclo.gs/).

## Proposed changes

Before submitting a change:

1. Build or obtain the MRPack using the official project process.
2. Import it into a completely new Modrinth instance.
3. Confirm startup, title screen, resource-pack defaults and English language.
4. Create and load a fresh world for quest changes.
5. Press `L` and verify QuestZ opens.
6. Test the affected gameplay or interface flow.
7. For quest changes, verify parent references, prerequisite gating and reward functions.
8. Review `latest.log` for new errors.
9. Update documentation and the changelog when necessary.

## Quest changes

Quest data lives in:

`datapacks/CobbleHorizons-QuestZ/data/cobblehorizons/advancement/questz/`

When adding or editing a non-root quest:

- keep a valid `parent`;
- include a real prerequisite check when the quest must be progression-gated;
- use supported criteria for the exact Cobblemon/Minecraft version;
- verify the reward function exists;
- test in a fresh world.

Do not re-enable the disabled Species Hunt quests until species-specific capture filtering has been validated.

## Commit style

- `feat:` new functionality
- `fix:` bug fix
- `config:` gameplay, UI or performance configuration
- `docs:` documentation
- `chore:` maintenance
- `release:` release preparation

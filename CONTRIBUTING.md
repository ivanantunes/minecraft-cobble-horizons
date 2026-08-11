# Contributing to CobbleHorizons

Thank you for helping improve CobbleHorizons.

## Project standards

- Target Minecraft 1.21.1, Fabric Loader 0.19.3 and Java 21.
- Keep Pokémon at the center of the experience.
- Prefer stability and compatibility over aggressive optimization.
- Keep all player-facing defaults and documentation in English.
- Respect every third-party project's license and distribution requirements.
- Never commit worlds, accounts, logs, screenshots, caches or crash reports.

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

1. Import the built MRPack into a completely new Modrinth instance.
2. Confirm startup, title screen, resource-pack defaults and English language.
3. Create and load a world.
4. Test the affected gameplay or interface flow.
5. Review `latest.log` for new errors.
6. Update documentation and the changelog when necessary.

## Commit style

- `feat:` new functionality
- `fix:` bug fix
- `config:` gameplay, UI or performance configuration
- `docs:` documentation
- `chore:` maintenance
- `release:` release preparation

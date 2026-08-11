# UI and Branding

## Runtime components

- Drippy Loading Screen controls startup.
- FancyMenu controls the title screen and compatible menu styling.
- Default Options provides fallback defaults for new installations.
- The root `options.txt` guarantees defaults during MRPack import.
- CobbleHorizons Branding provides selected Minecraft title assets.

## Assets

- `config/fancymenu/assets/menu_background.png` — official `fundo1` title background
- `config/fancymenu/assets/button_normal.png`
- `config/fancymenu/assets/button_hover.png`
- `config/fancymenu/assets/button_inactive.png`
- `config/fancymenu/assets/loading_bar_background.png`
- `config/fancymenu/assets/loading_bar_progress.png`

## Design system

- dark surfaces for readability;
- cyan and green accents;
- white primary text and pale-green hover text;
- 8 px nine-slice button borders;
- 16:9 artwork;
- reference GUI scale: 3.

## Title-screen architecture

The title screen uses FancyMenu's universal `title_screen` identifier. It must not be redeclared in `customizablemenus.txt`. The layout renders its custom image in front of the vanilla panorama, disables the vanilla background overlay and blur, and hides the vanilla logo, branding, splash, and Realms notification.

Other supported screens use Global Customizations to avoid fragile full-screen replacements.

## Default resource packs

Clean installations enable:

- CobbleHorizons Branding;
- Cobblemon Battle Tracks;
- Cobbreeding Pasture Fix.

Modrinth may label CobbleHorizons Branding as unknown because it is distributed as a private bundled resource pack rather than a separate catalog project. This does not affect runtime behavior.

## Validation

Test at multiple resolutions and verify mouse, keyboard, and controller navigation. Visual elements must never block access to game settings.

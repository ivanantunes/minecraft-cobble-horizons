# Troubleshooting

## The title screen still shows the vanilla panorama

1. Confirm `config/fancymenu/customization/cobblehorizons_title_screen.txt` exists.
2. Confirm `config/fancymenu/assets/menu_background.png` exists.
3. Verify `render_custom_elements_behind_vanilla = false`.
4. Search `latest.log` for `FANCYMENU`, `illegal`, and `title_screen`.
5. Do not edit layouts while the game is running.

## Resource packs are not enabled on first launch

1. Confirm the instance root contains the distributed `options.txt`.
2. Confirm it lists Branding, Battle Tracks, and `cobbreeding:pasturefix`.
3. Confirm both ZIP resource packs exist in `resourcepacks`.
4. Test with a newly imported instance. Existing player options are not overwritten.

## Loading screen works but the title screen does not

Drippy and FancyMenu use separate layouts. A working boot screen does not prove that the `title_screen` layout was packaged.

## Pink, black, or missing textures

Check file names, PNG extensions, capitalization, and `[source:local]` paths. Paths are case-sensitive on some systems.

## Layout is outside the screen

Test GUI scale 3 at 1920×1080 first, then verify other resolutions. Include resolution and scale in bug reports.

## Crash or severe error

Preserve `latest.log` and `crash-reports`. Record the exact action that caused the failure and reproduce it in a copy of the instance.

# Atomic Industry

A Horizon modpack for Minecraft 26.3: nuclear bombs, orbital strikes, deep quarries, factories, gems and
wayfarer stones, with JEI, Jade, schematics and quality-of-life mods. All 30 mods come from the [Horizon registry](https://playhorizon.dev/mods), pinned
by version and SHA-256; the pack holds none of them.

## Install

In the Horizon launcher open Mods, search for **Atomic Industry**, install it, press Build and confirm the
native-code warning. Native mods run with your account's permissions.

## Mods

| Mod | id | Version |
|---|---|---|
| Additional Lights | `additional_lights` | 3.1.4 |
| Factory Blocks | `factory_blocks` | 1.4.2 |
| ProjectE for Horizon (assets) | `projecte` | 0.1.0 |
| Silent's Gems | `silentgems` | 5.2.0 |
| Voltz (assets) | `voltz` | 0.3.0 |
| Applied Energistics 2 | `ae2` | 15.4.17 |
| AppleSkin | `appleskin` | 0.1.3 |
| Atlas | `atlas` | 0.2.0 |
| Big Nukes | `big_nukes_native` | 0.1.3 |
| Blood Particles | `blood_particles` | 1.2.0 |
| ContinuityHorizon | `connected_textures` | 0.1.7 |
| Deepbore Quarry | `deepbore_quarry_native` | 0.1.2 |
| Better Dynamic Lights | `dynamiclights` | 1.0.3 |
| Eating Animation | `eatinganimation` | 0.2.0 |
| FPS Counter | `fps_overlay` | 2.0.0 |
| PhysicsModHorizon | `horizon_physics` | 0.20.7 |
| Horizonmatica | `horizonmatica` | 0.3.2 |
| InventoryWizard | `inventory_wizard` | 2.3.3 |
| Jade | `jade` | 26.3.8 |
| JEI for Horizon | `jei` | 0.2.1 |
| Mod Menu | `mod_menu` | 0.3.5 |
| Mouse Tricks | `mousetricks` | 0.2.0 |
| Orbital Laser | `orbital` | 0.5.10 |
| ProjectE for Horizon | `projecte_core` | 0.1.0 |
| RightClickHarvest | `rightharvest` | 0.1.1 |
| Shulker Box Tooltip | `shulkerboxtooltip` | 1.0.1 |
| Toggle Sprint | `toggle_sprint` | 1.0.0 |
| Voltz | `voltz_core` | 0.3.0 |
| Wayfarer Stones | `wayfarer_stones_native` | 0.6.3 |
| Zoom | `zoom` | 2.0.0 |

All of them were built together and played on one Horizon Nightly before the pack was published.

## Settings

`overrides/` gives Toggle Sprint's settings. Your graphics, keys and language stay yours.

## Build

```sh
python tools/build.py      # checks every mod against the registry, writes dist/atomic_industry-<version>.hpack
cargo horizon-mod check dist/atomic_industry-1.1.0.hpack
```

## Licence

The manifest and the tools: MIT. Each mod keeps its own licence (see its page in the registry).

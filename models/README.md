# 3D Models

<!-- documentation-languages -->
[English](../docs/i18n/en/models/README.md) · [Русский](../docs/i18n/ru/models/README.md) · [Español](../docs/i18n/es/models/README.md) · [Français](../docs/i18n/fr/models/README.md) · [Deutsch](../docs/i18n/de/models/README.md) · [Português (Brasil)](../docs/i18n/pt-BR/models/README.md) · [简体中文](../docs/i18n/zh-CN/models/README.md) · [日本語](../docs/i18n/ja/models/README.md) · [हिन्दी](../docs/i18n/hi/models/README.md) · [العربية](../docs/i18n/ar/models/README.md)
<!-- /documentation-languages -->

This folder contains STL files for the Follower Gripper assembly.

## Complete Assembly

| File | Description | Compatible Printers |
|------|-------------|---------------------|
| `Follower gripper (165x165 bed size).STL` | Complete gripper parts kit | Printers with bed size > 165×165mm |

### Compatible 3D Printers

- **Bambu Lab A1 mini** (180×180×180mm)
- **Prusa MINI / MINI+** (180×180×180mm)
- **Creality Ender-2 Pro** (165×165×180mm)
- **Anycubic Kobra Neo** (220×220×250mm)
- **Artillery Genius** (220×220×250mm)

*Note: Any printer with bed size ≥165×165mm can print the complete assembly preview.*

## Individual Parts

Located in the `parts/` folder:

| Part Number | File | Qty | Description |
|-------------|------|:---:|-------------|
| RB9.01.060.074 | `Camera holder.STL` | 1 | Camera mounting bracket |
| RB9.01.060.080 | `Holder.STL` | 1 | Mounting bracket without camera |
| RB9.01.060.090 | `Camera spacer.STL` | 1 | Spacer for camera |
| RB9.01.060.110 | `D405 holder.STL` | 1 | Holder for D405 camera |
| RB9.01.062.010 | `Main frame.STL` | 1 | Main structural frame |
| RB9.01.062.021 (D6.0) | `Clamp.STL` | 2 | Finger clamps |
| RB9.01.062.021 (D6.1) | `Clamp.STL` | 2 | Finger clamps |
| RB9.01.062.021 (D6.2) | `Clamp.STL` | 2 | Finger clamps |
| RB9.01.062.021 (D6.3) | `Clamp.STL` | 2 | Finger clamps |
| RB9.01.062.031 | `Gear rack.STL` | 2 | Gear racks for linear motion |
| RB9.01.062.040 | `Gear.STL` | 1 | Drive gear |
| RB9.01.062.100 | `Nail.STL` | 2 | Nails |

## Print Settings

| Parameter | Recommended Value |
|-----------|-------------------|
| Material | PLA / PETG |
| Layer Height | 0.2mm (0.15mm for gears) |
| Infill | 20% (30% for gears) |
| Supports | As needed |
| Walls | 3-4 perimeters |

## Notes

- Print gears with higher infill (100%) for better strength
- Main frame may require supports depending on orientation
- Post-processing: light sanding may be needed for bearing fits
- Individual parts can be printed on any standard FDM printer

## Better rods fit
![Test plate](../assets/images/assembly/rod-test-plate.PNG)

To ensure the rods you purchase fit better into the clamps, you need to use a test piece. Print it and, working from the largest hole to the smallest, select the diameter that allows the rod to fit into the test part without difficulty and with minimal clearance. Then print clamps with the same hole diameter which is mentioned in stl file name (e.g. RB9.01.062.021 (D6.1) if you choose diameter 6.1 mm).

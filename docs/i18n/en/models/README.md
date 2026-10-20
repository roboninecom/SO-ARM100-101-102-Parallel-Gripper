<!-- translation-navigation -->
[English](README.md) · [Русский](../../ru/models/README.md) · [Español](../../es/models/README.md) · [Français](../../fr/models/README.md) · [Deutsch](../../de/models/README.md) · [Português (Brasil)](../../pt-BR/models/README.md) · [简体中文](../../zh-CN/models/README.md) · [日本語](../../ja/models/README.md) · [हिन्दी](../../hi/models/README.md) · [العربية](../../ar/models/README.md)

[English source](../../../../models/README.md)

[English](../README.md)

> Complete English source copy. Images, code, CAD, and original PDFs are shared.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="3d-models"></a>
# 3D Models

This folder contains STL files for the Follower Gripper assembly.

<a id="complete-assembly"></a>
## Complete Assembly

| File | Description | Compatible Printers |
|------|-------------|---------------------|
| `Follower gripper (165x165 bed size).STL` | Complete gripper parts kit | Printers with bed size > 165×165mm |

<a id="compatible-3d-printers"></a>
### Compatible 3D Printers

- **Bambu Lab A1 mini** (180×180×180mm)
- **Prusa MINI / MINI+** (180×180×180mm)
- **Creality Ender-2 Pro** (165×165×180mm)
- **Anycubic Kobra Neo** (220×220×250mm)
- **Artillery Genius** (220×220×250mm)

*Note: Any printer with bed size ≥165×165mm can print the complete assembly preview.*

<a id="individual-parts"></a>
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

<a id="print-settings"></a>
## Print Settings

| Parameter | Recommended Value |
|-----------|-------------------|
| Material | PLA / PETG |
| Layer Height | 0.2mm (0.15mm for gears) |
| Infill | 20% (30% for gears) |
| Supports | As needed |
| Walls | 3-4 perimeters |

<a id="notes"></a>
## Notes

- Print gears with higher infill (100%) for better strength
- Main frame may require supports depending on orientation
- Post-processing: light sanding may be needed for bearing fits
- Individual parts can be printed on any standard FDM printer

<a id="better-rods-fit"></a>
## Better rods fit
![Test plate](../../../../assets/images/assembly/rod-test-plate.PNG)

To ensure the rods you purchase fit better into the clamps, you need to use a test piece. Print it and, working from the largest hole to the smallest, select the diameter that allows the rod to fit into the test part without difficulty and with minimal clearance. Then print clamps with the same hole diameter which is mentioned in stl file name (e.g. RB9.01.062.021 (D6.1) if you choose diameter 6.1 mm).
<!-- /translated-content -->

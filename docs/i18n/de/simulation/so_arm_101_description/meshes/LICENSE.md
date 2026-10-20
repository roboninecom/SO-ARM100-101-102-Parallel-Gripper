<!-- translation-navigation -->
[English](../../../../en/simulation/so_arm_101_description/meshes/LICENSE.md) · [Русский](../../../../ru/simulation/so_arm_101_description/meshes/LICENSE.md) · [Español](../../../../es/simulation/so_arm_101_description/meshes/LICENSE.md) · [Français](../../../../fr/simulation/so_arm_101_description/meshes/LICENSE.md) · [Deutsch](LICENSE.md) · [Português (Brasil)](../../../../pt-BR/simulation/so_arm_101_description/meshes/LICENSE.md) · [简体中文](../../../../zh-CN/simulation/so_arm_101_description/meshes/LICENSE.md) · [日本語](../../../../ja/simulation/so_arm_101_description/meshes/LICENSE.md) · [हिन्दी](../../../../hi/simulation/so_arm_101_description/meshes/LICENSE.md) · [العربية](../../../../ar/simulation/so_arm_101_description/meshes/LICENSE.md)

[Englische Quelle](../../../../../../simulation/so_arm_101_description/meshes/LICENSE.md)

[Deutsch](../../../README.md)

> Vollständige maschinelle Übersetzung, noch nicht von Muttersprachlern geprüft. Bilder, Code, CAD und Original-PDFs werden gemeinsam genutzt. Im Zweifel gilt die englische Quelle.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="licensing-of-the-meshes-in-this-directory"></a>
# Lizenzierung der Maschen in diesem Verzeichnis

**Dieses Verzeichnis ist gemischt.** Nicht jedes Netz hier gehört Robonine, also die
Die Lizenz wird nicht nach Verzeichnis, sondern nach Datei zugewiesen.

`collision/` enthält konvexe Rumpfstoffe, die aus `visual/` durch
`../scripts/generate_collision_meshes.py`. Jeder Rumpf trägt die gleiche Lizenz wie
die visuelle Masche, aus der sie erzeugt wurde.

| Datei (beide `visual/` und `collision/`) | Lizenz | Urheberrecht |
|---|---|---|
| `clamp_1.stl`, `clamp_2.stl` | CERN-OHL-P-2.0 | Robonine |
| `base_link.stl` | Apache-2.0 | TheRobotStudio |
| `link1_1.stl`, `link2_1.stl`, `link3_1.stl`, `link4_1.stl` | Apache-2.0 | TheRobotStudio |
| `link5_1.stl` | Apache-2.0 | gemischt  ⁇  siehe unten |

<a id="upstream-geometry"></a>
## Vorwärtsgeometrie

`base_link.stl` und `link1_1.stl` … `link4_1.stl` sind die SO-ARM101 **Arm**,
aus dem Vorstrom gewonnen [SO-ARM100/101 Projekte nach
TheRobotStudio](https://github.com/TheRobotStudio/SO-ARM100) und umverteilt
unter Apache-2.0. Dieses Projekt entwarf diese Geometrie nicht. Siehe Repository
`NOTICE`.

<a id="link5_1stl--fused-mesh"></a>
## `link5_1.stl` ⁇  Vermischte Mesh

`link5_1.stl` ist ein einziges Netz, das den Strom nach oben verschmilzt SO-ARM101 mit
Robonine's `RB9.01.062.010 Main frame`. Die gesamte Datei wird unter
**Apache-2.0**: Robonine kann nicht gewährt werden CERN-OHL-P-2.0 über Geometrie nicht
die eigene und ist frei, seinen eigenen Teil unter Apache-2.0.

Wenn man diese als zwei separate Maschen wieder exportiert, kann jeder Teil seine eigene
Lizenz. Bis dahin, behandeln Sie die Akte als Apache-2.0 Ganz und gar.

<a id="robonine-geometry"></a>
## Robonine Geometrie

`clamp_1.stl` und `clamp_2.stl` sind RobonineEigenes Design  ⁇  die
`RB9.01.062.021 Clamp` mit der `RB9.01.062.031 Gear rack`. Sie sind offen .
Hardware unter CERN-OHL-P-2.0:

```
Copyright (c) 2025 Robonine

This source describes Open Hardware and is licensed under the CERN-OHL-P v2.
You may redistribute and modify this source and make products using it under
the terms of the CERN-OHL-P v2 (https://ohwr.org/cern_ohl_p_v2.txt).

This source is distributed WITHOUT ANY EXPRESS OR IMPLIED WARRANTY, INCLUDING
OF MERCHANTABILITY, SATISFACTORY QUALITY AND FITNESS FOR A PARTICULAR PURPOSE.

SPDX-License-Identifier: CERN-OHL-P-2.0
```

Siehst du ? `LICENSING.md` in der Wurzel des Repositoriums für die vollständige Lizenzkarte.
<!-- /translated-content -->

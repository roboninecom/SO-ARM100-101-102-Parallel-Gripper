<!-- translation-navigation -->
[English](../en/LICENSING.md) · [Русский](../ru/LICENSING.md) · [Español](../es/LICENSING.md) · [Français](../fr/LICENSING.md) · [Deutsch](LICENSING.md) · [Português (Brasil)](../pt-BR/LICENSING.md) · [简体中文](../zh-CN/LICENSING.md) · [日本語](../ja/LICENSING.md) · [हिन्दी](../hi/LICENSING.md) · [العربية](../ar/LICENSING.md)

[Englische Quelle](../../../LICENSING.md)

[Deutsch](README.md)

> Vollständige maschinelle Übersetzung, noch nicht von Muttersprachlern geprüft. Bilder, Code, CAD und Original-PDFs werden gemeinsam genutzt. Im Zweifel gilt die englische Quelle.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="licensing"></a>
# Lizenzierung

Urheberrecht (c) 2025 Robonine

Dieses Projekt veröffentlicht verschiedene Arten von Material unter verschiedenen Lizenzen.
Jede Datei in diesem Repository ist genau von einer davon abgedeckt.

| Material | Lizenz | Text |
|---|---|---|
| Hardware-Designs (CAD, herstellbare Geometrie) | CERN-OHL-P-2.0 | [`HARDWARE-LICENSE.txt`](../../../HARDWARE-LICENSE.txt) |
| Software (Code, Konfiguration, CI, Roboterbeschreibungen) | Apache-2.0 | [`SOFTWARE-LICENSE.txt`](../../../SOFTWARE-LICENSE.txt) |
| Dokumentation, Darstellung und Fotografien | CC-BY-4.0 | [`DOCS-LICENSE.txt`](../../../DOCS-LICENSE.txt) |

Die maschinenlesbare Version dieser Karte ist [`REUSE.toml`](../../../REUSE.toml), die
die Lizenz für jede Datei nach Pfad zugeordnet wird und durch `reuse lint` in
Vorverpflichtung und CI. `LICENSES/` enthält die gleichen drei Texte unter ihrem SPDX
Namen, wie in der REUSE-Spezifikation vorgeschrieben.

**Einige Materialien hier sind nicht Robonine's.** Siehst du ? [`NOTICE`](../../../NOTICE) für die Zuordnung
und Abschnitt 4 nachfolgend für die genaue Dateiliste.

---

<a id="1-hardware--cern-ohl-p-20"></a>
## 1. Hardware CERN-OHL-P-2.0

```
models/                                             *.STEP, *.STL
models/parts/                                       *.STL
community/histology-slide-gripper/cad/              *.step, *.stl
community/histology-slide-gripper/mujoco/meshes/    base.stl, jaw_left.stl,
                                                    jaw_right.stl, pinion.stl
simulation/so_arm_101_description/meshes/visual/    clamp_1.stl, clamp_2.stl
simulation/so_arm_101_description/meshes/collision/ clamp_1.stl, clamp_2.stl
```

`README.md` Die Dateien in diesen Verzeichnissen sind Dokumentation und fallen unter
CC-BY-4.0- Nein . CERN-OHL-P-2.0.

empfohlene Hinweise bei der Wiederverwendung dieser Hardware:

```
Copyright (c) 2025 Robonine

This source describes Open Hardware and is licensed under the CERN-OHL-P v2.
You may redistribute and modify this source and make products using it under
the terms of the CERN-OHL-P v2 (https://ohwr.org/cern_ohl_p_v2.txt).

This source is distributed WITHOUT ANY EXPRESS OR IMPLIED WARRANTY, INCLUDING
OF MERCHANTABILITY, SATISFACTORY QUALITY AND FITNESS FOR A PARTICULAR PURPOSE.

SPDX-License-Identifier: CERN-OHL-P-2.0
```

<a id="2-software--apache-20"></a>
## 2. Software  ⁇ Apache-2.0

```
software/python/                    examples/                 .github/workflows/
.pre-commit-config.yaml             .gitignore
simulation/so_arm_101_description/  package.xml, setup.py, setup.cfg, Dockerfile,
                                    docker-compose.yaml, .dockerignore,
                                    urdf/, config/, launch/, scripts/, test/,
                                    docker/, worlds/, so_arm_101_description/
community/histology-slide-gripper/mujoco/   *.py, *.xml, *.urdf, *.xacro,
                                            requirements.txt
```

Die Roboterbeschreibung nachstehend `urdf/` ist als Software lizenziert und nicht als
Hardware: sie kodiert Kinematik, Inertien und Gelenkgrenzen für den gesamten Arm;
Ein Großteil davon beschreibt SO-ARM101 Geometrie, die Robonine nicht besitzt
und kann daher nicht unter CERN-OHL-P-2.0. Der herstellbare Griff
Das Design selbst lebt in `models/` und unter Abschnitt 1 fallen.

<a id="3-documentation--cc-by-40"></a>
## 3. Dokumentation  ⁇ CC-BY-4.0

```
README.md, CONTRIBUTING.md, LICENSING.md, RELICENSING.md
docs/                   *.md, *.pdf
assets/images/          *.png, *.PNG, *.jpg
every other README.md in the repository
community/histology-slide-gripper/assets/   *.png, *.jpg, *.gif
```

Angabe für Wiederverwendung: "Robonine — SO-ARM100/101 Parallelgreifer,
https://github.com/roboninecom/SO-ARM100-101-Parallel-Gripper, CC BY 4.0".

<a id="4-mixed-and-third-party-material"></a>
## 4. Gemischte und Drittanbietermaterialien

Die folgenden sind: **nicht** die von Robonine Das Urheberrecht oben. Das sind sie.
aus dem Vorstrom gewonnen SO-ARM100/SO-ARM101 Projekte nach TheRobotStudio und sind
übertragen unter Apache-2.0. Siehst du ? [`NOTICE`](../../../NOTICE).

```
simulation/so_arm_101_description/meshes/visual/     base_link.stl, link1_1.stl,
                                                     link2_1.stl, link3_1.stl,
                                                     link4_1.stl
simulation/so_arm_101_description/meshes/collision/  convex hulls of the above,
                                                     generated by
                                                     scripts/generate_collision_meshes.py
```

`link5_1.stl` (beide `visual/` und `collision/`) ist ein einzelnes Netz, das verschmilzt
Vorwärts SO-ARM101 Handgelenksgeometrie Robonine's `RB9.01.062.010 Main frame`.
Bis es als zwei separate Maschen wieder exportiert wird, wird die gesamte Datei verteilt.
unter Apache-2.0: Robonine kann nicht gewährt werden CERN-OHL-P-2.0 über Geometrie nicht
die eigene und ist frei, seinen eigenen Teil unter Apache-2.0. Die gleiche Geometrie.
ist getrennt unter CERN-OHL-P-2.0 wie
`models/parts/RB9.01.062.010 Main frame.STL`.

`community/histology-slide-gripper/mujoco/meshes/arm/*.stl` sind identisch mit Bytes
Kopien von `simulation/so_arm_101_description/meshes/visual/*.stl` und erben
Ihre Lizenz von dort  ⁇  also sechs dieser acht Dateien sind Upstream Material,
nicht RobonineDas ist die Arbeit.

`community/histology-slide-gripper/` wurde von Michael Viacheslavov beigetragen.
([@histochemichael](https://github.com/histochemichael)) und ist unter
Das gleiche dreiseitige Spaltung; das Urheberrecht ist im Besitz des Autors.

Siehst du ? [`simulation/so_arm_101_description/meshes/LICENSE.md`](simulation/so_arm_101_description/meshes/LICENSE.md)
für die Aufgliederung pro Datei dieses Verzeichnisses.
<!-- /translated-content -->

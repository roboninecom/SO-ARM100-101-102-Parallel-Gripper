<!-- translation-navigation -->
[English](../../../en/simulation/so_arm_101_description/LICENSE.md) · [Русский](../../../ru/simulation/so_arm_101_description/LICENSE.md) · [Español](../../../es/simulation/so_arm_101_description/LICENSE.md) · [Français](../../../fr/simulation/so_arm_101_description/LICENSE.md) · [Deutsch](LICENSE.md) · [Português (Brasil)](../../../pt-BR/simulation/so_arm_101_description/LICENSE.md) · [简体中文](../../../zh-CN/simulation/so_arm_101_description/LICENSE.md) · [日本語](../../../ja/simulation/so_arm_101_description/LICENSE.md) · [हिन्दी](../../../hi/simulation/so_arm_101_description/LICENSE.md) · [العربية](../../../ar/simulation/so_arm_101_description/LICENSE.md)

[Englische Quelle](../../../../../simulation/so_arm_101_description/LICENSE.md)

[Deutsch](../../README.md)

> Vollständige maschinelle Übersetzung, noch nicht von Muttersprachlern geprüft. Bilder, Code, CAD und Original-PDFs werden gemeinsam genutzt. Im Zweifel gilt die englische Quelle.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="licensing-of-this-package"></a>
# Genehmigung dieses Pakets

`so_arm_101_description` ist als Teil der
[SO-ARM100/101 Parallelgreifer](https://github.com/roboninecom/SO-ARM100-101-Parallel-Gripper)
Projekt, das mehrfach lizenziert ist. Diese Datei beschreibt das Paket so ist es
selbstverständlich, wenn sie alleine installiert oder neu verteilt werden.

| Inhalte | Lizenz | Urheberrecht |
|---|---|---|
| `urdf/`, `config/`, `launch/`, `scripts/`, `test/`, `worlds/`, `docker/`, `so_arm_101_description/`, `setup.py`, `package.xml` | Apache-2.0 | Robonine |
| `meshes/` | **gemischt** ⁇  siehe [`meshes/LICENSE.md`](meshes/LICENSE.md) | gemischt |

<a id="meshes--read-before-reusing"></a>
## Meshes  ⁇  vor Wiederverwendung gelesen

`meshes/` ist nicht einheitlich zugelassen:

- `clamp_1.stl`, `clamp_2.stl` sind RobonineDie Geometrie des Griffes, **CERN-OHL-P-2.0**.
- `base_link.stl`, `link1_1.stl` … `link4_1.stl` sind die SO-ARM101 **Arm**, abgeleitet
  aus dem Vorstrom [SO-ARM100/101 Projekte nach
  TheRobotStudio](https://github.com/TheRobotStudio/SO-ARM100) und lizenziert
  **Apache-2.0**. Das sind sie nicht. RobonineDas ist die Arbeit.
- `link5_1.stl` Schmelzungen mit Handgelenkgeometrie RobonineDer Hauptrahmen in einer
  einheitlicher Körper und ist **Apache-2.0** Ganz und gar.

Die Roboterbeschreibung nachstehend `urdf/` ist als Software lizenziert und nicht als
Hardware: es kodiert Kinematik und Trägheitsparameter für den gesamten Arm, viel
davon beschreibt die Strömungsgeometrie, die Robonine Sie besitzt nicht.

Die vollständigen Lizenztexte sind im Repository root als `HARDWARE-LICENSE.txt`,
`SOFTWARE-LICENSE.txt` und `DOCS-LICENSE.txt` (und wieder unter ihren SPDX-Namen
in `LICENSES/`, wie die REUSE-Spezifikation vorschreibt). Siehe auch `LICENSING.md`
für die vollständige Karte, `NOTICE` für die Zuteilung durch Dritte und `REUSE.toml` für die
Maschinenlesbare Version.
<!-- /translated-content -->

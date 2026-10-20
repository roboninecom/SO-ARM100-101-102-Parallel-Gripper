<!-- translation-navigation -->
[English](../en/LICENSING.md) · [Русский](../ru/LICENSING.md) · [Español](../es/LICENSING.md) · [Français](LICENSING.md) · [Deutsch](../de/LICENSING.md) · [Português (Brasil)](../pt-BR/LICENSING.md) · [简体中文](../zh-CN/LICENSING.md) · [日本語](../ja/LICENSING.md) · [हिन्दी](../hi/LICENSING.md) · [العربية](../ar/LICENSING.md)

[Source anglaise](../../../LICENSING.md)

[Français](README.md)

> Traduction automatique intégrale, pas encore relue par des locuteurs natifs. Images, code, CAO et PDF originaux sont partagés. En cas de doute, consultez la source anglaise.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="licensing"></a>
# Licence d'exploitation

Droit d'auteur (c) 2025 Robonine

Ce projet publie différents types de matériel sous différentes licences.
Chaque fichier de ce référentiel est couvert par exactement l'un d'eux.

| Matériel | Licence | Le texte |
|---|---|---|
| Des conceptions de matériel (CAD, géométrie manufacturable) | CERN-OHL-P-2.0 | [`HARDWARE-LICENSE.txt`](../../../HARDWARE-LICENSE.txt) |
| Logiciel (code, configuration, IC, descriptions de robots) | Apache-2.0 | [`SOFTWARE-LICENSE.txt`](../../../SOFTWARE-LICENSE.txt) |
| Documentation, rendus et photographies | CC-BY-4.0 | [`DOCS-LICENSE.txt`](../../../DOCS-LICENSE.txt) |

La version lisible de cette carte est [`REUSE.toml`](../../../REUSE.toml), qui
attribue une licence à chaque dossier par voie et est exécutée `reuse lint` dans
pré-engagement et informatique. `LICENSES/` contient les mêmes trois textes dans leur SPDX
les noms, comme l'exige la spécification REUSE.

**Quelque chose qui ne l'est pas Robonine's.** Vous voyez ? [`NOTICE`](../../../NOTICE) pour attribution
et la section 4 ci-dessous pour une liste précise des dossiers.

---

<a id="1-hardware--cern-ohl-p-20"></a>
## 1. Le matériel  ⁇ CERN-OHL-P-2.0

```
models/                                             *.STEP, *.STL
models/parts/                                       *.STL
community/histology-slide-gripper/cad/              *.step, *.stl
community/histology-slide-gripper/mujoco/meshes/    base.stl, jaw_left.stl,
                                                    jaw_right.stl, pinion.stl
simulation/so_arm_101_description/meshes/visual/    clamp_1.stl, clamp_2.stl
simulation/so_arm_101_description/meshes/collision/ clamp_1.stl, clamp_2.stl
```

`README.md` Les fichiers à l'intérieur de ces répertoires sont des documents et relèvent du
CC-BY-4.0- Je ne sais pas . CERN-OHL-P-2.0.

Avis recommandé lors de la réutilisation de ce matériel:

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

La description du robot ci-après `urdf/` est sous licence en tant que logiciel plutôt qu'en
matériel: il encode la cinématie, les inerties et les limites articulaires pour l'ensemble du bras;
dont une grande partie décrit en amont SO-ARM101 géométrie qui Robonine ne possède pas
et ne peut donc pas être placé sous CERN-OHL-P-2.0. L'adhésif de fabrication
le design lui-même vit dans `models/` et est couverte par la section 1.

<a id="3-documentation--cc-by-40"></a>
## 3. Documentation  ⁇ CC-BY-4.0

```
README.md, CONTRIBUTING.md, LICENSING.md, RELICENSING.md
docs/                   *.md, *.pdf
assets/images/          *.png, *.PNG, *.jpg
every other README.md in the repository
community/histology-slide-gripper/assets/   *.png, *.jpg, *.gif
```

Attribution pour réutilisation: "Robonine — SO-ARM100/101 Pince parallèle,
https://github.com/roboninecom/SO-ARM100-101-Parallel-Gripper, CC BY 4.0".

<a id="4-mixed-and-third-party-material"></a>
## 4. Matériau mixte et de tiers

Les éléments suivants sont **pas** couverts par le Robonine le droit d'auteur ci-dessus. Ils sont
dérivé de l'aérien SO-ARM100/SO-ARM101 projet par TheRobotStudio et sont
redistribué en Apache-2.0. Vous voyez ? [`NOTICE`](../../../NOTICE).

```
simulation/so_arm_101_description/meshes/visual/     base_link.stl, link1_1.stl,
                                                     link2_1.stl, link3_1.stl,
                                                     link4_1.stl
simulation/so_arm_101_description/meshes/collision/  convex hulls of the above,
                                                     generated by
                                                     scripts/generate_collision_meshes.py
```

`link5_1.stl` (dans les deux `visual/` et `collision/`) est une seule maille qui fusionne
en amont SO-ARM101 géométrie du poignet avec Robonine's `RB9.01.062.010 Main frame`.
Jusqu'à ce qu'il soit réexporté sous forme de deux mailles distinctes, l'ensemble du dossier est distribué
sous Apache-2.0: Robonine ne peut pas accorder CERN-OHL-P-2.0 sur la géométrie il ne
Il est libre de licencier sa propre partie en vertu du Apache-2.0. La même géométrie.
est disponible séparément sous CERN-OHL-P-2.0 comme
`models/parts/RB9.01.062.010 Main frame.STL`.

`community/histology-slide-gripper/mujoco/meshes/arm/*.stl` sont identiques en octets
des exemplaires `simulation/so_arm_101_description/meshes/visual/*.stl` et hériter
leur licence de là  ⁇  donc six de ces huit dossiers sont du matériel en amont,
pas RobonineC'est le travail.

`community/histology-slide-gripper/` a été contribué par Michael Viacheslavov
([@histochemichael](https://github.com/histochemichael)) et est agréé en vertu du
Le droit d'auteur est détenu par son auteur.

Vous voyez ? [`simulation/so_arm_101_description/meshes/LICENSE.md`](simulation/so_arm_101_description/meshes/LICENSE.md)
pour la répartition par fichier de ce répertoire.
<!-- /translated-content -->

<!-- translation-navigation -->
[English](../../../../en/simulation/so_arm_101_description/meshes/LICENSE.md) · [Русский](../../../../ru/simulation/so_arm_101_description/meshes/LICENSE.md) · [Español](../../../../es/simulation/so_arm_101_description/meshes/LICENSE.md) · [Français](LICENSE.md) · [Deutsch](../../../../de/simulation/so_arm_101_description/meshes/LICENSE.md) · [Português (Brasil)](../../../../pt-BR/simulation/so_arm_101_description/meshes/LICENSE.md) · [简体中文](../../../../zh-CN/simulation/so_arm_101_description/meshes/LICENSE.md) · [日本語](../../../../ja/simulation/so_arm_101_description/meshes/LICENSE.md) · [हिन्दी](../../../../hi/simulation/so_arm_101_description/meshes/LICENSE.md) · [العربية](../../../../ar/simulation/so_arm_101_description/meshes/LICENSE.md)

[Source anglaise](../../../../../../simulation/so_arm_101_description/meshes/LICENSE.md)

[Français](../../../README.md)

> Traduction automatique intégrale, pas encore relue par des locuteurs natifs. Images, code, CAO et PDF originaux sont partagés. En cas de doute, consultez la source anglaise.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="licensing-of-the-meshes-in-this-directory"></a>
# Licence des mailles dans ce répertoire

**Ce répertoire est mélangé.** Tous les réseaux ici ne sont pas propriétaires de Robonine, donc le
La licence est attribuée par dossier plutôt que par répertoire.

`collision/` contient des coques convexes générées à partir de `visual/` par
`../scripts/generate_collision_meshes.py`. Chaque coffre porte la même licence que
le filet visuel à partir duquel il a été généré.

| Fichier (dans les deux `visual/` et `collision/`) | Licence | Droit d'auteur |
|---|---|---|
| `clamp_1.stl`, `clamp_2.stl` | CERN-OHL-P-2.0 | Robonine |
| `base_link.stl` | Apache-2.0 | TheRobotStudio |
| `link1_1.stl`, `link2_1.stl`, `link3_1.stl`, `link4_1.stl` | Apache-2.0 | TheRobotStudio |
| `link5_1.stl` | Apache-2.0 | mélangé voir ci-dessous |

<a id="upstream-geometry"></a>
## Géométrie en amont

`base_link.stl` et `link1_1.stl` … `link4_1.stl` sont les SO-ARM101 **bras**,
dérivé de l'aérien [SO-ARM100/101 projet par
TheRobotStudio](https://github.com/TheRobotStudio/SO-ARM100) et redistribué
sous Apache-2.0. Ce projet n'a pas conçu cette géométrie. Voir le référentiel
`NOTICE`.

<a id="link5_1stl--fused-mesh"></a>
## `link5_1.stl` ⁇  filets fusionnés

`link5_1.stl` est une seule maille qui fusionne le courant ascendant SO-ARM101 poignet avec
Robonine's `RB9.01.062.010 Main frame`. L'ensemble du dossier est distribué sous
**Apache-2.0**: Robonine ne peut pas accorder CERN-OHL-P-2.0 sur la géométrie il ne
Il est libre de licencier sa propre partie en vertu du Apache-2.0.

La re-exportation de ces deux mailles séparées permettrait à chacune des parties de porter son propre
Le permis. En attendant, traitez le dossier comme Apache-2.0 Tout à fait.

<a id="robonine-geometry"></a>
## Robonine géométrie

`clamp_1.stl` et `clamp_2.stl` sont RobonineLe design propre
`RB9.01.062.021 Clamp` fusionné avec le `RB9.01.062.031 Gear rack`. Ils sont ouverts
Le matériel sous CERN-OHL-P-2.0:

```
Copyright (c) 2025 Robonine

This source describes Open Hardware and is licensed under the CERN-OHL-P v2.
You may redistribute and modify this source and make products using it under
the terms of the CERN-OHL-P v2 (https://ohwr.org/cern_ohl_p_v2.txt).

This source is distributed WITHOUT ANY EXPRESS OR IMPLIED WARRANTY, INCLUDING
OF MERCHANTABILITY, SATISFACTORY QUALITY AND FITNESS FOR A PARTICULAR PURPOSE.

SPDX-License-Identifier: CERN-OHL-P-2.0
```

Vous voyez ? `LICENSING.md` dans la racine du référentiel pour la carte complète des licences.
<!-- /translated-content -->

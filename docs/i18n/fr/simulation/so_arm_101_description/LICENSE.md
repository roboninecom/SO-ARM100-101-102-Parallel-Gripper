<!-- translation-navigation -->
[English](../../../en/simulation/so_arm_101_description/LICENSE.md) · [Русский](../../../ru/simulation/so_arm_101_description/LICENSE.md) · [Español](../../../es/simulation/so_arm_101_description/LICENSE.md) · [Français](LICENSE.md) · [Deutsch](../../../de/simulation/so_arm_101_description/LICENSE.md) · [Português (Brasil)](../../../pt-BR/simulation/so_arm_101_description/LICENSE.md) · [简体中文](../../../zh-CN/simulation/so_arm_101_description/LICENSE.md) · [日本語](../../../ja/simulation/so_arm_101_description/LICENSE.md) · [हिन्दी](../../../hi/simulation/so_arm_101_description/LICENSE.md) · [العربية](../../../ar/simulation/so_arm_101_description/LICENSE.md)

[Source anglaise](../../../../../simulation/so_arm_101_description/LICENSE.md)

[Français](../../README.md)

> Traduction automatique intégrale, pas encore relue par des locuteurs natifs. Images, code, CAO et PDF originaux sont partagés. En cas de doute, consultez la source anglaise.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="licensing-of-this-package"></a>
# Licence de ce forfait

`so_arm_101_description` est distribué dans le cadre du
[SO-ARM100/101 Pince parallèle](https://github.com/roboninecom/SO-ARM100-101-Parallel-Gripper)
Le projet, qui est multi-licence. Ce fichier décrit le paquet de sorte qu'il est
auto-expliquant lorsqu'il est installé ou redistribué par lui-même.

| Le contenu | Licence | Droit d'auteur |
|---|---|---|
| `urdf/`, `config/`, `launch/`, `scripts/`, `test/`, `worlds/`, `docker/`, `so_arm_101_description/`, `setup.py`, `package.xml` | Apache-2.0 | Robonine |
| `meshes/` | **mélangé** ⁇  voir [`meshes/LICENSE.md`](meshes/LICENSE.md) | mélangé |

<a id="meshes--read-before-reusing"></a>
## Mesures  ⁇  lues avant réutilisation

`meshes/` n'est pas homologué:

- `clamp_1.stl`, `clamp_2.stl` sont Roboninela géométrie du gripper, **CERN-OHL-P-2.0**.
- `base_link.stl`, `link1_1.stl` … `link4_1.stl` sont les SO-ARM101 **bras**, dérivé
  à partir du courant d'en-haut [SO-ARM100/101 projet par
  TheRobotStudio](https://github.com/TheRobotStudio/SO-ARM100) et sous licence
  **Apache-2.0**. Ce n'est pas le cas. RobonineC'est le travail.
- `link5_1.stl` fusions de géométrie du poignet en amont avec RobonineLe cadre principal dans un
  un seul corps et est **Apache-2.0** Tout à fait.

La description du robot ci-après `urdf/` est sous licence en tant que logiciel plutôt qu'en
le matériel: il codifie les paramètres cinémiques et inertiels pour l'ensemble du bras, beaucoup
dont la géométrie en amont est décrite Robonine ne possède pas.

Les textes complets des licences se trouvent dans la racine du référentiel comme `HARDWARE-LICENSE.txt`,
`SOFTWARE-LICENSE.txt` et `DOCS-LICENSE.txt` (et encore sous leur nom SPDX
dans `LICENSES/`, selon les exigences de la spécification REUSE). Voir aussi: `LICENSING.md`
pour la carte complète, `NOTICE` pour l'attribution à des tiers, et `REUSE.toml` pour le
une version lisible par machine.
<!-- /translated-content -->

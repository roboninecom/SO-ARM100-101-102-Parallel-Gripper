<!-- translation-navigation -->
[English](../../../../en/simulation/so_arm_101_description/meshes/LICENSE.md) · [Русский](../../../../ru/simulation/so_arm_101_description/meshes/LICENSE.md) · [Español](LICENSE.md) · [Français](../../../../fr/simulation/so_arm_101_description/meshes/LICENSE.md) · [Deutsch](../../../../de/simulation/so_arm_101_description/meshes/LICENSE.md) · [Português (Brasil)](../../../../pt-BR/simulation/so_arm_101_description/meshes/LICENSE.md) · [简体中文](../../../../zh-CN/simulation/so_arm_101_description/meshes/LICENSE.md) · [日本語](../../../../ja/simulation/so_arm_101_description/meshes/LICENSE.md) · [हिन्दी](../../../../hi/simulation/so_arm_101_description/meshes/LICENSE.md) · [العربية](../../../../ar/simulation/so_arm_101_description/meshes/LICENSE.md)

[Original en inglés](../../../../../../simulation/so_arm_101_description/meshes/LICENSE.md)

[Español](../../../README.md)

> Traducción automática completa, aún sin revisión de hablantes nativos. Las imágenes, el código, CAD y PDF originales son compartidos. En caso de duda, consulte el original en inglés.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="licensing-of-the-meshes-in-this-directory"></a>
# Licencia de las redes en este directorio

**Este directorio es mezclado.** No todas las redes aquí son propiedad de Robonine, por lo que el
La licencia se asigna por archivo en lugar de por directorio.

`collision/` contiene cascos convexos generados a partir de `visual/` por
`../scripts/generate_collision_meshes.py`. Cada casco lleva la misma licencia que
la malla visual de la que se generó.

| Archivo (en ambos `visual/` y `collision/`) | Licencia | Derecho de autor |
|---|---|---|
| `clamp_1.stl`, `clamp_2.stl` | CERN-OHL-P-2.0 | Robonine |
| `base_link.stl` | Apache-2.0 | TheRobotStudio |
| `link1_1.stl`, `link2_1.stl`, `link3_1.stl`, `link4_1.stl` | Apache-2.0 | TheRobotStudio |
| `link5_1.stl` | Apache-2.0 | mezclado  ⁇  véase a continuación |

<a id="upstream-geometry"></a>
## Geometría aguas arriba

`base_link.stl` y `link1_1.stl` … `link4_1.stl` ¿Son los SO-ARM101 **el brazo**,
derivados de la corriente superior [SO-ARM100/101 proyecto por
TheRobotStudio](https://github.com/TheRobotStudio/SO-ARM100) y redistribuido
en el Apache-2.0. Este proyecto no diseñó esa geometría. Ver el repositorio
`NOTICE`.

<a id="link5_1stl--fused-mesh"></a>
## `link5_1.stl` ⁇  malla fundida

`link5_1.stl` es una sola malla que fusiona el río arriba SO-ARM101 el muñeco con
Robonine's `RB9.01.062.010 Main frame`. Todo el archivo se distribuye en:
**Apache-2.0**: Robonine no puede conceder CERN-OHL-P-2.0 sobre la geometría no
de propiedad, y es libre de licenciar su propia porción bajo Apache-2.0.

La reexportación de esto como dos redes separadas permitiría que cada parte lleve su propio
Licencia. Hasta entonces, trate el expediente como Apache-2.0 En su totalidad.

<a id="robonine-geometry"></a>
## Robonine geometría

`clamp_1.stl` y `clamp_2.stl` son Robonineel diseño propio
`RB9.01.062.021 Clamp` fusionado con el `RB9.01.062.031 Gear rack`. Están abiertas
Hardware bajo CERN-OHL-P-2.0:

```
Copyright (c) 2025 Robonine

This source describes Open Hardware and is licensed under the CERN-OHL-P v2.
You may redistribute and modify this source and make products using it under
the terms of the CERN-OHL-P v2 (https://ohwr.org/cern_ohl_p_v2.txt).

This source is distributed WITHOUT ANY EXPRESS OR IMPLIED WARRANTY, INCLUDING
OF MERCHANTABILITY, SATISFACTORY QUALITY AND FITNESS FOR A PARTICULAR PURPOSE.

SPDX-License-Identifier: CERN-OHL-P-2.0
```

¿Ves ? `LICENSING.md` en la raíz del repositorio para el mapa completo de las licencias.
<!-- /translated-content -->

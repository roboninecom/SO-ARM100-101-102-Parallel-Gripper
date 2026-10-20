<!-- translation-navigation -->
[English](../en/LICENSING.md) · [Русский](../ru/LICENSING.md) · [Español](LICENSING.md) · [Français](../fr/LICENSING.md) · [Deutsch](../de/LICENSING.md) · [Português (Brasil)](../pt-BR/LICENSING.md) · [简体中文](../zh-CN/LICENSING.md) · [日本語](../ja/LICENSING.md) · [हिन्दी](../hi/LICENSING.md) · [العربية](../ar/LICENSING.md)

[Original en inglés](../../../LICENSING.md)

[Español](README.md)

> Traducción automática completa, aún sin revisión de hablantes nativos. Las imágenes, el código, CAD y PDF originales son compartidos. En caso de duda, consulte el original en inglés.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="licensing"></a>
# Licenciamiento

Derecho de autor (c) 2025 Robonine

Este proyecto libera diferentes tipos de material bajo diferentes licencias.
Cada archivo en este repositorio está cubierto por exactamente uno de ellos.

| Materiales | Licencia | El texto |
|---|---|---|
| Diseños de hardware (CAD, geometría fabricable) | CERN-OHL-P-2.0 | [`HARDWARE-LICENSE.txt`](../../../HARDWARE-LICENSE.txt) |
| Software (código, configuración, CI, descripciones de robots) | Apache-2.0 | [`SOFTWARE-LICENSE.txt`](../../../SOFTWARE-LICENSE.txt) |
| Documentación, renderización y fotografías | CC-BY-4.0 | [`DOCS-LICENSE.txt`](../../../DOCS-LICENSE.txt) |

La versión legible de esta mapa es [`REUSE.toml`](../../../REUSE.toml), que
asigna una licencia a cada expediente por vía y se ejecuta mediante `reuse lint` en el
Precompromiso y CI. `LICENSES/` contiene los mismos tres textos en su SPDX
nombres, según lo exija la especificación REUSE.

**Algunos materiales aquí no son Robonine's.** ¿Ves ? [`NOTICE`](../../../NOTICE) para la atribución
y sección 4 a continuación para la lista exacta de archivos.

---

<a id="1-hardware--cern-ohl-p-20"></a>
## 1. Hardware  ⁇ CERN-OHL-P-2.0

```
models/                                             *.STEP, *.STL
models/parts/                                       *.STL
community/histology-slide-gripper/cad/              *.step, *.stl
community/histology-slide-gripper/mujoco/meshes/    base.stl, jaw_left.stl,
                                                    jaw_right.stl, pinion.stl
simulation/so_arm_101_description/meshes/visual/    clamp_1.stl, clamp_2.stl
simulation/so_arm_101_description/meshes/collision/ clamp_1.stl, clamp_2.stl
```

`README.md` los archivos dentro de estos directorios son documentación y se encuentran bajo
CC-BY-4.0No , no . CERN-OHL-P-2.0.

Notificación recomendada para la reutilización de este hardware:

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

La descripción del robot a continuación `urdf/` se ha licenciado como software en lugar de como
hardware: codifica la cinemática, las inercias y los límites articulares para todo el brazo;
gran parte de los cuales describe río arriba SO-ARM101 la geometría que Robonine no posee
y por lo tanto no puede colocar bajo CERN-OHL-P-2.0. El sujetador manufacturable
el diseño en sí mismo vive en `models/` y está cubierta por la sección 1.

<a id="3-documentation--cc-by-40"></a>
## 3. Documentación CC-BY-4.0

```
README.md, CONTRIBUTING.md, LICENSING.md, RELICENSING.md
docs/                   *.md, *.pdf
assets/images/          *.png, *.PNG, *.jpg
every other README.md in the repository
community/histology-slide-gripper/assets/   *.png, *.jpg, *.gif
```

Atribución para reutilización: "Robonine — SO-ARM100/101 Pinza paralela,
https://github.com/roboninecom/SO-ARM100-101-Parallel-Gripper, CC BY 4.0".

<a id="4-mixed-and-third-party-material"></a>
## 4. Materiales mixtos y de terceros

Los siguientes son: **No** cubiertos por el Robonine derechos de autor arriba. Ellos lo son .
derivados de la corriente superior SO-ARM100/SO-ARM101 proyecto por TheRobotStudio y son
redistribuido en Apache-2.0. ¿Ves ? [`NOTICE`](../../../NOTICE).

```
simulation/so_arm_101_description/meshes/visual/     base_link.stl, link1_1.stl,
                                                     link2_1.stl, link3_1.stl,
                                                     link4_1.stl
simulation/so_arm_101_description/meshes/collision/  convex hulls of the above,
                                                     generated by
                                                     scripts/generate_collision_meshes.py
```

`link5_1.stl` (en ambos `visual/` y `collision/`) es una malla única que se fusiona
en aguas subidas SO-ARM101 geometría de muñeca con Robonine's `RB9.01.062.010 Main frame`.
Hasta que se reexporte como dos redes separadas, todo el archivo se distribuye
en el Apache-2.0: Robonine no puede conceder CERN-OHL-P-2.0 sobre la geometría no
de propiedad, y es libre de licenciar su propia porción bajo Apache-2.0. La misma geometría.
se encuentra disponible por separado en CERN-OHL-P-2.0 como
`models/parts/RB9.01.062.010 Main frame.STL`.

`community/histology-slide-gripper/mujoco/meshes/arm/*.stl` son idénticos en byte
ejemplares de `simulation/so_arm_101_description/meshes/visual/*.stl` y heredar
su licencia desde allí  ⁇  por lo que seis de esos ocho archivos son material upstream,
No RobonineEs el trabajo.

`community/histology-slide-gripper/` fue aportado por Michael Viacheslavov
([@histochemichael](https://github.com/histochemichael)) y está autorizada en virtud del
la misma división de tres vías; el copyright es propiedad del autor.

¿Ves ? [`simulation/so_arm_101_description/meshes/LICENSE.md`](simulation/so_arm_101_description/meshes/LICENSE.md)
para el desglose por archivo de ese directorio.
<!-- /translated-content -->

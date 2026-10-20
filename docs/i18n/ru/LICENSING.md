<!-- translation-navigation -->
[English](../en/LICENSING.md) · [Русский](LICENSING.md) · [Español](../es/LICENSING.md) · [Français](../fr/LICENSING.md) · [Deutsch](../de/LICENSING.md) · [Português (Brasil)](../pt-BR/LICENSING.md) · [简体中文](../zh-CN/LICENSING.md) · [日本語](../ja/LICENSING.md) · [हिन्दी](../hi/LICENSING.md) · [العربية](../ar/LICENSING.md)

[Английский оригинал](../../../LICENSING.md)

[Русский](README.md)

> Полный машинный перевод; носители языка его ещё не проверяли. Изображения, код, CAD и исходные PDF общие. При неоднозначности используйте английский оригинал.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="licensing"></a>
# Лицензирование

Авторское право (c) 2025 Robonine

Этот проект выпускает различные виды материалов по разным лицензиям.
Каждый файл в этом хранилище покрыт именно одним из них.

| Материал | Лицензия | Текст |
|---|---|---|
| Конструкции оборудования (CAD, производственная геометрия) | CERN-OHL-P-2.0 | [`HARDWARE-LICENSE.txt`](../../../HARDWARE-LICENSE.txt) |
| Программное обеспечение (код, конфигурация, ИС, описания роботов) | Apache-2.0 | [`SOFTWARE-LICENSE.txt`](../../../SOFTWARE-LICENSE.txt) |
| Документация, рендеры и фотографии | CC-BY-4.0 | [`DOCS-LICENSE.txt`](../../../DOCS-LICENSE.txt) |

Машиночитаемая версия этой карты [`REUSE.toml`](../../../REUSE.toml), который
присваивает лицензию каждому файлу по маршруту и обеспечивается исполнением `reuse lint` в
предварительное обязательство и информационное сообщение. `LICENSES/` содержит те же три текста в своем SPDX
названия, как требуется в спецификации REUSE.

**Некоторые материалы здесь не Robonine's.** Посмотрите . [`NOTICE`](../../../NOTICE) для присвоения
и раздел 4 ниже для точного списка файлов.

---

<a id="1-hardware--cern-ohl-p-20"></a>
## 1. Оборудование  ⁇ CERN-OHL-P-2.0

```
models/                                             *.STEP, *.STL
models/parts/                                       *.STL
community/histology-slide-gripper/cad/              *.step, *.stl
community/histology-slide-gripper/mujoco/meshes/    base.stl, jaw_left.stl,
                                                    jaw_right.stl, pinion.stl
simulation/so_arm_101_description/meshes/visual/    clamp_1.stl, clamp_2.stl
simulation/so_arm_101_description/meshes/collision/ clamp_1.stl, clamp_2.stl
```

`README.md` файлы в этих каталогах являются документацией и подпадают под
CC-BY-4.0, нет CERN-OHL-P-2.0.

Рекомендуемое уведомление при повторном использовании этого оборудования:

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
## 2. Программное обеспечение Apache-2.0

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

Описание робота ниже `urdf/` лицензируется как программное обеспечение, а не как
аппаратное обеспечение: он кодирует кинематику, инерции и ограничения суставов для всей руки;
большая часть которых описывает вверх по течению SO-ARM101 геометрии, что Robonine не владеет
и, следовательно, не может поместить под CERN-OHL-P-2.0. Производственный захват
дизайн сам живет в `models/` и охватывается разделом 1.

<a id="3-documentation--cc-by-40"></a>
## 3. Документация  ⁇ CC-BY-4.0

```
README.md, CONTRIBUTING.md, LICENSING.md, RELICENSING.md
docs/                   *.md, *.pdf
assets/images/          *.png, *.PNG, *.jpg
every other README.md in the repository
community/histology-slide-gripper/assets/   *.png, *.jpg, *.gif
```

Присвоение для повторного использования: "Robonine — SO-ARM100/101 Параллельный захват,
https://github.com/roboninecom/SO-ARM100-101-Parallel-Gripper, CC BY 4.0".

<a id="4-mixed-and-third-party-material"></a>
## 4. Смешанный и сторонний материал

Следующие: **Нет** охватываемые Robonine авторские права выше. Они так и есть.
полученные из подводного потока SO-ARM100/SO-ARM101 проект по TheRobotStudio и являются
перераспределяется по Apache-2.0. Посмотрите . [`NOTICE`](../../../NOTICE).

```
simulation/so_arm_101_description/meshes/visual/     base_link.stl, link1_1.stl,
                                                     link2_1.stl, link3_1.stl,
                                                     link4_1.stl
simulation/so_arm_101_description/meshes/collision/  convex hulls of the above,
                                                     generated by
                                                     scripts/generate_collision_meshes.py
```

`link5_1.stl` (в обоих `visual/` и `collision/`) - это единая сетка, которая сливается
вверх по течению SO-ARM101 геометрия запястья с Robonine's `RB9.01.062.010 Main frame`.
До тех пор, пока он не будет реэкспортирован как две отдельные сетки, весь файл распределяется
под Apache-2.0: Robonine не может предоставить CERN-OHL-P-2.0 по геометрии это не
собственных, и свободно лицензировать свою часть в соответствии с Apache-2.0. Та же геометрия.
доступна отдельно в CERN-OHL-P-2.0 как
`models/parts/RB9.01.062.010 Main frame.STL`.

`community/histology-slide-gripper/mujoco/meshes/arm/*.stl` являются идентичными байтами
копии `simulation/so_arm_101_description/meshes/visual/*.stl` и наследуют
их лицензирование оттуда  ⁇  так что шесть из этих восьми файлов являются материалом вверх потока,
Нет RobonineЭто работа.

`community/histology-slide-gripper/` вносил вклад Михаил Виачеславов
([@histochemichael](https://github.com/histochemichael)) и имеет лицензию на
то же самое трехстороннее разделение; авторское право принадлежит его автору.

Посмотрите . [`simulation/so_arm_101_description/meshes/LICENSE.md`](simulation/so_arm_101_description/meshes/LICENSE.md)
для разбивки по файлам этого каталога.
<!-- /translated-content -->

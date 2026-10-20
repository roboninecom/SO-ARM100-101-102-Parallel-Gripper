<!-- translation-navigation -->
[English](../../../../en/simulation/so_arm_101_description/meshes/LICENSE.md) · [Русский](LICENSE.md) · [Español](../../../../es/simulation/so_arm_101_description/meshes/LICENSE.md) · [Français](../../../../fr/simulation/so_arm_101_description/meshes/LICENSE.md) · [Deutsch](../../../../de/simulation/so_arm_101_description/meshes/LICENSE.md) · [Português (Brasil)](../../../../pt-BR/simulation/so_arm_101_description/meshes/LICENSE.md) · [简体中文](../../../../zh-CN/simulation/so_arm_101_description/meshes/LICENSE.md) · [日本語](../../../../ja/simulation/so_arm_101_description/meshes/LICENSE.md) · [हिन्दी](../../../../hi/simulation/so_arm_101_description/meshes/LICENSE.md) · [العربية](../../../../ar/simulation/so_arm_101_description/meshes/LICENSE.md)

[Английский оригинал](../../../../../../simulation/so_arm_101_description/meshes/LICENSE.md)

[Русский](../../../README.md)

> Полный машинный перевод; носители языка его ещё не проверяли. Изображения, код, CAD и исходные PDF общие. При неоднозначности используйте английский оригинал.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="licensing-of-the-meshes-in-this-directory"></a>
# Лицензирование сеток в этом каталоге

**Этот справочник смешанный.** Не каждая сетка здесь принадлежит Robonine, так что
Лицензия присваивается по файлу, а не по каталогу.

`collision/` содержит конвексные корпуса, полученные из `visual/` по
`../scripts/generate_collision_meshes.py`. Каждый корпус имеет такую же лицензию, что и
визуальная сетка, из которой она была создана.

| Файл (в обоих) `visual/` и `collision/`) | Лицензия | Авторские права |
|---|---|---|
| `clamp_1.stl`, `clamp_2.stl` | CERN-OHL-P-2.0 | Robonine |
| `base_link.stl` | Apache-2.0 | TheRobotStudio |
| `link1_1.stl`, `link2_1.stl`, `link3_1.stl`, `link4_1.stl` | Apache-2.0 | TheRobotStudio |
| `link5_1.stl` | Apache-2.0 | смешанные  ⁇  см. ниже |

<a id="upstream-geometry"></a>
## Геометрия вверх по течению

`base_link.stl` и `link1_1.stl` … `link4_1.stl` Это SO-ARM101 **рукой**,
полученные из подводного потока [SO-ARM100/101 проект по
TheRobotStudio](https://github.com/TheRobotStudio/SO-ARM100) и перераспределяется
под Apache-2.0. Этот проект не разработал эту геометрию. Смотрите репозиторий
`NOTICE`.

<a id="link5_1stl--fused-mesh"></a>
## `link5_1.stl` ⁇  сливная сетка

`link5_1.stl` является единственной сеткой, которая сливается вверх по течению SO-ARM101 запястья с
Robonine's `RB9.01.062.010 Main frame`. Весь файл распределен под
**Apache-2.0**: Robonine не может предоставить CERN-OHL-P-2.0 по геометрии это не
собственных, и свободно лицензировать свою часть в соответствии с Apache-2.0.

Реэкспорт этого в виде двух отдельных сеток позволит каждой части нести свой собственный
Лицензия. До тех пор обращайтесь с файлом как Apache-2.0 В полном объеме.

<a id="robonine-geometry"></a>
## Robonine геометрия

`clamp_1.stl` и `clamp_2.stl` являются Robonineсобственный дизайн  ⁇
`RB9.01.062.021 Clamp` слияние с `RB9.01.062.031 Gear rack`. Они открыты .
Оборудование под CERN-OHL-P-2.0:

```
Copyright (c) 2025 Robonine

This source describes Open Hardware and is licensed under the CERN-OHL-P v2.
You may redistribute and modify this source and make products using it under
the terms of the CERN-OHL-P v2 (https://ohwr.org/cern_ohl_p_v2.txt).

This source is distributed WITHOUT ANY EXPRESS OR IMPLIED WARRANTY, INCLUDING
OF MERCHANTABILITY, SATISFACTORY QUALITY AND FITNESS FOR A PARTICULAR PURPOSE.

SPDX-License-Identifier: CERN-OHL-P-2.0
```

Посмотрите . `LICENSING.md` в корне хранилища для полной карты лицензии.
<!-- /translated-content -->

<!-- translation-navigation -->
[English](../../../../en/simulation/so_arm_101_description/meshes/LICENSE.md) · [Русский](../../../../ru/simulation/so_arm_101_description/meshes/LICENSE.md) · [Español](../../../../es/simulation/so_arm_101_description/meshes/LICENSE.md) · [Français](../../../../fr/simulation/so_arm_101_description/meshes/LICENSE.md) · [Deutsch](../../../../de/simulation/so_arm_101_description/meshes/LICENSE.md) · [Português (Brasil)](../../../../pt-BR/simulation/so_arm_101_description/meshes/LICENSE.md) · [简体中文](LICENSE.md) · [日本語](../../../../ja/simulation/so_arm_101_description/meshes/LICENSE.md) · [हिन्दी](../../../../hi/simulation/so_arm_101_description/meshes/LICENSE.md) · [العربية](../../../../ar/simulation/so_arm_101_description/meshes/LICENSE.md)

[英文原文](../../../../../../simulation/so_arm_101_description/meshes/LICENSE.md)

[简体中文](../../../README.md)

> 完整机器翻译，尚未经母语使用者审核。图像、代码、CAD 和原始 PDF 为共用文件。如有歧义，请参阅英文原文。
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="licensing-of-the-meshes-in-this-directory"></a>
# 本目录中的网格许可

**这个目录是混杂的.** 不是每一个网格都属于 Robonine所以,
许可证以文件而不是指南分配.

`collision/` 含有由 `visual/` 通过
`../scripts/generate_collision_meshes.py`. 每个船体都携带相同的许可证
它的视觉网格.

| 文件 (在两个 `visual/` 和 `collision/`) | 许可证 | 版权所有 |
|---|---|---|
| `clamp_1.stl`, `clamp_2.stl` | CERN-OHL-P-2.0 | Robonine |
| `base_link.stl` | Apache-2.0 | TheRobotStudio |
| `link1_1.stl`, `link2_1.stl`, `link3_1.stl`, `link4_1.stl` | Apache-2.0 | TheRobotStudio |
| `link5_1.stl` | Apache-2.0 | 混合 ⁇ 见下面 |

<a id="upstream-geometry"></a>
## 上游几何

`base_link.stl` 和 `link1_1.stl` … `link4_1.stl` 是 SO-ARM101 **双臂**,
来自上游的 [SO-ARM100/101 项目
TheRobotStudio](https://github.com/TheRobotStudio/SO-ARM100) 并重新分配
下面 Apache-2.0. 这项项目并没有设计那种几何. 查看库
`NOTICE`.

<a id="link5_1stl--fused-mesh"></a>
## `link5_1.stl` ⁇  合并网

`link5_1.stl` 是单个网格,将上游的 SO-ARM101 手腕
Robonine's `RB9.01.062.010 Main frame`. 整个文件分布在
**Apache-2.0**: Robonine 无法授予 CERN-OHL-P-2.0 在几何学上,它没有
免费授权自己的部分 Apache-2.0.

通过将其重新出口为两个单独的网格,
许可证. 在此之前,请将文件视为 Apache-2.0 在全部.

<a id="robonine-geometry"></a>
## Robonine 几何

`clamp_1.stl` 和 `clamp_2.stl` 是 Robonine自己的设计
`RB9.01.062.021 Clamp` 合并与 `RB9.01.062.031 Gear rack`. 他们开放
下面的硬件 CERN-OHL-P-2.0:

```
Copyright (c) 2025 Robonine

This source describes Open Hardware and is licensed under the CERN-OHL-P v2.
You may redistribute and modify this source and make products using it under
the terms of the CERN-OHL-P v2 (https://ohwr.org/cern_ohl_p_v2.txt).

This source is distributed WITHOUT ANY EXPRESS OR IMPLIED WARRANTY, INCLUDING
OF MERCHANTABILITY, SATISFACTORY QUALITY AND FITNESS FOR A PARTICULAR PURPOSE.

SPDX-License-Identifier: CERN-OHL-P-2.0
```

看看 `LICENSING.md` 在存储库根中查看完整的许可证地图.
<!-- /translated-content -->

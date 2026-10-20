<!-- translation-navigation -->
[English](../../../../en/simulation/so_arm_101_description/meshes/LICENSE.md) · [Русский](../../../../ru/simulation/so_arm_101_description/meshes/LICENSE.md) · [Español](../../../../es/simulation/so_arm_101_description/meshes/LICENSE.md) · [Français](../../../../fr/simulation/so_arm_101_description/meshes/LICENSE.md) · [Deutsch](../../../../de/simulation/so_arm_101_description/meshes/LICENSE.md) · [Português (Brasil)](../../../../pt-BR/simulation/so_arm_101_description/meshes/LICENSE.md) · [简体中文](../../../../zh-CN/simulation/so_arm_101_description/meshes/LICENSE.md) · [日本語](LICENSE.md) · [हिन्दी](../../../../hi/simulation/so_arm_101_description/meshes/LICENSE.md) · [العربية](../../../../ar/simulation/so_arm_101_description/meshes/LICENSE.md)

[英語原文](../../../../../../simulation/so_arm_101_description/meshes/LICENSE.md)

[日本語](../../../README.md)

> 文書全体の機械翻訳です。母語話者による確認は未実施です。画像、コード、CAD、元の PDF は共通です。不明点は英語原文を参照してください。
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="licensing-of-the-meshes-in-this-directory"></a>
# このディレクトリにおけるメッシュのライセンス

**このディレクトリは混同している.** ネットワークの所有者は Robonineそして,
免許はファイルではなくディレクトリごとに割り当てられます.

`collision/` ⁇ 状の船体を含んでいる `visual/` による
`../scripts/generate_collision_meshes.py`. 各船体には同じ免許証があります
視覚網から生成されたもの

| ファイル (両方とも `visual/` そして `collision/`) | ライセンス | 著作権 |
|---|---|---|
| `clamp_1.stl`, `clamp_2.stl` | CERN-OHL-P-2.0 | Robonine |
| `base_link.stl` | Apache-2.0 | TheRobotStudio |
| `link1_1.stl`, `link2_1.stl`, `link3_1.stl`, `link4_1.stl` | Apache-2.0 | TheRobotStudio |
| `link5_1.stl` | Apache-2.0 | 混合物  ⁇  以下を参照 |

<a id="upstream-geometry"></a>
## 上流ジオメトリ

`base_link.stl` そして `link1_1.stl` … `link4_1.stl` は SO-ARM101 **腕**,
上流から生じる [SO-ARM100/101 プロジェクト
TheRobotStudio](https://github.com/TheRobotStudio/SO-ARM100) そして再分配された
下 Apache-2.0. このプロジェクトはその幾何学を設計しませんでした 資料庫を見る
`NOTICE`.

<a id="link5_1stl--fused-mesh"></a>
## `link5_1.stl` ⁇  溶けたマッシュ

`link5_1.stl` 上流を融合させる単一網である. SO-ARM101 手首
Robonine's `RB9.01.062.010 Main frame`. ファイル全体は
**Apache-2.0**: Robonine 譲渡できない CERN-OHL-P-2.0 ゲオメトリでは
自有で,自有部分のライセンスを自由に Apache-2.0.

二つの独立したメッシュとして再出力すれば、各部分に適切な
免許書 それまでは ファイルは Apache-2.0 完全に

<a id="robonine-geometry"></a>
## Robonine ジオメトリ

`clamp_1.stl` そして `clamp_2.stl` は Robonineデザインは
`RB9.01.062.021 Clamp` 合併した `RB9.01.062.031 Gear rack`. オープンです
下のハードウェア CERN-OHL-P-2.0:

```
Copyright (c) 2025 Robonine

This source describes Open Hardware and is licensed under the CERN-OHL-P v2.
You may redistribute and modify this source and make products using it under
the terms of the CERN-OHL-P v2 (https://ohwr.org/cern_ohl_p_v2.txt).

This source is distributed WITHOUT ANY EXPRESS OR IMPLIED WARRANTY, INCLUDING
OF MERCHANTABILITY, SATISFACTORY QUALITY AND FITNESS FOR A PARTICULAR PURPOSE.

SPDX-License-Identifier: CERN-OHL-P-2.0
```

見てください `LICENSING.md` ライセンスマップの完全なリポジトリルーツに
<!-- /translated-content -->

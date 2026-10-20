<!-- translation-navigation -->
[English](../../../en/simulation/so_arm_101_description/LICENSE.md) · [Русский](../../../ru/simulation/so_arm_101_description/LICENSE.md) · [Español](../../../es/simulation/so_arm_101_description/LICENSE.md) · [Français](../../../fr/simulation/so_arm_101_description/LICENSE.md) · [Deutsch](../../../de/simulation/so_arm_101_description/LICENSE.md) · [Português (Brasil)](../../../pt-BR/simulation/so_arm_101_description/LICENSE.md) · [简体中文](../../../zh-CN/simulation/so_arm_101_description/LICENSE.md) · [日本語](LICENSE.md) · [हिन्दी](../../../hi/simulation/so_arm_101_description/LICENSE.md) · [العربية](../../../ar/simulation/so_arm_101_description/LICENSE.md)

[英語原文](../../../../../simulation/so_arm_101_description/LICENSE.md)

[日本語](../../README.md)

> 文書全体の機械翻訳です。母語話者による確認は未実施です。画像、コード、CAD、元の PDF は共通です。不明点は英語原文を参照してください。
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="licensing-of-this-package"></a>
# このパッケージのライセンス

`so_arm_101_description` 配分は,
[SO-ARM100/101 平行グリッパー](https://github.com/roboninecom/SO-ARM100-101-Parallel-Gripper)
複数のライセンスを持つプロジェクトです このファイルはパッケージを記述します
設置または再分配された場合,自明である.

| 内容 | ライセンス | 著作権 |
|---|---|---|
| `urdf/`, `config/`, `launch/`, `scripts/`, `test/`, `worlds/`, `docker/`, `so_arm_101_description/`, `setup.py`, `package.xml` | Apache-2.0 | Robonine |
| `meshes/` | **混合物** ⁇ 参照 [`meshes/LICENSE.md`](meshes/LICENSE.md) | 混合物 |

<a id="meshes--read-before-reusing"></a>
## 再利用前に読み取れるメッシュ

`meshes/` 単一のライセンスがない場合:

- `clamp_1.stl`, `clamp_2.stl` は Robonine握手体の幾何学 **CERN-OHL-P-2.0**.
- `base_link.stl`, `link1_1.stl` … `link4_1.stl` は SO-ARM101 **腕**産物
  上流から [SO-ARM100/101 プロジェクト
  TheRobotStudio](https://github.com/TheRobotStudio/SO-ARM100) ライセンス付き
  **Apache-2.0**. 彼らはそうではない Robonine仕事だ
- `link5_1.stl` 腕の上流ジオメトリを Robonine基本のフレームは
  単体で **Apache-2.0** 完全に

下のロボットの記述 `urdf/` ソフトウェアとしてではなく
ハードウェア:全腕の кинеマティックと慣性パラメータをコードする
その中,上流幾何学を記述する Robonine 持っていない.

リポジトリのルーツに完全なライセンスのテキストが表示されます. `HARDWARE-LICENSE.txt`,
`SOFTWARE-LICENSE.txt` そして `DOCS-LICENSE.txt` (またSPDXの名前で)
中 `LICENSES/`,REUSE規格が要求する). 参照 `LICENSING.md`
完全な地図については `NOTICE` 第三者による属性について,および `REUSE.toml` について
機械で読むバージョン.
<!-- /translated-content -->

<!-- translation-navigation -->
[English](../../../en/simulation/so_arm_101_description/LICENSE.md) · [Русский](../../../ru/simulation/so_arm_101_description/LICENSE.md) · [Español](../../../es/simulation/so_arm_101_description/LICENSE.md) · [Français](../../../fr/simulation/so_arm_101_description/LICENSE.md) · [Deutsch](../../../de/simulation/so_arm_101_description/LICENSE.md) · [Português (Brasil)](../../../pt-BR/simulation/so_arm_101_description/LICENSE.md) · [简体中文](LICENSE.md) · [日本語](../../../ja/simulation/so_arm_101_description/LICENSE.md) · [हिन्दी](../../../hi/simulation/so_arm_101_description/LICENSE.md) · [العربية](../../../ar/simulation/so_arm_101_description/LICENSE.md)

[英文原文](../../../../../simulation/so_arm_101_description/LICENSE.md)

[简体中文](../../README.md)

> 完整机器翻译，尚未经母语使用者审核。图像、代码、CAD 和原始 PDF 为共用文件。如有歧义，请参阅英文原文。
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="licensing-of-this-package"></a>
# 本包的许可

`so_arm_101_description` 作为
[SO-ARM100/101 平行夹爪](https://github.com/roboninecom/SO-ARM100-101-Parallel-Gripper)
项目是多个许可证的. 这档案描述了包裹,所以它是
在单独安装或重新分配时自行解释.

| 内容 | 许可证 | 版权所有 |
|---|---|---|
| `urdf/`, `config/`, `launch/`, `scripts/`, `test/`, `worlds/`, `docker/`, `so_arm_101_description/`, `setup.py`, `package.xml` | Apache-2.0 | Robonine |
| `meshes/` | **混合物** ⁇ 见 [`meshes/LICENSE.md`](meshes/LICENSE.md) | 混合物 |

<a id="meshes--read-before-reusing"></a>
## 在重复使用之前读取的网格

`meshes/` 没有统一许可证:

- `clamp_1.stl`, `clamp_2.stl` 是 Robonine它们的地质, **CERN-OHL-P-2.0**.
- `base_link.stl`, `link1_1.stl` … `link4_1.stl` 是 SO-ARM101 **双臂**衍生品
  从上游 [SO-ARM100/101 项目
  TheRobotStudio](https://github.com/TheRobotStudio/SO-ARM100) 有许可证
  **Apache-2.0**. 他们不是 Robonine是工作.
- `link5_1.stl` 合并上游手腕几何 Robonine在一个
  单体,是 **Apache-2.0** 在全部.

下面的机器人描述 `urdf/` 作为软件而不是
硬件:它编码整个臂部的动力和惯性参数,很多
其中描述上游几何学 Robonine 没有拥有.

完整的许可文本在存储库根中存在 `HARDWARE-LICENSE.txt`,
`SOFTWARE-LICENSE.txt` 和 `DOCS-LICENSE.txt` (又以他们的SPDX名称)
在 `LICENSES/`根据REUSE规范要求). 查看 `LICENSING.md`
对于完整的地图, `NOTICE` 对于第三方归属,以及 `REUSE.toml` 对于
机器可读的版本.
<!-- /translated-content -->

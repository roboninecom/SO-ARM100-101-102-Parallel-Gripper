<!-- translation-navigation -->
[English](LICENSE.md) · [Русский](../../../ru/simulation/so_arm_101_description/LICENSE.md) · [Español](../../../es/simulation/so_arm_101_description/LICENSE.md) · [Français](../../../fr/simulation/so_arm_101_description/LICENSE.md) · [Deutsch](../../../de/simulation/so_arm_101_description/LICENSE.md) · [Português (Brasil)](../../../pt-BR/simulation/so_arm_101_description/LICENSE.md) · [简体中文](../../../zh-CN/simulation/so_arm_101_description/LICENSE.md) · [日本語](../../../ja/simulation/so_arm_101_description/LICENSE.md) · [हिन्दी](../../../hi/simulation/so_arm_101_description/LICENSE.md) · [العربية](../../../ar/simulation/so_arm_101_description/LICENSE.md)

[English source](../../../../../simulation/so_arm_101_description/LICENSE.md)

[English](../../README.md)

> Complete English source copy. Images, code, CAD, and original PDFs are shared.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="licensing-of-this-package"></a>
# Licensing of this package

`so_arm_101_description` is distributed as part of the
[SO-ARM100/101 Parallel Gripper](https://github.com/roboninecom/SO-ARM100-101-Parallel-Gripper)
project, which is multi-licensed. This file describes the package so it is
self-explanatory when installed or redistributed on its own.

| Contents | Licence | Copyright |
|---|---|---|
| `urdf/`, `config/`, `launch/`, `scripts/`, `test/`, `worlds/`, `docker/`, `so_arm_101_description/`, `setup.py`, `package.xml` | Apache-2.0 | Robonine |
| `meshes/` | **mixed** — see [`meshes/LICENSE.md`](meshes/LICENSE.md) | mixed |

<a id="meshes--read-before-reusing"></a>
## Meshes — read before reusing

`meshes/` is not uniformly licensed:

- `clamp_1.stl`, `clamp_2.stl` are Robonine's gripper geometry, **CERN-OHL-P-2.0**.
- `base_link.stl`, `link1_1.stl` … `link4_1.stl` are the SO-ARM101 **arm**, derived
  from the upstream [SO-ARM100/101 project by
  TheRobotStudio](https://github.com/TheRobotStudio/SO-ARM100) and licensed
  **Apache-2.0**. They are not Robonine's work.
- `link5_1.stl` fuses upstream wrist geometry with Robonine's main frame in a
  single body and is **Apache-2.0** in full.

The robot description under `urdf/` is licensed as software rather than as
hardware: it encodes kinematics and inertial parameters for the whole arm, much
of which describes upstream geometry that Robonine does not own.

Full licence texts live in the repository root as `HARDWARE-LICENSE.txt`,
`SOFTWARE-LICENSE.txt` and `DOCS-LICENSE.txt` (and again under their SPDX names
in `LICENSES/`, as the REUSE Specification requires). See also `LICENSING.md`
for the full map, `NOTICE` for third-party attribution, and `REUSE.toml` for the
machine-readable version.
<!-- /translated-content -->

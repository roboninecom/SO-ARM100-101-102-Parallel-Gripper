<!-- translation-navigation -->
[English](../../../en/simulation/so_arm_101_description/LICENSE.md) · [Русский](LICENSE.md) · [Español](../../../es/simulation/so_arm_101_description/LICENSE.md) · [Français](../../../fr/simulation/so_arm_101_description/LICENSE.md) · [Deutsch](../../../de/simulation/so_arm_101_description/LICENSE.md) · [Português (Brasil)](../../../pt-BR/simulation/so_arm_101_description/LICENSE.md) · [简体中文](../../../zh-CN/simulation/so_arm_101_description/LICENSE.md) · [日本語](../../../ja/simulation/so_arm_101_description/LICENSE.md) · [हिन्दी](../../../hi/simulation/so_arm_101_description/LICENSE.md) · [العربية](../../../ar/simulation/so_arm_101_description/LICENSE.md)

[Английский оригинал](../../../../../simulation/so_arm_101_description/LICENSE.md)

[Русский](../../README.md)

> Полный машинный перевод; носители языка его ещё не проверяли. Изображения, код, CAD и исходные PDF общие. При неоднозначности используйте английский оригинал.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="licensing-of-this-package"></a>
# Лицензирование данного пакета

`so_arm_101_description` распределяется в рамках
[SO-ARM100/101 Параллельный захват](https://github.com/roboninecom/SO-ARM100-101-Parallel-Gripper)
проект, который имеет многолицензию. Этот файл описывает пакет, так что он
самообъясняющийся при установке или перераспределении в одиночку.

| Содержание | Лицензия | Авторские права |
|---|---|---|
| `urdf/`, `config/`, `launch/`, `scripts/`, `test/`, `worlds/`, `docker/`, `so_arm_101_description/`, `setup.py`, `package.xml` | Apache-2.0 | Robonine |
| `meshes/` | **смешанная** ⁇  см. [`meshes/LICENSE.md`](meshes/LICENSE.md) | смешанная |

<a id="meshes--read-before-reusing"></a>
## Маши  ⁇  читать перед повторным использованием

`meshes/` не имеет единообразной лицензии:

- `clamp_1.stl`, `clamp_2.stl` являются RobonineГеометрия захвата, **CERN-OHL-P-2.0**.
- `base_link.stl`, `link1_1.stl` … `link4_1.stl` Это SO-ARM101 **рукой**, полученные
  из потока [SO-ARM100/101 проект по
  TheRobotStudio](https://github.com/TheRobotStudio/SO-ARM100) и лицензированный
  **Apache-2.0**. Это не так. RobonineЭто работа.
- `link5_1.stl` сливается с геометрией запястья RobonineГлавная рама в
  единое тело и является **Apache-2.0** В полном объеме.

Описание робота ниже `urdf/` лицензируется как программное обеспечение, а не как
аппаратное обеспечение: он кодирует кинематику и инерционные параметры для всей руки, много
из которых описывается геометрия вверх по течению, которая Robonine не владеет.

Полный текст лицензии находится в корне хранилища как `HARDWARE-LICENSE.txt`,
`SOFTWARE-LICENSE.txt` и `DOCS-LICENSE.txt` (и снова под названием SPDX)
в `LICENSES/`, как это требует спецификация REUSE). См. также `LICENSING.md`
для полной карты, `NOTICE` для присвоения третьим лицам, и `REUSE.toml` для
машинночитаемая версия.
<!-- /translated-content -->

<!-- translation-navigation -->
[English](../../../en/simulation/so_arm_101_description/LICENSE.md) · [Русский](../../../ru/simulation/so_arm_101_description/LICENSE.md) · [Español](LICENSE.md) · [Français](../../../fr/simulation/so_arm_101_description/LICENSE.md) · [Deutsch](../../../de/simulation/so_arm_101_description/LICENSE.md) · [Português (Brasil)](../../../pt-BR/simulation/so_arm_101_description/LICENSE.md) · [简体中文](../../../zh-CN/simulation/so_arm_101_description/LICENSE.md) · [日本語](../../../ja/simulation/so_arm_101_description/LICENSE.md) · [हिन्दी](../../../hi/simulation/so_arm_101_description/LICENSE.md) · [العربية](../../../ar/simulation/so_arm_101_description/LICENSE.md)

[Original en inglés](../../../../../simulation/so_arm_101_description/LICENSE.md)

[Español](../../README.md)

> Traducción automática completa, aún sin revisión de hablantes nativos. Las imágenes, el código, CAD y PDF originales son compartidos. En caso de duda, consulte el original en inglés.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="licensing-of-this-package"></a>
# Licencia de este paquete

`so_arm_101_description` se distribuye como parte de la
[SO-ARM100/101 Pinza paralela](https://github.com/roboninecom/SO-ARM100-101-Parallel-Gripper)
proyecto, que tiene múltiples licencias. Este archivo describe el paquete así que es
autoexplicativo cuando se instala o redistribuye por sí solo.

| Contenidos | Licencia | Derecho de autor |
|---|---|---|
| `urdf/`, `config/`, `launch/`, `scripts/`, `test/`, `worlds/`, `docker/`, `so_arm_101_description/`, `setup.py`, `package.xml` | Apache-2.0 | Robonine |
| `meshes/` | **mezclado** ⁇  ver [`meshes/LICENSE.md`](meshes/LICENSE.md) | mezclado |

<a id="meshes--read-before-reusing"></a>
## Las redes  ⁇  se leen antes de reutilizarlas

`meshes/` no tiene una licencia uniforme:

- `clamp_1.stl`, `clamp_2.stl` son Roboninela geometría del agarre, **CERN-OHL-P-2.0**.
- `base_link.stl`, `link1_1.stl` … `link4_1.stl` ¿Son los SO-ARM101 **el brazo**, derivado
  desde el río arriba [SO-ARM100/101 proyecto por
  TheRobotStudio](https://github.com/TheRobotStudio/SO-ARM100) y con licencia
  **Apache-2.0**. No lo son . RobonineEs el trabajo.
- `link5_1.stl` fusiones geométricas de muñeca a la corriente con RobonineEl marco principal en un
  un solo cuerpo y es **Apache-2.0** En su totalidad.

La descripción del robot a continuación `urdf/` se ha licenciado como software en lugar de como
hardware: codifica kinemáticas y parámetros de inercia para todo el brazo, mucho
de los cuales se describe la geometría aguas arriba que Robonine no es dueño.

Los textos completos de las licencias se encuentran en la raíz del repositorio como `HARDWARE-LICENSE.txt`,
`SOFTWARE-LICENSE.txt` y `DOCS-LICENSE.txt` (y de nuevo bajo sus nombres SPDX
en el `LICENSES/`, según lo requiere la especificación REUSE). Vea también `LICENSING.md`
para el mapa completo, `NOTICE` para la atribución de terceros, y `REUSE.toml` para el
versión legible por máquina.
<!-- /translated-content -->

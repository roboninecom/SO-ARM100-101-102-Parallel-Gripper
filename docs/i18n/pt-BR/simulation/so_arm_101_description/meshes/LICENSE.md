<!-- translation-navigation -->
[English](../../../../en/simulation/so_arm_101_description/meshes/LICENSE.md) · [Русский](../../../../ru/simulation/so_arm_101_description/meshes/LICENSE.md) · [Español](../../../../es/simulation/so_arm_101_description/meshes/LICENSE.md) · [Français](../../../../fr/simulation/so_arm_101_description/meshes/LICENSE.md) · [Deutsch](../../../../de/simulation/so_arm_101_description/meshes/LICENSE.md) · [Português (Brasil)](LICENSE.md) · [简体中文](../../../../zh-CN/simulation/so_arm_101_description/meshes/LICENSE.md) · [日本語](../../../../ja/simulation/so_arm_101_description/meshes/LICENSE.md) · [हिन्दी](../../../../hi/simulation/so_arm_101_description/meshes/LICENSE.md) · [العربية](../../../../ar/simulation/so_arm_101_description/meshes/LICENSE.md)

[Original em inglês](../../../../../../simulation/so_arm_101_description/meshes/LICENSE.md)

[Português (Brasil)](../../../README.md)

> Tradução automática completa, ainda sem revisão de falantes nativos. Imagens, código, CAD e PDFs originais são compartilhados. Em caso de dúvida, consulte o original em inglês.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="licensing-of-the-meshes-in-this-directory"></a>
# Licenciamento das malhas deste diretório

**Este diretório é misturado.** Nem todas as malhas aqui são de propriedade de Robonine, então o
A licença é atribuída por arquivo e não por diretório.

`collision/` contém cascos convexos gerados a partir de `visual/` por
`../scripts/generate_collision_meshes.py`. Cada casco tem a mesma licença que
a malha visual da qual foi gerada.

| Arquivo (em ambos `visual/` e `collision/`) | Licença | Direitos de autor |
|---|---|---|
| `clamp_1.stl`, `clamp_2.stl` | CERN-OHL-P-2.0 | Robonine |
| `base_link.stl` | Apache-2.0 | TheRobotStudio |
| `link1_1.stl`, `link2_1.stl`, `link3_1.stl`, `link4_1.stl` | Apache-2.0 | TheRobotStudio |
| `link5_1.stl` | Apache-2.0 | misturados  ⁇  ver abaixo |

<a id="upstream-geometry"></a>
## Geometria a montante

`base_link.stl` e `link1_1.stl` … `link4_1.stl` são os SO-ARM101 **braço**,
derivados do fluxo ascendente [SO-ARM100/101 projeto por
TheRobotStudio](https://github.com/TheRobotStudio/SO-ARM100) e redistribuído
em Apache-2.0. Este projeto não desenhou essa geometria. Veja o repositório
`NOTICE`.

<a id="link5_1stl--fused-mesh"></a>
## `link5_1.stl` ⁇  malhas fundidas

`link5_1.stl` é uma única malha que funde a corrente superior SO-ARM101 pulso com
Robonine's `RB9.01.062.010 Main frame`. O arquivo inteiro é distribuído sob
**Apache-2.0**: Robonine não pode conceder CERN-OHL-P-2.0 sobre a geometria não
O Estado-Membro de origem é o responsável pela Apache-2.0.

A re-exportação deste como duas malhas separadas permitiria que cada parte carregasse sua própria
Licença. Até então, trate o ficheiro como Apache-2.0 - Não, não.

<a id="robonine-geometry"></a>
## Robonine Geometria

`clamp_1.stl` e `clamp_2.stl` são RobonineO próprio design
`RB9.01.062.021 Clamp` A partir da data de `RB9.01.062.031 Gear rack`. Estão abertas .
Ferramentas por baixo CERN-OHL-P-2.0:

```
Copyright (c) 2025 Robonine

This source describes Open Hardware and is licensed under the CERN-OHL-P v2.
You may redistribute and modify this source and make products using it under
the terms of the CERN-OHL-P v2 (https://ohwr.org/cern_ohl_p_v2.txt).

This source is distributed WITHOUT ANY EXPRESS OR IMPLIED WARRANTY, INCLUDING
OF MERCHANTABILITY, SATISFACTORY QUALITY AND FITNESS FOR A PARTICULAR PURPOSE.

SPDX-License-Identifier: CERN-OHL-P-2.0
```

Veja . `LICENSING.md` na raiz do repositório para o mapa completo da licença.
<!-- /translated-content -->

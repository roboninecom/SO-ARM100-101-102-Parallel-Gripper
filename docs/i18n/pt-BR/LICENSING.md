<!-- translation-navigation -->
[English](../en/LICENSING.md) · [Русский](../ru/LICENSING.md) · [Español](../es/LICENSING.md) · [Français](../fr/LICENSING.md) · [Deutsch](../de/LICENSING.md) · [Português (Brasil)](LICENSING.md) · [简体中文](../zh-CN/LICENSING.md) · [日本語](../ja/LICENSING.md) · [हिन्दी](../hi/LICENSING.md) · [العربية](../ar/LICENSING.md)

[Original em inglês](../../../LICENSING.md)

[Português (Brasil)](README.md)

> Tradução automática completa, ainda sem revisão de falantes nativos. Imagens, código, CAD e PDFs originais são compartilhados. Em caso de dúvida, consulte o original em inglês.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="licensing"></a>
# Licenciamento

Direito de autor (c) 2025 Robonine

Este projecto liberta diferentes tipos de material sob licenças diferentes.
Cada arquivo neste repositório está coberto por exatamente um deles.

| Materiais | Licença | Texto |
|---|---|---|
| Desenhos de hardware (CAD, geometria fabricável) | CERN-OHL-P-2.0 | [`HARDWARE-LICENSE.txt`](../../../HARDWARE-LICENSE.txt) |
| Software (código, configuração, CI, descrições de robôs) | Apache-2.0 | [`SOFTWARE-LICENSE.txt`](../../../SOFTWARE-LICENSE.txt) |
| Documentação, representações e fotografias | CC-BY-4.0 | [`DOCS-LICENSE.txt`](../../../DOCS-LICENSE.txt) |

A versão legível por máquina deste mapa é [`REUSE.toml`](../../../REUSE.toml), que
atribui uma licença a cada arquivo por caminho e é executada pelo `reuse lint` em
Pre-compromisso e CI. `LICENSES/` contém os mesmos três textos no seu SPDX
Nome, conforme exigido pela especificação REUSE.

**Alguns materiais aqui não são Robonine's.** Veja . [`NOTICE`](../../../NOTICE) para atribuição
e secção 4 abaixo para a lista precisa de ficheiros.

---

<a id="1-hardware--cern-ohl-p-20"></a>
## 1. Hardware  ⁇ CERN-OHL-P-2.0

```
models/                                             *.STEP, *.STL
models/parts/                                       *.STL
community/histology-slide-gripper/cad/              *.step, *.stl
community/histology-slide-gripper/mujoco/meshes/    base.stl, jaw_left.stl,
                                                    jaw_right.stl, pinion.stl
simulation/so_arm_101_description/meshes/visual/    clamp_1.stl, clamp_2.stl
simulation/so_arm_101_description/meshes/collision/ clamp_1.stl, clamp_2.stl
```

`README.md` Os arquivos dentro desses diretórios são documentação e caem sob
CC-BY-4.0Não , não . CERN-OHL-P-2.0.

Aviso recomendado para a reutilização deste hardware:

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
## 2. Software  ⁇ Apache-2.0

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

A descrição do robô abaixo `urdf/` é licenciado como software e não como
Hardware: codifica cinemática, inercias e limites articulares para todo o braço;
grande parte dos quais descreve a montante SO-ARM101 Geometria que Robonine não possui
e, por conseguinte, não pode colocar CERN-OHL-P-2.0. O agarrador fabricável
O design em si vive `models/` e está abrangida pela secção 1.

<a id="3-documentation--cc-by-40"></a>
## 3. Documentação CC-BY-4.0

```
README.md, CONTRIBUTING.md, LICENSING.md, RELICENSING.md
docs/                   *.md, *.pdf
assets/images/          *.png, *.PNG, *.jpg
every other README.md in the repository
community/histology-slide-gripper/assets/   *.png, *.jpg, *.gif
```

Atribuição para reutilização: "Robonine — SO-ARM100/101 Garra paralela,
https://github.com/roboninecom/SO-ARM100-101-Parallel-Gripper, CC BY 4.0".

<a id="4-mixed-and-third-party-material"></a>
## 4. Materiais mistos e de terceiros

Os seguintes são: **Não** abrangidos pela Robonine direitos autorais acima. Eles são
derivados do fluxo ascendente SO-ARM100/SO-ARM101 projeto por TheRobotStudio e são
redistribuído Apache-2.0. Veja . [`NOTICE`](../../../NOTICE).

```
simulation/so_arm_101_description/meshes/visual/     base_link.stl, link1_1.stl,
                                                     link2_1.stl, link3_1.stl,
                                                     link4_1.stl
simulation/so_arm_101_description/meshes/collision/  convex hulls of the above,
                                                     generated by
                                                     scripts/generate_collision_meshes.py
```

`link5_1.stl` (em ambas as `visual/` e `collision/`) é uma única malha que se funde
para cima do rio SO-ARM101 Geometria do pulso com Robonine's `RB9.01.062.010 Main frame`.
Até ser reexportado como duas malhas separadas, o arquivo inteiro é distribuído
em Apache-2.0: Robonine não pode conceder CERN-OHL-P-2.0 sobre a geometria não
O Estado-Membro de origem é o responsável pela Apache-2.0. A mesma geometria .
está disponível separadamente no CERN-OHL-P-2.0 como
`models/parts/RB9.01.062.010 Main frame.STL`.

`community/histology-slide-gripper/mujoco/meshes/arm/*.stl` são idênticos em byte
cópias de `simulation/so_arm_101_description/meshes/visual/*.stl` e herdar
A licença deles de lá  ⁇  por isso seis desses oito arquivos são material upstream,
Não RobonineÉ o trabalho.

`community/histology-slide-gripper/` foi contribuído por Michael Viacheslavov
([@histochemichael](https://github.com/histochemichael)) e é licenciada no
A mesma divisão tripartita; os direitos autorais são detidos pelo seu autor.

Veja . [`simulation/so_arm_101_description/meshes/LICENSE.md`](simulation/so_arm_101_description/meshes/LICENSE.md)
para a desagregação por arquivo desse diretório.
<!-- /translated-content -->

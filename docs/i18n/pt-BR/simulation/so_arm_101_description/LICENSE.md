<!-- translation-navigation -->
[English](../../../en/simulation/so_arm_101_description/LICENSE.md) · [Русский](../../../ru/simulation/so_arm_101_description/LICENSE.md) · [Español](../../../es/simulation/so_arm_101_description/LICENSE.md) · [Français](../../../fr/simulation/so_arm_101_description/LICENSE.md) · [Deutsch](../../../de/simulation/so_arm_101_description/LICENSE.md) · [Português (Brasil)](LICENSE.md) · [简体中文](../../../zh-CN/simulation/so_arm_101_description/LICENSE.md) · [日本語](../../../ja/simulation/so_arm_101_description/LICENSE.md) · [हिन्दी](../../../hi/simulation/so_arm_101_description/LICENSE.md) · [العربية](../../../ar/simulation/so_arm_101_description/LICENSE.md)

[Original em inglês](../../../../../simulation/so_arm_101_description/LICENSE.md)

[Português (Brasil)](../../README.md)

> Tradução automática completa, ainda sem revisão de falantes nativos. Imagens, código, CAD e PDFs originais são compartilhados. Em caso de dúvida, consulte o original em inglês.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="licensing-of-this-package"></a>
# Licença para o presente pacote

`so_arm_101_description` É distribuído como parte do
[SO-ARM100/101 Garra paralela](https://github.com/roboninecom/SO-ARM100-101-Parallel-Gripper)
Projeto, que é multi-licenciado. Este arquivo descreve o pacote para que seja
auto-explicativo quando instalado ou redistribuído por conta própria.

| Conteúdo | Licença | Direitos de autor |
|---|---|---|
| `urdf/`, `config/`, `launch/`, `scripts/`, `test/`, `worlds/`, `docker/`, `so_arm_101_description/`, `setup.py`, `package.xml` | Apache-2.0 | Robonine |
| `meshes/` | **misturados** ⁇  ver [`meshes/LICENSE.md`](meshes/LICENSE.md) | misturados |

<a id="meshes--read-before-reusing"></a>
## Mesas  ⁇  de leitura antes da reutilização

`meshes/` não tem uma licença uniforme:

- `clamp_1.stl`, `clamp_2.stl` são RobonineA geometria do agarrador, **CERN-OHL-P-2.0**.
- `base_link.stl`, `link1_1.stl` … `link4_1.stl` são os SO-ARM101 **braço**, derivado
  a partir da corrente superior [SO-ARM100/101 projeto por
  TheRobotStudio](https://github.com/TheRobotStudio/SO-ARM100) e licenciado
  **Apache-2.0**. Não são . RobonineÉ o trabalho.
- `link5_1.stl` fusões de geometria do pulso a montante com RobonineO quadro principal em um
  corpo único e é **Apache-2.0** - Não, não.

A descrição do robô abaixo `urdf/` é licenciado como software e não como
hardware: codifica cinemática e parâmetros de inercia para todo o braço, muito
dos quais descreve a geometria de montante que Robonine Não possui.

Os textos completos da licença estão presentes na raiz do repositório como `HARDWARE-LICENSE.txt`,
`SOFTWARE-LICENSE.txt` e `DOCS-LICENSE.txt` (e novamente sob os seus nomes SPDX
em `LICENSES/`, conforme exigido pela especificação REUSE). Veja também `LICENSING.md`
para o mapa completo, `NOTICE` para atribuição por terceiros, e `REUSE.toml` para o
versão legível por máquina.
<!-- /translated-content -->

<!-- translation-navigation -->
[English](../../../en/community/histology-slide-gripper/README.md) · [Русский](../../../ru/community/histology-slide-gripper/README.md) · [Español](../../../es/community/histology-slide-gripper/README.md) · [Français](../../../fr/community/histology-slide-gripper/README.md) · [Deutsch](../../../de/community/histology-slide-gripper/README.md) · [Português (Brasil)](README.md) · [简体中文](../../../zh-CN/community/histology-slide-gripper/README.md) · [日本語](../../../ja/community/histology-slide-gripper/README.md) · [हिन्दी](../../../hi/community/histology-slide-gripper/README.md) · [العربية](../../../ar/community/histology-slide-gripper/README.md)

[Original em inglês](../../../../../community/histology-slide-gripper/README.md)

[Português (Brasil)](../../README.md)

> Tradução automática completa, ainda sem revisão de falantes nativos. Imagens, código, CAD e PDFs originais são compartilhados. Em caso de dúvida, consulte o original em inglês.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="histology-slide-gripper-community-mod"></a>
# Histologia Gripper de deslizamento (Mod comunitário)

Uma variante comunitária da SO-ARM100/101 Gripper paralelo por [Michael Viacheslavov](https://github.com/histochemichael), adaptado para a automação histológica e histotecnológica: recolha suave de diapositivos do microscópio padrão 75 x 25 mm, coloração de diapositivos/racks e visualização por câmera da pegada.

<div align="center">

![Histologia demonstração de agarrador de deslizamento](../../../../../community/histology-slide-gripper/assets/histology-slide-gripper-demo.gif)

*SO-ARM100/101 Garrafa paralela que utiliza as pinças personalizadas para manipular os toboganos do microscópio e um carregador/rack de coloração.*

</div>

<a id="what-changed-vs-the-base-gripper"></a>
## O que mudou em relação ao Gripper Base

| Adição | Descrição |
|----------|-------------|
| Clemas de diapositivas para microscópios | Geometria de pinça larga e plana suporta a captura direta de diapositivos de microscópio padrão 75 x 25 mm. |
| Manutenção do rack de deslizamento/marca | O espaçamento e as pontas das pinças envolvem os dippers/racks de coloração de diapositivas, como o dipper de coloração de diapositivos Medicus Health ligado abaixo. |
| Retalhador de Arducam em ângulo | Um suportador impressable aponta uma câmera USB de fechadura global Arducam na mandíbula do agarrador para monitoramento próximo da captação de desliz e rack. |
| Montagem completa CAD | Um STL completo e editável STEP montagem estão em [`cad/`](../../../../../community/histology-slide-gripper/cad). |

<a id="gallery"></a>
## Galeria

<div align="center">

| Recuperação de diapositivas | Colocação de carrinho/recepção | Visualização do portador de Arducam |
|:-:|:-:|:-:|
| ![Clamp que segura um slide do microscópio](../../../../../community/histology-slide-gripper/assets/slide-gripper-single-slide.jpg) | ![Clamp alinhado com o deslizador de coloração](../../../../../community/histology-slide-gripper/assets/slide-gripper-staining-dipper.jpg) | ![Retalhador de arducam acima das mandíbulas do agarrador](../../../../../community/histology-slide-gripper/assets/arducam-holder-front.jpg) |

| Vista da frente | Geometria da mandíbula | Montagem isométrica |
|:-:|:-:|:-:|
| <img src="../../../../../community/histology-slide-gripper/assets/parallel-microscope-gripper-front.png" alt="Front CAD view of the microscope slide gripper mod" width="250"> | <img src="../../../../../community/histology-slide-gripper/assets/parallel-microscope-gripper-side.png" alt="Angled CAD view showing the microscope slide jaw geometry" width="250"> | <img src="../../../../../community/histology-slide-gripper/assets/parallel-microscope-gripper-isometric.png" alt="Isometric CAD view of the full microscope slide gripper assembly" width="250"> |

</div>

<a id="cad-files"></a>
## Arquivos CAD

| Arquivo | Formatar | Utilização |
|------|--------|-----|
| [`cad/the-parallel-microscope-slide-gripper.stl`](../../../../../community/histology-slide-gripper/cad/the-parallel-microscope-slide-gripper.stl) | LST | Montagem completa impressa para o mod de agarrador do microscópio. |
| [`cad/the-parallel-microscope-slide-gripper.step`](../../../../../community/histology-slide-gripper/cad/the-parallel-microscope-slide-gripper.step) | PASSO | Fonte CAD editável para a montagem completa. |

<a id="add-on-bill-of-materials"></a>
## Lista de materiais adicionais

Esses elementos são específicos do fluxo de trabalho da slide/rack e não fazem parte da sujeira base [BOM](../../docs/bom.md).

| Componente | Qty | Notas | Ligação |
|-----------|:---:|-------|------|
| Arducam 100fps Mono Global Shutter Câmara USB, OV9281 | 1 | Câmara usada com o segurador de ângulo para assistir deslizamento e rack pickup perto das mandíbulas. | [Amazon Reino Unido](https://www.amazon.co.uk/Arducam-Shutter-Distortion-Computer-Raspberry/dp/B0FXWWF55X) |
| Slide Dyeing Plastic Dipper com Manilha | 1+ | Referência de coloração para o alvo do carrinho/rack; concebido para deslizas padrão de 75 x 25 mm. | [Medicus Saúde](https://www.medicus-health.com/slide-staining-dipper.html) |
| Montagem de agarrador paralelo do microscópio | 1 | Impressão `the-parallel-microscope-slide-gripper.stl`; O arquivo STEP está incluído para edições. | [`cad/`](../../../../../community/histology-slide-gripper/cad) |

<a id="mujoco-simulation"></a>
## MuJoCo Simulação

<div align="center">

![SO-ARM101 Grifas de deslizamento de histologia MuJoCo](../../../../../community/histology-slide-gripper/mujoco/mujoco_simulation_preview.png)

*SO-ARM101 com o agarrador de deslizamento histológico montado e em funcionamento MuJoCo.*

</div>

Uma pessoa independente MuJoCo O modelo 3.4.0 está disponível em [`mujoco/`](mujoco/README.md). Inclui a totalidade SO-ARM101 Modelo, malhas de aderência, banco de testes de aderência independente, construção de guiões e um controle de agarrar e levantar sem cabeça.

A partir da raiz do repositório:

```bash
conda activate lerobot
cd community/histology-slide-gripper/mujoco
python -m pip install -r requirements.txt
python view.py
```

Usar o `sg_grip` controlo no MuJoCo O telespectador abre e fecha as mandíbulas. Veja o [simulação README](mujoco/README.md) para detalhes do modelo, controles, validação e instruções de reconstrução.

<a id="notes"></a>
## Notas

- Os dedos do agarrador são destinados a deslizas de microscópio e colocadores/racks para deslizas normais de 75 x 25 mm.
- A montagem mantém a visão da câmera direcionada para as mandíbulas do agarrador para que a câmera possa observar o deslizamento e a captura de rack.
- Teste primeiro com diapositivos não críticos e ajuste o material de impressão, a força do preenchimento e da aderência para o seu fluxo de trabalho.

<a id="links"></a>
## Links

- 🎥 [Demo: deslizamento e coloração de rack pickup (LinkedIn)](https://www.linkedin.com/posts/michael-viacheslavov_histology-histotechnology-robotics-ugcPost-7482570199859240960-Gqpw/)
<!-- /translated-content -->

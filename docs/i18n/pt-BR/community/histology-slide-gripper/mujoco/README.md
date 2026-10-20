<!-- translation-navigation -->
[English](../../../../en/community/histology-slide-gripper/mujoco/README.md) · [Русский](../../../../ru/community/histology-slide-gripper/mujoco/README.md) · [Español](../../../../es/community/histology-slide-gripper/mujoco/README.md) · [Français](../../../../fr/community/histology-slide-gripper/mujoco/README.md) · [Deutsch](../../../../de/community/histology-slide-gripper/mujoco/README.md) · [Português (Brasil)](README.md) · [简体中文](../../../../zh-CN/community/histology-slide-gripper/mujoco/README.md) · [日本語](../../../../ja/community/histology-slide-gripper/mujoco/README.md) · [हिन्दी](../../../../hi/community/histology-slide-gripper/mujoco/README.md) · [العربية](../../../../ar/community/histology-slide-gripper/mujoco/README.md)

[Original em inglês](../../../../../../community/histology-slide-gripper/mujoco/README.md)

[Português (Brasil)](../../../README.md)

> Tradução automática completa, ainda sem revisão de falantes nativos. Imagens, código, CAD e PDFs originais são compartilhados. Em caso de dúvida, consulte o original em inglês.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="microscope-slide-gripper-in-mujoco"></a>
# Gripper de diapositivas no microscópio MuJoCo

O SO-ARM101 com a aderência paralela de deslizamento histológico, exportada da Fusion e montada no lugar das sujeitas Robo9 do estoque.

Testeado com `mujoco` 3.4.0 no `lerobot` - O ambiente. - Não , não . ROS 2 Se o Docker for necessário.

```bash
conda activate lerobot
cd community/histology-slide-gripper/mujoco
python -m pip install -r requirements.txt
python view.py                      # full arm + slide gripper
python view.py scene_gripper.xml    # gripper alone on a testbench
python test_grasp.py                # headless grasp-and-lift check -> grasp_check.png
```

<a id="mujoco-simulation-preview"></a>
## MuJoCo Previsão de simulação

![SO-ARM101 Grifas de deslizamento de histologia MuJoCo](../../../../../../community/histology-slide-gripper/mujoco/mujoco_simulation_preview.png)

Esta cena mostra o SO-ARM101 com o agarrador paralelo de deslizamento histológico montado no
o pulso, usando o mesmo MuJoCo modelo lançado por:

```bash
conda activate lerobot
cd community/histology-slide-gripper/mujoco
python view.py
```

<a id="what-is-modelled"></a>
## O que é modelado

| Ligação | Fonte | Massa |
|---|---|---|
| `slide_gripper_base` | Estrutura principal, STS3215, barras de guia, rolamentos, suportes de câmera, Arducam OV9281 | 0.20kg |
| `sg_jaw_right` / `sg_jaw_left` | RB9.01.062.020 clamp + RB9.01.062.030 rack (m)0.8) | 0.035kg cada |
| `sg_pinion` | RB9.01.062.040 equipamento involuído,18 T, 0.8módulo | 0.008kg |

Cinemática extraída das articulações construídas no conjunto de fusão
(`Slide_Jaw_Right`, `Slide_Jaw_Left`, `Drive_Pinion`), que são auto-consistentes:
O18 T / 0.8Pinião do módulo tem um7.2Radius de ponta mm e7.2mm x4.9306Rad =
**35.5mm** de viagem por mandíbula  ⁇  exatamente os limites do deslizador no CAD.

<a id="control"></a>
## Controle

Um atuador, `sg_grip`, comandado em **Metros de viagem da mandíbula**:

| `ctrl` | viagem de mandíbula | abertura entre as faces da lâmina |
|---|---|---|
| `0.0` | 0 mm | **84 mm** (Totalmente aberto) |
| `0.0295` | 29.5mm | 25 mm (um slide do microscópio) |
| `0.0355` | 35.5mm | **13 mm** (totalmente fechado) |

Ambas as mandíbulas são movidas a partir do único pinião, por isso `sg_jaw_left_joint` e
`sg_pinion_joint` são escravos a `sg_jaw_right_joint` por `<equality>` restrições  ⁇
O equipamento gira visível com as mandíbulas. Comando *passado* O objeto a ser apertado:
fechar em um objeto de 25 mm com `ctrl=0.0355` dá sobre4.7N nas almofadas.

As cinco articulações do braço mantêm os seus nomes URDF (`base_link_to_link1` ... `link4_to_link5`).

<a id="collision-geometry"></a>
## Geometria de colisão

As redes geométricas são **Apenas visuais** (`contype=0`), porque MuJoCo Massas de carcas convexas e
O casco de uma mandíbula em forma de L preenche a lacuna com que está tentando agarrar. O contacto é
Carregadas por caixas nas duas superfícies de agarre de cada mandíbula (grupo 3, escondidas no
Renderings:

- `sg_pad_*` ⁇  a lâmina de deslizamento de 30 mm, CAD x 42 ⁇ 50, z 26 ⁇ 31
- `sg_mid_*` ⁇  a secção média mais ampla, CAD x 42 ⁇ 58, z 18.5 ⁇ 38.5

O site TCP `sg_tcp` Senta-se entre as lâminas; `sg_camera` é o quadro óptico Arducam.

<a id="files"></a>
## Arquivos

- `so101_slide_gripper.xml` ⁇  o robô completo (gerado por `build_full.py`)
- `scene_gripper.xml` ⁇  Grifas sozinhas, com eixo de elevação para ensaio
- `gripper_assets.xml` / `gripper_body.xml` / `gripper_actuation.xml` ⁇  o agarrador,
  que inclui usáveis tanto de modelos de unidade de graus como de radianos
- `meshes/{base,jaw_right,jaw_left,pinion}.stl` ⁇  exportados a partir de Fusion em **Montagem
  Coordenadas**, então cada parte já está no seu lugar certo (não por partes origens para perseguir)
- `meshes/arm/` ⁇  Mesas de braços do Robo9 repo
- `build_arm.py` ⁇  tiras xacro de `so_101.urdf.xacro`, deixa cair as pinças de estoque, compila para o MJCF
- `build_full.py` ⁇  Injecta o agarrador `link5`; **edição `MOUNT_POS`/`MOUNT_QUAT` Aqui está.**

<a id="how-the-gripper-was-located-on-the-wrist"></a>
## Como o agarrador foi localizado no pulso

`link5_1.stl` No Robo9 repo não é apenas o pulso  ⁇  contém todo o estoque
Grifas (quadro, barras de orientação, câmera). Então é a parte que o design da pega-slide substitui, e
`build_full.py` elimina a sua malha e deixa cair a sua massa de0.556kg a0.08Quatro quilos.

A posição da montanha foi resolvida, não adivinhou: `base.stl` foi montado contra
`link5_1.stl` sobre a geometria que compartilham (quadro principal + barras de guia) procurando todas as
24 rotações alinhadas com eixos e pontuação da distância vizinha mais próxima. A melhor forma é
**+90 graus aproximadamente X** (CAD + Y -> link)5+Z, CAD +Z -> link5-Y) com um2.0mm mediana
Residual  ⁇  as pinças de deslizamento penduradas perpendiculares às pinças pontiagudas do Robo9, correspondendo
O conjunto de fusão.

<a id="stability"></a>
## Estabilidade

O modelo estabelece-se em `max|qvel| = 0` E fica lá. Se alguma vez o virem tremer,
A primeira coisa a verificar são os contactos perdidos (`ncon` no painel de informações do espectador deve ser 0
com o braço em repouso). Três coisas eram necessárias:

1. **`<exclude body1="world" body2="link1_1"/>`** - a verdadeira solução. Importador da URDF
   fusões `base_link` em `worldbody`, e MuJoCo Salta colisões entre pais e filhos
   *exceto* Quando o pai é o corpo do mundo. Então a malha base e link1
   interpenetrada no ombro, produzindo um contato permanente que fixava o jargo
   atuador em seu +-1.5N.m limite. Isto só levou a resolver . `|qvel|` de4.78para0.
2. `sg_pinion_joint` Armatura 1e-6 -> **1e-4**. Uma articulação escravizada por uma rígida igualdade com
   Quase nenhuma conversa de inércia (estava a atingir o pico em 12 rad/s).
3. Igualdade `solref` 0.002 -> **0.01**. Uma constante de tempo de restrição igual ao passo temporal
   é muito rígido para resolver limpo; isto também fez o pinhão aterrar exatamente em-282.5DEG
   em vez de -280 graus.

<a id="caveats"></a>
## Cavernas

- **As massas são assumidas, não medidas.** A fusão informa cada corpo como aço (as mandíbulas)
  Saiam em221g); os valores acima referidos são estimativas de PLA e hardware. Se você
  atribuir materiais reais em Fusion, atualizar o `mass=` atributos em `gripper_body.xml`.
- A inercia é derivada por: MuJoCo da forma de malha mais essa massa, não do tensor da Fusão.
- Os limites articulares do braço, o amortecimento e a fricção são herdados da URDF do repo e
  não foram reajustadas.
- **As massas de ligação do braço também são densas em aço.**, o mesmo defeito que o agarrador:
  Total de depósitos URDF **2.81kg** em relação a aproximadamente 1 kg para um SO-101 real, e `link2_to_link3`
  necessidades1.91N.m para resistir a um1.5N.m limite do atuador, por isso desce. Isto é verdade.
  Não causa tremores (ver acima), mas faz o braço se comportar como um muito mais pesado
  Máquina. Escalando cada massa do braço e `diaginertia` Por ~0.36traz o total para
  1.19O volume de água em kg e elimina a saturação; o real STS3215 Também está mais perto.2.9N.m do que o
  A URDF é conservadora de 1.5.
- O resíduo de alinhamento de 2 mm é real: o "Folher principal frame_125" não é idêntico
  para o quadro cozido em `link5_1.stl`.
- `sg_pinion_joint` é cosmético - não carrega carga, porque as duas prateleiras estão acopladas
  um ao outro diretamente. Existe para que o engrenagem gire na direcção certa na tela.

<a id="driving-it-in-the-mujoco-viewer"></a>
## Conduzindo-o no MuJoCo telespectador

Usar o **`sg_grip` Deslizador no painel de controle**. Os deslizadores no *Juntas* painel
escrever `qpos` A Comissão propõe que os Estados-Membros, em conformidade com as disposições do Tratado de Maastricht e da Convenção
Quando estacionado) dessincroniza as mandíbulas do pinhão. A pressão Run reconverge-o.

<a id="re-exporting-after-a-cad-change"></a>
## Reexportação após uma alteração do CAD

A exportação foi efectuada através da conexão MCP Fusion:
corpos em quatro links rígidos, e escreve STLs binários em coordenadas de montagem
(mm). Re-exportação com o desenho Fusion aberto para refrescar as malhas em
Nada mais precisa de mudar a menos que se mova uma articulação.
<!-- /translated-content -->

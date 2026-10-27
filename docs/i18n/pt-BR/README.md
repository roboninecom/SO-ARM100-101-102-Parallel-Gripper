<!-- translation-navigation -->
[English](../en/README.md) · [Русский](../ru/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Deutsch](../de/README.md) · [Português (Brasil)](README.md) · [简体中文](../zh-CN/README.md) · [日本語](../ja/README.md) · [हिन्दी](../hi/README.md) · [العربية](../ar/README.md)

[Original em inglês](../../../README.md)

[Português (Brasil)](README.md)

> Tradução automática completa, ainda sem revisão de falantes nativos. Imagens, código, CAD e PDFs originais são compartilhados. Em caso de dúvida, consulte o original em inglês.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="so-arm100101-parallel-gripper"></a>
# SO-ARM100/101 Garra paralela

<div align="center">

[![SO-ARM101 Garra paralela](../../../assets/images/SO%20ARM%20101%20Parallel%20Gripper%20Live.jpg)](https://youtube.com/shorts/bSyXjgNGXZk)

**🎥 [Observe o agarrador em ação!](https://youtube.com/shorts/bSyXjgNGXZk)** · **🛒 [Compre o SO-ARM102 Kit com agarrador paralelo](https://robonine.com/shop/so-arm102-robotic-arm-kit/)**

Um agarrador paralelo leve impresso em 3D, concebido por: **[Robonine](https://robonine.com)** para o código aberto SO-ARM100/101 plataforma robótica.

> Prefere um kit completo de braços robóticos com uma agarrada paralela? **[Compre o SO-ARM102 kit](https://robonine.com/shop/so-arm102-robotic-arm-kit/)**.

[![Ferramentas: CERN-OHL-P-2.0](https://img.shields.io/badge/Hardware-CERN--OHL--P--2.0-blue.svg)](../../../HARDWARE-LICENSE.txt)
[![Software: Apache-2.0](https://img.shields.io/badge/Software-Apache--2.0-blue.svg)](../../../SOFTWARE-LICENSE.txt)
[![Docs: CC BY 4.0](https://img.shields.io/badge/Docs-CC%20BY%204.0-blue.svg)](../../../DOCS-LICENSE.txt)
[![Custo: ~$50](https://img.shields.io/badge/Cost-~%2450-green.svg)](docs/bom.md)
[![Assemblagem: 30 minutos](https://img.shields.io/badge/Assembly-30%20min-orange.svg)](docs/assembly-guide.md)

---

**Perguntas? Estamos aqui para ajudar!**
⁇  Email: [hello@robonine.com](mailto:hello@robonine.com)

</div>

---

<a id="-key-features"></a>
## ✨ Características-chave

| Características | Descrição |
|---------|-------------|
| **Força de agarramento 120N** | Mecanismo de maxilar paralelo confiável |
| **14 mm/s Velocidade** | Velocidade de operação do agarrador |
| **84 mm de golpe total** | Larga abertura para vários objetos |
| **0.5mm Repetibilidade** | Posicionamento de alta precisão |
| **Compatível com a câmera** | Suporte RealSense, Orbbec, câmeras USB |
| **Impressível em 3D** | Impressão de todas as peças em impressoras FDM padrão |
| **~$50Custo total** | Solução de código aberto acessível |
| **Assembleia fácil** | 30-45 minutos com ferramentas básicas |

---

<a id="-gallery"></a>
## Galeria

<div align="center">

<a id="gripper-on-so-arm101"></a>
### Garra no SO-ARM101

![Garra montada no SO-ARM101](../../../assets/images/specification/07-gripper-on-so-arm100.jpg)

*Garrafas de seguimento integradas com SO-ARM101 braço robótico*

<a id="dimensions"></a>
### Dimensões

![Dimensões da garra](../../../assets/images/specification/08-gripper-dimensions-3d.png)

*128 × 109 × 130.5mm, revestimento completo84mm*

</div>

---

<a id="-specifications"></a>
## ⁇  Especificações

<a id="gripper-parameters"></a>
### Parâmetros da garra

| Parâmetro | Valor |
|-----------|-------|
| Força máxima de agarre | **120 N** |
| Velocidade máxima de agarre | **14 mm/s** |
| Infracção total | **84 mm** |
| Repetibilidade | **0.5mm** |
| Massas de montagem (PLA, 30% de enchimento) | **170 g** |
| DOF | **1** |

<a id="dimensions-1"></a>
### Dimensões

| Dimensão | Valor |
|-----------|-------|
| Largura | 128 mm |
| Profundidade | 130.5mm |
| Altura | 109 mm |

<a id="servo-parameters-feetech-sts3215"></a>
### Parâmetros servo (Feetech STS3215)

| Parâmetro | Valor |
|-----------|-------|
| Voltagem de funcionamento | 12V |
| Torque de bloqueio | 30 kg·cm |
| Velocidade (sem carga) | 45 RPM |
| Encoder | Magnético absoluto de 12 bits |
| Protocolo | RS485/TTL até 1 Mbps |
| Temperatura de funcionamento | -20°C ~ 60°C |

---

<a id="-camera-compatibility"></a>
## ⁇  Compatibilidade com a câmera

O agarrador suporta várias câmeras através de um suportador interchangeável:

| Câmara | Tipo | Caso de utilização |
|--------|------|----------|
| IMX335 5MP USB | RGB | Funções básicas da visão |
| GC2093 USB de 2 MP | RGB | Opção orçamental |
| Orbbec Gémeos 2 | RGB-D | Percepção 3D |
| RealSense D405 | RGB-D | Profundidade de estreito alcance |
| RealSense D435/D435i | RGB-D | Propósito geral |
| RealSense D455 | RGB-D | Profundidade de longo alcance |

<div align="center">

![Diferentes câmeras montadas no agarrador](../../../assets/images/specification/09-camera-types.png)

*RealSense, módulo de câmera USB, Orbbec Gémeos 2*

</div>

---

<a id="-bill-of-materials"></a>
## ⁇  Concurso de materiais

**Custo total: ~$50** ([BOM completo com links Amazon](docs/bom.md))

| Categoria | Componentes | - Não. Custo |
|----------|------------|-----------|
| Eletrônica | Feetech STS3215 Servo | ~$29 |
| Rolamentos | MF106ZZ (x2) | ~$2 |
| Tubos de alumínio/carbono | D6x1x125mm (x2) | ~$4 |
| Impressão 3D | 8 peças (~ 100-150 g PLA) | ~$12 |
| Fixadores | Parafusos M2/M4, Nuts M2, Set de parafusos M3 | ~$3 |

---

<a id="-quick-start"></a>
## ⁇  Começo rápido

Para um conjunto completo de braços robóticos com agarrador paralelo, **[Compre o SO-ARM102 kit](https://robonine.com/shop/so-arm102-robotic-arm-kit/)**. Para construir o SO-ARM100/101 Segue os passos abaixo.

<a id="1-print-the-parts-2-4-hours"></a>
### 1. Impressão das peças (2-4 horas)

Descarregar arquivos STL de [`models/parts/`](models/README.md). Compatível com impressoras populares como **Bambu Lab A1 mini**, **Prusa MINI+**, e qualquer impressora com cama ≥ 180×180 mm.

| Parte | Qty | Configurações |
|------|:---:|----------|
| Estrutura principal (RB9.01.062.010) | 1 | 20% de enchimento |
| Mordente (RB9.01.062.020) | 2 | 20% de enchimento |
| Cremalheira (RB9.01.062.030) | 2 | 100% de enchimento |
| Engrenagem (RB9.01.062.040) | 1 | 100% de enchimento |
| Suporte da câmera (RB9.01.060.074) | 1 | 20% de enchimento |
| Suporte (RB9.01.060.080) | 1 | 20% de enchimento |
| Espaçador da câmera (RB9.01.060.090) | 1 | 20% de enchimento |
| D405 detentor (RB9.01.060.110) | 1 | 20% de enchimento |

<a id="2-order-components-1-2-days"></a>
### 2. Componentes da ordem (1-2 dias)

Veja . [Lista de Materiais](docs/bom.md) para ligações diretas da Amazon.

<a id="3-assemble-30-45-minutes"></a>
### 3. Reunião (30-45 minutos)

Seguir o [Guia de Assembleia](docs/assembly-guide.md) com imagens passo a passo:

1. Montar o engrenagem no servo disc, instalar este conjunto no servo
2. Inserir cabo de servo
3. Utilização Feetech software mover servo para a sua posição mínima (mover o deslizador no software para a esquerda)
4. Prenda as cremalheiras aos mordentes
5. Insira as hastes-guia nos dois mordentes
6. Instale os rolamentos na estrutura principal e fixe-os com parafusos
7. Encaixe as hastes-guia na estrutura
8. Afaste os mordentes até as posições extremas à esquerda e à direita
9. Insira o servo e fixa com parafusos
10. Aplicar a câmera de espaçamento e a câmera UVC, fixação com parafusos 4x e frutos secos M2 (facultativo)
11. Montagem para braço robótico (opcional)

<a id="4-software"></a>
### 4. Software

```bash
# Configure servo motor if necessary
https://lab.robonine.com/tools/robonine/feetech-bus

# Control gripper
https://lab.robonine.com/tools/robonine/control-robot
```

---

<a id="-repository-structure"></a>
## ⁇  Estrutura do repositório

```
├── assets/
│   └── images/
│       ├── assembly/          # Assembly step images
│       └── specification/     # Technical drawings
├── docs/
│   ├── assembly-guide.md                # Step-by-step assembly
│   ├── bom.md                           # Bill of materials with links
│   ├── Parallel gripper by Robo9.pdf    # Gripper product specification
│   ├── quick-start.md                   # Getting started guide
│   ├── SO-ARM101 by Robo9.pdf           # SO-ARM101 product specification
│   └── specifications.md               # Technical specifications
├── models/
│   ├── parts/                                    # Individual STL files
│   └── Follower gripper (165x165 bed size).STL   # Complete assembly (165×165mm bed)
├── community/
│   └── histology-slide-gripper/   # Community variant (CAD, MuJoCo model)
├── simulation/
│   ├── README.md                  # Simulation overview
│   ├── gazebo/                    # Gazebo guide
│   ├── mujoco/                    # MuJoCo guide
│   ├── webots/                    # Webots guide
│   ├── coppeliasim/               # CoppeliaSim guide
│   ├── isaac_sim/                 # Isaac Sim guide
│   └── so_arm_101_description/    # ROS2 package (URDF, launch, Docker)
├── software/
│   └── python/                # Control software
├── examples/                  # Usage examples
├── HARDWARE-LICENSE.txt       # CERN-OHL-P-2.0 (CAD, geometry)
├── SOFTWARE-LICENSE.txt       # Apache-2.0 (code)
├── DOCS-LICENSE.txt           # CC BY 4.0 (docs, images)
├── LICENSING.md               # Which licence covers what
├── NOTICE                     # Third-party attribution
├── REUSE.toml                 # Machine-readable licence map
├── RELICENSING.md             # Record of the 2026 relicensing
└── CONTRIBUTING.md
```

---

<a id="-documentation"></a>
## ⁇  Documentação

| Documento | Descrição |
|----------|-------------|
| [Guia de início rápido](docs/quick-start.md) | Vamos correr daqui a 30 minutos. |
| [Guia de Assembleia](docs/assembly-guide.md) | Passo a passo com imagens |
| [Guia de montagem do Gripper (PDF)](../../Assembly%20Guide%20Follower%20Gripper.pdf) | Instruções para a montagem do agarrador impressível |
| [SO-ARM101 Guia de montagem (PDF)](../../Assembly%20Guide%20SO-ARM101.pdf) | Com o máximo de SO-ARM101 instruções de montagem do braço |
| [Lista de Materiais](docs/bom.md) | Lista de peças com links Amazon |
| [Especificações](docs/specifications.md) | Detalhes técnicos |
| [Modelos 3D](models/README.md) | Impressão de configurações e arquivos |
| [Especificações do produto de pegamento paralelo (PDF)](../../Parallel%20gripper%20by%20Robo9.pdf) | Especificação do produto de aderente paralelo da Robo9 |
| [SO-ARM101 Especificações do produto (PDF)](../../SO-ARM101%20by%20Robo9.pdf) | SO-ARM101 especificação do produto de braço robótico da Robo9 |

---

<a id="-hardware-requirements"></a>
## ⁇  Requisitos de hardware

<a id="electronics"></a>
### Eletrônica
- 1× Feetech STS3215 Servo motor

Conectar o agarrador ao existente SO-ARM100/101 Servobus e controlador.
O controlador robótico e a alimentação fazem parte da configuração do braço, fora do agarrador BOM.

<a id="mechanical"></a>
### Mecânico
- 2× MF106ZZ Os rolamentos (6×10×3 mm)
- 2× Tubos de alumínio/carbono D6x1x125 mm

<a id="fasteners"></a>
### Fixadores
- 2 × M4 × 8 parafusos DIN 7991
- 4x M2x8 DIN 912 parafusos
- 4× M2 Nuts DIN 934
- 4× M3×4 DIN 913 parafusos definidos

<a id="tools-required"></a>
### Ferramentas necessárias
- Fornecedor de parafusos de cabeça Phillips (PH1)
- Chaves de hexagonal M2 (H1.5) e M4 (H2.5)

---

<a id="-simulation"></a>
## ⁇ ️ Simulação

O SO-ARM101 pode ser simulado em 5 motores de física usando um pacote de descrição ROS2 com um único URDF parametrizado. Não é necessário instalar ROS2: o Docker cuida de tudo.

<div align="center">

| Gazebo (Fortaleza da Ignição) | MuJoCo |
|:-:|:-:|
| ![SO-ARM-101 em Gazebo](../../../assets/images/simulation/gazebo/gazebo_pick_place.png) | ![SO-ARM-101 em MuJoCo](../../../assets/images/simulation/mujoco/mujoco_pick_place.png) |

</div>

| Simulador | Estatuto | Docker |
|-----------|--------|--------|
| [Gazebo](simulation/gazebo/README.md) | Pronto. | `docker compose run gazebo` |
| [MuJoCo](simulation/mujoco/README.md) | Pronto. | `docker compose run mujoco` |
| [Webots](simulation/webots/README.md) | Inestabilidade | `docker compose run webots` |
| [CoppeliaSim](simulation/coppeliasim/README.md) | Não testado | Simulador externo |
| [NVIDIA Isaac Sim](simulation/isaac_sim/README.md) | Não testado | Simulador externo |

**Começo rápido (Docker):**

```bash
cd simulation/so_arm_101_description
docker compose run gazebo    # or mujoco, webots
```

Veja o [Guia de simulação](simulation/README.md) Para configuração completa, detalhes de arquitetura e comando robótico.

---

<a id="-community-mods"></a>
## ⁇  Modos comunitários

Variantes do agarrador construídas pela comunidade, cada uma autónoma [`community/`](../../../community):

| Mod | Autor | Descrição |
|-----|--------|-------------|
| [Histologia Gripper de deslizamento](community/histology-slide-gripper/README.md) | [Michael Viacheslavov](https://github.com/histochemichael) | Clampes para deslizes de microscópio de 75 x 25 mm e cartuchos/racks de coloração, além de um suportador Arducam com ângulo para monitoramento da aderência. |

<div align="center">

<a href="community/histology-slide-gripper/README.md"><img src="../../../community/histology-slide-gripper/assets/slide-gripper-single-slide.jpg" alt="Histology slide gripper mod holding a microscope slide" width="400"></a>

*Histologia Slide Gripper mod  ⁇  clique para a descrição completa, arquivos CAD e demo*

</div>

---

<a id="-contributing"></a>
## ⁇  Contribuição

Acolhemos as contribuições! Por favor, sinta-se à vontade para:
- ⁇  Relatar erros e problemas
- ⁇  Sugerir novos recursos
- ⁇  Enviar pedidos de puxamento
- ⁇  Melhorar a documentação

---

<a id="-license"></a>
## ⁇  Licença

Direito de autor (c) 2025 Robonine. Este projecto é multi-licenciado  ⁇  diferentes tipos de
Material com diferentes licenças:

| Materiais | Licença |
|---|---|
| Projetos de hardware  ⁇ `models/`, CAD comunitário, malhas de aderência | [CERN-OHL-P-2.0](../../../HARDWARE-LICENSE.txt) |
| Software  ⁇ `software/`, `examples/`, `simulation/`, código de simulação em `community/` | [Apache-2.0](../../../SOFTWARE-LICENSE.txt) |
| Documentos e imagens  ⁇ `docs/`, `assets/`, todos `README.md` | [CC BY 4.0](../../../DOCS-LICENSE.txt) |

Veja . [`LICENSING.md`](LICENSING.md) para o mapa exacto de arquivo por arquivo e
[`REUSE.toml`](../../../REUSE.toml) para a versão legível por máquina.

**Nem tudo aqui é RobonineÉ o trabalho.** O SO-ARM101 são derivadas malhas de braço
de [TheRobotStudioÉ um projeto para cima .](https://github.com/TheRobotStudio/SO-ARM100)
e permanecer Apache-2.0; o agarrador de deslizamento histológico foi contribuído por
[@histochemichael](https://github.com/histochemichael). Veja . [`NOTICE`](../../../NOTICE)
antes de reutilizar qualquer malha.

Liberações até e incluindo `v0.3.1` foram publicadas sob a GPL-3.0 e permanecem
Disponível nos termos destes termos  ⁇  ver [`RELICENSING.md`](RELICENSING.md).

---

<a id="-links"></a>
## ⁇  Links

- [Feetech STS3215 Servo](https://www.feetechrc.com/525603.html)
- [STServo Python SDK](https://github.com/FEETECH-RC/STServo_SDK_Python)

---

<a id="-engineering-team"></a>
## ⁇  Equipa de Engenharia

| Nome | Função | Contacto |
|------|------|---------|
| **Boris Kotov** | Engenheiro de software | [Telegrama](https://t.me/bkotov) |
| **Alan Subin** | Engenheiro de Design | [Linkedin](https://www.linkedin.com/in/alan-subin/) |

---

<a id="-star-history"></a>
## ⭐ Histórico de estrelas

[![Histórico de estrelas](https://api.star-history.com/svg?repos=roboninecom/so-arm100-101-parallel-gripper&type=Date&legend=top-left)](https://www.star-history.com/?repos=roboninecom%2Fso-arm100-101-parallel-gripper&type=date&legend=top-left)

---

<div align="center">

**Construído para a comunidade robótica por [Robonine](https://robonine.com)** 🤖

**Perguntas? Estamos aqui para ajudar!**
⁇  Email: [hello@robonine.com](mailto:hello@robonine.com)

</div>
<!-- /translated-content -->

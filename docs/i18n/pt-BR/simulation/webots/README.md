<!-- translation-navigation -->
[English](../../../en/simulation/webots/README.md) · [Русский](../../../ru/simulation/webots/README.md) · [Español](../../../es/simulation/webots/README.md) · [Français](../../../fr/simulation/webots/README.md) · [Deutsch](../../../de/simulation/webots/README.md) · [Português (Brasil)](README.md) · [简体中文](../../../zh-CN/simulation/webots/README.md) · [日本語](../../../ja/simulation/webots/README.md) · [हिन्दी](../../../hi/simulation/webots/README.md) · [العربية](../../../ar/simulation/webots/README.md)

[Original em inglês](../../../../../simulation/webots/README.md)

[Português (Brasil)](../../README.md)

> Tradução automática completa, ainda sem revisão de falantes nativos. Imagens, código, CAD e PDFs originais são compartilhados. Em caso de dúvida, consulte o original em inglês.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="webots"></a>
# Webots

> **Status: Inestabilidade** -- Webots A integração funciona, mas tem problemas conhecidos de desempenho e renderização. Recomenda- se a utilização somente no Docker.

Webots Simulação utilizando `webots_ros2_control`. O Webots O motorista incorpora o gerente do controlador.

<a id="prerequisites"></a>
## Pre-requisitos

**Docker (recomendado):**
- Docker Desktop

**Indivíduo ROS2:**
- ROS2 Humilde
- [Webots](https://cyberbotics.com/) R2023b+
- `ros-humble-webots-ros2`
- `urdf2webots` Pacote de pip

<a id="launch"></a>
## Lançamento

<a id="docker"></a>
### Docker

```bash
cd simulation/so_arm_101_description
docker compose run webots
```

> **Nota**A: Webots O serviço de docking não tem volume montado. O arquivo do mundo é gerado dentro da imagem no momento de construção. Se modificar o URDF, deve reconstruir: `docker compose build webots`.

<a id="native-ros2"></a>
### Indivíduo ROS2

```bash
pip install urdf2webots

# Generate the Webots world file
python scripts/setup_webots.py

# Generate pre-expanded URDF for the Webots driver
xacro urdf/so_101.urdf.xacro sim_backend:=webots > urdf/so_101_webots.urdf

# Launch
ros2 launch so_arm_101_description sim.launch.py sim:=webots
```

<a id="how-it-works"></a>
## Como funciona

1. `scripts/setup_webots.py` transforma o URDF em um Webots Nodo de robô via `urdf2webots` e gera `worlds/webots_sim.wbt`
2. O `WebotsLauncher` abre o arquivo do mundo em Webots
3. `WebotsController` liga-se ao robô através do IPC e inicia a `ros2_control` motorista
4. O controlador `<extern>` Tag no arquivo mundo permite `webots_ros2_driver` para assumir
5. Um URDF pré-ampliado (`so_101_webots.urdf`) é necessária porque `WebotsController` requer um caminho de arquivo, não XML em linha

<a id="world-settings"></a>
### Configurações mundiais

- `basicTimeStep`: 16 ms (reduzido do padrão para estabilidade física)
- `maxContactJoints`: 4 (limita as despesas de colisão a partir das malhas detalhadas)

<a id="known-issues"></a>
## Questões conhecidas

- **Lenta carga mundial sobre X11**: O mundo leva ~ 120s para carregar quando o renderizado é encaminhado através de X11. O tempo limite do controlador é de 180s para acomodar isto.
- **Representação de tela em Windows**: VcXsrv fornece apenas OpenGL 1.4, mas Webots requer OpenGL 3.3. A simulação é executada, mas rende no modo de tela.
- **Detecção WSL2**: Docker em WSL2 herda o nome do kernel WSL, causando `webots_ros2_driver` para procurar `webots.exe`. Os patches do Dockerfile `is_wsl()` para voltar sempre `False`.
- **Alertas de Física**: "O seu mundo pode ser muito complexo" avisos podem aparecer devido a malhas de colisão de alto pólio.

<a id="troubleshooting"></a>
## Resolução de problemas

- **`WEBOTS_HOME` Não encontrados**Asegurar: `WEBOTS_HOME=/usr/local/webots` Está definido. A imagem do Docker define isto automaticamente.
- **Tempo de execução do controlador**: Se os controladores não se activarem, aumentar o tempo de intervalo em `launch/sim.launch.py` (atualmente 180 anos).
- **Sem exibição**: Webots Precisa de X11. No Windows, use VcXsrv com `-ac -wgl` bandeiras.
<!-- /translated-content -->

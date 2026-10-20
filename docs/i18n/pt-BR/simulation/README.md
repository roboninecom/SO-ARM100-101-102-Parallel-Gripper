<!-- translation-navigation -->
[English](../../en/simulation/README.md) · [Русский](../../ru/simulation/README.md) · [Español](../../es/simulation/README.md) · [Français](../../fr/simulation/README.md) · [Deutsch](../../de/simulation/README.md) · [Português (Brasil)](README.md) · [简体中文](../../zh-CN/simulation/README.md) · [日本語](../../ja/simulation/README.md) · [हिन्दी](../../hi/simulation/README.md) · [العربية](../../ar/simulation/README.md)

[Original em inglês](../../../../simulation/README.md)

[Português (Brasil)](../README.md)

> Tradução automática completa, ainda sem revisão de falantes nativos. Imagens, código, CAD e PDFs originais são compartilhados. Em caso de dúvida, consulte o original em inglês.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="simulation"></a>
# Simulação

ROS2 • a utilização de SO-ARM-101 braço robótico com aderência paralela. Um único URDF parametrizado impulsiona 5 motores de física através de um arquivo de lançamento.

<a id="gazebo-ignition-fortress"></a>
## Gazebo (Fortaleza da Ignição)

![SO-ARM-101 em Gazebo](../../../../assets/images/simulation/gazebo/gazebo_pick_place.png)

*SO-ARM-101 desempenhar pick & place em Gazebo O braço pega um objeto e coloca-o numa prateleira acima.*

<a id="mujoco"></a>
## MuJoCo

![SO-ARM-101 em MuJoCo](../../../../assets/images/simulation/mujoco/mujoco_pick_place.png)

*A mesma sequência de escolha e colocação em execução MuJoCo com simulação física completa.*

<a id="simulator-status"></a>
## Situação do simulador

| Simulador | Estatuto | Docker | Gestor do controlador |
|-----------|--------|--------|--------------------|
| [Gazebo - Sim , sim .](gazebo/README.md) | Pronto. | `docker compose run gazebo` | Incorporado no simulador |
| [MuJoCo](mujoco/README.md) | Pronto. | `docker compose run mujoco` | Externas (`ros2_control_node`) |
| [Webots](webots/README.md) | Inestabilidade | `docker compose run webots` | Embedded em driver |
| [CoppeliaSim](coppeliasim/README.md) | Não testado | N/A (simulação externa) | Externas (`ros2_control_node`) |
| [NVIDIA Isaac Sim](isaac_sim/README.md) | Não testado | N/A (simulação externa) | Externas (`ros2_control_node`) |

<a id="architecture"></a>
## Arquitetura

- **URDF único** -- `so_arm_101_description/urdf/so_101.urdf.xacro` é a única descrição do robô para todos os simuladores
- **Retrospectivas parametrizadas** -- `sim_backend:=gazebo|mujoco|webots|coppeliasim|isaac` seleciona o `ros2_control` Plugin no tempo de expansão do xacro
- **Controladores unificados** -- `config/controllers.yaml` define as mesmas articulações, interfaces e nomes do controlador em todos os backends
- **Um arquivo de lançamento** -- `launch/sim.launch.py` com `sim:=<backend>` Argumento

<a id="robot"></a>
### Robô

- **Braço 5 DOF**: rotação da base, ponta do ombro, cotovelo, ponta do pulso, rolamento do pulso
- **Garra paralela**: 2 articulações prismáticas de sujeira (espelhos do sujeiro esquerdo à direita via `<mimic>`)
- **Servos**: STS3215 (1.5Nm torque,5.2velocidade rad/s)

<a id="prerequisites"></a>
## Pre-requisitos

**Opção A: Docker (recomendado, não) ROS2 instalação necessária)**

- Docker Desktop

**Opção B: nativo ROS2**

- ROS2 Humilde
- Dependências específicas do simulador (ver guias por simulador)

<a id="installation"></a>
## Instalação

<a id="docker-recommended"></a>
### Docker (recomendado)

```bash
cd simulation/so_arm_101_description
docker compose run gazebo    # or mujoco, webots
```

<a id="native-ros2"></a>
### Indivíduo ROS2

```bash
# Copy the ROS2 package into your workspace
cp -r simulation/so_arm_101_description ~/ros2_ws/src/

# Install dependencies
cd ~/ros2_ws
rosdep install --from-paths src --ignore-src -r -y

# Build
colcon build --packages-select so_arm_101_description
source install/setup.bash
```

<a id="quick-start"></a>
## Começo rápido

```bash
# RViz visualization (no simulator needed)
ros2 launch so_arm_101_description display.launch.py

# Launch a simulator
ros2 launch so_arm_101_description sim.launch.py sim:=gazebo
ros2 launch so_arm_101_description sim.launch.py sim:=mujoco
ros2 launch so_arm_101_description sim.launch.py sim:=webots
ros2 launch so_arm_101_description sim.launch.py sim:=coppeliasim
ros2 launch so_arm_101_description sim.launch.py sim:=isaac
```

<a id="commanding-the-robot"></a>
## Comandando o Robô

```bash
# Check joint states
ros2 topic echo /joint_states --once

# Move arm via trajectory action
ros2 action send_goal /arm_controller/follow_joint_trajectory \
  control_msgs/action/FollowJointTrajectory "{
    trajectory: {
      joint_names: [base_link_to_link1, link1_to_link2, link2_to_link3, link3_to_link4, link4_to_link5],
      points: [{positions: [0.5, -0.5, 0.8, -0.3, 0.0], time_from_start: {sec: 2}}]
    }
  }"
```

<a id="docker-services"></a>
## Serviços do Docker

Todos os serviços são definidos em `so_arm_101_description/docker-compose.yaml`:

```bash
docker compose run build       # Interactive shell with built workspace
docker compose run validate    # Validate URDF for all 5 backends
docker compose run test        # Run 65 offline pytest tests
docker compose run check-launch # Verify launch files parse
docker compose run rviz        # RViz (needs X11)
docker compose run gazebo      # Gazebo (needs X11)
docker compose run mujoco      # MuJoCo (needs X11)
docker compose run webots      # Webots (needs X11)
```

<a id="collision-meshes"></a>
## Mesas de colisão

As redes de colisão do casco convexo simplificadas são fornecidas em `so_arm_101_description/meshes/collision/`. Para regenerar:

```bash
pip install trimesh
python scripts/generate_collision_meshes.py
```

<a id="package-structure"></a>
## Estrutura do pacote

```
so_arm_101_description/
├── urdf/
│   ├── so_101.urdf.xacro          # Main robot description
│   ├── so_101.ros2_control.xacro  # Parameterized hardware interface
│   └── materials.xacro
├── meshes/
│   ├── visual/                    # High-poly STL for rendering
│   └── collision/                 # Convex hull STL for physics
├── config/
│   ├── controllers.yaml           # Shared controller config
│   └── display.rviz
├── launch/
│   ├── display.launch.py          # RViz visualization
│   └── sim.launch.py              # Unified simulator launcher
├── worlds/
│   ├── empty.sdf                  # Gazebo world
│   └── webots_world.wbt           # Webots world
├── scripts/
│   ├── generate_collision_meshes.py
│   ├── publish_mujoco_description.py
│   ├── setup_webots.py
│   └── validate_xml.py
├── docker/
│   ├── entrypoint.sh
│   └── constrain-window.sh
├── test/                          # 65 offline tests
├── Dockerfile                     # Multi-stage (base/test/rviz/gazebo/mujoco/webots)
├── docker-compose.yaml
├── package.xml
└── setup.py
```
<!-- /translated-content -->

<!-- translation-navigation -->
[English](../../../en/simulation/gazebo/README.md) · [Русский](../../../ru/simulation/gazebo/README.md) · [Español](../../../es/simulation/gazebo/README.md) · [Français](../../../fr/simulation/gazebo/README.md) · [Deutsch](../../../de/simulation/gazebo/README.md) · [Português (Brasil)](README.md) · [简体中文](../../../zh-CN/simulation/gazebo/README.md) · [日本語](../../../ja/simulation/gazebo/README.md) · [हिन्दी](../../../hi/simulation/gazebo/README.md) · [العربية](../../../ar/simulation/gazebo/README.md)

[Original em inglês](../../../../../simulation/gazebo/README.md)

[Português (Brasil)](../../README.md)

> Tradução automática completa, ainda sem revisão de falantes nativos. Imagens, código, CAD e PDFs originais são compartilhados. Em caso de dúvida, consulte o original em inglês.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="gazebo-gz-sim"></a>
# Gazebo - Sim , sim .

**Status: Pronto**

Gazebo Simulação utilizando `gz_ros2_control` Plug-in. O gerente do controlador corre para dentro da Gazebo processo.

<a id="prerequisites"></a>
## Pre-requisitos

**Docker (recomendado):**
- Docker Desktop

**Indivíduo ROS2:**
- ROS2 Humilde
- `ros-humble-gz-ros2-control`
- `ros-humble-ros-gz-sim`
- `ros-humble-ros-gz-bridge`

<a id="launch"></a>
## Lançamento

<a id="docker"></a>
### Docker

```bash
cd simulation/so_arm_101_description
docker compose run gazebo
```

Para o NVIDIA GPU passthrough, não comentem `deploy:` Bloco de entrada `docker-compose.yaml`:

```yaml
deploy:
  resources:
    reservations:
      devices:
        - driver: nvidia
          count: all
          capabilities: [gpu]
```

<a id="native-ros2"></a>
### Indivíduo ROS2

```bash
ros2 launch so_arm_101_description sim.launch.py sim:=gazebo
```

<a id="how-it-works"></a>
## Como funciona

1. O Gazebo Plugin `gz_ros2_control/GazeboSimSystem` é selecionado através do `sim_backend:=gazebo` Argumento de xacro
2. Gazebo Embeds o gerente do controlador - não separado `ros2_control_node` necessária
3. O robô é criado para `worlds/empty.sdf` por via `ros_gz_sim create`
4. Os geradores de controladores começam depois `robot_state_publisher` Está a correr.

<a id="world-file"></a>
### Arquivo Mundial

`worlds/empty.sdf` prevê:
- Motor de física ODE (passo temporal)0.004s / 250Hz)
- Plano de terra (100x100m)
- Iluminação solar direcional

<a id="verify"></a>
## Verificar

```bash
# Joint states should be published at 50 Hz
ros2 topic echo /joint_states --once

# Move the arm
ros2 action send_goal /arm_controller/follow_joint_trajectory \
  control_msgs/action/FollowJointTrajectory "{
    trajectory: {
      joint_names: [base_link_to_link1],
      points: [{positions: [0.5], time_from_start: {sec: 2}}]
    }
  }"
```

<a id="troubleshooting"></a>
## Resolução de problemas

- **Não encontrados**Asegurar: `GZ_SIM_RESOURCE_PATH` Inclui o diretório das parcerias. O ponto de entrada do Docker define isto automaticamente.
- **Sem exibição**: Gazebo Precisa de um servidor X11. No Windows, use VcXsrv com `-ac` bandeira. No macOS, use o XQuartz.
- **Transmissão lenta**: Descomentar a GPU através do bloco `docker-compose.yaml` se tiver uma GPU NVIDIA.
<!-- /translated-content -->

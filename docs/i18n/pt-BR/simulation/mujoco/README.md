<!-- translation-navigation -->
[English](../../../en/simulation/mujoco/README.md) · [Русский](../../../ru/simulation/mujoco/README.md) · [Español](../../../es/simulation/mujoco/README.md) · [Français](../../../fr/simulation/mujoco/README.md) · [Deutsch](../../../de/simulation/mujoco/README.md) · [Português (Brasil)](README.md) · [简体中文](../../../zh-CN/simulation/mujoco/README.md) · [日本語](../../../ja/simulation/mujoco/README.md) · [हिन्दी](../../../hi/simulation/mujoco/README.md) · [العربية](../../../ar/simulation/mujoco/README.md)

[Original em inglês](../../../../../simulation/mujoco/README.md)

[Português (Brasil)](../../README.md)

> Tradução automática completa, ainda sem revisão de falantes nativos. Imagens, código, CAD e PDFs originais são compartilhados. Em caso de dúvida, consulte o original em inglês.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="mujoco"></a>
# MuJoCo

**Status: Pronto**

MuJoCo Simulação utilizando `mujoco_ros2_control` (forcão de controlo de rosas). MuJoCo converte o URDF em MJCF internamente e executa física + renderização no `ros2_control_node` processo.

<a id="prerequisites"></a>
## Pre-requisitos

**Docker (recomendado):**
- Docker Desktop

**Indivíduo ROS2:**
- ROS2 Humilde
- `mujoco_ros2_control` (construído a partir da fonte - ver abaixo)
- `mujoco` Pacote de pip

<a id="launch"></a>
## Lançamento

<a id="docker"></a>
### Docker

```bash
cd simulation/so_arm_101_description
docker compose run mujoco
```

A imagem do Docker constrói `mujoco_ros2_control` da fonte automaticamente.

<a id="native-ros2"></a>
### Indivíduo ROS2

```bash
# Clone dependencies into your workspace
cd ~/ros2_ws/src
git clone --depth 1 https://github.com/ros-controls/ros2_control_cmake.git
git clone --depth 1 https://github.com/pal-robotics/mujoco_vendor.git
git clone --depth 1 https://github.com/ros-controls/mujoco_ros2_control.git

# Build
cd ~/ros2_ws
colcon build --packages-up-to mujoco_ros2_control so_arm_101_description

# Launch
source install/setup.bash
ros2 launch so_arm_101_description sim.launch.py sim:=mujoco
```

<a id="how-it-works"></a>
## Como funciona

1. O plugin `mujoco_ros2_control/MujocoSystemInterface` é selecionado através `sim_backend:=mujoco`
2. Um nó personalizado (`publish_mujoco_description`) publica o URDF em `/mujoco_robot_description`
3. O MuJoCo O plugin lê o URDF, converte-o em MJCF e inicia a simulação
4. O `<mujoco><compiler meshdir=.../>` Tag no URDF diz MuJoCo onde encontrar malhas de colisão
5. Abre-se uma janela de renderização que mostra a simulação (1280x720, corrigida por padrão em tela inteira)

<a id="key-parameters-in-so_101ros2_controlxacro"></a>
### Parâmetros-chave `so_101.ros2_control.xacro`)

- `headless`Configuração: `true` para o modo sem cabeça (sem janela de renderização)
- `sim_speed_factor`: Multiplicador de velocidade de simulação (default:1.0)

<a id="verify"></a>
## Verificar

```bash
ros2 topic echo /joint_states --once

ros2 action send_goal /arm_controller/follow_joint_trajectory \
  control_msgs/action/FollowJointTrajectory "{
    trajectory: {
      joint_names: [base_link_to_link1, link1_to_link2, link2_to_link3, link3_to_link4, link4_to_link5],
      points: [{positions: [0.5, -0.5, 0.8, -0.3, 0.0], time_from_start: {sec: 2}}]
    }
  }"
```

<a id="troubleshooting"></a>
## Resolução de problemas

- **Erros em OpenGL**: Certifique-se de que os drivers da GPU estão instalados. Para o Docker, descomentar o bloqueio da GPU NVIDIA em `docker-compose.yaml`.
- **Janela muito grande**A imagem do Docker fixa a janela em 1280x720. Para instalações nativas, o MuJoCo A janela pode estar com tela inteira por padrão.
- **Sem exibição**: MuJoCo Precisa de um servidor X11 para a janela de renderização. Utilização `headless:=true` no xacro se não estiver disponível.
<!-- /translated-content -->

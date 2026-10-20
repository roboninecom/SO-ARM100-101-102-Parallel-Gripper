<!-- translation-navigation -->
[English](../../../en/simulation/coppeliasim/README.md) · [Русский](../../../ru/simulation/coppeliasim/README.md) · [Español](../../../es/simulation/coppeliasim/README.md) · [Français](../../../fr/simulation/coppeliasim/README.md) · [Deutsch](../../../de/simulation/coppeliasim/README.md) · [Português (Brasil)](README.md) · [简体中文](../../../zh-CN/simulation/coppeliasim/README.md) · [日本語](../../../ja/simulation/coppeliasim/README.md) · [हिन्दी](../../../hi/simulation/coppeliasim/README.md) · [العربية](../../../ar/simulation/coppeliasim/README.md)

[Original em inglês](../../../../../simulation/coppeliasim/README.md)

[Português (Brasil)](../../README.md)

> Tradução automática completa, ainda sem revisão de falantes nativos. Imagens, código, CAD e PDFs originais são compartilhados. Em caso de dúvida, consulte o original em inglês.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="coppeliasim"></a>
# CoppeliaSim

**Status: Não testado (simulador externo)**

CoppeliaSim corre externamente e comunica com ROS2 por via `topic_based_ros2_control`. Tu corres. CoppeliaSim separadamente e lançar o ROS2 lado com `sim:=coppeliasim`.

<a id="prerequisites"></a>
## Pre-requisitos

- [CoppeliaSim EDU/PRO](https://www.coppeliarobotics.com/downloads) v4.6+
- ROS2 Humilde
- `simROS2` Plugin habilitado em CoppeliaSim
- `topic_based_ros2_control`:
  ```bash
  sudo apt install ros-humble-topic-based-ros2-control
  ```

<a id="setup"></a>
## Configuração

<a id="1-import-urdf-into-coppeliasim"></a>
### 1. Importação de URDF CoppeliaSim

```bash
# Generate expanded URDF
source /opt/ros/humble/setup.bash
xacro so_arm_101_description/urdf/so_101.urdf.xacro sim_backend:=coppeliasim > /tmp/so_101_coppeliasim.urdf
```

No CoppeliaSim:
1. **Arquivo > Importação > URDF...**
2. Selecionar `/tmp/so_101_coppeliasim.urdf`
3. Verificação **Asignar formas de colisão a formas visíveis**
4. Verificação **Assegurar a massa e a inércia às formas**
5. Clique em **Importação**
6. Salvar a cena (opcional: `worlds/coppeliasim_scene.ttt`)

<a id="2-add-ros2-bridge-script"></a>
### 2. Adicionar ROS2 Escrito de ponte

O `topic_based_ros2_control` O plugin comunica através destes tópicos:

| Tópico | Tipo | Direcção |
|-------|------|-----------|
| `/joint_states` | `sensor_msgs/JointState` | CoppeliaSim -> ROS2 |
| `/joint_commands` | `std_msgs/Float64MultiArray` | ROS2 -> CoppeliaSim |

Adicionar um **guião infantil** para o link de base do robô com este código Lua:

```lua
function sysCall_init()
    -- Joint handles (order must match controllers.yaml)
    jointNames = {
        'base_link_to_link1', 'link1_to_link2', 'link2_to_link3',
        'link3_to_link4', 'link4_to_link5', 'right_clamp', 'left_clamp'
    }
    joints = {}
    for i, name in ipairs(jointNames) do
        joints[i] = sim.getObject('/' .. name)
    end

    -- ROS2 publisher for joint states
    statePub = simROS2.createPublisher('/joint_states', 'sensor_msgs/msg/JointState')

    -- ROS2 subscriber for joint commands
    cmdSub = simROS2.createSubscription('/joint_commands', 'std_msgs/msg/Float64MultiArray',
        'commandCallback')
end

function commandCallback(msg)
    for i, pos in ipairs(msg.data) do
        if joints[i] then
            sim.setJointTargetPosition(joints[i], pos)
        end
    end
end

function sysCall_sensing()
    local msg = {
        header = {stamp = simROS2.getSimulationTime(), frame_id = ''},
        name = jointNames,
        position = {},
        velocity = {},
        effort = {}
    }
    for i, j in ipairs(joints) do
        msg.position[i] = sim.getJointPosition(j)
        msg.velocity[i] = sim.getJointVelocity(j)
        msg.effort[i] = sim.getJointForce(j)
    end
    simROS2.publish(statePub, msg)
end

function sysCall_cleanup()
    simROS2.shutdownPublisher(statePub)
    simROS2.shutdownSubscription(cmdSub)
end
```

<a id="3-launch"></a>
### 3. Lançamento

```bash
# Terminal 1: Start CoppeliaSim with the scene loaded and press Play

# Terminal 2: Launch ROS2 side
ros2 launch so_arm_101_description sim.launch.py sim:=coppeliasim
```

<a id="verify"></a>
## Verificar

```bash
ros2 topic echo /joint_states --once

ros2 topic pub /arm_controller/joint_trajectory trajectory_msgs/msg/JointTrajectory "{
  joint_names: ['base_link_to_link1'],
  points: [{positions: [0.5], time_from_start: {sec: 2}}]
}" --once
```

<a id="troubleshooting"></a>
## Resolução de problemas

- **simROS2 não carregando**Asegurar: `libsimROS2.so` Está dentro CoppeliaSimPlug-in diretório e `ROS_DISTRO=humble` Está definido.
- **Nenhum Estado comum**: Verifique se o script Lua está ligado ao objeto correto e a simulação está em execução.
- **Descoincidência de nomes comuns**: Os nomes comuns na escrita Lua devem corresponder exatamente aos de `config/controllers.yaml`.
<!-- /translated-content -->

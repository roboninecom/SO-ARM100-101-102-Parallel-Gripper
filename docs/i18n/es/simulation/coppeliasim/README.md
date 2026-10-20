<!-- translation-navigation -->
[English](../../../en/simulation/coppeliasim/README.md) · [Русский](../../../ru/simulation/coppeliasim/README.md) · [Español](README.md) · [Français](../../../fr/simulation/coppeliasim/README.md) · [Deutsch](../../../de/simulation/coppeliasim/README.md) · [Português (Brasil)](../../../pt-BR/simulation/coppeliasim/README.md) · [简体中文](../../../zh-CN/simulation/coppeliasim/README.md) · [日本語](../../../ja/simulation/coppeliasim/README.md) · [हिन्दी](../../../hi/simulation/coppeliasim/README.md) · [العربية](../../../ar/simulation/coppeliasim/README.md)

[Original en inglés](../../../../../simulation/coppeliasim/README.md)

[Español](../../README.md)

> Traducción automática completa, aún sin revisión de hablantes nativos. Las imágenes, el código, CAD y PDF originales son compartidos. En caso de duda, consulte el original en inglés.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="coppeliasim"></a>
# CoppeliaSim

**Estado: No probado (simulador externo)**

CoppeliaSim se ejecuta externamente y comunica con ROS2 a través de `topic_based_ros2_control`. Tú huyes . CoppeliaSim separadamente y lanzar el ROS2 lado con `sim:=coppeliasim`.

<a id="prerequisites"></a>
## Pré-requisitos

- [CoppeliaSim EDU/PRO](https://www.coppeliarobotics.com/downloads) v4.6+
- ROS2 Humilde
- `simROS2` Plugin habilitado en CoppeliaSim
- `topic_based_ros2_control`:
  ```bash
  sudo apt install ros-humble-topic-based-ros2-control
  ```

<a id="setup"></a>
## Configuración

<a id="1-import-urdf-into-coppeliasim"></a>
### 1. Importar URDF en CoppeliaSim

```bash
# Generate expanded URDF
source /opt/ros/humble/setup.bash
xacro so_arm_101_description/urdf/so_101.urdf.xacro sim_backend:=coppeliasim > /tmp/so_101_coppeliasim.urdf
```

En el CoppeliaSim:
1. **Archivo > Importar > URDF...**
2. Seleccionar `/tmp/so_101_coppeliasim.urdf`
3. El cheque **Asignar formas de colisión a formas visibles**
4. El cheque **Asignar masa e inercia a las formas**
5. Haga clic **Importar**
6. Salvar la escena (opcional: `worlds/coppeliasim_scene.ttt`)

<a id="2-add-ros2-bridge-script"></a>
### 2. Añadir ROS2 Escrito del puente

El `topic_based_ros2_control` el plugin se comunica a través de estos temas:

| Título | Tipo | Dirección |
|-------|------|-----------|
| `/joint_states` | `sensor_msgs/JointState` | CoppeliaSim -> ROS2 |
| `/joint_commands` | `std_msgs/Float64MultiArray` | ROS2 -> CoppeliaSim |

Añadir una **guión infantil** al enlace de base del robot con este código Lua:

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
### 3. Lanzamiento

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
## Solución de problemas

- **simROS2 sin carga**Asegurar: `libsimROS2.so` está en CoppeliaSimel directorio de plugins y `ROS_DISTRO=humble` Está listo.
- **No hay estados comunes**: Compruebe si el script Lua está conectado al objeto correcto y la simulación se está ejecutando.
- **Desajuste de nombres comunes**: Los nombres comunes en la escritura Lua deben coincidir exactamente con los de `config/controllers.yaml`.
<!-- /translated-content -->

<!-- translation-navigation -->
[English](../../../en/simulation/coppeliasim/README.md) · [Русский](../../../ru/simulation/coppeliasim/README.md) · [Español](../../../es/simulation/coppeliasim/README.md) · [Français](../../../fr/simulation/coppeliasim/README.md) · [Deutsch](README.md) · [Português (Brasil)](../../../pt-BR/simulation/coppeliasim/README.md) · [简体中文](../../../zh-CN/simulation/coppeliasim/README.md) · [日本語](../../../ja/simulation/coppeliasim/README.md) · [हिन्दी](../../../hi/simulation/coppeliasim/README.md) · [العربية](../../../ar/simulation/coppeliasim/README.md)

[Englische Quelle](../../../../../simulation/coppeliasim/README.md)

[Deutsch](../../README.md)

> Vollständige maschinelle Übersetzung, noch nicht von Muttersprachlern geprüft. Bilder, Code, CAD und Original-PDFs werden gemeinsam genutzt. Im Zweifel gilt die englische Quelle.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="coppeliasim"></a>
# CoppeliaSim

**Status: Nicht getestet (externer Simulator)**

CoppeliaSim Sie ist von außen ausgeführt und mit ROS2 durch `topic_based_ros2_control`. Du fährst . CoppeliaSim Sie werden von der ROS2 Seite mit `sim:=coppeliasim`.

<a id="prerequisites"></a>
## Voraussetzungen

- [CoppeliaSim EDU/PRO](https://www.coppeliarobotics.com/downloads) v4.6+
- ROS2 Demütig
- `simROS2` Plugin aktiviert CoppeliaSim
- `topic_based_ros2_control`:
  ```bash
  sudo apt install ros-humble-topic-based-ros2-control
  ```

<a id="setup"></a>
## Einrichtung

<a id="1-import-urdf-into-coppeliasim"></a>
### 1. URDF-Import in CoppeliaSim

```bash
# Generate expanded URDF
source /opt/ros/humble/setup.bash
xacro so_arm_101_description/urdf/so_101.urdf.xacro sim_backend:=coppeliasim > /tmp/so_101_coppeliasim.urdf
```

In CoppeliaSim:
1. **Datei > Import > URDF...**
2. Auswahl `/tmp/so_101_coppeliasim.urdf`
3. Überprüfen **Kollisionsformen zu sichtbaren Formen zuordnen**
4. Überprüfen **Masse und Trägheit auf Formen zuweisen**
5. Klicken Sie **Importe**
6. Speichern Sie die Szene (optional: `worlds/coppeliasim_scene.ttt`)

<a id="2-add-ros2-bridge-script"></a>
### 2. Hinzufügen ROS2 Bridge Script

Die `topic_based_ros2_control` Plugin kommuniziert über diese Themen:

| Thema | Typ | Anleitung |
|-------|------|-----------|
| `/joint_states` | `sensor_msgs/JointState` | CoppeliaSim -> ROS2 |
| `/joint_commands` | `std_msgs/Float64MultiArray` | ROS2 -> CoppeliaSim |

Hinzufügen einer **Kinderbuch** auf die Basisverbindung des Roboters mit diesem Lua-Code:

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
### 3. Start

```bash
# Terminal 1: Start CoppeliaSim with the scene loaded and press Play

# Terminal 2: Launch ROS2 side
ros2 launch so_arm_101_description sim.launch.py sim:=coppeliasim
```

<a id="verify"></a>
## Überprüfen

```bash
ros2 topic echo /joint_states --once

ros2 topic pub /arm_controller/joint_trajectory trajectory_msgs/msg/JointTrajectory "{
  joint_names: ['base_link_to_link1'],
  points: [{positions: [0.5], time_from_start: {sec: 2}}]
}" --once
```

<a id="troubleshooting"></a>
## Fehlerbehebung

- **simROS2 nicht geladen**: Sicherstellen `libsimROS2.so` ist in CoppeliaSimDas Plugin-Verzeichnis und `ROS_DISTRO=humble` ist eingestellt.
- **Keine gemeinsamen Staaten**: Überprüfen Sie, ob das Lua-Skript an das richtige Objekt befestigt ist und die Simulation läuft.
- **Gemeinsame Namensunvereinbarkeit**: Gemeinsame Namen in der Lua Schrift müssen genau mit denen in `config/controllers.yaml`.
<!-- /translated-content -->

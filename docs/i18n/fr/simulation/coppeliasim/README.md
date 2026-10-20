<!-- translation-navigation -->
[English](../../../en/simulation/coppeliasim/README.md) · [Русский](../../../ru/simulation/coppeliasim/README.md) · [Español](../../../es/simulation/coppeliasim/README.md) · [Français](README.md) · [Deutsch](../../../de/simulation/coppeliasim/README.md) · [Português (Brasil)](../../../pt-BR/simulation/coppeliasim/README.md) · [简体中文](../../../zh-CN/simulation/coppeliasim/README.md) · [日本語](../../../ja/simulation/coppeliasim/README.md) · [हिन्दी](../../../hi/simulation/coppeliasim/README.md) · [العربية](../../../ar/simulation/coppeliasim/README.md)

[Source anglaise](../../../../../simulation/coppeliasim/README.md)

[Français](../../README.md)

> Traduction automatique intégrale, pas encore relue par des locuteurs natifs. Images, code, CAO et PDF originaux sont partagés. En cas de doute, consultez la source anglaise.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="coppeliasim"></a>
# CoppeliaSim

**Statut: Non testé (simulateur externe)**

CoppeliaSim fonctionne à l'extérieur et communique avec ROS2 à travers `topic_based_ros2_control`. Vous courez CoppeliaSim séparément et lancer le ROS2 côté avec `sim:=coppeliasim`.

<a id="prerequisites"></a>
## Préalabilités

- [CoppeliaSim EDU/PRO](https://www.coppeliarobotics.com/downloads) v4.6+
- ROS2 Humble
- `simROS2` Plugin activé dans CoppeliaSim
- `topic_based_ros2_control`:
  ```bash
  sudo apt install ros-humble-topic-based-ros2-control
  ```

<a id="setup"></a>
## Installation

<a id="1-import-urdf-into-coppeliasim"></a>
### 1. Importation de l'URDF dans CoppeliaSim

```bash
# Generate expanded URDF
source /opt/ros/humble/setup.bash
xacro so_arm_101_description/urdf/so_101.urdf.xacro sim_backend:=coppeliasim > /tmp/so_101_coppeliasim.urdf
```

Dans CoppeliaSim:
1. **Fichier > Importation > URDF...**
2. Sélectionner `/tmp/so_101_coppeliasim.urdf`
3. Vérifiez **Assigner des formes de collision à des formes visibles**
4. Vérifiez **Assigner la masse et l'inertie aux formes**
5. Cliquez sur **Les importations**
6. Enregistrer la scène (optionnel: `worlds/coppeliasim_scene.ttt`)

<a id="2-add-ros2-bridge-script"></a>
### 2. Ajouter ROS2 Scénario du pont

Les `topic_based_ros2_control` le plugin communique par l'intermédiaire de ces sujets:

| Thème | Type | Direction |
|-------|------|-----------|
| `/joint_states` | `sensor_msgs/JointState` | CoppeliaSim -> ROS2 |
| `/joint_commands` | `std_msgs/Float64MultiArray` | ROS2 -> CoppeliaSim |

Ajouter un **scénario pour enfants** au lien de base du robot avec ce code Lua:

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
### 3. Lancement

```bash
# Terminal 1: Start CoppeliaSim with the scene loaded and press Play

# Terminal 2: Launch ROS2 side
ros2 launch so_arm_101_description sim.launch.py sim:=coppeliasim
```

<a id="verify"></a>
## Vérifiez

```bash
ros2 topic echo /joint_states --once

ros2 topic pub /arm_controller/joint_trajectory trajectory_msgs/msg/JointTrajectory "{
  joint_names: ['base_link_to_link1'],
  points: [{positions: [0.5], time_from_start: {sec: 2}}]
}" --once
```

<a id="troubleshooting"></a>
## Résolution des problèmes

- **simROS2 non chargé**: Assurer `libsimROS2.so` est dans CoppeliaSimle répertoire des plugins et `ROS_DISTRO=humble` - C'est réglé.
- **Aucun État commun**: Vérifiez que le script Lua est attaché à l'objet correct et que la simulation fonctionne.
- **Non-conformité des noms communs**: Les noms communs dans l'écriture Lua doivent correspondre exactement à ceux de `config/controllers.yaml`.
<!-- /translated-content -->

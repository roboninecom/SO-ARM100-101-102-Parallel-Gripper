<!-- translation-navigation -->
[English](../../en/simulation/README.md) · [Русский](../../ru/simulation/README.md) · [Español](../../es/simulation/README.md) · [Français](README.md) · [Deutsch](../../de/simulation/README.md) · [Português (Brasil)](../../pt-BR/simulation/README.md) · [简体中文](../../zh-CN/simulation/README.md) · [日本語](../../ja/simulation/README.md) · [हिन्दी](../../hi/simulation/README.md) · [العربية](../../ar/simulation/README.md)

[Source anglaise](../../../../simulation/README.md)

[Français](../README.md)

> Traduction automatique intégrale, pas encore relue par des locuteurs natifs. Images, code, CAO et PDF originaux sont partagés. En cas de doute, consultez la source anglaise.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="simulation"></a>
# Simulation

ROS2 soutien à la simulation pour le SO-ARM-101 bracelet robotisé avec poignée parallèle. Une seule URDF paramétrisée entraîne 5 moteurs de physique à travers un fichier de lancement.

<a id="gazebo-ignition-fortress"></a>
## Gazebo (Forteresse de l'Ignition)

![SO-ARM-101 dans Gazebo](../../../../assets/images/simulation/gazebo/gazebo_pick_place.png)

*SO-ARM-101 effectuer le choix et la place dans Gazebo ⁇  le bras prend un objet et le place sur une étagère au-dessus.*

<a id="mujoco"></a>
## MuJoCo

![SO-ARM-101 dans MuJoCo](../../../../assets/images/simulation/mujoco/mujoco_pick_place.png)

*La même séquence de sélection et de placement MuJoCo avec une simulation physique complète.*

<a id="simulator-status"></a>
## Statut du simulateur

| Simulateur | Le statut | Docker | Gestionnaire du contrôleur |
|-----------|--------|--------|--------------------|
| [Gazebo Je vous en prie .](gazebo/README.md) | Je suis prêt. | `docker compose run gazebo` | Embedded dans le simulateur |
| [MuJoCo](mujoco/README.md) | Je suis prêt. | `docker compose run mujoco` | Externe (`ros2_control_node`) |
| [Webots](webots/README.md) | Instable | `docker compose run webots` | Embedded dans le conducteur |
| [CoppeliaSim](coppeliasim/README.md) | Ne pas testé | N/A (simulation externe) | Externe (`ros2_control_node`) |
| [NVIDIA Isaac Oui](isaac_sim/README.md) | Ne pas testé | N/A (simulation externe) | Externe (`ros2_control_node`) |

<a id="architecture"></a>
## Architecture

- **RDF unique** -- `so_arm_101_description/urdf/so_101.urdf.xacro` est la seule description de robot pour tous les simulateurs
- **Les arrière-plans paramétrisés** -- `sim_backend:=gazebo|mujoco|webots|coppeliasim|isaac` sélectionne le `ros2_control` Plugin au moment de l'expansion xacro
- **Contrôleurs unifiés** -- `config/controllers.yaml` définit les mêmes joints, interfaces et noms de contrôleurs sur tous les arrière-plans
- **Un fichier de lancement** -- `launch/sim.launch.py` avec `sim:=<backend>` arguments

<a id="robot"></a>
### Robots

- **bras 5 DOF**: rotation de la base, épaule, coude, poignet, rouleau du poignet
- **Pince parallèle**: 2 articulations prismatiques de clamp (reflecteurs de clamp gauche à droite via `<mimic>`)
- **Servoirs**: STS3215 (1.5Nm couple,5.2vitesse rad/s)

<a id="prerequisites"></a>
## Préalabilités

**Option A: Docker (recommandé, non) ROS2 installation nécessaire)**

- Tableau de bureau Docker

**Option B: Native ROS2**

- ROS2 Humble
- Dépendances spécifiques au simulateur (voir les guides par simulateur)

<a id="installation"></a>
## Installation

<a id="docker-recommended"></a>
### Docker (recommandé)

```bash
cd simulation/so_arm_101_description
docker compose run gazebo    # or mujoco, webots
```

<a id="native-ros2"></a>
### Native ROS2

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
## Un début rapide

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
## Le commandement du robot

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
## Services de dockers

Tous les services sont définis en: `so_arm_101_description/docker-compose.yaml`:

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
## Mesures de collision

Les réseaux de collision convexes simplifiés sont fournis dans `so_arm_101_description/meshes/collision/`. Pour régénérer:

```bash
pip install trimesh
python scripts/generate_collision_meshes.py
```

<a id="package-structure"></a>
## Structure du paquet

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

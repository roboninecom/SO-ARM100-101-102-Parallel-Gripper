<!-- translation-navigation -->
[English](../../en/simulation/README.md) · [Русский](../../ru/simulation/README.md) · [Español](../../es/simulation/README.md) · [Français](../../fr/simulation/README.md) · [Deutsch](README.md) · [Português (Brasil)](../../pt-BR/simulation/README.md) · [简体中文](../../zh-CN/simulation/README.md) · [日本語](../../ja/simulation/README.md) · [हिन्दी](../../hi/simulation/README.md) · [العربية](../../ar/simulation/README.md)

[Englische Quelle](../../../../simulation/README.md)

[Deutsch](../README.md)

> Vollständige maschinelle Übersetzung, noch nicht von Muttersprachlern geprüft. Bilder, Code, CAD und Original-PDFs werden gemeinsam genutzt. Im Zweifel gilt die englische Quelle.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="simulation"></a>
# Simulation

ROS2 Simulationsunterstützung für die SO-ARM-101 Roboterarm mit parallelem Griff. Ein einziges parametrierter URDF treibt 5 Physikmotoren durch eine Startdatei.

<a id="gazebo-ignition-fortress"></a>
## Gazebo (Ignition Festung)

![SO-ARM-101 in Gazebo](../../../../assets/images/simulation/gazebo/gazebo_pick_place.png)

*SO-ARM-101 die Auswahl und Platzierung in Gazebo ⁇  der Arm nimmt ein Objekt und legt es auf einem Regal oben.*

<a id="mujoco"></a>
## MuJoCo

![SO-ARM-101 in MuJoCo](../../../../assets/images/simulation/mujoco/mujoco_pick_place.png)

*Die gleiche Pick & Place-Sequenz läuft in MuJoCo Mit einer vollständigen Physik-Simulation.*

<a id="simulator-status"></a>
## Simulatorstatus

| Simulator | Status | Docker | Controller-Manager |
|-----------|--------|--------|--------------------|
| [Gazebo - Ich weiß .](gazebo/README.md) | Bereit ! | `docker compose run gazebo` | In Simulator eingebettet |
| [MuJoCo](mujoco/README.md) | Bereit ! | `docker compose run mujoco` | Externe (`ros2_control_node`) |
| [Webots](webots/README.md) | Unbeständig | `docker compose run webots` | Eingebettet in den Fahrer |
| [CoppeliaSim](coppeliasim/README.md) | Nicht getestet | N/A (externe Simulation) | Externe (`ros2_control_node`) |
| [NVIDIA Isaac - Ja .](isaac_sim/README.md) | Nicht getestet | N/A (externe Simulation) | Externe (`ros2_control_node`) |

<a id="architecture"></a>
## Architektur

- **Einheitliche URDF** -- `so_arm_101_description/urdf/so_101.urdf.xacro` ist die einzige Roboterbeschreibung für alle Simulatoren
- **Parameterierte Hinterläufe** -- `sim_backend:=gazebo|mujoco|webots|coppeliasim|isaac` wählt `ros2_control` Plugin zur Xacro-Erweiterungszeit
- **Einheitliche Steuergeräte** -- `config/controllers.yaml` definiert die gleichen Gelenke, Schnittstellen und Controller-Namen über alle Hintergründe
- **Eine Startdatei** -- `launch/sim.launch.py` mit `sim:=<backend>` Argumentation

<a id="robot"></a>
### Roboter

- **5-DOF Arm**: Basisrotation, Schulterpitch, Ellenbogen, Handgelenkpitch, Handgelenkroll
- **Parallelgreifer**: 2 prismatische Klemmgelenke (linker Klemmspiegel rechts über `<mimic>`)
- **Servos**: STS3215 (1.5Nm Drehmoment5.2Rad/s Geschwindigkeit)

<a id="prerequisites"></a>
## Voraussetzungen

**Option A: Docker (empfohlen, nein) ROS2 Installation notwendig)**

- Docker-Desktop

**Option B: Einheimische ROS2**

- ROS2 Demütig
- Simulator-spezifische Abhängigkeiten (siehe Leitfaden pro Simulator)

<a id="installation"></a>
## Installation

<a id="docker-recommended"></a>
### Docker (empfehlen)

```bash
cd simulation/so_arm_101_description
docker compose run gazebo    # or mujoco, webots
```

<a id="native-ros2"></a>
### Einheimische ROS2

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
## Ein schneller Start

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
## Kommando über den Roboter

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
## Docker-Dienste

Alle Dienstleistungen sind in `so_arm_101_description/docker-compose.yaml`:

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
## Kollisionsmeschen

Einfach vereinfachte konvexe Rumpf-Kollisionsmeschen sind in `so_arm_101_description/meshes/collision/`. Zur Regeneration:

```bash
pip install trimesh
python scripts/generate_collision_meshes.py
```

<a id="package-structure"></a>
## Verpackungsstruktur

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

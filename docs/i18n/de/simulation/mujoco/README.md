<!-- translation-navigation -->
[English](../../../en/simulation/mujoco/README.md) · [Русский](../../../ru/simulation/mujoco/README.md) · [Español](../../../es/simulation/mujoco/README.md) · [Français](../../../fr/simulation/mujoco/README.md) · [Deutsch](README.md) · [Português (Brasil)](../../../pt-BR/simulation/mujoco/README.md) · [简体中文](../../../zh-CN/simulation/mujoco/README.md) · [日本語](../../../ja/simulation/mujoco/README.md) · [हिन्दी](../../../hi/simulation/mujoco/README.md) · [العربية](../../../ar/simulation/mujoco/README.md)

[Englische Quelle](../../../../../simulation/mujoco/README.md)

[Deutsch](../../README.md)

> Vollständige maschinelle Übersetzung, noch nicht von Muttersprachlern geprüft. Bilder, Code, CAD und Original-PDFs werden gemeinsam genutzt. Im Zweifel gilt die englische Quelle.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="mujoco"></a>
# MuJoCo

**Status: Bereit**

MuJoCo Simulation mit `mujoco_ros2_control` (Ros-Kontrollen Gabel). MuJoCo Umwandelt den URDF in MJCF intern und führt Physik + Rendering im `ros2_control_node` Prozess.

<a id="prerequisites"></a>
## Voraussetzungen

**Docker (empfohlen):**
- Docker-Desktop

**Einheimische ROS2:**
- ROS2 Demütig
- `mujoco_ros2_control` (aus der Quelle - siehe unten)
- `mujoco` Pip-Package

<a id="launch"></a>
## Start

<a id="docker"></a>
### Docker

```bash
cd simulation/so_arm_101_description
docker compose run mujoco
```

Das Docker-Bild baut `mujoco_ros2_control` von der Quelle automatisch.

<a id="native-ros2"></a>
### Einheimische ROS2

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
## Wie funktioniert es?

1. Das Plugin `mujoco_ros2_control/MujocoSystemInterface` wird über `sim_backend:=mujoco`
2. Ein benutzerdefinierter Knoten (`publish_mujoco_description`) veröffentlicht den URDF `/mujoco_robot_description`
3. Die MuJoCo Plugin liest den URDF, konvertiert ihn in MJCF und startet die Simulation
4. Die `<mujoco><compiler meshdir=.../>` Tag in der URDF sagt MuJoCo wo man Kollisionsmaschen findet
5. Ein Rendering-Fenster öffnet sich, das die Simulation zeigt (1280x720, von der Standardbildschirmpartie abgebildet)

<a id="key-parameters-in-so_101ros2_controlxacro"></a>
### Schlüsselparameter (in `so_101.ros2_control.xacro`)

- `headless`Auf: `true` für den Kopflosem Modus (ohne Renderingfenster)
- `sim_speed_factor`: Simulationsgeschwindigkeitsmultiplikator (Standard: 1.0)

<a id="verify"></a>
## Überprüfen

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
## Fehlerbehebung

- **Fehler bei OpenGL**: Stellen Sie sicher, dass GPU-Treiber installiert sind. Für Docker, Kommentieren Sie den NVIDIA GPU Block in `docker-compose.yaml`.
- **Das Fenster ist zu groß.**Das Docker-Bild passt das Fenster auf 1280x720. Für native Installationen MuJoCo Das Fenster kann standardmäßig voller Bildschirm sein.
- **Keine Anzeige**: MuJoCo Benötigt einen X11-Server für das Rendering-Fenster. Verwendung `headless:=true` in der Xacro, wenn kein Display verfügbar ist.
<!-- /translated-content -->

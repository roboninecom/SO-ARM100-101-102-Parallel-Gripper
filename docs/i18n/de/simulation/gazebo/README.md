<!-- translation-navigation -->
[English](../../../en/simulation/gazebo/README.md) · [Русский](../../../ru/simulation/gazebo/README.md) · [Español](../../../es/simulation/gazebo/README.md) · [Français](../../../fr/simulation/gazebo/README.md) · [Deutsch](README.md) · [Português (Brasil)](../../../pt-BR/simulation/gazebo/README.md) · [简体中文](../../../zh-CN/simulation/gazebo/README.md) · [日本語](../../../ja/simulation/gazebo/README.md) · [हिन्दी](../../../hi/simulation/gazebo/README.md) · [العربية](../../../ar/simulation/gazebo/README.md)

[Englische Quelle](../../../../../simulation/gazebo/README.md)

[Deutsch](../../README.md)

> Vollständige maschinelle Übersetzung, noch nicht von Muttersprachlern geprüft. Bilder, Code, CAD und Original-PDFs werden gemeinsam genutzt. Im Zweifel gilt die englische Quelle.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="gazebo-gz-sim"></a>
# Gazebo - Ich weiß .

**Status: Bereit**

Gazebo Simulation mit `gz_ros2_control` Ein Plugin. Der Controller-Manager läuft in die Gazebo Prozess.

<a id="prerequisites"></a>
## Voraussetzungen

**Docker (empfohlen):**
- Docker-Desktop

**Einheimische ROS2:**
- ROS2 Demütig
- `ros-humble-gz-ros2-control`
- `ros-humble-ros-gz-sim`
- `ros-humble-ros-gz-bridge`

<a id="launch"></a>
## Start

<a id="docker"></a>
### Docker

```bash
cd simulation/so_arm_101_description
docker compose run gazebo
```

Für die NVIDIA-GPU-Pass durch `deploy:` Block in `docker-compose.yaml`:

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
### Einheimische ROS2

```bash
ros2 launch so_arm_101_description sim.launch.py sim:=gazebo
```

<a id="how-it-works"></a>
## Wie funktioniert es?

1. Die Gazebo Plugin `gz_ros2_control/GazeboSimSystem` wird über die `sim_backend:=gazebo` xacro Argument
2. Gazebo Einbettung des Controller-Managers - keine separate `ros2_control_node` Notwendig
3. Der Roboter wird in `worlds/empty.sdf` durch `ros_gz_sim create`
4. Controller-Spowner starten nach `robot_state_publisher` ist laufen

<a id="world-file"></a>
### Weltdatei

`worlds/empty.sdf` die folgenden Bestimmungen enthält:
- ODE-Physikmotor (Zeitstufe)0.004s / 250(Hz)
- Bodenfläche (100x100m)
- Sonnenbeleuchtung in Richtung

<a id="verify"></a>
## Überprüfen

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
## Fehlerbehebung

- **Nicht gefunden**: Sicherstellen `GZ_SIM_RESOURCE_PATH` enthält das Verzeichnis der Paketanteile. Das Docker-Eingangspunkt setzt das automatisch ein.
- **Keine Anzeige**: Gazebo Benötigt einen X11-Server. Auf Windows verwenden Sie VcXsrv mit `-ac` Flagge. Auf macOS benutzen Sie XQuartz.
- **Langsames Darstellen**: Uncomment die GPU durch den Block in `docker-compose.yaml` wenn Sie eine NVIDIA-GPU haben.
<!-- /translated-content -->

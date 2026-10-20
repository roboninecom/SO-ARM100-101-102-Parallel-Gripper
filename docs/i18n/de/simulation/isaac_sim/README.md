<!-- translation-navigation -->
[English](../../../en/simulation/isaac_sim/README.md) · [Русский](../../../ru/simulation/isaac_sim/README.md) · [Español](../../../es/simulation/isaac_sim/README.md) · [Français](../../../fr/simulation/isaac_sim/README.md) · [Deutsch](README.md) · [Português (Brasil)](../../../pt-BR/simulation/isaac_sim/README.md) · [简体中文](../../../zh-CN/simulation/isaac_sim/README.md) · [日本語](../../../ja/simulation/isaac_sim/README.md) · [हिन्दी](../../../hi/simulation/isaac_sim/README.md) · [العربية](../../../ar/simulation/isaac_sim/README.md)

[Englische Quelle](../../../../../simulation/isaac_sim/README.md)

[Deutsch](../../README.md)

> Vollständige maschinelle Übersetzung, noch nicht von Muttersprachlern geprüft. Bilder, Code, CAD und Original-PDFs werden gemeinsam genutzt. Im Zweifel gilt die englische Quelle.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="nvidia-isaac-sim"></a>
# NVIDIA Isaac - Ja .

**Status: Nicht getestet (externer Simulator)**

Isaac Sim läuft externe und kommuniziert mit ROS2 durch `topic_based_ros2_control`. Du fährst . Isaac Sim separat und starten Sie die ROS2 Seite mit `sim:=isaac`.

<a id="prerequisites"></a>
## Voraussetzungen

- [NVIDIA Isaac - Ja .](https://developer.nvidia.com/isaac-sim) 4.0+ (NVIDIA RTX-GPU benötigt)
- ROS2 Demütig
- Isaac - Ja . ROS2 Brücke aktiviert
- `topic_based_ros2_control`:
  ```bash
  sudo apt install ros-humble-topic-based-ros2-control
  ```

<a id="setup"></a>
## Einrichtung

<a id="1-import-urdf-into-isaac-sim"></a>
### 1. URDF-Import in Isaac - Ja .

```bash
# Generate expanded URDF
source /opt/ros/humble/setup.bash
xacro so_arm_101_description/urdf/so_101.urdf.xacro sim_backend:=isaac > /tmp/so_101_isaac.urdf
```

In Isaac - Ja .
1. **Isaac Utils > URDF-Einfuhrer**
2. **Eingabe-Datei**Auswahl: `/tmp/so_101_isaac.urdf`
3. **Einführungsort**: `/World/so_101`
4. **Typ des gemeinsamen Antriebs**Position:
5. **Fix Basisverbindung**: geprüft
6. Klicken Sie **Importe**
7. Fügen Sie ein Bodenflugzeug hinzu: **Erstellen > Physik > Bodenplan**
8. Ausgenommen als USD-Phasen (optional)

<a id="2-configure-ros2-bridge-omnigraph"></a>
### 2. Konfiguration ROS2 Brücke (Omnigraph)

Die `topic_based_ros2_control` Plugin kommuniziert über diese Themen:

| Thema | Typ | Anleitung |
|-------|------|-----------|
| `/joint_states` | `sensor_msgs/JointState` | Isaac Sim -> ROS2 |
| `/joint_commands` | `std_msgs/Float64MultiArray` | ROS2 -> Isaac - Ja . |

<a id="omnigraph-setup"></a>
#### UmniGraph-Einstellung

1. Öffnen **Fenster > Bildschrift > Aktionsdiagramm**
2. Erstellen Sie eine neue Aktionsgrafik
3. Fügen Sie diese Knoten hinzu:
   - **Auf der Wiedergabe Tick** (Vorlage Quelle)
   - **Isaac Lesen Sie Simulationszeit**
   - **ROS2 Veröffentlichung des Gemeinsamen Staates** -- verbinden `/World/so_101`
   - **ROS2 Unterzeichnen Sie den gemeinsamen Staat** - für die Empfangsbefehle
   - **Isaac Verknüpfungskontroller** - Befehle für Gelenke

4. Verbinden Sie das Diagramm:
   ```
   On Playback Tick -> Read Sim Time -> Publish Joint State
   On Playback Tick -> Subscribe Joint State -> Articulation Controller
   ```

5. Konfiguration **Veröffentlichung des Gemeinsamen Staates** Knoten:
   - `targetPrim`: `/World/so_101`
   - `topicName`: `/joint_states`

6. Konfiguration **Verknüpfungskontroller** Knoten:
   - `targetPrim`: `/World/so_101`
   - `jointNames`Alle:7Gemeinsame Namen von `config/controllers.yaml`

<a id="alternative-isaac_ros2_control"></a>
#### Alternative: isaac_ros2_control

Wenn `isaac_ros2_control` ist für Ihre Isaac Sim Version:

```bash
sudo apt install ros-humble-isaac-ros2-control
```

Dies ersetzt die OmniGraph-Einstellung durch eine direkte `ros2_control` Hardware-Schnittstelle.

<a id="3-launch"></a>
### 3. Start

```bash
# Terminal 1: Start Isaac Sim and press Play

# Terminal 2: Launch ROS2 side
ros2 launch so_arm_101_description sim.launch.py sim:=isaac
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

- **Importe von URDF scheitern**: Stellen Sie sicher, dass alle Mesh-Wege absolut sind. Erstellen Sie die URDF mit `xacro` Erstens - die `.xacro` Sie müssen direkt einreichen.
- **Keine gemeinsamen Staaten**: Überprüfen Sie, ob die OmniGraph-Anlage verbunden ist und Isaac Sim ist im Spielmodus.
- **Physikalische Instabilität**: In Physik-Szene-Eigenschaften setzen Sie den Lösungsmitteltyp auf TGS und erhöhen die Iterationszahl.
- **ROS2 Brücke nicht gefunden**: Die Erweiterung in **Fenster > Erweiterungen > ROS2 Brücke**.
<!-- /translated-content -->

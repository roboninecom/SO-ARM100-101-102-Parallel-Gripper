<!-- translation-navigation -->
[English](README.md) · [Русский](../../../ru/simulation/isaac_sim/README.md) · [Español](../../../es/simulation/isaac_sim/README.md) · [Français](../../../fr/simulation/isaac_sim/README.md) · [Deutsch](../../../de/simulation/isaac_sim/README.md) · [Português (Brasil)](../../../pt-BR/simulation/isaac_sim/README.md) · [简体中文](../../../zh-CN/simulation/isaac_sim/README.md) · [日本語](../../../ja/simulation/isaac_sim/README.md) · [हिन्दी](../../../hi/simulation/isaac_sim/README.md) · [العربية](../../../ar/simulation/isaac_sim/README.md)

[English source](../../../../../simulation/isaac_sim/README.md)

[English](../../README.md)

> Complete English source copy. Images, code, CAD, and original PDFs are shared.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="nvidia-isaac-sim"></a>
# NVIDIA Isaac Sim

**Status: Not tested (external simulator)**

Isaac Sim runs externally and communicates with ROS2 via `topic_based_ros2_control`. You run Isaac Sim separately and launch the ROS2 side with `sim:=isaac`.

<a id="prerequisites"></a>
## Prerequisites

- [NVIDIA Isaac Sim](https://developer.nvidia.com/isaac-sim) 4.0+ (requires NVIDIA RTX GPU)
- ROS2 Humble
- Isaac Sim ROS2 bridge enabled
- `topic_based_ros2_control`:
  ```bash
  sudo apt install ros-humble-topic-based-ros2-control
  ```

<a id="setup"></a>
## Setup

<a id="1-import-urdf-into-isaac-sim"></a>
### 1. Import URDF into Isaac Sim

```bash
# Generate expanded URDF
source /opt/ros/humble/setup.bash
xacro so_arm_101_description/urdf/so_101.urdf.xacro sim_backend:=isaac > /tmp/so_101_isaac.urdf
```

In Isaac Sim:
1. **Isaac Utils > URDF Importer**
2. **Input File**: select `/tmp/so_101_isaac.urdf`
3. **Import location**: `/World/so_101`
4. **Joint Drive Type**: Position
5. **Fix Base Link**: checked
6. Click **Import**
7. Add a ground plane: **Create > Physics > Ground Plane**
8. Save as USD stage (optional)

<a id="2-configure-ros2-bridge-omnigraph"></a>
### 2. Configure ROS2 Bridge (OmniGraph)

The `topic_based_ros2_control` plugin communicates via these topics:

| Topic | Type | Direction |
|-------|------|-----------|
| `/joint_states` | `sensor_msgs/JointState` | Isaac Sim -> ROS2 |
| `/joint_commands` | `std_msgs/Float64MultiArray` | ROS2 -> Isaac Sim |

<a id="omnigraph-setup"></a>
#### OmniGraph Setup

1. Open **Window > Visual Scripting > Action Graph**
2. Create a new Action Graph
3. Add these nodes:
   - **On Playback Tick** (event source)
   - **Isaac Read Simulation Time**
   - **ROS2 Publish Joint State** -- connect to `/World/so_101`
   - **ROS2 Subscribe Joint State** -- for receiving commands
   - **Isaac Articulation Controller** -- applies commands to joints

4. Connect the graph:
   ```
   On Playback Tick -> Read Sim Time -> Publish Joint State
   On Playback Tick -> Subscribe Joint State -> Articulation Controller
   ```

5. Configure **Publish Joint State** node:
   - `targetPrim`: `/World/so_101`
   - `topicName`: `/joint_states`

6. Configure **Articulation Controller** node:
   - `targetPrim`: `/World/so_101`
   - `jointNames`: all 7 joint names from `config/controllers.yaml`

<a id="alternative-isaac_ros2_control"></a>
#### Alternative: isaac_ros2_control

If `isaac_ros2_control` is available for your Isaac Sim version:

```bash
sudo apt install ros-humble-isaac-ros2-control
```

This replaces the OmniGraph setup with a direct `ros2_control` hardware interface.

<a id="3-launch"></a>
### 3. Launch

```bash
# Terminal 1: Start Isaac Sim and press Play

# Terminal 2: Launch ROS2 side
ros2 launch so_arm_101_description sim.launch.py sim:=isaac
```

<a id="verify"></a>
## Verify

```bash
ros2 topic echo /joint_states --once

ros2 topic pub /arm_controller/joint_trajectory trajectory_msgs/msg/JointTrajectory "{
  joint_names: ['base_link_to_link1'],
  points: [{positions: [0.5], time_from_start: {sec: 2}}]
}" --once
```

<a id="troubleshooting"></a>
## Troubleshooting

- **URDF import fails**: Ensure all mesh paths are absolute. Generate the URDF with `xacro` first -- do not import the `.xacro` file directly.
- **No joint states**: Verify the OmniGraph is connected and Isaac Sim is in Play mode.
- **Physics instability**: In Physics Scene properties, set solver type to TGS and increase iteration counts.
- **ROS2 bridge not found**: Enable the extension in **Window > Extensions > ROS2 Bridge**.
<!-- /translated-content -->

<!-- translation-navigation -->
[English](README.md) · [Русский](../../../ru/simulation/mujoco/README.md) · [Español](../../../es/simulation/mujoco/README.md) · [Français](../../../fr/simulation/mujoco/README.md) · [Deutsch](../../../de/simulation/mujoco/README.md) · [Português (Brasil)](../../../pt-BR/simulation/mujoco/README.md) · [简体中文](../../../zh-CN/simulation/mujoco/README.md) · [日本語](../../../ja/simulation/mujoco/README.md) · [हिन्दी](../../../hi/simulation/mujoco/README.md) · [العربية](../../../ar/simulation/mujoco/README.md)

[English source](../../../../../simulation/mujoco/README.md)

[English](../../README.md)

> Complete English source copy. Images, code, CAD, and original PDFs are shared.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="mujoco"></a>
# MuJoCo

**Status: Ready**

MuJoCo simulation using `mujoco_ros2_control` (ros-controls fork). MuJoCo converts the URDF to MJCF internally and runs physics + rendering in the `ros2_control_node` process.

<a id="prerequisites"></a>
## Prerequisites

**Docker (recommended):**
- Docker Desktop

**Native ROS2:**
- ROS2 Humble
- `mujoco_ros2_control` (built from source -- see below)
- `mujoco` pip package

<a id="launch"></a>
## Launch

<a id="docker"></a>
### Docker

```bash
cd simulation/so_arm_101_description
docker compose run mujoco
```

The Docker image builds `mujoco_ros2_control` from source automatically.

<a id="native-ros2"></a>
### Native ROS2

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
## How It Works

1. The plugin `mujoco_ros2_control/MujocoSystemInterface` is selected via `sim_backend:=mujoco`
2. A custom node (`publish_mujoco_description`) publishes the URDF to `/mujoco_robot_description`
3. The MuJoCo plugin reads the URDF, converts it to MJCF, and starts the simulation
4. The `<mujoco><compiler meshdir=.../>` tag in the URDF tells MuJoCo where to find collision meshes
5. A rendering window opens showing the simulation (1280x720, patched from full-screen default)

<a id="key-parameters-in-so_101ros2_controlxacro"></a>
### Key Parameters (in `so_101.ros2_control.xacro`)

- `headless`: Set to `true` for headless mode (no rendering window)
- `sim_speed_factor`: Simulation speed multiplier (default: 1.0)

<a id="verify"></a>
## Verify

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
## Troubleshooting

- **OpenGL errors**: Ensure GPU drivers are installed. For Docker, uncomment the NVIDIA GPU block in `docker-compose.yaml`.
- **Window too large**: The Docker image patches the window to 1280x720. For native installs, the MuJoCo window may be full-screen by default.
- **No display**: MuJoCo needs an X11 server for the rendering window. Use `headless:=true` in the xacro if no display is available.
<!-- /translated-content -->

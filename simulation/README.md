# Simulation

<!-- documentation-languages -->
[English](../docs/i18n/en/simulation/README.md) · [Русский](../docs/i18n/ru/simulation/README.md) · [Español](../docs/i18n/es/simulation/README.md) · [Français](../docs/i18n/fr/simulation/README.md) · [Deutsch](../docs/i18n/de/simulation/README.md) · [Português (Brasil)](../docs/i18n/pt-BR/simulation/README.md) · [简体中文](../docs/i18n/zh-CN/simulation/README.md) · [日本語](../docs/i18n/ja/simulation/README.md) · [हिन्दी](../docs/i18n/hi/simulation/README.md) · [العربية](../docs/i18n/ar/simulation/README.md)
<!-- /documentation-languages -->

ROS2 simulation support for the SO-ARM-101 robotic arm with parallel gripper. A single parameterized URDF drives 5 physics engines through one launch file.

## Gazebo (Ignition Fortress)

![SO-ARM-101 in Gazebo](../assets/images/simulation/gazebo/gazebo_pick_place.png)

*SO-ARM-101 performing pick & place in Gazebo — the arm picks an object and places it on a shelf above.*

## MuJoCo

![SO-ARM-101 in MuJoCo](../assets/images/simulation/mujoco/mujoco_pick_place.png)

*Same pick & place sequence running in MuJoCo with full physics simulation.*

## Simulator Status

| Simulator | Status | Docker | Controller Manager |
|-----------|--------|--------|--------------------|
| [Gazebo (gz-sim)](gazebo/README.md) | Ready | `docker compose run gazebo` | Embedded in simulator |
| [MuJoCo](mujoco/README.md) | Ready | `docker compose run mujoco` | External (`ros2_control_node`) |
| [Webots](webots/README.md) | Unstable | `docker compose run webots` | Embedded in driver |
| [CoppeliaSim](coppeliasim/README.md) | Not tested | N/A (external sim) | External (`ros2_control_node`) |
| [NVIDIA Isaac Sim](isaac_sim/README.md) | Not tested | N/A (external sim) | External (`ros2_control_node`) |

## Architecture

- **Single URDF** -- `so_arm_101_description/urdf/so_101.urdf.xacro` is the sole robot description for all simulators
- **Parameterized backends** -- `sim_backend:=gazebo|mujoco|webots|coppeliasim|isaac` selects the `ros2_control` plugin at xacro expansion time
- **Unified controllers** -- `config/controllers.yaml` defines the same joints, interfaces, and controller names across all backends
- **One launch file** -- `launch/sim.launch.py` with `sim:=<backend>` argument

### Robot

- **5-DOF arm**: base rotation, shoulder pitch, elbow, wrist pitch, wrist roll
- **Parallel gripper**: 2 prismatic clamp joints (left clamp mirrors right via `<mimic>`)
- **Servos**: STS3215 (1.5 Nm torque, 5.2 rad/s velocity)

## Prerequisites

**Option A: Docker (recommended, no ROS2 install needed)**

- Docker Desktop

**Option B: Native ROS2**

- ROS2 Humble
- Simulator-specific dependencies (see per-simulator guides)

## Installation

### Docker (recommended)

```bash
cd simulation/so_arm_101_description
docker compose run gazebo    # or mujoco, webots
```

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

## Quick Start

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

## Commanding the Robot

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

## Docker Services

All services are defined in `so_arm_101_description/docker-compose.yaml`:

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

## Collision Meshes

Simplified convex hull collision meshes are provided in `so_arm_101_description/meshes/collision/`. To regenerate:

```bash
pip install trimesh
python scripts/generate_collision_meshes.py
```

## Package Structure

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

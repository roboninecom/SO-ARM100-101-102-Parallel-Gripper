# Gazebo (gz-sim)

<!-- documentation-languages -->
[English](../../docs/i18n/en/simulation/gazebo/README.md) · [Русский](../../docs/i18n/ru/simulation/gazebo/README.md) · [Español](../../docs/i18n/es/simulation/gazebo/README.md) · [Français](../../docs/i18n/fr/simulation/gazebo/README.md) · [Deutsch](../../docs/i18n/de/simulation/gazebo/README.md) · [Português (Brasil)](../../docs/i18n/pt-BR/simulation/gazebo/README.md) · [简体中文](../../docs/i18n/zh-CN/simulation/gazebo/README.md) · [日本語](../../docs/i18n/ja/simulation/gazebo/README.md) · [हिन्दी](../../docs/i18n/hi/simulation/gazebo/README.md) · [العربية](../../docs/i18n/ar/simulation/gazebo/README.md)
<!-- /documentation-languages -->

**Status: Ready**

Gazebo simulation using `gz_ros2_control` plugin. The controller manager runs inside the Gazebo process.

## Prerequisites

**Docker (recommended):**
- Docker Desktop

**Native ROS2:**
- ROS2 Humble
- `ros-humble-gz-ros2-control`
- `ros-humble-ros-gz-sim`
- `ros-humble-ros-gz-bridge`

## Launch

### Docker

```bash
cd simulation/so_arm_101_description
docker compose run gazebo
```

For NVIDIA GPU passthrough, uncomment the `deploy:` block in `docker-compose.yaml`:

```yaml
deploy:
  resources:
    reservations:
      devices:
        - driver: nvidia
          count: all
          capabilities: [gpu]
```

### Native ROS2

```bash
ros2 launch so_arm_101_description sim.launch.py sim:=gazebo
```

## How It Works

1. The Gazebo plugin `gz_ros2_control/GazeboSimSystem` is selected via the `sim_backend:=gazebo` xacro argument
2. Gazebo embeds the controller manager -- no separate `ros2_control_node` needed
3. The robot is spawned into `worlds/empty.sdf` via `ros_gz_sim create`
4. Controller spawners start after `robot_state_publisher` is running

### World File

`worlds/empty.sdf` provides:
- ODE physics engine (timestep 0.004s / 250 Hz)
- Ground plane (100x100m)
- Directional sun lighting

## Verify

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

## Troubleshooting

- **Meshes not found**: Ensure `GZ_SIM_RESOURCE_PATH` includes the package share directory. The Docker entrypoint sets this automatically.
- **No display**: Gazebo needs an X11 server. On Windows, use VcXsrv with `-ac` flag. On macOS, use XQuartz.
- **Slow rendering**: Uncomment the GPU passthrough block in `docker-compose.yaml` if you have an NVIDIA GPU.

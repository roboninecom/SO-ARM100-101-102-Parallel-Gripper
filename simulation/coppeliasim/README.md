# CoppeliaSim

<!-- documentation-languages -->
[English](../../docs/i18n/en/simulation/coppeliasim/README.md) · [Русский](../../docs/i18n/ru/simulation/coppeliasim/README.md) · [Español](../../docs/i18n/es/simulation/coppeliasim/README.md) · [Français](../../docs/i18n/fr/simulation/coppeliasim/README.md) · [Deutsch](../../docs/i18n/de/simulation/coppeliasim/README.md) · [Português (Brasil)](../../docs/i18n/pt-BR/simulation/coppeliasim/README.md) · [简体中文](../../docs/i18n/zh-CN/simulation/coppeliasim/README.md) · [日本語](../../docs/i18n/ja/simulation/coppeliasim/README.md) · [हिन्दी](../../docs/i18n/hi/simulation/coppeliasim/README.md) · [العربية](../../docs/i18n/ar/simulation/coppeliasim/README.md)
<!-- /documentation-languages -->

**Status: Not tested (external simulator)**

CoppeliaSim runs externally and communicates with ROS2 via `topic_based_ros2_control`. You run CoppeliaSim separately and launch the ROS2 side with `sim:=coppeliasim`.

## Prerequisites

- [CoppeliaSim EDU/PRO](https://www.coppeliarobotics.com/downloads) v4.6+
- ROS2 Humble
- `simROS2` plugin enabled in CoppeliaSim
- `topic_based_ros2_control`:
  ```bash
  sudo apt install ros-humble-topic-based-ros2-control
  ```

## Setup

### 1. Import URDF into CoppeliaSim

```bash
# Generate expanded URDF
source /opt/ros/humble/setup.bash
xacro so_arm_101_description/urdf/so_101.urdf.xacro sim_backend:=coppeliasim > /tmp/so_101_coppeliasim.urdf
```

In CoppeliaSim:
1. **File > Import > URDF...**
2. Select `/tmp/so_101_coppeliasim.urdf`
3. Check **Assign collision shapes to visible shapes**
4. Check **Assign mass and inertia to shapes**
5. Click **Import**
6. Save the scene (optional: `worlds/coppeliasim_scene.ttt`)

### 2. Add ROS2 Bridge Script

The `topic_based_ros2_control` plugin communicates via these topics:

| Topic | Type | Direction |
|-------|------|-----------|
| `/joint_states` | `sensor_msgs/JointState` | CoppeliaSim -> ROS2 |
| `/joint_commands` | `std_msgs/Float64MultiArray` | ROS2 -> CoppeliaSim |

Add a **child script** to the robot's base link with this Lua code:

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

### 3. Launch

```bash
# Terminal 1: Start CoppeliaSim with the scene loaded and press Play

# Terminal 2: Launch ROS2 side
ros2 launch so_arm_101_description sim.launch.py sim:=coppeliasim
```

## Verify

```bash
ros2 topic echo /joint_states --once

ros2 topic pub /arm_controller/joint_trajectory trajectory_msgs/msg/JointTrajectory "{
  joint_names: ['base_link_to_link1'],
  points: [{positions: [0.5], time_from_start: {sec: 2}}]
}" --once
```

## Troubleshooting

- **simROS2 not loading**: Ensure `libsimROS2.so` is in CoppeliaSim's plugin directory and `ROS_DISTRO=humble` is set.
- **No joint states**: Check that the Lua script is attached to the correct object and the simulation is running.
- **Joint names mismatch**: Joint names in the Lua script must exactly match those in `config/controllers.yaml`.

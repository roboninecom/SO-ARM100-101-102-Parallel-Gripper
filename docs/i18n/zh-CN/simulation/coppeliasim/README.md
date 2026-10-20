<!-- translation-navigation -->
[English](../../../en/simulation/coppeliasim/README.md) · [Русский](../../../ru/simulation/coppeliasim/README.md) · [Español](../../../es/simulation/coppeliasim/README.md) · [Français](../../../fr/simulation/coppeliasim/README.md) · [Deutsch](../../../de/simulation/coppeliasim/README.md) · [Português (Brasil)](../../../pt-BR/simulation/coppeliasim/README.md) · [简体中文](README.md) · [日本語](../../../ja/simulation/coppeliasim/README.md) · [हिन्दी](../../../hi/simulation/coppeliasim/README.md) · [العربية](../../../ar/simulation/coppeliasim/README.md)

[英文原文](../../../../../simulation/coppeliasim/README.md)

[简体中文](../../README.md)

> 完整机器翻译，尚未经母语使用者审核。图像、代码、CAD 和原始 PDF 为共用文件。如有歧义，请参阅英文原文。
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="coppeliasim"></a>
# CoppeliaSim

**状态:未经测试 (外部模拟器)**

CoppeliaSim 运行外部,与 ROS2 通过 `topic_based_ros2_control`. 你跑了 CoppeliaSim 单独启动 ROS2 侧面 `sim:=coppeliasim`.

<a id="prerequisites"></a>
## 预先条件

- [CoppeliaSim 经济发展和发展](https://www.coppeliarobotics.com/downloads) v4.6+
- ROS2 谦卑
- `simROS2` 插件启用 CoppeliaSim
- `topic_based_ros2_control`:
  ```bash
  sudo apt install ros-humble-topic-based-ros2-control
  ```

<a id="setup"></a>
## 设置

<a id="1-import-urdf-into-coppeliasim"></a>
### 1. 进口URDF CoppeliaSim

```bash
# Generate expanded URDF
source /opt/ros/humble/setup.bash
xacro so_arm_101_description/urdf/so_101.urdf.xacro sim_backend:=coppeliasim > /tmp/so_101_coppeliasim.urdf
```

在 CoppeliaSim:
1. **文件 > 进口 > URDF...**
2. 选择 `/tmp/so_101_coppeliasim.urdf`
3. 检查 **将碰撞形状分配到可见的形状**
4. 检查 **将质量和惯性分配给形状**
5. 单击 **进口**
6. 保存场景 (可选: `worlds/coppeliasim_scene.ttt`)

<a id="2-add-ros2-bridge-script"></a>
### 2. 添加 ROS2 桥脚本

其他 `topic_based_ros2_control` 插件通过这些主题进行沟通:

| 主题 | 类型 | 方向 |
|-------|------|-----------|
| `/joint_states` | `sensor_msgs/JointState` | CoppeliaSim -> ROS2 |
| `/joint_commands` | `std_msgs/Float64MultiArray` | ROS2 -> CoppeliaSim |

添加一个 **儿童剧本** 在机器人的基因链接上使用这个Lua代码:

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

<a id="3-launch"></a>
### 3. 发射

```bash
# Terminal 1: Start CoppeliaSim with the scene loaded and press Play

# Terminal 2: Launch ROS2 side
ros2 launch so_arm_101_description sim.launch.py sim:=coppeliasim
```

<a id="verify"></a>
## 验证

```bash
ros2 topic echo /joint_states --once

ros2 topic pub /arm_controller/joint_trajectory trajectory_msgs/msg/JointTrajectory "{
  joint_names: ['base_link_to_link1'],
  points: [{positions: [0.5], time_from_start: {sec: 2}}]
}" --once
```

<a id="troubleshooting"></a>
## 解决问题

- **simROS2不加载**确保: `libsimROS2.so` 在 CoppeliaSim插件目录和 `ROS_DISTRO=humble` 已经设置了.
- **没有联合国家**: 检查Lua脚本是否连接到正确的对象,模拟正在运行.
- **共同名称不匹配**:  ⁇ 字母中的共同名称必须完全匹配 `config/controllers.yaml`.
<!-- /translated-content -->

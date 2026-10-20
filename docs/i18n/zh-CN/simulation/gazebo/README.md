<!-- translation-navigation -->
[English](../../../en/simulation/gazebo/README.md) · [Русский](../../../ru/simulation/gazebo/README.md) · [Español](../../../es/simulation/gazebo/README.md) · [Français](../../../fr/simulation/gazebo/README.md) · [Deutsch](../../../de/simulation/gazebo/README.md) · [Português (Brasil)](../../../pt-BR/simulation/gazebo/README.md) · [简体中文](README.md) · [日本語](../../../ja/simulation/gazebo/README.md) · [हिन्दी](../../../hi/simulation/gazebo/README.md) · [العربية](../../../ar/simulation/gazebo/README.md)

[英文原文](../../../../../simulation/gazebo/README.md)

[简体中文](../../README.md)

> 完整机器翻译，尚未经母语使用者审核。图像、代码、CAD 和原始 PDF 为共用文件。如有歧义，请参阅英文原文。
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="gazebo-gz-sim"></a>
# Gazebo 现在,我们要做什么呢?

**状态:准备**

Gazebo 使用模拟 `gz_ros2_control` 插件. 控制器经理走进 Gazebo 过程.

<a id="prerequisites"></a>
## 预先条件

**医生 (建议):**
- 达克桌面

**原住民 ROS2:**
- ROS2 谦卑
- `ros-humble-gz-ros2-control`
- `ros-humble-ros-gz-sim`
- `ros-humble-ros-gz-bridge`

<a id="launch"></a>
## 发射

<a id="docker"></a>
### 码头

```bash
cd simulation/so_arm_101_description
docker compose run gazebo
```

对于NVIDIA GPU的通过,请不要评论 `deploy:` 封锁 `docker-compose.yaml`:

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
### 原住民 ROS2

```bash
ros2 launch so_arm_101_description sim.launch.py sim:=gazebo
```

<a id="how-it-works"></a>
## 它是如何工作的

1. 其他 Gazebo 插件 `gz_ros2_control/GazeboSimSystem` 通过 `sim_backend:=gazebo` ⁇ 克罗论点
2. Gazebo 嵌入控制器管理器 - - 没有单独的 `ros2_control_node` 需要
3. 机器人被生育到 `worlds/empty.sdf` 通过 `ros_gz_sim create`
4. 控制器 ⁇ 子开始后 `robot_state_publisher` 正在运行

<a id="world-file"></a>
### 世界文件

`worlds/empty.sdf` 提供:
- 电机 (时间步骤 0.004s / 250 Hz)
- 地平面 (100x100m)
- 方向的阳光照明

<a id="verify"></a>
## 验证

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
## 解决问题

- **没有找到的网格**确保: `GZ_SIM_RESOURCE_PATH` 包含包股目录. 达克入口点自动设置.
- **没有显示器**: Gazebo 需要一个X11服务器. 在Windows上,使用VcXsrv `-ac` 旗 ⁇ 在macOS上,使用XQuartz.
- **缓慢的转载**: 不评论GPU通过区块 `docker-compose.yaml` 如果您有一个NVIDIA GPU.
<!-- /translated-content -->

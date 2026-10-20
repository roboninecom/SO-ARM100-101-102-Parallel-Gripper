<!-- translation-navigation -->
[English](../../../en/simulation/mujoco/README.md) · [Русский](../../../ru/simulation/mujoco/README.md) · [Español](../../../es/simulation/mujoco/README.md) · [Français](../../../fr/simulation/mujoco/README.md) · [Deutsch](../../../de/simulation/mujoco/README.md) · [Português (Brasil)](../../../pt-BR/simulation/mujoco/README.md) · [简体中文](README.md) · [日本語](../../../ja/simulation/mujoco/README.md) · [हिन्दी](../../../hi/simulation/mujoco/README.md) · [العربية](../../../ar/simulation/mujoco/README.md)

[英文原文](../../../../../simulation/mujoco/README.md)

[简体中文](../../README.md)

> 完整机器翻译，尚未经母语使用者审核。图像、代码、CAD 和原始 PDF 为共用文件。如有歧义，请参阅英文原文。
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="mujoco"></a>
# MuJoCo

**状态:准备**

MuJoCo 使用模拟 `mujoco_ros2_control` (可控制分叉) MuJoCo 内部将URDF转换为MJCF,并运行物理+ ⁇ 染 `ros2_control_node` 过程.

<a id="prerequisites"></a>
## 预先条件

**医生 (建议):**
- 达克桌面

**原住民 ROS2:**
- ROS2 谦卑
- `mujoco_ros2_control` (从来源中获取 - 下面见)
- `mujoco` 管包

<a id="launch"></a>
## 发射

<a id="docker"></a>
### 码头

```bash
cd simulation/so_arm_101_description
docker compose run mujoco
```

达克图像的构建 `mujoco_ros2_control` 从源自动.

<a id="native-ros2"></a>
### 原住民 ROS2

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
## 它是如何工作的

1. 插件 `mujoco_ros2_control/MujocoSystemInterface` 通过 `sim_backend:=mujoco`
2. 一个自定义节点 (`publish_mujoco_description`) 发布了URDF `/mujoco_robot_description`
3. 其他 MuJoCo 插件读取URDF,将其转换为MJCF,并启动模拟
4. 其他 `<mujoco><compiler meshdir=.../>` 在 URDF 中的标签表示 MuJoCo 在哪里找到碰撞网
5. 显示模拟 (1280x720,从全屏默认调整) 的 ⁇ 染窗口打开

<a id="key-parameters-in-so_101ros2_controlxacro"></a>
### 关键参数 `so_101.ros2_control.xacro`)

- `headless`设置为: `true` 无头模式 (没有 ⁇ 染窗口)
- `sim_speed_factor`:模拟速度乘法 (默认: 1.0)

<a id="verify"></a>
## 验证

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
## 解决问题

- **开放GL错误**: 确保安装GPU驱动器. 对于Docker来说,请不要评论NVIDIAGPU区块 `docker-compose.yaml`.
- **窗户太大**:Docker的图像将窗口调整为1280x720. 对于本地安装, MuJoCo 窗户可能默认是全屏.
- **没有显示器**: MuJoCo 需要一个X11服务器用于 ⁇ 染窗口. 使用 `headless:=true` 在xacro中,如果没有显示屏.
<!-- /translated-content -->

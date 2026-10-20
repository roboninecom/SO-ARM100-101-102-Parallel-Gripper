<!-- translation-navigation -->
[English](../../en/simulation/README.md) · [Русский](../../ru/simulation/README.md) · [Español](../../es/simulation/README.md) · [Français](../../fr/simulation/README.md) · [Deutsch](../../de/simulation/README.md) · [Português (Brasil)](../../pt-BR/simulation/README.md) · [简体中文](README.md) · [日本語](../../ja/simulation/README.md) · [हिन्दी](../../hi/simulation/README.md) · [العربية](../../ar/simulation/README.md)

[英文原文](../../../../simulation/README.md)

[简体中文](../README.md)

> 完整机器翻译，尚未经母语使用者审核。图像、代码、CAD 和原始 PDF 为共用文件。如有歧义，请参阅英文原文。
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="simulation"></a>
# 模拟

ROS2 模拟支持 SO-ARM-101 机器人手臂,并行抓住. 单个参数化的URDF通过一个发射文件驱动5个物理引擎.

<a id="gazebo-ignition-fortress"></a>
## Gazebo (火焰堡垒)

![SO-ARM-101 在 Gazebo](../../../../assets/images/simulation/gazebo/gazebo_pick_place.png)

*SO-ARM-101 执行选择 & 位置 Gazebo ⁇ 手臂挑选一个物体,把它放在上面的货架上.*

<a id="mujoco"></a>
## MuJoCo

![SO-ARM-101 在 MuJoCo](../../../../assets/images/simulation/mujoco/mujoco_pick_place.png)

*同样的选择和位置序列运行 MuJoCo 通过完整的物理模拟.*

<a id="simulator-status"></a>
## 模拟器状态

| 模拟器 | 状态 | 码头 | 控制器管理员 |
|-----------|--------|--------|--------------------|
| [Gazebo 现在,我们要做什么呢?](gazebo/README.md) | 准备好 | `docker compose run gazebo` | 嵌入模拟器 |
| [MuJoCo](mujoco/README.md) | 准备好 | `docker compose run mujoco` | 外部 (`ros2_control_node`) |
| [Webots](webots/README.md) | 不稳定 | `docker compose run webots` | 嵌入于驱动器中 |
| [CoppeliaSim](coppeliasim/README.md) | 未经测试 | N/A (外部模拟) | 外部 (`ros2_control_node`) |
| [印度 Isaac 是的](isaac_sim/README.md) | 未经测试 | N/A (外部模拟) | 外部 (`ros2_control_node`) |

<a id="architecture"></a>
## 建筑

- **单一的URDF** -- `so_arm_101_description/urdf/so_101.urdf.xacro` 是所有模拟器的唯一机器人描述
- **参数化后端** -- `sim_backend:=gazebo|mujoco|webots|coppeliasim|isaac` 选择了 `ros2_control` 在 xacro 扩展时间
- **统一控制器** -- `config/controllers.yaml` 定义所有后端的相同关节,接口和控制器名称
- **一个发射文件** -- `launch/sim.launch.py` 在 `sim:=<backend>` 论证

<a id="robot"></a>
### 机器人

- **5DOF臂**: 基础旋转,肩膀 ⁇ ,肘部,手腕 ⁇ ,手腕滚动
- **平行夹爪**: 2个 ⁇ 门关节 (左侧 ⁇ 门镜子通过右侧 `<mimic>`)
- **服务器**: STS3215 转矩1.5Nm,速度5.2rad/s

<a id="prerequisites"></a>
## 预先条件

**选择A:Docker (推 ⁇ ,没有) ROS2 需要安装)**

- 达克桌面

**选择B:本地 ROS2**

- ROS2 谦卑
- 模拟器特定的依赖性 (参见每个模拟器指南)

<a id="installation"></a>
## 装备

<a id="docker-recommended"></a>
### 托克 (推 ⁇ )

```bash
cd simulation/so_arm_101_description
docker compose run gazebo    # or mujoco, webots
```

<a id="native-ros2"></a>
### 原住民 ROS2

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

<a id="quick-start"></a>
## 快速开始

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

<a id="commanding-the-robot"></a>
## 命令机器人

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

<a id="docker-services"></a>
## 码头服务

所有服务都定义在 `so_arm_101_description/docker-compose.yaml`:

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

<a id="collision-meshes"></a>
## 碰撞网

简单的 ⁇ 形船体碰撞网 `so_arm_101_description/meshes/collision/`. 为了再生:

```bash
pip install trimesh
python scripts/generate_collision_meshes.py
```

<a id="package-structure"></a>
## 包装结构

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
<!-- /translated-content -->

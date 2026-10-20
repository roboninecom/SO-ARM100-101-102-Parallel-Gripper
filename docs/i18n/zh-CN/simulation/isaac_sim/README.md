<!-- translation-navigation -->
[English](../../../en/simulation/isaac_sim/README.md) · [Русский](../../../ru/simulation/isaac_sim/README.md) · [Español](../../../es/simulation/isaac_sim/README.md) · [Français](../../../fr/simulation/isaac_sim/README.md) · [Deutsch](../../../de/simulation/isaac_sim/README.md) · [Português (Brasil)](../../../pt-BR/simulation/isaac_sim/README.md) · [简体中文](README.md) · [日本語](../../../ja/simulation/isaac_sim/README.md) · [हिन्दी](../../../hi/simulation/isaac_sim/README.md) · [العربية](../../../ar/simulation/isaac_sim/README.md)

[英文原文](../../../../../simulation/isaac_sim/README.md)

[简体中文](../../README.md)

> 完整机器翻译，尚未经母语使用者审核。图像、代码、CAD 和原始 PDF 为共用文件。如有歧义，请参阅英文原文。
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="nvidia-isaac-sim"></a>
# 印度 Isaac 是的

**状态:未经测试 (外部模拟器)**

Isaac 系统在外部运行,与 ROS2 通过 `topic_based_ros2_control`. 你跑了 Isaac 单独 ⁇ 动,然后启动 ROS2 侧面 `sim:=isaac`.

<a id="prerequisites"></a>
## 预先条件

- [印度 Isaac 是的](https://developer.nvidia.com/isaac-sim) 4.0+ (需要NVIDIA RTX GPU)
- ROS2 谦卑
- Isaac 是的 ROS2 启用桥梁
- `topic_based_ros2_control`:
  ```bash
  sudo apt install ros-humble-topic-based-ros2-control
  ```

<a id="setup"></a>
## 设置

<a id="1-import-urdf-into-isaac-sim"></a>
### 1. 进口URDF Isaac 是的

```bash
# Generate expanded URDF
source /opt/ros/humble/setup.bash
xacro so_arm_101_description/urdf/so_101.urdf.xacro sim_backend:=isaac > /tmp/so_101_isaac.urdf
```

在 Isaac ⁇ ,你知道吗?
1. **Isaac 工具 > URDF进口商**
2. **输入文件**选择: `/tmp/so_101_isaac.urdf`
3. **进口地点**: `/World/so_101`
4. **联合驱动型**位置:
5. **修复基础链接**: 检查
6. 单击 **进口**
7. 添加一个地面飞机: **创建 > 物理 > 地平面**
8. 除了美元阶段 (可选)

<a id="2-configure-ros2-bridge-omnigraph"></a>
### 2. 配置 ROS2 桥梁 (全图)

其他 `topic_based_ros2_control` 插件通过这些主题进行沟通:

| 主题 | 类型 | 方向 |
|-------|------|-----------|
| `/joint_states` | `sensor_msgs/JointState` | Isaac 是的 -> ROS2 |
| `/joint_commands` | `std_msgs/Float64MultiArray` | ROS2 -> Isaac 是的 |

<a id="omnigraph-setup"></a>
#### 泛图格设置

1. 开放 **窗口 > 视觉脚本 > 行动图**
2. 创建一个新的行动图表
3. 加入这些节点:
   - **在播放标签上** (事件来源)
   - **Isaac 阅读模拟时间**
   - **ROS2 发表联合国家** -- 连接到 `/World/so_101`
   - **ROS2 签署联合国家** -- 接收命令
   - **Isaac 关节控制器** -- 对关节执行命令

4. 连接图表:
   ```
   On Playback Tick -> Read Sim Time -> Publish Joint State
   On Playback Tick -> Subscribe Joint State -> Articulation Controller
   ```

5. 配置 **发表联合国家** 节点:
   - `targetPrim`: `/World/so_101`
   - `topicName`: `/joint_states`

6. 配置 **关节控制器** 节点:
   - `targetPrim`: `/World/so_101`
   - `jointNames`:所有7个共同名称 `config/controllers.yaml`

<a id="alternative-isaac_ros2_control"></a>
#### 替代: isaac_ros2_control

如果 `isaac_ros2_control` 在您的 Isaac 简单版本:

```bash
sudo apt install ros-humble-isaac-ros2-control
```

这取代了OmniGraph设置 `ros2_control` 硬件接口.

<a id="3-launch"></a>
### 3. 发射

```bash
# Terminal 1: Start Isaac Sim and press Play

# Terminal 2: Launch ROS2 side
ros2 launch so_arm_101_description sim.launch.py sim:=isaac
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

- **URDF进口失败**确保所有网路都是绝对的. 通过 `xacro` 首先 - 不要进口 `.xacro` 直接提交文件.
- **没有联合国家**: 验证OmniGraph连接和 Isaac 现在,Sim在播放模式下.
- **物理不稳定性**:在物理场景属性中,设置解决器类型为TGS并增加 ⁇ 代数.
- **ROS2 没有找到的桥**: 启用扩展 **窗口 > 扩展 > ROS2 桥梁**.
<!-- /translated-content -->

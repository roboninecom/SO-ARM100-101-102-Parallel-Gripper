<!-- translation-navigation -->
[English](../../../en/simulation/webots/README.md) · [Русский](../../../ru/simulation/webots/README.md) · [Español](../../../es/simulation/webots/README.md) · [Français](../../../fr/simulation/webots/README.md) · [Deutsch](../../../de/simulation/webots/README.md) · [Português (Brasil)](../../../pt-BR/simulation/webots/README.md) · [简体中文](README.md) · [日本語](../../../ja/simulation/webots/README.md) · [हिन्दी](../../../hi/simulation/webots/README.md) · [العربية](../../../ar/simulation/webots/README.md)

[英文原文](../../../../../simulation/webots/README.md)

[简体中文](../../README.md)

> 完整机器翻译，尚未经母语使用者审核。图像、代码、CAD 和原始 PDF 为共用文件。如有歧义，请参阅英文原文。
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="webots"></a>
# Webots

> **状态:不稳定** -- Webots 整合工作,但已知性能和 ⁇ 染问题. 建议只使用Docker.

Webots 使用模拟 `webots_ros2_control`. 其他 Webots 驾驶员嵌入控制器管理器.

<a id="prerequisites"></a>
## 预先条件

**医生 (建议):**
- 达克桌面

**原住民 ROS2:**
- ROS2 谦卑
- [Webots](https://cyberbotics.com/) R2023b+
- `ros-humble-webots-ros2`
- `urdf2webots` 管包

<a id="launch"></a>
## 发射

<a id="docker"></a>
### 码头

```bash
cd simulation/so_arm_101_description
docker compose run webots
```

> **备注**其他: Webots 码头服务没有音量. 在构建时,世界文件在图像内生成. 如果修改URDF,您必须重建: `docker compose build webots`.

<a id="native-ros2"></a>
### 原住民 ROS2

```bash
pip install urdf2webots

# Generate the Webots world file
python scripts/setup_webots.py

# Generate pre-expanded URDF for the Webots driver
xacro urdf/so_101.urdf.xacro sim_backend:=webots > urdf/so_101_webots.urdf

# Launch
ros2 launch so_arm_101_description sim.launch.py sim:=webots
```

<a id="how-it-works"></a>
## 它是如何工作的

1. `scripts/setup_webots.py` 将 URDF 转换为 Webots 通过机器人节点 `urdf2webots` 产生的 `worlds/webots_sim.wbt`
2. 其他 `WebotsLauncher` 打开世界文件 Webots
3. `WebotsController` 通过IPC连接到机器人,并启动 `ros2_control` 司机
4. 控制器 `<extern>` 世界文件中的标签允许 `webots_ros2_driver` 接管
5. 一个先前扩展的URDF (`so_101_webots.urdf`) 是因为 `WebotsController` 需要文件路径,而不是直线XML

<a id="world-settings"></a>
### 世界环境

- `basicTimeStep`: 16ms (减少了物理稳定性的默认值)
- `maxContactJoints`: 4 (限制细节网的碰撞上空费)

<a id="known-issues"></a>
## 已知问题

- **速度慢的世界加载 X11**:当通过X11传输时,世界需要120秒才能加载. 控制器生殖器时间设置为180s以适应这一点.
- **在Windows上转载电线框**: VcXsrv只提供OpenGL 1.4,但 Webots 需要OpenGL 3.3 模拟运行,但在线框模式下呈现.
- **WSL2检测**:在WSL2上的Docker继承了WSL内核名称,导致 `webots_ros2_driver` 寻找 `webots.exe`. 文件补丁 `is_wsl()` 总是回来 `False`.
- **物理警告**由于高聚合物碰撞网,可能会出现"你的世界太复杂了".

<a id="troubleshooting"></a>
## 解决问题

- **`WEBOTS_HOME` 没有找到**确保: `WEBOTS_HOME=/usr/local/webots` 已经设置了. 在Docker的图像中,它自动设置.
- **控制器时间**如果控制器未能激活, `launch/sim.launch.py` (目前的180年代).
- **没有显示器**: Webots 需要X11. 在Windows上,使用VcXsrv `-ac -wgl` 旗 ⁇ .
<!-- /translated-content -->

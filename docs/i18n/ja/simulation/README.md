<!-- translation-navigation -->
[English](../../en/simulation/README.md) · [Русский](../../ru/simulation/README.md) · [Español](../../es/simulation/README.md) · [Français](../../fr/simulation/README.md) · [Deutsch](../../de/simulation/README.md) · [Português (Brasil)](../../pt-BR/simulation/README.md) · [简体中文](../../zh-CN/simulation/README.md) · [日本語](README.md) · [हिन्दी](../../hi/simulation/README.md) · [العربية](../../ar/simulation/README.md)

[英語原文](../../../../simulation/README.md)

[日本語](../README.md)

> 文書全体の機械翻訳です。母語話者による確認は未実施です。画像、コード、CAD、元の PDF は共通です。不明点は英語原文を参照してください。
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="simulation"></a>
# シミュレーション

ROS2 シミュレーション支援 SO-ARM-101 パラレルグリッパーを持つロボット腕. 単一のパラメータ化された URDF と一つの起動ファイルで、5 種類の物理エンジンに対応します。

<a id="gazebo-ignition-fortress"></a>
## Gazebo (イグニッション砦)

![SO-ARM-101 中 Gazebo](../../../../assets/images/simulation/gazebo/gazebo_pick_place.png)

*SO-ARM-101 選択 & 場所の実行 Gazebo ⁇ 腕は物体を拾い,上にある棚の上に置く.*

<a id="mujoco"></a>
## MuJoCo

![SO-ARM-101 中 MuJoCo](../../../../assets/images/simulation/mujoco/mujoco_pick_place.png)

*同じ選択と位置の順序が実行されます MuJoCo 物理的なシミュレーションを*

<a id="simulator-status"></a>
## シミュレーターの状態

| シミュレーター | 状態 | ドーカー | コントローラーマネージャー |
|-----------|--------|--------|--------------------|
| [Gazebo (gz-sim)](gazebo/README.md) | 準備する | `docker compose run gazebo` | シミュレーターに組み込み |
| [MuJoCo](mujoco/README.md) | 準備する | `docker compose run mujoco` | 外部 (`ros2_control_node`) |
| [Webots](webots/README.md) | 不安定 | `docker compose run webots` | ドライバーに埋め込み |
| [CoppeliaSim](coppeliasim/README.md) | 試験されていない | N/A (外部シム) | 外部 (`ros2_control_node`) |
| [NVIDIA Isaac はい](isaac_sim/README.md) | 試験されていない | N/A (外部シム) | 外部 (`ros2_control_node`) |

<a id="architecture"></a>
## 建築

- **単一のURDF** -- `so_arm_101_description/urdf/so_101.urdf.xacro` すべてのシミュレーターのための唯一のロボット説明です
- **パラメータ化されたバックエンド** -- `sim_backend:=gazebo|mujoco|webots|coppeliasim|isaac` 選択する `ros2_control` xacro 拡張時にプラグイン
- **統一制御器** -- `config/controllers.yaml` すべてのバックエンドで同じ関節,インターフェース,コントローラー名を定義します
- **単一の起動ファイル** -- `launch/sim.launch.py` と `sim:=<backend>` 議論

<a id="robot"></a>
### ロボット

- **5DOF腕**: ベース回転,肩のピッチ,肘,腕のピッチ,腕ロール
- **平行グリッパー**: 2つのプリズマティックなクランプ関節 (左側クランプ鏡が右側を通過) `<mimic>`)
- **セルボス**: STS3215 (1.5 Nmトーク,5.2 rad/s速度)

<a id="prerequisites"></a>
## 前提条件

**オプション A:ドッカー (推奨,不要) ROS2 インストールが必要)**

- ドッカーデスクトップ

**オプションB:ネイティブ ROS2**

- ROS2 謙虚
- シミュレーター専用依存 (シミュレーターごとにガイドを参照)

<a id="installation"></a>
## 設置

<a id="docker-recommended"></a>
### ドッカー (推奨)

```bash
cd simulation/so_arm_101_description
docker compose run gazebo    # or mujoco, webots
```

<a id="native-ros2"></a>
### 原産 ROS2

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
## 早いスタート

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
## ロボットを指揮する

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
## ドッカーサービス

すべてのサービスは, `so_arm_101_description/docker-compose.yaml`:

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
## 衝突メッシュ

単純化された凸状の船体衝突網が提供されています `so_arm_101_description/meshes/collision/`. 再生する

```bash
pip install trimesh
python scripts/generate_collision_meshes.py
```

<a id="package-structure"></a>
## パッケージ構造

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

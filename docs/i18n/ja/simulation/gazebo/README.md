<!-- translation-navigation -->
[English](../../../en/simulation/gazebo/README.md) · [Русский](../../../ru/simulation/gazebo/README.md) · [Español](../../../es/simulation/gazebo/README.md) · [Français](../../../fr/simulation/gazebo/README.md) · [Deutsch](../../../de/simulation/gazebo/README.md) · [Português (Brasil)](../../../pt-BR/simulation/gazebo/README.md) · [简体中文](../../../zh-CN/simulation/gazebo/README.md) · [日本語](README.md) · [हिन्दी](../../../hi/simulation/gazebo/README.md) · [العربية](../../../ar/simulation/gazebo/README.md)

[英語原文](../../../../../simulation/gazebo/README.md)

[日本語](../../README.md)

> 文書全体の機械翻訳です。母語話者による確認は未実施です。画像、コード、CAD、元の PDF は共通です。不明点は英語原文を参照してください。
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="gazebo-gz-sim"></a>
# Gazebo (gz-sim)

**状態: 準備済み**

Gazebo シミュレーション `gz_ros2_control` プラグイン コントローラーマネージャーは Gazebo プロセス

<a id="prerequisites"></a>
## 前提条件

**ドッカー (推奨):**
- ドッカーデスクトップ

**原産 ROS2:**
- ROS2 謙虚
- `ros-humble-gz-ros2-control`
- `ros-humble-ros-gz-sim`
- `ros-humble-ros-gz-bridge`

<a id="launch"></a>
## 打ち上げ

<a id="docker"></a>
### ドーカー

```bash
cd simulation/so_arm_101_description
docker compose run gazebo
```

NVIDIAGPUの経路については, `deploy:` ブロックイン `docker-compose.yaml`:

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
### 原産 ROS2

```bash
ros2 launch so_arm_101_description sim.launch.py sim:=gazebo
```

<a id="how-it-works"></a>
## 働き方

1. 労働組合 Gazebo プラグイン `gz_ros2_control/GazeboSimSystem` 選定は `sim_backend:=gazebo` xacro 議論
2. Gazebo 制御管理者を埋め込みます `ros2_control_node` 必要なこと
3. ロボットは `worlds/empty.sdf` 経由 `ros_gz_sim create`
4. コントローラーズ・スレーバーは `robot_state_publisher` 走っている

<a id="world-file"></a>
### 世界ファイル

`worlds/empty.sdf` 規定する
- ODE物理エンジン (タイムステップ 0.004s / 250 Hz)
- 地面平面 (100x100m)
- 方向性太陽照明

<a id="verify"></a>
## 確認する

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
## 問題解決

- **メッシュが見つかりませんでした**: 確保する `GZ_SIM_RESOURCE_PATH` パッケージシェアディレクトリを含む. ドーカーエントリーポイントは自動的に設定します
- **ディスプレイなし**: Gazebo X11サーバーが必要 Windows で,VcXsrv を `-ac` フラグ MacOSではXQuartzを使います
- **スローランディング**: ブロックを通過するGPUをコメントしない `docker-compose.yaml` NVIDIA GPUを搭載している場合は
<!-- /translated-content -->

<!-- translation-navigation -->
[English](../../../en/simulation/mujoco/README.md) · [Русский](../../../ru/simulation/mujoco/README.md) · [Español](../../../es/simulation/mujoco/README.md) · [Français](../../../fr/simulation/mujoco/README.md) · [Deutsch](../../../de/simulation/mujoco/README.md) · [Português (Brasil)](../../../pt-BR/simulation/mujoco/README.md) · [简体中文](../../../zh-CN/simulation/mujoco/README.md) · [日本語](README.md) · [हिन्दी](../../../hi/simulation/mujoco/README.md) · [العربية](../../../ar/simulation/mujoco/README.md)

[英語原文](../../../../../simulation/mujoco/README.md)

[日本語](../../README.md)

> 文書全体の機械翻訳です。母語話者による確認は未実施です。画像、コード、CAD、元の PDF は共通です。不明点は英語原文を参照してください。
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="mujoco"></a>
# MuJoCo

**状態: 準備済み**

MuJoCo シミュレーション `mujoco_ros2_control` (ロス制御フォーク) MuJoCo 内部でURDFをMJCFに変換し,物理+レンダリングを実行する `ros2_control_node` プロセス

<a id="prerequisites"></a>
## 前提条件

**ドッカー (推奨):**
- ドッカーデスクトップ

**原産 ROS2:**
- ROS2 謙虚
- `mujoco_ros2_control` (ソースから作成された - 下に参照)
- `mujoco` パッケージ

<a id="launch"></a>
## 打ち上げ

<a id="docker"></a>
### ドーカー

```bash
cd simulation/so_arm_101_description
docker compose run mujoco
```

ドーカー画像が構築される `mujoco_ros2_control` 源から自動的に

<a id="native-ros2"></a>
### 原産 ROS2

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
## 働き方

1. プラグイン `mujoco_ros2_control/MujocoSystemInterface` 選択される `sim_backend:=mujoco`
2. カスタムノード (`publish_mujoco_description`) に URDF を 公開する `/mujoco_robot_description`
3. 労働組合 MuJoCo プラグインは URDF を読み取り,MJCF に変換し,シミュレーションを開始します
4. 労働組合 `<mujoco><compiler meshdir=.../>` URDFのタグは MuJoCo 衝突網をどこで探すか
5. レンダリングウィンドウが開かれ,シミュレーション (1280x720,フルスクリーンデフォルトからパッチ)

<a id="key-parameters-in-so_101ros2_controlxacro"></a>
### キーパラメータ `so_101.ros2_control.xacro`)

- `headless`: に設定 `true` 頭なしモード (レンダリングウィンドウがない)
- `sim_speed_factor`: シミュレーション速度の倍数 (デフォルト: 1.0)

<a id="verify"></a>
## 確認する

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
## 問題解決

- **OpenGL エラー**: GPU ドライバをインストールしていることを確認します. NVIDIA GPU ブロックを削除する `docker-compose.yaml`.
- **窓が大きすぎる**: ドッカー画像は窓を1280x720に修正します 固有のインストールについては, MuJoCo ウィンドウは,デフォルトでフルスクリーンに動いている可能性があります.
- **ディスプレイなし**: MuJoCo レンダリングウィンドウに X11サーバが必要です 使用 `headless:=true` xacroに表示されない場合.
<!-- /translated-content -->

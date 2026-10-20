<!-- translation-navigation -->
[English](../../../en/simulation/isaac_sim/README.md) · [Русский](../../../ru/simulation/isaac_sim/README.md) · [Español](../../../es/simulation/isaac_sim/README.md) · [Français](../../../fr/simulation/isaac_sim/README.md) · [Deutsch](../../../de/simulation/isaac_sim/README.md) · [Português (Brasil)](../../../pt-BR/simulation/isaac_sim/README.md) · [简体中文](../../../zh-CN/simulation/isaac_sim/README.md) · [日本語](README.md) · [हिन्दी](../../../hi/simulation/isaac_sim/README.md) · [العربية](../../../ar/simulation/isaac_sim/README.md)

[英語原文](../../../../../simulation/isaac_sim/README.md)

[日本語](../../README.md)

> 文書全体の機械翻訳です。母語話者による確認は未実施です。画像、コード、CAD、元の PDF は共通です。不明点は英語原文を参照してください。
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="nvidia-isaac-sim"></a>
# NVIDIA Isaac はい

**状態:試験されていない (外部シミュレーター)**

Isaac Simは外部で実行し,通信する ROS2 経由 `topic_based_ros2_control`. 逃げて Isaac シムを分離して起動する ROS2 側と `sim:=isaac`.

<a id="prerequisites"></a>
## 前提条件

- [NVIDIA Isaac はい](https://developer.nvidia.com/isaac-sim) 4.0+ (NVIDIA RTX GPU を必要とする)
- ROS2 謙虚
- Isaac はい ROS2 ブリッジが有効
- `topic_based_ros2_control`:
  ```bash
  sudo apt install ros-humble-topic-based-ros2-control
  ```

<a id="setup"></a>
## 設定

<a id="1-import-urdf-into-isaac-sim"></a>
### 1. URDFを輸入する Isaac はい

```bash
# Generate expanded URDF
source /opt/ros/humble/setup.bash
xacro so_arm_101_description/urdf/so_101.urdf.xacro sim_backend:=isaac > /tmp/so_101_isaac.urdf
```

中 Isaac ええと
1. **Isaac Utils > URDFインポート**
2. **入力ファイル**:を選択する `/tmp/so_101_isaac.urdf`
3. **輸入場所**: `/World/so_101`
4. **共同ドライブタイプ**位置:
5. **ベースリンクを修正する**: チェック
6. クリックする **輸入**
7. 地面飛行機を追加する: **作成 > 物理 > 地面飛行機**
8. USD段階を除く (オプション)

<a id="2-configure-ros2-bridge-omnigraph"></a>
### 2. 設定 ROS2 橋 (オムニグラフ)

労働組合 `topic_based_ros2_control` プラグインは以下のテーマで通信します:

| テーマ | タイプ | 方向 |
|-------|------|-----------|
| `/joint_states` | `sensor_msgs/JointState` | Isaac Sim -> ROS2 |
| `/joint_commands` | `std_msgs/Float64MultiArray` | ROS2 -> Isaac はい |

<a id="omnigraph-setup"></a>
#### オムニグラフ設定

1. オープン **ウィンドウ > ビジュアルスクリプト > アクショングラフ**
2. 新しいアクショングラフを作成する
3. これらのノードを追加する:
   - **プレイバック・ティック** (イベント情報源)
   - **Isaac シミュレーション時間**
   - **ROS2 共同国家を出版する** -- 接続する `/World/so_101`
   - **ROS2 加盟国** -- 命令を受け取る
   - **Isaac 関節制御器** -- 関節に命令を適用する

4. グラフを接続する
   ```
   On Playback Tick -> Read Sim Time -> Publish Joint State
   On Playback Tick -> Subscribe Joint State -> Articulation Controller
   ```

5. 設定 **共同国家を出版する** ノード:
   - `targetPrim`: `/World/so_101`
   - `topicName`: `/joint_states`

6. 設定 **関節制御器** ノード:
   - `targetPrim`: `/World/so_101`
   - `jointNames`: 7つの共同名 `config/controllers.yaml`

<a id="alternative-isaac_ros2_control"></a>
#### オルタナティブ: isaac_ros2_control

もし `isaac_ros2_control` あなたのために利用できます. Isaac Simバージョン:

```bash
sudo apt install ros-humble-isaac-ros2-control
```

オムニグラフの設定を直接に置き換える `ros2_control` ハードウェアインターフェース

<a id="3-launch"></a>
### 3. 打ち上げ

```bash
# Terminal 1: Start Isaac Sim and press Play

# Terminal 2: Launch ROS2 side
ros2 launch so_arm_101_description sim.launch.py sim:=isaac
```

<a id="verify"></a>
## 確認する

```bash
ros2 topic echo /joint_states --once

ros2 topic pub /arm_controller/joint_trajectory trajectory_msgs/msg/JointTrajectory "{
  joint_names: ['base_link_to_link1'],
  points: [{positions: [0.5], time_from_start: {sec: 2}}]
}" --once
```

<a id="troubleshooting"></a>
## 問題解決

- **URDF輸入失敗**: すべての網路が絶対であることを確認する. URDF を生成する `xacro` まず 輸入しないでください `.xacro` 直接ファイル
- **共同国家はない**: OmniGraphが接続されていることを確認し Isaac シムはプレイモードです.
- **物理的不安定**: 物理シーン属性において,ソルバータイプを TGS に設定し,繰り返しの数を増やす.
- **ROS2 橋が見つかりませんでした**: 拡張を有効にする **窓 > エクステンション > ROS2 橋**.
<!-- /translated-content -->

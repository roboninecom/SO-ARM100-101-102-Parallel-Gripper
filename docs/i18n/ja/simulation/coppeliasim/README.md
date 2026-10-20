<!-- translation-navigation -->
[English](../../../en/simulation/coppeliasim/README.md) · [Русский](../../../ru/simulation/coppeliasim/README.md) · [Español](../../../es/simulation/coppeliasim/README.md) · [Français](../../../fr/simulation/coppeliasim/README.md) · [Deutsch](../../../de/simulation/coppeliasim/README.md) · [Português (Brasil)](../../../pt-BR/simulation/coppeliasim/README.md) · [简体中文](../../../zh-CN/simulation/coppeliasim/README.md) · [日本語](README.md) · [हिन्दी](../../../hi/simulation/coppeliasim/README.md) · [العربية](../../../ar/simulation/coppeliasim/README.md)

[英語原文](../../../../../simulation/coppeliasim/README.md)

[日本語](../../README.md)

> 文書全体の機械翻訳です。母語話者による確認は未実施です。画像、コード、CAD、元の PDF は共通です。不明点は英語原文を参照してください。
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="coppeliasim"></a>
# CoppeliaSim

**状態:試験されていない (外部シミュレーター)**

CoppeliaSim 外部で実行し, ROS2 経由 `topic_based_ros2_control`. 逃げて CoppeliaSim 単独で開始し ROS2 側と `sim:=coppeliasim`.

<a id="prerequisites"></a>
## 前提条件

- [CoppeliaSim EDU/PRO](https://www.coppeliarobotics.com/downloads) v4.6+
- ROS2 謙虚
- `simROS2` プラグインが有効 CoppeliaSim
- `topic_based_ros2_control`:
  ```bash
  sudo apt install ros-humble-topic-based-ros2-control
  ```

<a id="setup"></a>
## 設定

<a id="1-import-urdf-into-coppeliasim"></a>
### 1. URDFを輸入する CoppeliaSim

```bash
# Generate expanded URDF
source /opt/ros/humble/setup.bash
xacro so_arm_101_description/urdf/so_101.urdf.xacro sim_backend:=coppeliasim > /tmp/so_101_coppeliasim.urdf
```

中 CoppeliaSim:
1. **ファイル > アインポート > URDF...**
2. 選択する `/tmp/so_101_coppeliasim.urdf`
3. チェック **衝突形を目に見える形に割り当て**
4. チェック **質量と惰性を形に割り当てる**
5. クリックする **輸入**
6. シーンの保存 (オプション: `worlds/coppeliasim_scene.ttt`)

<a id="2-add-ros2-bridge-script"></a>
### 2. 追加する ROS2 ブリッジスクリプト

労働組合 `topic_based_ros2_control` プラグインは以下のテーマで通信します:

| テーマ | タイプ | 方向 |
|-------|------|-----------|
| `/joint_states` | `sensor_msgs/JointState` | CoppeliaSim -> ROS2 |
| `/joint_commands` | `std_msgs/Float64MultiArray` | ROS2 -> CoppeliaSim |

A を追加する **子供の脚本** この Lua コードでロボットのベースリンクへ:

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
### 3. 打ち上げ

```bash
# Terminal 1: Start CoppeliaSim with the scene loaded and press Play

# Terminal 2: Launch ROS2 side
ros2 launch so_arm_101_description sim.launch.py sim:=coppeliasim
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

- **simROS2 負荷なし**: 確保する `libsimROS2.so` 中に入っている CoppeliaSimプラグインディレクトリと `ROS_DISTRO=humble` 設定されています.
- **共同国家はない**: Lua スクリプトが正しいオブジェクトに接続され,シミュレーションが実行されていることを確認します.
- **共通名不一致**: Lua文字の共通名は, `config/controllers.yaml`.
<!-- /translated-content -->

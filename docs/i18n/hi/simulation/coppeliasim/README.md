<!-- translation-navigation -->
[English](../../../en/simulation/coppeliasim/README.md) · [Русский](../../../ru/simulation/coppeliasim/README.md) · [Español](../../../es/simulation/coppeliasim/README.md) · [Français](../../../fr/simulation/coppeliasim/README.md) · [Deutsch](../../../de/simulation/coppeliasim/README.md) · [Português (Brasil)](../../../pt-BR/simulation/coppeliasim/README.md) · [简体中文](../../../zh-CN/simulation/coppeliasim/README.md) · [日本語](../../../ja/simulation/coppeliasim/README.md) · [हिन्दी](README.md) · [العربية](../../../ar/simulation/coppeliasim/README.md)

[अंग्रेज़ी मूल](../../../../../simulation/coppeliasim/README.md)

[हिन्दी](../../README.md)

> यह पूरे दस्तावेज़ का मशीन अनुवाद है; मूल भाषा बोलने वालों ने अभी इसकी समीक्षा नहीं की है। चित्र, कोड, CAD और मूल PDF साझा हैं। अस्पष्टता होने पर अंग्रेज़ी मूल देखें।
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="coppeliasim"></a>
# CoppeliaSim

**स्थितिः परीक्षण नहीं किया गया (बाहरी सिम्युलेटर)**

CoppeliaSim बाहरी रूप से चलाता है और संवाद करता है ROS2 द्वारा `topic_based_ros2_control`. तुम भागते हो CoppeliaSim अलग से और लॉन्च ROS2 साथ पक्ष `sim:=coppeliasim`.

<a id="prerequisites"></a>
## पूर्व शर्तें

- [CoppeliaSim EDU/PRO](https://www.coppeliarobotics.com/downloads) v4.6+
- ROS2 विनम्र
- `simROS2` प्लगइन में सक्षम CoppeliaSim
- `topic_based_ros2_control`:
  ```bash
  sudo apt install ros-humble-topic-based-ros2-control
  ```

<a id="setup"></a>
## सेटअप

<a id="1-import-urdf-into-coppeliasim"></a>
### 1. यूआरडीएफ का आयात CoppeliaSim

```bash
# Generate expanded URDF
source /opt/ros/humble/setup.bash
xacro so_arm_101_description/urdf/so_101.urdf.xacro sim_backend:=coppeliasim > /tmp/so_101_coppeliasim.urdf
```

में CoppeliaSim:
1. **फ़ाइल > आयात > URDF...**
2. चुनें `/tmp/so_101_coppeliasim.urdf`
3. चेक **टक्कर के आकारों को दिखाई देने वाले आकारों में असाइन करें**
4. चेक **आकारों को द्रव्यमान और गतिहीनता आवंटित करें**
5. क्लिक करें **आयात**
6. दृश्य सहेजें (वैकल्पिकः `worlds/coppeliasim_scene.ttt`)

<a id="2-add-ros2-bridge-script"></a>
### 2. जोड़ें ROS2 ब्रिज स्क्रिप्ट

इनका `topic_based_ros2_control` प्लगइन इन विषयों के माध्यम से संवाद करता हैः

| विषय | प्रकार | दिशा |
|-------|------|-----------|
| `/joint_states` | `sensor_msgs/JointState` | CoppeliaSim -> ROS2 |
| `/joint_commands` | `std_msgs/Float64MultiArray` | ROS2 -> CoppeliaSim |

एक जोड़ें **बाल स्क्रिप्ट** इस Lua कोड के साथ रोबोट के आधार लिंक परः

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
### 3. लॉन्च

```bash
# Terminal 1: Start CoppeliaSim with the scene loaded and press Play

# Terminal 2: Launch ROS2 side
ros2 launch so_arm_101_description sim.launch.py sim:=coppeliasim
```

<a id="verify"></a>
## सत्यापित करें

```bash
ros2 topic echo /joint_states --once

ros2 topic pub /arm_controller/joint_trajectory trajectory_msgs/msg/JointTrajectory "{
  joint_names: ['base_link_to_link1'],
  points: [{positions: [0.5], time_from_start: {sec: 2}}]
}" --once
```

<a id="troubleshooting"></a>
## समस्या निवारण

- **simROS2 लोड नहीं**सुनिश्चित करनाः `libsimROS2.so` में है CoppeliaSimप्लगइन निर्देशिका और `ROS_DISTRO=humble` सेट है।
- **संयुक्त राज्य नहीं**: जांचें कि Lua स्क्रिप्ट सही वस्तु से जुड़ा हुआ है और अनुकरण चल रहा है.
- **संयुक्त नाम असंगत**: लू लिपि में संयुक्त नामों को ठीक से उन लोगों के अनुरूप होना चाहिए `config/controllers.yaml`.
<!-- /translated-content -->

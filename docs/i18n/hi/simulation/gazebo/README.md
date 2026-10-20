<!-- translation-navigation -->
[English](../../../en/simulation/gazebo/README.md) · [Русский](../../../ru/simulation/gazebo/README.md) · [Español](../../../es/simulation/gazebo/README.md) · [Français](../../../fr/simulation/gazebo/README.md) · [Deutsch](../../../de/simulation/gazebo/README.md) · [Português (Brasil)](../../../pt-BR/simulation/gazebo/README.md) · [简体中文](../../../zh-CN/simulation/gazebo/README.md) · [日本語](../../../ja/simulation/gazebo/README.md) · [हिन्दी](README.md) · [العربية](../../../ar/simulation/gazebo/README.md)

[अंग्रेज़ी मूल](../../../../../simulation/gazebo/README.md)

[हिन्दी](../../README.md)

> यह पूरे दस्तावेज़ का मशीन अनुवाद है; मूल भाषा बोलने वालों ने अभी इसकी समीक्षा नहीं की है। चित्र, कोड, CAD और मूल PDF साझा हैं। अस्पष्टता होने पर अंग्रेज़ी मूल देखें।
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="gazebo-gz-sim"></a>
# Gazebo (गज़-सिम)

**स्थितिः तैयार**

Gazebo प्रयोग करके सिमुलेशन `gz_ros2_control` प्लगइन. नियंत्रक प्रबंधक अंदर चला जाता है Gazebo प्रक्रिया।

<a id="prerequisites"></a>
## पूर्व शर्तें

**डॉकर (अनुशंसित):**
- डॉकर डेस्कटॉप

**स्वदेशी ROS2:**
- ROS2 विनम्र
- `ros-humble-gz-ros2-control`
- `ros-humble-ros-gz-sim`
- `ros-humble-ros-gz-bridge`

<a id="launch"></a>
## लॉन्च

<a id="docker"></a>
### डॉकर

```bash
cd simulation/so_arm_101_description
docker compose run gazebo
```

NVIDIA जीपीयू पास के लिए, टिप्पणी नहीं `deploy:` ब्लॉक में `docker-compose.yaml`:

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
### स्वदेशी ROS2

```bash
ros2 launch so_arm_101_description sim.launch.py sim:=gazebo
```

<a id="how-it-works"></a>
## यह कैसे काम करता है

1. इनका Gazebo प्लगइन `gz_ros2_control/GazeboSimSystem` चयन किया जाता है `sim_backend:=gazebo` xacro तर्क
2. Gazebo नियंत्रक प्रबंधक एम्बेड - कोई अलग `ros2_control_node` आवश्यक
3. रोबोट में spawned है `worlds/empty.sdf` द्वारा `ros_gz_sim create`
4. नियंत्रक spawners के बाद शुरू `robot_state_publisher` चल रहा है

<a id="world-file"></a>
### विश्व फ़ाइल

`worlds/empty.sdf` प्रदान करता हैः
- ओडीई भौतिकी इंजन (टाइमस्टेप 0.004s / 250 हर्ट्ज)
- जमीनी विमान (100x100 मीटर)
- दिशात्मक सूर्यप्रकाश

<a id="verify"></a>
## सत्यापित करें

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
## समस्या निवारण

- **जाल नहीं मिला**सुनिश्चित करनाः `GZ_SIM_RESOURCE_PATH` पैकेज शेयर निर्देशिका को शामिल करता है। डॉकर प्रवेश बिंदु यह स्वचालित रूप से सेट करता है।
- **कोई प्रदर्शन नहीं**: Gazebo एक X11 सर्वर की जरूरत है. विंडोज पर, VcXsrv का उपयोग करें `-ac` ध्वज। macOS पर, XQuartz का उपयोग करें।
- **धीमी रेंडरिंग**: में ब्लॉक के माध्यम से जीपीयू पास की टिप्पणी नहीं `docker-compose.yaml` यदि आपके पास एक NVIDIA GPU है।
<!-- /translated-content -->

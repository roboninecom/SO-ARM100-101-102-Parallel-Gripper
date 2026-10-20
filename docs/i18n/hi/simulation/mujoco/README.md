<!-- translation-navigation -->
[English](../../../en/simulation/mujoco/README.md) · [Русский](../../../ru/simulation/mujoco/README.md) · [Español](../../../es/simulation/mujoco/README.md) · [Français](../../../fr/simulation/mujoco/README.md) · [Deutsch](../../../de/simulation/mujoco/README.md) · [Português (Brasil)](../../../pt-BR/simulation/mujoco/README.md) · [简体中文](../../../zh-CN/simulation/mujoco/README.md) · [日本語](../../../ja/simulation/mujoco/README.md) · [हिन्दी](README.md) · [العربية](../../../ar/simulation/mujoco/README.md)

[अंग्रेज़ी मूल](../../../../../simulation/mujoco/README.md)

[हिन्दी](../../README.md)

> यह पूरे दस्तावेज़ का मशीन अनुवाद है; मूल भाषा बोलने वालों ने अभी इसकी समीक्षा नहीं की है। चित्र, कोड, CAD और मूल PDF साझा हैं। अस्पष्टता होने पर अंग्रेज़ी मूल देखें।
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="mujoco"></a>
# MuJoCo

**स्थितिः तैयार**

MuJoCo प्रयोग करके सिमुलेशन `mujoco_ros2_control` (रोस-नियंत्रण कांटा) । MuJoCo आंतरिक रूप से URDF को MJCF में परिवर्तित करता है और भौतिक + रेंडरिंग को `ros2_control_node` प्रक्रिया।

<a id="prerequisites"></a>
## पूर्व शर्तें

**डॉकर (अनुशंसित):**
- डॉकर डेस्कटॉप

**स्वदेशी ROS2:**
- ROS2 विनम्र
- `mujoco_ros2_control` (स्रोत से निर्मित - नीचे देखें)
- `mujoco` पाइप पैकेज

<a id="launch"></a>
## लॉन्च

<a id="docker"></a>
### डॉकर

```bash
cd simulation/so_arm_101_description
docker compose run mujoco
```

डॉकर छवि निर्माण `mujoco_ros2_control` स्रोत से स्वचालित रूप से।

<a id="native-ros2"></a>
### स्वदेशी ROS2

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
## यह कैसे काम करता है

1. प्लगइन `mujoco_ros2_control/MujocoSystemInterface` द्वारा चुना जाता है `sim_backend:=mujoco`
2. एक कस्टम नोड (`publish_mujoco_description`) URDF को प्रकाशित करता है `/mujoco_robot_description`
3. इनका MuJoCo प्लगइन URDF पढ़ता है, इसे MJCF में परिवर्तित करता है, और सिमुलेशन शुरू
4. इनका `<mujoco><compiler meshdir=.../>` URDF में टैग बताता है MuJoCo टकराव जाल कहाँ मिलें
5. एक रेंडरिंग विंडो खुलती है जो सिमुलेशन (1280x720, फुल स्क्रीन डिफ़ॉल्ट से पैच किया गया) को दिखाती है

<a id="key-parameters-in-so_101ros2_controlxacro"></a>
### मुख्य पैरामीटर (में) `so_101.ros2_control.xacro`)

- `headless`सेट किया गयाः `true` सिर रहित मोड के लिए (कोई रेंडरिंग विंडो नहीं)
- `sim_speed_factor`: सिमुलेशन गति गुणक (पूर्वनिर्धारितः 1.0)

<a id="verify"></a>
## सत्यापित करें

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
## समस्या निवारण

- **OpenGL त्रुटियाँ**: सुनिश्चित करें कि जीपीयू ड्राइवर स्थापित हैं। डॉकर के लिए, NVIDIA GPU ब्लॉक में टिप्पणी छोड़ दें `docker-compose.yaml`.
- **खिड़की बहुत बड़ी है**: डॉकर की छवि खिड़की को 1280x720 पर पैच करती है। मूल स्थापना के लिए, MuJoCo विंडो डिफ़ॉल्ट रूप से पूर्ण स्क्रीन हो सकती है।
- **कोई प्रदर्शन नहीं**: MuJoCo रेंडरिंग विंडो के लिए एक X11 सर्वर की जरूरत है. उपयोग `headless:=true` xacro में यदि कोई डिस्प्ले उपलब्ध नहीं है।
<!-- /translated-content -->

<!-- translation-navigation -->
[English](../../../en/simulation/isaac_sim/README.md) · [Русский](../../../ru/simulation/isaac_sim/README.md) · [Español](../../../es/simulation/isaac_sim/README.md) · [Français](../../../fr/simulation/isaac_sim/README.md) · [Deutsch](../../../de/simulation/isaac_sim/README.md) · [Português (Brasil)](../../../pt-BR/simulation/isaac_sim/README.md) · [简体中文](../../../zh-CN/simulation/isaac_sim/README.md) · [日本語](../../../ja/simulation/isaac_sim/README.md) · [हिन्दी](README.md) · [العربية](../../../ar/simulation/isaac_sim/README.md)

[अंग्रेज़ी मूल](../../../../../simulation/isaac_sim/README.md)

[हिन्दी](../../README.md)

> यह पूरे दस्तावेज़ का मशीन अनुवाद है; मूल भाषा बोलने वालों ने अभी इसकी समीक्षा नहीं की है। चित्र, कोड, CAD और मूल PDF साझा हैं। अस्पष्टता होने पर अंग्रेज़ी मूल देखें।
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="nvidia-isaac-sim"></a>
# एनवीडीआईए Isaac हाँ

**स्थितिः परीक्षण नहीं किया गया (बाहरी सिम्युलेटर)**

Isaac सिम बाहरी रूप से चलाता है और संवाद करता है ROS2 द्वारा `topic_based_ros2_control`. तुम भागते हो Isaac अलग से सिम और लॉन्च ROS2 साथ पक्ष `sim:=isaac`.

<a id="prerequisites"></a>
## पूर्व शर्तें

- [एनवीडीआईए Isaac हाँ](https://developer.nvidia.com/isaac-sim) 4.0+ (NVIDIA RTX GPU की आवश्यकता है)
- ROS2 विनम्र
- Isaac हाँ ROS2 पुल सक्षम
- `topic_based_ros2_control`:
  ```bash
  sudo apt install ros-humble-topic-based-ros2-control
  ```

<a id="setup"></a>
## सेटअप

<a id="1-import-urdf-into-isaac-sim"></a>
### 1. यूआरडीएफ का आयात Isaac हाँ

```bash
# Generate expanded URDF
source /opt/ros/humble/setup.bash
xacro so_arm_101_description/urdf/so_101.urdf.xacro sim_backend:=isaac > /tmp/so_101_isaac.urdf
```

में Isaac हाँ.
1. **Isaac उपयोगिताएँ > URDF आयातक**
2. **इनपुट फ़ाइल**चुनेंः `/tmp/so_101_isaac.urdf`
3. **आयात स्थान**: `/World/so_101`
4. **संयुक्त ड्राइव प्रकार**पदः
5. **बेस लिंक को ठीक करें**: जाँच की गई
6. क्लिक करें **आयात**
7. एक जमीन विमान जोड़ेंः **बनाएँ > भौतिकी > ग्राउंड विमान**
8. USD चरण के रूप में छोड़ें (वैकल्पिक)

<a id="2-configure-ros2-bridge-omnigraph"></a>
### 2. विन्यास ROS2 ब्रिज (ओम्निग्राफ)

इनका `topic_based_ros2_control` प्लगइन इन विषयों के माध्यम से संवाद करता हैः

| विषय | प्रकार | दिशा |
|-------|------|-----------|
| `/joint_states` | `sensor_msgs/JointState` | Isaac हाँ -> ROS2 |
| `/joint_commands` | `std_msgs/Float64MultiArray` | ROS2 -> Isaac हाँ |

<a id="omnigraph-setup"></a>
#### OmniGraph सेटअप

1. खुला **विंडो > दृश्य स्क्रिप्टिंग > कार्य ग्राफ**
2. एक नया एक्शन ग्राफ बनाएं
3. इन नोड्स जोड़ेंः
   - **प्लेबैक टिकट पर** (घटना स्रोत)
   - **Isaac सिमुलेशन समय पढ़ें**
   - **ROS2 संयुक्त राज्य प्रकाशित करें** -- कनेक्ट करने के लिए `/World/so_101`
   - **ROS2 संयुक्त राज्य की सदस्यता लें** -- आदेश प्राप्त करने के लिए
   - **Isaac अनुच्छेद नियंत्रक** -- जोड़ों पर आदेश लागू करता है

4. ग्राफ कनेक्ट करेंः
   ```
   On Playback Tick -> Read Sim Time -> Publish Joint State
   On Playback Tick -> Subscribe Joint State -> Articulation Controller
   ```

5. विन्यास **संयुक्त राज्य प्रकाशित करें** नोडः
   - `targetPrim`: `/World/so_101`
   - `topicName`: `/joint_states`

6. विन्यास **अनुच्छेद नियंत्रक** नोडः
   - `targetPrim`: `/World/so_101`
   - `jointNames`: सभी 7 संयुक्त नाम `config/controllers.yaml`

<a id="alternative-isaac_ros2_control"></a>
#### वैकल्पिकः isaac_ros2_control

यदि `isaac_ros2_control` आपके लिए उपलब्ध Isaac सिम संस्करणः

```bash
sudo apt install ros-humble-isaac-ros2-control
```

यह OmniGraph सेटअप को एक प्रत्यक्ष के साथ बदल देता है `ros2_control` हार्डवेयर इंटरफ़ेस।

<a id="3-launch"></a>
### 3. लॉन्च

```bash
# Terminal 1: Start Isaac Sim and press Play

# Terminal 2: Launch ROS2 side
ros2 launch so_arm_101_description sim.launch.py sim:=isaac
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

- **यूआरडीएफ आयात विफल**: सुनिश्चित करें कि सभी जाल पथ पूर्ण हों। URDF उत्पन्न करें `xacro` पहले - आयात न करें `.xacro` सीधे फ़ाइल.
- **संयुक्त राज्य नहीं**: सत्यापित करें OmniGraph जुड़ा हुआ है और Isaac सिम प्ले मोड में है।
- **भौतिक अस्थिरता**: भौतिकी दृश्य गुणों में, हलकर्ता प्रकार को टीजीएस पर सेट करें और पुनरावृत्ति गिनती बढ़ाएं।
- **ROS2 पुल नहीं मिला**: विस्तार को सक्षम करें **विंडो > एक्सटेंशन > ROS2 पुल**.
<!-- /translated-content -->

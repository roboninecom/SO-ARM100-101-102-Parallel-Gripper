<!-- translation-navigation -->
[English](../../../en/simulation/isaac_sim/README.md) · [Русский](../../../ru/simulation/isaac_sim/README.md) · [Español](../../../es/simulation/isaac_sim/README.md) · [Français](../../../fr/simulation/isaac_sim/README.md) · [Deutsch](../../../de/simulation/isaac_sim/README.md) · [Português (Brasil)](../../../pt-BR/simulation/isaac_sim/README.md) · [简体中文](../../../zh-CN/simulation/isaac_sim/README.md) · [日本語](../../../ja/simulation/isaac_sim/README.md) · [हिन्दी](../../../hi/simulation/isaac_sim/README.md) · [العربية](README.md)

[الأصل الإنجليزي](../../../../../simulation/isaac_sim/README.md)

[العربية](../../README.md)

> ترجمة آلية كاملة لم يراجعها متحدثون أصليون بعد. الصور والشيفرة وملفات CAD وPDF الأصلية مشتركة. عند الالتباس يُرجى الرجوع إلى الأصل الإنجليزي.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="nvidia-isaac-sim"></a>
# نفيديا Isaac نعم

**حالة: لم يتم اختبارها (المحاكي الخارجي)**

Isaac سيم يعمل خارجيًا ويتواصل مع ROS2 عن طريق `topic_based_ros2_control`. أنت تهرب Isaac قم بتجهيزها بشكل منفصل وإطلاق ROS2 الجانب `sim:=isaac`.

<a id="prerequisites"></a>
## الشروط المسبقة

- [نفيديا Isaac نعم](https://developer.nvidia.com/isaac-sim) 4.0+ (تطلب GPU NVIDIA RTX)
- ROS2 التواضع
- Isaac نعم ROS2 تمكين الجسر
- `topic_based_ros2_control`:
  ```bash
  sudo apt install ros-humble-topic-based-ros2-control
  ```

<a id="setup"></a>
## الإعداد

<a id="1-import-urdf-into-isaac-sim"></a>
### 1. استيراد URDF إلى Isaac نعم

```bash
# Generate expanded URDF
source /opt/ros/humble/setup.bash
xacro so_arm_101_description/urdf/so_101.urdf.xacro sim_backend:=isaac > /tmp/so_101_isaac.urdf
```

في Isaac نعم
1. **Isaac الاستخدامات > مستورد URDF**
2. **ملف إدخال**إختيار: `/tmp/so_101_isaac.urdf`
3. **مكان الاستيراد**: `/World/so_101`
4. **نوع القيادة المشتركة**الموقع:
5. **إصلاح رابط الأساس**: تم التحقق منها
6. انقر **الاستيراد**
7. إضافة طائرة أرضية: **إنشاء > الفيزياء > الطائرة الأرضية**
8. باستثناء مرحلة الدولار الأمريكي (اختياري)

<a id="2-configure-ros2-bridge-omnigraph"></a>
### 2. الإعداد ROS2 الجسر (OmniGraph)

(الـ) `topic_based_ros2_control` المكون يتواصل عبر هذه الموضوعات:

| الموضوع | النوع | الاتجاه |
|-------|------|-----------|
| `/joint_states` | `sensor_msgs/JointState` | Isaac سم -> ROS2 |
| `/joint_commands` | `std_msgs/Float64MultiArray` | ROS2 -> Isaac نعم |

<a id="omnigraph-setup"></a>
#### إعداد OmniGraph

1. مفتوحة **النافذة > النص البصري > الرسم البياني للعمل**
2. إعداد الرسم البياني للعمل الجديد
3. إضافة هذه العقد:
   - **على علامة التشغيل** (مصدر الحدث)
   - **Isaac قراءة وقت المحاكاة**
   - **ROS2 نشر الدولة المشتركة** -- الاتصال `/World/so_101`
   - **ROS2 التوقيع على الدولة المشتركة** - لتلقي الأوامر
   - **Isaac جهاز تحكم المفاصل** - يطبق الأوامر على المفاصل

4. ربط الرسم البياني:
   ```
   On Playback Tick -> Read Sim Time -> Publish Joint State
   On Playback Tick -> Subscribe Joint State -> Articulation Controller
   ```

5. الإعداد **نشر الدولة المشتركة** العقدة:
   - `targetPrim`: `/World/so_101`
   - `topicName`: `/joint_states`

6. الإعداد **جهاز تحكم المفاصل** العقدة:
   - `targetPrim`: `/World/so_101`
   - `jointNames`جميعها:7الأسماء المشتركة من `config/controllers.yaml`

<a id="alternative-isaac_ros2_control"></a>
#### البديل: isaac_ros2_control

إذا `isaac_ros2_control` متاح لك Isaac نسخة Sim:

```bash
sudo apt install ros-humble-isaac-ros2-control
```

هذا يحل محل إعداد OmniGraph بإعداد مباشر `ros2_control` واجهة الأجهزة

<a id="3-launch"></a>
### 3. إطلاق

```bash
# Terminal 1: Start Isaac Sim and press Play

# Terminal 2: Launch ROS2 side
ros2 launch so_arm_101_description sim.launch.py sim:=isaac
```

<a id="verify"></a>
## التأكد

```bash
ros2 topic echo /joint_states --once

ros2 topic pub /arm_controller/joint_trajectory trajectory_msgs/msg/JointTrajectory "{
  joint_names: ['base_link_to_link1'],
  points: [{positions: [0.5], time_from_start: {sec: 2}}]
}" --once
```

<a id="troubleshooting"></a>
## حل المشاكل

- **فشل في استيراد URDF**: تأكد من أن جميع مسارات الشبكة مطلقة. إنشاء URDF مع `xacro` أولا - لا تستورد `.xacro` الملف مباشرة.
- **لا دول مشتركة**: التحقق من أن OmniGraph متصل و Isaac سيم في وضع اللعب.
- **عدم الاستقرار في الفيزياء**: في خصائص المشهد الفيزيائي، حدد نوع الحل إلى TGS وزيادة عدد التكرار.
- **ROS2 الجسر لم يجد**: تمكين التوسع في **النافذة > التوسع > ROS2 الجسر**.
<!-- /translated-content -->

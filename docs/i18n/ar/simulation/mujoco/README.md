<!-- translation-navigation -->
[English](../../../en/simulation/mujoco/README.md) · [Русский](../../../ru/simulation/mujoco/README.md) · [Español](../../../es/simulation/mujoco/README.md) · [Français](../../../fr/simulation/mujoco/README.md) · [Deutsch](../../../de/simulation/mujoco/README.md) · [Português (Brasil)](../../../pt-BR/simulation/mujoco/README.md) · [简体中文](../../../zh-CN/simulation/mujoco/README.md) · [日本語](../../../ja/simulation/mujoco/README.md) · [हिन्दी](../../../hi/simulation/mujoco/README.md) · [العربية](README.md)

[الأصل الإنجليزي](../../../../../simulation/mujoco/README.md)

[العربية](../../README.md)

> ترجمة آلية كاملة لم يراجعها متحدثون أصليون بعد. الصور والشيفرة وملفات CAD وPDF الأصلية مشتركة. عند الالتباس يُرجى الرجوع إلى الأصل الإنجليزي.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="mujoco"></a>
# MuJoCo

**الحالة: جاهزة**

MuJoCo المحاكاة باستخدام `mujoco_ros2_control` (المركز يسيطر على الشوكة) MuJoCo تحويل URDF إلى MJCF داخليا وتشغيل الفيزياء + التصوير في `ros2_control_node` العملية

<a id="prerequisites"></a>
## الشروط المسبقة

**Docker (موصى به):**
- أداة المكتب

**الأصلي ROS2:**
- ROS2 التواضع
- `mujoco_ros2_control` (من المصدر - انظر أدناه)
- `mujoco` حزمة النفط

<a id="launch"></a>
## إطلاق

<a id="docker"></a>
### (دوكر)

```bash
cd simulation/so_arm_101_description
docker compose run mujoco
```

تصميم صورة دوكر `mujoco_ros2_control` من المصدر تلقائياً

<a id="native-ros2"></a>
### الأصلي ROS2

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
## كيف يعمل

1. التضمين `mujoco_ros2_control/MujocoSystemInterface` يتم اختيارها عن طريق `sim_backend:=mujoco`
2. عقد مخصص (`publish_mujoco_description`) يُعلن عن URDF `/mujoco_robot_description`
3. (الـ) MuJoCo يقرأ المضغوط URDF ، ويحوله إلى MJCF ، ويبدأ المحاكاة
4. (الـ) `<mujoco><compiler meshdir=.../>` علامة في URDF تقول MuJoCo أين يمكن العثور على شبكات التصادم
5. يفتح نافذة التصوير تظهر المحاكاة (1280x720، تم تصحيحها من افتراضية الشاشة الكاملة)

<a id="key-parameters-in-so_101ros2_controlxacro"></a>
### المعايير الرئيسية (في `so_101.ros2_control.xacro`)

- `headless`تعيين: `true` لنظام بدون رأس (لا توجد نافذة إظهار)
- `sim_speed_factor`: مضاعف سرعة المحاكاة (تخلفيا: 1.0)

<a id="verify"></a>
## التأكد

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
## حل المشاكل

- **أخطاء OpenGL**: تأكد من تثبيت برامج تشغيل GPU. بالنسبة لـ (دوكر) ، لا تعليق على حظر GPU NVIDIA في `docker-compose.yaml`.
- **نافذة كبيرة جدا**: صورة Docker تصحيح النافذة إلى 1280x720. بالنسبة لتركيبات محلية، MuJoCo يمكن أن تكون النافذة كاملة الشاشة افتراضيًا
- **لا يوجد عرض**: MuJoCo يحتاج إلى خادم X11 لنفذة التصوير. الاستخدام `headless:=true` في xacro إذا لم يكن هناك عرض متاح.
<!-- /translated-content -->

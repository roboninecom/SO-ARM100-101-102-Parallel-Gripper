<!-- translation-navigation -->
[English](../../../en/simulation/gazebo/README.md) · [Русский](../../../ru/simulation/gazebo/README.md) · [Español](../../../es/simulation/gazebo/README.md) · [Français](../../../fr/simulation/gazebo/README.md) · [Deutsch](../../../de/simulation/gazebo/README.md) · [Português (Brasil)](../../../pt-BR/simulation/gazebo/README.md) · [简体中文](../../../zh-CN/simulation/gazebo/README.md) · [日本語](../../../ja/simulation/gazebo/README.md) · [हिन्दी](../../../hi/simulation/gazebo/README.md) · [العربية](README.md)

[الأصل الإنجليزي](../../../../../simulation/gazebo/README.md)

[العربية](../../README.md)

> ترجمة آلية كاملة لم يراجعها متحدثون أصليون بعد. الصور والشيفرة وملفات CAD وPDF الأصلية مشتركة. عند الالتباس يُرجى الرجوع إلى الأصل الإنجليزي.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="gazebo-gz-sim"></a>
# Gazebo (غز-سم)

**الحالة: جاهزة**

Gazebo المحاكاة باستخدام `gz_ros2_control` المضخة. مدير المراقبة يذهب داخل Gazebo العملية

<a id="prerequisites"></a>
## الشروط المسبقة

**Docker (موصى به):**
- أداة المكتب

**الأصلي ROS2:**
- ROS2 التواضع
- `ros-humble-gz-ros2-control`
- `ros-humble-ros-gz-sim`
- `ros-humble-ros-gz-bridge`

<a id="launch"></a>
## إطلاق

<a id="docker"></a>
### (دوكر)

```bash
cd simulation/so_arm_101_description
docker compose run gazebo
```

بالنسبة لـ NVIDIA GPU من خلال، لا تعليق على `deploy:` حلقة في `docker-compose.yaml`:

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
### الأصلي ROS2

```bash
ros2 launch so_arm_101_description sim.launch.py sim:=gazebo
```

<a id="how-it-works"></a>
## كيف يعمل

1. (الـ) Gazebo إضافة `gz_ros2_control/GazeboSimSystem` يتم اختيارها عبر `sim_backend:=gazebo` حجة xacro
2. Gazebo يدمج مدير التحكم -- لا يوجد منفصل `ros2_control_node` مطلوبة
3. الروبوت تم إنجابها في `worlds/empty.sdf` عن طريق `ros_gz_sim create`
4. أجهزة التحكم تبدأ بعد `robot_state_publisher` هو يجري

<a id="world-file"></a>
### الملف العالمي

`worlds/empty.sdf` تنص على:
- محرك الفيزياء ODE (خطوة زمنية 0.004s / 250 هرتز)
- الطائرة الأرضية (100 × 100 متر)
- الإضاءة الشمسية التوجيهية

<a id="verify"></a>
## التأكد

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
## حل المشاكل

- **لا توجد شبكات**: التأكد `GZ_SIM_RESOURCE_PATH` يتضمن دليل حصص الحزمة. نقطة دخول (دوكر) تعيين هذا تلقائياً
- **لا يوجد عرض**: Gazebo يحتاج إلى خادم X11. على Windows، استخدم VcXsrv مع `-ac` العلم. على macOS، استخدم XQuartz.
- **التعبير البطيء**: لا تعليق على المقاطعة `docker-compose.yaml` إذا كان لديك GPU NVIDIA.
<!-- /translated-content -->

<!-- translation-navigation -->
[English](../../en/simulation/README.md) · [Русский](../../ru/simulation/README.md) · [Español](../../es/simulation/README.md) · [Français](../../fr/simulation/README.md) · [Deutsch](../../de/simulation/README.md) · [Português (Brasil)](../../pt-BR/simulation/README.md) · [简体中文](../../zh-CN/simulation/README.md) · [日本語](../../ja/simulation/README.md) · [हिन्दी](../../hi/simulation/README.md) · [العربية](README.md)

[الأصل الإنجليزي](../../../../simulation/README.md)

[العربية](../README.md)

> ترجمة آلية كاملة لم يراجعها متحدثون أصليون بعد. الصور والشيفرة وملفات CAD وPDF الأصلية مشتركة. عند الالتباس يُرجى الرجوع إلى الأصل الإنجليزي.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="simulation"></a>
# المحاكاة

ROS2 دعم المحاكاة SO-ARM-101 ذراع روبوتية مع قبضة متوازية. يُدفع نظام URDF واحد المعلم 5 محركات فيزيائية من خلال ملف إطلاق واحد.

<a id="gazebo-ignition-fortress"></a>
## Gazebo (حصن الإضاءة)

![SO-ARM-101 في Gazebo](../../../../assets/images/simulation/gazebo/gazebo_pick_place.png)

*SO-ARM-101 أداء اختيار & مكان في Gazebo ⁇  يختار الذراع شيئاً ويضعها على رف فوق.*

<a id="mujoco"></a>
## MuJoCo

![SO-ARM-101 في MuJoCo](../../../../assets/images/simulation/mujoco/mujoco_pick_place.png)

*نفس التسلسل اختيار ووضع يبدأ في MuJoCo مع محاكاة الفيزياء الكاملة.*

<a id="simulator-status"></a>
## حالة المحاكي

| محاكاة | الحالة | (دوكر) | مدير المراقب |
|-----------|--------|--------|--------------------|
| [Gazebo (غز-سم)](gazebo/README.md) | جاهز | `docker compose run gazebo` | مدمج في المحاكي |
| [MuJoCo](mujoco/README.md) | جاهز | `docker compose run mujoco` | الخارجي (`ros2_control_node`) |
| [Webots](webots/README.md) | غير مستقرة | `docker compose run webots` | متضمنة في السائق |
| [CoppeliaSim](coppeliasim/README.md) | لم يتم اختباره | N/A (التنسيق الخارجي) | الخارجي (`ros2_control_node`) |
| [نفيديا Isaac نعم](isaac_sim/README.md) | لم يتم اختباره | N/A (التنسيق الخارجي) | الخارجي (`ros2_control_node`) |

<a id="architecture"></a>
## الهندسة المعمارية

- **الـ URDF الواحد** -- `so_arm_101_description/urdf/so_101.urdf.xacro` هو وصف الروبوت الوحيد لجميع المحاكاة
- **الخلفيات المتعبرة** -- `sim_backend:=gazebo|mujoco|webots|coppeliasim|isaac` يختار `ros2_control` إضافة في وقت توسيع xacro
- **وحدات التحكم** -- `config/controllers.yaml` يحدد نفس المفاصل والواجهات وأسماء المحكمين على جميع الخلفيات
- **ملف إطلاق واحد** -- `launch/sim.launch.py` مع `sim:=<backend>` الحجة

<a id="robot"></a>
### الروبوت

- **ذراع 5-DOF**: دورة القاعدة، ارتفاع الكتف، المرفق، ارتفاع المعصم، رول معصم
- **قابض متوازٍ**: 2 مفصلات ضغط منقطعة (مرايا الضغط اليسرى يمينا عبر `<mimic>`)
- **الخدمات**: STS3215 (1.5 Nm من الدوران، 5.2 rad/s السرعة)

<a id="prerequisites"></a>
## الشروط المسبقة

**الخيار A: Docker (موصى به، لا) ROS2 إضافة مطلوبة)**

- أداة المكتب

**الخيار ب: الأصلي ROS2**

- ROS2 التواضع
- الاعتمادات الخاصة بالمحاكي (انظر الدليل لكل محاكي)

<a id="installation"></a>
## التثبيت

<a id="docker-recommended"></a>
### Docker (موصى به)

```bash
cd simulation/so_arm_101_description
docker compose run gazebo    # or mujoco, webots
```

<a id="native-ros2"></a>
### الأصلي ROS2

```bash
# Copy the ROS2 package into your workspace
cp -r simulation/so_arm_101_description ~/ros2_ws/src/

# Install dependencies
cd ~/ros2_ws
rosdep install --from-paths src --ignore-src -r -y

# Build
colcon build --packages-select so_arm_101_description
source install/setup.bash
```

<a id="quick-start"></a>
## بداية سريعة

```bash
# RViz visualization (no simulator needed)
ros2 launch so_arm_101_description display.launch.py

# Launch a simulator
ros2 launch so_arm_101_description sim.launch.py sim:=gazebo
ros2 launch so_arm_101_description sim.launch.py sim:=mujoco
ros2 launch so_arm_101_description sim.launch.py sim:=webots
ros2 launch so_arm_101_description sim.launch.py sim:=coppeliasim
ros2 launch so_arm_101_description sim.launch.py sim:=isaac
```

<a id="commanding-the-robot"></a>
## قيادة الروبوت

```bash
# Check joint states
ros2 topic echo /joint_states --once

# Move arm via trajectory action
ros2 action send_goal /arm_controller/follow_joint_trajectory \
  control_msgs/action/FollowJointTrajectory "{
    trajectory: {
      joint_names: [base_link_to_link1, link1_to_link2, link2_to_link3, link3_to_link4, link4_to_link5],
      points: [{positions: [0.5, -0.5, 0.8, -0.3, 0.0], time_from_start: {sec: 2}}]
    }
  }"
```

<a id="docker-services"></a>
## خدمات المرفأ

يتم تعريف جميع الخدمات في `so_arm_101_description/docker-compose.yaml`:

```bash
docker compose run build       # Interactive shell with built workspace
docker compose run validate    # Validate URDF for all 5 backends
docker compose run test        # Run 65 offline pytest tests
docker compose run check-launch # Verify launch files parse
docker compose run rviz        # RViz (needs X11)
docker compose run gazebo      # Gazebo (needs X11)
docker compose run mujoco      # MuJoCo (needs X11)
docker compose run webots      # Webots (needs X11)
```

<a id="collision-meshes"></a>
## شبكات التصادم

يتم توفير شبكات تصادم الهيكل المتواصلة المبسطة في `so_arm_101_description/meshes/collision/`. للتجديد:

```bash
pip install trimesh
python scripts/generate_collision_meshes.py
```

<a id="package-structure"></a>
## هيكل الحزمة

```
so_arm_101_description/
├── urdf/
│   ├── so_101.urdf.xacro          # Main robot description
│   ├── so_101.ros2_control.xacro  # Parameterized hardware interface
│   └── materials.xacro
├── meshes/
│   ├── visual/                    # High-poly STL for rendering
│   └── collision/                 # Convex hull STL for physics
├── config/
│   ├── controllers.yaml           # Shared controller config
│   └── display.rviz
├── launch/
│   ├── display.launch.py          # RViz visualization
│   └── sim.launch.py              # Unified simulator launcher
├── worlds/
│   ├── empty.sdf                  # Gazebo world
│   └── webots_world.wbt           # Webots world
├── scripts/
│   ├── generate_collision_meshes.py
│   ├── publish_mujoco_description.py
│   ├── setup_webots.py
│   └── validate_xml.py
├── docker/
│   ├── entrypoint.sh
│   └── constrain-window.sh
├── test/                          # 65 offline tests
├── Dockerfile                     # Multi-stage (base/test/rviz/gazebo/mujoco/webots)
├── docker-compose.yaml
├── package.xml
└── setup.py
```
<!-- /translated-content -->

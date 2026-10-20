<!-- translation-navigation -->
[English](../../en/simulation/README.md) · [Русский](../../ru/simulation/README.md) · [Español](../../es/simulation/README.md) · [Français](../../fr/simulation/README.md) · [Deutsch](../../de/simulation/README.md) · [Português (Brasil)](../../pt-BR/simulation/README.md) · [简体中文](../../zh-CN/simulation/README.md) · [日本語](../../ja/simulation/README.md) · [हिन्दी](README.md) · [العربية](../../ar/simulation/README.md)

[अंग्रेज़ी मूल](../../../../simulation/README.md)

[हिन्दी](../README.md)

> यह पूरे दस्तावेज़ का मशीन अनुवाद है; मूल भाषा बोलने वालों ने अभी इसकी समीक्षा नहीं की है। चित्र, कोड, CAD और मूल PDF साझा हैं। अस्पष्टता होने पर अंग्रेज़ी मूल देखें।
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="simulation"></a>
# सिमुलेशन

ROS2 सिमुलेशन सहायता SO-ARM-101 समानांतर पकड़ के साथ रोबोट हाथ। एक पैरामीटर URDF एक प्रक्षेपण फ़ाइल के माध्यम से 5 भौतिकी इंजन चलाता है।

<a id="gazebo-ignition-fortress"></a>
## Gazebo (इग्निशन किले)

![SO-ARM-101 में Gazebo](../../../../assets/images/simulation/gazebo/gazebo_pick_place.png)

*SO-ARM-101 प्रदर्शन करने के लिए चुनें & जगह में Gazebo ⁇  हाथ किसी वस्तु को उठाता है और उसे ऊपर की शेल्फ पर रखता है।*

<a id="mujoco"></a>
## MuJoCo

![SO-ARM-101 में MuJoCo](../../../../assets/images/simulation/mujoco/mujoco_pick_place.png)

*एक ही पिक एंड प्लेस अनुक्रम में चल रहा है MuJoCo पूर्ण भौतिकी अनुकरण के साथ.*

<a id="simulator-status"></a>
## सिम्युलेटर की स्थिति

| सिम्युलेटर | स्थिति | डॉकर | नियंत्रक प्रबंधक |
|-----------|--------|--------|--------------------|
| [Gazebo (गज़-सिम)](gazebo/README.md) | तैयार | `docker compose run gazebo` | सिम्युलेटर में सम्मिलित |
| [MuJoCo](mujoco/README.md) | तैयार | `docker compose run mujoco` | बाहरी (`ros2_control_node`) |
| [Webots](webots/README.md) | अस्थिर | `docker compose run webots` | ड्राइवर में एम्बेड |
| [CoppeliaSim](coppeliasim/README.md) | परीक्षण नहीं किया | N/A (बाहरी सिमिंग) | बाहरी (`ros2_control_node`) |
| [एनवीडीआईए Isaac हाँ](isaac_sim/README.md) | परीक्षण नहीं किया | N/A (बाहरी सिमिंग) | बाहरी (`ros2_control_node`) |

<a id="architecture"></a>
## वास्तुकला

- **एकल URDF** -- `so_arm_101_description/urdf/so_101.urdf.xacro` सभी सिम्युलेटर के लिए एकमात्र रोबोट विवरण है
- **पैरामेटरीकृत बैकेंड** -- `sim_backend:=gazebo|mujoco|webots|coppeliasim|isaac` चुनता है `ros2_control` xacro विस्तार समय पर प्लगइन
- **एकीकृत नियंत्रक** -- `config/controllers.yaml` सभी बैकेंड पर एक ही जोड़ों, इंटरफेस और नियंत्रक नाम परिभाषित करता है
- **एक प्रक्षेपण फ़ाइल** -- `launch/sim.launch.py` के साथ `sim:=<backend>` तर्क

<a id="robot"></a>
### रोबोट

- **5-डीओएफ हाथ**: आधार घूर्णन, कंधे की पिच, कोहनी, कलाई की पिच, कलाई रोल
- **समानांतर ग्रिपर**: 2 प्रिस्मेटिक क्लैंप जंक्शन (बाएं क्लैंप दर्पण दाईं ओर `<mimic>`)
- **सरबोस**: STS3215 (1.5 Nm टोक़, 5.2 rad/s गति)

<a id="prerequisites"></a>
## पूर्व शर्तें

**विकल्प A: डॉकर (अनुशंसित, नहीं) ROS2 स्थापित करने की आवश्यकता)**

- डॉकर डेस्कटॉप

**विकल्प बी: मूल ROS2**

- ROS2 विनम्र
- सिमुलेटर-विशिष्ट निर्भरताएं (प्रति सिम्युलेटर गाइड देखें)

<a id="installation"></a>
## स्थापना

<a id="docker-recommended"></a>
### डॉकर (अनुशंसित)

```bash
cd simulation/so_arm_101_description
docker compose run gazebo    # or mujoco, webots
```

<a id="native-ros2"></a>
### स्वदेशी ROS2

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
## त्वरित शुरुआत

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
## रोबोट का आदेश

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
## डॉकर सेवाएं

सभी सेवाएँ `so_arm_101_description/docker-compose.yaml`:

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
## टकराव जाल

सरलीकृत घुमावदार पतवार टकराव जाल में प्रदान की जाती हैं `so_arm_101_description/meshes/collision/`. पुनरुत्पादित करने के लिएः

```bash
pip install trimesh
python scripts/generate_collision_meshes.py
```

<a id="package-structure"></a>
## पैकेज संरचना

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

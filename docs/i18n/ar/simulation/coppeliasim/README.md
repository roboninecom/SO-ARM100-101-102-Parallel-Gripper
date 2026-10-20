<!-- translation-navigation -->
[English](../../../en/simulation/coppeliasim/README.md) · [Русский](../../../ru/simulation/coppeliasim/README.md) · [Español](../../../es/simulation/coppeliasim/README.md) · [Français](../../../fr/simulation/coppeliasim/README.md) · [Deutsch](../../../de/simulation/coppeliasim/README.md) · [Português (Brasil)](../../../pt-BR/simulation/coppeliasim/README.md) · [简体中文](../../../zh-CN/simulation/coppeliasim/README.md) · [日本語](../../../ja/simulation/coppeliasim/README.md) · [हिन्दी](../../../hi/simulation/coppeliasim/README.md) · [العربية](README.md)

[الأصل الإنجليزي](../../../../../simulation/coppeliasim/README.md)

[العربية](../../README.md)

> ترجمة آلية كاملة لم يراجعها متحدثون أصليون بعد. الصور والشيفرة وملفات CAD وPDF الأصلية مشتركة. عند الالتباس يُرجى الرجوع إلى الأصل الإنجليزي.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="coppeliasim"></a>
# CoppeliaSim

**حالة: لم يتم اختبارها (المحاكي الخارجي)**

CoppeliaSim تعمل خارجا وتتواصل مع ROS2 عن طريق `topic_based_ros2_control`. أنت تهرب CoppeliaSim بشكل منفصل وإطلاق ROS2 الجانب `sim:=coppeliasim`.

<a id="prerequisites"></a>
## الشروط المسبقة

- [CoppeliaSim إدارة الطاقة/التنمية](https://www.coppeliarobotics.com/downloads) v4.6+
- ROS2 التواضع
- `simROS2` إضافة فعالة في CoppeliaSim
- `topic_based_ros2_control`:
  ```bash
  sudo apt install ros-humble-topic-based-ros2-control
  ```

<a id="setup"></a>
## الإعداد

<a id="1-import-urdf-into-coppeliasim"></a>
### 1. استيراد URDF إلى CoppeliaSim

```bash
# Generate expanded URDF
source /opt/ros/humble/setup.bash
xacro so_arm_101_description/urdf/so_101.urdf.xacro sim_backend:=coppeliasim > /tmp/so_101_coppeliasim.urdf
```

في CoppeliaSim:
1. **الملف > الاستيراد > URDF...**
2. إختيار `/tmp/so_101_coppeliasim.urdf`
3. تحقق **تخصيص أشكال التصادم للأشكال المرئية**
4. تحقق **تخصيص الكتلة والعجز للشكلات**
5. انقر **الاستيراد**
6. حفظ المشهد (اختياري: `worlds/coppeliasim_scene.ttt`)

<a id="2-add-ros2-bridge-script"></a>
### 2. إضافة ROS2 نص الجسر

(الـ) `topic_based_ros2_control` المكون يتواصل عبر هذه الموضوعات:

| الموضوع | النوع | الاتجاه |
|-------|------|-----------|
| `/joint_states` | `sensor_msgs/JointState` | CoppeliaSim -> ROS2 |
| `/joint_commands` | `std_msgs/Float64MultiArray` | ROS2 -> CoppeliaSim |

إضافة a **النص الصغار** إلى الرابط الأساسي للروبوت مع رمز Lua هذا:

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
### 3. إطلاق

```bash
# Terminal 1: Start CoppeliaSim with the scene loaded and press Play

# Terminal 2: Launch ROS2 side
ros2 launch so_arm_101_description sim.launch.py sim:=coppeliasim
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

- **simROS2 لا تحميل**: التأكد `libsimROS2.so` هو في CoppeliaSimإداري المكونات و `ROS_DISTRO=humble` لقد تم تحديدها
- **لا دول مشتركة**: التحقق من أن الخطوط Lua مرفقة إلى الكائن الصحيح وتشغيل المحاكاة.
- **الإسم المشترك غير مطابق**: الأسماء المشتركة في الخطوط Lua يجب أن تتطابق تماما مع تلك في `config/controllers.yaml`.
<!-- /translated-content -->

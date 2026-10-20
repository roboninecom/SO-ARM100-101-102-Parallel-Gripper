<!-- translation-navigation -->
[English](../../../en/simulation/coppeliasim/README.md) · [Русский](README.md) · [Español](../../../es/simulation/coppeliasim/README.md) · [Français](../../../fr/simulation/coppeliasim/README.md) · [Deutsch](../../../de/simulation/coppeliasim/README.md) · [Português (Brasil)](../../../pt-BR/simulation/coppeliasim/README.md) · [简体中文](../../../zh-CN/simulation/coppeliasim/README.md) · [日本語](../../../ja/simulation/coppeliasim/README.md) · [हिन्दी](../../../hi/simulation/coppeliasim/README.md) · [العربية](../../../ar/simulation/coppeliasim/README.md)

[Английский оригинал](../../../../../simulation/coppeliasim/README.md)

[Русский](../../README.md)

> Полный машинный перевод; носители языка его ещё не проверяли. Изображения, код, CAD и исходные PDF общие. При неоднозначности используйте английский оригинал.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="coppeliasim"></a>
# CoppeliaSim

**Статус: Не проверенный (внешний симулятор)**

CoppeliaSim работает снаружи и общается с ROS2 через `topic_based_ros2_control`. Ты бежишь . CoppeliaSim отдельно и запустить ROS2 стороной с `sim:=coppeliasim`.

<a id="prerequisites"></a>
## Предусмотренные условия

- [CoppeliaSim ЭДУ/ПРО](https://www.coppeliarobotics.com/downloads) v4.6+
- ROS2 Смирение
- `simROS2` включенный плагин CoppeliaSim
- `topic_based_ros2_control`:
  ```bash
  sudo apt install ros-humble-topic-based-ros2-control
  ```

<a id="setup"></a>
## Настройка

<a id="1-import-urdf-into-coppeliasim"></a>
### 1. Импорт URDF в CoppeliaSim

```bash
# Generate expanded URDF
source /opt/ros/humble/setup.bash
xacro so_arm_101_description/urdf/so_101.urdf.xacro sim_backend:=coppeliasim > /tmp/so_101_coppeliasim.urdf
```

В CoppeliaSim:
1. **Файл > Импорт > URDF...**
2. Выберите `/tmp/so_101_coppeliasim.urdf`
3. Проверка **Назначать формы столкновения на видимые формы**
4. Проверка **Присвоение массы и инерции к формам**
5. Нажмите **Импорт**
6. Сохранить сцену (необязательно: `worlds/coppeliasim_scene.ttt`)

<a id="2-add-ros2-bridge-script"></a>
### 2. Добавить ROS2 Сценарий моста

В. `topic_based_ros2_control` Plugin общается через эти темы:

| Тема | Тип | Направление |
|-------|------|-----------|
| `/joint_states` | `sensor_msgs/JointState` | CoppeliaSim -> ROS2 |
| `/joint_commands` | `std_msgs/Float64MultiArray` | ROS2 -> CoppeliaSim |

Добавить **детский сценарий** к базовой ссылке робота с этим кодом Lua:

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
### 3. Запуск

```bash
# Terminal 1: Start CoppeliaSim with the scene loaded and press Play

# Terminal 2: Launch ROS2 side
ros2 launch so_arm_101_description sim.launch.py sim:=coppeliasim
```

<a id="verify"></a>
## Проверка

```bash
ros2 topic echo /joint_states --once

ros2 topic pub /arm_controller/joint_trajectory trajectory_msgs/msg/JointTrajectory "{
  joint_names: ['base_link_to_link1'],
  points: [{positions: [0.5], time_from_start: {sec: 2}}]
}" --once
```

<a id="troubleshooting"></a>
## Устранение неполадок

- **simROS2 не загружается**Убедитесь: `libsimROS2.so` Входит в CoppeliaSimСправочник плагинов и `ROS_DISTRO=humble` Установлено.
- **Совместные государства**: Проверьте, что сценарий Lua прикреплен к правильному объекту и симуляция работает.
- **Несовместимость названий**: Совместные имена в письме Луа должны соответствовать точно тем, что в `config/controllers.yaml`.
<!-- /translated-content -->

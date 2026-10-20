<!-- translation-navigation -->
[English](../../../en/simulation/gazebo/README.md) · [Русский](README.md) · [Español](../../../es/simulation/gazebo/README.md) · [Français](../../../fr/simulation/gazebo/README.md) · [Deutsch](../../../de/simulation/gazebo/README.md) · [Português (Brasil)](../../../pt-BR/simulation/gazebo/README.md) · [简体中文](../../../zh-CN/simulation/gazebo/README.md) · [日本語](../../../ja/simulation/gazebo/README.md) · [हिन्दी](../../../hi/simulation/gazebo/README.md) · [العربية](../../../ar/simulation/gazebo/README.md)

[Английский оригинал](../../../../../simulation/gazebo/README.md)

[Русский](../../README.md)

> Полный машинный перевод; носители языка его ещё не проверяли. Изображения, код, CAD и исходные PDF общие. При неоднозначности используйте английский оригинал.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="gazebo-gz-sim"></a>
# Gazebo (гз-сим)

**Статус: Готовый**

Gazebo симуляции с использованием `gz_ros2_control` Вставка. Менеджер контроллера бежит внутрь Gazebo процесс.

<a id="prerequisites"></a>
## Предусмотренные условия

**Докер (рекомендуется):**
- Рабочий стол Docker

**Родина ROS2:**
- ROS2 Смирение
- `ros-humble-gz-ros2-control`
- `ros-humble-ros-gz-sim`
- `ros-humble-ros-gz-bridge`

<a id="launch"></a>
## Запуск

<a id="docker"></a>
### Докер

```bash
cd simulation/so_arm_101_description
docker compose run gazebo
```

Для NVIDIA GPU прохожие, не комментируйте `deploy:` блок в `docker-compose.yaml`:

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
### Родина ROS2

```bash
ros2 launch so_arm_101_description sim.launch.py sim:=gazebo
```

<a id="how-it-works"></a>
## Как это работает

1. В. Gazebo плагин `gz_ros2_control/GazeboSimSystem` выбирается через `sim_backend:=gazebo` аргумент xacro
2. Gazebo внедряет управляющего контроллером - нет отдельных `ros2_control_node` необходимые
3. Робот создан в `worlds/empty.sdf` через `ros_gz_sim create`
4. Контроллерные порожники начинаются после `robot_state_publisher` бежит

<a id="world-file"></a>
### Всемирный файл

`worlds/empty.sdf` предусматривает:
- Двигатель физики ODE (срок времени)0.004s / 250Гц)
- Наземная плоскость (100x100 м)
- Направленное солнечное освещение

<a id="verify"></a>
## Проверка

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
## Устранение неполадок

- **Не найденные сетки**Убедитесь: `GZ_SIM_RESOURCE_PATH` включает в себя каталог пакетной доли. Входный пункт Docker устанавливает это автоматически.
- **Нет дисплея**: Gazebo Нужен сервер X11. В Windows используйте VcXsrv с `-ac` флаг. На macOS используйте XQuartz.
- **Медленная передача**: Не комментируйте проход GPU через блок в `docker-compose.yaml` если у вас есть NVIDIA GPU.
<!-- /translated-content -->

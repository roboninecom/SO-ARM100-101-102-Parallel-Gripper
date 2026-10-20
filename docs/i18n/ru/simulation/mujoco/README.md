<!-- translation-navigation -->
[English](../../../en/simulation/mujoco/README.md) · [Русский](README.md) · [Español](../../../es/simulation/mujoco/README.md) · [Français](../../../fr/simulation/mujoco/README.md) · [Deutsch](../../../de/simulation/mujoco/README.md) · [Português (Brasil)](../../../pt-BR/simulation/mujoco/README.md) · [简体中文](../../../zh-CN/simulation/mujoco/README.md) · [日本語](../../../ja/simulation/mujoco/README.md) · [हिन्दी](../../../hi/simulation/mujoco/README.md) · [العربية](../../../ar/simulation/mujoco/README.md)

[Английский оригинал](../../../../../simulation/mujoco/README.md)

[Русский](../../README.md)

> Полный машинный перевод; носители языка его ещё не проверяли. Изображения, код, CAD и исходные PDF общие. При неоднозначности используйте английский оригинал.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="mujoco"></a>
# MuJoCo

**Статус: Готовый**

MuJoCo симуляции с использованием `mujoco_ros2_control` (роскоконтрольный вилок). MuJoCo преобразует URDF в MJCF внутренне и выполняет физику + рендеринг в `ros2_control_node` процесс.

<a id="prerequisites"></a>
## Предусмотренные условия

**Докер (рекомендуется):**
- Рабочий стол Docker

**Родина ROS2:**
- ROS2 Смирение
- `mujoco_ros2_control` (из источника - см. ниже)
- `mujoco` упаковка

<a id="launch"></a>
## Запуск

<a id="docker"></a>
### Докер

```bash
cd simulation/so_arm_101_description
docker compose run mujoco
```

Изображение Докера создается `mujoco_ros2_control` из источника автоматически.

<a id="native-ros2"></a>
### Родина ROS2

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
## Как это работает

1. Вставка `mujoco_ros2_control/MujocoSystemInterface` выбирается через `sim_backend:=mujoco`
2. Настроенный узел (`publish_mujoco_description`) публикует URDF в `/mujoco_robot_description`
3. В. MuJoCo плагин читает URDF, преобразует его в MJCF и запускает моделирование
4. В. `<mujoco><compiler meshdir=.../>` Тег в URDF говорит MuJoCo где найти столкновение сетки
5. Открывается окно рендеринга, показывающее симуляцию (1280x720, отремонтированная по умолчанию на полный экран)

<a id="key-parameters-in-so_101ros2_controlxacro"></a>
### Ключевые параметры `so_101.ros2_control.xacro`)

- `headless`Настроен на: `true` для режима без головы (без рендерингового окна)
- `sim_speed_factor`: Умножитель скорости моделирования (по умолчанию: 1.0)

<a id="verify"></a>
## Проверка

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
## Устранение неполадок

- **Ошибки OpenGL**: Убедитесь, что установлены драйверы GPU. Для Докера, не комментируйте блок NVIDIA GPU в `docker-compose.yaml`.
- **Окно слишком большое**: Изображение Docker закрепляет окно на 1280x720. Для местных установки MuJoCo окно может быть полноэкранным по умолчанию.
- **Нет дисплея**: MuJoCo Нужен сервер X11 для окна рендеринга. Использование `headless:=true` в ксакро, если дисплей отсутствует.
<!-- /translated-content -->

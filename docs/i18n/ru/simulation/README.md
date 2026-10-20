<!-- translation-navigation -->
[English](../../en/simulation/README.md) · [Русский](README.md) · [Español](../../es/simulation/README.md) · [Français](../../fr/simulation/README.md) · [Deutsch](../../de/simulation/README.md) · [Português (Brasil)](../../pt-BR/simulation/README.md) · [简体中文](../../zh-CN/simulation/README.md) · [日本語](../../ja/simulation/README.md) · [हिन्दी](../../hi/simulation/README.md) · [العربية](../../ar/simulation/README.md)

[Английский оригинал](../../../../simulation/README.md)

[Русский](../README.md)

> Полный машинный перевод; носители языка его ещё не проверяли. Изображения, код, CAD и исходные PDF общие. При неоднозначности используйте английский оригинал.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="simulation"></a>
# Симуляция

ROS2 поддержка моделирования для SO-ARM-101 роботизированная рука с параллельным захватлением. Один параметризированный URDF управляет 5 двигателями физики через один файл запуска.

<a id="gazebo-ignition-fortress"></a>
## Gazebo (Огневая крепость)

![SO-ARM-101 в Gazebo](../../../../assets/images/simulation/gazebo/gazebo_pick_place.png)

*SO-ARM-101 выполнение подбора & место в Gazebo ⁇  рука выбирает предмет и ставит его на шельфе наверху.*

<a id="mujoco"></a>
## MuJoCo

![SO-ARM-101 в MuJoCo](../../../../assets/images/simulation/mujoco/mujoco_pick_place.png)

*Те же последовательности отбора и размещения MuJoCo с полной физической симуляцией.*

<a id="simulator-status"></a>
## Статус симулятора

| Симулятор | Статус | Докер | Управляющий контроллером |
|-----------|--------|--------|--------------------|
| [Gazebo (гз-сим)](gazebo/README.md) | Готов. | `docker compose run gazebo` | Встроенный в симулятор |
| [MuJoCo](mujoco/README.md) | Готов. | `docker compose run mujoco` | Внешние (`ros2_control_node`) |
| [Webots](webots/README.md) | Нестабильный | `docker compose run webots` | Встроенный в драйвер |
| [CoppeliaSim](coppeliasim/README.md) | Не проверено | N/A (внешняя симуляция) | Внешние (`ros2_control_node`) |
| [НВИДИЯ Isaac Да , да .](isaac_sim/README.md) | Не проверено | N/A (внешняя симуляция) | Внешние (`ros2_control_node`) |

<a id="architecture"></a>
## Архитектура

- **Единый УРФ** -- `so_arm_101_description/urdf/so_101.urdf.xacro` является единственным описанием робота для всех симуляторов
- **Параметризированные обратные списки** -- `sim_backend:=gazebo|mujoco|webots|coppeliasim|isaac` выбирает `ros2_control` плагин на xacro время расширения
- **Единые контроллеры** -- `config/controllers.yaml` Определяет те же соединения, интерфейсы и имена контроллеров на всех фонах
- **Один файл запуска** -- `launch/sim.launch.py` с `sim:=<backend>` аргумент

<a id="robot"></a>
### Робот

- **5-DOF рука**: вращение основы, удар плеча, локтей, удар запястья, рулетка
- **Параллельный захват**: 2 призма клеймовые суставы (левое зеркало клейма через правое окно) `<mimic>`)
- **Серво**: STS3215 (1.5Nm крутящий момент,5.2скорость радиации/с)

<a id="prerequisites"></a>
## Предусмотренные условия

**Выбор А: Docker (рекомендуется, нет) ROS2 установка необходима)**

- Рабочий стол Docker

**В варианте B: родной ROS2**

- ROS2 Смирение
- Специфические зависимости от симулятора (см. руководства по симулятору)

<a id="installation"></a>
## Установка

<a id="docker-recommended"></a>
### Докер (рекомендуется)

```bash
cd simulation/so_arm_101_description
docker compose run gazebo    # or mujoco, webots
```

<a id="native-ros2"></a>
### Родина ROS2

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
## Быстрый старт

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
## Командование роботом

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
## Докерные услуги

Все услуги определяются в `so_arm_101_description/docker-compose.yaml`:

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
## Стыковочные сетки

Упрощенные стыковые сетки для столкновения корпуса `so_arm_101_description/meshes/collision/`. Для регенерации:

```bash
pip install trimesh
python scripts/generate_collision_meshes.py
```

<a id="package-structure"></a>
## Структура пакета

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

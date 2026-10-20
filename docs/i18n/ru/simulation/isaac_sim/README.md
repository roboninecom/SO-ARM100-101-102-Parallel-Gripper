<!-- translation-navigation -->
[English](../../../en/simulation/isaac_sim/README.md) · [Русский](README.md) · [Español](../../../es/simulation/isaac_sim/README.md) · [Français](../../../fr/simulation/isaac_sim/README.md) · [Deutsch](../../../de/simulation/isaac_sim/README.md) · [Português (Brasil)](../../../pt-BR/simulation/isaac_sim/README.md) · [简体中文](../../../zh-CN/simulation/isaac_sim/README.md) · [日本語](../../../ja/simulation/isaac_sim/README.md) · [हिन्दी](../../../hi/simulation/isaac_sim/README.md) · [العربية](../../../ar/simulation/isaac_sim/README.md)

[Английский оригинал](../../../../../simulation/isaac_sim/README.md)

[Русский](../../README.md)

> Полный машинный перевод; носители языка его ещё не проверяли. Изображения, код, CAD и исходные PDF общие. При неоднозначности используйте английский оригинал.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="nvidia-isaac-sim"></a>
# НВИДИЯ Isaac Да , да .

**Статус: Не проверенный (внешний симулятор)**

Isaac Сим работает снаружи и общается с ROS2 через `topic_based_ros2_control`. Ты бежишь . Isaac Смотреть отдельно и запустить ROS2 стороной с `sim:=isaac`.

<a id="prerequisites"></a>
## Предусмотренные условия

- [НВИДИЯ Isaac Да , да .](https://developer.nvidia.com/isaac-sim) 4.0+ (требует GPU NVIDIA RTX)
- ROS2 Смирение
- Isaac Да , да . ROS2 мостик включен
- `topic_based_ros2_control`:
  ```bash
  sudo apt install ros-humble-topic-based-ros2-control
  ```

<a id="setup"></a>
## Настройка

<a id="1-import-urdf-into-isaac-sim"></a>
### 1. Импорт URDF в Isaac Да , да .

```bash
# Generate expanded URDF
source /opt/ros/humble/setup.bash
xacro so_arm_101_description/urdf/so_101.urdf.xacro sim_backend:=isaac > /tmp/so_101_isaac.urdf
```

В Isaac Да , конечно .
1. **Isaac Утилиты > Импортер URDF**
2. **Файл ввода**Выберите: `/tmp/so_101_isaac.urdf`
3. **Место импорта**: `/World/so_101`
4. **Тип совместного привода**Положение:
5. **Исправление базовой ссылки**: проверено
6. Нажмите **Импорт**
7. Добавьте наземный самолет: **Создание > Физика > Земляная плоскость**
8. За исключением стадии USD (необязательно)

<a id="2-configure-ros2-bridge-omnigraph"></a>
### 2. Конфигурация ROS2 Мост (OmniGraph)

В. `topic_based_ros2_control` Plugin общается через эти темы:

| Тема | Тип | Направление |
|-------|------|-----------|
| `/joint_states` | `sensor_msgs/JointState` | Isaac - Да, да. ROS2 |
| `/joint_commands` | `std_msgs/Float64MultiArray` | ROS2 -> Isaac Да , да . |

<a id="omnigraph-setup"></a>
#### Настройка OmniGraph

1. Открыто **Окно > Визуальный сценарий > График действий**
2. Создать новый график действий
3. Добавьте эти узлы:
   - **На "Плей-блок"** (источник событий)
   - **Isaac Время симуляции**
   - **ROS2 Публикация Совместного государства** -- подключить к `/World/so_101`
   - **ROS2 Подписание Совместного государства** -- для приема команд
   - **Isaac Контролер соединения** -- применяет команды к суставам

4. Соедините график:
   ```
   On Playback Tick -> Read Sim Time -> Publish Joint State
   On Playback Tick -> Subscribe Joint State -> Articulation Controller
   ```

5. Конфигурация **Публикация Совместного государства** узел:
   - `targetPrim`: `/World/so_101`
   - `topicName`: `/joint_states`

6. Конфигурация **Контролер соединения** узел:
   - `targetPrim`: `/World/so_101`
   - `jointNames`: все 7 совместных названий из `config/controllers.yaml`

<a id="alternative-isaac_ros2_control"></a>
#### Альтернатива: isaac_ros2_control

Если `isaac_ros2_control` доступна для вашего Isaac Версия Sim:

```bash
sudo apt install ros-humble-isaac-ros2-control
```

Это заменяет настройку OmniGraph прямым `ros2_control` аппаратный интерфейс.

<a id="3-launch"></a>
### 3. Запуск

```bash
# Terminal 1: Start Isaac Sim and press Play

# Terminal 2: Launch ROS2 side
ros2 launch so_arm_101_description sim.launch.py sim:=isaac
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

- **Неудачи в импорте URDF**: Убедитесь, что все маршруты сетки абсолютны. Создать URDF с помощью `xacro` Во-первых - не импортируйте `.xacro` Документ прямо.
- **Совместные государства**: Проверьте , что OmniGraph подключен и Isaac Сим в режиме игры.
- **Физическая нестабильность**: В свойствах физической сцены устанавливают тип решителя на TGS и увеличивают количество повторений.
- **ROS2 мост не найден**: Включить расширение в **Окно > Расширения > ROS2 Мост**.
<!-- /translated-content -->

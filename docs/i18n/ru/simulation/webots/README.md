<!-- translation-navigation -->
[English](../../../en/simulation/webots/README.md) · [Русский](README.md) · [Español](../../../es/simulation/webots/README.md) · [Français](../../../fr/simulation/webots/README.md) · [Deutsch](../../../de/simulation/webots/README.md) · [Português (Brasil)](../../../pt-BR/simulation/webots/README.md) · [简体中文](../../../zh-CN/simulation/webots/README.md) · [日本語](../../../ja/simulation/webots/README.md) · [हिन्दी](../../../hi/simulation/webots/README.md) · [العربية](../../../ar/simulation/webots/README.md)

[Английский оригинал](../../../../../simulation/webots/README.md)

[Русский](../../README.md)

> Полный машинный перевод; носители языка его ещё не проверяли. Изображения, код, CAD и исходные PDF общие. При неоднозначности используйте английский оригинал.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="webots"></a>
# Webots

> **Статус: неустойчивый** -- Webots Интеграционные работы, но имеют известные проблемы с производительностью и рендерингом. Рекомендуется использовать только докер.

Webots симуляции с использованием `webots_ros2_control`. В. Webots драйвер встраивает управляющего контроллером.

<a id="prerequisites"></a>
## Предусмотренные условия

**Докер (рекомендуется):**
- Рабочий стол Docker

**Родина ROS2:**
- ROS2 Смирение
- [Webots](https://cyberbotics.com/) R2023b+
- `ros-humble-webots-ros2`
- `urdf2webots` упаковка

<a id="launch"></a>
## Запуск

<a id="docker"></a>
### Докер

```bash
cd simulation/so_arm_101_description
docker compose run webots
```

> **Примечание**В: Webots Служба докеров не имеет установки объемов. Всемирный файл генерируется внутри изображения во время создания. Если вы изменяете URDF, вы должны восстановить: `docker compose build webots`.

<a id="native-ros2"></a>
### Родина ROS2

```bash
pip install urdf2webots

# Generate the Webots world file
python scripts/setup_webots.py

# Generate pre-expanded URDF for the Webots driver
xacro urdf/so_101.urdf.xacro sim_backend:=webots > urdf/so_101_webots.urdf

# Launch
ros2 launch so_arm_101_description sim.launch.py sim:=webots
```

<a id="how-it-works"></a>
## Как это работает

1. `scripts/setup_webots.py` преобразует URDF в Webots Роботный узел через `urdf2webots` и создает `worlds/webots_sim.wbt`
2. В. `WebotsLauncher` открывает мировой файл в Webots
3. `WebotsController` подключается к роботу через IPC и запускает `ros2_control` водитель
4. Контроллер `<extern>` Тег в файле мира позволяет `webots_ros2_driver` взять на себя
5. Уже расширенный URDF (`so_101_webots.urdf`) необходима, поскольку `WebotsController` требует пути файла, а не XML встроенного

<a id="world-settings"></a>
### События в мире

- `basicTimeStep`: 16 мс (уменьшенный от дефолта для физической стабильности)
- `maxContactJoints`: 4 (ограничает воздействие столкновений с детальными сетками)

<a id="known-issues"></a>
## Известные проблемы

- **Медленная загрузка на X11**: Загрузка требует около 120 секунд, когда рендер передается через X11. Время выхода контроллера на порожье установлено на 180 секунд, чтобы удовлетворить это.
- **Рендерингование проводных систем на Windows**: VcXsrv предоставляет только OpenGL 1.4, но Webots требует OpenGL 3.3. Симуляция работает, но передается в режиме кадра.
- **обнаружение WSL2**: Docker на WSL2 унаследует название ядра WSL, что вызывает `webots_ros2_driver` искать `webots.exe`. Пачты докер-файла `is_wsl()` чтобы всегда возвращаться `False`.
- **Предупреждения по физике**: Из-за высокополированных столкновений могут появиться предупреждения: "Ваш мир может быть слишком сложным".

<a id="troubleshooting"></a>
## Устранение неполадок

- **`WEBOTS_HOME` не найдено**Убедитесь: `WEBOTS_HOME=/usr/local/webots` Установлено. Изображение Докера устанавливает это автоматически.
- **Время действия контроллера**Если контроллеры не активируются, увеличивайте время `launch/sim.launch.py` (в настоящее время 180).
- **Нет дисплея**: Webots нужны X11. В Windows используйте VcXsrv с `-ac -wgl` флаги.
<!-- /translated-content -->

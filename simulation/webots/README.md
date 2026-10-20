# Webots

<!-- documentation-languages -->
[English](../../docs/i18n/en/simulation/webots/README.md) · [Русский](../../docs/i18n/ru/simulation/webots/README.md) · [Español](../../docs/i18n/es/simulation/webots/README.md) · [Français](../../docs/i18n/fr/simulation/webots/README.md) · [Deutsch](../../docs/i18n/de/simulation/webots/README.md) · [Português (Brasil)](../../docs/i18n/pt-BR/simulation/webots/README.md) · [简体中文](../../docs/i18n/zh-CN/simulation/webots/README.md) · [日本語](../../docs/i18n/ja/simulation/webots/README.md) · [हिन्दी](../../docs/i18n/hi/simulation/webots/README.md) · [العربية](../../docs/i18n/ar/simulation/webots/README.md)
<!-- /documentation-languages -->

> **Status: Unstable** -- Webots integration works but has known performance and rendering issues. Docker-only usage is recommended.

Webots simulation using `webots_ros2_control`. The Webots driver embeds the controller manager.

## Prerequisites

**Docker (recommended):**
- Docker Desktop

**Native ROS2:**
- ROS2 Humble
- [Webots](https://cyberbotics.com/) R2023b+
- `ros-humble-webots-ros2`
- `urdf2webots` pip package

## Launch

### Docker

```bash
cd simulation/so_arm_101_description
docker compose run webots
```

> **Note**: The Webots Docker service has no volume mount. The world file is generated inside the image at build time. If you modify the URDF, you must rebuild: `docker compose build webots`.

### Native ROS2

```bash
pip install urdf2webots

# Generate the Webots world file
python scripts/setup_webots.py

# Generate pre-expanded URDF for the Webots driver
xacro urdf/so_101.urdf.xacro sim_backend:=webots > urdf/so_101_webots.urdf

# Launch
ros2 launch so_arm_101_description sim.launch.py sim:=webots
```

## How It Works

1. `scripts/setup_webots.py` converts the URDF to a Webots Robot node via `urdf2webots` and generates `worlds/webots_sim.wbt`
2. The `WebotsLauncher` opens the world file in Webots
3. `WebotsController` connects to the robot via IPC and starts the `ros2_control` driver
4. The controller `<extern>` tag in the world file allows `webots_ros2_driver` to take over
5. A pre-expanded URDF (`so_101_webots.urdf`) is needed because `WebotsController` requires a file path, not inline XML

### World Settings

- `basicTimeStep`: 16ms (reduced from default for physics stability)
- `maxContactJoints`: 4 (limits collision overhead from detailed meshes)

## Known Issues

- **Slow world loading over X11**: The world takes ~120s to load when rendering is forwarded via X11. Controller spawner timeout is set to 180s to accommodate this.
- **Wireframe rendering on Windows**: VcXsrv provides only OpenGL 1.4, but Webots requires OpenGL 3.3. The simulation runs but renders in wireframe mode.
- **WSL2 detection**: Docker on WSL2 inherits the WSL kernel name, causing `webots_ros2_driver` to look for `webots.exe`. The Dockerfile patches `is_wsl()` to always return `False`.
- **Physics warnings**: "Your world may be too complex" warnings may appear due to high-poly collision meshes.

## Troubleshooting

- **`WEBOTS_HOME` not found**: Ensure `WEBOTS_HOME=/usr/local/webots` is set. The Docker image sets this automatically.
- **Controller timeout**: If controllers fail to activate, increase the timeout in `launch/sim.launch.py` (currently 180s).
- **No display**: Webots needs X11. On Windows, use VcXsrv with `-ac -wgl` flags.

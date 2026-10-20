<!-- translation-navigation -->
[English](../../en/simulation/README.md) · [Русский](../../ru/simulation/README.md) · [Español](README.md) · [Français](../../fr/simulation/README.md) · [Deutsch](../../de/simulation/README.md) · [Português (Brasil)](../../pt-BR/simulation/README.md) · [简体中文](../../zh-CN/simulation/README.md) · [日本語](../../ja/simulation/README.md) · [हिन्दी](../../hi/simulation/README.md) · [العربية](../../ar/simulation/README.md)

[Original en inglés](../../../../simulation/README.md)

[Español](../README.md)

> Traducción automática completa, aún sin revisión de hablantes nativos. Las imágenes, el código, CAD y PDF originales son compartidos. En caso de duda, consulte el original en inglés.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="simulation"></a>
# Simulación

ROS2 apoyo de simulación para el SO-ARM-101 brazo robótico con agarre paralelo. Un único URDF parametrizado impulsa 5 motores de física a través de un archivo de lanzamiento.

<a id="gazebo-ignition-fortress"></a>
## Gazebo (Fortaleza de la Ignición)

![SO-ARM-101 en el Gazebo](../../../../assets/images/simulation/gazebo/gazebo_pick_place.png)

*SO-ARM-101 ejecutando el pick & place en Gazebo ⁇  el brazo toma un objeto y lo coloca en una estantería arriba.*

<a id="mujoco"></a>
## MuJoCo

![SO-ARM-101 en el MuJoCo](../../../../assets/images/simulation/mujoco/mujoco_pick_place.png)

*La misma secuencia de pick & place se ejecuta en MuJoCo con una simulación física completa.*

<a id="simulator-status"></a>
## Estatus del simulador

| Simulador | El estado | - ¿Qué es eso? | Administrador del controlador |
|-----------|--------|--------|--------------------|
| [Gazebo ¿Qué es eso ?](gazebo/README.md) | Estoy listo. | `docker compose run gazebo` | Incluido en el simulador |
| [MuJoCo](mujoco/README.md) | Estoy listo. | `docker compose run mujoco` | Exteriores (`ros2_control_node`) |
| [Webots](webots/README.md) | No está estable | `docker compose run webots` | Incluido en el controlador |
| [CoppeliaSim](coppeliasim/README.md) | No probado | N/A (simulación externa) | Exteriores (`ros2_control_node`) |
| [NVIDIA Isaac Sí](isaac_sim/README.md) | No probado | N/A (simulación externa) | Exteriores (`ros2_control_node`) |

<a id="architecture"></a>
## Arquitectura

- **Único URDF** -- `so_arm_101_description/urdf/so_101.urdf.xacro` es la única descripción del robot para todos los simuladores
- **Los retrospectivos parámetrizados** -- `sim_backend:=gazebo|mujoco|webots|coppeliasim|isaac` selecciona el `ros2_control` Plugin en el tiempo de expansión xacro
- **Los controladores unificados** -- `config/controllers.yaml` define las mismas articulaciones, interfaces y nombres de controladores en todos los fondos
- **Un archivo de lanzamiento** -- `launch/sim.launch.py` con `sim:=<backend>` El argumento

<a id="robot"></a>
### Robótico

- **Armo de 5 DOF**: rotación de la base, lanzamiento del hombro, codo, lanzamiento de la muñeca, movimiento de la muñeca
- **Pinza paralela**: 2 articulaciones prismáticas (espejos de sujeción izquierda a la derecha vía `<mimic>`)
- **Servicios**: STS3215 (1.5Nm par,5.2velocidad rad/s)

<a id="prerequisites"></a>
## Pré-requisitos

**Opción A: Docker (recomendado, no) ROS2 instalación necesaria)**

- Escritorio de Docker

**Opción B: nativo ROS2**

- ROS2 Humilde
- Las dependencias específicas del simulador (véase las guías por simulador)

<a id="installation"></a>
## Instalación

<a id="docker-recommended"></a>
### Docker (recomendado)

```bash
cd simulation/so_arm_101_description
docker compose run gazebo    # or mujoco, webots
```

<a id="native-ros2"></a>
### Nativo ROS2

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
## Un comienzo rápido

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
## Comandando al robot

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
## Servicios de acoplamiento

Todos los servicios se definen en: `so_arm_101_description/docker-compose.yaml`:

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
## Las redes de colisión

Las redes de colisión del casco convexo simplificadas se proporcionan en `so_arm_101_description/meshes/collision/`. Para regenerar:

```bash
pip install trimesh
python scripts/generate_collision_meshes.py
```

<a id="package-structure"></a>
## Estructura del paquete

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

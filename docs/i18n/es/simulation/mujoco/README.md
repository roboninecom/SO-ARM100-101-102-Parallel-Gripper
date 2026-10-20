<!-- translation-navigation -->
[English](../../../en/simulation/mujoco/README.md) · [Русский](../../../ru/simulation/mujoco/README.md) · [Español](README.md) · [Français](../../../fr/simulation/mujoco/README.md) · [Deutsch](../../../de/simulation/mujoco/README.md) · [Português (Brasil)](../../../pt-BR/simulation/mujoco/README.md) · [简体中文](../../../zh-CN/simulation/mujoco/README.md) · [日本語](../../../ja/simulation/mujoco/README.md) · [हिन्दी](../../../hi/simulation/mujoco/README.md) · [العربية](../../../ar/simulation/mujoco/README.md)

[Original en inglés](../../../../../simulation/mujoco/README.md)

[Español](../../README.md)

> Traducción automática completa, aún sin revisión de hablantes nativos. Las imágenes, el código, CAD y PDF originales son compartidos. En caso de duda, consulte el original en inglés.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="mujoco"></a>
# MuJoCo

**Estatus: listo**

MuJoCo simulación utilizando `mujoco_ros2_control` (forca de los controles de rosas). MuJoCo converte el URDF en MJCF internamente y ejecuta física + renderización en la `ros2_control_node` el proceso.

<a id="prerequisites"></a>
## Pré-requisitos

**Docker (recomendado):**
- Escritorio de Docker

**Nativo ROS2:**
- ROS2 Humilde
- `mujoco_ros2_control` (construido a partir de la fuente - vea abajo)
- `mujoco` paquete de pip

<a id="launch"></a>
## Lanzamiento

<a id="docker"></a>
### - ¿Qué es eso?

```bash
cd simulation/so_arm_101_description
docker compose run mujoco
```

La imagen de Docker se construye `mujoco_ros2_control` de la fuente automáticamente.

<a id="native-ros2"></a>
### Nativo ROS2

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
## Cómo funciona

1. El complemento `mujoco_ros2_control/MujocoSystemInterface` se selecciona a través de `sim_backend:=mujoco`
2. Un nodo personalizado (`publish_mujoco_description`) publica la URDF en el `/mujoco_robot_description`
3. El MuJoCo El plugin lee el URDF, lo convierte en MJCF y inicia la simulación
4. El `<mujoco><compiler meshdir=.../>` la etiqueta en el URDF dice MuJoCo Dónde encontrar redes de colisión
5. Se abre una ventana de renderización que muestra la simulación (1280x720, corregida por defecto en pantalla completa)

<a id="key-parameters-in-so_101ros2_controlxacro"></a>
### Parámetros clave (en `so_101.ros2_control.xacro`)

- `headless`Se fija en: `true` para el modo sin cabeza (sin ventana de renderización)
- `sim_speed_factor`: Multiplicador de velocidad de simulación (por defecto: 1.0)

<a id="verify"></a>
## Verificar

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
## Solución de problemas

- **Errores en OpenGL**: Asegúrese de que los controladores de GPU estén instalados. Para Docker, descomentar el bloqueo de la GPU NVIDIA en `docker-compose.yaml`.
- **Ventana demasiado grande**: La imagen de Docker corrige la ventana a 1280x720. Para las instalaciones nativas, el MuJoCo la ventana puede estar completa por defecto.
- **No hay pantalla**: MuJoCo necesita un servidor X11 para la ventana de renderización. Utilización `headless:=true` en el xacro si no hay pantalla disponible.
<!-- /translated-content -->

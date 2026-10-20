<!-- translation-navigation -->
[English](../../../en/simulation/gazebo/README.md) · [Русский](../../../ru/simulation/gazebo/README.md) · [Español](README.md) · [Français](../../../fr/simulation/gazebo/README.md) · [Deutsch](../../../de/simulation/gazebo/README.md) · [Português (Brasil)](../../../pt-BR/simulation/gazebo/README.md) · [简体中文](../../../zh-CN/simulation/gazebo/README.md) · [日本語](../../../ja/simulation/gazebo/README.md) · [हिन्दी](../../../hi/simulation/gazebo/README.md) · [العربية](../../../ar/simulation/gazebo/README.md)

[Original en inglés](../../../../../simulation/gazebo/README.md)

[Español](../../README.md)

> Traducción automática completa, aún sin revisión de hablantes nativos. Las imágenes, el código, CAD y PDF originales son compartidos. En caso de duda, consulte el original en inglés.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="gazebo-gz-sim"></a>
# Gazebo ¿Qué es eso ?

**Estatus: listo**

Gazebo simulación utilizando `gz_ros2_control` Plug-in. El gerente del controlador corre dentro de la Gazebo el proceso.

<a id="prerequisites"></a>
## Pré-requisitos

**Docker (recomendado):**
- Escritorio de Docker

**Nativo ROS2:**
- ROS2 Humilde
- `ros-humble-gz-ros2-control`
- `ros-humble-ros-gz-sim`
- `ros-humble-ros-gz-bridge`

<a id="launch"></a>
## Lanzamiento

<a id="docker"></a>
### - ¿Qué es eso?

```bash
cd simulation/so_arm_101_description
docker compose run gazebo
```

Para el NVIDIA GPU, sin comentarios `deploy:` bloqueo en `docker-compose.yaml`:

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
### Nativo ROS2

```bash
ros2 launch so_arm_101_description sim.launch.py sim:=gazebo
```

<a id="how-it-works"></a>
## Cómo funciona

1. El Gazebo Plugin `gz_ros2_control/GazeboSimSystem` se seleccionará a través de la `sim_backend:=gazebo` Argumento de xacro
2. Gazebo incrusta el administrador del controlador - no separado `ros2_control_node` necesario
3. El robot es generado en `worlds/empty.sdf` a través de `ros_gz_sim create`
4. Los reproductores de controladores comienzan después `robot_state_publisher` está corriendo

<a id="world-file"></a>
### Archivos mundiales

`worlds/empty.sdf` se establece:
- El motor de física ODE (fase en tiempo)0.004s / 250Hz)
- Planas de tierra (100x100m)
- Iluminación solar direccional

<a id="verify"></a>
## Verificar

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
## Solución de problemas

- **Las redes no encontradas**Asegurar: `GZ_SIM_RESOURCE_PATH` Incluye el directorio de las acciones del paquete. El punto de entrada del Docker establece esto automáticamente.
- **No hay pantalla**: Gazebo Necesita un servidor X11. En Windows, utilice VcXsrv con `-ac` bandera. En macOS, utiliza XQuartz.
- **Rendición lenta**: No comentar el paso de la GPU a través del bloque en `docker-compose.yaml` si tienes una GPU NVIDIA.
<!-- /translated-content -->

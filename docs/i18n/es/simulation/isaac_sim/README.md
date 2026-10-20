<!-- translation-navigation -->
[English](../../../en/simulation/isaac_sim/README.md) · [Русский](../../../ru/simulation/isaac_sim/README.md) · [Español](README.md) · [Français](../../../fr/simulation/isaac_sim/README.md) · [Deutsch](../../../de/simulation/isaac_sim/README.md) · [Português (Brasil)](../../../pt-BR/simulation/isaac_sim/README.md) · [简体中文](../../../zh-CN/simulation/isaac_sim/README.md) · [日本語](../../../ja/simulation/isaac_sim/README.md) · [हिन्दी](../../../hi/simulation/isaac_sim/README.md) · [العربية](../../../ar/simulation/isaac_sim/README.md)

[Original en inglés](../../../../../simulation/isaac_sim/README.md)

[Español](../../README.md)

> Traducción automática completa, aún sin revisión de hablantes nativos. Las imágenes, el código, CAD y PDF originales son compartidos. En caso de duda, consulte el original en inglés.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="nvidia-isaac-sim"></a>
# NVIDIA Isaac Sí

**Estado: No probado (simulador externo)**

Isaac El Sim se ejecuta externamente y comunica con ROS2 a través de `topic_based_ros2_control`. Tú huyes . Isaac Sim separadamente y lanzar el ROS2 lado con `sim:=isaac`.

<a id="prerequisites"></a>
## Pré-requisitos

- [NVIDIA Isaac Sí](https://developer.nvidia.com/isaac-sim) 4.0+ (requiere GPU NVIDIA RTX)
- ROS2 Humilde
- Isaac Sí ROS2 puente habilitado
- `topic_based_ros2_control`:
  ```bash
  sudo apt install ros-humble-topic-based-ros2-control
  ```

<a id="setup"></a>
## Configuración

<a id="1-import-urdf-into-isaac-sim"></a>
### 1. Importar URDF en Isaac Sí

```bash
# Generate expanded URDF
source /opt/ros/humble/setup.bash
xacro so_arm_101_description/urdf/so_101.urdf.xacro sim_backend:=isaac > /tmp/so_101_isaac.urdf
```

En el Isaac Sí , estoy bien .
1. **Isaac Utils > Importador de la URDF**
2. **Archivos de entrada**: seleccionar `/tmp/so_101_isaac.urdf`
3. **Lugar de importación**: `/World/so_101`
4. **Tipo de accionamiento conjunto**Posición:
5. **Corrección de la conexión base**: comprobado
6. Haga clic **Importar**
7. Añadir un avión de tierra: **Crear > Física > Planas de tierra**
8. Salvo como etapa USD (opcional)

<a id="2-configure-ros2-bridge-omnigraph"></a>
### 2. Configuración ROS2 Puente (Omnigrafo)

El `topic_based_ros2_control` el plugin se comunica a través de estos temas:

| Título | Tipo | Dirección |
|-------|------|-----------|
| `/joint_states` | `sensor_msgs/JointState` | Isaac Sí -> ROS2 |
| `/joint_commands` | `std_msgs/Float64MultiArray` | ROS2 -> Isaac Sí |

<a id="omnigraph-setup"></a>
#### Configuración de OmniGraph

1. Abierto **Ventana > Escrito visual > Gráfico de acción**
2. Crear un nuevo gráfico de acción
3. Añadir estos nodos:
   - **En la etiqueta de reproducción** (fuente del evento)
   - **Isaac Leer el tiempo de la simulación**
   - **ROS2 Publicación del Estado conjunto** -- conectarse a `/World/so_101`
   - **ROS2 Subscribirse al Estado común** -- para recibir órdenes
   - **Isaac Controlador de articulación** -- aplica comandos a las articulaciones

4. Conecta el gráfico:
   ```
   On Playback Tick -> Read Sim Time -> Publish Joint State
   On Playback Tick -> Subscribe Joint State -> Articulation Controller
   ```

5. Configuración **Publicación del Estado conjunto** el nodo:
   - `targetPrim`: `/World/so_101`
   - `topicName`: `/joint_states`

6. Configuración **Controlador de articulación** el nodo:
   - `targetPrim`: `/World/so_101`
   - `jointNames`: los 7 nombres conjuntos de `config/controllers.yaml`

<a id="alternative-isaac_ros2_control"></a>
#### Alternativa: isaac_ros2_control

Si `isaac_ros2_control` está disponible para su Isaac La versión de Sim:

```bash
sudo apt install ros-humble-isaac-ros2-control
```

Esto reemplaza la configuración de OmniGraph con una `ros2_control` Interfaz de hardware.

<a id="3-launch"></a>
### 3. Lanzamiento

```bash
# Terminal 1: Start Isaac Sim and press Play

# Terminal 2: Launch ROS2 side
ros2 launch so_arm_101_description sim.launch.py sim:=isaac
```

<a id="verify"></a>
## Verificar

```bash
ros2 topic echo /joint_states --once

ros2 topic pub /arm_controller/joint_trajectory trajectory_msgs/msg/JointTrajectory "{
  joint_names: ['base_link_to_link1'],
  points: [{positions: [0.5], time_from_start: {sec: 2}}]
}" --once
```

<a id="troubleshooting"></a>
## Solución de problemas

- **Fallas en la importación del URDF**: Asegúrese de que todos los caminos de malla sean absolutos. Generar el URDF con `xacro` en primer lugar - no importar el `.xacro` archivo directamente.
- **No hay estados comunes**: Verifique si el OmniGraph está conectado y Isaac Sim está en modo juego.
- **Inestabilidad física**: En las propiedades de escena física, establece el tipo de solvente en TGS y aumenta el recuento de iteraciones.
- **ROS2 puente no encontrado**: Habilitar la extensión en **Ventana > Extensiones > ROS2 Puente**.
<!-- /translated-content -->

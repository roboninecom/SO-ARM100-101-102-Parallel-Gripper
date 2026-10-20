<!-- translation-navigation -->
[English](../../../en/simulation/webots/README.md) · [Русский](../../../ru/simulation/webots/README.md) · [Español](README.md) · [Français](../../../fr/simulation/webots/README.md) · [Deutsch](../../../de/simulation/webots/README.md) · [Português (Brasil)](../../../pt-BR/simulation/webots/README.md) · [简体中文](../../../zh-CN/simulation/webots/README.md) · [日本語](../../../ja/simulation/webots/README.md) · [हिन्दी](../../../hi/simulation/webots/README.md) · [العربية](../../../ar/simulation/webots/README.md)

[Original en inglés](../../../../../simulation/webots/README.md)

[Español](../../README.md)

> Traducción automática completa, aún sin revisión de hablantes nativos. Las imágenes, el código, CAD y PDF originales son compartidos. En caso de duda, consulte el original en inglés.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="webots"></a>
# Webots

> **Estatus: Inestable** -- Webots la integración de los trabajos, pero tiene conocidos problemas de rendimiento y renderización. Se recomienda el uso solo de Docker.

Webots simulación utilizando `webots_ros2_control`. El Webots El conductor incorpora el controlador de control.

<a id="prerequisites"></a>
## Pré-requisitos

**Docker (recomendado):**
- Escritorio de Docker

**Nativo ROS2:**
- ROS2 Humilde
- [Webots](https://cyberbotics.com/) R2023b+
- `ros-humble-webots-ros2`
- `urdf2webots` paquete de pip

<a id="launch"></a>
## Lanzamiento

<a id="docker"></a>
### - ¿Qué es eso?

```bash
cd simulation/so_arm_101_description
docker compose run webots
```

> **Nota**Las siguientes: Webots El servicio de Docker no tiene montaje de volumen. El archivo del mundo se genera dentro de la imagen en el momento de la creación. Si modifica el URDF, debe reconstruir: `docker compose build webots`.

<a id="native-ros2"></a>
### Nativo ROS2

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
## Cómo funciona

1. `scripts/setup_webots.py` convertirá el URDF en un Webots Nodo de robot a través `urdf2webots` y genera `worlds/webots_sim.wbt`
2. El `WebotsLauncher` abre el archivo del mundo en Webots
3. `WebotsController` se conecta al robot a través del IPC y inicia el `ros2_control` conductor
4. El controlador `<extern>` etiqueta en el archivo del mundo permite `webots_ros2_driver` para tomar el control
5. Una URDF preampliada (`so_101_webots.urdf`) es necesario porque `WebotsController` requiere un camino de archivo, no XML en línea

<a id="world-settings"></a>
### Configuraciones del mundo

- `basicTimeStep`: 16 ms (reducido del estándar para la estabilidad física)
- `maxContactJoints`: 4 (limite las tasas de colisión por encima de las redes detalladas)

<a id="known-issues"></a>
## Cuestiones conocidas

- **Lento mundo de carga sobre X11**: El mundo toma ~ 120s para cargarse cuando el renderizado se reenvía a través de X11. El tiempo de espera del controller es de 180s para acomodar esto.
- **Renderización de las cuadradas en Windows**: VcXsrv sólo proporciona OpenGL 1.4, pero Webots Requiere OpenGL 3.3. La simulación se ejecuta, pero se renderiza en modo wireframe.
- **Detección de WSL2**: Docker en WSL2 hereda el nombre del núcleo de WSL, causando `webots_ros2_driver` para buscar `webots.exe`. Los parches del archivo Docker `is_wsl()` para volver siempre `False`.
- **Advertencias de la física**: Las advertencias "Tu mundo puede ser demasiado complejo" pueden aparecer debido a las redes de colisión de alto pólio.

<a id="troubleshooting"></a>
## Solución de problemas

- **`WEBOTS_HOME` no se encontró**Asegurar: `WEBOTS_HOME=/usr/local/webots` Está listo. La imagen de Docker establece esto automáticamente.
- **Tiempo de espera del controlador**: Si los controladores no se activan, aumentar el tiempo de espera en `launch/sim.launch.py` (actualmente 180 años).
- **No hay pantalla**: Webots Necesita X11. En Windows, utilice VcXsrv con `-ac -wgl` las banderas.
<!-- /translated-content -->

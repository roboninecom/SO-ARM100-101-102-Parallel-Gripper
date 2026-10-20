<!-- translation-navigation -->
[English](../../../en/simulation/webots/README.md) · [Русский](../../../ru/simulation/webots/README.md) · [Español](../../../es/simulation/webots/README.md) · [Français](../../../fr/simulation/webots/README.md) · [Deutsch](README.md) · [Português (Brasil)](../../../pt-BR/simulation/webots/README.md) · [简体中文](../../../zh-CN/simulation/webots/README.md) · [日本語](../../../ja/simulation/webots/README.md) · [हिन्दी](../../../hi/simulation/webots/README.md) · [العربية](../../../ar/simulation/webots/README.md)

[Englische Quelle](../../../../../simulation/webots/README.md)

[Deutsch](../../README.md)

> Vollständige maschinelle Übersetzung, noch nicht von Muttersprachlern geprüft. Bilder, Code, CAD und Original-PDFs werden gemeinsam genutzt. Im Zweifel gilt die englische Quelle.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="webots"></a>
# Webots

> **Status: Unsicher** -- Webots In diesem Zusammenhang ist die Kommission der Auffassung, daß die Es wird empfohlen, nur Docker zu verwenden.

Webots Simulation mit `webots_ros2_control`. Die Webots der Fahrer den Controller-Manager einbricht.

<a id="prerequisites"></a>
## Voraussetzungen

**Docker (empfohlen):**
- Docker-Desktop

**Einheimische ROS2:**
- ROS2 Demütig
- [Webots](https://cyberbotics.com/) R2023b+
- `ros-humble-webots-ros2`
- `urdf2webots` Pip-Package

<a id="launch"></a>
## Start

<a id="docker"></a>
### Docker

```bash
cd simulation/so_arm_101_description
docker compose run webots
```

> **Anmerkung**Die: Webots Der Docker-Service hat keine Lautstärke. Die Weltdatei wird zur Erstellung des Bildes in der Bilderzeit generiert. Wenn Sie den URDF ändern, müssen Sie: `docker compose build webots`.

<a id="native-ros2"></a>
### Einheimische ROS2

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
## Wie funktioniert es?

1. `scripts/setup_webots.py` umwandelt den URDF in eine Webots Roboterknoten über `urdf2webots` und erzeugt `worlds/webots_sim.wbt`
2. Die `WebotsLauncher` öffnet die Weltdatei in Webots
3. `WebotsController` Sie verbindet sich mit dem Roboter über IPC und startet die `ros2_control` Fahrer
4. Der Controller `<extern>` Tag in der Welt-Datei erlaubt `webots_ros2_driver` zu übernehmen
5. Eine vorgeweiterte URDF (`so_101_webots.urdf`) erforderlich ist, weil `WebotsController` erfordert einen Dateipfad, nicht inline XML

<a id="world-settings"></a>
### Weltverhältnisse

- `basicTimeStep`: 16 ms (abgeschnitten von der Standardzahl für die physikalische Stabilität)
- `maxContactJoints`: 4 (Beschränkung der Kollisionshöhe durch detaillierte Maschen)

<a id="known-issues"></a>
## Bekannte Themen

- **Langsames Weltladen über X11**Die Welt braucht ~ 120 Sekunden, um zu laden, wenn das Rendering über X11 weitergeleitet wird. Die Zeitdurchlaufzeit des Controllers ist auf 180 Sekunden gesetzt, um dies zu ermöglichen.
- **Wireframe-Rendering auf Windows**: VcXsrv bietet nur OpenGL 1.4, aber Webots erfordert OpenGL 3.3. Die Simulation läuft, aber erläutert sich im Wireframe-Modus.
- **WSL2-Detektion**: Docker auf WSL2 erbt den Namen des WSL-Kernels, wodurch `webots_ros2_driver` zu suchen `webots.exe`. Die Dockerfile Patches `is_wsl()` immer wieder zurückzukehren `False`.
- **Physik Warnungen**: "Eure Welt ist möglicherweise zu komplex" - Warnungen können aufgrund von hochpoly-Kollisionsmassen angezeigt werden.

<a id="troubleshooting"></a>
## Fehlerbehebung

- **`WEBOTS_HOME` nicht gefunden**: Sicherstellen `WEBOTS_HOME=/usr/local/webots` ist eingestellt. Das Docker-Bild setzt das automatisch ein.
- **Controller Timeout**Wenn die Controller nicht aktiviert werden, erhöhen `launch/sim.launch.py` (derzeit 180er Jahre).
- **Keine Anzeige**: Webots X11 ist nötig. Auf Windows verwenden Sie VcXsrv mit `-ac -wgl` Flags.
<!-- /translated-content -->

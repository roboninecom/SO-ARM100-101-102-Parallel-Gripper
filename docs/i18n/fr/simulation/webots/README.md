<!-- translation-navigation -->
[English](../../../en/simulation/webots/README.md) · [Русский](../../../ru/simulation/webots/README.md) · [Español](../../../es/simulation/webots/README.md) · [Français](README.md) · [Deutsch](../../../de/simulation/webots/README.md) · [Português (Brasil)](../../../pt-BR/simulation/webots/README.md) · [简体中文](../../../zh-CN/simulation/webots/README.md) · [日本語](../../../ja/simulation/webots/README.md) · [हिन्दी](../../../hi/simulation/webots/README.md) · [العربية](../../../ar/simulation/webots/README.md)

[Source anglaise](../../../../../simulation/webots/README.md)

[Français](../../README.md)

> Traduction automatique intégrale, pas encore relue par des locuteurs natifs. Images, code, CAO et PDF originaux sont partagés. En cas de doute, consultez la source anglaise.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="webots"></a>
# Webots

> **Statut: instable** -- Webots Les travaux d'intégration, mais avec des problèmes de performance et de rendu connus. Il est recommandé d'utiliser le docker uniquement.

Webots simulation en utilisant `webots_ros2_control`. Les Webots le conducteur intègre le gestionnaire du contrôleur.

<a id="prerequisites"></a>
## Préalabilités

**Docker (recommandé):**
- Tableau de bureau Docker

**Native ROS2:**
- ROS2 Humble
- [Webots](https://cyberbotics.com/) R2023b+
- `ros-humble-webots-ros2`
- `urdf2webots` paquet de tuyaux

<a id="launch"></a>
## Lancement

<a id="docker"></a>
### Docker

```bash
cd simulation/so_arm_101_description
docker compose run webots
```

> **Notes**Le: Webots Le service d'accueil n'a pas de volume. Le fichier mondial est généré à l'intérieur de l'image au moment de la création. Si vous modifiez l'URDF, vous devez reconstruire: `docker compose build webots`.

<a id="native-ros2"></a>
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

<a id="how-it-works"></a>
## Comment cela fonctionne

1. `scripts/setup_webots.py` convertisse l'URDF en un Webots Nœud robot via `urdf2webots` et génère `worlds/webots_sim.wbt`
2. Les `WebotsLauncher` ouvre le fichier monde dans Webots
3. `WebotsController` se connecte au robot par l'intermédiaire de l'IPC et démarre le `ros2_control` conducteur
4. Le contrôleur `<extern>` la balise dans le fichier monde permet `webots_ros2_driver` pour prendre le contrôle
5. Un URDF pré-expansionné (`so_101_webots.urdf`) est nécessaire parce que `WebotsController` nécessite un chemin de fichier, pas XML en ligne

<a id="world-settings"></a>
### Les situations dans le monde

- `basicTimeStep`: 16 ms (réduit par défaut pour la stabilité physique)
- `maxContactJoints`: 4 (limite les frais de collision des réseaux détaillés)

<a id="known-issues"></a>
## Des questions connues

- **Chargement global lent sur X11**: Le monde prend environ 120 secondes à charger lorsque le rendu est transféré via X11. Le temps de répartition du régulateur est fixé à 180s pour s'adapter.
- **Rendering du câble sur Windows**: VcXsrv fournit seulement OpenGL 1.4, mais Webots nécessite OpenGL 3.3. La simulation fonctionne, mais se rend dans le mode wireframe.
- **Détection WSL2**: Docker sur WSL2 hérite du nom du noyau WSL, causant `webots_ros2_driver` à rechercher `webots.exe`. Les correctifs du fichier Docker `is_wsl()` pour toujours revenir `False`.
- **Avertissements de physique**: "Votre monde est peut-être trop complexe" des avertissements peuvent apparaître en raison de réseaux de collision à polyvalence élevée.

<a id="troubleshooting"></a>
## Résolution des problèmes

- **`WEBOTS_HOME` non trouvé**: Assurer `WEBOTS_HOME=/usr/local/webots` - C'est réglé. L'image de Docker le définit automatiquement.
- **Temps d'arrêt du contrôleur**: Si les contrôleurs ne s'activent pas, augmentez le délai de `launch/sim.launch.py` (actuellement des années 180).
- **Pas d' affichage**: Webots Il a besoin de X11. Sur Windows, utilisez VcXsrv avec `-ac -wgl` les drapeaux.
<!-- /translated-content -->

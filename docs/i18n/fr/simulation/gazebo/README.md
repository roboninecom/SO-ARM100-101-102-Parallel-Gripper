<!-- translation-navigation -->
[English](../../../en/simulation/gazebo/README.md) · [Русский](../../../ru/simulation/gazebo/README.md) · [Español](../../../es/simulation/gazebo/README.md) · [Français](README.md) · [Deutsch](../../../de/simulation/gazebo/README.md) · [Português (Brasil)](../../../pt-BR/simulation/gazebo/README.md) · [简体中文](../../../zh-CN/simulation/gazebo/README.md) · [日本語](../../../ja/simulation/gazebo/README.md) · [हिन्दी](../../../hi/simulation/gazebo/README.md) · [العربية](../../../ar/simulation/gazebo/README.md)

[Source anglaise](../../../../../simulation/gazebo/README.md)

[Français](../../README.md)

> Traduction automatique intégrale, pas encore relue par des locuteurs natifs. Images, code, CAO et PDF originaux sont partagés. En cas de doute, consultez la source anglaise.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="gazebo-gz-sim"></a>
# Gazebo Je vous en prie .

**Statut: prêt**

Gazebo simulation en utilisant `gz_ros2_control` Le plugin. Le gestionnaire du contrôleur court à l'intérieur de la Gazebo le processus.

<a id="prerequisites"></a>
## Préalabilités

**Docker (recommandé):**
- Tableau de bureau Docker

**Native ROS2:**
- ROS2 Humble
- `ros-humble-gz-ros2-control`
- `ros-humble-ros-gz-sim`
- `ros-humble-ros-gz-bridge`

<a id="launch"></a>
## Lancement

<a id="docker"></a>
### Docker

```bash
cd simulation/so_arm_101_description
docker compose run gazebo
```

Pour le NVIDIA GPU, passez par `deploy:` bloc dans `docker-compose.yaml`:

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
### Native ROS2

```bash
ros2 launch so_arm_101_description sim.launch.py sim:=gazebo
```

<a id="how-it-works"></a>
## Comment cela fonctionne

1. Les Gazebo Plugin `gz_ros2_control/GazeboSimSystem` est sélectionnée par le `sim_backend:=gazebo` l'argument de xacro
2. Gazebo intégre le gestionnaire du contrôleur - pas de séparation `ros2_control_node` nécessaire
3. Le robot est engendré dans `worlds/empty.sdf` à travers `ros_gz_sim create`
4. Les régulateurs commencent après `robot_state_publisher` est en cours d' exécution

<a id="world-file"></a>
### Fichier mondial

`worlds/empty.sdf` prévoit:
- Moteur de physique ODE (étape en temps)0.004s / 250Hz)
- Plan de terrain (100x100m)
- L'éclairage solaire directionnel

<a id="verify"></a>
## Vérifiez

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
## Résolution des problèmes

- **Ne trouvant pas de filets**: Assurer `GZ_SIM_RESOURCE_PATH` inclut le répertoire des parts de forfait. Le point d'entrée Docker le fixe automatiquement.
- **Pas d' affichage**: Gazebo Il a besoin d'un serveur X11. Sur Windows, utilisez VcXsrv avec `-ac` Le drapeau. Sur macOS, utilisez XQuartz.
- **Rendering lent**: Décommenter la GPU en passant par le bloc `docker-compose.yaml` si vous avez un GPU NVIDIA.
<!-- /translated-content -->

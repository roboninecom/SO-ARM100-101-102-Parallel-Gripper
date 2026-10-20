<!-- translation-navigation -->
[English](../../../en/simulation/mujoco/README.md) · [Русский](../../../ru/simulation/mujoco/README.md) · [Español](../../../es/simulation/mujoco/README.md) · [Français](README.md) · [Deutsch](../../../de/simulation/mujoco/README.md) · [Português (Brasil)](../../../pt-BR/simulation/mujoco/README.md) · [简体中文](../../../zh-CN/simulation/mujoco/README.md) · [日本語](../../../ja/simulation/mujoco/README.md) · [हिन्दी](../../../hi/simulation/mujoco/README.md) · [العربية](../../../ar/simulation/mujoco/README.md)

[Source anglaise](../../../../../simulation/mujoco/README.md)

[Français](../../README.md)

> Traduction automatique intégrale, pas encore relue par des locuteurs natifs. Images, code, CAO et PDF originaux sont partagés. En cas de doute, consultez la source anglaise.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="mujoco"></a>
# MuJoCo

**Statut: prêt**

MuJoCo simulation en utilisant `mujoco_ros2_control` (Ros-contrôle fourchette). MuJoCo convertisse l'URDF en MJCF en interne et exécute la physique + le rendu dans le `ros2_control_node` le processus.

<a id="prerequisites"></a>
## Préalabilités

**Docker (recommandé):**
- Tableau de bureau Docker

**Native ROS2:**
- ROS2 Humble
- `mujoco_ros2_control` (construit à partir de la source - voir ci-dessous)
- `mujoco` paquet de tuyaux

<a id="launch"></a>
## Lancement

<a id="docker"></a>
### Docker

```bash
cd simulation/so_arm_101_description
docker compose run mujoco
```

L'image de Docker se construit `mujoco_ros2_control` à partir de la source automatiquement.

<a id="native-ros2"></a>
### Native ROS2

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
## Comment cela fonctionne

1. Le plugin `mujoco_ros2_control/MujocoSystemInterface` est sélectionnée via `sim_backend:=mujoco`
2. Un nœud personnalisé (`publish_mujoco_description`) publie l'URDF au `/mujoco_robot_description`
3. Les MuJoCo Le plugin lit l'URDF, le convertit en MJCF et démarre la simulation
4. Les `<mujoco><compiler meshdir=.../>` la balise dans l'URDF indique MuJoCo où trouver des mailles de collision
5. Une fenêtre de rendu s'ouvre montrant la simulation (1280x720, par défaut à l'écran complet)

<a id="key-parameters-in-so_101ros2_controlxacro"></a>
### Paramètres clés `so_101.ros2_control.xacro`)

- `headless`Réglage: `true` pour le mode sans tête (pas de fenêtre de rendu)
- `sim_speed_factor`: Multiplicateur de vitesse de simulation (par défaut: 1.0)

<a id="verify"></a>
## Vérifiez

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
## Résolution des problèmes

- **Erreurs OpenGL**: Assurez-vous que les pilotes de GPU sont installés. Pour Docker, décommenter le blocage de la GPU NVIDIA dans `docker-compose.yaml`.
- **La fenêtre est trop grande**: L'image de Docker fixe la fenêtre à 1280x720. Pour les installations natives, le MuJoCo la fenêtre peut être plein écran par défaut.
- **Pas d' affichage**: MuJoCo Il a besoin d'un serveur X11 pour la fenêtre de rendu. Utilisation `headless:=true` dans le xacro si aucun écran n'est disponible.
<!-- /translated-content -->

<!-- translation-navigation -->
[English](../../../en/simulation/isaac_sim/README.md) · [Русский](../../../ru/simulation/isaac_sim/README.md) · [Español](../../../es/simulation/isaac_sim/README.md) · [Français](README.md) · [Deutsch](../../../de/simulation/isaac_sim/README.md) · [Português (Brasil)](../../../pt-BR/simulation/isaac_sim/README.md) · [简体中文](../../../zh-CN/simulation/isaac_sim/README.md) · [日本語](../../../ja/simulation/isaac_sim/README.md) · [हिन्दी](../../../hi/simulation/isaac_sim/README.md) · [العربية](../../../ar/simulation/isaac_sim/README.md)

[Source anglaise](../../../../../simulation/isaac_sim/README.md)

[Français](../../README.md)

> Traduction automatique intégrale, pas encore relue par des locuteurs natifs. Images, code, CAO et PDF originaux sont partagés. En cas de doute, consultez la source anglaise.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="nvidia-isaac-sim"></a>
# NVIDIA Isaac Oui

**Statut: Non testé (simulateur externe)**

Isaac Le Sim fonctionne à l'extérieur et communique avec ROS2 à travers `topic_based_ros2_control`. Vous courez Isaac Simuler séparément et lancer le ROS2 côté avec `sim:=isaac`.

<a id="prerequisites"></a>
## Préalabilités

- [NVIDIA Isaac Oui](https://developer.nvidia.com/isaac-sim) 4.0+ (exige une GPU NVIDIA RTX)
- ROS2 Humble
- Isaac Oui ROS2 pont activé
- `topic_based_ros2_control`:
  ```bash
  sudo apt install ros-humble-topic-based-ros2-control
  ```

<a id="setup"></a>
## Installation

<a id="1-import-urdf-into-isaac-sim"></a>
### 1. Importation de l'URDF dans Isaac Oui

```bash
# Generate expanded URDF
source /opt/ros/humble/setup.bash
xacro so_arm_101_description/urdf/so_101.urdf.xacro sim_backend:=isaac > /tmp/so_101_isaac.urdf
```

Dans Isaac Je vous en prie .
1. **Isaac Utils > Importateur URDF**
2. **Fichier d'entrée**: sélectionner `/tmp/so_101_isaac.urdf`
3. **Localisation de l'importation**: `/World/so_101`
4. **Type d'entraînement commun**Position:
5. **Régler le lien de base**: vérifiée
6. Cliquez sur **Les importations**
7. Ajoutez un avion au sol: **Créer > Physique > Plan de terre**
8. Exception de l'étape USD (facultative)

<a id="2-configure-ros2-bridge-omnigraph"></a>
### 2. Configuration ROS2 Le pont (Omnigraph)

Les `topic_based_ros2_control` le plugin communique par l'intermédiaire de ces sujets:

| Thème | Type | Direction |
|-------|------|-----------|
| `/joint_states` | `sensor_msgs/JointState` | Isaac Sim -> ROS2 |
| `/joint_commands` | `std_msgs/Float64MultiArray` | ROS2 -> Isaac Oui |

<a id="omnigraph-setup"></a>
#### Configuration de l' omnigraph

1. Ouvert **Fenêtre > Scripts visuels > Graphique d'action**
2. Créer un nouveau graphique d'action
3. Ajoutez ces nœuds:
   - **Sur le tique de lecture** (source de l'événement)
   - **Isaac Temps de simulation**
   - **ROS2 Publier État commun** -- se connecter à `/World/so_101`
   - **ROS2 Souscrivez à l'État commun** -- pour recevoir des commandes
   - **Isaac Contrôleur de l'articulation** -- applique des commandes aux articulations

4. Connectez le graphique:
   ```
   On Playback Tick -> Read Sim Time -> Publish Joint State
   On Playback Tick -> Subscribe Joint State -> Articulation Controller
   ```

5. Configuration **Publier État commun** le nœud:
   - `targetPrim`: `/World/so_101`
   - `topicName`: `/joint_states`

6. Configuration **Contrôleur de l'articulation** le nœud:
   - `targetPrim`: `/World/so_101`
   - `jointNames`: tous les 7 noms communs de `config/controllers.yaml`

<a id="alternative-isaac_ros2_control"></a>
#### Alternative: isaac_ros2_control

Si `isaac_ros2_control` est disponible pour votre Isaac La version sim:

```bash
sudo apt install ros-humble-isaac-ros2-control
```

Cela remplace la configuration OmniGraph par une `ros2_control` interface matérielle.

<a id="3-launch"></a>
### 3. Lancement

```bash
# Terminal 1: Start Isaac Sim and press Play

# Terminal 2: Launch ROS2 side
ros2 launch so_arm_101_description sim.launch.py sim:=isaac
```

<a id="verify"></a>
## Vérifiez

```bash
ros2 topic echo /joint_states --once

ros2 topic pub /arm_controller/joint_trajectory trajectory_msgs/msg/JointTrajectory "{
  joint_names: ['base_link_to_link1'],
  points: [{positions: [0.5], time_from_start: {sec: 2}}]
}" --once
```

<a id="troubleshooting"></a>
## Résolution des problèmes

- **Échec de l'importation du URDF**: Veillez à ce que tous les voies de maillage soient absolues. Générer l' URDF avec `xacro` d'abord - ne pas importer le `.xacro` le dossier directement.
- **Aucun État commun**: Vérifiez que l' OmniGraph est connecté et Isaac Sim est en mode jeu.
- **Instabilité physique**: Dans les propriétés de scène physique, définissez le type de solveur à TGS et augmentez le nombre d'itérations.
- **ROS2 pont non trouvé**: Activer l'extension dans **Fenêtre > Extensions > ROS2 Ponte**.
<!-- /translated-content -->

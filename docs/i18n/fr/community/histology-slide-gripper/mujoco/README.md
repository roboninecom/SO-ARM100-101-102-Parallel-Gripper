<!-- translation-navigation -->
[English](../../../../en/community/histology-slide-gripper/mujoco/README.md) · [Русский](../../../../ru/community/histology-slide-gripper/mujoco/README.md) · [Español](../../../../es/community/histology-slide-gripper/mujoco/README.md) · [Français](README.md) · [Deutsch](../../../../de/community/histology-slide-gripper/mujoco/README.md) · [Português (Brasil)](../../../../pt-BR/community/histology-slide-gripper/mujoco/README.md) · [简体中文](../../../../zh-CN/community/histology-slide-gripper/mujoco/README.md) · [日本語](../../../../ja/community/histology-slide-gripper/mujoco/README.md) · [हिन्दी](../../../../hi/community/histology-slide-gripper/mujoco/README.md) · [العربية](../../../../ar/community/histology-slide-gripper/mujoco/README.md)

[Source anglaise](../../../../../../community/histology-slide-gripper/mujoco/README.md)

[Français](../../../README.md)

> Traduction automatique intégrale, pas encore relue par des locuteurs natifs. Images, code, CAO et PDF originaux sont partagés. En cas de doute, consultez la source anglaise.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="microscope-slide-gripper-in-mujoco"></a>
# Grippe à diapositives au microscope MuJoCo

Les SO-ARM101 avec la poignée parallèle de glissage histologique, exportée à partir de Fusion et montée au lieu des pinces Robo9 en stock.

Testé avec: `mujoco` 3.4.0 dans le `lerobot` l'environnement du condo. Je ne peux pas . ROS 2 ou Docker est nécessaire.

```bash
conda activate lerobot
cd community/histology-slide-gripper/mujoco
python -m pip install -r requirements.txt
python view.py                      # full arm + slide gripper
python view.py scene_gripper.xml    # gripper alone on a testbench
python test_grasp.py                # headless grasp-and-lift check -> grasp_check.png
```

<a id="mujoco-simulation-preview"></a>
## MuJoCo prévisualisation de la simulation

![SO-ARM101 l'accélérateur de glissage en cours d'exécution MuJoCo](../../../../../../community/histology-slide-gripper/mujoco/mujoco_simulation_preview.png)

Cette scène montre SO-ARM101 avec la griffe parallèle à l'écoulement histologique montée sur
le poignet, en utilisant la même MuJoCo modèle lancé par:

```bash
conda activate lerobot
cd community/histology-slide-gripper/mujoco
python view.py
```

<a id="what-is-modelled"></a>
## Ce qui est modélisé

| Le lien | Sources | La masse |
|---|---|---|
| `slide_gripper_base` | Châssis principal, STS3215, barres de guidage, roulements, tenant de caméra, Arducam OV9281 | 0.20kg |
| `sg_jaw_right` / `sg_jaw_left` | RB9.01.062.020 accrocheuse + RB9.01.062.030 rack (m)0.8) | 0.035kg par personne |
| `sg_pinion` | RB9.01.062.040 équipement involu,18 T, 0.8module | 0.008kg |

Cinématique tirée des articulations construites dans l'assemblage Fusion
(`Slide_Jaw_Right`, `Slide_Jaw_Left`, `Drive_Pinion`), qui sont cohérentes:
le18 T / 0.8le pignon du module a une7.2radius de plongée mm et7.2mm x4.9306RAD =
**35.5le** de déplacement par mâchoire  ⁇  exactement les limites du curseur dans le CAD.

<a id="control"></a>
## Contrôle

Un actionneur, `sg_grip`, commandé en **mètres de déplacement des mâchoires**:

| `ctrl` | voyage de la mâchoire | ouverture entre les faces de la lame |
|---|---|---|
| `0.0` | 0 mm | **84 mm** (Tou pleinement ouvert) |
| `0.0295` | 29.5le | 25 mm (une diapositive au microscope) |
| `0.0355` | 35.5le | **13 mm** (completement fermé) |

Les deux mâchoires sont entraînées par le seul pignon, donc `sg_jaw_left_joint` et
`sg_pinion_joint` sont asservis à `sg_jaw_right_joint` par `<equality>` restrictions  ⁇
l'équipement tourne visiblement avec les mâchoires. Le commandement *passé* l'objet à serrer:
se fermer sur un objet de 25 mm avec `ctrl=0.0355` donne sur4.7N à l'étagère.

Les cinq articulations de bras conservent leur nom URDF (`base_link_to_link1` ... `link4_to_link5`).

<a id="collision-geometry"></a>
## Géométrie de collision

Les géomètres de maille sont **uniquement visuel** (`contype=0`), parce que MuJoCo des tresses convexes et
la coque d'une mâchoire en forme de L remplit le vide que vous essayez de saisir. Le contact est
portés par des boîtes sur les deux surfaces de prise de chaque mâchoire (groupe 3, caché dans le
les rendements):

- `sg_pad_*` ⁇  la lame à diapositives de 30 mm, CAD x 42 ⁇ 50, z 26 ⁇ 31
- `sg_mid_*` ⁇  la section centrale plus large, CAD x 42 ⁇ 58, z 18.5 ⁇ 38.5

Le site TCP `sg_tcp` se trouve entre les lames; `sg_camera` est le cadre optique Arducam.

<a id="files"></a>
## Fichiers

- `so101_slide_gripper.xml` ⁇  le robot complet (généré par `build_full.py`)
- `scene_gripper.xml` ⁇  seule prise, avec axe de levage pour l'essai
- `gripper_assets.xml` / `gripper_body.xml` / `gripper_actuation.xml` ⁇  la prise,
  comme incluant les modèles d'unité de degré et de radian utilisables
- `meshes/{base,jaw_right,jaw_left,pinion}.stl` ⁇  exporté à partir de Fusion **assemblage
  coordonnées**, de sorte que chaque partie est déjà à sa place correcte (pas d' origines par partie pour poursuivre)
- `meshes/arm/` ⁇  des mailles de bras du repo Robo9
- `build_arm.py` ⁇  rayures xacro de `so_101.urdf.xacro`, abandonne les pinces de stock, compile à MJCF
- `build_full.py` ⁇  greffe la poignée sur `link5`; **modifier `MOUNT_POS`/`MOUNT_QUAT` Je suis ici.**

<a id="how-the-gripper-was-located-on-the-wrist"></a>
## Comment la poignée était placée sur le poignet

`link5_1.stl` dans le Robo9 repo n'est pas seulement le poignet  ⁇  il contient l'ensemble du stock
le capteur (cadre, barres de guidage, caméra). C'est donc la partie que remplace la conception de l'adhésif, et
`build_full.py` supprime son filet et la masse de0.556kg à0.08Le poids de l'eau

La pose de la montagne a été résolue, pas devinée: `base.stl` a été monté contre
`link5_1.stl` sur la géométrie qu'ils partagent (cadre principale + barres de guidage) en recherchant tous
24 rotations alignées sur un axe et marquant la distance du voisin le plus proche. Le meilleur adapté est
**+90 degrés environ X** (CAD + Y -> lien)5+Z, CAD +Z -> lien5-Y) avec un2.0mm médiane
les pinces de diapositives sont suspendues perpendiculairement aux pinces poncées de Robo9, correspondant
l'assemblage de fusion.

<a id="stability"></a>
## Stabilité

Le modèle s'arrête à `max|qvel| = 0` et reste là. Si vous le voyez trembler,
La première chose à vérifier est les contacts errants (`ncon` dans le panneau d'information du spectateur devrait être 0
avec le bras au repos). Trois choses étaient nécessaires:

1. **`<exclude body1="world" body2="link1_1"/>`** - la vraie solution. L'importateur URDF
   fusions `base_link` dans `worldbody`, et MuJoCo échappe aux collisions parent/enfant
   *à l'exception* quand le parent est le corps mondial. Donc le filet de base et le filet de lien1
   interpénétré à l'épaule, produisant un contact permanent qui a collé le jaune
   l'actionneur à son +-1.5N.m limite. Cela seul a pris réglé `|qvel|` à partir4.78à0.
2. `sg_pinion_joint` l'armature 1e-6 -> **1e-4**. Une union esclave d'une rigide égalité avec
   Il n'y avait pratiquement pas de bavardage d'inertie (il atteignait un pic à 12 rad/s).
3. L'égalité `solref` 0.002 -> **0.01**. Une constante de contrainte temporelle égale à l'étape du temps
   est trop rigide pour résoudre de manière propre; cela a également fait l'atterrissage du pivot exactement sur-282.5dégagement
   au lieu de -280 degrés.

<a id="caveats"></a>
## Les cavernes

- **Les masses sont supposées, pas mesurées.** La fusion rapporte que chaque corps est en acier (les mâchoires
  sortir à221g); les valeurs ci-dessus sont des estimations de PLA et de matériel. Si vous
  attribuer des matériaux réels dans Fusion, mettre à jour le `mass=` attributs dans `gripper_body.xml`.
- L'inertie est dérivée de MuJoCo de la forme du maillage plus cette masse, pas du tensor de Fusion.
- Les limites articulaires du bras, l'amortissement et la friction sont hérités de l'URDF du repo et
  n'ont pas été réajustés.
- **Les masses de liens du bras sont aussi denses en acier**, le même défaut que la prise:
  totaux des références URDF **2.81kg** contre environ 1 kg pour un vrai SO-101, et `link2_to_link3`
  besoins1.91N.m pour se tenir debout contre un1.5N.m limite de l'actionneur, donc il s'affaisse. C' est vrai .
  ne provoque pas de tremblement (voir ci-dessus), mais il fait le bras se comporte comme un beaucoup plus lourd
  machine. L'échelle de chaque masse du bras et `diaginertia` par ~0.36le total est
  1.19kg et élimine la saturation; STS3215 aussi des stands plus proches2.9N.m que le
  L'URDF est conservateur de 1.5.
- Le résidu d'alignement de 2 mm est réel: le "Follower main frame_125" n'est pas identique
  à l'arbre cuit dans `link5_1.stl`.
- `sg_pinion_joint` est cosmétique - il ne porte pas de charge, parce que les deux étagères sont couplées
  directement les uns aux autres. Il existe pour que le matériel tourne dans la bonne direction à l'écran.

<a id="driving-it-in-the-mujoco-viewer"></a>
## Je le conduis dans la MuJoCo le spectateur

Utilisez le **`sg_grip` glisser dans le panneau de contrôle**. Les curseurs dans le *Partage des* panneau
écrire `qpos` Il est important que l'éducation et la formation des enfants soient plus efficaces.
- le pivot de l'appareil. Presser Run le converge à nouveau.

<a id="re-exporting-after-a-cad-change"></a>
## Réexportation après changement de CA

L'exportation s'est effectuée à travers la connexion MCP Fusion: elle traverse tous les événements, groupes
corps dans les quatre liaisons rigides, et écrit des STL binaires en coordonnées d'assemblage
Il y en a un. Réexportation avec la conception Fusion ouverte pour rafraîchir les mailles dans
Il n'y a rien d'autre à changer, sauf si vous déplacez un joint.
<!-- /translated-content -->

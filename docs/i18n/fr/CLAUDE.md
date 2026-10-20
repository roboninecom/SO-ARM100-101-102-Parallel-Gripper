<!-- translation-navigation -->
[English](../en/CLAUDE.md) · [Русский](../ru/CLAUDE.md) · [Español](../es/CLAUDE.md) · [Français](CLAUDE.md) · [Deutsch](../de/CLAUDE.md) · [Português (Brasil)](../pt-BR/CLAUDE.md) · [简体中文](../zh-CN/CLAUDE.md) · [日本語](../ja/CLAUDE.md) · [हिन्दी](../hi/CLAUDE.md) · [العربية](../ar/CLAUDE.md)

[Source anglaise](../../../CLAUDE.md)

[Français](README.md)

> Traduction automatique intégrale, pas encore relue par des locuteurs natifs. Images, code, CAO et PDF originaux sont partagés. En cas de doute, consultez la source anglaise.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="claudemd"></a>
# CLAUDE.md

Ce fichier fournit des conseils au code Claude (claude.ai/code) pour travailler avec le code dans ce référentiel.

<a id="what-this-repository-is"></a>
## Ce qu'est ce référentiel

Un projet de matériel open source: une prise parallèle imprimée en 3D SO-ARM100/101 bras robot (par Robonine). Les licences multiples: CERN-OHL-P-2.0 pour le matériel/CAD, Apache-2.0 pour le logiciel, CC BY 4.0 pour les docs  ⁇  la carte est dans `LICENSING.md`, la version lisible par machine en `REUSE.toml`, attribution à des tiers dans `NOTICE`. Les nouveaux fichiers doivent être couverts par: `REUSE.toml`; `reuse lint` Il est en précommande. La plupart des références sont des modèles CAD (`models/`), la documentation (`docs/`), et des images (`assets/`). Le code vit en deux endroits:

- `software/python/gripper_control.py` ⁇  un script de commande servo autonome pour le Feetech STS3215 (dépend de la STServo SDK, qui est cloné manuellement  ⁇  voir `software/python/requirements.txt`; il n' est pas présent sur PyPI). `examples/basic_usage.py` les importations en provenance d'une `sys.path` Je vous en prie.
- `simulation/so_arm_101_description/` — a ROS2 Un paquet de description qui simule le bracelet avec une prise dans 5 moteurs physiques. C'est ici que vivent tous les tests et la plupart des informateurs.

<a id="commands"></a>
## Les commandes

```bash
# Lint (what CI runs; hooks exclude STL/STEP files)
pre-commit run --all-files

# Offline tests (65 pytest tests; deps: pytest trimesh numpy mujoco pyyaml)
cd simulation/so_arm_101_description
python -m pytest test/ -v

# Single test file / single test
python -m pytest test/test_urdf_structure.py -v
python -m pytest test/test_config.py -k <name> -v

# Validate xacro/URDF XML without ROS2
python simulation/so_arm_101_description/scripts/validate_xml.py simulation/so_arm_101_description/urdf/*.xacro

# Docker (from simulation/so_arm_101_description/; no ROS2 install needed)
docker compose run test          # run pytest suite
docker compose run validate      # xacro + check_urdf for all 5 backends
docker compose run check-launch  # verify launch files parse
docker compose run gazebo        # or: mujoco, webots, rviz (need X11)
```

CPI (`.github/workflows/ci.yaml`) fonctionne: pré-engagement, validation XML/YAML, `xacro ... sim_backend:=<backend> | check_urdf` pour les 5 arrière-plans à l'intérieur d'une `ros:humble` Le conteneur, et la suite la plus petite. Une modification de l'URDF doit rester valable pour **tous** Les arrière-plan, pas seulement celui que vous ciblez.

<a id="simulation-architecture"></a>
## Architecture de simulation

Une description paramétrisée du robot entraîne chaque simulateur:

- `urdf/so_101.urdf.xacro` est la seule source de vérité. Le xacro arg `sim_backend:=gazebo|mujoco|webots|coppeliasim|isaac` sélectionne le `ros2_control` le plug-in (via `urdf/so_101.ros2_control.xacro`) au moment de l'expansion.
- `config/controllers.yaml` définit des joints/contrôleur identiques pour tous les arrière-plans; `launch/sim.launch.py` avec `sim:=<backend>` est le point d'entrée unique.
- Robot: bras 5 DOF + poignée avec 2 joints prismatiques, où la poignée gauche reflète la droite via `<mimic>`.
- Les mailles sont divisées: `meshes/visual/` (Poly haut) contre `meshes/collision/` (carcasses convexes, régénérées avec `scripts/generate_collision_meshes.py`).

Une modification des joints, liens ou noms de contrôleurs nécessite généralement des modifications coordonnées à travers les fichiers xacro. `controllers.yaml`, et les tests en `test/`.

<a id="cad-models-and-part-numbering"></a>
## Modèles CAD et numérotation des pièces

Parties dans `models/parts/` utilisation Robonine numéros de pièces (par exemple: `RB9.01.062.010 Main frame.STL`). Ces chiffres sont référencés dans `README.md` (tableau imprimé), `docs/bom.md`, et `docs/assembly-guide.md` ⁇  ajouter ou renommer une partie implique également la mise à jour de ces documents. Les STL sont binaires; les variantes encodent les tolérances d'ajustement dans le nom du fichier (p. ex. `RB9.01.062.021 (D6.1) Clamp.STL` pour différents diamètres de la tige). Les crochets pré-engagement (espace blanc, EOF, fin de ligne) excluent délibérément `.stl/.STL/.STEP` les fichiers et les fichiers de plus de 1 Mo sont rejetés par `check-added-large-files`.

<a id="conventions"></a>
## Les assemblées

- Python: flake8 avec `--max-line-length=100`, est classé avec un profil noir (imposé par l'engagement préalable; `software/` et `examples/` sont exclus de la flèche8).
- Les documents sont dupliqués par conception bom.md, specifications.md, assembly-guide.md)  ⁇  les maintenir cohérents lors de la modification des spécifications, pièces ou prix.
- Ne pas ajouter un `Co-Authored-By: Claude` La ligne des engagements.
<!-- /translated-content -->

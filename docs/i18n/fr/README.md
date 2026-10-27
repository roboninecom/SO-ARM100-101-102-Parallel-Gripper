<!-- translation-navigation -->
[English](../en/README.md) · [Русский](../ru/README.md) · [Español](../es/README.md) · [Français](README.md) · [Deutsch](../de/README.md) · [Português (Brasil)](../pt-BR/README.md) · [简体中文](../zh-CN/README.md) · [日本語](../ja/README.md) · [हिन्दी](../hi/README.md) · [العربية](../ar/README.md)

[Source anglaise](../../../README.md)

[Français](README.md)

> Traduction automatique intégrale, pas encore relue par des locuteurs natifs. Images, code, CAO et PDF originaux sont partagés. En cas de doute, consultez la source anglaise.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="so-arm100101-parallel-gripper"></a>
# SO-ARM100/101 Pince parallèle

<div align="center">

[![SO-ARM101 Pince parallèle](../../../assets/images/SO%20ARM%20101%20Parallel%20Gripper%20Live.jpg)](https://youtube.com/shorts/bSyXjgNGXZk)

**🎥 [Attention à la prise en action !](https://youtube.com/shorts/bSyXjgNGXZk)** · **🛒 [Achetez le SO-ARM102 un kit avec une prise parallèle](https://robonine.com/shop/so-arm102-robotic-arm-kit/)**

Une prise parallèle légère imprimée en 3D conçue par: **[Robonine](https://robonine.com)** pour le code open source SO-ARM100/101 une plateforme robotique.

> Vous préférez un kit de bras robot complet avec une prise parallèle ? **[Achetez le SO-ARM102 kit](https://robonine.com/shop/so-arm102-robotic-arm-kit/)**.

[![Le matériel: CERN-OHL-P-2.0](https://img.shields.io/badge/Hardware-CERN--OHL--P--2.0-blue.svg)](../../../HARDWARE-LICENSE.txt)
[![Logiciel: Apache-2.0](https://img.shields.io/badge/Software-Apache--2.0-blue.svg)](../../../SOFTWARE-LICENSE.txt)
[![Documents: CC BY 4.0](https://img.shields.io/badge/Docs-CC%20BY%204.0-blue.svg)](../../../DOCS-LICENSE.txt)
[![Coût: ~$50](https://img.shields.io/badge/Cost-~%2450-green.svg)](docs/bom.md)
[![Assemblage: 30 minutes](https://img.shields.io/badge/Assembly-30%20min-orange.svg)](docs/assembly-guide.md)

---

**Des questions ? On est là pour aider !**
⁇  E-mail: [bonjour@robonine.com](mailto:hello@robonine.com)

</div>

---

<a id="-key-features"></a>
## ✨ Caractéristiques clés

| Caractéristiques | Définition |
|---------|-------------|
| **Force d'attraction 120N** | Mécanisme de mâchoire parallèle fiable |
| **14 mm/s Vitesse** | Vitesse de fonctionnement de la griffe |
| **84 mm coup complet** | Large ouverture pour divers objets |
| **0.5mm Répétabilité** | Positionnement de haute précision |
| **Compatible avec la caméra** | Apports RealSense, Orbbec, caméras USB |
| **Imprimable en 3D** | Toutes les pièces imprimées sur des imprimantes FDM standard |
| **~$50Coût total** | Une solution open source abordable |
| **Assemblage facile** | 30-45minutes avec des outils de base |

---

<a id="-gallery"></a>
## ⁇  Galerie

<div align="center">

<a id="gripper-on-so-arm101"></a>
### Pince sur SO-ARM101

![Pince montée sur SO-ARM101](../../../assets/images/specification/07-gripper-on-so-arm100.jpg)

*Grippe de suivi intégrée à SO-ARM101 bras robot*

<a id="dimensions"></a>
### Dimensions

![Dimensions de la pince](../../../assets/images/specification/08-gripper-dimensions-3d.png)

*128 × 109 × 130.5mm, coup complet84le*

</div>

---

<a id="-specifications"></a>
## ⁇  Spécifications

<a id="gripper-parameters"></a>
### Paramètres de la pince

| Paramètre | La valeur |
|-----------|-------|
| Force d'attraction maximale | **120 N** |
| Vitesse de prise maximale | **14 mm/s** |
| Un coup complet | **84 mm** |
| Répétabilité | **0.5le** |
| Masse de l'assemblage (PLA, 30% de remplissage) | **170 g** |
| DOF | **1** |

<a id="dimensions-1"></a>
### Dimensions

| Dimension | La valeur |
|-----------|-------|
| Largeur | 128 mm |
| Profondeur | 130.5le |
| La hauteur | 109 mm |

<a id="servo-parameters-feetech-sts3215"></a>
### Paramètres servo (Feetech STS3215)

| Paramètre | La valeur |
|-----------|-------|
| Voltage de fonctionnement | 12V |
| Couple de blocage | 30 kg·cm |
| Vitesse (pas de charge) | 45 tours à la minute |
| Codificateur | Magnétique absolue à 12 bits |
| Protocole | RS485/TTL jusqu'à 1 Mbps |
| Température de fonctionnement | -20°C ~ 60°C |

---

<a id="-camera-compatibility"></a>
## ⁇  Compatibilité avec la caméra

La prise prend en charge plusieurs caméras via le support de la caméra interchangeable:

| Une caméra | Type | Cas d'utilisation |
|--------|------|----------|
| L'équipement335 5USB MP | RGB | Les tâches de base de la vision |
| GC2093 USB de 2 MP | RGB | Option budgétaire |
| Orbbec Gémeaux 2 | RGB-D | Perception en 3D |
| RealSense D405 | RGB-D | Profondeur à courte portée |
| RealSense D435/D435i | RGB-D | Objectif général |
| RealSense D455 | RGB-D | Profondeur à longue portée |

<div align="center">

![Différentes caméras montées sur la prise](../../../assets/images/specification/09-camera-types.png)

*RealSense, module de caméra USB, Orbbec Gémeaux 2*

</div>

---

<a id="-bill-of-materials"></a>
## ⁇  Résumé des matériaux

**Coût total: ~$50** ([BOM complet avec des liens Amazon](docs/bom.md))

| Catégorie | Components | Est. Coût |
|----------|------------|-----------|
| Électronique | Feetech STS3215 Servo | ~$29 |
| Roulements | MF106ZZ (x2) | ~$2 |
| Tubes d'aluminium et de carbone | D6x1x125mm (x2) | ~$4 |
| Impression en 3D | 8pièces (~100-150g PLA) | ~$12 |
| Fixations | Viraux M2/M4, noix M2, vis de série M3 | ~$3 |

---

<a id="-quick-start"></a>
## ⁇  Début rapide

Pour un kit de bras robot complet avec une prise parallèle, **[acheter le SO-ARM102 kit](https://robonine.com/shop/so-arm102-robotic-arm-kit/)**. Pour construire le SO-ARM100/101 Prenez-vous, suivez les étapes ci-dessous.

<a id="1-print-the-parts-2-4-hours"></a>
### 1. Impression des pièces (2-4 heures)

Télécharger des fichiers STL à partir [`models/parts/`](models/README.md). Compatible avec les imprimantes populaires comme **Lab A1 mini**, **Prusa MINI+**, et toute imprimante avec un lit de 180 × 180 mm ou plus.

| Partie | Qty | Paramètres |
|------|:---:|----------|
| Châssis principal (RB9.01.062.010) | 1 | Remplissage de 20% |
| Mâchoire (RB9.01.062.020) | 2 | Remplissage de 20% |
| Crémaillère (RB9.01.062.030) | 2 | Remplissage à 100% |
| Engrenage (RB9.01.062.040) | 1 | Remplissage à 100% |
| Support de caméra (RB9.01.060.074) | 1 | Remplissage de 20% |
| Support (RB9.01.060.080) | 1 | Remplissage de 20% |
| Entretoise de caméra (RB9.01.060.090) | 1 | Remplissage de 20% |
| D405 détenteur (RB9.01.060.110) | 1 | Remplissage de 20% |

<a id="2-order-components-1-2-days"></a>
### 2. Components d'ordre (1-2jours)

Vous voyez ? [Résumé des matières](docs/bom.md) pour les liens directs Amazon.

<a id="3-assemble-30-45-minutes"></a>
### 3. Assemblage (30-45minutes)

Suivez le [Guide d'assemblage](docs/assembly-guide.md) avec des images pas à pas:

1. Montez l'équipement sur le disque servo, installez cet ensemble sur le servo
2. Insérer le câble servo
3. Utilisation Feetech Le logiciel déplace le serveur à sa position minimale (déplacez le curseur dans le logiciel vers la gauche)
4. Fixez les crémaillères aux mâchoires
5. Insérez les tiges de guidage dans les deux mâchoires
6. Installez les roulements sur le châssis principal et fixez-les avec des vis
7. Enclenchez les tiges de guidage dans le châssis
8. Écartez les mâchoires jusqu’aux positions extrêmes à gauche et à droite
9. Insérer le servo et le fixer avec des vis
10. Appliquer une caméra spacer et une caméra UVC, fixée avec des vis 4x et des noix M2 (facultatif)
11. Montage au bras robot (facultatif)

<a id="4-software"></a>
### 4. Logiciel

```bash
# Configure servo motor if necessary
https://lab.robonine.com/tools/robonine/feetech-bus

# Control gripper
https://lab.robonine.com/tools/robonine/control-robot
```

---

<a id="-repository-structure"></a>
## ⁇  Structure du référentiel

```
├── assets/
│   └── images/
│       ├── assembly/          # Assembly step images
│       └── specification/     # Technical drawings
├── docs/
│   ├── assembly-guide.md                # Step-by-step assembly
│   ├── bom.md                           # Bill of materials with links
│   ├── Parallel gripper by Robo9.pdf    # Gripper product specification
│   ├── quick-start.md                   # Getting started guide
│   ├── SO-ARM101 by Robo9.pdf           # SO-ARM101 product specification
│   └── specifications.md               # Technical specifications
├── models/
│   ├── parts/                                    # Individual STL files
│   └── Follower gripper (165x165 bed size).STL   # Complete assembly (165×165mm bed)
├── community/
│   └── histology-slide-gripper/   # Community variant (CAD, MuJoCo model)
├── simulation/
│   ├── README.md                  # Simulation overview
│   ├── gazebo/                    # Gazebo guide
│   ├── mujoco/                    # MuJoCo guide
│   ├── webots/                    # Webots guide
│   ├── coppeliasim/               # CoppeliaSim guide
│   ├── isaac_sim/                 # Isaac Sim guide
│   └── so_arm_101_description/    # ROS2 package (URDF, launch, Docker)
├── software/
│   └── python/                # Control software
├── examples/                  # Usage examples
├── HARDWARE-LICENSE.txt       # CERN-OHL-P-2.0 (CAD, geometry)
├── SOFTWARE-LICENSE.txt       # Apache-2.0 (code)
├── DOCS-LICENSE.txt           # CC BY 4.0 (docs, images)
├── LICENSING.md               # Which licence covers what
├── NOTICE                     # Third-party attribution
├── REUSE.toml                 # Machine-readable licence map
├── RELICENSING.md             # Record of the 2026 relicensing
└── CONTRIBUTING.md
```

---

<a id="-documentation"></a>
## ⁇  Documentation

| Documents | Définition |
|----------|-------------|
| [Un guide rapide pour commencer](docs/quick-start.md) | Retourne dans 30 minutes. |
| [Guide d'assemblage](docs/assembly-guide.md) | Pas à pas avec des images |
| [Guide de l'assemblage des griffes (PDF)](../../Assembly%20Guide%20Follower%20Gripper.pdf) | Instructions d'assemblage de la poignée imprimable |
| [SO-ARM101 Guide de l'assemblage (PDF)](../../Assembly%20Guide%20SO-ARM101.pdf) | Résumé SO-ARM101 instructions d'assemblage des bras |
| [Résumé des matières](docs/bom.md) | Liste des pièces avec liens Amazon |
| [Les spécifications](docs/specifications.md) | Détails techniques |
| [Modèles 3D](models/README.md) | Imprimer les paramètres et les fichiers |
| [Spécification du produit de l'adhésif parallèle (PDF)](../../Parallel%20gripper%20by%20Robo9.pdf) | Spécification du produit de la colle paralelale par Robo9 |
| [SO-ARM101 Spécification du produit (PDF)](../../SO-ARM101%20by%20Robo9.pdf) | SO-ARM101 spécification du produit de l'armure robot par Robo9 |

---

<a id="-hardware-requirements"></a>
## ⁇  Exigences matérielles

<a id="electronics"></a>
### Électronique
- 1× Feetech STS3215 Moteur de servo

Connectez la poignée à l' existing SO-ARM100/101 le serveur et le contrôleur.
Le contrôleur robot et l'alimentation font partie de la configuration du bras, en dehors du BOM de la prise.

<a id="mechanical"></a>
### Mecanique
- 2× MF106ZZ Les roulements (6×10×3 mm)
- 2x Tubes en aluminium/carbone D6x1x125 mm

<a id="fasteners"></a>
### Fixations
- 2 × M4 × 8 vis DIN 7991
- 4 fois M2x8 DIN 912 vis
- 4× M2 DIN 934 noix
- 4× M3×4 DIN 913 à vis

<a id="tools-required"></a>
### Les outils nécessaires
- Propulseur à vis à tête Phillips (PH1)
- Les clés Hex M2 (H1.5) et M4 (H2.5)

---

<a id="-simulation"></a>
## ⁇ ️ Simulation

SO-ARM101 peut être simulé dans 5 moteurs physiques grâce à un paquet de description ROS2 et un unique URDF paramétré. Aucune installation de ROS2 n’est nécessaire : Docker prend tout en charge.

<div align="center">

| Gazebo (Forteresse de l'Ignition) | MuJoCo |
|:-:|:-:|
| ![SO-ARM-101 dans Gazebo](../../../assets/images/simulation/gazebo/gazebo_pick_place.png) | ![SO-ARM-101 dans MuJoCo](../../../assets/images/simulation/mujoco/mujoco_pick_place.png) |

</div>

| Simulateur | Le statut | Docker |
|-----------|--------|--------|
| [Gazebo](simulation/gazebo/README.md) | Je suis prêt. | `docker compose run gazebo` |
| [MuJoCo](simulation/mujoco/README.md) | Je suis prêt. | `docker compose run mujoco` |
| [Webots](simulation/webots/README.md) | Instable | `docker compose run webots` |
| [CoppeliaSim](simulation/coppeliasim/README.md) | Ne pas testé | Simulateur externe |
| [NVIDIA Isaac Oui](simulation/isaac_sim/README.md) | Ne pas testé | Simulateur externe |

**Début rapide (Docker):**

```bash
cd simulation/so_arm_101_description
docker compose run gazebo    # or mujoco, webots
```

Voir le [Guide de simulation](simulation/README.md) Pour la configuration complète, les détails de l'architecture et le commandement robot.

---

<a id="-community-mods"></a>
## ⁇  Mods communautaires

Variantes de l'adhésif construites par la communauté, chacune autonome [`community/`](../../../community):

| Mod | Autrice | Définition |
|-----|--------|-------------|
| [Histologie Grippe à diapositives](community/histology-slide-gripper/README.md) | [Michael Viacheslavov](https://github.com/histochemichael) | Clampes pour les diapositives du microscope de 75 x 25 mm et les pinces/racks de coloration, ainsi qu'un support Arducam angulé pour surveiller la prise. |

<div align="center">

<a href="community/histology-slide-gripper/README.md"><img src="../../../community/histology-slide-gripper/assets/slide-gripper-single-slide.jpg" alt="Histology slide gripper mod holding a microscope slide" width="400"></a>

*Histologie Slide Gripper mod  ⁇  cliquez pour la description complète, les fichiers CAD et la démonstration*

</div>

---

<a id="-star-history"></a>
## ⭐ Historique des étoiles

[![Historique des étoiles](https://api.star-history.com/svg?repos=roboninecom/so-arm100-101-parallel-gripper&type=Date&legend=top-left)](https://www.star-history.com/?repos=roboninecom%2Fso-arm100-101-parallel-gripper&type=date&legend=top-left)

---

<a id="-contributing"></a>
## ⁇  Contribution

Les contributions sont les bienvenues ! N'hésitez pas à:
- ⁇  Rapporter les bugs et les problèmes
- ⁇  Suggérer de nouvelles fonctionnalités
- ⁇  Soumettre des demandes de retrait
- ⁇  Améliorer la documentation

---

<a id="-license"></a>
## ⁇  Licence

Droit d'auteur (c) 2025 Robonine. Ce projet est multilicencé  ⁇  différents types de
le matériel porte différentes licences:

| Matériel | Licence |
|---|---|
| Des conceptions matérielles  ⁇ `models/`, CAD communautaire, maillage de grippe | [CERN-OHL-P-2.0](../../../HARDWARE-LICENSE.txt) |
| Software  ⁇ `software/`, `examples/`, `simulation/`, code de simulation en `community/` | [Apache-2.0](../../../SOFTWARE-LICENSE.txt) |
| Documentation et images  ⁇ `docs/`, `assets/`, tous `README.md` | [CC BY 4.0](../../../DOCS-LICENSE.txt) |

Vous voyez ? [`LICENSING.md`](LICENSING.md) pour la carte de fichier par fichier exacte et
[`REUSE.toml`](../../../REUSE.toml) pour la version lisible par machine.

**Tout n' est pas ici. RobonineC'est le travail.** Les SO-ARM101 Les mailles de bras sont dérivées
à partir [TheRobotStudioLe projet en amont](https://github.com/TheRobotStudio/SO-ARM100)
et rester Apache-2.0; la collecte de diapositives histologique a été apportée par
[@histochemichael](https://github.com/histochemichael). Vous voyez ? [`NOTICE`](../../../NOTICE)
avant de réutiliser une maille.

Libérations jusqu'à et y compris `v0.3.1` ont été publiés sous la GPL-3.0 et restent
disponible en vertu de ces conditions  ⁇  voir [`RELICENSING.md`](RELICENSING.md).

---

<a id="-links"></a>
## ⁇  Liens

- [Feetech STS3215 Servo](https://www.feetechrc.com/525603.html)
- [STServo Python SDK](https://github.com/FEETECH-RC/STServo_SDK_Python)

---

<a id="-engineering-team"></a>
## ⁇  Équipe d'ingénierie

| Nom | Rôle | Contacts |
|------|------|---------|
| **Boris Kotov** | Ingénieur logiciel | [Télégramme](https://t.me/bkotov) |
| **Alan Subin** | Ingénieur de conception | [Résultats](https://www.linkedin.com/in/alan-subin/) |

---

<div align="center">

**Construit pour la communauté robotique par [Robonine](https://robonine.com)** 🤖

**Des questions ? On est là pour aider !**
⁇  E-mail: [bonjour@robonine.com](mailto:hello@robonine.com)

</div>
<!-- /translated-content -->

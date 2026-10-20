<!-- translation-navigation -->
[English](../../../en/community/histology-slide-gripper/README.md) · [Русский](../../../ru/community/histology-slide-gripper/README.md) · [Español](../../../es/community/histology-slide-gripper/README.md) · [Français](README.md) · [Deutsch](../../../de/community/histology-slide-gripper/README.md) · [Português (Brasil)](../../../pt-BR/community/histology-slide-gripper/README.md) · [简体中文](../../../zh-CN/community/histology-slide-gripper/README.md) · [日本語](../../../ja/community/histology-slide-gripper/README.md) · [हिन्दी](../../../hi/community/histology-slide-gripper/README.md) · [العربية](../../../ar/community/histology-slide-gripper/README.md)

[Source anglaise](../../../../../community/histology-slide-gripper/README.md)

[Français](../../README.md)

> Traduction automatique intégrale, pas encore relue par des locuteurs natifs. Images, code, CAO et PDF originaux sont partagés. En cas de doute, consultez la source anglaise.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="histology-slide-gripper-community-mod"></a>
# Histologie Gripper à diapositives (mod communitaire)

Une variante communautaire de la SO-ARM100/101 Gripper parallèle [Michael Viacheslavov](https://github.com/histochemichael), adapté à l'automatisation histologique et histotechnologique: prise en charge douce des diapositives microscopiques standard 75 x 25 mm, des plongeurs/racks de colorisation des diapositives et une vue d'écran de la prise.

<div align="center">

![Démo d'attraction de glisserie histologie](../../../../../community/histology-slide-gripper/assets/histology-slide-gripper-demo.gif)

*SO-ARM100/101 une poignée parallèle utilisant des pinces personnalisées pour manipuler les diapositives du microscope et un plongeur/rack de coloration.*

</div>

<a id="what-changed-vs-the-base-gripper"></a>
## Qu'est-ce qui a changé par rapport à la base gripper

| Ajout | Définition |
|----------|-------------|
| Clampes à diapositives au microscope | La géométrie de la clampure longue et plate prend en charge le ramassage direct des diapositives microscopiques standard 75 x 25 mm. |
| Maniabilité du rack de glissade/de la plongée | L'écart entre les pinces et les extrémités de la clampure interagit avec des plongeurs/racks de colorisage de diapositives comme le plongeur de colorisage de diapositives Medicus Health lié ci-dessous. |
| Titule d'Arducam à angle | Un support imprimable vise une caméra USB à fermeture globale Arducam sur les mâchoires de la prise pour surveiller de près le ramassage des diapositives et du rack. |
| L'ensemble complet du CAD | Un assemblage STL imprimable complet et un assemblage STEP éditable sont en [`cad/`](../../../../../community/histology-slide-gripper/cad). |

<a id="gallery"></a>
## Galerie

<div align="center">

| Remplacement à diapositive unique | Déplacement de plâtre/de rack | Vue du support Arducam |
|:-:|:-:|:-:|
| ![Clamp tenant une diapositive au microscope](../../../../../community/histology-slide-gripper/assets/slide-gripper-single-slide.jpg) | ![Clampe alignée avec la plongeuse de colorisation des diapositives](../../../../../community/histology-slide-gripper/assets/slide-gripper-staining-dipper.jpg) | ![Titule d'arducam au-dessus des mâchoires de la prise](../../../../../community/histology-slide-gripper/assets/arducam-holder-front.jpg) |

| Vue avant | Géométrie de la broche | Assemblage isométrique |
|:-:|:-:|:-:|
| <img src="../../../../../community/histology-slide-gripper/assets/parallel-microscope-gripper-front.png" alt="Front CAD view of the microscope slide gripper mod" width="250"> | <img src="../../../../../community/histology-slide-gripper/assets/parallel-microscope-gripper-side.png" alt="Angled CAD view showing the microscope slide jaw geometry" width="250"> | <img src="../../../../../community/histology-slide-gripper/assets/parallel-microscope-gripper-isometric.png" alt="Isometric CAD view of the full microscope slide gripper assembly" width="250"> |

</div>

<a id="cad-files"></a>
## Fichiers CAD

| Fichier | Formatation | Utilisation |
|------|--------|-----|
| [`cad/the-parallel-microscope-slide-gripper.stl`](../../../../../community/histology-slide-gripper/cad/the-parallel-microscope-slide-gripper.stl) | LTS | Montage intégral imprimable pour le mod de prise à diapositive du microscope. |
| [`cad/the-parallel-microscope-slide-gripper.step`](../../../../../community/histology-slide-gripper/cad/the-parallel-microscope-slide-gripper.step) | Étapes | Source CAD éditable pour l'ensemble intégral. |

<a id="add-on-bill-of-materials"></a>
## Liste complémentaire des matériaux

Ces éléments sont spécifiques au flux de travail des toboggans et du rack et ne font pas partie de la prise de base [BOM](../../docs/bom.md).

| Components | Qty | Notes | Le lien |
|-----------|:---:|-------|------|
| L'appareil photo USB à fermeture globale mono 100 fps, OV9281 | 1 | Caméra utilisée avec le support angulaire pour regarder les toboggans et les racks près des mâchoires. | [Amazon Royaume-Uni](https://www.amazon.co.uk/Arducam-Shutter-Distortion-Computer-Raspberry/dp/B0FXWWF55X) |
| Démolisseuse de plâtre en plastique avec poignée | 1+ | Cible de colorisation de référence pour la plongée/rack; conçue pour les diapositives standard 75 x 25 mm. | [Santé médicale](https://www.medicus-health.com/slide-staining-dipper.html) |
| Assemblage d'adhésifs de diapositives parallèles au microscope | 1 | Impression `the-parallel-microscope-slide-gripper.stl`; Le fichier STEP est inclus pour les modifications. | [`cad/`](../../../../../community/histology-slide-gripper/cad) |

<a id="mujoco-simulation"></a>
## MuJoCo Simulation

<div align="center">

![SO-ARM101 l'accélérateur de glissage en cours d'exécution MuJoCo](../../../../../community/histology-slide-gripper/mujoco/mujoco_simulation_preview.png)

*SO-ARM101 avec la poignée de glissement histologique montée et allumée MuJoCo.*

</div>

Une personne indépendante MuJoCo Le modèle 3.4.0 est disponible en [`mujoco/`](mujoco/README.md). Il inclut la pleine SO-ARM101 un modèle, des mailles de griffe, une banque d'essai autonome de griffe, des scripts de construction et un contrôle sans tête pour la prise en charge.

De la racine du référentiel:

```bash
conda activate lerobot
cd community/histology-slide-gripper/mujoco
python -m pip install -r requirements.txt
python view.py
```

Utilisez le `sg_grip` le contrôle dans les MuJoCo l'observateur ouvre et ferme les mâchoires. Voir le [simulation README](mujoco/README.md) pour les détails du modèle, les contrôles, la validation et les instructions de reconstruction.

<a id="notes"></a>
## Notes

- Les doigts d'adhérence sont destinés à des diapositives microscopiques standard de 75 x 25 mm et à des diapositives de colorisation.
- L'assemblage garde la vue de la caméra dirigée vers les mâchoires de l'adhésif afin que la caméra puisse observer le ramassage des diapositives et du rack.
- Testez d'abord avec des diapositives non critiques et ajustez le matériau d'impression, la force de remplissage et l'adhérence pour votre flux de travail.

<a id="links"></a>
## Les liens

- 🎥 [Démo: ramassage des diapositives et des étagères de coloration (LinkedIn)](https://www.linkedin.com/posts/michael-viacheslavov_histology-histotechnology-robotics-ugcPost-7482570199859240960-Gqpw/)
<!-- /translated-content -->

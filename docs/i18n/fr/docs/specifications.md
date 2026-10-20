<!-- translation-navigation -->
[English](../../en/docs/specifications.md) · [Русский](../../ru/docs/specifications.md) · [Español](../../es/docs/specifications.md) · [Français](specifications.md) · [Deutsch](../../de/docs/specifications.md) · [Português (Brasil)](../../pt-BR/docs/specifications.md) · [简体中文](../../zh-CN/docs/specifications.md) · [日本語](../../ja/docs/specifications.md) · [हिन्दी](../../hi/docs/specifications.md) · [العربية](../../ar/docs/specifications.md)

[Source anglaise](../../../specifications.md)

[Français](../README.md)

> Traduction automatique intégrale, pas encore relue par des locuteurs natifs. Images, code, CAO et PDF originaux sont partagés. En cas de doute, consultez la source anglaise.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="so-arm-100101-parallel-follower-gripper"></a>
# SO ARM 100/101 Gripper parallèle à suivi

<a id="overview"></a>
## Vue d'ensemble

Légèreté de l'effet final imprimé en 3D conçu par: **Robonine** pour la plateforme robotique télopératrice open source SO ARM 100/101. Le mécanisme fournit un mouvement parallèle fiable de la mâchoire et une force d'attraction suffisante pour un large éventail d'applications pédagogiques et expérimentales.

![Garde de suivi montée sur SO-ARM100](../../../../assets/images/specification/07-gripper-on-so-arm100.jpg)

*Garde de suivi montée sur SO-ARM100 bras robot*

<a id="key-features"></a>
## Caractéristiques clés

- Conception open source
- Coût BOM pour une prise: ~$62
- Peut être imprimé pendant un cycle sur une imprimante 3D FDM de qualité consommateur
- Compatible avec les caméras vidéo populaires:
  - Orbbec Gémeaux 2
  - RealSense D405, D435/D435i, D455
  - GC2093 Module de caméra USB à 2 MP
  - Caméra USB IMX335 de 5 MP

---

<a id="dimensions"></a>
## Dimensions

<a id="3d-overview"></a>
### Vue d'ensemble en 3D

![Dimensions de la griffe  ⁇  vue isométrique](../../../../assets/images/specification/08-gripper-dimensions-3d.png)

*Vue isométrique montrant les dimensions globales:128 × 109 × 130.5mm, coup complet84le*

| Dimension | La valeur |
|-----------|-------|
| Largeur | 128 mm |
| Profondeur | 130.5le |
| La hauteur | 109 mm |
| Un coup complet | 84 mm |

---

<a id="mounting-interface"></a>
## Interface de montage

![Dimensions d'interface de montage](../../../../assets/images/specification/03-mounting-interface.jpg)

*Flanche de montage avec motif trou pour l'attachement du bras robot*

| Caractéristiques | Dimension |
|---------|-----------|
| Diamètre de la flange de montage | Ø 20 mm |
| Bourses au centre | Ø7 mm |
| Des trous de montage | 4x Ø3.2le |

---

<a id="gripper-parameters"></a>
## Paramètres de la pince

| Paramètre | Pince du bras suiveur |
|-----------|------------------|
| Masse de l'assemblage (PLA, 30% de remplissage) | 170 g |
| Force d'attraction maximale | 120 N |
| Vitesse de prise maximale | 14 mm/s |
| Un coup complet | 84 mm |
| Répétabilité | 0.5le |
| DOF | 1 |

---

<a id="technical-specifications"></a>
## Spécifications techniques

<a id="materials--construction"></a>
### Matériaux et construction

| Components | Spécifications |
|-----------|---------------|
| Matériau primaire | PETG / PLA |
| Transmission | Réservoir et pionniers |
| Les guides | Tubes ronds en aluminium/carbone (Ø6 mm) |
| Chauffeur | Feetech actionneur de servo STS3215 |

<a id="servo-parameters-feetech-sts3215"></a>
### Paramètres servo (Feetech STS3215)

| Paramètre | La valeur |
|-----------|-------|
| Range de tension d'exploitation | 12V |
| Vitesse (pas de charge) | 45 tours à la minute |
| courant courant (pas de charge) | 180 mA |
| Le couple d'arrêt (à verrouillé) | 30 kg·cm |
| Courant d'arrêt (à verrouillage) | 2.7 A |
| Courant par défaut (à l'arrêt) | 30 mA |
| Couple nominal | 10 kg·cm |
| Courant nommé | 900 mA |
| Résistance du terminal | 1 Ω |
| Température de fonctionnement | -20°C ~ 60°C |
| Type de codeur | Magnétique absolue à 12 bits |
| Protocole de contrôle | RS485/TTL jusqu'à 1 Mbps |
| Protection électronique | Contre une tension élevée, un courant, une charge et une température élevées |

---

<a id="camera-compatibility"></a>
## Compatibilité avec les appareils photo

La prise Follower est compatible avec diverses caméras via un support de caméra interchangeable.

![Différentes caméras montées sur la prise](../../../../assets/images/specification/09-camera-types.png)

*Différentes caméras montées sur la prise (de gauche à droite): RealSense, module de caméra USB, Orbbec Gémeaux 2*

<a id="supported-cameras"></a>
### Caméras prises en charge

| Une caméra | Type | Notes |
|--------|------|-------|
| L'équipement335 5USB MP | RGB | Compact et peu coûteux |
| GC2093 USB de 2 MP | RGB | Option budgétaire |
| Orbbec Gémeaux 2 | RGB-D | Détection de profondeur |
| RealSense D405 | RGB-D | Profondeur à courte portée |
| RealSense D435/D435i | RGB-D | Objectif général |
| RealSense D455 | RGB-D | Profondeur à longue portée |

---

<a id="supplied-resources"></a>
## Les ressources fournies

- Ensemble complet de fichiers STL pour l'impression 3D
- Guide d'assemblage
- Des dessins avec des dimensions de montage
- Fichier URDF pour les simulateurs robotiques

---

<a id="integration"></a>
## L'intégration

La prise peut être intégrée indépendamment à de nombreux systèmes robotiques grâce à son installation pratique et simple via la flange standard de montage.

<a id="mounting-requirements"></a>
### Des exigences croissantes

- 4 fois vis M3 pour la fixation de la flange
- Compatible avec SO-ARM100/101 bras robot
- Plaques d'adaptateur personnalisées disponibles pour les autres bras de robot

<a id="communication"></a>
### Communiqué

- Connexion en série via TTL ou RS485
- Taux de baud: jusqu'à 1 Mbps
- Protocole: Feetech Protocole STS

---

<a id="product-specification-documents"></a>
## Documents de spécifications du produit

- [Spécification du produit de la colle parallèle (PDF)](../../../Parallel%20gripper%20by%20Robo9.pdf) ⁇  Spécification complète du produit pour la poignée parallèle de Robo9
- [SO-ARM101 Spécification du produit (PDF)](../../../SO-ARM101%20by%20Robo9.pdf) ⁇  Spécification complète du produit SO-ARM101 Arm robot par Robo9

---

*Spécifications susceptibles de changer en fonction de la mise en œuvre et des essais réels*
<!-- /translated-content -->

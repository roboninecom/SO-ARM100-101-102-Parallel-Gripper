<!-- translation-navigation -->
[English](../../en/models/README.md) · [Русский](../../ru/models/README.md) · [Español](../../es/models/README.md) · [Français](README.md) · [Deutsch](../../de/models/README.md) · [Português (Brasil)](../../pt-BR/models/README.md) · [简体中文](../../zh-CN/models/README.md) · [日本語](../../ja/models/README.md) · [हिन्दी](../../hi/models/README.md) · [العربية](../../ar/models/README.md)

[Source anglaise](../../../../models/README.md)

[Français](../README.md)

> Traduction automatique intégrale, pas encore relue par des locuteurs natifs. Images, code, CAO et PDF originaux sont partagés. En cas de doute, consultez la source anglaise.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="3d-models"></a>
# Modèles 3D

Ce dossier contient des fichiers STL pour l'assemblage de Gripper Follower.

<a id="complete-assembly"></a>
## Assemblée complète

| Fichier | Définition | Imprimantes compatibles |
|------|-------------|---------------------|
| `Follower gripper (165x165 bed size).STL` | Kit complet de pièces d'adhérence | Imprimantes dont la taille du lit est supérieure à 165 × 165 mm |

<a id="compatible-3d-printers"></a>
### Imprimantes 3D compatibles

- **Lab A1 mini** (180×180×180en mm)
- **Prusa MINI / MINI+** (180×180×180en mm)
- **Créativité Ender-2 Pro** (165×165×180mm)
- **Cobra néo** (220×220×250en mm)
- **Génie de l'artillerie** (220×220×250en mm)

*Remarque: Toute imprimante dont la taille du lit est ≥ 165 × 165 mm peut imprimer l'aperçu complet de l'assemblage.*

<a id="individual-parts"></a>
## Parties individuelles

Situé dans le `parts/` dépôt:

| Numéro de partie | Fichier | Qty | Définition |
|-------------|------|:---:|-------------|
| RB9.01.060.074 | `Camera holder.STL` | 1 | Appareil photo |
| RB9.01.060.080 | `Holder.STL` | 1 | Appareil de montage sans appareil photo |
| RB9.01.060.090 | `Camera spacer.STL` | 1 | Appareil d'écran |
| RB9.01.060.110 | `D405 holder.STL` | 1 | Garde pour la caméra D405 |
| RB9.01.062.010 | `Main frame.STL` | 1 | Cadre structural principal |
| RB9.01.062.021 (D6.0) | `Clamp.STL` | 2 | Mâchoires de la pince |
| RB9.01.062.021 (D6.1) | `Clamp.STL` | 2 | Mâchoires de la pince |
| RB9.01.062.021 (D6.2) | `Clamp.STL` | 2 | Mâchoires de la pince |
| RB9.01.062.021 (D6.3) | `Clamp.STL` | 2 | Mâchoires de la pince |
| RB9.01.062.031 | `Gear rack.STL` | 2 | Les étagères de vitesses pour le mouvement linéaire |
| RB9.01.062.040 | `Gear.STL` | 1 | Engrenage moteur |
| RB9.01.062.100 | `Nail.STL` | 2 | Les ongles |

<a id="print-settings"></a>
## Paramètres d'impression

| Paramètre | Value recommandée |
|-----------|-------------------|
| Matériel | PLA / PETG |
| La hauteur de la couche | 0.2à l'aide de0.15mm pour les engrenages) |
| Remplissage | 20% (30% pour les engrenages) |
| Apports | Au besoin |
| Des murs | 3-4les périmètres |

<a id="notes"></a>
## Notes

- Les engrenages d'impression avec une charge plus élevée (100%) pour une meilleure résistance
- Le cadre principal peut nécessiter des supports selon l'orientation
- Post-traitement: le ponçage léger peut être nécessaire pour l'ajustement des roulements
- Les pièces individuelles peuvent être imprimées sur n'importe quelle imprimante FDM standard

<a id="better-rods-fit"></a>
## Des bâtons mieux adaptés
![Plaque d'essai](../../../../assets/images/assembly/rod-test-plate.PNG)

Pour vous assurer que les barres que vous achetez s'intégrent mieux dans les pinces, vous devez utiliser une pièce d'essai. Imprimez-le et, en travaillant du plus grand trou au plus petit, sélectionnez le diamètre permettant à la tige de s'intégrer dans la pièce d'essai sans difficulté et avec un dégagement minimal. Puis imprimer des pinces avec le même diamètre de trou que celui mentionné dans le nom du fichier stl (p. ex. RB9.01.062.021 (D6.1) si vous choisissez le diamètre6.1mm).
<!-- /translated-content -->

<!-- translation-navigation -->
[English](../../en/docs/quick-start.md) · [Русский](../../ru/docs/quick-start.md) · [Español](../../es/docs/quick-start.md) · [Français](quick-start.md) · [Deutsch](../../de/docs/quick-start.md) · [Português (Brasil)](../../pt-BR/docs/quick-start.md) · [简体中文](../../zh-CN/docs/quick-start.md) · [日本語](../../ja/docs/quick-start.md) · [हिन्दी](../../hi/docs/quick-start.md) · [العربية](../../ar/docs/quick-start.md)

[Source anglaise](../../../quick-start.md)

[Français](../README.md)

> Traduction automatique intégrale, pas encore relue par des locuteurs natifs. Images, code, CAO et PDF originaux sont partagés. En cas de doute, consultez la source anglaise.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="quick-start-guide"></a>
# Un guide rapide pour commencer

Prends ton Gripper pour le suiveur SO-ARM101 Levez-vous et courez !

[![SO-ARM101 Pince parallèle](../../../../assets/images/SO%20ARM%20101%20Parallel%20Gripper%20Live.jpg)](https://youtube.com/shorts/bSyXjgNGXZk)

*Cliquez sur l'image pour [surveillez la prise en action](https://youtube.com/shorts/bSyXjgNGXZk)!*

<a id="what-youll-need"></a>
## Ce dont vous aurez besoin

<a id="hardware"></a>
### L'équipement
- [ ] Toutes les pièces imprimées en 3D (voir [Modèles 3D](../models/README.md))
- [ ] Components électroniques (voir [BOM](bom.md))
- [ ] Components mécaniques (rouges, barres, attaches)
- [ ] Outils: tournevis Phillips PH1, clés Hex M2 (H1.5) et M4 (H2.5)

<a id="software"></a>
### Logiciel
- [ ] Python 3.6+ installé
- [ ] STServo SDK téléchargé
- [ ] Les produits existants SO-ARM100/101 contrôleur, connexion USB et alimentation au bras

---

<a id="step-1-3d-print-the-parts-2-4-hours"></a>
## Étape 1: Impression 3D des pièces (2-4 heures)

1. Télécharger des fichiers STL à partir `models/parts/`
2. Imprimez avec les paramètres recommandés:
   - hauteur de la couche:0.2le
   - Remplissage: 20% (frame/clamps), 100% (engrenages)
   - Matériel: PLA ou PETG
3. Supprimer les supports

![Plaque d'essai](../../../../assets/images/assembly/rod-test-plate.PNG)

Pour vous assurer que les barres que vous achetez s'intégrent mieux dans les pinces, vous devez utiliser une pièce d'essai. Imprimez-le et, en travaillant du plus grand trou au plus petit, sélectionnez le diamètre permettant à la tige de s'intégrer dans la pièce d'essai sans difficulté et avec un dégagement minimal. Puis imprimer des pinces avec le même diamètre de trou que celui mentionné dans le nom du fichier stl (p. ex. RB9.01.062.021 (D6.1) si vous choisissez le diamètre6.1mm).

**Imprimantes 3D compatibles** (lit de 180 × 180 mm):
- Lab A1 mini
- Prusa MINI / MINI+
- Cobra néo
- Tout imprimant avec un lit ≥ 180×180 mm

**Parties à imprimer:**
- 1x Châssis principal (RB9.01.062.010)
- 2x Mâchoire (RB9.01.062.020)
- 2x Crémaillère (RB9.01.062.030)
- 1x Engrenage (RB9.01.062.040)
- 1x Support de caméra (RB9.01.060.074)
- 1x Support (RB9.01.060.080)
- 1x Entretoise de caméra (RB9.01.060.090)

---

<a id="step-2-gather-components-1-2-days-shipping"></a>
## Pas de départ2: Rassemblement des composants (1-2jour de livraison

Les pièces de commande [Résumé des matières](bom.md). Réutiliser le contrôleur de bras et l'alimentation; ceux-ci sont en dehors du coût de la prise:

| Components | Qty | Est. Coût |
|-----------|:---:|-----------|
| Feetech STS3215 servo | 1 | ~$29 |
| MF106ZZ les roulements (10x6x3 mm) | 2 | ~$2 |
| Tubes d'aluminium/carbone D6x1x125mm | 2 | ~$4 |
| Impression 3D PLA| 8 pièces | ~$12 |
| Appareils de fixation (croûtes/noix M2/M4) | divers | ~$3 |

**Coût total estimé: ~$50**

---

<a id="step-3-assembly-30-45-minutes"></a>
## Pas de départ3Assemblée (30-45minutes)

Suivez les détails [Guide d'assemblage](assembly-guide.md):


1. Insérer le câble servo
2. Utilisation Feetech Le logiciel déplace le serveur à sa position minimale (déplacez le curseur dans le logiciel vers la gauche)
3. Fixez les crémaillères aux mâchoires
4. Insérez les tiges de guidage dans les deux mâchoires
5. Installez les roulements sur le châssis principal et fixez-les avec des vis
6. Enclenchez les tiges de guidage dans le châssis
7. Écartez les mâchoires jusqu’aux positions extrêmes à gauche et à droite
8. Insérer le servo et le fixer avec des vis
9. Appliquer une caméra spacer et une caméra UVC, fixée avec des vis 4x et des noix M2 (facultatif)
10. Montage au bras robot (facultatif)

---

<a id="step-4-software-setup-10-minutes"></a>
## Étape 4: Installation du logiciel (10 minutes)

1. **Installation STServo SDK**
   ```bash
   git clone https://github.com/FEETECH-RC/STServo_SDK_Python.git
   cd STServo_SDK_Python
   cp -r STservo_sdk /path/to/your/project/
   ```

2. **Installation Python les dépendances**
   ```bash
   pip install pyserial
   ```

3. **Configurer la connexion**
   ```python
   DEVICENAME = 'COM7'  # Windows
   # DEVICENAME = '/dev/ttyUSB0'  # Linux
   STS_ID = 1  # Servo ID (use 6 if connected as gripper on SO-ARM101)
   ```

---

<a id="step-5-first-test-5-minutes"></a>
## Étape 5: Première épreuve (5 minutes)

1. **Connectez le matériel**
   - Servo à grippe → servo n°5 sur le SO-ARM101 bus de service
   - Contrôleur de bras existant → ordinateur (USB)
   - Utilisez l'alimentation du bras configurée pour les servos installés
   - Réglez l' identification servo de la prise à correspondre `STS_ID` et le garder unique dans l'autobus
   - Fermez d'autres applications de contrôle robot avant d'ouvrir le port série

2. **Exécuter un test de base**
   ```bash
   cd software/python
   python gripper_control.py
   ```

3. **Essayez les commandes de base.**
   - Entrez `45` pour ouvrir la pince
   - Entrez `-45` pour fermer la pince
   - Entrez `0` au centre
   - Appuyez sur Entrer pour sortir

---

<a id="troubleshooting"></a>
## Résolution des problèmes

<a id="connection-issues"></a>
### Problèmes de connexion
- ✅ Vérifiez le port COM dans Gestionnaire de périphériques (Windows) ou `ls /dev/ttyUSB*` (Linux)
- ✅ Vérifiez que la LED à servo-alimentation est allumée
- ✅ Essayez différents taux de baud (par défaut: 1000000)
- ✅ Vérifiez les connexions par câble

<a id="movement-issues"></a>
### Problèmes liés au mouvement
- ✅ Vérifiez l'engagement des engins avec le rack
- ✅ Vérifiez la liaison mécanique
- ✅ Veiller à ce que les roulements se déplacent librement sur les tiges
- ✅ Moniteur de température servo (maxime 60°C)

<a id="software-issues"></a>
### Problèmes liés au logiciel
- ✅ Installation STServo SDK correctement
- ✅ Vérifiez Python version (3.6+)
- ✅ Vérifiez les autorisations de port série: `sudo chmod 666 /dev/ttyUSB0` (Linux)

---

<a id="next-steps"></a>
## Les prochaines étapes

🎉 **Je vous félicite !** Votre poignée fonctionne !

Vous pouvez maintenant:
- Montage sur SO-ARM100/101 bras robot
- Intégrer avec votre logiciel de contrôle
- Ajoutez une caméra au support de la caméra
- Créer des applications personnalisées

<a id="need-help"></a>
## Vous avez besoin d'aide ?

- ⁇  Lire le [Les spécifications](specifications.md)
- ⁇  Vérifiez le [Guide d'assemblage](assembly-guide.md)
- 📄 [Spécification du produit de l'adhésif parallèle (PDF)](../../../Parallel%20gripper%20by%20Robo9.pdf)
- 📄 [SO-ARM101 Spécification du produit (PDF)](../../../SO-ARM101%20by%20Robo9.pdf)
- ⁇  Rapporter les problèmes sur GitHub

---

**Bienvenue dans la communauté des grippers parallèles !** 🤖
<!-- /translated-content -->

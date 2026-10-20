<!-- translation-navigation -->
[English](../../en/docs/assembly-guide.md) · [Русский](../../ru/docs/assembly-guide.md) · [Español](../../es/docs/assembly-guide.md) · [Français](assembly-guide.md) · [Deutsch](../../de/docs/assembly-guide.md) · [Português (Brasil)](../../pt-BR/docs/assembly-guide.md) · [简体中文](../../zh-CN/docs/assembly-guide.md) · [日本語](../../ja/docs/assembly-guide.md) · [हिन्दी](../../hi/docs/assembly-guide.md) · [العربية](../../ar/docs/assembly-guide.md)

[Source anglaise](../../../assembly-guide.md)

[Français](../README.md)

> Traduction automatique intégrale, pas encore relue par des locuteurs natifs. Images, code, CAO et PDF originaux sont partagés. En cas de doute, consultez la source anglaise.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="assembly-guide-for-follower-gripper-so-arm101"></a>
# Guide d'assemblage pour les adhérents SO-ARM101

Ce manuel fournit des instructions étape par étape pour assembler la poignée en parallèle. Suivez attentivement ces étapes pour assurer un bon fonctionnement.

<a id="required-tools"></a>
## Les outils nécessaires

- Le tournevis à tête de Phillips PH1
- Les clés Hex M2 (H1.5) et M4 (H2.5)

---

<a id="step-1-install-gear-on-servo"></a>
## Étape 1: Installez l'équipement sur le servo

![Servo avec assemblage d'équipement](../../../../assets/images/assembly/02-servo-with-gear-assembly.png)

**Components nécessaires:**
- 1x Feetech STS3215 Servo
- 1x Engrenage  (RB9.01.062.040)
- 1x disque servo (à partir du kit servo)
- 1x Servo vis de montage M3x6 (du kit servo)
- 4x Sette à vis DIN 913 M3x4

**Les instructions:**
1. Placez les engrenages pour la griffe sur le disque de servo et serrez les vis à 4 fois M3x4 dans la direction du disque de servo vers les engrenages. Veillez à ce qu'il n'y ait pas d'écart entre le disque et l'engrenage lorsque vous serrez les vis.
2. Mettez l'assemblage de vitesses sur l'arbre de sortie du servo.
3. Sécuriser avec la vis M3x6 fournie dans le servo kit.

---

<a id="step-2-servo-positioning-and-torque-limit"></a>
## Étape 2: Positionnement du serveur et limite de couple

![Positionnement en servo](../../../../assets/images/assembly/Feetech-Servo-Window.png)

**Components nécessaires:**
- 1x Plate et câbles de servo-bus en série

**Instructions pour les utilisateurs de Windows:**
1. Connectez Servo à la carte serveuse de bus série, connectez la carte au PC par USB.
2. Configurer le servo avec Feetech's **FD** (SCServo outil de débogage. C' est à source fermée
   Le logiciel Windows de Feetech et est **pas** redistribué dans ce référentiel:
   - Téléchargement officiel: <https://www.feetechrc.com/software.html> ⁇  chercher le FD /
     SCServo Débogage de l'archive. Certains téléchargements sont protégés par mot de passe;
     mot de passe Feetech.
   - Alternative multiplateforme open source:
     <https://github.com/Kotakku/FT_SCServo_Debug_Qt>

   Les étapes ci-dessous décrivent l'interface FD; l'alternative expose la même
   paramètres sous des noms similaires.
3. Choisissez votre port COM, sélectionnez BaudRate 1 000 000, appuyez sur les boutons "Ouvre" et après "Recherche".
4. Ci-dessous de la liste, sélectionnez votre serveur.
5. Vérifiez la case pour activer le couple sur le servo.
6. Mettez le curseur à gauche.

![Limite de couple maximal](../../../../assets/images/assembly/max-torque-window.png)

7. Passez la fenêtre à l'onglet "Programmer".
8. Choisissez le paramètre "Maximum Torque Limit", réglez-le à 500 ans en appuyant sur "Save".

---

<a id="step-3-clamps"></a>
## Étape 3: Clamps

![Mâchoires](../../../../assets/images/assembly/clamp+rack+nail.PNG)

**Components nécessaires:**
- 2x Mâchoires (RB9.01.062.021)
- 2x Crémaillères (RB9.01.062.031)
- 2x ongles (RB9.01.062.100)

**Les instructions:**
1. Insérez les crémaillères dans les mâchoires par le côté.
2. Insérez ensuite les clous par l’arrière.

---

<a id="step-4-rods"></a>
## Étape 4: Les bâtons

![Tiges de guidage](../../../../assets/images/assembly/rods+clamps.PNG)

**Components nécessaires:**
- 2 pièces de bois D6x125 mm

**Les instructions:**
1. Insérez les barres dans les deux pinces. Si vous avez commandé des tiges/tubes de plus de 125 mm, vous devez les couper à cette longueur.

---

<a id="step-5-install-bearings-on-main-frame"></a>
## Étape 5: Installez des roulements sur le cadre principal

![Les roulements installés sur le cadre principal](../../../../assets/images/assembly/frame+bearings.png)

**Components nécessaires:**
- 2x MF106ZZ Les roulements (10x6x3 mm)
- 2 fois M4x8 DIN 7991 vis

**Les instructions:**
1. Insérer le 2x MF106ZZ les roulements dans leurs positions désignées sur le cadre principal. La flange de roulement doit être tournée vers le haut.
2. Fixez chaque roulement avec une vis M4x8.

---

<a id="step-6-connection-of-rods-and-frame"></a>
## Étape 6: Connexion des barres et du cadre

![Connexion des tiges et du cadre principal](../../../../assets/images/assembly/frame-with-clamps.png)

**Les instructions:**
1. Enclenchez les tiges de guidage dans le châssis.
2. Écartez les mâchoires jusqu’aux positions extrêmes à gauche et à droite.

---

<a id="step-7-mount-servo-on-main-frame"></a>
## Étape 7: Montagne Servo sur le cadre principal

![Servo monté sur le cadre principal](../../../../assets/images/assembly/servo-on-frame.png)

**Components nécessaires:**
- 3x vis à tapage automatique (à partir de servo kit)

**Les instructions:**
1. Positionnez le servo sur la structure principale et alignez les trous de montage.
2. Fixez le servomoteur avec 3x vis autotaraudeuses de son kit.

---

<a id="step-8-gripper-holder-attachment"></a>
## Étape 8: Rattachement du tenant de griffe

![Appareil de fixation du support d'adhésif](../../../../assets/images/assembly/09-gripper-holder-attachment.png)

**Components nécessaires:**
- 1x Support de caméra (RB9.01.060.074) ou détenteur (RB9.01.060.080)
- 1x SO-ARM101
- 4x M3x6 Vis (à partir du servo kit)
- 4 fois vis à tapage automatique (d'un kit servo)

**Les instructions:**
1. Si vous prévoyez d'utiliser Gripper avec caméra, attachez le support de la caméra. SO-ARM101 et fixer avec des vis 4x M3x6
2. Attachez la griffe parallèle au support ou à l'appareil photo et fixez-le avec des vis automatiques 4 fois
3. Connectez le câble de l'adhésif parallèle au servo n° 5 du SO-ARM101

---

<a id="step-9-camera-attachment-optional"></a>
## Étape 9: Attache de la caméra (optionnelle)

![Appareil photo](../../../../assets/images/assembly/camera-attachment.png)

**Components nécessaires:**
- 1x caméra UVC avec des trous de montage à 28x28 mm
- 1x Entretoise de caméra (RB9.01.060.090)
- 4x M2x8 vis
- 4x M2 Noix

**Les instructions:**
1. Insérez 4x écrous M2 par l’arrière du support de caméra.
2. Placez l’entretoise et la caméra à l’avant, puis fixez avec 4x vis M2x8.

---
<a id="assembly-complete"></a>
## L'assemblée est terminée!

![Assemblées SO-ARM101 avec Follower Gripper](../../../../assets/images/specification/07-gripper-on-so-arm100.jpg)

Je vous félicite ! Votre SO-ARM101 est désormais assemblé et prêt à être utilisé.

<a id="next-steps"></a>
### Les prochaines étapes
- Opération d'essai de la poignée avant utilisation
<!-- /translated-content -->

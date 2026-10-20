<!-- translation-navigation -->
[English](../en/CONTRIBUTING.md) · [Русский](../ru/CONTRIBUTING.md) · [Español](../es/CONTRIBUTING.md) · [Français](CONTRIBUTING.md) · [Deutsch](../de/CONTRIBUTING.md) · [Português (Brasil)](../pt-BR/CONTRIBUTING.md) · [简体中文](../zh-CN/CONTRIBUTING.md) · [日本語](../ja/CONTRIBUTING.md) · [हिन्दी](../hi/CONTRIBUTING.md) · [العربية](../ar/CONTRIBUTING.md)

[Source anglaise](../../../CONTRIBUTING.md)

[Français](README.md)

> Traduction automatique intégrale, pas encore relue par des locuteurs natifs. Images, code, CAO et PDF originaux sont partagés. En cas de doute, consultez la source anglaise.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="contributing-to-open-source-parallel-gripper"></a>
# Contribution à la prise en parallèle open-source

Merci pour votre intérêt à contribuer à ce projet! Nous accueillons les contributions de la communauté robotique.

<a id="ways-to-contribute"></a>
## Façons de contribuer

<a id="-bug-reports"></a>
### ⁇  Rapports de bugs
- Utilisez le détecteur de problèmes GitHub
- Inclure des étapes de reproduction détaillées
- Fournir des informations sur le système (OS, Python version, modèle servo)
- Ajouter des journaux ou des messages d'erreur

<a id="-feature-requests"></a>
### ⁇  Les demandes de caractéristiques
- Vérifiez d'abord les problèmes existants
- Décrire clairement le cas d'utilisation
- Considérer la complexité de la mise en œuvre
- Discutez avec les responsables de l'entretien avant d'apporter des changements importants.

<a id="-code-contributions"></a>
### ⁇  Contributions au code
- Faites la fourchette
- Créer une branche de fonctionnalité
- Suivre les normes de codage
- Ajouter des essais le cas échéant
- Documentation mise à jour

<a id="-documentation"></a>
### ⁇  Documentation
- Améliorer la documentation existante
- Ajouter des exemples d'utilisation
- Créer des tutoriels ou des guides
- Correction des fautes de frappe ou des explications peu claires

<a id="-hardware-improvements"></a>
### ⁇ ️ Amélioration du matériel
- Modifications ou améliorations de conception
- Suggestions de parties alternatives
- Nouvelle compatibilité servo
- Optimisations mécaniques

<a id="development-setup"></a>
## Mise en place du développement

1. **Cloner le référentiel**
   ```bash
   git clone https://github.com/your-org/parallel-gripper.git
   cd parallel-gripper
   ```

2. **Installez les dépendances**
   ```bash
   pip install -r software/python/requirements.txt
   ```

3. **Installation STServo SDK**
   ```bash
   git clone https://github.com/FEETECH-RC/STServo_SDK_Python.git
   cp -r STServo_SDK_Python/STservo_sdk ./software/python/
   ```

<a id="coding-standards"></a>
## Normes de codage

<a id="python-code"></a>
### Python Code
- Suivez le guide de style PEP 8
- Utilisez des indications de type si nécessaire
- Ajouter des chaînes de documents à toutes les fonctions/classes
- Longueur maximale de la ligne: 88 caractères
- Utilisez des noms de variables significatifs

<a id="documentation"></a>
### Documentation
- Utilisez le format Markdown
- Inclure des exemples de codes
- Gardez votre langage clair et concis.
- Mettre à jour README si nécessaire

<a id="3d-models"></a>
### Modèles 3D
- Fournir des fichiers STL en format binaire
- Si possible, inclure les fichiers source (STEP, Fusion 360, etc.)
- Impression d'essai avant de soumettre
- Paramètres d'impression du document

<a id="pull-request-process"></a>
## Procédure de retrait des demandes

1. **Avant de commencer**
   - Vérifiez les problèmes existants et les relations publiques
   - Discutez d'abord des changements majeurs.
   - Assurez-vous que vous pouvez tester vos changements

2. **Je fais des changements**
   - Créer un nom de branche descriptif
   - Faites des engagements atomiques avec des messages clairs
   - Testez vos changements avec soin.
   - Mise à jour de la documentation au besoin

3. **Présentation des relations publiques**
   - Remplissez le modèle de relations publiques
   - Problèmes liés au lien
   - Des descriptions claires des changements
   - Inclure des informations sur les essais

4. **Processus d'examen**
   - Les commentaires des réviseurs d'adresse
   - Gardez les discussions constructives.
   - Soyez patient avec le processus d'examen

<a id="testing-guidelines"></a>
## Les lignes directrices relatives aux essais

<a id="software-testing"></a>
### Test de logiciels
- Testez la configuration de votre matériel
- Vérifiez la compatibilité entre les plateformes
- Vérifiez la gestion des erreurs
- Cas de bord d'essai

<a id="hardware-testing"></a>
### Test du matériel
- Vérifiez que les impressions 3D fonctionnent correctement
- Procédures d'assemblage des essais
- Vérifiez les tolérances mécaniques
- Valider avec différents matériaux

<a id="communication"></a>
## Communiqué

<a id="channels"></a>
### Les canaux
- Problèmes de GitHub: rapports de bugs, demandes de fonctionnalités
- Discussions sur GitHub: questions générales, idées
- Demande de retrait: révision du code, discussion technique

<a id="guidelines"></a>
### Les lignes directrices
- Soyez respectueux et constructif.
- Recherche avant de publier
- Fournir le contexte et les détails
- Aidez les autres quand c'est possible.

<a id="recognition"></a>
## Reconnaissance

Les contributeurs seront reconnus dans:
- README.md section contributeurs
- Notes de libération
- Documentation du projet

<a id="license"></a>
## Licence

Ce projet a plusieurs licences  ⁇  voir [`LICENSING.md`](LICENSING.md) Pour la carte complète.

En soumettant une contribution, vous certifiez que vous avez le droit de la soumettre,
et vous acceptez qu'il soit autorisé en vertu de la licence qui s'applique à la partie
le référentiel dans lequel il atterrit:

| Vous changez | Votre contribution est autorisée. |
|---|---|
| Le matériel / CAD | CERN-OHL-P-2.0 |
| Logiciel | Apache-2.0 |
| Documentation et images | CC BY 4.0 |

En d'autres termes, entrée = sortie: quelle que soit la licence sous laquelle un dossier est déjà soumis,
votre changement est sous la même licence.

**Matériel de tiers.** Si votre contribution comprend quelque chose que vous n'avez pas fait
créez vous-même, dites-le dans la demande de tirage afin qu'il puisse être enregistré dans
[`NOTICE`](../../../NOTICE). S' il vous plaît ne pas commettre des binaires que vous ne pouvez pas licencier  ⁇  que
inclut les outils et le firmware des fournisseurs.

**Nouveaux fichiers** doivent être couverts par: [`REUSE.toml`](../../../REUSE.toml). `reuse lint` se déplace dans
Il ne sera pas possible d'obtenir un certificat de délivrance en cas d'absence de droits d'auteur et de licence.
l'information.

<a id="questions"></a>
## Des questions ?

N'hésitez pas à ouvrir un numéro ou à entamer une discussion si vous avez des questions sur la façon de contribuer!

---

**Merci d'avoir aidé à améliorer ce projet !** 🤝
<!-- /translated-content -->

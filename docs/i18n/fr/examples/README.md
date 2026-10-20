<!-- translation-navigation -->
[English](../../en/examples/README.md) · [Русский](../../ru/examples/README.md) · [Español](../../es/examples/README.md) · [Français](README.md) · [Deutsch](../../de/examples/README.md) · [Português (Brasil)](../../pt-BR/examples/README.md) · [简体中文](../../zh-CN/examples/README.md) · [日本語](../../ja/examples/README.md) · [हिन्दी](../../hi/examples/README.md) · [العربية](../../ar/examples/README.md)

[Source anglaise](../../../../examples/README.md)

[Français](../README.md)

> Traduction automatique intégrale, pas encore relue par des locuteurs natifs. Images, code, CAO et PDF originaux sont partagés. En cas de doute, consultez la source anglaise.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="examples---parallel-gripper"></a>
# Exemples - Grippe parallèle

Ce répertoire contient un code d'exemple montrant comment utiliser la prise parallèle dans divers scénarios.

<a id="available-examples"></a>
## Exemples disponibles

<a id="basic_usagepy"></a>
### `basic_usage.py`
Démontre les opérations fondamentales de la poignée:
- Connexion à l'adhésif
- Passage à des positions spécifiques
- Informations sur l'état de lecture
- Traitement des erreurs de base

**Utilisation:**
```bash
cd examples
python basic_usage.py
```

<a id="configuration"></a>
## Configuration

Avant d'exécuter des exemples, vous devrez peut-être ajuster les paramètres de configuration:

```python
config = GripperConfig()
config.DEVICENAME = '/dev/ttyUSB0'  # Linux/Mac
# config.DEVICENAME = 'COM7'        # Windows
config.STS_ID = 1                   # Servo ID
config.BAUDRATE = 1000000          # Communication speed
```

<a id="common-issues"></a>
## Des questions courantes

<a id="connection-problems"></a>
### Problèmes de connexion
- **Les fenêtres**: Vérifiez le Gestionnaire de périphériques pour le port COM correct
- **Linux**: Veiller à ce que l'utilisateur ait accès aux ports sériels (`sudo usermod -a -G dialout $USER`)
- **macOS**Utilisation: `/dev/cu.usbserial-*` ou `/dev/tty.usbserial-*`

<a id="permission-errors"></a>
### Erreurs de permis
```bash
# Linux/macOS
sudo chmod 666 /dev/ttyUSB0
# or add user to dialout group
sudo usermod -a -G dialout $USER
```

<a id="stservo-sdk-issues"></a>
### STServo Problèmes liés au SDK
Assurez-vous que le STServo SDK est correctement installé:
1. Télécharger depuis: [STServo Python SDK](https://files.waveshare.com/wiki/Bus-Servo-Adapter-(A)/STServo_Python.zip)
2. Extraire le fichier ZIP téléchargé et copier `STservo_sdk` le dossier (avec le dossier lui-même) à `software/python/` répertoire

<a id="creating-your-own-examples"></a>
## Créer ses propres exemples

Lors de la création de nouveaux exemples:

1. **Importer le module de prise**
   ```python
   from gripper_control import ParallelGripper, GripperConfig
   ```

2. **Traitez les erreurs avec grâce.**
   ```python
   try:
       gripper = ParallelGripper()
       if not gripper.connect():
           print("Connection failed!")
           return
       # Your code here
   finally:
       gripper.disconnect()
   ```

3. **Inclure une documentation appropriée**
   - Une description claire de ce que fait l'exemple
   - Installation matérielle requise
   - Le comportement attendu

<a id="safety-notes"></a>
## Notes de sécurité

⚠️ **Des considérations importantes en matière de sécurité:**
- Surveillez toujours la température et le tirage courant
- Mettre en œuvre une gestion correcte des erreurs
- Test avec des forces faibles d'abord
- Assurer une installation mécanique appropriée
- Gardez vos doigts à l'écart des parties mobiles

<a id="contributing-examples"></a>
## Des exemples qui ont contribué

Nous accueillons de nouveaux exemples ! Je vous en prie !
- Suivre le style de code existant
- Incluez des commentaires complets
- Testez attentivement avant de soumettre
- Ajouter une entrée à ce README

---

**Heureux avec le code !** 🤖
<!-- /translated-content -->

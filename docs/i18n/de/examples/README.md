<!-- translation-navigation -->
[English](../../en/examples/README.md) · [Русский](../../ru/examples/README.md) · [Español](../../es/examples/README.md) · [Français](../../fr/examples/README.md) · [Deutsch](README.md) · [Português (Brasil)](../../pt-BR/examples/README.md) · [简体中文](../../zh-CN/examples/README.md) · [日本語](../../ja/examples/README.md) · [हिन्दी](../../hi/examples/README.md) · [العربية](../../ar/examples/README.md)

[Englische Quelle](../../../../examples/README.md)

[Deutsch](../README.md)

> Vollständige maschinelle Übersetzung, noch nicht von Muttersprachlern geprüft. Bilder, Code, CAD und Original-PDFs werden gemeinsam genutzt. Im Zweifel gilt die englische Quelle.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="examples---parallel-gripper"></a>
# Beispiele - Parallelgriffer

Dieses Verzeichnis enthält Beispielcodes, die zeigen, wie der Parallelgreifer in verschiedenen Szenarien verwendet wird.

<a id="available-examples"></a>
## Vorhandene Beispiele

<a id="basic_usagepy"></a>
### `basic_usage.py`
Beweist grundlegende Griffbetrieb:
- Anbindung an den Griff
- Übergang zu bestimmten Positionen
- Lesestatusinformationen
- Grundlegende Fehlerbearbeitung

**Verwendung:**
```bash
cd examples
python basic_usage.py
```

<a id="configuration"></a>
## Konfiguration

Bevor Sie Beispiele ausführen, müssen Sie möglicherweise die Konfigurationsparameter anpassen:

```python
config = GripperConfig()
config.DEVICENAME = '/dev/ttyUSB0'  # Linux/Mac
# config.DEVICENAME = 'COM7'        # Windows
config.STS_ID = 1                   # Servo ID
config.BAUDRATE = 1000000          # Communication speed
```

<a id="common-issues"></a>
## Häufige Fragen

<a id="connection-problems"></a>
### Verbindungsprobleme
- **Fenster**: Überprüfen Sie den Geräteverwalter nach dem richtigen COM-Port
- **Linux**: Sicherstellen, dass der Benutzer Zugriff auf serielle Ports hat (`sudo usermod -a -G dialout $USER`)
- **macOS**Verwendung: `/dev/cu.usbserial-*` oder `/dev/tty.usbserial-*`

<a id="permission-errors"></a>
### Erlaubnisfehler
```bash
# Linux/macOS
sudo chmod 666 /dev/ttyUSB0
# or add user to dialout group
sudo usermod -a -G dialout $USER
```

<a id="stservo-sdk-issues"></a>
### STServo SDK-Fragen
Stellen Sie sicher, dass STServo SDK ist ordnungsgemäß installiert:
1. Download von: [STServo Python SDK](https://files.waveshare.com/wiki/Bus-Servo-Adapter-(A)/STServo_Python.zip)
2. Extrahieren Sie die heruntergeladenen ZIP-Dateien und kopieren Sie `STservo_sdk` Folder (mit dem Ordner selbst) `software/python/` Verzeichnis

<a id="creating-your-own-examples"></a>
## Erstellen Sie eigene Beispiele

Bei der Erstellung neuer Beispiele:

1. **Importieren Sie das Griffmodul**
   ```python
   from gripper_control import ParallelGripper, GripperConfig
   ```

2. **Handeln Sie Fehler mit Anmutigkeit**
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

3. **Genauere Unterlagen enthalten**
   - Eine klare Beschreibung dessen, was das Beispiel tut
   - Erforderliche Hardware-Einstellung
   - Erwartetes Verhalten

<a id="safety-notes"></a>
## Sicherheitsanmerkungen

⚠️ **Wichtige Sicherheitsaspekte:**
- Überwachen Sie immer die Temperatur und den Strom
- Ein ordnungsgemäßes Fehlerbearbeitungssystem umsetzen
- Test mit geringen Kräften zuerst
- Sicherstellung einer ordnungsgemäßen mechanischen Einrichtung
- Halten Sie Ihre Finger von beweglichen Teilen fern

<a id="contributing-examples"></a>
## Beispiele, die dazu beitragen

Wir begrüßen neue Beispiele! Ich bitte Sie:
- Folgen Sie dem vorhandenen Code-Stil
- Umfassende Kommentare enthalten
- Gründliche Prüfung vor der Einreichung
- Hinzufügen von Eintrag zu diesem README

---

**Schön, dass du sie programmierst!** 🤖
<!-- /translated-content -->

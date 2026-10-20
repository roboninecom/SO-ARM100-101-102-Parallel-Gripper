<!-- translation-navigation -->
[English](../../en/docs/quick-start.md) · [Русский](../../ru/docs/quick-start.md) · [Español](../../es/docs/quick-start.md) · [Français](../../fr/docs/quick-start.md) · [Deutsch](quick-start.md) · [Português (Brasil)](../../pt-BR/docs/quick-start.md) · [简体中文](../../zh-CN/docs/quick-start.md) · [日本語](../../ja/docs/quick-start.md) · [हिन्दी](../../hi/docs/quick-start.md) · [العربية](../../ar/docs/quick-start.md)

[Englische Quelle](../../../quick-start.md)

[Deutsch](../README.md)

> Vollständige maschinelle Übersetzung, noch nicht von Muttersprachlern geprüft. Bilder, Code, CAD und Original-PDFs werden gemeinsam genutzt. Im Zweifel gilt die englische Quelle.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="quick-start-guide"></a>
# Schnellbeginnsanleitung

Holen Sie Ihren Follower Gripper für SO-ARM101 Auf und laufen!

[![SO-ARM101 Parallelgreifer](../../../../assets/images/SO%20ARM%20101%20Parallel%20Gripper%20Live.jpg)](https://youtube.com/shorts/bSyXjgNGXZk)

*Klicken Sie auf das Bild [Beobachten Sie den Griff in Aktion.](https://youtube.com/shorts/bSyXjgNGXZk)!*

<a id="what-youll-need"></a>
## Was Sie brauchen werden

<a id="hardware"></a>
### Hardware
- [ ] Alle 3D-gedruckten Teile (siehe [3D-Modelle](../models/README.md))
- [ ] Elektronische Komponenten (siehe [BOM](bom.md))
- [ ] Mechanische Komponenten (Lägger, Stangen, Bindungen)
- [ ] Werkzeuge: Phillips-Schraubenzieher PH1, Hex-Schlüssel M2 (H1.5) und M4 (H2.5)

<a id="software"></a>
### Software
- [ ] Python 3.6+ installiert
- [ ] STServo SDK heruntergeladen
- [ ] Serienkommunikationsschnittstelle

---

<a id="step-1-3d-print-the-parts-2-4-hours"></a>
## Schritt 1: 3D-Druck der Teile (2-4 Stunden)

1. STL-Dateien von `models/parts/`
2. Drucken mit empfohlenen Einstellungen:
   - Schichthöhe:0.2mm
   - Füllung: 20% (Rahmen/Klammern), 100% (Gänge)
   - Material: Pla oder PETG
3. Entfernen von Stützungen

![Prüfplatte](../../../../assets/images/assembly/rod-test-plate.PNG)

Um sicherzustellen, daß die Stangen, die Sie kaufen, besser in die Klemmen passen, müssen Sie ein Teststück verwenden. Drucken Sie ihn aus und wählen Sie vom größten bis zum kleinsten Loch den Durchmesser aus, der es dem Stang ermöglicht, ohne Schwierigkeiten und mit minimalem Abstand in das Prüfteil zu passen. Drucken Sie dann Klammern mit dem gleichen Lochdiameter, der im Stl-Dateinamen erwähnt wird (z.B. RB9.01.062.021 (D6.1) wenn Sie den Durchmesser wählen6.1mm).

**Kompatible 3D-Drucker** (180×180 mm + Bett):
- Bambu Lab A1 Mini
- Prusa MINI / MINI+
- Anycubic Kobra Neo
- Jeder Drucker mit einem Bett von ≥ 180×180 mm

**Teile zum Drucken:**
- 1x Hauptrahmen (RB9.01.062.010)
- 2x Klemmbacke (RB9.01.062.020)
- 2x Zahnstange (RB9.01.062.030)
- 1x Zahnrad (RB9.01.062.040)
- 1x Kamerahalter (RB9.01.060.074)
- 1x Halter (RB9.01.060.080)
- 1x Kamera-Abstandshalter (RB9.01.060.090)

---

<a id="step-2-gather-components-1-2-days-shipping"></a>
## Schritt 2: Sammeln von Komponenten (1-2 Tage Versand)

Bestellte Teile von der [Vorlage der Materialien](bom.md):

| Komponente | Qty | Ist. Kosten |
|-----------|:---:|-----------|
| Feetech STS3215 Servo | 1 | ~$29 |
| Busservo-Adapterbrett | 1 | ~$11 |
| MF106ZZ Lager (10x6x3 mm) | 2 | ~$2 |
| Aluminium/Kohlenstoffröhren D6x1x125mm | 2 | ~$4 |
| 3D-Druck PLA| 8 Teile | ~$12 |
| Fastener (M2/M4-Schrauben/Nüsse) | verschiedene | ~$3 |

**Gesamtgeschätzte Kosten: ~$62**

---

<a id="step-3-assembly-30-45-minutes"></a>
## Schritt 3: Versammlung (30-45 Minuten)

Folgen Sie den detaillierten [Versammlungsführer](assembly-guide.md):


1. Einfügen von Servokabeln
2. Verwendung von Feetech Software bewegt Servo auf seine minimale Position (bewegt den Schieber in der Software nach links)
3. Befestigen Sie die Zahnstangen an den Klemmbacken
4. Führen Sie die Führungsstangen durch beide Klemmbacken
5. Setzen Sie die Lager in den Hauptrahmen ein und befestigen Sie sie mit Schrauben
6. Rasten Sie die Führungsstangen im Rahmen ein
7. Schieben Sie die Klemmbacken ganz nach links und rechts auseinander
8. Setzen Sie Servo ein und fixieren Sie es mit Schrauben
9. Kamera-Spacer und UVC-Kamera befestigen, mit 4x Schrauben und M2 Nüssen (optional)
10. Montage auf Roboterarm (optional)

---

<a id="step-4-software-setup-10-minutes"></a>
## Schritt 4: Einrichtung der Software (10 Minuten)

1. **Installation STServo SDK**
   ```bash
   git clone https://github.com/FEETECH-RC/STServo_SDK_Python.git
   cd STServo_SDK_Python
   cp -r STservo_sdk /path/to/your/project/
   ```

2. **Installation Python Abhängigkeiten**
   ```bash
   pip install pyserial
   ```

3. **Konfiguration der Verbindung**
   ```python
   DEVICENAME = 'COM7'  # Windows
   # DEVICENAME = '/dev/ttyUSB0'  # Linux
   STS_ID = 1  # Servo ID (use 6 if connected as gripper on SO-ARM101)
   ```

---

<a id="step-5-first-test-5-minutes"></a>
## Schritt 5: Erster Test (5 Minuten)

1. **Verknüpfen von Hardware**
   - Servo → Busservo-Adapter
   - Busadapter → Computer (USB)
   - Stromversorgung (6-12 V, min 3A)

2. **Ausführen der Grundprüfung**
   ```bash
   cd software/python
   python gripper_control.py
   ```

3. **Versuchen Sie die Grundbefehle .**
   - Geben Sie ein . `45` zum Öffnen des Greifers
   - Geben Sie ein . `-45` zum Schließen des Greifers
   - Geben Sie ein . `0` Zentrum
   - Drücken Sie auf Eingabe , um auszugehen

---

<a id="troubleshooting"></a>
## Fehlerbehebung

<a id="connection-issues"></a>
### Verbindungsprobleme
- ✅ Überprüfen Sie den COM-Anschluss im Geräteverwalter (Windows) oder `ls /dev/ttyUSB*` (Linux)
- ✅ Überprüfen Sie, ob die Servo-LED eingeschaltet ist
- ✅ Versuchen Sie verschiedene Baudraten (Standard: 1000000)
- ✅ Überprüfen Sie Kabelverbindungen

<a id="movement-issues"></a>
### Bewegungsprobleme
- ✅ Überprüfen Sie die Verbindung von Geräten mit dem Rack
- ✅ Überprüfen Sie nach mechanischer Bindung
- ✅ Stellen Sie sicher, dass sich die Lager frei auf den Stangen bewegen
- ✅ Servo-Temperatur überwachen (maximal 60°C)

<a id="software-issues"></a>
### Softwareprobleme
- ✅ Installieren STServo SDK richtig
- ✅ Überprüfen Python Version (3.6+)
- ✅ Überprüfen Sie die seriellen Portberechtigungen: `sudo chmod 666 /dev/ttyUSB0` (Linux)

---

<a id="next-steps"></a>
## Nähere Schritte

🎉 **Ich gratuliere Ihnen!** Dein Griff funktioniert!

Jetzt kannst du:
- Auf dem Berg SO-ARM100/101 Roboterarm
- Integration mit Ihrer Steuerungssoftware
- Fügen Sie eine Kamera zum Kamerahalter hinzu
- Erstellen von benutzerdefinierten Anwendungen

<a id="need-help"></a>
## Brauchen Sie Hilfe?

- ⁇  Lesen Sie [Spezifikationen](specifications.md)
- ⁇  Überprüfen Sie [Versammlungsführer](assembly-guide.md)
- 📄 [Spezifikation des Parallelgripper-Produkts (PDF)](../../../Parallel%20gripper%20by%20Robo9.pdf)
- 📄 [SO-ARM101 Spezifikation des Produkts (PDF)](../../../SO-ARM101%20by%20Robo9.pdf)
- ⁇  Berichte über Probleme auf GitHub

---

**Willkommen in der Parallel-Gripper-Community!** 🤖
<!-- /translated-content -->

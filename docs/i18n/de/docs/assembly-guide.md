<!-- translation-navigation -->
[English](../../en/docs/assembly-guide.md) · [Русский](../../ru/docs/assembly-guide.md) · [Español](../../es/docs/assembly-guide.md) · [Français](../../fr/docs/assembly-guide.md) · [Deutsch](assembly-guide.md) · [Português (Brasil)](../../pt-BR/docs/assembly-guide.md) · [简体中文](../../zh-CN/docs/assembly-guide.md) · [日本語](../../ja/docs/assembly-guide.md) · [हिन्दी](../../hi/docs/assembly-guide.md) · [العربية](../../ar/docs/assembly-guide.md)

[Englische Quelle](../../../assembly-guide.md)

[Deutsch](../README.md)

> Vollständige maschinelle Übersetzung, noch nicht von Muttersprachlern geprüft. Bilder, Code, CAD und Original-PDFs werden gemeinsam genutzt. Im Zweifel gilt die englische Quelle.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="assembly-guide-for-follower-gripper-so-arm101"></a>
# Versammlungsführer für Follower Gripper SO-ARM101

In diesem Leitfaden sind Schritt für Schritt Anweisungen zur Montage des parallelen Griffes enthalten. Folgen Sie diesen Schritten sorgfältig, um den richtigen Betrieb zu gewährleisten.

<a id="required-tools"></a>
## Notwendige Werkzeuge

- Phillips-Schraubdreher PH1
- Hex-Schlüssel M2 (H1.5) und M4 (H2.5)

---

<a id="step-1-install-gear-on-servo"></a>
## Schritt 1: Installieren Sie Geräte auf Servo

![Servo mit Ausrüstungsanlage](../../../../assets/images/assembly/02-servo-with-gear-assembly.png)

**Benötigte Komponenten:**
- 1x Feetech STS3215 Servo
- 1x Zahnrad  (RB9.01.062.040)
- 1x Servoscheibe (aus Servosystem)
- 1x Servo-Anbauschraube M3x6 (aus Servo-Kit)
- 4x Set Schrauben DIN 913 M3x4

**Anweisungen:**
1. Setzen Sie das Gerät für den Gripper auf die Servoscheibe und schnallen Sie die 4x Set-Schrauben M3x4 in Richtung von der Servoscheibe bis zum Gerät. Stellen Sie sicher, dass keine Lücke zwischen Disk und Gear bei der Verschärfung der Schrauben erscheint.
2. Montieren Sie die Getriebe auf den Servo-Ausgangsschacht.
3. Sicher mit der Schraube M3x6, die im Servokatten zur Verfügung steht.

---

<a id="step-2-servo-positioning-and-torque-limit"></a>
## Schritt 2: Servo-Positionierung und Drehmomentgrenze

![Servo-Positionierung](../../../../assets/images/assembly/Feetech-Servo-Window.png)

**Benötigte Komponenten:**
- Bestehende SO-ARM100/101 Steuerung, Servokabel und Armstromversorgung

**Anweisungen für Windows-Benutzer:**
1. Verbinden Sie den Servo mit dem vorhandenen Armcontroller über den Servobuss und verbinden Sie den Controller mit dem PC per USB. Nutzen Sie die Armstromversorgung. Konfiguration einer einzigartigen Servo-ID vor Hinzufügung des Griffes zur Kette; Schließung anderer Robotersteuerungsanwendungen vor Öffnung des COM-Ports.
2. Konfigurieren Sie den Servo mit Feetech's **FD** (SCServo Debug) Werkzeug. Es ist geschlossener Quell
   Windows-Software von Feetech und ist **nicht** in diesem Repositorium umverteilt:
   - Offizieller Download: <https://www.feetechrc.com/software.html> ⁇  Suchen Sie nach der FD /
     SCServo Debug-Archiv. Einige Downloads sind passwortgeschützt;
     Kennwort von Feetech.
   - Open-Source-Cross-Plattform Alternative:
     <https://github.com/Kotakku/FT_SCServo_Debug_Qt>

   Die folgenden Schritte beschreiben die FD-Schnittstelle; die Alternative zeigt dieselbe
   Parameter unter ähnlichen Namen.
3. Wählen Sie Ihren COM-Port aus, wählen Sie BaudRate 1 000 000, drücken Sie die Tasten "Offnen" und nach "Suchen".
4. Aus der Liste unten wählen Sie Ihren Servo aus.
5. Überprüfen Sie die Box, um das Drehmoment auf Servo zu aktivieren.
6. Bewegen Sie den Schieber nach links.

![Maximale Drehmomentgrenze](../../../../assets/images/assembly/max-torque-window.png)

7. Schalten Sie das Fenster auf die Registerkarte "Programmieren".
8. Wählen Sie den Parameter "Maximum Drehmoment Limit" aus, setzen Sie ihn auf 500 ans und drücken Sie "Speichern".

---

<a id="step-3-clamps"></a>
## Schritt 3: Klammern

![Klemmbacken](../../../../assets/images/assembly/clamp+rack+nail.PNG)

**Benötigte Komponenten:**
- 2x Klemmbacken (RB9.01.062.021)
- 2x Zahnstangen (RB9.01.062.031)
- 2x Nägel (RB9.01.062.100)

**Anweisungen:**
1. Schieben Sie die Zahnstangen seitlich in die Klemmbacken.
2. Setzen Sie anschließend die Nägel von hinten ein.

---

<a id="step-4-rods"></a>
## Schritt 4: Stangen

![Führungsstangen](../../../../assets/images/assembly/rods+clamps.PNG)

**Benötigte Komponenten:**
- 2x Rods D6x125mm

**Anweisungen:**
1. Stecken Sie die Stäbe in beide Klammern ein. Wenn Sie Stangen/Röhren mit einer Länge von mehr als 125 mm bestellt haben, müssen Sie sie auf diese Länge schneiden.

---

<a id="step-5-install-bearings-on-main-frame"></a>
## Schritt 5: Installieren Sie Lager auf den Hauptrahmen

![Auf den Hauptrahmen installierte Lager](../../../../assets/images/assembly/frame+bearings.png)

**Benötigte Komponenten:**
- 2x MF106ZZ Lager (10x6x3 mm)
- 2x M4x8 DIN 7991 Schrauben

**Anweisungen:**
1. Fügen Sie die 2x ein MF106ZZ die Lager in ihre bezeichneten Positionen auf dem Hauptrahmen. Die Flanze sollte nach oben liegen.
2. Befestigen Sie jedes Lager mit einer Schraube M4x8.

---

<a id="step-6-connection-of-rods-and-frame"></a>
## Schritt 6: Verbindung von Stangen und Rahmen

![Verbindung von Stangen und Hauptrahmen](../../../../assets/images/assembly/frame-with-clamps.png)

**Anweisungen:**
1. Rasten Sie die Führungsstangen im Rahmen ein.
2. Schieben Sie die Klemmbacken ganz nach links und rechts auseinander.

---

<a id="step-7-mount-servo-on-main-frame"></a>
## Schritt 7: Berg Servo auf dem Hauptrahmen

![Servo auf den Hauptrahmen montiert](../../../../assets/images/assembly/servo-on-frame.png)

**Benötigte Komponenten:**
- 3x Selbstschraubschrauben (aus Servo-Kit)

**Anweisungen:**
1. Positionieren Sie den Servo auf den Hauptrahmen und richten Sie die Montagelöcher aus.
2. Befestigen Sie den Servo mit 3x selbstschneidenden Schrauben aus dem Servosatz.

---

<a id="step-8-gripper-holder-attachment"></a>
## Schritt 8: Anschluss an den Gripperhalter

![Anschließung des Gripperhalters](../../../../assets/images/assembly/09-gripper-holder-attachment.png)

**Benötigte Komponenten:**
- 1x Kamerahalter (RB9.01.060.074) oder Inhaber (RB9.01.060.080)
- 1x SO-ARM101
- 4x M3x6 Schrauben (aus Servo-Kit)
- 4x Selbstschraubschrauben (aus Servokatten)

**Anweisungen:**
1. Wenn Sie planen, Gripper mit Kamera zu verwenden, dann befestigen Sie den Kamerahalter. SO-ARM101 und mit 4x M3x6 Schrauben befestigen
2. Fügen Sie den Parallelgripper an den Kamerahalter oder -halter und befestigen Sie ihn mit 4x selbstschraubenden Schrauben
3. Verbindung von Kabel vom Parallel Gripper zum Servo Nr. 5 SO-ARM101

---

<a id="step-9-camera-attachment-optional"></a>
## Schritt 9: Kameraanbindung (optional)

![Kameraanbindung](../../../../assets/images/assembly/camera-attachment.png)

**Benötigte Komponenten:**
- 1x UVC-Kamera mit Montagelöchern von 28x28 mm
- 1x Kamera-Abstandshalter (RB9.01.060.090)
- 4x M2x8 Schrauben
- 4x M2 Nüsse

**Anweisungen:**
1. Setzen Sie 4x Muttern M2 von hinten in den Kamerahalter ein.
2. Setzen Sie Abstandshalter und Kamera von vorne ein und befestigen Sie sie mit 4x Schrauben M2x8.

---
<a id="assembly-complete"></a>
## Die Versammlung ist vollständig!

![Verbundung SO-ARM101 mit Follower Gripper](../../../../assets/images/specification/07-gripper-on-so-arm100.jpg)

Ich gratuliere Ihnen! Ihr SO-ARM101 ist nun zusammengestellt und einsatzbereit.

<a id="next-steps"></a>
### Nähere Schritte
- Prüfgreiferbetrieb vor Verwendung
<!-- /translated-content -->

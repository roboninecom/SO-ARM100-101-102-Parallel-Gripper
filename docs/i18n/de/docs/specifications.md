<!-- translation-navigation -->
[English](../../en/docs/specifications.md) · [Русский](../../ru/docs/specifications.md) · [Español](../../es/docs/specifications.md) · [Français](../../fr/docs/specifications.md) · [Deutsch](specifications.md) · [Português (Brasil)](../../pt-BR/docs/specifications.md) · [简体中文](../../zh-CN/docs/specifications.md) · [日本語](../../ja/docs/specifications.md) · [हिन्दी](../../hi/docs/specifications.md) · [العربية](../../ar/docs/specifications.md)

[Englische Quelle](../../../specifications.md)

[Deutsch](../README.md)

> Vollständige maschinelle Übersetzung, noch nicht von Muttersprachlern geprüft. Bilder, Code, CAD und Original-PDFs werden gemeinsam genutzt. Im Zweifel gilt die englische Quelle.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="so-arm-100101-parallel-follower-gripper"></a>
# SO ARM 100/101 Parallel-Follower-Gripper

<a id="overview"></a>
## Überblick

Leichtgewichtes 3D-gedrucktes Endefektor, entworfen von **Robonine** für die Open-Source-teleoperative Roboterplattform SO ARM 100/101. Der Mechanismus bietet eine zuverlässige parallele Kieferbewegung und ausreichende Fangkraft für eine breite Palette von pädagogischen und experimentellen Anwendungen.

![Anschließender Greifer SO-ARM100](../../../../assets/images/specification/07-gripper-on-so-arm100.jpg)

*Anschließender Greifer SO-ARM100 Roboterarm*

<a id="key-features"></a>
## Schlüsselmerkmale

- Open-Source-Entwurf
- BOM-Kosten für einen Gripper: ~ $50
- Kann während eines Zyklus auf einem FDM 3D-Drucker für den Verbraucher gedruckt werden
- Kompatibel mit beliebten Videokameras:
  - Orbbec Zwillinge 2
  - RealSense D405, D435/D435i, D455
  - GC2093 2MP USB-Kamera Modul
  - IMX335 5MP USB-Kamera

---

<a id="dimensions"></a>
## Dimensionen

<a id="3d-overview"></a>
### 3D-Überblick

![Gripperdimensionen  ⁇  isometrischer Ansicht](../../../../assets/images/specification/08-gripper-dimensions-3d.png)

*Isometrische Ansicht mit Gesamtdimensionen:128 × 109 × 130.5mm, Vollschlag84mm*

| Dimension | Wert |
|-----------|-------|
| Breite | 128 mm |
| Tiefe | 130.5mm |
| Höhen | 109 mm |
| Vollschlag | 84 mm |

---

<a id="mounting-interface"></a>
## Montageoberfläche

![Montage-Schnittstellendimensionen](../../../../assets/images/specification/03-mounting-interface.jpg)

*Befestigungsflanze mit Lochmuster für die Roboterarmbindung*

| Funktion | Dimension |
|---------|-----------|
| Durchmesser der Flanze für die Montage | Ø20 mm |
| Zentrale Bohrung | Ø7 mm |
| Befestigungslöcher | 4x Ø3.2mm |

---

<a id="gripper-parameters"></a>
## Greiferparameter

| Parameter | Greifer des Folgearms |
|-----------|------------------|
| Masse der Montage (PLA, 30% Füllung) | 170 g |
| Höchstgreifkraft | 120 N |
| Höchstgreifgeschwindigkeit | 14 mm/s |
| Vollschlag | 84 mm |
| Wiederholbarkeit | 0.5mm |
| DOF | 1 |

---

<a id="technical-specifications"></a>
## Technische Spezifikation

<a id="materials--construction"></a>
### Materialien & Bauarbeiten

| Komponente | Spezifikation |
|-----------|---------------|
| Hauptmaterial | PETG / PLA |
| Übertragung | Rast und Pinion |
| Führer | Runde Aluminium-/Kohlenstoffröhren (Ø6 mm) |
| Fahrer | Feetech Servo-Aktuator STS3215 |

<a id="servo-parameters-feetech-sts3215"></a>
### Servo-Parameter (Feetech STS3215)

| Parameter | Wert |
|-----------|-------|
| Betriebsspannungsbereich | 12V |
| Geschwindigkeit (ohne Belastung) | 45 RPM |
| Laufstrom (ohne Belastung) | 180 mA |
| Stallmoment (gefahren) | 30 kg cm |
| Stallstrom (verriegelt) | 2.7 A |
| Untätige Strömung (unter Stopp) | 30 mA |
| Nenndrehmoment | 10 kg·cm |
| Bewertet Strom | 900 mA |
| Terminalwiderstand | 1 Ω |
| Betriebstemperatur | -20°C ~ 60°C |
| Typ des Encoders | Absolute Magnet 12 Bit |
| Kontrollprotokoll | RS485/TTL bis zu 1 Mbps |
| Elektronischer Schutz | Gegen hohe Spannung, Strom, Last und Temperatur |

---

<a id="camera-compatibility"></a>
## Kamera Kompatibilität

Der Follower-Gripper ist über den austauschbaren Kamerahalter mit verschiedenen Kameras kompatibel.

![Verschiedene Kameras, die auf den Griff montiert sind](../../../../assets/images/specification/09-camera-types.png)

*Verschiedene Kameras, die auf den Griff montiert sind (links nach rechts): RealSense, USB-Kamera-Modul, Orbbec Zwillinge 2*

<a id="supported-cameras"></a>
### Unterstützte Kameras

| Kamera | Typ | Anmerkungen |
|--------|------|-------|
| IMX335 5MP USB | RGB | Kompakt und kostengünstig |
| GC2093 2MP USB | RGB | Haushaltsoption |
| Orbbec Zwillinge 2 | RGB-D | Tiefsensing |
| RealSense D405 | RGB-D | Nähere Tiefe |
| RealSense D435/D435i | RGB-D | Allgemeiner Zweck |
| RealSense D455 | RGB-D | Langstreckentiefe |

---

<a id="supplied-resources"></a>
## Bereitgestellte Ressourcen

- Vollständiger Satz von STL-Dateien für den 3D-Druck
- Zusammenstellungsführer
- Zeichnungen mit Montage-Dimensionen
- URDF-Datei für Robotersimulatoren

---

<a id="integration"></a>
## Integration

Der Gripper kann dank seiner bequemen und einfachen Installation über die Standardmontageflanze unabhängig in zahlreiche Robotersysteme integriert werden.

<a id="mounting-requirements"></a>
### Anstieg der Anforderungen

- 4x-M3-Schrauben für die Flangenabbindung
- Kompatibel mit SO-ARM100/101 Roboterarm
- Für andere Roboterarme verfügbare benutzerdefinierte Adapterplatten

<a id="communication"></a>
### Mitteilung

- Serienverbindung über TTL oder RS485
- Baudrate: bis zu 1 Mbps
- Protokoll: Feetech STS-Protokoll

---

<a id="product-specification-documents"></a>
## Produktbeschreibung Dokumente

- [Spezifikation des Produkts für Parallelgripper (PDF)](../../../Parallel%20gripper%20by%20Robo9.pdf) ⁇  Vollständige Produktbeschreibung für den Parallelgriff von Robo9
- [SO-ARM101 Produktbeschreibung (PDF)](../../../SO-ARM101%20by%20Robo9.pdf) ⁇  Vollständige Produktbeschreibung für die SO-ARM101 Roboterarm von Robo9

---

*Spezifikationen, die sich aufgrund der tatsächlichen Umsetzung und Prüfung ändern können*
<!-- /translated-content -->

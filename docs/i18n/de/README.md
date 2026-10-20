<!-- translation-navigation -->
[English](../en/README.md) · [Русский](../ru/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Deutsch](README.md) · [Português (Brasil)](../pt-BR/README.md) · [简体中文](../zh-CN/README.md) · [日本語](../ja/README.md) · [हिन्दी](../hi/README.md) · [العربية](../ar/README.md)

[Englische Quelle](../../../README.md)

[Deutsch](README.md)

> Vollständige maschinelle Übersetzung, noch nicht von Muttersprachlern geprüft. Bilder, Code, CAD und Original-PDFs werden gemeinsam genutzt. Im Zweifel gilt die englische Quelle.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="so-arm100101-parallel-gripper"></a>
# SO-ARM100/101 Parallelgreifer

<div align="center">

[![SO-ARM101 Parallelgreifer](../../../assets/images/SO%20ARM%20101%20Parallel%20Gripper%20Live.jpg)](https://youtube.com/shorts/bSyXjgNGXZk)

**🎥 [Pass auf den Griff in Aktion auf!](https://youtube.com/shorts/bSyXjgNGXZk)**

Eine leichte 3D-gedruckte Parallelgriffer, konstruiert von **[Robonine](https://robonine.com)** für die Open-Source SO-ARM100/101 Roboterplattform.

[![Hardware: CERN-OHL-P-2.0](https://img.shields.io/badge/Hardware-CERN--OHL--P--2.0-blue.svg)](../../../HARDWARE-LICENSE.txt)
[![Software: Apache-2.0](https://img.shields.io/badge/Software-Apache--2.0-blue.svg)](../../../SOFTWARE-LICENSE.txt)
[![Das ist alles . CC BY 4.0](https://img.shields.io/badge/Docs-CC%20BY%204.0-blue.svg)](../../../DOCS-LICENSE.txt)
[![Kosten:$70](https://img.shields.io/badge/Cost-~%2470-green.svg)](docs/bom.md)
[![Versammlung: 30 Minuten](https://img.shields.io/badge/Assembly-30%20min-orange.svg)](docs/assembly-guide.md)

---

**Fragen? Wir sind hier, um zu helfen!**
⁇  E-Mail: [Hallo@robonine.com](mailto:hello@robonine.com)

</div>

---

<a id="-key-features"></a>
## ✨ Schlüsselmerkmale

| Funktion | Beschreibung |
|---------|-------------|
| **120N Anschlagkraft** | Zuverlässiger paralleler Kiefermechanismus |
| **14 mm/s Geschwindigkeit** | Betriebsgeschwindigkeit des Grippers |
| **84mm Vollschlag** | Breite Öffnung für verschiedene Objekte |
| **0.5mm Wiederholbarkeit** | Hochpräzise Positionierung |
| **Kamera kompatibel** | Unterstützungen RealSense, Orbbec, USB-Kameras |
| **3D-Druckbar** | Alle Teile werden auf Standard-FDM-Drucker gedruckt |
| **~$62Gesamtkosten** | Erschwingliche Open-Source-Lösung |
| **Einfache Versammlung** | 30-45 Minuten mit Grundwerkzeugen |

---

<a id="-gallery"></a>
## ⁇  Gallery

<div align="center">

<a id="gripper-on-so-arm101"></a>
### Greifer an SO-ARM101

![Greifer montiert an SO-ARM101](../../../assets/images/specification/07-gripper-on-so-arm100.jpg)

*Follower-Greifer mit integrierter SO-ARM101 Roboterarm*

<a id="dimensions"></a>
### Dimensionen

![Greiferabmessungen](../../../assets/images/specification/08-gripper-dimensions-3d.png)

*128 × 109 × 130.5mm, Vollschlag84mm*

</div>

---

<a id="-specifications"></a>
## ⁇  Spezifikationen

<a id="gripper-parameters"></a>
### Greiferparameter

| Parameter | Wert |
|-----------|-------|
| Höchstgreifkraft | **120 N** |
| Höchstgreifgeschwindigkeit | **14 mm/s** |
| Vollschlag | **84 mm** |
| Wiederholbarkeit | **0.5mm** |
| Masse der Montage (PLA, 30% Füllung) | **170 g** |
| DOF | **1** |

<a id="dimensions-1"></a>
### Dimensionen

| Dimension | Wert |
|-----------|-------|
| Breite | 128 mm |
| Tiefe | 130.5mm |
| Höhen | 109 mm |

<a id="servo-parameters-feetech-sts3215"></a>
### Servo-Parameter (Feetech STS3215)

| Parameter | Wert |
|-----------|-------|
| Betriebsspannung | 12V |
| Blockiermoment | 30 kg cm |
| Geschwindigkeit (ohne Belastung) | 45 RPM |
| Verzeichner | Absolute Magnet 12 Bit |
| Protokoll | RS485/TTL bis zu 1 Mbps |
| Betriebstemperatur | -20°C ~ 60°C |

---

<a id="-camera-compatibility"></a>
## ⁇  Kamera Kompatibilität

Der Gripper unterstützt mehrere Kameras über den austauschbaren Kamerahalter:

| Kamera | Typ | Verwendungsfall |
|--------|------|----------|
| IMX335 5MP USB | RGB | Grundlegende Visionsaufgaben |
| GC2093 2MP USB | RGB | Haushaltsoption |
| Orbbec Zwillinge 2 | RGB-D | 3D-Wahrnehmung |
| RealSense D405 | RGB-D | Nähere Tiefe |
| RealSense D435/D435i | RGB-D | Allgemeiner Zweck |
| RealSense D455 | RGB-D | Langstreckentiefe |

<div align="center">

![Verschiedene Kameras, die auf den Griff montiert sind](../../../assets/images/specification/09-camera-types.png)

*RealSense, USB-Kamera-Modul, Orbbec Zwillinge 2*

</div>

---

<a id="-bill-of-materials"></a>
## ⁇  Vorlage der Materialien

**Gesamtkosten: ~ $62** ([Vollständige BOM mit Amazon-Links](docs/bom.md))

| Kategorie | Komponenten | Ist. Kosten |
|----------|------------|-----------|
| Elektronik | Feetech STS3215 Servo + Servo Bus Adapter | ~$40 |
| Lager | MF106ZZ (x2) | ~$2 |
| Aluminium/Kohlenstoffröhren | D6x1x125mm (x2) | ~$4 |
| 3D-Druck | 8 Teile (~100-150 g PLA) | ~$12 |
| Befestigungsteile | Schrauben M2/M4, Nüsse M2, Setschrauben M3 | ~$3 |

---

<a id="-quick-start"></a>
## ⁇  Schnell anfangen

<a id="1-print-the-parts-2-4-hours"></a>
### 1. Die Teile ausdrucken (2-4 Stunden)

STL-Dateien von [`models/parts/`](models/README.md). Kompatibel mit beliebten Druckern wie **Bambu Lab A1 Mini**, **Prusa MINI+**, und jeder Drucker mit einem Bett von ≥ 180 × 180 mm.

| Teil | Qty | Einstellungen |
|------|:---:|----------|
| Hauptrahmen (RB9.01.062.010) | 1 | 20% Füllung |
| Klemmbacke (RB9.01.062.020) | 2 | 20% Füllung |
| Zahnstange (RB9.01.062.030) | 2 | 100% Füllung |
| Zahnrad (RB9.01.062.040) | 1 | 100% Füllung |
| Kamerahalter (RB9.01.060.074) | 1 | 20% Füllung |
| Halter (RB9.01.060.080) | 1 | 20% Füllung |
| Kamera-Abstandshalter (RB9.01.060.090) | 1 | 20% Füllung |
| Inhaber von D405 (RB9.01.060.110) | 1 | 20% Füllung |

<a id="2-order-components-1-2-days"></a>
### 2. Bestellkomponenten (1-2 Tage)

Siehst du ? [Vorlage der Materialien](docs/bom.md) für direkte Amazon-Links.

<a id="3-assemble-30-45-minutes"></a>
### 3. Zusammenbau (30-45 Minuten)

Folgen Sie den [Versammlungsführer](docs/assembly-guide.md) mit Schritt-für-Schritt-Bilder:

1. Montieren Sie die Ausrüstung auf Servoscheibe, installieren Sie diese Einrichtung auf Servoscheibe
2. Einfügen von Servokabeln
3. Verwendung von Feetech Software bewegt Servo auf seine minimale Position (bewegt den Schieber in der Software nach links)
4. Befestigen Sie die Zahnstangen an den Klemmbacken
5. Führen Sie die Führungsstangen durch beide Klemmbacken
6. Setzen Sie die Lager in den Hauptrahmen ein und befestigen Sie sie mit Schrauben
7. Rasten Sie die Führungsstangen im Rahmen ein
8. Schieben Sie die Klemmbacken ganz nach links und rechts auseinander
9. Setzen Sie Servo ein und fixieren Sie es mit Schrauben
10. Kamera-Spacer und UVC-Kamera befestigen, mit 4x Schrauben und M2 Nüssen (optional)
11. Montage auf Roboterarm (optional)

<a id="4-software"></a>
### 4. Software

```bash
# Configure servo motor if necessary
https://lab.robonine.com/tools/robonine/feetech-bus

# Control gripper
https://lab.robonine.com/tools/robonine/control-robot
```

---

<a id="-repository-structure"></a>
## ⁇  Repository-Struktur

```
├── assets/
│   └── images/
│       ├── assembly/          # Assembly step images
│       └── specification/     # Technical drawings
├── docs/
│   ├── assembly-guide.md                # Step-by-step assembly
│   ├── bom.md                           # Bill of materials with links
│   ├── Parallel gripper by Robo9.pdf    # Gripper product specification
│   ├── quick-start.md                   # Getting started guide
│   ├── SO-ARM101 by Robo9.pdf           # SO-ARM101 product specification
│   └── specifications.md               # Technical specifications
├── models/
│   ├── parts/                                    # Individual STL files
│   └── Follower gripper (165x165 bed size).STL   # Complete assembly (165×165mm bed)
├── community/
│   └── histology-slide-gripper/   # Community variant (CAD, MuJoCo model)
├── simulation/
│   ├── README.md                  # Simulation overview
│   ├── gazebo/                    # Gazebo guide
│   ├── mujoco/                    # MuJoCo guide
│   ├── webots/                    # Webots guide
│   ├── coppeliasim/               # CoppeliaSim guide
│   ├── isaac_sim/                 # Isaac Sim guide
│   └── so_arm_101_description/    # ROS2 package (URDF, launch, Docker)
├── software/
│   └── python/                # Control software
├── examples/                  # Usage examples
├── HARDWARE-LICENSE.txt       # CERN-OHL-P-2.0 (CAD, geometry)
├── SOFTWARE-LICENSE.txt       # Apache-2.0 (code)
├── DOCS-LICENSE.txt           # CC BY 4.0 (docs, images)
├── LICENSING.md               # Which licence covers what
├── NOTICE                     # Third-party attribution
├── REUSE.toml                 # Machine-readable licence map
├── RELICENSING.md             # Record of the 2026 relicensing
└── CONTRIBUTING.md
```

---

<a id="-documentation"></a>
## ⁇  Dokumentation

| Dokument | Beschreibung |
|----------|-------------|
| [Schnellbeginnsanleitung](docs/quick-start.md) | Laufen Sie in 30 Minuten. |
| [Versammlungsführer](docs/assembly-guide.md) | Schritt für Schritt mit Bildern |
| [Gripper Assembly Guide (PDF)](../../Assembly%20Guide%20Follower%20Gripper.pdf) | Anweisungen zur Montage der Druckgreifer |
| [SO-ARM101 Versammlungsleitfaden (PDF)](../../Assembly%20Guide%20SO-ARM101.pdf) | Voll SO-ARM101 Anweisungen zur Armmontage |
| [Vorlage der Materialien](docs/bom.md) | Teilliste mit Amazon-Links |
| [Spezifikationen](docs/specifications.md) | Technische Angaben |
| [3D-Modelle](models/README.md) | Drucken von Einstellungen und Dateien |
| [Spezifikation des Parallelgripper-Produkts (PDF)](../../Parallel%20gripper%20by%20Robo9.pdf) | Spezifikation des Parallelgriffprodukts von Robo9 |
| [SO-ARM101 Spezifikation des Produkts (PDF)](../../SO-ARM101%20by%20Robo9.pdf) | SO-ARM101 Produktbeschreibung des Roboterarms von Robo9 |

---

<a id="-hardware-requirements"></a>
## ⁇  Hardwareanforderungen

<a id="electronics"></a>
### Elektronik
- 1× Feetech STS3215 Servomotor
- 1× Busservo-Adapter (Waveshare)

<a id="mechanical"></a>
### Mechanische Maschinen
- 2× MF106ZZ Lager (6×10×3 mm)
- 2 × Aluminium/Kohlenstoffröhren D6x1×125 mm

<a id="fasteners"></a>
### Befestigungsteile
- 2 × M4 × 8 DIN 7991 Schrauben
- 4x M2x8 DIN 912 Schrauben
- 4 × M2 DIN 934 Nüsse
- 4x M3x4 DIN 913 Setschrauben

<a id="tools-required"></a>
### Benötigte Werkzeuge
- Phillips-Schraubdreher (PH1)
- Hex-Schlüssel M2 (H1.5) und M4 (H2.5)

---

<a id="-simulation"></a>
## ⁇ ️ Simulation

SO-ARM101 lässt sich mit einem ROS2-Beschreibungspaket und einer einzigen parametrisierten URDF in 5 Physik-Engines simulieren. Eine Installation von ROS2 ist nicht erforderlich; Docker übernimmt alles.

<div align="center">

| Gazebo (Ignition Festung) | MuJoCo |
|:-:|:-:|
| ![SO-ARM-101 in Gazebo](../../../assets/images/simulation/gazebo/gazebo_pick_place.png) | ![SO-ARM-101 in MuJoCo](../../../assets/images/simulation/mujoco/mujoco_pick_place.png) |

</div>

| Simulator | Status | Docker |
|-----------|--------|--------|
| [Gazebo](simulation/gazebo/README.md) | Bereit ! | `docker compose run gazebo` |
| [MuJoCo](simulation/mujoco/README.md) | Bereit ! | `docker compose run mujoco` |
| [Webots](simulation/webots/README.md) | Unbeständig | `docker compose run webots` |
| [CoppeliaSim](simulation/coppeliasim/README.md) | Nicht getestet | Externe Simulatoren |
| [NVIDIA Isaac - Ja .](simulation/isaac_sim/README.md) | Nicht getestet | Externe Simulatoren |

**Schnellstart (Docker):**

```bash
cd simulation/so_arm_101_description
docker compose run gazebo    # or mujoco, webots
```

Sieh die [Simulationsführer](simulation/README.md) Für die komplette Einrichtung, Architekturdetails und Roboterkommando.

---

<a id="-community-mods"></a>
## ⁇  Mods der Gemeinschaft

Varianten des von der Gemeinschaft gebauten Grippers, die jeweils selbständig in [`community/`](../../../community):

| Mod | Autor | Beschreibung |
|-----|--------|-------------|
| [Histologie-Slide Gripper](community/histology-slide-gripper/README.md) | [Michael Viacheslavov](https://github.com/histochemichael) | Klammern für 75 x 25 mm Mikroskop-Slide und Farbdippen/Rakens sowie einen gewinkelten Arducam-Halter zur Überwachung des Greifens. |

<div align="center">

<a href="community/histology-slide-gripper/README.md"><img src="../../../community/histology-slide-gripper/assets/slide-gripper-single-slide.jpg" alt="Histology slide gripper mod holding a microscope slide" width="400"></a>

*Histologie Slide Gripper mod  ⁇  Klicken Sie auf die vollständige Beschreibung, CAD-Dateien und Demo*

</div>

---

<a id="-contributing"></a>
## ⁇  Mitwirkung

Wir begrüßen Beiträge! Bitte fühlen Sie sich frei:
- ⁇  Fehler und Probleme melden
- ⁇  Neue Funktionen vorschlagen
- ⁇  Einreichung von Pull-Anfragen
- ⁇  Verbesserung der Dokumentation

---

<a id="-license"></a>
## ⁇  Lizenz

Urheberrecht (c) 2025 Robonine. Dieses Projekt ist mit mehreren Lizenzen
Material mit unterschiedlichen Lizenzen:

| Material | Lizenz |
|---|---|
| Hardware-Designs  ⁇ `models/`, Gemeinschafts-CAD, Greifermaschen | [CERN-OHL-P-2.0](../../../HARDWARE-LICENSE.txt) |
| Software  ⁇ `software/`, `examples/`, `simulation/`, Simulationscode in `community/` | [Apache-2.0](../../../SOFTWARE-LICENSE.txt) |
| Dokumentation und Bilder  ⁇ `docs/`, `assets/`, alle `README.md` | [CC BY 4.0](../../../DOCS-LICENSE.txt) |

Siehst du ? [`LICENSING.md`](LICENSING.md) für die genaue Karte von Datei zu Datei und
[`REUSE.toml`](../../../REUSE.toml) für die maschinenlesbare Version.

**Nicht alles hier ist RobonineDas ist die Arbeit.** Die SO-ARM101 Armbänder werden abgeleitet
von [TheRobotStudioDas ist ein Vorhaben .](https://github.com/TheRobotStudio/SO-ARM100)
und bleiben Apache-2.0Der histologische Schiebergriffer wurde durch
[@histochemichael](https://github.com/histochemichael). Siehst du ? [`NOTICE`](../../../NOTICE)
vor der Wiederverwendung eines Netznetzes.

Freigabe bis einschließlich `v0.3.1` wurden unter GPL-3.0 veröffentlicht und bleiben
unter diesen Bedingungen verfügbar  ⁇  siehe [`RELICENSING.md`](RELICENSING.md).

---

<a id="-links"></a>
## ⁇  Links

- [Feetech STS3215 Servo](https://www.feetechrc.com/525603.html)
- [Waveshare Busservo-Adapter](https://www.waveshare.com/bus-servo-adapter-a.htm)
- [STServo Python SDK](https://github.com/FEETECH-RC/STServo_SDK_Python)

---

<a id="-engineering-team"></a>
## ⁇  Ingenieurteam

| Name | Rolle | Kontakt |
|------|------|---------|
| **Boris Kotov** | Software-Ingenieur | [Telegramm](https://t.me/bkotov) |
| **Alan Subin** | Konstruktionsingenieur | [Linkedin](https://www.linkedin.com/in/alan-subin/) |

---

<div align="center">

**Erbaut für die Robotik-Community von [Robonine](https://robonine.com)** 🤖

**Fragen? Wir sind hier, um zu helfen!**
⁇  E-Mail: [Hallo@robonine.com](mailto:hello@robonine.com)

</div>
<!-- /translated-content -->

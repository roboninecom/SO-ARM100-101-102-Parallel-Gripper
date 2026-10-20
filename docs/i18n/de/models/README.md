<!-- translation-navigation -->
[English](../../en/models/README.md) · [Русский](../../ru/models/README.md) · [Español](../../es/models/README.md) · [Français](../../fr/models/README.md) · [Deutsch](README.md) · [Português (Brasil)](../../pt-BR/models/README.md) · [简体中文](../../zh-CN/models/README.md) · [日本語](../../ja/models/README.md) · [हिन्दी](../../hi/models/README.md) · [العربية](../../ar/models/README.md)

[Englische Quelle](../../../../models/README.md)

[Deutsch](../README.md)

> Vollständige maschinelle Übersetzung, noch nicht von Muttersprachlern geprüft. Bilder, Code, CAD und Original-PDFs werden gemeinsam genutzt. Im Zweifel gilt die englische Quelle.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="3d-models"></a>
# 3D-Modelle

Dieser Ordner enthält STL-Dateien für die Follower Gripper Montage.

<a id="complete-assembly"></a>
## Vollständige Versammlung

| Datei | Beschreibung | Kompatible Drucker |
|------|-------------|---------------------|
| `Follower gripper (165x165 bed size).STL` | Komplettes Gripperteilspaket | Druckereien mit Bettengröße > 165×165 mm |

<a id="compatible-3d-printers"></a>
### Kompatible 3D-Drucker

- **Bambu Lab A1 Mini** (180×180×180mm)
- **Prusa MINI / MINI+** (180×180×180mm)
- **Kreativität Ender-2 Pro** (165x165x180mm)
- **Anycubic Kobra Neo** (220 x 220 x 250 mm)
- **Artillerie-Genie** (220 x 220 x 250 mm)

*Hinweis: Jeder Drucker mit einer Bettengröße von ≥ 165×165 mm kann die vollständige Montagevorführung drucken.*

<a id="individual-parts"></a>
## Einzelteile

In der `parts/` Ordner:

| Teilnummer | Datei | Qty | Beschreibung |
|-------------|------|:---:|-------------|
| RB9.01.060.074 | `Camera holder.STL` | 1 | Kamera-Behälter |
| RB9.01.060.080 | `Holder.STL` | 1 | Befestigungsstütze ohne Kamera |
| RB9.01.060.090 | `Camera spacer.STL` | 1 | Spannung für die Kamera |
| RB9.01.060.110 | `D405 holder.STL` | 1 | Halter für die Kamera D405 |
| RB9.01.062.010 | `Main frame.STL` | 1 | Hauptkonstruktionsrahmen |
| RB9.01.062.021 (D6.0) | `Clamp.STL` | 2 | Greiferbacken |
| RB9.01.062.021 (D6.1) | `Clamp.STL` | 2 | Greiferbacken |
| RB9.01.062.021 (D6.2) | `Clamp.STL` | 2 | Greiferbacken |
| RB9.01.062.021 (D6.3) | `Clamp.STL` | 2 | Greiferbacken |
| RB9.01.062.031 | `Gear rack.STL` | 2 | Geräte für lineare Bewegung |
| RB9.01.062.040 | `Gear.STL` | 1 | Antriebszahnrad |
| RB9.01.062.100 | `Nail.STL` | 2 | Nägel |

<a id="print-settings"></a>
## Druck Einstellungen

| Parameter | Empfohlener Wert |
|-----------|-------------------|
| Material | PLA / PETG |
| Schichthöhe | 0.2mm (0.15mm für Getriebe) |
| Befüllung | 20% (30% für Getriebe) |
| Unterstützungen | Nach Bedarf |
| Wände | 3-4Umgebungen |

<a id="notes"></a>
## Anmerkungen

- Druckgeräte mit höherer Füllung (100%) für eine bessere Festigkeit
- Der Hauptrahmen kann abhängig von der Orientierung Unterstützung benötigen.
- Nachbereitung: Für die Lageranlage kann eine leichte Schleifung erforderlich sein
- Einzelne Teile können auf jedem Standard-FDM-Drucker gedruckt werden

<a id="better-rods-fit"></a>
## Bessere Stangen passen
![Prüfplatte](../../../../assets/images/assembly/rod-test-plate.PNG)

Um sicherzustellen, daß die Stangen, die Sie kaufen, besser in die Klemmen passen, müssen Sie ein Teststück verwenden. Drucken Sie ihn aus und wählen Sie vom größten bis zum kleinsten Loch den Durchmesser aus, der es dem Stang ermöglicht, ohne Schwierigkeiten und mit minimalem Abstand in das Prüfteil zu passen. Drucken Sie dann Klammern mit dem gleichen Lochdiameter, der im Stl-Dateinamen erwähnt wird (z.B. RB9.01.062.021 (D6.1) wenn Sie den Durchmesser wählen6.1mm).
<!-- /translated-content -->

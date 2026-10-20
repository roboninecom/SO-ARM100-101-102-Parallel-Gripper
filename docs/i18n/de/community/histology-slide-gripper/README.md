<!-- translation-navigation -->
[English](../../../en/community/histology-slide-gripper/README.md) · [Русский](../../../ru/community/histology-slide-gripper/README.md) · [Español](../../../es/community/histology-slide-gripper/README.md) · [Français](../../../fr/community/histology-slide-gripper/README.md) · [Deutsch](README.md) · [Português (Brasil)](../../../pt-BR/community/histology-slide-gripper/README.md) · [简体中文](../../../zh-CN/community/histology-slide-gripper/README.md) · [日本語](../../../ja/community/histology-slide-gripper/README.md) · [हिन्दी](../../../hi/community/histology-slide-gripper/README.md) · [العربية](../../../ar/community/histology-slide-gripper/README.md)

[Englische Quelle](../../../../../community/histology-slide-gripper/README.md)

[Deutsch](../../README.md)

> Vollständige maschinelle Übersetzung, noch nicht von Muttersprachlern geprüft. Bilder, Code, CAD und Original-PDFs werden gemeinsam genutzt. Im Zweifel gilt die englische Quelle.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="histology-slide-gripper-community-mod"></a>
# Histologie-Slide Gripper (Gemeinschaftsmod)

Eine gemeinschaftliche Variante der SO-ARM100/101 Parallel Gripper durch [Michael Viacheslavov](https://github.com/histochemichael), für die Automatisierung der Histologie und der Histotechnologie angepasst:75 x 25mm-Mikroskopslides, Slide-Färbungen/Rakens und eine genaue Kameraansicht des Griffes.

<div align="center">

![Histologie-Demon der Schiebergriffer](../../../../../community/histology-slide-gripper/assets/histology-slide-gripper-demo.gif)

*SO-ARM100/101 Parallelgriffer mit benutzerdefinierten Klammern für die Bearbeitung von Mikroskopenrutschen und eines Färbungsstickers/Rakens.*

</div>

<a id="what-changed-vs-the-base-gripper"></a>
## Was sich verändert hat gegen den Basisgripper

| Zusatz | Beschreibung |
|----------|-------------|
| Mikroskop-Slide-Klammern | Lange, flache Klemm-Geometrie unterstützt die direkte Abholung von Standard 75 x 25 mm Mikroskopslides. |
| Handhabung von Schieberrack/Dipper | Die Klemm- und Spitzenentfernung beschäftigt die Schieberfarbungsdippe/Rakete wie die Medicus Health Schieberfarbungsdippe, die unten verknüpft sind. |
| Winkelhafter Arducam-Halter | Ein Druckhalter zielt eine Arducam-Globalshutter-USB-Kamera an den Gripperkaucheln für die Nahenüberwachung von Rutschen und Racks. |
| Vollständige Montage CAD | Eine vollständig druckbare STL und bearbeitbare STEP-Versammlung sind in [`cad/`](../../../../../community/histology-slide-gripper/cad). |

<a id="gallery"></a>
## Galerie

<div align="center">

| Einzelschifffahrzeug | Verfärbung von Dipper/Rack-Aufnahme | Anzeige des Arducam-Halter |
|:-:|:-:|:-:|
| ![Kleber, der eine Mikroskopfläche hält](../../../../../community/histology-slide-gripper/assets/slide-gripper-single-slide.jpg) | ![Klemm ausgerichtet auf die Schieberfläche](../../../../../community/histology-slide-gripper/assets/slide-gripper-staining-dipper.jpg) | ![Arducam-Halter über den Griffknochen](../../../../../community/histology-slide-gripper/assets/arducam-holder-front.jpg) |

| Ansicht vorne | Geometrie der Schlange | Isometrische Einrichtung |
|:-:|:-:|:-:|
| <img src="../../../../../community/histology-slide-gripper/assets/parallel-microscope-gripper-front.png" alt="Front CAD view of the microscope slide gripper mod" width="250"> | <img src="../../../../../community/histology-slide-gripper/assets/parallel-microscope-gripper-side.png" alt="Angled CAD view showing the microscope slide jaw geometry" width="250"> | <img src="../../../../../community/histology-slide-gripper/assets/parallel-microscope-gripper-isometric.png" alt="Isometric CAD view of the full microscope slide gripper assembly" width="250"> |

</div>

<a id="cad-files"></a>
## CAD-Dateien

| Datei | Format | Verwendung |
|------|--------|-----|
| [`cad/the-parallel-microscope-slide-gripper.stl`](../../../../../community/histology-slide-gripper/cad/the-parallel-microscope-slide-gripper.stl) | STL | Druckbare Vollmontage für den Mikroskop-Slide-Grippermodus. |
| [`cad/the-parallel-microscope-slide-gripper.step`](../../../../../community/histology-slide-gripper/cad/the-parallel-microscope-slide-gripper.step) | Schritt | Bearbeitbare CAD-Quelle für die gesamte Montage. |

<a id="add-on-bill-of-materials"></a>
## Zusätzliche Vorlage der Materialien

Diese Elemente sind spezifisch für den Schieber- und Rackworkflow und gehören nicht zum Basisgriffer. [BOM](../../docs/bom.md).

| Komponente | Qty | Anmerkungen | Link |
|-----------|:---:|-------|------|
| Arducam 100fps Mono Global Shutter USB-Kamera, OV9281 | 1 | Kamera, die mit dem gewinkelten Halter benutzt wird, um die Aufnahme von Rutschen und Racks in der Nähe der Kiefer zu beobachten. | [Amazon UK](https://www.amazon.co.uk/Arducam-Shutter-Distortion-Computer-Raspberry/dp/B0FXWWF55X) |
| Schieberfarben Plastikdippel mit Handgriff | 1+ | Referenzfärbungsziel für Dipper/Rak; für Standard-Slide von 75 x 25 mm. | [Medicus Gesundheit](https://www.medicus-health.com/slide-staining-dipper.html) |
| Parallelmikroskop-Slide-Grippermontage | 1 | Drucken `the-parallel-microscope-slide-gripper.stl`Die STEP-Datei ist für die Bearbeitung enthalten. | [`cad/`](../../../../../community/histology-slide-gripper/cad) |

<a id="mujoco-simulation"></a>
## MuJoCo Simulation

<div align="center">

![SO-ARM101 HISTOLOGische Schiebergriffer, der eingeht MuJoCo](../../../../../community/histology-slide-gripper/mujoco/mujoco_simulation_preview.png)

*SO-ARM101 mit dem HISTOLOGischen Schiebergriff montiert und eingeschaltet MuJoCo.*

</div>

Ein selbständiger MuJoCo Das Modell 3.4.0 ist in [`mujoco/`](mujoco/README.md). Es beinhaltet die vollständige SO-ARM101 Modell, Gripper-Messe, eine eigenständige Gripper-Testbank, Bauschriften und ein kopfloses Griff-und Lift-Check.

Von der Repository-Wurzel:

```bash
conda activate lerobot
cd community/histology-slide-gripper/mujoco
python -m pip install -r requirements.txt
python view.py
```

Verwenden Sie `sg_grip` Kontrolle in der MuJoCo Der Betrachter öffnet und schließt die Kiefer. Sieh die [Simulation README](mujoco/README.md) für Modelldetails, Kontrollen, Validierungs- und Wiederaufbauanleitungen.

<a id="notes"></a>
## Anmerkungen

- Die Grifffinger sind für Standard 75 x 25 mm Mikroskop-Slide und -Slide-Färbungen bestimmt.
- Die Montage hält die Kamera-Ansicht auf den Griffknochen gerichtet, damit die Kamera die Aufnahme von Rutschen und Racks beobachten kann.
- Testen Sie zuerst mit nicht-kritischen Folien und passen Sie Druckmaterial, Auffüllung und Griffkraft für Ihren Workflow an.

<a id="links"></a>
## Links

- 🎥 [Demo: Aufnahme von Schieben und Färbständen (LinkedIn)](https://www.linkedin.com/posts/michael-viacheslavov_histology-histotechnology-robotics-ugcPost-7482570199859240960-Gqpw/)
<!-- /translated-content -->

<!-- translation-navigation -->
[English](../../../../en/community/histology-slide-gripper/mujoco/README.md) · [Русский](../../../../ru/community/histology-slide-gripper/mujoco/README.md) · [Español](../../../../es/community/histology-slide-gripper/mujoco/README.md) · [Français](../../../../fr/community/histology-slide-gripper/mujoco/README.md) · [Deutsch](README.md) · [Português (Brasil)](../../../../pt-BR/community/histology-slide-gripper/mujoco/README.md) · [简体中文](../../../../zh-CN/community/histology-slide-gripper/mujoco/README.md) · [日本語](../../../../ja/community/histology-slide-gripper/mujoco/README.md) · [हिन्दी](../../../../hi/community/histology-slide-gripper/mujoco/README.md) · [العربية](../../../../ar/community/histology-slide-gripper/mujoco/README.md)

[Englische Quelle](../../../../../../community/histology-slide-gripper/mujoco/README.md)

[Deutsch](../../../README.md)

> Vollständige maschinelle Übersetzung, noch nicht von Muttersprachlern geprüft. Bilder, Code, CAD und Original-PDFs werden gemeinsam genutzt. Im Zweifel gilt die englische Quelle.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="microscope-slide-gripper-in-mujoco"></a>
# Mikroskop-Slide-Gripper MuJoCo

Die SO-ARM101 mit der histologischen Gleitparallelgriffer, aus Fusion ausgeführt und anstelle der Lager Robo9 Klemmen montiert.

mit `mujoco` 3.4.0 in der `lerobot` - Die Umwelt. - Nein . ROS 2 oder Docker ist erforderlich.

```bash
conda activate lerobot
cd community/histology-slide-gripper/mujoco
python -m pip install -r requirements.txt
python view.py                      # full arm + slide gripper
python view.py scene_gripper.xml    # gripper alone on a testbench
python test_grasp.py                # headless grasp-and-lift check -> grasp_check.png
```

<a id="mujoco-simulation-preview"></a>
## MuJoCo Simulationsvorschau

![SO-ARM101 HISTOLOGische Schiebergriffer, der eingeht MuJoCo](../../../../../../community/histology-slide-gripper/mujoco/mujoco_simulation_preview.png)

Diese Szene zeigt die SO-ARM101 mit dem histologischen Schieberparallelgriffer auf
die Handgelenk mit der gleichen MuJoCo Modell von:

```bash
conda activate lerobot
cd community/histology-slide-gripper/mujoco
python view.py
```

<a id="what-is-modelled"></a>
## Was wird modelliert

| Link | Quelle | Masse |
|---|---|---|
| `slide_gripper_base` | Hauptrahmen, STS3215, Leitstäbe, Lager, Kamerahalter, Arducam OV9281 | 0.20kg |
| `sg_jaw_right` / `sg_jaw_left` | RB9.01.062.020 Klemm + RB9.01.062.030 Rack (m0.8) | 0.035kg pro |
| `sg_pinion` | RB9.01.062.040 Ausrüstung,18 T, 0.8Modul | 0.008kg |

Kinematik aus den wie gebauten Gelenken der Fusion-Versammlung
(`Slide_Jaw_Right`, `Slide_Jaw_Left`, `Drive_Pinion`), die sich selbstverständlich sind:
die18 T / 0.8Modul-Pinion hat eine7.2Radius mm und7.2mm x4.9306Rad =
**35.5mm** Die Grenzwerte des Schieberschutzes in der CAD sind genau die Grenzwerte für den Fahrplan pro Kiefer.

<a id="control"></a>
## Kontrolle

Ein Akteur, `sg_grip`, im kommando **Meter der Kieferreise**:

| `ctrl` | Schädelreise | Durchgang zwischen den Gesichtern der Klinge |
|---|---|---|
| `0.0` | 0 mm | **84 mm** (vollständig geöffnet) |
| `0.0295` | 29.5mm | 25 mm (eine Mikroskopfläche) |
| `0.0355` | 35.5mm | **13 mm** (vollständig geschlossen) |

Beide Kiefer sind vom einzigen Schnur getrieben, also `sg_jaw_left_joint` und
`sg_pinion_joint` sind versklavt `sg_jaw_right_joint` durch `<equality>` Beschränkungen  ⁇
die Ausrüstung dreht sich sichtbar mit den Kiefern. Kommando . *Vergangenheit* das zu drängende Objekt:
auf ein 25 mm großes Objekt mit `ctrl=0.0355` gibt etwa4.7N an den Pads.

Die fünf Armgelenke behalten ihre URDF-Bezeichnungen (`base_link_to_link1` ... `link4_to_link5`).

<a id="collision-geometry"></a>
## Kollisionsgeometrie

Die Größenordnung ist: **nur visuell** (`contype=0`), weil MuJoCo Netze aus konvexen Hüllen und
Der Rumpf eines L-förmigen Kieferes füllt die Lücke, mit der du versuchst zu greifen. Der Kontakt ist
Sie werden von Schachteln auf den beiden Griffflächen jedes Kiefers (Gruppe 3, versteckt in der
Veröffentlichungen:

- `sg_pad_*` ⁇  das 30 mm-Slideblatt, CAD x 42 ⁇ 50, z 26 ⁇ 31
- `sg_mid_*` ⁇  die breitere Mitte, CAD x 42 ⁇ 58, z 18.5 ⁇ 38.5

Die TCP-Website `sg_tcp` zwischen den Klingen sitzt; `sg_camera` ist der Arducam-optische Rahmen.

<a id="files"></a>
## Dateien

- `so101_slide_gripper.xml` ⁇  Vollroboter (generiert von `build_full.py`)
- `scene_gripper.xml` ⁇  Griffe allein, mit einer AufzugsAchse zur Prüfung
- `gripper_assets.xml` / `gripper_body.xml` / `gripper_actuation.xml` ⁇  das Greifer,
  wie auch verwendet werden kann, sowohl aus Grad- als auch Radianeinheitsmodellen
- `meshes/{base,jaw_right,jaw_left,pinion}.stl` ⁇  aus Fusion in **Einbau
  Koordinaten**, so ist jeder Teil bereits an seinem richtigen Ort (keine Pro-Teil Ursprünge zu verfolgen)
- `meshes/arm/` ⁇  Armmeschen aus dem Robo9 Repo
- `build_arm.py` ⁇  Streifen aus Xacro `so_101.urdf.xacro`, lässt die Lagerklemmen fallen, kompilliert sie an MJCF
- `build_full.py` ⁇  das Greifer auf `link5`; **bearbeiten `MOUNT_POS`/`MOUNT_QUAT` Hier .**

<a id="how-the-gripper-was-located-on-the-wrist"></a>
## Wie sich der Griff am Handgelenk befand

`link5_1.stl` In der Robo9 repo ist nicht nur das Handgelenk  ⁇  es enthält die gesamte Aktie
Gripper (Rahmen, Leitstäbe, Kamera). Es ist also der Teil, den das Schiebergriffer-Design ersetzt.
`build_full.py` die Masse von0.556kg bis0.08kg.

Die Berghaltung wurde gelöst, nicht erraten: `base.stl` wurde gegen
`link5_1.stl` Über die gemeinsame Geometrie (Hauptrahmen + Leitstäbe) durch Suche nach allen
24 Achsenbereinigte Rotationen und die Punktzahl der Nächsten Nachbarentfernung. Die beste Passform ist
**+90 Grad etwa X** (CAD + Y -> Link)5+Z, CAD +Z -> Link5-Y) mit einer2.0mm Median
Die Schieberklappen hängen senkrecht auf die Spitzenklappen von Robo9,
die Fusion-Versammlung.

<a id="stability"></a>
## Stabilität

Das Modell setzt sich auf `max|qvel| = 0` und bleibt dort. Wenn du jemals sie schütteln siehst,
Erstens müssen wir die verlorenen Kontakte überprüfen (`ncon` in der Informationsplatte des Betrachters sollte 0 sein
mit dem Arm in Ruhe). Drei Dinge waren nötig:

1. **`<exclude body1="world" body2="link1_1"/>`** - die richtige Lösung. Der URDF-Einfuhrer
   Verschmelzungen `base_link` in `worldbody`, und MuJoCo Überspringt die Kollision zwischen Eltern und Kindern
   *außer* wenn der Elternteil der Weltkörper ist. Also das Basis- und Link1 Mesh
   die sich an der Schulter durchdringen und einen dauerhaften Kontakt erzeugen, der den Giegel festhält
   Antriebsgerät an seiner Grenze von +-1.5 N.m. Allein das hat sich belegt. `|qvel|` von4.78zu0.
2. `sg_pinion_joint` Armatur 1e-6 -> **1e-4**. Eine Verbindung, die von einer starken Gleichheit mit
   Fast keine Trägheitskletscher (es war mit 12 Rad/s am Höhepunkt).
3. Gleichberechtigung `solref` 0.002 -> **0.01**. Eine Zwangszeitkonstante gleich dem Zeitschritt
   ist zu steif, um sauber zu lösen; dies machte auch das Pinion land genau auf-282.5der
   anstelle von -280 Grad.

<a id="caveats"></a>
## Höhlen

- **Massen werden angenommen, nicht gemessen.** Fusion berichtet, dass jeder Körper als Stahl (die Kiefer)
  die jeweils 221 g entstehen); die oben genannten Werte sind PLA- und Hardware-Schätzungen. Wenn Sie
  die Realmaterialien in Fusion zuzuordnen, `mass=` Eigenschaften in `gripper_body.xml`.
- Inertia wird durch MuJoCo Aus der Massenform und dieser Masse, nicht aus dem Fusions-Tensor.
- Die Gelenkgrenzen, Dämpfung und Reibung des Arms werden vom URDF der
  sind nicht neu abgestimmt worden.
- **Die Schnittmassen des Arms sind auch Stahldichte.**, das gleiche Defekt wie der Griff:
  Repo-URDF-Gesamtzahlungen **2.81kg** gegen etwa 1 kg für eine echte SO-101 und `link2_to_link3`
  Bedürfnisse1.91N.m, sich gegen eine1.5N.m. Aktorengrenze, also sinkt es ab. Das ist es.
  Es verursacht kein Schütteln (siehe oben), aber es macht den Arm wie eine viel schwerere
  Die Maschine. Skalieren Sie jede Armverbindungsmasse und `diaginertia` von ~0.36die Gesamtzahl auf
  1.19kg und beseitigt die Sättigung; STS3215 und Stände näher2.9N.m als die
  Der Konservative der URDF ist 1.5.
- Der 2 mm-Ausrichtungshintergrund ist real: der "Hauptsystem_125-Follower" ist nicht identisch
  bis zum gebackenen Rahmen `link5_1.stl`.
- `sg_pinion_joint` ist kosmetisch - es trägt keine Last, weil die beiden Racks gekoppelt sind
  Sie sind direkt miteinander verbunden. Es existiert, so dass die Ausrüstung auf dem Bildschirm in die richtige Richtung dreht.

<a id="driving-it-in-the-mujoco-viewer"></a>
## Ich fahre ihn in den MuJoCo Zuschauer

Verwenden Sie **`sg_grip` Schieber in der Steuerung**. Die Schieber in der *Gemischte* Panel
Schreiben `qpos` Die Kommission hat die Möglichkeit, die
während der Pause) die Kiefer vom Schwanz desynchronisiert. Wenn Sie Run drücken, konvergiert es wieder.

<a id="re-exporting-after-a-cad-change"></a>
## Nach einer CAD-Änderung wieder exportiert

Die Ausfuhr lief durch die Fusion MCP-Verbindung:
Körper in die vier starren Verbindungen und schreibt binäre STLs in der Zusammenstellung Koordinaten
(mm). Wieder Export mit dem Fusion-Design offen, um die Maschen in
Es muss nichts anderes geändert werden, es sei denn, Sie bewegen einen Joint.
<!-- /translated-content -->

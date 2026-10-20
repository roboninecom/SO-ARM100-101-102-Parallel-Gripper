<!-- translation-navigation -->
[English](../en/CLAUDE.md) · [Русский](../ru/CLAUDE.md) · [Español](../es/CLAUDE.md) · [Français](../fr/CLAUDE.md) · [Deutsch](CLAUDE.md) · [Português (Brasil)](../pt-BR/CLAUDE.md) · [简体中文](../zh-CN/CLAUDE.md) · [日本語](../ja/CLAUDE.md) · [हिन्दी](../hi/CLAUDE.md) · [العربية](../ar/CLAUDE.md)

[Englische Quelle](../../../CLAUDE.md)

[Deutsch](README.md)

> Vollständige maschinelle Übersetzung, noch nicht von Muttersprachlern geprüft. Bilder, Code, CAD und Original-PDFs werden gemeinsam genutzt. Im Zweifel gilt die englische Quelle.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="claudemd"></a>
# CLAUDE.md

Diese Datei enthält Anleitungen für den Claude-Code (claude.ai/code) bei der Arbeit mit Code in diesem Repository.

<a id="what-this-repository-is"></a>
## Was ist dieses Repositorium?

Ein Open-Source-Hardware-Projekt: 3D gedruckte Parallelgriffer für die SO-ARM100/101 Roboterarm (von Robonine). Mehrfach lizenziert: CERN-OHL-P-2.0 für Hardware/CAD, Apache-2.0 für Software, CC BY 4.0 für Dokumente  ⁇  ist die Karte in `LICENSING.md`, die maschinenlesbare Version in `REUSE.toml`, Zuschreibung von Dritten in `NOTICE`. Neue Dateien müssen durch `REUSE.toml`; `reuse lint` Sie läuft im Vorverpflichtungsverfahren. Der größte Teil der Repos sind CAD-Modelle (`models/`), Dokumentation (`docs/`), und Bilder (`assets/`). Code lebt an zwei Orten:

- `software/python/gripper_control.py` ⁇  eigenständiges Servo-Steuerungsschreiben für die Feetech STS3215 (abhängig von der STServo SDK, der manuell geklont wird  ⁇  siehe `software/python/requirements.txt`; es ist nicht auf PyPI). `examples/basic_usage.py` Einfuhren aus diesem Land über eine `sys.path` - Das ist ein Hacker.
- `simulation/so_arm_101_description/` — a ROS2 (Humble) Beschreibungspaket, das den Arm+Gripper in 5 Physikmotoren simuliert. Hier wohnen alle Tests und die meisten Informanten.

<a id="commands"></a>
## Befehle

```bash
# Lint (what CI runs; hooks exclude STL/STEP files)
pre-commit run --all-files

# Offline tests (65 pytest tests; deps: pytest trimesh numpy mujoco pyyaml)
cd simulation/so_arm_101_description
python -m pytest test/ -v

# Single test file / single test
python -m pytest test/test_urdf_structure.py -v
python -m pytest test/test_config.py -k <name> -v

# Validate xacro/URDF XML without ROS2
python simulation/so_arm_101_description/scripts/validate_xml.py simulation/so_arm_101_description/urdf/*.xacro

# Docker (from simulation/so_arm_101_description/; no ROS2 install needed)
docker compose run test          # run pytest suite
docker compose run validate      # xacro + check_urdf for all 5 backends
docker compose run check-launch  # verify launch files parse
docker compose run gazebo        # or: mujoco, webots, rviz (need X11)
```

IC (`.github/workflows/ci.yaml`) läuft: Vorverpflichtung, XML/YAML-Bestätigung, `xacro ... sim_backend:=<backend> | check_urdf` für alle 5 Rückstände innerhalb einer `ros:humble` Ein Container und eine Suite. Eine Änderung des URDF muss für **alle** Rückstände, nicht nur die, die Sie zielen.

<a id="simulation-architecture"></a>
## Simulationsarchitektur

Eine parametrierte Roboterbeschreibung treibt jeden Simulator an:

- `urdf/so_101.urdf.xacro` ist die einzige Quelle der Wahrheit. Die xacro arg `sim_backend:=gazebo|mujoco|webots|coppeliasim|isaac` wählt `ros2_control` Plugin (über `urdf/so_101.ros2_control.xacro`) zur Zeit der Erweiterung.
- `config/controllers.yaml` identiche Verbindungen/Controller für alle Backends definiert; `launch/sim.launch.py` mit `sim:=<backend>` ist der einzige Eintrittspunkt.
- Roboter: 5-DOF-Arm + Gripper mit 2 prismatischen Klemmengelenken, wobei der linke Klemm über die rechte Spiegel spiegelt `<mimic>`.
- Die Maschen sind aufgespalten: `meshes/visual/` (Hoch-Poly) vs. `meshes/collision/` (konvexe Rümpfe, mit `scripts/generate_collision_meshes.py`).

Eine Änderung von Gelenken, Links oder Controller-Namen benötigt in der Regel koordinierte Bearbeitungen über die xacro-Dateien hinweg. `controllers.yaml`, und die Tests in `test/`.

<a id="cad-models-and-part-numbering"></a>
## CAD-Modelle und Teilnummerierung

Teile in `models/parts/` Verwendung Robonine Teilnummern (z.B. `RB9.01.062.010 Main frame.STL`). Diese Zahlen werden überall verwiesen. `README.md` (Drucktabelle), `docs/bom.md`, und `docs/assembly-guide.md` ⁇  Die Hinzufügung oder Umbenennung eines Teils bedeutet auch die Aktualisierung dieser Dokumente. STLs sind binär; Varianten kodieren Fitttoleranzen im Dateinamen (z.B. `RB9.01.062.021 (D6.1) Clamp.STL` für verschiedene Stangdiameter). Vorverpflichtungshäcke (Weißraum, EOF, Linienende) absichtlich ausschließen `.stl/.STL/.STEP` Dateien über 1 MB werden von `check-added-large-files`.

<a id="conventions"></a>
## Kongresse

- Python: flake8 mit `--max-line-length=100`, ist mit schwarzem Profil (durch das Vorverpflichtungsverfahren durchgesetzt; `software/` und `examples/` sind von Flaken ausgeschlossen8).
- Die Dokumente werden nach Design dupliziert (README fasst zusammen) bom.md, specifications.md, assembly-guide.md)  ⁇  halten sie bei Änderungen von Spezifikationen, Teilen oder Preisen gleich.
- Hinzufügen `Co-Authored-By: Claude` Die Kommission hat sich mit dem Vorschlag befaßt.
<!-- /translated-content -->

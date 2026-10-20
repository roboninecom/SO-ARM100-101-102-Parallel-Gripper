<!-- translation-navigation -->
[English](../en/CLAUDE.md) · [Русский](../ru/CLAUDE.md) · [Español](CLAUDE.md) · [Français](../fr/CLAUDE.md) · [Deutsch](../de/CLAUDE.md) · [Português (Brasil)](../pt-BR/CLAUDE.md) · [简体中文](../zh-CN/CLAUDE.md) · [日本語](../ja/CLAUDE.md) · [हिन्दी](../hi/CLAUDE.md) · [العربية](../ar/CLAUDE.md)

[Original en inglés](../../../CLAUDE.md)

[Español](README.md)

> Traducción automática completa, aún sin revisión de hablantes nativos. Las imágenes, el código, CAD y PDF originales son compartidos. En caso de duda, consulte el original en inglés.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="claudemd"></a>
# CLAUDE.md

Este archivo proporciona orientación al código claude (claude.ai/code) cuando se trabaja con el código en este repositorio.

<a id="what-this-repository-is"></a>
## ¿Qué es este repositorio ?

Un proyecto de hardware de código abierto: un agarrador paralelo impreso en 3D SO-ARM100/101 brazo robótico (por Robonine). Licenciados múltiples: CERN-OHL-P-2.0 para el hardware/CAD, Apache-2.0 para el software, CC BY 4.0 para los documentos  ⁇  el mapa está en `LICENSING.md`, la versión legible por máquina en `REUSE.toml`, atribución de terceros en `NOTICE`. Los nuevos archivos deben estar cubiertos por: `REUSE.toml`; `reuse lint` se ejecuta en precomit. La mayor parte de los repositorios son modelos CAD (`models/`), documentación (`docs/`), y las imágenes (`assets/`). El código vive en dos lugares:

- `software/python/gripper_control.py` ⁇  un guión de control servo independiente para el Feetech STS3215 (depende del STServo SDK, que se clona manualmente  ⁇  ver `software/python/requirements.txt`; no está en PyPI). `examples/basic_usage.py` las importaciones procedentes de la misma a través de un `sys.path` Hackear.
- `simulation/so_arm_101_description/` — a ROS2 Un paquete de descripción que simula el brazo+agarrador en 5 motores físicos. Aquí es donde viven todos los exámenes y la mayoría de las CI.

<a id="commands"></a>
## Los comandos

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

CI (`.github/workflows/ci.yaml`) ejecuciones: pre-compromiso, validación XML/YAML, `xacro ... sim_backend:=<backend> | check_urdf` para los 5 backends dentro de un `ros:humble` Contenedor, y la suite más pequeña. Un cambio en el URDF debe permanecer válido para **todos** retrospectivas, no sólo la que estás apuntando.

<a id="simulation-architecture"></a>
## Arquitectura de simulación

Una descripción de robot parámetrizada impulsa cada simulador:

- `urdf/so_101.urdf.xacro` Es la única fuente de verdad. El xacro arg `sim_backend:=gazebo|mujoco|webots|coppeliasim|isaac` selecciona el `ros2_control` Plugin (a través de `urdf/so_101.ros2_control.xacro`) en el momento de la expansión.
- `config/controllers.yaml` se definen juntas/controladores idénticos para todos los fondos; `launch/sim.launch.py` con `sim:=<backend>` es el único punto de entrada.
- Robot: brazo + agarre de 5 DOF con 2 juntas prismáticas de sujeción, donde la sujeción izquierda se refleja a la derecha a través de `<mimic>`.
- Las rejillas se dividen: `meshes/visual/` (alto-poly) vs `meshes/collision/` (cascos convexos, regenerados con `scripts/generate_collision_meshes.py`).

Un cambio en las juntas, enlaces o nombres de controladores normalmente requiere modificaciones coordinadas a través de los archivos xacro. `controllers.yaml`, y las pruebas en `test/`.

<a id="cad-models-and-part-numbering"></a>
## Modelos CAD y numeración de piezas

Partes en `models/parts/` el uso Robonine Números de partes (por ejemplo: `RB9.01.062.010 Main frame.STL`). Estos números se hacen referencia en todo `README.md` (tabla de impresión), `docs/bom.md`, y `docs/assembly-guide.md` ⁇  añadir o renombrar una parte significa también actualizar esos documentos. Las LST son binarias; las variantes codifican tolerancias de ajuste en el nombre del archivo (por ejemplo: `RB9.01.062.021 (D6.1) Clamp.STL` para diferentes diámetros de varillas). Los ganchos precomitados (espacio blanco, EOF, terminaciones de líneas) excluyen deliberadamente `.stl/.STL/.STEP` los archivos y archivos superiores a 1 MB son rechazados por `check-added-large-files`.

<a id="conventions"></a>
## Los congresos

- Python: flake8 con `--max-line-length=100`, esortado con perfil negro (impulsado por pre-compromiso; `software/` y `examples/` se excluyen de las hojas de flaque8).
- Los documentos se duplican por diseño (README resume bom.md, specifications.md, assembly-guide.md)  ⁇  mantenerlas consistentes al cambiar las especificaciones, piezas o precios.
- No añadir una `Co-Authored-By: Claude` línea a los compromisos.
<!-- /translated-content -->

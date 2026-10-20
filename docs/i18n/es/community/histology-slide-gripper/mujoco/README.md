<!-- translation-navigation -->
[English](../../../../en/community/histology-slide-gripper/mujoco/README.md) · [Русский](../../../../ru/community/histology-slide-gripper/mujoco/README.md) · [Español](README.md) · [Français](../../../../fr/community/histology-slide-gripper/mujoco/README.md) · [Deutsch](../../../../de/community/histology-slide-gripper/mujoco/README.md) · [Português (Brasil)](../../../../pt-BR/community/histology-slide-gripper/mujoco/README.md) · [简体中文](../../../../zh-CN/community/histology-slide-gripper/mujoco/README.md) · [日本語](../../../../ja/community/histology-slide-gripper/mujoco/README.md) · [हिन्दी](../../../../hi/community/histology-slide-gripper/mujoco/README.md) · [العربية](../../../../ar/community/histology-slide-gripper/mujoco/README.md)

[Original en inglés](../../../../../../community/histology-slide-gripper/mujoco/README.md)

[Español](../../../README.md)

> Traducción automática completa, aún sin revisión de hablantes nativos. Las imágenes, el código, CAD y PDF originales son compartidos. En caso de duda, consulte el original en inglés.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="microscope-slide-gripper-in-mujoco"></a>
# Gripera de diapositivas en el microscopio MuJoCo

El SO-ARM101 con el agarre paralelo a la cola histológica, exportado de Fusion y montado en lugar de los acoplamientos Robo9.

Prueba con `mujoco` 3.4.0 en el `lerobot` El medio ambiente de la vivienda. No , no . ROS 2 o se requiere Docker.

```bash
conda activate lerobot
cd community/histology-slide-gripper/mujoco
python -m pip install -r requirements.txt
python view.py                      # full arm + slide gripper
python view.py scene_gripper.xml    # gripper alone on a testbench
python test_grasp.py                # headless grasp-and-lift check -> grasp_check.png
```

<a id="mujoco-simulation-preview"></a>
## MuJoCo Previsión de la simulación

![SO-ARM101 agarrador de deslizamiento histológico que entra MuJoCo](../../../../../../community/histology-slide-gripper/mujoco/mujoco_simulation_preview.png)

Esta escena muestra el SO-ARM101 con el agarre paralelo del tobogán histológico montado en
la muñeca, utilizando el mismo MuJoCo modelo lanzado por:

```bash
conda activate lerobot
cd community/histology-slide-gripper/mujoco
python view.py
```

<a id="what-is-modelled"></a>
## Lo que se modela

| Enlace | Fuente | Masa |
|---|---|---|
| `slide_gripper_base` | Bastidor principal, STS3215, barras de guía, rodamientos, sujetador de cámara, Arducam OV9281 | 0.20kg |
| `sg_jaw_right` / `sg_jaw_left` | RB9.01.062.020 clamp + RB9.01.062.030 rúa (m)0.8) | 0.035kg cada uno |
| `sg_pinion` | RB9.01.062.040 el equipo involute,18 T, 0.8módulo | 0.008kg |

Kinemática extraída de las articulaciones construidas en el ensamblaje Fusion
(`Slide_Jaw_Right`, `Slide_Jaw_Left`, `Drive_Pinion`), que son coherentes:
el18 T / 0.8el pinón del módulo tiene un7.2en mm de radio, y7.2mm x4.9306RAD =
**35.5mm** de movimiento por mandíbula  ⁇  exactamente los límites del deslizador en el CAD.

<a id="control"></a>
## Control

Un actuador, `sg_grip`, comandado en **metros de viaje en la mandíbula**:

| `ctrl` | viaje de la mandíbula | abertura entre las caras de la hoja |
|---|---|---|
| `0.0` | 0 mm | **84 mm** (totalmente abierto) |
| `0.0295` | 29.5mm | 25 mm (una diapositiva del microscopio) |
| `0.0355` | 35.5mm | **13 mm** (closos por completo) |

Ambas mandíbulas están empujadas por el único pinión, así que `sg_jaw_left_joint` y
`sg_pinion_joint` son esclavos de `sg_jaw_right_joint` por `<equality>` restricciones  ⁇
el equipo gira visiblemente con las mandíbulas. El mando *el pasado* el objeto a apretar:
cerrarse a un objeto de 25 mm con `ctrl=0.0355` da alrededor de4.7N en las almohadillas.

Las cinco articulaciones de los brazos conservan sus nombres URDF (`base_link_to_link1` ... `link4_to_link5`).

<a id="collision-geometry"></a>
## Geometría de colisión

Las redes geométricas son **sólo visuales** (`contype=0`), porque MuJoCo las redes de los cascos convexos y
El casco de una mandíbula en forma de L llena el hueco con el que estás tratando de agarrarte. El contacto es
transportados por cajas en las dos superficies de agarre de cada mandíbula (grupo 3, escondidas en el
renderizaciones):

- `sg_pad_*` ⁇  la hoja de deslizamiento de 30 mm, CAD x 42 ⁇ 50, z 26 ⁇ 31
- `sg_mid_*` ⁇  la sección media más amplia, CAD x 42 ⁇ 58, z 18.5 ⁇ 38.5

El sitio de TCP `sg_tcp` se sienta entre las cuchillas; `sg_camera` es el marco óptico Arducam.

<a id="files"></a>
## Archivos

- `so101_slide_gripper.xml` ⁇  el robot completo (generado por `build_full.py`)
- `scene_gripper.xml` ⁇  solo agarre, con eje de elevación para ensayos
- `gripper_assets.xml` / `gripper_body.xml` / `gripper_actuation.xml` ⁇  el sujetador,
  como incluye utilizables tanto en modelos de unidad de grado como en radianos
- `meshes/{base,jaw_right,jaw_left,pinion}.stl` ⁇  exportado de Fusion en **montaje
  Coordenadas**, así que cada parte ya está en su lugar correcto (no por partes de origen para perseguir)
- `meshes/arm/` ⁇  Las mallas de los brazos del Robo9 repo
- `build_arm.py` ⁇  tiras xacro de `so_101.urdf.xacro`, deja caer las pinzas de stock, recopila a MJCF
- `build_full.py` ⁇  Injerta el agarre en `link5`; **editado `MOUNT_POS`/`MOUNT_QUAT` - ¿Por qué no ?**

<a id="how-the-gripper-was-located-on-the-wrist"></a>
## Cómo se localizó el agarre en la muñeca

`link5_1.stl` En el Robo9 repo no es sólo la muñeca  ⁇  contiene todo el stock
Gripera (marco, barras de guía, cámara). Así que es la parte que el diseño de la pegadura de diapositivas reemplaza, y
`build_full.py` elimina su malla y deja caer su masa de0.556de kg a0.08En el caso de los animales.

La postura de montaña fue resuelta, no adivinada: `base.stl` fue instalado contra
`link5_1.stl` sobre la geometría que comparten (marco principal + barras de guía) buscando todos
24 rotaciones alineadas con los ejes y marcando la distancia más cercana al vecino. Lo mejor que encaja es
**+90 grados aproximadamente en X** (CAD + Y -> enlace)5+Z, CAD +Z -> enlace5-Y) con una2.0mm mediano
residual  ⁇  las pinzas de deslizamiento cuelgan perpendiculares a las pinzas puntiagudas de Robo9, coincidiendo
el conjunto de fusión.

<a id="stability"></a>
## Estabilidad

El modelo se establece en `max|qvel| = 0` y se queda allí. Si alguna vez la ves temblar, el
Lo primero que hay que comprobar son los contactos perdidos (`ncon` en el panel de información del espectador debe ser 0
con el brazo en reposo). Se necesitaban tres cosas:

1. **`<exclude body1="world" body2="link1_1"/>`** - la verdadera solución. El importador URDF
   fusiones `base_link` en el `worldbody`, y MuJoCo Salta las colisiones entre padres e hijos
   *excepto* cuando el padre es el cuerpo mundial. Así que la malla de base y el enlace 1 malla
   se interpenetra en el hombro, produciendo un contacto permanente que fijó el jaque
   actuador en su +-1.5N.m límite. Esto solo se ha resuelto `|qvel|` de4.78de la0.
2. `sg_pinion_joint` Armadura 1e-6 -> **1e-4**. Una unión esclavizada por una rigurosa igualdad con
   casi sin charlas de inercia (estaba alcanzando su punto máximo a 12 rad/s).
3. Igualdad `solref` 0.002 -> **0.01**. Una constante de tiempo de restricción igual al paso del tiempo
   es demasiado rígido para resolver limpiamente; esto también hizo que el pinion aterrizara exactamente en -282.5 grados
   en lugar de -280 grados.

<a id="caveats"></a>
## Cuevas

- **Las masas se asumen, no se miden.** La fusión informa que cada cuerpo es de acero (las mandíbulas
  se publican en 221 g cada uno); los valores anteriores son estimaciones de PLA y hardware. Si usted
  asignar materiales reales en Fusion, actualizar el `mass=` los atributos en `gripper_body.xml`.
- La inercia se deriva de: MuJoCo de la forma de malla más esa masa, no del tensor de Fusion.
- Los límites articulares del brazo, el amortiguación y la fricción son heredados de la URDF del repo y
  no se han reajustado.
- **Las masas de los enlaces del brazo también son densas de acero**, el mismo defecto que el sujetador:
  Total de las operaciones de la URDF **2.81kg** en comparación con aproximadamente 1 kg para un SO-101 real, y `link2_to_link3`
  Necesidades1.91N.m para mantenerse contra un1.5N.m límite del actuador, por lo que se cae. Esto sí .
  no causa temblor (ver arriba), pero hace que el brazo se comporte como un mucho más pesado
  La máquina. Escalación de cada masa del brazo y `diaginertia` por ~0.36el total de los
  1.19kg y elimina la saturación; el real STS3215 también puestos más cercanos2.9N.m más que el
  El URDF es conservador 1.5.
- El residuo de alineación de 2 mm es real: el "seguidor principal frame_125" no es idéntico
  al marco horneado en `link5_1.stl`.
- `sg_pinion_joint` es cosmético - no lleva carga, porque las dos estanterías están acopladas
  entre sí directamente. Existe para que el engranaje gire en la dirección correcta en pantalla.

<a id="driving-it-in-the-mujoco-viewer"></a>
## Conducirlo en el MuJoCo el espectador

Utilice el **`sg_grip` Deslizador en el panel de control**. Los deslizadores en el *Juntas* panel
escribe `qpos` Las restricciones de igualdad se limitan directamente y se omiten, por lo que se arrastran las
mientras se hace una pausa) desincroniza las mandíbulas del pinión. Presionar Run vuelve a convergerlo.

<a id="re-exporting-after-a-cad-change"></a>
## Reexportación después de un cambio en el CAD

La exportación se realizó a través de la conexión MCP Fusion:
los cuerpos en los cuatro vínculos rígidos, y escribe STL binarios en coordenadas de ensamblaje
(mm). Re-exportación con el diseño Fusion abierto para refrescar las mallas en
lugar  ⁇  nada más necesita cambiar a menos que se mueva una unión.
<!-- /translated-content -->

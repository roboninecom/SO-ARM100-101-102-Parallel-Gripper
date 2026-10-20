<!-- translation-navigation -->
[English](../../../en/community/histology-slide-gripper/README.md) · [Русский](../../../ru/community/histology-slide-gripper/README.md) · [Español](README.md) · [Français](../../../fr/community/histology-slide-gripper/README.md) · [Deutsch](../../../de/community/histology-slide-gripper/README.md) · [Português (Brasil)](../../../pt-BR/community/histology-slide-gripper/README.md) · [简体中文](../../../zh-CN/community/histology-slide-gripper/README.md) · [日本語](../../../ja/community/histology-slide-gripper/README.md) · [हिन्दी](../../../hi/community/histology-slide-gripper/README.md) · [العربية](../../../ar/community/histology-slide-gripper/README.md)

[Original en inglés](../../../../../community/histology-slide-gripper/README.md)

[Español](../../README.md)

> Traducción automática completa, aún sin revisión de hablantes nativos. Las imágenes, el código, CAD y PDF originales son compartidos. En caso de duda, consulte el original en inglés.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="histology-slide-gripper-community-mod"></a>
# Histología Gripper de diapositivas (mod comunitario)

Una variante comunitaria de la SO-ARM100/101 Gripper paralelo por [Michael Viacheslavov](https://github.com/histochemichael), adaptado para la automatización histológica y histotecnológica: recogida suave de las diapositivas del microscopio estándar de 75 x 25 mm, coloraciones de diapositivas/racks, y una visión cercana por cámara del agarre.

<div align="center">

![Histología de la demostración del agarre de diapositiva](../../../../../community/histology-slide-gripper/assets/histology-slide-gripper-demo.gif)

*SO-ARM100/101 un agarre paralelo que utiliza las pinzas personalizadas para manejar los toboganes del microscopio y una carcasa/rack de coloración.*

</div>

<a id="what-changed-vs-the-base-gripper"></a>
## Lo que cambió contra el Gripper Base

| Adición | Descripción |
|----------|-------------|
| Clemas de diapositivas del microscopio | La geometría larga y plana de las pinzas soporta la captura directa de diapositivas estándar del microscopio de 75 x 25 mm. |
| Manejo de las estanterías y de los envases | Los espacios entre los sujetadores y las puntas involucran los cartuchos de coloración de diapositivas/racks como el cartucho de coloración de diapositivos Medicus Health vinculado a continuación. |
| Titular de Arducam en ángulo | Un soporte impresible apunta a una cámara USB de cierre global Arducam en las mandíbulas del agarre para el monitoreo cercano de la recogida de toboganes y estanterías. |
| Ensamblaje completo CAD | Un conjunto completo de STL impresible y editable STEP están en [`cad/`](../../../../../community/histology-slide-gripper/cad). |

<a id="gallery"></a>
## Galería

<div align="center">

| Recuperación de diapositivas | Recuperación de calzoncillos/estantes para tinturas | Vista del soporte de Arducam |
|:-:|:-:|:-:|
| ![Clamp que sostiene una diapositiva del microscopio](../../../../../community/histology-slide-gripper/assets/slide-gripper-single-slide.jpg) | ![Clamp alineado con el dipper de coloración de tobogan](../../../../../community/histology-slide-gripper/assets/slide-gripper-staining-dipper.jpg) | ![Titular de Arducam por encima de las mandíbulas del sujetador](../../../../../community/histology-slide-gripper/assets/arducam-holder-front.jpg) |

| Vista delantera | Geometría de la mandíbula | Conjunto isométrico |
|:-:|:-:|:-:|
| <img src="../../../../../community/histology-slide-gripper/assets/parallel-microscope-gripper-front.png" alt="Front CAD view of the microscope slide gripper mod" width="250"> | <img src="../../../../../community/histology-slide-gripper/assets/parallel-microscope-gripper-side.png" alt="Angled CAD view showing the microscope slide jaw geometry" width="250"> | <img src="../../../../../community/histology-slide-gripper/assets/parallel-microscope-gripper-isometric.png" alt="Isometric CAD view of the full microscope slide gripper assembly" width="250"> |

</div>

<a id="cad-files"></a>
## Archivos CAD

| Archivos | El formato | Utilización |
|------|--------|-----|
| [`cad/the-parallel-microscope-slide-gripper.stl`](../../../../../community/histology-slide-gripper/cad/the-parallel-microscope-slide-gripper.stl) | LST | Ensamblaje completo impresible para el modo de agarre del microscopio. |
| [`cad/the-parallel-microscope-slide-gripper.step`](../../../../../community/histology-slide-gripper/cad/the-parallel-microscope-slide-gripper.step) | STEP | Fuente CAD editable para el conjunto completo. |

<a id="add-on-bill-of-materials"></a>
## Conjunto de materiales

Estos elementos son específicos para el flujo de trabajo del tobogán/estante y no forman parte del agarre base. [BOM](../../docs/bom.md).

| Componente | El número de | Notas | Enlace |
|-----------|:---:|-------|------|
| Arducam 100fps Mono Global Shutter cámara USB, OV9281 | 1 | Una cámara utilizada con el soporte ángulado para ver el deslizamiento y la recogida cerca de las mandíbulas. | [Amazon Reino Unido](https://www.amazon.co.uk/Arducam-Shutter-Distortion-Computer-Raspberry/dp/B0FXWWF55X) |
| Pista de plástico con manillas | 1+ | Tinta de coloración de referencia para la lancha/rack; diseñada para diapositivas estándar de 75 x 25 mm. | [Medicus Salud](https://www.medicus-health.com/slide-staining-dipper.html) |
| Ensamblaje de agarre paralelo del microscopio | 1 | Impresión `the-parallel-microscope-slide-gripper.stl`El archivo STEP está incluido para las modificaciones. | [`cad/`](../../../../../community/histology-slide-gripper/cad) |

<a id="mujoco-simulation"></a>
## MuJoCo Simulación

<div align="center">

![SO-ARM101 agarrador de deslizamiento histológico que entra MuJoCo](../../../../../community/histology-slide-gripper/mujoco/mujoco_simulation_preview.png)

*SO-ARM101 con el agarre de deslizamiento histológico montado y en marcha MuJoCo.*

</div>

Una persona autónoma MuJoCo El modelo 3.4.0 está disponible en [`mujoco/`](mujoco/README.md). Incluye la totalidad SO-ARM101 modelo, redes de agarre, un banco de pruebas independiente del agarre, guiones de construcción y un control de agarramiento sin cabeza.

Desde la raíz del repositorio:

```bash
conda activate lerobot
cd community/histology-slide-gripper/mujoco
python -m pip install -r requirements.txt
python view.py
```

Utilice el `sg_grip` control en el MuJoCo para abrir y cerrar las mandíbulas. Veamos el [simulación README](mujoco/README.md) para los detalles del modelo, controles, validación e instrucciones de reconstrucción.

<a id="notes"></a>
## Notas

- Los dedos del agarre están destinados a los diapositivos de microscopio estándar de 75 x 25 mm y a los dippers/racks para la coloración de diapositivos.
- El montaje mantiene la vista de la cámara dirigida hacia las mandíbulas del agarre para que la cámara pueda observar el deslizamiento y la recogida de rack.
- Pruebe primero con diapositivas no críticas y ajuste el material de impresión, la carga y la fuerza del agarre para su flujo de trabajo.

<a id="links"></a>
## Enlaces

- 🎥 [Demo: recarga de las estanterías para los toboganes y la pintura (LinkedIn)](https://www.linkedin.com/posts/michael-viacheslavov_histology-histotechnology-robotics-ugcPost-7482570199859240960-Gqpw/)
<!-- /translated-content -->

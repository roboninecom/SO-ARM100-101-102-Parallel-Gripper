<!-- translation-navigation -->
[English](../en/README.md) · [Русский](../ru/README.md) · [Español](README.md) · [Français](../fr/README.md) · [Deutsch](../de/README.md) · [Português (Brasil)](../pt-BR/README.md) · [简体中文](../zh-CN/README.md) · [日本語](../ja/README.md) · [हिन्दी](../hi/README.md) · [العربية](../ar/README.md)

[Original en inglés](../../../README.md)

[Español](README.md)

> Traducción automática completa, aún sin revisión de hablantes nativos. Las imágenes, el código, CAD y PDF originales son compartidos. En caso de duda, consulte el original en inglés.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="so-arm100101-parallel-gripper"></a>
# SO-ARM100/101 Pinza paralela

<div align="center">

[![SO-ARM101 Pinza paralela](../../../assets/images/SO%20ARM%20101%20Parallel%20Gripper%20Live.jpg)](https://youtube.com/shorts/bSyXjgNGXZk)

**🎥 [¡Cuidado con el agarre en acción!](https://youtube.com/shorts/bSyXjgNGXZk)** · **🛒 [Comprar el SO-ARM102 equipo con un agarre paralelo](https://robonine.com/shop/so-arm102-robotic-arm-kit/)**

Un agarrador paralelo ligero impreso en 3D diseñado por: **[Robonine](https://robonine.com)** para el código abierto SO-ARM100/101 plataforma robótica.

> ¿Prefieres un equipo completo de brazos robóticos con una agarre paralela? **[Comprar el SO-ARM102 el kit](https://robonine.com/shop/so-arm102-robotic-arm-kit/)**.

[![Hardware: CERN-OHL-P-2.0](https://img.shields.io/badge/Hardware-CERN--OHL--P--2.0-blue.svg)](../../../HARDWARE-LICENSE.txt)
[![Software: Apache-2.0](https://img.shields.io/badge/Software-Apache--2.0-blue.svg)](../../../SOFTWARE-LICENSE.txt)
[![Documents: CC BY 4.0](https://img.shields.io/badge/Docs-CC%20BY%204.0-blue.svg)](../../../DOCS-LICENSE.txt)
[![Costo: ~$50](https://img.shields.io/badge/Cost-~%2450-green.svg)](docs/bom.md)
[![Encuentro: 30 minutos](https://img.shields.io/badge/Assembly-30%20min-orange.svg)](docs/assembly-guide.md)

---

**¿Preguntas? ¡Estamos aquí para ayudar!**
⁇  Correos electrónicos: [Hola@robonine.com](mailto:hello@robonine.com)

</div>

---

<a id="-key-features"></a>
## ✨ Características clave

| Características | Descripción |
|---------|-------------|
| **Fuerza de agarre 120N** | Mecanismo de mandíbula paralelo confiable |
| **14 mm/s Velocidad** | Velocidad de funcionamiento del pegamento |
| **84 mm de golpe completo** | Abertura amplia para varios objetos |
| **0.5mm Repetibilidad** | Posicionamiento de alta precisión |
| **Compatible con la cámara** | Los apoyos RealSense, Orbbec, cámaras USB |
| **Imprimible en 3D** | Impresión de todas las piezas en impresoras FDM estándar |
| **~$50Costos totales** | Solución de código abierto asequible |
| **Asamblea fácil** | 30-45 minutos con herramientas básicas |

---

<a id="-gallery"></a>
## ⁇  Galería

<div align="center">

<a id="gripper-on-so-arm101"></a>
### Pinza en SO-ARM101

![Pinza montada en SO-ARM101](../../../assets/images/specification/07-gripper-on-so-arm100.jpg)

*Grifas de seguimiento integradas con SO-ARM101 brazo robot*

<a id="dimensions"></a>
### Dimensiones

![Dimensiones de la pinza](../../../assets/images/specification/08-gripper-dimensions-3d.png)

*128 × 109 × 130.5mm, golpe completo84mm*

</div>

---

<a id="-specifications"></a>
## ⁇  Especificaciones

<a id="gripper-parameters"></a>
### Parámetros de la pinza

| Parámetro | El valor |
|-----------|-------|
| Fuerza máxima de agarre | **120 N** |
| Velocidad máxima de agarre | **14 mm/s** |
| Un golpe completo | **84 mm** |
| Repetibilidad | **0.5mm** |
| Masa de ensamblaje (PLA, 30% de relleno) | **170 g** |
| DOF | **1** |

<a id="dimensions-1"></a>
### Dimensiones

| Dimensión | El valor |
|-----------|-------|
| Ancho | 128 mm |
| Profundidad | 130.5mm |
| Alturas | 109 mm |

<a id="servo-parameters-feetech-sts3215"></a>
### Parámetros servo (Feetech STS3215)

| Parámetro | El valor |
|-----------|-------|
| Voltagem de funcionamiento | 12V |
| Par de bloqueo | 30 kg·cm |
| Velocidad (sin carga) | 45 RPM |
| El codificador | Magnético absoluto de 12 bits |
| Protocolo | RS485/TTL hasta 1 Mbps |
| Temperatura de funcionamiento | -20°C ~ 60°C |

---

<a id="-camera-compatibility"></a>
## ⁇  Compatibilidad con las cámaras

El sujetador soporta múltiples cámaras a través de un portafoto intercambiable:

| La cámara | Tipo | Caso de uso |
|--------|------|----------|
| IMX335 USB de 5MP | RGB | Tareas básicas de visión |
| GC2093 USB de 2 MP | RGB | Opción presupuestaria |
| Orbbec Géminis 2 | RGB-D | Percepción en 3D |
| RealSense D405 | RGB-D | Profundidad de alcance cercano |
| RealSense D435/D435i | RGB-D | Propósito general |
| RealSense D455 | RGB-D | Profundidad de largo alcance |

<div align="center">

![Diferentes cámaras montadas en el agarre](../../../assets/images/specification/09-camera-types.png)

*RealSense, módulo de cámara USB, Orbbec Géminis 2*

</div>

---

<a id="-bill-of-materials"></a>
## ⁇  Presentación de los materiales

**Costo total: ~$50** ([BOM completo con enlaces de Amazon](docs/bom.md))

| Categoría | Componentes | ¿Qué es esto? El coste |
|----------|------------|-----------|
| Electrónica | Feetech STS3215 Servicios | ~$29 |
| Rodamientos | MF106ZZ (x2) | ~$2 |
| Tubos de aluminio/carbono | D6x1x125mm (x2) | ~$4 |
| Impresión en 3D | 8 piezas (~ 100-150 g PLA) | ~$12 |
| Elementos de fijación | Parafusos M2/M4, frutos secos M2, parafusos de conjunto M3 | ~$3 |

---

<a id="-quick-start"></a>
## ⁇  Comienza rápido

Para un conjunto completo de brazo robótico con un agarre paralelo, **[comprar el SO-ARM102 el kit](https://robonine.com/shop/so-arm102-robotic-arm-kit/)**. Para construir el SO-ARM100/101 agarre a ti mismo, siga los pasos de abajo.

<a id="1-print-the-parts-2-4-hours"></a>
### 1. Impresión de las piezas (2-4 horas)

Descargar archivos STL desde [`models/parts/`](models/README.md). Compatible con impresoras populares como **Laboratorio de Bambu A1 mini**, **Prusa MINI+**, y cualquier impresora con una cama ≥ 180×180 mm.

| Parte | El número de | Configuración |
|------|:---:|----------|
| Bastidor principal (RB9.01.062.010) | 1 | 20% de relleno |
| Mordaza (RB9.01.062.020) | 2 | 20% de relleno |
| Cremallera (RB9.01.062.030) | 2 | 100% de relleno |
| Engranaje (RB9.01.062.040) | 1 | 100% de relleno |
| Soporte de cámara (RB9.01.060.074) | 1 | 20% de relleno |
| Soporte (RB9.01.060.080) | 1 | 20% de relleno |
| Separador de cámara (RB9.01.060.090) | 1 | 20% de relleno |
| Titular D405 (RB9.01.060.110) | 1 | 20% de relleno |

<a id="2-order-components-1-2-days"></a>
### 2. Componentes de orden (1-2 días)

¿Ves ? [Conjunto de materiales](docs/bom.md) para los enlaces directos de Amazon.

<a id="3-assemble-30-45-minutes"></a>
### 3. Ensamblaje (30-45 minutos)

Seguir el [Guía de la Asamblea](docs/assembly-guide.md) con imágenes paso a paso:

1. Montar el equipo en servo disco, instalar este conjunto en servo
2. Inserir el cable servo
3. El uso de Feetech el software mueve el servo a su posición mínima (mueva el deslizador en el software hacia la izquierda)
4. Fije las cremalleras a las mordazas
5. Introduzca las varillas guía en ambas mordazas
6. Instale los rodamientos en el bastidor principal y fíjelos con tornillos
7. Encaje las varillas guía en el bastidor
8. Separe las mordazas hasta sus posiciones extremas izquierda y derecha
9. Inserir el servo y arreglarlo con tornillos
10. Aponte la cámara espaciadora y la cámara UVC, fija con tornillos 4x y frutos secos M2 (opcional)
11. Montado en el brazo robótico (opcional)

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
## ⁇  Estructura del repositorio

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
## ⁇  Documentación

| Documento | Descripción |
|----------|-------------|
| [Guía de inicio rápido](docs/quick-start.md) | - Vamos a correr en 30 minutos . |
| [Guía de la Asamblea](docs/assembly-guide.md) | Paso a paso con imágenes |
| [Guía de ensamblaje de pegatinas (PDF)](../../Assembly%20Guide%20Follower%20Gripper.pdf) | Instrucciones para el montaje del agarre impresible |
| [SO-ARM101 Guía de montaje (PDF)](../../Assembly%20Guide%20SO-ARM101.pdf) | Todo SO-ARM101 instrucciones de montaje del brazo |
| [Conjunto de materiales](docs/bom.md) | Lista de piezas con enlaces de Amazon |
| [Las especificaciones](docs/specifications.md) | Detalles técnicos |
| [Modelos en 3D](models/README.md) | Imprimir configuraciones y archivos |
| [Específico del producto paralelo de pegamento (PDF)](../../Parallel%20gripper%20by%20Robo9.pdf) | Especificación del producto de sujetadores paralelos de Robo9 |
| [SO-ARM101 Específicos del producto (PDF)](../../SO-ARM101%20by%20Robo9.pdf) | SO-ARM101 especificación de producto del brazo robótico de Robo9 |

---

<a id="-hardware-requirements"></a>
## ⁇  Requisitos de hardware

<a id="electronics"></a>
### Electrónica
- 1× Feetech STS3215 Motor de servicio

Conectar el agarre al existente SO-ARM100/101 Servo bus y controlador.
El controlador robótico y la fuente de alimentación forman parte de la configuración del brazo, fuera del BOM del agarre.

<a id="mechanical"></a>
### Mecánico
- 2× MF106ZZ Los rodamientos (6×10×3 mm)
- 2× Tubos de aluminio/carbono D6x1x125 mm

<a id="fasteners"></a>
### Elementos de fijación
- 2 × M4 × 8 tornillos DIN 7991
- 4x M2x8 tornillos DIN 912
- 4× M2 DIN 934 nueces
- 4× M3×4 DIN 913 set de tornillos

<a id="tools-required"></a>
### Herramientas necesarias
- Descripción de la letra a)1)
- Las claves de hexagonal M2 (H1.5) y M4 (H2.5)

---

<a id="-simulation"></a>
## ⁇ ️ Simulación

SO-ARM101 se puede simular en 5 motores de física mediante un paquete de descripción ROS2 con un único URDF parametrizado. No es necesario instalar ROS2: Docker se encarga de todo.

<div align="center">

| Gazebo (Fortaleza de la Ignición) | MuJoCo |
|:-:|:-:|
| ![SO-ARM-101 en el Gazebo](../../../assets/images/simulation/gazebo/gazebo_pick_place.png) | ![SO-ARM-101 en el MuJoCo](../../../assets/images/simulation/mujoco/mujoco_pick_place.png) |

</div>

| Simulador | El estado | - ¿Qué es eso? |
|-----------|--------|--------|
| [Gazebo](simulation/gazebo/README.md) | Estoy listo. | `docker compose run gazebo` |
| [MuJoCo](simulation/mujoco/README.md) | Estoy listo. | `docker compose run mujoco` |
| [Webots](simulation/webots/README.md) | No está estable | `docker compose run webots` |
| [CoppeliaSim](simulation/coppeliasim/README.md) | No probado | Simulador externo |
| [NVIDIA Isaac Sí](simulation/isaac_sim/README.md) | No probado | Simulador externo |

**Inicio rápido (Docker):**

```bash
cd simulation/so_arm_101_description
docker compose run gazebo    # or mujoco, webots
```

Veamos el [Guía de simulación](simulation/README.md) para la configuración completa, detalles de arquitectura y mando robot.

---

<a id="-community-mods"></a>
## ⁇  Modos comunitarios

Variantes del agarre construidas por la comunidad, cada una autónoma en [`community/`](../../../community):

| Mod | El autor | Descripción |
|-----|--------|-------------|
| [Histología Gripera de diapositivas](community/histology-slide-gripper/README.md) | [Michael Viacheslavov](https://github.com/histochemichael) | Clemas para toboganes de microscopio de 75 x 25 mm y colocadores/racks, además de un soporte Arducam en ángulo para el seguimiento del agarre. |

<div align="center">

<a href="community/histology-slide-gripper/README.md"><img src="../../../community/histology-slide-gripper/assets/slide-gripper-single-slide.jpg" alt="Histology slide gripper mod holding a microscope slide" width="400"></a>

*Histología Slide Gripper mod  ⁇  haga clic para obtener la descripción completa, archivos CAD y demostración*

</div>

---

<a id="-contributing"></a>
## ⁇  Contribución

¡Damos la bienvenida a las contribuciones! Por favor, siéntase libre de:
- ⁇  Informar errores y problemas
- ⁇  Sugerir nuevas características
- ⁇  Envíe solicitudes de retiro
- ⁇  Mejorar la documentación

---

<a id="-license"></a>
## ⁇  Licencia

Derecho de autor (c) 2025 Robonine. Este proyecto tiene múltiples licencias  ⁇  diferentes tipos de
el material tiene diferentes licencias:

| Materiales | Licencia |
|---|---|
| Diseños de hardware  ⁇ `models/`, CAD comunitario, redes de agarre | [CERN-OHL-P-2.0](../../../HARDWARE-LICENSE.txt) |
| Software  ⁇ `software/`, `examples/`, `simulation/`, código de simulación en `community/` | [Apache-2.0](../../../SOFTWARE-LICENSE.txt) |
| Documentación e imágenes  ⁇ `docs/`, `assets/`, todos `README.md` | [CC BY 4.0](../../../DOCS-LICENSE.txt) |

¿Ves ? [`LICENSING.md`](LICENSING.md) para el mapa exacto archivo por archivo y
[`REUSE.toml`](../../../REUSE.toml) para la versión legible por máquina.

**No todo aquí es RobonineEs el trabajo.** El SO-ARM101 Las redes de brazos se derivan
de [TheRobotStudioEl proyecto de aguas arriba](https://github.com/TheRobotStudio/SO-ARM100)
y permanecer Apache-2.0; el sujetador de diapositivas histológico fue aportado por
[@histochemichael](https://github.com/histochemichael). ¿Ves ? [`NOTICE`](../../../NOTICE)
antes de reutilizar cualquier malla.

Liberaciones hasta y incluidas `v0.3.1` se publicaron bajo GPL-3.0 y permanecen
disponible bajo dichos términos  ⁇  ver [`RELICENSING.md`](RELICENSING.md).

---

<a id="-links"></a>
## ⁇  Enlaces

- [Feetech STS3215 Servicios](https://www.feetechrc.com/525603.html)
- [STServo Python SDK](https://github.com/FEETECH-RC/STServo_SDK_Python)

---

<a id="-engineering-team"></a>
## ⁇  Equipo de Ingenieros

| Nombre | Role | Contacto |
|------|------|---------|
| **Boris Kotov** | Ingeniero de software | [Telegrama](https://t.me/bkotov) |
| **Alan Subin** | Ingeniero de diseño | [Linkedin](https://www.linkedin.com/in/alan-subin/) |

---

<a id="-star-history"></a>
## ⭐ Historial de estrellas

[![Historial de estrellas](https://api.star-history.com/svg?repos=roboninecom/so-arm100-101-parallel-gripper&type=Date&legend=top-left)](https://www.star-history.com/?repos=roboninecom%2Fso-arm100-101-parallel-gripper&type=date&legend=top-left)

---

<div align="center">

**Construido para la comunidad robótica por [Robonine](https://robonine.com)** 🤖

**¿Preguntas? ¡Estamos aquí para ayudar!**
⁇  Correos electrónicos: [Hola@robonine.com](mailto:hello@robonine.com)

</div>
<!-- /translated-content -->

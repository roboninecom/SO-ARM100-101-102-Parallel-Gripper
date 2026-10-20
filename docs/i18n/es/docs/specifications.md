<!-- translation-navigation -->
[English](../../en/docs/specifications.md) · [Русский](../../ru/docs/specifications.md) · [Español](specifications.md) · [Français](../../fr/docs/specifications.md) · [Deutsch](../../de/docs/specifications.md) · [Português (Brasil)](../../pt-BR/docs/specifications.md) · [简体中文](../../zh-CN/docs/specifications.md) · [日本語](../../ja/docs/specifications.md) · [हिन्दी](../../hi/docs/specifications.md) · [العربية](../../ar/docs/specifications.md)

[Original en inglés](../../../specifications.md)

[Español](../README.md)

> Traducción automática completa, aún sin revisión de hablantes nativos. Las imágenes, el código, CAD y PDF originales son compartidos. En caso de duda, consulte el original en inglés.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="so-arm-100101-parallel-follower-gripper"></a>
# SO ARM 100/101 Gripera paralela de seguimiento

<a id="overview"></a>
## Presentación general

Efector final de impresión 3D ligero diseñado por: **Robonine** para la plataforma robótica de teletrabajo SO ARM 100/101 de código abierto. El mecanismo proporciona un movimiento paralelo confiable y una fuerza de agarre suficiente para una amplia gama de aplicaciones educativas y experimentales.

![El agarre de seguimiento montado SO-ARM100](../../../../assets/images/specification/07-gripper-on-so-arm100.jpg)

*El agarre de seguimiento montado SO-ARM100 brazo robot*

<a id="key-features"></a>
## Características clave

- Diseño de código abierto
- Costo BOM por un sujetador: ~ $50
- Puede imprimirse durante un ciclo en una impresora 3D FDM de grado consumidor
- Compatible con las cámaras de vídeo populares:
  - Orbbec Géminis 2
  - RealSense D405, D435/D435i, D455
  - GC2093 Modulo de cámara USB 2MP
  - IMX335 cámara USB de 5MP

---

<a id="dimensions"></a>
## Dimensiones

<a id="3d-overview"></a>
### 3D En general

![Dimensiones de la pegadura  ⁇  vista isométrica](../../../../assets/images/specification/08-gripper-dimensions-3d.png)

*Vista isométrica que muestra las dimensiones generales:128 × 109 × 130.5mm, golpe completo84mm*

| Dimensión | El valor |
|-----------|-------|
| Ancho | 128 mm |
| Profundidad | 130.5mm |
| Alturas | 109 mm |
| Un golpe completo | 84 mm |

---

<a id="mounting-interface"></a>
## Interfaz de montaje

![Dimensiones de interfaz de montaje](../../../../assets/images/specification/03-mounting-interface.jpg)

*Flanza de montaje con patrón de agujero para el brazo robótico*

| Características | Dimensión |
|---------|-----------|
| Diámetro de la flanza de montaje | Ø 20 mm |
| Término de la operación | Ø7 mm |
| Los agujeros de montaje | 4x Ø3.2mm |

---

<a id="gripper-parameters"></a>
## Parámetros de la pinza

| Parámetro | Pinza del brazo seguidor |
|-----------|------------------|
| Masa de ensamblaje (PLA, 30% de relleno) | 170 g |
| Fuerza máxima de agarre | 120 N |
| Velocidad máxima de agarre | 14 mm/s |
| Un golpe completo | 84 mm |
| Repetibilidad | 0.5mm |
| DOF | 1 |

---

<a id="technical-specifications"></a>
## Las especificaciones técnicas

<a id="materials--construction"></a>
### Materiales y construcción

| Componente | Especificación |
|-----------|---------------|
| Material primario | PETG / PLA |
| Transmisión | Rapaz y pinón |
| Guías | Tubos redondos de aluminio/carbono (Ø6 mm) |
| Conductor | Feetech el servo actuador STS3215 |

<a id="servo-parameters-feetech-sts3215"></a>
### Parámetros servo (Feetech STS3215)

| Parámetro | El valor |
|-----------|-------|
| Rango de voltaje operativo | 12V |
| Velocidad (sin carga) | 45 RPM |
| Corriente corriente (sin carga) | 180 mA |
| Torsión de estacionamiento (bloqueada) | 30 kg·cm |
| Corriente de suspensión (bloqueado) | 2.7 A |
| Corriente ociosa (a punto de parada) | 30 mA |
| Par nominal | 10 kg·cm |
| corriente calificada | 900 mA |
| Resistencia terminal | 1 Ω |
| Temperatura de funcionamiento | -20°C ~ 60°C |
| Tipo de codificador | Magnético absoluto de 12 bits |
| Protocolo de control | RS485/TTL hasta 1 Mbps |
| Protección electrónica | Contra alta tensión, corriente, carga y temperatura |

---

<a id="camera-compatibility"></a>
## Compatibilidad con las cámaras

El agarre Follower es compatible con varias cámaras a través del soporte de cámara intercambiable.

![Diferentes cámaras montadas en el agarre](../../../../assets/images/specification/09-camera-types.png)

*Diferentes cámaras montadas en el agarre (de izquierda a derecha): RealSense, módulo de cámara USB, Orbbec Géminis 2*

<a id="supported-cameras"></a>
### Cámaras con soporte

| La cámara | Tipo | Notas |
|--------|------|-------|
| IMX335 USB de 5MP | RGB | Compacto y de bajo coste |
| GC2093 USB de 2 MP | RGB | Opción presupuestaria |
| Orbbec Géminis 2 | RGB-D | Detección de profundidad |
| RealSense D405 | RGB-D | Profundidad de alcance cercano |
| RealSense D435/D435i | RGB-D | Propósito general |
| RealSense D455 | RGB-D | Profundidad de largo alcance |

---

<a id="supplied-resources"></a>
## Recursos suministrados

- Completo conjunto de archivos STL para impresión 3D
- Guía de montaje
- Dibujos con dimensiones de montaje
- Archivo URDF para simuladores robóticos

---

<a id="integration"></a>
## Integración

El agarre se puede integrar de forma independiente en numerosos sistemas robóticos gracias a su instalación conveniente y sencilla mediante la flange de montaje estándar.

<a id="mounting-requirements"></a>
### Las exigencias crecientes

- 4x tornillos M3 para el montaje de las flanges
- Compatible con SO-ARM100/101 brazo robot
- Placas adaptadoras personalizadas disponibles para otros brazos de robot

<a id="communication"></a>
### Comunicación

- Conexión en serie a través de TTL o RS485
- Rate de Baud: hasta 1 Mbps
- Protocolo: Feetech Protocolo STS

---

<a id="product-specification-documents"></a>
## Documentos de especificación del producto

- [Especificación del producto de pegamento paralelo (PDF)](../../../Parallel%20gripper%20by%20Robo9.pdf) ⁇  Especificación completa del producto para el agarre paralelo de Robo9
- [SO-ARM101 Especificación del producto (PDF)](../../../SO-ARM101%20by%20Robo9.pdf) ⁇  Especificación completa del producto SO-ARM101 brazo robótico de Robo9

---

*Las especificaciones sujetas a cambios basadas en la implementación y las pruebas reales*
<!-- /translated-content -->

<!-- translation-navigation -->
[English](../../en/models/README.md) · [Русский](../../ru/models/README.md) · [Español](README.md) · [Français](../../fr/models/README.md) · [Deutsch](../../de/models/README.md) · [Português (Brasil)](../../pt-BR/models/README.md) · [简体中文](../../zh-CN/models/README.md) · [日本語](../../ja/models/README.md) · [हिन्दी](../../hi/models/README.md) · [العربية](../../ar/models/README.md)

[Original en inglés](../../../../models/README.md)

[Español](../README.md)

> Traducción automática completa, aún sin revisión de hablantes nativos. Las imágenes, el código, CAD y PDF originales son compartidos. En caso de duda, consulte el original en inglés.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="3d-models"></a>
# Modelos en 3D

Esta carpeta contiene archivos STL para el conjunto de Follower Gripper.

<a id="complete-assembly"></a>
## Asamblea completa

| Archivos | Descripción | Printeras compatibles |
|------|-------------|---------------------|
| `Follower gripper (165x165 bed size).STL` | Kit completo de piezas de agarre | Impresoras con tamaño de cama > 165×165 mm |

<a id="compatible-3d-printers"></a>
### Printeras 3D compatibles

- **Laboratorio de Bambu A1 mini** (180×180×180mm)
- **Prusa MINI / MINI+** (180×180×180mm)
- **Creatividad Ender-2 Pro** (165×165×180mm)
- **Cobra Neo de cualquier cubo** (220×220×250 mm)
- **Un genio de la artillería** (220×220×250 mm)

*Nota: Cualquier impresora con un tamaño de cama ≥ 165×165 mm puede imprimir la vista previa completa del montaje.*

<a id="individual-parts"></a>
## Partes individuales

Localizado en el `parts/` carpeta:

| Número de la parte | Archivos | El número de | Descripción |
|-------------|------|:---:|-------------|
| RB9.01.060.074 | `Camera holder.STL` | 1 | Cubierta de montaje para cámaras |
| RB9.01.060.080 | `Holder.STL` | 1 | Cubierta de montaje sin cámara |
| RB9.01.060.090 | `Camera spacer.STL` | 1 | Espaciador para cámara |
| RB9.01.060.110 | `D405 holder.STL` | 1 | Tener para la cámara D405 |
| RB9.01.062.010 | `Main frame.STL` | 1 | Cuadro estructural principal |
| RB9.01.062.021 (D6.0) | `Clamp.STL` | 2 | Mordazas de la pinza |
| RB9.01.062.021 (D6.1) | `Clamp.STL` | 2 | Mordazas de la pinza |
| RB9.01.062.021 (D6.2) | `Clamp.STL` | 2 | Mordazas de la pinza |
| RB9.01.062.021 (D6.3) | `Clamp.STL` | 2 | Mordazas de la pinza |
| RB9.01.062.031 | `Gear rack.STL` | 2 | Recajas de engranajes para movimiento lineal |
| RB9.01.062.040 | `Gear.STL` | 1 | Engranaje motriz |
| RB9.01.062.100 | `Nail.STL` | 2 | Las uñas |

<a id="print-settings"></a>
## Configuración de impresión

| Parámetro | Valor recomendado |
|-----------|-------------------|
| Materiales | Pla / PETG |
| Alturas de la capa | 0.2mm (0.15mm para engranajes) |
| Envasado | 20% (30% para los engranajes) |
| Los apoyos | Según sea necesario |
| Paredes | 3-4perímetros |

<a id="notes"></a>
## Notas

- Gráficos de impresión con mayor relleno (100%) para una mejor resistencia
- El marco principal puede requerir soportes dependiendo de la orientación
- Posprocesamiento: puede ser necesario ligerar el encaje de los rodamientos
- Las piezas individuales se pueden imprimir en cualquier impresora FDM estándar

<a id="better-rods-fit"></a>
## Mejores barras que encajan
![Placa de ensayo](../../../../assets/images/assembly/rod-test-plate.PNG)

Para asegurarse de que las varillas compradas encajan mejor en los pinzones, es necesario utilizar una pieza de prueba. Imprimirlo y, trabajando desde el agujero más grande hasta el más pequeño, seleccionar el diámetro que permita que la varilla se ajuste a la parte de ensayo sin dificultad y con un mínimo espacio libre. Luego imprimir las compresoras con el mismo diámetro del agujero que se menciona en el nombre de archivo stl (por ejemplo: RB9.01.062.021 (D6.1) si elige el diámetro6.1mm).
<!-- /translated-content -->

<!-- translation-navigation -->
[English](../../en/docs/assembly-guide.md) · [Русский](../../ru/docs/assembly-guide.md) · [Español](assembly-guide.md) · [Français](../../fr/docs/assembly-guide.md) · [Deutsch](../../de/docs/assembly-guide.md) · [Português (Brasil)](../../pt-BR/docs/assembly-guide.md) · [简体中文](../../zh-CN/docs/assembly-guide.md) · [日本語](../../ja/docs/assembly-guide.md) · [हिन्दी](../../hi/docs/assembly-guide.md) · [العربية](../../ar/docs/assembly-guide.md)

[Original en inglés](../../../assembly-guide.md)

[Español](../README.md)

> Traducción automática completa, aún sin revisión de hablantes nativos. Las imágenes, el código, CAD y PDF originales son compartidos. En caso de duda, consulte el original en inglés.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="assembly-guide-for-follower-gripper-so-arm101"></a>
# Guía de reunión para el agarre del seguidor SO-ARM101

Esta guía proporciona instrucciones paso a paso para montar el agarre paralelo. Sigue estos pasos cuidadosamente para garantizar un funcionamiento adecuado.

<a id="required-tools"></a>
## Herramientas necesarias

- Descripción de las características del dispositivo1
- Las claves de hexagonal M2 (H1.5) y M4 (H2.5)

---

<a id="step-1-install-gear-on-servo"></a>
## Paso 1: Instalar el equipo en servo

![Servo con montaje de engranajes](../../../../assets/images/assembly/02-servo-with-gear-assembly.png)

**Componentes necesarios:**
- 1x Feetech STS3215 Servicios
- 1x Engranaje  (RB9.01.062.040)
- 1x Disco de servo (desde el kit de servo)
- 1x tornillo de montaje servo M3x6 (desde el kit servo)
- 4x Set de tornillos DIN 913 M3x4

**Las instrucciones:**
1. Coloque el engranaje para agarrar en el disco de servo y aprete los tornillos 4x Set M3x4 en la dirección del disco de servo a Gear. Asegúrese de que no aparezca ninguna brecha entre el disco y el engranaje al apretar los tornillos.
2. Montar el conjunto de engranajes en el eje de salida del servo.
3. Se asegure con el tornillo M3x6 que se encuentra en el kit de servo.

---

<a id="step-2-servo-positioning-and-torque-limit"></a>
## Paso 2: Posicionamiento del servo y límite de par

![Posicionamiento por servo](../../../../assets/images/assembly/Feetech-Servo-Window.png)

**Componentes necesarios:**
- 1x Tabla y cables de bus servo en serie

**Instrucciones para los usuarios de Windows:**
1. Conecta Servo a la Junta de Servicios de Autobús Serial, conecta la Junta a PC por USB.
2. Configurar el servo con Feetech's **FD** (SCServo Desarrollo) herramienta. Es de fuente cerrada
   El software de Windows desde Feetech y es **No** redistribuidos en este repositorio:
   - Descarga oficial: <https://www.feetechrc.com/software.html> ⁇  Buscar el FD /
     SCServo Debug archivo. Algunas descargas están protegidas por contraseña; solicite la
     contraseña de Feetech.
   - Alternativa de plataforma transversal de código abierto:
     <https://github.com/Kotakku/FT_SCServo_Debug_Qt>

   Los pasos a continuación describen la interfaz de FD; la alternativa expone el mismo
   Parámetros con nombres similares.
3. Seleccione su puerto COM, seleccione BaudRate 1 000 000, pulse los botones "Abrir" y después de "Búsqueda".
4. A continuación, seleccione su servo.
5. Compruebe la caja para activar el par en servo.
6. Mueve el deslizador a la izquierda.

![Límite máximo de par](../../../../assets/images/assembly/max-torque-window.png)

7. Cambiar la ventana a una pestaña "Programación".
8. Seleccione el parámetro "Limite máximo de torque", ajuste a 500 ans pulsar "Ahorrar".

---

<a id="step-3-clamps"></a>
## Paso 3: Clemas

![Mordazas](../../../../assets/images/assembly/clamp+rack+nail.PNG)

**Componentes necesarios:**
- 2x Mordazas (RB9.01.062.021)
- 2x Cremalleras (RB9.01.062.031)
- 2x Las uñas (RB9.01.062.100)

**Las instrucciones:**
1. Introduzca las cremalleras en las mordazas desde un lateral.
2. Después introduzca los clavos desde la parte posterior.

---

<a id="step-4-rods"></a>
## Paso 4: Varillas

![Varillas guía](../../../../assets/images/assembly/rods+clamps.PNG)

**Componentes necesarios:**
- 2x Varillas D6x125mm

**Las instrucciones:**
1. Inserta las varillas en ambas pinzas. Si ha pedido barras/tubos de más de 125 mm, deberá cortarlos a esta longitud.

---

<a id="step-5-install-bearings-on-main-frame"></a>
## Paso 5: Instale los rodamientos en el marco principal

![Los rodamientos instalados en el marco principal](../../../../assets/images/assembly/frame+bearings.png)

**Componentes necesarios:**
- 2x MF106ZZ Los rodamientos (10x6x3 mm)
- 2x M4x8 tornillos DIN 7991

**Las instrucciones:**
1. Insertar el 2x MF106ZZ los rodamientos en sus posiciones designadas en el marco principal. La flange de rodamiento debe mirar hacia arriba.
2. Fije cada rodamiento con un tornillo M4x8.

---

<a id="step-6-connection-of-rods-and-frame"></a>
## Paso 6: Conexión de barras y marco

![Conexión de barras y marco principal](../../../../assets/images/assembly/frame-with-clamps.png)

**Las instrucciones:**
1. Encaje las varillas guía en el bastidor.
2. Separe las mordazas hasta sus posiciones extremas izquierda y derecha.

---

<a id="step-7-mount-servo-on-main-frame"></a>
## Paso 7: Monte Servo en el marco principal

![Servo montado en el marco principal](../../../../assets/images/assembly/servo-on-frame.png)

**Componentes necesarios:**
- 3x parafusos automáticos (desde el kit servo)

**Las instrucciones:**
1. Coloque el servo en el marco principal y alinear los agujeros de montaje.
2. Fije el servo con 3x tornillos autorroscantes del kit del servo.

---

<a id="step-8-gripper-holder-attachment"></a>
## Paso 8: Adjunto del sujetador de agarre

![Adhesivo del sujetador de pegadura](../../../../assets/images/assembly/09-gripper-holder-attachment.png)

**Componentes necesarios:**
- 1x Soporte de cámara (RB9.01.060.074) o Titular (RB9.01.060.080)
- 1x SO-ARM101
- Parafusos 4x M3x6 (desde el kit servo)
- 4x parafusos de auto-apertura (desde el kit servo)

**Las instrucciones:**
1. Si planea usar Gripper con cámara, adjunta el sujetador de la cámara. SO-ARM101 y fijar con tornillos 4x M3x6
2. Conecte la pegadura paralela al sujetador de la cámara y fija con tornillos automáticos 4x
3. Conectar el cable desde la pegadura paralela al servo no 5 de SO-ARM101

---

<a id="step-9-camera-attachment-optional"></a>
## Paso 9: Adjunto de la cámara (opcional)

![Aparecimiento de la cámara](../../../../assets/images/assembly/camera-attachment.png)

**Componentes necesarios:**
- 1x cámara UVC con agujeros de montaje en 28x28 mm
- 1x Separador de cámara (RB9.01.060.090)
- 4x M2x8 tornillos
- 4x M2 nueces

**Las instrucciones:**
1. Introduzca 4x tuercas M2 desde la parte posterior del soporte de cámara.
2. Coloque el separador y la cámara por delante y fíjelos con 4x tornillos M2x8.

---
<a id="assembly-complete"></a>
## ¡La Asamblea completa!

![Reunidos SO-ARM101 con Follower Gripper](../../../../assets/images/specification/07-gripper-on-so-arm100.jpg)

¡Felicitaciones! Su ... SO-ARM101 se ha ensamblado y está listo para su uso.

<a id="next-steps"></a>
### Los próximos pasos
- Funcionamiento del agarre de ensayo antes de su uso
<!-- /translated-content -->

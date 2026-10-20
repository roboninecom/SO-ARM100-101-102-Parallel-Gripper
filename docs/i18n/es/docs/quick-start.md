<!-- translation-navigation -->
[English](../../en/docs/quick-start.md) · [Русский](../../ru/docs/quick-start.md) · [Español](quick-start.md) · [Français](../../fr/docs/quick-start.md) · [Deutsch](../../de/docs/quick-start.md) · [Português (Brasil)](../../pt-BR/docs/quick-start.md) · [简体中文](../../zh-CN/docs/quick-start.md) · [日本語](../../ja/docs/quick-start.md) · [हिन्दी](../../hi/docs/quick-start.md) · [العربية](../../ar/docs/quick-start.md)

[Original en inglés](../../../quick-start.md)

[Español](../README.md)

> Traducción automática completa, aún sin revisión de hablantes nativos. Las imágenes, el código, CAD y PDF originales son compartidos. En caso de duda, consulte el original en inglés.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="quick-start-guide"></a>
# Guía de inicio rápido

Trae su Gripper de seguidores para SO-ARM101 ¡Vamos a correr!

[![SO-ARM101 Pinza paralela](../../../../assets/images/SO%20ARM%20101%20Parallel%20Gripper%20Live.jpg)](https://youtube.com/shorts/bSyXjgNGXZk)

*Haga clic en la imagen para [observe el agarre en acción](https://youtube.com/shorts/bSyXjgNGXZk)!*

<a id="what-youll-need"></a>
## Lo que necesitarás

<a id="hardware"></a>
### Hardware
- [ ] Todas las piezas impresas en 3D (véase [Modelos en 3D](../models/README.md))
- [ ] Componentes electrónicos (véase [BOM](bom.md))
- [ ] Componentes mecánicos (serradillos, barras, sujetadores)
- [ ] Herramientas: destornillador Phillips PH1, teclas Hex M2 (H1.5) y M4 (H2.5)

<a id="software"></a>
### Software
- [ ] Python 3.6 + instalado
- [ ] STServo Descargado del SDK
- [ ] Las actuales SO-ARM100/101 controlador, conexión USB y alimentación del brazo

---

<a id="step-1-3d-print-the-parts-2-4-hours"></a>
## Paso 1: Impresión 3D de las piezas (2-4 horas)

1. Descargar archivos STL desde `models/parts/`
2. Impresión con configuraciones recomendadas:
   - Alto de la capa:0.2mm
   - Carga: 20% (marco/clames), 100% (engranajes)
   - Material: PLA o PETG
3. Eliminar los soportes

![Placa de ensayo](../../../../assets/images/assembly/rod-test-plate.PNG)

Para asegurarse de que las varillas compradas encajan mejor en los pinzones, es necesario utilizar una pieza de prueba. Imprimirlo y, trabajando desde el agujero más grande hasta el más pequeño, seleccionar el diámetro que permita que la varilla se ajuste a la parte de ensayo sin dificultad y con un mínimo espacio libre. Luego imprimir las compresoras con el mismo diámetro del agujero que se menciona en el nombre de archivo stl (por ejemplo: RB9.01.062.021 (D6.1) si elige el diámetro6.1mm).

**Printeras 3D compatibles** (180×180 mm + cama):
- Laboratorio de Bambu A1 mini
- Prusa MINI / MINI+
- Cobra Neo de cualquier cubo
- Cualquier impresora con una cama ≥ 180×180 mm

**Partes para imprimir:**
- 1x Bastidor principal (RB9.01.062.010)
- 2x Mordaza (RB9.01.062.020)
- 2x Cremallera (RB9.01.062.030)
- 1x Engranaje (RB9.01.062.040)
- 1x Soporte de cámara (RB9.01.060.074)
- 1x Soporte (RB9.01.060.080)
- 1x Separador de cámara (RB9.01.060.090)

---

<a id="step-2-gather-components-1-2-days-shipping"></a>
## Paso 2: Recolectar los componentes (1-2 días de envío)

Las piezas de pedido en el [Conjunto de materiales](bom.md). Reutilizar el controlador de brazos y la fuente de alimentación; éstos están fuera del coste del agarre:

| Componente | El número de | ¿Qué es esto? El coste |
|-----------|:---:|-----------|
| Feetech STS3215 servo | 1 | ~$29 |
| MF106ZZ los rodamientos (10x6x3 mm) | 2 | ~$2 |
| Tubos de aluminio/carbono D6x1x125mm | 2 | ~$4 |
| Impresión 3D PLA| 8 partes | ~$12 |
| Los elementos de sujeción (viscos/nudos M2/M4) | varios | ~$3 |

**Costo total estimado: ~ $50**

---

<a id="step-3-assembly-30-45-minutes"></a>
## Paso 3: Asamblea (30-45 minutos)

Sigue los detalles [Guía de la Asamblea](assembly-guide.md):


1. Inserir el cable servo
2. El uso de Feetech el software mueve el servo a su posición mínima (mueva el deslizador en el software hacia la izquierda)
3. Fije las cremalleras a las mordazas
4. Introduzca las varillas guía en ambas mordazas
5. Instale los rodamientos en el bastidor principal y fíjelos con tornillos
6. Encaje las varillas guía en el bastidor
7. Separe las mordazas hasta sus posiciones extremas izquierda y derecha
8. Inserir el servo y arreglarlo con tornillos
9. Aponte la cámara espaciadora y la cámara UVC, fija con tornillos 4x y frutos secos M2 (opcional)
10. Montado en el brazo robótico (opcional)

---

<a id="step-4-software-setup-10-minutes"></a>
## Paso 4: Configuración del software (10 minutos)

1. **Instalación STServo SDK**
   ```bash
   git clone https://github.com/FEETECH-RC/STServo_SDK_Python.git
   cd STServo_SDK_Python
   cp -r STservo_sdk /path/to/your/project/
   ```

2. **Instalación Python Las dependencias**
   ```bash
   pip install pyserial
   ```

3. **Configurar la conexión**
   ```python
   DEVICENAME = 'COM7'  # Windows
   # DEVICENAME = '/dev/ttyUSB0'  # Linux
   STS_ID = 1  # Servo ID (use 6 if connected as gripper on SO-ARM101)
   ```

---

<a id="step-5-first-test-5-minutes"></a>
## Paso 5: Primera prueba (5 minutos)

1. **Conecta el hardware**
   - Servo de pegamento → servo no 5 en el SO-ARM101 autobús de servicio
   - Controlador de brazos → Computadora (USB) existente
   - Utilice la fuente de alimentación del brazo configurada para los servidores instalados
   - Ajuste la identificación de servo del agarre para que coincida `STS_ID` y mantenerlo único en el autobús
   - Cierre otras aplicaciones de control robótico antes de abrir el puerto en serie

2. **Realizar la prueba básica**
   ```bash
   cd software/python
   python gripper_control.py
   ```

3. **Prueba los comandos básicos**
   - Ingrese `45` para abrir la pinza
   - Ingrese `-45` para cerrar la pinza
   - Ingrese `0` al centro
   - Presione Entrar para salir

---

<a id="troubleshooting"></a>
## Solución de problemas

<a id="connection-issues"></a>
### Cuestiones de conexión
- ✅ Compruebe el puerto COM en Gerente de Dispositivos (Windows) o `ls /dev/ttyUSB*` (Linux)
- ✅ Verifique si el LED de energía servo está encendido
- ✅ Prueba diferentes velocidades de baud (por defecto: 1000000)
- ✅ Compruebe las conexiones por cable

<a id="movement-issues"></a>
### Problemas de movimiento
- ✅ Verificar el compromiso de los equipos con el estante
- ✅ Compruebe si hay unión mecánica
- ✅ Asegúrese de que los rodes se muevan libremente en barras
- ✅ Monitorear la temperatura del servo (máximo 60°C)

<a id="software-issues"></a>
### Problemas con el software
- ✅ Instalar STServo SDK correctamente
- ✅ Cheque Python versión (3.6+)
- ✅ Verifique los permisos de puerto en serie: `sudo chmod 666 /dev/ttyUSB0` (Linux)

---

<a id="next-steps"></a>
## Los próximos pasos

🎉 **¡Felicitaciones!** ¡Tu agarre está funcionando!

Ahora puedes:
- El monte en SO-ARM100/101 brazo robot
- Integra con su software de control
- Añadir una cámara al portafoto
- Crear aplicaciones personalizadas

<a id="need-help"></a>
## ¿Necesitas ayuda?

- ⁇  Leer el [Las especificaciones](specifications.md)
- ⁇  Compruebe el [Guía de la Asamblea](assembly-guide.md)
- 📄 [Específico del producto paralelo de pegamento (PDF)](../../../Parallel%20gripper%20by%20Robo9.pdf)
- 📄 [SO-ARM101 Específicos del producto (PDF)](../../../SO-ARM101%20by%20Robo9.pdf)
- ⁇  Informar los problemas en GitHub

---

**¡Bienvenido a la comunidad de sujetadores paralelos!** 🤖
<!-- /translated-content -->

<!-- translation-navigation -->
[English](../../en/examples/README.md) · [Русский](../../ru/examples/README.md) · [Español](README.md) · [Français](../../fr/examples/README.md) · [Deutsch](../../de/examples/README.md) · [Português (Brasil)](../../pt-BR/examples/README.md) · [简体中文](../../zh-CN/examples/README.md) · [日本語](../../ja/examples/README.md) · [हिन्दी](../../hi/examples/README.md) · [العربية](../../ar/examples/README.md)

[Original en inglés](../../../../examples/README.md)

[Español](../README.md)

> Traducción automática completa, aún sin revisión de hablantes nativos. Las imágenes, el código, CAD y PDF originales son compartidos. En caso de duda, consulte el original en inglés.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="examples---parallel-gripper"></a>
# Ejemplos: Gripera paralela

Este directorio contiene ejemplos de código que demuestran cómo utilizar el agarre paralelo en varios escenarios.

<a id="available-examples"></a>
## Ejemplos disponibles

<a id="basic_usagepy"></a>
### `basic_usage.py`
Demuestra las operaciones fundamentales del agarre:
- Conexión al sujetador
- Traslado a posiciones específicas
- Información sobre el estado de lectura
- Manejo de errores básicos

**Uso:**
```bash
cd examples
python basic_usage.py
```

<a id="configuration"></a>
## Configuración

Antes de ejecutar ejemplos, es posible que deba ajustar los parámetros de configuración:

```python
config = GripperConfig()
config.DEVICENAME = '/dev/ttyUSB0'  # Linux/Mac
# config.DEVICENAME = 'COM7'        # Windows
config.STS_ID = 1                   # Servo ID
config.BAUDRATE = 1000000          # Communication speed
```

<a id="common-issues"></a>
## Cuestiones comunes

<a id="connection-problems"></a>
### Problemas de conexión
- **Las ventanas**: Compruebe el Administrador de Dispositivos para encontrar el puerto COM correcto
- **Linux**: Asegurar que el usuario tenga acceso a los puertos en serie (`sudo usermod -a -G dialout $USER`)
- **macOS**Uso: `/dev/cu.usbserial-*` o `/dev/tty.usbserial-*`

<a id="permission-errors"></a>
### Errores de autorización
```bash
# Linux/macOS
sudo chmod 666 /dev/ttyUSB0
# or add user to dialout group
sudo usermod -a -G dialout $USER
```

<a id="stservo-sdk-issues"></a>
### STServo Cuestiones de SDK
Asegúrese de que el STServo SDK está instalado correctamente:
1. Descargar desde: [STServo Python SDK](https://files.waveshare.com/wiki/Bus-Servo-Adapter-(A)/STServo_Python.zip)
2. Extraer el archivo ZIP descargado y copiar `STservo_sdk` carpeta (con la carpeta en sí) a `software/python/` directorio

<a id="creating-your-own-examples"></a>
## Creando sus propios ejemplos

Al crear nuevos ejemplos:

1. **Importar el módulo de agarre**
   ```python
   from gripper_control import ParallelGripper, GripperConfig
   ```

2. **Maneja los errores con gracia**
   ```python
   try:
       gripper = ParallelGripper()
       if not gripper.connect():
           print("Connection failed!")
           return
       # Your code here
   finally:
       gripper.disconnect()
   ```

3. **Incluye la documentación adecuada**
   - Descripción clara de lo que hace el ejemplo
   - Configuración de hardware requerida
   - El comportamiento esperado

<a id="safety-notes"></a>
## Notas de seguridad

⚠️ **Principales consideraciones de seguridad:**
- Seguir siempre la temperatura y el tracto de corriente
- Implementar el manejo adecuado de errores
- Prueba con fuerzas bajas primero
- Garantizar una configuración mecánica adecuada
- Mantenga los dedos alejados de las partes móviles

<a id="contributing-examples"></a>
## Ejemplos que contribuyen

¡Damos la bienvenida a nuevos ejemplos! Por favor ...
- Sigue el estilo de código existente
- Incluya comentarios completos
- Prueba exhaustiva antes de la presentación
- Añadir la entrada a este README

---

**¡Feliz codificación!** 🤖
<!-- /translated-content -->

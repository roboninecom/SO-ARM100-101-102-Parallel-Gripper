<!-- translation-navigation -->
[English](../en/CONTRIBUTING.md) · [Русский](../ru/CONTRIBUTING.md) · [Español](CONTRIBUTING.md) · [Français](../fr/CONTRIBUTING.md) · [Deutsch](../de/CONTRIBUTING.md) · [Português (Brasil)](../pt-BR/CONTRIBUTING.md) · [简体中文](../zh-CN/CONTRIBUTING.md) · [日本語](../ja/CONTRIBUTING.md) · [हिन्दी](../hi/CONTRIBUTING.md) · [العربية](../ar/CONTRIBUTING.md)

[Original en inglés](../../../CONTRIBUTING.md)

[Español](README.md)

> Traducción automática completa, aún sin revisión de hablantes nativos. Las imágenes, el código, CAD y PDF originales son compartidos. En caso de duda, consulte el original en inglés.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="contributing-to-open-source-parallel-gripper"></a>
# Contribuir a la Gripper paralela de código abierto

¡Gracias por su interés en contribuir a este proyecto! Agradecemos las contribuciones de la comunidad robótica.

<a id="ways-to-contribute"></a>
## Maneras de contribuir

<a id="-bug-reports"></a>
### ⁇  Informes de insectos
- Utilice el rastreador de problemas de GitHub
- Incluir pasos detallados de reproducción
- Proporcionar información sobre el sistema (OS, Python versión, modelo servo)
- Anexar registros o mensajes de error

<a id="-feature-requests"></a>
### ⁇  Solicitudes de características
- Compruebe primero los problemas existentes
- Describa claramente el caso de uso
- Considerar la complejidad de la aplicación
- Discuta con los encargados de mantenimiento antes de realizar grandes cambios.

<a id="-code-contributions"></a>
### ⁇  Contribuciones al código
- Forque el depósito
- Crear una rama de características
- Seguir las normas de codificación
- Añadir los ensayos cuando proceda
- Documentación actualizada

<a id="-documentation"></a>
### ⁇  Documentación
- Mejorar la documentación existente
- Añadir ejemplos de uso
- Crear tutoriales o guías
- Corrección de errores o explicaciones poco claras

<a id="-hardware-improvements"></a>
### ⁇ ️ Mejoras en el hardware
- Modificaciones o mejoras en el diseño
- Sugerencias de piezas alternativas
- Nueva compatibilidad con el servo
- Optimizaciones mecánicas

<a id="development-setup"></a>
## Configuración del desarrollo

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/your-org/parallel-gripper.git
   cd parallel-gripper
   ```

2. **Instalar dependencias**
   ```bash
   pip install -r software/python/requirements.txt
   ```

3. **Instalación STServo SDK**
   ```bash
   git clone https://github.com/FEETECH-RC/STServo_SDK_Python.git
   cp -r STServo_SDK_Python/STservo_sdk ./software/python/
   ```

<a id="coding-standards"></a>
## Normas de codificación

<a id="python-code"></a>
### Python Código
- Siga la guía de estilo PEP 8
- Utilice indicaciones de tipo cuando sea apropiado
- Añadir cadenas de documentos a todas las funciones/clases
- Duración máxima: 88 caracteres
- Utilizar nombres de variables significativos

<a id="documentation"></a>
### Documentación
- Utilice el formato de marcado
- Incluya ejemplos de código
- Mantenga el lenguaje claro y conciso
- Actualizar README si es necesario

<a id="3d-models"></a>
### Modelos en 3D
- Proporcionar archivos STL en formato binario
- Incluir los archivos fuente si es posible (STEP, Fusion 360, etc.)
- Impresión de ensayo antes del envío
- Configuración de impresión del documento

<a id="pull-request-process"></a>
## Proceso de extracción de la solicitud

1. **Antes de comenzar**
   - Compruebe los problemas existentes y las relaciones públicas
   - Hable primero de los cambios importantes
   - Asegúrese de poder probar sus cambios

2. **Haciendo cambios**
   - Crear un nombre de rama descriptiva
   - Hacer compromisos atómicos con mensajes claros
   - Prueba tus cambios a fondo
   - Actualizar la documentación según sea necesario

3. **Presentación de relaciones públicas**
   - Rellenar la plantilla de relaciones públicas
   - Cuestiones relacionadas con el enlace
   - Proporcione una descripción clara de los cambios
   - Incluye información sobre los ensayos

4. **Proceso de revisión**
   - Respuestas de los revisores de direcciones
   - Mantenga las discusiones constructivas
   - Tenga paciencia con el proceso de revisión

<a id="testing-guidelines"></a>
## Orientaciones para las pruebas

<a id="software-testing"></a>
### Pruebas de software
- Prueba en su configuración de hardware
- Verificar la compatibilidad entre plataformas
- Compruebe el manejo de errores
- Casas de bordes de ensayo

<a id="hardware-testing"></a>
### Pruebas de hardware
- Verifique que las impresiones 3D funcionan correctamente
- Procedimientos de ensayo de montaje
- Verifique las tolerancias mecánicas
- Validación con diferentes materiales

<a id="communication"></a>
## Comunicación

<a id="channels"></a>
### Canales
- Cuestiones de GitHub: informes de errores, solicitudes de características
- Discusiones de GitHub: preguntas generales, ideas
- Solicitudes de retirada: revisión del código, discusión técnica

<a id="guidelines"></a>
### Orientaciones
- Sea respetuoso y constructivo
- Busca antes de publicar
- Proporcione contexto y detalles
- Ayudar a otros cuando sea posible

<a id="recognition"></a>
## Reconocimiento

Los contribuyentes serán reconocidos en:
- README.md sección de contribuyentes
- Notas de liberación
- Documentación del proyecto

<a id="license"></a>
## Licencia

Este proyecto tiene múltiples licencias  ⁇  ver [`LICENSING.md`](LICENSING.md) para el mapa completo.

Al presentar una contribución, certifica que tiene derecho a hacerlo.
y usted acepta que está autorizado en virtud de la licencia que se aplica a la parte de
el depósito en el que aterriza:

| Estás cambiando . | Su contribución está autorizada. |
|---|---|
| Hardware / CAD | CERN-OHL-P-2.0 |
| Software | Apache-2.0 |
| Documentación e imágenes | CC BY 4.0 |

En otras palabras, entrada = salida: cualquiera que sea la licencia bajo la que ya esté un expediente.
su cambio en él está bajo la misma licencia.

**Material de terceros.** Si su contribución incluye algo que usted no hizo
Crear usted mismo, decirlo en la solicitud de tira para que pueda ser registrado en
[`NOTICE`](../../../NOTICE). Por favor , no cometa binarios que no puede licenciar
incluye herramientas de proveedores y firmware.

**Nuevos archivos** deben estar cubiertas por: [`REUSE.toml`](../../../REUSE.toml). `reuse lint` entra en
En el caso de un archivo que carezca de derechos de autor y licencia
la información.

<a id="questions"></a>
## ¿Preguntas?

Si tienes preguntas sobre cómo contribuir, puedes abrir un número o comenzar una conversación.

---

**¡Gracias por ayudar a mejorar este proyecto!** 🤝
<!-- /translated-content -->

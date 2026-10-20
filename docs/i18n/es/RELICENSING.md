<!-- translation-navigation -->
[English](../en/RELICENSING.md) · [Русский](../ru/RELICENSING.md) · [Español](RELICENSING.md) · [Français](../fr/RELICENSING.md) · [Deutsch](../de/RELICENSING.md) · [Português (Brasil)](../pt-BR/RELICENSING.md) · [简体中文](../zh-CN/RELICENSING.md) · [日本語](../ja/RELICENSING.md) · [हिन्दी](../hi/RELICENSING.md) · [العربية](../ar/RELICENSING.md)

[Original en inglés](../../../RELICENSING.md)

[Español](README.md)

> Traducción automática completa, aún sin revisión de hablantes nativos. Las imágenes, el código, CAD y PDF originales son compartidos. En caso de duda, consulte el original en inglés.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="relicensing-record"></a>
# Registro de relicencia

Este archivo registra cómo y por qué este proyecto se mudó de la GPL-3.0, y el acuerdo
de sus contribuyentes. Existe para que el historial de la licencia sea auditable sin
Estoy cavando en el git.

**Estatus: en progreso.** Este cambio no debe ser fusionado hasta que cada ac abajo es
registrado.

<a id="what-changed"></a>
## ¿Qué cambió?

| Materiales | Antes de | Después de |
|---|---|---|
| Hardware / CAD | Sólo con GPL-3.0 | CERN-OHL-P-2.0 |
| Software | Sólo con GPL-3.0 | Apache-2.0 |
| Documentación e imágenes | Sólo con GPL-3.0 | CC BY 4.0 |

Titular de los derechos de autor: **Robonine**. ¿Ves ? `LICENSING.md` para el mapa archivo por archivo,
`REUSE.toml` para la versión legible por máquina, y `NOTICE` para terceros
la atribución.

<a id="why"></a>
## ¿Por qué ?

GPL-3.0 está escrito para software. Sus definiciones  ⁇  "código fuente", "objeto"
código", "Fuente correspondiente"  ⁇  no se cartografian limpiamente en un objeto físico, por lo que
para la parte CAD de este proyecto nunca fue claro lo que realmente desencadenó
las obligaciones de la licencia. CERN-OHL-P-2.0 Está escrito para hardware y dice
el producto, la fuente cubierta y el componente disponible.

La elección permisiva es deliberada. Se intercambia la protección contra cerrados
los tenedores de agarre a cambio de fricción cero para los integradores, y
compatibilidad con el flujo ascendente SO-ARM100/101 el proyecto y la amplia
LeRobot/ROS ecosistema, que son Apache-2.0 En todas partes.

<a id="licence-history"></a>
## Historia de la licencia

| Compromiso | Fecha | ¿Qué es eso? |
|---|---|---|
| `00fae7b` | 2025-06-27 | Se creó un repositorio. `LICENSE` fue **El MIT** 21 líneas). |
| `64d3f01` | 2025-07-01 | `LICENSE` sustituido por GPL-3.0 (674 líneas). |
| `d37855a` | 2025-07-06 | `README.md` actualizada desde MIT a GPL-3.0. |
| este cambio | — | División de tres vías descrita anteriormente. |

`CONTRIBUTING.md` y `software/python/gripper_control.py` ¿Qué ha sido **Nunca**
se actualizó en 2025 y continuó diciendo MIT. Eso fue un descuido, no.
la doble licencia deliberada.

Las consecuencias son importantes: todos los contribuyentes externos se unieron *después* el revés de la GPL,
en un repositorio cuyo `CONTRIBUTING.md` Aún les dijo *"Al contribuir, usted
acepta que sus contribuciones serán licenciadas bajo la licencia MIT".* El
la licencia que realmente se les ofreció era más permisiva que GPL-3.0. Este cambio
que el repositorio esté en línea con lo que se les dijo a los contribuyentes y no contra
¿Qué es eso? No obstante, estamos pidiendo a cada uno de ellos explícitamente en lugar de confiar en
Eso es todo.

<a id="contributor-agreement"></a>
## Acuerdo de contribuyente

| Contribuyente | Compromiso | El ámbito de aplicación | ¿Qué es esto? |
|---|---|---|---|
| Robonine (Nikita Bragin  ⁇  también `brnikita`, `branikita`) | 76 | Propietario | n/a |
| Alan Workaholic (Alan Subin) | 44 | `models/`, `models/parts/`, `assets/images/`, `docs/` | Trabajos realizados en virtud de un contrato con asignación de PI a Robonine; ac solicitado como cortesía |
| histochemichael (Michael Viacheslavov) | 3 + archivos subidos en su nombre | `community/histology-slide-gripper/` | En espera. |
| Vladimir Osipov | 1 | `README.md` corrección de enlace muerto | En espera. |
| Syed Azhar Hussain Quadri | 1 | `software/python/gripper_control.py` | En espera. |

Cuestión de la relicencia: _para completar_

<a id="authorship-notes"></a>
### Notas de autor

- Compromiso de los autores `Codex <codex@openai.com>` fueron hechas por Nikita Bragin en
  en nombre de Robonine. No son contribuciones de terceros.
- CAD y imágenes de la variante comunitaria
  (`community/histology-slide-gripper/cad/*`, `assets/*`) fueron **cometidos por
  Robonine en nombre de Michael Viacheslavov** ⁇  Comprometió `537f347` y `b4698e7`
  se escriben como `Codex`. El autor de esos archivos pertenece a Michael.
  Los metadatos no reflejan eso, por lo que están escritos aquí.

<a id="decisions-on-the-record"></a>
## Decisiones en el expediente

**`link5_1.stl` es una malla fundida.** Combina el río arriba SO-ARM101 el muñeco con
Robonine's `RB9.01.062.010 Main frame` en un solo cuerpo. Las piezas no son
separable dentro del archivo, por lo que todo el archivo se distribuye bajo Apache-2.0:
Robonine no puede conceder CERN-OHL-P-2.0 sobre la geometría que no posee, y es libre
Licenciar su propia porción en virtud del Apache-2.0. La re-exportación como dos mallas
que cada parte tenga su licencia apropiada; eso se deja como trabajo futuro.

**Notificaciones para archivos binarios.** CERN-OHL-P-2.0 espera que los avisos de licencia sean
retenidos en la Fuente. Los archivos binarios STL y STEP no pueden llevarlos, y
`.pre-commit-config.yaml` excluye deliberadamente esos formatos de los ganchos de texto.
`REUSE.toml` ¿Cómo cumple este proyecto esa obligación?
derechos de autor y licencia para cada archivo por vía, y `reuse lint` hace cumplir que
Nada se deja descubierto.

Los avisos a nivel de directorio se mantuvieron deliberadamente al mínimo  ⁇  sólo cuando
el mapa raíz no lleva información. Dos sobrevivieron:
`simulation/so_arm_101_description/meshes/LICENSE.md`, porque ese directorio
mezclas Robonine y la geometría aguas arriba y alguien copiando una malla fuera necesita ver
que; y `simulation/so_arm_101_description/LICENSE.md`, porque ese ROS
el paquete se distribuye de forma independiente y debe ser auto-descriptivo.

**Los textos de la licencia existen en dos lugares.** `LICENSES/` es donde el REUSE
Las especificaciones las requieren; `HARDWARE-LICENSE.txt`, `SOFTWARE-LICENSE.txt` y
`DOCS-LICENSE.txt` en la raíz son lo que la detección de licencias de GitHub lee, así que el
el repositorio muestra las tres licencias en lugar de ninguna.

**`software/FD.exe` fue eliminado.** Lo es . Feetech"FT" de propiedad SCServo Descarga"
instrumento, comprometido en `7783073` No se concedió ninguna licencia, y estaba cubierto por el
la reclamación general de GPL-3.0 del proyecto  ⁇  que fue incorrecta. `docs/assembly-guide.md`
ahora señala Feetechsu propia descarga y a una alternativa de código abierto.

**El historial de Git no fue reescrito.** `FD.exe` permanece en la historia y en la fuente
archivos de publicaciones `v0.1.0` a través de `v0.3.1`. La reescritura invalidaría todos los
clone, fork y commit SHA referenciados en las solicitudes de puesta abiertas a la corriente ascendente, que es
No vale la pena para una herramienta Feetech se distribuye de forma gratuita.

**`ament_copyright` Se le cayó** de `package.xml`. Fue declarado pero nunca
se conectan o funcionan. Verifica los encabezados de las licencias dentro de los archivos fuente, que
En el marco del proyecto, los Estados miembros han adoptado medidas para garantizar que las licencias de certificación se cumplan. `REUSE.toml` —
Nos obligó por el hecho de que la mayoría de los archivos aquí son binarios. `reuse lint` las cubiertas
Cada archivo en el repositorio, no sólo la docena Python archivos dentro del ROS
el paquete.

<a id="releases"></a>
## Las liberaciones

Esto no cambia retroactivamente las liberaciones `v0.1.0` a través de `v0.3.1`, que
permanecen disponibles bajo GPL-3.0 solamente.

---

Preparado por los encargados del mantenimiento del proyecto. Este es un registro de decisiones, no legal.
¿Qué consejo?
<!-- /translated-content -->

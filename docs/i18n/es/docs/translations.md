<!-- translation-navigation -->
[English](../../en/docs/translations.md) · [Русский](../../ru/docs/translations.md) · [Español](translations.md) · [Français](../../fr/docs/translations.md) · [Deutsch](../../de/docs/translations.md) · [Português (Brasil)](../../pt-BR/docs/translations.md) · [简体中文](../../zh-CN/docs/translations.md) · [日本語](../../ja/docs/translations.md) · [हिन्दी](../../hi/docs/translations.md) · [العربية](../../ar/docs/translations.md)

[Original en inglés](../../../translations.md)

[Español](../README.md)

> Traducción automática completa, aún sin revisión de hablantes nativos. Las imágenes, el código, CAD y PDF originales son compartidos. En caso de duda, consulte el original en inglés.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="documentation-translations"></a>
# Traducciones de documentación

La documentación está disponible en inglés, ruso, español, francés, alemán y brasileño
Portugués, chino simplificado, japonés, hindi y árabe. Utilice los enlaces de idiomas
en el README principal o en el [índice de idiomas](../../README.md).

<a id="scope-and-source-of-truth"></a>
## El alcance y la fuente de la verdad

Los documentos de origen inglés permanecen en sus caminos originales. Traducciones completas en
`docs/i18n/<language>/` reflejar la estructura del repositorio, incluidas las guías de hardware;
ejemplos, modificaciones comunitarias, guías de simulación, instrucciones de contribución;
y explicaciones de licencias. Los enlaces entre los documentos traducidos permanecen en el texto elegido
el lenguaje. CAD, código, configuración, imágenes, video, PDF originales y licencia legal
Los textos se comparten. El texto incrustado en las imágenes y los archivos PDF existentes permanece sin traducir.

La raíz `NOTICE` es autorizada para atribución de terceros. Traducciones de
Las explicaciones de las licencias son informativas; los textos originales de las licencias tienen prioridad.

<a id="translation-status"></a>
## Estado de la traducción

Las traducciones iniciales se generaron con un modelo de traducción local NLLB-200 y
Asistencia de IA, luego comprobado para la estructura del documento, valores técnicos preservados,
Identificadores de piezas, bloques de código, enlaces y anclajes. No han sido revisadas por
hablantes nativos. Las verificaciones automatizadas no certifican la exactitud del lenguaje o del hardware.
Resolver la ambigüedad en relación con la fuente inglesa y informar sobre los problemas relacionados con el idioma,
el camino del documento y la frase afectada.

<a id="maintain-translations"></a>
## Mantener las traducciones

1. Cambiar primero la fuente en inglés, luego actualizar el documento correspondiente en cada
   el lenguaje. Conservar todas las instrucciones, advertencias, tablas, valores, identificadores de piezas.
   los comandos y las URL externas.
2. Mantenga enlaces de documentos traducidos dentro del idioma seleccionado. Los activos compartidos deben
   utilizar caminos relativos de regreso a las ubicaciones existentes del depósito. Preservación explícita
   Los identificadores de anclaje en inglés para que los enlaces de sección funcionen entre idiomas.
3. Después de comprobar una traducción, registra su versión fuente con
   `python .github/scripts/check_translations.py --record-reviewed --locale ru --source docs/bom.md`.
   Este comando registra una versión; no traduce ni revisa el documento.
4. Corra `python .github/scripts/check_translations.py` y
   `pre-commit run --all-files`. Indique qué lenguas han recibido una revisión humana en la PR.

Añadir nuevos documentos de Markdown rastreados a `docs/i18n/manifest.json` con una completa
traducción para cada idioma. El verificador utiliza archivos de origen rastreados, por lo que local
las notas no rastreadas no se convierten en requisitos de documentación. Inglés se incluye como
una copia fuente para la navegación consistente. Las etiquetas de idioma siguen BCP 47.
<!-- /translated-content -->

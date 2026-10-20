<!-- translation-navigation -->
[English](translations.md) · [Русский](../../ru/docs/translations.md) · [Español](../../es/docs/translations.md) · [Français](../../fr/docs/translations.md) · [Deutsch](../../de/docs/translations.md) · [Português (Brasil)](../../pt-BR/docs/translations.md) · [简体中文](../../zh-CN/docs/translations.md) · [日本語](../../ja/docs/translations.md) · [हिन्दी](../../hi/docs/translations.md) · [العربية](../../ar/docs/translations.md)

[English source](../../../translations.md)

[English](../README.md)

> Complete English source copy. Images, code, CAD, and original PDFs are shared.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="documentation-translations"></a>
# Documentation translations

Documentation is available in English, Russian, Spanish, French, German, Brazilian
Portuguese, Simplified Chinese, Japanese, Hindi, and Arabic. Use the language links
in the main README or the [language index](../../README.md).

<a id="scope-and-source-of-truth"></a>
## Scope and source of truth

English source documents stay at their original paths. Complete translations in
`docs/i18n/<language>/` mirror the repository structure, including hardware guides,
examples, community modifications, simulation guides, contribution instructions,
and licensing explanations. Links between translated documents stay in the chosen
language. CAD, code, configuration, images, video, original PDFs, and legal licence
texts are shared. Text embedded in existing images and PDFs remains untranslated.

The root `NOTICE` is authoritative for third-party attribution. Translations of
licensing explanations are informational; original licence texts take precedence.

<a id="translation-status"></a>
## Translation status

Initial translations were generated with a local NLLB-200 translation model and
AI assistance, then checked for document structure, preserved technical values,
part identifiers, code blocks, links, and anchors. They have not been reviewed by
native speakers. Automated checks do not certify language or hardware accuracy.
Resolve ambiguity against the English source and report issues with the language,
document path, and affected sentence.

<a id="maintain-translations"></a>
## Maintain translations

1. Change the English source first, then update the corresponding document in every
   language. Preserve all instructions, warnings, tables, values, part identifiers,
   commands, and external URLs.
2. Keep translated document links within the selected language. Shared assets must
   use relative paths back to their existing repository locations. Preserve explicit
   English anchor IDs so section links work across languages.
3. After checking a translation, record its source version with
   `python .github/scripts/check_translations.py --record-reviewed --locale ru --source docs/bom.md`.
   This command records a version; it does not translate or review the document.
4. Run `python .github/scripts/check_translations.py` and
   `pre-commit run --all-files`. State which languages received human review in the PR.

Add new tracked Markdown documents to `docs/i18n/manifest.json` with a complete
translation for each language. The checker uses tracked source files, so local
untracked notes do not become documentation requirements. English is included as
a source copy for consistent navigation. Language tags follow BCP 47.
<!-- /translated-content -->

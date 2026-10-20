<!-- translation-navigation -->
[English](../../en/docs/translations.md) · [Русский](../../ru/docs/translations.md) · [Español](../../es/docs/translations.md) · [Français](translations.md) · [Deutsch](../../de/docs/translations.md) · [Português (Brasil)](../../pt-BR/docs/translations.md) · [简体中文](../../zh-CN/docs/translations.md) · [日本語](../../ja/docs/translations.md) · [हिन्दी](../../hi/docs/translations.md) · [العربية](../../ar/docs/translations.md)

[Source anglaise](../../../translations.md)

[Français](../README.md)

> Traduction automatique intégrale, pas encore relue par des locuteurs natifs. Images, code, CAO et PDF originaux sont partagés. En cas de doute, consultez la source anglaise.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="documentation-translations"></a>
# Traduction de la documentation

La documentation est disponible en anglais, russe, espagnol, français, allemand et brésilien
Portugais, chinois simplifié, japonais, hindi et arabe. Utilisez les liens linguistiques
dans le README principal ou [indice de langue](../../README.md).

<a id="scope-and-source-of-truth"></a>
## La portée et la source de la vérité

Les documents originaux en anglais restent à leur origine. Traduction complète en français
`docs/i18n/<language>/` refléter la structure du référentiel, y compris les guides matériels;
des exemples, des modifications communautaires, des guides de simulation, des instructions de contribution;
et des explications sur les licences. Les liens entre les documents traduits restent dans le texte choisi
le langage. CAD, code, configuration, images, vidéo, PDF originaux et licence légale
Les textes sont partagés. Le texte intégré dans les images et les fichiers PDF existants reste non traduit.

La racine `NOTICE` est autorisé à être attribué par un tiers. Les traductions de
les explications relatives aux licences sont informatives; les textes originaux des licences ont la priorité.

<a id="translation-status"></a>
## Statut de la traduction

Les traductions initiales ont été générées avec un modèle de traduction NLLB-200 local et
L'aide de l'IA, puis vérifiée pour la structure du document, les valeurs techniques préservées,
les identifiants de pièces, les blocs de code, les liens et les ancres. Ils n'ont pas été examinés par
les locuteurs natifs. Les contrôles automatisés ne certifient pas l'exactitude du langage ou du matériel.
Résoudre l'ambiguïté à l'égard de la source anglaise et signaler les problèmes liés à la langue,
le chemin du document et la phrase affectée.

<a id="maintain-translations"></a>
## Maintenir les traductions

1. Modifiez d'abord la source anglaise, puis mettez à jour le document correspondant dans chaque
   le langage. Conserver toutes les instructions, avertissements, tables, valeurs, identifiants de pièces
   commandes et URL externes.
2. Gardez les liens des documents traduits dans la langue choisie. Les actifs partagés doivent
   utiliser des chemins relatifs pour revenir à leurs emplacements de référentiel existants. Préserver explicite
   Les identifiants d'ancrage en anglais permettent aux liens de section de fonctionner entre les langues.
3. Après avoir vérifié une traduction, enregistrez sa version source avec
   `python .github/scripts/check_translations.py --record-reviewed --locale ru --source docs/bom.md`.
   Cette commande enregistre une version; elle ne traduit ni n'examine pas le document.
4. Courir `python .github/scripts/check_translations.py` et
   `pre-commit run --all-files`. Indiquer quelles langues ont reçu une évaluation humaine dans le PR.

Ajouter de nouveaux documents Markdown suivis à `docs/i18n/manifest.json` avec une
traduction pour chaque langue. Le vérificateur utilise des fichiers source suivis, donc local
les notes non suivies ne deviennent pas des exigences de documentation. L'anglais est inclus comme
une copie source pour une navigation cohérente. Les balises linguistiques suivent BCP 47.
<!-- /translated-content -->

<!-- translation-navigation -->
[English](../../en/docs/translations.md) · [Русский](../../ru/docs/translations.md) · [Español](../../es/docs/translations.md) · [Français](../../fr/docs/translations.md) · [Deutsch](translations.md) · [Português (Brasil)](../../pt-BR/docs/translations.md) · [简体中文](../../zh-CN/docs/translations.md) · [日本語](../../ja/docs/translations.md) · [हिन्दी](../../hi/docs/translations.md) · [العربية](../../ar/docs/translations.md)

[Englische Quelle](../../../translations.md)

[Deutsch](../README.md)

> Vollständige maschinelle Übersetzung, noch nicht von Muttersprachlern geprüft. Bilder, Code, CAD und Original-PDFs werden gemeinsam genutzt. Im Zweifel gilt die englische Quelle.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="documentation-translations"></a>
# Übersetzungen der Dokumentation

Dokumentation ist in englischer, russischer, spanischer, französischer, deutscher und brasilianischer Sprache verfügbar
Portugiesisch, Vereinfachtes Chinesisch, Japanisch, Hindi und Arabisch. Verwenden Sie die Sprachverbindungen
in der HauptREADME oder [Sprachindex](../../README.md).

<a id="scope-and-source-of-truth"></a>
## Umfang und Quelle der Wahrheit

Die englischen Quelldokumente bleiben auf ihren ursprünglichen Pfaden. Vollständige Übersetzungen in
`docs/i18n/<language>/` die Repository-Struktur, einschließlich der Hardware-Anleitungen, spiegeln;
Beispiele, Gemeinschaftsänderungen, Simulationsleitlinien, Beitragsanweisungen;
und Lizenzerklärungen. Links zwischen übersetzten Dokumenten bleiben in der ausgewählten
Sprache. CAD, Code, Konfiguration, Bilder, Video, Original-PDF und rechtliche Lizenz
Die Texte werden geteilt. Der Text, der in vorhandene Bilder und PDF-Dateien eingebettet ist, bleibt unübersetzt.

Die Wurzel `NOTICE` ist für die Zuteilung durch Dritte autorisiert. Übersetzungen
die Erläuterungen für die Lizenzierung sind informativ; Vorrang haben die ursprünglichen Lizenztexte.

<a id="translation-status"></a>
## Übersetzungsstatus

Die ersten Übersetzungen wurden mit einem lokalen NLLB-200-Übersetzungsmodell erstellt und
KI-Hilfe, dann nach Dokumentstruktur geprüft, technische Werte bewahrt,
Teilidentifikatoren, Codeblöcke, Links und Anker. Sie wurden nicht von
Muttersprachler. Automatische Kontrollen bestätigen weder die Sprache noch die Hardware-Genauigkeit.
Zweideutigkeiten gegen die englische Quelle zu lösen und Probleme mit der Sprache zu melden,
Dokumentenweg und betroffene Sätze.

<a id="maintain-translations"></a>
## Übersetzungen beibehalten

1. Ändern Sie zuerst die englische Quelle und aktualisieren Sie dann das entsprechende Dokument in jeder
   Sprache. Alle Anweisungen, Warnungen, Tabellen, Werte und Teileidentifikatoren behalten
   Befehle und externe URLs.
2. Behalten Sie übersetzte Dokumentenverbindungen in der gewählten Sprache. Die Aktiva müssen
   Verwendet relative Wege zurück zu ihren vorhandenen Repository-Standorten. Aufschrift
   Englische Anker-IDs, so dass Abschnittverbindungen über Sprachen hinweg funktionieren.
3. Nach der Überprüfung einer Übersetzung erfassen Sie die Quellversion mit
   `python .github/scripts/check_translations.py --record-reviewed --locale ru --source docs/bom.md`.
   Dieser Befehl nimmt eine Version auf; er übersetzt oder überprüft das Dokument nicht.
4. Lauf ! `python .github/scripts/check_translations.py` und
   `pre-commit run --all-files`. Erläutern Sie, welche Sprachen in der PR von Menschen bewertet wurden.

Hinzufügen neuer verfolgter Markdown-Dokumente `docs/i18n/manifest.json` mit einem vollständigen
Übersetzung für jede Sprache. Der Checker verwendet verfolgte Quelldateien, so dass lokale
nicht verfolgte Notizen werden nicht zu Dokumentationsanforderungen. Englisch ist als
eine Quellkopie für die konsequente Navigation. Die Sprachtags folgen BCP 47.
<!-- /translated-content -->

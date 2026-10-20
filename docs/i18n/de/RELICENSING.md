<!-- translation-navigation -->
[English](../en/RELICENSING.md) · [Русский](../ru/RELICENSING.md) · [Español](../es/RELICENSING.md) · [Français](../fr/RELICENSING.md) · [Deutsch](RELICENSING.md) · [Português (Brasil)](../pt-BR/RELICENSING.md) · [简体中文](../zh-CN/RELICENSING.md) · [日本語](../ja/RELICENSING.md) · [हिन्दी](../hi/RELICENSING.md) · [العربية](../ar/RELICENSING.md)

[Englische Quelle](../../../RELICENSING.md)

[Deutsch](README.md)

> Vollständige maschinelle Übersetzung, noch nicht von Muttersprachlern geprüft. Bilder, Code, CAD und Original-PDFs werden gemeinsam genutzt. Im Zweifel gilt die englische Quelle.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="relicensing-record"></a>
# Aufzeichnungen über die Wiedereingliederung

Diese Datei dokumentiert, wie und warum dieses Projekt von der GPL abgezogen wurde.-3.0, und die Vereinbarung
von ihren Mitwirkenden. Es existiert, sodass die Lizenzgeschichte ohne
Ich gräbe durch Git.

**Status: In Vorbereitung.** Diese Änderung darf nicht zusammengeführt werden, bis jeder Akk unten
Aufgenommen.

<a id="what-changed"></a>
## Was hat sich geändert?

| Material | Vorher | Nach |
|---|---|---|
| Hardware / CAD | Nur mit GPL-3.0 | CERN-OHL-P-2.0 |
| Software | Nur mit GPL-3.0 | Apache-2.0 |
| Dokumentation und Bilder | Nur mit GPL-3.0 | CC BY 4.0 |

Inhaber des Urheberrechts: **Robonine**. Siehst du ? `LICENSING.md` für die Karte von Datei zu Datei,
`REUSE.toml` für die maschinenlesbare Version und `NOTICE` für Dritte
Zuschreibung.

<a id="why"></a>
## Warum?

GPL-3.0 ist für Software geschrieben. Seine Definitionen  ⁇  "Quellcode", "Objekt
Code", "Korrespondenzquelle"  ⁇  nicht sauber auf ein physisches Objekt abbilden, so dass
Für den CAD-Teil dieses Projekts war es nie klar, was tatsächlich ausgelöst hat
die Verpflichtungen der Lizenz. CERN-OHL-P-2.0 ist für Hardware geschrieben und sagt:
die Definition eines Produkts, der abgedeckten Quelle und des verfügbaren Bestandteils.

Die zulässige Wahl ist bewusst. Es verkauft Schutz gegen geschlossene
Gabeln des Griffes im Austausch für Null-Friction für Integratoren und
Kompatibilität mit dem Upstream SO-ARM100/101 Projekt und die breitere
LeRobot/ROS-Ökosysteme, die Apache-2.0 - Ganz durch.

<a id="licence-history"></a>
## Lizenzgeschichte

| Verpflichten | Datum | Was ist das? |
|---|---|---|
| `00fae7b` | 2025-06-27 | Das Repository wurde erstellt. `LICENSE` war **MIT** (21 Zeilen). |
| `64d3f01` | 2025-07-01 | `LICENSE` durch GPL-3.0 (674 Zeilen) ersetzt. |
| `d37855a` | 2025-07-06 | `README.md` von MIT auf GPL-3.0 aktualisiert. |
| Diese Veränderung | — | Drei-Wege-Spaltung, wie oben beschrieben. |

`CONTRIBUTING.md` und `software/python/gripper_control.py` waren **nie**
die im Jahr 2025 aktualisiert wurde und weiterhin MIT-Status enthält. Das war eine Übersicht.
Zweiglizenzierungen auf Absicht.

Die Konsequenz ist wichtig: Jeder externe Beitrittspartner *nach* die GPL-Flip,
in einem Speicher, dessen `CONTRIBUTING.md` Ich habe es ihnen immer noch gesagt. *"Durch Ihren Beitrag
Sie stimmen zu, dass Ihre Beiträge unter der MIT-Lizenz lizenziert werden".* Die
Die Lizenz, die sie tatsächlich angeboten haben, war mehr zugelassen als GPL-3.0. Diese Veränderung
das Repository mit dem übereinstimmt, was den Mitwirkenden gesagt wurde und nicht gegen
- Das ist es. Die Kommission hat die Möglichkeit, daß die Mitgliedstaaten sich mit der
Das ist es.

<a id="contributor-agreement"></a>
## Mitwirkungsvereinbarung

| Mitwirker | Verpflichtungen | Anwendungsbereich | - Ich weiß nicht. |
|---|---|---|---|
| Robonine (Nikita Bragin  ⁇  auch `brnikita`, `branikita`) | 76 | Eigentümer | n/a |
| Alan Workaholic (Alan Subin) | 44 | `models/`, `models/parts/`, `assets/images/`, `docs/` | Arbeit im Rahmen eines Vertrags mit IP-Zuschreibung an RobonineSie wurde als Höflichkeit angefordert. |
| seineTochemichael (Michael Viacheslavov) | 3 + Dateien, die in seinem Namen hochgeladen wurden | `community/histology-slide-gripper/` | - in Auswahl |
| Wladimir Osipov | 1 | `README.md` Schnittstelle | - in Auswahl |
| Syed Azhar Hussain Quadri | 1 | `software/python/gripper_control.py` | - in Auswahl |

Ausgabe der erneuten Genehmigung: _zu füllen_

<a id="authorship-notes"></a>
### Schriftstellern

- Verpflichtungen, die als `Codex <codex@openai.com>` wurden von Nikita Bragin auf
  im Namen von Robonine. Es handelt sich nicht um Beiträge Dritter.
- Die CAD- und Bilder der Community-Variante
  (`community/histology-slide-gripper/cad/*`, `assets/*`) waren **durch
  Robonine im Namen von Michael Viacheslavov** ⁇  Verpflichtungen `537f347` und `b4698e7`
  sind als `Codex`. Die Autorin dieser Dateien gehört Michael.
  Metadaten spiegeln das nicht wider, weshalb sie hier niedergeschrieben sind.

<a id="decisions-on-the-record"></a>
## Beschluß auf dem Register

**`link5_1.stl` ist ein verschmolzenes Netz.** Es kombiniert den Upstream SO-ARM101 mit
Robonine's `RB9.01.062.010 Main frame` in einem einzigen Körper. Die Teile sind nicht
Die gesamte Datei wird unter Apache-2.0:
Robonine kann nicht gewährt werden CERN-OHL-P-2.0 über Geometrie nicht besitzen, und ist frei
die Genehmigung für einen eigenen Teil unter Apache-2.0. Die Rückführung wie zwei Maschen würde
Die Kommission hat sich in diesem Zusammenhang mit der Frage der Erweiterung des Binnenmarktes befaßt.

**Hinweise für binäre Dateien.** CERN-OHL-P-2.0 Erwartet, dass die Genehmigungsbekanntmachungen
in der Quelle behalten. Binäre STL- und STEP-Dateien können sie nicht übernehmen, und
`.pre-commit-config.yaml` diese Formate aus Texthaken absichtlich ausschließt.
`REUSE.toml` Wie dieses Projekt diese Verpflichtung erfüllt:
das Urheberrecht und die Lizenz für jede Datei nach dem Weg; `reuse lint` die
Nichts bleibt offen.

Die Ankündigungen auf Verzeichnisebene wurden bewusst auf ein Minimum reduziert  ⁇  nur dann, wenn sie
Die Wurzelkarte trägt keine Informationen. Zwei überlebten:
`simulation/so_arm_101_description/meshes/LICENSE.md`, weil dieses Verzeichnis
Mischungen Robonine Und die Upstream-Geometrie und jemand, der ein Mesh aus kopiert muss sehen
das; und `simulation/so_arm_101_description/LICENSE.md`, weil diese ROS
Die Verpackung wird unabhängig verteilt und muss sich selbst beschreiben.

**Die Lizenzbestimmungen sind an zwei Stellen vorhanden.** `LICENSES/` ist, wo die REUSE
Die Spezifikation verlangt sie. `HARDWARE-LICENSE.txt`, `SOFTWARE-LICENSE.txt` und
`DOCS-LICENSE.txt` Das ist das, was die Lizenzerkennung von GitHub lautet.
Das Repository zeigt alle drei Lizenzen anstatt keine.

**`software/FD.exe` wurde entfernt.** Das ist es. Feetech"FT" ist Eigentümer SCServo "Auslösen"
Veröffentlichung von `7783073` Die Kommission hat die Genehmigung für das
die allgemeine GPL-3.0-Behauptung des Projekts  ⁇ , die unrichtig war. `docs/assembly-guide.md`
Jetzt wird auf FeetechSie können sich selbst herunterladen und eine Open-Source-Alternative nutzen.

**Die Git-Geschichte wurde nicht neu geschrieben.** `FD.exe` Verbleibt in der Geschichte und in der Quelle
Archive der Veröffentlichungen `v0.1.0` durch `v0.3.1`. Die Umschreibung würde alle
Klonen, Fork und Commit SHA aus offenen Upstream-Pull-Anfragen, die
Es lohnt sich nicht für ein Werkzeug. Feetech Die Kommission hat die Möglichkeit, diese Daten kostenlos zu verbreiten.

**`ament_copyright` wurde fallen gelassen.** von `package.xml`. Es wurde erklärt, aber nie.
Wirbel-auf oder laufen. Sie prüft, ob in den Quelldateien Lizenzüberschriften vorhanden sind.
Die Kommission hat die Möglichkeit, die Genehmigungen für die `REUSE.toml` —
Wir wurden durch die Tatsache gezwungen, dass die meisten Dateien hier binär sind. `reuse lint` Abdeckungen
Alle Dateien im Repository, nicht nur die Dutzend Python Dateien innerhalb des ROS
Packung.

<a id="releases"></a>
## Veröffentlichungen

Dies ändert die Freigabe nicht rückwirkend `v0.1.0` durch `v0.3.1`, die
bleiben nur unter GPL-3.0 verfügbar.

---

Von den Projektbetreibern vorbereitet. Das ist eine Aufzeichnung von Entscheidungen, nicht legal.
Ich gebe dir einen Rat.
<!-- /translated-content -->

<!-- translation-navigation -->
[English](../en/CONTRIBUTING.md) · [Русский](../ru/CONTRIBUTING.md) · [Español](../es/CONTRIBUTING.md) · [Français](../fr/CONTRIBUTING.md) · [Deutsch](CONTRIBUTING.md) · [Português (Brasil)](../pt-BR/CONTRIBUTING.md) · [简体中文](../zh-CN/CONTRIBUTING.md) · [日本語](../ja/CONTRIBUTING.md) · [हिन्दी](../hi/CONTRIBUTING.md) · [العربية](../ar/CONTRIBUTING.md)

[Englische Quelle](../../../CONTRIBUTING.md)

[Deutsch](README.md)

> Vollständige maschinelle Übersetzung, noch nicht von Muttersprachlern geprüft. Bilder, Code, CAD und Original-PDFs werden gemeinsam genutzt. Im Zweifel gilt die englische Quelle.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="contributing-to-open-source-parallel-gripper"></a>
# Beitrag zur Open-Source Parallel Gripper

Vielen Dank für Ihr Interesse an diesem Projekt! Wir begrüßen die Beiträge der Robotikgemeinschaft.

<a id="ways-to-contribute"></a>
## Möglichkeiten, einen Beitrag zu leisten

<a id="-bug-reports"></a>
### ⁇  Fehlerberichte
- Benutzen Sie den GitHub Problem Tracker
- Einzelne Fortpflanzungsschritte
- Systeminformationen (OS, Python (Version, Servomodell)
- Anschließen von Logs oder Fehlermeldungen

<a id="-feature-requests"></a>
### ⁇  Feature Anfragen
- Überprüfen Sie zuerst die bestehenden Probleme
- Beschreiben Sie den Anwendungsfall klar
- Überlegen Sie die Komplexität der Umsetzung
- Besprechen Sie mit den Unterhaltern vor großen Veränderungen

<a id="-code-contributions"></a>
### ⁇  Code Beiträge
- Fork das Repository
- Erstellen Sie eine Funktionsbranche
- Folgen Sie Coding-Standards
- Hinzufügen von Prüfungen gegebenenfalls
- Aktualisierte Dokumentation

<a id="-documentation"></a>
### ⁇  Dokumentation
- Verbesserung der vorhandenen Dokumentation
- Hinzufügen von Nutzungsbeispielen
- Erstellen von Tutorials oder Leitfaden
- Behebung von Schreibfehlern oder unklaren Erklärungen

<a id="-hardware-improvements"></a>
### ⁇ ️ Hardwareverbesserungen
- Entwurfsänderungen oder -verbesserungen
- Alternative Teilvorschläge
- Neue Servokompatibilität
- Mechanische Optimierungen

<a id="development-setup"></a>
## Entwicklungsvorrichtung

1. **Klonen des Repositoriums**
   ```bash
   git clone https://github.com/your-org/parallel-gripper.git
   cd parallel-gripper
   ```

2. **Installieren von Abhängigkeiten**
   ```bash
   pip install -r software/python/requirements.txt
   ```

3. **Installation STServo SDK**
   ```bash
   git clone https://github.com/FEETECH-RC/STServo_SDK_Python.git
   cp -r STServo_SDK_Python/STservo_sdk ./software/python/
   ```

<a id="coding-standards"></a>
## Coding-Standards

<a id="python-code"></a>
### Python Code
- Folgen Sie dem PEP 8-Stilleitfaden
- Verwenden Sie gegebenenfalls Tippschilder
- Hinzufügen von Dokumentstrings zu allen Funktionen/Klassen
- Höchstzeilenlänge: 88 Zeichen
- Verwenden Sie aussagekräftige Variablenamen

<a id="documentation"></a>
### Dokumentation
- Verwenden Sie das Markdown-Format
- Codebeispiele enthalten
- Die Sprache sei klar und prägnant
- Aktualisierung von README bei Bedarf

<a id="3d-models"></a>
### 3D-Modelle
- Bereitstellung von STL-Dateien im binären Format
- Wenn möglich, Quelldateien (STEP, Fusion 360 usw.) einzubeziehen.
- Prüfdruck vor Abgabe
- Einstellungen für Druckdokumente

<a id="pull-request-process"></a>
## Anforderungsprozess

1. **Bevor wir anfangen**
   - Überprüfen Sie bestehende Probleme und PRs
   - Besprechen Sie zuerst die wichtigsten Änderungen
   - Stellen Sie sicher, dass Sie Ihre Änderungen testen können

2. **Veränderungen vornehmen**
   - Erstellen Sie einen beschreibenden Zweignamen
   - Atom-Verpflichtungen mit klaren Nachrichten machen
   - Prüfen Sie Ihre Veränderungen gründlich
   - Aktualisieren Sie die Dokumentation nach Bedarf

3. **Einreichung von PR**
   - Füllen Sie die PR-Vorlage aus
   - Linksbezogene Fragen
   - Eine klare Beschreibung der Änderungen
   - Inklusion von Prüfinformationen

4. **Überprüfungsprozess**
   - Rückmeldung von Adressreviewern
   - Erhalten Sie die Gespräche aufbauend
   - Sei geduldig mit der Überprüfung

<a id="testing-guidelines"></a>
## Prüfrichtlinien

<a id="software-testing"></a>
### Software-Tests
- Test auf Ihrer Hardware-Einstellung
- Überprüfung der plattformübergreifenden Kompatibilität
- Überprüfen Sie die Fehlerbearbeitung
- Testkantenhülle

<a id="hardware-testing"></a>
### Hardwareprüfung
- Überprüfen Sie , ob 3D-Drucke richtig funktionieren .
- Prüfmontageverfahren
- Überprüfen Sie mechanische Toleranzen
- Validiert mit verschiedenen Materialien

<a id="communication"></a>
## Mitteilung

<a id="channels"></a>
### Kanäle
- GitHub-Fragen: Fehlerberichte, Funktionsanfragen
- GitHub-Diskussionen: Allgemeine Fragen, Ideen
- Anträge auf Rückziehung: Code-Überprüfung, technische Diskussion

<a id="guidelines"></a>
### Leitlinien
- Seien Sie respektvoll und konstruktiv
- Suchen Sie vor dem Posten
- Kontext und Einzelheiten
- Wenn möglich, anderen helfen

<a id="recognition"></a>
## Anerkennung

Die Mitwirkenden werden in:
- README.md Teil "Beitragspersonen"
- Veröffentlichungsnotizen
- Projektdokumentation

<a id="license"></a>
## Lizenz

Dieses Projekt hat mehrere Lizenzen [`LICENSING.md`](LICENSING.md) Für die gesamte Karte.

Mit der Einreichung eines Beitrags bestätigen Sie, dass Sie das Recht haben, ihn einzulegen.
und Sie stimmen zu, dass es unter der Lizenz erhältlich ist, die für den Teil von
das Repository, in dem es landet:

| Du änderst dich. | Ihr Beitrag ist lizenziert. |
|---|---|
| Hardware / CAD | CERN-OHL-P-2.0 |
| Software | Apache-2.0 |
| Dokumentation und Bilder | CC BY 4.0 |

Mit anderen Worten, inbound = outbound: unabhängig von der Lizenz, unter der eine Akte bereits steht,
Ihr Wechsel ist unter der gleichen Lizenz.

**Material von Dritten.** Wenn Ihr Beitrag etwas beinhaltet, das Sie nicht geleistet haben
Schöpfe dich selbst, sag es in der Anforderung, damit sie aufgenommen werden kann
[`NOTICE`](../../../NOTICE). Bitte verpflichten Sie sich nicht zu binären, die Sie nicht lizenzieren können  ⁇
enthält Verkäufer-Tools und Firmware.

**Neue Dateien** müssen durch [`REUSE.toml`](../../../REUSE.toml). `reuse lint` ist ein
Vorverpflichtung und in CI und wird versagt, wenn eine Datei nicht urheberrechtlich erfasst ist und keine Lizenz hat
Informationen.

<a id="questions"></a>
## Fragen?

Fühlen Sie sich frei, eine Ausgabe zu öffnen oder eine Diskussion zu beginnen, wenn Sie Fragen zum Beitrag haben!

---

**Vielen Dank, dass Sie uns dabei geholfen haben, dieses Projekt zu verbessern!** 🤝
<!-- /translated-content -->

[English](../../MCP/v2027.2/Scripting.md) • **Deutsch** • [日本語](../../MCP.ja/v2027.2/Scripting.md)

# Scripting — Python-Skripte

> **Server:** Vectorworks MCP · **Version:** Vectorworks 2027 Update 2

[Zurück zum Index](README.md)

Werkzeuge zum Ausführen von Python-Skripten in Vectorworks, Lesen und Speichern von Python-Skriptressourcen sowie Nachschlagen des von Skripten verwendeten Python-`api`-Moduls.

## Inhaltsverzeichnis

- [Überblick](#überblick)
- [Scripting](#scripting)
  - [listScripts](#listscripts)
  - [getScript](#getscript)
  - [saveScript](#savescript)
  - [describePythonApi](#describepythonapi)
  - [getPythonApiGuide](#getpythonapiguide)
  - [runPythonScript](#runpythonscript)
  - [runScript](#runscript)

## Überblick

Dieser Ordner enthält 1 Werkzeuggruppe mit insgesamt 7 Werkzeugen.

| Gruppe | Gruppen-ID | Standardmäßig aktiv | Risikostufe | Anzahl der Werkzeuge | Zusammenfassung |
|---|---|---|---|---|---|
| [Scripting](#scripting) | `scripting` | Nein | hoch | 7 | Führt Python-Skripte aus, liest und speichert Python-Skriptressourcen und schlägt das Python-`api`-Modul nach. |

## Scripting

> **Gruppe:** `Scripting` · **Gruppen-ID:** `scripting` · **Standardmäßig aktiv:** Nein · **Risikostufe:** hoch · **Werkzeuge:** 7

**Führt Python-Skripte aus, liest und speichert Python-Skriptressourcen und schlägt das Python-`api`-Modul nach.**

Führt Python-Skripte in Vectorworks aus, liest und speichert die Python-Skriptressourcen des aktiven Dokuments und schlägt das von Skripten verwendete Python-`api`-Modul nach. runPythonScript führt Python-Code aus, runScript eine gespeicherte Python-Skriptressource; listScripts und getScript lesen Skriptressourcen (Name, Sprache, Palette, Text); saveScript erstellt oder aktualisiert eine Python-Skriptressource, ohne sie auszuführen; describePythonApi gibt den Hilfetext einer `api`-Klasse, Enumeration, Funktion oder eines Elements zurück und listet ohne Namensangabe die Namen von `api` und `api.Math` auf. getPythonApiGuide gibt den Leitfaden zum Schreiben dieser Skripte abschnittsweise zurück: Lesen Sie ihn, bevor Sie ein Skript schreiben.

Schreiben Sie Skripte ausschließlich für das Python-`api`-Modul (import api, dann api.Document() und die anderen Klassen), nicht für das `vs`-Modul. Seine Namen haben kein Präfix (api.Document); schlagen Sie deshalb jede Klasse mit describePythonApi nach, bevor Sie sie verwenden. Geben Sie Ergebnisse als JSON aus (json.dumps), damit sie in `output` zurückgegeben werden. Jeder Lauf ist EIN Rückgängig-Schritt „MCP: script“: Die Aufrufe für Rückgängig-Ereignisse des Skripts selbst werden ignoriert. Daher muss das Skript registrieren, was es erstellt (doc.AddAfterSwapObject(obj.GetHandle())) und was es ändert (doc.AddBothSwapObject(handle), vor der Änderung); andernfalls kann „Rückgängig“ die Änderung nicht zurücksetzen.

Ein fehlgeschlagener Lauf wird zurückgenommen (`rolledBack`), sodass nichts von dem registrierten Inhalt erhalten bleibt: Korrigieren Sie das Skript und führen Sie es erneut aus. Änderungen, die das Skript nicht registriert hat, können nicht zurückgenommen werden. Ein Skript darf niemals auf Benutzereingaben warten (GetPt, Dialoge); eine Endlosschleife lässt Vectorworks einfrieren. Ein Lauf wird abgelehnt, während ein anderes Skript ausgeführt wird oder ein Rückgängig-Ereignis geöffnet ist. Ein Skript mit mehr als 250 Zeilen, das etwas löscht oder ein Datensatzformat ändert, wird erst ausgeführt, nachdem der Benutzer dies in Vectorworks bestätigt hat.

Skripte werden mit den Rechten des Benutzers ausgeführt, jetzt oder später über die Skriptpalette: Fragen Sie vor jedem Lauf den Benutzer und erklären Sie, was das Skript tun wird. Teilen Sie ihm mit, was und wo Sie gespeichert haben. Deshalb hat die Gruppe die Risikostufe `high` und ist standardmäßig deaktiviert. Verwenden Sie sie nur, wenn der Benutzer Sie auffordert, ein Skript auszuführen, zu lesen, zu schreiben oder zu dokumentieren. Jeder Aufruf von saveScript ist ein eigener, benannter Vectorworks-Rückgängig-Schritt.

| Werkzeug | Wirkung | Risiko | Zusammenfassung |
|---|---|---|---|
| [`listScripts`](#listscripts) | Nur lesend | niedrig | Listet die Skriptressourcen des Dokuments auf. |
| [`getScript`](#getscript) | Nur lesend | niedrig | Liest eine Skriptressource, ohne sie auszuführen. |
| [`saveScript`](#savescript) | Bearbeitung | mittel | Erstellt oder aktualisiert eine Python-Skriptressource, ohne sie auszuführen. |
| [`describePythonApi`](#describepythonapi) | Nur lesend | niedrig | Gibt den Hilfetext des Python-`api`-Moduls oder eines seiner Namen zurück. |
| [`getPythonApiGuide`](#getpythonapiguide) | Nur lesend | niedrig | Gibt einen Abschnitt des Leitfadens zum Schreiben von Python-Skripten zurück. |
| [`runPythonScript`](#runpythonscript) | Skriptausführung | hoch | Führt Python-Code in Vectorworks aus. |
| [`runScript`](#runscript) | Skriptausführung | hoch | Führt eine gespeicherte Python-Skriptressource aus. |

### listScripts

Listet die Skriptressourcen des Dokuments auf.

> **Wirkung:** Nur lesend · **Risiko:** niedrig · **Rückgängig:** keiner · **In runToolBatch:** zulässig

**Einzelheiten**

Listet die Skriptressourcen des aktiven Dokuments nach Namen sortiert auf: `name`, `language` (`python` oder `vectorscript`) und `palette` (Name der Skriptpalette, in der das Skript enthalten ist). Die Liste wird mit `limit` (Standardwert 200) und `offset` seitenweise ausgegeben; `count` ist die Gesamtzahl und `truncated` gibt an, ob weitere Einträge folgen; `countOnly` gibt nur die Anzahl zurück. Es wird nichts ausgeführt oder geändert.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `limit` | integer |  | Seitennavigation: die maximale Anzahl zurückzugebender Elemente (mindestens 1). Siehe [Seitennavigation](Common.md#seitennavigation). |
| `offset` | integer |  | Seitennavigation: die Anzahl zu überspringender Elemente (Standardwert 0). |
| `countOnly` | boolean |  | Seitennavigation: Gibt nur die Anzahlen, nicht die Elemente zurück. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `scripts` | Diese Seite der Skriptressourcen, nach Namen sortiert, als Liste von `{ "name", "language", "palette" }`. `language` ist `unknown`, wenn es nicht gelesen werden kann. Bei `countOnly` ausgelassen. |
| `count`, `returned`, `offset`, `limit`, `truncated`, `nextOffset` | Seitennavigationsschlüssel (siehe [Seitennavigation](Common.md#seitennavigation)). |


### getScript

Liest eine Skriptressource, ohne sie auszuführen.

> **Wirkung:** Nur lesend · **Risiko:** niedrig · **Rückgängig:** keiner · **In runToolBatch:** zulässig

**Einzelheiten**

Liest die Skriptressource `name` (1 bis 63 Zeichen) aus: `name`, `language` (`python` oder `vectorscript`), `palette` und `text` mit LF-Zeilenumbrüchen. Das Skript wird nicht ausgeführt. Fehler: `name` fehlt, ist leer, kein String oder länger als 63 Zeichen; es gibt keine Skriptressource mit diesem Namen (eine gespeicherte Ansicht oder ein anderes Objekt mit diesem Namen ist kein Skript); der Skripttext ist größer als 256 KB.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `name` | string | Ja | 1 bis 63 Zeichen. |

### saveScript

Erstellt oder aktualisiert eine Python-Skriptressource, ohne sie auszuführen.

> **Wirkung:** Bearbeitung · **Risiko:** mittel · **Rückgängig:** ein Schritt „MCP: saveScript“ · **In runToolBatch:** ja

**Einzelheiten**

Erstellt oder aktualisiert die Python-Skriptressource `name` (1 bis 63 Zeichen) mit `code` (höchstens 256 KB UTF-8, keine NUL-Zeichen), OHNE sie auszuführen; schreiben Sie den Code ausschließlich für das Python-`api`-Modul. Ein neues Skript wird in der Skriptpalette `palette` (1 bis 63 Zeichen, Standardwert „MCP Scripts“) erstellt; eine noch nicht vorhandene Palette wird erstellt und geöffnet (`paletteCreated`: true).

Wenn bereits ein Skript mit diesem Namen existiert, wird nur dessen Text ersetzt: Palette und Sprache bleiben erhalten und ein angegebenes `palette` wird ignoriert (`paletteIgnored`: true). Ein vorhandenes VectorScript-Skript wird niemals geändert. Gibt `name`, `language`, `palette`, `created` und `codeLength` (UTF-8-Bytes von `code`) zurück. Eine Skriptpalette kann weiterhin eine kompilierte Kopie eines zuvor ausgeführten Skripts ausführen, bis das Skript in Vectorworks bearbeitet oder das Dokument erneut geöffnet wird.

**Fehler:** `name`, `code` oder `palette` fehlt, ist kein String oder überschreitet die jeweilige Grenze; `name` wird von einem anderen Objekt (einschließlich einer Skriptpalette) verwendet; `palette` entspricht `name` oder dem Namen eines Objekts, das keine Skriptpalette ist; das vorhandene Skript ist ein VectorScript-Skript.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `name` | string | Ja | 1 bis 63 Zeichen. |
| `code` | string | Ja | Höchstens 256 KB UTF-8, keine NUL-Zeichen. |
| `palette` | string |  | 1 bis 63 Zeichen, Standardwert „MCP Scripts“. |

### describePythonApi

Gibt den Hilfetext des Python-`api`-Moduls oder eines seiner Namen zurück.

> **Wirkung:** Nur lesend · **Risiko:** niedrig · **Rückgängig:** keiner · **In runToolBatch:** zulässig

**Einzelheiten**

Schlägt das von Skripten verwendete Python-`api`-Modul mithilfe eines festgelegten, schreibgeschützten Python-Skripts nach: Nichts in den Argumenten wird als Code ausgeführt. `name` (optional) ist ein durch Punkte getrennter Name, der vom `api`-Modul aus aufgelöst wird; das Präfix `api.` kann optional vorangestellt werden. Er besteht aus 1 bis 8 Teilen mit Buchstaben, Ziffern und `_`, die nicht mit einer Ziffer beginnen, und ist höchstens 128 Zeichen lang. Python-Namen haben kein Präfix: `Document`, `Document.StartUndoEvent`, `WallObject.HeightBound` oder `Math.Point2D`, nicht `CDocument`.

Gibt `text` zurück: die Hilfe für die Klasse, Enumeration, Funktion oder das Element in Klartext, wie von pydoc ausgegeben (eine Konstante zeigt ihren Wert; das Untermodul `Math` listet seine Namen auf), auf 256 KB begrenzt (`truncated`: true). Ohne `name` listet `text` die Namen der Module `api` und `api.Math` nach Typ auf (Module, Klassen, Enumerationen, Funktionen, Konstanten): Verwenden Sie die Liste, um Klassennamen zu finden.

**Fehler:** `name` ist kein String oder kein gültiger, durch Punkte getrennter Name (wird abgelehnt, bevor ein Skript ausgeführt wird); „unknown api name“; die Python-Engine kann derzeit nicht ausgeführt werden (kein Dokument, ein anderes Skript wird ausgeführt, Engine nicht verfügbar) oder die Suche ist fehlgeschlagen.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `name` | string |  | Ein punktierter Name, der im Modul `api` aufgelöst wird, optional mit vorangestelltem `api.`: 1 bis 8 Teile aus Buchstaben, Ziffern und `_`, die nicht mit einer Ziffer beginnen; höchstens 128 Zeichen. Ohne diesen Wert listet `text` die Modulnamen auf. Eine leere Zeichenfolge oder `null` gilt als fehlendes `name`. Die 128 Zeichen schließen ein vorangestelltes `api.` ein. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `name` | Gesuchter Name ohne vorangestelltes `api.`. Nur vorhanden, wenn `name` angegeben wurde. |
| `text` | Hilfetext. |
| `truncated` | `true`, wenn `text` bei 256 KB abgeschnitten wurde. |


### getPythonApiGuide

Gibt einen Abschnitt des Leitfadens zum Schreiben von Python-Skripten zurück.

> **Wirkung:** Nur lesend · **Risiko:** niedrig · **Rückgängig:** keiner · **In runToolBatch:** zulässig

**Einzelheiten**

Gibt den Leitfaden zum Schreiben von Vectorworks-Python-Skripten mit dem `api`-Modul abschnittsweise als Markdown-Text mit LF-Zeilenumbrüchen zurück. Es wird nichts ausgeführt oder geändert. Rufen Sie das Werkzeug zunächst ohne `section` auf: `text` enthält dann den Anfang des Leitfadens (Titel, Inhaltsverzeichnis und Einführung), `sections` listet die Abschnitte 1 bis 6 auf (`section`, `title` und `bytes`: die Größe des Texts) und `reference` gibt an, wo Abschnitt 7 zu finden ist.

Die Abschnitte: 1 Regeln; 2 Wo sich Elemente befinden; 3 Rückgängig, einschließlich der Regeln für über MCP ausgeführte Skripte am Ende (Lesen Sie vor dem ersten runPythonScript die Abschnitte 1 und 3); 4 Beispiele; 5 Werkzeuge, Menüs und die Objekt-Info-Palette; 6 Fallstricke. Mit `section` (Ganzzahl von 1 bis 6) wird der entsprechende Abschnitt zurückgegeben: `section`, `title` und `text` (von der Überschrift „## n. “ bis zum nächsten Abschnitt).

`truncated` ist true, wenn ein `text` bei 256 KB abgeschnitten wurde. Abschnitt 7 (Referenz) wird nicht zurückgegeben: Wenn der Leitfaden auf Abschnitt 7 oder eine andere .md-Seite verweist, schlagen Sie die Klasse, Funktion oder das Element mit describePythonApi nach.

**Fehler:** `section` ist keine Ganzzahl von 1 bis 6; Abschnitt 7; der Leitfaden ist nicht verfügbar (fehlt in den Vectorworks-Anwendungsressourcen, ist kein gültiges UTF-8 oder enthält nicht alle nummerierten Abschnitte): Verwenden Sie stattdessen describePythonApi.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `section` | integer |  | Eine Ganzzahl von 1 bis 6. |

### runPythonScript

Führt Python-Code in Vectorworks aus.

> **Wirkung:** Skriptausführung · **Risiko:** hoch · **Rückgängig:** ein Schritt „MCP: script“ · **In runToolBatch:** nein

**Einzelheiten**

Führt `code` als Python-Skript in Vectorworks aus: höchstens 256 KB UTF-8, keine NUL-Zeichen.

**HOHES RISIKO:** Teilen Sie dem Benutzer vor jedem Lauf mit, was das Skript tun wird, und bitten Sie um Erlaubnis. Schreiben Sie den Code ausschließlich für das Python-`api`-Modul (import api; nicht `vs`) und schlagen Sie seine Namen mit describePythonApi nach (zum Beispiel api.Document). Geben Sie Ergebnisse als JSON aus (print(json.dumps(...)), damit sie in `output` zurückgegeben werden. Lesen Sie vor dem ersten Lauf die Abschnitte 1 und 3 des Leitfadens mit getPythonApiGuide: Abschnitt 3 endet mit den Regeln für über MCP ausgeführte Skripte.

**Rückgängig:** Der gesamte Lauf ist EIN Rückgängig-Schritt „MCP: script“. Die Aufrufe des Skripts für StartUndoEvent, NameUndoEvent, EndUndoEvent und RevertUndoEvent werden ignoriert. Das Skript muss registrieren, was es erstellt (doc.AddAfterSwapObject(obj.GetHandle()), nach dem Erstellen) und was es ändert (doc.AddBothSwapObject(handle), VOR der Änderung); andernfalls kann „Rückgängig“ die Änderung nicht zurücksetzen. Delete() muss nicht registriert werden. Ein fehlgeschlagener Lauf wird zurückgenommen (`rolledBack`: true, kein Rückgängig-Schritt); nichts von dem registrierten Inhalt bleibt erhalten: Korrigieren Sie das Skript und führen Sie es erneut aus. Änderungen, die das Skript nicht registriert hat, können nicht zurückgenommen werden. Warten Sie niemals auf Benutzereingaben (GetPt, Dialoge): Der Lauf endet dann mit `Waiting`, und es kann kein Skript ausgeführt werden, bis der Benutzer den Vorgang abgeschlossen hat. Eine Endlosschleife lässt Vectorworks einfrieren: Skripte werden im Hauptthread ausgeführt. Das Skript wird nicht ausgeführt (`NotStarted`, kein Rückgängig-Schritt), während ein anderes Skript läuft oder ein Rückgängig-Ereignis geöffnet ist (ein anderer Vectorworks-Vorgang läuft: Versuchen Sie es später erneut). Ein Skript mit mehr als 250 Zeilen, das etwas löscht oder ein Datensatzformat ändert, wird erst ausgeführt, nachdem der Benutzer in einer Vectorworks-Warnmeldung „Ausführen“ auswählt. „Abbrechen“ oder eine Warnmeldung, die aktuell nicht angezeigt werden kann, gibt `NotStarted` mit dem Grund zurück. Umgehen Sie diese Prüfung niemals. Gibt `status` (Succeeded, Failed, NotStarted oder Waiting), `output` (ausgegebener Text) und `errors` (Fehlerablaufverfolgungen) zurück, jeweils auf 256 KB begrenzt (`outputTruncated`, `errorsTruncated`), außerdem `undoStep` (true, wenn der Lauf der Rückgängig-Schritt `undoName` ist), `rolledBack` für einen fehlgeschlagenen Lauf oder einen Lauf, der nicht gestartet wurde (true, wenn der registrierte Inhalt zurückgenommen wurde), `err`, wenn das Skript fehlgeschlagen ist oder nicht ausgeführt wurde, `note` für Waiting und `warning`, wenn nach dem Lauf noch ein Rückgängig-Ereignis geöffnet ist.

**Fehler:** `code` fehlt, ist leer, kein String, größer als 256 KB oder enthält NUL-Zeichen.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `code` | string | Ja | Nicht leer, höchstens 256 KB UTF-8 und ohne NUL-Zeichen. |

### runScript

Führt eine gespeicherte Python-Skriptressource aus.

> **Wirkung:** Skriptausführung · **Risiko:** hoch · **Rückgängig:** ein Schritt „MCP: script“ · **In runToolBatch:** nein

**Einzelheiten**

Führt den aktuellen Text der gespeicherten Python-Skriptressource `name` (1 bis 63 Zeichen) aus, zum Beispiel ein mit saveScript gespeichertes Skript, und zwar wie runPythonScript den `code`: EIN Rückgängig-Schritt „MCP: script“. Ein fehlgeschlagener Lauf wird zurückgenommen (`rolledBack`), sodass nichts von dem registrierten Inhalt erhalten bleibt: Korrigieren Sie das Skript (saveScript) und führen Sie es erneut aus. Änderungen, die das Skript nicht registriert hat, können nicht zurückgenommen werden.

Es gelten dieselben Skriptregeln, Ablehnungen und Bestätigungsanforderungen (die den Text des Skripts prüfen) und dasselbe Ergebnis; zurückgegeben wird `name`.

**HOHES RISIKO:** Teilen Sie dem Benutzer vor jedem Lauf mit, welches Skript ausgeführt wird und was es tut, und bitten Sie um Erlaubnis.

**Fehler:** `name` fehlt, ist leer, kein String oder länger als 63 Zeichen; es gibt keine Skriptressource mit diesem Namen (eine gespeicherte Ansicht oder ein anderes Objekt mit diesem Namen ist kein Skript); das Skript ist ein VectorScript-Skript (nur Python-Skripte können ausgeführt werden).

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `name` | string | Ja | 1 bis 63 Zeichen. |

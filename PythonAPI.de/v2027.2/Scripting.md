[English](../../PythonAPI/v2027.2/Scripting.md) • **Deutsch** • [日本語](../../PythonAPI.ja/v2027.2/Scripting.md)

# Scripting — Scripts und Scriptpaletten

> **Python-Modul:** `api` · **Version:** Vectorworks 2027 Update 2

[Zurück zum Index](README.md)

Die Klassen für Scripts: `ScriptResource` ist ein im aktuellen Dokument gespeichertes VectorScript- oder Python-Script (erzeugen, suchen, lesen, ändern und löschen), und `ScriptPalette` ist eine Scriptpalette, eine benannte Gruppe von Scripts, die Vectorworks als frei schwebende Palette und als Scriptordner im Zubehör-Manager anzeigt.

Scripts können über diese API erzeugt, gelesen, geändert und organisiert werden; ihre Ausführung ist nicht Teil der API.

## Inhaltsverzeichnis

- [Überblick](#überblick)
- [Klassen](#klassen)
  - [ScriptResource](#scriptresource)
  - [ScriptPalette](#scriptpalette)
- [Aufzählungen](#aufzählungen)
  - [ScriptLanguage](#scriptlanguage)

## Überblick

| Name | Art | Erbt von | Zusammenfassung |
|---|---|---|---|
| [`ScriptResource`](#scriptresource) | Klasse |  | Ein Script, identifiziert durch sein Handle. |
| [`ScriptPalette`](#scriptpalette) | Klasse |  | Eine Scriptpalette, identifiziert durch ihr Handle. |
| [`ScriptLanguage`](#scriptlanguage) | IntEnum |  | Sprache eines Scripts. |

## Klassen

### ScriptResource

> **Vollständiger Name:** `api.ScriptResource` · **Erbt von:** `api.Object`

Ein Script, identifiziert durch sein Handle. Wie jede Objektklasse dieser API ist es eine schlanke Sicht: Sein Kopieren kopiert nicht das Script, und das Löschen des Python-Objekts löscht nicht das Script. Wird es aus einem Handle erzeugt, das nicht auf ein Script verweist, entsteht ein ungültiges Objekt (`IsValid()` == `False`); Abfragemethoden geben dann `None` und Setzmethoden / Operationen `False` zurück. Zeichenfolgen sind UTF-8-kodiert; Scripttexte verwenden "\n" als Zeilenumbruch.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `ScriptResource(hScript: Handle)` | Verweist auf das vorhandene Script `hScript`; prüfen Sie vor der Verwendung `IsValid()`. |

**Methoden**

*Typ*

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | `True`, wenn das Handle auf ein Script verweist (gesicherte Darstellungen zählen nicht dazu). |

*Nachschlagen*

| Methode | Beschreibung |
|---|---|
| `FromName(name: str) -> ScriptResource` *statisch* | Script des aktuellen Dokuments mit diesem Namen; ungültig, wenn keines vorhanden ist. |
| `GetAll() -> list[ScriptResource]` *statisch* | Alle Scripts des aktuellen Dokuments, nach Namen sortiert. |

*Erzeugung*

| Methode | Beschreibung |
|---|---|
| `Create(name: str, paletteName: str, text: str, language: ScriptLanguage) -> ScriptResource` *statisch* | Erzeugt ein Script in der Scriptpalette `paletteName`; eine fehlende Palette wird zuerst erzeugt und geöffnet. Schlägt fehl (ungültiges Objekt), wenn `name` oder `paletteName` leer oder länger als 63 Zeichen ist, wenn beide gleich sind, wenn ein Objekt des Dokuments bereits `name` verwendet oder wenn `paletteName` ein Objekt bezeichnet, das keine Scriptpalette ist. Rückgängig-Funktion: Vectorworks registriert eine neue Palette, aber nicht das neue Script. Registrieren Sie das Script innerhalb eines Rückgängig-Ereignisses mit `Document.AddAfterSwapObject`; registrieren Sie die Palette nicht erneut. |

*Identität*

| Methode | Beschreibung |
|---|---|
| `GetHandle() -> Handle` | Handle des Scripts. |
| `IsValid() -> bool` | True, wenn dieses Objekt auf ein vorhandenes Script verweist. |
| `GetName() -> str \| None` | Gibt den Namen zurück. |
| `SetName(name: str) -> bool` | Benennt das Script um; schlägt fehl, wenn der Name länger als 63 Zeichen ist oder ein anderes Objekt ihn bereits verwendet. |

*Script*

| Methode | Beschreibung |
|---|---|
| `GetLanguage() -> ScriptLanguage \| None` | Gibt die Sprache zurück. |
| `GetText() -> str \| None` | Gibt den Text zurück. |
| `SetText(text: str) -> bool` | Ersetzt den Text und behält die Sprache bei. Eine Scriptpalette behält eine kompilierte Kopie eines ausgeführten Scripts und führt diese Kopie aus, wenn der Benutzer das Script erneut aus der Palette startet, bis das Script in Vectorworks bearbeitet oder das Dokument erneut geöffnet wird. Execute führt immer den aktuellen Text aus. |
| `SetText(text: str, language: ScriptLanguage) -> bool` | Ersetzt den Text und die Sprache (siehe SetText oben). |

*Scriptpalette*

| Methode | Beschreibung |
|---|---|
| `GetPalette() -> ScriptPalette` | Palette, die das Script enthält. |

*Lebensdauer*

| Methode | Beschreibung |
|---|---|
| `Delete(useUndo: bool = True) -> bool` | Löscht das Script aus dem Dokument; das Objekt wird ungültig. Schlägt fehl, solange ein Script ausgeführt wird, da das laufende Script das zu löschende sein könnte. |

**Operatoren und Python-Protokolle**

| Operator | Methode | Beschreibung |
|---|---|---|
| `bool()` | `__bool__() -> bool` | `bool(a)`: True, wenn das Objekt gültig ist (entspricht `IsValid()`). |
| `==` | `__eq__(o: ScriptResource) -> bool` | `a == b`: True, wenn beide Objekte auf dasselbe Script verweisen. |
| `!=` | `__ne__(o: ScriptResource) -> bool` | `a != b`: True, wenn die Objekte auf unterschiedliche Scripts verweisen. |

### ScriptPalette

> **Vollständiger Name:** `api.ScriptPalette` · **Erbt von:** `api.Object`

Eine Scriptpalette, identifiziert durch ihr Handle. Eine schlanke Sicht wie ScriptResource. Wird sie aus einem Handle erzeugt, das nicht auf eine Scriptpalette verweist, entsteht ein ungültiges Objekt (`IsValid()` == `False`); Abfragemethoden geben dann `None` und Setzmethoden / Operationen `False` zurück.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `ScriptPalette(hPalette: Handle)` | Verweist auf die vorhandene Scriptpalette `hPalette`; prüfen Sie vor der Verwendung `IsValid()`. |

**Methoden**

*Typ*

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | `True`, wenn das Handle auf eine Scriptpalette verweist (die Palette „Darstellungen“ mit den gesicherten Darstellungen zählt nicht dazu). |

*Nachschlagen*

| Methode | Beschreibung |
|---|---|
| `FromName(name: str) -> ScriptPalette` *statisch* | Scriptpalette des aktuellen Dokuments mit diesem Namen; ungültig, wenn keine vorhanden ist. |
| `GetAll() -> list[ScriptPalette]` *statisch* | Alle Scriptpaletten des aktuellen Dokuments, nach Namen sortiert. |

*Identität*

| Methode | Beschreibung |
|---|---|
| `GetHandle() -> Handle` | Handle der Scriptpalette. |
| `IsValid() -> bool` | True, wenn dieses Objekt auf eine vorhandene Scriptpalette verweist. |
| `GetName() -> str \| None` | Gibt den Namen zurück. |
| `SetName(name: str) -> bool` | Benennt die Palette um; schlägt fehl, wenn der Name länger als 63 Zeichen ist oder ein anderes Objekt ihn bereits verwendet. |

*Scripts*

| Methode | Beschreibung |
|---|---|
| `GetScripts() -> list[ScriptResource]` | Scripts der Palette in Palettenreihenfolge. |
| `GetScriptCount() -> int` | Anzahl der Scripteinträge. |

*Anzeige*

| Methode | Beschreibung |
|---|---|
| `SetOpen(isOpen: bool) -> bool` | Zeigt die frei schwebende Palette an (`True`) oder schließt sie (`False`). |

*Lebensdauer*

| Methode | Beschreibung |
|---|---|
| `Delete(useUndo: bool = True) -> bool` | Löscht die Palette mit allen ihren Scripts; das Objekt wird ungültig. Schlägt fehl, solange ein Script ausgeführt wird, da das laufende Script eines der zu löschenden sein könnte. |

**Operatoren und Python-Protokolle**

| Operator | Methode | Beschreibung |
|---|---|---|
| `bool()` | `__bool__() -> bool` | `bool(a)`: True, wenn das Objekt gültig ist (entspricht `IsValid()`). |
| `==` | `__eq__(o: ScriptPalette) -> bool` | `a == b`: True, wenn beide Objekte auf dieselbe Scriptpalette verweisen. |
| `!=` | `__ne__(o: ScriptPalette) -> bool` | `a != b`: True, wenn die Objekte auf unterschiedliche Scriptpaletten verweisen. |

## Aufzählungen

### ScriptLanguage

> **Vollständiger Name:** `api.ScriptLanguage` · **Art:** `IntEnum`

Sprache eines Scripts.

| Element | Wert | Beschreibung |
|---|---|---|
| `VectorScript` | `0` | Die Pascal-ähnliche Skriptsprache von Vectorworks. |
| `Python` | `1` | Python mit den Vectorworks-Modulen "vs" und "api". |

---

[Zurück zum Index](README.md) · [Nach oben](#scripting--scripts-und-scriptpaletten)

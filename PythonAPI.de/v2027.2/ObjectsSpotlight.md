[English](../../PythonAPI/v2027.2/ObjectsSpotlight.md) • **Deutsch** • [日本語](../../PythonAPI.ja/v2027.2/ObjectsSpotlight.md)

# ObjectsSpotlight — Scheinwerfer und GDTF-Gerätetypen

> **Python-Modul:** `api` · **Version:** Vectorworks 2027 Update 2

[Zurück zum Index](README.md)

Die Spotlight-Klassen (sie erfordern Spotlight). `LightingDeviceObject` ist ein Scheinwerfer im Lichtplan ("Lighting Device"), der anhand eines Scheinwerfersymbols, eines GDTF-Gerätetyps oder beidem gezeichnet wird. `GDTFLibrary` listet die für Spotlight verfügbaren GDTF-Gerätetypen auf und importiert `.gdtf`-Dateien in die Zeichnung.

Der allgemeine Parameterzugriff wird von [`ParametricObject`](ObjectPrimitives.md#parametricobject) bereitgestellt.

## Inhaltsverzeichnis

- [Überblick](#überblick)
- [Klassen](#klassen)
  - [LightingDeviceObject](#lightingdeviceobject)
  - [GDTFLibrary](#gdtflibrary)
    - [GDTFLibrary.Entry](#gdtflibraryentry)
    - [GDTFLibrary.ImportResult](#gdtflibraryimportresult)

## Überblick

| Name | Art | Erbt von | Zusammenfassung |
|---|---|---|---|
| [`LightingDeviceObject`](#lightingdeviceobject) | Klasse | [`ParametricObject`](ObjectPrimitives.md#parametricobject) | Plug-in-Objekt Scheinwerfer (universeller Name "Lighting Device") aus dem Plug-in Spotlight. |
| [`GDTFLibrary`](#gdtflibrary) | Klasse |  | Spotlight bekannte GDTF-Gerätetypen (General Device Type Format, DIN SPEC 15800). |
| [`GDTFLibrary.Entry`](#gdtflibraryentry) | Klasse (verschachtelt) |  | Ein DMX-Modus eines verfügbaren Gerätetyps. |
| [`GDTFLibrary.ImportResult`](#gdtflibraryimportresult) | Klasse (verschachtelt) |  | Ergebnis von Import: die GDTF-Symboldefinition, ihr GDTF-Name, ob sie durch diesen Aufruf importiert wurde und ob die Datei als GDTF gelesen wurde. |

## Klassen

### LightingDeviceObject

> **Vollständiger Name:** `api.LightingDeviceObject` · **Erbt von:** [`ParametricObject`](ObjectPrimitives.md#parametricobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Plug-in-Objekt Scheinwerfer (universeller Name "Lighting Device") aus dem Plug-in Spotlight.

Der allgemeine Parameterzugriff (GetParamString / SetParamString / ..., GetParameters, GetParamChoices) wird von ParametricObject bereitgestellt.

Ein Scheinwerferobjekt stellt einen Scheinwerfer (oder einen mehrzelligen Scheinwerfer) in einem Lichtplan dar. Seine Grafik stammt aus einem Scheinwerfersymbol ("Symbol Name") und/oder einem GDTF-Gerätetyp ("GDTF Fixture Name" mit "UseGDTFGeometry"). Der GDTF-Gerätetyp liefert außerdem den DMX-Modus und den Kanalumfang.

Typischer GDTF-Arbeitsablauf (verfügbare Gerätetypen siehe GDTFLibrary):

1. `GDTFLibrary.Import`(path) — - die .gdtf-Datei in die Zeichnung importieren (ein Scheinwerfer kann nur einen Gerätetyp verwenden, der sich in der Zeichnung befindet)
2. `LightingDeviceObject.Create`(position) — - ein Gerät ohne Scheinwerfersymbol
3. device.SetGDTF(gdtfName, mode) — - Gerätetyp, DMX-Modus und Kanalumfang
4. device.SetUseGDTFGeometry(`True`) — - das GDTF-3D-Modell zeichnen
5. device.`Reset()` — - das Gerät neu berechnen

Häufig verwendete Parameter mit benannten Zugriffsmethoden:

- "Inst Type" — Scheinwerfertyp, der in der Infopalette und in Auswertungen angezeigt wird
- "Symbol Name" — Scheinwerfersymbol des Geräts (hier nur lesbar: Symbole in Spotlight zuweisen)
- "GDTF Fixture Name" — GDTF-Name des Gerätetyps (`GDTFLibrary.Entry.gdtfName`)
- "GDTF Fixture Mode" — "<DMX mode>.<GDTF name>"; GetGDTFMode gibt nur den DMX-Modus zurück
- "Num Channels" — DMX-Kanalumfang
- "UseGDTFGeometry" — 3D-Modell des GDTF-Gerätetyps zeichnen

Weitere Parameter für GetParam.../SetParam... (Parametername | Typ | Hinweise). Mehrzellige Geräte speichern mehrere dieser Werte je Zelle; die Datenbank enthält die Werte der ersten Zelle.

- "Device Type" — Auswahlliste — Light / ...
- "Purpose", "Position", "Unit Number", "Color", "Dimmer", "Channel" — Zeichenfolge
- "Universe", "DMX Address", "Absolute Address", "UniverseAddress" — Zeichenfolge / int
- "Circuit Number", "Circuit Name", "System", "Breaker ID" — Zeichenfolge
- "Wattage", "Voltage", "Weight", "Cost", "Time", "Mark" — Zeichenfolge
- "Frame Size", "Template", "Template2", "TemplateRot1", "TemplateRot2" — Zeichenfolge / reell (Grad)
- "Field Angle", "Field Angle 2", "Beam Angle", "Beam Angle 2" — reell (Grad)
- "Lamp Rotation Angle", "Fall off distance", "Throw Distance" — reell
- "Draw Beam", "Draw Beam as Solid", "Use Vertical Beam", "Light On" — bool
- "Focus", "Pan", "Tilt" — Zeichenfolge / reell (Grad)
- "User Field 1" .. "User Field 6" — Zeichenfolge
- "Fixture Mode", "Vision Fixture Name" — Zeichenfolge (Vision-Gerätebibliothek)
- "GDTF Fixture Type ID", "GDTF Fixture Custom ID" — Zeichenfolge
- "Lightwright ID", "UID" — Zeichenfolge

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `LightingDeviceObject(h: Handle)` | Verweist auf den vorhandenen Scheinwerfer `h`; vor der Verwendung `IsValid()` prüfen. |

**Methoden**

*Allgemein*

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | True, wenn `h` auf ein Objekt des von dieser Klasse dargestellten Typs verweist. |
| `Create(position: Math.Point2D, angle: float = 0.0) -> LightingDeviceObject` *statisch* | Erzeugt einen Scheinwerfer ohne Scheinwerfersymbol an `position`, um `angle` gedreht (Bogenmaß), auf der aktiven Ebene / im aktuellen Container und berechnet ihn einmal neu. Weisen Sie mit SetGDTF einen GDTF-Gerätetyp zu und rufen Sie anschließend `Reset()` auf. |
| `Duplicate() -> LightingDeviceObject` | Dupliziert den Scheinwerfer in der Zeichnung und gibt die Kopie zurück. |
| `GetInstrumentType() -> str \| None` | Gibt den Scheinwerfertyp zurück. |
| `SetInstrumentType(value: str) -> bool` | Setzt den Scheinwerfertyp. |
| `GetSymbolName() -> str \| None` | Name des Scheinwerfersymbols des Geräts; leer bei einem Gerät ohne Symbol. |

*GDTF-Gerätetyp*

| Methode | Beschreibung |
|---|---|
| `GetGDTFName() -> str \| None` | Sein GDTF-Name (`GDTFLibrary.Entry.gdtfName`), leer, wenn dem Gerät kein GDTF-Gerätetyp zugewiesen ist. |
| `GetGDTFMode() -> str \| None` | DMX-Modus des GDTF-Gerätetyps ohne den GDTF-Namen, den das Plug-in daran anhängt. |
| `GetDMXFootprint() -> int \| None` | DMX-Kanalumfang (Anzahl der Kanäle) des Geräts. |
| `SetGDTF(gdtfName: str, mode: str = '') -> bool` | Weist den GDTF-Gerätetyp `gdtfName` (einen importierten Eintrag von `GDTFLibrary.GetAvailable`) im DMX-Modus `mode` zu – dem ersten Modus des Gerätetyps, wenn `mode` leer ist – und übernimmt seine Daten (Modus, Kanalumfang, ...), wie beim Ziehen des GDTF-Eintrags aus dem Zubehör-Manager auf das Gerät. Rufen Sie anschließend `Reset()` auf. Gibt `False` zurück, ohne das Gerät zu ändern, wenn die Zeichnung keinen Gerätetyp mit diesem Namen und Modus enthält. |
| `GetUseGDTFGeometry() -> bool \| None` | Ob das Gerät das 3D-Modell seines GDTF-Gerätetyps zeichnet. Rufen Sie nach einer Änderung `Reset()` auf. |
| `SetUseGDTFGeometry(value: bool) -> bool` | Schaltet *GDTF-Geometrie verwenden* ein oder aus. Ob das Gerät das 3D-Modell seines GDTF-Gerätetyps zeichnet. Rufen Sie nach einer Änderung `Reset()` auf. |

Geerbt: alle Elemente von [`ParametricObject`](ObjectPrimitives.md#parametricobject), [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

### GDTFLibrary

> **Vollständiger Name:** `api.GDTFLibrary` · **Erbt von:** `api.Object`

Spotlight bekannte GDTF-Gerätetypen (General Device Type Format, DIN SPEC 15800).

Verfügbar sind die in die Zeichnung importierten Gerätetypen (als GDTF-Symboldefinitionen gespeichert) und die .gdtf-Dateien im GDTF-Ordner der Spotlight-Daten in den Benutzer- und Programmordnern. Spotlight liest die Ordner einmal pro Sitzung; eine später dorthin kopierte Datei wird daher erst nach einem Neustart aufgelistet. Ein Gerätetyp muss in die Zeichnung importiert werden (Import), bevor ein Scheinwerfer ihn verwenden kann. Erfordert die Plug-ins Spotlight und GDTF; ohne sie ist die Liste leer und Import schlägt fehl.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `GDTFLibrary()` | Zustandsloses Objekt; jede Methode ist statisch und kann direkt an der Klasse aufgerufen werden. |

**Methoden**

| Methode | Beschreibung |
|---|---|
| `IsAvailable() -> bool` *statisch* | Ob die GDTF-Unterstützung von Spotlight installiert ist. |
| `GetAvailable() -> list[GDTFLibrary.Entry]` *statisch* | Jeder DMX-Modus jedes verfügbaren Gerätetyps: zuerst die importierten, dann die Dateien auf dem Datenträger. `LightingDeviceObject.SetGDTF` akzeptiert nur importierte Gerätetypen (isInDocument). |
| `Import(filePath: str, replaceExisting: bool = False) -> GDTFLibrary.ImportResult` *statisch* | Importiert die .gdtf-Datei unter `filePath` (vollständiger systemeigener Pfad) als GDTF-Symboldefinition in die Zeichnung. Ein bereits in der Zeichnung vorhandener Gerätetyp mit derselben GDTF-Typ-ID wird ersetzt, wenn `replaceExisting` den Wert `True` hat, andernfalls bleibt er unverändert (dann ist isImported gleich `False`; verwenden Sie GetAvailable, um ihn zu finden). Fragt den Benutzer niemals nach einer Bestätigung. Ein neuer Gerätetyp registriert seinen eigenen Rückgängig-Schritt, wenn eine Rückgängig-Aktion geöffnet ist; das Ersetzen eines vorhandenen Gerätetyps ändert diesen direkt, ohne seinen vorherigen Zustand für das Rückgängigmachen zu speichern. |

#### GDTFLibrary.Entry

> **Vollständiger Name:** `api.GDTFLibrary.Entry` · **Erbt von:** `api.Object`

Ein DMX-Modus eines verfügbaren Gerätetyps.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `Entry()` | Standardwert (Felder mit ihren Standardwerten). |
| `Entry(gdtfName, fixtureName, manufacturer, mode, footprint, symbolDefinition, isInDocument)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `gdtfName` | `str` | An `LightingDeviceObject.SetGDTF` zu übergebender Name. |
| `fixtureName` | `str` | Name des Gerätetyps, gefolgt von "@<revision>", sofern eine Revision vorhanden ist. |
| `manufacturer` | `str` | Hersteller des Gerätetyps. |
| `mode` | `str` | Name des DMX-Modus. |
| `footprint` | `int` | DMX-Kanäle des Modus. |
| `symbolDefinition` | `Handle` | GDTF-Symboldefinition; null bei einer nicht importierten Datei. |
| `isInDocument` | `bool` | In die Zeichnung importiert. |

#### GDTFLibrary.ImportResult

> **Vollständiger Name:** `api.GDTFLibrary.ImportResult` · **Erbt von:** `api.Object`

Ergebnis von Import.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `ImportResult()` | Standardwert (Felder mit ihren Standardwerten). |
| `ImportResult(symbolDefinition, gdtfName, isImported, isValidFile)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `symbolDefinition` | `Handle` | Durch den Import erzeugte oder ersetzte GDTF-Symboldefinition. |
| `gdtfName` | `str` | GDTF-Name des importierten Gerätetyps für `LightingDeviceObject.SetGDTF`. |
| `isImported` | `bool` | `False`, wenn die Datei nicht gelesen wurde oder der Gerätetyp bereits in der Zeichnung vorhanden war und beibehalten wurde. |
| `isValidFile` | `bool` | Die Datei wurde als GDTF gelesen; `False` bei einer fehlenden oder ungültigen Datei. |

---

[Zurück zum Index](README.md) · [Nach oben](#objectsspotlight--scheinwerfer-und-gdtf-gerätetypen)

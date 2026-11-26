[English](../../PythonAPI/v2027.2/README.md) • **Deutsch** • [日本語](../../PythonAPI.ja/v2027.2/README.md)

# Vectorworks Python API (`api`) — Referenz für Vectorworks 2027 Update 2

Diese Referenz dokumentiert das objektorientierte Python-Modul `api`, das Vectorworks für Skripte und KI-Arbeitsabläufe bereitstellt. Sie ist nach Funktionsgruppen gegliedert: eine Seite pro Gruppe, mit einem Inhaltsverzeichnis am Anfang jeder Seite und einem einheitlichen Aufbau für alle Klassen.

## Inhaltsverzeichnis

- [Erste Schritte](#erste-schritte)
- [Konventionen](#konventionen)
  - [Module](#module)
  - [Signaturen lesen](#signaturen-lesen)
  - [Funktionen aufrufen](#funktionen-aufrufen)
  - [Wertdatensätze](#wertdatensätze)
  - [Aufzählungen](#aufzählungen)
  - [Handles und Objekte](#handles-und-objekte)
  - [Kopieren, Ausgeben und Hashen](#kopieren-ausgeben-und-hashen)
  - [Rückruffunktionen](#rückruffunktionen)
  - [Fehler](#fehler)
- [API-Baum](#api-baum)
- [Inhalt nach Gruppen](#inhalt-nach-gruppen)
- [Stichwortverzeichnis A–Z](#stichwortverzeichnis-az)
- [Seitenaufbau](#seitenaufbau)
- [Statistik](#statistik)

## Erste Schritte

```python
import api
from api.Math import Point2D

doc = api.Document()
if doc.IsOpen():
    for h in doc.GetSelection():
        obj = api.PrimitiveObject(h)
        print(obj.GetName(), obj.GetBounds())
```

- Beginnen Sie mit [`api.Document`](DocumentAccess.md#document): die aktive Zeichnung, ihre aktivierten Objekte, Ebenen, Geschosse, Klassen und Einstellungen.
- Gemeinsame Operationen für Zeichnungsobjekte sind unter [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) dokumentiert. Beachten Sie die Vererbungsangaben der jeweiligen Klasse: Beispielsweise ist [`WorksheetObject`](ObjectsAnnotation.md#worksheetobject) von `TypedResource` und nicht von `PrimitiveObject` abgeleitet.
- Rein mathematische Werte befinden sich direkt im Untermodul [`api.Math`](ObjectPrimitives.Math.md); sie erzeugen keine Zeichnungsobjekte.
- `help(api.Document)` gibt in Vectorworks die Signaturen einer Klasse aus.

Verwenden Sie für die hier beschriebenen Vectorworks-Operationen ausschließlich `api` und `api.Math`. Mischen Sie keine Aufrufe der separaten Schnittstelle `vs` darunter und verwenden Sie diese nicht als Ersatz für fehlende Funktionen. Importe aus der Standardbibliothek sind erlaubt; weisen Sie auf nicht unterstützte Operationen hin, statt API-Aufrufe zu erfinden.

[Scripts und Scriptpaletten](Scripting.md) können verwaltet werden, Scripts lassen sich jedoch nicht über `api` ausführen. Die Automatisierung bereits geöffneter Dialogfenster sowie die verzögerten Hilfsfunktionen `RunLater` / `RunOnEventLoop` sind nicht verfügbar; [das Erstellen von Dialogfenstern, Meldungen und Standarddialoge](UILayoutCreate.md) werden weiterhin unterstützt. Die vollständigen Nutzungsregeln und Anwendungsbeispiele finden Sie in [AI-CONTEXT.md](../../PythonAPI/v2027.2/AI-CONTEXT.md).

## Konventionen

| Thema | Konvention |
|---|---|
| Ergebnisse | Abfragemethoden geben `None` zurück, wenn ein Wert nicht ermittelt werden kann; Ausnahmen sind Handle-Abfragen mit einem Null-Handle, Sammlungsabfragen mit einer leeren Liste und Anzahlabfragen mit 0. Erzeugungsmethoden für Zeichnungsobjekte geben bei einem Fehlschlag ungültige Objekte zurück. Die meisten Setzmethoden und Aktionen geben `True` / `False` zurück; prüfen Sie jede Signatur und ihr Ergebnis. |
| Einheiten | Längen und Koordinaten in Welteinheiten sind Millimeter, unabhängig von den Dokumenteinheiten. Verwenden Sie `Document.UnitsToWorld` / `Document.WorldToUnits` zur Umrechnung der Dokumenteinheiten. Winkel sind im Bogenmaß gegen den Uhrzeigersinn ab +X angegeben, sofern nichts anderes vermerkt ist. |
| Ausnahmen bei Einheiten | `Marker.angle`, `DropShadow.angle` und `RoofObject.Edge.slope` verwenden Grad; `Marker.length` / `Marker.width` verwenden Zoll auf der Seite. Linienstärken mit `*Mils` verwenden 1/1000 Zoll. Direkte Winkelparameter von Plug-ins, die mit `GetParamReal` / `SetParamReal` gelesen oder geschrieben werden, verwenden Grad; Längenparameter verwenden Welteinheiten. |
| Indizes | Nullbasiert, außer Tabellenzeilen und -spalten, die einsbasiert sind. |
| Farben | Die Kanäle von `ColorRGB` liegen im Bereich 0–65535; verwenden Sie `ColorRGB.FromRGB8` / `Red8()` für 8-Bit-Werte. Farbindizes sind Palettenindizes, keine RGB-Werte. Die Deckkraft liegt im Bereich 0–100 (`api.kMaxOpacity`). |
| Zeichenfolgen | Python-`str`, als UTF-8 ausgetauscht. Namenssuchen ignorieren Groß- und Kleinschreibung; universelle Plug-in-Namen müssen jedoch exakt übergeben werden. |
| Objekt-Handles | Übergeben Sie `None` als Null-Handle-Argument. Ein zurückgegebenes Null-`api.Handle` gilt im Wahrheitswerttest als falsch: Prüfen Sie mit `if h:`, nicht mit `h is None`. Objektklassen sind schlanke Sichten auf ein Handle; `bool(obj)` entspricht `IsValid()`. |
| Rückgängig | Änderungen an der Zeichnung erfordern ein Rückgängig-Ereignis und die entsprechenden Objektregistrierungen; rein lesende Skripte dürfen kein Ereignis starten. Informationen zu `StartUndoEvent(isRevertible=True)`, zum Zurücknehmen von Änderungen und zu anwendungsverwalteten Ereignissen finden Sie im [Rückgängig-Ablauf](../../PythonAPI/v2027.2/AI-CONTEXT.md#3-undo---required-around-every-drawing-change). |
| Namen | Elemente, deren Namen Python-Schlüsselwörter sind, enden mit einem Unterstrich (`None_`); dasselbe gilt für Argumentnamen, die Schlüsselwörtern entsprechen (`from_`). |
| Wertdatensätze | Werttypen sind Kopien, die Python gehören: Ändern Sie sie und übergeben Sie sie anschließend wieder an die Setzmethode. Sie können aus Feldwerten erzeugt werden (`api.ColorRGB(red=65535)`). |
| Aufzählungen | `IntEnum` (`api.Descend` ist ein `IntFlag`); einfache Ganzzahlen werden akzeptiert. |
| Argumente | Jeder Parameter hat einen Schlüsselwortnamen; Parameter mit Standardwerten können weggelassen werden; für Wertdatensatz-Argumente werden Tupel, Listen und Dictionaries akzeptiert. |
| Signaturen | `Name(param: type = default) -> result`; *statisch* kennzeichnet statische Methoden; `T \| None` ist ein optionales Ergebnis. |

### Module

| Name | Beschreibung |
|---|---|
| `api` | Das Modul. Beginnen Sie mit `api.Document()`. |
| `api.Math` | Direktes Untermodul von `api` für eigenständige 2D-/3D-Mathematik ([Math](ObjectPrimitives.Math.md)); `import api.Math` und `from api.Math import Point2D` sind möglich. Es ist nicht unter `ObjectPrimitives` verschachtelt. |
| `api.Object` | Basisklasse jeder `api`-Klasse (siehe [Kopieren, Ausgeben und Hashen](#kopieren-ausgeben-und-hashen)). |
| `api.Handle` | Ein Vectorworks-Objekt-Handle. Prüfen Sie den Wahrheitswert zurückgegebener Handles, statt sie mit `None` zu vergleichen. |

### Signaturen lesen

Die Signaturen verwenden folgende Typen:

| Typ | Bedeutung |
|---|---|
| `bool`, `int`, `float`, `str` | In Python eingebaute Werte. Ein `int` wird akzeptiert, wenn ein `float` erwartet wird. |
| `Handle` | Ein Vectorworks-Objekt-Handle (`api.Handle`). Übergeben Sie `None` als Null-Handle-Argument; zurückgegebene Null-Handles gelten im Wahrheitswerttest als falsch. Jedes Objekt mit `GetHandle()` wird ebenfalls akzeptiert. |
| `T \| None` | Ein optionaler Wert: `None` bedeutet „kein Wert“. |
| `list[T]` | Eine Liste (als Argument wird eine Liste oder ein Tupel akzeptiert). |
| `tuple[T * N]` | Ein Tupel aus genau N Werten. |
| `tuple[A, B]` | Ein Wertepaar. |
| `dict[K, V]` | Ein Dictionary. |
| `callable(A, ...)` | Ein beliebiges aufrufbares Python-Objekt, das die aufgeführten Argumente entgegennimmt (siehe [Rückruffunktionen](#rückruffunktionen)). |
| `bytes` | `bytes`, `bytearray` oder ein beliebiger anderer Puffer (nicht `str`). |
| `type` | Eine `api`-Klasse, zum Beispiel `api.ArcObject` in `api.Document.As(api.ArcObject, h)`; geeignet sind nur Klassen mit einer statischen Methode `Is(h)` und einem Konstruktor, der ein Handle entgegennimmt. |
| `object` | Ein beliebiges Python-Objekt; die Methodenbeschreibung gibt an, was zurückgegeben wird. |
| Aufzählungsnamen | `IntEnum`- / `IntFlag`-Klassen; einfache Ganzzahlen werden akzeptiert. |
| Klassennamen | `api`-Klassen; Wertdatensatz-Argumente akzeptieren auch Tupel, Listen und Dictionaries (siehe [Wertdatensätze](#wertdatensätze)). |

Standardwerte werden als Python-Ausdrücke dargestellt (`2**64 - 1` bedeutet „keine Begrenzung“). Methoden mit mehreren gleichnamigen Zeilen akzeptieren mehrere Argumentlisten (Überladungen).

### Funktionen aufrufen

- **Überladungen:** Wenn eine Methode mehrere Argumentlisten akzeptiert, wird die erste zu den Argumenten passende verwendet: zuerst mit exakten Typen, dann mit den hier beschriebenen Konvertierungen. Wenn sich Überladungen durch Wertdatensatztypen unterscheiden, erzeugen Sie den Typ ausdrücklich: Ein Tupel für `ToolControl.Click` wählt `Point2D`; verwenden Sie daher `api.Point3D(...)` oder `api.ViewPoint(...)` für die anderen Koordinatentypen.
- **Schlüsselwörter und Standardwerte:** Jeder Parameter kann per Schlüsselwort übergeben werden (mit den Namen aus den Signaturen); Parameter mit einem Standardwert können weggelassen werden.
- **Statische Methoden:** Mit *statisch* gekennzeichnete Methoden können über die Klasse (`api.ArcObject.Create(...)`) oder eine Instanz aufgerufen werden. Wenn es für einen Namen sowohl statische als auch Instanzmethoden gibt, rufen Sie die Methode über eine Instanz auf.
- **Konvertierungen:** Ein Wertdatensatz-Argument kann als Tupel oder Liste (die Werte eines Konstruktors), als Dictionary (Feldwerte) oder als kompatibler Wertdatensatz angegeben werden (`api.Math.Point2D` und `api.Point2D` sowie `api.Math.Point3D` und `api.Point3D` lassen sich jeweils ineinander konvertieren); ein `int` wird für einen `bool` oder einen `float` akzeptiert; jedes Objekt mit einer Methode `GetHandle()` wird akzeptiert, wenn ein `Handle` erwartet wird.
- **Ergebnisse:** Ergebnisse sind neue Python-Werte, außer bei Methoden, die einen Wert direkt ändern und zurückgeben (zum Beispiel `Math.Point2D.Normalize()`): Sie geben dasselbe Python-Objekt zurück, sodass Aufrufe verkettet werden können.
- **Operatoren:** Vergleichsoperatoren und arithmetische Operatoren geben für nicht unterstützte Operanden `NotImplemented` zurück, sodass Python die Operation mit vertauschten Operanden versuchen kann.

### Wertdatensätze

Wertdatensätze (Werttypen wie `api.ColorRGB`, `api.WallObject.Heights`, `api.Math.Point2D`) sind Werte, die Python gehören. Das Ändern eines Wertdatensatzes ändert niemals die Zeichnung: Übergeben Sie ihn wieder an die zugehörige Setzmethode.

Wenn kein Konstruktor die Argumente akzeptiert, kann ein Wertdatensatz auch aus Feldwerten erzeugt werden: entweder alle Felder als Positionsargumente (in der Reihenfolge der Feldtabellen, zuerst die Felder der Basisklasse) oder beliebige Felder als Schlüsselwortargumente, zum Beispiel `api.ColorRGB(red=65535)`. Klassen ohne Konstruktoren und Felder können nicht aus Python erzeugt werden.

Ein Feld, dessen Typ selbst ein Wertdatensatz ist, wird als direkte Sicht auf seinen Besitzer gelesen (`rect.origin.x = 1` ändert `rect`); Felder anderer Typen (Zahlen, Zeichenfolgen, Listen, optionale Werte) werden als Kopien gelesen. Felder können nicht gelöscht werden.

### Aufzählungen

Aufzählungen sind `enum.IntEnum`-Klassen (`api.Descend` ist ein `enum.IntFlag`: Kombinieren Sie seine Elemente mit `|`). Verschachtelte Aufzählungen befinden sich in ihrer Klasse (`api.TextObject.HorizontalAlignment`). Elemente, deren Namen Python-Schlüsselwörter sind, enden mit `_` (`api.Descend.None_`). Einfache Ganzzahlen werden als Argumente akzeptiert, und Werte ohne zugehöriges Aufzählungselement werden als Ganzzahlen zurückgegeben.

### Handles und Objekte

Objekt-Handles sind `api.Handle`-Werte. Übergeben Sie `None` als Null-Handle-Argument, prüfen Sie zurückgegebene Handles jedoch mit `if h:`: Ein Null-Handle ist nicht `None`. Die Handle-Kompatibilität rechtfertigt kein Mischen von `api` und `vs`. Die Objektklassen sind schlanke Sichten auf ein Handle: Ihnen gehört das Zeichnungsobjekt nicht. Die meisten haben eine statische Methode `Is(h)` und einen Konstruktor, der ein Handle entgegennimmt; die Erzeugung aus einem Handle des falschen Typs ergibt ein ungültiges Objekt (`IsValid()` / `bool(obj)` ist `False`). `api.Document.As(type, h)` gibt ein typisiertes Objekt oder `None` zurück.

Die Basissichten `PrimitiveObject(h)`, `ArchitectObject(h)`, `LandmarkObject(h)` und `AnnotationObject(h)` akzeptieren jedes Handle außer einem Null-Handle; konkrete Klassen prüfen den Objekttyp. `Delete()` macht die Sicht ungültig, auf der es aufgerufen wird. Verwenden Sie niemals andere Sichten oder Handles des gelöschten Objekts.

### Kopieren, Ausgeben und Hashen

Jede `api`-Klasse ist von `api.Object` abgeleitet und erhält dadurch:

| Element | Beschreibung |
|---|---|
| `copy.copy(x)` / `copy.deepcopy(x)` | Eine Kopie des Werts. Bei einer Objektklasse wird die Sicht (das Handle) kopiert, **nicht** das Zeichnungsobjekt; verwenden Sie `Duplicate()`, um Zeichnungsobjekte zu duplizieren. Löst `TypeError` für Klassen aus, die nicht kopiert werden können (zum Beispiel `ResourceList`). |
| `repr(x)` | Wertdatensätze geben ihre Felder aus (`api.ColorRGB(red=0, green=0, blue=0)`), Objektklassen ihr Handle (`<api.ArcObject handle=0x...>`) und Instanzen, deren `__init__` nicht aufgerufen wurde, `<... (not initialized)>`. |
| `hash(x)` | Bei Objektklassen wird der Hashwert aus dem Handle gebildet, sodass sie als Dictionary-Schlüssel oder Mengenelemente dienen können; Wertdatensätze sind nicht hashbar. Zeichnungsobjekte, Ebenen, Klassen und Zubehör werden mit `==` anhand ihrer Handles verglichen. Die Gleichheit von Werttypen ist in den Operatorentabellen dokumentiert; andere Python-Objekte werden anhand ihrer Identität verglichen. |

### Rückruffunktionen

Parameter des Typs `callable(...)` nehmen jedes aufrufbare Python-Objekt entgegen (zum Beispiel bei der Traversierung `Document.ForEachObject`). Das Objekt wird synchron aufgerufen, und sein Rückgabewert wird ignoriert; es kann die Traversierung nicht vorzeitig beenden. Verwenden Sie die entsprechende listenrückgebende Methode, wenn Sie vorzeitig abbrechen möchten. Löst ein Aufruf eine Ausnahme aus, werden die übrigen Aufrufe übersprungen, und die Ausnahme wird nach Rückkehr der Methode weitergegeben.

### Fehler

Fehlschläge bei Operationen werden durch die dokumentierten Rückgabewerte gemeldet; prüfen Sie immer die Ergebnisse. Fehler bei der Python-Nutzung und Konvertierung sowie die unten aufgeführten fehlgeschlagenen Geometrieoperationen lösen die unten beschriebenen Ausnahmen aus; Ausnahmen in Rückruffunktionen werden an den Aufrufer weitergegeben.

| Situation | Python-Ausnahme |
|---|---|
| Keine Argumentliste der Methode passt zu den Argumenten | `TypeError` mit einer Auflistung aller Signaturen der Methode. |
| Erzeugen einer Klasse, die nicht aus Python erzeugt werden kann, oder Verwenden einer Instanz, deren `__init__` nicht aufgerufen wurde (zum Beispiel in einer Unterklasse) | `TypeError`. |
| Setzen eines Felds auf einen Wert des falschen Typs oder Löschen eines Felds | `TypeError`. |
| Kopieren einer Klasse, die nicht kopiert werden kann | `TypeError`. |
| Ein Index außerhalb des gültigen Bereichs eines mathematischen Werts (zum Beispiel `Polygon2D`) | `IndexError`. |
| Eine fehlgeschlagene Geometrieoperation: `Math.Polygon2D` `Union`, `Intersection`, `Difference`, `SymmetricDifference`, `Offset`; `PolyObject` `BooleanUnion`, `BooleanIntersection`, `BooleanDifference`, `BooleanSymmetricDifference`, `CombineShapes` | `RuntimeError` mit einer Meldung. |
| Ein Ergebnis, das nicht konvertiert werden kann | `RuntimeError`. |
| Das Modul konnte nicht initialisiert werden | `ImportError` bei `import api`. |

## API-Baum

`Math` ist ein direktes Untermodul von `api`. Die anderen Einträge unten sind Dokumentationsgruppen für Namen, die direkt unter `api` verfügbar sind (zum Beispiel `api.Document` und `api.PrimitiveObject`), keine Python-Untermodule. Die Dateinamen der Referenz definieren keine Python-Namensräume: `ObjectPrimitives.Math.md` dokumentiert `api.Math`.

```text
api
├── Math  (api.Math)               → ObjectPrimitives.Math.md
├── DocumentAccess                 → DocumentAccess.md
├── Attributes                     → Attributes.md
├── ObjectPrimitives               → ObjectPrimitives.md
├── Objects3D                      → Objects3D.md
├── ObjectsAnnotation              → ObjectsAnnotation.md
├── ObjectsArchitect               → ObjectsArchitect.md
├── ObjectsConnectCAD              → ObjectsConnectCAD.md
├── ObjectsLandmark                → ObjectsLandmark.md
├── ObjectsSpotlight               → ObjectsSpotlight.md
├── Resources                      → Resources.md
├── Scripting                      → Scripting.md
├── UIAutomation                   → UIAutomation.md
└── UILayoutCreate                 → UILayoutCreate.md
```

## Inhalt nach Gruppen

- **[DocumentAccess](DocumentAccess.md)** — Das aktive Dokument: aktivierte Objekte, Objekte, Ebenen, Geschosse, Klassen, Ansicht, Einheiten, Rückgängig-Funktion und Einstellungen.
  - Klassen:
    - [`TextStyleData`](DocumentAccess.md#textstyledata)
    - [`ProgramVariables`](DocumentAccess.md#programvariables)
    - [`DisplaySettings`](DocumentAccess.md#displaysettings)
    - [`EditingSettings`](DocumentAccess.md#editingsettings)
    - [`SnapSettings`](DocumentAccess.md#snapsettings)
    - [`GridSettings`](DocumentAccess.md#gridsettings)
    - [`StackLayersSettings`](DocumentAccess.md#stacklayerssettings)
    - [`UnitSettings`](DocumentAccess.md#unitsettings)
    - [`TextDefaults`](DocumentAccess.md#textdefaults)
    - [`DefaultAttributes`](DocumentAccess.md#defaultattributes)
    - [`LayerContents`](DocumentAccess.md#layercontents)
    - [`Layer`](DocumentAccess.md#layer)
    - [`StoryLevel`](DocumentAccess.md#storylevel)
    - [`StoryLevelTemplate`](DocumentAccess.md#storyleveltemplate)
    - [`Story`](DocumentAccess.md#story)
    - [`Document`](DocumentAccess.md#document)
  - Aufzählungen: [`Traverse`](DocumentAccess.md#traverse) · [`Descend`](DocumentAccess.md#descend) · [`LayerType`](DocumentAccess.md#layertype) · [`LayerVisibility`](DocumentAccess.md#layervisibility) · [`VisibilityOptions`](DocumentAccess.md#visibilityoptions) · [`StoryElevationChangeMode`](DocumentAccess.md#storyelevationchangemode) · [`UndoMethod`](DocumentAccess.md#undomethod) · [`AngularUnit`](DocumentAccess.md#angularunit) · [`TextJustification`](DocumentAccess.md#textjustification) · [`TextVerticalAlignment`](DocumentAccess.md#textverticalalignment) · [`TextLineSpacing`](DocumentAccess.md#textlinespacing)
- **[Attributes](Attributes.md)** — Stift, Füllung, Füllungszuordnung, Linienendzeichen, Schlagschatten, Objektattribute, Klassen und Attributwerttypen.
  - Klassen:
    - [`Point2D`](Attributes.md#point2d)
    - [`ColorRGB`](Attributes.md#colorrgb)
    - [`ColorPair`](Attributes.md#colorpair)
    - [`ObjectColors`](Attributes.md#objectcolors)
    - [`Marker`](Attributes.md#marker)
    - [`DropShadow`](Attributes.md#dropshadow)
    - [`WallTextures`](Attributes.md#walltextures)
    - [`RoofTextures`](Attributes.md#rooftextures)
    - [`AttributesBase`](Attributes.md#attributesbase)
    - [`PenAttributes`](Attributes.md#penattributes)
    - [`FillAttributes`](Attributes.md#fillattributes)
    - [`FillMappingAttributes`](Attributes.md#fillmappingattributes) — [`Frame`](Attributes.md#fillmappingattributesframe)
    - [`MarkerAttributes`](Attributes.md#markerattributes)
    - [`DropShadowAttributes`](Attributes.md#dropshadowattributes)
    - [`ClassAttributes`](Attributes.md#classattributes)
    - [`ObjectAttributes`](Attributes.md#objectattributes)
  - Aufzählungen: [`PenStyleKind`](Attributes.md#penstylekind) · [`FillType`](Attributes.md#filltype) · [`MarkerShape`](Attributes.md#markershape) · [`MarkerFill`](Attributes.md#markerfill) · [`MarkerBase`](Attributes.md#markerbase) · [`MarkerHalfTick`](Attributes.md#markerhalftick) · [`MarkerThicknessBasis`](Attributes.md#markerthicknessbasis) · [`MarkerThicknessUnits`](Attributes.md#markerthicknessunits) · [`DropShadowUnits`](Attributes.md#dropshadowunits) · [`ClassVisibility`](Attributes.md#classvisibility) · [`ObjectType`](Attributes.md#objecttype)
  - [Modulkonstanten](Attributes.md#modulkonstanten): `kMaxOpacity`
- **[ObjectPrimitives](ObjectPrimitives.md)** — Die gemeinsame Objektbasisklasse (PrimitiveObject) und 2D-Objekte: Linien, Rechtecke, Kreisbögen, Kreise, Polygone, Polylinien, Gruppen, Plug-in-Objekte, Text.
  - Klassen:
    - [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) — [`Bounds3D`](ObjectPrimitives.md#primitiveobjectbounds3d)
    - [`Locus2DObject`](ObjectPrimitives.md#locus2dobject)
    - [`Line2DObject`](ObjectPrimitives.md#line2dobject)
    - [`RectangularObject`](ObjectPrimitives.md#rectangularobject)
    - [`RectangleObject`](ObjectPrimitives.md#rectangleobject)
    - [`CornerDiameters`](ObjectPrimitives.md#cornerdiameters)
    - [`RoundRectObject`](ObjectPrimitives.md#roundrectobject)
    - [`ArcObject`](ObjectPrimitives.md#arcobject)
    - [`CircleObject`](ObjectPrimitives.md#circleobject)
    - [`PolyObject`](ObjectPrimitives.md#polyobject) — [`BooleanOperation`](ObjectPrimitives.md#polyobjectbooleanoperation)
    - [`PolygonObject`](ObjectPrimitives.md#polygonobject)
    - [`PolylineObject`](ObjectPrimitives.md#polylineobject)
    - [`GroupObject`](ObjectPrimitives.md#groupobject)
    - [`ParametricObject`](ObjectPrimitives.md#parametricobject) — [`PluginKind`](ObjectPrimitives.md#parametricobjectpluginkind)
    - [`TextObject`](ObjectPrimitives.md#textobject) — [`StyleRun`](ObjectPrimitives.md#textobjectstylerun) · [`TabStop`](ObjectPrimitives.md#textobjecttabstop) · [`HorizontalAlignment`](ObjectPrimitives.md#textobjecthorizontalalignment) · [`VerticalAlignment`](ObjectPrimitives.md#textobjectverticalalignment) · [`Spacing`](ObjectPrimitives.md#textobjectspacing) · [`TabAlignment`](ObjectPrimitives.md#textobjecttabalignment)
- **[Mathematik (`api.Math`)](ObjectPrimitives.Math.md)** — Das Untermodul api.Math: Punkte/Vektoren, Transformationen, Rechtecke, Linien, geometrische Ebenen, Kreise, Kreisbögen, Polygone, Hilfsfunktionen.
  - Klassen:
    - [`Math.Point2D`](ObjectPrimitives.Math.md#mathpoint2d)
    - [`Math.Transform2D`](ObjectPrimitives.Math.md#mathtransform2d)
    - [`Math.Rect2D`](ObjectPrimitives.Math.md#mathrect2d)
    - [`Math.RotatedRect2D`](ObjectPrimitives.Math.md#mathrotatedrect2d)
    - [`Math.Line2D`](ObjectPrimitives.Math.md#mathline2d) — [`Intersection`](ObjectPrimitives.Math.md#mathline2dintersection)
    - [`Math.Circle2D`](ObjectPrimitives.Math.md#mathcircle2d)
    - [`Math.Arc2D`](ObjectPrimitives.Math.md#matharc2d)
    - [`Math.PolyVertex`](ObjectPrimitives.Math.md#mathpolyvertex)
    - [`Math.Polygon2D`](ObjectPrimitives.Math.md#mathpolygon2d) — [`CurveLocation`](ObjectPrimitives.Math.md#mathpolygon2dcurvelocation)
    - [`Math.Point3D`](ObjectPrimitives.Math.md#mathpoint3d)
    - [`Math.Transform3D`](ObjectPrimitives.Math.md#mathtransform3d)
    - [`Math.Line3D`](ObjectPrimitives.Math.md#mathline3d)
    - [`Math.Plane3D`](ObjectPrimitives.Math.md#mathplane3d)
  - Aufzählungen: [`Math.VertexType`](ObjectPrimitives.Math.md#mathvertextype) · [`Math.OffsetJoin`](ObjectPrimitives.Math.md#mathoffsetjoin)
  - [Modulfunktionen](ObjectPrimitives.Math.md#modulfunktionen): `AngleDelta`, `AnglesAreEqual`, `AreEqual`, `Clamp`, `DegToRad`, `IsBetween`, `IsGreater`, `IsLess`, `IsZero`, `Lerp`, `NormalizeAngle`, `NormalizeAngleSigned`, `RadToDeg`, `Sign`
  - [Modulkonstanten](ObjectPrimitives.Math.md#modulkonstanten): `kPi`, `kTwoPi`, `kHalfPi`, `kEpsilon`, `kAngleEpsilon`
- **[Objects3D](Objects3D.md)** — Extrusionskörper, Schichtkörper, Rotationskörper, Vollkörper, Grundkörper (Kugel, Kegel, ...), NURBS, 3D-Polygone, Punktkörper, Hohlkörper.
  - Klassen:
    - [`ExtrudeObject`](Objects3D.md#extrudeobject) — [`Values`](Objects3D.md#extrudeobjectvalues) · [`Transform`](Objects3D.md#extrudeobjecttransform)
    - [`SweepObject`](Objects3D.md#sweepobject) — [`Values`](Objects3D.md#sweepobjectvalues)
    - [`MultiExtrudeObject`](Objects3D.md#multiextrudeobject)
    - [`SurfaceModelObject`](Objects3D.md#surfacemodelobject) — [`PathOptions`](Objects3D.md#surfacemodelobjectpathoptions)
    - [`GenericSolidObject`](Objects3D.md#genericsolidobject) — [`HistoryStep`](Objects3D.md#genericsolidobjecthistorystep) · [`Operation`](Objects3D.md#genericsolidobjectoperation)
    - [`ShellObject`](Objects3D.md#shellobject)
    - [`Polygon3DObject`](Objects3D.md#polygon3dobject) — [`Plane`](Objects3D.md#polygon3dobjectplane) · [`ClosestPoint`](Objects3D.md#polygon3dobjectclosestpoint)
    - [`MeshObject`](Objects3D.md#meshobject) — [`Face`](Objects3D.md#meshobjectface) · [`Part`](Objects3D.md#meshobjectpart) · [`Smoothing`](Objects3D.md#meshobjectsmoothing)
    - [`SolidPrimitiveObject`](Objects3D.md#solidprimitiveobject) — [`Kind`](Objects3D.md#solidprimitiveobjectkind)
    - [`SphereObject`](Objects3D.md#sphereobject)
    - [`HemisphereObject`](Objects3D.md#hemisphereobject)
    - [`ConeObject`](Objects3D.md#coneobject) — [`Radii`](Objects3D.md#coneobjectradii)
    - [`NurbsCurveObject`](Objects3D.md#nurbscurveobject) — [`Location`](Objects3D.md#nurbscurveobjectlocation)
    - [`NurbsSurfaceObject`](Objects3D.md#nurbssurfaceobject)
- **[ObjectsAnnotation](ObjectsAnnotation.md)** — Bemaßungen (linear, Winkel, Bogen, Kreis), Achsenkreuze, Datenstempel, Planköpfe, Tabellen.
  - Klassen:
    - [`AnnotationObject`](ObjectsAnnotation.md#annotationobject)
    - [`DataTagObject`](ObjectsAnnotation.md#datatagobject) — [`LeaderType`](ObjectsAnnotation.md#datatagobjectleadertype) · [`HorizontalPosition`](ObjectsAnnotation.md#datatagobjecthorizontalposition) · [`MoveBehaviour`](ObjectsAnnotation.md#datatagobjectmovebehaviour)
    - [`TitleBlockBorderObject`](ObjectsAnnotation.md#titleblockborderobject) — [`Revision`](ObjectsAnnotation.md#titleblockborderobjectrevision)
    - [`DimensionObject`](ObjectsAnnotation.md#dimensionobject)
    - [`LinearDimensionObject`](ObjectsAnnotation.md#lineardimensionobject)
    - [`AngularDimensionObject`](ObjectsAnnotation.md#angulardimensionobject)
    - [`ArcLengthDimensionObject`](ObjectsAnnotation.md#arclengthdimensionobject)
    - [`RadialDimensionObject`](ObjectsAnnotation.md#radialdimensionobject)
    - [`CenterMarkObject`](ObjectsAnnotation.md#centermarkobject)
    - [`WorksheetObject`](ObjectsAnnotation.md#worksheetobject) — [`Range`](ObjectsAnnotation.md#worksheetobjectrange) · [`NumberFormat`](ObjectsAnnotation.md#worksheetobjectnumberformat) · [`TextFormat`](ObjectsAnnotation.md#worksheetobjecttextformat) · [`Fill`](ObjectsAnnotation.md#worksheetobjectfill) · [`Borders`](ObjectsAnnotation.md#worksheetobjectborders)
  - Aufzählungen: [`DimensionKind`](ObjectsAnnotation.md#dimensionkind) · [`DimensionTolerance`](ObjectsAnnotation.md#dimensiontolerance)
- **[ObjectsArchitect](ObjectsArchitect.md)** — Architekturobjekte: Wände, Dächer, Böden/Decken, Fenster, Türen, Stützen und Treppen.
  - Klassen:
    - [`ArchitectObject`](ObjectsArchitect.md#architectobject)
    - [`WallObject`](ObjectsArchitect.md#wallobject) — [`Heights`](ObjectsArchitect.md#wallobjectheights) · [`HeightBound`](ObjectsArchitect.md#wallobjectheightbound) · [`Caps`](ObjectsArchitect.md#wallobjectcaps) · [`BoundStatus`](ObjectsArchitect.md#wallobjectboundstatus) · [`BoundKind`](ObjectsArchitect.md#wallobjectboundkind)
    - [`SlabObject`](ObjectsArchitect.md#slabobject)
    - [`RoofObject`](ObjectsArchitect.md#roofobject) — [`Attributes`](ObjectsArchitect.md#roofobjectattributes) · [`Accessories`](ObjectsArchitect.md#roofobjectaccessories) · [`Edge`](ObjectsArchitect.md#roofobjectedge) · [`MiterType`](ObjectsArchitect.md#roofobjectmitertype)
    - [`WindowObject`](ObjectsArchitect.md#windowobject)
    - [`DoorObject`](ObjectsArchitect.md#doorobject)
    - [`ColumnObject`](ObjectsArchitect.md#columnobject)
    - [`StairObject`](ObjectsArchitect.md#stairobject)
- **[ObjectsConnectCAD](ObjectsConnectCAD.md)** — Schematische ConnectCAD-Geräte (aus JSON-Beschreibungen erzeugt), Anschlüsse, Gerätetypen, Signal- und Verbindertypen.
  - Klassen:
    - [`ConnectCADLibrary`](ObjectsConnectCAD.md#connectcadlibrary) — [`Signal`](ObjectsConnectCAD.md#connectcadlibrarysignal) · [`Connector`](ObjectsConnectCAD.md#connectcadlibraryconnector) · [`Validation`](ObjectsConnectCAD.md#connectcadlibraryvalidation) · [`DeviceDefinition`](ObjectsConnectCAD.md#connectcadlibrarydevicedefinition)
    - [`ConnectCADSocketObject`](ObjectsConnectCAD.md#connectcadsocketobject)
    - [`ConnectCADDeviceObject`](ObjectsConnectCAD.md#connectcaddeviceobject) — [`CreateResult`](ObjectsConnectCAD.md#connectcaddeviceobjectcreateresult) · [`AddSocketResult`](ObjectsConnectCAD.md#connectcaddeviceobjectaddsocketresult) · [`DeviceTypeResult`](ObjectsConnectCAD.md#connectcaddeviceobjectdevicetyperesult)
- **[ObjectsLandmark](ObjectsLandmark.md)** — Landmark-Objekte: Pflanzen, Flächenpflanzungen, Geländemodelle und Geländemodifikatoren, Vermessungspunkte, Belag/Weg-Objekte, Grenzlinien, Kataster-Bäume.
  - Klassen:
    - [`LandmarkObject`](ObjectsLandmark.md#landmarkobject)
    - [`PlantObject`](ObjectsLandmark.md#plantobject) — [`Config`](ObjectsLandmark.md#plantobjectconfig) · [`TagDisplay`](ObjectsLandmark.md#plantobjecttagdisplay)
    - [`LandscapeAreaObject`](ObjectsLandmark.md#landscapeareaobject) — [`PlantDisplay2D`](ObjectsLandmark.md#landscapeareaobjectplantdisplay2d) · [`DrawingMode`](ObjectsLandmark.md#landscapeareaobjectdrawingmode) · [`AreaUnits`](ObjectsLandmark.md#landscapeareaobjectareaunits)
    - [`SiteModelObject`](ObjectsLandmark.md#sitemodelobject) — [`Display2D`](ObjectsLandmark.md#sitemodelobjectdisplay2d) · [`Display3D`](ObjectsLandmark.md#sitemodelobjectdisplay3d)
    - [`SiteModifierObject`](ObjectsLandmark.md#sitemodifierobject) — [`Config`](ObjectsLandmark.md#sitemodifierobjectconfig) · [`ApplyTo`](ObjectsLandmark.md#sitemodifierobjectapplyto)
    - [`StakeObject`](ObjectsLandmark.md#stakeobject) — [`Mode`](ObjectsLandmark.md#stakeobjectmode) · [`SiteModel`](ObjectsLandmark.md#stakeobjectsitemodel)
    - [`HardscapeObject`](ObjectsLandmark.md#hardscapeobject) — [`Mode3D`](ObjectsLandmark.md#hardscapeobjectmode3d)
    - [`PropertyLineObject`](ObjectsLandmark.md#propertylineobject) — [`AreaUnits`](ObjectsLandmark.md#propertylineobjectareaunits)
    - [`ExistingTreeObject`](ObjectsLandmark.md#existingtreeobject) — [`Origin`](ObjectsLandmark.md#existingtreeobjectorigin) · [`TreeProtection`](ObjectsLandmark.md#existingtreeobjecttreeprotection) · [`Condition`](ObjectsLandmark.md#existingtreeobjectcondition) · [`SULE`](ObjectsLandmark.md#existingtreeobjectsule) · [`Significance`](ObjectsLandmark.md#existingtreeobjectsignificance) · [`Action`](ObjectsLandmark.md#existingtreeobjectaction)
- **[ObjectsSpotlight](ObjectsSpotlight.md)** — Spotlight-Scheinwerfer und die GDTF-Bibliothek für Scheinwerfertypen (Import, verfügbare Modi).
  - Klassen:
    - [`LightingDeviceObject`](ObjectsSpotlight.md#lightingdeviceobject)
    - [`GDTFLibrary`](ObjectsSpotlight.md#gdtflibrary) — [`Entry`](ObjectsSpotlight.md#gdtflibraryentry) · [`ImportResult`](ObjectsSpotlight.md#gdtflibraryimportresult)
- **[Resources](Resources.md)** — Funktionen des Zubehör-Managers: Zubehör aller Art, Zubehörlisten und Import sowie typisiertes Zubehör (Schraffuren, Symbole, Stile, ...).
  - Klassen:
    - [`Resource`](Resources.md#resource)
    - [`ResourceList`](Resources.md#resourcelist) — [`Entry`](Resources.md#resourcelistentry) · [`ImportResult`](Resources.md#resourcelistimportresult)
    - [`TypedResource`](Resources.md#typedresource)
    - [`HatchLevel`](Resources.md#hatchlevel)
    - [`Hatch`](Resources.md#hatch)
    - [`GradientSegment`](Resources.md#gradientsegment)
    - [`Gradient`](Resources.md#gradient)
    - [`Tile`](Resources.md#tile)
    - [`ImageFill`](Resources.md#imagefill) — [`Compression`](Resources.md#imagefillcompression)
    - [`LineType`](Resources.md#linetype)
    - [`RecordField`](Resources.md#recordfield)
    - [`RecordFormat`](Resources.md#recordformat)
    - [`Texture`](Resources.md#texture) — [`Part`](Resources.md#texturepart)
    - [`RenderStyle`](Resources.md#renderstyle)
    - [`RenderBackground`](Resources.md#renderbackground) — [`Kind`](Resources.md#renderbackgroundkind)
    - [`TextStyle`](Resources.md#textstyle)
    - [`WallStyle`](Resources.md#wallstyle)
    - [`SlabStyle`](Resources.md#slabstyle)
    - [`RoofStyle`](Resources.md#roofstyle)
    - [`ViewportStyle`](Resources.md#viewportstyle)
    - [`BuildingMaterial`](Resources.md#buildingmaterial)
    - [`DataVisualization`](Resources.md#datavisualization)
    - [`ResourceFolderPath`](Resources.md#resourcefolderpath)
    - [`ResourceFolder`](Resources.md#resourcefolder)
    - [`SymbolDefinition`](Resources.md#symboldefinition) — [`GeometryType`](Resources.md#symboldefinitiongeometrytype) · [`InsertMode`](Resources.md#symboldefinitioninsertmode) · [`BreakMode`](Resources.md#symboldefinitionbreakmode)
    - [`WorksheetCell`](Resources.md#worksheetcell)
    - [`WorksheetCellContent`](Resources.md#worksheetcellcontent)
    - [`Worksheet`](Resources.md#worksheet)
  - Aufzählungen: [`ResourceType`](Resources.md#resourcetype) · [`ContentFolder`](Resources.md#contentfolder) · [`ImportConflict`](Resources.md#importconflict) · [`RecordFieldType`](Resources.md#recordfieldtype)
- **[Scripting](Scripting.md)** — Im Dokument gespeichertes Script-Zubehör (VectorScript / Python) und Scriptpaletten.
  - Klassen:
    - [`ScriptResource`](Scripting.md#scriptresource)
    - [`ScriptPalette`](Scripting.md#scriptpalette)
  - Aufzählungen: [`ScriptLanguage`](Scripting.md#scriptlanguage)
- **[UIAutomation](UIAutomation.md)** — Steuerung der Benutzeroberfläche: Werkzeuge und ihre Aktivierung, Methodenzeile (`ModeBar`), Werkzeugeingaben, Menübefehle und Menüblöcke, Bedienelemente der Infopalette.
  - Klassen:
    - [`Point3D`](UIAutomation.md#point3d)
    - [`ViewPoint`](UIAutomation.md#viewpoint)
    - [`ViewSize`](UIAutomation.md#viewsize)
    - [`ToolPoint`](UIAutomation.md#toolpoint)
    - [`ModeButtonDefinition`](UIAutomation.md#modebuttondefinition)
    - [`Tool`](UIAutomation.md#tool)
    - [`ModeChoice`](UIAutomation.md#modechoice)
    - [`ToolMode`](UIAutomation.md#toolmode)
    - [`ModeSetting`](UIAutomation.md#modesetting)
    - [`ModeBar`](UIAutomation.md#modebar)
    - [`ToolControl`](UIAutomation.md#toolcontrol)
    - [`ToolAccess`](UIAutomation.md#toolaccess)
    - [`MenuCommand`](UIAutomation.md#menucommand)
    - [`MenuChunkItem`](UIAutomation.md#menuchunkitem)
    - [`MenuEntry`](UIAutomation.md#menuentry)
    - [`MenuAccess`](UIAutomation.md#menuaccess)
    - [`OIPControl`](UIAutomation.md#oipcontrol)
    - [`OIPSetting`](UIAutomation.md#oipsetting)
    - [`OIPAccess`](UIAutomation.md#oipaccess)
  - Aufzählungen: [`ToolKind`](UIAutomation.md#toolkind) · [`ToolCreationType`](UIAutomation.md#toolcreationtype) · [`ToolFilter`](UIAutomation.md#toolfilter) · [`ModeType`](UIAutomation.md#modetype) · [`ModeButtonKind`](UIAutomation.md#modebuttonkind) · [`ToolKey`](UIAutomation.md#toolkey) · [`MenuCommandKind`](UIAutomation.md#menucommandkind) · [`MenuChunkKind`](UIAutomation.md#menuchunkkind) · [`MenuFilter`](UIAutomation.md#menufilter) · [`MenuEntryType`](UIAutomation.md#menuentrytype) · [`MenuStatus`](UIAutomation.md#menustatus) · [`OIPPane`](UIAutomation.md#oippane) · [`OIPControlType`](UIAutomation.md#oipcontroltype)
- **[UILayoutCreate](UILayoutCreate.md)** — Meldungen und Fragen, vorgefertigte Eingabedialoge und aus einzelnen Bedienelementen aufgebaute modale Dialoge.
  - Klassen:
    - [`DialogEvent`](UILayoutCreate.md#dialogevent)
    - [`ListBrowserEvent`](UILayoutCreate.md#listbrowserevent)
    - [`DialogSize`](UILayoutCreate.md#dialogsize)
    - [`Alerts`](UILayoutCreate.md#alerts)
    - [`TextPair`](UILayoutCreate.md#textpair)
    - [`StandardDialogs`](UILayoutCreate.md#standarddialogs)
    - [`LayoutDialog`](UILayoutCreate.md#layoutdialog)
  - Aufzählungen: [`DialogResult`](UILayoutCreate.md#dialogresult) · [`AlertButton`](UILayoutCreate.md#alertbutton) · [`EditRealType`](UILayoutCreate.md#editrealtype) · [`StaticTextStyle`](UILayoutCreate.md#statictextstyle) · [`CheckState`](UILayoutCreate.md#checkstate) · [`DialogEventType`](UILayoutCreate.md#dialogeventtype) · [`ListBrowserControlType`](UILayoutCreate.md#listbrowsercontroltype) · [`ListBrowserDisplayType`](UILayoutCreate.md#listbrowserdisplaytype) · [`ListBrowserEventType`](UILayoutCreate.md#listbrowsereventtype)

## Stichwortverzeichnis A–Z

[A](#stichwortverzeichnis-a) · [B](#stichwortverzeichnis-b) · [C](#stichwortverzeichnis-c) · [D](#stichwortverzeichnis-d) · [E](#stichwortverzeichnis-e) · [F](#stichwortverzeichnis-f) · [G](#stichwortverzeichnis-g) · [H](#stichwortverzeichnis-h) · [I](#stichwortverzeichnis-i) · [L](#stichwortverzeichnis-l) · [M](#stichwortverzeichnis-m) · [N](#stichwortverzeichnis-n) · [O](#stichwortverzeichnis-o) · [P](#stichwortverzeichnis-p) · [R](#stichwortverzeichnis-r) · [S](#stichwortverzeichnis-s) · [T](#stichwortverzeichnis-t) · [U](#stichwortverzeichnis-u) · [V](#stichwortverzeichnis-v) · [W](#stichwortverzeichnis-w)

### Stichwortverzeichnis A

| Name | Art | Seite | Zusammenfassung |
|---|---|---|---|
| [`AlertButton`](UILayoutCreate.md#alertbutton) | IntEnum | [UILayoutCreate](UILayoutCreate.md) | Standardschaltfläche einer Rückfrage. |
| [`Alerts`](UILayoutCreate.md#alerts) | Klasse | [UILayoutCreate](UILayoutCreate.md) | Standardmeldungen von Vectorworks: Informationen, Fehler und Rückfragen (nur statische Funktionen). |
| [`AngularDimensionObject`](ObjectsAnnotation.md#angulardimensionobject) | Klasse | [ObjectsAnnotation](ObjectsAnnotation.md) | Winkelbemaßung: misst den Winkel zwischen zwei Schenkeln, die sich in einem Scheitelpunkt treffen. |
| [`AngularUnit`](DocumentAccess.md#angularunit) | IntEnum | [DocumentAccess](DocumentAccess.md) | Einheit, in der Winkel angezeigt werden (`UnitSettings.GetAngularUnit`). |
| [`AnnotationObject`](ObjectsAnnotation.md#annotationobject) | Klasse | [ObjectsAnnotation](ObjectsAnnotation.md) | Gemeinsame Basisklasse der Beschriftungs-Plug-in-Objektklassen (Datenstempel, Plankopf). |
| [`Math.Arc2D`](ObjectPrimitives.Math.md#matharc2d) | Klasse | [Math](ObjectPrimitives.Math.md) | Kreisbogen. |
| [`ArchitectObject`](ObjectsArchitect.md#architectobject) | Klasse | [ObjectsArchitect](ObjectsArchitect.md) | Gemeinsame Basisklasse der Architect-Objektklassen (Wand, Boden/Decke, Dach, Fenster, Tür, Stütze, Treppe). |
| [`ArcLengthDimensionObject`](ObjectsAnnotation.md#arclengthdimensionobject) | Klasse | [ObjectsAnnotation](ObjectsAnnotation.md) | Bogenbemaßung: misst die Länge ENTLANG eines Bogens statt des geraden Abstands zwischen seinen ... |
| [`ArcObject`](ObjectPrimitives.md#arcobject) | Klasse | [ObjectPrimitives](ObjectPrimitives.md) | Kreisbogen (`ObjectType.Arc`). |
| [`AttributesBase`](Attributes.md#attributesbase) | Klasse | [Attributes](Attributes.md) | Gemeinsame Basisklasse der Klassen für grafische Attribute. |

### Stichwortverzeichnis B

| Name | Art | Seite | Zusammenfassung |
|---|---|---|---|
| [`BuildingMaterial`](Resources.md#buildingmaterial) | Klasse | [Resources](Resources.md) | Material (Baumaterial, `ObjectType.BuildingMaterial`): das physische Material einer Wand-, Boden/Decken- oder Dachschicht. |

### Stichwortverzeichnis C

| Name | Art | Seite | Zusammenfassung |
|---|---|---|---|
| [`CenterMarkObject`](ObjectsAnnotation.md#centermarkobject) | Klasse | [ObjectsAnnotation](ObjectsAnnotation.md) | Achsenkreuz: das Kreuz, das den Mittelpunkt eines Kreises oder Kreisbogens kennzeichnet. |
| [`CheckState`](UILayoutCreate.md#checkstate) | IntEnum | [UILayoutCreate](UILayoutCreate.md) | Zustand eines Kontrollkästchens mit drei Zuständen, einer Zelle in einer mehrspaltigen Liste oder eines Kontrollkästchens in einem Baumeintrag. |
| [`Math.Circle2D`](ObjectPrimitives.Math.md#mathcircle2d) | Klasse | [Math](ObjectPrimitives.Math.md) | Kreis. |
| [`CircleObject`](ObjectPrimitives.md#circleobject) | Klasse | [ObjectPrimitives](ObjectPrimitives.md) | Kreis. |
| [`ClassAttributes`](Attributes.md#classattributes) | Klasse | [Attributes](Attributes.md) | Eine Klassendefinition (`ObjectType.ClassDefinition`): eine benannte, gespeicherte Attributkonfiguration. |
| [`ClassVisibility`](Attributes.md#classvisibility) | IntEnum | [Attributes](Attributes.md) | Klassen |
| [`ColorPair`](Attributes.md#colorpair) | Klasse | [Attributes](Attributes.md) | Vordergrund- und Hintergrundfarbe eines Stifts oder einer Füllung als Farbindizes. |
| [`ColorRGB`](Attributes.md#colorrgb) | Klasse | [Attributes](Attributes.md) | RGB-Farbe mit 16 Bit pro Kanal (0 .. |
| [`ColumnObject`](ObjectsArchitect.md#columnobject) | Klasse | [ObjectsArchitect](ObjectsArchitect.md) | Plug-in-Objekt Stütze – die Vectorworks-Stütze, universeller Name "Column2". |
| [`ConeObject`](Objects3D.md#coneobject) | Klasse | [Objects3D](Objects3D.md) | Vectorworks-eigener Kegel. |
| [`ConeObject.Radii`](Objects3D.md#coneobjectradii) | Klasse (verschachtelt) | [Objects3D](Objects3D.md) | Grundflächenradien entlang der lokalen I- und J-Achsen. |
| [`ConnectCADDeviceObject`](ObjectsConnectCAD.md#connectcaddeviceobject) | Klasse | [ObjectsConnectCAD](ObjectsConnectCAD.md) | Schematisches ConnectCAD-Gerät (universeller Name "Device"): ein benannter Kasten mit Anschlüssen in seiner Profilgruppe. |
| [`ConnectCADDeviceObject.AddSocketResult`](ObjectsConnectCAD.md#connectcaddeviceobjectaddsocketresult) | Klasse (verschachtelt) | [ObjectsConnectCAD](ObjectsConnectCAD.md) | Ergebnis von AddSocket: der Anschluss (null, wenn er nicht hinzugefügt wurde) und Fehler. |
| [`ConnectCADDeviceObject.CreateResult`](ObjectsConnectCAD.md#connectcaddeviceobjectcreateresult) | Klasse (verschachtelt) | [ObjectsConnectCAD](ObjectsConnectCAD.md) | Ergebnis von CreateFromJSON: das Gerät (null, wenn es nicht erzeugt wurde), Fehler und Warnungen. |
| [`ConnectCADDeviceObject.DeviceTypeResult`](ObjectsConnectCAD.md#connectcaddeviceobjectdevicetyperesult) | Klasse (verschachtelt) | [ObjectsConnectCAD](ObjectsConnectCAD.md) | Ergebnis von CreateDeviceType: die Symboldefinition des Gerätetyps, ob sie neu ist und ob die vollständige ... |
| [`ConnectCADLibrary`](ObjectsConnectCAD.md#connectcadlibrary) | Klasse | [ObjectsConnectCAD](ObjectsConnectCAD.md) | ConnectCAD-Daten, die von den Geräten gemeinsam genutzt werden: Signal- und Verbindertypen, die Validierung von Gerätebeschreibungen ... |
| [`ConnectCADLibrary.Connector`](ObjectsConnectCAD.md#connectcadlibraryconnector) | Klasse (verschachtelt) | [ObjectsConnectCAD](ObjectsConnectCAD.md) | Ein ConnectCAD-Verbindertyp. |
| [`ConnectCADLibrary.DeviceDefinition`](ObjectsConnectCAD.md#connectcadlibrarydevicedefinition) | Klasse (verschachtelt) | [ObjectsConnectCAD](ObjectsConnectCAD.md) | Datenbank „Device Definition“ einer Gerätetyp-Symboldefinition. |
| [`ConnectCADLibrary.Signal`](ObjectsConnectCAD.md#connectcadlibrarysignal) | Klasse (verschachtelt) | [ObjectsConnectCAD](ObjectsConnectCAD.md) | Ein ConnectCAD-Signaltyp mit seiner Kategorie und seinen bevorzugten Verbindern. |
| [`ConnectCADLibrary.Validation`](ObjectsConnectCAD.md#connectcadlibraryvalidation) | Klasse (verschachtelt) | [ObjectsConnectCAD](ObjectsConnectCAD.md) | Ergebnis von ValidateDevice: Fehler (das Gerät wäre fehlerhaft) und Warnungen (Daten, die nur in einem Gerätetyp erhalten bleiben). |
| [`ConnectCADSocketObject`](ObjectsConnectCAD.md#connectcadsocketobject) | Klasse | [ObjectsConnectCAD](ObjectsConnectCAD.md) | ConnectCAD-Anschluss (universeller Name „Socket“): ein Anschlusspunkt eines schematischen Geräts innerhalb seiner Profilgruppe. |
| [`ContentFolder`](Resources.md#contentfolder) | IntEnum | [Resources](Resources.md) | Standard-Inhaltsordner von Vectorworks für externes Zubehör (Bibliothek / Vorgaben). |
| [`CornerDiameters`](ObjectPrimitives.md#cornerdiameters) | Klasse | [ObjectPrimitives](ObjectPrimitives.md) | Eckenrundung eines Radiusrechtecks: die Durchmesser der Eckellipse entlang der Breitenseite (alongWidth) ... |

### Stichwortverzeichnis D

| Name | Art | Seite | Zusammenfassung |
|---|---|---|---|
| [`DataTagObject`](ObjectsAnnotation.md#datatagobject) | Klasse | [ObjectsAnnotation](ObjectsAnnotation.md) | Plug-in-Objekt Datenstempel (universeller Name "Data Tag"). |
| [`DataTagObject.HorizontalPosition`](ObjectsAnnotation.md#datatagobjecthorizontalposition) | IntEnum (verschachtelt) | [ObjectsAnnotation](ObjectsAnnotation.md) | Seite der Verweislinie, auf der sich der Stempeltext befindet („Horizontale Position“). |
| [`DataTagObject.LeaderType`](ObjectsAnnotation.md#datatagobjectleadertype) | IntEnum (verschachtelt) | [ObjectsAnnotation](ObjectsAnnotation.md) | Form der Verweislinie eines Datenstempels („Verweislinientyp“). |
| [`DataTagObject.MoveBehaviour`](ObjectsAnnotation.md#datatagobjectmovebehaviour) | IntEnum (verschachtelt) | [ObjectsAnnotation](ObjectsAnnotation.md) | Was beim Ziehen des Stempels in der Zeichnung verschoben wird: der gesamte Stempel oder nur die Spitze seiner Verweislinie. |
| [`DataVisualization`](Resources.md#datavisualization) | Klasse | [Resources](Resources.md) | Datenvisualisierung (`ObjectType.DataVisualization`): eine Regel, die die grafischen Attribute der ... überschreibt |
| [`DefaultAttributes`](DocumentAccess.md#defaultattributes) | Klasse | [DocumentAccess](DocumentAccess.md) | Standardattribute für neue Objekte (die Attributpalette, wenn kein Objekt aktiviert ist). |
| [`Descend`](DocumentAccess.md#descend) | IntFlag | [DocumentAccess](DocumentAccess.md) | Wie tief beim Durchlaufen in Containerobjekte (Gruppen, Symbole, Ansichtsbereiche, ...) abgestiegen wird. |
| [`DialogEvent`](UILayoutCreate.md#dialogevent) | Klasse | [UILayoutCreate](UILayoutCreate.md) | Ein Ereignis, das an die Ereignisbehandlung eines Layoutdialogs übergeben wird. |
| [`DialogEventType`](UILayoutCreate.md#dialogeventtype) | IntEnum | [UILayoutCreate](UILayoutCreate.md) | Art eines Dialogereignisses (siehe DialogEvent). |
| [`DialogResult`](UILayoutCreate.md#dialogresult) | IntEnum | [UILayoutCreate](UILayoutCreate.md) | Wie ein Dialog oder eine Meldung geschlossen wurde. |
| [`DialogSize`](UILayoutCreate.md#dialogsize) | Klasse | [UILayoutCreate](UILayoutCreate.md) | Größe eines Dialogs in Pixeln. |
| [`DimensionKind`](ObjectsAnnotation.md#dimensionkind) | IntEnum | [ObjectsAnnotation](ObjectsAnnotation.md) | Bemaßungsart eines Objekts. |
| [`DimensionObject`](ObjectsAnnotation.md#dimensionobject) | Klasse | [ObjectsAnnotation](ObjectsAnnotation.md) | Basisklasse jedes Bemaßungsobjekts (`ObjectType.Dimension`). |
| [`DimensionTolerance`](ObjectsAnnotation.md#dimensiontolerance) | IntEnum | [ObjectsAnnotation](ObjectsAnnotation.md) | Abweichung einer Bemaßung vom Nennwert, die neben dem Messwert ausgegeben wird. |
| [`DisplaySettings`](DocumentAccess.md#displaysettings) | Klasse | [DocumentAccess](DocumentAccess.md) | Anzeigeeinstellungen. |
| [`Document`](DocumentAccess.md#document) | Klasse | [DocumentAccess](DocumentAccess.md) | Zustandslose Zugriffsschnittstelle für das aktive Vectorworks-Dokument. |
| [`DoorObject`](ObjectsArchitect.md#doorobject) | Klasse | [ObjectsArchitect](ObjectsArchitect.md) | Plug-in-Objekt Tür (universeller Name "Door") aus dem Plug-in Architectural Objects. |
| [`DropShadow`](Attributes.md#dropshadow) | Klasse | [Attributes](Attributes.md) | Schlagschatteneinstellungen eines Objekts, einer Klasse oder des Dokuments: ein/aus, Einheiten, Versatz, Unschärferadius, Winkel, Farbe ... |
| [`DropShadowAttributes`](Attributes.md#dropshadowattributes) | Klasse | [Attributes](Attributes.md) | Schlagschatten eines Objekts. |
| [`DropShadowUnits`](Attributes.md#dropshadowunits) | IntEnum | [Attributes](Attributes.md) | Schlagschatten |

### Stichwortverzeichnis E

| Name | Art | Seite | Zusammenfassung |
|---|---|---|---|
| [`EditingSettings`](DocumentAccess.md#editingsettings) | Klasse | [DocumentAccess](DocumentAccess.md) | Bearbeitungs- und Sitzungseinstellungen. |
| [`EditRealType`](UILayoutCreate.md#editrealtype) | IntEnum | [UILayoutCreate](UILayoutCreate.md) | Art des in einem Eingabefeld für reelle Zahlen angezeigten Werts. |
| [`ExistingTreeObject`](ObjectsLandmark.md#existingtreeobject) | Klasse | [ObjectsLandmark](ObjectsLandmark.md) | Plug-in-Objekt Baumkataster (universeller Name "Existing Tree") aus dem Plug-in Landmark. |
| [`ExistingTreeObject.Action`](ObjectsLandmark.md#existingtreeobjectaction) | IntEnum (verschachtelt) | [ObjectsLandmark](ObjectsLandmark.md) | Vorgeschlagene Maßnahme für einen Kataster-Baum. |
| [`ExistingTreeObject.Condition`](ObjectsLandmark.md#existingtreeobjectcondition) | IntEnum (verschachtelt) | [ObjectsLandmark](ObjectsLandmark.md) | Baumpflegerische Beurteilung |
| [`ExistingTreeObject.Origin`](ObjectsLandmark.md#existingtreeobjectorigin) | IntEnum (verschachtelt) | [ObjectsLandmark](ObjectsLandmark.md) | Herkunft der Art eines Kataster-Baums. |
| [`ExistingTreeObject.Significance`](ObjectsLandmark.md#existingtreeobjectsignificance) | IntEnum (verschachtelt) | [ObjectsLandmark](ObjectsLandmark.md) | Bewertung der Bedeutung eines Kataster-Baums. |
| [`ExistingTreeObject.SULE`](ObjectsLandmark.md#existingtreeobjectsule) | IntEnum (verschachtelt) | [ObjectsLandmark](ObjectsLandmark.md) | Voraussichtliche sichere Reststandzeit |
| [`ExistingTreeObject.TreeProtection`](ObjectsLandmark.md#existingtreeobjecttreeprotection) | IntEnum (verschachtelt) | [ObjectsLandmark](ObjectsLandmark.md) | Darstellung des Baumschutzbereichs |
| [`ExtrudeObject`](Objects3D.md#extrudeobject) | Klasse | [Objects3D](Objects3D.md) | Vectorworks-eigener Extrusionskörper (kein Plug-in-Objekt). |
| [`ExtrudeObject.Transform`](Objects3D.md#extrudeobjecttransform) | Klasse (verschachtelt) | [Objects3D](Objects3D.md) | Orthonormale lokale Achsen und Ursprung im übergeordneten Koordinatensystem (standardmäßig die Identitätstransformation). |
| [`ExtrudeObject.Values`](Objects3D.md#extrudeobjectvalues) | Klasse (verschachtelt) | [Objects3D](Objects3D.md) | Lokale Basishöhe und vorzeichenbehaftete Dicke in Welteinheiten. |

### Stichwortverzeichnis F

| Name | Art | Seite | Zusammenfassung |
|---|---|---|---|
| [`FillAttributes`](Attributes.md#fillattributes) | Klasse | [Attributes](Attributes.md) | Füllattribute eines Objekts: Farben, Stil (Muster / Schraffur / Mosaik / Farbverlauf / Bild), Deckkraft und Klassenabhängigkeit ... |
| [`FillMappingAttributes`](Attributes.md#fillmappingattributes) | Klasse | [Attributes](Attributes.md) | Zuordnung von Schraffur-, Mosaik-, Farbverlaufs- und Bildfüllungen (Füllraum): Ursprung, Achsen, Versätze, Drehung, Wiederholung, ... |
| [`FillMappingAttributes.Frame`](Attributes.md#fillmappingattributesframe) | Klasse (verschachtelt) | [Attributes](Attributes.md) | Ausrichtungsrahmen einer Schraffur-, Mosaik-, Farbverlaufs- oder Bildfüllung: der Ursprung und die Endpunkte der I- und J-Achsen. |
| [`FillType`](Attributes.md#filltype) | IntEnum | [Attributes](Attributes.md) | Art der Füllung eines Objekts. |

### Stichwortverzeichnis G

| Name | Art | Seite | Zusammenfassung |
|---|---|---|---|
| [`GDTFLibrary`](ObjectsSpotlight.md#gdtflibrary) | Klasse | [ObjectsSpotlight](ObjectsSpotlight.md) | Spotlight bekannte GDTF-Gerätetypen (General Device Type Format, DIN SPEC 15800). |
| [`GDTFLibrary.Entry`](ObjectsSpotlight.md#gdtflibraryentry) | Klasse (verschachtelt) | [ObjectsSpotlight](ObjectsSpotlight.md) | Ein DMX-Modus eines verfügbaren Gerätetyps. |
| [`GDTFLibrary.ImportResult`](ObjectsSpotlight.md#gdtflibraryimportresult) | Klasse (verschachtelt) | [ObjectsSpotlight](ObjectsSpotlight.md) | Ergebnis von Import: die GDTF-Symboldefinition, ihr GDTF-Name, ob dieser Aufruf sie importiert hat und ob die ... |
| [`GenericSolidObject`](Objects3D.md#genericsolidobject) | Klasse | [Objects3D](Objects3D.md) | Umfasst Vectorworks-eigene Vollkörper, einschließlich der mit den Befehlen Volumen zusammenfügen, Schnittvolumen löschen und Schnittvolumen anlegen erzeugten Vollkörper und einfacher Vollkörper ohne Bearbeitungshistorie. |
| [`GenericSolidObject.HistoryStep`](Objects3D.md#genericsolidobjecthistorystep) | Klasse (verschachtelt) | [Objects3D](Objects3D.md) | Ein Knoten im Vectorworks-eigenen Konstruktionsbaum, in Präorder-Reihenfolge. |
| [`GenericSolidObject.Operation`](Objects3D.md#genericsolidobjectoperation) | IntEnum (verschachtelt) | [Objects3D](Objects3D.md) | Boolesche Vollkörperoperation. |
| [`Gradient`](Resources.md#gradient) | Klasse | [Resources](Resources.md) | Verlaufsfüllung (`ObjectType.GradientDefinition`): ein Übergang zwischen zwei oder mehr Farbpunkten. |
| [`GradientSegment`](Resources.md#gradientsegment) | Klasse | [Resources](Resources.md) | Ein Farbstopp eines Farbverlaufs. |
| [`GridSettings`](DocumentAccess.md#gridsettings) | Klasse | [DocumentAccess](DocumentAccess.md) | Rastereinstellungen. |
| [`GroupObject`](ObjectPrimitives.md#groupobject) | Klasse | [ObjectPrimitives](ObjectPrimitives.md) | Gruppe (`ObjectType.Group`): ein Container für andere Objekte. |

### Stichwortverzeichnis H

| Name | Art | Seite | Zusammenfassung |
|---|---|---|---|
| [`HardscapeObject`](ObjectsLandmark.md#hardscapeobject) | Klasse | [ObjectsLandmark](ObjectsLandmark.md) | Plug-in-Objekt Belag/Weg (universeller Name "Hardscape") aus dem Plug-in Landmark. |
| [`HardscapeObject.Mode3D`](ObjectsLandmark.md#hardscapeobjectmode3d) | IntEnum (verschachtelt) | [ObjectsLandmark](ObjectsLandmark.md) | 3D-Modus des Belag/Weg-Objekts. |
| [`Hatch`](Resources.md#hatch) | Klasse | [Resources](Resources.md) | Vektorschraffurfüllung (`ObjectType.HatchDefinition`): eine Menge von Linienfamilien, die sich über die gefüllte Fläche wiederholen. |
| [`HatchLevel`](Resources.md#hatchlevel) | Klasse | [Resources](Resources.md) | Eine Linienfamilie einer Schraffur. |
| [`HemisphereObject`](Objects3D.md#hemisphereobject) | Klasse | [Objects3D](Objects3D.md) | Vectorworks-eigene Halbkugel: Mittelpunkt, Radien und eine in Richtung der lokalen K-Achse weisende Kuppel; schlanke Sicht auf ... |

### Stichwortverzeichnis I

| Name | Art | Seite | Zusammenfassung |
|---|---|---|---|
| [`ImageFill`](Resources.md#imagefill) | Klasse | [Resources](Resources.md) | Bildzubehör (`ObjectType.ImageDefinition`): eine Bitmap, die als Bildfüllung, als Bildobjekt oder als ... verwendet wird |
| [`ImageFill.Compression`](Resources.md#imagefillcompression) | IntEnum (verschachtelt) | [Resources](Resources.md) | Komprimierung, mit der das Bild gespeichert wird. |
| [`ImportConflict`](Resources.md#importconflict) | IntEnum | [Resources](Resources.md) | Wie ein Namenskonflikt gelöst wird, wenn Zubehör in die aktuelle Zeichnung importiert wird und dort bereits Zubehör ... |

### Stichwortverzeichnis L

| Name | Art | Seite | Zusammenfassung |
|---|---|---|---|
| [`LandmarkObject`](ObjectsLandmark.md#landmarkobject) | Klasse | [ObjectsLandmark](ObjectsLandmark.md) | Gemeinsame Basisklasse der Landmark-Plug-in-Objektklassen (Pflanze, Flächenpflanzung, Geländemodell, Geländemodifikator, Vermessungspunkt, ... |
| [`LandscapeAreaObject`](ObjectsLandmark.md#landscapeareaobject) | Klasse | [ObjectsLandmark](ObjectsLandmark.md) | Plug-in-Objekt Flächenpflanzung (universeller Name "Landscape Area") aus dem Plug-in Landmark. |
| [`LandscapeAreaObject.AreaUnits`](ObjectsLandmark.md#landscapeareaobjectareaunits) | IntEnum (verschachtelt) | [ObjectsLandmark](ObjectsLandmark.md) | Einheiten, in denen die Fläche einer Flächenpflanzung angezeigt wird. |
| [`LandscapeAreaObject.DrawingMode`](ObjectsLandmark.md#landscapeareaobjectdrawingmode) | IntEnum (verschachtelt) | [ObjectsLandmark](ObjectsLandmark.md) | Ob das Objekt als Flächenpflanzung oder als Hecke gezeichnet wird. |
| [`LandscapeAreaObject.PlantDisplay2D`](ObjectsLandmark.md#landscapeareaobjectplantdisplay2d) | IntEnum (verschachtelt) | [ObjectsLandmark](ObjectsLandmark.md) | Wie die Pflanzen einer Flächenpflanzung in 2D dargestellt werden. |
| [`Layer`](DocumentAccess.md#layer) | Klasse | [DocumentAccess](DocumentAccess.md) | Eine Ebene (Konstruktions- oder Layoutebene). |
| [`LayerContents`](DocumentAccess.md#layercontents) | Klasse | [DocumentAccess](DocumentAccess.md) | Objektanzahl und Begrenzung der Objekte auf der obersten Stufe einer Ebene. |
| [`LayerType`](DocumentAccess.md#layertype) | IntEnum | [DocumentAccess](DocumentAccess.md) | Art einer Ebene. |
| [`LayerVisibility`](DocumentAccess.md#layervisibility) | IntEnum | [DocumentAccess](DocumentAccess.md) | Sichtbarkeit einer Ebene (wie in der Navigationspalette angezeigt). |
| [`LayoutDialog`](UILayoutCreate.md#layoutdialog) | Klasse | [UILayoutCreate](UILayoutCreate.md) | Modaler Dialog mit Layoutverwaltung, der im Code aus einzelnen Bedienelementen aufgebaut wird. |
| [`LightingDeviceObject`](ObjectsSpotlight.md#lightingdeviceobject) | Klasse | [ObjectsSpotlight](ObjectsSpotlight.md) | Plug-in-Objekt Scheinwerfer (universeller Name "Lighting Device") aus dem Plug-in Spotlight. |
| [`Math.Line2D`](ObjectPrimitives.Math.md#mathline2d) | Klasse | [Math](ObjectPrimitives.Math.md) | Strecke von `start` nach `end`. |
| [`Math.Line2D.Intersection`](ObjectPrimitives.Math.md#mathline2dintersection) | Klasse (verschachtelt) | [Math](ObjectPrimitives.Math.md) | Schnittpunkt der Geraden. |
| [`Line2DObject`](ObjectPrimitives.md#line2dobject) | Klasse | [ObjectPrimitives](ObjectPrimitives.md) | 2D-Linie (`ObjectType.Line`): eine gerade Strecke zwischen zwei Punkten. |
| [`Math.Line3D`](ObjectPrimitives.Math.md#mathline3d) | Klasse | [Math](ObjectPrimitives.Math.md) | Von Python verwaltete 3D-Strecke vom Anfang zum Ende in Millimetern des Weltkoordinatensystems. |
| [`LinearDimensionObject`](ObjectsAnnotation.md#lineardimensionobject) | Klasse | [ObjectsAnnotation](ObjectsAnnotation.md) | Lineare Bemaßung: misst den Abstand zwischen zwei Punkten. |
| [`LineType`](Resources.md#linetype) | Klasse | [Resources](Resources.md) | Linienart-Zubehör. |
| [`ListBrowserControlType`](UILayoutCreate.md#listbrowsercontroltype) | IntEnum | [UILayoutCreate](UILayoutCreate.md) | Verhalten einer Spalte in einer mehrspaltigen Liste. |
| [`ListBrowserDisplayType`](UILayoutCreate.md#listbrowserdisplaytype) | IntEnum | [UILayoutCreate](UILayoutCreate.md) | Was eine Spalte in einer mehrspaltigen Liste anzeigt. |
| [`ListBrowserEvent`](UILayoutCreate.md#listbrowserevent) | Klasse | [UILayoutCreate](UILayoutCreate.md) | Details zum letzten Ereignis einer mehrspaltigen Liste. |
| [`ListBrowserEventType`](UILayoutCreate.md#listbrowsereventtype) | IntEnum | [UILayoutCreate](UILayoutCreate.md) | Was in einer mehrspaltigen Liste geschehen ist (siehe `LayoutDialog.GetListBrowserEvent`). |
| [`Locus2DObject`](ObjectPrimitives.md#locus2dobject) | Klasse | [ObjectPrimitives](ObjectPrimitives.md) | 2D-Punkt (`ObjectType.Locus`): ein Referenzpunkt. |

### Stichwortverzeichnis M

| Name | Art | Seite | Zusammenfassung |
|---|---|---|---|
| [`Marker`](Attributes.md#marker) | Klasse | [Attributes](Attributes.md) | Linienendzeichen (Pfeilspitze) am Anfang oder Ende einer Linie: Form, Füllung, Basis, halber Strich, Schaft, Winkel (Grad), ... |
| [`MarkerAttributes`](Attributes.md#markerattributes) | Klasse | [Attributes](Attributes.md) | Linienendzeichen (Pfeilspitzen) am Anfang und Ende eines Objekts. |
| [`MarkerBase`](Attributes.md#markerbase) | IntEnum | [Attributes](Attributes.md) | Form der Basis eines Linienendzeichens (bereits bitverschobene Werte, siehe `Marker.GetStyleValue`). |
| [`MarkerFill`](Attributes.md#markerfill) | IntEnum | [Attributes](Attributes.md) | Die folgenden Aufzählungen für Linienendzeichenstile (MarkerFill, MarkerBase, MarkerHalfTick) verwenden bereits bitverschobene Werte, sodass sie ... |
| [`MarkerHalfTick`](Attributes.md#markerhalftick) | IntEnum | [Attributes](Attributes.md) | Ganzes Linienendzeichen oder nur dessen linke oder rechte Hälfte (bereits bitverschobene Werte, siehe `Marker.GetStyleValue`). |
| [`MarkerShape`](Attributes.md#markershape) | IntEnum | [Attributes](Attributes.md) | Linienendzeichen (Pfeilspitzen) |
| [`MarkerThicknessBasis`](Attributes.md#markerthicknessbasis) | IntEnum | [Attributes](Attributes.md) | Woran sich die Linienstärke eines Linienendzeichens orientiert. |
| [`MarkerThicknessUnits`](Attributes.md#markerthicknessunits) | IntEnum | [Attributes](Attributes.md) | Einheiten einer benutzerdefinierten Linienstärke für Linienendzeichen. |
| [`MenuAccess`](UIAutomation.md#menuaccess) | Klasse | [UIAutomation](UIAutomation.md) | Zustandslose Schnittstelle zum Vectorworks-Menüsystem. |
| [`MenuChunkItem`](UIAutomation.md#menuchunkitem) | Klasse | [UIAutomation](UIAutomation.md) | Ein aktueller Eintrag eines Menüblocks. |
| [`MenuChunkKind`](UIAutomation.md#menuchunkkind) | IntEnum | [UIAutomation](UIAutomation.md) | Art eines Menüblocks (siehe „Menüblock“ oben). |
| [`MenuCommand`](UIAutomation.md#menucommand) | Klasse | [UIAutomation](UIAutomation.md) | Beschreibung eines installierten Menübefehls. |
| [`MenuCommandKind`](UIAutomation.md#menucommandkind) | IntEnum | [UIAutomation](UIAutomation.md) | Wie ein Menübefehl bereitgestellt wird. |
| [`MenuEntry`](UIAutomation.md#menuentry) | Klasse | [UIAutomation](UIAutomation.md) | Ein Eintrag eines Menüs in der Menüleiste gemäß der aktuellen Arbeitsumgebung. |
| [`MenuEntryType`](UIAutomation.md#menuentrytype) | IntEnum | [UIAutomation](UIAutomation.md) | Art eines Eintrags in einem Menü der Menüleiste. |
| [`MenuFilter`](UIAutomation.md#menufilter) | IntEnum | [UIAutomation](UIAutomation.md) | Welche Menübefehle `MenuAccess.GetMenuCommands` zurückgibt. |
| [`MenuStatus`](UIAutomation.md#menustatus) | IntEnum | [UIAutomation](UIAutomation.md) | Ob ein Menübefehl (oder ein Menüblockeintrag) jetzt ausgeführt werden kann und gegebenenfalls warum nicht (siehe `MenuAccess.GetMenuStatus`). |
| [`MeshObject`](Objects3D.md#meshobject) | Klasse | [Objects3D](Objects3D.md) | Vectorworks-eigener Punktkörper (`ObjectType.Mesh`): eine gemeinsame Scheitelpunktliste und polygonale Flächen, die über Indizes darauf verweisen. |
| [`MeshObject.Face`](Objects3D.md#meshobjectface) | Klasse (verschachtelt) | [Objects3D](Objects3D.md) | Teil 0 bezeichnet den gesamten, nicht texturierten Teil, siehe `GetOverallPart()`. |
| [`MeshObject.Part`](Objects3D.md#meshobjectpart) | Klasse (verschachtelt) | [Objects3D](Objects3D.md) | Texturteil: ID, Texturreferenz (0 = nicht texturiert) und Anzahl der Flächen, die ihn verwenden. |
| [`MeshObject.Smoothing`](Objects3D.md#meshobjectsmoothing) | IntEnum (verschachtelt) | [Objects3D](Objects3D.md) | Art der Glättung des Punktkörpers beim Rendern. |
| [`ModeBar`](UIAutomation.md#modebar) | Klasse | [UIAutomation](UIAutomation.md) | Zustandslose Sicht auf die Methodenzeile (`ModeBar`) des aktiven Werkzeugs. |
| [`ModeButtonDefinition`](UIAutomation.md#modebuttondefinition) | Klasse | [UIAutomation](UIAutomation.md) | Eine vom Werkzeug deklarierte Methodenschaltfläche (statische Informationen, die ohne Aktivierung des Werkzeugs verfügbar sind). |
| [`ModeButtonKind`](UIAutomation.md#modebuttonkind) | IntEnum | [UIAutomation](UIAutomation.md) | Art einer Methodenschaltfläche, wie sie ein Werkzeug bei seiner Registrierung deklariert (kann vom aktuellen ModeType abweichen). |
| [`ModeChoice`](UIAutomation.md#modechoice) | Klasse | [UIAutomation](UIAutomation.md) | Eine Auswahlmöglichkeit einer Methodengruppe: ein Optionsfeld, die einzelne Schaltfläche einer Schaltflächen-/Umschaltgruppe oder ein Eintrag in einem ... |
| [`ModeSetting`](UIAutomation.md#modesetting) | Klasse | [UIAutomation](UIAutomation.md) | Eine Anforderung zum Methodenwechsel für die allgemeine textbasierte Methoden-API (siehe `ModeBar.SetMode`). |
| [`ModeType`](UIAutomation.md#modetype) | IntEnum | [UIAutomation](UIAutomation.md) | Art einer Methodengruppe in der Methodenzeile des aktiven Werkzeugs. |
| [`MultiExtrudeObject`](Objects3D.md#multiextrudeobject) | Klasse | [Objects3D](Objects3D.md) | Vectorworks-eigener Schichtkörper. |

### Stichwortverzeichnis N

| Name | Art | Seite | Zusammenfassung |
|---|---|---|---|
| [`NurbsCurveObject`](Objects3D.md#nurbscurveobject) | Klasse | [Objects3D](Objects3D.md) | Vectorworks-eigene abschnittsweise definierte NURBS-Kurve. |
| [`NurbsCurveObject.Location`](Objects3D.md#nurbscurveobjectlocation) | Klasse (verschachtelt) | [Objects3D](Objects3D.md) | Kurvenpunkt und kurveneigener Parameter auf einem ab 0 indizierten Abschnitt; die Parameter sind keine Bogenlängen. |
| [`NurbsSurfaceObject`](Objects3D.md#nurbssurfaceobject) | Klasse | [Objects3D](Objects3D.md) | Vectorworks-eigene NURBS-Fläche. |

### Stichwortverzeichnis O

| Name | Art | Seite | Zusammenfassung |
|---|---|---|---|
| [`ObjectAttributes`](Attributes.md#objectattributes) | Klasse | [Attributes](Attributes.md) | Alle grafischen Attribute eines Objekts. |
| [`ObjectColors`](Attributes.md#objectcolors) | Klasse | [Attributes](Attributes.md) | Alle vier Objektfarben (Stift-Vordergrund/-Hintergrund, Füllungs-Vordergrund/-Hintergrund) als Farbindizes. |
| [`ObjectType`](Attributes.md#objecttype) | IntEnum | [Attributes](Attributes.md) | Typ eines Objekts. |
| [`Math.OffsetJoin`](ObjectPrimitives.Math.md#mathoffsetjoin) | IntEnum | [Math](ObjectPrimitives.Math.md) | Eckentyp für Parallelkonturen von Polygonen (`Polygon2D.Offset`). |
| [`OIPAccess`](UIAutomation.md#oipaccess) | Klasse | [UIAutomation](UIAutomation.md) | Zustandslose Schnittstelle zur Infopalette. |
| [`OIPControl`](UIAutomation.md#oipcontrol) | Klasse | [UIAutomation](UIAutomation.md) | Beschreibung und aktueller Zustand eines Bedienelements der Infopalette. |
| [`OIPControlType`](UIAutomation.md#oipcontroltype) | IntEnum | [UIAutomation](UIAutomation.md) | Art eines Bedienelements der Infopalette. |
| [`OIPPane`](UIAutomation.md#oippane) | IntEnum | [UIAutomation](UIAutomation.md) | Bereich (Reiter) der Infopalette. |
| [`OIPSetting`](UIAutomation.md#oipsetting) | Klasse | [UIAutomation](UIAutomation.md) | Eine Änderungsanforderung für ein Bedienelement, die von der allgemeinen, textbasierten API verwendet wird (siehe `OIPAccess.SetValue`). |

### Stichwortverzeichnis P

| Name | Art | Seite | Zusammenfassung |
|---|---|---|---|
| [`ParametricObject`](ObjectPrimitives.md#parametricobject) | Klasse | [ObjectPrimitives](ObjectPrimitives.md) | Allgemeines Plug-in-Objekt (parametrisches Objekt, `ObjectType.Parametric`) beliebiger Art, das durch ein Skript oder durch ein ... definiert wird |
| [`ParametricObject.PluginKind`](ObjectPrimitives.md#parametricobjectpluginkind) | IntEnum (verschachtelt) | [ObjectPrimitives](ObjectPrimitives.md) | Die Platzierungsart der Objekte eines Plug-ins: der vom Plug-in deklarierte Objektuntertyp. |
| [`PenAttributes`](Attributes.md#penattributes) | Klasse | [Attributes](Attributes.md) | Stiftattribute (Linienattribute) eines Objekts: Farben, Stil (Muster / Linienart), Liniendicke, Deckkraft, Klassenabhängigkeit ... |
| [`PenStyleKind`](Attributes.md#penstylekind) | IntEnum | [Attributes](Attributes.md) | Klassifizierung eines Stiftstil-Rohwerts. |
| [`Math.Plane3D`](ObjectPrimitives.Math.md#mathplane3d) | Klasse | [Math](ObjectPrimitives.Math.md) | Von Python verwaltete orientierte unendliche Ebene mit Einheitsnormalenvektor. |
| [`PlantObject`](ObjectsLandmark.md#plantobject) | Klasse | [ObjectsLandmark](ObjectsLandmark.md) | Plug-in-Objekt Pflanze (universeller Name "Plant") aus dem Landmark-Plug-in. |
| [`PlantObject.Config`](ObjectsLandmark.md#plantobjectconfig) | IntEnum (verschachtelt) | [ObjectsLandmark](ObjectsLandmark.md) | Konfiguration und Darstellung |
| [`PlantObject.TagDisplay`](ObjectsLandmark.md#plantobjecttagdisplay) | IntEnum (verschachtelt) | [ObjectsLandmark](ObjectsLandmark.md) | Wo die Pflanzenbeschriftung angezeigt wird. |
| [`Math.Point2D`](ObjectPrimitives.Math.md#mathpoint2d) | Klasse | [Math](ObjectPrimitives.Math.md) | 2D-Punkt / -Vektor. |
| [`Point2D`](Attributes.md#point2d) | Klasse | [Attributes](Attributes.md) | Einfacher 2D-Punkt-Wertdatensatz (`x`, `y` in Welteinheiten), der von den Dialog- und Attribut-APIs verwendet wird. |
| [`Math.Point3D`](ObjectPrimitives.Math.md#mathpoint3d) | Klasse | [Math](ObjectPrimitives.Math.md) | Von Python verwalteter 3D-Punkt / -Vektor in Millimetern des Weltkoordinatensystems. |
| [`Point3D`](UIAutomation.md#point3d) | Klasse | [UIAutomation](UIAutomation.md) | 3D-Punkt in Weltkoordinaten. |
| [`Math.Polygon2D`](ObjectPrimitives.Math.md#mathpolygon2d) | Klasse | [Math](ObjectPrimitives.Math.md) | Scheitelpunktliste eines Polygons oder einer Polylinie. |
| [`Math.Polygon2D.CurveLocation`](ObjectPrimitives.Math.md#mathpolygon2dcurvelocation) | Klasse (verschachtelt) | [Math](ObjectPrimitives.Math.md) | Punkt und ursprünglicher Segmentparameter auf der temporären NURBS-Darstellung des gekrümmten äußeren Polygonpfads. |
| [`Polygon3DObject`](Objects3D.md#polygon3dobject) | Klasse | [Objects3D](Objects3D.md) | Vectorworks-eigenes 3D-Polygon (`ObjectType.Polygon3D`). |
| [`Polygon3DObject.ClosestPoint`](Objects3D.md#polygon3dobjectclosestpoint) | Klasse (verschachtelt) | [Objects3D](Objects3D.md) | Nächstgelegener Punkt auf dem Polygonpfad, sein Abstand, der Kantenindex und die Pfadlänge ab dem ersten Scheitelpunkt. |
| [`Polygon3DObject.Plane`](Objects3D.md#polygon3dobjectplane) | Klasse (verschachtelt) | [Objects3D](Objects3D.md) | Ebene durch den Schwerpunkt der Eckpunkte; die Normale ist ein Einheitsvektor gemäß der Eckpunktreihenfolge (Rechte-Hand-Regel), und d ... |
| [`PolygonObject`](ObjectPrimitives.md#polygonobject) | Klasse | [ObjectPrimitives](ObjectPrimitives.md) | Polygon (`ObjectType.Polygon` sowie Freihandpolygone `ObjectType.FreehandPolygon`): ausschließlich Eckpunkte. |
| [`PolylineObject`](ObjectPrimitives.md#polylineobject) | Klasse | [ObjectPrimitives](ObjectPrimitives.md) | Polylinie (`ObjectType.Polyline`): eine Polygonform mit Eckpunkten, Bézierpunkten, kubischen Punkten, Bogenpunkten oder Radiuspunkten ... |
| [`PolyObject`](ObjectPrimitives.md#polyobject) | Klasse | [ObjectPrimitives](ObjectPrimitives.md) | Gemeinsame Basisklasse der Polygon- und Polylinienklassen. |
| [`PolyObject.BooleanOperation`](ObjectPrimitives.md#polyobjectbooleanoperation) | IntEnum (verschachtelt) | [ObjectPrimitives](ObjectPrimitives.md) | Operation der booleschen 2D-Funktionen |
| [`Math.PolyVertex`](ObjectPrimitives.Math.md#mathpolyvertex) | Klasse | [Math](ObjectPrimitives.Math.md) | Ein Scheitelpunkt eines `Polygon2D`: sein Punkt, Scheitelpunkttyp, Bogenradius (Radiuspunkte) und die Sichtbarkeit der ... |
| [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) | Klasse | [ObjectPrimitives](ObjectPrimitives.md) | Gemeinsame Basisklasse jeder Objektklasse der API (2D-Grundobjekte und über deren Unterklassen 3D-, Beschriftungs-, ... |
| [`PrimitiveObject.Bounds3D`](ObjectPrimitives.md#primitiveobjectbounds3d) | Klasse (verschachtelt) | [ObjectPrimitives](ObjectPrimitives.md) | Achsenparalleler 3D-Begrenzungsrahmen in Welteinheiten |
| [`ProgramVariables`](DocumentAccess.md#programvariables) | Klasse | [DocumentAccess](DocumentAccess.md) | Direkter, typisierter Zugriff auf jede Vectorworks-Programmvariable (anwendungsweite oder dokumentbezogene Einstellung) über ... |
| [`PropertyLineObject`](ObjectsLandmark.md#propertylineobject) | Klasse | [ObjectsLandmark](ObjectsLandmark.md) | Plug-in-Objekt Grenzlinie (universeller Name "Property Line") aus dem Plug-in Landmark. |
| [`PropertyLineObject.AreaUnits`](ObjectsLandmark.md#propertylineobjectareaunits) | IntEnum (verschachtelt) | [ObjectsLandmark](ObjectsLandmark.md) | Flächeneinheiten, die sowohl von "Area Units Imperial" als auch von "Area Units Metric" unterstützt werden. |

### Stichwortverzeichnis R

| Name | Art | Seite | Zusammenfassung |
|---|---|---|---|
| [`RadialDimensionObject`](ObjectsAnnotation.md#radialdimensionobject) | Klasse | [ObjectsAnnotation](ObjectsAnnotation.md) | Kreisbemaßung: Misst den Radius oder den Durchmesser eines Kreises oder Kreisbogens. |
| [`RecordField`](Resources.md#recordfield) | Klasse | [Resources](Resources.md) | Ein Feld einer Datenbank. |
| [`RecordFieldType`](Resources.md#recordfieldtype) | IntEnum | [Resources](Resources.md) | Datentyp eines Datenbankfelds. |
| [`RecordFormat`](Resources.md#recordformat) | Klasse | [Resources](Resources.md) | Datenbank. |
| [`Math.Rect2D`](ObjectPrimitives.Math.md#mathrect2d) | Klasse | [Math](ObjectPrimitives.Math.md) | Achsenparalleles Rechteck. |
| [`RectangleObject`](ObjectPrimitives.md#rectangleobject) | Klasse | [ObjectPrimitives](ObjectPrimitives.md) | Rechteck (`ObjectType.Box`), gegebenenfalls gedreht. |
| [`RectangularObject`](ObjectPrimitives.md#rectangularobject) | Klasse | [ObjectPrimitives](ObjectPrimitives.md) | Gemeinsame Basisklasse der Klassen für Rechtecke und Radiusrechtecke. |
| [`RenderBackground`](Resources.md#renderbackground) | Klasse | [Resources](Resources.md) | Renderworks-Hintergrund (`ObjectType.RenderBackground`): die Darstellung hinter dem Modell beim Rendern. |
| [`RenderBackground.Kind`](Resources.md#renderbackgroundkind) | IntEnum (verschachtelt) | [Resources](Resources.md) | Art des Hintergrunds, mit dem neues Zubehör erzeugt wird. |
| [`RenderStyle`](Resources.md#renderstyle) | Klasse | [Resources](Resources.md) | Renderstil (`ObjectType.RenderStyle`): eine gespeicherte Konfiguration der Rendereinstellungen, die auf ein ... angewendet wird |
| [`Resource`](Resources.md#resource) | Klasse | [Resources](Resources.md) | Ein Zubehör, identifiziert durch sein Handle. |
| [`ResourceFolder`](Resources.md#resourcefolder) | Klasse | [Resources](Resources.md) | Zubehörordner (`ObjectType.Folder`): gruppiert Zubehör desselben Typs im Zubehör-Manager. |
| [`ResourceFolderPath`](Resources.md#resourcefolderpath) | Klasse | [Resources](Resources.md) | Ordner eines mit `ResourceFolder.CreatePathFolders` erzeugten Pfads: alle Ordner des Pfads und diejenigen, die der Aufruf ... |
| [`ResourceList`](Resources.md#resourcelist) | Klasse | [Resources](Resources.md) | Eine Liste von Zubehör eines Typs aus der aktuellen Zeichnung oder aus externen Inhalten. |
| [`ResourceList.Entry`](Resources.md#resourcelistentry) | Klasse (verschachtelt) | [Resources](Resources.md) | Ein Eintrag der Liste. |
| [`ResourceList.ImportResult`](Resources.md#resourcelistimportresult) | Klasse (verschachtelt) | [Resources](Resources.md) | Ergebnis von ImportWithResult: das Zubehör in der Zeichnung und ob dieser Aufruf es hineinkopiert hat (`False`, wenn das ... |
| [`ResourceType`](Resources.md#resourcetype) | IntEnum | [Resources](Resources.md) | Typ eines Zubehörs. |
| [`RoofObject`](ObjectsArchitect.md#roofobject) | Klasse | [ObjectsArchitect](ObjectsArchitect.md) | Dach (`ObjectType.RoofContainer`) – ein polygonales Dach, das durch eine Liste von Kanten definiert wird. |
| [`RoofObject.Accessories`](ObjectsArchitect.md#roofobjectaccessories) | Klasse (verschachtelt) | [ObjectsArchitect](ObjectsArchitect.md) | Dachelemente entlang des Umfangs. |
| [`RoofObject.Attributes`](ObjectsArchitect.md#roofobjectattributes) | Klasse (verschachtelt) | [ObjectsArchitect](ObjectsArchitect.md) | Attribute des gesamten Dachs. |
| [`RoofObject.Edge`](ObjectsArchitect.md#roofobjectedge) | Klasse (verschachtelt) | [ObjectsArchitect](ObjectsArchitect.md) | Dachkanten (Polygoneckpunkt + Neigung und Überstand pro Kante) in der Reihenfolge des Dachumrisses. |
| [`RoofObject.MiterType`](ObjectsArchitect.md#roofobjectmitertype) | IntEnum (verschachtelt) | [ObjectsArchitect](ObjectsArchitect.md) | Gehrungsarten für die Dachkanten (Verbindung zweier benachbarter geneigter Flächen). |
| [`RoofStyle`](Resources.md#roofstyle) | Klasse | [Resources](Resources.md) | Dachstil (`ObjectType.RoofStyle`): Schalen und Attribute eines Dachs. |
| [`RoofTextures`](Attributes.md#rooftextures) | Klasse | [Attributes](Attributes.md) | Dachtexturen einer Klasse (interne Indizes von Texturen, 0 = keine). |
| [`Math.RotatedRect2D`](ObjectPrimitives.Math.md#mathrotatedrect2d) | Klasse | [Math](ObjectPrimitives.Math.md) | Ein gegebenenfalls gedrehtes Rechteck: eine Ecke, die Richtung der Breitenseite und die beiden Seitenlängen. |
| [`RoundRectObject`](ObjectPrimitives.md#roundrectobject) | Klasse | [ObjectPrimitives](ObjectPrimitives.md) | Radiusrechteck (`ObjectType.RoundedRectangle`), gegebenenfalls gedreht. |

### Stichwortverzeichnis S

| Name | Art | Seite | Zusammenfassung |
|---|---|---|---|
| [`ScriptLanguage`](Scripting.md#scriptlanguage) | IntEnum | [Scripting](Scripting.md) | Sprache eines Scripts. |
| [`ScriptPalette`](Scripting.md#scriptpalette) | Klasse | [Scripting](Scripting.md) | Eine Scriptpalette, identifiziert durch ihr Handle. |
| [`ScriptResource`](Scripting.md#scriptresource) | Klasse | [Scripting](Scripting.md) | Ein Script, identifiziert durch sein Handle. |
| [`ShellObject`](Objects3D.md#shellobject) | Klasse | [Objects3D](Objects3D.md) | Hohlkörper: ein CSG-Versatzknoten (Werkzeug Hohlkörper, VectorScript CreateShell). |
| [`SiteModelObject`](ObjectsLandmark.md#sitemodelobject) | Klasse | [ObjectsLandmark](ObjectsLandmark.md) | Plug-in-Objekt Geländemodell (universeller Name "DTM6") aus dem Plug-in Landmark. |
| [`SiteModelObject.Display2D`](ObjectsLandmark.md#sitemodelobjectdisplay2d) | IntEnum (verschachtelt) | [ObjectsLandmark](ObjectsLandmark.md) | Auswahl der 2D- / 3D-Darstellung |
| [`SiteModelObject.Display3D`](ObjectsLandmark.md#sitemodelobjectdisplay3d) | IntEnum (verschachtelt) | [ObjectsLandmark](ObjectsLandmark.md) | Was die 3D-Darstellung eines Geländemodells zeigt. |
| [`SiteModifierObject`](ObjectsLandmark.md#sitemodifierobject) | Klasse | [ObjectsLandmark](ObjectsLandmark.md) | Plug-in-Objekt Geländemodifikator (universeller Name "Site Modifiers") aus dem Plug-in Landmark. |
| [`SiteModifierObject.ApplyTo`](ObjectsLandmark.md#sitemodifierobjectapplyto) | IntEnum (verschachtelt) | [ObjectsLandmark](ObjectsLandmark.md) | Auf welche Oberfläche des Geländemodells ein Geländemodifikator angewendet wird. |
| [`SiteModifierObject.Config`](ObjectsLandmark.md#sitemodifierobjectconfig) | IntEnum (verschachtelt) | [ObjectsLandmark](ObjectsLandmark.md) | Umformungsmethode eines Geländemodifikators ("Config"). |
| [`SlabObject`](ObjectsArchitect.md#slabobject) | Klasse | [ObjectsArchitect](ObjectsArchitect.md) | Boden/Decke – ein horizontales Bauteil (Fußboden, Dachdecke, Geschossdecke, ...), definiert durch ein 2D-Begrenzungsprofil und ... |
| [`SlabStyle`](Resources.md#slabstyle) | Klasse | [Resources](Resources.md) | Boden/Deckenstil (`ObjectType.SlabStyle`): Schalen und Attribute eines Bodens bzw. einer Decke. |
| [`SnapSettings`](DocumentAccess.md#snapsettings) | Klasse | [DocumentAccess](DocumentAccess.md) | Zeigerfang-Einstellungen (Intelligenter Zeiger). |
| [`SolidPrimitiveObject`](Objects3D.md#solidprimitiveobject) | Klasse | [Objects3D](Objects3D.md) | Gemeinsame Basisklasse der Vectorworks-eigenen parametrischen Grundkörper (`ObjectType.Solid`): Kugeln, Halbkugeln und Kegel. |
| [`SolidPrimitiveObject.Kind`](Objects3D.md#solidprimitiveobjectkind) | IntEnum (verschachtelt) | [Objects3D](Objects3D.md) | Art eines Grundkörpers. |
| [`SphereObject`](Objects3D.md#sphereobject) | Klasse | [Objects3D](Objects3D.md) | Vectorworks-eigene Kugel: Mittelpunkt und I-/J-/K-Radien (ungleiche Radien ergeben ein Ellipsoid); schlanke Sicht auf ... |
| [`StackLayersSettings`](DocumentAccess.md#stacklayerssettings) | Klasse | [DocumentAccess](DocumentAccess.md) | Einstellungen für die Modellansicht. |
| [`StairObject`](ObjectsArchitect.md#stairobject) | Klasse | [ObjectsArchitect](ObjectsArchitect.md) | Plug-in-Objekt Treppe – die Vectorworks-Treppe, universeller Name "Stairs CW". |
| [`StakeObject`](ObjectsLandmark.md#stakeobject) | Klasse | [ObjectsLandmark](ObjectsLandmark.md) | Plug-in-Objekt Vermessungspunkt (universeller Name "Stake Object") aus dem Plug-in Landmark. |
| [`StakeObject.Mode`](ObjectsLandmark.md#stakeobjectmode) | IntEnum (verschachtelt) | [ObjectsLandmark](ObjectsLandmark.md) | Funktion des Vermessungspunkts in Bezug auf das Geländemodell. |
| [`StakeObject.SiteModel`](ObjectsLandmark.md#stakeobjectsitemodel) | IntEnum (verschachtelt) | [ObjectsLandmark](ObjectsLandmark.md) | Auf welche Oberfläche des Geländemodells sich ein Vermessungspunkt bezieht. |
| [`StandardDialogs`](UILayoutCreate.md#standarddialogs) | Klasse | [UILayoutCreate](UILayoutCreate.md) | Vorgefertigte Dialoge zum Bearbeiten eines oder zweier Werte oder zur Auswahl aus einer Liste (nur statische Funktionen). |
| [`StaticTextStyle`](UILayoutCreate.md#statictextstyle) | IntEnum | [UILayoutCreate](UILayoutCreate.md) | Schriftstil eines statischen Texts. |
| [`Story`](DocumentAccess.md#story) | Klasse | [DocumentAccess](DocumentAccess.md) | Ein Geschoss: ein Stockwerk des Gebäudes auf einer bestimmten Höhe. |
| [`StoryElevationChangeMode`](DocumentAccess.md#storyelevationchangemode) | IntEnum | [DocumentAccess](DocumentAccess.md) | Welche Geschosse `Story.SetElevation` verschiebt (die Optionen des Dialogfensters „Geschossbasishöhe ändern“). |
| [`StoryLevel`](DocumentAccess.md#storylevel) | Klasse | [DocumentAccess](DocumentAccess.md) | Eine Referenzhöhe eines Geschosses: eine benannte Höhe (ihr Referenzhöhentyp) relativ zur Geschosshöhe, optional mit der ... |
| [`StoryLevelTemplate`](DocumentAccess.md#storyleveltemplate) | Klasse | [DocumentAccess](DocumentAccess.md) | Eine Referenzhöhenvorgabe (Dialogfenster „Organisation“ > Reiter „Geschosse 3D“ > „Referenzhöhenvorgaben“): eine Vorlage für Geschossreferenzhöhen. |
| [`SurfaceModelObject`](Objects3D.md#surfacemodelobject) | Klasse | [Objects3D](Objects3D.md) | Ein Modellierungsergebnis ist eine NURBS-Fläche, ein CSG-Vollkörper oder eine Gruppe von Modellierungsergebnissen. |
| [`SurfaceModelObject.PathOptions`](Objects3D.md#surfacemodelobjectpathoptions) | Klasse (verschachtelt) | [Objects3D](Objects3D.md) | Optionen für Skalierung und Profilplatzierung eines Pfadkörpers (Extrusion entlang eines Pfads). |
| [`SweepObject`](Objects3D.md#sweepobject) | Klasse | [Objects3D](Objects3D.md) | Vectorworks-eigener Rotationskörper. |
| [`SweepObject.Values`](Objects3D.md#sweepobjectvalues) | Klasse (verschachtelt) | [Objects3D](Objects3D.md) | Rotationswinkel im Bogenmaß und Steigung in Welteinheiten pro voller Umdrehung. |
| [`SymbolDefinition`](Resources.md#symboldefinition) | Klasse | [Resources](Resources.md) | Symboldefinition. |
| [`SymbolDefinition.BreakMode`](Resources.md#symboldefinitionbreakmode) | IntEnum (verschachtelt) | [Resources](Resources.md) | Wie die Wand an der Einfügestelle des Symbols ausgeschnitten wird. |
| [`SymbolDefinition.GeometryType`](Resources.md#symboldefinitiongeometrytype) | IntEnum (verschachtelt) | [Resources](Resources.md) | Was das Symbol darstellen kann: nur 2D, nur 3D oder beides (ein hybrides Symbol zeigt seinen 2D-Teil in der Planansicht). |
| [`SymbolDefinition.InsertMode`](Resources.md#symboldefinitioninsertmode) | IntEnum (verschachtelt) | [Resources](Resources.md) | Position des Symbols relativ zur Wand, in die es eingesetzt wird. |

### Stichwortverzeichnis T

| Name | Art | Seite | Zusammenfassung |
|---|---|---|---|
| [`TextDefaults`](DocumentAccess.md#textdefaults) | Klasse | [DocumentAccess](DocumentAccess.md) | Text-Vorgabeeinstellungen für neue Textobjekte. |
| [`TextJustification`](DocumentAccess.md#textjustification) | IntEnum | [DocumentAccess](DocumentAccess.md) | Horizontale Ausrichtung neuer Texte (`TextDefaults`). |
| [`TextLineSpacing`](DocumentAccess.md#textlinespacing) | IntEnum | [DocumentAccess](DocumentAccess.md) | Zeilenabstand neuer Texte (`TextDefaults`); `Custom` verwendet den Durchschuss von `TextDefaults.GetLeading`. |
| [`TextObject`](ObjectPrimitives.md#textobject) | Klasse | [ObjectPrimitives](ObjectPrimitives.md) | Textblock (`ObjectType.Text`): formatierter Text, der an einem Ursprungspunkt platziert wird. |
| [`TextObject.HorizontalAlignment`](ObjectPrimitives.md#textobjecthorizontalalignment) | IntEnum (verschachtelt) | [ObjectPrimitives](ObjectPrimitives.md) | Horizontale Ausrichtung eines Textblocks. |
| [`TextObject.Spacing`](ObjectPrimitives.md#textobjectspacing) | IntEnum (verschachtelt) | [ObjectPrimitives](ObjectPrimitives.md) | Zeilenabstand eines Textblocks; `Custom` verwendet den an `SetSpacing` übergebenen Zeilenabstand. |
| [`TextObject.StyleRun`](ObjectPrimitives.md#textobjectstylerun) | Klasse (verschachtelt) | [ObjectPrimitives](ObjectPrimitives.md) | Zeichenfolge mit einheitlicher Formatierung: Anfang, Länge, Schriftart, Größe (Welteinheiten und Punkt), Stil ... |
| [`TextObject.TabAlignment`](ObjectPrimitives.md#textobjecttabalignment) | IntEnum (verschachtelt) | [ObjectPrimitives](ObjectPrimitives.md) | Ausrichtung des Texts an einem Tabulatorstopp. |
| [`TextObject.TabStop`](ObjectPrimitives.md#textobjecttabstop) | Klasse (verschachtelt) | [ObjectPrimitives](ObjectPrimitives.md) | Tabulatorstopp: Abstand vom linken Textrand in Welteinheiten sowie Ausrichtung. |
| [`TextObject.VerticalAlignment`](ObjectPrimitives.md#textobjectverticalalignment) | IntEnum (verschachtelt) | [ObjectPrimitives](ObjectPrimitives.md) | Vertikale Ausrichtung eines Textblocks relativ zu seinem Ursprung. |
| [`TextPair`](UILayoutCreate.md#textpair) | Klasse | [UILayoutCreate](UILayoutCreate.md) | Im Dialog mit zwei Textfeldern eingegebene Werte. |
| [`TextStyle`](Resources.md#textstyle) | Klasse | [Resources](Resources.md) | Textstil (`ObjectType.TextStyle`): Schriftart, Größe und Textattribute für Textobjekte und Bemaßungen. |
| [`TextStyleData`](DocumentAccess.md#textstyledata) | Klasse | [DocumentAccess](DocumentAccess.md) | Schriftstil-Flags eines Texts (fett, kursiv, unterstrichen, Kontur, Schatten), wie sie von `TextDefaults.GetStyle` / ... verwendet werden |
| [`Texture`](Resources.md#texture) | Klasse | [Resources](Resources.md) | Textur (`ObjectType.Texture`): Farbe, Reflexion, Transparenz und Relief einer gerenderten Oberfläche. |
| [`Texture.Part`](Resources.md#texturepart) | IntEnum (verschachtelt) | [Resources](Resources.md) | Teil eines Objekts, auf den eine Textur angewendet wird. |
| [`TextVerticalAlignment`](DocumentAccess.md#textverticalalignment) | IntEnum | [DocumentAccess](DocumentAccess.md) | Vertikale Ausrichtung neuer Texte (`TextDefaults`). |
| [`Tile`](Resources.md#tile) | Klasse | [Resources](Resources.md) | Mosaikfüllung (`ObjectType.TileDefinition`): eine Gruppe von 2D-Objekten, die sich auf einem Raster über die gefüllte Fläche wiederholt. |
| [`TitleBlockBorderObject`](ObjectsAnnotation.md#titleblockborderobject) | Klasse | [ObjectsAnnotation](ObjectsAnnotation.md) | Plug-in-Objekt Plankopf (universeller Name "Title Block Border"). |
| [`TitleBlockBorderObject.Revision`](ObjectsAnnotation.md#titleblockborderobjectrevision) | Klasse (verschachtelt) | [ObjectsAnnotation](ObjectsAnnotation.md) | Eine Revision eines Plankopfs: Nummer, Datum, Anmerkung, Veröffentlichungsdatum und Empfänger. |
| [`Tool`](UIAutomation.md#tool) | Klasse | [UIAutomation](UIAutomation.md) | Beschreibung eines Werkzeugs. |
| [`ToolAccess`](UIAutomation.md#toolaccess) | Klasse | [UIAutomation](UIAutomation.md) | Zustandslose Schnittstelle zum Vectorworks-Werkzeugsystem. |
| [`ToolControl`](UIAutomation.md#toolcontrol) | Klasse | [UIAutomation](UIAutomation.md) | Zustandslose Steuerung des aktiven Werkzeugs. |
| [`ToolCreationType`](UIAutomation.md#toolcreationtype) | IntEnum | [UIAutomation](UIAutomation.md) | Welche Art der Interaktion das Werkzeug zum Erzeugen von Objekten verwendet. |
| [`ToolFilter`](UIAutomation.md#toolfilter) | IntEnum | [UIAutomation](UIAutomation.md) | Welche Werkzeuge `ToolAccess.GetTools` zurückgibt. |
| [`ToolKey`](UIAutomation.md#toolkey) | IntEnum | [UIAutomation](UIAutomation.md) | Tasten, auf die Werkzeuge bei der Punkteingabe reagieren (siehe `ToolControl.PressKey`). |
| [`ToolKind`](UIAutomation.md#toolkind) | IntEnum | [UIAutomation](UIAutomation.md) | Wie ein Werkzeug bereitgestellt wird. |
| [`ToolMode`](UIAutomation.md#toolmode) | Klasse | [UIAutomation](UIAutomation.md) | Aktueller Zustand einer Methodengruppe des aktiven Werkzeugs. |
| [`ToolPoint`](UIAutomation.md#toolpoint) | Klasse | [UIAutomation](UIAutomation.md) | Ein in das aktive Werkzeug eingegebener Punkt in der Form, in der das Werkzeug ihn empfängt. |
| [`Math.Transform2D`](ObjectPrimitives.Math.md#mathtransform2d) | Klasse | [Math](ObjectPrimitives.Math.md) | Affine 2D-Transformation. |
| [`Math.Transform3D`](ObjectPrimitives.Math.md#mathtransform3d) | Klasse | [Math](ObjectPrimitives.Math.md) | Von Python verwaltete affine 3D-Matrix, die auf Spaltenvektoren wirkt; A * B wendet zuerst B an. |
| [`Traverse`](DocumentAccess.md#traverse) | IntEnum | [DocumentAccess](DocumentAccess.md) | Welche Objektmenge beim Durchlaufen des Dokuments besucht wird. |
| [`TypedResource`](Resources.md#typedresource) | Klasse | [Resources](Resources.md) | Auf einen ResourceType beschränktes Zubehör. |

### Stichwortverzeichnis U

| Name | Art | Seite | Zusammenfassung |
|---|---|---|---|
| [`UndoMethod`](DocumentAccess.md#undomethod) | IntEnum | [DocumentAccess](DocumentAccess.md) | Rückgängig-Methode, die an `Document.StartUndoEvent` übergeben wird. |
| [`UnitSettings`](DocumentAccess.md#unitsettings) | Klasse | [DocumentAccess](DocumentAccess.md) | Primäre oder sekundäre Bemaßungseinheiten des aktiven Dokuments. |

### Stichwortverzeichnis V

| Name | Art | Seite | Zusammenfassung |
|---|---|---|---|
| [`Math.VertexType`](ObjectPrimitives.Math.md#mathvertextype) | IntEnum | [Math](ObjectPrimitives.Math.md) | Typ eines Polygon-Scheitelpunkts. |
| [`ViewPoint`](UIAutomation.md#viewpoint) | Klasse | [UIAutomation](UIAutomation.md) | Punkt in Ansichtskoordinaten in Pixeln (16-Bit-Koordinaten). |
| [`ViewportStyle`](Resources.md#viewportstyle) | Klasse | [Resources](Resources.md) | Ansichtsbereichstil (`ObjectType.ViewportStyle`): die gespeicherten Einstellungen eines Ansichtsbereichs auf einer Layoutebene. |
| [`ViewSize`](UIAutomation.md#viewsize) | Klasse | [UIAutomation](UIAutomation.md) | Größe des aktiven Ansichtsfensters in Pixeln. |
| [`VisibilityOptions`](DocumentAccess.md#visibilityoptions) | IntEnum | [DocumentAccess](DocumentAccess.md) | Wie andere als die aktive Ebene oder Klasse dargestellt werden. |

### Stichwortverzeichnis W

| Name | Art | Seite | Zusammenfassung |
|---|---|---|---|
| [`WallObject`](ObjectsArchitect.md#wallobject) | Klasse | [ObjectsArchitect](ObjectsArchitect.md) | Wand (`ObjectType.Wall`) - eine gerade oder runde Wand, in die Fenster, Türen und andere Wandobjekte eingesetzt werden können. |
| [`WallObject.BoundKind`](ObjectsArchitect.md#wallobjectboundkind) | IntEnum (verschachtelt) | [ObjectsArchitect](ObjectsArchitect.md) | Woran sich ein Wandhöhenbezug orientiert: an der Ebenenbasishöhe, der Ebenenwandhöhe oder einer Geschossreferenzhöhe. |
| [`WallObject.BoundStatus`](ObjectsArchitect.md#wallobjectboundstatus) | IntEnum (verschachtelt) | [ObjectsArchitect](ObjectsArchitect.md) | Status eines Wandhöhenbezugs (`WallObject.HeightBound.fStatus`). |
| [`WallObject.Caps`](ObjectsArchitect.md#wallobjectcaps) | Klasse (verschachtelt) | [ObjectsArchitect](ObjectsArchitect.md) | Endabschlüsse. |
| [`WallObject.HeightBound`](ObjectsArchitect.md#wallobjectheightbound) | Klasse (verschachtelt) | [ObjectsArchitect](ObjectsArchitect.md) | Bezug der Wandunter- oder -oberkante: woran sich ihre Höhe orientiert. |
| [`WallObject.Heights`](ObjectsArchitect.md#wallobjectheights) | Klasse (verschachtelt) | [ObjectsArchitect](ObjectsArchitect.md) | Höhen (Welteinheiten) relativ zur Ebenenbasishöhe (0 = Oberkante der Ebene, negativ = darunter). |
| [`WallStyle`](Resources.md#wallstyle) | Klasse | [Resources](Resources.md) | Wandstil (`ObjectType.WallStyle`): Schalen, Dicke und Attribute einer Wand. |
| [`WallTextures`](Attributes.md#walltextures) | Klasse | [Attributes](Attributes.md) | Wandtexturen einer Klasse (interne Indizes von Texturen, 0 = keine). |
| [`WindowObject`](ObjectsArchitect.md#windowobject) | Klasse | [ObjectsArchitect](ObjectsArchitect.md) | Plug-in-Objekt Fenster (universeller Name "Window") aus dem Plug-in Architectural Objects. |
| [`Worksheet`](Resources.md#worksheet) | Klasse | [Resources](Resources.md) | Tabelle. |
| [`WorksheetCell`](Resources.md#worksheetcell) | Klasse | [Resources](Resources.md) | Eine Tabellenzelle. |
| [`WorksheetCellContent`](Resources.md#worksheetcellcontent) | Klasse | [Resources](Resources.md) | Eine Zelle mit ihrem Inhalt. |
| [`WorksheetObject`](ObjectsAnnotation.md#worksheetobject) | Klasse | [ObjectsAnnotation](ObjectsAnnotation.md) | Verweis auf eine Tabelle (ZUBEHÖR) ohne Übernahme des Objekts, keine platzierte Tabellengrafik und kein Plug-in-Objekt zur Beschriftung. |
| [`WorksheetObject.Borders`](ObjectsAnnotation.md#worksheetobjectborders) | Klasse (verschachtelt) | [ObjectsAnnotation](ObjectsAnnotation.md) | Kennzeichen für Zellenränder sowie für die Anwendung auf den äußeren Rahmen und die inneren Ränder eines Bereichs. |
| [`WorksheetObject.Fill`](ObjectsAnnotation.md#worksheetobjectfill) | Klasse (verschachtelt) | [ObjectsAnnotation](ObjectsAnnotation.md) | Vectorworks-eigener Füllstil, ColorRef-Indizes des Dokuments und Muster. |
| [`WorksheetObject.NumberFormat`](ObjectsAnnotation.md#worksheetobjectnumberformat) | Klasse (verschachtelt) | [ObjectsAnnotation](ObjectsAnnotation.md) | Vectorworks-eigenes Zahlenformat für Tabellen, einschließlich formatabhängiger Genauigkeit und UTF-8-Präfix/-Suffix. |
| [`WorksheetObject.Range`](ObjectsAnnotation.md#worksheetobjectrange) | Klasse (verschachtelt) | [ObjectsAnnotation](ObjectsAnnotation.md) | Ab 1 indizierter Tabellenbereich einschließlich seiner Grenzen. |
| [`WorksheetObject.TextFormat`](ObjectsAnnotation.md#worksheetobjecttextformat) | Klasse (verschachtelt) | [ObjectsAnnotation](ObjectsAnnotation.md) | Tabellentext: Punktgröße, Schriftart/-stil, Ausrichtungen, Winkel in Grad, ColorRef-Index und Zeilenumbruch. |

## Seitenaufbau

Jede Gruppenseite hat denselben Aufbau:

1. **Titel** — die Gruppe, das Python-Modul und die Vectorworks-Version.
2. **Inhaltsverzeichnis** — alle Klassen, verschachtelten Typen und Aufzählungen der Seite.
3. **Übersicht** — eine Zeile je Typ mit seiner Basisklasse und einer einzeiligen Zusammenfassung.
4. **Klassen** — für jede Klasse: ihr vollständiger Name, wovon sie erbt, eine Beschreibung und anschließend Tabellen der Konstruktoren, Methoden (nach Themen gruppiert), Operatoren, Felder und Konstanten. Verschachtelte Klassen und Aufzählungen folgen der zugehörigen Klasse. Geerbte Methoden werden einmalig bei der Basisklasse dokumentiert.
5. **Aufzählungen** — Elemente mit ihren numerischen Werten und Beschreibungen.

In Vectorworks zeigen `dir(api)` und `help(...)` an, was in der laufenden Version verfügbar ist.

## Statistik

| Seite | Klassen | Aufzählungen | Methoden | Konstruktoren | Felder | Konstanten |
|---|---|---|---|---|---|---|
| [DocumentAccess](DocumentAccess.md) | 16 | 11 | 508 | 16 | 18 | 0 |
| [Attributes](Attributes.md) | 17 | 11 | 249 | 17 | 37 | 1 |
| [ObjectPrimitives](ObjectPrimitives.md) | 18 | 6 | 329 | 16 | 17 | 12 |
| [Math](ObjectPrimitives.Math.md) | 15 | 2 | 383 | 36 | 51 | 5 |
| [Objects3D](Objects3D.md) | 25 | 3 | 303 | 25 | 38 | 0 |
| [ObjectsAnnotation](ObjectsAnnotation.md) | 16 | 5 | 291 | 16 | 32 | 0 |
| [ObjectsArchitect](ObjectsArchitect.md) | 14 | 3 | 176 | 14 | 31 | 0 |
| [ObjectsConnectCAD](ObjectsConnectCAD.md) | 10 | 0 | 34 | 10 | 31 | 0 |
| [ObjectsLandmark](ObjectsLandmark.md) | 9 | 19 | 211 | 9 | 0 | 0 |
| [ObjectsSpotlight](ObjectsSpotlight.md) | 4 | 0 | 15 | 4 | 11 | 0 |
| [Resources](Resources.md) | 30 | 10 | 270 | 30 | 29 | 2 |
| [Scripting](Scripting.md) | 2 | 1 | 30 | 2 | 0 | 0 |
| [UIAutomation](UIAutomation.md) | 19 | 13 | 75 | 19 | 81 | 0 |
| [UILayoutCreate](UILayoutCreate.md) | 7 | 9 | 182 | 5 | 12 | 0 |
| **Gesamt** | **202** | **93** | **3056** | **219** | **388** | **20** |

Bei Methoden werden die Namen gezählt (mehrere Argumentlisten desselben Namens zählen einmal).

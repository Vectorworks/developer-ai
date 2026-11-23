[English](../../PythonAPI/v2027.2/ObjectPrimitives.md) • **Deutsch** • [日本語](../../PythonAPI.ja/v2027.2/ObjectPrimitives.md)

# ObjectPrimitives — 2D-Grundobjekte

> **Python-Modul:** `api` · **Version:** Vectorworks 2027 Update 2

[Zurück zum Index](README.md)

Die 2D-Objektklassen. Jede Objektklasse bietet eine leichtgewichtige Sicht auf ein Zeichnungsobjekt: Das Kopieren eines Python-Objekts kopiert nicht das Zeichnungsobjekt, und das Löschen des Python-Objekts löscht nicht das Zeichnungsobjekt.

`PrimitiveObject` ist die gemeinsame Basisklasse **jeder** Objektklasse der API (einschließlich der 3D-, Beschriftungs-, Architektur-, Landschafts-, Spotlight- und ConnectCAD-Objekte): Identität, Hierarchie, Zustand, Attribute und Transformationen sind dort einmalig dokumentiert. `ParametricObject` stellt ein beliebiges Plug-in-Objekt dar (zu verwenden, wenn keine spezifische Klasse vorhanden ist); `PolyObject` ist die gemeinsame Basisklasse von `PolygonObject` und `PolylineObject`; `RectangularObject` ist die gemeinsame Basisklasse der Rechteckklassen.

Abfragemethoden geben `None` zurück, wenn ein Wert nicht verfügbar ist; Änderungsmethoden geben bei einem Fehlschlag `False` zurück. Koordinaten werden in Welteinheiten angegeben, Winkel im Bogenmaß (gegen den Uhrzeigersinn ab der X-Achse).

## Inhaltsverzeichnis

- [Überblick](#überblick)
- [Klassen](#klassen)
  - [PrimitiveObject](#primitiveobject)
    - [PrimitiveObject.Bounds3D](#primitiveobjectbounds3d)
  - [Locus2DObject](#locus2dobject)
  - [Line2DObject](#line2dobject)
  - [RectangularObject](#rectangularobject)
  - [RectangleObject](#rectangleobject)
  - [CornerDiameters](#cornerdiameters)
  - [RoundRectObject](#roundrectobject)
  - [ArcObject](#arcobject)
  - [CircleObject](#circleobject)
  - [PolyObject](#polyobject)
    - [PolyObject.BooleanOperation](#polyobjectbooleanoperation)
  - [PolygonObject](#polygonobject)
  - [PolylineObject](#polylineobject)
  - [GroupObject](#groupobject)
  - [ParametricObject](#parametricobject)
    - [ParametricObject.PluginKind](#parametricobjectpluginkind)
  - [TextObject](#textobject)
    - [TextObject.StyleRun](#textobjectstylerun)
    - [TextObject.TabStop](#textobjecttabstop)
    - [TextObject.HorizontalAlignment](#textobjecthorizontalalignment)
    - [TextObject.VerticalAlignment](#textobjectverticalalignment)
    - [TextObject.Spacing](#textobjectspacing)
    - [TextObject.TabAlignment](#textobjecttabalignment)

## Überblick

| Name | Art | Erbt von | Zusammenfassung |
|---|---|---|---|
| [`PrimitiveObject`](#primitiveobject) | Klasse |  | Gemeinsame Basisklasse jeder Objektklasse der API (2D-Grundobjekte und über ihre Unterklassen 3D-, Beschriftungs-, Architektur-, Landschafts-, Spotlight- und ConnectCAD-Objekte... |
| [`PrimitiveObject.Bounds3D`](#primitiveobjectbounds3d) | Klasse (verschachtelt) |  | Achsenparalleler 3D-Begrenzungsrahmen in Welteinheiten |
| [`Locus2DObject`](#locus2dobject) | Klasse | [`PrimitiveObject`](#primitiveobject) | 2D-Punkt (`ObjectType.Locus`): ein Referenzpunkt. |
| [`Line2DObject`](#line2dobject) | Klasse | [`PrimitiveObject`](#primitiveobject) | 2D-Linie (`ObjectType.Line`): eine gerade Strecke zwischen zwei Punkten. |
| [`RectangularObject`](#rectangularobject) | Klasse | [`PrimitiveObject`](#primitiveobject) | Gemeinsame Basisklasse der Klassen für Rechtecke und Radiusrechtecke. |
| [`RectangleObject`](#rectangleobject) | Klasse | [`RectangularObject`](#rectangularobject) | Rechteck (`ObjectType.Box`), gegebenenfalls gedreht. |
| [`CornerDiameters`](#cornerdiameters) | Klasse |  | Eckenrundung eines Radiusrechtecks: die Durchmesser der Eckellipse entlang der Breitenseite (alongWidth) und der Höhenseite (alongHeight). |
| [`RoundRectObject`](#roundrectobject) | Klasse | [`RectangularObject`](#rectangularobject) | Radiusrechteck (`ObjectType.RoundedRectangle`), gegebenenfalls gedreht. |
| [`ArcObject`](#arcobject) | Klasse | [`PrimitiveObject`](#primitiveobject) | Kreisbogen (`ObjectType.Arc`). |
| [`CircleObject`](#circleobject) | Klasse | [`PrimitiveObject`](#primitiveobject) | Kreis. |
| [`PolyObject`](#polyobject) | Klasse | [`PrimitiveObject`](#primitiveobject) | Gemeinsame Basisklasse der Polygon- und Polylinienklassen. |
| [`PolyObject.BooleanOperation`](#polyobjectbooleanoperation) | IntEnum (verschachtelt) |  | Operation der booleschen 2D-Funktionen |
| [`PolygonObject`](#polygonobject) | Klasse | [`PolyObject`](#polyobject) | Polygon (`ObjectType.Polygon` sowie Freihandpolygone `ObjectType.FreehandPolygon`): ausschließlich Eckpunkte. |
| [`PolylineObject`](#polylineobject) | Klasse | [`PolyObject`](#polyobject) | Polylinie (`ObjectType.Polyline`): eine Polygonform, deren Scheitelpunkte Eck-, Bézier-, kubische, Bogen- oder Radiuspunkte sein können. |
| [`GroupObject`](#groupobject) | Klasse | [`PrimitiveObject`](#primitiveobject) | Gruppe (`ObjectType.Group`): ein Container für andere Objekte. |
| [`ParametricObject`](#parametricobject) | Klasse | [`PrimitiveObject`](#primitiveobject) | Allgemeines Plug-in-Objekt (parametrisches Objekt, `ObjectType.Parametric`) beliebiger Art, das durch ein Skript oder ein kompiliertes Plug-in definiert wird. |
| [`ParametricObject.PluginKind`](#parametricobjectpluginkind) | IntEnum (verschachtelt) |  | Die Platzierungsart der Objekte eines Plug-ins: der vom Plug-in deklarierte Objektuntertyp. |
| [`TextObject`](#textobject) | Klasse | [`PrimitiveObject`](#primitiveobject) | Textblock (`ObjectType.Text`): formatierter Text, der an einem Ursprungspunkt platziert wird. |
| [`TextObject.StyleRun`](#textobjectstylerun) | Klasse (verschachtelt) |  | Zeichenfolge mit einheitlicher Formatierung: Beginn, Länge, Schriftart, Schriftgröße (in Welteinheiten und Punkten), Stilkennzeichen, Farbe, Textstil und Laufweite. |
| [`TextObject.TabStop`](#textobjecttabstop) | Klasse (verschachtelt) |  | Tabulatorstopp: Abstand vom linken Textrand in Welteinheiten sowie Ausrichtung. |
| [`TextObject.HorizontalAlignment`](#textobjecthorizontalalignment) | IntEnum (verschachtelt) |  | Horizontale Ausrichtung eines Textblocks. |
| [`TextObject.VerticalAlignment`](#textobjectverticalalignment) | IntEnum (verschachtelt) |  | Vertikale Ausrichtung eines Textblocks relativ zu seinem Ursprung. |
| [`TextObject.Spacing`](#textobjectspacing) | IntEnum (verschachtelt) |  | Zeilenabstand eines Textblocks; `Custom` verwendet den an `SetSpacing` übergebenen Zeilenabstand. |
| [`TextObject.TabAlignment`](#textobjecttabalignment) | IntEnum (verschachtelt) |  | Ausrichtung des Texts an einem Tabulatorstopp. |

## Klassen

### PrimitiveObject

> **Vollständiger Name:** `api.PrimitiveObject` · **Erbt von:** `api.Object`

Gemeinsame Basisklasse jeder Objektklasse der API (2D-Grundobjekte und über ihre Unterklassen 3D-, Beschriftungs-, Architektur-, Landschafts-, Spotlight- und ConnectCAD-Objekte). Eine Instanz bietet über ihren Handle eine leichtgewichtige Sicht auf ein Zeichnungsobjekt: Das Kopieren der Instanz kopiert nicht das Zeichnungsobjekt, und das Löschen der Instanz löscht nicht das Zeichnungsobjekt. So arbeiten Sie mit einem direkten Handle:

- Prüfen Sie zuerst den Typ: `if api.Line2DObject.Is(h): ...`
- Oder verwenden Sie `api.Document.As(api.Line2DObject, h)`; dies gibt das typisierte Objekt oder `None` zurück.
- `api.PrimitiveObject(h)` akzeptiert jeden Objekthandle.

Wird ein typisiertes Objekt aus dem Handle eines anderen Typs erzeugt, entsteht ein ungültiges Objekt (`IsValid()` ist `False`); Abfragemethoden geben dann `None` und Änderungsmethoden bzw. Operationen `False` zurück. API-weit gelten folgende Konventionen:

- Koordinaten werden in Welt- bzw. Modelleinheiten angegeben, Winkel im Bogenmaß gegen den Uhrzeigersinn ab der X-Achse; Zeichenfolgen sind UTF-8-kodiert.
- Wertabfragen geben `None` zurück, wenn ein Wert nicht verfügbar ist; Änderungsmethoden und Operationen geben einen Wert vom Typ `bool` zurück. Bei einem Fehlschlag geben Handle-Abfragen einen Null-Handle und Erzeugungsfunktionen ungültige Objekte zurück.
- Transformationen (Move, Rotate, Scale, Mirror) können dazu führen, dass Vectorworks den Handle des Zeichnungsobjekts ersetzt; das Python-Objekt übernimmt den neuen Handle automatisch. Vor der Transformation erstellte Kopien des Python-Objekts müssen aktualisiert werden.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `PrimitiveObject(h: Handle)` | Verweist auf ein beliebiges Zeichnungsobjekt `h` als allgemeines `PrimitiveObject`. |

**Methoden**

*Allgemein*

| Methode | Beschreibung |
|---|---|
| `GetHandle() -> Handle` | Handle des Zeichnungsobjekts. |
| `IsValid() -> bool` | Gibt True zurück, wenn dieses Objekt auf ein vorhandenes Zeichnungsobjekt verweist. |
| `GetObjectType() -> ObjectType` | Gibt den Objekttyp zurück. |

*Identität*

| Methode | Beschreibung |
|---|---|
| `GetName() -> str \| None` | Gibt den Namen zurück. |
| `SetName(name: str) -> bool` | Legt den Namen fest (schlägt fehl, wenn ein anderes Objekt diesen Namen verwendet). |
| `GetInternalIndex() -> int \| None` | Gibt den internen Index zurück. |

*Hierarchie*

| Methode | Beschreibung |
|---|---|
| `GetParent() -> Handle` | Gibt das übergeordnete Objekt zurück: Ebene, Gruppe, Symboldefinition, ... |
| `GetNext() -> Handle` | Nachbarobjekte in derselben Liste (VectorScript NextObj / PrevObj); ein Null-Handle nach dem letzten bzw. vor dem ersten Objekt. |
| `GetPrevious() -> Handle` | Gibt das vorherige Element zurück. |
| `MoveToContainer(container: Handle) -> bool` | Verschiebt das Objekt in einen Container (Ebene, Gruppe, ...). Wie die anderen Operationen zeichnet diese keine Rückgängig-Aktion auf: Damit das Verschieben eines Objekts in der Zeichnung rückgängig gemacht werden kann, rufen Sie davor `Document.AddBeforeMoveObject` und danach `Document.AddAfterMoveObject` auf; registrieren Sie ein dadurch eingefügtes neues Objekt mit `Document.AddAfterSwapObject`. Die Operation ändert nur die Zuordnung des Objekts: Sie setzt keine Tür und kein Fenster in eine Wand ein und nimmt diese auch nicht aus einer Wand heraus. Das Verschieben eines Objekts in eine Wand, ein Plug-in-Objekt, sich selbst oder eines seiner enthaltenen Objekte oder aus einem dieser Objekte heraus kann das Dokument beschädigen. Verschieben Sie Objekte nur zwischen Ebenen, Gruppen und Symboldefinitionen. Auch Symbole werden nicht geprüft: Wird eine Instanz eines Symbols oder eines Symbols, das auf beliebiger Verschachtelungstiefe eine Instanz davon enthält, in die zugehörige Symboldefinition (oder eine darin enthaltene Gruppe) verschoben, wird das Symbol in sich selbst verschachtelt. Dadurch entsteht eine Endlosschleife. |
| `GetFirstMember() -> Handle` | Enthaltene Objekte (Durchlaufen mit VectorScript FInGroup / LInGroup). Jeder Objekttyp kann durchlaufen werden; Objekte ohne enthaltene Objekte (Linien, Rechtecke, ...) geben einen Null-Handle bzw. eine leere Liste zurück. |
| `GetLastMember() -> Handle` | Gibt das letzte enthaltene Objekt zurück. |
| `ForEachMember(callback: callable(Handle)) -> None` | Nur direkt enthaltene Objekte. Das nächste enthaltene Objekt wird vor der Ausführung von `callback` abgefragt, sodass die Rückruffunktion das aktuelle Objekt löschen oder verschieben darf. |
| `GetMembers() -> list[Handle]` | Gibt die enthaltenen Objekte zurück. |

*Zustand*

| Methode | Beschreibung |
|---|---|
| `IsVisible() -> bool \| None` | Gibt True zurück, wenn das Objekt unter Berücksichtigung der Sichtbarkeit seiner Klasse und Ebene sichtbar ist. |
| `SetVisible(visible: bool) -> bool` | Schaltet *Sichtbar* ein oder aus. |
| `IsLocked() -> bool \| None` | Gibt True zurück, wenn das Objekt gesperrt ist. |
| `SetLocked(locked: bool) -> bool` | Schaltet *Gesperrt* ein oder aus. |
| `IsSelected() -> bool \| None` | Gibt True zurück, wenn das Objekt aktiviert ist. |
| `SetSelected(selected: bool) -> bool` | Schaltet *Aktiviert* ein oder aus. |

*Klasse*

| Methode | Beschreibung |
|---|---|
| `GetClass() -> ClassAttributes` | Gibt die Klasse zurück. |
| `SetClass(theClass: ClassAttributes, useClassAttributes: bool = False) -> bool` | Weist das Objekt `theClass` zu. Wenn `useClassAttributes` den Wert `True` hat, wird jedes Attribut des Objekts auf „nach Klasse“ gesetzt. |
| `Attributes() -> ObjectAttributes` | Grafische Attribute (Stift, Füllung, Linienendzeichen, Schlagschatten, ...) |

*Messung*

| Methode | Beschreibung |
|---|---|
| `GetBounds() -> Math.Rect2D \| None` | Gibt die Begrenzungen zurück. |
| `GetArea() -> float \| None` | Gibt den Flächeninhalt zurück. |
| `GetPerimeter() -> float \| None` | Gibt den Umfang zurück. |
| `GetBounds3D(layerRelative: bool = False) -> PrimitiveObject.Bounds3D \| None` | Gibt 3D-Grenzen mit den Ecken `minimum` und `maximum` (`Point3D`) zurück, die für jedes Objekt verfügbar sind (2D-Objekte liefern einen flachen Begrenzungsrahmen bei z = 0). Bei `layerRelative` = `False` wird die tatsächliche Z-Koordinate in Weltkoordinaten zurückgegeben; bei `True` wird die bisherige Ebenenhöhe abgezogen, entsprechend VectorScript Get3DCntr. Gibt `None` für ein ungültiges Objekt oder ein Objekt ohne Ausdehnung zurück. |
| `GetCenter3D(layerRelative: bool = False) -> Point3D \| None` | Mittelpunkt des 3D-Begrenzungsrahmens (VectorScript Get3DCntr mit layerRelative = `True`). |
| `GetSize3D() -> Point3D \| None` | Abmessungen des 3D-Begrenzungsrahmens: x = Breite, y = Höhe, z = Tiefe (VectorScript Get3DInfo). |
| `Move(offset: Math.Point2D) -> bool` | Transformationen (bei manchen Operationen kann sich der Objekthandle ändern; das Objekt übernimmt die Änderung). |
| `Move(dx: float, dy: float) -> bool` | Transformationen (bei manchen Operationen kann sich der Objekthandle ändern; das Objekt übernimmt die Änderung). |
| `Rotate(angle: float, center: Math.Point2D) -> bool` | Dreht das Objekt um den Winkel `angle` im Bogenmaß um `center`. Transformationen (bei manchen Operationen kann sich der Objekthandle ändern; das Objekt übernimmt die Änderung). |
| `Scale(scaleX: float, scaleY: float, center: Math.Point2D) -> bool` | Skaliert das Objekt um die Faktoren `scaleX` / `scaleY` relativ zu `center`. Transformationen (bei manchen Operationen kann sich der Objekthandle ändern; das Objekt übernimmt die Änderung). |
| `Mirror(axisStart: Math.Point2D, axisEnd: Math.Point2D) -> bool` | Spiegelt das Objekt an der Achse von `axisStart` nach `axisEnd`. Transformationen (bei manchen Operationen kann sich der Objekthandle ändern; das Objekt übernimmt die Änderung). |

*Lebensdauer*

| Methode | Beschreibung |
|---|---|
| `Reset() -> None` | Benachrichtigt Vectorworks, dass das Objekt extern geändert wurde. Nach mehreren zusammengefassten grundlegenden Bearbeitungsschritten aufrufen oder wenn das Objekt ein Plug-in-Objekt ist und neu erzeugt werden muss. |
| `Delete(useUndo: bool = True) -> bool` | Löscht das Objekt aus dem Dokument; das Objekt wird ungültig. |
| `ConvertToPolygon(keepOriginal: bool = False, resolution: int = 0) -> PolygonObject` | Umwandlung in ein neues Polygon- bzw. Polylinienobjekt. Ohne `keepOriginal` wird dieses Objekt durch das Ergebnis ersetzt und das Objekt wird ungültig, auch bei einer Umwandlung an Ort und Stelle. Eine fehlgeschlagene Umwandlung lässt das Ausgangsobjekt unverändert. Bei `resolution` = 0 wird die Umwandlungsauflösung des Dokuments verwendet. |
| `ConvertToPolyline(keepOriginal: bool = False) -> PolylineObject` | Wandelt das Objekt in eine Polylinie um. Umwandlung in ein neues Polygon- bzw. Polylinienobjekt. Ohne `keepOriginal` wird dieses Objekt durch das Ergebnis ersetzt und das Objekt wird ungültig, auch bei einer Umwandlung an Ort und Stelle. Eine fehlgeschlagene Umwandlung lässt das Ausgangsobjekt unverändert. Bei `resolution` = 0 wird die Umwandlungsauflösung des Dokuments verwendet. |

**Operatoren und Python-Protokolle**

| Operator | Methode | Beschreibung |
|---|---|---|
| `bool()` | `__bool__() -> bool` | `bool(a)`: True, wenn das Objekt gültig ist (entspricht `IsValid()`). |
| `==` | `__eq__(o: PrimitiveObject) -> bool` | `a == b`: Gibt True zurück, wenn beide Objekte auf dasselbe Zeichnungsobjekt verweisen. |
| `!=` | `__ne__(o: PrimitiveObject) -> bool` | `a != b`: Gibt True zurück, wenn die Objekte auf unterschiedliche Zeichnungsobjekte verweisen. |

#### PrimitiveObject.Bounds3D

> **Vollständiger Name:** `api.PrimitiveObject.Bounds3D` · **Erbt von:** `api.Object`

Achsenparalleler 3D-Begrenzungsrahmen in Welteinheiten

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `Bounds3D()` | Standardwert (Felder mit ihren Standardwerten). |
| `Bounds3D(minimum, maximum)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `minimum` | `Point3D` | Ecke mit den kleinsten Koordinaten. |
| `maximum` | `Point3D` | Ecke mit den größten Koordinaten. |

### Locus2DObject

> **Vollständiger Name:** `api.Locus2DObject` · **Erbt von:** [`PrimitiveObject`](#primitiveobject) → `api.Object`

2D-Punkt (`ObjectType.Locus`): ein Referenzpunkt.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `Locus2DObject(h: Handle)` | Verweist auf den vorhandenen 2D-Punkt `h`; vor der Verwendung `IsValid()` prüfen. |

**Methoden**

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | True, wenn `h` auf ein Objekt des von dieser Klasse dargestellten Typs verweist. |
| `Create(position: Math.Point2D) -> Locus2DObject` *statisch* | Erstellt einen 2D-Punkt auf der aktiven Ebene bzw. im aktuellen Container. |
| `Duplicate() -> Locus2DObject` | Dupliziert den 2D-Punkt in der Zeichnung und gibt die Kopie zurück. |
| `GetPosition() -> Math.Point2D \| None` | Gibt die Position zurück. |
| `SetPosition(position: Math.Point2D) -> bool` | Legt die Position fest. |
| `GetMasterSnapPoint() -> bool \| None` | Fangpunktverhalten, wenn sich der 2D-Punkt innerhalb einer Symboldefinition befindet. |
| `SetMasterSnapPoint(isMasterSnap: bool) -> bool` | Schaltet *Hauptfangpunkt* ein oder aus (Fangpunktverhalten, wenn sich der 2D-Punkt innerhalb einer Symboldefinition befindet). |
| `GetShowMasterSnapOutsideSnapBox() -> bool \| None` | Gibt an, ob *Hauptfangpunkt außerhalb der Fangbox anzeigen* eingeschaltet ist. |
| `SetShowMasterSnapOutsideSnapBox(show: bool) -> bool` | Schaltet *Hauptfangpunkt außerhalb der Fangbox anzeigen* ein oder aus. |
| `DistanceTo(pt: Math.Point2D) -> float \| None` | Abstand vom 2D-Punkt zu `pt`. |

Geerbt: alle Elemente von [`PrimitiveObject`](#primitiveobject).

### Line2DObject

> **Vollständiger Name:** `api.Line2DObject` · **Erbt von:** [`PrimitiveObject`](#primitiveobject) → `api.Object`

2D-Linie (`ObjectType.Line`): eine gerade Strecke zwischen zwei Punkten.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `Line2DObject(h: Handle)` | Verweist auf die vorhandene Linie `h`; vor der Verwendung `IsValid()` prüfen. |

**Methoden**

*Allgemein*

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | True, wenn `h` auf ein Objekt des von dieser Klasse dargestellten Typs verweist. |
| `Create(start: Math.Point2D, end: Math.Point2D) -> Line2DObject` *statisch* | Erstellt eine Linie auf der aktiven Ebene bzw. im aktuellen Container. |
| `Create(line: Math.Line2D) -> Line2DObject` *statisch* | Erstellt eine Linie auf der aktiven Ebene bzw. im aktuellen Container. |
| `Duplicate() -> Line2DObject` | Dupliziert die Linie in der Zeichnung und gibt die Kopie zurück. |

*Geometrie*

| Methode | Beschreibung |
|---|---|
| `GetLine() -> Math.Line2D \| None` | Gibt die Linie zurück. |
| `SetLine(line: Math.Line2D) -> bool` | Legt die Linie fest. |
| `SetLine(start: Math.Point2D, end: Math.Point2D) -> bool` | Legt die Linie fest. |
| `GetStartPoint() -> Math.Point2D \| None` | Gibt den Anfangspunkt zurück. |
| `SetStartPoint(pt: Math.Point2D) -> bool` | Legt den Anfangspunkt fest. |
| `GetEndPoint() -> Math.Point2D \| None` | Gibt den Endpunkt zurück. |
| `SetEndPoint(pt: Math.Point2D) -> bool` | Legt den Endpunkt fest. |

*Abgeleitete Werte*

| Methode | Beschreibung |
|---|---|
| `GetLength() -> float \| None` | Gibt die Länge zurück. |
| `SetLength(length: float) -> bool` | Legt die Länge fest (Anfangspunkt und Richtung bleiben erhalten). |
| `GetAngle() -> float \| None` | Gibt den Winkel zurück (Richtung vom Anfang zum Ende). |
| `SetAngle(angle: float) -> bool` | Legt den Winkel fest (dreht um den Anfangspunkt und behält die Länge bei). |
| `GetMidPoint() -> Math.Point2D \| None` | Gibt den Mittelpunkt zurück. |
| `GetDirection() -> Math.Point2D \| None` | Gibt die Richtung zurück (Einheitsvektor vom Anfang zum Ende). |

*Operationen*

| Methode | Beschreibung |
|---|---|
| `Reverse() -> bool` | Vertauscht Anfangs- und Endpunkt. |
| `Extend(atStart: float, atEnd: float) -> bool` | Verlängert die Linie um `atStart` vor dem Anfang und um `atEnd` nach dem Ende (negative Werte kürzen die Linie). |
| `OffsetParallel(distance: float) -> bool` | Verschiebt die Linie parallel um `distance` (positive Werte nach links, bezogen auf Anfang -> Ende). |

*Abfragen*

| Methode | Beschreibung |
|---|---|
| `ClosestPoint(pt: Math.Point2D) -> Math.Point2D \| None` | Punkt auf der Strecke mit dem geringsten Abstand zu `pt`. |
| `DistanceTo(pt: Math.Point2D) -> float \| None` | Kürzester Abstand von `pt` zur Strecke. |
| `Intersect(other: Line2DObject) -> Math.Point2D \| None` | Schnittpunkt mit einem anderen Linienobjekt (Strecken). |

Geerbt: alle Elemente von [`PrimitiveObject`](#primitiveobject).

### RectangularObject

> **Vollständiger Name:** `api.RectangularObject` · **Erbt von:** [`PrimitiveObject`](#primitiveobject) → `api.Object`

Gemeinsame Basisklasse der Klassen für Rechtecke und Radiusrechtecke. Die Geometrie ist ein möglicherweise gedrehtes Rechteck (`Math.RotatedRect2D`): eine Ecke (Ursprung), die Richtung der Breitenseite, die Breite und die Höhe.

**Konstruktoren**

Kann nicht direkt in Python instanziiert werden: Instanzen werden von anderen API-Funktionen zurückgegeben.

**Methoden**

*Allgemein*

| Methode | Beschreibung |
|---|---|
| `GetRect() -> Math.RotatedRect2D \| None` | Geometrie. |
| `SetRect(rect: Math.RotatedRect2D) -> bool` | Legt das Rechteck fest. |
| `GetOrigin() -> Math.Point2D \| None` | Gibt den Ursprung zurück. |
| `GetDirection() -> Math.Point2D \| None` | Gibt die Richtung zurück (Einheitsvektor entlang der Breitenseite). |
| `GetWidth() -> float \| None` | Gibt die Breite zurück. |
| `SetWidth(width: float) -> bool` | Legt die Breite fest (die Ursprungsecke bleibt erhalten). |
| `GetHeight() -> float \| None` | Gibt die Höhe zurück. |
| `SetHeight(height: float) -> bool` | Legt die Höhe fest (die Ursprungsecke bleibt erhalten). |
| `SetSize(width: float, height: float, keepCenter: bool = True) -> bool` | Setzt die Größe. |
| `GetCenter() -> Math.Point2D \| None` | Gibt den Mittelpunkt zurück. |
| `SetCenter(center: Math.Point2D) -> bool` | Legt den Mittelpunkt fest (verschiebt das Objekt). |
| `GetAngle() -> float \| None` | Gibt den Winkel zurück (Winkel der Breitenseite). |
| `SetAngle(angle: float) -> bool` | Legt den Winkel fest (dreht um den Mittelpunkt). |
| `IsAxisAligned() -> bool \| None` | Gibt True zurück, wenn das Rechteck nicht gedreht ist (seine Seiten verlaufen parallel zu den Achsen). |
| `GetCorners() -> tuple[Math.Point2D * 4] \| None` | Ecken gegen den Uhrzeigersinn, beginnend am Ursprung (bei positiver Breite und Höhe). |
| `SetBounds(bounds: Math.Rect2D) -> bool` | Legt ein ungedrehtes Rechteck fest. |

*Abfragen*

| Methode | Beschreibung |
|---|---|
| `Contains(pt: Math.Point2D) -> bool` | Gibt True zurück, wenn `pt` innerhalb des Rechtecks oder auf seinem Rand liegt. |
| `GetPolygon() -> Math.Polygon2D \| None` | Gibt das Polygon zurück (die vier Ecken; Eckrundungen werden ignoriert). |

Geerbt: alle Elemente von [`PrimitiveObject`](#primitiveobject).

### RectangleObject

> **Vollständiger Name:** `api.RectangleObject` · **Erbt von:** [`RectangularObject`](#rectangularobject) → [`PrimitiveObject`](#primitiveobject) → `api.Object`

Rechteck (`ObjectType.Box`), gegebenenfalls gedreht.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `RectangleObject(h: Handle)` | Verweist auf das vorhandene Rechteck `h`; vor der Verwendung `IsValid()` prüfen. |

**Methoden**

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | True, wenn `h` auf ein Objekt des von dieser Klasse dargestellten Typs verweist. |
| `Create(rect: Math.RotatedRect2D) -> RectangleObject` *statisch* | Erstellt ein Rechteck auf der aktiven Ebene bzw. im aktuellen Container. Breite und Höhe dürfen nicht null sein. |
| `Create(bounds: Math.Rect2D) -> RectangleObject` *statisch* | Erstellt ein Rechteck auf der aktiven Ebene bzw. im aktuellen Container. Breite und Höhe dürfen nicht null sein. |
| `Create(center: Math.Point2D, width: float, height: float, angle: float = 0.0) -> RectangleObject` *statisch* | Erstellt ein Rechteck auf der aktiven Ebene bzw. im aktuellen Container. Breite und Höhe dürfen nicht null sein. |
| `Duplicate() -> RectangleObject` | Dupliziert das Rechteck in der Zeichnung und gibt die Kopie zurück. |
| `IsSquare() -> bool \| None` | Gibt True zurück, wenn Breite und Höhe gleich sind. |

Geerbt: alle Elemente von [`RectangularObject`](#rectangularobject), [`PrimitiveObject`](#primitiveobject).

### CornerDiameters

> **Vollständiger Name:** `api.CornerDiameters` · **Erbt von:** `api.Object`

Eckenrundung eines Radiusrechtecks: die Durchmesser der Eckellipse entlang der Breitenseite (alongWidth) und der Höhenseite (alongHeight).

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `CornerDiameters()` | Standardwert (Felder mit ihren Standardwerten). |
| `CornerDiameters(alongWidth, alongHeight)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Operatoren und Python-Protokolle**

| Operator | Methode | Beschreibung |
|---|---|---|
| `==` | `__eq__(o: CornerDiameters) -> bool` | `a == b`: True, wenn die beiden Werte gleich sind. |
| `!=` | `__ne__(o: CornerDiameters) -> bool` | `a != b`: True, wenn sich die beiden Werte unterscheiden. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `alongWidth` | `float` | Eckdurchmesser entlang der Breitenseite. |
| `alongHeight` | `float` | Eckdurchmesser entlang der Höhenseite. |

### RoundRectObject

> **Vollständiger Name:** `api.RoundRectObject` · **Erbt von:** [`RectangularObject`](#rectangularobject) → [`PrimitiveObject`](#primitiveobject) → `api.Object`

Radiusrechteck (`ObjectType.RoundedRectangle`), gegebenenfalls gedreht.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `RoundRectObject(h: Handle)` | Verweist auf das vorhandene Radiusrechteck `h`; vor der Verwendung `IsValid()` prüfen. |

**Methoden**

*Allgemein*

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | True, wenn `h` auf ein Objekt des von dieser Klasse dargestellten Typs verweist. |
| `Create(rect: Math.RotatedRect2D, corners: CornerDiameters, proportional: bool = False) -> RoundRectObject` *statisch* | Erstellt ein Radiusrechteck auf der aktiven Ebene bzw. im aktuellen Container. Breite und Höhe dürfen nicht null sein. Mit `proportional` werden die Eckdurchmesser bei einer interaktiven Größenänderung proportional zum Rechteck skaliert. |
| `Create(bounds: Math.Rect2D, corners: CornerDiameters, proportional: bool = False) -> RoundRectObject` *statisch* | Erstellt ein Radiusrechteck auf der aktiven Ebene bzw. im aktuellen Container. Breite und Höhe dürfen nicht null sein. Mit `proportional` werden die Eckdurchmesser bei einer interaktiven Größenänderung proportional zum Rechteck skaliert. |
| `Create(center: Math.Point2D, width: float, height: float, cornerRadius: float, angle: float = 0.0) -> RoundRectObject` *statisch* | Erstellt ein Radiusrechteck auf der aktiven Ebene bzw. im aktuellen Container. Breite und Höhe dürfen nicht null sein. Mit `proportional` werden die Eckdurchmesser bei einer interaktiven Größenänderung proportional zum Rechteck skaliert. |
| `Duplicate() -> RoundRectObject` | Dupliziert das Radiusrechteck in der Zeichnung und gibt die Kopie zurück. |

*Eckrundung*

| Methode | Beschreibung |
|---|---|
| `GetCornerDiameters() -> CornerDiameters \| None` | Gibt die Eckdurchmesser zurück. |
| `SetCornerDiameters(corners: CornerDiameters) -> bool` | Legt die Eckdurchmesser fest. |
| `GetCornerRadius() -> float \| None` | Radius kreisförmiger Ecken (bei elliptischen Ecken der Mittelwert). |
| `SetCornerRadius(radius: float) -> bool` | Legt den Eckradius fest (Radius kreisförmiger Ecken; bei elliptischen Ecken der Mittelwert). |
| `HasCircularCorners() -> bool \| None` | Gibt True zurück, wenn die Ecken kreisförmig sind (gleiche Eckbreite und -höhe). |

Geerbt: alle Elemente von [`RectangularObject`](#rectangularobject), [`PrimitiveObject`](#primitiveobject).

### ArcObject

> **Vollständiger Name:** `api.ArcObject` · **Erbt von:** [`PrimitiveObject`](#primitiveobject) → `api.Object`

Kreisbogen (`ObjectType.Arc`). Winkel werden im Bogenmaß gegen den Uhrzeigersinn ab der X-Achse angegeben. Das Dokument speichert Kreisbögen stets gegen den Uhrzeigersinn: Ein an eine Änderungsmethode übergebener negativer Öffnungswinkel wird normalisiert, sodass `GetSweepAngle()` immer positiv ist. Auch Vollkreise sind Kreisbögen; siehe auch CircleObject.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `ArcObject(h: Handle)` | Verweist auf den vorhandenen Kreisbogen `h`; vor der Verwendung `IsValid()` prüfen. |

**Methoden**

*Allgemein*

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | Gibt True zurück, wenn `h` auf ein Objekt der von dieser Klasse dargestellten Art verweist (jedes `ObjectType.Arc`, einschließlich Vollkreisen). |
| `Create(arc: Math.Arc2D) -> ArcObject` *statisch* | Erstellt einen Kreisbogen auf der aktiven Ebene / im aktuellen Container. Radius und Öffnungswinkel dürfen nicht null sein. |
| `Create(center: Math.Point2D, radius: float, startAngle: float, sweepAngle: float) -> ArcObject` *statisch* | Erstellt einen Kreisbogen auf der aktiven Ebene / im aktuellen Container. Radius und Öffnungswinkel dürfen nicht null sein. |
| `CreateThreePoints(start: Math.Point2D, onArc: Math.Point2D, end: Math.Point2D) -> ArcObject` *statisch* | Erstellt einen Kreisbogen durch die drei Punkte `start`, `onArc` und `end` auf der aktiven Ebene bzw. im aktuellen Container. |
| `Duplicate() -> ArcObject` | Dupliziert den Kreisbogen in der Zeichnung und gibt die Kopie zurück. |

*Geometrie*

| Methode | Beschreibung |
|---|---|
| `GetArc() -> Math.Arc2D \| None` | Gibt den Kreisbogen zurück. |
| `SetArc(arc: Math.Arc2D) -> bool` | Legt den Kreisbogen fest. |
| `GetCenter() -> Math.Point2D \| None` | Gibt den Mittelpunkt zurück. |
| `SetCenter(center: Math.Point2D) -> bool` | Legt den Mittelpunkt fest. |
| `GetRadius() -> float \| None` | Gibt den Radius zurück. |
| `SetRadius(radius: float) -> bool` | Legt den Radius fest. |
| `GetStartAngle() -> float \| None` | Gibt den Anfangswinkel zurück. |
| `SetStartAngle(angle: float) -> bool` | Legt den Anfangswinkel fest (der Endwinkel bleibt erhalten). |
| `GetSweepAngle() -> float \| None` | Gibt den Öffnungswinkel zurück. |
| `SetSweepAngle(sweep: float) -> bool` | Legt den Öffnungswinkel fest (der Anfangswinkel bleibt erhalten). |
| `GetEndAngle() -> float \| None` | Gibt den Endwinkel zurück. |
| `SetEndAngle(angle: float) -> bool` | Legt den Endwinkel fest (der Anfangswinkel bleibt erhalten). |
| `SetAngles(startAngle: float, sweepAngle: float) -> bool` | Legt die Winkel fest. |
| `GetStartPoint() -> Math.Point2D \| None` | Gibt den Anfangspunkt zurück. |
| `GetEndPoint() -> Math.Point2D \| None` | Gibt den Endpunkt zurück. |
| `GetMidPoint() -> Math.Point2D \| None` | Gibt den Mittelpunkt zurück. |
| `GetChord() -> Math.Line2D \| None` | Gibt die Sehne zurück. |

*Maße*

| Methode | Beschreibung |
|---|---|
| `GetLength() -> float \| None` | Gibt die Länge zurück. |
| `GetChordLength() -> float \| None` | Gibt die Sehnenlänge zurück. |
| `GetSagitta() -> float \| None` | Gibt die Pfeilhöhe zurück. |
| `IsCircle() -> bool \| None` | Gibt True zurück, wenn der Kreisbogen ein Vollkreis ist. |

*Abfragen*

| Methode | Beschreibung |
|---|---|
| `ClosestPoint(pt: Math.Point2D) -> Math.Point2D \| None` | Der `pt` nächstgelegene Punkt des Bogens. |
| `DistanceTo(pt: Math.Point2D) -> float \| None` | Kürzester Abstand von `pt` zum Kreisbogen. |
| `Intersect(other: ArcObject) -> list[Math.Point2D]` | Schnittpunkte mit dem Kreisbogen `other`. |
| `Intersect(line: Math.Line2D) -> list[Math.Point2D]` | Schnittpunkte mit der Strecke `line`. |

Geerbt: alle Elemente von [`PrimitiveObject`](#primitiveobject).

### CircleObject

> **Vollständiger Name:** `api.CircleObject` · **Erbt von:** [`PrimitiveObject`](#primitiveobject) → `api.Object`

Kreis. Im Dokument ist ein Kreis ein Kreisbogen (`ObjectType.Arc`) mit einem vollen Öffnungswinkel von 360 Grad.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `CircleObject(h: Handle)` | Verweist auf den vorhandenen Kreis `h`; vor der Verwendung `IsValid()` prüfen. |

**Methoden**

*Allgemein*

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | Gibt True zurück, wenn `h` auf ein Objekt der von dieser Klasse dargestellten Art verweist (`ObjectType.Arc` mit vollem Öffnungswinkel). |
| `Create(circle: Math.Circle2D) -> CircleObject` *statisch* | Erstellt einen Kreis auf der aktiven Ebene / im aktuellen Container. Der Radius muss positiv sein. |
| `Create(center: Math.Point2D, radius: float) -> CircleObject` *statisch* | Erstellt einen Kreis auf der aktiven Ebene / im aktuellen Container. Der Radius muss positiv sein. |
| `CreateThreePoints(p1: Math.Point2D, p2: Math.Point2D, p3: Math.Point2D) -> CircleObject` *statisch* | Erstellt einen Kreis durch die drei Punkte `p1`, `p2` und `p3` auf der aktiven Ebene bzw. im aktuellen Container. |
| `Duplicate() -> CircleObject` | Dupliziert den Kreis in der Zeichnung und gibt die Kopie zurück. |
| `AsArc() -> ArcObject` | Dasselbe Objekt als `ArcObject` betrachtet (ein Kreis ist ein Kreisbogen mit vollem Öffnungswinkel). |

*Geometrie*

| Methode | Beschreibung |
|---|---|
| `GetCircle() -> Math.Circle2D \| None` | Gibt den Kreis zurück. |
| `SetCircle(circle: Math.Circle2D) -> bool` | Legt den Kreis fest. |
| `GetCenter() -> Math.Point2D \| None` | Gibt den Mittelpunkt zurück. |
| `SetCenter(center: Math.Point2D) -> bool` | Legt den Mittelpunkt fest. |
| `GetRadius() -> float \| None` | Gibt den Radius zurück. |
| `SetRadius(radius: float) -> bool` | Legt den Radius fest. |
| `GetDiameter() -> float \| None` | Gibt den Durchmesser zurück. |
| `SetDiameter(diameter: float) -> bool` | Legt den Durchmesser fest. |

*Maße*

| Methode | Beschreibung |
|---|---|
| `GetCircumference() -> float \| None` | Gibt den Kreisumfang zurück. |

*Abfragen*

| Methode | Beschreibung |
|---|---|
| `Contains(pt: Math.Point2D) -> bool` | Gibt True zurück, wenn `pt` innerhalb des Kreises oder auf ihm liegt. |
| `ClosestPoint(pt: Math.Point2D) -> Math.Point2D \| None` | Der `pt` nächstgelegene Kreispunkt. |
| `DistanceTo(pt: Math.Point2D) -> float \| None` | Abstand von `pt` zur Kreislinie. |
| `PointAt(angle: float) -> Math.Point2D \| None` | Punkt auf dem Kreis beim Winkel `angle` (im Bogenmaß, gegen den Uhrzeigersinn ab der X-Achse). |
| `Intersect(other: CircleObject) -> list[Math.Point2D]` | Schnittpunkte mit dem Kreis `other`. |
| `Intersect(line: Math.Line2D) -> list[Math.Point2D]` | Schnittpunkte mit der Strecke `line`. |
| `GetTangentPoints(from_: Math.Point2D) -> list[Math.Point2D]` | Gibt die Tangentialpunkte für `from_` zurück. |

Geerbt: alle Elemente von [`PrimitiveObject`](#primitiveobject).

### PolyObject

> **Vollständiger Name:** `api.PolyObject` · **Erbt von:** [`PrimitiveObject`](#primitiveobject) → `api.Object`

Gemeinsame Basisklasse der Polygon- und Polylinienklassen. Scheitelpunktindizes beginnen bei 0. Die Sichtbarkeit eines Scheitelpunkts entspricht der Sichtbarkeit der Kante, die an ihm beginnt.

**Konstruktoren**

Kann nicht direkt in Python instanziiert werden: Instanzen werden von anderen API-Funktionen zurückgegeben.

**Methoden**

*Scheitelpunkte*

| Methode | Beschreibung |
|---|---|
| `GetVertexCount() -> int` | Anzahl der Scheitelpunkte. |
| `GetVertex(index: int) -> Math.PolyVertex \| None` | Gibt den Scheitelpunkt bei `index` zurück. |
| `GetVertexPoint(index: int) -> Math.Point2D \| None` | Gibt den Scheitelpunkt am Index `index` zurück. |
| `SetVertexPoint(index: int, pt: Math.Point2D) -> bool` | Legt den Scheitelpunkt am Index `index` fest (der Scheitelpunkttyp bleibt erhalten). |
| `GetVertexPoints() -> list[Math.Point2D]` | Gibt die Scheitelpunkte zurück. |
| `DeleteVertex(index: int) -> bool` | Löscht den Scheitelpunkt am Index `index`. |
| `DeleteAllVertices() -> bool` | Löscht alle Scheitelpunkte. |

*Kantensichtbarkeit*

| Methode | Beschreibung |
|---|---|
| `GetVertexVisible(index: int) -> bool \| None` | Gibt an, ob *Scheitelpunkt sichtbar* am Index `index` eingeschaltet ist. |
| `SetVertexVisible(index: int, visible: bool) -> bool` | Legt die Sichtbarkeit des Scheitelpunkts am Index `index` fest. |
| `SetAllVerticesVisible(visible: bool) -> bool` | Schaltet *Alle Scheitelpunkte sichtbar* ein oder aus. |

*Geschlossen / offen*

| Methode | Beschreibung |
|---|---|
| `IsClosed() -> bool \| None` | Gibt True zurück, wenn die Form geschlossen ist. |
| `SetClosed(closed: bool) -> bool` | Schaltet *Geschlossen* ein oder aus. |

*Gesamte Geometrie*

| Methode | Beschreibung |
|---|---|
| `GetPolygon() -> Math.Polygon2D \| None` | Gibt das Polygon zurück. |

*Orientierung*

| Methode | Beschreibung |
|---|---|
| `IsClockwise() -> bool \| None` | Gibt True zurück, wenn die Scheitelpunkte im Uhrzeigersinn angeordnet sind. |
| `Reverse() -> bool` | Kehrt die Reihenfolge der Scheitelpunkte um und behält die Kantensichtbarkeit bei. |
| `SetClockwise(clockwise: bool) -> bool` | Schaltet *Im Uhrzeigersinn* ein oder aus. |
| `GetPolyArea() -> float \| None` | Messung (die Basismethoden GetArea / GetPerimeter liefern über die allgemeinen Objektaufrufe dieselben Ergebnisse). |
| `GetPolyPerimeter() -> float \| None` | Gibt den Umfang der Polygonform zurück. |
| `GetCurveLength() -> float \| None` | Tatsächlich gekrümmter äußerer Pfad in der lokalen XY-Ebene des Objekts. Diese Abfragen lassen die Zeichnung unverändert, berücksichtigen unsichtbare und schließende Kanten, schließen Löcher aus und verwenden keine Längen des Kontrollpolygons. Siehe `Math.Polygon2D` zu Abstandsgrenzen, temporären NURBS-Parametern und der Behandlung von Endpunkten. |
| `GetCurveLocationAtDistance(distance: float) -> Math.Polygon2D.CurveLocation \| None` | Gibt die Kurvenposition im Abstand für `distance` zurück. |
| `GetCurvePointAtDistance(distance: float) -> Math.Point2D \| None` | Gibt den Kurvenpunkt im Abstand für `distance` zurück. |
| `GetCurveTangentAtDistance(distance: float) -> Math.Point2D \| None` | Gibt die Kurventangente im Abstand für `distance` zurück. |
| `GetCurveCurvatureAtDistance(distance: float) -> float \| None` | Gibt die Kurvenkrümmung im Abstand für `distance` zurück. |
| `GetCurveClosestPoint(point: Math.Point2D) -> Math.Polygon2D.CurveLocation \| None` | Gibt den nächstgelegenen Kurvenpunkt für `point` zurück. |
| `GetCurveDistanceTo(point: Math.Point2D) -> float \| None` | Gibt den Abstand von `point` zur Kurve zurück. |
| `DivideCurveByCount(count: int, includeEnd: bool = True) -> list[Math.Point2D] \| None` | Genau `count` (>= 2) gleichmäßig entlang des tatsächlich gekrümmten Pfads verteilte Punkte (`includeEnd=False` lässt den letzten Endpunkt bzw. die Nahtstelle aus); bei einem Fehlschlag `None`. Tatsächlich gekrümmter äußerer Pfad in der lokalen XY-Ebene des Objekts. Diese Abfragen lassen die Zeichnung unverändert, berücksichtigen unsichtbare und schließende Kanten, schließen Löcher aus und verwenden keine Längen des Kontrollpolygons. Siehe `Math.Polygon2D` zu Abstandsgrenzen, temporären NURBS-Parametern und der Behandlung von Endpunkten. |
| `Contains(pt: Math.Point2D) -> bool` | Abfragen am Scheitelpunktpolygon (Kurvenpunkte werden als Kontrollpunkte behandelt). |
| `ClosestPoint(pt: Math.Point2D) -> Math.Point2D \| None` | Punkt auf dem Scheitelpunktpolygon mit dem geringsten Abstand zu `pt`. Abfragen am Scheitelpunktpolygon (Kurvenpunkte werden als Kontrollpunkte behandelt). |
| `DistanceTo(pt: Math.Point2D) -> float \| None` | Abstand von `pt` zum Scheitelpunktpolygon. Abfragen am Scheitelpunktpolygon (Kurvenpunkte werden als Kontrollpunkte behandelt). |
| `GetCentroid() -> Math.Point2D \| None` | Gibt den Schwerpunkt zurück. |
| `IsConvex() -> bool \| None` | Gibt True zurück, wenn die Form konvex ist. |
| `IsSelfIntersecting() -> bool \| None` | Gibt True zurück, wenn sich zwei nicht benachbarte Kanten schneiden. |
| `Intersect(line: Math.Line2D) -> list[Math.Point2D]` | Schnittpunkte des Scheitelpunktpolygons mit der Strecke `line`. Abfragen am Scheitelpunktpolygon (Kurvenpunkte werden als Kontrollpunkte behandelt). |
| `BooleanUnion(other: PolyObject) -> list[Handle]` | Vereinigung mit `other`: eine möglicherweise leere Liste von Handles noch nicht eingefügter Ergebnisobjekte mit den Attributen dieser Form; beide Eingabeobjekte bleiben unverändert. Fügen Sie die Ergebnisse mit `PrimitiveObject(h).MoveToContainer(...)` ein oder löschen Sie sie. Löst bei ungültiger Eingabe `RuntimeError` aus. |
| `BooleanIntersection(other: PolyObject) -> list[Handle]` | Schnittmenge mit `other`: eine möglicherweise leere Liste von Handles noch nicht eingefügter Ergebnisobjekte; beide Eingabeobjekte bleiben unverändert. Löst bei ungültiger Eingabe `RuntimeError` aus. |
| `BooleanDifference(other: PolyObject) -> list[Handle]` | Diese Form abzüglich `other`: eine möglicherweise leere Liste von Handles noch nicht eingefügter Ergebnisobjekte; beide Eingabeobjekte bleiben unverändert. Löst bei ungültiger Eingabe `RuntimeError` aus. |
| `BooleanSymmetricDifference(other: PolyObject) -> list[Handle]` | Bereiche, die von genau einer der beiden Formen abgedeckt werden: eine möglicherweise leere Liste von Handles noch nicht eingefügter Ergebnisobjekte; beide Eingabeobjekte bleiben unverändert. Löst bei ungültiger Eingabe `RuntimeError` aus. |
| `IsCombinableShape(h: Handle) -> bool` *statisch* | Gibt an, ob CombineShapes den Handle `h` als Operanden akzeptiert (eine 2D-Form, die von den booleschen 2D-Operationen unterstützt wird). |
| `AreShapesInOnePlane(first: Handle, second: Handle) -> bool` *statisch* | Gibt an, ob `first` und `second` in derselben Ebene liegen (dieselbe Ebenenreferenz-ID haben), wie von CombineShapes gefordert. |
| `AlignShapePlanes(first: Handle, second: Handle) -> bool` *statisch* | Verschiebt zwei koplanare Formen in dieselbe Ebene, wie es die Befehle Ändern > Flächen zusammenfügen / Schnittfläche löschen / Schnittfläche bilden vor dem Kombinieren von Formen tun. Gibt `True` zurück, wenn beide Formen danach in derselben Ebene liegen (auch wenn dies bereits der Fall war); gibt `False` zurück, wenn sie nicht koplanar sind, eine Form einen Null-Handle hat oder nicht kombinierbar ist oder beide dasselbe Objekt sind. Ändert die Ebene der verschobenen Formen und zeichnet keine Rückgängig-Aktion auf: Registrieren Sie vor dem Aufruf beide Formen (`Document.AddBothSwapObject`). |
| `CombineShapes(operation: PolyObject.BooleanOperation, first: Handle, second: Handle) -> list[Handle]` *statisch* | Kombiniert die 2D-Formen `first` und `second` mit `operation`: eine möglicherweise leere Liste von Handles noch nicht eingefügter Ergebnisobjekte mit den Attributen von `first`; die Eingabeobjekte bleiben unverändert. Löst bei ungültiger Eingabe `RuntimeError` aus (eine Form mit Null-Handle oder eine nicht kombinierbare Form, dasselbe Objekt zweimal, Formen in unterschiedlichen Ebenen oder eine unbekannte Operation). |

Geerbt: alle Elemente von [`PrimitiveObject`](#primitiveobject).

#### PolyObject.BooleanOperation

> **Vollständiger Name:** `api.PolyObject.BooleanOperation` · **Art:** `IntEnum`

Operation der booleschen 2D-Funktionen

| Element | Wert | Beschreibung |
|---|---|---|
| `Union` | `0` |  |
| `Intersection` | `1` |  |
| `Difference` | `2` | `first` abzüglich `second`. |
| `SymmetricDifference` | `3` | Die Bereiche, die von genau einer der beiden Formen abgedeckt werden. |

### PolygonObject

> **Vollständiger Name:** `api.PolygonObject` · **Erbt von:** [`PolyObject`](#polyobject) → [`PrimitiveObject`](#primitiveobject) → `api.Object`

Polygon (`ObjectType.Polygon` sowie Freihandpolygone `ObjectType.FreehandPolygon`): nur Eckpunkte. Verwenden Sie PolylineObject für Kurvenscheitelpunkte.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `PolygonObject(h: Handle)` | Verweist auf das vorhandene Polygon `h`; vor der Verwendung `IsValid()` prüfen. |

**Methoden**

*Allgemein*

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | True, wenn `h` auf ein Objekt des von dieser Klasse dargestellten Typs verweist. |
| `Create(poly: Math.Polygon2D) -> PolygonObject` *statisch* | Erstellt ein Polygon auf der aktiven Ebene bzw. im aktuellen Container (mindestens zwei Scheitelpunkte). Kurvenpunkte von `poly` werden als Eckpunkte hinzugefügt. |
| `Create(points: list[Math.Point2D], closed: bool = True) -> PolygonObject` *statisch* | Erstellt ein Polygon auf der aktiven Ebene bzw. im aktuellen Container (mindestens zwei Scheitelpunkte). Kurvenpunkte von `poly` werden als Eckpunkte hinzugefügt. |
| `Create(rect: Math.Rect2D) -> PolygonObject` *statisch* | Erstellt ein Polygon auf der aktiven Ebene bzw. im aktuellen Container (mindestens zwei Scheitelpunkte). Kurvenpunkte von `poly` werden als Eckpunkte hinzugefügt. |
| `CreateRegular(center: Math.Point2D, circumradius: float, sides: int, startAngle: float = 0.0) -> PolygonObject` *statisch* | Erstellt auf der aktiven Ebene bzw. im aktuellen Container ein regelmäßiges Polygon mit `sides` Ecken auf einem Kreis mit Radius `circumradius` um `center` (erste Ecke bei `startAngle`). |
| `Duplicate() -> PolygonObject` | Dupliziert das Polygon in der Zeichnung und gibt die Kopie zurück. |
| `IsFreehand() -> bool \| None` | Gibt True zurück, wenn das Polygon ein Freihandpolygon ist (`ObjectType.FreehandPolygon`). |

*Scheitelpunkte*

| Methode | Beschreibung |
|---|---|
| `AddVertex(pt: Math.Point2D, visible: bool = True) -> bool` | Hängt einen Scheitelpunkt bei `pt` an; `visible` bestimmt, ob die Kante zum nächsten Scheitelpunkt gezeichnet wird. |
| `InsertVertex(beforeIndex: int, pt: Math.Point2D, visible: bool = True) -> bool` | Fügt einen Scheitelpunkt bei `pt` vor dem Scheitelpunkt `beforeIndex` ein; `visible` steuert die Kantensichtbarkeit. |
| `SetPolygon(poly: Math.Polygon2D) -> bool` | Ersetzt alle Scheitelpunkte und das Kennzeichen für die geschlossene Form (Kurvenpunkte werden als Eckpunkte festgelegt). |
| `SetVertexPoints(points: list[Math.Point2D]) -> bool` | Legt die Scheitelpunkte fest (das Kennzeichen für die geschlossene Form bleibt erhalten). |

Geerbt: alle Elemente von [`PolyObject`](#polyobject), [`PrimitiveObject`](#primitiveobject).

### PolylineObject

> **Vollständiger Name:** `api.PolylineObject` · **Erbt von:** [`PolyObject`](#polyobject) → [`PrimitiveObject`](#primitiveobject) → `api.Object`

Polylinie (`ObjectType.Polyline`): eine Polygonform, deren Scheitelpunkte Eck-, Bézier-, kubische, Bogen- oder Radiuspunkte sein können. Scheitelpunkte sind Kontrollpunkte; die Kurve verläuft nur durch Eckpunkte (sowie durch Bogenpunkte mit einem Radius ungleich null, wenn dieser hineinpasst).

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `PolylineObject(h: Handle)` | Verweist auf die vorhandene Polylinie `h`; vor der Verwendung `IsValid()` prüfen. |

**Methoden**

*Allgemein*

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | True, wenn `h` auf ein Objekt des von dieser Klasse dargestellten Typs verweist. |
| `Create(poly: Math.Polygon2D) -> PolylineObject` *statisch* | Erstellt eine Polylinie auf der aktiven Ebene bzw. im aktuellen Container (mindestens zwei Scheitelpunkte). Das Ergebnis ist immer eine Polylinie, auch wenn alle Scheitelpunkte Eckpunkte sind. |
| `CreateCircle(center: Math.Point2D, radius: float) -> PolylineObject` *statisch* | Geschlossene Polylinie aus vier Radiuspunkten, die einen Kreis bildet. |
| `CreateFilletedRect(rect: Math.Rect2D, cornerRadius: float) -> PolylineObject` *statisch* | Geschlossene Polylinie eines Rechtecks mit abgerundeten Ecken. |
| `Duplicate() -> PolylineObject` | Dupliziert die Polylinie in der Zeichnung und gibt die Kopie zurück. |

*Typisierte Scheitelpunkte*

| Methode | Beschreibung |
|---|---|
| `AddVertex(vertex: Math.PolyVertex) -> bool` | Hängt den Scheitelpunkt `vertex` an (Punkt, Scheitelpunkttyp, Bogenradius und Kantensichtbarkeit). |
| `AddVertex(pt: Math.Point2D, type: Math.VertexType = Math.VertexType.Corner, arcRadius: float = 0.0) -> bool` | Hängt bei `pt` einen Scheitelpunkt des Typs `type` an (`arcRadius` für Radiuspunkte). |
| `InsertVertex(beforeIndex: int, vertex: Math.PolyVertex) -> bool` | Fügt den Scheitelpunkt `vertex` vor dem Scheitelpunkt `beforeIndex` ein. |
| `SetVertex(index: int, vertex: Math.PolyVertex) -> bool` | Legt den Scheitelpunkt am Index `index` fest. |
| `GetVertexType(index: int) -> Math.VertexType \| None` | Gibt den Scheitelpunkttyp am Index `index` zurück. |
| `SetVertexType(index: int, type: Math.VertexType) -> bool` | Legt den Scheitelpunkttyp am Index `index` fest. |
| `GetVertexArcRadius(index: int) -> float \| None` | Gibt den Bogenradius des Scheitelpunkts am Index `index` zurück (0 für Scheitelpunkte, die keine Bogenpunkte sind). |
| `SetVertexArcRadius(index: int, radius: float) -> bool` | Legt den Bogenradius des Scheitelpunkts am Index `index` fest (macht den Scheitelpunkt zu einem Bogenpunkt). |
| `GetVertexMaxRadius(index: int) -> float \| None` | Größter Radius, mit dem ein Bogenpunkt zwischen seine Nachbarpunkte passt. |
| `GetControlVertex(index: int) -> Math.PolyVertex \| None` | Kontrollpunkt, wie er im Dokument gespeichert ist (bei Bogenpunkten der Punkt, der die Abrundung definiert). |
| `HasCurves() -> bool \| None` | Gibt True zurück, wenn die Polylinie Kurvenpunkte enthält (Bézier-, kubische, Bogen- oder Radiuspunkte). |

*Ersetzt alle Scheitelpunkte und das Kennzeichen für die geschlossene Form*

| Methode | Beschreibung |
|---|---|
| `SetPolygon(poly: Math.Polygon2D) -> bool` | Legt das Polygon fest. |

Geerbt: alle Elemente von [`PolyObject`](#polyobject), [`PrimitiveObject`](#primitiveobject).

### GroupObject

> **Vollständiger Name:** `api.GroupObject` · **Erbt von:** [`PrimitiveObject`](#primitiveobject) → `api.Object`

Gruppe (`ObjectType.Group`): ein Container für andere Objekte. Enthaltene Objekte werden mit den entsprechenden Methoden von PrimitiveObject durchlaufen (GetFirstMember, ForEachMember, GetMembers, ...).

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `GroupObject(h: Handle)` | Verweist auf die vorhandene Gruppe `h`; vor der Verwendung `IsValid()` prüfen. |

**Methoden**

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | True, wenn `h` auf ein Objekt des von dieser Klasse dargestellten Typs verweist. |
| `Create() -> GroupObject` *statisch* | Erstellt eine leere Gruppe auf der aktiven Ebene bzw. im aktuellen Container. |
| `Create(members: list[Handle]) -> GroupObject` *statisch* | Erstellt eine Gruppe auf der aktiven Ebene bzw. im aktuellen Container und verschiebt `members` hinein. Null-Handles werden übersprungen. |
| `CreateFromSelection() -> GroupObject` *statisch* | Gruppiert die aktivierten Objekte der aktiven Ebene (VectorScript Group). |
| `Duplicate() -> GroupObject` | Dupliziert die Gruppe in der Zeichnung und gibt die Kopie zurück. |
| `GetMemberCount() -> int \| None` | Anzahl der enthaltenen Objekte. |
| `AddMember(h: Handle) -> bool` | Verschiebt `h` als letztes enthaltenes Objekt in die Gruppe und aktualisiert die Gruppenbegrenzungen. |
| `Ungroup() -> bool` | Verschiebt die enthaltenen Objekte in den Container der Gruppe und löscht die Gruppe; das Objekt wird ungültig. |

Geerbt: alle Elemente von [`PrimitiveObject`](#primitiveobject).

### ParametricObject

> **Vollständiger Name:** `api.ParametricObject` · **Erbt von:** [`PrimitiveObject`](#primitiveobject) → `api.Object`

Allgemeines Plug-in-Objekt (parametrisches Objekt, `ObjectType.Parametric`) beliebiger Art, das durch ein Skript oder ein kompiliertes Plug-in definiert wird.

Verwenden Sie diese Klasse NUR, wenn für das Plug-in keine spezifische Klasse vorhanden ist. Die spezifischen Klassen (PlantObject, WindowObject, DataTagObject, ...) berücksichtigen die Bedeutung der Parameter, prüfen sie und halten das Objekt konsistent; diese Klasse liest und schreibt lediglich die unverarbeiteten parametrischen Datenbankfelder anhand ihrer universellen Namen.

Ermitteln Sie die Parameter eines Plug-ins mit GetParameterDefinitions(universalName) (keine Instanz erforderlich) oder mit `GetParameters()` an einer Instanz und die Platzierungsart seiner Objekte mit GetPluginKind(universalName). Verwenden Sie anschließend die typisierten Get/SetParam*-Zugriffsmethoden:

- Zeichenfolge — jeder Feldtyp als Text — GetParamString / SetParamString
- reell — Feldtypen Real, Dimension, CoordLocX/Y, Angle, Area, Volume — GetParamReal / SetParamReal
- bool — Feldtyp Boolean — GetParamBool / SetParamBool
- int — Feldtypen Integer, DimStdPopUp — GetParamInt / SetParamInt
- popUp — ein Textwert aus N Auswahlmöglichkeiten; Auswahlwerte aus GetParamChoices (GetDefinitionChoices ohne Instanz) GetParamString / SetParamString

Die typisierten Abfragemethoden geben `None` und die Änderungsmethoden `False` zurück, wenn das Objekt ungültig ist, der Parameter nicht vorhanden ist oder sein Typ nicht zur Zugriffsmethode passt. Längen werden in Welteinheiten angegeben; Angle-Felder enthalten die gespeicherten Werte in Grad. Rufen Sie nach Parameteränderungen `Reset()` auf, damit das Plug-in seine Geometrie neu erzeugt.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `ParametricObject(h: Handle)` | Verweist auf das vorhandene Plug-in-Objekt `h`; vor der Verwendung `IsValid()` prüfen. |

**Methoden**

*Allgemein*

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | Gibt `True` für jedes Plug-in-Objekt zurück. |
| `IsNamed(h: Handle, universalName: str) -> bool` *statisch* | Gibt `True` für ein Plug-in-Objekt des Plug-ins mit diesem universellen Namen zurück, z. B. „Door“. |
| `Create(universalName: str, location: Math.Point2D, angle: float = 0.0) -> ParametricObject` *statisch* | Erstellt ein punktbasiertes Plug-in-Objekt auf der aktiven Ebene bzw. im aktuellen Container. `angle` im Bogenmaß. |
| `CreateFromPath(universalName: str, hPath: Handle) -> ParametricObject` *statisch* | Erstellt ein pfadbasiertes Plug-in-Objekt, das `hPath` (eine 2D-Polygonform) als Pfad verwendet. |
| `Duplicate() -> ParametricObject` | Dupliziert das Plug-in-Objekt in der Zeichnung und gibt die Kopie zurück. |

*Plug-in-Definitionen (nach universellem Namen, keine Instanz erforderlich)*

| Methode | Beschreibung |
|---|---|
| `GetDefinitionFormat(universalName: str) -> RecordFormat` *statisch* | Parametrische Datenbank des Plug-ins; ungültig, wenn kein Plug-in mit diesem universellen Namen installiert ist. Fügt die Datenbank dem aktiven Dokument hinzu, falls sie dort noch nicht vorhanden ist. |
| `GetParameterDefinitions(universalName: str) -> list[RecordField]` *statisch* | Parameter des Plug-ins mit ihren universellen und lokalisierten Namen, Typen und Standardwerten in der Reihenfolge ihrer Deklaration. Leer, wenn kein Plug-in mit diesem universellen Namen installiert ist. |
| `GetDefinitionChoices(universalName: str, univParamName: str) -> list[str]` *statisch* | Universelle Auswahlwerte des PopUp-Parameters `univParamName` des Plug-ins, in derselben Reihenfolge, wie GetParamChoices sie für ein Objekt des Plug-ins zurückgibt. Leer bei unbekanntem Plug-in oder Parameter sowie bei einem Parameter, der kein PopUp ist. Fügt wie GetDefinitionFormat die Datenbank des Plug-ins dem aktiven Dokument hinzu, falls sie dort noch nicht vorhanden ist, und benennt sie genau nach dem angegebenen `universalName`: Übergeben Sie den exakten universellen Namen (siehe GetPluginKind). |
| `GetPluginKind(universalName: str) -> ParametricObject.PluginKind \| None` *statisch* | Art des Plug-in-Objekts mit genau diesem universellen Namen, aus der Vectorworks-Liste der installierten Plug-ins. Groß- und Kleinschreibung sind relevant: Vectorworks findet ein Plug-in unabhängig von der Schreibweise, benennt eine von ihm angelegte Datenbank jedoch nach dem angegebenen Namen. Deshalb wird nur der exakte universelle Name akzeptiert. Leer, wenn kein Plug-in-Objekt mit genau diesem Namen installiert ist (unbekannter Name, abweichende Groß- und Kleinschreibung oder ein Menübefehl bzw. Werkzeug). Ändert nichts im Dokument. |

*Universeller Name des Plug-ins, z. B. „Door“*

| Methode | Beschreibung |
|---|---|
| `GetParametricName() -> str \| None` | Gibt den universellen (parametrischen) Namen zurück. |
| `GetParameters() -> list[RecordField]` | Parameter des Plug-ins dieses Objekts, siehe GetParameterDefinitions. |
| `GetParamNames() -> list[str]` | Gibt die Parameternamen zurück. |
| `HasParam(univParamName: str) -> bool` | Gibt True zurück, wenn das Objekt den Parameter mit dem universellen Namen `univParamName` besitzt. |
| `GetParamType(univParamName: str) -> RecordFieldType \| None` | Gibt den Parametertyp für `univParamName` zurück. |
| `GetParamChoices(univParamName: str) -> list[str]` | Universelle Auswahlwerte eines PopUp-Parameters in ihrer Reihenfolge; bei anderen Parametern leer. |
| `GetParamString(univParamName: str) -> str \| None` | Gibt den Parameterwert für `univParamName` als Zeichenfolge zurück. |
| `SetParamString(univParamName: str, value: str) -> bool` | Legt den Parameterwert als Zeichenfolge fest. |
| `GetParamReal(univParamName: str) -> float \| None` | Gibt den Parameterwert vom Typ real für `univParamName` zurück. |
| `SetParamReal(univParamName: str, value: float) -> bool` | Setzt den Parameterwert vom Typ real. |
| `GetParamBool(univParamName: str) -> bool \| None` | Ob *Boolescher Parameter* für `univParamName` aktiviert ist. |
| `SetParamBool(univParamName: str, value: bool) -> bool` | Setzt den booleschen Parameterwert. |
| `GetParamInt(univParamName: str) -> int \| None` | Gibt den ganzzahligen Parameterwert für `univParamName` zurück. |
| `SetParamInt(univParamName: str, value: int) -> bool` | Setzt den ganzzahligen Parameterwert. |
| `GetPathObject() -> Handle` | Pfadobjekt eines pfadbasierten Plug-in-Objekts; bei punktbasierten Objekten ein Null-Handle. |

Geerbt: alle Elemente von [`PrimitiveObject`](#primitiveobject).

#### ParametricObject.PluginKind

> **Vollständiger Name:** `api.ParametricObject.PluginKind` · **Art:** `IntEnum`

Die Platzierungsart der Objekte eines Plug-ins: der vom Plug-in deklarierte Objektuntertyp.

| Element | Wert | Beschreibung |
|---|---|---|
| `Point` | `0` | Wird an einem Punkt mit einer Drehung eingefügt, z. B. eine Tür oder eine Pflanze (hybride, symbolartige Plug-ins). |
| `Linear` | `1` | Wird als Linie von einem Anfangspunkt zu einem Endpunkt gezeichnet. |
| `Rectangle` | `2` | Wird als Rechteck gezeichnet. |
| `Path2D` | `3` | Wird auf einem 2D-Pfad aufgebaut, den es übernimmt: CreateFromPath (Vectorworks wandelt den Pfad in eine Polylinie um). |
| `Path3D` | `4` | Wird auf einem 3D-Pfad aufgebaut, den es übernimmt: CreateFromPath (eine NURBS-Kurve, ein 3D-Polygon, ...) |
| `Custom` | `5` | Das Plug-in übernimmt das Einfügen selbst. |

### TextObject

> **Vollständiger Name:** `api.TextObject` · **Erbt von:** [`PrimitiveObject`](#primitiveobject) → `api.Object`

Textblock (`ObjectType.Text`): formatierter Text, der an einem Ursprungspunkt platziert wird. Zeichenindizes beginnen bei 0 und zählen UTF-16-Codeeinheiten (ein Zeichen außerhalb der mehrsprachigen Basisebene belegt zwei). Text wird als UTF-8 ausgetauscht; Zeilen werden durch „\r“ getrennt (siehe GetNewLine). Formatierungsänderungen wirken auf den Bereich [first, first + count); `count` wird auf das Textende begrenzt, sodass die Standardwerte (0, `kToEnd`) den gesamten Text formatieren. Größen werden in Welteinheiten angegeben, sofern der Name nicht „Points“ enthält.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `TextObject(h: Handle)` | Verweist auf den vorhandenen Text `h`; vor der Verwendung `IsValid()` prüfen. |

**Methoden**

*Allgemein*

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | True, wenn `h` auf ein Objekt des von dieser Klasse dargestellten Typs verweist. |
| `Create(text: str, origin: Math.Point2D, width: float = 0.0) -> TextObject` *statisch* | Erstellt einen Textblock auf der aktiven Ebene bzw. im aktuellen Container mit den Standardtextattributen des Dokuments. Bei `width` > 0 wird ein Textblock mit fester Breite und Zeilenumbruch erstellt. |
| `Duplicate() -> TextObject` | Dupliziert den Text in der Zeichnung und gibt die Kopie zurück. |
| `CreateUnlinkedCopy() -> TextObject` | Kopie des Texts, die die Formatierung beibehält, aber nicht mit einem Datenbankfeld verknüpft ist. |

*Inhalt*

| Methode | Beschreibung |
|---|---|
| `GetText() -> str \| None` | Gibt den Text zurück. |
| `SetText(text: str, clearFormatting: bool = False) -> bool` | Ersetzt den Text. Mit `clearFormatting` wird jedes Zeichen auf die Formatierung des ersten Zeichens zurückgesetzt. |
| `GetLength() -> int \| None` | Gibt die Länge zurück. |
| `InsertText(text: str, beforeIndex: int) -> bool` | Fügt vor dem Zeichen `beforeIndex` ein (mit `GetLength()` wird angehängt); der neue Text übernimmt die benachbarte Formatierung. |
| `AppendText(text: str) -> bool` | Hängt `text` am Textende an; der neue Text übernimmt die Formatierung des letzten Zeichens. |
| `DeleteText(first: int = 0, count: int = kToEnd) -> bool` | Löscht `count` Zeichen ab `first` (Standard: der gesamte Text). |
| `GetNewLine() -> str` *statisch* | Von Textobjekten verwendetes Zeilentrennzeichen: „\r“. |

*Platzierung*

| Methode | Beschreibung |
|---|---|
| `GetOrigin() -> Math.Point2D \| None` | Gibt den Ursprung zurück. |
| `SetOrigin(origin: Math.Point2D) -> bool` | Legt den Ursprung fest. |
| `GetAngle() -> float \| None` | Drehung im Bogenmaß (gegen den Uhrzeigersinn). |
| `IsFlipped() -> bool \| None` | Gibt True zurück, wenn der Text umgekehrt ist (vertikal gespiegelt). |
| `SetOrientation(angle: float, flipped: bool = False) -> bool` | Legt die Orientierung fest. |
| `GetBoxCorners() -> tuple[Math.Point2D * 4] \| None` | Ecken des möglicherweise gedrehten Textrahmens: oben links, oben rechts, unten rechts, unten links. |
| `GetCharIndexAt(point: Math.Point2D) -> int \| None` | Index des Zeichens mit dem geringsten Abstand zu `point`. |

*Textanordnung*

| Methode | Beschreibung |
|---|---|
| `GetHorizontalAlignment() -> TextObject.HorizontalAlignment \| None` | Gibt die horizontale Ausrichtung zurück. |
| `SetHorizontalAlignment(alignment: TextObject.HorizontalAlignment) -> bool` | Legt die horizontale Ausrichtung fest. |
| `GetVerticalAlignment() -> TextObject.VerticalAlignment \| None` | Gibt die vertikale Ausrichtung zurück. |
| `SetVerticalAlignment(alignment: TextObject.VerticalAlignment) -> bool` | Setzt die vertikale Ausrichtung. |
| `GetSpacing() -> TextObject.Spacing \| None` | Gibt den Zeilenabstand zurück. |
| `GetLeading() -> float \| None` | Benutzerdefinierter Zeilenabstand in Welteinheiten; relevant, wenn `GetSpacing()` den Wert `TextObject.Spacing.Custom` hat. |
| `SetSpacing(spacing: TextObject.Spacing, leading: float = 0.0) -> bool` | `leading` wird nur mit `TextObject.Spacing.Custom` verwendet. |
| `GetWidth() -> float \| None` | Breite des Textrahmens in Welteinheiten. |
| `SetWidth(width: float) -> bool` | Legt die Umbruchbreite fest; sie gilt, wenn `IsWrapped()` den Wert `True` hat. |
| `IsWrapped() -> bool \| None` | Text mit fester Breite, dessen Zeilen bei `GetWidth()` umgebrochen werden. |
| `SetWrapped(wrapped: bool) -> bool` | Schaltet *Zeilenumbruch* ein oder aus (Text mit fester Breite, dessen Zeilen bei `GetWidth()` umgebrochen werden). |
| `GetLineHeight(charIndex: int = 0) -> float \| None` | Höhe der Zeile, die das Zeichen `charIndex` enthält, in Welteinheiten. |
| `GetLineCount() -> int \| None` | Zeilen nach dem Zeilenumbruch. |
| `GetLineStarts() -> list[int]` | Gibt die Zeilenanfänge zurück (Index des ersten Zeichens jeder Zeile). |
| `GetLines() -> list[str]` | Gibt die Zeilen zurück (Zeilentexte ohne Trennzeichen). |
| `GetCharWidths() -> list[float]` | Vorschubbreite jedes Zeichens in Welteinheiten. |

*Zeichenformatierung bei `charIndex`*

| Methode | Beschreibung |
|---|---|
| `GetFont(charIndex: int = 0) -> str \| None` | Gibt die Schriftart bei `charIndex` zurück. |
| `GetFontIndex(charIndex: int = 0) -> int \| None` | Gibt den Schriftartindex bei `charIndex` zurück. |
| `GetSize(charIndex: int = 0) -> float \| None` | Gibt die Schriftgröße bei `charIndex` zurück. |
| `GetSizePoints(charIndex: int = 0) -> float \| None` | Gibt die Schriftgröße in Punkten bei `charIndex` zurück. |
| `GetStyle(charIndex: int = 0) -> int \| None` | Gibt den Stil bei `charIndex` zurück. |
| `GetCustomStyle(charIndex: int = 0) -> int \| None` | Gibt den benutzerdefinierten Stil bei `charIndex` zurück. |
| `GetColor(charIndex: int = 0) -> ColorRGB \| None` | Gibt die Farbe bei `charIndex` zurück. |
| `GetColorIndex(charIndex: int = 0) -> int \| None` | Gibt den Farbindex bei `charIndex` zurück. |

*Zeichenabstandsfaktor*

| Methode | Beschreibung |
|---|---|
| `GetTracking(charIndex: int = 0) -> float \| None` | 1 = normaler Zeichenabstand, 0.1 .. 10. |
| `GetStyleRuns() -> list[TextObject.StyleRun]` | Die gleich formatierten Abschnitte des gesamten Texts in ihrer Reihenfolge. |
| `SetFont(fontName: str, first: int = 0, count: int = kToEnd) -> bool` | Zeichenformatierung eines Bereichs (schlägt bei einem leeren Bereich oder einer unbekannten Schriftart fehl). |
| `SetFontIndex(fontIndex: int, first: int = 0, count: int = kToEnd) -> bool` | Legt den Schriftartindex auf `fontIndex` fest. |
| `SetSize(size: float, first: int = 0, count: int = kToEnd) -> bool` | Setzt die Größe. |
| `SetSizePoints(points: float, first: int = 0, count: int = kToEnd) -> bool` | Legt die Schriftgröße in Punkten fest. |
| `SetStyle(style: int, first: int = 0, count: int = kToEnd) -> bool` | Ersetzt die Stilkennzeichen des Bereichs (`kStylePlain` löscht sie). |
| `SetCustomStyle(customStyle: int, first: int = 0, count: int = kToEnd) -> bool` | Legt den benutzerdefinierten Stil fest. |
| `SetColor(color: ColorRGB, first: int = 0, count: int = kToEnd) -> bool` | Legt die Farbe fest. |
| `SetColorIndex(color: int, first: int = 0, count: int = kToEnd) -> bool` | Legt den Farbindex fest. |
| `SetTracking(tracking: float, first: int = 0, count: int = kToEnd) -> bool` | `tracking` muss im Bereich 0.1 .. 10 liegen. |
| `GetTextStyleRef() -> int \| None` | Textstile (siehe TextStyle). 0 = kein Textstil. |
| `GetTextStyleRefAt(charIndex: int) -> int \| None` | Gibt die Textstilreferenz bei `charIndex` zurück. |
| `SetTextStyleRef(textStyle: int, first: int = 0, count: int = kToEnd) -> bool` | Legt die Textstilreferenz fest. Textstile (siehe TextStyle). 0 = kein Textstil. |
| `IsTextStyleByClass() -> bool \| None` | Gibt True zurück, wenn der Text seinen Textstil von seiner Klasse übernimmt. |
| `IsTextStyleByClassAt(charIndex: int) -> bool \| None` | Gibt True zurück, wenn das Zeichen `charIndex` seinen Textstil von der Klasse übernimmt. |
| `SetTextStyleByClass(first: int = 0, count: int = kToEnd) -> bool` | Lässt den Bereich den Textstil der Objektklasse übernehmen. |
| `UpdateTextStyleSize() -> bool` | Skaliert die Textstilgrößen neu, nachdem das Objekt auf eine Ebene mit einem anderen Maßstab verschoben wurde. |
| `GetTabStops() -> list[TextObject.TabStop]` | Tabulatorstopps (ab 0 indiziert, nach Abstand sortiert). |
| `GetTabStopCount() -> int \| None` | Anzahl der Tabulatorstopps. |
| `AddTabStop(offset: float) -> bool` | Fügt einen linksbündigen Tabulatorstopp bei `offset` hinzu. |
| `MoveTabStop(index: int, offset: float) -> bool` | Verschiebt den Tabulatorstopp `index` zu `offset` (Abstand vom linken Textrand in Welteinheiten). |
| `RemoveTabStop(index: int) -> bool` | Vectorworks behält den ersten Tabulatorstopp bei: Index 0 kann nicht entfernt werden. |
| `GetRepeatingTabStop() -> float \| None` | Abstand zwischen den wiederholten Tabulatorstopps in Welteinheiten (0 = keine). |
| `SetRepeatingTabStop(interval: float) -> bool` | Legt den wiederholten Tabulatorstopp fest (Abstand zwischen den wiederholten Tabulatorstopps in Welteinheiten; 0 = keine). |

*Kennzeichen*

| Methode | Beschreibung |
|---|---|
| `HasTightFill() -> bool \| None` | Die Füllung bedeckt nur die Textbegrenzungen statt des gesamten Textrahmens. |
| `SetTightFill(tightFill: bool) -> bool` | Schaltet *Enge Füllung* ein oder aus (die Füllung bedeckt nur die Textbegrenzungen statt des gesamten Textrahmens). |
| `IsLinkedToRecord() -> bool \| None` | Mit einem Datenbankfeld eines Symbols verknüpfter Text. |
| `UnlinkFromRecord() -> bool` | Löst die Verknüpfung des Texts mit dem Datenbankfeld seines Symbols; er wird zu normalem Text. |
| `IsNoteText() -> bool \| None` | Gibt True zurück, wenn der Text die Anmerkung einer Bemaßung ist. |
| `IsSIAElevationText() -> bool \| None` | Gibt True zurück, wenn der Text eine SIA-Höhenbeschriftung ist. |
| `IsRightToLeft() -> bool \| None` | Gibt True zurück, wenn der Text von rechts nach links verläuft. |
| `FormatAsSIA(centimeters: str, millimeters: str, superscriptPercent: float = 100.0) -> bool` | SIA-Formatierung (Schweizer Schreibweise: Zentimeter mit hochgestellten Millimetern). |
| `FormatValueAsSIA(value: float, alwaysMeters: bool, superscriptPercent: float = 100.0) -> bool` | Formatiert `value` (Welteinheiten) als SIA-Text; `alwaysMeters` erzwingt Meter. |
| `FormatSegmentAsSIA(first: int, count: int, superscriptPercent: float = 100.0) -> bool` | Formatiert die `count` Zeichen ab `first` in SIA-Schreibweise (Zentimeter mit hochgestellten Millimetern). |

*Schriftarten*

| Methode | Beschreibung |
|---|---|
| `FontIndexFromName(fontName: str) -> int \| None` *statisch* | Schriftartindex der Schriftart mit dem Namen `fontName`. |
| `FontNameFromIndex(fontIndex: int) -> str \| None` *statisch* | Name der Schriftart mit dem Index `fontIndex`. |
| `PointsToWorld(points: float) -> float` *statisch* | Wandelt eine Größe in Seitenpunkten in eine Länge in Welteinheiten um. |
| `WorldToPoints(length: float) -> float` *statisch* | Wandelt eine Länge in Welteinheiten in eine Größe in Seitenpunkten um. |

**Konstanten**

| Konstante | Typ | Wert | Beschreibung |
|---|---|---|---|
| `TextObject.kStylePlain` | `int` | `0` | Zeichenstilkennzeichen (GetStyle / SetStyle), kombinierbar mit '\|'. Kontur und Schatten werden nur unter macOS angezeigt. |
| `TextObject.kStyleBold` | `int` | `1` | Zeichenstilkennzeichen (GetStyle / SetStyle), kombinierbar mit '\|'. Kontur und Schatten werden nur unter macOS angezeigt. |
| `TextObject.kStyleItalic` | `int` | `2` | Zeichenstilkennzeichen (GetStyle / SetStyle), kombinierbar mit '\|'. Kontur und Schatten werden nur unter macOS angezeigt. |
| `TextObject.kStyleUnderline` | `int` | `4` | Zeichenstilkennzeichen (GetStyle / SetStyle), kombinierbar mit '\|'. Kontur und Schatten werden nur unter macOS angezeigt. |
| `TextObject.kStyleOutline` | `int` | `8` | Zeichenstilkennzeichen (GetStyle / SetStyle), kombinierbar mit '\|'. Kontur und Schatten werden nur unter macOS angezeigt. |
| `TextObject.kStyleShadow` | `int` | `16` | Zeichenstilkennzeichen (GetStyle / SetStyle), kombinierbar mit '\|'. Kontur und Schatten werden nur unter macOS angezeigt. |
| `TextObject.kCustomStyleNone` | `int` | `0` | Benutzerdefinierte Stilkennzeichen (GetCustomStyle / SetCustomStyle). |
| `TextObject.kCustomDiagonalFraction` | `int` | `1` | Benutzerdefinierte Stilkennzeichen (GetCustomStyle / SetCustomStyle). |
| `TextObject.kCustomVerticalFraction` | `int` | `2` | Benutzerdefinierte Stilkennzeichen (GetCustomStyle / SetCustomStyle). |
| `TextObject.kCustomSuperscript` | `int` | `32` | Benutzerdefinierte Stilkennzeichen (GetCustomStyle / SetCustomStyle). |
| `TextObject.kCustomSubscript` | `int` | `64` | Benutzerdefinierte Stilkennzeichen (GetCustomStyle / SetCustomStyle). |
| `TextObject.kToEnd` | `int` | `2**64 - 1` | Bereichslänge mit der Bedeutung „bis zum Textende“. |

Geerbt: alle Elemente von [`PrimitiveObject`](#primitiveobject).

#### TextObject.StyleRun

> **Vollständiger Name:** `api.TextObject.StyleRun` · **Erbt von:** `api.Object`

Eine Zeichenfolge mit einheitlicher Formatierung

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `StyleRun()` | Standardwert (Felder mit ihren Standardwerten). |
| `StyleRun(start, length, font, fontIndex, size, sizePoints, style, customStyle, color, textStyle, tracking)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `start` | `int` | Index des ersten Zeichens der Zeichenfolge. |
| `length` | `int` | Anzahl der Zeichen in der Zeichenfolge. |
| `font` | `str` | Schriftartname. |
| `fontIndex` | `int` | Schriftartindex. |
| `size` | `float` | Welteinheiten. |
| `sizePoints` | `float` | Seitenpunkte. |
| `style` | `int` | `TextObject.kStyle...`-Kennzeichen. |
| `customStyle` | `int` | `TextObject.kCustom...`-Kennzeichen. |
| `color` | `ColorRGB` | Textfarbe (Farbindex). |
| `textStyle` | `int` | Textstil; 0 = keiner. |
| `tracking` | `float` | Zeichenabstandsfaktor, 1 = normal. |

#### TextObject.TabStop

> **Vollständiger Name:** `api.TextObject.TabStop` · **Erbt von:** `api.Object`

Tabulatorstopp: Abstand vom linken Textrand in Welteinheiten sowie Ausrichtung.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `TabStop()` | Standardwert (Felder mit ihren Standardwerten). |
| `TabStop(offset, alignment)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `offset` | `float` | Abstand vom linken Textrand in Welteinheiten. |
| `alignment` | `TextObject.TabAlignment` | Ausrichtung des Texts am Tabulatorstopp. |

#### TextObject.HorizontalAlignment

> **Vollständiger Name:** `api.TextObject.HorizontalAlignment` · **Art:** `IntEnum`

Horizontale Ausrichtung eines Textblocks.

| Element | Wert | Beschreibung |
|---|---|---|
| `Left` | `1` |  |
| `Center` | `2` |  |
| `Right` | `3` |  |
| `Justify` | `4` |  |

#### TextObject.VerticalAlignment

> **Vollständiger Name:** `api.TextObject.VerticalAlignment` · **Art:** `IntEnum`

Vertikale Ausrichtung eines Textblocks relativ zu seinem Ursprung.

| Element | Wert | Beschreibung |
|---|---|---|
| `TopBox` | `1` | Oberkante des Textrahmens. |
| `TopBaseline` | `2` | Grundlinie der ersten Zeile. |
| `CenterBox` | `3` |  |
| `BottomBaseline` | `4` | Grundlinie der letzten Zeile. |
| `BottomBox` | `5` |  |

#### TextObject.Spacing

> **Vollständiger Name:** `api.TextObject.Spacing` · **Art:** `IntEnum`

Zeilenabstand eines Textblocks; `Custom` verwendet den an `SetSpacing` übergebenen Zeilenabstand.

| Element | Wert | Beschreibung |
|---|---|---|
| `Custom` | `0` | Benutzerdefinierter Zeilenabstand, siehe GetLeading. |
| `Single` | `2` |  |
| `OneAndHalf` | `3` |  |
| `Double` | `4` |  |

#### TextObject.TabAlignment

> **Vollständiger Name:** `api.TextObject.TabAlignment` · **Art:** `IntEnum`

Ausrichtung des Texts an einem Tabulatorstopp.

| Element | Wert | Beschreibung |
|---|---|---|
| `Left` | `1` |  |
| `Right` | `2` |  |
| `Center` | `3` |  |
| `Decimal` | `4` |  |

---

[Zurück zum Index](README.md) · [Nach oben](#objectprimitives--2d-grundobjekte)

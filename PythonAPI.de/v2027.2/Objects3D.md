[English](../../PythonAPI/v2027.2/Objects3D.md) • **Deutsch** • [日本語](../../PythonAPI.ja/v2027.2/Objects3D.md)

# Objects3D — 3D-Objekte

> **Python-Modul:** `api` · **Version:** Vectorworks 2027 Update 2

[Zurück zum Index](README.md)

Die 3D-Objektklassen: Extrusionskörper, Schichtkörper und Rotationskörper, Vollkörper (mit den Befehlen Volumen zusammenfügen, Schnittvolumen löschen und Schnittvolumen anlegen erzeugte Vollkörper, die ihre Bearbeitungshistorie behalten, sowie einfache Vollkörper ohne Bearbeitungshistorie), Grundkörper (Kugeln, Halbkugeln, Kegel, ...), NURBS-Kurven und -Flächen, 3D-Polygone, Punktkörper, Hohlkörper und Oberflächenmodelle. Alle leiten sich von [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) ab; die gemeinsamen Objektoperationen (Name, Klasse, Ebene, Attribute, Begrenzungen, Verschieben, Löschen, ...) sind daher dort dokumentiert.

Koordinaten werden in Welteinheiten im 3D-Modellraum angegeben, Winkel im Bogenmaß.

## Inhaltsverzeichnis

- [Überblick](#überblick)
- [Klassen](#klassen)
  - [ExtrudeObject](#extrudeobject)
    - [ExtrudeObject.Values](#extrudeobjectvalues)
    - [ExtrudeObject.Transform](#extrudeobjecttransform)
  - [SweepObject](#sweepobject)
    - [SweepObject.Values](#sweepobjectvalues)
  - [MultiExtrudeObject](#multiextrudeobject)
  - [SurfaceModelObject](#surfacemodelobject)
    - [SurfaceModelObject.PathOptions](#surfacemodelobjectpathoptions)
  - [GenericSolidObject](#genericsolidobject)
    - [GenericSolidObject.HistoryStep](#genericsolidobjecthistorystep)
    - [GenericSolidObject.Operation](#genericsolidobjectoperation)
  - [ShellObject](#shellobject)
  - [Polygon3DObject](#polygon3dobject)
    - [Polygon3DObject.Plane](#polygon3dobjectplane)
    - [Polygon3DObject.ClosestPoint](#polygon3dobjectclosestpoint)
  - [MeshObject](#meshobject)
    - [MeshObject.Face](#meshobjectface)
    - [MeshObject.Part](#meshobjectpart)
    - [MeshObject.Smoothing](#meshobjectsmoothing)
  - [SolidPrimitiveObject](#solidprimitiveobject)
    - [SolidPrimitiveObject.Kind](#solidprimitiveobjectkind)
  - [SphereObject](#sphereobject)
  - [HemisphereObject](#hemisphereobject)
  - [ConeObject](#coneobject)
    - [ConeObject.Radii](#coneobjectradii)
  - [NurbsCurveObject](#nurbscurveobject)
    - [NurbsCurveObject.Location](#nurbscurveobjectlocation)
  - [NurbsSurfaceObject](#nurbssurfaceobject)

## Überblick

| Name | Art | Erbt von | Zusammenfassung |
|---|---|---|---|
| [`ExtrudeObject`](#extrudeobject) | Klasse | [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) | Vectorworks-eigener Extrusionskörper (kein Plug-in-Objekt). |
| [`ExtrudeObject.Values`](#extrudeobjectvalues) | Klasse (verschachtelt) |  | Lokale Basishöhe und vorzeichenbehaftete Dicke in Welteinheiten. |
| [`ExtrudeObject.Transform`](#extrudeobjecttransform) | Klasse (verschachtelt) |  | Orthonormale lokale Achsen und Ursprung im übergeordneten Koordinatensystem (standardmäßig die Identitätstransformation). |
| [`SweepObject`](#sweepobject) | Klasse | [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) | Vectorworks-eigener Rotationskörper. |
| [`SweepObject.Values`](#sweepobjectvalues) | Klasse (verschachtelt) |  | Rotationswinkel im Bogenmaß und Steigung in Welteinheiten pro voller Umdrehung. |
| [`MultiExtrudeObject`](#multiextrudeobject) | Klasse | [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) | Vectorworks-eigener Schichtkörper. |
| [`SurfaceModelObject`](#surfacemodelobject) | Klasse | [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) | Ein Modellierungsergebnis ist eine NURBS-Fläche, ein CSG-Vollkörper oder eine Gruppe von Modellierungsergebnissen. |
| [`SurfaceModelObject.PathOptions`](#surfacemodelobjectpathoptions) | Klasse (verschachtelt) |  | Optionen für Skalierung und Profilplatzierung eines Pfadkörpers (Extrusion entlang eines Pfads). |
| [`GenericSolidObject`](#genericsolidobject) | Klasse | [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) | Umfasst Vectorworks-eigene Vollkörper, einschließlich der mit den Befehlen Volumen zusammenfügen, Schnittvolumen löschen und Schnittvolumen anlegen erzeugten Vollkörper und einfacher Vollkörper ohne Bearbeitungshistorie. |
| [`GenericSolidObject.HistoryStep`](#genericsolidobjecthistorystep) | Klasse (verschachtelt) |  | Ein Knoten im Vectorworks-eigenen Konstruktionsbaum, in Präorder-Reihenfolge. |
| [`GenericSolidObject.Operation`](#genericsolidobjectoperation) | IntEnum (verschachtelt) |  | Boolesche Vollkörperoperation. |
| [`ShellObject`](#shellobject) | Klasse | [`GenericSolidObject`](#genericsolidobject) | Hohlkörper: ein CSG-Versatzknoten (Werkzeug Hohlkörper, VectorScript CreateShell). |
| [`Polygon3DObject`](#polygon3dobject) | Klasse | [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) | Vectorworks-eigenes 3D-Polygon (`ObjectType.Polygon3D`). |
| [`Polygon3DObject.Plane`](#polygon3dobjectplane) | Klasse (verschachtelt) |  | Ebene durch den Schwerpunkt der Scheitelpunkte; die Normale ist ein Einheitsvektor gemäß der Scheitelpunktreihenfolge (Rechte-Hand-Regel), und d erfüllt die Bedingung normal . |
| [`Polygon3DObject.ClosestPoint`](#polygon3dobjectclosestpoint) | Klasse (verschachtelt) |  | Nächstgelegener Punkt auf dem Polygonpfad, sein Abstand, der Kantenindex und die Pfadlänge ab dem ersten Scheitelpunkt. |
| [`MeshObject`](#meshobject) | Klasse | [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) | Vectorworks-eigener Punktkörper (`ObjectType.Mesh`): eine gemeinsame Scheitelpunktliste und polygonale Flächen, die über Indizes darauf verweisen. |
| [`MeshObject.Face`](#meshobjectface) | Klasse (verschachtelt) |  | Teil 0 bezeichnet den gesamten, nicht texturierten Teil, siehe `GetOverallPart()`. |
| [`MeshObject.Part`](#meshobjectpart) | Klasse (verschachtelt) |  | Texturteil: ID, Texturreferenz (0 = nicht texturiert) und Anzahl der Flächen, die ihn verwenden. |
| [`MeshObject.Smoothing`](#meshobjectsmoothing) | IntEnum (verschachtelt) |  | Art der Glättung des Punktkörpers beim Rendern. |
| [`SolidPrimitiveObject`](#solidprimitiveobject) | Klasse | [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) | Gemeinsame Basisklasse der Vectorworks-eigenen parametrischen Grundkörper (`ObjectType.Solid`): Kugeln, Halbkugeln und Kegel. |
| [`SolidPrimitiveObject.Kind`](#solidprimitiveobjectkind) | IntEnum (verschachtelt) |  | Art eines Grundkörpers. |
| [`SphereObject`](#sphereobject) | Klasse | [`SolidPrimitiveObject`](#solidprimitiveobject) | Vectorworks-eigene Kugel: Mittelpunkt und I-/J-/K-Radien (ungleiche Radien ergeben ein Ellipsoid); leichtgewichtige Sicht auf das Zeichnungsobjekt. |
| [`HemisphereObject`](#hemisphereobject) | Klasse | [`SphereObject`](#sphereobject) | Vectorworks-eigene Halbkugel: Mittelpunkt, Radien und eine Kuppel in Richtung der lokalen K-Achse; leichtgewichtige Sicht auf das Zeichnungsobjekt. |
| [`ConeObject`](#coneobject) | Klasse | [`SolidPrimitiveObject`](#solidprimitiveobject) | Vectorworks-eigener Kegel. |
| [`ConeObject.Radii`](#coneobjectradii) | Klasse (verschachtelt) |  | Grundflächenradien entlang der lokalen I- und J-Achsen. |
| [`NurbsCurveObject`](#nurbscurveobject) | Klasse | [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) | Vectorworks-eigene abschnittsweise definierte NURBS-Kurve. |
| [`NurbsCurveObject.Location`](#nurbscurveobjectlocation) | Klasse (verschachtelt) |  | Kurvenpunkt und kurveneigener Parameter auf einem ab 0 indizierten Abschnitt; die Parameter sind keine Bogenlängen. |
| [`NurbsSurfaceObject`](#nurbssurfaceobject) | Klasse | [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) | Vectorworks-eigene NURBS-Fläche. |

## Klassen

### ExtrudeObject

> **Vollständiger Name:** `api.ExtrudeObject` · **Erbt von:** [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Vectorworks-eigener Extrusionskörper (kein Plug-in-Objekt). Abmessungen und Profilkoordinaten sind lokal zur Objektmatrix; Längen werden in Welteinheiten angegeben. Der Zugriff auf einen vorhandenen Extrusionskörper über diese Klasse verändert ihn nicht.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `ExtrudeObject(h: Handle)` | Verweist auf den vorhandenen Extrusionskörper `h`; vor der Verwendung `IsValid()` prüfen. |

**Methoden**

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | True, wenn `h` auf ein Objekt des von dieser Klasse dargestellten Typs verweist. |
| `Create(hProfile: Handle, baseElevation: float, thickness: float, keepOriginal: bool = False) -> ExtrudeObject` *statisch* | Ein über einen Handle angegebenes Profil muss eine Vectorworks-eigene 2D-Form sein. Bei Erfolg wird es in den Extrusionskörper verschoben, außer wenn keepOriginal den Wert `True` hat (dann wird eine Kopie verwendet). Bei einem Fehlschlag bleibt das Original unverändert. |
| `Create(profile: Math.Polygon2D, thickness: float) -> ExtrudeObject` *statisch* | Ein über einen Handle angegebenes Profil muss eine Vectorworks-eigene 2D-Form sein. Bei Erfolg wird es in den Extrusionskörper verschoben, außer wenn keepOriginal den Wert `True` hat (dann wird eine Kopie verwendet). Bei einem Fehlschlag bleibt das Original unverändert. |
| `Create(profile: Math.Polygon2D, baseElevation: float, thickness: float) -> ExtrudeObject` *statisch* | Ein über einen Handle angegebenes Profil muss eine Vectorworks-eigene 2D-Form sein. Bei Erfolg wird es in den Extrusionskörper verschoben, außer wenn keepOriginal den Wert `True` hat (dann wird eine Kopie verwendet). Bei einem Fehlschlag bleibt das Original unverändert. |
| `Create(points: list[Math.Point2D], baseElevation: float, thickness: float, closed: bool = True) -> ExtrudeObject` *statisch* | Ein über einen Handle angegebenes Profil muss eine Vectorworks-eigene 2D-Form sein. Bei Erfolg wird es in den Extrusionskörper verschoben, außer wenn keepOriginal den Wert `True` hat (dann wird eine Kopie verwendet). Bei einem Fehlschlag bleibt das Original unverändert. |
| `Create(rect: Math.Rect2D, baseElevation: float, thickness: float) -> ExtrudeObject` *statisch* | Ein über einen Handle angegebenes Profil muss eine Vectorworks-eigene 2D-Form sein. Bei Erfolg wird es in den Extrusionskörper verschoben, außer wenn keepOriginal den Wert `True` hat (dann wird eine Kopie verwendet). Bei einem Fehlschlag bleibt das Original unverändert. |
| `CreatePlanar(points: list[Point3D], thickness: float) -> ExtrudeObject` *statisch* | Eine geschlossene, ebene 3D-Begrenzung; ihre Ebene bestimmt die Platzierung. |
| `CreateBetween(hProfile: Handle, start: Point3D, end: Point3D, keepOriginal: bool = False) -> ExtrudeObject` *statisch* | Die lokale Z-Achse folgt start -> end. Der optionale Aufwärtsvektor definiert die lokale +Y-Richtung (auf die Profilebene projiziert); er darf nicht parallel zur Extrusionsrichtung sein. |
| `CreateBetween(hProfile: Handle, start: Point3D, end: Point3D, up: Point3D, keepOriginal: bool = False) -> ExtrudeObject` *statisch* | Die lokale Z-Achse folgt start -> end. Der optionale Aufwärtsvektor definiert die lokale +Y-Richtung (auf die Profilebene projiziert); er darf nicht parallel zur Extrusionsrichtung sein. |
| `Duplicate() -> ExtrudeObject` | Dupliziert den Extrusionskörper in der Zeichnung und gibt die Kopie zurück. |
| `GetExtrudeValues() -> ExtrudeObject.Values \| None` | Gibt die Extrusionswerte zurück. |
| `SetExtrudeValues(baseElevation: float, thickness: float) -> bool` | Legt die Extrusionswerte fest. |
| `SetExtrudeValues(values: ExtrudeObject.Values) -> bool` | Legt die Extrusionswerte fest. |
| `GetBaseElevation() -> float \| None` | Gibt die Basishöhe zurück. |
| `SetBaseElevation(baseElevation: float) -> bool` | Legt die Basishöhe fest (die Dicke bleibt erhalten). |
| `GetThickness() -> float \| None` | Gibt die Dicke zurück. |
| `SetThickness(thickness: float) -> bool` | Legt die Dicke fest (die Basishöhe bleibt erhalten). |
| `GetTopElevation() -> float \| None` | Gibt die Oberkantenhöhe zurück. |
| `SetTopElevation(topElevation: float) -> bool` | Legt die Oberkantenhöhe fest (die Basishöhe bleibt erhalten). |
| `GetBaseObject() -> Handle` | Handles, die lediglich auf Profile bzw. Löcher verweisen. Änderungen über diese Handles erfordern `Reset()`. |
| `SetBaseObject(hProfile: Handle, keepOriginal: bool = False) -> bool` | Legt das Basisobjekt fest. Handles, die lediglich auf Profile bzw. Löcher verweisen. Änderungen über diese Handles erfordern `Reset()`. |
| `GetBasePolygon() -> Math.Polygon2D \| None` | Gibt das Basispolygon zurück. |
| `SetBasePolygon(profile: Math.Polygon2D) -> bool` | Legt das Basispolygon fest (ersetzt Profil UND Löcher). |
| `GetHoleObjects() -> list[Handle]` | Gibt die Lochobjekte zurück. |
| `GetHoleCount() -> int` | Anzahl der Aussparungen. |
| `GetHoleObject(index: int) -> Handle` | Gibt das Lochobjekt am Index `index` zurück. |
| `AddHoleObject(hProfile: Handle, keepOriginal: bool = False) -> bool` | Fügt das 2D-Objekt `hProfile` als Loch des Profils hinzu (bei `keepOriginal` eine Kopie davon). Handles, die lediglich auf Profile bzw. Löcher verweisen. Änderungen über diese Handles erfordern `Reset()`. |
| `AddHoleObject(profile: Math.Polygon2D) -> bool` | Fügt ein Loch mit der Form `profile` hinzu. Handles, die lediglich auf Profile bzw. Löcher verweisen. Änderungen über diese Handles erfordern `Reset()`. |
| `RemoveHole(index: int) -> bool` | Entfernt das Loch am Index `index`. Handles, die lediglich auf Profile bzw. Löcher verweisen. Änderungen über diese Handles erfordern `Reset()`. |
| `RemoveAllHoles() -> bool` | Entfernt alle Löcher. Handles, die lediglich auf Profile bzw. Löcher verweisen. Änderungen über diese Handles erfordern `Reset()`. |
| `GetTransform() -> ExtrudeObject.Transform \| None` | Gibt die Transformation zurück. |
| `SetTransform(transform: ExtrudeObject.Transform) -> bool` | Legt die Transformation fest (weist nicht orthonormale Achsen zurück). |
| `Move3D(offset: Point3D) -> bool` | Verschiebt den Extrusionskörper um `offset` im 3D-Raum. |
| `GetVolume() -> float \| None` | Gibt das Volumen zurück (in kubischen Welteinheiten). |

Geerbt: alle Elemente von [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

#### ExtrudeObject.Values

> **Vollständiger Name:** `api.ExtrudeObject.Values` · **Erbt von:** `api.Object`

Lokale Basishöhe und vorzeichenbehaftete Dicke in Welteinheiten.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `Values()` | Standardwert (Felder mit ihren Standardwerten). |
| `Values(baseElevation, thickness)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `baseElevation` | `float` | Höhe der Unterkante des Extrusionskörpers. |
| `thickness` | `float` | Höhe des Extrusionskörpers. |

#### ExtrudeObject.Transform

> **Vollständiger Name:** `api.ExtrudeObject.Transform` · **Erbt von:** `api.Object`

Orthonormale lokale Achsen und Ursprung im übergeordneten Koordinatensystem (standardmäßig die Identitätstransformation).

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `Transform()` | Standardwert (Felder mit ihren Standardwerten). |
| `Transform(origin, uAxis, vAxis, wAxis)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `origin` | `Point3D` | Ursprung des lokalen Koordinatensystems. |
| `uAxis` | `Point3D` | Lokale X-Achse. |
| `vAxis` | `Point3D` | Lokale Y-Achse. |
| `wAxis` | `Point3D` | Lokale Z-Achse (Extrusionsrichtung). |

### SweepObject

> **Vollständiger Name:** `api.SweepObject` · **Erbt von:** [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Vectorworks-eigener Rotationskörper. Die X-Richtung des Profils ist radial, die Y-Richtung axial; die Rotationsachse ist die lokale Y-Achse. Beim Winkel null zeigt die radiale Richtung nach lokal +Z; positive Winkel drehen in Richtung lokal +X. Winkel werden im Bogenmaß angegeben, die Steigung in Welteinheiten pro voller Umdrehung. Eingabeobjekte werden immer kopiert.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `SweepObject(h: Handle)` | Verweist auf den vorhandenen Rotationskörper `h`; vor der Verwendung `IsValid()` prüfen. |

**Methoden**

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | True, wenn `h` auf ein Objekt des von dieser Klasse dargestellten Typs verweist. |
| `Create(profile: Handle) -> SweepObject` *statisch* | Erstellt einen Rotationskörper aus dem 2D-Objekt `profile` mit den Standardrotationswerten. |
| `Create(profile: Handle, values: SweepObject.Values) -> SweepObject` *statisch* | Erstellt einen Rotationskörper aus dem 2D-Objekt `profile` mit den Rotationswerten `values`. |
| `Create(profiles: list[Handle], values: SweepObject.Values) -> SweepObject` *statisch* | Ein optionaler 2D-Punkt legt die Achse fest; andernfalls verwendet Vectorworks die linke Kante der Profile. |
| `AreValidValues(values: SweepObject.Values) -> bool` *statisch* | Gibt True zurück, wenn `values` gültige Rotationswerte für `Create` sind. |
| `Duplicate() -> SweepObject` | Dupliziert den Rotationskörper in der Zeichnung und gibt die Kopie zurück. |
| `GetSweepValues() -> SweepObject.Values \| None` | Gibt die Rotationswerte zurück. |
| `SetSweepValues(values: SweepObject.Values) -> bool` | Legt die Rotationswerte fest. |
| `GetProfiles() -> list[Handle]` | Gibt die Profile zurück. |

Geerbt: alle Elemente von [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

#### SweepObject.Values

> **Vollständiger Name:** `api.SweepObject.Values` · **Erbt von:** `api.Object`

Rotationswinkel im Bogenmaß und Steigung in Welteinheiten pro voller Umdrehung.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `Values()` | Standardwert (Felder mit ihren Standardwerten). |
| `Values(startAngle, sweepAngle, incrementAngle, pitch)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `startAngle` | `float` | Anfangswinkel des Rotationskörpers (im Bogenmaß). |
| `sweepAngle` | `float` | Überstrichener Winkel (im Bogenmaß, standardmäßig eine volle Umdrehung; das Vorzeichen bestimmt die Richtung). |
| `incrementAngle` | `float` | Positiver Betrag; das Vorzeichen von sweepAngle bestimmt die Richtung. |
| `pitch` | `float` | Positiver Betrag; das Vorzeichen von sweepAngle bestimmt die Richtung. |

### MultiExtrudeObject

> **Vollständiger Name:** `api.MultiExtrudeObject` · **Erbt von:** [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Vectorworks-eigener Schichtkörper. Profile werden in Querschnittsreihenfolge kopiert und gleichmäßig zwischen baseElevation und baseElevation + thickness verteilt. Mindestens zwei Vectorworks-eigene 2D-Profile sind erforderlich.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `MultiExtrudeObject(h: Handle)` | Verweist auf den vorhandenen Schichtkörper `h`; vor der Verwendung `IsValid()` prüfen. |

**Methoden**

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | True, wenn `h` auf ein Objekt des von dieser Klasse dargestellten Typs verweist. |
| `Create(profiles: list[Handle], baseElevation: float, thickness: float) -> MultiExtrudeObject` *statisch* | Erstellt einen Schichtkörper aus den 2D-Profilen `profiles` (Liste von Handles) auf der Basishöhe `baseElevation` mit der Dicke `thickness`. |
| `Duplicate() -> MultiExtrudeObject` | Dupliziert den Schichtkörper in der Zeichnung und gibt die Kopie zurück. |
| `GetExtrudeValues() -> ExtrudeObject.Values \| None` | Gibt die Extrusionswerte zurück. |
| `SetExtrudeValues(baseElevation: float, thickness: float) -> bool` | Legt die Extrusionswerte fest. |
| `GetProfiles() -> list[Handle]` | Gibt die Profile zurück. |

Geerbt: alle Elemente von [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

### SurfaceModelObject

> **Vollständiger Name:** `api.SurfaceModelObject` · **Erbt von:** [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Ein Modellierungsergebnis ist eine NURBS-Fläche, ein CSG-Vollkörper oder eine Gruppe von Modellierungsergebnissen. Hier wird die Ergebnisform geprüft; es handelt sich nicht um einen dauerhaften Typ für Modellierungsmerkmale oder Herkunft. Erzeugungsfunktionen erhalten alle Eingabeobjekte und platzieren ein Ergebnis im aktuellen Container. Koordinaten und Längen werden in Welteinheiten angegeben, alle Winkel im Bogenmaß.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `SurfaceModelObject(h: Handle)` | Verweist auf das vorhandene Oberflächenmodell `h`; vor der Verwendung `IsValid()` prüfen. |

**Methoden**

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | True, wenn `h` auf ein Objekt des von dieser Klasse dargestellten Typs verweist. |
| `CreateLoft(sections: list[Handle], ruled: bool = False, closed: bool = False, solid: bool = False) -> SurfaceModelObject` *statisch* | Geordnete NURBS-Kurven oder 3D-Punkte. Geschlossene Kurvenverbindungen benötigen mindestens drei Querschnitte. solid fordert Abschlussflächen und das Zusammenfügen an; ein fehlgeschlagenes Zusammenfügen wird gemeldet und nicht als Gruppe zurückgegeben. |
| `CreateRailSweep(sections: list[Handle], rail: Handle, secondRail: Handle = None, solid: bool = False) -> SurfaceModelObject` *statisch* | Eine oder zwei NURBS-Leitkurven; die Querschnitte sind NURBS-Kurven in ihrer Reihenfolge entlang der Leitkurven. |
| `CreateRevolve(profile: Handle, values: SweepObject.Values = SweepObject.Values()) -> SurfaceModelObject` *statisch* | Verwendet die Vectorworks-eigene Profil- und Achsenkonvention für Rotationskörper und wandelt das Ergebnis anschließend in NURBS um. |
| `CreateRevolveWithRail(profile: Handle, rail: Handle, axis: Handle) -> SurfaceModelObject` *statisch* | Die Achse muss eine lineare Kurve sein. Vectorworks prüft Schnittpunkte und die Kompatibilität von Profil und Leitkurve. |
| `CreateExtrudeAlongPath(path: Handle, profile: Handle) -> SurfaceModelObject` *statisch* | Der Pfad muss eine NURBS-Kurve sein. Das Ergebnis ist ein CSG-Vollkörper bzw. eine CSG-Fläche ohne Bearbeitungshistorie. |
| `CreateExtrudeAlongPath(path: Handle, profile: Handle, options: SurfaceModelObject.PathOptions) -> SurfaceModelObject` *statisch* | Der Pfad muss eine NURBS-Kurve sein. Das Ergebnis ist ein CSG-Vollkörper bzw. eine CSG-Fläche ohne Bearbeitungshistorie. |
| `CreateTaperedExtrude(profile: Handle, angle: float, height: float) -> SurfaceModelObject` *statisch* | Erstellt einen Verjüngungskörper aus dem 2D-Profil `profile` mit dem Verjüngungswinkel `angle` und der Höhe `height`. |
| `CreateCylinder(baseCenter: Point3D, radius: float, height: float) -> ExtrudeObject` *statisch* | Erstellt einen Zylinder (einen Extrusionskörper aus einem Kreis) mit dem Grundflächenmittelpunkt `baseCenter`, dem Radius `radius` und der Höhe `height`. |
| `CreateBox(minimum: Point3D, maximum: Point3D) -> ExtrudeObject` *statisch* | Erstellt einen achsenparallelen Quader (einen Extrusionskörper aus einem Rechteck) von der Ecke `minimum` bis zur Ecke `maximum`. |
| `CreateTorus(center: Point3D, majorRadius: float, minorRadius: float) -> SweepObject` *statisch* | Ringtorus um die Z-Achse des Weltkoordinatensystems; majorRadius > minorRadius > 0. |
| `Duplicate() -> SurfaceModelObject` | Dupliziert das Oberflächenmodell in der Zeichnung und gibt die Kopie zurück. |

Geerbt: alle Elemente von [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

#### SurfaceModelObject.PathOptions

> **Vollständiger Name:** `api.SurfaceModelObject.PathOptions` · **Erbt von:** `api.Object`

Optionen für Skalierung und Profilplatzierung eines Pfadkörpers (Extrusion entlang eines Pfads).

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `PathOptions()` | Standardwert (Felder mit ihren Standardwerten). |
| `PathOptions(isExponentialScale, scale, isProfilePlaneLocked, isProfileFixed)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `isExponentialScale` | `bool` | Skaliert das Profil entlang des Pfads exponentiell statt linear. |
| `scale` | `float` | Skalierung des Profils am Pfadende. |
| `isProfilePlaneLocked` | `bool` | Hält die Profilebene fest, während das Profil dem Pfad folgt. |
| `isProfileFixed` | `bool` | Hält das Profil unverändert ausgerichtet (keine Drehung entlang des Pfads). |

### GenericSolidObject

> **Vollständiger Name:** `api.GenericSolidObject` · **Erbt von:** [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Umfasst Vectorworks-eigene Vollkörper, einschließlich der mit den Befehlen Volumen zusammenfügen, Schnittvolumen löschen und Schnittvolumen anlegen erzeugten Vollkörper und einfacher Vollkörper ohne Bearbeitungshistorie. Es wird keine künstliche Historie gespeichert: Verwendet wird der tatsächliche Operandenbaum des Dokuments.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `GenericSolidObject(h: Handle)` | Verweist auf den vorhandenen einfachen Vollkörper `h`; vor der Verwendung `IsValid()` prüfen. |

**Methoden**

*Allgemein*

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | True, wenn `h` auf ein Objekt des von dieser Klasse dargestellten Typs verweist. |
| `IsGenericSolid(h: Handle) -> bool` *statisch* | Gibt True zurück, wenn `h` ein einfacher Vollkörper (ein CSG-Vollkörper) ist. |
| `Create(hSolid: Handle, keepOriginal: bool = True) -> GenericSolidObject` *statisch* | Vorhandene CSG-Vollkörper werden unverändert verwendet oder dupliziert. Andere Grundkörper werden zu einer Vereinigung mit einem einzigen Operanden, wobei der Grundkörper erhalten bleibt. Bei Erfolg verschiebt keepOriginal=`False` die Eingabeobjekte in die Bearbeitungshistorie; bei einem Fehlschlag bleiben sie unverändert. Erzeugte Ergebnisse verbleiben im Container des Eingabeobjekts, außer Ergebnissen boolescher Operationen mit zwei Eingabeobjekten, die in den aktiven Container eingefügt werden. |
| `CreateBoolean(operation: GenericSolidObject.Operation, hBlank: Handle, hTool: Handle, keepOriginal: bool = True) -> GenericSolidObject` *statisch* | Erstellt das Ergebnis der booleschen Vollkörperoperation `operation` mit `hBlank` und `hTool`. Vorhandene CSG-Vollkörper werden unverändert verwendet oder dupliziert. Andere Grundkörper werden zu einer Vereinigung mit einem einzigen Operanden, wobei der Grundkörper erhalten bleibt. Bei Erfolg verschiebt keepOriginal=`False` die Eingabeobjekte in die Bearbeitungshistorie; bei einem Fehlschlag bleiben sie unverändert. Erzeugte Ergebnisse verbleiben im Container des Eingabeobjekts, außer Ergebnissen boolescher Operationen mit zwei Eingabeobjekten, die in den aktiven Container eingefügt werden. |
| `CreateUnion(hBlank: Handle, hTool: Handle, keepOriginal: bool = True) -> GenericSolidObject` *statisch* | Erstellt die Vereinigung von `hBlank` und `hTool`. Vorhandene CSG-Vollkörper werden unverändert verwendet oder dupliziert. Andere Grundkörper werden zu einer Vereinigung mit einem einzigen Operanden, wobei der Grundkörper erhalten bleibt. Bei Erfolg verschiebt keepOriginal=`False` die Eingabeobjekte in die Bearbeitungshistorie; bei einem Fehlschlag bleiben sie unverändert. Erzeugte Ergebnisse verbleiben im Container des Eingabeobjekts, außer Ergebnissen boolescher Operationen mit zwei Eingabeobjekten, die in den aktiven Container eingefügt werden. |
| `CreateIntersection(hBlank: Handle, hTool: Handle, keepOriginal: bool = True) -> GenericSolidObject` *statisch* | Erstellt die Schnittmenge von `hBlank` und `hTool`. Vorhandene CSG-Vollkörper werden unverändert verwendet oder dupliziert. Andere Grundkörper werden zu einer Vereinigung mit einem einzigen Operanden, wobei der Grundkörper erhalten bleibt. Bei Erfolg verschiebt keepOriginal=`False` die Eingabeobjekte in die Bearbeitungshistorie; bei einem Fehlschlag bleiben sie unverändert. Erzeugte Ergebnisse verbleiben im Container des Eingabeobjekts, außer Ergebnissen boolescher Operationen mit zwei Eingabeobjekten, die in den aktiven Container eingefügt werden. |
| `CreateDifference(hBlank: Handle, hTool: Handle, keepOriginal: bool = True) -> GenericSolidObject` *statisch* | Erstellt `hBlank` abzüglich `hTool`. Vorhandene CSG-Vollkörper werden unverändert verwendet oder dupliziert. Andere Grundkörper werden zu einer Vereinigung mit einem einzigen Operanden, wobei der Grundkörper erhalten bleibt. Bei Erfolg verschiebt keepOriginal=`False` die Eingabeobjekte in die Bearbeitungshistorie; bei einem Fehlschlag bleiben sie unverändert. Erzeugte Ergebnisse verbleiben im Container des Eingabeobjekts, außer Ergebnissen boolescher Operationen mit zwei Eingabeobjekten, die in den aktiven Container eingefügt werden. |
| `CreateFromExtrude(hProfile: Handle, baseElevation: float, thickness: float, keepOriginal: bool = True) -> GenericSolidObject` *statisch* | Erstellt einen Vollkörper durch Extrusion des 2D-Objekts `hProfile` ab der Basishöhe `baseElevation` um die Dicke `thickness`. Vorhandene CSG-Vollkörper werden unverändert verwendet oder dupliziert. Andere Grundkörper werden zu einer Vereinigung mit einem einzigen Operanden, wobei der Grundkörper erhalten bleibt. Bei Erfolg verschiebt keepOriginal=`False` die Eingabeobjekte in die Bearbeitungshistorie; bei einem Fehlschlag bleiben sie unverändert. Erzeugte Ergebnisse verbleiben im Container des Eingabeobjekts, außer Ergebnissen boolescher Operationen mit zwei Eingabeobjekten, die in den aktiven Container eingefügt werden. |
| `CreateFromExtrude(profile: Math.Polygon2D, baseElevation: float, thickness: float) -> GenericSolidObject` *statisch* | Erstellt einen Vollkörper durch Extrusion des Polygons `profile` ab der Basishöhe `baseElevation` um die Dicke `thickness`. Vorhandene CSG-Vollkörper werden unverändert verwendet oder dupliziert. Andere Grundkörper werden zu einer Vereinigung mit einem einzigen Operanden, wobei der Grundkörper erhalten bleibt. Bei Erfolg verschiebt keepOriginal=`False` die Eingabeobjekte in die Bearbeitungshistorie; bei einem Fehlschlag bleiben sie unverändert. Erzeugte Ergebnisse verbleiben im Container des Eingabeobjekts, außer Ergebnissen boolescher Operationen mit zwei Eingabeobjekten, die in den aktiven Container eingefügt werden. |
| `CreateFromExtrude(rect: Math.Rect2D, baseElevation: float, thickness: float) -> GenericSolidObject` *statisch* | Erstellt einen Vollkörper durch Extrusion des Rechtecks `rect` ab der Basishöhe `baseElevation` um die Dicke `thickness`. Vorhandene CSG-Vollkörper werden unverändert verwendet oder dupliziert. Andere Grundkörper werden zu einer Vereinigung mit einem einzigen Operanden, wobei der Grundkörper erhalten bleibt. Bei Erfolg verschiebt keepOriginal=`False` die Eingabeobjekte in die Bearbeitungshistorie; bei einem Fehlschlag bleiben sie unverändert. Erzeugte Ergebnisse verbleiben im Container des Eingabeobjekts, außer Ergebnissen boolescher Operationen mit zwei Eingabeobjekten, die in den aktiven Container eingefügt werden. |
| `CreateFromExtrude(points: list[Math.Point2D], baseElevation: float, thickness: float, closed: bool = True) -> GenericSolidObject` *statisch* | Erstellt einen Vollkörper durch Extrusion des Polygons durch `points` ab der Basishöhe `baseElevation` um die Dicke `thickness`. Vorhandene CSG-Vollkörper werden unverändert verwendet oder dupliziert. Andere Grundkörper werden zu einer Vereinigung mit einem einzigen Operanden, wobei der Grundkörper erhalten bleibt. Bei Erfolg verschiebt keepOriginal=`False` die Eingabeobjekte in die Bearbeitungshistorie; bei einem Fehlschlag bleiben sie unverändert. Erzeugte Ergebnisse verbleiben im Container des Eingabeobjekts, außer Ergebnissen boolescher Operationen mit zwei Eingabeobjekten, die in den aktiven Container eingefügt werden. |
| `CreatePlanar(points: list[Point3D], thickness: float) -> GenericSolidObject` *statisch* | Erstellt einen Vollkörper aus dem ebenen 3D-Polygon `points` mit der Dicke `thickness`. Vorhandene CSG-Vollkörper werden unverändert verwendet oder dupliziert. Andere Grundkörper werden zu einer Vereinigung mit einem einzigen Operanden, wobei der Grundkörper erhalten bleibt. Bei Erfolg verschiebt keepOriginal=`False` die Eingabeobjekte in die Bearbeitungshistorie; bei einem Fehlschlag bleiben sie unverändert. Erzeugte Ergebnisse verbleiben im Container des Eingabeobjekts, außer Ergebnissen boolescher Operationen mit zwei Eingabeobjekten, die in den aktiven Container eingefügt werden. |
| `CreateBetween(hProfile: Handle, start: Point3D, end: Point3D, keepOriginal: bool = True) -> GenericSolidObject` *statisch* | Erstellt einen Vollkörper durch Extrusion des Profils `hProfile` von `start` nach `end`. Vorhandene CSG-Vollkörper werden unverändert verwendet oder dupliziert. Andere Grundkörper werden zu einer Vereinigung mit einem einzigen Operanden, wobei der Grundkörper erhalten bleibt. Bei Erfolg verschiebt keepOriginal=`False` die Eingabeobjekte in die Bearbeitungshistorie; bei einem Fehlschlag bleiben sie unverändert. Erzeugte Ergebnisse verbleiben im Container des Eingabeobjekts, außer Ergebnissen boolescher Operationen mit zwei Eingabeobjekten, die in den aktiven Container eingefügt werden. |
| `CreateBetween(hProfile: Handle, start: Point3D, end: Point3D, up: Point3D, keepOriginal: bool = True) -> GenericSolidObject` *statisch* | Erstellt einen Vollkörper durch Extrusion des Profils `hProfile` von `start` nach `end`, wobei `up` das Profil ausrichtet. Vorhandene CSG-Vollkörper werden unverändert verwendet oder dupliziert. Andere Grundkörper werden zu einer Vereinigung mit einem einzigen Operanden, wobei der Grundkörper erhalten bleibt. Bei Erfolg verschiebt keepOriginal=`False` die Eingabeobjekte in die Bearbeitungshistorie; bei einem Fehlschlag bleiben sie unverändert. Erzeugte Ergebnisse verbleiben im Container des Eingabeobjekts, außer Ergebnissen boolescher Operationen mit zwei Eingabeobjekten, die in den aktiven Container eingefügt werden. |
| `CanConvertToGenericSolid(h: Handle) -> bool` *statisch* | Gibt `True` für Objekte zurück, die ConvertToGenericSolid akzeptiert: CSG-Vollkörper (einschließlich Hohlkörpern), Extrusionskörper, Rotationskörper, Punktkörper, Grundkörper (Kugel, Halbkugel, Kegel, ...), geschlossene 3D-Polygone mit mindestens drei Scheitelpunkten und andere zulässige CSG-Grundobjekte (Wände, Böden/Decken, NURBS, Symbole, ...). |

*Wie VectorScript ConvertToGenericSolid*

| Methode | Beschreibung |
|---|---|
| `ConvertToGenericSolid(hObject: Handle, keepOriginal: bool = True) -> GenericSolidObject` *statisch* | Erstellt einen einfachen Vollkörper ohne Bearbeitungshistorie. Objektarten, die die Vectorworks-Umwandlung nicht direkt akzeptiert, werden zunächst in eine Vereinigung mit einem einzigen Operanden aufgenommen. Das Ergebnis wird neben dem Ausgangsobjekt platziert; keepOriginal=`False` löscht bei Erfolg das Ausgangsobjekt (nicht für Operanden verwenden, die in der Bearbeitungshistorie eines anderen Vollkörpers verschachtelt sind). Für das Ergebnis nicht umkehrbar. |
| `Duplicate() -> GenericSolidObject` | Dupliziert den einfachen Vollkörper in der Zeichnung und gibt die Kopie zurück. |
| `GetAction() -> int \| None` | Gibt die Aktion zurück. |
| `GetOperation() -> GenericSolidObject.Operation \| None` | Gibt die Operation zurück. |
| `HasHistory() -> bool \| None` | Gibt True zurück, wenn der Vollkörper seine Modellierungshistorie beibehält. |
| `SetOperation(operation: GenericSolidObject.Operation) -> bool` | Legt die Operation fest. |
| `GetOperands() -> list[Handle]` | Gibt die Operanden zurück. |
| `GetOperandCount() -> int` | Anzahl der Operanden. |
| `GetOperand(index: int) -> Handle` | Gibt den Operanden am Index `index` zurück. |
| `SetOperand(index: int, hSolid: Handle) -> bool` | Kopiert den angegebenen Vollkörper in diese Position, im ursprünglichen Koordinatensystem der Operanden. Nur boolesche Knoten können bearbeitet werden. Handles ersetzter Operanden werden nur bei Erfolg ungültig. |
| `GetHistory() -> list[GenericSolidObject.HistoryStep]` | Gibt die Bearbeitungshistorie zurück. |
| `Rebuild() -> bool` | Berechnet im Gegensatz zum geerbten `Reset()` nach Änderungen über Handles aus der Bearbeitungshistorie die zwischengespeicherten CSG-Daten neu. Berechnen Sie nach mehreren zusammengefassten Änderungen den äußersten Vollkörper neu. Bei `False` bleiben die Änderungen bestehen. |

*Nicht umkehrbar*

| Methode | Beschreibung |
|---|---|
| `ClearHistory() -> bool` | Entfernt alle Operanden und Merkmalsdaten und macht deren Handles ungültig. |
| `GetTransform() -> ExtrudeObject.Transform \| None` | Gibt die Transformation zurück. |
| `SetTransform(transform: ExtrudeObject.Transform) -> bool` | Legt die Transformation fest. |
| `GetScale() -> Point3D \| None` | Gibt den Skalierungsfaktor zurück. |
| `SetScale(scale: Point3D) -> bool` | Setzt den Maßstab. |
| `Move3D(offset: Point3D) -> bool` | Verschiebt den Vollkörper um `offset` im 3D-Raum. |
| `GetVolume() -> float \| None` | Gibt das Volumen zurück. |
| `GetSurfaceArea() -> float \| None` | Gibt den Oberflächeninhalt zurück. |
| `ConvertToMesh(keepOriginal: bool = True) -> MeshObject` | Zerlegt den Vollkörper in einen Punktkörper, der unmittelbar danach platziert wird; der Vollkörper wird gelöscht, sofern keepOriginal nicht den Wert `True` hat. Für Vollkörper, die in der Bearbeitungshistorie eines anderen Vollkörpers verschachtelt sind, ist keepOriginal = `True` erforderlich. |

Geerbt: alle Elemente von [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

#### GenericSolidObject.HistoryStep

> **Vollständiger Name:** `api.GenericSolidObject.HistoryStep` · **Erbt von:** `api.Object`

Ein Knoten im Vectorworks-eigenen Konstruktionsbaum, in Präorder-Reihenfolge.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `HistoryStep()` | Standardwert (Felder mit ihren Standardwerten). |
| `HistoryStep(object, parent, operandIndex, depth, action, operation, hasHistory)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `object` | `Handle` | Handle des Objekts dieses Schritts. |
| `parent` | `Handle` | Handle des übergeordneten Schritts. |
| `operandIndex` | `int` | Index des Operanden im übergeordneten Objekt. |
| `depth` | `int` | Tiefe des Schritts im Historienbaum. |
| `action` | `int` | Unverarbeiteter Aktionscode des Schritts (-1, wenn keiner vorhanden ist). |
| `operation` | `GenericSolidObject.Operation \| None` | Vollkörperoperation des Schritts; `None`, wenn es keine boolesche Operation ist. |
| `hasHistory` | `bool` | Gibt an, ob der Schritt eine eigene Bearbeitungshistorie hat. |

#### GenericSolidObject.Operation

> **Vollständiger Name:** `api.GenericSolidObject.Operation` · **Art:** `IntEnum`

Boolesche Vollkörperoperation.

| Element | Wert | Beschreibung |
|---|---|---|
| `Union` | `0` |  |
| `Intersection` | `1` |  |
| `Difference` | `2` |  |

### ShellObject

> **Vollständiger Name:** `api.ShellObject` · **Erbt von:** [`GenericSolidObject`](#genericsolidobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Hohlkörper: ein CSG-Versatzknoten (Werkzeug Hohlkörper, VectorScript CreateShell). Er hat genau einen Operanden (die Ausgangsfläche oder den Ausgangsvollkörper) und speichert die Dicke und die gewählten Flächen in der Bearbeitungshistorie. Eine NURBS-Fläche wird verdickt; ein Vollkörper wird ausgehöhlt, wobei die gewählten Flächen entfernt werden (offene Flächen). Die gespeicherte Dicke ist vorzeichenbehaftet: Negative Werte versetzen zur gegenüberliegenden Seite („Versatzseite“ in der Infopalette). Die geerbte boolesche Bearbeitung (SetOperation / SetOperand) ist auf Hohlkörperknoten nicht anwendbar.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `ShellObject(h: Handle)` | Verweist auf den vorhandenen Hohlkörper `h`; vor der Verwendung `IsValid()` prüfen. |

**Methoden**

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | CSG-Knoten mit der Versatzaktion, einschließlich eines Knotens, dessen letzte Neuberechnung fehlgeschlagen ist. |
| `Create(hSurface: Handle, thickness: float, keepOriginal: bool = True) -> ShellObject` *statisch* | `thickness` muss endlich und ungleich null sein; ein negativer Wert verdickt zur gegenüberliegenden Seite. Das Ergebnis wird anstelle des Ausgangsobjekts eingefügt, das zum Operanden des Hohlkörpers wird; mit keepOriginal wird stattdessen eine Kopie des Ausgangsobjekts verwendet. Bei einem Fehlschlag bleiben die Eingabeobjekte unverändert. Registriert den Hohlkörper und gegebenenfalls die Kopie des Ausgangsobjekts für Rückgängig und schließt sich einem vorhandenen Ereignis an. Registrieren Sie den zurückgegebenen Hohlkörper nicht erneut. Ein neu erstelltes Ausgangsobjekt muss vor diesem Aufruf registriert werden. |
| `CreateFromSolid(hSolid: Handle, openFaceIndices: list[int], thickness: float, keepOriginal: bool = True) -> ShellObject` *statisch* | Höhlt einen Vollkörper aus; `openFaceIndices` enthält ab 0 indizierte Flächenindizes (siehe GetFaceCount), deren Flächen aus dem Hohlkörper entfernt werden. |
| `GetFaceCount(h: Handle) -> int \| None` *statisch* | Anzahl der über CreateFromSolid ansprechbaren Flächen. |
| `Duplicate() -> ShellObject` | Dupliziert den Hohlkörper in der Zeichnung und gibt die Kopie zurück. |
| `IsFailed() -> bool \| None` | Gibt True zurück, wenn der Hohlkörper nicht erstellt werden konnte. |
| `GetThickness() -> float \| None` | Betrag der Dicke; die Seite wird von IsReversed angegeben. |
| `SetThickness(thickness: float) -> bool` | Positiver Betrag unter Beibehaltung der Seite. Eine fehlgeschlagene Neuberechnung stellt den vorherigen Wert wieder her. |
| `IsReversed() -> bool \| None` | Gibt True zurück, wenn der Hohlkörper auf der umgekehrten Seite der Oberfläche erstellt wird. |
| `SetReversed(isReversed: bool) -> bool` | Schaltet *Umgekehrt* ein oder aus. |
| `GetSource() -> Handle` | Die verdickte Fläche oder der ausgehöhlte Vollkörper (der einzige Operand). |
| `IsMonikerBased() -> bool \| None` | Flächen werden anhand dauerhafter Kennungen verfolgt, wenn das Ausgangsobjekt diese unterstützt, andernfalls anhand ihres Index. |
| `GetSelectedFaceIndices() -> list[int]` | Gibt die Indizes der gewählten Flächen zurück. |
| `GetSelectedFaceMonikers() -> list[str]` | Gibt die Kennungen der gewählten Flächen zurück. |
| `ResolveSelectedFaceIndices() -> list[int] \| None` | Sortierte, eindeutige aktuelle Flächenindizes des Ausgangsobjekts, beginnend bei 0, einschließlich der als Kennungen gespeicherten Auswahl. Nicht verfügbar, wenn das Ausgangsobjekt nicht gelesen werden kann oder eine gewählte Fläche nicht mehr zugeordnet werden kann. |

Geerbt: alle Elemente von [`GenericSolidObject`](#genericsolidobject), [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

### Polygon3DObject

> **Vollständiger Name:** `api.Polygon3DObject` · **Erbt von:** [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Vectorworks-eigenes 3D-Polygon (`ObjectType.Polygon3D`). Scheitelpunkte sind Eckpunkte in übergeordneten Koordinaten (Welteinheiten); ein 3D-Polygon hat weder Bogen-/Bézier-Punkte noch eine Sichtbarkeit pro Kante. Indizes beginnen bei 0. Ein 3D-Polygon behält immer mindestens zwei Scheitelpunkte. Der Zugriff auf ein vorhandenes Polygon über diese Klasse verändert es nicht.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `Polygon3DObject(h: Handle)` | Verweist auf das vorhandene 3D-Polygon `h`; vor der Verwendung `IsValid()` prüfen. |

**Methoden**

*Allgemein*

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | True, wenn `h` auf ein Objekt des von dieser Klasse dargestellten Typs verweist. |
| `Create(points: list[Point3D], closed: bool = True) -> Polygon3DObject` *statisch* | Erfordert 2..32767 Punkte mit endlichen Koordinaten; das neue Polygon wird auf der aktiven Ebene eingefügt. |

*Nur Eckpunkte*

| Methode | Beschreibung |
|---|---|
| `Create(polygon: Math.Polygon2D, z: float = 0.0) -> Polygon3DObject` *statisch* | Bogen- und Bézier-Punktdaten des 2D-Polygons werden ignoriert. |
| `Create(rect: Math.Rect2D, z: float = 0.0) -> Polygon3DObject` *statisch* | Bogen- und Bézier-Punktdaten des 2D-Polygons werden ignoriert. |
| `ConvertToGroup(hObject: Handle, keepOriginal: bool = True) -> Handle` *statisch* | Wandelt ein beliebiges 2D-/3D-Objekt in 3D-Polygone um (ConvertTo3DPolygons). Gibt die Gruppe mit den Polygonen oder einen Null-Handle zurück. Das Original wird gelöscht, sofern keepOriginal nicht den Wert `True` hat. |
| `GetPolygonsIn(hContainer: Handle) -> list[Handle]` *statisch* | 3D-Polygone innerhalb eines Containers (Gruppe, Ebene, Symbol, ...), einschließlich solcher in verschachtelten Gruppen. |
| `Duplicate() -> Polygon3DObject` | Dupliziert das 3D-Polygon in der Zeichnung und gibt die Kopie zurück. |

*Scheitelpunkte*

| Methode | Beschreibung |
|---|---|
| `GetVertexCount() -> int` | Anzahl der Scheitelpunkte. |
| `GetVertex(index: int) -> Point3D \| None` | Gibt den Scheitelpunkt bei `index` zurück. |
| `SetVertex(index: int, point: Point3D) -> bool` | Legt den Scheitelpunkt am Index `index` fest. |
| `GetVertices() -> list[Point3D]` | Gibt die Scheitelpunkte zurück. |
| `SetVertices(points: list[Point3D]) -> bool` | Legt die Scheitelpunkte fest (2..32767 Punkte). |
| `AddVertex(point: Point3D) -> bool` | Hängt den Scheitelpunkt `point` an. |
| `AddVertices(points: list[Point3D], reverse: bool = False) -> bool` | Hängt die Scheitelpunkte `points` an (in umgekehrter Reihenfolge, wenn `reverse` den Wert `True` hat). |
| `InsertVertex(beforeIndex: int, point: Point3D) -> bool` | Fügt `point` vor dem Scheitelpunkt `beforeIndex` ein (0 .. Anzahl der Scheitelpunkte). |
| `DeleteVertex(index: int) -> bool` | Löscht den Scheitelpunkt am Index `index`; schlägt fehl, wenn nur noch zwei Scheitelpunkte vorhanden sind. |
| `IsClosed() -> bool` | True, wenn das Polygon geschlossen ist. |
| `SetClosed(closed: bool) -> bool` | Schaltet *Geschlossen* ein oder aus. |

*Form*

| Methode | Beschreibung |
|---|---|
| `GetPolygon2D() -> Math.Polygon2D \| None` | Gibt das 2D-Polygon zurück (XY-Projektion; das Kennzeichen für die geschlossene Form bleibt erhalten). |
| `IsClockwise() -> bool \| None` | Gibt True zurück, wenn die XY-Projektion im Uhrzeigersinn verläuft (Vorzeichen der z-Komponente der Newell-Normalen). |
| `Reverse() -> bool` | Kehrt die Scheitelpunktreihenfolge um (kehrt die Polygonnormale um). |
| `IsPlanar(tolerance: float = 1e-09) -> bool \| None` | Gibt True zurück, wenn alle Scheitelpunkte innerhalb der Toleranz `tolerance` in einer Ebene liegen. |
| `IsValidPolygon(tolerance: float = 1e-09) -> bool \| None` | Gibt True zurück, wenn das Polygon genügend unterschiedliche Scheitelpunkte besitzt, um gültig zu sein (innerhalb der Toleranz `tolerance`). |
| `GetNormal() -> Point3D \| None` | Gibt die Normale zurück (Newell-Normale mit Einheitslänge). |
| `GetPlane() -> Polygon3DObject.Plane \| None` | Gibt die Ebene zurück. |
| `GetPlaneTransform() -> ExtrudeObject.Transform \| None` | Gibt die Ebenentransformation zurück (lokales Koordinatensystem mit W entlang der Polygonnormalen). |
| `GetVertexCentroid() -> Point3D \| None` | Messungen (Welteinheiten); 3D-Begrenzungen, Mittelpunkt (Get3DCntr) und Größe (Get3DInfo) stammen von PrimitiveObject (Mittelwert der Scheitelpunkte). |
| `GetLength() -> float \| None` | Gibt die Länge zurück (bei geschlossenem Polygon einschließlich der schließenden Kante). |
| `GetSegmentLength(segmentIndex: int) -> float \| None` | Gibt die Segmentlänge am Index `segmentIndex` zurück. |
| `GetArea() -> float \| None` | Gibt den Flächeninhalt zurück (ebener Flächeninhalt eines geschlossenen Polygons nach Newell). |
| `GetPointAtDistance(distance: float) -> Point3D \| None` | Gibt den Punkt beim Abstand `distance` zurück (Abstand entlang des Pfads). |
| `GetClosestPoint(point: Point3D) -> Polygon3DObject.ClosestPoint \| None` | Gibt den nächstgelegenen Punkt zu `point` zurück. |
| `GetDistanceTo(point: Point3D) -> float \| None` | Gibt den Abstand zu `point` zurück. |
| `GetDistanceToPlane(point: Point3D) -> float \| None` | Gibt den vorzeichenbehafteten Abstand von `point` zur Ebene zurück. |
| `IntersectLine(start: Point3D, direction: Point3D) -> Point3D \| None` | Schnittpunkt der Geraden durch `start` in Richtung `direction` mit der Ebene des Polygons. |

*Bearbeitungen*

| Methode | Beschreibung |
|---|---|
| `Cleanup(tolerance: float = 1e-09) -> bool` | Entfernt doppelte und kollineare Scheitelpunkte (innerhalb der Toleranz `tolerance`). |
| `CleanupFeaturePreserving(collinearTolerance: float, closenessTolerance: float) -> bool` | Entfernt kollineare (`collinearTolerance`) und nahezu zusammenfallende (`closenessTolerance`) Scheitelpunkte unter Beibehaltung der Form. |
| `Simplify(maxDeviation: float) -> bool` | Vereinfacht das Polygon mit dem Douglas-Peucker-Algorithmus bei einer maximalen Abweichung von `maxDeviation`. |
| `Segment(maxSegmentLength: float) -> bool` | Unterteilt die Kanten, die länger als `maxSegmentLength` sind. |
| `Transform(transform: ExtrudeObject.Transform) -> bool` | Transformiert das Polygon mit `transform` (bildet lokale Koordinaten auf das übergeordnete Koordinatensystem ab). |
| `Move3D(offset: Point3D) -> bool` | Verschiebt das Polygon um `offset` im 3D-Raum. |
| `Rotate3D(center: Point3D, axis: Point3D, angleDegrees: float) -> bool` | Dreht das Polygon um `angleDegrees` Grad um die Achse `axis` durch `center`. |
| `Scale3D(center: Point3D, factors: Point3D) -> bool` | Skaliert das Polygon mit `factors` (pro Achse) relativ zu `center`. |

*Zusammenarbeit mit einfachen Vollkörpern*

| Methode | Beschreibung |
|---|---|
| `IsValidSolidOperand() -> bool` | Nur geschlossene Polygone mit mindestens drei Scheitelpunkten sind gültige Operanden. keepOriginal = `False` verschiebt dieses Polygon in die Bearbeitungshistorie des neuen Vollkörpers. |
| `ToGenericSolid(keepOriginal: bool = True) -> GenericSolidObject` | Wandelt das Polygon in einen einfachen Vollkörper um. Nur geschlossene Polygone mit mindestens drei Scheitelpunkten sind gültige Operanden. keepOriginal = `False` verschiebt dieses Polygon in die Bearbeitungshistorie des neuen Vollkörpers. |
| `Union(hTool: Handle, keepOriginal: bool = True) -> GenericSolidObject` | Vereinigung mit dem Vollkörper `hTool` als einfacher Vollkörper. Nur geschlossene Polygone mit mindestens drei Scheitelpunkten sind gültige Operanden. keepOriginal = `False` verschiebt dieses Polygon in die Bearbeitungshistorie des neuen Vollkörpers. |
| `Subtract(hTool: Handle, keepOriginal: bool = True) -> GenericSolidObject` | Subtrahiert den Vollkörper `hTool` und ergibt einen einfachen Vollkörper. Nur geschlossene Polygone mit mindestens drei Scheitelpunkten sind gültige Operanden. keepOriginal = `False` verschiebt dieses Polygon in die Bearbeitungshistorie des neuen Vollkörpers. |
| `Intersect(hTool: Handle, keepOriginal: bool = True) -> GenericSolidObject` | Schnittmenge mit dem Vollkörper `hTool` als einfacher Vollkörper. Nur geschlossene Polygone mit mindestens drei Scheitelpunkten sind gültige Operanden. keepOriginal = `False` verschiebt dieses Polygon in die Bearbeitungshistorie des neuen Vollkörpers. |
| `ConvertToGenericSolid(keepOriginal: bool = True) -> GenericSolidObject` | Einfacher Vollkörper ohne Bearbeitungshistorie (wie ConvertToGenericSolid); keepOriginal = `False` löscht dieses Polygon. |
| `ToPlanarSolid(thickness: float) -> GenericSolidObject` | Vollkörper mit den Polygonscheitelpunkten als ebener Grundfläche, um die Dicke entlang der Normalen extrudiert. |

Geerbt: alle Elemente von [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

#### Polygon3DObject.Plane

> **Vollständiger Name:** `api.Polygon3DObject.Plane` · **Erbt von:** `api.Object`

Ebene durch den Schwerpunkt der Scheitelpunkte; die Normale ist ein Einheitsvektor gemäß der Scheitelpunktreihenfolge (Rechte-Hand-Regel), und d erfüllt für Punkte p auf der Ebene die Gleichung normal . p + d = 0.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `Plane()` | Standardwert (Felder mit ihren Standardwerten). |
| `Plane(point, normal, d)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `point` | `Point3D` | Schwerpunkt der Scheitelpunkte (ein Punkt auf der Ebene). |
| `normal` | `Point3D` | Einheitsnormale gemäß der Scheitelpunktreihenfolge (Rechte-Hand-Regel). |
| `d` | `float` | Ebenenkonstante: `normal . p + d = 0` für Punkte `p` auf der Ebene. |

#### Polygon3DObject.ClosestPoint

> **Vollständiger Name:** `api.Polygon3DObject.ClosestPoint` · **Erbt von:** `api.Object`

Nächstgelegener Punkt auf dem Polygonpfad, sein Abstand, der Kantenindex und die Pfadlänge ab dem ersten Scheitelpunkt.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `ClosestPoint()` | Standardwert (Felder mit ihren Standardwerten). |
| `ClosestPoint(point, distance, segmentIndex, distanceAlong)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `point` | `Point3D` | Nächstgelegener Punkt. |
| `distance` | `float` | Abstand zum nächstgelegenen Punkt. |
| `segmentIndex` | `int` | Kante vom Scheitelpunkt segmentIndex zum nächsten Scheitelpunkt. |
| `distanceAlong` | `float` | Pfadlänge vom ersten Scheitelpunkt zum Punkt. |

### MeshObject

> **Vollständiger Name:** `api.MeshObject` · **Erbt von:** [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Vectorworks-eigener Punktkörper (`ObjectType.Mesh`): eine gemeinsame Scheitelpunktliste und polygonale Flächen, die über Indizes darauf verweisen. Scheitelpunkt- und Flächenindizes beginnen bei 0. Optionale Normalen und UV-Koordinaten pro Scheitelpunkt sowie Texturteile (Flächengruppen mit eigener Textur) werden unterstützt. Punktkörper sind gültige Operanden für einfache Vollkörper: ToGenericSolid/Union/Subtract/Intersect erzeugen Vollkörper aus Punktkörpern, und `GenericSolidObject.ConvertToMesh` wandelt einen Vollkörper wieder in einen Punktkörper um. Das Neuschreiben der Flächenliste (SetFaces, SetGeometry, DeleteFace, FlipFaces) erhält die Texturteilzuordnung der Flächen, setzt aber flächenspezifische Attribute (Klasse, Füllung, Stift) auf die Standardwerte des Punktkörpers zurück.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `MeshObject(h: Handle)` | Verweist auf den vorhandenen Punktkörper `h`; vor der Verwendung `IsValid()` prüfen. |

**Methoden**

*Allgemein*

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | True, wenn `h` auf ein Objekt des von dieser Klasse dargestellten Typs verweist. |
| `GetOverallPart() -> int` *statisch* | Gibt den Gesamtteil zurück. |
| `Create(vertices: list[Point3D], faces: list[list[int]]) -> MeshObject` *statisch* | Flächen benötigen mindestens drei gültige Scheitelpunktindizes. Der Punktkörper wird auf der aktiven Ebene eingefügt. |
| `Create(vertices: list[Point3D], faces: list[MeshObject.Face]) -> MeshObject` *statisch* | Flächen benötigen mindestens drei gültige Scheitelpunktindizes. Der Punktkörper wird auf der aktiven Ebene eingefügt. |
| `CreateFromPolygons(polygons: list[list[Point3D]]) -> MeshObject` *statisch* | Jedes Polygon wird zu einer Fläche; zusammenfallende Punkte werden zu gemeinsamen Scheitelpunkten zusammengeführt. |
| `CreateFromGroup(hGroup: Handle) -> MeshObject` *statisch* | Wandelt eine Gruppe von 3D-Polygonen an Ort und Stelle um (verschachtelte Gruppen werden zuvor aufgelöst). Der Gruppenhandle wird zum Punktkörperhandle. Schlägt ohne Änderungen fehl, wenn die Gruppe andere Objekte enthält. |
| `CreateFromObject(hObject: Handle, keepOriginal: bool = True) -> MeshObject` *statisch* | Wandelt ein beliebiges 3D-Objekt (Vollkörper, Extrusionskörper, einfache Vollkörper, ...) über 3D-Polygone in einen Punktkörper um. Der Punktkörper wird unmittelbar nach dem Original platziert, das gelöscht wird, sofern keepOriginal nicht den Wert `True` hat. Ein Operand in der Bearbeitungshistorie eines einfachen Vollkörpers kann nur mit keepOriginal = `True` umgewandelt werden. |
| `GetMeshesIn(hContainer: Handle) -> list[Handle]` *statisch* | Punktkörper, die direkt in einem Container (Gruppe, Ebene, Symbol, ...) enthalten sind. |
| `GetMeshOperands(hSolid: Handle) -> list[Handle]` *statisch* | Punktkörper, die an beliebiger Stelle in der Bearbeitungshistorie eines einfachen Vollkörpers verwendet werden. |
| `Duplicate() -> MeshObject` | Dupliziert den Punktkörper in der Zeichnung und gibt die Kopie zurück. |

*Scheitelpunkte*

| Methode | Beschreibung |
|---|---|
| `GetVertexCount() -> int` | Anzahl der Scheitelpunkte. |
| `GetVertex(index: int) -> Point3D \| None` | Gibt den Scheitelpunkt bei `index` zurück. |
| `SetVertex(index: int, point: Point3D) -> bool` | Legt den Scheitelpunkt am Index `index` fest. |
| `GetVertices() -> list[Point3D]` | Gibt die Scheitelpunkte zurück. |
| `SetVertices(points: list[Point3D]) -> bool` | Legt die Scheitelpunkte fest (gleiche Scheitelpunktanzahl). |
| `HasNormals() -> bool` | Normalen und UV-Koordinaten pro Scheitelpunkt (ein Eintrag je Scheitelpunkt). |
| `GetNormals() -> list[Point3D]` | Gibt die Normalen zurück (Normalen und UV-Koordinaten pro Scheitelpunkt; ein Eintrag je Scheitelpunkt). |
| `SetNormals(normals: list[Point3D]) -> bool` | Legt die Normalen fest (Normalen und UV-Koordinaten pro Scheitelpunkt; ein Eintrag je Scheitelpunkt; beim Schreiben normiert). |
| `ClearNormals() -> bool` | Entfernt die Normalen pro Scheitelpunkt. |
| `HasUVs() -> bool` | Gibt True zurück, wenn der Punktkörper UV-Koordinaten pro Scheitelpunkt hat. |
| `GetUVs() -> list[Math.Point2D]` | Gibt die UV-Koordinaten zurück. |
| `SetUVs(uvs: list[Math.Point2D]) -> bool` | Legt die UV-Koordinaten fest. |
| `ClearUVs() -> bool` | Entfernt die UV-Koordinaten pro Scheitelpunkt (setzt auch alle Flächen auf den Gesamtteil zurück). |

*Flächen*

| Methode | Beschreibung |
|---|---|
| `GetFaceCount() -> int` | Anzahl der Flächen. |
| `GetFace(index: int) -> MeshObject.Face \| None` | Gibt die Fläche am Index `index` zurück. |
| `GetFaces() -> list[MeshObject.Face]` | Gibt die Flächen zurück. |
| `SetFaces(faces: list[MeshObject.Face]) -> bool` | Legt die Flächen fest. |
| `AddFace(vertexIndices: list[int], part: int = 0) -> bool` | Fügt eine Fläche durch die Scheitelpunkte `vertexIndices` im Texturteil `part` hinzu (die Flächenattribute bleiben erhalten). |
| `DeleteFace(index: int) -> bool` | Löscht die Fläche am Index `index`. |
| `SetGeometry(vertices: list[Point3D], faces: list[MeshObject.Face]) -> bool` | Ersetzt Scheitelpunkte und Flächen gleichzeitig (die Scheitelpunktanzahl darf sich ändern). Bei einer Änderung der Scheitelpunktanzahl werden Normalen und UV-Koordinaten gelöscht. |
| `SetFacePart(faceIndex: int, part: int) -> bool` | Legt den Texturteil der Fläche am Index `faceIndex` fest. |
| `GetFaceNormal(faceIndex: int) -> Point3D \| None` | Gibt die Flächennormale am Index `faceIndex` zurück (Newell-Normale mit Einheitslänge). |
| `GetFaceArea(faceIndex: int) -> float \| None` | Gibt den Flächeninhalt am Index `faceIndex` zurück. |
| `GetFaceCenter(faceIndex: int) -> Point3D \| None` | Gibt den Flächenmittelpunkt am Index `faceIndex` zurück (Mittelwert der Flächenscheitelpunkte). |

*Texturteile*

| Methode | Beschreibung |
|---|---|
| `GetParts() -> list[MeshObject.Part]` | Gibt die Teile zurück. |
| `AddPart(texture: int = 0) -> int \| None` | Fügt einen Texturteil hinzu (mit dem Texturindex `texture`, 0 = keine Textur); gibt den Index des neuen Teils zurück. |
| `GetPartTexture(part: int) -> int \| None` | Gibt die Textur für den Teil `part` zurück. |
| `SetPartTexture(part: int, texture: int) -> bool` | Legt die Textur des Teils fest. |

*Glättung*

| Methode | Beschreibung |
|---|---|
| `GetSmoothing() -> MeshObject.Smoothing \| None` | Gibt die Glättung zurück. |
| `SetSmoothing(smoothing: MeshObject.Smoothing) -> bool` | Legt die Glättung fest. |
| `GetCreaseAngle() -> float \| None` | Gibt den Knickwinkel zurück. |
| `SetCreaseAngle(degrees: float) -> bool` | Legt den Knickwinkel fest (0..180, wechselt zu CustomCrease). |

*Topologie*

| Methode | Beschreibung |
|---|---|
| `IsClosed() -> bool` | Gibt True zurück, wenn der Punktkörper geschlossen ist (wasserdicht: Jede Kante wird von zwei entgegengesetzt orientierten Flächen gemeinsam verwendet). |
| `FlipFaces() -> bool` | Kehrt die Umlaufrichtung und die Scheitelpunktnormalen um. |

*Operationen*

| Methode | Beschreibung |
|---|---|
| `Simplify(qualityPercent: float) -> bool` | Vereinfacht den Punktkörper an Ort und Stelle auf den Detailanteil `qualityPercent` (0 < quality < 100). |
| `Repair() -> list[Handle]` | Reparierte Punktkörper werden nach diesem Punktkörper eingefügt; dieser Punktkörper bleibt unverändert. |
| `ConvertToGroup() -> Handle` | Wandelt diesen Punktkörper an Ort und Stelle in eine Gruppe von 3D-Polygonen um; dieses Objekt wird ungültig. |
| `ToGenericSolid(keepOriginal: bool = True) -> GenericSolidObject` | Zusammenarbeit mit einfachen Vollkörpern. keepOriginal = `False` verschiebt diesen Punktkörper in die Bearbeitungshistorie des neuen Vollkörpers, sodass das Objekt anschließend auf den Operanden in der Historie verweist. |
| `Union(hTool: Handle, keepOriginal: bool = True) -> GenericSolidObject` | Vereinigung mit dem Vollkörper `hTool` als einfacher Vollkörper. Zusammenarbeit mit einfachen Vollkörpern. keepOriginal = `False` verschiebt diesen Punktkörper in die Bearbeitungshistorie des neuen Vollkörpers, sodass das Objekt anschließend auf den Operanden in der Historie verweist. |
| `Subtract(hTool: Handle, keepOriginal: bool = True) -> GenericSolidObject` | Subtrahiert den Vollkörper `hTool` und ergibt einen einfachen Vollkörper. Zusammenarbeit mit einfachen Vollkörpern. keepOriginal = `False` verschiebt diesen Punktkörper in die Bearbeitungshistorie des neuen Vollkörpers, sodass das Objekt anschließend auf den Operanden in der Historie verweist. |
| `Intersect(hTool: Handle, keepOriginal: bool = True) -> GenericSolidObject` | Schnittmenge mit dem Vollkörper `hTool` als einfacher Vollkörper. Zusammenarbeit mit einfachen Vollkörpern. keepOriginal = `False` verschiebt diesen Punktkörper in die Bearbeitungshistorie des neuen Vollkörpers, sodass das Objekt anschließend auf den Operanden in der Historie verweist. |
| `ConvertToGenericSolid(keepOriginal: bool = True) -> GenericSolidObject` | Einfacher Vollkörper ohne Bearbeitungshistorie (wie ConvertToGenericSolid); keepOriginal = `False` löscht diesen Punktkörper. |
| `Transform(transform: ExtrudeObject.Transform) -> bool` | Transformationen (Scheitelpunktnormalen werden mittransformiert; Spiegeln kehrt auch die Umlaufrichtung der Flächen um); bildet lokale Koordinaten auf das übergeordnete Koordinatensystem ab. |
| `Move3D(offset: Point3D) -> bool` | Verschiebt den Punktkörper um `offset`. Transformationen (Scheitelpunktnormalen werden mittransformiert; Spiegeln kehrt auch die Umlaufrichtung der Flächen um). |
| `Rotate3D(center: Point3D, axis: Point3D, angleDegrees: float) -> bool` | Dreht den Punktkörper um `angleDegrees` Grad um die Achse `axis` durch `center`. Transformationen (Scheitelpunktnormalen werden mittransformiert; Spiegeln kehrt auch die Umlaufrichtung der Flächen um). |
| `Scale3D(center: Point3D, factors: Point3D) -> bool` | Skaliert den Punktkörper mit `factors` (pro Achse) relativ zu `center`. Transformationen (Scheitelpunktnormalen werden mittransformiert; Spiegeln kehrt auch die Umlaufrichtung der Flächen um). |
| `GetSurfaceArea() -> float \| None` | Messungen (Welteinheiten); 3D-Begrenzungen, Mittelpunkt und Größe stammen von PrimitiveObject. |
| `GetVolume() -> float \| None` | Gibt das Volumen zurück (aussagekräftig bei geschlossenen Punktkörpern). |

Geerbt: alle Elemente von [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

#### MeshObject.Face

> **Vollständiger Name:** `api.MeshObject.Face` · **Erbt von:** `api.Object`

Teil 0 bezeichnet den gesamten, nicht texturierten Teil, siehe `GetOverallPart()`.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `Face()` | Standardwert (Felder mit ihren Standardwerten). |
| `Face(vertexIndices, part)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `vertexIndices` | `list[int]` | Indizes der Flächenscheitelpunkte. |
| `part` | `int` | Index des Texturteils der Fläche. |

#### MeshObject.Part

> **Vollständiger Name:** `api.MeshObject.Part` · **Erbt von:** `api.Object`

Texturteil: ID, Texturreferenz (0 = nicht texturiert) und Anzahl der Flächen, die ihn verwenden.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `Part()` | Standardwert (Felder mit ihren Standardwerten). |
| `Part(id, texture, faceCount)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `id` | `int` | Teil-ID. |
| `texture` | `int` | Referenz auf die Textur; 0, wenn nicht texturiert. |
| `faceCount` | `int` | Anzahl der Flächen im Teil. |

#### MeshObject.Smoothing

> **Vollständiger Name:** `api.MeshObject.Smoothing` · **Art:** `IntEnum`

Art der Glättung des Punktkörpers beim Rendern.

| Element | Wert | Beschreibung |
|---|---|---|
| `None_` | `0` |  |
| `DocumentPreference` | `1` |  |
| `CustomCrease` | `2` |  |
| `Imported` | `3` |  |

### SolidPrimitiveObject

> **Vollständiger Name:** `api.SolidPrimitiveObject` · **Erbt von:** [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Gemeinsame Basisklasse der Vectorworks-eigenen parametrischen Grundkörper (`ObjectType.Solid`): Kugeln, Halbkugeln und Kegel. Jeder Grundkörper wird als lokales Koordinatensystem (Ursprung + orthonormale I-/J-/K-Achsen) mit seinen Parametern gespeichert:

- Kugel / Halbkugel: Ursprung = Mittelpunkt, K = Aufwärtsachse (die Halbkugelkuppel zeigt entlang +K)
- Kegel: Ursprung = Grundflächenmittelpunkt, K = Achse von der Grundfläche zur Spitze

Grundkörper sind gültige Operanden für einfache Vollkörper. Rufen Sie nach der Bearbeitung eines Grundkörpers, der sich in der Bearbeitungshistorie eines einfachen Vollkörpers befindet, `GenericSolidObject.Rebuild()` am äußersten Vollkörper auf.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `SolidPrimitiveObject(h: Handle)` | Verweist auf den vorhandenen Grundkörper `h`; vor der Verwendung `IsValid()` prüfen. |

**Methoden**

*Allgemein*

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | True, wenn `h` auf ein Objekt des von dieser Klasse dargestellten Typs verweist. |
| `GetKindOf(h: Handle) -> SolidPrimitiveObject.Kind \| None` *statisch* | Gibt die Art von `h` zurück. |
| `GetPrimitivesIn(hContainer: Handle) -> list[Handle]` *statisch* | Kugel-, Halbkugel- und Kegelgrundkörper, die direkt in einem Container (Gruppe, Ebene, ...) enthalten sind |
| `GetPrimitiveOperands(hSolid: Handle) -> list[Handle]` *statisch* | Grundkörper, die an beliebiger Stelle in der Bearbeitungshistorie eines einfachen Vollkörpers verwendet werden. |
| `GetKind() -> SolidPrimitiveObject.Kind \| None` | Gibt die Art zurück. |

*Lokales Koordinatensystem*

| Methode | Beschreibung |
|---|---|
| `GetFrame() -> ExtrudeObject.Transform \| None` | Ursprung, uAxis = I, vAxis = J, wAxis = K (Einheitsvektoren). |
| `SetFrame(origin: Point3D, iAxis: Point3D, jAxis: Point3D) -> bool` | Verschiebt den Ursprung und richtet den Grundkörper neu aus. iAxis und jAxis werden orthonormalisiert, K = I x J. |
| `GetAxis() -> Point3D \| None` | Gibt die Achse zurück. |
| `SetAxis(axis: Point3D) -> bool` | Dreht den Grundkörper um seinen Ursprung, sodass K in Richtung `axis` zeigt (kürzeste Drehung). |
| `Move3D(offset: Point3D) -> bool` | Starre Transformationen und gleichmäßige Skalierungen (der Grundkörper behält seine Art bei). |
| `Rotate3D(center: Point3D, axis: Point3D, angleDegrees: float) -> bool` | Dreht um `angleDegrees` Grad um die Achse `axis` durch `center`. Starre Transformationen und gleichmäßige Skalierungen (der Grundkörper behält seine Art bei). |
| `Scale3D(center: Point3D, factor: float) -> bool` | Skaliert gleichmäßig mit dem Faktor `factor` (> 0) relativ zu `center`. Starre Transformationen und gleichmäßige Skalierungen (der Grundkörper behält seine Art bei). |
| `GetVolume() -> float \| None` | Messungen (Welteinheiten). |
| `GetSurfaceArea() -> float \| None` | Gibt den Oberflächeninhalt zurück. |
| `ToGenericSolid(keepOriginal: bool = True) -> GenericSolidObject` | Zusammenarbeit mit einfachen Vollkörpern. keepOriginal = `False` verschiebt diesen Grundkörper in die Bearbeitungshistorie des neuen Vollkörpers, sodass das Objekt anschließend auf den Operanden in der Historie verweist. |
| `Union(hTool: Handle, keepOriginal: bool = True) -> GenericSolidObject` | Vereinigung mit dem Vollkörper `hTool` als einfacher Vollkörper. Zusammenarbeit mit einfachen Vollkörpern. keepOriginal = `False` verschiebt diesen Grundkörper in die Bearbeitungshistorie des neuen Vollkörpers, sodass das Objekt anschließend auf den Operanden in der Historie verweist. |
| `Subtract(hTool: Handle, keepOriginal: bool = True) -> GenericSolidObject` | Subtrahiert den Vollkörper `hTool` und ergibt einen einfachen Vollkörper. Zusammenarbeit mit einfachen Vollkörpern. keepOriginal = `False` verschiebt diesen Grundkörper in die Bearbeitungshistorie des neuen Vollkörpers, sodass das Objekt anschließend auf den Operanden in der Historie verweist. |
| `Intersect(hTool: Handle, keepOriginal: bool = True) -> GenericSolidObject` | Schnittmenge mit dem Vollkörper `hTool` als einfacher Vollkörper. Zusammenarbeit mit einfachen Vollkörpern. keepOriginal = `False` verschiebt diesen Grundkörper in die Bearbeitungshistorie des neuen Vollkörpers, sodass das Objekt anschließend auf den Operanden in der Historie verweist. |
| `ConvertToGenericSolid(keepOriginal: bool = True) -> GenericSolidObject` | Einfacher Vollkörper ohne Bearbeitungshistorie (wie ConvertToGenericSolid); keepOriginal = `False` löscht diesen Grundkörper. |
| `ToMesh(keepOriginal: bool = True) -> MeshObject` | Zerlegt den Grundkörper in einen Punktkörper, der unmittelbar danach platziert wird. |

Geerbt: alle Elemente von [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

#### SolidPrimitiveObject.Kind

> **Vollständiger Name:** `api.SolidPrimitiveObject.Kind` · **Art:** `IntEnum`

Art eines Grundkörpers.

| Element | Wert | Beschreibung |
|---|---|---|
| `Sphere` | `0` |  |
| `Hemisphere` | `1` |  |
| `Cone` | `2` |  |

### SphereObject

> **Vollständiger Name:** `api.SphereObject` · **Erbt von:** [`SolidPrimitiveObject`](#solidprimitiveobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Vectorworks-eigene Kugel. Die Radien werden entlang der lokalen I-/J-/K-Achsen gemessen; ungleiche Radien ergeben daher ein Ellipsoid.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `SphereObject(h: Handle)` | Verweist auf die vorhandene Kugel `h`; vor der Verwendung `IsValid()` prüfen. |

**Methoden**

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | True, wenn `h` auf ein Objekt des von dieser Klasse dargestellten Typs verweist. |
| `Create(center: Point3D, radius: float) -> SphereObject` *statisch* | Erstellt eine Kugel mit dem angegebenen Mittelpunkt `center` und Radius `radius`. |
| `CreateEllipsoid(center: Point3D, radii: Point3D) -> SphereObject` *statisch* | Achsenparalleles Ellipsoid; Radien = (I-Radius, J-Radius, K-Radius). |
| `Duplicate() -> SphereObject` | Dupliziert die Kugel in der Zeichnung und gibt die Kopie zurück. |
| `GetCenter() -> Point3D \| None` | Gibt den Mittelpunkt zurück. |
| `SetCenter(center: Point3D) -> bool` | Legt den Mittelpunkt fest. |
| `GetRadius() -> float \| None` | GetRadius gibt den I-Radius zurück; SetRadius legt alle drei Radien fest. |
| `SetRadius(radius: float) -> bool` | Legt den Radius fest. GetRadius gibt den I-Radius zurück; SetRadius legt alle drei Radien fest. |
| `GetRadii() -> Point3D \| None` | Gibt die Radien zurück. |
| `SetRadii(radii: Point3D) -> bool` | Legt die Radien fest. |
| `IsEllipsoid() -> bool` | Gibt True zurück, wenn die Kugel ungleichmäßig skaliert ist (ein Ellipsoid). |

Geerbt: alle Elemente von [`SolidPrimitiveObject`](#solidprimitiveobject), [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

### HemisphereObject

> **Vollständiger Name:** `api.HemisphereObject` · **Erbt von:** [`SphereObject`](#sphereobject) → [`SolidPrimitiveObject`](#solidprimitiveobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Vectorworks-eigene Halbkugel: Die Kuppel zeigt vom Mittelpunkt entlang der lokalen K-Achse

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `HemisphereObject(h: Handle)` | Verweist auf die vorhandene Halbkugel `h`; vor der Verwendung `IsValid()` prüfen. |

**Methoden**

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | True, wenn `h` auf ein Objekt des von dieser Klasse dargestellten Typs verweist. |
| `Create(center: Point3D, topPoint: Point3D) -> HemisphereObject` *statisch* | Erstellt eine Halbkugel um `center`, deren oberster Punkt (Pol) bei `topPoint` liegt. |
| `Create(center: Point3D, radius: float) -> HemisphereObject` *statisch* | Erstellt eine aufrechte Halbkugel mit dem angegebenen Mittelpunkt `center` und Radius `radius`. |
| `Duplicate() -> HemisphereObject` | Dupliziert die Halbkugel in der Zeichnung und gibt die Kopie zurück. |
| `GetTopPoint() -> Point3D \| None` | Mittelpunkt + K * K-Radius. |
| `SetTopPoint(topPoint: Point3D) -> bool` | Richtet die Kuppel auf topPoint aus und legt einen einheitlichen Radius = \|topPoint - center\| fest. |

Geerbt: alle Mitglieder von [`SphereObject`](#sphereobject), [`SolidPrimitiveObject`](#solidprimitiveobject), [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

### ConeObject

> **Vollständiger Name:** `api.ConeObject` · **Erbt von:** [`SolidPrimitiveObject`](#solidprimitiveobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Vectorworks-eigener Kegel. Die Grundfläche ist eine Ellipse in der lokalen I-/J-Ebene um den Grundflächenmittelpunkt (Ursprung des Koordinatensystems); die Spitze wird in Objektkoordinaten gespeichert, sodass das Verschieben des Grundflächenmittelpunkts den gesamten Kegel verschiebt. Bei einem geraden Kegel liegt die Spitze auf der lokalen K-Achse; bei einem schiefen Kegel liegt sie an beliebiger Stelle oberhalb oder unterhalb der Grundflächenebene.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `ConeObject(h: Handle)` | Verweist auf den vorhandenen Kegel `h`; vor der Verwendung `IsValid()` prüfen. |

**Methoden**

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | True, wenn `h` auf ein Objekt des von dieser Klasse dargestellten Typs verweist. |
| `Create(baseCenter: Point3D, tipPoint: Point3D, radius: float) -> ConeObject` *statisch* | Erstellt einen Kegel mit einem Grundkreis vom Radius `radius` um `baseCenter` und der Spitze bei `tipPoint`. |
| `Create(baseCenter: Point3D, radius: float, height: float) -> ConeObject` *statisch* | Erstellt einen Kegel mit einem Grundkreis vom Radius `radius` um `baseCenter` und der Spitze bei `tipPoint`. |
| `Duplicate() -> ConeObject` | Dupliziert den Kegel in der Zeichnung und gibt die Kopie zurück. |
| `GetBaseCenter() -> Point3D \| None` | Gibt den Grundflächenmittelpunkt zurück. |
| `SetBaseCenter(baseCenter: Point3D) -> bool` | Legt den Grundflächenmittelpunkt fest. |
| `GetTipPoint() -> Point3D \| None` | Spitze in Weltkoordinaten. keepRight = `True` richtet den Kegel neu aus, sodass er ein gerader Kegel bleibt; `False` behält die Grundflächenebene bei und macht den Kegel bei Bedarf schief. |
| `SetTipPoint(tipPoint: Point3D, keepRight: bool = True) -> bool` | Legt den Spitzenpunkt fest. Spitze in Weltkoordinaten. keepRight = `True` richtet den Kegel neu aus, sodass er ein gerader Kegel bleibt; `False` behält die Grundflächenebene bei und macht den Kegel bei Bedarf schief. |
| `GetLocalTipPoint() -> Point3D \| None` | Spitze im lokalen Koordinatensystem (I, J, K). |
| `SetLocalTipPoint(localTipPoint: Point3D) -> bool` | Legt den lokalen Spitzenpunkt fest (Spitze im lokalen Koordinatensystem I, J, K). |
| `IsRightCone() -> bool` | Gibt True zurück, wenn die Spitze auf der Achse durch den Grundflächenmittelpunkt liegt. |
| `GetHeight() -> float \| None` | Abstand von der Grundflächenebene zur Spitze. SetHeight macht den Kegel zu einem geraden Kegel; eine negative Höhe kehrt ihn auf die andere Seite seiner Grundfläche um. |
| `SetHeight(height: float) -> bool` | Legt die Höhe fest. Abstand von der Grundflächenebene zur Spitze. SetHeight macht den Kegel zu einem geraden Kegel; eine negative Höhe kehrt ihn auf die andere Seite seiner Grundfläche um. |
| `GetRadius() -> float \| None` | GetRadius gibt den I-Radius zurück; SetRadius legt beide Grundflächenradien fest. |
| `SetRadius(radius: float) -> bool` | Legt den Radius fest. GetRadius gibt den I-Radius zurück; SetRadius legt beide Grundflächenradien fest. |
| `GetRadii() -> ConeObject.Radii \| None` | Gibt die Radien zurück. |
| `SetRadii(radii: ConeObject.Radii) -> bool` | Legt die Radien fest. |
| `IsElliptical() -> bool` | Gibt True zurück, wenn die Grundfläche eine Ellipse statt eines Kreises ist. |

Geerbt: alle Elemente von [`SolidPrimitiveObject`](#solidprimitiveobject), [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

#### ConeObject.Radii

> **Vollständiger Name:** `api.ConeObject.Radii` · **Erbt von:** `api.Object`

Grundflächenradien entlang der lokalen I- und J-Achsen.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `Radii()` | Standardwert (Felder mit ihren Standardwerten). |
| `Radii(i, j)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `i` | `float` | Grundflächenradius entlang der lokalen I-Achse. |
| `j` | `float` | Grundflächenradius entlang der lokalen J-Achse. |

### NurbsCurveObject

> **Vollständiger Name:** `api.NurbsCurveObject` · **Erbt von:** [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Vectorworks-eigene abschnittsweise definierte NURBS-Kurve. Abschnitts-, Punkt- und Knotenindizes beginnen bei 0; Koordinaten und Abstände werden in Welteinheiten angegeben. Eine Instanz bietet eine leichtgewichtige Sicht auf das Zeichnungsobjekt.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `NurbsCurveObject(h: Handle)` | Verweist auf die vorhandene NURBS-Kurve `h`; vor der Verwendung `IsValid()` prüfen. |

**Methoden**

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | True, wenn `h` auf ein Objekt des von dieser Klasse dargestellten Typs verweist. |
| `Create(points: list[Point3D], degree: int, byControlPoints: bool = True) -> NurbsCurveObject` *statisch* | Erstellt eine Kurve mit Kontrollpunkten oder Interpolationspunkten. Der erste Punkt erzeugt die Vectorworks-eigene Kurve; die übrigen Punkte werden mit der Vectorworks-Operation für NURBS-Punkte eingefügt. |
| `Duplicate() -> NurbsCurveObject` | Dupliziert die NURBS-Kurve in der Zeichnung und gibt die Kopie zurück. |
| `GetPieceCount() -> int` | Anzahl der Abschnitte. |
| `GetPointCount(pieceIndex: int = 0) -> int` | Anzahl der Punkte im Abschnitt `pieceIndex`. |
| `GetControlPointCount(pieceIndex: int = 0) -> int` | Anzahl der Kontrollpunkte im Abschnitt `pieceIndex`. |
| `GetDegree(pieceIndex: int = 0) -> int \| None` | Gibt den Grad des Abschnitts `pieceIndex` zurück. |
| `GetPoint(pieceIndex: int, pointIndex: int) -> Point3D \| None` | Gibt den Punkt für `pieceIndex`, `pointIndex` zurück. |
| `SetPoint(pieceIndex: int, pointIndex: int, point: Point3D) -> bool` | Setzt den Punkt bei `pieceIndex`. |
| `GetWeight(pieceIndex: int, controlPointIndex: int) -> float \| None` | Gibt das Gewicht für `pieceIndex`, `controlPointIndex` zurück. |
| `SetWeight(pieceIndex: int, controlPointIndex: int, weight: float) -> bool` | Legt das Gewicht im Abschnitt `pieceIndex` fest. |
| `GetKnotCount(pieceIndex: int = 0) -> int` | Anzahl der Knoten im Abschnitt `pieceIndex`. |
| `GetKnot(pieceIndex: int, knotIndex: int) -> float \| None` | Gibt den Knoten für `pieceIndex`, `knotIndex` zurück. |
| `SetKnot(pieceIndex: int, knotIndex: int, knot: float) -> bool` | Legt den Knoten im Abschnitt `pieceIndex` fest. |
| `Evaluate(pieceIndex: int, parameter: float) -> Point3D \| None` | Punkt des Abschnitts `pieceIndex` beim Parameter `parameter`. |
| `GetLength() -> float \| None` | Analyse ohne Änderungen in Weltkoordinaten, nicht mit auf den Bildschirm projizierten Abständen. Parameter sind die kurveneigenen Knotenparameter pro Abschnitt, keine normierten Bogenlängen. An einer Abschnittsverbindung wählt eine Abstandsabfrage den vorangehenden Abschnitt mit einer Länge ungleich null. |
| `GetLocationAtDistance(distance: float) -> NurbsCurveObject.Location \| None` | Gibt die Position beim Abstand `distance` zurück. |
| `GetPointAtDistance(distance: float) -> Point3D \| None` | Gibt den Punkt beim Abstand `distance` zurück. |
| `GetClosestPoint(point: Point3D) -> NurbsCurveObject.Location \| None` | Gibt den nächstgelegenen Punkt zu `point` zurück. |
| `GetDistanceTo(point: Point3D) -> float \| None` | Gibt den Abstand zu `point` zurück. |
| `GetTangent(pieceIndex: int, parameter: float) -> Point3D \| None` | Einheitstangente und nicht negative Krümmung (in inversen Welteinheiten). An Knoten wird die rechtsseitige Ableitung verwendet, außer am Abschnittsende, wo die linksseitige verwendet wird. Ein Punkt mit Geschwindigkeit null hat weder Tangente noch Krümmung und liefert `None`. |
| `GetCurvature(pieceIndex: int, parameter: float) -> float \| None` | Gibt die Krümmung für `pieceIndex`, `parameter` zurück. |
| `DivideByCount(count: int, includeEnd: bool = True) -> list[Point3D] \| None` | Genau count >= 2 Punkte mit gleichen Bogenlängenabständen. includeEnd schließt beide Endpunkte ein, auch bei einer geschlossenen Kurve; `False` lässt das Ende bzw. die Nahtstelle aus. Kein zyklisches Fortsetzen und keine Begrenzung auf den gültigen Bereich. Ungültige oder degenerierte Kurven, nicht endliche oder außerhalb des gültigen Bereichs liegende Abstände sowie Fehlschläge liefern `None`. |
| `Extend(distance: float, atStart: bool, linear: bool) -> NurbsCurveObject` | Vectorworks-eigene Operationen fügen ihre Ergebnisse auf der aktiven Ebene ein und lassen diese Kurve unverändert. |
| `Offset(distance: float) -> NurbsCurveObject` | Erstellt eine um `distance` versetzte Kurve. Vectorworks-eigene Operationen fügen ihre Ergebnisse auf der aktiven Ebene ein und lassen diese Kurve unverändert. |

Geerbt: alle Elemente von [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

#### NurbsCurveObject.Location

> **Vollständiger Name:** `api.NurbsCurveObject.Location` · **Erbt von:** `api.Object`

Kurvenpunkt und kurveneigener Parameter auf einem ab 0 indizierten Abschnitt; die Parameter sind keine Bogenlängen.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `Location()` | Standardwert (Felder mit ihren Standardwerten). |
| `Location(point, pieceIndex, parameter)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `point` | `Point3D` | Punkt auf der Kurve. |
| `pieceIndex` | `int` | Index des Kurvensegments. |
| `parameter` | `float` | Parameter auf diesem Segment. |

### NurbsSurfaceObject

> **Vollständiger Name:** `api.NurbsSurfaceObject` · **Erbt von:** [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Vectorworks-eigene NURBS-Fläche. Koordinaten des Kontrollnetzes und Abstände werden in Welteinheiten angegeben; U-/V-Punkt- und -Knotenindizes beginnen bei 0. Eine Instanz bietet eine leichtgewichtige Sicht auf das Zeichnungsobjekt.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `NurbsSurfaceObject(h: Handle)` | Verweist auf die vorhandene NURBS-Fläche `h`; vor der Verwendung `IsValid()` prüfen. |

**Methoden**

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | True, wenn `h` auf ein Objekt des von dieser Klasse dargestellten Typs verweist. |
| `Create(uPointCount: int, vPointCount: int, uDegree: int, vDegree: int) -> NurbsSurfaceObject` *statisch* | Erstellt eine NURBS-Fläche mit `uPointCount` x `vPointCount` Kontrollpunkten und den Graden `uDegree` / `vDegree`. |
| `CreateFromCurvesNetwork() -> bool` *statisch* | Verwendet die aktivierten, sich schneidenden Kurven und verbraucht sie; verwenden Sie danach keines der Ausgangsobjekte weiter. Auch die Vectorworks-Fehlerbereinigung kann Eingabeobjekte löschen. Registrieren Sie vor dem Aufruf eine Rückgängig-Aktion. |
| `Duplicate() -> NurbsSurfaceObject` | Dupliziert die NURBS-Fläche in der Zeichnung und gibt die Kopie zurück. |
| `GetUPointCount() -> int` | Anzahl der U-Punkte. |
| `GetVPointCount() -> int` | Anzahl der V-Punkte. |
| `GetUDegree() -> int \| None` | Gibt den U-Grad zurück. |
| `GetVDegree() -> int \| None` | Gibt den V-Grad zurück. |
| `GetPoint(uIndex: int, vIndex: int) -> Point3D \| None` | Gibt den Punkt für `uIndex`, `vIndex` zurück. |
| `SetPoint(uIndex: int, vIndex: int, point: Point3D) -> bool` | Setzt den Punkt bei `uIndex`. |
| `GetWeight(uIndex: int, vIndex: int) -> float \| None` | Gibt das Gewicht für `uIndex`, `vIndex` zurück. |
| `SetWeight(uIndex: int, vIndex: int, weight: float) -> bool` | Legt das Gewicht im Abschnitt `uIndex` fest. |
| `GetUKnotCount() -> int` | Anzahl der U-Knoten. |
| `GetVKnotCount() -> int` | Anzahl der V-Knoten. |
| `GetUKnot(knotIndex: int) -> float \| None` | Gibt den U-Knoten am Index `knotIndex` zurück. |
| `GetVKnot(knotIndex: int) -> float \| None` | Gibt den V-Knoten am Index `knotIndex` zurück. |
| `SetUKnot(knotIndex: int, knot: float) -> bool` | Legt den U-Knoten am Index `knotIndex` fest. |
| `SetVKnot(knotIndex: int, knot: float) -> bool` | Legt den V-Knoten am Index `knotIndex` fest. |
| `Evaluate(u: float, v: float) -> Point3D \| None` | Punkt der Fläche bei den Parametern `u`, `v`. |
| `TrimByCurve(curve: NurbsCurveObject) -> bool` | TrimNurbsSurface ordnet der Fläche die Kurve als Trimmbegrenzung zu. |
| `Extend(distance: float, atStart: bool, linear: bool, uDirection: bool) -> NurbsSurfaceObject` | Vectorworks-eigene Operationen fügen ihre Ergebnisse auf der aktiven Ebene ein und lassen diese Fläche unverändert. |
| `Offset(distance: float) -> NurbsSurfaceObject` | Erstellt eine um `distance` versetzte Fläche. Vectorworks-eigene Operationen fügen ihre Ergebnisse auf der aktiven Ebene ein und lassen diese Fläche unverändert. |

Geerbt: alle Elemente von [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

---

[Zurück zum Index](README.md) · [Nach oben](#objects3d--3d-objekte)

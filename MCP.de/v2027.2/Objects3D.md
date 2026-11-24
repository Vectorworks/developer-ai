[English](../../MCP/v2027.2/Objects3D.md) • **Deutsch** • [日本語](../../MCP.ja/v2027.2/Objects3D.md)

# Objects3D — 3D-Modellierung

> **Server:** Vectorworks MCP · **Version:** Vectorworks 2027 Update 2

[Zurück zum Inhaltsverzeichnis](README.md)

Werkzeuge zum Erstellen, Lesen und Bearbeiten von 3D-Geometrie: Volumenkörper, 3D-Polygone, Netze, NURBS-Kurven und -Flächen sowie Flächenmodelle.

## Inhaltsverzeichnis

- [Überblick](#überblick)
- [3D Modeling](#3d-modeling)
  - [createExtrude](#createextrude)
  - [createSolidPrimitive](#createsolidprimitive)
  - [createSweep](#createsweep)
  - [combineSolids](#combinesolids)
  - [createShell](#createshell)
  - [convertSolid](#convertsolid)
  - [getSolid](#getsolid)
  - [editSolid](#editsolid)
  - [create3DPolygon](#create3dpolygon)
  - [createMesh](#createmesh)
  - [createNurbsCurve](#createnurbscurve)
  - [createNurbsSurface](#createnurbssurface)
  - [createSurfaceModel](#createsurfacemodel)
  - [get3DGeometry](#get3dgeometry)
  - [edit3DGeometry](#edit3dgeometry)
  - [convertTo3D](#convertto3d)

## Überblick

Dieser Ordner enthält 1 Werkzeuggruppe mit insgesamt 16 Werkzeugen.

| Gruppe | Gruppen-ID | Standardmäßig aktiv | Risikostufe | Werkzeuge | Zusammenfassung |
|---|---|---|---|---|---|
| [3D Modeling](#3d-modeling) | `3d-modeling` | Nein | mittel | 16 | Erstellt, liest und bearbeitet Volumenkörper, 3D-Polygone, Netze, NURBS-Kurven und -Flächen sowie Flächenmodelle. |

## 3D Modeling

> **Gruppe:** `3D Modeling` · **Gruppen-ID:** `3d-modeling` · **Standardmäßig aktiv:** Nein · **Risikostufe:** mittel · **Werkzeuge:** 16

**Erstellt, liest und bearbeitet Volumenkörper, 3D-Polygone, Netze, NURBS-Kurven und -Flächen sowie Flächenmodelle.**

Erstellen, Lesen und Bearbeiten von 3D-Volumenkörpern: Extrusionskörper (aus Punkten, einem Rechteck, einer 2D-Form oder koplanaren 3D-Punkten oder zwischen zwei 3D-Punkten; mit Aussparungen und 3D-Platzierung), Mehrfach- und verjüngte Extrusionskörper (createExtrude); Kugeln, Ellipsoide, Halbkugeln, Kegel, Quader, Zylinder und Torusobjekte (createSolidPrimitive); Rotationskörper und um eine Achse gedrehte Profile (createSweep); Volumenkörper zu einem allgemeinen Volumenkörper kombinieren (combineSolids), Hüllen erstellen (createShell) und Volumenkörper in allgemeine Volumenkörper oder Netze umwandeln (convertSolid); Art, 3D-Begrenzungsrahmen, Parameter und Verlauf allgemeiner Volumenkörper auslesen (getSolid) sowie Extrusionskörper, Mehrfach-Extrusionskörper, Rotationskörper, Kugeln, Halbkugeln und Kegel verschieben, drehen, skalieren, neu ausrichten und in der Größe ändern (editSolid). 3D-Polygone und Netze: 3D-Polygone aus 3D-Punkten, 2D-Punkten oder einem Rechteck auf einer Z-Höhe erstellen (create3DPolygon) sowie Netze aus Scheitelpunkten und Flächen, Polygonen oder einer Gruppe von 3D-Polygonen erstellen (createMesh); ihre Scheitelpunkte, Flächen, Ebene, Fläche, Volumen, Glättung und Teile auslesen, wobei jede Liste seitenweise zurückgegeben wird (`limit`, `offset`, `countOnly`) (get3DGeometry); Scheitelpunkte, Flächen, Geschlossenheit, Glättung und Teile bearbeiten, vereinfachen, segmentieren, verschieben, drehen und skalieren sowie planare Volumenkörper aus 3D-Polygonen und reparierte Kopien von Netzen erstellen (edit3DGeometry); beliebige 2D- oder 3D-Objekte in eine Gruppe von 3D-Polygonen, ein Netz oder einen allgemeinen Volumenkörper umwandeln (convertTo3D).

**NURBS-Kurven und -Flächen:** Kurven aus Kontrollpunkten (mit Gewichten) oder Stützpunkten eines Grades erstellen (createNurbsCurve) und Flächen aus einem Kontrollnetz `points[u][v]` mit Graden und Gewichten erstellen (createNurbsSurface); Teilstücke, Punkte, Gewichte und Knoten auslesen und Kurven vermessen: Punkte in bestimmten Abständen, nächstgelegene Punkte, Punkte mit Tangente und Krümmung an Parametern sowie Unterteilung in gleich große Abschnitte (get3DGeometry); ihre Punkte und Gewichte festlegen, eine Fläche mit einer Kurve trimmen und erweiterte sowie versetzte Kopien beider erzeugen (edit3DGeometry; für NURBS sind `move3D`, `rotate3D`, `scale3D` und Knotenbearbeitungen nicht verfügbar). Flächenmodelle aus NURBS-Flächen: Übergänge durch Querschnitte, Schienensweeps von Querschnitten entlang einer oder zwei Schienen, Rotationen eines Profils (um dessen linke Kante oder entlang einer Schiene um eine Achse) und Extrusionen eines Profils entlang eines Pfads; das Ergebnis ist eine NURBS-Fläche, ein allgemeiner Volumenkörper oder eine Gruppe davon (createSurfaceModel). Längen werden in Welteinheiten und Winkel gegen den Uhrzeigersinn im Bogenmaß angegeben. Rahmen, Mittelpunkte und Eingabepunkte verwenden Ebenenkoordinaten; `bounds3D` verwendet die Welt-Z-Koordinate, und `layerElevation` gibt die Welt-Z-Höhe der zugehörigen Konstruktionsebene an (ohne Konstruktionsebenen-Eigentümer `null`). Neue Objekte werden normalerweise auf der aktiven Ebene angelegt; Hüllen und Umwandlungen können den Container des Quellobjekts beibehalten. Die optionale Erstellungsoption `select` legt fest, ob ein Ergebnis ausgewählt wird. Eingabeformen werden nie geändert: Die Werkzeuge kopieren sie (nicht mehr benötigte Formen anschließend mit der Aktion `delete` von editObject löschen). Jede Änderung wird als eigener benannter, rückgängig zu machender Vectorworks-Vorgang ausgeführt; ein abgewiesener Aufruf ändert nichts.

| Werkzeug | Auswirkung | Risikostufe | Zusammenfassung |
|---|---|---|---|
| [`createExtrude`](#createextrude) | Bearbeiten | mittel | Erstellt einen Extrusionskörper, Mehrfach-Extrusionskörper oder verjüngten Extrusionskörper. |
| [`createSolidPrimitive`](#createsolidprimitive) | Bearbeiten | mittel | Erstellt eine Kugel, ein Ellipsoid, eine Halbkugel, einen Kegel, Quader, Zylinder oder Torus. |
| [`createSweep`](#createsweep) | Bearbeiten | mittel | Erstellt einen Rotationskörper aus 2D-Profilen, die um eine Achse gedreht werden. |
| [`combineSolids`](#combinesolids) | Bearbeiten | mittel | Kombiniert zwei Volumenkörper durch Vereinigung, Schnitt oder Differenz zu einem allgemeinen Volumenkörper. |
| [`createShell`](#createshell) | Bearbeiten | mittel | Erstellt eine Hülle durch Aufdicken einer NURBS-Fläche oder Aushöhlen eines Volumenkörpers. |
| [`convertSolid`](#convertsolid) | Bearbeiten | mittel | Erstellt eine Kopie eines Volumenkörpers, umgewandelt in einen allgemeinen Volumenkörper oder ein Netz. |
| [`getSolid`](#getsolid) | Nur lesend | niedrig | Liest Art, 3D-Begrenzungen, Parameter und Verlauf eines Volumenkörpers aus. |
| [`editSolid`](#editsolid) | Bearbeiten | mittel | Verschiebt, dreht, skaliert, richtet einen Volumenkörper neu aus oder ändert seine Größe. |
| [`create3DPolygon`](#create3dpolygon) | Bearbeiten | mittel | Erstellt ein 3D-Polygon aus 3D-Punkten, 2D-Punkten auf einer Höhe oder einem Rechteck. |
| [`createMesh`](#createmesh) | Bearbeiten | mittel | Erstellt ein Netz aus Scheitelpunkten und Flächen, Polygonen oder einer Gruppe von 3D-Polygonen. |
| [`createNurbsCurve`](#createnurbscurve) | Bearbeiten | mittel | Erstellt eine NURBS-Kurve aus Kontrollpunkten oder Stützpunkten. |
| [`createNurbsSurface`](#createnurbssurface) | Bearbeiten | mittel | Erstellt eine NURBS-Fläche aus ihrem Kontrollnetz. |
| [`createSurfaceModel`](#createsurfacemodel) | Bearbeiten | mittel | Erstellt aus vorhandenen Objekten ein Übergangs-, Schienensweep-, Rotations- oder Pfadextrusions-Flächenmodell. |
| [`get3DGeometry`](#get3dgeometry) | Nur lesend | niedrig | Liest ein 3D-Polygon, Netz, eine NURBS-Kurve oder -Fläche aus. |
| [`edit3DGeometry`](#edit3dgeometry) | Bearbeiten | mittel | Bearbeitet ein 3D-Polygon, Netz, eine NURBS-Kurve oder -Fläche. |
| [`convertTo3D`](#convertto3d) | Bearbeiten | mittel | Wandelt eine Kopie eines Objekts in 3D-Polygone, ein Netz oder einen allgemeinen Volumenkörper um. |

### createExtrude

Erstellt einen Extrusionskörper, Mehrfach-Extrusionskörper oder verjüngten Extrusionskörper.

> **Auswirkung:** Bearbeiten · **Risikostufe:** mittel · **Rückgängig:** ein Schritt "MCP: createExtrude" · **Bei runToolBatch:** Ja

**Details**

Erstellt einen Extrusionskörper aus genau einer Profilquelle: `points` (mindestens 3 Punkte `{ x, y }`, ein geschlossenes Profil in der Ebenenfläche), `rect` { left, top, right, bottom } (die Form, die getObjectInfo unter `bounds` meldet), `profileUuid` (eine 2D-Form: Linie, Rechteck, abgerundetes Rechteck, Oval, Bogen, Polygon, Freihandpolygon oder Polylinie), `points3D` (mindestens 3 koplanare 3D-Punkte `{ x, y, z }` in Ebenenkoordinaten: Das Profil liegt in ihrer Ebene und wird entlang ihrer Normalen extrudiert) oder `profileUuids` (mindestens 2 2D-Formen in der Reihenfolge der Querschnitte: ein Mehrfach-Extrusionskörper, dessen Querschnitte gleichmäßig zwischen `baseElevation` und `baseElevation` + `thickness` verteilt werden).

`thickness` ist erforderlich (ungleich 0; eine negative Dicke extrudiert in die Gegenrichtung); `baseElevation` (Standardwert 0) gilt für `points`, `rect`, `profileUuid` und `profileUuids`. `between` { start, end, up? } (3D-Punkte) extrudiert das Profil stattdessen mit `profileUuid` oder `points` von start nach end, wobei sein Ursprung bei start liegt (die Dicke entspricht ihrem Abstand; das +Y des Profils folgt `up`, standardmäßig der Welt-Z-Achse oder bei einer vertikalen Extrusion der Welt-Y-Achse; `up` darf nicht parallel zu end - start sein); dabei sind `thickness` und `baseElevation` nicht zulässig.

`taper` { angle, height } mit `profileUuid` erstellt einen verjüngten Extrusionskörper, dessen Seiten über `height` (ungleich 0) um `angle` (Bogenmaß, |angle| &lt; pi/2) geneigt sind: eine NURBS-Fläche, ein CSG-Volumenkörper oder eine Gruppe davon (Art `surfaceModel`), ohne `thickness` oder `baseElevation`. Einzelne Extrusionskörper unterstützen `holes`: ein Array aus `{ points }` (mindestens 3 Punkte) oder `{ uuid }` (eine geschlossene 2D-Form) in den Koordinaten des Profils; wenn eine Aussparung nicht hinzugefügt werden kann, wird der Aufruf abgewiesen.

`transform` { origin, uAxis, vAxis, wAxis? } platziert eine einzelne Extrusion aus `points`, `rect` oder `profileUuid` im 3D-Raum: `origin` verwendet Ebenenkoordinaten; die lokalen Achsen sind orthonormale Einheitsvektoren (`wAxis` ist standardmäßig `uAxis x vAxis`). Über UUID angegebene Formen werden kopiert und bleiben unverändert. Alle Argumente werden überprüft, bevor etwas erstellt wird. Gibt die Objekt-Referenz, `kind` (extrude, multipleExtrude oder surfaceModel), `bounds3D` { min, max } in Welt-Z sowie `layerElevation` in Welteinheiten zurück; getSolid liest den Extrusionskörper aus.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `points` | array of [Punkt](Common.md#punkte) |  | Mindestens 3 Punkte `{ x, y }`, ein geschlossenes Profil in der Ebenenfläche. |
| `rect` | [Rechteck](Common.md#rechtecke) |  |  |
| `profileUuid` | string |  | Eine 2D-Form: Linie, Rechteck, abgerundetes Rechteck, Oval, Bogen, Polygon, Freihandpolygon oder Polylinie. |
| `points3D` | array of [3D-Punkt](Common.md#punkte) |  | Jedes Element: Ein 3D-Punkt in Ebenenkoordinaten oder ein Vektor in Welteinheiten: { x, y, z }. Punkt-Z ist relativ zur Konstruktionsebene; Vektoren sind unabhängig von der Ebenenhöhe; bounds3D verwendet Welt-Z. |
| `profileUuids` | array of string |  |  |
| `baseElevation` | number |  | Welt-Z-Wert der Basis (Standard 0). Gilt für `points`, `rect`, `profileUuid` und `profileUuids`. |
| `thickness` | number |  | Dicke in Welteinheiten. |
| `between` | object |  |  |
| `between.start` | [3D-Punkt](Common.md#punkte) | Ja | Ein 3D-Punkt in Ebenenkoordinaten oder ein Vektor in Welteinheiten: { x, y, z }. Punkt-Z ist relativ zur Konstruktionsebene; Vektoren sind unabhängig von der Ebenenhöhe; bounds3D verwendet Welt-Z. |
| `between.end` | [3D-Punkt](Common.md#punkte) | Ja | Ein 3D-Punkt in Ebenenkoordinaten oder ein Vektor in Welteinheiten: { x, y, z }. Punkt-Z ist relativ zur Konstruktionsebene; Vektoren sind unabhängig von der Ebenenhöhe; bounds3D verwendet Welt-Z. |
| `between.up` | [3D-Punkt](Common.md#punkte) |  | Ein 3D-Punkt in Ebenenkoordinaten oder ein Vektor in Welteinheiten: { x, y, z }. Punkt-Z ist relativ zur Konstruktionsebene; Vektoren sind unabhängig von der Ebenenhöhe; bounds3D verwendet Welt-Z. |
| `taper` | object |  |  |
| `taper.angle` | number | Ja |  |
| `taper.height` | number | Ja |  |
| `holes` | array of object |  |  |
| `holes[].points` | array of [Punkt](Common.md#punkte) |  |  |
| `holes[].uuid` | string |  |  |
| `transform` | object |  | 3D-Platzierung `{ origin, uAxis, vAxis, wAxis? }` eines einzelnen Extrusionskörpers aus `points`, `rect` oder `profileUuid`; nicht zulässig zusammen mit `between`, `points3D`, `profileUuids` oder `taper`. |
| `transform.origin` | [3D-Punkt](Common.md#punkte) | Ja | Ein 3D-Punkt in Ebenenkoordinaten oder ein Vektor in Welteinheiten: { x, y, z }. Punkt-Z ist relativ zur Konstruktionsebene; Vektoren sind unabhängig von der Ebenenhöhe; bounds3D verwendet Welt-Z. |
| `transform.uAxis` | [3D-Punkt](Common.md#punkte) | Ja | Ein 3D-Punkt in Ebenenkoordinaten oder ein Vektor in Welteinheiten: { x, y, z }. Punkt-Z ist relativ zur Konstruktionsebene; Vektoren sind unabhängig von der Ebenenhöhe; bounds3D verwendet Welt-Z. |
| `transform.vAxis` | [3D-Punkt](Common.md#punkte) | Ja | Ein 3D-Punkt in Ebenenkoordinaten oder ein Vektor in Welteinheiten: { x, y, z }. Punkt-Z ist relativ zur Konstruktionsebene; Vektoren sind unabhängig von der Ebenenhöhe; bounds3D verwendet Welt-Z. |
| `transform.wAxis` | [3D-Punkt](Common.md#punkte) |  | Ein 3D-Punkt in Ebenenkoordinaten oder ein Vektor in Welteinheiten: { x, y, z }. Punkt-Z ist relativ zur Konstruktionsebene; Vektoren sind unabhängig von der Ebenenhöhe; bounds3D verwendet Welt-Z. |
| `class` | string |  | Erstellungsoption: Klasse des neuen Objekts; wird angelegt, falls sie noch nicht vorhanden ist. Siehe [Optionen zur Erstellung](Common.md#optionen-zur-erstellung). |
| `name` | string |  | Erstellungsoption: Name des neuen Objekts. |
| `select` | boolean |  | Erstellungsoption: neues Objekt auswählen. |
| `useClassAttributes` | boolean |  | Erstellungsoption: mit `class` auch die Attribute des neuen Objekts anhand der Klasse festlegen. |

### createSolidPrimitive

Erstellt eine Kugel, ein Ellipsoid, eine Halbkugel, einen Kegel, Quader, Zylinder oder Torus.

> **Auswirkung:** Bearbeiten · **Risikostufe:** mittel · **Rückgängig:** ein Schritt "MCP: createSolidPrimitive" · **Bei runToolBatch:** Ja

**Details**

Erstellt einen primitiven Volumenkörper der Art `kind`: Kugel (`center` in Ebenenkoordinaten mit `radius` oder mit `radii` { x, y, z } für ein Ellipsoid mit Radien entlang der Weltachsen), Halbkugel (`center` in Ebenenkoordinaten mit `radius` für eine Kuppel in +Z-Richtung oder mit `topPoint` in Ebenenkoordinaten als Kuppelspitze), Kegel (`baseCenter` in Ebenenkoordinaten und `radius` mit `height` für einen geraden Kegel in +Z-Richtung; eine negative Höhe zeigt ihn in -Z-Richtung; alternativ mit `tipPoint` in Ebenenkoordinaten), Quader (`minimum` und `maximum`, die gegenüberliegenden Ecken: eine Extrusion), Zylinder (`baseCenter`, `radius` und `height` (ungleich 0) entlang Z: eine Extrusion eines Kreises) oder Torus (`majorRadius` &gt; `minorRadius` &gt; 0, um die Welt-Z-Achse: ein Rotationskörper).

Radien müssen positiv sein. Alle Argumente werden überprüft, bevor etwas erstellt wird. Gibt die Objekt-Referenz, `kind` entsprechend der Meldung von getSolid (sphere, hemisphere, cone; extrude bei einem Quader oder Zylinder; sweep bei einem Torus), `bounds3D` { min, max } in Welt-Z sowie `layerElevation` in Welteinheiten zurück.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `kind` | string | Ja | Einer von: `sphere`, `hemisphere`, `cone`, `box`, `cylinder`, `torus`. |
| `center` | [3D-Punkt](Common.md#punkte) |  | Ein 3D-Punkt in Ebenenkoordinaten oder ein Vektor in Welteinheiten: { x, y, z }. Punkt-Z ist relativ zur Konstruktionsebene; Vektoren sind unabhängig von der Ebenenhöhe; bounds3D verwendet Welt-Z. |
| `radius` | number |  | Radius in Welteinheiten. |
| `radii` | [3D-Punkt](Common.md#punkte) |  | Ein 3D-Punkt in Ebenenkoordinaten oder ein Vektor in Welteinheiten: { x, y, z }. Punkt-Z ist relativ zur Konstruktionsebene; Vektoren sind unabhängig von der Ebenenhöhe; bounds3D verwendet Welt-Z. |
| `topPoint` | [3D-Punkt](Common.md#punkte) |  | Ein 3D-Punkt in Ebenenkoordinaten oder ein Vektor in Welteinheiten: { x, y, z }. Punkt-Z ist relativ zur Konstruktionsebene; Vektoren sind unabhängig von der Ebenenhöhe; bounds3D verwendet Welt-Z. |
| `baseCenter` | [3D-Punkt](Common.md#punkte) |  | Ein 3D-Punkt in Ebenenkoordinaten oder ein Vektor in Welteinheiten: { x, y, z }. Punkt-Z ist relativ zur Konstruktionsebene; Vektoren sind unabhängig von der Ebenenhöhe; bounds3D verwendet Welt-Z. |
| `height` | number |  | Höhe in Welteinheiten. |
| `tipPoint` | [3D-Punkt](Common.md#punkte) |  | Ein 3D-Punkt in Ebenenkoordinaten oder ein Vektor in Welteinheiten: { x, y, z }. Punkt-Z ist relativ zur Konstruktionsebene; Vektoren sind unabhängig von der Ebenenhöhe; bounds3D verwendet Welt-Z. |
| `minimum` | [3D-Punkt](Common.md#punkte) |  | Ein 3D-Punkt in Ebenenkoordinaten oder ein Vektor in Welteinheiten: { x, y, z }. Punkt-Z ist relativ zur Konstruktionsebene; Vektoren sind unabhängig von der Ebenenhöhe; bounds3D verwendet Welt-Z. |
| `maximum` | [3D-Punkt](Common.md#punkte) |  | Ein 3D-Punkt in Ebenenkoordinaten oder ein Vektor in Welteinheiten: { x, y, z }. Punkt-Z ist relativ zur Konstruktionsebene; Vektoren sind unabhängig von der Ebenenhöhe; bounds3D verwendet Welt-Z. |
| `majorRadius` | number |  |  |
| `minorRadius` | number |  |  |
| `class` | string |  | Erstellungsoption: Klasse des neuen Objekts; wird angelegt, falls sie noch nicht vorhanden ist. Siehe [Optionen zur Erstellung](Common.md#optionen-zur-erstellung). |
| `name` | string |  | Erstellungsoption: Name des neuen Objekts. |
| `select` | boolean |  | Erstellungsoption: neues Objekt auswählen. |
| `useClassAttributes` | boolean |  | Erstellungsoption: mit `class` auch die Attribute des neuen Objekts anhand der Klasse festlegen. |

### createSweep

Erstellt einen Rotationskörper aus 2D-Profilen, die um eine Achse gedreht werden.

> **Auswirkung:** Bearbeiten · **Risikostufe:** mittel · **Rückgängig:** ein Schritt "MCP: createSweep" · **Bei runToolBatch:** Ja

**Details**

Erstellt einen Rotationskörper, also einen Volumen- oder Flächenkörper, indem Kopien der 2D-Formen `profileUuids` (mindestens 1: Linien, Rechtecke, abgerundete Rechtecke, Ovale, Bögen, Polygone, Freihandpolygone oder Polylinien) gedreht werden. Die X-Achse des Profils entspricht dem Radius und seine Y-Achse liegt entlang der Drehachse: Diese verläuft parallel zur Y-Achse durch den 2D-Ort `axisUuid` (wird kopiert) oder ohne diesen entlang der linken Kante der Profile; der neue Rotationskörper dreht sich um eine Linie parallel zur Welt-Y-Achse.

`startAngle` (Standardwert 0), `sweepAngle` (Standardwert 2*pi, eine volle Drehung; negative Werte drehen in die Gegenrichtung), `incrementAngle` (Standardwert pi/36, positiv: der Winkel jedes Segments) und `pitch` (Standardwert 0: Steigung entlang der Achse pro voller Drehung in Welteinheiten für eine Helix). Profile und Ortspunkte bleiben in Ebenenkoordinaten. Alle Argumente werden überprüft, bevor etwas erstellt wird.

Gibt die Objekt-Referenz, `kind` sweep, `bounds3D` { min, max } in Welt-Z sowie `layerElevation` in Welteinheiten zurück; editSolid ändert die Winkel und die Steigung.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `profileUuids` | array of string | Ja | Mindestens 1: Linien, Rechtecke, abgerundete Rechtecke, Ovale, Bögen, Polygone, Freihandpolygone oder Polylinien. |
| `axisUuid` | string |  |  |
| `startAngle` | number |  | Startwinkel im Bogenmaß, gegen den Uhrzeigersinn. |
| `sweepAngle` | number |  | Drehwinkel im Bogenmaß; positive Werte drehen gegen den Uhrzeigersinn. |
| `incrementAngle` | number |  | Winkel jedes Segments in Radiant: positiv; über `sweepAngle` sind höchstens 3600 Segmente zulässig (Standard `pi/36`). |
| `pitch` | number |  |  |
| `class` | string |  | Erstellungsoption: Klasse des neuen Objekts; wird angelegt, falls sie noch nicht vorhanden ist. Siehe [Optionen zur Erstellung](Common.md#optionen-zur-erstellung). |
| `name` | string |  | Erstellungsoption: Name des neuen Objekts. |
| `select` | boolean |  | Erstellungsoption: neues Objekt auswählen. |
| `useClassAttributes` | boolean |  | Erstellungsoption: mit `class` auch die Attribute des neuen Objekts anhand der Klasse festlegen. |

### combineSolids

Kombiniert zwei Volumenkörper durch Vereinigung, Schnitt oder Differenz zu einem allgemeinen Volumenkörper.

> **Auswirkung:** Bearbeiten · **Risikostufe:** mittel · **Rückgängig:** ein Schritt "MCP: combineSolids" · **Bei runToolBatch:** Ja

**Details**

Kombiniert zwei Volumenkörper anhand von `blankUuid` und `toolUuid` mit der Operation `operation` (Vereinigung, Schnitt oder Differenz). Beide Eingaben werden kopiert und bleiben unverändert; ein gesperrter Volumenkörper oder ein Volumenkörper, der sich nicht in einer Ebene, einer Symboldefinition oder einer Gruppe davon befindet, wird abgewiesen. Das Ergebnis ist ein allgemeiner Volumenkörper mit seiner booleschen Operation und seinem Verlauf; es enthält `bounds3D` { min, max } in Welt-Z sowie `layerElevation` in Welteinheiten.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `operation` | string | Ja | Einer von: `union`, `intersection`, `difference`. |
| `blankUuid` | string | Ja |  |
| `toolUuid` | string | Ja |  |
| `class` | string |  | Erstellungsoption: Klasse des neuen Objekts; wird angelegt, falls sie noch nicht vorhanden ist. Siehe [Optionen zur Erstellung](Common.md#optionen-zur-erstellung). |
| `name` | string |  | Erstellungsoption: Name des neuen Objekts. |
| `select` | boolean |  | Erstellungsoption: neues Objekt auswählen. |
| `useClassAttributes` | boolean |  | Erstellungsoption: mit `class` auch die Attribute des neuen Objekts anhand der Klasse festlegen. |

### createShell

Erstellt eine Hülle durch Aufdicken einer NURBS-Fläche oder Aushöhlen eines Volumenkörpers.

> **Auswirkung:** Bearbeiten · **Risikostufe:** mittel · **Rückgängig:** ein Schritt "MCP: createShell" · **Bei runToolBatch:** Ja

**Details**

Erstellt eine Hülle aus einer NURBS-Fläche (durch Aufdicken) oder einem Volumenkörper (durch Aushöhlen). `uuid` identifiziert die Quelle und `thickness` ist endlich, ungleich null und mit Vorzeichen versehen; bei einem Volumenkörper ist `openFaceIndices` ein nicht leeres Array mit den zu entfernenden Flächen (Indizes ab 0). Die Quelle wird kopiert und bleibt unverändert; die Hülle kann den Container der Quelle beibehalten, anstatt auf der aktiven Ebene angelegt zu werden.

Eine gesperrte Quelle oder eine Quelle, die sich nicht in einer Ebene, einer Symboldefinition oder einer Gruppe davon befindet, wird abgewiesen. Die optionale Erstellungsoption `select` legt fest, ob die Hülle ausgewählt wird. Gibt die Art shell, den Verlauf des allgemeinen Volumenkörpers, `openFaceIndices` (sofern verfügbar anhand der aktuellen Flächen der Quelle aufgelöst), `bounds3D` { min, max } in Welt-Z sowie `layerElevation` in Welteinheiten zurück.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `uuid` | string | Ja | Referenz über UUID (bevorzugt). Siehe [Objektreferenzen](Common.md#objektreferenzen). |
| `thickness` | number | Ja | Dicke in Welteinheiten. |
| `openFaceIndices` | array of integer |  | Für eine Volumenkörperquelle erforderlich: nicht leeres Array mit 0-basierten Indizes der zu entfernenden Flächen (jeder Index muss kleiner als die Flächenanzahl des Körpers sein). Für eine NURBS-Fläche nicht zulässig. |
| `class` | string |  | Erstellungsoption: Klasse des neuen Objekts; wird angelegt, falls sie noch nicht vorhanden ist. Siehe [Optionen zur Erstellung](Common.md#optionen-zur-erstellung). |
| `name` | string |  | Erstellungsoption: Name des neuen Objekts. |
| `select` | boolean |  | Erstellungsoption: neues Objekt auswählen. |
| `useClassAttributes` | boolean |  | Erstellungsoption: mit `class` auch die Attribute des neuen Objekts anhand der Klasse festlegen. |

### convertSolid

Erstellt eine Kopie eines Volumenkörpers, umgewandelt in einen allgemeinen Volumenkörper oder ein Netz.

> **Auswirkung:** Bearbeiten · **Risikostufe:** mittel · **Rückgängig:** ein Schritt "MCP: convertSolid" · **Bei runToolBatch:** Ja

**Details**

Erstellt eine Kopie des unterstützten, durch `sourceUuid` identifizierten Volumenkörpers und wandelt sie in `genericSolid` (ohne Verlauf) oder `mesh` um; die Quelle bleibt unverändert. Ein Ergebnis vom Typ allgemeiner Volumenkörper kann den Container der Quelle beibehalten, anstatt auf der aktiven Ebene angelegt zu werden; ein Volumenkörper, der sich nicht in einer Ebene, einer Symboldefinition oder einer Gruppe davon befindet, wird abgewiesen; die Umwandlung in `genericSolid` wird außerdem bei gesperrten Volumenkörpern abgewiesen.

Die optionale Erstellungsoption `select` legt fest, ob das Ergebnis ausgewählt wird. Gibt die Objekt-Referenz, die resultierende Art `kind`, `bounds3D` { min, max } in Welt-Z sowie `layerElevation` in Welteinheiten zurück; Ergebnisse vom Typ allgemeiner Volumenkörper enthalten zusätzlich ihren Verlauf.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `sourceUuid` | string | Ja |  |
| `to` | string | Ja | Einer von: `genericSolid`, `mesh`. |
| `class` | string |  | Erstellungsoption: Klasse des neuen Objekts; wird angelegt, falls sie noch nicht vorhanden ist. Siehe [Optionen zur Erstellung](Common.md#optionen-zur-erstellung). |
| `name` | string |  | Erstellungsoption: Name des neuen Objekts. |
| `select` | boolean |  | Erstellungsoption: neues Objekt auswählen. |
| `useClassAttributes` | boolean |  | Erstellungsoption: mit `class` auch die Attribute des neuen Objekts anhand der Klasse festlegen. |

### getSolid

Liest Art, 3D-Begrenzungen, Parameter und Verlauf eines Volumenkörpers aus.

> **Auswirkung:** Nur lesend · **Risikostufe:** niedrig · **Rückgängig:** keiner · **Bei runToolBatch:** Zulässig

**Details**

Liest einen Volumenkörper anhand von UUID, Name oder Index aus: die Objekt-Referenz, seine Art `kind` (extrude, multipleExtrude, sweep, sphere, hemisphere, cone, genericSolid oder shell), `bounds3D` { min, max } in Welt-Z, `layerElevation` in Welteinheiten (`null` ohne Konstruktionsebenen-Eigentümer) und die Werte seiner Art. Rahmen, Mittelpunkte und Punkte bleiben in Ebenenkoordinaten; Eingaben und Geometrie werden nicht zwischen Koordinatensystemen umgewandelt. extrude: `baseElevation`, `thickness`, `topElevation`, `transform` { origin, uAxis, vAxis, wAxis }, `volume`, `profileBounds` (2D, in Profilkoordinaten), `holeCount` und `holes` [{ index, bounds }]. multipleExtrude: `baseElevation`, `thickness`, `topElevation` und `profileCount`. sweep: `startAngle`, `sweepAngle`, `incrementAngle`, `pitch` und `profileCount` (ohne Achsenort). sphere und hemisphere: `center`, `radii` { x, y, z } (entlang der lokalen Achsen), `isEllipsoid`, `frame` { origin, uAxis, vAxis, wAxis }, `axis` (lokale Z-Achse; die Kuppel einer Halbkugel zeigt in diese Richtung), `volume` und `surfaceArea`; hemisphere enthält zusätzlich `topPoint`. cone: `baseCenter`, `tipPoint`, `height`, `radii` { i, j }, `isRightCone`, `isElliptical`, `frame`, `axis` (von der Basis zur Spitze), analytisches `volume` und `surfaceArea`; die Fläche eines asymmetrischen Kegels wird anhand des vorhandenen polygonalen Caches näherungsweise für die geschlossene Oberfläche berechnet und weggelassen, falls sie nicht verfügbar ist; bei geraden Kreiskegeln wird die analytische Mantelfläche ausgegeben.

**Allgemeine Volumenkörper und Hüllen:** `hasHistory`, `operation` (sofern bekannt), `volume`, `surfaceArea` und Verlaufseinträge mit Objekt-Referenzen, Verschachtelungstiefe, Operandenindex, übergeordneter UUID und verschachtelter Operation; Hüllen melden außerdem `thickness`, `openFaceIndices` (aktuelle Quellindizes, wobei persistente Flächennamen aufgelöst werden) und `sourceUuid`, sofern verfügbar. Volumen und Flächen werden in Welteinheiten angegeben; Werte, die Vectorworks nicht melden kann, werden ausgelassen.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `uuid` | string |  | Referenz über UUID (bevorzugt). Siehe [Objektreferenzen](Common.md#objektreferenzen). |
| `name` | string |  | Referenz über Namen. |
| `index` | integer |  | Referenz über internen Index. |

### editSolid

Verschiebt, dreht, skaliert, richtet einen Volumenkörper neu aus oder ändert seine Größe.

> **Auswirkung:** Bearbeiten · **Risikostufe:** mittel · **Rückgängig:** ein Schritt "MCP: editSolid" · **Bei runToolBatch:** Ja

**Details**

Bearbeitet einen unterstützten Volumenkörper anhand von UUID, Name oder Index; der Aufruf ist ein einzelner Rückgängig-Schritt. Abgewiesen, ohne Änderungen: ein Objekt, das getSolid nicht unterstützt, ein allgemeiner Volumenkörper oder eine Hülle (getSolid liest deren Verlauf, editSolid bearbeitet sie jedoch nicht), ein gesperrter Volumenkörper (zuerst mit editObject `locked` false entsperren), ein Volumenkörper, der sich nicht in einer Ebene, einer Symboldefinition oder einer Gruppe davon befindet (z. B. ein Operand eines allgemeinen Volumenkörpers oder ein Objekt in einer Wand, einem Plug-in-Objekt oder einem Ansichtsbereich), eine für die jeweilige Art nicht unterstützte Operation, ein ungültiger Wert oder ein Aufruf ohne Änderungen.

Die Operationen werden in dieser Reihenfolge angewendet: `transform` { origin, uAxis, vAxis, wAxis? } (orthonormal; Kugeln, Halbkugeln und Kegel benötigen ein rechtshändiges Koordinatensystem), `move3D` { offset } und `rotate3D` { center, axis, angle } (Bogenmaß, rechtshändig um die Achse) für Extrusionskörper, Kugeln, Halbkugeln und Kegel; `scale3D` { center, factor &gt; 0 } und `axis` (dreht die lokale Z-Achse in diese Richtung) für Kugeln, Halbkugeln und Kegel; `baseElevation`, `thickness` und `topElevation` (legt die Dicke fest; nicht zusammen mit `thickness`) für Extrusions- und Mehrfach-Extrusionskörper; bei Extrusionskörpern `removeHoles` (Indizes aus getSolid `holes`) oder `removeAllHoles` true, danach `addHoles` (wie `holes` bei createExtrude); Kugel und Halbkugel: `center`, danach `radius` oder `radii` { x, y, z }; Halbkugel: `topPoint` (dreht die Kuppel dorthin und legt den Radius auf ihren Abstand fest); Kegel: `baseCenter` (verschiebt den Kegel), `tipPoint` mit `keepRight` (Standardwert true: Der Kegel wird so gedreht, dass er gerade bleibt; false behält die Basisebene bei und erzeugt einen schiefen Kegel), `height` (erstellt einen geraden Kegel; ein negativer Wert kehrt ihn um), `radius` oder `radii` { i, j }; Rotationskörper: `startAngle`, `sweepAngle`, `incrementAngle` und `pitch`.

Gibt die Objekt-Referenz, `changed` (die angewendeten Argumente in Reihenfolge) und die getSolid-Werte nach der Änderung zurück.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `uuid` | string |  | Referenz über UUID (bevorzugt). Siehe [Objektreferenzen](Common.md#objektreferenzen). |
| `name` | string |  | Referenz über Namen. |
| `index` | integer |  | Referenz über internen Index. |
| `transform` | object |  |  |
| `transform.origin` | [3D-Punkt](Common.md#punkte) | Ja | Ein 3D-Punkt in Ebenenkoordinaten oder ein Vektor in Welteinheiten: { x, y, z }. Punkt-Z ist relativ zur Konstruktionsebene; Vektoren sind unabhängig von der Ebenenhöhe; bounds3D verwendet Welt-Z. |
| `transform.uAxis` | [3D-Punkt](Common.md#punkte) | Ja | Ein 3D-Punkt in Ebenenkoordinaten oder ein Vektor in Welteinheiten: { x, y, z }. Punkt-Z ist relativ zur Konstruktionsebene; Vektoren sind unabhängig von der Ebenenhöhe; bounds3D verwendet Welt-Z. |
| `transform.vAxis` | [3D-Punkt](Common.md#punkte) | Ja | Ein 3D-Punkt in Ebenenkoordinaten oder ein Vektor in Welteinheiten: { x, y, z }. Punkt-Z ist relativ zur Konstruktionsebene; Vektoren sind unabhängig von der Ebenenhöhe; bounds3D verwendet Welt-Z. |
| `transform.wAxis` | [3D-Punkt](Common.md#punkte) |  | Ein 3D-Punkt in Ebenenkoordinaten oder ein Vektor in Welteinheiten: { x, y, z }. Punkt-Z ist relativ zur Konstruktionsebene; Vektoren sind unabhängig von der Ebenenhöhe; bounds3D verwendet Welt-Z. |
| `move3D` | object |  |  |
| `move3D.offset` | [3D-Punkt](Common.md#punkte) | Ja | Ein 3D-Punkt in Ebenenkoordinaten oder ein Vektor in Welteinheiten: { x, y, z }. Punkt-Z ist relativ zur Konstruktionsebene; Vektoren sind unabhängig von der Ebenenhöhe; bounds3D verwendet Welt-Z. |
| `rotate3D` | object |  |  |
| `rotate3D.center` | [3D-Punkt](Common.md#punkte) | Ja | Ein 3D-Punkt in Ebenenkoordinaten oder ein Vektor in Welteinheiten: { x, y, z }. Punkt-Z ist relativ zur Konstruktionsebene; Vektoren sind unabhängig von der Ebenenhöhe; bounds3D verwendet Welt-Z. |
| `rotate3D.axis` | [3D-Punkt](Common.md#punkte) | Ja | Ein 3D-Punkt in Ebenenkoordinaten oder ein Vektor in Welteinheiten: { x, y, z }. Punkt-Z ist relativ zur Konstruktionsebene; Vektoren sind unabhängig von der Ebenenhöhe; bounds3D verwendet Welt-Z. |
| `rotate3D.angle` | number | Ja |  |
| `scale3D` | object |  |  |
| `scale3D.center` | [3D-Punkt](Common.md#punkte) | Ja | Ein 3D-Punkt in Ebenenkoordinaten oder ein Vektor in Welteinheiten: { x, y, z }. Punkt-Z ist relativ zur Konstruktionsebene; Vektoren sind unabhängig von der Ebenenhöhe; bounds3D verwendet Welt-Z. |
| `scale3D.factor` | number | Ja |  |
| `axis` | [3D-Punkt](Common.md#punkte) |  | Ein 3D-Punkt in Ebenenkoordinaten oder ein Vektor in Welteinheiten: { x, y, z }. Punkt-Z ist relativ zur Konstruktionsebene; Vektoren sind unabhängig von der Ebenenhöhe; bounds3D verwendet Welt-Z. |
| `baseElevation` | number |  | Welt-Z-Wert der Basis, bei einer Extrusion oder Mehrfachextrusion. |
| `thickness` | number |  | Dicke in Welteinheiten. |
| `topElevation` | number |  | Legt die Dicke fest; nicht zusammen mit `thickness`. |
| `removeHoles` | array of integer |  | Indizes aus getSolid `holes`. |
| `removeAllHoles` | boolean |  |  |
| `addHoles` | array of object |  | Wie `holes` bei createExtrude. |
| `addHoles[].points` | array of [Punkt](Common.md#punkte) |  |  |
| `addHoles[].uuid` | string |  |  |
| `center` | [3D-Punkt](Common.md#punkte) |  | Ein 3D-Punkt in Ebenenkoordinaten oder ein Vektor in Welteinheiten: { x, y, z }. Punkt-Z ist relativ zur Konstruktionsebene; Vektoren sind unabhängig von der Ebenenhöhe; bounds3D verwendet Welt-Z. |
| `radius` | number |  | Radius in Welteinheiten. |
| `radii` | object |  | Kugel und Halbkugel: { x, y, z }; Kegel: { i, j }. |
| `radii.x` | number |  |  |
| `radii.y` | number |  |  |
| `radii.z` | number |  |  |
| `radii.i` | number |  |  |
| `radii.j` | number |  |  |
| `topPoint` | [3D-Punkt](Common.md#punkte) |  | Ein 3D-Punkt in Ebenenkoordinaten oder ein Vektor in Welteinheiten: { x, y, z }. Punkt-Z ist relativ zur Konstruktionsebene; Vektoren sind unabhängig von der Ebenenhöhe; bounds3D verwendet Welt-Z. |
| `baseCenter` | [3D-Punkt](Common.md#punkte) |  | Ein 3D-Punkt in Ebenenkoordinaten oder ein Vektor in Welteinheiten: { x, y, z }. Punkt-Z ist relativ zur Konstruktionsebene; Vektoren sind unabhängig von der Ebenenhöhe; bounds3D verwendet Welt-Z. |
| `tipPoint` | [3D-Punkt](Common.md#punkte) |  | Ein 3D-Punkt in Ebenenkoordinaten oder ein Vektor in Welteinheiten: { x, y, z }. Punkt-Z ist relativ zur Konstruktionsebene; Vektoren sind unabhängig von der Ebenenhöhe; bounds3D verwendet Welt-Z. |
| `keepRight` | boolean |  | Kegel mit `tipPoint`: Standard `true`, der Kegel wird so gedreht, dass er ein gerader Kegel bleibt; `false` erhält die Basisebene (schiefer Kegel). Bewirkt für sich allein keine Bearbeitung. |
| `height` | number |  | Erstellt einen geraden Kegel; ein negativer Wert kehrt ihn um. |
| `startAngle` | number |  | Startwinkel im Bogenmaß, gegen den Uhrzeigersinn. |
| `sweepAngle` | number |  | Drehwinkel im Bogenmaß; positive Werte drehen gegen den Uhrzeigersinn. |
| `incrementAngle` | number |  | Winkel jedes Segments in Radiant: positiv; über `sweepAngle` sind höchstens 3600 Segmente zulässig. |
| `pitch` | number |  |  |

### create3DPolygon

Erstellt ein 3D-Polygon aus 3D-Punkten, 2D-Punkten auf einer Höhe oder einem Rechteck.

> **Auswirkung:** Bearbeiten · **Risikostufe:** mittel · **Rückgängig:** ein Schritt "MCP: create3DPolygon" · **Bei runToolBatch:** Ja

**Details**

Erstellt ein 3D-Polygon aus genau einer Quelle: `points` (2 bis 32767 3D-Punkte `{ x, y, z }` in Ebenenkoordinaten, Z relativ zur Konstruktionsebene), `points2D` (2 bis 32767 Punkte `{ x, y }` in der Ebene bei `z`, standardmäßig 0, relativ zur Konstruktionsebene) oder `rect` { left, top, right, bottom } (die Form, die getObjectInfo unter `bounds` meldet) bei `z`. `closed` (Standardwert true) gilt für `points` und `points2D`; ein Rechteck ist immer geschlossen, und `z` gilt nicht für `points`.

Alle Argumente werden überprüft, bevor etwas erstellt wird; das Polygon wird auf der aktiven Ebene angelegt. Gibt die Objekt-Referenz, `kind` polygon3D, `vertexCount`, `closed`, `bounds3D` { min, max } in Welt-Z sowie `layerElevation` (Welt-Z-Höhe der zugehörigen Konstruktionsebene, ohne Konstruktionsebenen-Eigentümer `null`) zurück; get3DGeometry liest das Polygon aus und edit3DGeometry bearbeitet es.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `points` | array of [3D-Punkt](Common.md#punkte) |  | Jedes Element: Ein 3D-Punkt in Ebenenkoordinaten oder ein Vektor in Welteinheiten: { x, y, z }. Punkt-Z ist relativ zur Konstruktionsebene; Vektoren sind unabhängig von der Ebenenhöhe; bounds3D verwendet Welt-Z. |
| `points2D` | array of [Punkt](Common.md#punkte) |  | 2 bis 32767 Punkte { x, y } in der Ebene bei `z`, standardmäßig 0, relativ zur Konstruktionsebene. |
| `rect` | [Rechteck](Common.md#rechtecke) |  |  |
| `z` | number |  | Z-Wert (Höhe) in Welteinheiten. |
| `closed` | boolean |  | Gibt an, ob die Form geschlossen ist. |
| `class` | string |  | Erstellungsoption: Klasse des neuen Objekts; wird angelegt, falls sie noch nicht vorhanden ist. Siehe [Optionen zur Erstellung](Common.md#optionen-zur-erstellung). |
| `name` | string |  | Erstellungsoption: Name des neuen Objekts. |
| `select` | boolean |  | Erstellungsoption: neues Objekt auswählen. |
| `useClassAttributes` | boolean |  | Erstellungsoption: mit `class` auch die Attribute des neuen Objekts anhand der Klasse festlegen. |

### createMesh

Erstellt ein Netz aus Scheitelpunkten und Flächen, Polygonen oder einer Gruppe von 3D-Polygonen.

> **Auswirkung:** Bearbeiten · **Risikostufe:** mittel · **Rückgängig:** ein Schritt "MCP: createMesh" · **Bei runToolBatch:** Ja

**Details**

Erstellt ein Netz aus genau einer Quelle: `vertices` (mindestens 3 3D-Punkte `{ x, y, z }` in Ebenenkoordinaten, Z relativ zur Konstruktionsebene) mit `faces` (ein Array von Flächen, jede ein Array aus mindestens 3 Indizes ab 0 in `vertices`, von außen gegen den Uhrzeigersinn betrachtet), `polygons` (ein Array aus Polygonen, jeweils mindestens 3 3D-Punkte in Ebenenkoordinaten; zusammenfallende Punkte werden zu gemeinsamen Scheitelpunkten verbunden) oder `groupUuid` (eine Gruppe, die ausschließlich 3D-Polygone und Gruppen davon enthält, z. B. das Ergebnis `polygons` von convertTo3D: Das Netz wird aus einer Kopie erstellt und direkt nach der Gruppe platziert; die Gruppe bleibt bestehen).

Eine gesperrte Gruppe oder eine Gruppe, die sich nicht in einer Ebene, einer Symboldefinition oder einer Gruppe davon befindet, wird abgewiesen. Alle Argumente werden überprüft, bevor etwas erstellt wird; Netze aus Scheitelpunkten oder Polygonen werden auf der aktiven Ebene angelegt. Gibt die Objekt-Referenz, `kind` mesh, `vertexCount`, `faceCount`, `isClosed` (wasserdicht), `bounds3D` { min, max } in Welt-Z sowie `layerElevation` in Welteinheiten zurück.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `vertices` | array of [3D-Punkt](Common.md#punkte) |  | Jedes Element: Ein 3D-Punkt in Ebenenkoordinaten oder ein Vektor in Welteinheiten: { x, y, z }. Punkt-Z ist relativ zur Konstruktionsebene; Vektoren sind unabhängig von der Ebenenhöhe; bounds3D verwendet Welt-Z. |
| `faces` | array of array of integer |  | Ein Array von Flächen, jede ein Array aus mindestens 3 Indizes ab 0 in `vertices`, von außen gegen den Uhrzeigersinn betrachtet. |
| `polygons` | array of array of [3D-Punkt](Common.md#punkte) |  | Ein Array von Polygonen, jeweils mindestens 3 3D-Punkte in Ebenenkoordinaten; zusammenfallende Punkte werden zu gemeinsamen Scheitelpunkten verbunden. |
| `groupUuid` | string |  |  |
| `class` | string |  | Erstellungsoption: Klasse des neuen Objekts; wird angelegt, falls sie noch nicht vorhanden ist. Siehe [Optionen zur Erstellung](Common.md#optionen-zur-erstellung). |
| `name` | string |  | Erstellungsoption: Name des neuen Objekts. |
| `select` | boolean |  | Erstellungsoption: neues Objekt auswählen. |
| `useClassAttributes` | boolean |  | Erstellungsoption: mit `class` auch die Attribute des neuen Objekts anhand der Klasse festlegen. |

### createNurbsCurve

Erstellt eine NURBS-Kurve aus Kontrollpunkten oder Stützpunkten.

> **Auswirkung:** Bearbeiten · **Risikostufe:** mittel · **Rückgängig:** ein Schritt "MCP: createNurbsCurve" · **Bei runToolBatch:** Ja

**Details**

Erstellt eine NURBS-Kurve aus `points` (3D-Punkte `{ x, y, z }` in Ebenenkoordinaten, Z relativ zur Konstruktionsebene: 2 bis 1000 oder bis 998 bei einer Kurve mit Stützpunkten und Grad 2 oder höher, da Vectorworks 2 Kontrollpunkte mehr als Stützpunkte verwendet): `pointKind` control (Standardwert: Die Punkte sind Kontrollpunkte, denen die Kurve folgt, ohne durch alle Punkte zu verlaufen) oder fit (die Kurve verläuft durch jeden Punkt); `degree` (Ganzzahl von 1 bis 28, Standardwert 3; eine Kurve mit Kontrollpunkten und Grad d benötigt mindestens d + 1 Punkte); `weights` (nur Kontrollpunkte: ein Gewicht von 0.0001 bis 100 je Punkt; ein höheres Gewicht zieht die Kurve stärker zum jeweiligen Punkt).

Alle Argumente werden überprüft, bevor etwas erstellt wird; die Kurve wird auf der aktiven Ebene angelegt. Gibt die Objekt-Referenz, `kind` nurbsCurve, `pieceCount`, `degree`, `pointCount` und `controlPointCount` (des ersten Teilstücks), `length` (bei Nichtverfügbarkeit `null`), `bounds3D` { min, max } in Welt-Z sowie `layerElevation` (Welt-Z-Höhe der zugehörigen Konstruktionsebene, ohne Konstruktionsebenen-Eigentümer `null`) zurück; get3DGeometry liest und vermisst die Kurve und edit3DGeometry bearbeitet sie.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `points` | array of [3D-Punkt](Common.md#punkte) | Ja | Jedes Element: Ein 3D-Punkt in Ebenenkoordinaten oder ein Vektor in Welteinheiten: { x, y, z }. Punkt-Z ist relativ zur Konstruktionsebene; Vektoren sind unabhängig von der Ebenenhöhe; bounds3D verwendet Welt-Z. |
| `pointKind` | string |  | Einer von: `control`, `fit`. |
| `degree` | integer |  | Ganzzahl von 1 bis 28, Standardwert 3; eine Kurve mit Kontrollpunkten und Grad d benötigt mindestens d + 1 Punkte. |
| `weights` | array of number |  | Nur Kontrollpunkte: ein Gewicht von 0.0001 bis 100 je Punkt; ein höheres Gewicht zieht die Kurve stärker zum jeweiligen Punkt. |
| `class` | string |  | Erstellungsoption: Klasse des neuen Objekts; wird angelegt, falls sie noch nicht vorhanden ist. Siehe [Optionen zur Erstellung](Common.md#optionen-zur-erstellung). |
| `name` | string |  | Erstellungsoption: Name des neuen Objekts. |
| `select` | boolean |  | Erstellungsoption: neues Objekt auswählen. |
| `useClassAttributes` | boolean |  | Erstellungsoption: mit `class` auch die Attribute des neuen Objekts anhand der Klasse festlegen. |

### createNurbsSurface

Erstellt eine NURBS-Fläche aus ihrem Kontrollnetz.

> **Auswirkung:** Bearbeiten · **Risikostufe:** mittel · **Rückgängig:** ein Schritt "MCP: createNurbsSurface" · **Bei runToolBatch:** Ja

**Details**

Erstellt eine NURBS-Fläche aus dem Kontrollnetz `points`: ein Array mit mindestens 2 Zeilen, von denen jede ein Array mit mindestens 2 3D-Punkten `{ x, y, z }` in Ebenenkoordinaten enthält (Z relativ zur Konstruktionsebene); alle Zeilen sind gleich lang. `points[u][v]` ist der Punkt v der Zeile u (höchstens 32767 Zeilen und Punkte je Zeile). `uDegree` und `vDegree`: Ganzzahlen von 1 bis 28; bei n Punkten in einer Richtung ist ein Grad bis n - 1 möglich, standardmäßig der kleinere Wert aus 3 und n - 1.

`weights` (optional, in derselben Form wie `points`: ein Gewicht von 0.0001 bis 100 je Kontrollpunkt). Alle Argumente werden überprüft, bevor etwas erstellt wird; die Fläche wird auf der aktiven Ebene angelegt. Gibt die Objekt-Referenz, `kind` nurbsSurface, `uPointCount`, `vPointCount`, `uDegree`, `vDegree`, `bounds3D` { min, max } in Welt-Z sowie `layerElevation` in Welteinheiten zurück; get3DGeometry liest die Fläche aus und edit3DGeometry bearbeitet sie.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `points` | array of array of [3D-Punkt](Common.md#punkte) | Ja | Die Punkte in Reihenfolge. |
| `uDegree` | integer |  |  |
| `vDegree` | integer |  |  |
| `weights` | array of array of number |  |  |
| `class` | string |  | Erstellungsoption: Klasse des neuen Objekts; wird angelegt, falls sie noch nicht vorhanden ist. Siehe [Optionen zur Erstellung](Common.md#optionen-zur-erstellung). |
| `name` | string |  | Erstellungsoption: Name des neuen Objekts. |
| `select` | boolean |  | Erstellungsoption: neues Objekt auswählen. |
| `useClassAttributes` | boolean |  | Erstellungsoption: mit `class` auch die Attribute des neuen Objekts anhand der Klasse festlegen. |

### createSurfaceModel

Erstellt aus vorhandenen Objekten ein Übergangs-, Schienensweep-, Rotations- oder Pfadextrusions-Flächenmodell.

> **Auswirkung:** Bearbeiten · **Risikostufe:** mittel · **Rückgängig:** ein Schritt "MCP: createSurfaceModel" · **Bei runToolBatch:** Ja

**Details**

Erstellt ein Flächenmodell der Art `kind` aus Kopien vorhandener Objekte, die unverändert bleiben: Übergang: NURBS-Flächen durch `sectionUuids` (mindestens 2 Querschnitte in Reihenfolge, jeweils eine NURBS-Kurve oder ein 3D-Ort, mindestens einer davon eine Kurve), `ruled` (Standardwert false: glatt; true: gerade zwischen benachbarten Querschnitten; bei zwei Querschnitten entsteht immer ein geradliniger Übergang) und `closed` (Standardwert false; true erstellt den Übergang vom letzten Querschnitt zum ersten, daher müssen die mindestens 3 Querschnitte eine Schleife bilden, z. B. um eine Achse: in einer Reihe angeordnete Querschnitte führen dazu, dass der Abschluss den Übergang kreuzt und Vectorworks keinen Übergang erstellt); railSweep: `sectionUuids` (mindestens 1 NURBS-Kurve), die entlang der NURBS-Kurve `railUuid` und optional der zweiten Schiene `secondRailUuid` geführt werden.

**Übergang und railSweep:** `solid` (Standardwert false: offene Flächenenden; true: Endkappen, außer bei einem geschlossenen Übergang, und Zusammenfügen zu einem allgemeinen Volumenkörper; die Querschnitte müssen geschlossene Kurven sein und das Ergebnis muss geschlossen sein, andernfalls wird nichts erstellt). revolve: Die 2D-Form `profileUuid` (Linie, Rechteck, abgerundetes Rechteck, Oval, Bogen, Polygon, Freihandpolygon oder Polylinie) wird wie ein Profil in createSweep ohne `axisUuid` gedreht (die X-Achse des Profils entspricht dem Radius und seine Y-Achse liegt entlang der Achse, der linken Profilkante parallel zur Welt-Y-Achse) mit `startAngle` (Standardwert 0), `sweepAngle` (Standardwert 2*pi), `incrementAngle` (Standardwert pi/36) und `pitch` (Standardwert 0) von createSweep: Die Form und Platzierung entsprechen dem dortigen Rotationskörper, bestehen hier jedoch aus NURBS-Flächen; oder mit `railUuid` und dem erforderlichen `axisUuid` (Profil, Schiene und Achse sind jeweils eine 2D-Form, NURBS-Kurve oder ein 3D-Polygon; keine Winkel oder Steigung): Das Profil wird entlang der Schiene um die Achse gedreht. Die Achse muss gerade sein, das Profil muss zusammen mit der Achse in einer Ebene liegen, ohne sie zu kreuzen, und die Schiene muss diese Ebene verlassen (eine ebene Schiene liegt in einer dazu senkrechten Ebene). extrudeAlongPath: `profileUuid` (eine ebene 2D-Form, NURBS-Kurve oder ein 3D-Polygon, das sich nicht selbst kreuzt), die entlang der NURBS-Kurve `pathUuid` geführt wird, mit `scale` (größer als 0, Standardwert 1; bei der standardmäßigen linearen Skalierung bleibt die Profilgröße bei 1 unverändert), `exponentialScale` (Standardwert false: Das Profil wird entlang des Pfads linear skaliert; true: exponentiell), `lockProfilePlane` (Standardwert false; true führt die Extrusion mit einer festen Richtung aus, der Z-Achse, nachdem Vectorworks den Pfad in die XY-Ebene transformiert hat, sodass das Profil seine Ausrichtung beibehält), `fixProfile` (Standardwert false; true führt das Profil an seiner gezeichneten Position entlang, anstatt es zum Pfadanfang zu drehen; dann darf der Pfad nicht parallel zur Profilebene beginnen); bei geschlossenen Pfaden oder Pfaden mit Ecken funktioniert nur `scale` 1 ohne `exponentialScale`. Argumente einer anderen Art sowie die Verwendung desselben Objekts für zwei Eingaben werden abgewiesen. Alle Argumente werden überprüft, bevor etwas erstellt wird; das Ergebnis wird auf der aktiven Ebene angelegt. Gibt die Objekt-Referenz, `kind` (nurbsSurface; genericSolid, wenn Vectorworks aus einer zusammengesetzten Fläche einen Volumenkörper erstellt; group für mehrere Ergebnisse mit `members` [{ reference, kind }]), `bounds3D` { min, max } in Welt-Z zurück (bei NURBS-Flächen die Box aller Kontrollpunkte von Vectorworks, die auch bei getrimmten Flächen größer als die Fläche sein kann) sowie `layerElevation` in Welteinheiten; get3DGeometry liest NURBS-Flächen aus und getSolid liest allgemeine Volumenkörper aus.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `kind` | string | Ja | Einer von: `loft`, `railSweep`, `revolve`, `extrudeAlongPath`. |
| `sectionUuids` | array of string |  | Mindestens 2 Querschnitte in Reihenfolge, jeweils eine NURBS-Kurve oder ein 3D-Ort, mindestens einer davon eine Kurve. |
| `ruled` | boolean |  |  |
| `closed` | boolean |  | Gibt an, ob die Form geschlossen ist. |
| `solid` | boolean |  |  |
| `railUuid` | string |  | Bei `railSweep`: eine NURBS-Kurve; bei `revolve`: eine 2D-Form, NURBS-Kurve oder ein 3D-Polygon (mit `axisUuid`). |
| `secondRailUuid` | string |  | Nur für `railSweep`: zweite NURBS-Kurvenschiene. |
| `profileUuid` | string |  | Linie, Rechteck, abgerundetes Rechteck, Oval, Bogen, Polygon, Freihandpolygon oder Polylinie. |
| `axisUuid` | string |  |  |
| `startAngle` | number |  | Startwinkel im Bogenmaß, gegen den Uhrzeigersinn. |
| `sweepAngle` | number |  | Drehwinkel im Bogenmaß; positive Werte drehen gegen den Uhrzeigersinn. |
| `incrementAngle` | number |  | Winkel jedes Segments in Radiant: positiv; über `sweepAngle` sind höchstens 3600 Segmente zulässig (Standard `pi/36`). |
| `pitch` | number |  |  |
| `pathUuid` | string |  | UUID des Objekts, das den Pfad vorgibt. |
| `scale` | number |  | Größer als 0, Standardwert 1; bei der standardmäßigen linearen Skalierung bleibt die Profilgröße bei 1 unverändert. |
| `exponentialScale` | boolean |  |  |
| `lockProfilePlane` | boolean |  |  |
| `fixProfile` | boolean |  |  |
| `class` | string |  | Erstellungsoption: Klasse des neuen Objekts; wird angelegt, falls sie noch nicht vorhanden ist. Siehe [Optionen zur Erstellung](Common.md#optionen-zur-erstellung). |
| `name` | string |  | Erstellungsoption: Name des neuen Objekts. |
| `select` | boolean |  | Erstellungsoption: neues Objekt auswählen. |
| `useClassAttributes` | boolean |  | Erstellungsoption: mit `class` auch die Attribute des neuen Objekts anhand der Klasse festlegen. |

### get3DGeometry

Liest ein 3D-Polygon, Netz, eine NURBS-Kurve oder -Fläche aus.

> **Auswirkung:** Nur lesend · **Risikostufe:** niedrig · **Rückgängig:** keiner · **Bei runToolBatch:** Zulässig

**Details**

Liest ein 3D-Polygon, ein Netz, eine NURBS-Kurve oder eine NURBS-Fläche anhand von UUID, Name oder Index aus (getSolid liest Volumenkörper aus). Scheitelpunkte und Punkte verwenden Ebenenkoordinaten (Z relativ zur Konstruktionsebene); `bounds3D` { min, max } verwendet Welt-Z; `layerElevation` ist die Welt-Z-Höhe der zugehörigen Konstruktionsebene (ohne Konstruktionsebenen-Eigentümer `null`); Winkel werden im Bogenmaß angegeben. `limit` (Standardwert 100), `offset` und `countOnly` gelten für jede Liste: Eine Liste hat die Form { count, returned, offset, limit, truncated, nextOffset (bei abgeschnittenen Listen), items } (bei `countOnly` ohne `items`). 3D-Polygon: `kind` polygon3D, `vertexCount`, `closed`, `planar`, `normal` (Einheitsvektor, rechtshändig entsprechend der Reihenfolge der Scheitelpunkte; bei Nichtverfügbarkeit `null`), `plane` { point, normal, d } (normal . p + d = 0; bei Nichtverfügbarkeit `null`), `area` (bei offenen Polygonen `null`), `length` (einschließlich der schließenden Kante, wenn geschlossen), `bounds3D`, `layerElevation` und `vertices` (Elemente { x, y, z }).

**Netz:** `kind` mesh, `vertexCount`, `faceCount`, `isClosed` (wasserdicht), `surfaceArea`, `volume` (nur bei geschlossenem Netz; andernfalls `null`), `smoothing` (none, documentPreference, customCrease oder imported), `creaseAngle` (Bogenmaß; bei Nichtverfügbarkeit `null`), `parts` [{ id, texture, faceCount }] (Teil 0 ist das Gesamtteil; Textur 0 bedeutet keine), `bounds3D`, `layerElevation`, `vertices` (Elemente { x, y, z }) und `faces` (Elemente { vertexIndices, part }).

**NURBS-Kurve:** `kind` nurbsCurve, `pieceCount`, `degree`, `pointCount` und `controlPointCount` (des ersten Teilstücks), `length` (bei Nichtverfügbarkeit `null`), `bounds3D`, `layerElevation`, `pieces` [{ index, degree, pointCount, controlPointCount, knotCount }] und für das Teilstück `piece` (Standardwert 0): `piece`, `points` (Elemente { x, y, z, weight }: die definierenden Punkte des Teilstücks, seine Stützpunkte oder Kontrollpunkte; `weight` ist das Gewicht des Kontrollpunkts dieses Index, falls vorhanden) und `knots` (alle Knoten). Kurvenmessungen, jeweils ein Array aus 1 bis 100 Einträgen mit `null`-Werten, wenn Vectorworks kein Ergebnis hat: `atDistance` [Abstände von 0 bis zur Länge] gibt `pointsAtDistance` [{ distance, point, piece, parameter }] zurück; `closestTo` [3D-Punkte] gibt `closestPoints` [{ to, point, distance, piece, parameter }] zurück; `evaluate` [{ piece? (Standardwert 0), parameter }] gibt `evaluated` [{ piece, parameter, point, tangent (Einheitsvektor), curvature (in 1 / Welteinheiten) }] zurück; `divide` { count (2 bis 1000), includeEnd? (Standardwert true: beide Enden) } gibt `divisionPoints` zurück, `count` gleichmäßig entlang der Kurve verteilte Punkte (Fehler, wenn Vectorworks die Kurve nicht unterteilen kann). Parameter sind die nativen Knotenparameter eines Teilstücks (innerhalb seiner `knots`), keine Bogenlängen.

**NURBS-Fläche:** `kind` nurbsSurface, `uPointCount`, `vPointCount`, `uDegree`, `vDegree`, `uKnots` und `vKnots` (alle Knoten), `bounds3D`, `layerElevation` und `points`, das Kontrollnetz in u-zuerst-Reihenfolge (Element i ist points[i / vPointCount][i % vPointCount]: { u, v, x, y, z, weight }); `evaluate` [{ u, v }] (1 bis 100 Parameter innerhalb von `uKnots` und `vKnots`) gibt `evaluated` [{ u, v, point }] zurück. `piece`, `atDistance`, `closestTo` und `divide` gelten nur für NURBS-Kurven; `evaluate` gilt für NURBS-Kurven und -Flächen.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `uuid` | string |  | Referenz über UUID (bevorzugt). Siehe [Objektreferenzen](Common.md#objektreferenzen). |
| `name` | string |  | Referenz über Namen. |
| `index` | integer |  | Referenz über internen Index. |
| `limit` | integer |  | Seitennavigation: maximale Anzahl zurückzugebender Elemente (mindestens 1). Siehe [Seitennavigation](Common.md#seitennavigation). |
| `offset` | integer |  | Seitennavigation: Anzahl der zu überspringenden Elemente (Standardwert 0). |
| `countOnly` | boolean |  | Seitennavigation: nur die Anzahl zurückgeben, ohne Elemente. |
| `piece` | integer |  | Wird für NURBS-Kurven verwendet. |
| `atDistance` | array of number |  |  |
| `closestTo` | array of [3D-Punkt](Common.md#punkte) |  | Jedes Element: Ein 3D-Punkt in Ebenenkoordinaten oder ein Vektor in Welteinheiten: { x, y, z }. Punkt-Z ist relativ zur Konstruktionsebene; Vektoren sind unabhängig von der Ebenenhöhe; bounds3D verwendet Welt-Z. |
| `evaluate` | array of object |  |  |
| `evaluate[].piece` | integer |  |  |
| `evaluate[].parameter` | number |  |  |
| `evaluate[].u` | number |  |  |
| `evaluate[].v` | number |  |  |
| `divide` | object |  |  |
| `divide.count` | integer | Ja |  |
| `divide.includeEnd` | boolean |  |  |

### edit3DGeometry

Bearbeitet ein 3D-Polygon, Netz, eine NURBS-Kurve oder -Fläche.

> **Auswirkung:** Bearbeiten · **Risikostufe:** mittel · **Rückgängig:** ein Schritt "MCP: edit3DGeometry" · **Bei runToolBatch:** Ja

**Details**

Bearbeitet ein 3D-Polygon, ein Netz, eine NURBS-Kurve oder eine NURBS-Fläche anhand von UUID, Name oder Index; der Aufruf ist ein einzelner Rückgängig-Schritt (editSolid bearbeitet Volumenkörper). Punkte verwenden Ebenenkoordinaten (Z relativ zur Konstruktionsebene); `bounds3D` verwendet Welt-Z; Winkel werden im Bogenmaß und Indizes ab 0 angegeben. Abgewiesen, ohne Änderungen: ein Objekt anderer Art, ein gesperrtes Objekt (zuerst mit editObject `locked` false entsperren), ein Objekt, das sich nicht in einer Ebene, einer Symboldefinition oder einer Gruppe davon befindet, eine für die jeweilige Art nicht unterstützte Operation, ein Aufruf ohne Operationen, eine Erstellungsoperation zusammen mit einer anderen Operation oder ein ungültiger Wert.

Die Operationen werden in dieser Reihenfolge angewendet: `vertices` (ersetzt alle Scheitelpunkte; ein Polygon benötigt 2 bis 32767 3D-Punkte; bei einem Netz mit `faces` kann sich die Anzahl der Scheitelpunkte ändern, wodurch Normalen und UVs gelöscht werden; ohne `faces` bleibt die Anzahl erhalten), `faces` (Netz: [{ vertexIndices, part? }], ersetzt die Flächen), `setVertex` { index, point }, `insertVertex` { index, point } (Polygon: vor dem Index; mit index = vertexCount wird angehängt), `deleteVertex` { index } (Polygon: mindestens 2 Scheitelpunkte bleiben erhalten), `addFace` { vertexIndices, part? }, `deleteFace` { index } und `setFacePart` { index, part } (Netz), `closed` (Polygon), `reverse` true (Polygon) oder `flipFaces` true (Netz), `cleanup` { tolerance? } (Polygon: entfernt doppelte und kollineare Scheitelpunkte), `simplify` (Polygon { maxDeviation &gt; 0 }: Douglas-Peucker; Netz { quality }: der beizubehaltende Detailgrad in Prozent, 0 &lt; quality &lt; 100; niedrigere Werte entfernen mehr Flächen), `segment` { maxSegmentLength &gt; 0 } (Polygon: unterteilt längere Kanten), `smoothing` (Netz: none, documentPreference oder customCrease), `creaseAngle` (Netz: 0 bis pi; stellt die Glättung auf customCrease um), `addPart` { texture? } (Netz: ein Teil mit Textur-Ressourcenreferenz, 0 bedeutet keine; gibt die ID unter `addedPart` zurück), `setPartTexture` { part, texture } (Netz), anschließend für beide Arten `move3D` { offset }, `rotate3D` { center, axis, angle } (rechtshändig um die Achse) und `scale3D` { center, factor &gt; 0 }.

**NURBS-Kurven und -Flächen:** `setPoint` (Kurve { piece? (Standardwert 0), index, point }: ein Punkt aus get3DGeometry `points` des Teilstücks; Fläche { u, v, point }: ein Kontrollpunkt des Netzes), `setWeight` (Kurve { piece?, index, weight }, Index eines Kontrollpunkts; Fläche { u, v, weight }; Gewicht von 0.0001 bis 100; ein Kurvenstück, das durch Stützpunkte definiert ist, unterstützt keine Gewichte), danach `trimByCurve` { curveUuid } (Fläche: Eine Kopie der NURBS-Kurve wird zur Trimgrenze; die Kurve bleibt erhalten). NURBS unterstützen weder `move3D`, `rotate3D` noch `scale3D` (es gibt keine 3D-Transformationen für NURBS), und Knoten werden nicht bearbeitet (das ist mit runPythonScript möglich). Erstellungsoperationen, die jeweils die einzige Operation eines Aufrufs sein müssen, lassen das Objekt unverändert: `toPlanarSolid` { thickness } (ungleich 0; ein geschlossenes, planares Polygon mit mindestens 3 Scheitelpunkten) erstellt auf der aktiven Ebene einen allgemeinen Volumenkörper, das Polygon wird entlang seiner Normalen extrudiert; `repair` true (Netz) erstellt reparierte Netze direkt nach dem Netz; `extend` { distance &gt; 0, atStart? (Standardwert false: das Ende), linear? (Standardwert false), direction (nur Fläche, erforderlich: u oder v) } und `offset` { distance } (ungleich 0) erstellen eine erweiterte oder versetzte Kopie einer NURBS-Kurve oder -Fläche auf der aktiven Ebene. Gibt die Objekt-Referenz, `changed` (angewendete Operationen in Reihenfolge), `kind`, `vertexCount`, `closed` (Polygon) oder `faceCount` und `isClosed` (Netz), `pieceCount`, `degree`, `pointCount`, `controlPointCount` und `length` (Kurve) oder `uPointCount`, `vPointCount`, `uDegree` und `vDegree` (Fläche), `bounds3D` und `layerElevation` zurück; `toPlanarSolid` ergänzt `created` (Referenz und getSolid-Werte des neuen Volumenkörpers), `repair` ergänzt `created`, ein Array der neuen Netze (leer, wenn Vectorworks keine erstellt hat), und `extend` sowie `offset` ergänzen `created` (Referenz und diese Werte der neuen Kurve oder Fläche).

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `uuid` | string |  | Referenz über UUID (bevorzugt). Siehe [Objektreferenzen](Common.md#objektreferenzen). |
| `name` | string |  | Referenz über Namen. |
| `index` | integer |  | Referenz über internen Index. |
| `vertices` | array of [3D-Punkt](Common.md#punkte) |  | Jedes Element: Ein 3D-Punkt in Ebenenkoordinaten oder ein Vektor in Welteinheiten: { x, y, z }. Punkt-Z ist relativ zur Konstruktionsebene; Vektoren sind unabhängig von der Ebenenhöhe; bounds3D verwendet Welt-Z. |
| `faces` | array of object |  | Netz: [{ vertexIndices, part? }], ersetzt die Flächen. |
| `faces[].vertexIndices` | array of integer | Ja |  |
| `faces[].part` | integer |  |  |
| `setVertex` | object |  |  |
| `setVertex.index` | integer | Ja |  |
| `setVertex.point` | [3D-Punkt](Common.md#punkte) | Ja | Ein 3D-Punkt in Ebenenkoordinaten oder ein Vektor in Welteinheiten: { x, y, z }. Punkt-Z ist relativ zur Konstruktionsebene; Vektoren sind unabhängig von der Ebenenhöhe; bounds3D verwendet Welt-Z. |
| `insertVertex` | object |  |  |
| `insertVertex.index` | integer | Ja |  |
| `insertVertex.point` | [3D-Punkt](Common.md#punkte) | Ja | Ein 3D-Punkt in Ebenenkoordinaten oder ein Vektor in Welteinheiten: { x, y, z }. Punkt-Z ist relativ zur Konstruktionsebene; Vektoren sind unabhängig von der Ebenenhöhe; bounds3D verwendet Welt-Z. |
| `deleteVertex` | object |  |  |
| `deleteVertex.index` | integer | Ja |  |
| `addFace` | object |  | Mesh: `{ vertexIndices, part? }` oder einfaches Array mit mindestens 3 Vertex-Indizes. |
| `addFace.vertexIndices` | array of integer | Ja |  |
| `addFace.part` | integer |  |  |
| `deleteFace` | object |  |  |
| `deleteFace.index` | integer | Ja |  |
| `setFacePart` | object |  |  |
| `setFacePart.index` | integer | Ja |  |
| `setFacePart.part` | integer | Ja |  |
| `closed` | boolean |  | Gibt an, ob die Form geschlossen ist. |
| `reverse` | boolean |  | Polygon: `true` kehrt die Reihenfolge der Vertices um; `false` wird abgelehnt. |
| `flipFaces` | boolean |  | Mesh: `true` spiegelt die Flächen; `false` wird abgelehnt. |
| `cleanup` | object |  |  |
| `cleanup.tolerance` | number |  |  |
| `simplify` | object |  |  |
| `simplify.maxDeviation` | number |  |  |
| `simplify.quality` | number |  |  |
| `segment` | object |  |  |
| `segment.maxSegmentLength` | number | Ja |  |
| `smoothing` | string |  | Einer von: `none`, `documentPreference`, `customCrease`. |
| `creaseAngle` | number |  | Netz: 0 bis pi; stellt die Glättung auf customCrease um. |
| `addPart` | object |  |  |
| `addPart.texture` | integer |  |  |
| `setPartTexture` | object |  |  |
| `setPartTexture.part` | integer | Ja |  |
| `setPartTexture.texture` | integer | Ja |  |
| `move3D` | object |  |  |
| `move3D.offset` | [3D-Punkt](Common.md#punkte) | Ja | Ein 3D-Punkt in Ebenenkoordinaten oder ein Vektor in Welteinheiten: { x, y, z }. Punkt-Z ist relativ zur Konstruktionsebene; Vektoren sind unabhängig von der Ebenenhöhe; bounds3D verwendet Welt-Z. |
| `rotate3D` | object |  |  |
| `rotate3D.center` | [3D-Punkt](Common.md#punkte) | Ja | Ein 3D-Punkt in Ebenenkoordinaten oder ein Vektor in Welteinheiten: { x, y, z }. Punkt-Z ist relativ zur Konstruktionsebene; Vektoren sind unabhängig von der Ebenenhöhe; bounds3D verwendet Welt-Z. |
| `rotate3D.axis` | [3D-Punkt](Common.md#punkte) | Ja | Ein 3D-Punkt in Ebenenkoordinaten oder ein Vektor in Welteinheiten: { x, y, z }. Punkt-Z ist relativ zur Konstruktionsebene; Vektoren sind unabhängig von der Ebenenhöhe; bounds3D verwendet Welt-Z. |
| `rotate3D.angle` | number | Ja |  |
| `scale3D` | object |  |  |
| `scale3D.center` | [3D-Punkt](Common.md#punkte) | Ja | Ein 3D-Punkt in Ebenenkoordinaten oder ein Vektor in Welteinheiten: { x, y, z }. Punkt-Z ist relativ zur Konstruktionsebene; Vektoren sind unabhängig von der Ebenenhöhe; bounds3D verwendet Welt-Z. |
| `scale3D.factor` | number | Ja |  |
| `setPoint` | object |  |  |
| `setPoint.piece` | integer |  |  |
| `setPoint.index` | integer |  |  |
| `setPoint.u` | integer |  |  |
| `setPoint.v` | integer |  |  |
| `setPoint.point` | [3D-Punkt](Common.md#punkte) | Ja | Ein 3D-Punkt in Ebenenkoordinaten oder ein Vektor in Welteinheiten: { x, y, z }. Punkt-Z ist relativ zur Konstruktionsebene; Vektoren sind unabhängig von der Ebenenhöhe; bounds3D verwendet Welt-Z. |
| `setWeight` | object |  |  |
| `setWeight.piece` | integer |  |  |
| `setWeight.index` | integer |  |  |
| `setWeight.u` | integer |  |  |
| `setWeight.v` | integer |  |  |
| `setWeight.weight` | number | Ja |  |
| `trimByCurve` | object |  |  |
| `trimByCurve.curveUuid` | string | Ja |  |
| `toPlanarSolid` | object |  |  |
| `toPlanarSolid.thickness` | number | Ja |  |
| `repair` | boolean |  | Mesh: `true` repariert das Mesh; `false` wird abgelehnt. |
| `extend` | object |  |  |
| `extend.distance` | number | Ja |  |
| `extend.atStart` | boolean |  |  |
| `extend.linear` | boolean |  |  |
| `extend.direction` | string |  | Einer von: `u`, `v`. |
| `offset` | object |  |  |
| `offset.distance` | number | Ja |  |

### convertTo3D

Wandelt eine Kopie eines Objekts in 3D-Polygone, ein Netz oder einen allgemeinen Volumenkörper um.

> **Auswirkung:** Bearbeiten · **Risikostufe:** mittel · **Rückgängig:** ein Schritt "MCP: convertTo3D" · **Bei runToolBatch:** Ja

**Details**

Wandelt eine Kopie des 2D- oder 3D-Objekts `sourceUuid` in `to` um: `polygons` (eine Gruppe von 3D-Polygonen), `mesh` oder `genericSolid` (ohne Verlauf; ein 2D-Objekt wird abgewiesen: zuerst in `polygons` oder `mesh` umwandeln oder extrudieren). convertSolid akzeptiert nur Volumenkörper; convertTo3D akzeptiert beliebige 2D- oder 3D-Objekte. Die Quelle bleibt unverändert und das Ergebnis wird direkt nach ihr in ihrem Container platziert; eine Quelle, die sich nicht in einer Ebene, einer Symboldefinition oder einer Gruppe davon befindet, wird abgewiesen, ebenso eine gesperrte Quelle bei `genericSolid`.

Die optionale Erstellungsoption `select` legt fest, ob das Ergebnis ausgewählt wird. Gibt die Objekt-Referenz, `kind` (group, mesh oder genericSolid), `bounds3D` { min, max } in Welt-Z sowie `layerElevation` in Welteinheiten zurück; eine Gruppe enthält zusätzlich `polygonCount`, ein Netz `vertexCount`, `faceCount` und `isClosed`, ein allgemeiner Volumenkörper seine getSolid-Werte. createMesh `groupUuid` erstellt ein Netz aus einer solchen Gruppe; get3DGeometry liest 3D-Polygone und Netze aus.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `sourceUuid` | string | Ja |  |
| `to` | string | Ja | Einer von: `polygons`, `mesh`, `genericSolid`. |
| `class` | string |  | Erstellungsoption: Klasse des neuen Objekts; wird angelegt, falls sie noch nicht vorhanden ist. Siehe [Optionen zur Erstellung](Common.md#optionen-zur-erstellung). |
| `name` | string |  | Erstellungsoption: Name des neuen Objekts. |
| `select` | boolean |  | Erstellungsoption: neues Objekt auswählen. |
| `useClassAttributes` | boolean |  | Erstellungsoption: mit `class` auch die Attribute des neuen Objekts anhand der Klasse festlegen. |

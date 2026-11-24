[English](../../MCP/v2027.2/ObjectPrimitives.md) • **Deutsch** • [日本語](../../MCP.ja/v2027.2/ObjectPrimitives.md)

# ObjectPrimitives — Objekte und 2D-Zeichnen

> **Server:** Vectorworks MCP · **Version:** Vectorworks 2027 Update 2

[Zurück zum Index](README.md)

Werkzeuge für beliebige Objekte der Zeichnung (Suchen, Prüfen, Gestalten, Transformieren, Plug-in-Parameter und Datensätze) sowie zum Erstellen, Bearbeiten, Messen und Kombinieren von 2D-Grundformen und Text.

## Inhaltsverzeichnis

- [Übersicht](#übersicht)
- [Draw2D](#draw2d)
  - [createLine](#createline)
  - [createRectangle](#createrectangle)
  - [createCircle](#createcircle)
  - [createArc](#createarc)
  - [createPolygon](#createpolygon)
  - [createPolyline](#createpolyline)
  - [createLocus](#createlocus)
  - [getGeometry](#getgeometry)
  - [setGeometry](#setgeometry)
  - [editVertices](#editvertices)
  - [queryGeometry](#querygeometry)
  - [combineShapes](#combineshapes)
  - [createText](#createtext)
  - [getText](#gettext)
  - [editText](#edittext)
- [Objects](#objects)
  - [findObjects](#findobjects)
  - [getObjectsAtPoint](#getobjectsatpoint)
  - [getObjectInfo](#getobjectinfo)
  - [getObjectAttributes](#getobjectattributes)
  - [setObjectAttributes](#setobjectattributes)
  - [copyAttributes](#copyattributes)
  - [editObject](#editobject)
  - [getObjectParameters](#getobjectparameters)
  - [getObjectRecords](#getobjectrecords)
  - [setObjectParameter](#setobjectparameter)
  - [getPluginDefinition](#getplugindefinition)
  - [createPluginObject](#createpluginobject)

## Übersicht

Dieser Ordner enthält 2 Werkzeuggruppen mit insgesamt 27 Werkzeugen.

| Gruppe | Gruppen-ID | Standardmäßig aktiv | Risikostufe | Werkzeuge | Zusammenfassung |
|---|---|---|---|---|---|
| [Draw2D](#draw2d) | `draw2d` | Nein | niedrig | 15 | 2D-Grundformen erstellen, bearbeiten, messen und kombinieren sowie Textobjekte erstellen, auslesen und bearbeiten. |
| [Objects](#objects) | `objects` | Ja | mittel | 12 | Beliebige Objekte suchen, prüfen und bearbeiten: Attribute, Transformationen, Container, Plug-in-Parameter und Datensätze. |

## Draw2D

> **Gruppe:** `Draw2D` · **Gruppen-ID:** `draw2d` · **Standardmäßig aktiv:** Nein · **Risikostufe:** niedrig · **Werkzeuge:** 15

**2D-Grundformen erstellen, bearbeiten, messen und kombinieren sowie Textobjekte erstellen, auslesen und bearbeiten.**

Erstellen, bearbeiten und messen Sie die Geometrie von 2D-Grundformen: Linien, Rechtecke, abgerundete Rechtecke, Kreise, Kreisbögen, Polygone, Polylinien und Ortspunkte. Kombinieren Sie zwei 2D-Formen mit Booleschen Operationen (`combineShapes`: Vereinigung, Schnittmenge, Differenz = erste Form minus zweite Form und symmetrische Differenz) für Linien, Rechtecke, abgerundete Rechtecke, Ovale, Kreisbögen und Kreise, Polygone (keine Freihandpolygone) und Polylinien. Die Ergebnisse sind neue 2D-Objekte beliebigen Typs mit den Attributen der ersten Form in deren Container. Die Originale bleiben unverändert, sofern `deleteOriginals` nichts anderes festlegt. Eine zweite Form in einer anderen Ebene wird zuvor in die Ebene der ersten verschoben. Ein leeres Ergebnis gilt als Erfolg und liefert keine Formen. Erstellen, lesen und bearbeiten Sie außerdem Textobjekte (`createText`, `getText`, `editText`): deren Inhalt, Zeichenformatierung, Textstile, Ausrichtung, Zeilenabstand, Umbruch und Tabulatoren.

Koordinaten werden in Welteinheiten, Winkel im Bogenmaß angegeben. Neue Objekte werden auf der aktiven Konstruktionsebene erstellt, Ergebnisse von `combineShapes` im Container der ersten Form. Jede Änderung wird als eigener, benannter und rückgängig machbarer Vectorworks-Vorgang ausgeführt. `queryGeometry` beantwortet Fragen zum nächsten Punkt, Abstand, Enthaltensein, Schnitt und zu Tangenten und misst Polygone und Polylinien entlang ihrer tatsächlichen Kurve (Länge, Punkt, Tangente und Krümmung an einer bestimmten Entfernung sowie Unterteilung in gleich große Abschnitte), ohne die Zeichnung zu ändern.

| Werkzeug | Wirkung | Risiko | Zusammenfassung |
|---|---|---|---|
| [`createLine`](#createline) | Bearbeiten | niedrig | Erstellt eine gerade Linie zwischen zwei Punkten. |
| [`createRectangle`](#createrectangle) | Bearbeiten | niedrig | Erstellt ein Rechteck, optional gedreht und mit abgerundeten Ecken. |
| [`createCircle`](#createcircle) | Bearbeiten | niedrig | Erstellt einen Kreis anhand von Mittelpunkt und Radius oder durch drei Punkte. |
| [`createArc`](#createarc) | Bearbeiten | niedrig | Erstellt einen Kreisbogen anhand von Mittelpunkt, Radius und Winkeln oder durch drei Punkte. |
| [`createPolygon`](#createpolygon) | Bearbeiten | niedrig | Erstellt ein Polygon aus Punkten oder ein regelmäßiges Polygon. |
| [`createPolyline`](#createpolyline) | Bearbeiten | niedrig | Erstellt eine Polylinie aus Scheitelpunkten beliebigen Typs oder eine abgerundete Form. |
| [`createLocus`](#createlocus) | Bearbeiten | niedrig | Erstellt einen 2D-Ortspunkt (Bezugspunkt). |
| [`getGeometry`](#getgeometry) | Nur lesend | niedrig | Liest die typspezifische Geometrie einer 2D-Grundform aus. |
| [`setGeometry`](#setgeometry) | Bearbeiten | niedrig | Bearbeitet die Geometrie einer 2D-Grundform. |
| [`editVertices`](#editvertices) | Bearbeiten | niedrig | Fügt Scheitelpunkte eines Polygons oder einer Polylinie hinzu oder ein, ändert, löscht, kehrt sie um oder ersetzt sie. |
| [`queryGeometry`](#querygeometry) | Nur lesend | niedrig | Beantwortet geometrische Fragen zu einer 2D-Grundform: nächster Punkt, Abstand, Enthaltensein, Schnittpunkte, Tangenten und Messungen entlang von Kurven. |
| [`combineShapes`](#combineshapes) | Bearbeiten | niedrig | Kombiniert zwei 2D-Formen mit einer Booleschen Operation: Vereinigung, Schnittmenge, Differenz oder symmetrische Differenz. |
| [`createText`](#createtext) | Bearbeiten | niedrig | Erstellt ein Textobjekt. |
| [`getText`](#gettext) | Nur lesend | niedrig | Liest Inhalt, Zeichenformatierung, Stil und Layout eines Textobjekts aus. |
| [`editText`](#edittext) | Bearbeiten | niedrig | Bearbeitet den Inhalt und die Formatierung eines Textobjekts. |

### createLine

Erstellt eine gerade Linie zwischen zwei Punkten.

> **Wirkung:** Bearbeiten · **Risiko:** niedrig · **Rückgängig:** ein Schritt „MCP: createLine“ · **Bei runToolBatch:** ja

**Details**

Erstellt eine gerade Linie zwischen den Punkten `start` und `end`.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `start` | [Punkt](Common.md#punkte) | Ja | Startpunkt. |
| `end` | [Punkt](Common.md#punkte) | Ja | Endpunkt. |
| `class` | string |  | Erstellungsoption: Klasse des neuen Objekts; wird bei Bedarf erstellt. Siehe [Erstellungsoptionen](Common.md#optionen-zur-erstellung). |
| `name` | string |  | Erstellungsoption: Name des neuen Objekts. |
| `select` | boolean |  | Erstellungsoption: neues Objekt auswählen. |
| `useClassAttributes` | boolean |  | Erstellungsoption: mit `class` auch die Attribute des neuen Objekts anhand der Klasse festlegen. |

### createRectangle

Erstellt ein Rechteck, optional gedreht und mit abgerundeten Ecken.

> **Wirkung:** Bearbeiten · **Risiko:** niedrig · **Rückgängig:** ein Schritt „MCP: createRectangle“ · **Bei runToolBatch:** ja

**Details**

Erstellt ein Rechteck mit Mittelpunkt `center`, `width` und `height` sowie optionalem `angle` (Bogenmaß). Ein positiver Wert für `cornerRadius` oder `cornerDiameters` { alongWidth, alongHeight } für elliptische Ecken (Eckdurchmesser entlang der Breiten- und Höhenseite) erzeugt ein abgerundetes Rechteck. Mit `proportional` werden die Ecken bei interaktiver Größenänderung proportional skaliert.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `center` | [Punkt](Common.md#punkte) | Ja | Mittelpunkt. |
| `width` | number | Ja | Breite in Welteinheiten. |
| `height` | number | Ja | Höhe in Welteinheiten. |
| `angle` | number |  | Winkel im Bogenmaß, gegen den Uhrzeigersinn. |
| `cornerRadius` | number |  | Eckenradius in Welteinheiten. |
| `cornerDiameters` | object |  | Elliptische Ecken: Durchmesser der Eckellipse. Hat Vorrang vor `cornerRadius`; keiner der Werte darf negativ sein. Bereits die Angabe in beliebiger Form erzeugt ein abgerundetes Rechteck; ein fehlendes Element gilt als 0. |
| `cornerDiameters.alongWidth` | number |  | Eckdurchmesser entlang der Breite in Welteinheiten. Standard 0. |
| `cornerDiameters.alongHeight` | number |  | Eckdurchmesser entlang der Höhe in Welteinheiten. Standard 0. |
| `proportional` | boolean |  | Nur für abgerundete Rechtecke: Ecken werden bei interaktiver Größenänderung mitskaliert. Standard `false`. |
| `class` | string |  | Erstellungsoption: Klasse des neuen Objekts; wird bei Bedarf erstellt. Siehe [Erstellungsoptionen](Common.md#optionen-zur-erstellung). |
| `name` | string |  | Erstellungsoption: Name des neuen Objekts. |
| `select` | boolean |  | Erstellungsoption: neues Objekt auswählen. |
| `useClassAttributes` | boolean |  | Erstellungsoption: mit `class` auch die Attribute des neuen Objekts anhand der Klasse festlegen. |

### createCircle

Erstellt einen Kreis anhand von Mittelpunkt und Radius oder durch drei Punkte.

> **Wirkung:** Bearbeiten · **Risiko:** niedrig · **Rückgängig:** ein Schritt „MCP: createCircle“ · **Bei runToolBatch:** ja

**Details**

Erstellt einen Kreis mit Mittelpunkt `center` und Radius `radius` oder den Kreis durch die drei Punkte `threePoints`.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `center` | [Punkt](Common.md#punkte) |  | Mittelpunkt. |
| `radius` | number |  | Radius in Welteinheiten. |
| `threePoints` | array of [Punkt](Common.md#punkte) |  | 3 Elemente. |
| `class` | string |  | Erstellungsoption: Klasse des neuen Objekts; wird bei Bedarf erstellt. Siehe [Erstellungsoptionen](Common.md#optionen-zur-erstellung). |
| `name` | string |  | Erstellungsoption: Name des neuen Objekts. |
| `select` | boolean |  | Erstellungsoption: neues Objekt auswählen. |
| `useClassAttributes` | boolean |  | Erstellungsoption: mit `class` auch die Attribute des neuen Objekts anhand der Klasse festlegen. |

### createArc

Erstellt einen Kreisbogen anhand von Mittelpunkt, Radius und Winkeln oder durch drei Punkte.

> **Wirkung:** Bearbeiten · **Risiko:** niedrig · **Rückgängig:** ein Schritt „MCP: createArc“ · **Bei runToolBatch:** ja

**Details**

Erstellt einen Kreisbogen mit Mittelpunkt `center`, Radius `radius`, `startAngle` und `sweepAngle` (Bogenmaß, gegen den Uhrzeigersinn) oder den Bogen durch `threePoints` [Startpunkt, Punkt auf dem Bogen, Endpunkt].

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `center` | [Punkt](Common.md#punkte) |  | Mittelpunkt. |
| `radius` | number |  | Radius in Welteinheiten. |
| `startAngle` | number |  | Startwinkel im Bogenmaß, gegen den Uhrzeigersinn. |
| `sweepAngle` | number |  | Überstreichwinkel im Bogenmaß; positive Werte verlaufen gegen den Uhrzeigersinn. |
| `threePoints` | array of [Punkt](Common.md#punkte) |  | 3 Elemente. |
| `class` | string |  | Erstellungsoption: Klasse des neuen Objekts; wird bei Bedarf erstellt. Siehe [Erstellungsoptionen](Common.md#optionen-zur-erstellung). |
| `name` | string |  | Erstellungsoption: Name des neuen Objekts. |
| `select` | boolean |  | Erstellungsoption: neues Objekt auswählen. |
| `useClassAttributes` | boolean |  | Erstellungsoption: mit `class` auch die Attribute des neuen Objekts anhand der Klasse festlegen. |

### createPolygon

Erstellt ein Polygon aus Punkten oder ein regelmäßiges Polygon.

> **Wirkung:** Bearbeiten · **Risiko:** niedrig · **Rückgängig:** ein Schritt „MCP: createPolygon“ · **Bei runToolBatch:** ja

**Details**

Erstellt ein Polygon aus einem `points`-Array (mit `closed`, standardmäßig true) oder ein regelmäßiges Polygon anhand von `center`/`radius`/`sides` (optional `startAngle`).

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `points` | array of [Punkt](Common.md#punkte) |  | Die Punkte in Reihenfolge. |
| `closed` | boolean |  | Gibt an, ob die Form geschlossen ist. |
| `center` | [Punkt](Common.md#punkte) |  | Mittelpunkt. |
| `radius` | number |  | Radius in Welteinheiten. |
| `sides` | integer |  | Anzahl der Seiten eines regelmäßigen Polygons, mindestens 3. Bei Angabe wird `points` nicht gelesen. Ein Wert, der keine Zahl ist, wird als 3 gelesen. |
| `startAngle` | number |  | Startwinkel im Bogenmaß, gegen den Uhrzeigersinn. |
| `class` | string |  | Erstellungsoption: Klasse des neuen Objekts; wird bei Bedarf erstellt. Siehe [Erstellungsoptionen](Common.md#optionen-zur-erstellung). |
| `name` | string |  | Erstellungsoption: Name des neuen Objekts. |
| `select` | boolean |  | Erstellungsoption: neues Objekt auswählen. |
| `useClassAttributes` | boolean |  | Erstellungsoption: mit `class` auch die Attribute des neuen Objekts anhand der Klasse festlegen. |

### createPolyline

Erstellt eine Polylinie aus Scheitelpunkten beliebigen Typs oder eine abgerundete Form.

> **Wirkung:** Bearbeiten · **Risiko:** niedrig · **Rückgängig:** ein Schritt „MCP: createPolyline“ · **Bei runToolBatch:** ja

**Details**

Erstellt eine Polylinie aus einem `vertices`-Array. Jeder Scheitelpunkt hat die Form { x, y, type?, arcRadius?, visible? }, wobei `type` corner|bezier|cubic|arc|radius ist und `visible` mit dem Wert false die Kante zum nächsten Scheitelpunkt ausblendet. `closed` ist optional (standardmäßig false). Ohne `vertices` erstellt `center` mit `radius` einen geschlossenen Kreis aus vier Bogenscheitelpunkten. `center` mit `width` und `height` erstellt ein geschlossenes Rechteck mit Bogenscheitelpunkten an den Ecken und `cornerRadius` (standardmäßig 0: scharfe Ecken; maximal die Hälfte der kürzeren Seite).

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `vertices` | array of object |  | Vertices der Reihe nach (mindestens 2); jeder ist ein Objekt oder ein Punkt `[x, y]`. Einträge ohne Punkt werden übersprungen. |
| `vertices[].x` | number |  | X-Koordinate in Welteinheiten. |
| `vertices[].y` | number |  | Y-Koordinate in Welteinheiten. |
| `vertices[].type` | string |  | Einer von: `corner`, `bezier`, `cubic`, `arc`, `radius`. |
| `vertices[].arcRadius` | number |  | Radius eines `arc`-Vertex in Welteinheiten; bei anderen Vertextypen ignoriert. Standard 0. |
| `vertices[].visible` | boolean |  | `false` blendet die Kante zum nächsten Vertex aus. Standard `true`. |
| `closed` | boolean |  | Gibt an, ob die Form geschlossen ist. |
| `center` | [Punkt](Common.md#punkte) |  | Mittelpunkt. |
| `radius` | number |  | Radius in Welteinheiten. |
| `width` | number |  | Breite in Welteinheiten. |
| `height` | number |  | Höhe in Welteinheiten. |
| `cornerRadius` | number |  | Eckenradius in Welteinheiten. |
| `class` | string |  | Erstellungsoption: Klasse des neuen Objekts; wird bei Bedarf erstellt. Siehe [Erstellungsoptionen](Common.md#optionen-zur-erstellung). |
| `name` | string |  | Erstellungsoption: Name des neuen Objekts. |
| `select` | boolean |  | Erstellungsoption: neues Objekt auswählen. |
| `useClassAttributes` | boolean |  | Erstellungsoption: mit `class` auch die Attribute des neuen Objekts anhand der Klasse festlegen. |

### createLocus

Erstellt eine 2D-Ortspunkt (Bezugspunkt).

> **Wirkung:** Bearbeiten · **Risiko:** niedrig · **Rückgängig:** ein Schritt „MCP: createLocus“ · **Bei runToolBatch:** ja

**Details**

Erstellt eine 2D-Ortspunkt (Bezugs-/Fangpunkt) an `position`.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `position` | [Punkt](Common.md#punkte) | Ja | Einfügepunkt. |
| `class` | string |  | Erstellungsoption: Klasse des neuen Objekts; wird bei Bedarf erstellt. Siehe [Erstellungsoptionen](Common.md#optionen-zur-erstellung). |
| `name` | string |  | Erstellungsoption: Name des neuen Objekts. |
| `select` | boolean |  | Erstellungsoption: neues Objekt auswählen. |
| `useClassAttributes` | boolean |  | Erstellungsoption: mit `class` auch die Attribute des neuen Objekts anhand der Klasse festlegen. |

### getGeometry

Liest die typspezifische Geometrie einer 2D-Grundform aus.

> **Wirkung:** Nur lesend · **Risiko:** niedrig · **Rückgängig:** keine · **Bei runToolBatch:** zulässig

**Details**

Liest die typspezifische Geometrie einer 2D-Grundform (`kind`) aus.

**Linie:** start, end, length, angle, midPoint, direction (Einheitsvektor).

**Kreis:** center, radius, diameter, circumference.

**Kreisbogen:** center, radius, startAngle, sweepAngle, endAngle, startPoint und endPoint (Endpunkte der Sehne), midPoint, length (entlang des Bogens), chordLength, sagitta.

**Rechteck und abgerundetes Rechteck:** center, width, height, angle, origin (erste Ecke), direction (Einheitsvektor entlang der Breite), corners (gegen den Uhrzeigersinn ab origin), isAxisAligned sowie isSquare (Rechteck) oder cornerRadius, cornerDiameters { alongWidth, alongHeight } und hasCircularCorners (abgerundetes Rechteck).

**Ortspunkt:** position, masterSnapPoint, showMasterSnapOutsideSnapBox.

**Polygon:** closed, isFreehand, points (bei einem Punkt, dessen Kante zum nächsten Punkt ausgeblendet ist, ist visible false).

**Polylinie:** closed, hasCurves, vertices { x, y, type, arcRadius, maxRadius (größter Radius, der für einen Bogenscheitelpunkt möglich ist), controlPoint (gespeicherter Kontrollpunkt, wenn er von x/y abweicht), visible }. Für Polygone und Polylinien werden zusätzlich Scheitelpunktanzahl, Fläche, Umfang, Schwerpunkt und die Flags clockwise/convex/self-intersecting zurückgegeben.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `uuid` | string |  | Über UUID referenzieren (bevorzugt). Siehe [Objektreferenzen](Common.md#objektreferenzen). |
| `name` | string |  | Über den Namen referenzieren. |
| `index` | integer |  | Über den internen Index referenzieren. |

### setGeometry

Bearbeitet die Geometrie einer 2D-Grundform.

> **Wirkung:** Bearbeiten · **Risiko:** niedrig · **Rückgängig:** ein Schritt „MCP: setGeometry“ · **Bei runToolBatch:** ja

**Details**

Bearbeitet die Geometrie einer 2D-Grundform anhand ihrer UUID. Geben Sie die Felder des jeweiligen Typs an.

**Linie:** start, end, length, angle, extendStart/extendEnd (Enden verlängern, negative Werte kürzen), offsetParallel (seitlich verschieben; positive Werte nach links von start→end), reverse (Enden vertauschen).

**Kreis:** threePoints (3 Punkte auf dem Kreis), center, radius, diameter; mit startAngle/sweepAngle/endAngle wird daraus ein Kreisbogen.

**Kreisbogen:** threePoints [Startpunkt, Punkt auf dem Bogen, Endpunkt], center, radius, startAngle (der Endwinkel bleibt erhalten), sweepAngle und endAngle (der Startwinkel bleibt erhalten); mit startAngle und sweepAngle werden beide festgelegt.

**Rechteck und abgerundetes Rechteck:** center, angle, width/height (Mittelpunkt bleibt erhalten), origin und direction (erste Ecke und Breitenseite platzieren, Größe beibehalten), bounds { left, top, right, bottom } (ungedreht); beim abgerundeten Rechteck zusätzlich cornerRadius und cornerDiameters { alongWidth, alongHeight }.

**Ortspunkt:** position, masterSnapPoint und showMasterSnapOutsideSnapBox (Fangverhalten innerhalb einer Symboldefinition). Verwenden Sie für Polygone und Polylinien `editVertices`.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `uuid` | string |  | Über UUID referenzieren (bevorzugt). Siehe [Objektreferenzen](Common.md#objektreferenzen). |
| `name` | string |  | Über den Namen referenzieren. |
| `index` | integer |  | Über den internen Index referenzieren. |
| `start` | [Punkt](Common.md#punkte) |  | Für eine Linie. Startpunkt. |
| `end` | [Punkt](Common.md#punkte) |  | Für eine Linie. Endpunkt. |
| `length` | number |  | Für eine Linie. |
| `angle` | number |  | Für Linie, Kreisbogen, Rechteck und abgerundetes Rechteck. Winkel im Bogenmaß, gegen den Uhrzeigersinn. |
| `extendStart` | number |  | Für eine Linie. |
| `extendEnd` | number |  | Für eine Linie. Enden verlängern, negative Werte kürzen. |
| `offsetParallel` | number |  | Für eine Linie. Seitlich verschieben; positive Werte nach links von start→end. |
| `reverse` | boolean |  | Für eine Linie. Enden vertauschen. |
| `center` | [Punkt](Common.md#punkte) |  | Für Kreis, Kreisbogen, Rechteck und abgerundetes Rechteck. Mittelpunkt. |
| `radius` | number |  | Für Kreis und Kreisbogen. Radius in Welteinheiten. |
| `diameter` | number |  | Für einen Kreis. Durchmesser in Welteinheiten. |
| `threePoints` | array of [Punkt](Common.md#punkte) |  | Für einen Kreis. 3 Elemente. |
| `startAngle` | number |  | Für Kreis und Kreisbogen. Startwinkel im Bogenmaß, gegen den Uhrzeigersinn. |
| `sweepAngle` | number |  | Für Kreis und Kreisbogen. Überstreichwinkel im Bogenmaß; positive Werte verlaufen gegen den Uhrzeigersinn. |
| `endAngle` | number |  | Für einen Kreisbogen. Startwinkel beibehalten. |
| `width` | number |  | Für Rechteck und abgerundetes Rechteck. Breite in Welteinheiten. |
| `height` | number |  | Für Rechteck und abgerundetes Rechteck. Mittelpunkt beibehalten. |
| `origin` | [Punkt](Common.md#punkte) |  | Für Rechteck und abgerundetes Rechteck. |
| `direction` | [Punkt](Common.md#punkte) |  | Für Rechteck und abgerundetes Rechteck. Erste Ecke und Breitenseite platzieren, Größe beibehalten. |
| `bounds` | [Rechteck](Common.md#rechtecke) |  | Für Rechteck und abgerundetes Rechteck. |
| `cornerRadius` | number |  | Für Rechteck und abgerundetes Rechteck. Eckenradius in Welteinheiten. |
| `cornerDiameters` | object |  | Für Rechteck und abgerundetes Rechteck. |
| `cornerDiameters.alongWidth` | number |  | Eckdurchmesser entlang der Breite in Welteinheiten. |
| `cornerDiameters.alongHeight` | number |  | Eckdurchmesser entlang der Höhe in Welteinheiten. |
| `position` | [Punkt](Common.md#punkte) |  | Für Ortspunkte. Einfügepunkt. |
| `masterSnapPoint` | boolean |  | Für Ortspunkte. |
| `showMasterSnapOutsideSnapBox` | boolean |  | Für Ortspunkte. Fangverhalten innerhalb einer Symboldefinition. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `applied` | Ein Eintrag pro angegebenem Wert, den der Objekttyp unterstützt; `true`, wenn er geschrieben wurde. |


### editVertices

Fügt Scheitelpunkte eines Polygons oder einer Polylinie hinzu oder ein, ändert, löscht, kehrt sie um oder ersetzt sie.

> **Wirkung:** Bearbeiten · **Risiko:** niedrig · **Rückgängig:** ein Schritt „MCP: editVertices“ · **Bei runToolBatch:** ja

**Details**

Bearbeitet die Scheitelpunkte eines Polygons oder einer Polylinie. `action`: add (fügt `point` an), insert (fügt `point` vor `index` ein), set (ändert `point`, `type`, `arcRadius` oder das Kanten-Flag `visible` des Scheitelpunkts bei `index`), delete (`index`), deleteAll, reverse oder replace (alle Scheitelpunkte: aus `points`, wobei alle Kanten sichtbar sind, oder aus `vertices` { x, y, type?, arcRadius?, visible? } wie bei `createPolyline`; mindestens zwei Scheitelpunkte; das Flag closed bleibt erhalten). Bei add und insert können für den neuen Scheitelpunkt auch `type`, `arcRadius` und `visible` angegeben werden.

Scheitelpunkt-`type` (corner|bezier|cubic|arc|radius) und `arcRadius` gelten nur für Polylinien. `closed`, `clockwise` und `allVerticesVisible` können bei jeder Aktion festgelegt werden. Gibt `applied` sowie die aktualisierte Anzahl der Scheitelpunkte, Fläche, Umfang, den Schwerpunkt und die Form-Flags zurück.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `uuid` | string |  | Über UUID referenzieren (bevorzugt). Siehe [Objektreferenzen](Common.md#objektreferenzen). |
| `name` | string |  | Über den Namen referenzieren. |
| `index` | integer |  | Über den internen Index referenzieren. |
| `action` | string |  | Einer von: `add`, `insert`, `set`, `delete`, `deleteAll`, `reverse`, `replace`. |
| `point` | [Punkt](Common.md#punkte) |  | Ein Punkt. |
| `type` | string |  | Einer von: `corner`, `bezier`, `cubic`, `arc`, `radius`. |
| `arcRadius` | number |  | Nur Polylinien. Bogenradius des Vertex in Welteinheiten, mindestens 0. Bei `add` und `insert` nur verwendet, wenn `type` `arc` ist (Standard 0). Bei `set` wird der Vertex mit diesem Radius zum `arc`-Vertex, auch wenn `type` im selben Aufruf einen anderen Typ angibt; ein negativer Wert führt zu `applied.arcRadius` `false`. |
| `visible` | boolean |  | Gibt an, ob die Kante vom Vertex zum nächsten sichtbar ist. Bei `add` und `insert` ist der Standard `true`; bei `set` wird der Vertex am Index geändert. |
| `points` | array of [Punkt](Common.md#punkte) |  | Die Punkte in Reihenfolge. |
| `vertices` | array of object |  | Vertices für `replace`, wie bei createPolyline; mindestens zwei. Ein Element ohne Punkt wird übersprungen. Ein Polygon verwendet sie als Ecken. |
| `vertices[].x` | number |  | X-Koordinate in Welteinheiten. |
| `vertices[].y` | number |  | Y-Koordinate in Welteinheiten. |
| `vertices[].type` | string |  | Einer von: `corner`, `bezier`, `cubic`, `arc`, `radius`. |
| `vertices[].arcRadius` | number |  | Bogenradius in Welteinheiten; nur verwendet, wenn `type` `arc` ist. Standard 0. |
| `vertices[].visible` | boolean |  | Gibt an, ob die Kante zum nächsten Vertex sichtbar ist. Standard `true`. |
| `closed` | boolean |  | Gibt an, ob die Form geschlossen ist. |
| `clockwise` | boolean |  | Reihenfolge der Vertices: `true` im Uhrzeigersinn, `false` gegen den Uhrzeigersinn. Mit jeder Aktion verwendbar. |
| `allVerticesVisible` | boolean |  | `true` macht die Kante jedes Vertex sichtbar, `false` blendet alle aus. Mit jeder Aktion verwendbar. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `applied` | Ein Eintrag für die Bearbeitung sowie je ein Eintrag für jedes angegebene Feld aus `closed`, `clockwise` und `allVerticesVisible`; jeweils `true`, wenn geschrieben. Der Bearbeitungseintrag ist nach `action` benannt (`add`, `insert`, `delete`, `deleteAll`, `reverse`, `replace`). Bei `set` gibt es je angegebenem Feld aus `point`, `type`, `arcRadius` und `visible` einen Eintrag; bei Polygonen entfallen `type` und `arcRadius`, ebenso ein ungültiger `point`. `replace` mit weniger als zwei Vertices ergibt `replace: false`. |
| `vertexCount` | Anzahl der Vertices. |
| `area`, `perimeter`, `centroid` | Measures of the shape, each only when Vectorworks can compute it. |
| `clockwise`, `convex`, `selfIntersecting` | Shape flags, each only when Vectorworks can compute it. |


### queryGeometry

Beantwortet geometrische Fragen zu einer 2D-Grundform: nächster Punkt, Abstand, Enthaltensein, Schnittpunkte, Tangenten und Messungen entlang von Kurven.

> **Wirkung:** Nur lesend · **Risiko:** niedrig · **Rückgängig:** keine · **Bei runToolBatch:** zulässig

**Details**

Beantwortet eine geometrische Frage zu einer 2D-Grundform, ohne sie zu ändern. `operation`: closestPoint (`point`; gibt den nächstgelegenen `point` auf dem Objekt und dessen `distance` zurück) und distanceTo (`point`; gibt `distance` zurück) für Linien, Kreisbögen, Kreise (bis zum Umfang), Rechtecke, Polygone, Polylinien und Ortspunkte; contains (`point`; true innerhalb oder auf der Begrenzung) für Kreise, Rechtecke sowie geschlossene Polygone/Polylinien; intersect (gibt `points` zurück) mit dem Objekt `otherUuid` oder dem Segment `lineStart`-`lineEnd`: Linien, Kreisbögen, Kreise, Rechtecke, Polygone und Polylinien schneiden Segmente und Linienobjekte; Kreisbögen und Kreise schneiden außerdem einander; pointAt (`angle` im Bogenmaß; gibt `point` zurück) und tangentPoints (`point`; gibt die `points` des Kreises zurück, deren Tangenten durch diesen Punkt verlaufen; von einem Punkt innerhalb des Kreises gibt es keine) für Kreise.

Für Polygone und Polylinien außerdem: curveLength (gibt `length` zurück); pointAtDistance (`distance` entlang der Kurve ab ihrem Anfang, von 0 bis zu ihrer Länge; gibt `point`, die Einheits-`tangent` (Richtung der Kurve an dieser Stelle) und die `curvature` (1 / Radius, 0 entlang gerader Kanten) zurück; Tangente und Krümmung werden ausgelassen, wenn die Kurve dort keine Richtung hat); divide (`count` Punkte, 2 bis 10000, gleichmäßig entlang der Kurve ab ihrem Anfang verteilt; bei `includeEnd` true (Standard) liegt der letzte Punkt am Ende, das bei einer geschlossenen Kurve wieder dem Anfang entspricht. Bei false werden die Punkte im Abstand Länge / count verteilt und der Endpunkt ausgelassen. Gibt `points` zurück.

Polygone und Polylinien werden entlang ihrer tatsächlichen Kurve gemessen, wie gezeichnet (Bögen und Splines statt ihrer Kontrollpunkte): entlang des äußeren Pfads einschließlich ausgeblendeter Kanten und der Schließkante, ohne Löcher. Dies gilt für closestPoint, distanceTo, curveLength, pointAtDistance und divide. contains und intersect verwenden stattdessen das Scheitelpunktpolygon (gerade Kanten zwischen den Scheitelpunkten; Kurvenscheitelpunkte gelten als Ecken): Ein Test auf Enthaltensein entlang der tatsächlichen Kurve ist nicht verfügbar.

Rechtecke werden entlang ihrer vier Ecken gemessen (Eckenabrundungen werden ignoriert).

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `uuid` | string |  | Über UUID referenzieren (bevorzugt). Siehe [Objektreferenzen](Common.md#objektreferenzen). |
| `name` | string |  | Über den Namen referenzieren. |
| `index` | integer |  | Über den internen Index referenzieren. |
| `operation` | string | Ja | Einer von: `closestPoint`, `distanceTo`, `contains`, `intersect`, `pointAt`, `tangentPoints`, `curveLength`, `pointAtDistance`, `divide`. |
| `point` | [Punkt](Common.md#punkte) |  | Ein Punkt. |
| `otherUuid` | string |  | Für `intersect`: UUID des anderen Objekts. Suche ausschließlich anhand der UUID. |
| `lineStart` | [Punkt](Common.md#punkte) |  | Für `intersect`: Segmentanfang. Zusammen mit `lineEnd` verwenden; ein ungültiger Punkt wird als (0, 0) gelesen. |
| `lineEnd` | [Punkt](Common.md#punkte) |  | Für `intersect`: Segmentende. Zusammen mit `lineStart` verwenden. |
| `angle` | number |  | Winkel im Bogenmaß, gegen den Uhrzeigersinn. |
| `distance` | number |  | Für `pointAtDistance` erforderlich. Abstand entlang der Kurve ab ihrem Anfang, von 0 bis zur Kurvenlänge, in Welteinheiten. |
| `count` | integer |  | Für `divide` erforderlich. Anzahl der Punkte, 2 bis 10000. |
| `includeEnd` | boolean |  | Für `divide`: `true` (Standard) setzt den letzten Punkt ans Kurvenende; `false` verteilt die Punkte im Abstand Kurvenlänge / Anzahl und lässt das Ende aus. |

**Ergebnis**

| Operation | Schlüssel |
|---|---|
| `closestPoint` | `distance` und `point`: nächster Punkt auf dem Objekt. |
| `distanceTo` | `distance`. |
| `contains` | `contains`: `true` oder `false`. |
| `intersect` | `points`: Schnittpunkte; leere Liste, wenn sich die Objekte nicht schneiden. |
| `pointAt` | `point`. |
| `tangentPoints` | `points`: Punkte auf dem Kreis, deren Tangenten durch `point` verlaufen; von einem Punkt innerhalb des Kreises aus ist die Liste leer. |
| `curveLength` | `length` in Welteinheiten. |
| `pointAtDistance` | `point`, Einheitstangente `tangent` und `curvature`; die letzten beiden werden ausgelassen, wenn die Kurve keine Richtung hat. |
| `divide` | `points`. |


### combineShapes

Kombiniert zwei 2D-Formen mit einer Booleschen Operation: Vereinigung, Schnittmenge, Differenz oder symmetrische Differenz.

> **Wirkung:** Bearbeiten · **Risiko:** niedrig · **Rückgängig:** ein Schritt "MCP: combineShapes" · **Bei runToolBatch:** ja

**Details**

Kombiniert zwei 2D-Formen mit einer Booleschen Operation wie Ändern &gt; Fläche hinzufügen, Fläche abziehen und Flächen schneiden, lässt die Originale jedoch bestehen, sofern nicht anders angegeben. `operation`: union (Fläche einer der beiden Formen), intersection (Fläche beider Formen), difference (erste Form minus zweite Form: `firstUuid` minus `secondUuid`; eine Linie als zweite Form zerteilt die erste an den Stellen, an denen sie diese vollständig durchquert) oder symmetricDifference (Fläche, die genau in einer der Formen liegt).

`firstUuid` und `secondUuid` bezeichnen zwei verschiedene Formen: Linien, Rechtecke, abgerundete Rechtecke, Ovale, Kreisbögen und Kreise, Polygone (keine Freihandpolygone) und Polylinien; keine Texte, Gruppen, Symbole, Plug-in-Objekte oder 3D-Objekte. Sie müssen koplanar sein. Liegen sie in verschiedenen Ebenen (z. B. eine in der Bildschirmebene und eine in der Konstruktionsebene in 2D-Plan), wird die zweite Form wie bei ändern &gt; Fläche hinzufügen zunächst in die Ebene der ersten verschoben. Dadurch ändert sich die Ebene des zweiten Originals und das Ergebnis erhält `planesAligned` true. Nicht koplanare Formen werden abgewiesen.

Ein offenes Polygon oder eine offene Polylinie mit mindestens drei Scheitelpunkten gilt durch eine gerade Kante als geschlossen, ein Kreisbogen durch seine Sehne. Eine Linie umschließt keine Fläche und ist daher nur als zweite Form einer Differenzoperation sinnvoll. Die erste Form muss sich auf einer Ebene, in einer Symboldefinition oder in einer Gruppe darin befinden (nicht in einer Wand, einem Plug-in-Objekt, einem Ansichtsbereich oder einer darin enthaltenen Gruppe). Das gilt auch für die zweite Form, wenn der Aufruf sie ändert (`deleteOriginals` auf both oder Verschieben in die Ebene der ersten Form).

Die Ergebnisse sind neue 2D-Objekte beliebigen Typs (meist Polylinien, ein Polygon oder eine Kopie einer Form, wenn keine neue Kontur erforderlich ist, z. B. eine Kopie der ersten Form bei einer Differenz ohne Überlappung) mit den grafischen Attributen, Datensätzen und der Sichtbarkeit der ersten Form sowie deren Klasse (`class` weist eine andere Klasse zu; `useClassAttributes` lässt die Attribute der Klasse folgen).

Sie werden im Container der ersten Form vor deren Objekten abgelegt, entsperrt und nur bei `select` ausgewählt; die Begrenzungen der umgebenden Gruppen werden entsprechend angepasst. Die Originale bleiben abgesehen von einer Ebenenausrichtung unverändert, sofern `deleteOriginals` nicht auf first oder both gesetzt ist (Standard: none). Wenn keine Form entsteht, wird nichts gelöscht. Eine gesperrte erste Form kann kombiniert werden. Eine gesperrte Form, die durch den Aufruf gelöscht oder in eine andere Ebene verschoben würde, wird abgewiesen.

Eine Kombination ohne Fläche (Schnittmenge sich nicht überlappender Formen, Differenz, bei der die zweite Form die erste vollständig abdeckt oder die erste Form eine Linie ist, symmetrische Differenz identischer Formen; Vectorworks meldet einen Modellierungsfehler auf dieselbe Weise) gilt als Erfolg ohne Formen und mit einem `note`. Eine leere Vereinigung ist ein Fehler. `name` benennt das einzelne Ergebnis. Der Aufruf wird abgewiesen, wenn die Kombination mehrere Formen ergibt oder ein anderes Objekt diesen Namen trägt.

Alle Argumente werden geprüft, bevor Änderungen vorgenommen werden. Ein abgewiesener Aufruf ändert nichts. Ein Aufruf entspricht einem Schritt zum Rückgängigmachen, der auch die Ebenen ausgerichteter Formen wiederherstellt. Zurückgegeben werden `operation`, `count`, `shapes` (Referenzen der neuen Objekte), `deleted` (UUIDs der gelöschten Originale), `planesAligned` (true, wenn die Ebenen der Formen angeglichen wurden) und bei ausbleibenden Ergebnissen `note`.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `operation` | string | Ja | Einer von: `union`, `intersection`, `difference`, `symmetricDifference`. |
| `firstUuid` | string | Ja | UUID der ersten Form. Die neuen Formen übernehmen deren Klasse, Attribute und Container. |
| `secondUuid` | string | Ja | UUID der zweiten Form. Muss sich von `firstUuid` unterscheiden. |
| `deleteOriginals` | string |  | Einer von: `none`, `first`, `both`. |
| `class` | string |  | Erstellungsoption: Klasse des neuen Objekts; wird bei Bedarf erstellt. Siehe [Erstellungsoptionen](Common.md#optionen-zur-erstellung). |
| `name` | string |  | Erstellungsoption: Name des neuen Objekts. |
| `select` | boolean |  | Erstellungsoption: neues Objekt auswählen. |
| `useClassAttributes` | boolean |  | Erstellungsoption: mit `class` auch die Attribute des neuen Objekts anhand der Klasse festlegen. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `operation` | Ausgeführte Operation. |
| `count` | Anzahl der neuen Formen. |
| `shapes` | Neue Formen als [Objektreferenzen](Common.md#objektreferenzen). |
| `deleted` | UUIDs der gelöschten Originale; leer, wenn nichts gelöscht wurde. |
| `planesAligned` | `true`, wenn die zweite Form in die Ebene der ersten verschoben wurde; andernfalls ausgelassen. |
| `note` | Nur wenn keine Ergebnisse vorliegen: Grund sowie Hinweis, dass nichts erstellt und die Originale beibehalten wurden, auch bei `deleteOriginals`. |


### createText

Erstellt ein Textobjekt.

> **Wirkung:** Bearbeiten · **Risiko:** niedrig · **Rückgängig:** ein Schritt "MCP: createText" · **Bei runToolBatch:** ja

**Details**

Erstellt an `origin`, dem Ausrichtungspunkt des Texts (Welteinheiten), ein Textobjekt aus `text` (UTF-8; "\n" und "\r\n" werden zu "\r", dem Zeilentrennzeichen von Textobjekten; höchstens 16383 UTF-16-Codeeinheiten). Der Text wird so positioniert, dass der durch die Ausrichtung festgelegte Punkt dort liegt. Mit der optionalen Angabe `width` (positive Welteinheiten) wird ein Text mit Zeilenumbruch erstellt, dessen Zeilen an dieser Breite umgebrochen werden.

Die Formatierung des gesamten Texts wird in dieser Reihenfolge angewendet, sodass explizite Werte die Einstellungen des Textstils überschreiben: `textStyle` (Name oder Ressourcen-UUID eines Textstils der Zeichnung; `getResources` listet diese mit resourceType `textStyle`; "" für keinen Textstil) oder `textStyleByClass` true (der Text übernimmt den Textstil seiner Klasse); `font` (Schriftname); `size` (Welteinheiten) oder `sizePoints` (Punkte); die Stil-Flags `bold`, `italic`, `underline`, `outline` und `shadow` (Kontur und Schatten werden nur unter macOS angezeigt); `color`.

Anschließend folgt das Layout: `horizontalAlignment` (left|center|right|justify), `verticalAlignment` (topBox|topBaseline|centerBox|bottomBaseline|bottomBox), `lineSpacing` (single|oneAndHalf|double oder custom mit `leading`, dem Zeilenabstand in Welteinheiten), `angle` (Bogenmaß, gegen den Uhrzeigersinn um den Ursprung) und `flipped` (vertikal gespiegelt). Nicht angegebene Werte stammen aus den Textstandards des Dokuments.

Alle Argumente werden geprüft, bevor etwas erstellt wird. Ein falscher Typ, ein unbekannter Name, eine unbekannte Schrift oder ein unbekannter Textstil, die gleichzeitige Angabe von `size` und `sizePoints` sowie eine nicht positive Breite, Größe oder ein nicht positiver Zeilenabstand führen zur Abweisung des Aufrufs; es wird dann nichts erstellt. Die Erstellungsoptionen (class, name, select, useClassAttributes) werden vor der Formatierung angewendet. Zurückgegeben werden die Objekt-Referenz und `applied` (true/false für jedes angegebene Formatierungs- und Layoutargument, einschließlich origin; leading unter lineSpacing). `getText` liest den Text wieder aus.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `text` | string | Ja | Der Text (UTF-8); "\n" beginnt eine neue Zeile. |
| `origin` | [Punkt](Common.md#punkte) | Ja | Ausrichtungspunkt des Texts in Welteinheiten. |
| `width` | number |  | Umbruchbreite in Welteinheiten; erzeugt einen Text mit Zeilenumbruch. |
| `textStyle` | string |  | Name oder Ressourcen-UUID eines Textstils; eine leere Zeichenfolge bedeutet keinen Textstil. |
| `textStyleByClass` | boolean |  | Textstil der Klasse verwenden. |
| `font` | string |  | Schriftname. |
| `size` | number |  | Textgröße in Welteinheiten (nicht zusammen mit `sizePoints` verwenden). |
| `sizePoints` | number |  | Textgröße in Punkt. |
| `color` | [Farbe](Common.md#farben) |  | Textfarbe. |
| `bold` | boolean |  | Fettschrift. |
| `italic` | boolean |  | Kursivschrift. |
| `underline` | boolean |  | Unterstreichung. |
| `outline` | boolean |  | Kontur (nur unter macOS angezeigt). |
| `shadow` | boolean |  | Schatten (nur unter macOS angezeigt). |
| `horizontalAlignment` | string |  | Einer von: `left`, `center`, `right`, `justify`. |
| `verticalAlignment` | string |  | Einer von: `topBox`, `topBaseline`, `centerBox`, `bottomBaseline`, `bottomBox`. |
| `lineSpacing` | string |  | Einer von: `single`, `oneAndHalf`, `double`, `custom`. |
| `leading` | number |  | Zeilenabstand in Welteinheiten für benutzerdefinierten Zeilenabstand. |
| `angle` | number |  | Drehung im Bogenmaß gegen den Uhrzeigersinn um den Ursprung. |
| `flipped` | boolean |  | Text vertikal spiegeln. |
| `class` | string |  | Erstellungsoption: Klasse des neuen Objekts; wird bei Bedarf erstellt. Siehe [Erstellungsoptionen](Common.md#optionen-zur-erstellung). |
| `name` | string |  | Erstellungsoption: Name des neuen Objekts. |
| `select` | boolean |  | Erstellungsoption: neues Objekt auswählen. |
| `useClassAttributes` | boolean |  | Erstellungsoption: mit `class` auch die Attribute des neuen Objekts anhand der Klasse festlegen. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `applied` | `true` oder `false` unter dem Namen jedes geschriebenen Arguments: `origin` (immer), Formatierungsargumente (`textStyle`, `textStyleByClass`, `font`, `size`, `sizePoints`, jedes angegebene Stil-Flag, `color`) und Layoutargumente (`horizontalAlignment`, `verticalAlignment`, `lineSpacing` mit `leading`, `angle`, `flipped`). `width` wird nicht aufgeführt: Es bestimmt die Form des neuen Texts. |


### getText

Liest Inhalt, Zeichenformatierung, Stil und Layout eines Textobjekts aus.

> **Wirkung:** Nur lesend · **Risiko:** niedrig · **Rückgängig:** keine · **Bei runToolBatch:** zulässig

**Details**

Liest ein Textobjekt anhand von UUID, Namen oder Index aus. Zeichenindizes sind 0-basierte UTF-16-Codeeinheiten (ein Zeichen außerhalb der Basic Multilingual Plane zählt als zwei); Längen werden in Welteinheiten, Winkel im Bogenmaß angegeben. Zurückgegeben werden `text` (vollständig; Zeilen durch "\r" getrennt), `length`, `lineCount` und `lines`, die umbrochenen Zeilen als { start, text }, paginiert wie bei `findObjects` mit `lineLimit` (Standard 100) und `lineOffset` (count, returned, offset, limit, truncated, nextOffset, items); `origin` (Ausrichtungspunkt), `angle`, `flipped` (vertikal gespiegelt) und `boxCorners` (oben links, oben rechts, unten rechts und unten links des Textfelds, mit dem Text gedreht); `horizontalAlignment`, `verticalAlignment`, `lineSpacing` (mit `leading` bei benutzerdefiniertem Zeilenabstand), `width` und `wrapped`; die Formatierung von Zeichen 0: `font`, `size` (Welteinheiten), `sizePoints`, `style` (Namen der Flags: bold, italic, underline, outline, shadow), `customStyle` (diagonalFraction|verticalFraction|superscript|subscript, sofern vorhanden), `color` und `tracking` (Zeichenabstand, 1 = normal); `textStyle` des gesamten Texts: { byClass, name, uuid }, { byClass: true } für eine Klasse ohne Textstil, { mixed: true }, wenn Zeichen unterschiedlichen Textstilen folgen, oder null, wenn kein Textstil verwendet wird; `styleRuns`, die Formatierungsbereiche in Reihenfolge als { start, length } mit denselben Formatierungsschlüsseln und dem jeweiligen `textStyle`, paginiert mit `runLimit` (Standard 100) und `runOffset`; `tabStops` ({ offset in Welteinheiten vom linken Textrand, Ausrichtung left|right|center|decimal }, nach offset sortiert), `repeatingTabStop` (Abstand gleichmäßig verteilter Tabulatoren, andernfalls 0), `tightFill` und `isLinkedToRecord`.

Die Namen und Schlüssel entsprechen den Parametern von `createText` und `editText`.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `uuid` | string |  | Über UUID referenzieren (bevorzugt). Siehe [Objektreferenzen](Common.md#objektreferenzen). |
| `name` | string |  | Über den Namen referenzieren. |
| `index` | integer |  | Über den internen Index referenzieren. |
| `lineLimit` | integer |  | Maximale Anzahl von `lines` auf der Seite; mindestens 1. Standard 100. |
| `lineOffset` | integer |  | Anzahl der zu überspringenden Zeilen; darf nicht negativ sein. Standard 0. |
| `runLimit` | integer |  | Maximale Anzahl von `styleRuns` auf der Seite; mindestens 1. Standard 100. |
| `runOffset` | integer |  | Anzahl der zu überspringenden Formatierungsdurchläufe; darf nicht negativ sein. Standard 0. |

### editText

Bearbeitet Inhalt und Formatierung eines Textobjekts.

> **Wirkung:** Bearbeiten · **Risiko:** niedrig · **Rückgängig:** ein Schritt "MCP: editText" · **Bei runToolBatch:** ja

**Details**

Bearbeitet ein Textobjekt anhand von UUID, Namen oder Index; der Aufruf entspricht einem Schritt zum Rückgängigmachen. Zeichenindizes und -anzahlen sind 0-basierte UTF-16-Codeeinheiten (ein Zeichen außerhalb der Basic Multilingual Plane zählt als zwei); Längen werden in Welteinheiten, Winkel im Bogenmaß angegeben. In neuem Text werden "\n" und "\r\n" zu "\r", dem Zeilentrennzeichen von Textobjekten. Alle Argumente werden vor Änderungen geprüft. Ein falscher Typ, ein unbekannter Name, eine unbekannte Schrift oder ein unbekannter Textstil, ein Bereich außerhalb des Texts, eine nicht positive Größe, Breite, Zeilenabstand, Intervall- oder Offset-Angabe, ein leerer Text, mehrere Inhaltsänderungen, ein Aufruf ohne Änderung oder ein Objekt, das kein Textobjekt ist, führen zur Abweisung des Aufrufs; es wird nichts geändert.

Die Änderungen werden in dieser Reihenfolge ausgeführt. 1. Inhalt, höchstens eine der folgenden Aktionen: `setText` (ersetzt den gesamten Text, der die Formatierung des letzten Zeichens übernimmt; alter und neuer Text dürfen zusammen höchstens 16383 Codeeinheiten umfassen), `insertText` { text, at } (fügt vor Zeichen `at` ein; ein Index gleich der Textlänge fügt am Ende an; der neue Text übernimmt die Formatierung des vorangehenden Zeichens, bei 0 die des ersten Zeichens), `appendText`, `deleteText` { first, count } (`count` ist standardmäßig der Rest des Texts; der gesamte Text kann nicht gelöscht werden). 2.

Die Zeichenformatierung des Bereichs ab `first` (Standard 0) und mit `count` Zeichen (Standard: Rest des Texts) nach der Inhaltsänderung erfolgt in dieser Reihenfolge: `textStyle` (Name oder Ressourcen-UUID eines Textstils der Zeichnung; "" löst den Bereich vom Textstil und behält seine Formatierung bei) oder `textStyleByClass` true (der Bereich übernimmt den Textstil der Textklasse); `font`; `size` (Welteinheiten) oder `sizePoints` (Punkte); die Stil-Flags `bold`, `italic`, `underline`, `outline` und `shadow` (nur angegebene Flags werden geändert; jedes Zeichen behält seine übrigen Flags und seinen Hoch-, Tief- oder Bruchstil bei); `color`. 3.

**Layout:** `horizontalAlignment` und `verticalAlignment` (eine neue Ausrichtung lässt den Text an seiner Position und verschiebt wie in Vectorworks den Ursprung, also den Ausrichtungspunkt), `lineSpacing` (custom erfordert `leading`), `width` (Umbruchbreite; der Text wird an dieser Breite umbrochen), `wrapped` (true bricht bei der aktuellen Breite um, false trennt Zeilen nur an Zeilentrennzeichen; nicht gemeinsam mit `width` auf false setzen), `origin` (verschiebt den Text so, dass sein Ausrichtungspunkt dort liegt), `angle` und `flipped`. Das Layout wird nach der Formatierung angewendet, da ein auf den gesamten Text angewendeter Textstil auch Ausrichtung und Zeilenabstand festlegt. 4.

**Tabulatoren:** `repeatingTabStop` (verteilt alle Tabulatoren in Intervallabständen neu, linksbündig), `removeTabStops` (Indizes in den `tabStops` von `getText`; Tabulator 0 kann nicht entfernt werden), `moveTabStop` { index, offset } (Index nach den Entfernungen; Tabulatoren bleiben nach offset sortiert), `addTabStops` (Offsets neuer linksbündiger Tabulatoren). 5. `unlinkFromRecord` true löst einen mit einem Datensatzfeld verknüpften Text davon (wird bei anderem Textobjekt abgewiesen). Zurückgegeben werden die Objekt-Referenz, `applied` (true/false für jedes angegebene Argument; leading unter lineSpacing), `length` und `lineCount`.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `uuid` | string |  | Über UUID referenzieren (bevorzugt). Siehe [Objektreferenzen](Common.md#objektreferenzen). |
| `name` | string |  | Über den Namen referenzieren. |
| `index` | integer |  | Über den internen Index referenzieren. |
| `setText` | string |  | Ersetzt den gesamten Text. Darf nicht leer sein; alter und neuer Text zusammen höchstens 16383 UTF-16-Codeeinheiten. |
| `insertText` | object |  | Fügt Text vor einem Zeichen ein. `text` und `at` angeben. |
| `insertText.text` | string | Ja | Einzufügender Text; darf nicht leer sein; `"\n"` beginnt eine neue Zeile. Zusammen mit dem alten Text höchstens 16383 UTF-16-Codeeinheiten. |
| `insertText.at` | integer | Ja | Zeichenindex, vor dem der Text eingefügt wird: 0 ist der Anfang, die Textlänge das Ende. |
| `appendText` | string |  | Am Ende anzufügender Text. Darf nicht leer sein; zusammen mit dem alten Text höchstens 16383 UTF-16-Codeeinheiten. |
| `deleteText` | object |  | Löscht einen Zeichenbereich. Der gesamte Text darf nicht gelöscht werden. |
| `deleteText.first` | integer |  | Index des ersten zu löschenden Zeichens, kleiner als die Textlänge. Standard 0. |
| `deleteText.count` | integer |  | Anzahl der zu löschenden Zeichen, vom ersten bis zum Ende des Texts. Bereich 1 bis Restlänge. Standard: Restlänge. |
| `first` | integer |  | Erstes Zeichen des Formatierungsbereichs, auf den die Formatierung nach der Inhaltsänderung angewendet wird. Standard 0. Wird nur gelesen, wenn ein Formatierungsargument angegeben ist (`textStyle`, `textStyleByClass`, `font`, `size`, `sizePoints`, ein Stil-Flag oder `color`). |
| `count` | integer |  | Anzahl der Zeichen des Bereichs, vom ersten bis zum Ende des Texts. Bereich 1 bis Restlänge. Standard: Restlänge. |
| `width` | number |  | Umbruchbreite in Welteinheiten; erzeugt einen Text mit Zeilenumbruch. |
| `wrapped` | boolean |  | True bricht bei der aktuellen Breite um, false trennt Zeilen nur an Zeilentrennzeichen; nicht gemeinsam mit `width` auf false setzen. |
| `repeatingTabStop` | number |  | Verteilt alle Tabulatoren in Intervallabständen neu, linksbündig. |
| `removeTabStops` | array of integer |  | Indizes in den `tabStops` von `getText`; Tabulator 0 kann nicht entfernt werden. |
| `moveTabStop` | object |  | Verschiebt einen Tabulator. `index` und `offset` angeben. |
| `moveTabStop.index` | integer | Ja | Index des Tabulators unter den nach `removeTabStops` verbleibenden; 0 ist der erste. |
| `moveTabStop.offset` | number | Ja | Neuer Versatz von der linken Textkante in Welteinheiten. Muss positiv sein. |
| `addTabStops` | array of number |  | Offsets neuer linksbündiger Tabulatoren. |
| `unlinkFromRecord` | boolean |  | `true` löst einen mit einem Datensatzfeld verknüpften Text (laut `isLinkedToRecord` von getText); bei einem nicht verknüpften Text wird der Aufruf abgelehnt. `false` ändert nichts und fügt keinen Eintrag zu `applied` hinzu. |
| `textStyle` | string |  | Name oder Ressourcen-UUID eines Textstils; eine leere Zeichenfolge bedeutet keinen Textstil. |
| `textStyleByClass` | boolean |  | Textstil der Klasse verwenden. |
| `font` | string |  | Schriftname. |
| `size` | number |  | Textgröße in Welteinheiten (nicht zusammen mit `sizePoints` verwenden). |
| `sizePoints` | number |  | Textgröße in Punkt. |
| `color` | [Farbe](Common.md#farben) |  | Textfarbe. |
| `bold` | boolean |  | Fettschrift. |
| `italic` | boolean |  | Kursivschrift. |
| `underline` | boolean |  | Unterstreichung. |
| `outline` | boolean |  | Kontur (nur unter macOS angezeigt). |
| `shadow` | boolean |  | Schatten (nur unter macOS angezeigt). |
| `horizontalAlignment` | string |  | Einer von: `left`, `center`, `right`, `justify`. |
| `verticalAlignment` | string |  | Einer von: `topBox`, `topBaseline`, `centerBox`, `bottomBaseline`, `bottomBox`. |
| `lineSpacing` | string |  | Einer von: `single`, `oneAndHalf`, `double`, `custom`. |
| `leading` | number |  | Zeilenabstand in Welteinheiten für benutzerdefinierten Zeilenabstand. |
| `origin` | [Punkt](Common.md#punkte) |  | Ausrichtungspunkt des Texts in Welteinheiten. |
| `angle` | number |  | Drehung im Bogenmaß gegen den Uhrzeigersinn um den Ursprung. |
| `flipped` | boolean |  | Text vertikal spiegeln. |

**Ergebnis**

Die [Objektreferenz](Common.md#objektreferenzen) und:

| Schlüssel | Beschreibung |
|---|---|
| `applied` | `true` oder `false` unter dem Namen jedes angegebenen Arguments: `setText`, `insertText`, `appendText` oder `deleteText`; Formatierungsargumente (`textStyle`, `textStyleByClass`, `font`, `size`, `sizePoints`, jedes angegebene Stil-Flag, `color`); Layoutargumente (`horizontalAlignment`, `verticalAlignment`, `lineSpacing` mit `leading`, `width`, `wrapped`, `origin`, `angle`, `flipped`); `repeatingTabStop`, `removeTabStops`, `moveTabStop`, `addTabStops` und `unlinkFromRecord`. `removeTabStops` und `addTabStops` werden nur bei nicht leerer Liste gemeldet, `unlinkFromRecord` nur bei `true`. |
| `length` | Textlänge nach dem Aufruf in UTF-16-Codeeinheiten. |
| `lineCount` | Anzahl der Zeilen nach dem Umbruch. |

Fehler: `object not found (provide 'uuid', 'name' or 'index')`; `the object is not a text object: getText and editText take text objects only`; `give at most one of 'setText', 'insertText', 'appendText' and 'deleteText' per call`; `'<key>' must be a text that is not empty`; `'<key>' is too long …: Vectorworks edits text objects of at most 16383 UTF-16 code units`; `'insertText' must be { text, at }` und `'insertText' needs 'at', a character index from 0 (the start) to <length> (the end of the text)`; `'deleteText' must be { first, count }`, `'deleteText' is outside the text: …` und `'deleteText' cannot delete the whole text: …`; `the formatting range is outside the text: …`; `'width' wraps the text at that width; it cannot be combined with 'wrapped' false`; `tab stop 0 cannot be removed: …`; `'removeTabStops' must be an array of indices of the <n> tab stops of the text (getText 'tabStops')`; `'moveTabStop' must be { index, offset }: …`; `'addTabStops' must be an array of offsets (world units, positive)`; `'unlinkFromRecord': the text is not linked to a record field`; Ablehnungen der Formatierung und des Layouts von `createText`; `nothing to change: give a content, formatting, layout, tab stop or 'unlinkFromRecord' argument`. Ein abgelehnter Aufruf ändert nichts (`rolledBack`).


## Objects

> **Gruppe:** `Objects` · **Gruppen-ID:** `objects` · **Standardmäßig aktiv:** Ja · **Risikostufe:** mittel · **Werkzeuge:** 12

**Beliebige Objekte finden, prüfen und bearbeiten: Attribute, Transformationen, Container, Plug-in-Parameter und Datensätze.**

Prüfen und bearbeiten Sie beliebige vorhandene Objekte anhand ihrer stabilen UUID: nach Kriterien oder durch Auswahl eines Punkts suchen; Informationen (auch 3D-Begrenzungsrahmen und Mitglieder von Gruppen, Ebenen und anderen Containern) sowie grafische Attribute auslesen; Stift, Füllung, Deckkraft, Marker und Schlagschatten festlegen; Attribute zwischen Objekten kopieren; transformieren, umbenennen, neu klassifizieren, zwischen Containern verschieben (auch in eine Gruppe), Gruppierungen aufheben, in Polygone/Polylinien umwandeln, Plug-in-Parameter (PIO) mit Typen und Popup-Auswahlen auslesen oder schreiben sowie angehängte Benutzerdatensätze auslesen.

Lesen Sie die Definition eines installierten Plug-in-Objekts anhand seines universellen Namens aus (`getPluginDefinition`: kind, parameters, pop-up choices) und erstellen Sie Plug-in-Objekte, für die keine Gruppe ein eigenes Erstellungswerkzeug bietet (`createPluginObject`; Türen, Fenster, Pflanzen, Datentags usw. werden mit eigenen Werkzeugen erstellt, die hier benannt werden). Identifizieren Sie ein Plug-in-Objekt anhand von `parametricName`. Leiten Sie seinen Typ niemals allein aus dem Typcode, angehängten Datensätzen oder seiner IFC-Entität ab.

IFC-Daten (IFC-Entität, standardmäßige und benutzerdefinierte Eigenschaftssätze, IFC-Eigenschaftstypen) werden mit den IFC-Gruppenwerkzeugen `getObjectIFCData`, `getIFCPsetDefinition` und `listIFCPsets` ausgelesen, nicht mit `getObjectRecords` oder `getResourceDetails`. Suchergebnisse geben mit `count` die Gesamtzahl der Treffer und mit `truncated` an, ob die Liste abgeschnitten wurde. Eine abgeschnittene Liste ist nur eine Stichprobe; leiten Sie daraus niemals Gesamtzahlen, Abwesenheit oder Eigenschaften aller Objekte ab.

Jede Bearbeitung wird als eigener, benannter und rückgängig machbarer Vectorworks-Vorgang ausgeführt.

| Werkzeug | Wirkung | Risiko | Zusammenfassung |
|---|---|---|---|
| [`findObjects`](#findobjects) | Nur lesend | niedrig | Findet Objekte, die einer Kriterienzeichenfolge entsprechen. |
| [`getObjectsAtPoint`](#getobjectsatpoint) | Nur lesend | niedrig | Findet die Objekte an einem Punkt. |
| [`getObjectInfo`](#getobjectinfo) | Nur lesend | niedrig | Gibt Identität, Klasse, Ebene, Begrenzungen, Status und Container eines Objekts zurück. |
| [`getObjectAttributes`](#getobjectattributes) | Nur lesend | niedrig | Gibt die grafischen Attribute eines Objekts zurück. |
| [`setObjectAttributes`](#setobjectattributes) | Bearbeiten | mittel | Legt grafische Attribute eines Objekts fest: Stift, Füllung, Deckkraft, Marker, Schlagschatten und mehr. |
| [`copyAttributes`](#copyattributes) | Bearbeiten | mittel | Kopiert die grafischen Attribute eines Objekts auf andere Objekte. |
| [`editObject`](#editobject) | Bearbeiten | mittel | Verschiebt, dreht, skaliert, spiegelt, dupliziert, gruppiert neu, wandelt um, setzt zurück oder löscht ein Objekt oder ändert dessen Namen und Klasse. |
| [`getObjectParameters`](#getobjectparameters) | Nur lesend | niedrig | Liest die Parameter eines Plug-in-Objekts aus. |
| [`getObjectRecords`](#getobjectrecords) | Nur lesend | niedrig | Liest die an ein Objekt angehängten Datensätze aus. |
| [`setObjectParameter`](#setobjectparameter) | Bearbeiten | mittel | Schreibt einen oder mehrere Parameter eines Plug-in-Objekts. |
| [`getPluginDefinition`](#getplugindefinition) | Nur lesend | niedrig | Beschreibt ein installiertes Plug-in-Objekt: Typ, Parameter und Popup-Auswahlen. |
| [`createPluginObject`](#createpluginobject) | Bearbeiten | mittel | Erstellt ein Plug-in-Objekt ohne eigenes Erstellungswerkzeug. |

### findObjects

Findet Objekte, die einer Kriterienzeichenfolge entsprechen.

> **Wirkung:** Nur lesend · **Risiko:** niedrig · **Rückgängig:** keine · **Bei runToolBatch:** zulässig

**Details**

Sucht Objekte anhand einer Vectorworks-Kriterienzeichenfolge (z. B. "(T=RECT)", "(C='My Class')", "ALL"). Gibt uuid/type/typeName/name für bis zu `limit` Treffer (Standard 200) ab `offset` (Standard 0) zurück. `count` ist die Gesamtzahl der Treffer, `returned` die Anzahl der unter `objects` aufgelisteten Objekte und `truncated` ist true, wenn weitere Treffer folgen. Rufen Sie diese ab, indem Sie `offset` auf `nextOffset` setzen, oder übergeben Sie `countOnly`, um nur `count` zu erhalten.

Offsets bleiben nur gültig, solange die Zeichnung unverändert ist. Verwenden Sie zum Zählen oder Prüfen, ob Objekte vorhanden sind, bevorzugt gezielte Kriterien mit `countOnly`, statt "ALL" aufzulisten. Die Suche umfasst Objekte auf Konstruktionsebenen und Layoutebenen, innerhalb von Gruppen sowie in Ansichtsbereichen auf Konstruktionsebenen. `notSearched` listet die im Kriterium fehlenden Bereichs-Schlüsselwörter auf: INSYMBOL (in Symboldefinitionen), INOBJECT (in Plug-in-Objekten), INVIEWPORT (Ansichtsbereich-Anmerkungen und Ausschnittgruppen), INOBJPATH und INOBJPROFILE (Pfade von Plug-in-Objekten und Profilgruppen). Stellen Sie diese voran, um dort zu suchen ("INSYMBOL & INOBJECT & (T=RECT)").

Ein count von 0 bedeutet lediglich, dass innerhalb dieses Bereichs keine Treffer gefunden wurden. Parametrische Plug-in-Objekte (Typ 86) geben außerdem `parametricName` und `localizedParametricName` zurück, die den Objekttyp angeben (z. B. "Window", "Door", "Plant"). Suchen Sie Plug-in-Objekte anhand ihres `parametricName` mit Kriterien wie "(PON=`Window`)". Kriterien, die nicht kompiliert werden können, geben einen Fehler mit der Ursache zurück. Gültige Kriterien ohne Treffer ergeben count 0.

Namen in den Kriterien (Datensatz, Feld, Klasse, Plug-in) werden nicht validiert: Ein falsch geschriebener oder nicht vorhandener Name wird kompiliert und ergibt ebenfalls count 0 (interne Datensatznamen `NNA_` werden mit einem Fehler abgewiesen). "(N='...')" stimmt ausschließlich mit dem Vectorworks-Objektnamen überein, ohne Beachtung der Groß-/Kleinschreibung. Ohne Platzhalter ist es ein exakter Name; '\*' entspricht einer beliebigen Zeichenfolge und '?' einem einzelnen Zeichen ("(N='\*door\*')"). Diese Platzhalter können nicht maskiert werden.

Schließen Sie Zeichenfolgen in einfache Anführungszeichen ein und verdoppeln Sie ein Apostroph im Namen ("(N='O''Brien')"). Ein exakter Name findet das Objekt unabhängig von seinem Speicherort; ein Platzhaltermuster durchsucht Objekte auf Konstruktions- und Layoutebenen einschließlich Gruppen. N stimmt nicht mit IFC-Namen, IFC-Eigenschaftssatzwerten oder Datensatzfeldwerten überein. Lesen Sie IFC-Daten mit den Werkzeugen der IFC-Gruppe aus.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `criteria` | string | Ja | Vectorworks-Kriterienzeichenfolge, zum Beispiel `(T=RECT)` oder `(C='My Class')`. Sie muss kompilierbar sein und darf kein internes IFC-Datensatzformat referenzieren. |
| `limit` | integer |  | Seitennavigation: maximale Anzahl zurückzugebender Elemente (mindestens 1). Siehe [Seitennavigation](Common.md#seitennavigation). |
| `offset` | integer |  | Seitennavigation: Anzahl zu überspringender Elemente (Standard 0). |
| `countOnly` | boolean |  | Seitennavigation: nur die Anzahl zurückgeben, nicht die Elemente. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `count` | Gesamtzahl der Treffer. |
| `returned` | Anzahl der Objekte in `objects` (0 bei `countOnly`). |
| `offset` | Verwendeter `offset`. |
| `limit` | Verwendeter `limit`. |
| `truncated` | `true`, wenn weitere Treffer auf nachfolgenden Seiten vorhanden sind. |
| `nextOffset` | `offset` der nächsten Seite; nur vorhanden, wenn `truncated` `true` ist. |
| `objects` | Treffer als [Objektreferenzen](Common.md#objektreferenzen); bei `countOnly` ausgelassen. |
| `notSearched` | Liste der Bereichsschlüsselwörter, die in den Kriterien nicht vorkommen (siehe Details); immer vorhanden, auch bei `countOnly`. |


### getObjectsAtPoint

Findet die Objekte an einem Punkt.

> **Wirkung:** Nur lesend · **Risiko:** niedrig · **Rückgängig:** keine · **Bei runToolBatch:** zulässig

**Details**

Sucht Objekte an einem Welt-`point`, optional innerhalb eines `radius`. `traverse` legt fest, welche Objekte geprüft werden (standardmäßig visibleObjects, außerdem allObjects, selectedObjects, editableObjects), und `descend`, welche Container betreten werden (standardmäßig none, außerdem groups, viewports, all). Unbekannte Werte führen zu einem Fehler; die angewendeten Werte werden zurückgegeben. Gibt bis zu `limit` Objekt-Referenzen (Standard 50) ab `offset` zurück, beginnend mit dem vordersten Objekt, zusammen mit `count`, `returned`, `truncated` und `nextOffset` wie bei `findObjects`. `countOnly` gibt nur `count` zurück.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `point` | [Punkt](Common.md#punkte) | Ja | Ein Punkt. |
| `radius` | number |  | Radius in Welteinheiten. |
| `traverse` | string |  | Einer von: `allObjects`, `visibleObjects`, `selectedObjects`, `editableObjects`. |
| `descend` | string |  | Einer von: `none`, `groups`, `viewports`, `all`. |
| `limit` | integer |  | Seitennavigation: maximale Anzahl zurückzugebender Elemente (mindestens 1). Siehe [Seitennavigation](Common.md#seitennavigation). |
| `offset` | integer |  | Seitennavigation: Anzahl zu überspringender Elemente (Standard 0). |
| `countOnly` | boolean |  | Seitennavigation: nur die Anzahl zurückgeben, nicht die Elemente. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `count`, `returned`, `offset`, `limit`, `truncated`, `nextOffset`, `objects` | The page of objects found, as for [`findObjects`](#findobjects) (there is no `notSearched`). |
| `traverse` | Verwendeter Wert für `traverse`. |
| `descend` | Verwendeter Wert für `descend`. |


### getObjectInfo

Gibt Identität, Klasse, Ebene, Begrenzungen, Status und Container eines Objekts zurück.

> **Wirkung:** Nur lesend · **Risiko:** niedrig · **Rückgängig:** keine · **Bei runToolBatch:** zulässig

**Details**

Gibt Identität, Klasse, Ebene, Begrenzungen, Fläche, Umfang und den Sichtbarkeits-/Sperr-/Auswahlstatus eines Objekts sowie dessen internen `index` zurück. Als Objekt-Referenzen werden außerdem der übergeordnete `parent`-Container (Ebene, Gruppe, Symboldefinition usw.) und die `next`-/`previous`-Nachbarn in der Stapelreihenfolge des übergeordneten Containers angegeben (`next` wird weiter vorne gezeichnet). Plug-in-Objekte geben außerdem `parametricName` und `localizedParametricName` zurück.

`bounds3D` { min: {x,y,z}, max: {x,y,z} }, `center3D` {x,y,z} und `size3D` {x,y,z} (Ausdehnungen entlang X, Y und Z; z ist die Höhe) geben den 3D-Begrenzungsrahmen in Welteinheiten mit Welt-Z-Koordinate an (einschließlich der Höhe einer Konstruktionsebene; innerhalb einer Symboldefinition in deren Koordinaten). Sie werden weggelassen, wenn der Rahmen bei z = 0 flach ist, wie bei einem 2D-Objekt in der Ebenen- oder Bildschirmebene ohne Höhenlage (verwenden Sie `bounds`) und bei einer Gruppe oder Ebene, die ausschließlich solche Objekte enthält.

`memberCount` ist die Anzahl der direkten Mitglieder eines Objekts, das Mitglieder enthält: einer Ebene, Gruppe oder Symboldefinition (auch 0) sowie jedes anderen Objekts mit Mitgliedern, etwa den Einfügungen einer Wand, dem Profil eines Extrusionskörpers oder der Geometrie eines Plug-in-Objekts oder Dachs (generiert: Vectorworks baut diese Geometrie beim Zurücksetzen des Objekts neu auf, daher bleiben Änderungen daran nicht erhalten).

Bei `includeMembers` true listet `members` die Mitglieder als Objekt-Referenzen in Stapelreihenfolge (hinten nach vorne) auf, paginiert wie bei `findObjects`: bis zu `memberLimit` (Standard 50) ab `memberOffset` (Standard 0), mit `count`, `returned`, `truncated`, `nextOffset` und `objects`. `name` ist der exakte Vectorworks-Objektname. Wird er nicht gefunden, bedeutet das nicht, dass kein Objekt diesen Wert in einem Datensatzfeld, in IFC-Daten oder einem Plug-in-Parameter enthält. Suchen Sie danach mit Kriterien in `findObjects`.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `uuid` | string |  | Über UUID referenzieren (bevorzugt). Siehe [Objektreferenzen](Common.md#objektreferenzen). |
| `name` | string |  | Über den Namen referenzieren. |
| `index` | integer |  | Über den internen Index referenzieren. |
| `includeMembers` | boolean |  | Standard: `false`. |
| `memberLimit` | integer |  | Mit `includeMembers`: maximale Anzahl der Elemente auf der Seite (mindestens 1). Standard 50. |
| `memberOffset` | integer |  | Mit `includeMembers`: Anzahl der zu überspringenden Elemente (mindestens 0). Standard 0. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `uuid`, `type`, `typeName`, `name` | Die [Objektreferenz](Common.md#objektreferenzen); ein Plug-in-Objekt enthält außerdem `parametricName` und `localizedParametricName`. |
| `bounds` | 2D-Begrenzungs-[Rechteck](Common.md#rechtecke) in Welteinheiten. |
| `bounds3D`, `center3D`, `size3D` | The 3D bounding box, its center and its size (see Details); left out when the box is flat at z = 0. |
| `area`, `perimeter` | The area and the perimeter, for an object that has them. |
| `visible`, `locked`, `selected` | The state of the object. |
| `class`, `layer` | The names of the class and of the layer of the object. |
| `index` | Interner Index des Objekts. |
| `memberCount` | Anzahl der direkten Elemente bei einem Objekt, das Elemente enthält. |
| `members` | Mit `includeMembers` für ein Objekt, das `memberCount` meldet (Ebene, Gruppe, Symboldefinition oder Objekt mit mindestens einem Element): Seite der Elemente `{ count, returned, offset, limit, truncated, nextOffset, objects }`; `objects` enthält Objektreferenzen in Stapelreihenfolge. |
| `parent`, `next`, `previous` | The container and the neighbours in its stacking order, as object references; each is left out when there is none, and the drawing header is never given as `parent`. |


### getObjectAttributes

Gibt die grafischen Attribute eines Objekts zurück.

> **Wirkung:** Nur lesend · **Risiko:** niedrig · **Rückgängig:** keine · **Bei runToolBatch:** zulässig

**Details**

Gibt die grafischen Attribute eines Objekts zurück: Stift (foreColor/backColor als RGB und foreColorIndex/backColorIndex in der Dokumentfarbtabelle, Linienstärke in mils/mm, Rohstil, Linientyp, Stilart, Deckkraft, Klassen-Flags und Linientypzuordnung), Füllung (Farben und Farbindexe, Typ, Stil, Füllressource, Deckkraft, Klassen-Flags), Füllzuordnung (Ursprung, Achsenendpunkte, Offsets, Achsenlängen, Winkel, Wiederholen/Spiegeln/Umkehren usw.) für Schraffur-, Kachel-, Verlaufs- und Bildfüllungen, Anfangs- und Endmarker mit beginningVisible/endVisible, Schlagschatten, Objektdeckkraft mit opacityByClass sowie die geerbte Klasse.

Die Schlüssel entsprechen den von `setObjectAttributes` akzeptierten Schlüsseln, mit Ausnahme der schreibgeschützten Werte pen styleKind und fill type.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `uuid` | string |  | Über UUID referenzieren (bevorzugt). Siehe [Objektreferenzen](Common.md#objektreferenzen). |
| `name` | string |  | Über den Namen referenzieren. |
| `index` | integer |  | Über den internen Index referenzieren. |

### setObjectAttributes

Legt grafische Attribute eines Objekts fest: Stift, Füllung, Deckkraft, Marker, Schlagschatten und mehr.

> **Wirkung:** Bearbeiten · **Risiko:** mittel · **Rückgängig:** ein Schritt "MCP: setObjectAttributes" · **Bei runToolBatch:** ja

**Details**

Legt grafische Attribute eines Objekts fest; geändert werden nur die angegebenen Elemente. `pen` und `fill` akzeptieren foreColor/backColor (RGB) oder foreColorIndex/backColorIndex (Index in der Dokumentfarbtabelle), Deckkraft 0–100, none/solid, true für colorsByClass (Alias byClass) und styleByClass zum Verwenden der Klassenwerte sowie true/false für opacityByClass. Für den Stift sind außerdem `lineWeightMm` oder `lineWeightMils`, `lineType` (interner Linientypindex), `style` (roher Stiftstil), lineWeightByClass und `lineTypeMapping` { localMapping, flipHorizontal, flipVertical, scale } möglich. Für die Füllung sind zudem `resource` (interner Index einer Schraffur, Kachel, eines Verlaufs oder Bilds) und `style` (roher Füllstil) möglich.

`fillMapping` positioniert eine Schraffur-, Kachel-, Verlaufs- oder Bildfüllung: origin, iAxisEnd, jAxisEnd (Weltpunkte), xOffset, yOffset, iAxisLength, jAxisLength (Welteinheiten), angle (Bogenmaß), repeat, mirror, flip, maintainAspectRatio, geometryType, localMapping. `markers` legt Anfangs-/Endmarker einer Linie, deren Sichtbarkeit (beginningVisible/endVisible) oder byClass fest.

`dropShadow` ist ein Boolean oder ein Objekt. Auf oberster Ebene werden außerdem `opacity`, `opacityByClass`, `allByClass` und `class` unterstützt.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `uuid` | string |  | Über UUID referenzieren (bevorzugt). Siehe [Objektreferenzen](Common.md#objektreferenzen). |
| `name` | string |  | Über den Namen referenzieren. |
| `index` | integer |  | Über den internen Index referenzieren. |
| `pen` | object |  | Stiftattribute; nur angegebene Elemente werden geändert. |
| `pen.foreColor` | [Farbe](Common.md#farben) |  | Vordergrundfarbe (RGB). |
| `pen.backColor` | [Farbe](Common.md#farben) |  | Hintergrundfarbe (RGB). |
| `pen.foreColorIndex` | integer |  | Vordergrundfarbe als Index in der Dokumentfarbtabelle. |
| `pen.backColorIndex` | integer |  | Hintergrundfarbe als Index in der Dokumentfarbtabelle. |
| `pen.lineWeightMm` | number |  | Linienstärke in Millimetern. |
| `pen.lineWeightMils` | integer |  | Linienstärke in mils. |
| `pen.lineType` | integer |  | Interner Linientypindex. |
| `pen.style` | integer |  | Roher Stiftstil. |
| `pen.opacity` | integer |  | Deckkraft, 0–100. |
| `pen.none` | boolean |  | `true` setzt die Stiftart auf keine Linie. `false` bewirkt nichts. |
| `pen.solid` | boolean |  | `true` setzt die Stiftart auf durchgezogen. `false` bewirkt nichts. |
| `pen.byClass` | boolean |  | Entspricht `pen.colorsByClass`. |
| `pen.colorsByClass` | boolean |  | `true` übernimmt die Stiftfarben aus der Klasse. `false` bewirkt nichts. |
| `pen.styleByClass` | boolean |  | `true` übernimmt die Stiftart aus der Klasse. `false` bewirkt nichts. |
| `pen.lineWeightByClass` | boolean |  | `true` übernimmt die Linienstärke aus der Klasse. `false` bewirkt nichts. |
| `pen.opacityByClass` | boolean |  | `true` übernimmt die Stiftdeckkraft aus der Klasse; `false` beendet diese Übernahme. |
| `pen.lineTypeMapping` | object |  | Legt fest, wie der Linientyp auf den Stift abgebildet wird; geändert werden nur angegebene Elemente. |
| `pen.lineTypeMapping.localMapping` | boolean |  | Lokale Zuordnungsmarkierung des Linientyps. |
| `pen.lineTypeMapping.flipHorizontal` | boolean |  | Linientyp horizontal spiegeln. |
| `pen.lineTypeMapping.flipVertical` | boolean |  | Linientyp vertikal spiegeln. |
| `pen.lineTypeMapping.scale` | number |  | Skalierung der Linientypzuordnung. |
| `fill` | object |  | Füllungsattribute; nur angegebene Elemente werden geändert. |
| `fill.foreColor` | [Farbe](Common.md#farben) |  | Vordergrundfarbe (RGB). |
| `fill.backColor` | [Farbe](Common.md#farben) |  | Hintergrundfarbe (RGB). |
| `fill.foreColorIndex` | integer |  | Vordergrundfarbe als Index in der Dokumentfarbtabelle. |
| `fill.backColorIndex` | integer |  | Hintergrundfarbe als Index in der Dokumentfarbtabelle. |
| `fill.opacity` | integer |  | Deckkraft, 0–100. |
| `fill.style` | integer |  | Roher Füllstil. |
| `fill.resource` | integer |  | Interner Index einer Schraffur, Kachel, eines Verlaufs oder Bilds. |
| `fill.none` | boolean |  | `true` setzt die Füllung auf keine. `false` bewirkt nichts. |
| `fill.solid` | boolean |  | `true` setzt die Füllung auf durchgezogen. `false` bewirkt nichts. |
| `fill.byClass` | boolean |  | Entspricht `fill.colorsByClass`. |
| `fill.colorsByClass` | boolean |  | `true` übernimmt die Füllfarben aus der Klasse. `false` bewirkt nichts. |
| `fill.styleByClass` | boolean |  | `true` übernimmt die Füllart aus der Klasse. `false` bewirkt nichts. |
| `fill.opacityByClass` | boolean |  | `true` übernimmt die Fülldeckkraft aus der Klasse; `false` beendet diese Übernahme. |
| `fillMapping` | object |  | Legt die Positionierung einer Schraffur-, Kachel-, Verlaufs- oder Bildfüllung fest; geändert werden nur angegebene Elemente. |
| `fillMapping.origin` | [Punkt](Common.md#punkte) |  | Ursprung der Zuordnung (Weltpunkt). |
| `fillMapping.iAxisEnd` | [Punkt](Common.md#punkte) |  | Endpunkt der I-Achse (Weltpunkt). |
| `fillMapping.jAxisEnd` | [Punkt](Common.md#punkte) |  | Endpunkt der J-Achse (Weltpunkt). |
| `fillMapping.xOffset` | number |  | Versatz in X-Richtung, in Welteinheiten. |
| `fillMapping.yOffset` | number |  | Versatz in Y-Richtung, in Welteinheiten. |
| `fillMapping.iAxisLength` | number |  | Länge der I-Achse in Welteinheiten. |
| `fillMapping.jAxisLength` | number |  | Länge der J-Achse in Welteinheiten. |
| `fillMapping.angle` | number |  | Winkel in Radiant. |
| `fillMapping.repeat` | boolean |  | Gibt an, ob die Füllung wiederholt wird. |
| `fillMapping.mirror` | boolean |  | Gibt an, ob die Füllung gespiegelt wird. |
| `fillMapping.flip` | boolean |  | Gibt an, ob die Füllung umgekehrt wird. |
| `fillMapping.maintainAspectRatio` | boolean |  | Gibt an, ob das Seitenverhältnis der Füllung beibehalten wird. |
| `fillMapping.geometryType` | integer |  | Geometrietyp des Farbverlaufs (linear, radial usw.) als Ganzzahl. |
| `fillMapping.localMapping` | boolean |  | `true` ordnet die Füllung relativ zum Objekt zu (lokale Zuordnung), `false` relativ zur Welt. |
| `markers` | object |  | Linienendmarkierungen; geändert werden nur angegebene Elemente. Siehe [Linienendmarkierungen](Attributes.md#linienendmarkierungen). |
| `markers.beginning` | [Marker](Attributes.md#linienendmarkierungen) |  | Markierung am Linienanfang. Beim Schreiben wird `byClass` für das Objekt deaktiviert. |
| `markers.end` | [Marker](Attributes.md#linienendmarkierungen) |  | Markierung am Linienende. Beim Schreiben wird `byClass` für das Objekt deaktiviert. |
| `markers.beginningVisible` | boolean |  | Anfangsmarkierung anzeigen (`true`) oder ausblenden (`false`). |
| `markers.endVisible` | boolean |  | Endmarkierung anzeigen (`true`) oder ausblenden (`false`). |
| `markers.byClass` | boolean |  | `true` verwendet die Markierungen der Klasse. `false` bewirkt nichts. |
| `opacity` | integer |  | Deckkraft, 0–100. |
| `opacityByClass` | boolean |  | `true` übernimmt die Deckkraft des Objekts aus der Klasse. `false` bewirkt nichts. |
| `dropShadow` | [Schlagschatten](Attributes.md#schlagschatten) |  | Boolean (Schlagschatten ein oder aus) oder Objekt mit den Schlagschattenelementen `byClass` und `delete`. |
| `allByClass` | boolean |  | `true` setzt jedes unterstützte Attribut auf „nach Klasse“: Stift- und Füllfarben sowie -arten, Linienstärke, Deckkraft, Markierungen und Schlagschatten. `false` bewirkt nichts. |
| `class` | string |  | Name der Klasse. |

**Ergebnis**

| Argument | Schlüssel in `applied` |
|---|---|
| `pen.foreColor`, `pen.backColor` | `penForeColor`, `penBackColor` |
| `pen.foreColorIndex`, `pen.backColorIndex` | `penForeColorIndex`, `penBackColorIndex` |
| `pen.lineWeightMm`, `pen.lineWeightMils` | `lineWeightMm`, `lineWeightMils` |
| `pen.opacity` | `penOpacity`. |
| `pen.style`, `pen.lineType` | `penStyle`, `penLineType` |
| `pen.none`, `pen.solid` | `penNone`, `penSolid` |
| `pen.byClass` or `pen.colorsByClass` | `penByClass` |
| `pen.styleByClass`, `pen.lineWeightByClass`, `pen.opacityByClass` | `penStyleByClass`, `lineWeightByClass`, `penOpacityByClass` |
| `pen.lineTypeMapping.localMapping`, `flipHorizontal`, `flipVertical`, `scale` | `penLocalMapping`, `penFlipHorizontal`, `penFlipVertical`, `penScale` |
| `fill.foreColor`, `fill.backColor` | `fillForeColor`, `fillBackColor` |
| `fill.foreColorIndex`, `fill.backColorIndex` | `fillForeColorIndex`, `fillBackColorIndex` |
| `fill.opacity`, `fill.style`, `fill.resource` | `fillOpacity`, `fillStyle`, `fillResource` |
| `fill.none`, `fill.solid` | `fillNone`, `fillSolid` |
| `fill.byClass` or `fill.colorsByClass` | `fillByClass` |
| `fill.styleByClass`, `fill.opacityByClass` | `fillStyleByClass`, `fillOpacityByClass` |
| `fillMapping.origin`, `iAxisEnd`, `jAxisEnd` | `mapOrigin`, `mapIAxisEnd`, `mapJAxisEnd` |
| `fillMapping.xOffset`, `yOffset`, `iAxisLength`, `jAxisLength`, `angle` | `mapXOffset`, `mapYOffset`, `mapIAxisLength`, `mapJAxisLength`, `mapAngle` |
| `fillMapping.repeat`, `mirror`, `flip`, `maintainAspectRatio`, `geometryType`, `localMapping` | `mapRepeat`, `mapMirror`, `mapFlip`, `mapAspect`, `mapGeometryType`, `mapLocalMapping` |
| `markers.beginning`, `markers.end` | `beginningMarker`, `endMarker` |
| `markers.beginningVisible`, `markers.endVisible` | `beginningMarkerVisible`, `endMarkerVisible` |
| `markers.byClass` | `markersByClass`. |
| `opacity`, `opacityByClass` | `opacity`, `opacityByClass` |
| `dropShadow` (a boolean, or an object with the members) | `dropShadow` |
| `dropShadow.byClass`, `dropShadow.delete` | `dropShadowByClass`, `dropShadowDeleted` |
| `class`, `allByClass` | `class`, `allByClass` |


### copyAttributes

Kopiert die grafischen Attribute eines Objekts auf andere Objekte.

> **Wirkung:** Bearbeiten · **Risiko:** mittel · **Rückgängig:** ein Schritt "MCP: copyAttributes" · **Bei runToolBatch:** ja

**Details**

Kopiert alle grafischen Attribute des Quellobjekts (Stift, Füllung, Marker, Schlagschatten, Deckkraft) auf ein `targetUuid` oder mehrere `targetUuids`. Setzen Sie `includeClass`, um den Zielen auch die Klasse der Quelle zuzuweisen.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `uuid` | string |  | Über UUID referenzieren (bevorzugt). Siehe [Objektreferenzen](Common.md#objektreferenzen). |
| `name` | string |  | Über den Namen referenzieren. |
| `index` | integer |  | Über den internen Index referenzieren. |
| `targetUuid` | string |  | UUID des Objekts, auf das die Attribute kopiert werden. |
| `targetUuids` | array of string |  | UUIDs mehrerer Zielobjekte. Bei gemeinsamer Angabe werden diese zu `targetUuid` hinzugefügt. |
| `includeClass` | boolean |  | `true` weist außerdem jedem Ziel die Klasse des Quellobjekts zu. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `uuid` | UUID des Zielobjekts wie angegeben. |
| `applied` | `true`, wenn die Attribute kopiert wurden; `false`, wenn Vectorworks dies abgelehnt hat. Hier ein einzelner Boolean, kein Objekt. |
| `class` | Nur mit `includeClass`: `true`, wenn die Klasse gesetzt wurde. |
| `err` | `object not found`, wenn kein Objekt mit dieser UUID existiert. In diesem Fall fehlt `applied`. |


### editObject

Verschiebt, dreht, skaliert, spiegelt, dupliziert, gruppiert neu, wandelt um, setzt zurück oder löscht ein Objekt oder ändert dessen Namen und Klasse.

> **Wirkung:** Bearbeiten · **Risiko:** mittel · **Rückgängig:** ein Schritt "MCP: editObject" · **Bei runToolBatch:** ja

**Details**

Transformiert oder aktualisiert ein Objekt. `action`: move (`offset`), rotate (`angle` im Bogenmaß, `center`), scale (`scaleX`,`scaleY`,`center`), mirror (`axisStart`,`axisEnd`), duplicate (`offset`), moveToContainer (in die Gruppe oder Symboldefinition `containerUuid` oder auf die Ebene `layer`), addToGroup (in die Gruppe `groupUuid`), ungroup (eine Gruppe), convertToPolygon / convertToPolyline (optional `keepOriginal`, `resolution`; gibt das neue Objekt zurück), reset (Plug-in-Objekt neu generieren) oder delete.

Ohne Angabe einer Aktion werden lediglich die angegebenen Werte aus `name`, `class`, `visible`, `locked`, `selected` angewendet. moveToContainer verschiebt Objekte ausschließlich zwischen Ebenen, Gruppen und Symboldefinitionen: Das Ziel muss eine Ebene, eine Symboldefinition oder eine Gruppe darin sein; ebenso der Container, in dem sich das Objekt befindet. Eine Ebene als Objekt, ein Ziel innerhalb des Objekts selbst sowie Objekte in oder in eine Wand, ein Plug-in-Objekt oder ein Dach werden abgewiesen. Das Verschieben einer Tür oder eines Fensters in eine Wand oder aus der Wand, in die es eingesetzt ist, würde die Wand beschädigen und wird nicht unterstützt (fügen Sie Türen und Fenster in Vectorworks in Wände ein).

Beim Verschieben in eine Symboldefinition oder eine darin enthaltene Gruppe wird ein Objekt abgewiesen, das eine Instanz dieses Symbols oder eines Symbols enthält, das wiederum in beliebiger Tiefe eine Instanz davon enthält: Ein in sich selbst verschachteltes Symbol erzeugt eine Endlosschleife. Die Aktion kann nicht mit einem neuen `name` (der eigene, identifizierende Name des Objekts ist zulässig), `class`, `visible`, `locked` oder `selected` kombiniert werden (ändern Sie diese Werte in einem anderen Aufruf). Ein abgewiesener oder fehlgeschlagener Verschiebevorgang ändert nichts.

Die Begrenzungen der Gruppen, aus denen das Objekt entfernt und in die es eingefügt wird, sowie der umgebenden Gruppen werden aktualisiert. Bearbeiten &gt; Rückgängig macht das Verschieben rückgängig und stellt die vorherigen Gruppenbegrenzungen wieder her. addToGroup entspricht moveToContainer in die Gruppe `groupUuid`, mit denselben Prüfungen, Abweisungen und Rückgängig-Funktionen. Ein `groupUuid`, das keine Gruppe bezeichnet (sondern z. B. eine Ebene oder Symboldefinition), wird abgewiesen: Verwenden Sie dafür moveToContainer. ungroup hebt eine Gruppe mit Vectorworks' Befehl „Gruppierung auflösen“ auf: Die Mitglieder werden in ihrer Reihenfolge an die Position der Gruppe in der Stapelreihenfolge des Containers der Gruppe verschoben. Die Gruppe wird gelöscht; die ehemaligen Mitglieder werden als Objekt-Referenzen in Stapelreihenfolge (`members`) mit ihrem Container (`parent`) zurückgegeben.

Die Mitglieder sind anschließend ausgewählt (andere ausgewählte Objekte bleiben ausgewählt). Es ist nicht garantiert, dass an die Gruppe angehängte Datensätze an die Mitglieder übertragen werden. Abgewiesen werden Objekte, die keine Gruppe sind, gesperrte Gruppen (entsperren Sie sie zuerst), Gruppen innerhalb einer Wand, eines Plug-in-Objekts oder Dachs, die gerade bearbeitete Gruppe (oder eine Gruppe, die sie enthält) sowie neue Angaben für name, class, visible, locked oder selected. Mitglieder, die in der aktuellen Detailstufe ausgeblendet sind (möglich in Symboldefinitionen), werden wie beim Befehl „Gruppierung auflösen“ mit der Gruppe gelöscht und unter `deletedMemberCount` gezählt.

Bearbeiten &gt; Rückgängig stellt die Gruppe samt Mitgliedern wieder her.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `uuid` | string |  | Über UUID referenzieren (bevorzugt). Siehe [Objektreferenzen](Common.md#objektreferenzen). |
| `name` | string |  | Über den Namen referenzieren. |
| `index` | integer |  | Über den internen Index referenzieren. |
| `action` | string |  | Einer von: `move`, `rotate`, `scale`, `mirror`, `duplicate`, `moveToContainer`, `addToGroup`, `ungroup`, `convertToPolygon`, `convertToPolyline`, `reset`, `delete`. |
| `offset` | [Punkt](Common.md#punkte) |  | Verschiebung für `move` und `duplicate`, in Welteinheiten. Standard (0, 0). |
| `angle` | number |  | Winkel im Bogenmaß, gegen den Uhrzeigersinn. |
| `center` | [Punkt](Common.md#punkte) |  | Mittelpunkt. |
| `scaleX` | number |  | Skalierungsfaktor in X-Richtung für `scale`. Standard 1. |
| `scaleY` | number |  | Skalierungsfaktor in Y-Richtung für `scale`. Standard 1. |
| `axisStart` | [Punkt](Common.md#punkte) |  | Erster Punkt der Spiegelachse für `mirror`. |
| `axisEnd` | [Punkt](Common.md#punkte) |  | Zweiter Punkt der Spiegelachse für `mirror`. Muss sich von `axisStart` unterscheiden. |
| `containerUuid` | string |  | UUID der Gruppe oder Symboldefinition, in die das Objekt mit `moveToContainer` verschoben wird. Hat Vorrang vor `layer`. |
| `layer` | string |  | Name der Ebene, auf die das Objekt mit `moveToContainer` verschoben wird. |
| `groupUuid` | string |  | UUID der Gruppe, der das Objekt mit `addToGroup` hinzugefügt wird. |
| `keepOriginal` | boolean |  | Für `convertToPolygon` und `convertToPolyline`: `true` behält das Originalobjekt bei. Standard `false`. |
| `resolution` | integer |  | Für `convertToPolygon`: Auflösung der Konvertierung als ganze Zahl (ohne Angabe 0). Für `convertToPolyline` nicht verwendet. |
| `class` | string |  | Name einer bestehenden Klasse, der das Objekt zugewiesen wird. Siehe Hinweis oben. |
| `useClassAttributes` | boolean |  | Mit `class`: `true` lässt außerdem die Attribute des Objekts den Klassenattributen folgen. |
| `visible` | boolean |  | Objekt einblenden (`true`) oder ausblenden (`false`). |
| `locked` | boolean |  | Objekt sperren (`true`) oder entsperren (`false`). |
| `selected` | boolean |  | Objekt auswählen (`true`) oder Auswahl aufheben (`false`). |

**Ergebnis**

| Aktion | Ergebnis |
|---|---|
| `delete` | `{ deleted }`: `true`, wenn das Objekt gelöscht wurde. |
| `duplicate`, `convertToPolygon`, `convertToPolyline` | Die [Objektreferenz](Common.md#objektreferenzen) des neuen Objekts. |
| `moveToContainer`, `addToGroup` | The object reference of the moved object, with `applied` set to `{ "moveToContainer": true }` or `{ "addToGroup": true }`. |
| `ungroup` | `{ ungrouped, parent, members, deletedMemberCount }`: `ungrouped` ist `true`, `parent` der Container, der die Elemente nun enthält, `members` sind die früheren Elemente als Objektreferenzen in Stapelreihenfolge; `deletedMemberCount` wird nur angegeben, wenn ausgeblendete Elemente mit der Gruppe gelöscht wurden. |
| `move`, `rotate`, `scale`, `mirror`, `reset`, no action, or an unknown action | The object reference of the object, with `applied`. It has an entry for the action (`move`, `rotate`, `scale`, `mirror` or `reset`) and an entry for each of `name`, `visible`, `locked`, `selected` and `class` that was given. An entry is `true` when Vectorworks took the value and `false` when it refused it. |


### getObjectParameters

Liest die Parameter eines Plug-in-Objekts aus.

> **Wirkung:** Nur lesend · **Risiko:** niedrig · **Rückgängig:** keine · **Bei runToolBatch:** zulässig

**Details**

Liest AUSSCHLIESSLICH den Parameter-Datensatz eines parametrischen Plug-in-Objekts (PIO) aus, z. B. Türen, Fenster, Pflanzen, Belagsflächen und Datentags. Prüfen Sie zuvor, ob `findObjects`/`getObjectInfo` ein `parametricName` zurückgibt. Gibt den parametrischen Namen, die Liste der Parameternamen und deren Werte als Zeichenfolgen zurück. Optional können Sie die Auswahl auf bestimmte `names` beschränken. Die optionale Angabe `includeDefinitions` (Standard false) ergänzt `definitions`: für jeden ausgelesenen Parameter dessen `type` (integer, boolean, real, text, dimension, popUp, angle, coordLocX usw.) und `localizedName`; bei popUp außerdem die universellen `choices`. `parameters` und `values` bleiben unverändert.

Die optionale Angabe `curated` (Standard false) ergänzt für Öffnungsparameter von Türen und Fenstern ein `curated`-Array der Form { param, label, value, display }: label ist der lokalisierte Parametername, display die lokalisierte Popup-Auswahl für Öffnungs-Popups (andernfalls oder falls nicht verfügbar null). Die Ausgabe `values` bleibt unverändert. Andere Plug-in-Objekte geben ein leeres `curated`-Array zurück.

Für alle anderen Objekte (Linien, Rechtecke, Kreisbögen, Polygone, Gruppen, Symbole, Wände usw.) wird ein Fehler zurückgegeben. Benutzerdatensätze (an Objekte angehängte Datensatzformate) werden niemals ausgelesen. Verwenden Sie dafür `getObjectRecords`.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `uuid` | string |  | Über UUID referenzieren (bevorzugt). Siehe [Objektreferenzen](Common.md#objektreferenzen). |
| `name` | string |  | Über den Namen referenzieren. |
| `index` | integer |  | Über den internen Index referenzieren. |
| `names` | array of string |  | Namen der zu lesenden Parameter. Standard: alle Parameter. Siehe Hinweis oben. |
| `includeDefinitions` | boolean |  | Standard: `false`. |
| `curated` | boolean |  | Standard: `false`. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `parametricName` | Universalname des Plug-in-Objekts. |
| `parameters` | Namen aller Parameter in Deklarationsreihenfolge. Wird ausgelassen, wenn `names` angegeben ist. |
| `values` | Werte als Text: `{ "<parameter>": "<value>" }`. |
| `definitions` | Nur mit `includeDefinitions`: `{ "<parameter>": { localizedName, type, choices } }` für jeden gelesenen Parameter. `type` ist der in den Details angegebene Typname. `choices` (allgemeine Auswahlmöglichkeiten) wird nur für `popUp` angegeben. |
| `curated` | Nur mit `curated`: Array aus `{ param, label, value, display }`. Bei Plug-in-Objekten, die weder Tür noch Fenster sind, leer. |


### getObjectRecords

Liest die an ein Objekt angehängten Datensätze aus.

> **Wirkung:** Nur lesend · **Risiko:** niedrig · **Rückgängig:** keine · **Bei runToolBatch:** zulässig

**Details**

Liest die an ein beliebiges Objekt (mit oder ohne Plug-in) angehängten Benutzerdatensätze aus. Für jedes angehängte, nicht interne Datensatzformat werden Name, lokalisierter Name und Feldwerte als Zeichenfolgen zurückgegeben. Mit `records` können Sie die Ausgabe optional auf bestimmte Datensatzformatnamen beschränken (universeller oder lokalisierter Name, ohne Beachtung der Groß-/Kleinschreibung). Interne IFC-Datensätze werden ausgelassen: Lesen Sie IFC-Daten eines Objekts (Entität, standardmäßige und benutzerdefinierte Eigenschaftssätze, IFC-Eigenschaftstypen) mit `getObjectIFCData` und Eigenschaftssatzdefinitionen mit `listIFCPsets` und `getIFCPsetDefinition` aus.

Der Parameter-Datensatz eines Plug-in-Objekts ist nicht enthalten. Verwenden Sie dafür `getObjectParameters`. Um Objekte anhand eines Datensatzwerts zu finden, verwenden Sie `findObjects` mit Kriterien wie "(`MyRecord`.`MyField` &gt; 1)". Felddefinitionen eines Datensatzformats werden mit `getResourceDetails` ausgelesen.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `uuid` | string |  | Über UUID referenzieren (bevorzugt). Siehe [Objektreferenzen](Common.md#objektreferenzen). |
| `name` | string |  | Über den Namen referenzieren. |
| `index` | integer |  | Über den internen Index referenzieren. |
| `records` | array of string |  | Universeller oder lokalisierter Name, ohne Beachtung der Groß-/Kleinschreibung. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `name` | Universalname des Datensatzformats. |
| `localizedName` | Lokalisierter Name. Wird ausgelassen, wenn das Format keinen hat. |
| `values` | Feldwerte als Text: `{ "<field>": "<value>" }`. |


### setObjectParameter

Schreibt einen oder mehrere Parameter eines Plug-in-Objekts.

> **Wirkung:** Bearbeiten · **Risiko:** mittel · **Rückgängig:** ein Schritt "MCP: setObjectParameter" · **Bei runToolBatch:** ja

**Details**

Schreibt Parameter eines parametrischen Plug-in-Objekts. Legen Sie entweder ein einzelnes `name`/`value` fest (Typ gemäß Parameterdefinition oder durch `type` erzwungen) oder übergeben Sie ein `params`-Objekt mit Name/Wert-Paaren. Numerische Parameter akzeptieren auch numerische Zeichenfolgen (z. B. "5", "5.0"). Ein Wert, der nicht in den Parametertyp umgewandelt werden kann, wird nicht geschrieben und mit false gemeldet (`ok` oder der zugehörige Eintrag in `applied`). Anschließend wird das Objekt neu generiert.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `uuid` | string |  | Über UUID referenzieren (bevorzugt). Siehe [Objektreferenzen](Common.md#objektreferenzen). |
| `name` | string |  | Über den Namen referenzieren. |
| `index` | integer |  | Über den internen Index referenzieren. |
| `value` | string or number or integer or boolean |  | Typ aus der Parameterdefinition oder durch `type` erzwungen. |
| `type` | string |  | Einer von: `string`, `real`, `int`, `bool`. |
| `params` | object |  | Rohe Plug-in-Parameter `{ "ParamName": value }`. Siehe [Plug-in-Parameter](Common.md#plug-in-parameter). |

**Ergebnis**

| Form | Ergebnis |
|---|---|
| `params` | `{ applied }`: `{ "<parameter>": true or false }` für jeden Namen in `params`. |
| `name` and `value` | `{ ok }`: `true` when the value was written. |


### getPluginDefinition

Beschreibt ein installiertes Plug-in-Objekt: Typ, Parameter und Popup-Auswahlen.

> **Wirkung:** Nur lesend · **Risiko:** niedrig · **Rückgängig:** keine · **Bei runToolBatch:** zulässig

**Details**

Beschreibt ein installiertes Plug-in-Objekt (PIO) ohne Instanz anhand seines exakten universellen Namens `universalName` (Groß-/Kleinschreibung beachten: der von `findObjects` und `getObjectInfo` gemeldete `parametricName`, z. B. "Drawing Label2" oder "Revision Cloud"). Gibt `universalName`, `localizedName` und `kind` zurück. `kind` bestimmt, wie `createPluginObject` das Objekt platziert: point, linear, rectangle und custom erfordern `position`; path2D und path3D erfordern `pathUuid`. Außerdem werden `dedicatedTool` { tool, group } zurückgegeben, falls eine Gruppe ein eigenes Erstellungswerkzeug dafür hat (`createPluginObject` weist es ab; verwenden Sie das entsprechende Werkzeug), sowie `parameters` in Deklarationsreihenfolge: [{ name (universeller Name für `params` in `createPluginObject` und `setObjectParameter`), localizedName, type (integer, boolean, real, text, dimension, popUp, angle, coordLocX usw.), defaultValue (als Text), choices (universelle Auswahlmöglichkeiten eines popUp-Parameters) }].

Bei unbekanntem oder anders geschriebenem Namen, nicht installiertem Plug-in, Menübefehl oder Werkzeug wird ein Fehler zurückgegeben. Es werden keine Änderungen vorgenommen: Fehlt das Parameter-Datensatzformat des Plug-ins im Dokument, wird es ausschließlich zum Auslesen innerhalb eines privaten Rückgängig-Ereignisses definiert, das anschließend zurückgenommen wird. Daher bleiben weder das Format noch ein Rückgängig-Schritt bestehen.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `universalName` | string | Ja | Exakter, zwischen Groß- und Kleinschreibung unterscheidender universalName des Plug-in-Objekts: der von `findObjects` und `getObjectInfo` gemeldete `parametricName`. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `universalName` | Universalname. |
| `localizedName` | Lokalisierter Name. Wird ausgelassen, wenn keiner vorhanden ist. |
| `kind` | Legt fest, wie `createPluginObject` das Plug-in-Objekt platziert, wie in den Details benannt. |
| `dedicatedTool` | `{ tool, group }`. Nur vorhanden, wenn eine Gruppe ein eigenes Erstellungswerkzeug für dieses Plug-in-Objekt hat. |
| `parameters` | Parameter in Deklarationsreihenfolge: `{ name, localizedName, type, defaultValue, choices }`. `defaultValue` ist Text. `choices` (allgemeine Auswahlmöglichkeiten) wird nur für `popUp` angegeben. |


### createPluginObject

Erstellt ein Plug-in-Objekt ohne eigenes Erstellungswerkzeug.

> **Wirkung:** Bearbeiten · **Risiko:** mittel · **Rückgängig:** ein Schritt "MCP: createPluginObject" · **Bei runToolBatch:** ja

**Details**

Erstellt ein Plug-in-Objekt (PIO) anhand seines exakten universellen Namens `universalName` (Groß-/Kleinschreibung beachten; `getPluginDefinition` gibt Typ und Parameter zurück). Nur für Plug-ins ohne eigenes Erstellungswerkzeug. Türen, Fenster, Bodenplatten, Stützen, Treppen, Pflanzen, Belagsflächen, Landschaftsflächen, Geländemodifikatoren, Grundstücksgrenzen, Geländemodelle, Höhenkoten, vorhandene Bäume, Beleuchtungsgeräte, ConnectCAD-Geräte und -Anschlüsse, Datentags und Plankopf-Rahmen werden abgewiesen; die Fehlermeldung nennt das zu verwendende Werkzeug (`dedicatedTool` von `getPluginDefinition`).

Der Typ bestimmt die Platzierung: Ein Plug-in-Objekt vom Typ point, linear, rectangle oder custom wird an `position` (Weltpunkt) erstellt und optional um `angle` (Bogenmaß) gedreht. Ein path2D- oder path3D-Objekt benötigt `pathUuid`, aber weder `position` noch `angle`: ein vorhandenes Objekt, das direktes Mitglied der aktiven Ebene (oder einer Gruppe ist, die auf einer Ebene bearbeitet wird) und vom neuen Objekt als Pfad übernommen wird, wie es auch die Plug-in-Werkzeuge mit einer ausgewählten Form tun. Übernommen wird das Objekt selbst, keine Kopie: Es wird von der Ebene entfernt, und Vectorworks wandelt eine 2D-Form in eine Polylinie um.

Ein Pfad in einer gerade bearbeiteten Symboldefinition oder einer darin enthaltenen Gruppe wird abgewiesen: Vectorworks protokolliert Pfadänderungen nur, wenn der Pfad auf einer Ebene liegt. Andernfalls würde „Rückgängig“ zusammen mit dem neuen Objekt auch den Pfad löschen. Erstellen Sie das Objekt anhand eines Pfads auf einer Ebene und verschieben Sie es mit `editObject` `moveToContainer` in die Symboldefinition. Ein path2D-Plug-in-Objekt kann ein Rechteck, abgerundetes Rechteck, Oval, einen Kreisbogen, ein Polygon, Freihandpolygon oder eine Polylinie verwenden; path3D zusätzlich ein 3D-Polygon, eine NURBS-Kurve oder NURBS-Fläche.

Bearbeiten &gt; Rückgängig entfernt das neue Objekt und stellt den Pfad wieder her. Mit den optionalen `params` { "ParamName": value } werden Parameter anhand ihres universellen Namens wie bei `params` von `setObjectParameter` festgelegt. Danach wird das Objekt neu generiert; `applied` meldet jeden Parameter. Die Erstellungsoptionen class, useClassAttributes, name und select werden angewendet. Alles wird vor Änderungen geprüft: Ein unbekannter oder anders geschriebener Name, ein fehlendes oder zusätzliches `pathUuid` oder `position`, ein Pfadobjekt außerhalb des aktiven Containers, in einer Symboldefinition oder von einem anderen Formtyp, ein unbekannter Parametername oder ein Wert, der nicht zum Parametertyp passt, führt zur Abweisung; es wird nichts erstellt.

Lässt das Plug-in das Objekt an dieser Stelle oder einen Parameter nicht zu, schlägt der Aufruf fehl und wird rückgängig gemacht. Zurückgegeben wird die Referenz des neuen Objekts mit `kind` und bei einem Pfad-Plug-in-Objekt dessen `pathObject`. Wie bei der Verwendung des Plug-ins wird das Parameter-Datensatzformat des Plug-ins dem Dokument hinzugefügt, falls es fehlt (bei abgewiesenem oder fehlgeschlagenem Aufruf wird auch dieses rückgängig gemacht).

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `universalName` | string | Ja | Groß-/Kleinschreibung beachten; `getPluginDefinition` gibt Typ und Parameter zurück. |
| `position` | [Punkt](Common.md#punkte) |  | Ein Weltpunkt. |
| `angle` | number |  | Winkel im Bogenmaß, gegen den Uhrzeigersinn. |
| `pathUuid` | string |  | UUID des Objekts, das den Pfad bereitstellt. |
| `params` | object |  | Rohe Plug-in-Parameter `{ "ParamName": value }`. Siehe [Plug-in-Parameter](Common.md#plug-in-parameter). |
| `class` | string |  | Erstellungsoption: Klasse des neuen Objekts; wird bei Bedarf erstellt. Siehe [Erstellungsoptionen](Common.md#optionen-zur-erstellung). |
| `name` | string |  | Erstellungsoption: Name des neuen Objekts. |
| `select` | boolean |  | Erstellungsoption: neues Objekt auswählen. |
| `useClassAttributes` | boolean |  | Erstellungsoption: mit `class` auch die Attribute des neuen Objekts anhand der Klasse festlegen. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `kind` | Art des Plug-in-Objekts: `point`, `linear`, `rectangle`, `custom`, `path2D` oder `path3D`. |
| `applied` | Nur vorhanden, wenn `params` angegeben wurde und nicht leer ist: `{ "<parameter>": true }` für jeden Parameter. Ein nicht geschriebener Parameter lässt den Aufruf scheitern, daher ist jeder Eintrag `true`. |
| `pathObject` | Nur für Plug-in-Objekte vom Typ `path2D` oder `path3D`: Objektreferenz des Pfadobjekts, das mit `pathUuid` bezeichnet wurde. |

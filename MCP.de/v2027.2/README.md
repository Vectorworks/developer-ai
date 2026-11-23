[English](../../MCP/v2027.2/README.md) • **Deutsch** • [日本語](../../MCP.ja/v2027.2/README.md)

# Vectorworks MCP-Server — Tool-Referenz für Vectorworks 2027 Update 2

Diese Referenz dokumentiert die Tools des Vectorworks-MCP-Servers: ihre Funktion, die erforderlichen Argumente und die zurückgegebenen Ergebnisse. Die 154 Tools sind in 18 Tool-Gruppen organisiert, zusätzlich zu den 3 immer verfügbaren Meta-Tools der Gruppe Core. Für jeden Bereich gibt es eine eigene Seite. Oben auf jeder Seite befindet sich ein Inhaltsverzeichnis; alle Gruppen und Tools folgen demselben Aufbau.

Informationen zu MCP und zum Betrieb des Servers finden Sie unter [Vectorworks-MCP-Server](../README.md).

## Inhaltsverzeichnis

- [Erste Schritte](#erste-schritte)
- [Konventionen](#konventionen)
- [Tool-Struktur](#tool-struktur)
- [Inhalte nach Kategorie](#inhalte-nach-kategorie)
  - [Gemeinsame Konventionen und Formate](#gemeinsame-konventionen-und-formate)
  - [Dokument und Auswahl](#dokument-und-auswahl)
  - [Objekte und Geometrie](#objekte-und-geometrie)
  - [Beschriftung](#beschriftung)
  - [Branchenobjekte](#branchenobjekte)
  - [Ressourcen und Daten](#ressourcen-und-daten)
  - [Automatisierung und Benutzeroberfläche](#automatisierung-und-benutzeroberfläche)
- [Index A–Z](#index-az)
- [Seitenaufbau](#seitenaufbau)
- [Statistik](#statistik)

## Erste Schritte

1. Wählen Sie in Vectorworks **Extras > MCP-Server > MCP-Server starten...** (in den Standard-Arbeitsumgebungen außer Viewer), wählen Sie den Werkzeugmodus und den Port (Standardwert 8765) und klicken Sie auf **Server starten**. Der Dialog zeigt die Server-URL, zum Beispiel `http://localhost:8765`; mit **URL kopieren** wird sie kopiert. Ist der Port belegt, versucht der Server bis zu 9 weitere Ports und zeigt den verwendeten Port im Dialog an. Fügen Sie die URL in Ihrem MCP-Client als HTTP-MCP-Server hinzu und öffnen Sie eine Zeichnung in Vectorworks: Ohne geöffnete Zeichnung geben die Werkzeuge `no active Vectorworks document` zurück. Details zu Dialog und Server finden Sie unter [Server starten und verbinden](../README.md#server-starten-und-verbinden).
2. Die Werkzeugliste (`tools/list`) zeigt nur die Werkzeuge aktiver Gruppen: die Meta-Werkzeuge der Gruppe [Core](Common.md#core-gruppe) und die standardmäßig aktiven Gruppen [Document](DocumentAccess.md#document), [Selection](DocumentAccess.md#selection), [IFC](IFC.md#ifc) und [Objects](ObjectPrimitives.md#objects). Der gewählte Werkzeugmodus bestimmt, welche Gruppen der Server anbietet: **Alle Werkzeuge aktivieren** (Standard) bietet alle Gruppen an, **Alle Werkzeuge ohne Skriptwerkzeuge aktivieren** alle Gruppen außer [Scripting](Scripting.md#scripting) und **Nur Skriptwerkzeuge aktivieren** nur die Meta-Werkzeuge von Core und die Gruppe Scripting, die sofort aktiviert wird. Siehe [Werkzeuggruppen und Aktivierung](Common.md#werkzeuggruppen-und-aktivierung).
3. Rufen Sie [`listToolGroups`](Common.md#listtoolgroups) auf, um alle Gruppen anzuzeigen, und [`activateToolGroups`](Common.md#activatetoolgroups), um benötigte Gruppen wie [Architecture](ObjectsArchitect.md#architecture) zu aktivieren. Aktualisieren Sie danach die Werkzeugliste.
4. Rufen Sie die Werkzeuge auf. Jeder erfolgreiche Aufruf, der die Zeichnung ändert, bildet einen Rückgängig-Schritt (`MCP: <tool>`; Skripte `MCP: script`), den Sie mit einem einzigen „Bearbeiten > Rückgängig“ zurücksetzen können. Interaktive Werkzeuge und Menübefehle zeichnen wie Benutzereingaben ihre eigenen Rückgängig-Schritte auf. Mit [`runToolBatch`](Common.md#runtoolbatch) können Sie mehrere Bearbeitungsaufrufe zu einem Rückgängig-Schritt zusammenfassen. Das Tool lehnt Werkzeuge ab, die eigene Rückgängig-Schritte aufzeichnen (`activateTool`, `setToolMode`, `setToolModes`, `sendToolPointer`, `sendToolAction`, `setOIPValues`, `pressOIPButton` und `runMenuCommand`), Skriptläufe (`runPythonScript` und `runScript`), Meta-Werkzeuge sowie Werkzeuge in inaktiven Gruppen. Siehe [Rückgängig machen](Common.md#rückgängig-machen).

Beispiel: Aktivieren Sie die Gruppe Architecture und zeichnen Sie eine Wand:

```json
{
  "name": "activateToolGroups",
  "arguments": {"groups": ["architecture"]}
}
```

```json
{
  "name": "createWall",
  "arguments": {
    "start": {"x": 0, "y": 0},
    "end": {"x": 5000, "y": 0},
    "thickness": 200
  }
}
```

`createWall` gibt die [Objektreferenz](Common.md#objektreferenzen) der neuen Wand zurück. Die folgenden Aufrufe verwenden deren `uuid`. Längen werden in den Einheiten der Zeichnung angegeben (in diesem Beispiel Millimeter).

## Konventionen

Die Seite [Common](Common.md) beschreibt die Konventionen, die für alle Tools gelten; [Attributes](Attributes.md) erläutert die Formate für Linienendmarkierungen und Schlagschatten.

| Thema | Konvention |
|---|---|
| [Tool-Gruppen und Aktivierung](Common.md#werkzeuggruppen-und-aktivierung) | Es werden nur die Tools aktiver Gruppen aufgelistet. `activateToolGroups` aktiviert Gruppen für die Sitzung. |
| [Ergebnisse und Fehler](Common.md#ergebnisse-und-fehler) | Jedes Tool gibt ein JSON-Objekt zurück; bei einem Fehler wird `{ "err": "..." }` zurückgegeben. |
| [Objektreferenzen](Common.md#objektreferenzen) | Objekte werden als `uuid` (bevorzugt), `name` oder `index` übergeben und mit `uuid`, `type`, `typeName` und `name` zurückgegeben. |
| [Punkte, Rechtecke und Farben](Common.md#punkte-rechtecke-und-farben) | `{ x, y }`, `{ left, top, right, bottom }` und `{ r, g, b }` mit Farbkanälen von 0 bis 255. |
| [Einheiten und Winkel](Common.md#einheiten-und-winkel) | Längen werden in Welteinheiten (den Einheiten der Zeichnung) und Winkel in Radiant angegeben, sofern ein Tool nichts anderes festlegt. |
| [Erstellungsoptionen](Common.md#optionen-zur-erstellung) | Erstellungs-Tools akzeptieren `class`, `useClassAttributes`, `name` und `select`. |
| [Übernommene Einstellungen](Common.md#angewendete-einstellungen) | Tools, die mehrere Einstellungen schreiben, melden jede davon in `applied`. |
| [Plug-in-Parameter](Common.md#plug-in-parameter) | Parameter von Plug-in-Objekten werden über ihren universellen Namen mit `params` gelesen und geschrieben. |
| [Seitennavigation](Common.md#seitennavigation) | Lange Listen verwenden `limit`, `offset` und `countOnly` und geben `count`, `truncated` und `nextOffset` zurück. |
| [Auswirkungen und Sicherheitsstufen](Common.md#auswirkungen-und-sicherheitsstufen) | Jedes Tool ist schreibgeschützt, eine Bearbeitung, interaktiv oder ein Skriptlauf und hat eine niedrige, mittlere oder hohe Sicherheitsstufe. |
| [Rückgängig](Common.md#rückgängig-machen) | Jeder Bearbeitungsaufruf ist ein Rückgängig-Schritt `MCP: <tool>`; ein fehlgeschlagener Aufruf wird rückgängig gemacht. |
| [Linienendmarkierungen und Schlagschatten](Attributes.md) | Es handelt sich um Teilobjekte: Geändert werden nur die angegebenen Elemente. |

## Tool-Struktur

Die Seiten dieser Referenz und die dokumentierten Tool-Gruppen, in der Reihenfolge der Tool-Ordner. Mit *aktiv* markierte Gruppen sind standardmäßig aktiviert.

```text
Vectorworks MCP-Server
├── Attributes                    → Attributes.md       Linienendmarkierungen, Schlagschatten
├── Common                        → Common.md           Konventionen
│   └── Core                      (3 Tools, immer aktiv)
├── DocumentAccess                → DocumentAccess.md
│   ├── Document                  (17 Tools, aktiv)
│   └── Selection                 (3 Tools, aktiv)
├── IFC                           → IFC.md
│   ├── IFC                       (4 Tools, aktiv)
│   └── IFC Data Mapping          (2 Tools)
├── MenuAccess                    → MenuAccess.md
│   └── Menus                     (4 Tools)
├── ObjectPrimitives              → ObjectPrimitives.md
│   ├── Draw2D                    (15 Tools)
│   └── Objects                   (12 Tools, aktiv)
├── Objects3D                     → Objects3D.md
│   └── 3D Modeling               (16 Tools)
├── ObjectsAnnotation             → ObjectsAnnotation.md
│   ├── Annotation                (8 Tools)
│   └── Dimensioning              (8 Tools)
├── ObjectsArchitect              → ObjectsArchitect.md
│   └── Architecture              (9 Tools)
├── ObjectsConnectCAD             → ObjectsConnectCAD.md
│   └── ConnectCAD                (10 Tools)
├── ObjectsLandmark               → ObjectsLandmark.md
│   └── Landmark                  (10 Tools)
├── ObjectsSpotlight              → ObjectsSpotlight.md
│   └── Spotlight                 (5 Tools)
├── OIPAccess                     → OIPAccess.md
│   └── Object Info               (3 Tools)
├── Resources                     → Resources.md
│   └── Resources                 (11 Tools)
├── Scripting                     → Scripting.md
│   └── Scripting                 (7 Tools)
└── ToolAccess                    → ToolAccess.md
    └── InteractiveTools          (10 Tools)
```

## Inhalte nach Kategorie

Alle Seiten, Gruppen und Tools nach Themen geordnet. Jedes Tool ist mit seiner Beschreibung verknüpft.

### Gemeinsame Konventionen und Formate

Aufruf aller Tools und Aufbau der gemeinsam verwendeten Werteformate.

- **[Common](Common.md)** — Die Konventionen, die für alle Tools des Vectorworks-MCP-Servers gelten: Aufrufe und Ergebnisse, Objektreferenzen, Punkte und Farben, Einheiten, Erstellungsoptionen, übernommene Einstellungen, Plug-in-Parameter, Seitennavigation, Auswirkungen, Sicherheitsstufen und Rückgängig.
  - **[Core](Common.md#core-gruppe)** (`core`, 3 Tools, immer aktiv) — Tool-Gruppen ermitteln und aktivieren sowie mehrere Tool-Aufrufe als einen Rückgängig-Schritt ausführen.
    - [`listToolGroups`](Common.md#listtoolgroups) — Listet alle aktiven und inaktiven Tool-Gruppen mit ihrem Aktivierungsstatus und optional ihren Tools auf.
    - [`activateToolGroups`](Common.md#activatetoolgroups) — Aktiviert Tool-Gruppen für den Rest der Sitzung, damit ihre Tools in der Tool-Liste erscheinen.
    - [`runToolBatch`](Common.md#runtoolbatch) — Führt mehrere Tool-Aufrufe als einen Rückgängig-Schritt aus; entweder alle oder keinen.
  - Konventionen: [Tool-Aufruf](Common.md#ein-tool-aufrufen) · [Ergebnisse und Fehler](Common.md#ergebnisse-und-fehler) · [Objektreferenzen](Common.md#objektreferenzen) · [Punkte, Rechtecke und Farben](Common.md#punkte-rechtecke-und-farben) · [Einheiten und Winkel](Common.md#einheiten-und-winkel) · [Erstellungsoptionen](Common.md#optionen-zur-erstellung) · [Übernommene Einstellungen](Common.md#angewendete-einstellungen) · [Plug-in-Parameter](Common.md#plug-in-parameter) · [Seitennavigation](Common.md#seitennavigation) · [Auswirkungen und Sicherheitsstufen](Common.md#auswirkungen-und-sicherheitsstufen) · [Rückgängig](Common.md#rückgängig-machen)
- **[Attributes](Attributes.md)** — Die Werteformate für Linienendmarkierungen und Schlagschatten. Sie werden von Tools gemeinsam verwendet, die die grafischen Attribute von Klassen und Objekten lesen und schreiben.
  - Formate: [Linienendmarkierungen](Attributes.md#linienendmarkierungen) · [Schlagschatten](Attributes.md#schlagschatten)

### Dokument und Auswahl

Die Zeichnung als Ganzes: Ebenen, Geschosse, Klassen, Einheiten, Ansicht, Einstellungen und Auswahl.

- **[DocumentAccess](DocumentAccess.md)** — Tools für die aktive Zeichnung als Ganzes und die aktuelle Auswahl: Dokumentübersicht, Ebenen, Geschosse, Klassen, Einheiten, Ansicht und Dokumenteinstellungen sowie Massenbearbeitungen der ausgewählten Objekte.
  - **[Document](DocumentAccess.md#document)** (`document`, 17 Tools, standardmäßig aktiv) — Die aktive Zeichnung: Dokumentübersicht, Ebenen, Geschosse, Klassen, Einheiten, Ansicht und Dokumenteinstellungen.
    - [`getDocumentInfo`](DocumentAccess.md#getdocumentinfo) — Gibt eine Übersicht des aktiven Dokuments zurück: Datei, Anzahlen, Seitengrenzen, Ansichtsmitte und Benutzerursprung.
    - [`getLayers`](DocumentAccess.md#getlayers) — Listet Ebenen mit Typ, Sichtbarkeit, Maßstab, Höhe, Objektanzahl und Begrenzungen auf.
    - [`createLayer`](DocumentAccess.md#createlayer) — Erstellt eine Konstruktionsebene oder Layoutebene.
    - [`editLayer`](DocumentAccess.md#editlayer) — Ändert Eigenschaften einer Ebene, z. B. Name, Sichtbarkeit, Maßstab, Höhe und Dicke.
    - [`getStories`](DocumentAccess.md#getstories) — Listet die Geschosse mit ihren Ebenen von unten nach oben auf.
    - [`createStory`](DocumentAccess.md#createstory) — Erstellt ein oder mehrere Geschosse mit ihren Ebenen.
    - [`editStory`](DocumentAccess.md#editstory) — Ändert ein Geschoss, die Ebenentypen des Dokuments oder dessen Standard-Geschossebenen.
    - [`getClasses`](DocumentAccess.md#getclasses) — Listet die Klassen des Dokuments auf und benennt die speziellen Klassen.
    - [`createClass`](DocumentAccess.md#createclass) — Erstellt eine Klasse oder gibt die bereits vorhandene Klasse dieses Namens zurück.
    - [`editClass`](DocumentAccess.md#editclass) — Ändert eine Klasse: Beschreibung, Sichtbarkeit, Stift, Füllung, Markierungen, Schlagschatten und mehr.
    - [`setActiveContext`](DocumentAccess.md#setactivecontext) — Legt die aktive Ebene und Klasse sowie die Anzeige der anderen Ebenen und Klassen fest.
    - [`getUnits`](DocumentAccess.md#getunits) — Gibt die Einstellungen der primären und sekundären Einheiten des Dokuments zurück.
    - [`setUnits`](DocumentAccess.md#setunits) — Ändert die Einstellungen der primären oder sekundären Einheiten des Dokuments.
    - [`convertUnits`](DocumentAccess.md#convertunits) — Konvertiert Längen zwischen Welteinheiten und Dokumenteinheiten.
    - [`setView`](DocumentAccess.md#setview) — Verschiebt die Ansicht, legt den Zoom fest, verschiebt den Benutzerursprung oder zeichnet die Seite neu.
    - [`getPreferences`](DocumentAccess.md#getpreferences) — Liest eine Kategorie der Dokumenteinstellungen.
    - [`setPreferences`](DocumentAccess.md#setpreferences) — Schreibt Dokumenteinstellungen einer Kategorie.
  - **[Selection](DocumentAccess.md#selection)** (`selection`, 3 Tools, standardmäßig aktiv) — Listet die aktuelle Auswahl auf und verschiebt, dreht, skaliert, dupliziert, gruppiert, löscht oder klassifiziert sie neu.
    - [`getSelection`](DocumentAccess.md#getselection) — Listet die ausgewählten Objekte auf allen Ebenen und die Begrenzungen der Auswahl auf.
    - [`selectObjects`](DocumentAccess.md#selectobjects) — Wählt Objekte nach Kriterien oder UUID aus bzw. ab oder wählt alle oder keine aus.
    - [`editSelection`](DocumentAccess.md#editselection) — Verschiebt, dreht, skaliert, dupliziert, gruppiert, löscht oder klassifiziert die Auswahl neu.

### Objekte und Geometrie

Beliebige Objekte, 2D-Grundkörper, Text und 3D-Geometrie.

- **[ObjectPrimitives](ObjectPrimitives.md)** — Tools für beliebige Objekte der Zeichnung (Suchen, Prüfen, Gestalten, Transformieren, Plug-in-Parameter und Datensätze) sowie zum Erstellen, Bearbeiten, Messen und Kombinieren von 2D-Grundkörpern und Text.
  - **[Draw2D](ObjectPrimitives.md#draw2d)** (`draw2d`, 15 Tools, standardmäßig inaktiv) — Erstellt, bearbeitet, misst und kombiniert 2D-Grundkörper sowie Textobjekte; liest und bearbeitet Textobjekte.
    - [`createLine`](ObjectPrimitives.md#createline) — Erstellt eine gerade Linie zwischen zwei Punkten.
    - [`createRectangle`](ObjectPrimitives.md#createrectangle) — Erstellt ein Rechteck, optional gedreht und mit abgerundeten Ecken.
    - [`createCircle`](ObjectPrimitives.md#createcircle) — Erstellt einen Kreis anhand von Mittelpunkt und Radius oder durch drei Punkte.
    - [`createArc`](ObjectPrimitives.md#createarc) — Erstellt einen Kreisbogen anhand von Mittelpunkt, Radius und Winkeln oder durch drei Punkte.
    - [`createPolygon`](ObjectPrimitives.md#createpolygon) — Erstellt ein Polygon aus Punkten oder ein regelmäßiges Polygon.
    - [`createPolyline`](ObjectPrimitives.md#createpolyline) — Erstellt eine Polylinie aus Scheitelpunkten beliebigen Typs oder eine abgerundete Form.
    - [`createLocus`](ObjectPrimitives.md#createlocus) — Erstellt einen 2D-Ortsmarkierungspunkt (Referenzpunkt).
    - [`getGeometry`](ObjectPrimitives.md#getgeometry) — Liest die typspezifische Geometrie eines 2D-Grundkörpers.
    - [`setGeometry`](ObjectPrimitives.md#setgeometry) — Bearbeitet die Geometrie eines 2D-Grundkörpers.
    - [`editVertices`](ObjectPrimitives.md#editvertices) — Fügt Scheitelpunkte eines Polygons oder einer Polylinie hinzu, ein, ändert, löscht, kehrt sie um oder ersetzt sie.
    - [`queryGeometry`](ObjectPrimitives.md#querygeometry) — Beantwortet geometrische Fragen zu einem 2D-Grundkörper: nächster Punkt, Abstand, Enthaltensein, Schnittpunkte, Tangenten und Messungen entlang von Kurven.
    - [`combineShapes`](ObjectPrimitives.md#combineshapes) — Kombiniert zwei 2D-Formen durch eine boolesche Operation: Vereinigung, Schnittmenge, Differenz oder symmetrische Differenz.
    - [`createText`](ObjectPrimitives.md#createtext) — Erstellt ein Textobjekt.
    - [`getText`](ObjectPrimitives.md#gettext) — Liest ein Textobjekt: Inhalt, Zeichenformatierung, Stil und Layout.
    - [`editText`](ObjectPrimitives.md#edittext) — Bearbeitet Inhalt und Formatierung eines Textobjekts.
  - **[Objects](ObjectPrimitives.md#objects)** (`objects`, 12 Tools, standardmäßig aktiv) — Sucht, prüft und bearbeitet beliebige Objekte: Attribute, Transformationen, Container, Plug-in-Parameter und Datensätze.
    - [`findObjects`](ObjectPrimitives.md#findobjects) — Sucht Objekte, die einer Kriterienzeichenfolge entsprechen.
    - [`getObjectsAtPoint`](ObjectPrimitives.md#getobjectsatpoint) — Sucht Objekte an einem Punkt.
    - [`getObjectInfo`](ObjectPrimitives.md#getobjectinfo) — Gibt Identität, Klasse, Ebene, Begrenzungen, Status und Container eines Objekts zurück.
    - [`getObjectAttributes`](ObjectPrimitives.md#getobjectattributes) — Gibt die grafischen Attribute eines Objekts zurück.
    - [`setObjectAttributes`](ObjectPrimitives.md#setobjectattributes) — Legt grafische Attribute eines Objekts fest: Stift, Füllung, Deckkraft, Markierungen, Schlagschatten und mehr.
    - [`copyAttributes`](ObjectPrimitives.md#copyattributes) — Kopiert die grafischen Attribute eines Objekts auf andere Objekte.
    - [`editObject`](ObjectPrimitives.md#editobject) — Verschiebt, dreht, skaliert, spiegelt, dupliziert, gruppiert neu, konvertiert, setzt zurück oder löscht ein Objekt oder ändert dessen Namen und Klasse.
    - [`getObjectParameters`](ObjectPrimitives.md#getobjectparameters) — Liest die Parameter eines Plug-in-Objekts.
    - [`getObjectRecords`](ObjectPrimitives.md#getobjectrecords) — Liest die an ein Objekt angehängten Datensätze.
    - [`setObjectParameter`](ObjectPrimitives.md#setobjectparameter) — Schreibt einen oder mehrere Parameter eines Plug-in-Objekts.
    - [`getPluginDefinition`](ObjectPrimitives.md#getplugindefinition) — Beschreibt ein installiertes Plug-in-Objekt: Typ, Parameter und Popup-Auswahlmöglichkeiten.
    - [`createPluginObject`](ObjectPrimitives.md#createpluginobject) — Erstellt ein Plug-in-Objekt, für das kein eigenes Erstellungs-Tool vorhanden ist.
- **[Objects3D](Objects3D.md)** — Tools zum Erstellen, Lesen und Bearbeiten von 3D-Geometrie: Volumenkörper, 3D-Polygone, Netze, NURBS-Kurven und -Flächen sowie Flächenmodelle.
  - **[3D Modeling](Objects3D.md#3d-modeling)** (`3d-modeling`, 16 Tools, standardmäßig inaktiv) — Erstellt, liest und bearbeitet Volumenkörper, 3D-Polygone, Netze, NURBS-Kurven und -Flächen sowie Flächenmodelle.
    - [`createExtrude`](Objects3D.md#createextrude) — Erstellt einen Extrusionskörper, Mehrfach-Extrusionskörper oder verjüngten Extrusionskörper.
    - [`createSolidPrimitive`](Objects3D.md#createsolidprimitive) — Erstellt eine Kugel, ein Ellipsoid, eine Halbkugel, einen Kegel, Quader, Zylinder oder Torus.
    - [`createSweep`](Objects3D.md#createsweep) — Erstellt eine Rotation: 2D-Profile werden um eine Achse gedreht.
    - [`combineSolids`](Objects3D.md#combinesolids) — Kombiniert zwei Volumenkörper durch Vereinigung, Schnittmenge oder Differenz zu einem allgemeinen Volumenkörper.
    - [`createShell`](Objects3D.md#createshell) — Erstellt eine Schale durch Verdicken einer NURBS-Fläche oder Aushöhlen eines Volumenkörpers.
    - [`convertSolid`](Objects3D.md#convertsolid) — Erstellt eine Kopie eines in einen allgemeinen Volumenkörper oder ein Netz konvertierten Volumenkörpers.
    - [`getSolid`](Objects3D.md#getsolid) — Liest einen Volumenkörper: Typ, 3D-Begrenzungen, Parameter und Verlauf des allgemeinen Volumenkörpers.
    - [`editSolid`](Objects3D.md#editsolid) — Verschiebt, dreht, skaliert, richtet einen Volumenkörper neu aus oder ändert seine Größe.
    - [`create3DPolygon`](Objects3D.md#create3dpolygon) — Erstellt ein 3D-Polygon aus 3D-Punkten, aus 2D-Punkten auf einer Höhe oder aus einem Rechteck.
    - [`createMesh`](Objects3D.md#createmesh) — Erstellt ein Netz aus Scheitelpunkten und Flächen, aus Polygonen oder aus einer Gruppe von 3D-Polygonen.
    - [`createNurbsCurve`](Objects3D.md#createnurbscurve) — Erstellt eine NURBS-Kurve aus Kontrollpunkten oder Anpassungspunkten.
    - [`createNurbsSurface`](Objects3D.md#createnurbssurface) — Erstellt eine NURBS-Fläche aus ihrem Kontrollnetz.
    - [`createSurfaceModel`](Objects3D.md#createsurfacemodel) — Erstellt aus vorhandenen Objekten ein Loft-, Schienensweep-, Rotations- oder Pfadextrusions-Flächenmodell.
    - [`get3DGeometry`](Objects3D.md#get3dgeometry) — Liest ein 3D-Polygon, Netz, eine NURBS-Kurve oder NURBS-Fläche.
    - [`edit3DGeometry`](Objects3D.md#edit3dgeometry) — Bearbeitet ein 3D-Polygon, Netz, eine NURBS-Kurve oder NURBS-Fläche.
    - [`convertTo3D`](Objects3D.md#convertto3d) — Konvertiert eine Kopie eines Objekts in 3D-Polygone, ein Netz oder einen allgemeinen Volumenkörper.

### Beschriftung

Datenstempel, Planköpfe und Bemaßungen.

- **[ObjectsAnnotation](ObjectsAnnotation.md)** — Tools für Beschriftungen: Datenstempel, Plankopfstempel und Plankopf-Projektdaten sowie Bemaßungen mit Mittelpunktmarkierungen.
  - **[Annotation](ObjectsAnnotation.md#annotation)** (`annotation`, 8 Tools, standardmäßig inaktiv) — Datenstempel, Plankopfstempel und Plankopf-Projektdaten des Dokuments.
    - [`createDataTag`](ObjectsAnnotation.md#createdatatag) — Erstellt einen Datenstempel, optional an ein Objekt angehängt.
    - [`createTitleBlock`](ObjectsAnnotation.md#createtitleblock) — Erstellt einen Plankopfstempel.
    - [`getAnnotationObject`](ObjectsAnnotation.md#getannotationobject) — Liest einen Datenstempel oder Plankopfstempel.
    - [`setAnnotationObject`](ObjectsAnnotation.md#setannotationobject) — Bearbeitet einen Datenstempel oder Plankopfstempel.
    - [`tagObject`](ObjectsAnnotation.md#tagobject) — Hängt einen Datenstempel an ein Objekt an oder löst die Verknüpfung.
    - [`getObjectTags`](ObjectsAnnotation.md#getobjecttags) — Listet die an ein Objekt angehängten Datenstempel auf.
    - [`getProjectData`](ObjectsAnnotation.md#getprojectdata) — Liest die Plankopf-Projektdaten des Dokuments.
    - [`setProjectData`](ObjectsAnnotation.md#setprojectdata) — Schreibt die Plankopf-Projektdaten des Dokuments.
  - **[Dimensioning](ObjectsAnnotation.md#dimensioning)** (`dimensioning`, 8 Tools, standardmäßig inaktiv) — Lineare, Winkel-, Bogenlängen- und Radialbemaßungen sowie Mittelpunktmarkierungen.
    - [`createLinearDimension`](ObjectsAnnotation.md#createlineardimension) — Erstellt eine gebundene, horizontale, vertikale, ungebundene oder Ordinatenbemaßung.
    - [`createAngularDimension`](ObjectsAnnotation.md#createangulardimension) — Erstellt eine Winkelbemaßung.
    - [`createArcLengthDimension`](ObjectsAnnotation.md#createarclengthdimension) — Erstellt eine Bogenlängenbemaßung.
    - [`createRadialDimension`](ObjectsAnnotation.md#createradialdimension) — Erstellt eine Radial- oder Durchmesserbemaßung.
    - [`createCenterMark`](ObjectsAnnotation.md#createcentermark) — Erstellt eine Mittelpunktmarkierung für ein kreisförmiges Element.
    - [`getDimension`](ObjectsAnnotation.md#getdimension) — Liest eine Bemaßung: Typ, gemessene Punkte, Wert und Texteinstellungen.
    - [`setDimension`](ObjectsAnnotation.md#setdimension) — Bearbeitet eine Bemaßung.
    - [`getObjectDimensions`](ObjectsAnnotation.md#getobjectdimensions) — Listet die einem Objekt zugeordneten Bemaßungen auf.

### Branchenobjekte

Architektur-, Landschafts-, Unterhaltungsbeleuchtungs- und AV-Systemobjekte.

- **[ObjectsArchitect](ObjectsArchitect.md)** — Tools für BIM-Bauteile: Wände, Boden/Decken, Dächer, Türen, Fenster, Stützen und Treppen.
  - **[Architecture](ObjectsArchitect.md#architecture)** (`architecture`, 9 Tools, standardmäßig inaktiv) — BIM-Bauteile: Wände, Boden/Decken, Dächer, Türen, Fenster, Stützen und Treppen.
    - [`createWall`](ObjectsArchitect.md#createwall) — Erstellt eine gerade oder runde Wand.
    - [`createSlab`](ObjectsArchitect.md#createslab) — Erstellt einen Boden/eine Decke aus einem 2D-Begrenzungsobjekt.
    - [`createRoof`](ObjectsArchitect.md#createroof) — Erstellt ein polygonales Dach.
    - [`createDoor`](ObjectsArchitect.md#createdoor) — Erstellt eine freistehende Tür.
    - [`createWindow`](ObjectsArchitect.md#createwindow) — Erstellt ein freistehendes Fenster.
    - [`createColumn`](ObjectsArchitect.md#createcolumn) — Erstellt eine Stütze.
    - [`createStair`](ObjectsArchitect.md#createstair) — Erstellt eine Treppe.
    - [`getArchitectureObject`](ObjectsArchitect.md#getarchitectureobject) — Liest die Eigenschaften einer Wand, eines Bodens/einer Decke, Dachs, einer Tür, eines Fensters, einer Stütze oder Treppe.
    - [`setArchitectureObject`](ObjectsArchitect.md#setarchitectureobject) — Bearbeitet eine Wand, einen Boden/eine Decke, ein Dach, eine Tür, ein Fenster, eine Stütze oder eine Treppe.
- **[ObjectsLandmark](ObjectsLandmark.md)** — Tools für Gelände- und Landschaftsobjekte: Pflanzen, Beläge, Landschaftsflächen, Geländemodelle, Geländemodifikatoren, Höhenpunkte, Grundstücksgrenzen und bestehende Bäume.
  - **[Landmark](ObjectsLandmark.md#landmark)** (`landmark`, 10 Tools, standardmäßig inaktiv) — Pflanzen, Beläge, Landschaftsflächen, Geländemodelle, Geländemodifikatoren, Höhenpunkte, Grundstücksgrenzen und bestehende Bäume.
    - [`createPlant`](ObjectsLandmark.md#createplant) — Erstellt eine Pflanze an einem Punkt oder entlang eines Pfads.
    - [`createHardscape`](ObjectsLandmark.md#createhardscape) — Erstellt einen Belag aus einem 2D-Pfadobjekt.
    - [`createLandscapeArea`](ObjectsLandmark.md#createlandscapearea) — Erstellt eine Landschaftsfläche aus einem 2D-Pfadobjekt.
    - [`createSiteModifier`](ObjectsLandmark.md#createsitemodifier) — Erstellt einen Geländemodifikator aus einem 2D-Pfadobjekt.
    - [`createPropertyLine`](ObjectsLandmark.md#createpropertyline) — Erstellt eine Grundstücksgrenze aus einem geschlossenen 2D-Pfadobjekt.
    - [`createSiteModel`](ObjectsLandmark.md#createsitemodel) — Erstellt ein leeres Geländemodell.
    - [`createStake`](ObjectsLandmark.md#createstake) — Erstellt einen Höhenpunkt.
    - [`createExistingTree`](ObjectsLandmark.md#createexistingtree) — Erstellt einen bestehenden Baum.
    - [`getLandmarkObject`](ObjectsLandmark.md#getlandmarkobject) — Liest die Eigenschaften eines Gelände- oder Landschaftsobjekts.
    - [`setLandmarkObject`](ObjectsLandmark.md#setlandmarkobject) — Bearbeitet ein Gelände- oder Landschaftsobjekt.
- **[ObjectsSpotlight](ObjectsSpotlight.md)** — Tools für Spotlight-Beleuchtungsgeräte und die von ihnen verwendeten GDTF-Scheinwerfertypen (General Device Type Format).
  - **[Spotlight](ObjectsSpotlight.md#spotlight)** (`spotlight`, 5 Tools, standardmäßig inaktiv) — Spotlight-Beleuchtungsgeräte und die von ihnen verwendeten GDTF-Scheinwerfertypen.
    - [`listGDTFs`](ObjectsSpotlight.md#listgdtfs) — Listet verfügbare GDTF-Scheinwerfertypen und ihre DMX-Modi auf.
    - [`importGDTF`](ObjectsSpotlight.md#importgdtf) — Importiert eine .gdtf-Datei als GDTF-Scheinwerfertyp in die Zeichnung.
    - [`createLightingDevice`](ObjectsSpotlight.md#createlightingdevice) — Erstellt ein Beleuchtungsgerät, optional mit einem GDTF-Scheinwerfertyp.
    - [`getLightingDevice`](ObjectsSpotlight.md#getlightingdevice) — Liest ein Beleuchtungsgerät.
    - [`setLightingDevice`](ObjectsSpotlight.md#setlightingdevice) — Bearbeitet ein Beleuchtungsgerät.
- **[ObjectsConnectCAD](ObjectsConnectCAD.md)** — Tools für ConnectCAD-Schaltplan-Geräte, deren Anschlüsse und Gerätetypen sowie die verwendeten Signal- und Steckertypen.
  - **[ConnectCAD](ObjectsConnectCAD.md#connectcad)** (`connectcad`, 10 Tools, standardmäßig inaktiv) — ConnectCAD-Schaltplan-Geräte, Anschlüsse und Gerätetypen, erstellt anhand von JSON-Gerätebeschreibungen.
    - [`listConnectCADSignals`](ObjectsConnectCAD.md#listconnectcadsignals) — Listet die ConnectCAD-Signaltypen auf.
    - [`listConnectCADConnectors`](ObjectsConnectCAD.md#listconnectcadconnectors) — Listet die ConnectCAD-Steckertypen und ihre Pins auf.
    - [`validateConnectCADDevice`](ObjectsConnectCAD.md#validateconnectcaddevice) — Prüft eine Gerätebeschreibung, ohne etwas zu erstellen.
    - [`createConnectCADDevice`](ObjectsConnectCAD.md#createconnectcaddevice) — Erstellt ein Schaltplan-Gerät mit allen Anschlüssen anhand einer Gerätebeschreibung.
    - [`createConnectCADDevices`](ObjectsConnectCAD.md#createconnectcaddevices) — Erstellt mehrere Schaltplan-Geräte nacheinander in einem Vorgang.
    - [`getConnectCADDevice`](ObjectsConnectCAD.md#getconnectcaddevice) — Liest ein ConnectCAD-Gerät und seine Anschlüsse.
    - [`addConnectCADSocket`](ObjectsConnectCAD.md#addconnectcadsocket) — Fügt einem Gerät einen Anschluss hinzu.
    - [`setConnectCADSocket`](ObjectsConnectCAD.md#setconnectcadsocket) — Bearbeitet einen Anschluss.
    - [`createConnectCADDeviceType`](ObjectsConnectCAD.md#createconnectcaddevicetype) — Erstellt das Gerätetyp-Symbol eines Geräts.
    - [`getConnectCADDeviceType`](ObjectsConnectCAD.md#getconnectcaddevicetype) — Liest den Datensatz Device Definition eines Gerätetyp-Symbols.

### Ressourcen und Daten

Ressourcen, Tabellen und IFC-Daten.

- **[Resources](Resources.md)** — Tools für Ressourcen der Zeichnung und externe Inhalte (Bibliotheken, Dateien, andere Dokumente) sowie für Tabellen.
  - **[Resources](Resources.md#resources)** (`resources`, 11 Tools, standardmäßig inaktiv) — Listet Ressourcen auf, importiert, erstellt, prüft, bearbeitet und weist sie zu; liest und bearbeitet Tabellen.
    - [`getResourceTypes`](Resources.md#getresourcetypes) — Listet die Ressourcentypen und die Standardordner für Inhalte auf.
    - [`getResources`](Resources.md#getresources) — Listet Ressourcen eines Typs aus der Zeichnung, einer Bibliothek, einer Datei oder einem anderen Dokument auf.
    - [`getResource`](Resources.md#getresource) — Liest eine Ressource der Zeichnung.
    - [`importResource`](Resources.md#importresource) — Importiert eine externe Ressource in die Zeichnung.
    - [`editResource`](Resources.md#editresource) — Benennt eine Ressource um, beschreibt, verschiebt, dupliziert oder löscht sie.
    - [`createResource`](Resources.md#createresource) — Erstellt eine leere Ressource.
    - [`getResourceDetails`](Resources.md#getresourcedetails) — Liest den Inhalt einer Ressource: Schraffurstufen, Verlaufsstopps, Linientyp-Striche und mehr.
    - [`setResourceDetails`](Resources.md#setresourcedetails) — Ändert den Inhalt einer Ressource.
    - [`applyResource`](Resources.md#applyresource) — Weist einem Objekt eine Textur, einen Stil oder eine Datenvisualisierung zu.
    - [`getWorksheet`](Resources.md#getworksheet) — Liest eine Tabelle: Größe, Zellen, Formate und Datenbankzeilen.
    - [`editWorksheet`](Resources.md#editworksheet) — Ändert eine Tabelle anhand einer Aktionsliste.
- **[IFC](IFC.md)** — Schreibgeschützter Zugriff auf die IFC-Daten (Industry Foundation Classes) der Zeichnung: IFC-Entitäten und Eigenschaftensätze von Objekten, Definitionen von Eigenschaftensätzen sowie Zuordnungen des IFC Data Manager des Dokuments.
  - **[IFC](IFC.md#ifc)** (`ifc`, 4 Tools, standardmäßig aktiv) — Schreibgeschützte IFC-Daten: IFC-Entitäten und Eigenschaftensätze von Objekten sowie Definitionen der Eigenschaftensätze des Dokuments.
    - [`getObjectIFCData`](IFC.md#getobjectifcdata) — Liest die IFC-Daten eines Objekts so, wie sie beim IFC-Export berechnet werden.
    - [`getIFCPsetDefinition`](IFC.md#getifcpsetdefinition) — Liest eine IFC-Eigenschaftensatzdefinition anhand ihres Namens.
    - [`listIFCPsets`](IFC.md#listifcpsets) — Listet IFC-Eigenschaftensätze auf, die für einen IFC-Entitätstyp gelten.
    - [`listIFCCustomPsets`](IFC.md#listifccustompsets) — Listet die benutzerdefinierten IFC-Eigenschaftensatzdefinitionen des Dokuments auf.
  - **[IFC Data Mapping](IFC.md#ifc-data-mapping)** (`ifc-data-mapping`, 2 Tools, standardmäßig inaktiv) — Liest die Zuordnungsdefinitionen des IFC Data Manager des aktiven Dokuments.
    - [`listIFCMappingObjects`](IFC.md#listifcmappingobjects) — Listet die Zuordnungsobjekte der aktiven Data-Manager-Zuordnung auf.
    - [`getIFCMapping`](IFC.md#getifcmapping) — Liest die Data-Manager-Zuordnung eines Zuordnungsobjekts.

### Automatisierung und Benutzeroberfläche

Skripte, interaktive Tools, die Objekt-Info-Palette und Menübefehle.

- **[Scripting](Scripting.md)** — Tools zum Ausführen von Python-Skripten in Vectorworks, Lesen und Speichern von Python-Skriptressourcen und Nachschlagen des von Skripten verwendeten Python-`api`-Moduls.
  - **[Scripting](Scripting.md#scripting)** (`scripting`, 7 Tools, standardmäßig inaktiv) — Führt Python-Skripte aus, liest und speichert Python-Skriptressourcen und schlägt Informationen zum Python-`api`-Modul nach.
    - [`listScripts`](Scripting.md#listscripts) — Listet die Skriptressourcen des Dokuments auf.
    - [`getScript`](Scripting.md#getscript) — Liest eine Skriptressource, ohne sie auszuführen.
    - [`saveScript`](Scripting.md#savescript) — Erstellt oder aktualisiert eine Python-Skriptressource, ohne sie auszuführen.
    - [`describePythonApi`](Scripting.md#describepythonapi) — Gibt den Hilfetext des Python-`api`-Moduls oder eines seiner Namen zurück.
    - [`getPythonApiGuide`](Scripting.md#getpythonapiguide) — Gibt einen Abschnitt der Anleitung zum Schreiben von Python-Skripten zurück.
    - [`runPythonScript`](Scripting.md#runpythonscript) — Führt Python-Code in Vectorworks aus.
    - [`runScript`](Scripting.md#runscript) — Führt eine gespeicherte Python-Skriptressource aus.
- **[ToolAccess](ToolAccess.md)** — Tools, die interaktive Vectorworks-Tools in den Werkzeugpaletten wie ein Benutzer bedienen: ein Tool aktivieren, seine Modi festlegen und in die Zeichnung klicken.
  - **[InteractiveTools](ToolAccess.md#interactivetools)** (`interactivetools`, 10 Tools, standardmäßig inaktiv) — Bedient interaktive Vectorworks-Tools in den Werkzeugpaletten wie ein Benutzer.
    - [`getTools`](ToolAccess.md#gettools) — Listet die Vectorworks-Tools auf.
    - [`getTool`](ToolAccess.md#gettool) — Gibt ein Tool mit den deklarierten Modusschaltflächen zurück.
    - [`getActiveTool`](ToolAccess.md#getactivetool) — Gibt den Status des aktiven Tools zurück.
    - [`activateTool`](ToolAccess.md#activatetool) — Aktiviert ein Tool.
    - [`getToolModes`](ToolAccess.md#gettoolmodes) — Liest die aktuelle Modusleiste des aktiven Tools.
    - [`setToolMode`](ToolAccess.md#settoolmode) — Ändert einen Modus des aktiven Tools.
    - [`setToolModes`](ToolAccess.md#settoolmodes) — Legt mehrere Modi des aktiven Tools fest.
    - [`sendToolPointer`](ToolAccess.md#sendtoolpointer) — Klickt, doppelklickt, bewegt den Zeiger oder zieht mit dem aktiven Tool in der Zeichnung.
    - [`sendToolAction`](ToolAccess.md#sendtoolaction) — Beendet oder bricht die Aktion des aktiven Tools ab oder entfernt dessen letzten Punkt.
    - [`convertToolCoordinates`](ToolAccess.md#converttoolcoordinates) — Konvertiert Punkte zwischen dem Modellraum und der Ansicht des aktiven Fensters.
- **[OIPAccess](OIPAccess.md)** — Tools, die die Objekt-Info-Palette für die aktuelle Auswahl wie ein Benutzer lesen und bedienen.
  - **[Object Info](OIPAccess.md#object-info)** (`object-info`, 3 Tools, standardmäßig inaktiv) — Liest und bedient die Objekt-Info-Palette für die aktuelle Auswahl wie ein Benutzer.
    - [`getOIPControls`](OIPAccess.md#getoipcontrols) — Listet die Steuerelemente eines Bereichs der Objekt-Info-Palette auf.
    - [`setOIPValues`](OIPAccess.md#setoipvalues) — Legt Steuerelemente der Objekt-Info-Palette wie ein Benutzer fest.
    - [`pressOIPButton`](OIPAccess.md#pressoipbutton) — Betätigt eine Schaltfläche der Objekt-Info-Palette.
- **[MenuAccess](MenuAccess.md)** — Tools, die Vectorworks-Menüs lesen, die Ausführbarkeit eines Befehls prüfen und Menübefehle so ausführen, als hätte der Benutzer sie ausgewählt.
  - **[Menus](MenuAccess.md#menus)** (`menus`, 4 Tools, standardmäßig inaktiv) — Sucht Menübefehle, liest die Menüleiste, prüft, ob ein Befehl ausgeführt werden kann, und führt ihn aus.
    - [`findMenuCommands`](MenuAccess.md#findmenucommands) — Sucht installierte Menübefehle nach Text und Arbeitsumgebung.
    - [`getMenus`](MenuAccess.md#getmenus) — Liest die Menüleiste der aktuellen Arbeitsumgebung, ein Menü oder die Elemente eines Menüabschnitts.
    - [`getMenuStatus`](MenuAccess.md#getmenustatus) — Gibt an, ob ein Menübefehl oder Element eines Menüabschnitts jetzt ausgeführt werden kann und warum nicht.
    - [`runMenuCommand`](MenuAccess.md#runmenucommand) — Führt einen Menübefehl oder ein Element eines Menüabschnitts aus, als hätte der Benutzer es ausgewählt.

## Index A–Z

[A](#index-a) · [C](#index-c) · [D](#index-d) · [E](#index-e) · [F](#index-f) · [G](#index-g) · [I](#index-i) · [L](#index-l) · [P](#index-p) · [Q](#index-q) · [R](#index-r) · [S](#index-s) · [T](#index-t) · [V](#index-v)

### Index A

| Werkzeug | Gruppe | Seite | Zusammenfassung |
|---|---|---|---|
| [`activateTool`](ToolAccess.md#activatetool) | [InteractiveTools](ToolAccess.md#interactivetools) | [ToolAccess](ToolAccess.md) | Aktiviert ein Tool. |
| [`activateToolGroups`](Common.md#activatetoolgroups) | [Core](Common.md#core-gruppe) | [Common](Common.md) | Aktiviert Tool-Gruppen für den Rest der Sitzung, damit ihre Tools in der Tool-Liste erscheinen. |
| [`addConnectCADSocket`](ObjectsConnectCAD.md#addconnectcadsocket) | [ConnectCAD](ObjectsConnectCAD.md#connectcad) | [ObjectsConnectCAD](ObjectsConnectCAD.md) | Fügt einem Gerät einen Anschluss hinzu. |
| [`applyResource`](Resources.md#applyresource) | [Resources](Resources.md#resources) | [Resources](Resources.md) | Weist einem Objekt eine Textur, einen Stil oder eine Datenvisualisierung zu. |

### Index C

| Werkzeug | Gruppe | Seite | Zusammenfassung |
|---|---|---|---|
| [`combineShapes`](ObjectPrimitives.md#combineshapes) | [Draw2D](ObjectPrimitives.md#draw2d) | [ObjectPrimitives](ObjectPrimitives.md) | Kombiniert zwei 2D-Formen durch eine boolesche Operation: Vereinigung, Schnittmenge, Differenz oder symmetrische Differenz. |
| [`combineSolids`](Objects3D.md#combinesolids) | [3D Modeling](Objects3D.md#3d-modeling) | [Objects3D](Objects3D.md) | Kombiniert zwei Volumenkörper durch Vereinigung, Schnittmenge oder Differenz zu einem allgemeinen Volumenkörper. |
| [`convertSolid`](Objects3D.md#convertsolid) | [3D Modeling](Objects3D.md#3d-modeling) | [Objects3D](Objects3D.md) | Erstellt eine Kopie eines in einen allgemeinen Volumenkörper oder ein Netz konvertierten Volumenkörpers. |
| [`convertTo3D`](Objects3D.md#convertto3d) | [3D Modeling](Objects3D.md#3d-modeling) | [Objects3D](Objects3D.md) | Konvertiert eine Kopie eines Objekts in 3D-Polygone, ein Netz oder einen allgemeinen Volumenkörper. |
| [`convertToolCoordinates`](ToolAccess.md#converttoolcoordinates) | [InteractiveTools](ToolAccess.md#interactivetools) | [ToolAccess](ToolAccess.md) | Konvertiert Punkte zwischen dem Modellraum und der Ansicht des aktiven Fensters. |
| [`convertUnits`](DocumentAccess.md#convertunits) | [Document](DocumentAccess.md#document) | [DocumentAccess](DocumentAccess.md) | Konvertiert Längen zwischen Welteinheiten und Dokumenteinheiten. |
| [`copyAttributes`](ObjectPrimitives.md#copyattributes) | [Objects](ObjectPrimitives.md#objects) | [ObjectPrimitives](ObjectPrimitives.md) | Kopiert die grafischen Attribute eines Objekts auf andere Objekte. |
| [`create3DPolygon`](Objects3D.md#create3dpolygon) | [3D Modeling](Objects3D.md#3d-modeling) | [Objects3D](Objects3D.md) | Erstellt ein 3D-Polygon aus 3D-Punkten, aus 2D-Punkten auf einer Höhe oder aus einem Rechteck. |
| [`createAngularDimension`](ObjectsAnnotation.md#createangulardimension) | [Dimensioning](ObjectsAnnotation.md#dimensioning) | [ObjectsAnnotation](ObjectsAnnotation.md) | Erstellt eine Winkelbemaßung. |
| [`createArc`](ObjectPrimitives.md#createarc) | [Draw2D](ObjectPrimitives.md#draw2d) | [ObjectPrimitives](ObjectPrimitives.md) | Erstellt einen Kreisbogen anhand von Mittelpunkt, Radius und Winkeln oder durch drei Punkte. |
| [`createArcLengthDimension`](ObjectsAnnotation.md#createarclengthdimension) | [Dimensioning](ObjectsAnnotation.md#dimensioning) | [ObjectsAnnotation](ObjectsAnnotation.md) | Erstellt eine Bogenlängenbemaßung. |
| [`createCenterMark`](ObjectsAnnotation.md#createcentermark) | [Dimensioning](ObjectsAnnotation.md#dimensioning) | [ObjectsAnnotation](ObjectsAnnotation.md) | Erstellt eine Mittelpunktmarkierung für ein kreisförmiges Element. |
| [`createCircle`](ObjectPrimitives.md#createcircle) | [Draw2D](ObjectPrimitives.md#draw2d) | [ObjectPrimitives](ObjectPrimitives.md) | Erstellt einen Kreis anhand von Mittelpunkt und Radius oder durch drei Punkte. |
| [`createClass`](DocumentAccess.md#createclass) | [Document](DocumentAccess.md#document) | [DocumentAccess](DocumentAccess.md) | Erstellt eine Klasse oder gibt die bereits vorhandene Klasse dieses Namens zurück. |
| [`createColumn`](ObjectsArchitect.md#createcolumn) | [Architecture](ObjectsArchitect.md#architecture) | [ObjectsArchitect](ObjectsArchitect.md) | Erstellt eine Stütze. |
| [`createConnectCADDevice`](ObjectsConnectCAD.md#createconnectcaddevice) | [ConnectCAD](ObjectsConnectCAD.md#connectcad) | [ObjectsConnectCAD](ObjectsConnectCAD.md) | Erstellt ein Schaltplan-Gerät mit allen Anschlüssen anhand einer Gerätebeschreibung. |
| [`createConnectCADDevices`](ObjectsConnectCAD.md#createconnectcaddevices) | [ConnectCAD](ObjectsConnectCAD.md#connectcad) | [ObjectsConnectCAD](ObjectsConnectCAD.md) | Erstellt mehrere Schaltplan-Geräte nacheinander in einem Vorgang. |
| [`createConnectCADDeviceType`](ObjectsConnectCAD.md#createconnectcaddevicetype) | [ConnectCAD](ObjectsConnectCAD.md#connectcad) | [ObjectsConnectCAD](ObjectsConnectCAD.md) | Erstellt das Gerätetyp-Symbol eines Geräts. |
| [`createDataTag`](ObjectsAnnotation.md#createdatatag) | [Annotation](ObjectsAnnotation.md#annotation) | [ObjectsAnnotation](ObjectsAnnotation.md) | Erstellt einen Datenstempel, optional an ein Objekt angehängt. |
| [`createDoor`](ObjectsArchitect.md#createdoor) | [Architecture](ObjectsArchitect.md#architecture) | [ObjectsArchitect](ObjectsArchitect.md) | Erstellt eine freistehende Tür. |
| [`createExistingTree`](ObjectsLandmark.md#createexistingtree) | [Landmark](ObjectsLandmark.md#landmark) | [ObjectsLandmark](ObjectsLandmark.md) | Erstellt einen bestehenden Baum. |
| [`createExtrude`](Objects3D.md#createextrude) | [3D Modeling](Objects3D.md#3d-modeling) | [Objects3D](Objects3D.md) | Erstellt einen Extrusionskörper, Mehrfach-Extrusionskörper oder verjüngten Extrusionskörper. |
| [`createHardscape`](ObjectsLandmark.md#createhardscape) | [Landmark](ObjectsLandmark.md#landmark) | [ObjectsLandmark](ObjectsLandmark.md) | Erstellt einen Belag aus einem 2D-Pfadobjekt. |
| [`createLandscapeArea`](ObjectsLandmark.md#createlandscapearea) | [Landmark](ObjectsLandmark.md#landmark) | [ObjectsLandmark](ObjectsLandmark.md) | Erstellt eine Landschaftsfläche aus einem 2D-Pfadobjekt. |
| [`createLayer`](DocumentAccess.md#createlayer) | [Document](DocumentAccess.md#document) | [DocumentAccess](DocumentAccess.md) | Erstellt eine Konstruktionsebene oder Layoutebene. |
| [`createLightingDevice`](ObjectsSpotlight.md#createlightingdevice) | [Spotlight](ObjectsSpotlight.md#spotlight) | [ObjectsSpotlight](ObjectsSpotlight.md) | Erstellt ein Beleuchtungsgerät, optional mit einem GDTF-Scheinwerfertyp. |
| [`createLine`](ObjectPrimitives.md#createline) | [Draw2D](ObjectPrimitives.md#draw2d) | [ObjectPrimitives](ObjectPrimitives.md) | Erstellt eine gerade Linie zwischen zwei Punkten. |
| [`createLinearDimension`](ObjectsAnnotation.md#createlineardimension) | [Dimensioning](ObjectsAnnotation.md#dimensioning) | [ObjectsAnnotation](ObjectsAnnotation.md) | Erstellt eine gebundene, horizontale, vertikale, ungebundene oder Ordinatenbemaßung. |
| [`createLocus`](ObjectPrimitives.md#createlocus) | [Draw2D](ObjectPrimitives.md#draw2d) | [ObjectPrimitives](ObjectPrimitives.md) | Erstellt einen 2D-Ortsmarkierungspunkt (Referenzpunkt). |
| [`createMesh`](Objects3D.md#createmesh) | [3D Modeling](Objects3D.md#3d-modeling) | [Objects3D](Objects3D.md) | Erstellt ein Netz aus Scheitelpunkten und Flächen, aus Polygonen oder aus einer Gruppe von 3D-Polygonen. |
| [`createNurbsCurve`](Objects3D.md#createnurbscurve) | [3D Modeling](Objects3D.md#3d-modeling) | [Objects3D](Objects3D.md) | Erstellt eine NURBS-Kurve aus Kontrollpunkten oder Anpassungspunkten. |
| [`createNurbsSurface`](Objects3D.md#createnurbssurface) | [3D Modeling](Objects3D.md#3d-modeling) | [Objects3D](Objects3D.md) | Erstellt eine NURBS-Fläche aus ihrem Kontrollnetz. |
| [`createPlant`](ObjectsLandmark.md#createplant) | [Landmark](ObjectsLandmark.md#landmark) | [ObjectsLandmark](ObjectsLandmark.md) | Erstellt eine Pflanze an einem Punkt oder entlang eines Pfads. |
| [`createPluginObject`](ObjectPrimitives.md#createpluginobject) | [Objects](ObjectPrimitives.md#objects) | [ObjectPrimitives](ObjectPrimitives.md) | Erstellt ein Plug-in-Objekt, für das kein eigenes Erstellungs-Tool vorhanden ist. |
| [`createPolygon`](ObjectPrimitives.md#createpolygon) | [Draw2D](ObjectPrimitives.md#draw2d) | [ObjectPrimitives](ObjectPrimitives.md) | Erstellt ein Polygon aus Punkten oder ein regelmäßiges Polygon. |
| [`createPolyline`](ObjectPrimitives.md#createpolyline) | [Draw2D](ObjectPrimitives.md#draw2d) | [ObjectPrimitives](ObjectPrimitives.md) | Erstellt eine Polylinie aus Scheitelpunkten beliebigen Typs oder eine abgerundete Form. |
| [`createPropertyLine`](ObjectsLandmark.md#createpropertyline) | [Landmark](ObjectsLandmark.md#landmark) | [ObjectsLandmark](ObjectsLandmark.md) | Erstellt eine Grundstücksgrenze aus einem geschlossenen 2D-Pfadobjekt. |
| [`createRadialDimension`](ObjectsAnnotation.md#createradialdimension) | [Dimensioning](ObjectsAnnotation.md#dimensioning) | [ObjectsAnnotation](ObjectsAnnotation.md) | Erstellt eine Radial- oder Durchmesserbemaßung. |
| [`createRectangle`](ObjectPrimitives.md#createrectangle) | [Draw2D](ObjectPrimitives.md#draw2d) | [ObjectPrimitives](ObjectPrimitives.md) | Erstellt ein Rechteck, optional gedreht und mit abgerundeten Ecken. |
| [`createResource`](Resources.md#createresource) | [Resources](Resources.md#resources) | [Resources](Resources.md) | Erstellt eine leere Ressource. |
| [`createRoof`](ObjectsArchitect.md#createroof) | [Architecture](ObjectsArchitect.md#architecture) | [ObjectsArchitect](ObjectsArchitect.md) | Erstellt ein polygonales Dach. |
| [`createShell`](Objects3D.md#createshell) | [3D Modeling](Objects3D.md#3d-modeling) | [Objects3D](Objects3D.md) | Erstellt eine Schale durch Verdicken einer NURBS-Fläche oder Aushöhlen eines Volumenkörpers. |
| [`createSiteModel`](ObjectsLandmark.md#createsitemodel) | [Landmark](ObjectsLandmark.md#landmark) | [ObjectsLandmark](ObjectsLandmark.md) | Erstellt ein leeres Geländemodell. |
| [`createSiteModifier`](ObjectsLandmark.md#createsitemodifier) | [Landmark](ObjectsLandmark.md#landmark) | [ObjectsLandmark](ObjectsLandmark.md) | Erstellt einen Geländemodifikator aus einem 2D-Pfadobjekt. |
| [`createSlab`](ObjectsArchitect.md#createslab) | [Architecture](ObjectsArchitect.md#architecture) | [ObjectsArchitect](ObjectsArchitect.md) | Erstellt einen Boden/eine Decke aus einem 2D-Begrenzungsobjekt. |
| [`createSolidPrimitive`](Objects3D.md#createsolidprimitive) | [3D Modeling](Objects3D.md#3d-modeling) | [Objects3D](Objects3D.md) | Erstellt eine Kugel, ein Ellipsoid, eine Halbkugel, einen Kegel, Quader, Zylinder oder Torus. |
| [`createStair`](ObjectsArchitect.md#createstair) | [Architecture](ObjectsArchitect.md#architecture) | [ObjectsArchitect](ObjectsArchitect.md) | Erstellt eine Treppe. |
| [`createStake`](ObjectsLandmark.md#createstake) | [Landmark](ObjectsLandmark.md#landmark) | [ObjectsLandmark](ObjectsLandmark.md) | Erstellt einen Höhenpunkt. |
| [`createStory`](DocumentAccess.md#createstory) | [Document](DocumentAccess.md#document) | [DocumentAccess](DocumentAccess.md) | Erstellt ein oder mehrere Geschosse mit ihren Ebenen. |
| [`createSurfaceModel`](Objects3D.md#createsurfacemodel) | [3D Modeling](Objects3D.md#3d-modeling) | [Objects3D](Objects3D.md) | Erstellt aus vorhandenen Objekten ein Loft-, Schienensweep-, Rotations- oder Pfadextrusions-Flächenmodell. |
| [`createSweep`](Objects3D.md#createsweep) | [3D Modeling](Objects3D.md#3d-modeling) | [Objects3D](Objects3D.md) | Erstellt eine Rotation: 2D-Profile werden um eine Achse gedreht. |
| [`createText`](ObjectPrimitives.md#createtext) | [Draw2D](ObjectPrimitives.md#draw2d) | [ObjectPrimitives](ObjectPrimitives.md) | Erstellt ein Textobjekt. |
| [`createTitleBlock`](ObjectsAnnotation.md#createtitleblock) | [Annotation](ObjectsAnnotation.md#annotation) | [ObjectsAnnotation](ObjectsAnnotation.md) | Erstellt einen Plankopfstempel. |
| [`createWall`](ObjectsArchitect.md#createwall) | [Architecture](ObjectsArchitect.md#architecture) | [ObjectsArchitect](ObjectsArchitect.md) | Erstellt eine gerade oder runde Wand. |
| [`createWindow`](ObjectsArchitect.md#createwindow) | [Architecture](ObjectsArchitect.md#architecture) | [ObjectsArchitect](ObjectsArchitect.md) | Erstellt ein freistehendes Fenster. |

### Index D

| Werkzeug | Gruppe | Seite | Zusammenfassung |
|---|---|---|---|
| [`describePythonApi`](Scripting.md#describepythonapi) | [Scripting](Scripting.md#scripting) | [Scripting](Scripting.md) | Gibt den Hilfetext des Python-`api`-Moduls oder eines seiner Namen zurück. |

### Index E

| Werkzeug | Gruppe | Seite | Zusammenfassung |
|---|---|---|---|
| [`edit3DGeometry`](Objects3D.md#edit3dgeometry) | [3D Modeling](Objects3D.md#3d-modeling) | [Objects3D](Objects3D.md) | Bearbeitet ein 3D-Polygon, Netz, eine NURBS-Kurve oder NURBS-Fläche. |
| [`editClass`](DocumentAccess.md#editclass) | [Document](DocumentAccess.md#document) | [DocumentAccess](DocumentAccess.md) | Ändert eine Klasse: Beschreibung, Sichtbarkeit, Stift, Füllung, Markierungen, Schlagschatten und mehr. |
| [`editLayer`](DocumentAccess.md#editlayer) | [Document](DocumentAccess.md#document) | [DocumentAccess](DocumentAccess.md) | Ändert Eigenschaften einer Ebene, z. B. Name, Sichtbarkeit, Maßstab, Höhe und Dicke. |
| [`editObject`](ObjectPrimitives.md#editobject) | [Objects](ObjectPrimitives.md#objects) | [ObjectPrimitives](ObjectPrimitives.md) | Verschiebt, dreht, skaliert, spiegelt, dupliziert, gruppiert neu, konvertiert, setzt zurück oder löscht ein Objekt oder ändert dessen Namen und Klasse. |
| [`editResource`](Resources.md#editresource) | [Resources](Resources.md#resources) | [Resources](Resources.md) | Benennt eine Ressource um, beschreibt, verschiebt, dupliziert oder löscht sie. |
| [`editSelection`](DocumentAccess.md#editselection) | [Selection](DocumentAccess.md#selection) | [DocumentAccess](DocumentAccess.md) | Verschiebt, dreht, skaliert, dupliziert, gruppiert, löscht oder klassifiziert die Auswahl neu. |
| [`editSolid`](Objects3D.md#editsolid) | [3D Modeling](Objects3D.md#3d-modeling) | [Objects3D](Objects3D.md) | Verschiebt, dreht, skaliert, richtet einen Volumenkörper neu aus oder ändert seine Größe. |
| [`editStory`](DocumentAccess.md#editstory) | [Document](DocumentAccess.md#document) | [DocumentAccess](DocumentAccess.md) | Ändert ein Geschoss, die Ebenentypen des Dokuments oder dessen Standard-Geschossebenen. |
| [`editText`](ObjectPrimitives.md#edittext) | [Draw2D](ObjectPrimitives.md#draw2d) | [ObjectPrimitives](ObjectPrimitives.md) | Bearbeitet Inhalt und Formatierung eines Textobjekts. |
| [`editVertices`](ObjectPrimitives.md#editvertices) | [Draw2D](ObjectPrimitives.md#draw2d) | [ObjectPrimitives](ObjectPrimitives.md) | Fügt Scheitelpunkte eines Polygons oder einer Polylinie hinzu, ein, ändert, löscht, kehrt sie um oder ersetzt sie. |
| [`editWorksheet`](Resources.md#editworksheet) | [Resources](Resources.md#resources) | [Resources](Resources.md) | Ändert eine Tabelle anhand einer Aktionsliste. |

### Index F

| Werkzeug | Gruppe | Seite | Zusammenfassung |
|---|---|---|---|
| [`findMenuCommands`](MenuAccess.md#findmenucommands) | [Menus](MenuAccess.md#menus) | [MenuAccess](MenuAccess.md) | Sucht installierte Menübefehle nach Text und Arbeitsumgebung. |
| [`findObjects`](ObjectPrimitives.md#findobjects) | [Objects](ObjectPrimitives.md#objects) | [ObjectPrimitives](ObjectPrimitives.md) | Sucht Objekte, die einer Kriterienzeichenfolge entsprechen. |

### Index G

| Werkzeug | Gruppe | Seite | Zusammenfassung |
|---|---|---|---|
| [`get3DGeometry`](Objects3D.md#get3dgeometry) | [3D Modeling](Objects3D.md#3d-modeling) | [Objects3D](Objects3D.md) | Liest ein 3D-Polygon, Netz, eine NURBS-Kurve oder NURBS-Fläche. |
| [`getActiveTool`](ToolAccess.md#getactivetool) | [InteractiveTools](ToolAccess.md#interactivetools) | [ToolAccess](ToolAccess.md) | Gibt den Status des aktiven Tools zurück. |
| [`getAnnotationObject`](ObjectsAnnotation.md#getannotationobject) | [Annotation](ObjectsAnnotation.md#annotation) | [ObjectsAnnotation](ObjectsAnnotation.md) | Liest einen Datenstempel oder Plankopfstempel. |
| [`getArchitectureObject`](ObjectsArchitect.md#getarchitectureobject) | [Architecture](ObjectsArchitect.md#architecture) | [ObjectsArchitect](ObjectsArchitect.md) | Liest die Eigenschaften einer Wand, eines Bodens/einer Decke, Dachs, einer Tür, eines Fensters, einer Stütze oder Treppe. |
| [`getClasses`](DocumentAccess.md#getclasses) | [Document](DocumentAccess.md#document) | [DocumentAccess](DocumentAccess.md) | Listet die Klassen des Dokuments auf und benennt die speziellen Klassen. |
| [`getConnectCADDevice`](ObjectsConnectCAD.md#getconnectcaddevice) | [ConnectCAD](ObjectsConnectCAD.md#connectcad) | [ObjectsConnectCAD](ObjectsConnectCAD.md) | Liest ein ConnectCAD-Gerät und seine Anschlüsse. |
| [`getConnectCADDeviceType`](ObjectsConnectCAD.md#getconnectcaddevicetype) | [ConnectCAD](ObjectsConnectCAD.md#connectcad) | [ObjectsConnectCAD](ObjectsConnectCAD.md) | Liest den Datensatz Device Definition eines Gerätetyp-Symbols. |
| [`getDimension`](ObjectsAnnotation.md#getdimension) | [Dimensioning](ObjectsAnnotation.md#dimensioning) | [ObjectsAnnotation](ObjectsAnnotation.md) | Liest eine Bemaßung: Typ, gemessene Punkte, Wert und Texteinstellungen. |
| [`getDocumentInfo`](DocumentAccess.md#getdocumentinfo) | [Document](DocumentAccess.md#document) | [DocumentAccess](DocumentAccess.md) | Gibt eine Übersicht des aktiven Dokuments zurück: Datei, Anzahlen, Seitengrenzen, Ansichtsmitte und Benutzerursprung. |
| [`getGeometry`](ObjectPrimitives.md#getgeometry) | [Draw2D](ObjectPrimitives.md#draw2d) | [ObjectPrimitives](ObjectPrimitives.md) | Liest die typspezifische Geometrie eines 2D-Grundkörpers. |
| [`getIFCMapping`](IFC.md#getifcmapping) | [IFC Data Mapping](IFC.md#ifc-data-mapping) | [IFC](IFC.md) | Liest die Data-Manager-Zuordnung eines Zuordnungsobjekts. |
| [`getIFCPsetDefinition`](IFC.md#getifcpsetdefinition) | [IFC](IFC.md#ifc) | [IFC](IFC.md) | Liest eine IFC-Eigenschaftensatzdefinition anhand ihres Namens. |
| [`getLandmarkObject`](ObjectsLandmark.md#getlandmarkobject) | [Landmark](ObjectsLandmark.md#landmark) | [ObjectsLandmark](ObjectsLandmark.md) | Liest die Eigenschaften eines Gelände- oder Landschaftsobjekts. |
| [`getLayers`](DocumentAccess.md#getlayers) | [Document](DocumentAccess.md#document) | [DocumentAccess](DocumentAccess.md) | Listet Ebenen mit Typ, Sichtbarkeit, Maßstab, Höhe, Objektanzahl und Begrenzungen auf. |
| [`getLightingDevice`](ObjectsSpotlight.md#getlightingdevice) | [Spotlight](ObjectsSpotlight.md#spotlight) | [ObjectsSpotlight](ObjectsSpotlight.md) | Liest ein Beleuchtungsgerät. |
| [`getMenus`](MenuAccess.md#getmenus) | [Menus](MenuAccess.md#menus) | [MenuAccess](MenuAccess.md) | Liest die Menüleiste der aktuellen Arbeitsumgebung, ein Menü oder die Elemente eines Menüabschnitts. |
| [`getMenuStatus`](MenuAccess.md#getmenustatus) | [Menus](MenuAccess.md#menus) | [MenuAccess](MenuAccess.md) | Gibt an, ob ein Menübefehl oder Element eines Menüabschnitts jetzt ausgeführt werden kann und warum nicht. |
| [`getObjectAttributes`](ObjectPrimitives.md#getobjectattributes) | [Objects](ObjectPrimitives.md#objects) | [ObjectPrimitives](ObjectPrimitives.md) | Gibt die grafischen Attribute eines Objekts zurück. |
| [`getObjectDimensions`](ObjectsAnnotation.md#getobjectdimensions) | [Dimensioning](ObjectsAnnotation.md#dimensioning) | [ObjectsAnnotation](ObjectsAnnotation.md) | Listet die einem Objekt zugeordneten Bemaßungen auf. |
| [`getObjectIFCData`](IFC.md#getobjectifcdata) | [IFC](IFC.md#ifc) | [IFC](IFC.md) | Liest die IFC-Daten eines Objekts so, wie sie beim IFC-Export berechnet werden. |
| [`getObjectInfo`](ObjectPrimitives.md#getobjectinfo) | [Objects](ObjectPrimitives.md#objects) | [ObjectPrimitives](ObjectPrimitives.md) | Gibt Identität, Klasse, Ebene, Begrenzungen, Status und Container eines Objekts zurück. |
| [`getObjectParameters`](ObjectPrimitives.md#getobjectparameters) | [Objects](ObjectPrimitives.md#objects) | [ObjectPrimitives](ObjectPrimitives.md) | Liest die Parameter eines Plug-in-Objekts. |
| [`getObjectRecords`](ObjectPrimitives.md#getobjectrecords) | [Objects](ObjectPrimitives.md#objects) | [ObjectPrimitives](ObjectPrimitives.md) | Liest die an ein Objekt angehängten Datensätze. |
| [`getObjectsAtPoint`](ObjectPrimitives.md#getobjectsatpoint) | [Objects](ObjectPrimitives.md#objects) | [ObjectPrimitives](ObjectPrimitives.md) | Sucht Objekte an einem Punkt. |
| [`getObjectTags`](ObjectsAnnotation.md#getobjecttags) | [Annotation](ObjectsAnnotation.md#annotation) | [ObjectsAnnotation](ObjectsAnnotation.md) | Listet die an ein Objekt angehängten Datenstempel auf. |
| [`getOIPControls`](OIPAccess.md#getoipcontrols) | [Object Info](OIPAccess.md#object-info) | [OIPAccess](OIPAccess.md) | Listet die Steuerelemente eines Bereichs der Objekt-Info-Palette auf. |
| [`getPluginDefinition`](ObjectPrimitives.md#getplugindefinition) | [Objects](ObjectPrimitives.md#objects) | [ObjectPrimitives](ObjectPrimitives.md) | Beschreibt ein installiertes Plug-in-Objekt: Typ, Parameter und Popup-Auswahlmöglichkeiten. |
| [`getPreferences`](DocumentAccess.md#getpreferences) | [Document](DocumentAccess.md#document) | [DocumentAccess](DocumentAccess.md) | Liest eine Kategorie der Dokumenteinstellungen. |
| [`getProjectData`](ObjectsAnnotation.md#getprojectdata) | [Annotation](ObjectsAnnotation.md#annotation) | [ObjectsAnnotation](ObjectsAnnotation.md) | Liest die Plankopf-Projektdaten des Dokuments. |
| [`getPythonApiGuide`](Scripting.md#getpythonapiguide) | [Scripting](Scripting.md#scripting) | [Scripting](Scripting.md) | Gibt einen Abschnitt der Anleitung zum Schreiben von Python-Skripten zurück. |
| [`getResource`](Resources.md#getresource) | [Resources](Resources.md#resources) | [Resources](Resources.md) | Liest eine Ressource der Zeichnung. |
| [`getResourceDetails`](Resources.md#getresourcedetails) | [Resources](Resources.md#resources) | [Resources](Resources.md) | Liest den Inhalt einer Ressource: Schraffurstufen, Verlaufsstopps, Linientyp-Striche und mehr. |
| [`getResources`](Resources.md#getresources) | [Resources](Resources.md#resources) | [Resources](Resources.md) | Listet Ressourcen eines Typs aus der Zeichnung, einer Bibliothek, einer Datei oder einem anderen Dokument auf. |
| [`getResourceTypes`](Resources.md#getresourcetypes) | [Resources](Resources.md#resources) | [Resources](Resources.md) | Listet die Ressourcentypen und die Standardordner für Inhalte auf. |
| [`getScript`](Scripting.md#getscript) | [Scripting](Scripting.md#scripting) | [Scripting](Scripting.md) | Liest eine Skriptressource, ohne sie auszuführen. |
| [`getSelection`](DocumentAccess.md#getselection) | [Selection](DocumentAccess.md#selection) | [DocumentAccess](DocumentAccess.md) | Listet die ausgewählten Objekte auf allen Ebenen und die Begrenzungen der Auswahl auf. |
| [`getSolid`](Objects3D.md#getsolid) | [3D Modeling](Objects3D.md#3d-modeling) | [Objects3D](Objects3D.md) | Liest einen Volumenkörper: Typ, 3D-Begrenzungen, Parameter und Verlauf des allgemeinen Volumenkörpers. |
| [`getStories`](DocumentAccess.md#getstories) | [Document](DocumentAccess.md#document) | [DocumentAccess](DocumentAccess.md) | Listet die Geschosse mit ihren Ebenen von unten nach oben auf. |
| [`getText`](ObjectPrimitives.md#gettext) | [Draw2D](ObjectPrimitives.md#draw2d) | [ObjectPrimitives](ObjectPrimitives.md) | Liest ein Textobjekt: Inhalt, Zeichenformatierung, Stil und Layout. |
| [`getTool`](ToolAccess.md#gettool) | [InteractiveTools](ToolAccess.md#interactivetools) | [ToolAccess](ToolAccess.md) | Gibt ein Tool mit den deklarierten Modusschaltflächen zurück. |
| [`getToolModes`](ToolAccess.md#gettoolmodes) | [InteractiveTools](ToolAccess.md#interactivetools) | [ToolAccess](ToolAccess.md) | Liest die aktuelle Modusleiste des aktiven Tools. |
| [`getTools`](ToolAccess.md#gettools) | [InteractiveTools](ToolAccess.md#interactivetools) | [ToolAccess](ToolAccess.md) | Listet die Vectorworks-Tools auf. |
| [`getUnits`](DocumentAccess.md#getunits) | [Document](DocumentAccess.md#document) | [DocumentAccess](DocumentAccess.md) | Gibt die Einstellungen der primären und sekundären Einheiten des Dokuments zurück. |
| [`getWorksheet`](Resources.md#getworksheet) | [Resources](Resources.md#resources) | [Resources](Resources.md) | Liest eine Tabelle: Größe, Zellen, Formate und Datenbankzeilen. |

### Index I

| Werkzeug | Gruppe | Seite | Zusammenfassung |
|---|---|---|---|
| [`importGDTF`](ObjectsSpotlight.md#importgdtf) | [Spotlight](ObjectsSpotlight.md#spotlight) | [ObjectsSpotlight](ObjectsSpotlight.md) | Importiert eine .gdtf-Datei als GDTF-Scheinwerfertyp in die Zeichnung. |
| [`importResource`](Resources.md#importresource) | [Resources](Resources.md#resources) | [Resources](Resources.md) | Importiert eine externe Ressource in die Zeichnung. |

### Index L

| Werkzeug | Gruppe | Seite | Zusammenfassung |
|---|---|---|---|
| [`listConnectCADConnectors`](ObjectsConnectCAD.md#listconnectcadconnectors) | [ConnectCAD](ObjectsConnectCAD.md#connectcad) | [ObjectsConnectCAD](ObjectsConnectCAD.md) | Listet die ConnectCAD-Steckertypen und ihre Pins auf. |
| [`listConnectCADSignals`](ObjectsConnectCAD.md#listconnectcadsignals) | [ConnectCAD](ObjectsConnectCAD.md#connectcad) | [ObjectsConnectCAD](ObjectsConnectCAD.md) | Listet die ConnectCAD-Signaltypen auf. |
| [`listGDTFs`](ObjectsSpotlight.md#listgdtfs) | [Spotlight](ObjectsSpotlight.md#spotlight) | [ObjectsSpotlight](ObjectsSpotlight.md) | Listet verfügbare GDTF-Scheinwerfertypen und ihre DMX-Modi auf. |
| [`listIFCCustomPsets`](IFC.md#listifccustompsets) | [IFC](IFC.md#ifc) | [IFC](IFC.md) | Listet die benutzerdefinierten IFC-Eigenschaftensatzdefinitionen des Dokuments auf. |
| [`listIFCMappingObjects`](IFC.md#listifcmappingobjects) | [IFC Data Mapping](IFC.md#ifc-data-mapping) | [IFC](IFC.md) | Listet die Zuordnungsobjekte der aktiven Data-Manager-Zuordnung auf. |
| [`listIFCPsets`](IFC.md#listifcpsets) | [IFC](IFC.md#ifc) | [IFC](IFC.md) | Listet IFC-Eigenschaftensätze auf, die für einen IFC-Entitätstyp gelten. |
| [`listScripts`](Scripting.md#listscripts) | [Scripting](Scripting.md#scripting) | [Scripting](Scripting.md) | Listet die Skriptressourcen des Dokuments auf. |
| [`listToolGroups`](Common.md#listtoolgroups) | [Core](Common.md#core-gruppe) | [Common](Common.md) | Listet alle aktiven und inaktiven Tool-Gruppen mit ihrem Aktivierungsstatus und optional ihren Tools auf. |

### Index P

| Werkzeug | Gruppe | Seite | Zusammenfassung |
|---|---|---|---|
| [`pressOIPButton`](OIPAccess.md#pressoipbutton) | [Object Info](OIPAccess.md#object-info) | [OIPAccess](OIPAccess.md) | Betätigt eine Schaltfläche der Objekt-Info-Palette. |

### Index Q

| Werkzeug | Gruppe | Seite | Zusammenfassung |
|---|---|---|---|
| [`queryGeometry`](ObjectPrimitives.md#querygeometry) | [Draw2D](ObjectPrimitives.md#draw2d) | [ObjectPrimitives](ObjectPrimitives.md) | Beantwortet geometrische Fragen zu einem 2D-Grundkörper: nächster Punkt, Abstand, Enthaltensein, Schnittpunkte, Tangenten und Messungen entlang von Kurven. |

### Index R

| Werkzeug | Gruppe | Seite | Zusammenfassung |
|---|---|---|---|
| [`runMenuCommand`](MenuAccess.md#runmenucommand) | [Menus](MenuAccess.md#menus) | [MenuAccess](MenuAccess.md) | Führt einen Menübefehl oder ein Element eines Menüabschnitts aus, als hätte der Benutzer es ausgewählt. |
| [`runPythonScript`](Scripting.md#runpythonscript) | [Scripting](Scripting.md#scripting) | [Scripting](Scripting.md) | Führt Python-Code in Vectorworks aus. |
| [`runScript`](Scripting.md#runscript) | [Scripting](Scripting.md#scripting) | [Scripting](Scripting.md) | Führt eine gespeicherte Python-Skriptressource aus. |
| [`runToolBatch`](Common.md#runtoolbatch) | [Core](Common.md#core-gruppe) | [Common](Common.md) | Führt mehrere Tool-Aufrufe als einen Rückgängig-Schritt aus; entweder alle oder keinen. |

### Index S

| Werkzeug | Gruppe | Seite | Zusammenfassung |
|---|---|---|---|
| [`saveScript`](Scripting.md#savescript) | [Scripting](Scripting.md#scripting) | [Scripting](Scripting.md) | Erstellt oder aktualisiert eine Python-Skriptressource, ohne sie auszuführen. |
| [`selectObjects`](DocumentAccess.md#selectobjects) | [Selection](DocumentAccess.md#selection) | [DocumentAccess](DocumentAccess.md) | Wählt Objekte nach Kriterien oder UUID aus bzw. ab oder wählt alle oder keine aus. |
| [`sendToolAction`](ToolAccess.md#sendtoolaction) | [InteractiveTools](ToolAccess.md#interactivetools) | [ToolAccess](ToolAccess.md) | Beendet oder bricht die Aktion des aktiven Tools ab oder entfernt dessen letzten Punkt. |
| [`sendToolPointer`](ToolAccess.md#sendtoolpointer) | [InteractiveTools](ToolAccess.md#interactivetools) | [ToolAccess](ToolAccess.md) | Klickt, doppelklickt, bewegt den Zeiger oder zieht mit dem aktiven Tool in der Zeichnung. |
| [`setActiveContext`](DocumentAccess.md#setactivecontext) | [Document](DocumentAccess.md#document) | [DocumentAccess](DocumentAccess.md) | Legt die aktive Ebene und Klasse sowie die Anzeige der anderen Ebenen und Klassen fest. |
| [`setAnnotationObject`](ObjectsAnnotation.md#setannotationobject) | [Annotation](ObjectsAnnotation.md#annotation) | [ObjectsAnnotation](ObjectsAnnotation.md) | Bearbeitet einen Datenstempel oder Plankopfstempel. |
| [`setArchitectureObject`](ObjectsArchitect.md#setarchitectureobject) | [Architecture](ObjectsArchitect.md#architecture) | [ObjectsArchitect](ObjectsArchitect.md) | Bearbeitet eine Wand, einen Boden/eine Decke, ein Dach, eine Tür, ein Fenster, eine Stütze oder eine Treppe. |
| [`setConnectCADSocket`](ObjectsConnectCAD.md#setconnectcadsocket) | [ConnectCAD](ObjectsConnectCAD.md#connectcad) | [ObjectsConnectCAD](ObjectsConnectCAD.md) | Bearbeitet einen Anschluss. |
| [`setDimension`](ObjectsAnnotation.md#setdimension) | [Dimensioning](ObjectsAnnotation.md#dimensioning) | [ObjectsAnnotation](ObjectsAnnotation.md) | Bearbeitet eine Bemaßung. |
| [`setGeometry`](ObjectPrimitives.md#setgeometry) | [Draw2D](ObjectPrimitives.md#draw2d) | [ObjectPrimitives](ObjectPrimitives.md) | Bearbeitet die Geometrie eines 2D-Grundkörpers. |
| [`setLandmarkObject`](ObjectsLandmark.md#setlandmarkobject) | [Landmark](ObjectsLandmark.md#landmark) | [ObjectsLandmark](ObjectsLandmark.md) | Bearbeitet ein Gelände- oder Landschaftsobjekt. |
| [`setLightingDevice`](ObjectsSpotlight.md#setlightingdevice) | [Spotlight](ObjectsSpotlight.md#spotlight) | [ObjectsSpotlight](ObjectsSpotlight.md) | Bearbeitet ein Beleuchtungsgerät. |
| [`setObjectAttributes`](ObjectPrimitives.md#setobjectattributes) | [Objects](ObjectPrimitives.md#objects) | [ObjectPrimitives](ObjectPrimitives.md) | Legt grafische Attribute eines Objekts fest: Stift, Füllung, Deckkraft, Markierungen, Schlagschatten und mehr. |
| [`setObjectParameter`](ObjectPrimitives.md#setobjectparameter) | [Objects](ObjectPrimitives.md#objects) | [ObjectPrimitives](ObjectPrimitives.md) | Schreibt einen oder mehrere Parameter eines Plug-in-Objekts. |
| [`setOIPValues`](OIPAccess.md#setoipvalues) | [Object Info](OIPAccess.md#object-info) | [OIPAccess](OIPAccess.md) | Legt Steuerelemente der Objekt-Info-Palette wie ein Benutzer fest. |
| [`setPreferences`](DocumentAccess.md#setpreferences) | [Document](DocumentAccess.md#document) | [DocumentAccess](DocumentAccess.md) | Schreibt Dokumenteinstellungen einer Kategorie. |
| [`setProjectData`](ObjectsAnnotation.md#setprojectdata) | [Annotation](ObjectsAnnotation.md#annotation) | [ObjectsAnnotation](ObjectsAnnotation.md) | Schreibt die Plankopf-Projektdaten des Dokuments. |
| [`setResourceDetails`](Resources.md#setresourcedetails) | [Resources](Resources.md#resources) | [Resources](Resources.md) | Ändert den Inhalt einer Ressource. |
| [`setToolMode`](ToolAccess.md#settoolmode) | [InteractiveTools](ToolAccess.md#interactivetools) | [ToolAccess](ToolAccess.md) | Ändert einen Modus des aktiven Tools. |
| [`setToolModes`](ToolAccess.md#settoolmodes) | [InteractiveTools](ToolAccess.md#interactivetools) | [ToolAccess](ToolAccess.md) | Legt mehrere Modi des aktiven Tools fest. |
| [`setUnits`](DocumentAccess.md#setunits) | [Document](DocumentAccess.md#document) | [DocumentAccess](DocumentAccess.md) | Ändert die Einstellungen der primären oder sekundären Einheiten des Dokuments. |
| [`setView`](DocumentAccess.md#setview) | [Document](DocumentAccess.md#document) | [DocumentAccess](DocumentAccess.md) | Verschiebt die Ansicht, legt den Zoom fest, verschiebt den Benutzerursprung oder zeichnet die Seite neu. |

### Index T

| Werkzeug | Gruppe | Seite | Zusammenfassung |
|---|---|---|---|
| [`tagObject`](ObjectsAnnotation.md#tagobject) | [Annotation](ObjectsAnnotation.md#annotation) | [ObjectsAnnotation](ObjectsAnnotation.md) | Hängt einen Datenstempel an ein Objekt an oder löst die Verknüpfung. |

### Index V

| Werkzeug | Gruppe | Seite | Zusammenfassung |
|---|---|---|---|
| [`validateConnectCADDevice`](ObjectsConnectCAD.md#validateconnectcaddevice) | [ConnectCAD](ObjectsConnectCAD.md#connectcad) | [ObjectsConnectCAD](ObjectsConnectCAD.md) | Prüft eine Gerätebeschreibung, ohne etwas zu erstellen. |

## Seitenaufbau

Jede Seite eines Tool-Ordners folgt demselben Aufbau:

1. **Titel** — Ordner und Thema, Server und Vectorworks-Version sowie ein Link zurück zu diesem Index.
2. **Inhaltsverzeichnis** — alle Gruppen und Tools der Seite.
3. **Übersicht** — eine Zeile pro Gruppe mit Gruppen-ID, Standardaktivierung, Sicherheitsstufe, Tool-Anzahl und einer kurzen Zusammenfassung.
4. **Gruppen** — für jede Gruppe: Gruppen-ID, Aktivierung und Sicherheitsstufe, Zusammenfassung, vom Server gemeldete Beschreibung und eine Tabelle ihrer Tools mit Auswirkung, Sicherheitsstufe und Zusammenfassung.
5. **Werkzeuge** — für jedes Tool: kurze Zusammenfassung; Auswirkung, Sicherheitsstufe, Rückgängig-Verhalten und Ausführbarkeit innerhalb von `runToolBatch`; die vom Server gemeldeten **Details** und die Tabelle **Parameter** (Name, Typ, erforderlich, Beschreibung). Elemente von Objektparametern werden als `parameter.member`, Elemente von Array-Elementen als `parameter[].member` aufgeführt. Wenn bekannt, listet der Abschnitt **Ergebnis** die Ergebnisschlüssel auf; **Fehler** führt Fehlermeldungen auf, und ein **Hinweis** ergänzt Verhalten, das in der Beschreibung nicht genannt wird.

Links auf gemeinsam verwendete Formate verweisen auf [Common](Common.md) und [Attributes](Attributes.md), zum Beispiel [Punkt](Common.md#punkte), [Farbe](Common.md#farben) oder [Markierung](Attributes.md#linienendmarkierungen).

## Statistik

| Seite | Gruppen | Werkzeuge | Parameter | Schreibgeschützt | Bearbeitung | Interaktiv | Skriptlauf |
|---|---|---|---|---|---|---|---|
| [DocumentAccess](DocumentAccess.md) | 2 | 20 | 129 | 8 | 12 | 0 | 0 |
| [IFC](IFC.md) | 2 | 6 | 8 | 6 | 0 | 0 | 0 |
| [MenuAccess](MenuAccess.md) | 1 | 4 | 19 | 3 | 0 | 1 | 0 |
| [ObjectPrimitives](ObjectPrimitives.md) | 2 | 27 | 273 | 10 | 17 | 0 | 0 |
| [Objects3D](Objects3D.md) | 1 | 16 | 193 | 2 | 14 | 0 | 0 |
| [ObjectsAnnotation](ObjectsAnnotation.md) | 2 | 16 | 338 | 5 | 11 | 0 | 0 |
| [ObjectsArchitect](ObjectsArchitect.md) | 1 | 9 | 127 | 1 | 8 | 0 | 0 |
| [ObjectsConnectCAD](ObjectsConnectCAD.md) | 1 | 10 | 39 | 5 | 5 | 0 | 0 |
| [ObjectsLandmark](ObjectsLandmark.md) | 1 | 10 | 190 | 1 | 9 | 0 | 0 |
| [ObjectsSpotlight](ObjectsSpotlight.md) | 1 | 5 | 30 | 2 | 3 | 0 | 0 |
| [OIPAccess](OIPAccess.md) | 1 | 3 | 14 | 1 | 0 | 2 | 0 |
| [Resources](Resources.md) | 1 | 11 | 122 | 5 | 6 | 0 | 0 |
| [Scripting](Scripting.md) | 1 | 7 | 11 | 4 | 1 | 0 | 2 |
| [ToolAccess](ToolAccess.md) | 1 | 10 | 44 | 5 | 0 | 5 | 0 |
| **Gesamt** | **18** | **154** | **1537** | **58** | **86** | **8** | **2** |

Die Parameteranzahl bezieht sich auf die Parameter der obersten Ebene der Tools. Interaktiv umfasst das Tool für Menübefehle. Die Gruppe [Core](Common.md#core-gruppe) enthält zusätzlich 3 immer verfügbare Meta-Tools. `listToolGroups` ist schreibgeschützt, `activateToolGroups` eine Sitzungseinstellung und `runToolBatch` eine Batch-Bearbeitung; zusammen haben sie 5 Parameter der obersten Ebene.

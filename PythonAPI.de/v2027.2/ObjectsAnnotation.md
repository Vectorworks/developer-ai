[English](../../PythonAPI/v2027.2/ObjectsAnnotation.md) • **Deutsch** • [日本語](../../PythonAPI.ja/v2027.2/ObjectsAnnotation.md)

# ObjectsAnnotation — Bemaßungen, Datenstempel, Planköpfe und Tabellen

> **Python-Modul:** `api` · **Version:** Vectorworks 2027 Update 2

[Zurück zum Index](README.md)

Die Beschriftungsklassen. Beschriftungsobjekte beschreiben nicht das Gebäude, sondern die Zeichnung: Sie lesen Daten aus Objekten und dem Dokument und geben sie auf dem Plan aus.

`AnnotationObject` ist die Basisklasse der Plug-in-basierten Beschriftungen (`DataTagObject` beschriftet ein Objekt mit daraus gelesenen Daten, `TitleBlockBorderObject` umfasst Planrahmen, Rastereinteilung und Plankopf). Beide beziehen ihre grafische Darstellung aus einem **Stil** des Objekts. Daher ermitteln ihre `Create`-Funktionen einen Stil (und importieren einen aus den Vectorworks-Bibliotheken, wenn die Zeichnung keinen enthält) und schlagen fehl, wenn keiner verfügbar ist.

Bemaßungen bilden den anderen Teil der Beschriftung: `DimensionObject` enthält die gemeinsamen Einstellungen aller Bemaßungen, und `LinearDimensionObject`, `AngularDimensionObject`, `ArcLengthDimensionObject` und `RadialDimensionObject` messen Abstände, Winkel, Bogenlängen und Radien bzw. Durchmesser. Anders als Datenstempel und Planköpfe sind Bemaßungen Vectorworks-eigene Objekte ohne Plug-in-Datenbank oder -Stil: Ihr Aussehen wird vom referenzierten Bemaßungsstandard bestimmt. `CenterMarkObject` ist das Mittelpunktkreuz eines Kreises oder Kreisbogens (eine Gruppe von Linien, keine Bemaßung). `WorksheetObject` bearbeitet Tabellen (Zubehör).

## Inhaltsverzeichnis

- [Überblick](#überblick)
- [Klassen](#klassen)
  - [AnnotationObject](#annotationobject)
  - [DataTagObject](#datatagobject)
    - [DataTagObject.LeaderType](#datatagobjectleadertype)
    - [DataTagObject.HorizontalPosition](#datatagobjecthorizontalposition)
    - [DataTagObject.MoveBehaviour](#datatagobjectmovebehaviour)
  - [TitleBlockBorderObject](#titleblockborderobject)
    - [TitleBlockBorderObject.Revision](#titleblockborderobjectrevision)
  - [DimensionObject](#dimensionobject)
  - [LinearDimensionObject](#lineardimensionobject)
  - [AngularDimensionObject](#angulardimensionobject)
  - [ArcLengthDimensionObject](#arclengthdimensionobject)
  - [RadialDimensionObject](#radialdimensionobject)
  - [CenterMarkObject](#centermarkobject)
  - [WorksheetObject](#worksheetobject)
    - [WorksheetObject.Range](#worksheetobjectrange)
    - [WorksheetObject.NumberFormat](#worksheetobjectnumberformat)
    - [WorksheetObject.TextFormat](#worksheetobjecttextformat)
    - [WorksheetObject.Fill](#worksheetobjectfill)
    - [WorksheetObject.Borders](#worksheetobjectborders)
- [Aufzählungen](#aufzählungen)
  - [DimensionKind](#dimensionkind)
  - [DimensionTolerance](#dimensiontolerance)

## Überblick

| Name | Art | Erbt von | Zusammenfassung |
|---|---|---|---|
| [`AnnotationObject`](#annotationobject) | Klasse | [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) | Gemeinsame Basisklasse der Beschriftungs-Plug-in-Objektklassen (Datenstempel, Plankopf). |
| [`DataTagObject`](#datatagobject) | Klasse | [`AnnotationObject`](#annotationobject) | Plug-in-Objekt Datenstempel (universeller Name "Data Tag"). |
| [`DataTagObject.LeaderType`](#datatagobjectleadertype) | IntEnum (verschachtelt) |  | Form der Verweislinie eines Datenstempels („Verweislinientyp“). |
| [`DataTagObject.HorizontalPosition`](#datatagobjecthorizontalposition) | IntEnum (verschachtelt) |  | Seite der Verweislinie, auf der sich der Stempeltext befindet („Horizontale Position“). |
| [`DataTagObject.MoveBehaviour`](#datatagobjectmovebehaviour) | IntEnum (verschachtelt) |  | Was beim Ziehen des Stempels in der Zeichnung verschoben wird: der gesamte Stempel oder nur die Spitze seiner Verweislinie. |
| [`TitleBlockBorderObject`](#titleblockborderobject) | Klasse | [`AnnotationObject`](#annotationobject) | Plug-in-Objekt Plankopf (universeller Name "Title Block Border"). |
| [`TitleBlockBorderObject.Revision`](#titleblockborderobjectrevision) | Klasse (verschachtelt) |  | Eine Revision eines Plankopfs: Nummer, Datum, Anmerkung, Veröffentlichungsdatum und Empfänger. |
| [`DimensionObject`](#dimensionobject) | Klasse | [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) | Basisklasse jedes Bemaßungsobjekts (`ObjectType.Dimension`). |
| [`LinearDimensionObject`](#lineardimensionobject) | Klasse | [`DimensionObject`](#dimensionobject) | Lineare Bemaßung: misst den Abstand zwischen zwei Punkten. |
| [`AngularDimensionObject`](#angulardimensionobject) | Klasse | [`DimensionObject`](#dimensionobject) | Winkelbemaßung: misst den Winkel zwischen zwei Schenkeln, die sich in einem Scheitelpunkt treffen. |
| [`ArcLengthDimensionObject`](#arclengthdimensionobject) | Klasse | [`DimensionObject`](#dimensionobject) | Bogenbemaßung: misst die Länge ENTLANG eines Kreisbogens statt des geradlinigen Abstands zwischen seinen Endpunkten, den eine lineare Bemaßung angeben würde. |
| [`RadialDimensionObject`](#radialdimensionobject) | Klasse | [`DimensionObject`](#dimensionobject) | Kreisbemaßung: Misst den Radius oder den Durchmesser eines Kreises oder Kreisbogens. |
| [`CenterMarkObject`](#centermarkobject) | Klasse | [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) | Achsenkreuz: das Kreuz, das den Mittelpunkt eines Kreises oder Kreisbogens kennzeichnet. |
| [`WorksheetObject`](#worksheetobject) | Klasse | [`TypedResource`](Resources.md#typedresource) | Verweis auf eine Tabelle (ZUBEHÖR) ohne Übernahme des Objekts, keine platzierte Tabellengrafik und kein Plug-in-Objekt zur Beschriftung. |
| [`WorksheetObject.Range`](#worksheetobjectrange) | Klasse (verschachtelt) |  | Ab 1 indizierter Tabellenbereich einschließlich seiner Grenzen. |
| [`WorksheetObject.NumberFormat`](#worksheetobjectnumberformat) | Klasse (verschachtelt) |  | Vectorworks-eigenes Zahlenformat für Tabellen, einschließlich formatabhängiger Genauigkeit und UTF-8-Präfix/-Suffix. |
| [`WorksheetObject.TextFormat`](#worksheetobjecttextformat) | Klasse (verschachtelt) |  | Tabellentext: Punktgröße, Schriftart/-stil, Ausrichtungen, Winkel in Grad, ColorRef-Index und Zeilenumbruch. |
| [`WorksheetObject.Fill`](#worksheetobjectfill) | Klasse (verschachtelt) |  | Vectorworks-eigener Füllstil, ColorRef-Indizes des Dokuments und Muster. |
| [`WorksheetObject.Borders`](#worksheetobjectborders) | Klasse (verschachtelt) |  | Kennzeichen für Zellenränder sowie für die Anwendung auf den äußeren Rahmen und die inneren Ränder eines Bereichs. |
| [`DimensionKind`](#dimensionkind) | IntEnum |  | Bemaßungsart eines Objekts. |
| [`DimensionTolerance`](#dimensiontolerance) | IntEnum |  | Abweichung einer Bemaßung vom Nennwert, die neben dem Messwert ausgegeben wird. |

## Klassen

### AnnotationObject

> **Vollständiger Name:** `api.AnnotationObject` · **Erbt von:** [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Gemeinsame Basisklasse der Beschriftungs-Plug-in-Objektklassen (Datenstempel, Plankopf).

Ein Beschriftungsobjekt beschreibt keinen Gebäudeteil, sondern die Zeichnung. Es liest Daten aus den Objekten und dem Dokument und gibt sie auf dem Plan aus. Beide Beschriftungsobjekte sind Vectorworks-Plug-in-Objekte (Instanzen eines Plug-ins, in der API auch parametrische Objekte genannt), die anhand ihres universellen (parametrischen) Namens identifiziert werden: "Data Tag" und "Title Block Border".

Im Unterschied zu den Architect-/Landmark-Klassen stammt ihre grafische Darstellung nahezu vollständig aus einem STIL des Objekts (einem „Stil für Intelligente Objekte“): einer Symboldefinition mit einer Hauptinstanz des Plug-ins sowie der Text- und Geometrieanordnung, die auf jedes Objekt mit diesem Stil übertragen wird. Ein Datenstempel ohne Stil hat keine Textanordnung, und ein Plankopfobjekt ohne Stil hat keine Plankopfgrafik. Deshalb ermitteln beide Klassen beim Erstellen des Objekts einen Stil – siehe `DataTagObject.Create` und `TitleBlockBorderObject.Create` – und machen ihn über GetStyleName / SetStyle zugänglich.

Von PrimitiveObject übernommene Konventionen:

- Lesemethoden geben bei einem ungültigen Objekt oder fehlenden Parameter `None` zurück.
- Schreibmethoden geben bei Erfolg `True` und bei einem ungültigen Objekt oder fehlenden Parameter `False` zurück.
- Längen werden in Welteinheiten angegeben, Winkel im Bogenmaß; Zeichenfolgen sind UTF-8-kodiert.

Grundlagen des Parameterzugriffs (Get/SetParam*):

- Jedes Beschriftungsobjekt speichert seine Daten in einer Datenbank mit benannten Feldern („Parametern“). Jede Unterklasse führt die relevanten Parameternamen in ihrer „Vollständigen Parameterreferenz“ auf. Verwenden Sie diese Namen unverändert (Groß-/Kleinschreibung beachten, UTF-8) mit GetParamString / SetParamString / GetParamReal / ..., um Felder zu lesen oder zu schreiben, für die die Unterklasse keine eigene typisierte Zugriffsmethode bereitstellt.
- Für Parametertypen werden in den Tabellen folgende Kennzeichnungen verwendet:

- Zeichenfolge — Text (UTF-8) - GetParamString / SetParamString
- int — 32-Bit-Ganzzahl - GetParamInt / SetParamInt
- bool — boolescher Wert - GetParamBool / SetParamBool
- reell — Gleitkommawert (Weltkoordinate, Winkel in GRAD, einfache Zahl, ...) - GetParamReal / SetParamReal
- Auswahlliste — Auswahl einer Zeichenkette aus N Möglichkeiten - GetParamString / SetParamString; gültige Werte stehen neben dem Parameter

- Parameternamen, die mit einem doppelten Unterstrich ("__") beginnen, gehören zum privaten Zustand des Plug-ins; sie sind lesbar, direkte Änderungen sind jedoch in der Regel nicht sinnvoll.
- Ein Parameter, den das Objekt „nach Stil“ übernimmt, wird aus der Stilsymboldefinition gelesen. Das Schreiben an der Instanz hat keine dauerhafte Wirkung, bis der Parameter auf „nach Instanz“ umgestellt wird.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `AnnotationObject(h: Handle)` | Verweist auf ein beliebiges Objekt `h` als generisches `AnnotationObject`; `IsValid()` prüft nur, ob das Handle nicht null ist. Prüfen Sie die Objektart mit `GetParametricName()` oder mit `Is(h)` einer konkreten Klasse. |

**Methoden**

*Allgemein*

| Methode | Beschreibung |
|---|---|
| `GetParametricName() -> str \| None` | Universeller (parametrischer) Name dieses Objekts: "Data Tag" oder "Title Block Border". Leer, wenn das Objekt ungültig ist oder der zugrunde liegende Handle nicht auf ein Plug-in-Objekt verweist. |
| `HasParam(univParamName: str) -> bool` | Ob dieses Plug-in-Objekt ein Feld mit dem angegebenen universellen Namen hat. |
| `GetParamNames() -> list[str]` | Geordnete Liste aller vom Plug-in dieses Objekts definierten universellen Parameternamen. |
| `GetParamString(univParamName: str) -> str \| None` | Allgemeine Feldzugriffsmethoden mit Zeichenfolgen als Schlüsseln. Bevorzugen Sie die typisierten, benannten Zugriffsmethoden der Unterklassen, sofern vorhanden; verwenden Sie diese Methoden für Parameter ohne eigene Zugriffsmethode. Die Abfragemethoden geben `None` zurück, wenn der Parameter nicht vorhanden ist; die Änderungsmethoden geben `False` zurück. |
| `SetParamString(univParamName: str, value: str) -> bool` | Legt den Parameterwert als Zeichenfolge fest. Allgemeine Feldzugriffsmethoden mit Zeichenfolgen als Schlüsseln. Bevorzugen Sie die typisierten, benannten Zugriffsmethoden der Unterklassen, sofern vorhanden; verwenden Sie diese Methoden für Parameter ohne eigene Zugriffsmethode. Die Abfragemethoden geben `None` zurück, wenn der Parameter nicht vorhanden ist; die Änderungsmethoden geben `False` zurück. |
| `GetParamReal(univParamName: str) -> float \| None` | Gibt den Parameterwert vom Typ real für `univParamName` zurück. |
| `SetParamReal(univParamName: str, value: float) -> bool` | Setzt den Parameterwert vom Typ real. |
| `GetParamBool(univParamName: str) -> bool \| None` | Ob *Boolescher Parameter* für `univParamName` aktiviert ist. |
| `SetParamBool(univParamName: str, value: bool) -> bool` | Setzt den booleschen Parameterwert. |
| `GetParamInt(univParamName: str) -> int \| None` | Gibt den ganzzahligen Parameterwert für `univParamName` zurück. |
| `SetParamInt(univParamName: str, value: int) -> bool` | Setzt den ganzzahligen Parameterwert. |

*Objektstil (Stil für Intelligente Objekte)*

| Methode | Beschreibung |
|---|---|
| `GetStyleHandle() -> Handle` | Symboldefinition des dem Objekt zugeordneten Stils; ein Null-Handle, wenn das Objekt keinen Stil hat. |
| `GetStyleName() -> str \| None` | Name dieses Stils; `None`, wenn das Objekt keinen Stil hat oder ungültig ist. |
| `IsStyled() -> bool` | Gibt True zurück, wenn das Objekt einen Objektstil verwendet. |
| `SetStyle(styleName: str) -> bool` | Ordnet dem Objekt den Stil mit dem Namen `styleName` aus der aktuellen Zeichnung zu und übernimmt dessen stilgesteuerte Parameterwerte. Schlägt fehl, wenn kein solches Zubehör vorhanden ist oder es kein Objektstil ist. Die Unterklassen ergänzen eine statische Ensure*`Style()`-Methode, die den Stil zuvor aus den Vectorworks-Bibliotheken importiert. |
| `SetStyle(hStyleSymbolDefinition: Handle) -> bool` | Ordnet dem Objekt den Stil mit dem Namen `styleName` aus der aktuellen Zeichnung zu und übernimmt dessen stilgesteuerte Parameterwerte. Schlägt fehl, wenn kein solches Zubehör vorhanden ist oder es kein Objektstil ist. Die Unterklassen ergänzen eine statische Ensure*`Style()`-Methode, die den Stil zuvor aus den Vectorworks-Bibliotheken importiert. |
| `RemoveStyle() -> bool` | Löst die Verknüpfung des Objekts mit seinem Stil; jeder Parameter wird auf „nach Instanz“ umgestellt und behält seinen aktuellen Wert. |

Geerbt: alle Elemente von [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

### DataTagObject

> **Vollständiger Name:** `api.DataTagObject` · **Erbt von:** [`AnnotationObject`](#annotationobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Plug-in-Objekt Datenstempel (universeller Name "Data Tag").

Ein Datenstempel beschriftet ein anderes Objekt mit Daten, die aus diesem Objekt gelesen werden: Datenbankfelder, Plug-in-Parameter, Klasse, Attribute, Tabellenformeln, ... Die Textanordnung des Stempels – welche Felder er zeigt, in welcher Anordnung und innerhalb welcher Umrandung – ist vollständig im STIL des Stempels enthalten, einer Symboldefinition eines Objektstils. Ein Datenstempel ohne Stil zeigt daher überhaupt nichts an. Deshalb ermittelt `Create()` immer einen Stil (und importiert einen aus den Vectorworks-Bibliotheken, wenn die Zeichnung keinen enthält) und schlägt fehl, wenn nirgends ein Datenstempelstil verfügbar ist.

Der zweite Bestandteil eines nutzbaren Stempels ist die Verknüpfung mit dem beschriebenen Objekt: Der Stempel liest seine Daten aus dem zugeordneten Objekt und folgt ihm beim Verschieben. `Create()` nimmt das zu beschriftende Objekt entgegen; AttachTo / DetachFrom ändern die Zuordnung später.

Häufig verwendete Parameter mit benannten Zugriffsmethoden:

- "Use Leader" — legt fest, ob der Stempel eine Verweislinie zum beschrifteten Objekt zeichnet
- "Leader Type" — Form der Verweislinie (siehe `DataTagObject.LeaderType` unten)
- "Leader Length" — Länge der Verweislinie in Welteinheiten
- "Leader Angle" — Winkel der Verweislinie (die Zugriffsmethoden verwenden Bogenmaß, der direkte Parameter Grad)
- "Shoulder Length" — Länge der horizontalen Ansatzlinie zwischen Verweislinie und Text
- "Horizontal Position" — Seite der Verweislinie, auf der sich der Text befindet (siehe `DataTagObject.HorizontalPosition`)
- "Move Behaviour" — legt fest, was beim Ziehen des Stempels verschoben wird (siehe `DataTagObject.MoveBehaviour`)
- "X Offset"/"Y Offset" — Versatz des Stempels vom beschrifteten Objekt in Welteinheiten

Vollständige Parameterreferenz für GetParam.../SetParam... (Parametername | Typ | Hinweise/Auswahlwerte): Verweis- und Ansatzlinie

- "Use Leader" — bool
- "Leader Type" — Auswahlliste — Line / Arc / Bezier
- "Leader Length" — reell — Welteinheiten
- "Leader Angle" — reell — Grad
- "Leader Radius" — reell — Welteinheiten (bogenförmige Verweislinie)
- "Shoulder Length" — reell — Welteinheiten
- "Use Marker" — bool — zeichnet ein Linienendzeichen am Ende der Verweislinie
- "Clip Leader" — bool
- "Leader/Shoulder Class" — Zeichenfolge — Klasse der Geometrie von Verweis- und Ansatzlinie
- "__Marker", "__Marker Style", "__Marker Angle", "__Marker Size", "__Marker Width", "__Marker Thickness Basis", "__Marker Thickness" — Definition des Linienendzeichens (intern)
- "__Bezier Length Factor 1/2", "__Bezier Offset1/2" — Form der Bézier-Verweislinie (intern)
- "__LeaderEndX", "__LeaderEndY" — reell — lokale Verweislinienkoordinaten ohne Objektverknüpfung (Get/SetLeaderEnd verwenden)

Platzierung

- "Horizontal Position" — Auswahlliste — Left / Right / Auto
- "Move Behaviour" — Auswahlliste — Entire Tag / Leader End
- "Offset Mode" — Auswahlliste — Global / Local
- "X Offset", "Y Offset" — reell — Welteinheiten
- "Align to Walls" — bool
- "Wall Alignment" — Auswahlliste — Unconstrained / Center Line / Left Edge / Right Edge
- "World-based" — bool — hält den Stempel am Weltkoordinatensystem statt an der Ansicht ausgerichtet
- "MirrorElements" — bool
- "Allow Mult Att Points" — bool
- "__RefOffsetX/Y/Z", "__RefCenterX/Y/Z", "__MoveOffsetX/Y/Z" — reell (interner Platzierungszustand)
- "__RefWallOffset", "__IsRefWallLeftSide", "__RefOffsetFromWall", "__RefWallCenterOffse", "__IsRefWallCenterLeftSide", "__RefCenterOffsetFromWall" — (intern)

Skalierung

- "Scaling" — Auswahlliste — None / Symmetric / Asymmetric
- "Scale Text" — bool
- "X Scale", "Y Scale" — reell

Eignung (Objekte, denen dieser Stempel zugeordnet werden darf)

- "UseCriteriaEligibility" — bool
- "__CriteriaEligibility" — Zeichenfolge — Vectorworks-Kriterien, z. B. "((ALL))"
- "SubpartMode" — bool — beschriftet Teilobjekte statt des gesamten Objekts
- "EnableOverlappingVerticalChains" — bool

Dialoge / interner Zustand

- "Always Display ETD Dialog" — bool
- "__Edit Tag Layout" — Zeichenfolge — statischer Textplatzhalter in der Infopalette
- "__Was Moved", "__Is For Updating", "__Is For Moving", "__Was Rotated From OIP" — bool
- "__IsCompensateAngleUsed", "__IsBubbleFlipped" — bool
- "__Version" — int

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `DataTagObject(h: Handle)` | Verweist auf den vorhandenen Datenstempel `h`; vor der Verwendung `IsValid()` prüfen. |

**Methoden**

*Allgemein*

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | True, wenn `h` auf ein Objekt des von dieser Klasse dargestellten Typs verweist. |
| `Create(position: Math.Point2D, styleName: str = '', hObjectToTag: Handle = None) -> DataTagObject` *statisch* | Erstellt bei `position` einen Datenstempel, der `hObjectToTag` beschriftet (für einen freistehenden Stempel ist ein Null-Handle zulässig). `styleName` wählt den Datenstempelstil: Er wird zunächst in der Zeichnung gesucht und aus den Vectorworks-Datenstempelbibliotheken importiert, wenn er dort noch nicht vorhanden ist. Leer lassen, um einen beliebigen verfügbaren Stil zu verwenden. Gibt ein ungültiges Objekt zurück, wenn überhaupt kein Datenstempelstil gefunden werden kann – ein Stempel ohne Stil hat keine Textanordnung und wäre unsichtbar. |
| `EnsureStyle(styleName: str = '') -> str` *statisch* | Stellt sicher, dass in der aktuellen Zeichnung ein Datenstempelstil mit dem Namen `styleName` vorhanden ist, und importiert ihn bei Bedarf aus den Vectorworks-Bibliotheken. Gibt den Namen des nun verfügbaren Stils zurück (der vom angeforderten Namen abweichen kann, falls dieser Stil nicht vorhanden ist) oder eine leere Zeichenfolge, wenn kein Stil verfügbar ist. |
| `Duplicate() -> DataTagObject` | Dupliziert den Datenstempel in der Zeichnung und gibt die Kopie zurück. |

*Verknüpfung*

| Methode | Beschreibung |
|---|---|
| `GetTaggedObject() -> Handle` | Das Objekt, aus dem dieser Datenstempel seine Daten liest; null bei einem Datenstempel ohne Verknüpfung. |
| `AttachTo(hObject: Handle) -> bool` | Ordnet den Stempel `hObject` zu (ersetzt die aktuelle Verknüpfung) und aktualisiert den Stempeltext. |
| `DetachFrom(hObject: Handle = None) -> bool` | Löst die Verknüpfung des Stempels mit `hObject`. Übergeben Sie einen Null-Handle, um die Verknüpfung mit dem aktuell beschrifteten Objekt zu lösen. |
| `CanBeTagged(hObject: Handle) -> bool` *statisch* | Gibt an, ob `hObject` eine Objektart ist, der ein Datenstempel zugeordnet werden darf. |
| `GetTagsOfObject(hObject: Handle) -> list[Handle]` *statisch* | Alle `hObject` zugeordneten Datenstempel. |

*Inhalt*

| Methode | Beschreibung |
|---|---|
| `GetExtractedData() -> list[tuple[str, str]]` | Die aktuell vom Stempel angezeigten Daten als Paare aus Bezeichnung und Wert. Die Bezeichnung ist die in der Stempelanordnung definierte Feldbezeichnung; der Wert ist der Text, den der Stempel tatsächlich für das beschriftete Objekt ausgibt. |
| `Update() -> bool` | Liest die Daten erneut aus dem beschrifteten Objekt und zeichnet den Datenstempel neu. |

*Verweislinie*

| Methode | Beschreibung |
|---|---|
| `GetUseLeader() -> bool \| None` | Gibt an, ob *Verweislinie verwenden* eingeschaltet ist. |
| `SetUseLeader(value: bool) -> bool` | Schaltet *Verweislinie verwenden* ein oder aus. |
| `GetLeaderType() -> DataTagObject.LeaderType \| None` | Gibt den Verweislinientyp zurück. |
| `SetLeaderType(value: DataTagObject.LeaderType) -> bool` | Legt den Verweislinientyp fest. |
| `GetLeaderLength() -> float \| None` | Gibt die Verweislinienlänge zurück (Welteinheiten). |
| `SetLeaderLength(value: float) -> bool` | Legt die Verweislinienlänge fest. |
| `GetLeaderAngle() -> float \| None` | Gibt den Verweislinienwinkel zurück (im Bogenmaß). |
| `SetLeaderAngle(radians: float) -> bool` | Legt den Verweislinienwinkel fest. |
| `GetShoulderLength() -> float \| None` | Gibt die Länge der Ansatzlinie zurück (Welteinheiten). |
| `SetShoulderLength(value: float) -> bool` | Legt die Länge der Ansatzlinie fest. |
| `GetUseMarker() -> bool \| None` | Gibt an, ob *Linienendzeichen verwenden* eingeschaltet ist. |
| `SetUseMarker(value: bool) -> bool` | Schaltet *Linienendzeichen verwenden* ein oder aus. |
| `GetLeaderEnd() -> Math.Point2D \| None` | Spitze der Verweislinie in Welteinheiten. Das Festlegen verschiebt das Verweislinienende, ohne den Stempeltext zu verschieben. Globale bzw. Modell-XY-Koordinaten für verknüpfte und nicht verknüpfte Stempel. Die Abfrage setzt eine eingeschaltete Verweislinie und die Vectorworks-eigene Unterstützung für Verweislinien voraus; bei geneigten umschließenden Plug-in-Objekten leer (nur XY wird unterstützt). |
| `SetLeaderEnd(position: Math.Point2D) -> bool` | Legt das Verweislinienende fest. Spitze der Verweislinie in Welteinheiten. Das Festlegen verschiebt das Verweislinienende, ohne den Stempeltext zu verschieben. Globale bzw. Modell-XY-Koordinaten für verknüpfte und nicht verknüpfte Stempel. Die Abfrage setzt eine eingeschaltete Verweislinie und die Vectorworks-eigene Unterstützung für Verweislinien voraus; bei geneigten umschließenden Plug-in-Objekten leer (nur XY wird unterstützt). |

*Platzierung*

| Methode | Beschreibung |
|---|---|
| `GetHorizontalPosition() -> DataTagObject.HorizontalPosition \| None` | Gibt die horizontale Position zurück. |
| `SetHorizontalPosition(value: DataTagObject.HorizontalPosition) -> bool` | Legt die horizontale Position fest. |
| `GetMoveBehaviour() -> DataTagObject.MoveBehaviour \| None` | Gibt das Verschiebeverhalten zurück. |
| `SetMoveBehaviour(value: DataTagObject.MoveBehaviour) -> bool` | Legt das Verschiebeverhalten fest. |
| `GetOffset() -> Math.Point2D \| None` | Versatz des Datenstempels vom Objekt, das er beschriftet, in Welteinheiten. |
| `SetOffset(offset: Math.Point2D) -> bool` | Legt den Versatz fest. Versatz des Stempels vom beschrifteten Objekt in Welteinheiten. |
| `GetAlignToWalls() -> bool \| None` | Gibt an, ob *An Wänden ausrichten* eingeschaltet ist. |
| `SetAlignToWalls(value: bool) -> bool` | Schaltet *An Wänden ausrichten* ein oder aus. |

*Eignung*

| Methode | Beschreibung |
|---|---|
| `GetUseCriteriaEligibility() -> bool \| None` | Gibt an, ob der Stempel die zuordenbaren Objekte anhand einer Kriterienzeichenfolge einschränkt. |
| `SetUseCriteriaEligibility(value: bool) -> bool` | Schaltet *Eignungskriterien verwenden* ein oder aus. Gibt an, ob der Stempel die zuordenbaren Objekte anhand einer Kriterienzeichenfolge einschränkt. |
| `GetEligibilityCriteria() -> str \| None` | Die bei eingeschalteter Einschränkung verwendete Vectorworks-Kriterienzeichenfolge, z. B. "((ALL))" oder "((PON=`Door`))". |
| `SetEligibilityCriteria(criteria: str) -> bool` | Legt die Eignungskriterien fest. Die bei eingeschalteter Einschränkung verwendete Vectorworks-Kriterienzeichenfolge, z. B. "((ALL))" oder "((PON=`Door`))". |

Geerbt: alle Elemente von [`AnnotationObject`](#annotationobject), [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

#### DataTagObject.LeaderType

> **Vollständiger Name:** `api.DataTagObject.LeaderType` · **Art:** `IntEnum`

Form der Verweislinie eines Datenstempels („Verweislinientyp“).

| Element | Wert | Beschreibung |
|---|---|---|
| `Line` | `0` |  |
| `Arc` | `1` |  |
| `Bezier` | `2` |  |

#### DataTagObject.HorizontalPosition

> **Vollständiger Name:** `api.DataTagObject.HorizontalPosition` · **Art:** `IntEnum`

Seite der Verweislinie, auf der sich der Stempeltext befindet („Horizontale Position“).

| Element | Wert | Beschreibung |
|---|---|---|
| `Left` | `0` |  |
| `Right` | `1` |  |
| `Auto` | `2` |  |

#### DataTagObject.MoveBehaviour

> **Vollständiger Name:** `api.DataTagObject.MoveBehaviour` · **Art:** `IntEnum`

Was beim Ziehen des Stempels in der Zeichnung verschoben wird: der gesamte Stempel oder nur die Spitze seiner Verweislinie.

| Element | Wert | Beschreibung |
|---|---|---|
| `EntireTag` | `0` |  |
| `LeaderEnd` | `1` |  |

### TitleBlockBorderObject

> **Vollständiger Name:** `api.TitleBlockBorderObject` · **Erbt von:** [`AnnotationObject`](#annotationobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Plug-in-Objekt Plankopf (universeller Name "Title Block Border").

Ein Plankopfobjekt bildet den Rahmen eines Plans: den Planrahmen mit Rändern und Rastereinteilung sowie den eigentlichen Plankopf – den Textblock in der Ecke, der Projektname, Auftraggeber, Plannummer, Maßstab, Ausgabe- und Revisionshistorie usw. ausgibt. Es wird normalerweise auf einer Layoutebene platziert, eines pro Plan.

Wie beim Datenstempel ist die grafische Darstellung in einem STIL enthalten (einer Symboldefinition eines Objektstils): Der Stil bestimmt das Aussehen des Plankopfs und die ausgegebenen Felder. Ein Plankopfobjekt ohne Stil zeichnet nur einen leeren Rahmen. Deshalb ermittelt `Create()` einen Stil – und importiert einen aus den Vectorworks-Plankopfbibliotheken, wenn die Zeichnung keinen enthält – und schlägt fehl, wenn kein Stil verfügbar ist.

Die von einem Plankopf ausgegebenen Daten stammen aus drei Quellen:

- den eigenen Parametern des Objekts (Plangröße, Ränder, Rastereinteilung, Nordpfeil, Stempeltext, ...), zugänglich über die unten aufgeführten typisierten Zugriffsmethoden und über Get/SetParam...;
- den PLANDATEN, einem Satz benannter Felder, die pro Plankopfobjekt gespeichert werden (Plantitel, Plannummer, gezeichnet von, geprüft von, ...) – siehe GetSheetData / SetSheetData;
- den PROJEKTDATEN, einem Satz benannter Felder, die einmal pro Dokument gespeichert und von allen Planköpfen gemeinsam genutzt werden (Projektname, Auftraggeber, Adresse, ...) – siehe die statischen Methoden GetProjectData / SetProjectData.

Revisionen und Ausgaben werden mit GetRevisions / GetIssueDates gelesen.

Vollständige Parameterreferenz für GetParam.../SetParam... (Parametername | Typ | Hinweise/Auswahlwerte): Plan

- "Sheet Size ID" — int — Index der vordefinierten Plangröße, -1 für eine benutzerdefinierte Größe
- "Sheet Size Name" — Zeichenfolge — z. B. "ANSI D", "ISO A1"
- "Sheet Width", "Sheet Height" — reell — Welteinheiten (benutzerdefinierte Größen)
- "Sheet Orientation" — Auswahlliste — portrait / landscape
- "Sheet Fit Method" — Auswahlliste — legt fest, wie der Rahmen an die Seite angepasst wird
- "Lock To Page Center" — bool
- "Sheet Margin Left/Right/Top/Bottom" — reell — Welteinheiten
- "Sheet Hide Border" — bool
- "Border Use Object Line Weight" — bool
- "Border Line Weight" — reell
- "Sheet Fill Border" — bool
- "Display Format" — Auswahlliste
- "Units" — Auswahlliste — Einheiten, in denen die Plangröße angegeben wird
- "Show unit mark" — bool
- "Use custom name" — bool

Rastereinteilung (das entlang des Rahmens ausgegebene Raster A/B/C - 1/2/3): "Show Grids", "Show Grid Lines", "Show Grid Lines Extensions" — bool

- "Vertical Zones", "Horizontal Zones" — int
- "Grid Text Order", "Grid Number Order" — Auswahlliste
- "Grid Label Size" — reell
- "Grid Marker Line Length" — reell
- "Draw Crop Marks" — bool
- "Crop Marks Line Weight" — reell
- "Fold Mark" — Auswahlliste
- "Fold Mark Class" — Zeichenfolge
- "Margin Width", "Folded Width", "Folded Height" — reell
- "Zoom In to Title Block" — bool
- "Graphics Scale" — reell
- "__Version" — int

Plankopf

- "Use As Title Block" — bool — zeichnet den Plankopf, nicht nur den Rahmen
- "Title Block Position" — Auswahlliste — Planecke, in der sich der Plankopf befindet
- "Title Block Margin" — reell
- "Scale Factor" — reell
- "Use Layout Text Attributes" — bool
- "Countersignature" — bool
- "This Title Block Is Active" — bool — der Plankopf, der die Plandaten des Dokuments bereitstellt
- "Use Auto Drawing Coordination" — bool

Plan- / Revisions- / Ausgabedaten

- "Plot Date Format" — Auswahlliste
- "Scale" — Zeichenfolge
- "Date" — Zeichenfolge
- "Current Revision Number" — Zeichenfolge
- "Show Revisions Count" — int — Anzahl der auszugebenden Revisionszeilen
- "Revision Line Spacing" — reell
- "Revision Direction" — Auswahlliste — up / down
- "Current Issue Number" — Zeichenfolge
- "Show Issues Count" — int
- "Issue Line Spacing" — reell
- "Issue Direction" — Auswahlliste
- "Issue Increment", "Revision Increment" — int
- "Issue Mark", "Revision Mark" — Zeichenfolge

Nordpfeil

- "Display North Arrow" — bool
- "North Arrow Symbol" — Zeichenfolge — Name der Symboldefinition
- "North Angle" — reell — GRAD (GetNorthAngle/SetNorthAngle verwenden Bogenmaß)
- "North Scale Factor" — reell
- "Selected Heliodon City", "Selected Heliodon Country" — Zeichenfolge
- "Use Heliodon Rotation Angle" — bool
- "Show MN Declination" — bool
- "Declination Degree Offset" — reell — Grad
- "North Default Position X", "North Default Position Y" — reell — Welteinheiten

Stempeltext (der überlagerte Hinweis „VORLÄUFIG - NICHT ZUR BAUAUSFÜHRUNG“)

- "Display Drawing Stamp" — bool
- "Stamp Text" — Auswahlliste — vordefinierter Stempeltext
- "Custom Text" — Zeichenfolge — wird verwendet, wenn "Stamp Text" den benutzerdefinierten Eintrag auswählt
- "Stamp Text Style" — Zeichenfolge
- "Stamp Text Size" — reell
- "Stamp Text Size Unit" — Auswahlliste
- "Use ALL CAPS" — bool
- "Append Date" — bool
- "Stamp Date" — Zeichenfolge
- "Stamp Angle" — reell — Grad
- "Stamp Default Position X", "Stamp Default Position Y" — reell — Welteinheiten

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `TitleBlockBorderObject(h: Handle)` | Verweist auf das vorhandene Plankopfobjekt `h`; vor der Verwendung `IsValid()` prüfen. |

**Methoden**

*Allgemein*

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | True, wenn `h` auf ein Objekt des von dieser Klasse dargestellten Typs verweist. |
| `Create(position: Math.Point2D, styleName: str = '') -> TitleBlockBorderObject` *statisch* | Erstellt ein Plankopfobjekt mit seinem unteren linken Eckbereich bei `position`. `styleName` wählt den Plankopf-Stil: Er wird zunächst in der Zeichnung gesucht und aus den Vectorworks-Plankopfbibliotheken importiert, wenn er dort noch nicht vorhanden ist. Leer lassen, um einen beliebigen verfügbaren Stil zu verwenden. Gibt ein ungültiges Objekt zurück, wenn kein Plankopf-Stil gefunden werden kann – ein Plankopf ohne Stil hat keine Plankopfgrafik. |
| `EnsureStyle(styleName: str = '') -> str` *statisch* | Stellt sicher, dass in der aktuellen Zeichnung ein Plankopf-Stil mit dem Namen `styleName` vorhanden ist, und importiert ihn bei Bedarf aus den Vectorworks-Bibliotheken. Gibt den Namen des nun verfügbaren Stils zurück (der vom angeforderten Namen abweichen kann, falls dieser Stil nicht vorhanden ist); leer, wenn kein Stil verfügbar ist. |
| `Duplicate() -> TitleBlockBorderObject` | Dupliziert das Plankopfobjekt in der Zeichnung und gibt die Kopie zurück. |

*Plan*

| Methode | Beschreibung |
|---|---|
| `GetSheetSizeName() -> str \| None` | Name des vordefinierten Papierformats, z. B. "ANSI D" oder "ISO A1". |
| `SetSheetSizeName(name: str) -> bool` | Legt den Namen der Plangröße fest. Name der vordefinierten Plangröße, z. B. "ANSI D" oder "ISO A1". |
| `GetSheetWidth() -> float \| None` | Benutzerdefinierte Plangröße in Welteinheiten. Nur relevant, wenn das Objekt eine benutzerdefinierte Größe verwendet. |
| `SetSheetWidth(value: float) -> bool` | Legt die Planbreite fest. Benutzerdefinierte Plangröße in Welteinheiten. Nur relevant, wenn das Objekt eine benutzerdefinierte Größe verwendet. |
| `GetSheetHeight() -> float \| None` | Gibt die Planhöhe zurück. |
| `SetSheetHeight(value: float) -> bool` | Legt die Planhöhe fest. |
| `GetMarginLeft() -> float \| None` | Layoutränder, in Welteinheiten. |
| `GetMarginRight() -> float \| None` | Gibt den rechten Rand zurück. |
| `GetMarginTop() -> float \| None` | Gibt den oberen Rand zurück. |
| `GetMarginBottom() -> float \| None` | Gibt den unteren Rand zurück. |
| `SetMargins(left: float, right: float, top: float, bottom: float) -> bool` | Legt die Ränder fest. |

*Rastereinteilung*

| Methode | Beschreibung |
|---|---|
| `GetShowGrids() -> bool \| None` | Gibt an, ob *Raster anzeigen* eingeschaltet ist. |
| `SetShowGrids(value: bool) -> bool` | Schaltet *Raster anzeigen* ein oder aus. |
| `GetHorizontalZones() -> int \| None` | Gibt die horizontalen Zonen zurück. |
| `SetHorizontalZones(count: int) -> bool` | Legt die horizontalen Zonen fest. |
| `GetVerticalZones() -> int \| None` | Gibt die vertikalen Zonen zurück. |
| `SetVerticalZones(count: int) -> bool` | Legt die vertikalen Zonen fest. |
| `GetDrawCropMarks() -> bool \| None` | Gibt an, ob *Schnittmarken zeichnen* eingeschaltet ist. |
| `SetDrawCropMarks(value: bool) -> bool` | Schaltet *Schnittmarken zeichnen* ein oder aus. |

*Plankopf*

| Methode | Beschreibung |
|---|---|
| `GetUseAsTitleBlock() -> bool \| None` | Gibt an, ob das Objekt den Plankopf oder nur den Planrahmen zeichnet. |
| `SetUseAsTitleBlock(value: bool) -> bool` | Schaltet *Als Plankopf verwenden* ein oder aus. Gibt an, ob das Objekt den Plankopf oder nur den Planrahmen zeichnet. |
| `GetIsActiveTitleBlock() -> bool \| None` | Gibt an, ob dies der Plankopf ist, dessen Plandaten das Dokument liest (einer pro Plan). |
| `SetIsActiveTitleBlock(value: bool) -> bool` | Schaltet *Aktiver Plankopf* ein oder aus. Gibt an, ob dies der Plankopf ist, dessen Plandaten das Dokument liest (einer pro Plan). |

*Nordpfeil*

| Methode | Beschreibung |
|---|---|
| `GetDisplayNorthArrow() -> bool \| None` | Gibt an, ob *Nordpfeil anzeigen* eingeschaltet ist. |
| `SetDisplayNorthArrow(value: bool) -> bool` | Schaltet *Nordpfeil anzeigen* ein oder aus. |
| `GetNorthAngle() -> float \| None` | Gibt den Nordwinkel zurück (im Bogenmaß). |
| `SetNorthAngle(radians: float) -> bool` | Legt den Nordwinkel fest. |

*Stempeltext*

| Methode | Beschreibung |
|---|---|
| `GetDisplayDrawingStamp() -> bool \| None` | Gibt an, ob *Stempeltext anzeigen* eingeschaltet ist. |
| `SetDisplayDrawingStamp(value: bool) -> bool` | Schaltet *Stempeltext anzeigen* ein oder aus. |
| `GetDrawingStampText() -> str \| None` | Vom Stempel ausgegebener freier Text; wird verwendet, wenn für den Stempeltext der benutzerdefinierte Eintrag gewählt ist. |
| `SetDrawingStampText(text: str) -> bool` | Legt den Stempeltext fest. Vom Stempel ausgegebener freier Text; wird verwendet, wenn für den Stempeltext der benutzerdefinierte Eintrag gewählt ist. |

*Plandaten*

| Methode | Beschreibung |
|---|---|
| `GetSheetDataFieldNames() -> list[str]` | Gibt die Feldnamen der Plandaten zurück. |
| `GetSheetData(fieldName: str) -> str \| None` | Gibt die Plandaten für `fieldName` zurück. |
| `SetSheetData(fieldName: str, value: str) -> bool` | Legt die Plandaten fest. |
| `GetAllSheetData() -> list[tuple[str, str]]` | Alle Plandatenfelder dieses Plankopfs als Paare (Feldname, Wert). |

*Projektdaten*

| Methode | Beschreibung |
|---|---|
| `GetProjectDataFieldNames() -> list[str]` *statisch* | Gibt die Feldnamen der Projektdaten zurück. |
| `GetProjectData(fieldName: str) -> str \| None` *statisch* | Gibt die Projektdaten für `fieldName` zurück. |
| `SetProjectData(fieldName: str, value: str) -> bool` *statisch* | Legt die Projektdaten fest. |
| `GetAllProjectData() -> list[tuple[str, str]]` *statisch* | Gibt alle Projektdaten zurück. |

*Revisionen und Ausgaben*

| Methode | Beschreibung |
|---|---|
| `GetRevisions() -> list[TitleBlockBorderObject.Revision]` | Die von diesem Plankopf ausgegebene Änderungshistorie, älteste Einträge zuerst. |
| `GetSheetID() -> str \| None` | Plankennung, wie sie der Plankopf derzeit ausgibt. |
| `GetSheetTitle() -> str \| None` | Gibt den Plantitel zurück. |
| `GetSheetDate() -> str \| None` | Gibt das Plandatum zurück. |
| `GetLatestIssueDate() -> str \| None` | Datum der letzten Ausgabe dieses Plankopfs; leer, wenn er noch nie ausgegeben wurde. |
| `UpdateData(updateAutomaticData: bool = True) -> bool` *statisch* | Liest die Dokumentdaten erneut in jeden Plankopf der Zeichnung ein und zeichnet die Planköpfe neu. `updateAutomaticData` aktualisiert auch die von Vectorworks selbst verwalteten Werte (Dateiname, Seitenzahlen, Plananzahl, Plotdatum, ...). |

Geerbt: alle Elemente von [`AnnotationObject`](#annotationobject), [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

#### TitleBlockBorderObject.Revision

> **Vollständiger Name:** `api.TitleBlockBorderObject.Revision` · **Erbt von:** `api.Object`

Eine Revision eines Plankopfs: Nummer, Datum, Anmerkung, Veröffentlichungsdatum und Empfänger.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `Revision()` | Standardwert (Felder mit ihren Standardwerten). |
| `Revision(fNumber, fDate, fNote, fPublishDate, fRecipients)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `fNumber` | `str` | Revisionsnummer. |
| `fDate` | `str` | Revisionsdatum. |
| `fNote` | `str` | Revisionsanmerkung. |
| `fPublishDate` | `str` | Veröffentlichungsdatum. |
| `fRecipients` | `str` | Empfänger. |

### DimensionObject

> **Vollständiger Name:** `api.DimensionObject` · **Erbt von:** [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Basisklasse jedes Bemaßungsobjekts (`ObjectType.Dimension`).

Eine Bemaßung ist ein VECTORWORKS-EIGENES Objekt, kein Plug-in-Objekt: Sie hat weder eine Parameterdatenbank noch einen Objektstil. Alle Angaben – die Messpunkte, der ausgegebene Text und ob Maßhilfslinien gezeichnet werden – sind in Objektvariablen gespeichert, die diese Klasse über benannte Zugriffsmethoden zugänglich macht.

Die Darstellung einer Bemaßung beruht auf drei Quellen:

1. ihrer eigenen Geometrie (den Messpunkten und dem Abstand der Maßlinie zu ihnen),
2. dem referenzierten BEMASSUNGSSTANDARD (GetStandardName): Pfeilart und -größe, Abstand und Überstand der Maßhilfslinien, Textplatzierung, ...; alle Längen sind auf die Seite bezogen und berücksichtigen daher den Maßstab,
3. den EINHEITENEINSTELLUNGEN: standardmäßig den primären/sekundären Dokumenteinheiten oder einer benannten Bemaßungseinheiteneinstellung, falls eine zugewiesen ist (GetUnitSetting).

Eine Änderung des Standards oder der Einheiten einer Bemaßung ändert niemals die gemessene Größe, sondern nur deren Darstellung.

Der von einer Bemaßung ausgegebene Text besteht aus dem Messwert (GetShowValue) mit optionalem Präfix- und Suffixtext. Das Ausblenden des Werts und Festlegen eines Präfixtexts macht die Bemaßung zu einer einfachen Beschriftung. Die „sekundären“ Zugriffsmethoden bieten dieselben Einstellungen für die zweite (duale) Einheitenanzeige.

Bemaßungen können ASSOZIATIV sein: Wenn `Associate()` erfolgreich ist, misst die Bemaßung weiterhin das Objekt, an dem sie ausgerichtet wurde, und aktualisiert sich, wenn sich dieses Objekt ändert. Assoziativität ist sowohl eine Eigenschaft des Dokuments (Einstellung „Bemaßungen assoziativ“) als auch des Objekts.

Alle Winkel in dieser API werden im Bogenmaß angegeben, alle Längen in Welteinheiten.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `DimensionObject(h: Handle)` | Verweist auf die vorhandene Bemaßung `h`; vor der Verwendung `IsValid()` prüfen. |

**Methoden**

*Allgemein*

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | Gibt True zurück, wenn `h` auf ein Objekt der von dieser Klasse dargestellten Art verweist (ein beliebiges Bemaßungsobjekt). |
| `KindOf(h: Handle) -> DimensionKind` *statisch* | Art der Bemaßung oder Unknown, wenn `h` keine Bemaßung ist. |
| `Duplicate() -> DimensionObject` | Dupliziert die Bemaßung in der Zeichnung und gibt die Kopie zurück. |

*Identität*

| Methode | Beschreibung |
|---|---|
| `GetKind() -> DimensionKind \| None` | Gibt die Art zurück. |
| `GetKindName() -> str \| None` | Gibt den Namen der Bemaßungsart zurück. |
| `GetKindName(kind: DimensionKind) -> str` *statisch* | Gibt den Namen der Bemaßungsart für `kind` zurück. |

*Gemessene Geometrie*

| Methode | Beschreibung |
|---|---|
| `GetStartPoint() -> Math.Point2D \| None` | Die beiden Punkte, zwischen denen die Bemaßung misst. Bei Winkelbemaßungen sind dies die beiden Schenkelpunkte; der Scheitelpunkt wird separat gespeichert (siehe AngularDimensionObject). Bei Kreis- und Bogenbemaßungen sind es Punkte auf dem Kreis bzw. Kreisbogen. |
| `SetStartPoint(pt: Math.Point2D) -> bool` | Legt den Anfangspunkt fest. Die beiden Punkte, zwischen denen die Bemaßung misst. Bei Winkelbemaßungen sind dies die beiden Schenkelpunkte; der Scheitelpunkt wird separat gespeichert (siehe AngularDimensionObject). Bei Kreis- und Bogenbemaßungen sind es Punkte auf dem Kreis bzw. Kreisbogen. |
| `GetEndPoint() -> Math.Point2D \| None` | Gibt den Endpunkt zurück. |
| `SetEndPoint(pt: Math.Point2D) -> bool` | Legt den Endpunkt fest. |
| `SetPoints(start: Math.Point2D, end: Math.Point2D) -> bool` | Legt die Punkte fest. |
| `GetOffset() -> float \| None` | Abstand zwischen den Messpunkten und der Maßlinie selbst. Positive Versätze platzieren die Maßlinie links von der Richtung Anfang -> Ende, negative rechts davon. |
| `SetOffset(offset: float) -> bool` | Legt den Versatz fest. Abstand zwischen den Messpunkten und der Maßlinie selbst. Positive Versätze platzieren die Maßlinie links von der Richtung Anfang -> Ende, negative rechts davon. |
| `GetMeasuredLength() -> float \| None` | Gerader Abstand zwischen den beiden Messpunkten in Welteinheiten. Dies ist die von einer freien linearen Bemaßung ausgegebene Länge; winkelgebundene Bemaßungen geben die Projektion dieses Abstands auf ihre feste Richtung aus. |

*Maßhilfslinien (Verlängerungslinien)*

| Methode | Beschreibung |
|---|---|
| `GetStartWitness() -> bool \| None` | Gibt an, ob *Anfangsmaßhilfslinie* eingeschaltet ist. |
| `SetStartWitness(show: bool) -> bool` | Schaltet *Anfangsmaßhilfslinie* ein oder aus. |
| `GetEndWitness() -> bool \| None` | Gibt an, ob *Endmaßhilfslinie* eingeschaltet ist. |
| `SetEndWitness(show: bool) -> bool` | Schaltet *Endmaßhilfslinie* ein oder aus. |
| `GetWitnessOverride() -> int \| None` | 0 = Bemaßungsstandard verwenden, 1 = eine gemeinsame benutzerdefinierte Länge für beide Maßhilfslinien, 2 = eine benutzerdefinierte Länge je Maßhilfslinie, 3 = ein gemeinsamer benutzerdefinierter Abstand für beide, 4 = ein benutzerdefinierter Abstand je Maßhilfslinie. |
| `SetWitnessOverride(mode: int) -> bool` | Legt die benutzerdefinierte Einstellung der Maßhilfslinien fest. 0 = Bemaßungsstandard verwenden, 1 = eine gemeinsame benutzerdefinierte Länge für beide Maßhilfslinien, 2 = eine benutzerdefinierte Länge je Maßhilfslinie, 3 = ein gemeinsamer benutzerdefinierter Abstand für beide, 4 = ein benutzerdefinierter Abstand je Maßhilfslinie. |
| `GetStartWitnessLength() -> float \| None` | Gibt die Länge der Anfangsmaßhilfslinie zurück (Welteinheiten, benutzerdefinierter Wert). |
| `SetStartWitnessLength(length: float) -> bool` | Legt die Länge der Anfangsmaßhilfslinie fest. |
| `GetEndWitnessLength() -> float \| None` | Gibt die Länge der Endmaßhilfslinie zurück. |
| `SetEndWitnessLength(length: float) -> bool` | Legt die Länge der Endmaßhilfslinie fest. |
| `GetStartWitnessOffset() -> float \| None` | Gibt den Abstand der Anfangsmaßhilfslinie zurück (Welteinheiten, benutzerdefinierter Wert). |
| `SetStartWitnessOffset(offset: float) -> bool` | Legt den Abstand der Anfangsmaßhilfslinie fest. |
| `GetEndWitnessOffset() -> float \| None` | Gibt den Abstand der Endmaßhilfslinie zurück. |
| `SetEndWitnessOffset(offset: float) -> bool` | Legt den Abstand der Endmaßhilfslinie fest. |

*Pfeile und Verweislinie*

| Methode | Beschreibung |
|---|---|
| `GetArrowsInside() -> bool \| None` | Gibt `True` zurück, wenn die Pfeilspitzen nach innen (zwischen die Maßhilfslinien) statt nach außen zeigen. |
| `SetArrowsInside(inside: bool) -> bool` | Schaltet *Pfeile innen* ein oder aus. Gibt `True` zurück, wenn die Pfeilspitzen nach innen (zwischen die Maßhilfslinien) statt nach außen zeigen. |
| `GetLeaderLine() -> bool \| None` | Eine Verweislinie verbindet den Text mit der Maßlinie, wenn der Text nicht zwischen die Maßhilfslinien passt. Wird vor allem bei Kreisbemaßungen und kleinen linearen Bemaßungen verwendet. |
| `SetLeaderLine(use: bool) -> bool` | Schaltet *Verweislinie* ein oder aus. Eine Verweislinie verbindet den Text mit der Maßlinie, wenn der Text nicht zwischen die Maßhilfslinien passt. Wird vor allem bei Kreisbemaßungen und kleinen linearen Bemaßungen verwendet. |

*Ausgegebener Text*

| Methode | Beschreibung |
|---|---|
| `GetShowValue() -> bool \| None` | Gibt an, ob der Messwert überhaupt ausgegeben wird. Ausgeschaltet + Präfixtext = eine einfache Beschriftung. |
| `SetShowValue(show: bool) -> bool` | Schaltet *Wert anzeigen* ein oder aus. Gibt an, ob der Messwert überhaupt ausgegeben wird. Ausgeschaltet + Präfixtext = eine einfache Beschriftung. |
| `GetLeaderText() -> str \| None` | Gibt den Präfixtext zurück (wird vor dem Wert ausgegeben). |
| `SetLeaderText(text: str) -> bool` | Legt den Präfixtext fest. |
| `GetTrailerText() -> str \| None` | Gibt den Suffixtext zurück (wird nach dem Wert ausgegeben). |
| `SetTrailerText(text: str) -> bool` | Legt den Suffixtext fest. |
| `GetBoxText() -> bool \| None` | Gibt an, ob *Text einrahmen* eingeschaltet ist (zeichnet einen Rahmen um den Text). |
| `SetBoxText(box: bool) -> bool` | Schaltet *Text einrahmen* ein oder aus. |
| `GetPrecision() -> int \| None` | Nachkommastellen bei Dezimaleinheiten; eine Zweierpotenz (0 = 1/1 ... 6 = 1/64) bei Brucheinheiten; bei Winkelbemaßungen 1 = ganze Grad, 2 = Grad/Minuten, 3 = Grad/Minuten/Sekunden. |
| `SetPrecision(precision: int) -> bool` | Legt die Genauigkeit fest. Nachkommastellen bei Dezimaleinheiten; eine Zweierpotenz (0 = 1/1 ... 6 = 1/64) bei Brucheinheiten; bei Winkelbemaßungen 1 = ganze Grad, 2 = Grad/Minuten, 3 = Grad/Minuten/Sekunden. |
| `GetShowSecondaryValue() -> bool \| None` | Sekundäre (duale) Einheitenanzeige – dieselben vier Einstellungen für den zweiten Messwert. |
| `SetShowSecondaryValue(show: bool) -> bool` | Schaltet *Sekundären Wert anzeigen* ein oder aus. Sekundäre (duale) Einheitenanzeige – dieselben vier Einstellungen für den zweiten Messwert. |
| `GetSecondaryLeaderText() -> str \| None` | Gibt den sekundären Präfixtext zurück. |
| `SetSecondaryLeaderText(text: str) -> bool` | Legt den sekundären Präfixtext fest. |
| `GetSecondaryTrailerText() -> str \| None` | Gibt den sekundären Suffixtext zurück. |
| `SetSecondaryTrailerText(text: str) -> bool` | Legt den sekundären Suffixtext fest. |
| `GetSecondaryBoxText() -> bool \| None` | Gibt an, ob *Sekundären Text einrahmen* eingeschaltet ist. |
| `SetSecondaryBoxText(box: bool) -> bool` | Schaltet *Sekundären Text einrahmen* ein oder aus. |
| `GetSecondaryPrecision() -> int \| None` | Gibt die sekundäre Genauigkeit zurück. |
| `SetSecondaryPrecision(precision: int) -> bool` | Legt die sekundäre Genauigkeit fest. |
| `GetNoteText() -> str \| None` | Anmerkungstext der Bemaßung, der bei einigen Standards unter dem Messwert angezeigt wird. |
| `SetNoteText(text: str) -> bool` | Legt den Anmerkungstext fest. Anmerkungstext der Bemaßung, der bei einigen Standards unter dem Messwert angezeigt wird. |

*Textplatzierung*

| Methode | Beschreibung |
|---|---|
| `GetTextPositionAutomatic() -> bool \| None` | Gibt `True` zurück, wenn Vectorworks den Text selbst positioniert; `False`, wenn er an eine feste Stelle gezogen wurde. |
| `SetTextPositionAutomatic(automatic: bool) -> bool` | Schaltet *Automatische Textposition* ein oder aus. Gibt `True` zurück, wenn Vectorworks den Text selbst positioniert; `False`, wenn er an eine feste Stelle gezogen wurde. |
| `GetTextInside() -> bool \| None` | Gibt an, ob *Text innen* eingeschaltet ist (Text zwischen den Maßhilfslinien). |
| `SetTextInside(inside: bool) -> bool` | Schaltet *Text innen* ein oder aus. |
| `GetTextFlipped() -> bool \| None` | Gibt an, ob *Text umgekehrt* eingeschaltet ist. |
| `SetTextFlipped(flipped: bool) -> bool` | Schaltet *Text umgekehrt* ein oder aus. |
| `GetTextRotation() -> int \| None` | 0 = an der Maßlinie ausgerichtet, 1 = nur horizontal, 2 = horizontal / vertikal. |
| `SetTextRotation(rotation: int) -> bool` | Legt die Textdrehung fest. 0 = an der Maßlinie ausgerichtet, 1 = nur horizontal, 2 = horizontal / vertikal. |
| `GetTextOffsetAlongLine() -> float \| None` | Abstand des Texts vom Anfangspunkt (negativ) oder vom Endpunkt (positiv) in Welteinheiten. |
| `SetTextOffsetAlongLine(offset: float) -> bool` | Legt den Textversatz entlang der Linie fest. Abstand des Texts vom Anfangspunkt (negativ) oder vom Endpunkt (positiv) in Welteinheiten. |
| `GetTextOffsetAboveLine() -> float \| None` | Abstand des Texts oberhalb der Maßlinie, in Welteinheiten. |
| `SetTextOffsetAboveLine(offset: float) -> bool` | Legt den Textversatz oberhalb der Linie fest. Abstand des Texts oberhalb der Maßlinie in Welteinheiten. |

*Schriftart des Texts*

| Methode | Beschreibung |
|---|---|
| `GetFontSize() -> float \| None` | Gibt die Schriftgröße zurück (Punkte). |
| `SetFontSize(points: float) -> bool` | Legt die Schriftgröße fest. |
| `GetFontStyle() -> int \| None` | Summe aus 1 = fett, 2 = kursiv, 4 = unterstrichen. |
| `SetFontStyle(style: int) -> bool` | Legt den Schriftstil fest. Summe aus 1 = fett, 2 = kursiv, 4 = unterstrichen. |
| `GetTextStyleName() -> str \| None` | Name des auf den Bemaßungstext angewendeten Textstils; leer, wenn die Bemaßung eigene Schrifteinstellungen verwendet. |
| `SetTextStyleName(name: str) -> bool` | Legt den Textstilnamen fest. Name des auf den Bemaßungstext angewendeten Textstils; leer, wenn die Bemaßung eigene Schrifteinstellungen verwendet. |

*Toleranz*

| Methode | Beschreibung |
|---|---|
| `GetToleranceType() -> DimensionTolerance \| None` | Gibt den Toleranztyp zurück. |
| `SetToleranceType(type: DimensionTolerance) -> bool` | Legt den Toleranztyp fest. |
| `GetTolerancePlus() -> float \| None` | Gibt die Plustoleranz zurück (Welteinheiten). |
| `SetTolerancePlus(value: float) -> bool` | Legt die Plustoleranz fest. |
| `GetToleranceMinus() -> float \| None` | Gibt die Minustoleranz zurück (Welteinheiten). |
| `SetToleranceMinus(value: float) -> bool` | Legt die Minustoleranz fest. |

*Standard und Einheiten*

| Methode | Beschreibung |
|---|---|
| `GetStandardName() -> str \| None` | Name des vom Objekt referenzierten Bemaßungsstandards ("ASME", "ISO", ein benutzerdefinierter Standard, ...). Der Standard liefert alle auf Seitenlängen bezogenen Darstellungsdetails der Bemaßung. |
| `SetStandardName(name: str) -> bool` | Legt den Standardnamen fest. Name des vom Objekt referenzierten Bemaßungsstandards ("ASME", "ISO", ein benutzerdefinierter Standard, ...). Der Standard liefert alle auf Seitenlängen bezogenen Darstellungsdetails der Bemaßung. |
| `GetStandardIndex() -> int \| None` | Index des Standards: > 0 ein mitgelieferter Standard, < 0 ein benutzerdefinierter Dokumentstandard. |
| `SetStandardIndex(index: int) -> bool` | Legt den Standardindex fest. Index des Standards: > 0 ein mitgelieferter Standard, < 0 ein benutzerdefinierter Dokumentstandard. |
| `GetUnitSetting() -> int \| None` | 0 = Dokumenteinheiten verwenden; andernfalls der Index eines benannten Zubehörs für Bemaßungseinheiteneinstellungen. |
| `SetUnitSetting(index: int) -> bool` | Legt die Einheiteneinstellung fest. 0 = Dokumenteinheiten verwenden; andernfalls der Index eines benannten Zubehörs für Bemaßungseinheiteneinstellungen. |

*Assoziativität*

| Methode | Beschreibung |
|---|---|
| `Associate(selectedObjectsOnly: bool = False) -> bool` | Verknüpft die Bemaßung mit den gemessenen Objekten, sodass sie ihnen folgt. `selectedObjectsOnly` beschränkt die Suche nach geeigneten Objekten auf die aktuell aktivierten Objekte. Nicht jede Bemaßung kann verknüpft werden; gibt `False` zurück, wenn die Verknüpfung abgelehnt wurde. |
| `GetDimensionsOf(hObject: Handle) -> list[Handle]` *statisch* | Objekte, mit denen eine Bemaßung verknüpft sein kann: die Bemaßungen, die aktuell `hObject` messen. |

Geerbt: alle Elemente von [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

### LinearDimensionObject

> **Vollständiger Name:** `api.LinearDimensionObject` · **Erbt von:** [`DimensionObject`](#dimensionobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Lineare Bemaßung: misst den Abstand zwischen zwei Punkten.

Es gibt zwei Varianten; sie unterscheiden sich darin, was geschieht, wenn die beiden Messpunkte nicht mit der Maßlinie ausgerichtet sind:

WINKELGEBUNDEN (fester Winkel) - CreateConstrained / CreateHorizontal / CreateVertical Die Maßlinie behält die bei der Erstellung festgelegte Richtung bei. Der ausgegebene Wert ist die PROJEKTION des Abstands zwischen den beiden Punkten auf diese Richtung. Eine horizontale Bemaßung einer schräg verlaufenden Wand liefert daher die horizontale Strecke, nicht die Wandlänge. Diese Bemaßungen werden mit dem Werkzeug Bemaßung horizontal und vertikal gezeichnet und normalerweise für die Bemaßung von Plänen verwendet.

FREI (schräg) - CreateUnconstrained Die Maßlinie verläuft parallel zur Verbindungslinie der beiden Punkte; der ausgegebene Wert ist daher immer ihr tatsächlicher Abstand. Diese Bemaßungen werden mit dem Werkzeug Bemaßung diagonal gezeichnet.

Beide verwenden einen VERSATZ: den Abstand der Maßlinie von den Messpunkten in Welteinheiten. Ein positiver Versatz platziert sie links von der Richtung Anfang -> Ende, ein negativer rechts davon.

Eine dritte Variante, die ORDINATENBEMASSUNG, misst jeden Punkt relativ zu einem gemeinsamen Bezugspunkt und gibt nur den Abstand dazu aus; CreateOrdinate erstellt eine solche Bemaßung.

Lineare Bemaßungen können assoziativ sein (siehe `DimensionObject.Associate`): Sind sie mit dem Objekt verknüpft, an dem sie ausgerichtet wurden, messen sie sich bei jeder Änderung dieses Objekts neu.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `LinearDimensionObject(h: Handle)` | Verweist auf die vorhandene lineare Bemaßung `h`; vor der Verwendung `IsValid()` prüfen. |

**Methoden**

*Beliebige lineare Bemaßung*

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | Winkelgebundene, freie oder Ordinatenbemaßung. |
| `CreateConstrained(start: Math.Point2D, end: Math.Point2D, direction: Math.Point2D, offset: float = 0.0) -> LinearDimensionObject` *statisch* | Winkelgebundene Bemaßung entlang einer ausdrücklich angegebenen Richtung. `direction` ist die Richtung der Maßlinie; bei einem Nullvektor wird die Richtung von `start` nach `end` verwendet. Schlägt fehl, wenn die beiden Punkte zusammenfallen. |
| `CreateConstrained(start: Math.Point2D, end: Math.Point2D, angle: float, offset: float = 0.0) -> LinearDimensionObject` *statisch* | Winkelgebundene Bemaßung, deren Maßlinie um den Winkel `angle` im Bogenmaß gegenüber der X-Achse gedreht ist. |
| `CreateHorizontal(start: Math.Point2D, end: Math.Point2D, offset: float = 0.0) -> LinearDimensionObject` *statisch* | Richtungsgebundene Bemaßung des horizontalen / vertikalen Abstands zwischen den beiden Punkten. |
| `CreateVertical(start: Math.Point2D, end: Math.Point2D, offset: float = 0.0) -> LinearDimensionObject` *statisch* | Erstellt eine winkelgebundene Bemaßung des vertikalen Abstands zwischen `start` und `end` mit dem Versatz `offset`. |
| `CreateUnconstrained(start: Math.Point2D, end: Math.Point2D, offset: float = 0.0) -> LinearDimensionObject` *statisch* | Freie („schräge“) Bemaßung: Die Maßlinie folgt start -> end, und der Wert ist der tatsächliche Abstand zwischen den beiden Punkten. Schlägt fehl, wenn die beiden Punkte zusammenfallen. |

*Ordinatenbemaßung*

| Methode | Beschreibung |
|---|---|
| `CreateOrdinate(datum: Math.Point2D, point: Math.Point2D, direction: Math.Point2D, offset: float = 0.0) -> LinearDimensionObject` *statisch* | `start` ist der Bezugspunkt, `end` der Messpunkt. |
| `Duplicate() -> LinearDimensionObject` | Dupliziert die lineare Bemaßung in der Zeichnung und gibt die Kopie zurück. |
| `IsConstrained() -> bool \| None` | `True` für eine richtungsgebundene Bemaßung (fester Winkel), `False` für eine freie Bemaßung. |
| `GetDirectionAngle() -> float \| None` | Richtung der Maßlinie als Winkel im Bogenmaß ab der X-Achse. Bei einer freien Bemaßung ist dies die Richtung vom Anfangs- zum Endpunkt. |
| `SetDirectionAngle(angle: float) -> bool` | Nur bei einer winkelgebundenen Bemaßung relevant; dreht die Maßlinie, ohne die Messpunkte zu verschieben, wodurch sich der ausgegebene Wert ändert. |
| `GetValue() -> float \| None` | Von der Bemaßung ausgegebener Wert: der Abstand zwischen den Messpunkten, bei einer winkelgebundenen Bemaßung auf die Maßlinienrichtung projiziert. |

Geerbt: alle Elemente von [`DimensionObject`](#dimensionobject), [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

### AngularDimensionObject

> **Vollständiger Name:** `api.AngularDimensionObject` · **Erbt von:** [`DimensionObject`](#dimensionobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Winkelbemaßung: misst den Winkel zwischen zwei Schenkeln, die sich in einem Scheitelpunkt treffen.

Die Bemaßung wird durch drei Punkte definiert – den SCHEITELPUNKT, an dem sich die beiden Schenkel treffen, und je einen Punkt auf jedem Schenkel – sowie einen Versatz, der den Radius des zwischen den Schenkeln gezeichneten Maßbogens bestimmt. Der ausgegebene Wert ist der gegen den Uhrzeigersinn vom ersten zum zweiten Schenkel überstrichene Winkel. Das Vertauschen der beiden Schenkelpunkte ergibt daher den Explementwinkel (360 Grad minus den ursprünglichen Winkel).

Eine Winkelbemaßung kann einen BEZUGSWINKEL darstellen: Sie zeichnet dann nur eine Maßhilfslinie und misst den Winkel eines einzelnen Schenkels zur Bezugsrichtung statt den Winkel zwischen zwei Schenkeln. Vectorworks erstellt standardmäßig Bezugswinkelbemaßungen; deshalb schaltet `Create()` diese Einstellung aus, während `CreateReferenceAngle()` sie beibehält.

Die Winkelzugriffsmethoden dieser Klasse verwenden wie die übrige API Bogenmaß; die GENAUIGKEIT der Winkel folgt dagegen den Bemaßungskonventionen: 1 = ganze Grad, 2 = Grad + Minuten, 3 = Grad + Minuten + Sekunden, 5..12 = entsprechend viele Nachkommastellen.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `AngularDimensionObject(h: Handle)` | Verweist auf die vorhandene Winkelbemaßung `h`; vor der Verwendung `IsValid()` prüfen. |

**Methoden**

*Allgemein*

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | True, wenn `h` auf ein Objekt des von dieser Klasse dargestellten Typs verweist. |
| `Create(vertex: Math.Point2D, firstLegPoint: Math.Point2D, secondLegPoint: Math.Point2D, offset: float = 0.0) -> AngularDimensionObject` *statisch* | Winkel von `firstLegPoint` nach `secondLegPoint` um `vertex`, im Abstand von `offset` Welteinheiten vom Scheitelpunkt gezeichnet. Schlägt fehl, wenn zwei beliebige der drei Punkte zusammenfallen. |
| `Create(vertex: Math.Point2D, startAngle: float, endAngle: float, legLength: float, offset: float = 0.0) -> AngularDimensionObject` *statisch* | Dasselbe, jedoch aus dem Scheitelpunkt, den beiden Schenkelrichtungen (Bogenmaß) und einer Schenkellänge erstellt. |

*Bezugswinkelvariante*

| Methode | Beschreibung |
|---|---|
| `CreateReferenceAngle(vertex: Math.Point2D, firstLegPoint: Math.Point2D, secondLegPoint: Math.Point2D, offset: float = 0.0) -> AngularDimensionObject` *statisch* | Eine einzelne Maßhilfslinie, die einen Schenkel relativ zur Bezugsrichtung misst. |
| `Duplicate() -> AngularDimensionObject` | Dupliziert die Winkelbemaßung in der Zeichnung und gibt die Kopie zurück. |
| `GetVertex() -> Math.Point2D \| None` | Scheitelpunkt, an dem sich die beiden Schenkel treffen. Vectorworks speichert ihn im Bemaßungsrahmen statt in den Anfangs-/Endpunkten, die die beiden Schenkelpunkte enthalten. |
| `SetVertex(vertex: Math.Point2D) -> bool` | Legt den Scheitelpunkt fest. Scheitelpunkt, an dem sich die beiden Schenkel treffen. Vectorworks speichert ihn im Bemaßungsrahmen statt in den Anfangs-/Endpunkten, die die beiden Schenkelpunkte enthalten. |
| `GetStartAngle() -> float \| None` | Richtungen der beiden Schenkel, im Bogenmaß ab der X-Achse. |
| `GetEndAngle() -> float \| None` | Gibt den Endwinkel zurück. |
| `GetValue() -> float \| None` | Gemessener Winkel im Bogenmaß, gegen den Uhrzeigersinn vom ersten zum zweiten Schenkel, im Bereich [0, 2*pi). |
| `GetReferenceAngle() -> bool \| None` | Gibt an, ob die Bemaßung mit einer einzelnen Maßhilfslinie relativ zur Bezugsrichtung misst. |
| `SetReferenceAngle(reference: bool) -> bool` | Schaltet *Bezugswinkel* ein oder aus. Gibt an, ob die Bemaßung mit einer einzelnen Maßhilfslinie relativ zur Bezugsrichtung misst. |

Geerbt: alle Elemente von [`DimensionObject`](#dimensionobject), [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

### ArcLengthDimensionObject

> **Vollständiger Name:** `api.ArcLengthDimensionObject` · **Erbt von:** [`DimensionObject`](#dimensionobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Bogenbemaßung: misst die Länge ENTLANG eines Kreisbogens statt des geradlinigen Abstands zwischen seinen Endpunkten, den eine lineare Bemaßung angeben würde.

Sie wird durch die beiden Endpunkte des gemessenen Abschnitts und den MITTELPUNKT des Kreisbogens definiert, auf dem sie liegen. Der Mittelpunkt legt fest, wie die beiden Punkte miteinander verbunden sind. Da zwischen zwei Punkten auf einem Kreis zwei Kreisbögen verlaufen, bestimmt `clockwise`, welcher davon gemessen wird.

Drei Schalter bestimmen die Darstellung; Vectorworks legt alle drei bei der Erstellung fest (anschließend sind sie schreibgeschützt – erstellen Sie die Bemaßung neu, um sie zu ändern):

- clockwise — bestimmt, welcher der beiden Kreisbögen zwischen den Endpunkten gemessen wird
- witnessPerpChord — Maßhilfslinien senkrecht zur Sehne statt radial vom Mittelpunkt aus
- arcIndicator — zeichnet das Bogensymbol, das den Wert als Bogenlänge kennzeichnet

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `ArcLengthDimensionObject(h: Handle)` | Verweist auf die vorhandene Bogenbemaßung `h`; vor der Verwendung `IsValid()` prüfen. |

**Methoden**

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | True, wenn `h` auf ein Objekt des von dieser Klasse dargestellten Typs verweist. |
| `Create(start: Math.Point2D, end: Math.Point2D, center: Math.Point2D, offset: float = 0.0, clockwise: bool = False, witnessPerpendicularToChord: bool = False, arcIndicator: bool = True) -> ArcLengthDimensionObject` *statisch* | Misst von `start` nach `end` entlang des Kreisbogens um `center`. Schlägt fehl, wenn die Punkte miteinander oder mit dem Mittelpunkt zusammenfallen. |
| `Create(center: Math.Point2D, radius: float, startAngle: float, sweepAngle: float, offset: float = 0.0, witnessPerpendicularToChord: bool = False, arcIndicator: bool = True) -> ArcLengthDimensionObject` *statisch* | Dasselbe, als Kreisbogen ausgedrückt: Mittelpunkt, Radius sowie Anfangs- und Öffnungswinkel im Bogenmaß. Ein negativer Öffnungswinkel misst den Kreisbogen im Uhrzeigersinn. |
| `Duplicate() -> ArcLengthDimensionObject` | Dupliziert die Bogenbemaßung in der Zeichnung und gibt die Kopie zurück. |
| `GetCenter() -> Math.Point2D \| None` | Mittelpunkt des gemessenen Kreisbogens. Vectorworks speichert ihn im Bemaßungsrahmen; die Anfangs-/Endpunkte enthalten die beiden Endpunkte des gemessenen Abschnitts. |
| `GetRadius() -> float \| None` | Gibt den Radius zurück. |
| `GetStartAngle() -> float \| None` | Startwinkel und vorzeichenbehafteter Öffnungswinkel des bemaßten Kreisbogens, im Bogenmaß. |
| `GetSweepAngle() -> float \| None` | Gibt den Öffnungswinkel zurück. |
| `GetValue() -> float \| None` | Von der Bemaßung ausgegebener Wert: die Länge entlang des Kreisbogens, in Welteinheiten. |
| `IsClockwise() -> bool \| None` | Beim Erstellen festgelegte Zeichenoptionen (am Objekt schreibgeschützt). |
| `IsWitnessPerpendicularToChord() -> bool \| None` | Gibt True zurück, wenn die Maßhilfslinien senkrecht zur Sehne stehen. |
| `HasArcIndicator() -> bool \| None` | Gibt True zurück, wenn die Bemaßung das Bogensymbol anzeigt. |

Geerbt: alle Elemente von [`DimensionObject`](#dimensionobject), [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

### RadialDimensionObject

> **Vollständiger Name:** `api.RadialDimensionObject` · **Erbt von:** [`DimensionObject`](#dimensionobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Kreisbemaßung: Misst den Radius oder den Durchmesser eines Kreises oder Kreisbogens.

Beide Arten werden aus dem MITTELPUNKT des Kreises und einem PUNKT AUF DEM KREIS aufgebaut, der die Zeichenrichtung der Bemaßung festlegt. Sie unterscheiden sich nur darin, was gemessen und ausgegeben wird:

- RADIAL — zeichnet vom Mittelpunkt (oder von außen mit einer Verweislinie) zum Kreis und gibt den Radius aus, üblicherweise mit vorangestelltem "R". DIAMETRAL zeichnet quer durch den Kreis und gibt den Durchmesser aus, üblicherweise mit vorangestelltem Durchmesserzeichen.

Verwenden Sie SetLeaderText, um dieses Präfix zu ändern; es wird nicht durch die Bemaßungsart vorgegeben.

Der Versatz verschiebt den Text und die Verweislinie vom Kreis weg; bei einer Radiusbemaßung verschiebt ein positiver Versatz die Bemaßung nach außerhalb des Kreises.

Der KOMPAKT-Modus (Get/SetCompact) ist die verkürzte Radiusdarstellung: Statt einer bis zum Mittelpunkt reichenden Linie wird am Kreis nur ein kurzer Linienansatz mit Pfeilspitze gezeichnet. Dies wird verwendet, wenn der Kreis für die Bemaßung zu klein ist.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `RadialDimensionObject(h: Handle)` | Verweist auf die vorhandene Kreisbemaßung `h`; vor der Verwendung `IsValid()` prüfen. |

**Methoden**

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | Beliebige Kreisbemaßung (Radius- oder Durchmesserbemaßung). |
| `CreateRadial(center: Math.Point2D, radius: float, angle: float, offset: float = 0.0) -> RadialDimensionObject` *statisch* | Radiusbemaßung des Kreises `centre`/`radius`, gezeichnet in Richtung des Winkels `angle` im Bogenmaß. |
| `CreateRadial(center: Math.Point2D, pointOnCircle: Math.Point2D, offset: float = 0.0) -> RadialDimensionObject` *statisch* | Radiusbemaßung des Kreises durch `pointOnCircle` um `center`. |
| `CreateDiametrical(center: Math.Point2D, radius: float, angle: float, offset: float = 0.0) -> RadialDimensionObject` *statisch* | Durchmesserbemaßung, gleiche Argumente. |
| `CreateDiametrical(center: Math.Point2D, pointOnCircle: Math.Point2D, offset: float = 0.0) -> RadialDimensionObject` *statisch* | Durchmesserbemaßung, gleiche Argumente. |
| `Duplicate() -> RadialDimensionObject` | Dupliziert die Kreisbemaßung in der Zeichnung und gibt die Kopie zurück. |
| `IsDiametrical() -> bool \| None` | `True`, wenn die Bemaßung den Durchmesser ausgibt, `False`, wenn sie den Radius ausgibt. |
| `GetCenter() -> Math.Point2D \| None` | Kreis, den die Bemaßung misst. Der Mittelpunkt ist der Anfangspunkt, der Punkt auf dem Kreis der Endpunkt. |
| `SetCenter(center: Math.Point2D) -> bool` | Legt den Mittelpunkt fest. Kreis, den die Bemaßung misst. Der Mittelpunkt ist der Anfangspunkt, der Punkt auf dem Kreis der Endpunkt. |
| `GetRadius() -> float \| None` | Gibt den Radius zurück. |
| `SetRadius(radius: float) -> bool` | Legt den Radius fest (Mittelpunkt und Richtung bleiben erhalten). |
| `GetDiameter() -> float \| None` | Gibt den Durchmesser zurück. |
| `SetDiameter(diameter: float) -> bool` | Legt den Durchmesser fest. |
| `GetAngle() -> float \| None` | Zeichenrichtung der Bemaßung als Winkel im Bogenmaß ab der X-Achse. |
| `SetAngle(angle: float) -> bool` | Legt den Winkel fest. Zeichenrichtung der Bemaßung als Winkel im Bogenmaß ab der X-Achse. Mittelpunkt und Radius bleiben erhalten. |
| `GetValue() -> float \| None` | Von der Bemaßung ausgegebener Wert: bei einer Durchmesserbemaßung der Durchmesser, andernfalls der Radius. |
| `GetCompact() -> bool \| None` | Verkürzte Radiusdarstellung – ein Linienansatz mit Pfeilspitze statt einer Linie zum Mittelpunkt. |
| `SetCompact(compact: bool) -> bool` | Schaltet *Kompakt* ein oder aus. Verkürzte Radiusdarstellung – ein Linienansatz mit Pfeilspitze statt einer Linie zum Mittelpunkt. |

Geerbt: alle Elemente von [`DimensionObject`](#dimensionobject), [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

### CenterMarkObject

> **Vollständiger Name:** `api.CenterMarkObject` · **Erbt von:** [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Achsenkreuz: das Kreuz, das den Mittelpunkt eines Kreises oder Kreisbogens kennzeichnet.

Anders als alle anderen Objekte dieser Gruppe ist ein Achsenkreuz KEIN Bemaßungsobjekt. Vectorworks erstellt es als einfache GRUPPE von Liniensegmenten, genau wie das Werkzeug Achsenkreuz:

- ein horizontales und ein vertikales Segment, die das kleine Kreuz im Mittelpunkt bilden und jeweils eine Armlänge lang sind;
- optional vier Verlängerungssegmente, die bis zum Kreis und etwas darüber hinaus reichen und durch einen Abstand vom Kreuz getrennt sind. Sie werden nur hinzugefügt, wenn der Kreis groß genug für das Kreuz und die Abstände ist – dieselbe Regel, die auch das Werkzeug anwendet.

Da es sich um gewöhnliche Geometrie handelt, enthält die Markierung keinen Messwert und nichts, was neu erzeugt werden müsste. Verschieben oder Skalieren verschiebt bzw. skaliert lediglich die Linien.

Die drei auf die Seite bezogenen Längen, die ihre Form bestimmen (Armlänge, Abstand, Überstand der Verlängerung), stammen aus dem aktiven BEMASSUNGSSTANDARD. Daher ist ein auf einer Ebene im Maßstab 1:50 gezeichnetes Achsenkreuz auf dem Papier genauso groß wie eines auf einer Ebene im Maßstab 1:100. `Create()` liest diese Werte aus dem Standard; `CreateWithSizes()` verwendet stattdessen ausdrücklich angegebene Längen in Welteinheiten für vollständige Kontrolle.

Wie beim Werkzeug wird die Gruppe in der Bemaßungsklasse platziert, wenn die Dokumenteinstellung „Bemaßungen in der Bemaßungsklasse erstellen“ eingeschaltet ist, andernfalls in der aktiven Klasse.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `CenterMarkObject(h: Handle)` | Verweist auf das vorhandene Achsenkreuz `h`; vor der Verwendung `IsValid()` prüfen. |

**Methoden**

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | Vectorworks-eigene Achsenkreuze sind Gruppen ohne besondere Kennzeichnung: `Is()` gibt vorsichtshalber `False` zurück. Behalten Sie das von `Create()` zurückgegebene Objekt bei oder erstellen Sie eines aus dem Handle einer bekannten Achsenkreuz-Gruppe. |
| `Create(center: Math.Point2D, radius: float = 0.0) -> CenterMarkObject` *statisch* | Achsenkreuz für den Kreis `center`/`radius` mit Größen aus dem aktiven Bemaßungsstandard. Bei einem Radius von null oder einem negativen Radius wird nur das Kreuz ohne Verlängerungssegmente gezeichnet. |
| `CreateFor(hObject: Handle) -> CenterMarkObject` *statisch* | Achsenkreuz für einen vorhandenen Kreis, einen Kreisbogen, eine Ellipse oder ein beliebiges anderes Objekt; die Markierung wird im Mittelpunkt seines Begrenzungsrahmens platziert und an dessen Größe angepasst. |
| `CreateWithSizes(center: Math.Point2D, radius: float, spokeLength: float, gap: float, extension: float) -> CenterMarkObject` *statisch* | Achsenkreuz mit ausdrücklich angegebenen Längen in Welteinheiten: `spokeLength` ist die Länge eines Kreuzarms, `gap` der Abstand zwischen Kreuz und Verlängerungssegmenten und `extension` der Überstand der Verlängerungssegmente über den Kreis hinaus. Bei einem zu kleinen Kreis werden die Verlängerungen weggelassen. |
| `Duplicate() -> CenterMarkObject` | Dupliziert das Achsenkreuz in der Zeichnung und gibt die Kopie zurück. |
| `GetCenter() -> Math.Point2D \| None` | Mittelpunkt des Kreuzes. |
| `GetSegmentCount() -> int \| None` | Anzahl der Liniensegmente der Markierung: 2 für ein einfaches Kreuz, bis zu 6 mit Verlängerungen. |

Geerbt: alle Elemente von [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

### WorksheetObject

> **Vollständiger Name:** `api.WorksheetObject` · **Erbt von:** [`TypedResource`](Resources.md#typedresource) → [`Resource`](Resources.md#resource) → `api.Object`

Verweis auf eine Tabelle (ZUBEHÖR) ohne Übernahme des Objekts, keine platzierte Tabellengrafik und kein Plug-in-Objekt zur Beschriftung. Alle Zeilen-, Spalten- und Datenbank-Unterzeilenindizes beginnen tabellengemäß bei 1 (Spalte 1 = A), anders als die bei 0 beginnenden Geometrie-APIs. Bereiche schließen ihre Grenzen ein. Zeichenfolgen sind UTF-8-kodiert. Vectorworks verwendet vorzeichenbehaftete 16-Bit-Indizes und -Größen; Python weist Werte außerhalb dieses Darstellungsbereichs zurück.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `WorksheetObject(h: Handle)` | Verweist auf die vorhandene Tabelle `h`; vor der Verwendung `IsValid()` prüfen. |

**Methoden**

*Allgemein*

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | True, wenn `h` auf ein Objekt des von dieser Klasse dargestellten Typs verweist. |
| `FromName(name: str) -> WorksheetObject` *statisch* | Die Tabelle (Zubehör) mit dem Namen `name`; ein ungültiges Objekt, wenn keine vorhanden ist. |

*Nur Erstellung*

| Methode | Beschreibung |
|---|---|
| `Create(name: str, rows: int = 20, columns: int = 10) -> WorksheetObject` *statisch* | Ein bereits belegter Name (auch der einer anderen Tabelle) führt zu einem Fehlschlag; verwenden Sie FromName für die Suche. |
| `Duplicate() -> WorksheetObject` | Dupliziert die Tabelle in der Zeichnung und gibt die Kopie zurück. |
| `GetRowCount() -> int \| None` | Anzahl der Zeilen. |
| `GetColumnCount() -> int \| None` | Anzahl der Spalten. |
| `IsValidCell(row: int, column: int) -> bool` | Gibt True zurück, wenn die Zelle `row` / `column` in der Tabelle vorhanden ist. |
| `IsValidRange(range: WorksheetObject.Range) -> bool` | Gibt True zurück, wenn jede Zelle von `range` in der Tabelle vorhanden ist. |
| `InsertRows(beforeRow: int, count: int = 1) -> bool` | Fügt `count` Zeilen vor der Zeile `beforeRow` ein. |
| `InsertColumns(beforeColumn: int, count: int = 1) -> bool` | Fügt `count` Spalten vor der Spalte `beforeColumn` ein. |
| `DeleteRows(startRow: int, count: int = 1) -> bool` | Löscht `count` Zeilen ab der Zeile `startRow`. |
| `DeleteColumns(startColumn: int, count: int = 1) -> bool` | Löscht `count` Spalten ab der Spalte `startColumn`. |
| `GetCellFormula(row: int, column: int) -> str \| None` | Definitionszeichenfolge einschließlich Literalwerten. Wird unverändert an Vectorworks übergeben; Vectorworks kann Formeln normalisieren. |
| `SetCellFormula(row: int, column: int, formula: str) -> bool` | Legt die Zellenformel fest. Definitionszeichenfolge einschließlich Literalwerten. Wird unverändert an Vectorworks übergeben; Vectorworks kann Formeln normalisieren. |
| `SetRangeFormula(range: WorksheetObject.Range, formula: str) -> bool` | Legt die Formel für den Bereich fest. |
| `GetCellText(row: int, column: int) -> str \| None` | Gibt den Zellentext für `row`, `column` zurück. |
| `GetCellValue(row: int, column: int) -> float \| None` | Bei nicht numerischen Zellen oder Fehlerzellen leer statt einer irreführenden null. Werte entsprechen der letzten Neuberechnung. |
| `ClearCells(range: WorksheetObject.Range) -> bool` | Löscht den Inhalt der Zellen in `range`. |
| `IsDatabaseRow(row: int) -> bool \| None` | Gibt True zurück, wenn `row` eine Datenbankzeile ist. |
| `GetDatabaseCriteria(row: int) -> str \| None` | Gibt die Datenbankkriterien für `row` zurück. |
| `SetDatabaseCriteria(row: int, criteria: str) -> bool` | Nicht weiter ausgewertete Vectorworks-Definition, z. B. "=DATABASE(ALL)". Eine leere Angabe wandelt die Zeile in eine normale Tabellenzeile um. Die Kriterien werden hier nicht analysiert. Gibt `False` zurück, wenn Vectorworks die Definition nicht anwenden kann (z. B. bei einer zusammengeführten Zeile). |
| `GetSubrowCount(row: int) -> int \| None` | Anzahl der Unterzeilen für `row`. |
| `GetSubrowCellText(row: int, column: int, subrow: int) -> str \| None` | Gibt den Zellentext der Unterzeile für `row`, `column`, `subrow` zurück. |
| `GetSubrowCellValue(row: int, column: int, subrow: int) -> float \| None` | Gibt den Zellenwert der Unterzeile für `row`, `column`, `subrow` zurück. |
| `GetColumnWidth(column: int) -> int \| None` | Breite/Höhe werden in tabelleneigenen Pixeln angegeben, NICHT in Modell- oder Welteinheiten. |
| `SetColumnWidth(firstColumn: int, lastColumn: int, width: int) -> bool` | Legt die Spaltenbreite fest. Breite/Höhe werden in tabelleneigenen Pixeln angegeben, NICHT in Modell- oder Welteinheiten. |
| `GetRowHeight(row: int) -> int \| None` | Gibt die Zeilenhöhe für `row` zurück. |
| `GetRowHeightLocked(row: int) -> bool \| None` | Gibt an, ob *Zeilenhöhe gesperrt* für `row` eingeschaltet ist. |
| `SetRowHeight(firstRow: int, lastRow: int, height: int, lockHeight: bool = True, includeSubrows: bool = False) -> bool` | Legt die Zeilenhöhe fest. |
| `AutoFitRowHeights(firstRow: int, lastRow: int) -> bool` | Passt die Höhen der Zeilen `firstRow` .. `lastRow` an deren Inhalt an. |
| `GetSubrowHeight(row: int, subrow: int) -> int \| None` | Gibt die Unterzeilenhöhe für `row`, `subrow` zurück. |
| `GetCellNumberFormat(row: int, column: int) -> WorksheetObject.NumberFormat \| None` | Gibt das Zahlenformat der Zelle für `row`, `column` zurück. |
| `SetNumberFormat(range: WorksheetObject.Range, format: WorksheetObject.NumberFormat) -> bool` | Legt das Zahlenformat fest. |
| `GetCellTextFormat(row: int, column: int) -> WorksheetObject.TextFormat \| None` | Gibt das Textformat der Zelle für `row`, `column` zurück. |
| `SetTextFormat(range: WorksheetObject.Range, format: WorksheetObject.TextFormat) -> bool` | Legt das Textformat fest. |
| `GetCellFill(row: int, column: int) -> WorksheetObject.Fill \| None` | Gibt die Zellenfüllung für `row`, `column` zurück. |
| `SetFill(range: WorksheetObject.Range, fill: WorksheetObject.Fill) -> bool` | Legt die Füllung fest. |
| `GetCellBorders(row: int, column: int) -> WorksheetObject.Borders \| None` | Gibt die Zellenränder für `row`, `column` zurück. |
| `SetBorders(range: WorksheetObject.Range, borders: WorksheetObject.Borders) -> bool` | Legt die Ränder fest. |
| `GetMergedCellRange(row: int, column: int) -> WorksheetObject.Range \| None` | Gibt den Bereich zusammengeführter Zellen für `row`, `column` zurück. |
| `MergeCells(range: WorksheetObject.Range) -> bool` | Führt die Zellen von `range` zu einer Zelle zusammen. |
| `UnmergeCells(range: WorksheetObject.Range) -> bool` | Trennt die zusammengeführten Zellen von `range`. |
| `Recalculate() -> bool` | Berechnet die Tabelle neu. |
| `GetAutoRecalculate() -> bool \| None` | Gibt an, ob *Automatisch neu berechnen* eingeschaltet ist. |
| `SetAutoRecalculate(enabled: bool) -> bool` | Schaltet *Automatisch neu berechnen* ein oder aus. |
| `CreateImage(topLeftCorner: Point2D) -> Handle` | Abbildungshandles verweisen auf Zeichnungsobjekte: Verwenden Sie sie nicht als WorksheetObject. Die Methode positioniert die erste vorhandene Abbildung neu oder erstellt eine auf der aktiven Ebene, falls noch keine vorhanden ist. Diese Erzeugungsfunktion erstellt nicht bei jedem Aufruf eine weitere Abbildung. |
| `GetImage() -> Handle` | Gibt die Abbildung zurück: die erste zugeordnete Abbildung oder einen Null-Handle, wenn keine vorhanden ist. |
| `FromImage(image: Handle) -> WorksheetObject` *statisch* | Die Tabelle (Zubehör), die von der Tabellengrafik `image` (einem in der Zeichnung platzierten Objekt) dargestellt wird. |

Geerbt: alle Elemente von [`TypedResource`](Resources.md#typedresource), [`Resource`](Resources.md#resource).

#### WorksheetObject.Range

> **Vollständiger Name:** `api.WorksheetObject.Range` · **Erbt von:** `api.Object`

Ab 1 indizierter Tabellenbereich einschließlich seiner Grenzen.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `Range()` | Standardwert (Felder mit ihren Standardwerten). |
| `Range(firstRow, firstColumn, lastRow, lastColumn)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `firstRow` | `int` | Erste Zeile (ab 1 indiziert). |
| `firstColumn` | `int` | Erste Spalte (ab 1 indiziert). |
| `lastRow` | `int` | Letzte Zeile (einschließlich). |
| `lastColumn` | `int` | Letzte Spalte (einschließlich). |

#### WorksheetObject.NumberFormat

> **Vollständiger Name:** `api.WorksheetObject.NumberFormat` · **Erbt von:** `api.Object`

Vectorworks-eigenes Zahlenformat für Tabellen, einschließlich formatabhängiger Genauigkeit und UTF-8-Präfix/-Suffix.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `NumberFormat()` | Standardwert (Felder mit ihren Standardwerten). |
| `NumberFormat(style, accuracy, leader, trailer)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `style` | `int` | 0 allgemein, 1 dezimal, 2 dezimal mit Kommagruppierung, 3 wissenschaftlich, 4 Bruch, 5 Bemaßung, 6 Winkel, 7 Datum, 8 bedingt, 9 allgemeiner Bruch, 10 Bemaßung mit Trenner, 11 Fläche, 12 Volumen, 13 Text, 14 Prozent. |
| `accuracy` | `int` | Vectorworks-eigene formatabhängige Genauigkeit, nicht immer Nachkommastellen. |
| `leader` | `str` | 0 allgemein, 1 dezimal, 2 dezimal mit Kommagruppierung, 3 wissenschaftlich, 4 Bruch, 5 Bemaßung, 6 Winkel, 7 Datum, 8 bedingt, 9 allgemeiner Bruch, 10 Bemaßung mit Trenner, 11 Fläche, 12 Volumen, 13 Text, 14 Prozent. |
| `trailer` | `str` | 0 allgemein, 1 dezimal, 2 dezimal mit Kommagruppierung, 3 wissenschaftlich, 4 Bruch, 5 Bemaßung, 6 Winkel, 7 Datum, 8 bedingt, 9 allgemeiner Bruch, 10 Bemaßung mit Trenner, 11 Fläche, 12 Volumen, 13 Text, 14 Prozent. |

#### WorksheetObject.TextFormat

> **Vollständiger Name:** `api.WorksheetObject.TextFormat` · **Erbt von:** `api.Object`

Tabellentext: Punktgröße, Schriftart/-stil, Ausrichtungen, Winkel in Grad, ColorRef-Index und Zeilenumbruch.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `TextFormat()` | Standardwert (Felder mit ihren Standardwerten). |
| `TextFormat(fontIndex, size, style, alignment, verticalAlignment, angle, color, wrap)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `fontIndex` | `int` | Index in der Schriftarttabelle des Dokuments. |
| `size` | `int` | Punkte. |
| `style` | `int` | Vectorworks-eigene Textstilbits (bold=1, italic=2, underline=4, ...). |
| `alignment` | `int` | 0 allgemein, 1 links, 2 zentriert, 3 rechts. |
| `verticalAlignment` | `int` | 0 allgemein, 1 oben, 3 zentriert, 5 unten. |
| `angle` | `int` | Vectorworks-eigener Tabellen-Textwinkel in GRAD, nicht im Bogenmaß. |
| `color` | `int` | ColorRef-Index des Dokuments, kein RGB-Wert. |
| `wrap` | `bool` | Gibt an, ob der Text in der Zelle umgebrochen wird. |

#### WorksheetObject.Fill

> **Vollständiger Name:** `api.WorksheetObject.Fill` · **Erbt von:** `api.Object`

Vectorworks-eigener Füllstil, ColorRef-Indizes des Dokuments und Muster.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `Fill()` | Standardwert (Felder mit ihren Standardwerten). |
| `Fill(style, background, foreground, pattern)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `style` | `int` | 0 keine, 1 einfarbig, 2 Muster. |
| `background` | `int` | Hintergrundfarbe (Farbindex). |
| `foreground` | `int` | ColorRef-Indizes des Dokuments. |
| `pattern` | `int` | Vectorworks-eigenes Füllmuster, nur für Stil 2 verwendet. |

#### WorksheetObject.Borders

> **Vollständiger Name:** `api.WorksheetObject.Borders` · **Erbt von:** `api.Object`

Kennzeichen für Zellenränder sowie für die Anwendung auf den äußeren Rahmen und die inneren Ränder eines Bereichs.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `Borders()` | Standardwert (Felder mit ihren Standardwerten). |
| `Borders(top, left, bottom, right, outline, insideHorizontal, insideVertical)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `top` | `bool` | Oberer Rand. |
| `left` | `bool` | Linker Rand. |
| `bottom` | `bool` | Unterer Rand. |
| `right` | `bool` | Rechter Rand. |
| `outline` | `bool` | Optionen zur Anwendung auf Bereiche; eine Abfrage für eine einzelne Zelle belässt diese auf `False`. |
| `insideHorizontal` | `bool` | Optionen zur Anwendung auf Bereiche; eine Abfrage für eine einzelne Zelle belässt diese auf `False`. |
| `insideVertical` | `bool` | Optionen zur Anwendung auf Bereiche; eine Abfrage für eine einzelne Zelle belässt diese auf `False`. |

## Aufzählungen

### DimensionKind

> **Vollständiger Name:** `api.DimensionKind` · **Art:** `IntEnum`

Bemaßungsart eines Objekts. Sie wird am Objekt gespeichert, bestimmt Messung und Darstellung und kann nach der Erstellung nicht geändert werden (erstellen Sie stattdessen die passende Art).

| Element | Wert | Beschreibung |
|---|---|---|
| `Unknown` | `-1` |  |
| `ConstrainedLinear` | `0` | Linear, feste Richtung: Die Maßlinie behält die bei der Erstellung angegebene Richtung bei (horizontal, vertikal oder beliebig gedreht) und misst die Projektion der beiden Punkte auf diese Richtung. fix_ang. |
| `UnconstrainedLinear` | `1` | Linear, freie Richtung: Die Maßlinie folgt der Verbindungslinie zwischen den beiden Messpunkten, sodass die Bemaßung immer deren tatsächlichen Abstand ausgibt. sloped. |
| `Ordinate` | `2` | Linear, von einem gemeinsamen Bezugspunkt aus gemessen; die Bemaßung gibt nur den Abstand von diesem Bezugspunkt aus. |
| `Radial` | `3` | Radius eines Kreises / Kreisbogens. |
| `Diametrical` | `4` | Durchmesser eines Kreises / Kreisbogens. |
| `Angular` | `5` | Winkel zwischen zwei Schenkeln um einen Scheitelpunkt. |
| `ArcLength` | `6` | Länge entlang eines Kreisbogens. |

### DimensionTolerance

> **Vollständiger Name:** `api.DimensionTolerance` · **Art:** `IntEnum`

Abweichung einer Bemaßung vom Nennwert, die neben dem Messwert ausgegeben wird.

| Element | Wert | Beschreibung |
|---|---|---|
| `None_` | `0` |  |
| `Single` | `1` | Ein einzelner +/-Wert. |
| `Double` | `2` | Separate Plus- und Minuswerte. |
| `Limit` | `3` | Oberer und unterer Grenzwert statt des Nennwerts. |

---

[Zurück zum Index](README.md) · [Nach oben](#objectsannotation--bemaßungen-datenstempel-planköpfe-und-tabellen)

[English](../../MCP/v2027.2/ObjectsArchitect.md) • **Deutsch** • [日本語](../../MCP.ja/v2027.2/ObjectsArchitect.md)

# ObjectsArchitect — Architektur (BIM)

> **Server:** Vectorworks MCP · **Version:** Vectorworks 2027 Update 2

[Zurück zum Inhaltsverzeichnis](README.md)

Werkzeuge für BIM-Gebäudeelemente: Wände, Böden/Decken, Dächer, Türen, Fenster, Stützen und Treppen.

## Inhaltsverzeichnis

- [Überblick](#überblick)
- [Architecture](#architecture)
  - [createWall](#createwall)
  - [createSlab](#createslab)
  - [createRoof](#createroof)
  - [createDoor](#createdoor)
  - [createWindow](#createwindow)
  - [createColumn](#createcolumn)
  - [createStair](#createstair)
  - [getArchitectureObject](#getarchitectureobject)
  - [setArchitectureObject](#setarchitectureobject)

## Überblick

Dieser Ordner enthält 1 Werkzeuggruppe mit insgesamt 9 Werkzeugen.

| Gruppe | Gruppen-ID | Standardmäßig aktiv | Sicherheitsstufe | Werkzeuge | Zusammenfassung |
|---|---|---|---|---|---|
| [Architecture](#architecture) | `architecture` | Nein | mittel | 9 | BIM-Gebäudeelemente: Wände, Böden/Decken, Dächer, Türen, Fenster, Stützen und Treppen. |

## Architecture

> **Gruppe:** `Architecture` · **Gruppen-ID:** `architecture` · **Standardmäßig aktiv:** Nein · **Sicherheitsstufe:** mittel · **Werkzeuge:** 9

**BIM-Gebäudeelemente: Wände, Böden/Decken, Dächer, Türen, Fenster, Stützen und Treppen.**

BIM-Gebäudeobjekte anzeigen, erstellen und bearbeiten: gerade und runde (gekrümmte) Wände, Böden/Decken, Dächer, Türen, Fenster, Stützen und Treppen.

**BIM-Arbeitsablauf:** Zuerst Geschosse und deren Ebenen (Gruppe Document: getStories, createStory), dann Stile (Gruppe Resources) und anschließend die Gebäudeelemente auf den Geschossebenen. Wände werden mit `topBound` / `bottomBound` an die Geschossebenen gebunden. `getArchitectureObject` liest die Wandendhöhen und den Stil aus; mit `includeHeightDetails` werden die durchschnittliche Höhe sowie Metadaten, Versätze und geprüfte Höhen der oberen und unteren Bindung ausgegeben. Längen werden in Welteinheiten und Winkel in Radiant angegeben, außer Dachneigungen an Dachkanten, die in Grad (2 bis 90) angegeben werden. Türen und Fenster werden freistehend erstellt; füge sie in Vectorworks in eine Wand ein. Jede Änderung wird als eigener benannter, rückgängig machbarer Vectorworks-Vorgang ausgeführt.

| Werkzeug | Auswirkung | Sicherheit | Zusammenfassung |
|---|---|---|---|
| [`createWall`](#createwall) | Bearbeitung | mittel | Erstellt eine gerade oder runde Wand. |
| [`createSlab`](#createslab) | Bearbeitung | mittel | Erstellt einen Boden/eine Decke aus einem 2D-Begrenzungsobjekt. |
| [`createRoof`](#createroof) | Bearbeitung | mittel | Erstellt ein polygonales Dach. |
| [`createDoor`](#createdoor) | Bearbeitung | mittel | Erstellt eine freistehende Tür. |
| [`createWindow`](#createwindow) | Bearbeitung | mittel | Erstellt ein freistehendes Fenster. |
| [`createColumn`](#createcolumn) | Bearbeitung | mittel | Erstellt eine Stütze. |
| [`createStair`](#createstair) | Bearbeitung | mittel | Erstellt eine Treppe. |
| [`getArchitectureObject`](#getarchitectureobject) | Nur lesend | niedrig | Liest die Eigenschaften einer Wand, eines Bodens/einer Decke, Dachs, einer Tür, eines Fensters, einer Stütze oder Treppe aus. |
| [`setArchitectureObject`](#setarchitectureobject) | Bearbeitung | mittel | Bearbeitet eine Wand, einen Boden/eine Decke, ein Dach, eine Tür, ein Fenster, eine Stütze oder Treppe. |

### createWall

Erstellt eine gerade oder runde Wand.

> **Auswirkung:** Bearbeitung · **Sicherheit:** mittel · **Rückgängig:** ein Schritt „MCP: createWall“ · **In runToolBatch:** ja

**Details**

Erstellt eine Wand von `start` bis `end`: gerade oder rund (gekrümmt) über `pointOnArc`, einen Punkt auf dem Bogen zwischen Anfang und Ende, der nicht auf deren Verbindungslinie liegt. Bei `thickness` 0 wird die aktive Wandeinstellung verwendet. Mit `topHeight` / `bottomHeight` lassen sich optional die Wandhöhen relativ zur Ebenenebene festlegen. Mit `topBound` / `bottomBound` werden die Ober- / Unterkante der Wand wie in der Infopalette an Geschossebenen gebunden: { kind: story|layerElevation|layerWallHeight, levelType (Ebenentyp bei Geschossbindungen), relativeStory (Geschossbindung: -1 das Geschoss darunter, 0 das Geschoss der Wandschicht, Standardwert, 1 das Geschoss darüber), offset (Welteinheiten, Standardwert 0) }; `getArchitectureObject` mit `includeHeightDetails` liest diese Werte aus.

Die Bindungen werden nach den anderen Werten angewendet und verschieben die Wandenden auf die gebundenen Höhen; sie ersetzen daher `topHeight` / `bottomHeight`: Ein Aufruf mit beiden Optionen wird abgelehnt. Ist eine Bindung für die Wand nicht möglich (ihre Ebene gehört zu keinem Geschoss, es gibt kein Geschoss darüber/darunter, ein Geschoss hat diese Ebene nicht oder die obere Höhe liegt nicht über der unteren), schlägt der Aufruf fehl und erstellt nichts; `applied` meldet `topBound` / `bottomBound`.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `start` | [Punkt](Common.md#punkte) | Ja | Anfangspunkt. |
| `end` | [Punkt](Common.md#punkte) | Ja | Endpunkt. |
| `pointOnArc` | [Punkt](Common.md#punkte) |  | Macht die Wand rund (gekrümmt): Punkt auf dem Bogen zwischen `start` und `end`. Liegt der Punkt nicht außerhalb der Geraden von `start` nach `end`, schlägt der Aufruf fehl. |
| `thickness` | number |  | Wandstärke in Welteinheiten. |
| `topHeight` | number |  | Höhe der Wandoberkante an beiden Enden, in Welteinheiten relativ zur Ebenenebene. Wird nur `topHeight` oder `bottomHeight` angegeben, ist der jeweils andere Wert `0`. Nicht zusammen mit `topBound` oder `bottomBound` zulässig. |
| `bottomHeight` | number |  | Höhe der Wandunterkante an beiden Enden, in Welteinheiten relativ zur Ebenenebene. Wird nur `topHeight` oder `bottomHeight` angegeben, ist der jeweils andere Wert `0`. Nicht zusammen mit `topBound` oder `bottomBound` zulässig. |
| `topBound` | object |  | Bindet die Wandoberkante wie in der Objekt-Info-Palette; ersetzt `topHeight` und `bottomHeight`. |
| `topBound.kind` | string | Ja | Einer von: `story`, `layerElevation`, `layerWallHeight`. |
| `topBound.levelType` | string |  | Geschosstyp. Für `kind` `story` erforderlich und darf nicht leer sein; bei Ebenentypen wird er ignoriert. Ein Wert, der keine Zeichenfolge ist, führt bei allen Typen zur Ablehnung des Aufrufs. |
| `topBound.relativeStory` | integer |  | Einer von: `-1`, `0`, `1`. Standardwert: `0`. |
| `topBound.offset` | number |  | Standardwert: `0`. |
| `bottomBound` | object |  | Bindet die Wandunterkante wie in der Objekt-Info-Palette; ersetzt `topHeight` und `bottomHeight`. |
| `bottomBound.kind` | string | Ja | Einer von: `story`, `layerElevation`, `layerWallHeight`. |
| `bottomBound.levelType` | string |  | Geschosstyp. Für `kind` `story` erforderlich und darf nicht leer sein; bei Ebenentypen wird er ignoriert. Ein Wert, der keine Zeichenfolge ist, führt bei allen Typen zur Ablehnung des Aufrufs. |
| `bottomBound.relativeStory` | integer |  | Einer von: `-1`, `0`, `1`. Standardwert: `0`. |
| `bottomBound.offset` | number |  | Standardwert: `0`. |
| `class` | string |  | Erstellungsoption: Klasse des neuen Objekts; wird bei Bedarf erstellt. Siehe [Erstellungsoptionen](Common.md#optionen-zur-erstellung). |
| `name` | string |  | Erstellungsoption: Name des neuen Objekts. |
| `select` | boolean |  | Erstellungsoption: Neues Objekt auswählen. |
| `useClassAttributes` | boolean |  | Erstellungsoption: Mit `class` auch die Attribute des neuen Objekts anhand der Klasse festlegen. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `applied` | Nur `topBound` und `bottomBound`: Für jede angegebene und geschriebene Begrenzung `true`. Wird ausgelassen, wenn keine Begrenzung angegeben wurde; `thickness`, `pointOnArc` und die Höhen werden nicht gemeldet. |


### createSlab

Erstellt einen Boden/eine Decke aus einem 2D-Begrenzungsobjekt.

> **Auswirkung:** Bearbeitung · **Sicherheit:** mittel · **Rückgängig:** ein Schritt „MCP: createSlab“ · **In runToolBatch:** ja

**Details**

Erstellt einen Boden/eine Decke (Bodenplatte/Belag/Decke; Vectorworks-Plug-in-Objekt `Slab`) aus einem vorhandenen 2D-Begrenzungsobjekt, angegeben durch `profileUuid`: ein Polygon, eine Polylinie, ein Oval/Kreis oder ein Bogen, das/die/den der Boden/die Decke übernimmt. Die optionalen Werte `style` und `height` (Höhe des Bezugspunkts des Bodens/der Decke, also der Ober- oder Unterseite seiner/ihrer Kernkomponente gemäß Stil) werden in dieser Reihenfolge geschrieben. `style` ist ein Boden-/Deckenstil der Zeichnung: sein Name oder die UUID seiner Ressource (getResources mit `resourceType` `slabStyle` listet diese auf); der Stil wird vor dem Erstellen geprüft. Ist ein Name oder eine UUID kein Boden-/Deckenstil der Zeichnung, wird der Aufruf abgelehnt und nichts erstellt. Alternativ kann der interne Index verwendet werden: 0 hebt den Stil auf, wobei die Komponenten erhalten bleiben; ein Index, der keinem Boden-/Deckenstil entspricht, wird als falsch gemeldet und nicht geschrieben.

`applied` meldet für jeden angegebenen Wert true/false; `getArchitectureObject` gibt `style` (den Index) und `styleName` aus.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `profileUuid` | string | Ja | UUID des Objekts, das das Profil bereitstellt. |
| `height` | number |  | Höhe des Bezugspunkts des Bodens/der Decke (Ober- oder Unterseite der Kernkomponente gemäß Stil) in Welteinheiten. |
| `style` | integer or string |  | Ein Plattenstil der Zeichnung: sein Name oder die UUID seiner Ressource (die Liste der Plattenstile liefert `getResources` mit `resourceType` `slabStyle`), oder eine Ganzzahl als interner Index (`0`: ohne Stil, Komponenten bleiben erhalten). Ein Name oder eine UUID, die keinem Plattenstil entspricht, führt zur Ablehnung des Aufrufs; ein ungültiger Index wird als `false` gemeldet und nicht geschrieben. |
| `class` | string |  | Erstellungsoption: Klasse des neuen Objekts; wird bei Bedarf erstellt. Siehe [Erstellungsoptionen](Common.md#optionen-zur-erstellung). |
| `name` | string |  | Erstellungsoption: Name des neuen Objekts. |
| `select` | boolean |  | Erstellungsoption: Neues Objekt auswählen. |
| `useClassAttributes` | boolean |  | Erstellungsoption: Mit `class` auch die Attribute des neuen Objekts anhand der Klasse festlegen. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `applied` | Für jedes angegebene Feld `style` und `height`: `true`, wenn geschrieben, andernfalls `false` (bei falschem Typ oder einem `style`-Index, der keinem Plattenstil entspricht). Wird ausgelassen, wenn keines angegeben wurde. |


### createRoof

Erstellt ein polygonales Dach.

> **Auswirkung:** Bearbeitung · **Sicherheit:** mittel · **Rückgängig:** ein Schritt „MCP: createRoof“ · **In runToolBatch:** ja

**Details**

Erstellt ein polygonales Dach. Optional sind `generateGableWalls`, `bearingInset`, `roofThickness`, `miterType` (vertical|horizontal|double), `verticalMiter` und `edges`, die Umrisskanten des Dachs in Reihenfolge: mindestens 3 Einträge { point, slope, projection, eaveHeight }, wobei `slope` die Neigung in Grad von 2 bis 90 angibt (Vectorworks erstellt ein Dach nur bei Kantenneigungen von 2 bis 90 Grad) und `projection` (Dachüberstand) sowie `eaveHeight` (relativ zur Ebenenhöhe) in Welteinheiten angegeben werden; Standardwert jeweils 0.

Jede Kante wird vor dem Erstellen des Dachs geprüft: Eine fehlende `point`- oder `slope`-Angabe, ein Wert, der keine endliche Zahl ist, oder eine Neigung außerhalb von 2 bis 90 führt zur Ablehnung des Aufrufs; es wird nichts erstellt. Das neue Dach hat keinen Dachraum, keine Untersicht und keine Dachblende. `getArchitectureObject` gibt die Kanten im selben Format aus.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `generateGableWalls` | boolean |  | Standard `false`. |
| `bearingInset` | number |  | Standard `0`. |
| `roofThickness` | number |  | Standard `0`. |
| `miterType` | string |  | Einer von: `vertical`, `horizontal`, `double`. |
| `verticalMiter` | number |  | Standard `0`. |
| `edges` | array of object |  | Mindestens 3 Einträge. |
| `edges[].point` | [Punkt](Common.md#punkte) | Ja | Punkt auf der Dachkontur; die Kanten werden der Reihe nach verwendet. |
| `edges[].slope` | number | Ja | Grad, 2 bis 90. Minimum: `2`. Maximum: `90`. |
| `edges[].projection` | number |  | Dachüberstand an der Traufe in Welteinheiten. Standard `0`. |
| `edges[].eaveHeight` | number |  | Traufhöhe relativ zur Ebenenhöhe, in Welteinheiten. Standard `0`. |
| `class` | string |  | Erstellungsoption: Klasse des neuen Objekts; wird bei Bedarf erstellt. Siehe [Erstellungsoptionen](Common.md#optionen-zur-erstellung). |
| `name` | string |  | Erstellungsoption: Name des neuen Objekts. |
| `select` | boolean |  | Erstellungsoption: Neues Objekt auswählen. |
| `useClassAttributes` | boolean |  | Erstellungsoption: Mit `class` auch die Attribute des neuen Objekts anhand der Klasse festlegen. |

**Ergebnis**

Objektreferenz des neuen Dachs (siehe [Objektreferenzen](Common.md#objektreferenzen)). Es gibt kein `applied`.

Fehler: `'edges' must be an array of 3 to 32767 edges`; ein Problem mit einer Kante, stets mit dem Präfix `'edges'[<i>]: ` und vor dem Erstellen des Dachs erkannt (`an edge is an object { point, slope, projection, eaveHeight } whose slope, projection and eaveHeight are numbers`; `the edge needs a 'point' { x, y }`; `the edge needs a 'slope' (degrees, 2 to 90)`; `the point, slope, projection and eaveHeight must be finite numbers`; `the slope <n> is not 2 to 90 degrees: Vectorworks builds a roof only with edge slopes from 2 to 90 degrees`); `failed to create roof`; `Vectorworks refused the roof edge 'edges'[<i>]`. Ein fehlgeschlagener Aufruf wird zurückgerollt (`rolledBack`), sodass kein Dach bestehen bleibt.


### createDoor

Erstellt eine freistehende Tür.

> **Auswirkung:** Bearbeitung · **Sicherheit:** mittel · **Rückgängig:** ein Schritt „MCP: createDoor“ · **In runToolBatch:** ja

**Details**

Erstellt ein parametrisches Tür-Objekt an `position`, freistehend (füge es in Vectorworks in eine Wand ein). Die optionalen Werte `width` und `height` (positive Werte in Welteinheiten) legen die Türgröße fest, wie sie in der Infopalette angezeigt wird, gemessen anhand von `Size Reference`; Vectorworks berechnet daraus die Türblattgröße (siehe `leafWidth` / `leafHeight` in `getArchitectureObject`). Der optionale Wert `sizeReference` (leaf: Türblatt, unit: Einheit mit Rahmen, roughOpening: Rohbauöffnung) wird zuerst geschrieben; die Türeinstellungen der Zeichnung legen den Standardwert fest.

Wird die Referenz durch `sizeReference` geändert, müssen sowohl `width` als auch `height` angegeben werden, da die gespeicherte Größe der Tür anhand der neuen Referenz gemessen wird. Optional sind `config` (veraltetes Konfigurations-Popup) und `idLabel`. Ein Wert, der durch den Plug-in-Stil der Tür festgelegt wird, kann nicht geändert werden: Der Aufruf wird abgelehnt und erstellt nichts. `applied` meldet für jeden angegebenen Wert true/false; `getArchitectureObject` gibt `width` und `height` wie angegeben zurück.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `position` | [Punkt](Common.md#punkte) | Ja | Einfügepunkt. |
| `width` | number |  | Größer als `0`. |
| `height` | number |  | Größer als `0`. |
| `sizeReference` | string |  | Einer von: `leaf`, `unit`, `roughOpening`. |
| `config` | string |  | Veraltetes Konfigurations-Popup. |
| `idLabel` | string |  | ID-Beschriftung der Tür. |
| `class` | string |  | Erstellungsoption: Klasse des neuen Objekts; wird bei Bedarf erstellt. Siehe [Erstellungsoptionen](Common.md#optionen-zur-erstellung). |
| `name` | string |  | Erstellungsoption: Name des neuen Objekts. |
| `select` | boolean |  | Erstellungsoption: Neues Objekt auswählen. |
| `useClassAttributes` | boolean |  | Erstellungsoption: Mit `class` auch die Attribute des neuen Objekts anhand der Klasse festlegen. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `applied` | Für jedes angegebene Feld aus `sizeReference`, `width`, `height`, `config` und `idLabel` ein Eintrag: `true`, wenn geschrieben, andernfalls `false`, wenn die Tür den Wert ablehnt. Wird ausgelassen, wenn keines angegeben wurde. |


### createWindow

Erstellt ein freistehendes Fenster.

> **Auswirkung:** Bearbeitung · **Sicherheit:** mittel · **Rückgängig:** ein Schritt „MCP: createWindow“ · **In runToolBatch:** ja

**Details**

Erstellt ein parametrisches Fenster-Objekt an `position`, freistehend (füge es in Vectorworks in eine Wand ein). Die optionalen Werte `width` und `height` (positive Werte in Welteinheiten) legen die Fenstergröße fest, wie sie in der Infopalette angezeigt wird, gemessen anhand von `Size Reference`; Vectorworks berechnet daraus die Einheitsgröße (siehe `unitWidth` / `unitHeight` in `getArchitectureObject`). Der optionale Wert `sizeReference` (sash: Flügelöffnung, unit: Einheit, roughOpening: Rohbauöffnung) wird zuerst geschrieben; die Fenstereinstellungen der Zeichnung legen den Standardwert fest. Bei einer Referenzänderung müssen sowohl `width` als auch `height` angegeben werden.

Der optionale Wert `elevation` gibt die Höhe der Fensterbrüstung, also die Unterkante des Fensters, in Welteinheiten über der Ebenenebene an (auch bei einem Fenster in einer Wand: nicht über der Wandunterkante); er wird nach der Größe geschrieben. Das Fenster behält die Einstellung „Elevation Set At“ bei: Bei „Head of Window“ (Standard) speichert Vectorworks die Kopfhöhe, `elevation + height` (`getArchitectureObject` gibt `headHeight` und `elevationSetAt` aus).

Optional ist `idLabel`. Ein Wert, der durch den Plug-in-Stil des Fensters festgelegt wird, kann nicht geändert werden: Der Aufruf wird abgelehnt und erstellt nichts. `applied` meldet für jeden angegebenen Wert true/false; `getArchitectureObject` gibt `width`, `height` und `elevation` wie angegeben zurück.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `position` | [Punkt](Common.md#punkte) | Ja | Einfügepunkt. |
| `width` | number |  | Größer als `0`. |
| `height` | number |  | Größer als `0`. |
| `sizeReference` | string |  | Einer von: `sash`, `unit`, `roughOpening`. |
| `elevation` | number |  | Höhe in Welteinheiten. |
| `idLabel` | string |  | ID-Beschriftung des Fensters. |
| `class` | string |  | Erstellungsoption: Klasse des neuen Objekts; wird bei Bedarf erstellt. Siehe [Erstellungsoptionen](Common.md#optionen-zur-erstellung). |
| `name` | string |  | Erstellungsoption: Name des neuen Objekts. |
| `select` | boolean |  | Erstellungsoption: Neues Objekt auswählen. |
| `useClassAttributes` | boolean |  | Erstellungsoption: Mit `class` auch die Attribute des neuen Objekts anhand der Klasse festlegen. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `applied` | Für jedes angegebene Feld aus `sizeReference`, `width`, `height`, `elevation` und `idLabel` ein Eintrag: `true`, wenn geschrieben, andernfalls `false`, wenn das Fenster den Wert ablehnt. Wird ausgelassen, wenn keines angegeben wurde. |


### createColumn

Erstellt eine Stütze.

> **Auswirkung:** Bearbeitung · **Sicherheit:** mittel · **Rückgängig:** ein Schritt „MCP: createColumn“ · **In runToolBatch:** ja

**Details**

Erstellt eine Stütze (das Vectorworks-Plug-in-Objekt `Column2`) an `position`. Optional sind `shape` (Rectangular|Oval; Round entspricht Oval), `height` (der einzelnen aktiven Komponente; schlägt fehl, wenn die Stütze sowohl architektonische als auch statische Komponenten verwendet), `width` und `depth` (Schaft) sowie `diameter` (runder Schaft). Kann ein Wert nicht festgelegt werden, wird die Stütze entfernt und das Werkzeug schlägt fehl.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `position` | [Punkt](Common.md#punkte) | Ja | Einfügepunkt. |
| `shape` | string |  | `Rectangular` oder `Oval`; Round entspricht Oval. |
| `height` | number |  | Für die einzelne aktive Komponente; schlägt fehl, wenn die Stütze sowohl architektonische als auch statische Komponenten verwendet. |
| `width` | number |  | Breite in Welteinheiten. |
| `depth` | number |  | Tiefe in Welteinheiten. |
| `diameter` | number |  | Durchmesser in Welteinheiten. |
| `class` | string |  | Erstellungsoption: Klasse des neuen Objekts; wird bei Bedarf erstellt. Siehe [Erstellungsoptionen](Common.md#optionen-zur-erstellung). |
| `name` | string |  | Erstellungsoption: Name des neuen Objekts. |
| `select` | boolean |  | Erstellungsoption: Neues Objekt auswählen. |
| `useClassAttributes` | boolean |  | Erstellungsoption: Mit `class` auch die Attribute des neuen Objekts anhand der Klasse festlegen. |

**Ergebnis**

Objektreferenz der neuen Säule (siehe [Objektreferenzen](Common.md#objektreferenzen)). Es gibt kein `applied`.

Fehler: `failed to create column (requires the 'Column2' plug-in object)`; `failed to set column shape`; `failed to set column height (requires a single bound component)`; `failed to set column shaft width`; `failed to set column shaft depth`; `failed to set column shaft diameter`. Wenn ein Wert fehlschlägt, wird die Säule gelöscht; der fehlgeschlagene Aufruf wird zurückgerollt (`rolledBack`), sodass keine Säule bestehen bleibt.


### createStair

Erstellt eine Treppe.

> **Auswirkung:** Bearbeitung · **Sicherheit:** mittel · **Rückgängig:** ein Schritt „MCP: createStair“ · **In runToolBatch:** ja

**Details**

Erstellt an `position` eine Treppe (das Vectorworks-Plug-in-Objekt „Stairs CW“ in seiner Standardkonfiguration). Die optionalen positiven Werte `totalRise`, `totalRun` (Lauflänge), `treadDepth` und `riserHeight` werden vor dem Zurücksetzen der Treppe geschrieben; die Treppe berechnet abhängige Werte neu, lies sie daher mit `getArchitectureObject` erneut aus. `width` kann bei einer „Stairs CW“-Treppe nicht festgelegt werden. `applied` meldet für jeden angegebenen Wert true/false.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `position` | [Punkt](Common.md#punkte) | Ja | Einfügepunkt. |
| `width` | number |  | Breite in Welteinheiten. |
| `totalRise` | number |  | Gesamthöhe in Welteinheiten. Muss größer als `0` sein. |
| `totalRun` | number |  | Lauflänge. |
| `treadDepth` | number |  | Auftrittstiefe in Welteinheiten. Muss größer als `0` sein. |
| `riserHeight` | number |  | Steigungshöhe in Welteinheiten. Muss größer als `0` sein. |
| `class` | string |  | Erstellungsoption: Klasse des neuen Objekts; wird bei Bedarf erstellt. Siehe [Erstellungsoptionen](Common.md#optionen-zur-erstellung). |
| `name` | string |  | Erstellungsoption: Name des neuen Objekts. |
| `select` | boolean |  | Erstellungsoption: Neues Objekt auswählen. |
| `useClassAttributes` | boolean |  | Erstellungsoption: Mit `class` auch die Attribute des neuen Objekts anhand der Klasse festlegen. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `applied` | Für jedes angegebene Feld aus `width`, `totalRise`, `totalRun`, `treadDepth` und `riserHeight` ein Eintrag: `true`, wenn geschrieben, andernfalls `false`. `width` ist immer `false`. Wird ausgelassen, wenn keines angegeben wurde. |


### getArchitectureObject

Liest die Eigenschaften einer Wand, eines Bodens/einer Decke, Dachs, einer Tür, eines Fensters, einer Stütze oder Treppe aus.

> **Auswirkung:** Nur lesend · **Sicherheit:** niedrig · **Rückgängig:** keiner · **In runToolBatch:** zulässig

**Details**

Liest die typisierten Eigenschaften einer Wand, eines Bodens/einer Decke, Dachs, einer Tür, eines Fensters, einer Stütze oder Treppe aus (Abmessungen, Höhen, Stil, Kennung im Bauteilstempel usw.). Wände geben die nativen Z-Werte ihrer Endpunkte `startTop` / `startBottom` / `endTop` / `endBottom` in Welteinheiten aus, nicht die gespeicherten Bindungsversätze, außerdem Endkappen { leftCap (Anfangsseite), rightCap (Endseite), round } und `isCurtainWall`. Böden/Decken (das Plug-in-Objekt `Slab` oder ein älterer Bodenplatten-Knoten aus einer älteren Datei, der keine Höhe und keine Parameter hat) geben `height`, `style` (den internen Index des Boden-/Deckenstils; 0 bedeutet ohne Stil) und `styleName` (den Namen dieses Stils) aus.

Dächer geben `edgeCount` und `edges` aus, den Umriss in Reihenfolge: ein { point, slope (Grad), projection, eaveHeight (relativ zur Ebenenhöhe) } pro Kante, `null` für eine Kante, die nicht gelesen werden kann, im Format, das `createRoof` und `setArchitectureObject` erwarten; außerdem `generateGableWalls`, `bearingInset`, `roofThickness`, `miterType` (vertical|horizontal|double) und `verticalMiter`.

Türen geben `width` und `height` aus (die Türgröße, wie sie in der Infopalette angezeigt wird, in Welteinheiten und gemäß `sizeReference`: leaf|unit|roughOpening), `leafWidth` / `leafHeight` (die von Vectorworks beim letzten Zurücksetzen berechnete Türblattgröße), `config`, `idLabel`, `thickness` (Türblatt), `topShape`, `leafType` und `onSchedule`. Fenster geben auf dieselbe Weise `width`, `height` und `sizeReference` (sash|unit|roughOpening) aus, außerdem `unitWidth` / `unitHeight` (die von Vectorworks berechnete Einheitengröße), `elevation` (die Höhe der Brüstung: Unterkante des Fensters über der Ebenenebene, auch bei einem Fenster in einer Wand), `headHeight`, `elevationSetAt` (head|sill: welches der beiden Maße das Fenster als Elevation-Parameter speichert), `idLabel`, `sashOperation` (veraltetes SashOperation-Popup), `topShape`, `jambWidth`, `jambDepth`, `includeSill`, `sillStyle`, `onSchedule` und `description`. Stützen (`Column2`-Plug-in-Objekt oder ältere `Column`) geben `shape`, `height`, `width`, `depth` und `diameter` aus; Treppen (Plug-in-Objekt „Stairs CW“) geben `width` (die erste Treppenbreite), `totalRise`, `totalRun` (Lauflänge), `numRisers`, `treadDepth` und `riserHeight` aus.

Popup-Werte werden unverändert so ausgegeben, wie sie das Plug-in speichert. Der optionale Parameter `params` (Liste der Plug-in-Parameternamen; für Böden/Decken, Türen, Fenster, Stützen und Treppen) ergänzt `params` { name: value } mit typisierten Werten: reelle Zahlen als Zahlen in Welteinheiten (Winkelparameter in Grad), Ganzzahlen, boolesche Werte und andere Typen als Zeichenfolgen; nicht vorhandene Parameternamen werden ausgelassen.

Im Gegensatz zu den Anzeigetexten von `getObjectParameters` sind dies exakte Werte im Format, das `params` in `setArchitectureObject` schreibt. Der optionale Parameter `includeHeightDetails` (Standardwert false) ergänzt ein nur für Wände verfügbares Objekt `heightDetails`: `startHeight` / `endHeight` (Endpunkthöhenunterschiede), `averageHeight` (vorhandene geometrische Durchschnittsberechnung, auf Welteinheiten normiert), Status zur Verfügbarkeit der Messwerte sowie `topBound` / `bottomBound` mit `status` (valid|missing|unresolved|invalid), `kind` (layerElevation|layerWallHeight|story|unknown), `levelType`, `offset` und `relativeStory` für Geschossbindungen (-1 darunter, 0 aktuell, 1 darüber).

Nur gültige Bindungen haben `resolvedElevation`, wobei die Semantik des übergeordneten Containers in Vectorworks gilt; für fehlende Referenzen wird niemals eine Ersatzhöhe ausgegeben. Fehlende Bindungen bedeuten nicht, dass geometrische Höhen fehlen. Diese Bindungsebenen sind weder ein Geschosskatalog noch absolute Geschosskennungen (getStories der Gruppe Document listet die Geschosse und deren Ebenen auf). Alle Längenwerte in `heightDetails` werden in Welteinheiten angegeben; verwende `convertUnits` für Anzeigeeinheiten.

Der optionale Parameter `includeOpening` (Standardwert false) ergänzt für Türen und Fenster ein Objekt `opening`: `capability` (operable|fixed|notApplicable|unknown); `config` (Konfigurations-Popup bei Fenstern, unverändert) oder `configuration` (Konfigurations-Popup bei Türen, unverändert); `operation` (SwingOperation der Tür bei Swing-Konfiguration; CasementOperation, FixedGlassOperation oder HungOperation des Fensters für seine Konfiguration); `hingeSide` aus Sicht von außen (Tür-Swing; Fenster-Casement und Tilt/Turn); `openDirection` (Tür-Swing; Fenster-Awning, Casement, Hopper und Tilt/Turn; Vertical Pivot gibt stattdessen `outwardSide` aus); `hingeDirection` (Fenster), `interiorSide`, `flipped`, `show3DOpen` und `openAngleParameter` als unveränderte Werte sowie `legacyOperation` (Türen: das veraltete Operation-Popup, ersetzt durch `operation`).

Richtungsparameter werden nur ausgegeben, wenn sie für die Konfiguration gelten. `opensToward` ist für eine einflügelige Tür mit Swing sowie für geprüfte Fensteröffnungen (Awning, Hopper, Tilt/Turn, einflügelige Casement) anhand des In/Out-Werts interior oder exterior (In ist die Innenseite, Out die Außenseite). Vertical Pivot bedeutet beide Seiten; Opening, Cased Opening und Fixed Glass sind nicht zutreffend; andere Öffnungen sind unbekannt.

Der gezeichnete Öffnungswinkel wird getrennt von der Funktion ausgegeben. Die Tür-Eigenschaft `config` liest jetzt das Konfigurations-Popup aus.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `uuid` | string |  | Referenz über UUID (bevorzugt). Siehe [Objektreferenzen](Common.md#objektreferenzen). |
| `name` | string |  | Referenz über Namen. |
| `index` | integer |  | Referenz über internen Index. |
| `includeHeightDetails` | boolean |  | Standardwert: `false`. |
| `includeOpening` | boolean |  | Standardwert: `false`. |
| `params` | array of string |  | Namen der Plug-in-Parameter, die mit typisierten Werten ausgegeben werden sollen. Siehe [Plug-in-Parameter](Common.md#plug-in-parameter). |

**Ergebnis**

| Typ | Schlüssel |
|---|---|
| `Wall` | `start`, `end` ([Punkte](Common.md#punkte)), `length`, `angle` (Radiant), `startTop`, `startBottom`, `endTop`, `endBottom` (Welteinheiten), `style` (interner Index des Wandstils), `caps` (`{ leftCap, rightCap, round }`), `isCurtainWall` sowie `heightDetails`, wenn `includeHeightDetails` angegeben wurde. |
| `Slab` | `height`, `style` (interner Index; `0` bedeutet ohne Stil), `styleName` (nur wenn `style` nicht `0` ist) und `params`, wenn angefordert. |
| `Roof` | `edgeCount`, `edges`, `roofThickness`, `bearingInset`, `generateGableWalls`, `verticalMiter`, `miterType`. |
| `Door` | `opening` (mit `includeOpening`), `width`, `height`, `sizeReference`, `leafWidth`, `leafHeight`, `config`, `idLabel`, `thickness`, `topShape`, `leafType`, `onSchedule` und `params`, wenn angefordert. |
| `Window` | `opening` (mit `includeOpening`), `width`, `height`, `sizeReference`, `unitWidth`, `unitHeight`, `elevation`, `headHeight`, `elevationSetAt`, `idLabel`, `sashOperation`, `topShape`, `jambWidth`, `jambDepth`, `includeSill`, `sillStyle`, `onSchedule`, `description` und `params`, wenn angefordert. |
| `Column` | `shape`, `height`, `width`, `depth`, `diameter` (nur für einen `Oval`-Schaft, dessen Breite seiner Tiefe entspricht) sowie `params`, wenn angefordert. |
| `Stair` | `width` (erste Treppenbreite), `totalRise`, `totalRun`, `numRisers`, `treadDepth`, `riserHeight` und `params`, wenn angefordert. `numTreads`, `configuration`, `handrailLeft` und `handrailRight` werden nie gemeldet. |


### setArchitectureObject

Bearbeitet eine Wand, einen Boden/eine Decke, ein Dach, eine Tür, ein Fenster, eine Stütze oder Treppe.

> **Auswirkung:** Bearbeitung · **Sicherheit:** mittel · **Rückgängig:** ein Schritt „MCP: setArchitectureObject“ · **In runToolBatch:** ja

**Details**

Bearbeitet eine Wand, einen Boden/eine Decke, ein Dach, eine Tür, ein Fenster, eine Stütze oder Treppe anhand ihrer UUID. Gib die für den Objekttyp relevanten Felder mit den Schlüsseln und Werten an, die `getArchitectureObject` ausgibt; `applied` meldet für jede Änderung true/false.

**Wände:** `thickness`, `start` / `end`, `topHeight` / `bottomHeight` (beide Enden), `startTop` / `startBottom` / `endTop` / `endBottom` (Höhen einzelner Endpunkte, z. B. für eine geneigte Wand; werden als `endHeights` angewendet), `style` (interner Index eines Wandstils; ein anderer Wert wird als false gemeldet und nicht geschrieben), Endkappen { leftCap, rightCap } (runde Endkappen werden nicht mehr unterstützt), `isCurtainWall` sowie `topBound` / `bottomBound` wie bei `createWall`. Die Bindungen werden nach den anderen Werten angewendet: Jede verschiebt das Wandende um die Änderung ihrer Bindungshöhe (wie in der Infopalette), daher können sie nicht in einem Aufruf mit den Höhen kombiniert werden. Eine für die Wand nicht mögliche Bindung lässt den Aufruf fehlschlagen, ohne Änderungen vorzunehmen.

**Böden/Decken:** `style` wie bei `createSlab` (Boden-/Deckenstilname oder UUID seiner Ressource: Ist der Wert kein Boden-/Deckenstil der Zeichnung, wird der Aufruf abgelehnt und nichts geändert; alternativ interner Index: 0 entfernt den Stil, wobei Komponenten erhalten bleiben; ein Index, der keinem Boden-/Deckenstil der Zeichnung entspricht, wird als false gemeldet und nicht geschrieben) und `height` (nur Plug-in-Objekt `Slab`; false bei einem älteren Bodenplatten-Knoten), in dieser Reihenfolge.

**Dächer:** `generateGableWalls`, `bearingInset`, `roofThickness` (wird ignoriert, wenn das Dach Komponenten enthält), `miterType` (vertical|horizontal|double) und `verticalMiter`, gemeinsam als `attributes` angewendet; `accessories` { insertAttic, insertSoffit, insertFascia, fasciaWidth, fasciaHeight, atticHeight, recess, rakeThickness, trimDepth (Längen in Welteinheiten) } kann nicht ausgelesen werden und wird als Ganzes geschrieben: fehlende Elemente werden zu false/0. `edges` ersetzt den Dachumriss durch mindestens 3 Einträge in der von `getArchitectureObject` ausgegebenen Reihenfolge: Bei nicht angegebenen Elementen eines Eintrags bleiben die Werte der aktuellen Kante an dieser Position erhalten (ein Eintrag hinter den aktuellen Kanten erfordert `point` und `slope`); jede Neigung muss 2 bis 90 Grad betragen (Vectorworks erstellt ein Dach nur bei Kantenneigungen von 2 bis 90 Grad), und ein ungültiger Eintrag führt zur Ablehnung des Aufrufs, ohne Änderungen vorzunehmen. Unveränderte Kanten werden nicht erneut geschrieben, weitere Kanten werden angefügt und überzählige Kanten zusammen mit den daran befindlichen Dachgauben und Oberlichtern vom Ende entfernt. Es wird nichts geschrieben, wenn ein Punkt mit dem nächsten übereinstimmt oder mit seinen beiden Nachbarn auf einer Linie liegt (Vectorworks entfernt solche Punkte). Die Anwendung erfolgt als `edges`; true bedeutet, dass das Dach genau mit diesen Punkten, Neigungen und Projektionen endet (Vectorworks kann die Traufhöhe einer Giebelkante auf die Höhe erhöhen, auf der ihre Nachbarkanten aufliegen).

**Türen:** `width`, `height` und `sizeReference` (leaf|unit|roughOpening) wie bei `createDoor`, zuerst und in der Reihenfolge `sizeReference`, `width`, `height`, anschließend `thickness` (Türblatt), `config`, `topShape`, `leafType` (Solid|Glass|Panel|Custom), `onSchedule`, `idLabel`.

**Fenster:** `width`, `height`, `sizeReference` (sash|unit|roughOpening) und `elevation` (Brüstungshöhe) wie bei `createWindow`, zuerst und in der Reihenfolge `sizeReference`, `width`, `height`, `elevation` (ohne `elevation` behält das Fenster seine gespeicherte Elevation bei; bei Head of Window verschiebt sich also mit einer neuen Höhe auch die Brüstung), anschließend `topShape`, `sashOperation` (veraltet), `jambWidth`, `jambDepth`, `includeSill`, `sillStyle` (Timber|Masonry|Brick|Open Profile Beside Frame|Open Profile Below Frame|Closed Profile), `onSchedule`, `idLabel`, `description`. Ein durch den Plug-in-Stil des Tür- oder Fensterobjekts festgelegter Wert führt zur Ablehnung des Aufrufs, ohne Änderungen vorzunehmen; ein Wert, der dem aktuellen entspricht, wird nicht erneut geschrieben. `topShape` ist Square|Round|Segment|Sloped from Left|Sloped from Right|Gable|Ellipse|Gothic; bei Fenstern werden außerdem Half Round, Half Segment, Half Ellipse und Half Gothic akzeptiert, jeweils gefolgt von ' from Left' oder ' from Right'.

**Stützen:** `shape`, `height`, `width`, `depth`, `diameter`.

**Treppen (Stairs CW):** positive Werte für `totalRise`, `totalRun` (Lauflänge), `treadDepth`, `riserHeight` und `numRisers` (1-32767), die die Treppe nach der Bearbeitung beim Zurücksetzen anwendet und dabei abhängige Werte neu berechnet (lies diese erneut aus). `width`, `numTreads`, `configuration`, `handrailLeft` und `handrailRight` können nicht festgelegt werden (für `applied` wird false gemeldet). Ein Objekt `params` legt unveränderte Plug-in-Parameter fest (reelle Zahlen in Welteinheiten, wie `params` von `getArchitectureObject` sie ausgibt).

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `uuid` | string |  | Referenz über UUID (bevorzugt). Siehe [Objektreferenzen](Common.md#objektreferenzen). |
| `name` | string |  | Referenz über Namen. |
| `index` | integer |  | Referenz über internen Index. |
| `thickness` | number |  | Für Wände und Türen. Wandstärke in Welteinheiten. |
| `start` | [Punkt](Common.md#punkte) |  | Für Wände. Anfangspunkt. |
| `end` | [Punkt](Common.md#punkte) |  | Für Wände. Endpunkt. |
| `topHeight` | number |  | Für Wände. |
| `bottomHeight` | number |  | Für Wände. Beide Enden. |
| `style` | integer or string |  | Für Wände und Böden/Decken. |
| `height` | number |  | Für Böden/Decken (Höhe des Bezugs), Türen, Fenster und Stützen. In Welteinheiten. |
| `width` | number |  | Für Türen, Fenster und Stützen. Breite in Welteinheiten. |
| `sizeReference` | string |  | Für Türen und Fenster. Einer von: `leaf`, `unit`, `roughOpening`, `sash`. |
| `config` | string |  | Für Türen. |
| `idLabel` | string |  | Für Türen und Fenster. |
| `elevation` | number |  | Für Fenster. Die Brüstungshöhe. |
| `shape` | string |  | Für Stützen. |
| `depth` | number |  | Für Stützen. Tiefe in Welteinheiten. |
| `diameter` | number |  | Für Stützen. Durchmesser in Welteinheiten. |
| `totalRise` | number |  | Für Treppen (Stairs CW). |
| `totalRun` | number |  | Für Treppen (Stairs CW). Lauflänge. |
| `treadDepth` | number |  | Für Treppen (Stairs CW). |
| `riserHeight` | number |  | Für Treppen (Stairs CW). |
| `startTop` | number |  | Für Wände. |
| `startBottom` | number |  | Für Wände. |
| `endTop` | number |  | Für Wände. |
| `endBottom` | number |  | Für Wände. Höhen einzelner Endpunkte, z. B. für eine geneigte Wand; wird als `endHeights` angewendet. |
| `caps` | object |  | Für Wände. |
| `caps.leftCap` | boolean |  | Gibt an, ob das Anfangsende der Wand geschlossen ist. |
| `caps.rightCap` | boolean |  | Gibt an, ob das Endende der Wand geschlossen ist. |
| `isCurtainWall` | boolean |  | Für Wände. |
| `topBound` | object |  | Für Wände. |
| `topBound.kind` | string | Ja | Einer von: `story`, `layerElevation`, `layerWallHeight`. |
| `topBound.levelType` | string |  | Geschosstyp. Für `kind` `story` erforderlich und darf nicht leer sein; bei Ebenentypen wird er ignoriert. Ein Wert, der keine Zeichenfolge ist, führt bei allen Typen zur Ablehnung des Aufrufs. |
| `topBound.relativeStory` | integer |  | Einer von: `-1`, `0`, `1`. Standardwert: `0`. |
| `topBound.offset` | number |  | Standardwert: `0`. |
| `bottomBound` | object |  | Für Wände. |
| `bottomBound.kind` | string | Ja | Einer von: `story`, `layerElevation`, `layerWallHeight`. |
| `bottomBound.levelType` | string |  | Geschosstyp. Für `kind` `story` erforderlich und darf nicht leer sein; bei Ebenentypen wird er ignoriert. Ein Wert, der keine Zeichenfolge ist, führt bei allen Typen zur Ablehnung des Aufrufs. |
| `bottomBound.relativeStory` | integer |  | Einer von: `-1`, `0`, `1`. Standardwert: `0`. |
| `bottomBound.offset` | number |  | Standardwert: `0`. |
| `generateGableWalls` | boolean |  | Für Dächer. |
| `bearingInset` | number |  | Für Dächer. |
| `roofThickness` | number |  | Für Dächer. Wird ignoriert, wenn das Dach Komponenten enthält. |
| `miterType` | string |  | Für Dächer. Einer von: `vertical`, `horizontal`, `double`. |
| `verticalMiter` | number |  | Für Dächer. |
| `accessories` | object |  | Für Dächer. |
| `accessories.insertAttic` | boolean |  | Gibt an, ob ein Dachraum eingefügt werden soll. |
| `accessories.insertSoffit` | boolean |  | Gibt an, ob eine Untersicht eingefügt werden soll. |
| `accessories.insertFascia` | boolean |  | Gibt an, ob ein Traufbrett eingefügt werden soll. |
| `accessories.fasciaWidth` | number |  | Breite des Traufbretts in Welteinheiten. |
| `accessories.fasciaHeight` | number |  | Höhe des Traufbretts in Welteinheiten. |
| `accessories.atticHeight` | number |  | Höhe des Dachraums in Welteinheiten. |
| `accessories.recess` | number |  | Rücksprung in Welteinheiten. |
| `accessories.rakeThickness` | number |  | Dicke des Ortgangs in Welteinheiten. |
| `accessories.trimDepth` | number |  | Tiefe der Verkleidung in Welteinheiten. |
| `edges` | array of object |  | Mindestens 3 Einträge. |
| `edges[].point` | [Punkt](Common.md#punkte) |  | Punkt der Dachkontur. Wird er bei einem Element ausgelassen, bleibt der Punkt der aktuellen Kante an dieser Position erhalten; ein Element hinter den aktuellen Kanten benötigt `point` und `slope`. |
| `edges[].slope` | number |  | Grad, 2 bis 90. Minimum: `2`. Maximum: `90`. |
| `edges[].projection` | number |  | Dachüberstand an der Traufe in Welteinheiten. Wird der Wert ausgelassen, bleibt der aktuelle Wert erhalten. |
| `edges[].eaveHeight` | number |  | Traufhöhe relativ zur Ebenenhöhe, in Welteinheiten. Wird der Wert ausgelassen, bleibt der aktuelle Wert erhalten. |
| `topShape` | string |  | Für Türen und Fenster. |
| `leafType` | string |  | Für Türen. Einer von: `Solid`, `Glass`, `Panel`, `Custom`. |
| `onSchedule` | boolean |  | Für Türen und Fenster. |
| `sashOperation` | string |  | Für Fenster. Veraltet. |
| `jambWidth` | number |  | Für Fenster. |
| `jambDepth` | number |  | Für Fenster. |
| `includeSill` | boolean |  | Für Fenster. |
| `sillStyle` | string |  | Für Fenster. Einer von: `Timber`, `Masonry`, `Brick`, `Open Profile Beside Frame`, `Open Profile Below Frame`, `Closed Profile`. |
| `description` | string |  | Für Fenster. Beschreibungstext. |
| `numTreads` | integer |  | Treppen: kann nicht festgelegt werden (wird als nicht angewendet gemeldet). |
| `numRisers` | integer |  | Für Treppen (Stairs CW). 1-32767. |
| `configuration` | string |  | Treppen: kann nicht festgelegt werden (wird als nicht angewendet gemeldet). |
| `handrailLeft` | boolean |  | Treppen: kann nicht festgelegt werden (wird als nicht angewendet gemeldet). |
| `handrailRight` | boolean |  | Treppen: kann nicht festgelegt werden (wird als nicht angewendet gemeldet). |
| `params` | object |  | Unveränderte Plug-in-Parameter `{ "ParamName": value }`. Siehe [Plug-in-Parameter](Common.md#plug-in-parameter). |

**Ergebnis**

| Typ | Schlüssel von `applied` |
|---|---|
| Wall | `thickness`; `line` (`start` and `end`, only when both are given); `heights` (`topHeight` and `bottomHeight`); `style`; `endHeights` (`startTop`, `startBottom`, `endTop` and `endBottom`); `caps`; `isCurtainWall`; `topBound`; `bottomBound` |
| Slab | `style`; `height` |
| Roof | `attributes` (`generateGableWalls`, `bearingInset`, `roofThickness`, `miterType` and `verticalMiter` together); `accessories`; `edges` |
| Door | `sizeReference`; `width`; `height`; `config`; `idLabel`; `thickness`; `topShape`; `leafType`; `onSchedule` |
| Window | `sizeReference`; `width`; `height`; `elevation`; `idLabel`; `topShape`; `sashOperation`; `jambWidth`; `jambDepth`; `includeSill`; `sillStyle`; `onSchedule`; `description` |
| Column | `shape`; `height`; `width`; `depth`; `diameter` |
| Stair | `totalRise`; `totalRun`; `treadDepth`; `riserHeight`; `numRisers`; and, always `false`, `width`, `numTreads`, `configuration`, `handrailLeft`, `handrailRight` |

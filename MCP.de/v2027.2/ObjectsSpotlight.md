[English](../../MCP/v2027.2/ObjectsSpotlight.md) • **Deutsch** • [日本語](../../MCP.ja/v2027.2/ObjectsSpotlight.md)

# ObjectsSpotlight — Beleuchtungsgeräte und GDTF-Scheinwerfertypen

> **Server:** Vectorworks MCP · **Version:** Vectorworks 2027 Update 2

[Zurück zum Inhaltsverzeichnis](README.md)

Werkzeuge für Spotlight-Beleuchtungsgeräte und die von ihnen verwendeten GDTF-Scheinwerfertypen (General Device Type Format).

## Inhaltsverzeichnis

- [Überblick](#überblick)
- [Spotlight](#spotlight)
  - [listGDTFs](#listgdtfs)
  - [importGDTF](#importgdtf)
  - [createLightingDevice](#createlightingdevice)
  - [getLightingDevice](#getlightingdevice)
  - [setLightingDevice](#setlightingdevice)

## Überblick

Dieser Ordner enthält 1 Werkzeuggruppe mit insgesamt 5 Werkzeugen.

| Gruppe | Gruppen-ID | Standardmäßig aktiv | Sicherheitsstufe | Werkzeuge | Zusammenfassung |
|---|---|---|---|---|---|
| [Spotlight](#spotlight) | `spotlight` | Nein | mittel | 5 | Spotlight-Beleuchtungsgeräte und die von ihnen verwendeten GDTF-Scheinwerfertypen. |

## Spotlight

> **Gruppe:** `Spotlight` · **Gruppen-ID:** `spotlight` · **Standardmäßig aktiv:** Nein · **Sicherheitsstufe:** mittel · **Werkzeuge:** 5

**Spotlight-Beleuchtungsgeräte und die von ihnen verwendeten GDTF-Scheinwerfertypen.**

Spotlight-Beleuchtungsgeräte und die von ihnen verwendeten GDTF-Scheinwerfertypen (General Device Type Format) erstellen, anzeigen und bearbeiten: verfügbare GDTF-Scheinwerfertypen und ihre DMX-Modi auflisten, eine .gdtf-Datei in die Zeichnung importieren, ein Beleuchtungsgerät mit einem GDTF-Scheinwerfertyp, DMX-Modus und 3D-Modell erstellen sowie das Gerät auslesen oder ändern. Ein GDTF-Scheinwerfertyp wird über seinen `gdtfName` angesprochen, wie ihn `listGDTFs` ausgibt; ein Beleuchtungsgerät kann nur einen Scheinwerfertyp verwenden, der sich in der Zeichnung befindet (`isInDocument`); importiere daher zuerst eine .gdtf-Datei.

Jede Änderung wird als eigener benannter, rückgängig machbarer Vectorworks-Vorgang ausgeführt.

| Werkzeug | Auswirkung | Sicherheit | Zusammenfassung |
|---|---|---|---|
| [`listGDTFs`](#listgdtfs) | Nur lesend | niedrig | Listet die verfügbaren GDTF-Scheinwerfertypen und ihre DMX-Modi auf. |
| [`importGDTF`](#importgdtf) | Bearbeitung | mittel | Importiert eine .gdtf-Datei als GDTF-Scheinwerfertyp in die Zeichnung. |
| [`createLightingDevice`](#createlightingdevice) | Bearbeitung | mittel | Erstellt ein Beleuchtungsgerät, optional mit einem GDTF-Scheinwerfertyp. |
| [`getLightingDevice`](#getlightingdevice) | Nur lesend | niedrig | Liest ein Beleuchtungsgerät aus. |
| [`setLightingDevice`](#setlightingdevice) | Bearbeitung | mittel | Bearbeitet ein Beleuchtungsgerät. |

### listGDTFs

Listet die verfügbaren GDTF-Scheinwerfertypen und ihre DMX-Modi auf.

> **Auswirkung:** Nur lesend · **Sicherheit:** niedrig · **Rückgängig:** keiner · **In runToolBatch:** zulässig

**Details**

Listet die für Spotlight verfügbaren GDTF-Scheinwerfertypen auf, einen Eintrag pro DMX-Modus: `gdtfName` (an `createLightingDevice` / `setLightingDevice` übergeben), `fixtureName` (mit „@&lt;revision&gt;“, wenn die Datei eine Revision hat), `manufacturer`, `mode`, `footprint` (DMX-Kanäle) und `isInDocument` (in die Zeichnung importiert; dann auch `symbolDefinitionUuid`). Scheinwerfertypen in der Zeichnung erscheinen zuerst, danach die .gdtf-Dateien in den Spotlight-GDTF-Ordnern, die Spotlight einmal pro Sitzung einliest. Nur Scheinwerfertypen in der Zeichnung können einem Beleuchtungsgerät zugewiesen werden – importiere eine Datei mit `importGDTF`.

Optionale Filter: `manufacturer` und `search` (Teile des Herstellernamens / Scheinwerfer- oder GDTF-Namens, ohne Beachtung der Groß-/Kleinschreibung) sowie `documentOnly`. Seitennavigation über `limit` (Standardwert 200) und `offset`; `countOnly` gibt nur die Anzahl zurück.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `manufacturer` | string |  | Teil des Herstellernamens. Groß-/Kleinschreibung wird nur bei ASCII-Buchstaben ignoriert. |
| `search` | string |  | Teile des Hersteller-, Scheinwerfer- oder GDTF-Namens, ohne Beachtung der Groß-/Kleinschreibung. |
| `documentOnly` | boolean |  | Nur Fixture-Typen, die in die Zeichnung importiert wurden (`isInDocument` ist `true`). Standard `false`. |
| `limit` | integer |  | Seitennavigation: maximale Anzahl zurückzugebender Elemente (mindestens 1). Siehe [Seitennavigation](Common.md#seitennavigation). |
| `offset` | integer |  | Seitennavigation: Anzahl der zu überspringenden Elemente (Standardwert 0). |
| `countOnly` | boolean |  | Seitennavigation: Gibt nur die Anzahl, nicht die Elemente zurück. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `gdtfName` | Name, der an `createLightingDevice` und `setLightingDevice` übergeben wird. |
| `fixtureName` | Name des Fixtures, ergänzt um `@<revision>`, wenn die Datei eine Revision enthält. |
| `manufacturer` | Hersteller. |
| `mode` | DMX-Modus dieses Eintrags. |
| `footprint` | Anzahl der DMX-Kanäle des Modus. |
| `isInDocument` | `true`, wenn der Fixture-Typ in die Zeichnung importiert wurde. |
| `symbolDefinitionUuid` | UUID der Symboldefinition des Fixture-Typs. Nur wenn `isInDocument` `true` ist. |


### importGDTF

Importiert eine .gdtf-Datei als GDTF-Scheinwerfertyp in die Zeichnung.

> **Auswirkung:** Bearbeitung · **Sicherheit:** mittel · **Rückgängig:** ein Schritt „MCP: importGDTF“ · **In runToolBatch:** ja

**Details**

Importiert die .gdtf-Datei unter `filePath` (vollständiger nativer Pfad) als GDTF-Scheinwerfertyp (eine Symboldefinition im GDTF-Ressourcenordner) in die Zeichnung. Gibt deren Referenz und `gdtfName` zurück. Es wird nie eine Rückfrage gestellt: Ein Scheinwerfertyp mit derselben GDTF-Typ-ID, der sich bereits in der Zeichnung befindet, bleibt erhalten (`isImported` false); eine nicht lesbare Datei führt zu einem Fehler.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `filePath` | string | Ja | Vollständiger nativer Pfad. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `gdtfName` | Name, der an `createLightingDevice` und `setLightingDevice` übergeben wird. |
| `isImported` | `true`. |


### createLightingDevice

Erstellt ein Beleuchtungsgerät, optional mit einem GDTF-Scheinwerfertyp.

> **Auswirkung:** Bearbeitung · **Sicherheit:** mittel · **Rückgängig:** ein Schritt „MCP: createLightingDevice“ · **In runToolBatch:** ja

**Details**

Erstellt an `position` ein Spotlight-Beleuchtungsgerät (ohne Beleuchtungssymbol), gedreht um `angle` (Radiant). Ein optionaler `gdtfName` (ein Scheinwerfertyp in der Zeichnung, aus `listGDTFs` oder `importGDTF`) mit `mode` (DMX-Modus; wenn nicht angegeben, wird der erste Modus verwendet) weist dem Gerät wie beim Ablegen aus dem Ressourcen-Manager einen GDTF-Scheinwerfertyp zu und zeichnet anschließend dessen 3D-Modell, sofern `useGdtfGeometry` nicht false ist.

Optional sind `instrumentType` und rohe `params`. `applied` meldet für jede Einstellung, ob sie geschrieben wurde; `gdtf` false bedeutet, dass die Zeichnung keinen Scheinwerfertyp mit diesem `gdtfName` und `mode` enthält und das Gerät seine GDTF-Einstellungen beibehält; `mode` false bedeutet, dass ein Modus ohne `gdtfName` angegeben wurde.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `position` | [Punkt](Common.md#punkte) | Ja | Einfügepunkt. |
| `angle` | number |  | Winkel in Radiant, gegen den Uhrzeigersinn. |
| `gdtfName` | string |  | Ein Scheinwerfertyp in der Zeichnung, aus `listGDTFs` oder `importGDTF`. |
| `mode` | string |  | DMX-Modus; wenn nicht angegeben, wird der erste Modus verwendet. |
| `useGdtfGeometry` | boolean |  | 3D-Modell des GDTF-Fixture-Typs zeichnen. Standard `true`, nachdem `gdtfName` angewendet wurde. Muss ein JSON-Boolean sein; jeder andere Wert wird als `true` geschrieben. |
| `instrumentType` | string |  | Spotlight-Instrumententyp (Parameter `Inst Type` des Geräts). |
| `params` | object |  | Rohe Plug-in-Parameter { "ParamName": value } (siehe `getObjectParameters`). |
| `class` | string |  | Erstellungsoption: Klasse des neuen Objekts; wird bei Bedarf erstellt. Siehe [Erstellungsoptionen](Common.md#optionen-zur-erstellung). |
| `name` | string |  | Erstellungsoption: Name des neuen Objekts. |
| `select` | boolean |  | Erstellungsoption: Neues Objekt auswählen. |
| `useClassAttributes` | boolean |  | Erstellungsoption: Mit `class` auch die Attribute des neuen Objekts anhand der Klasse festlegen. |

**Ergebnis**

Objektreferenz des neuen Beleuchtungsgeräts (siehe [Objektreferenzen](Common.md#objektreferenzen)) und, nur wenn eine Einstellung angegeben wurde, `applied` (siehe [Angewendete Einstellungen](Common.md#angewendete-einstellungen)). Die Schlüssel sind `gdtf` und `mode` (wie oben beschrieben), `useGdtfGeometry`, `instrumentType` und `params`. Ein Schlüssel ist nur vorhanden, wenn die zugehörige Einstellung angegeben wurde, außer: Bei `gdtfName` umfasst `gdtf` auch `mode`, und es gibt keinen Schlüssel `mode` (`mode` erscheint immer mit `false` nur ohne `gdtfName`); `useGdtfGeometry` ist auch vorhanden, nachdem `gdtfName` angewendet wurde; `params` nur, wenn es ein Objekt ist. Ein `useGdtfGeometry`, das kein Boolean ist, gilt als `true`; ein `instrumentType`, das keine Zeichenfolge ist, schreibt leeren Text; beide melden `true`. Der Eintrag `params` ist ein Objekt mit `true` oder `false` für jeden Parameternamen.

Fehler: `failed to create the lighting device (is Spotlight installed?)`. Ein fehlgeschlagener Aufruf wird zurückgerollt (`rolledBack`).


### getLightingDevice

Liest ein Beleuchtungsgerät aus.

> **Auswirkung:** Nur lesend · **Sicherheit:** niedrig · **Rückgängig:** keiner · **In runToolBatch:** zulässig

**Details**

Liest ein Beleuchtungsgerät anhand von UUID, Namen oder Index aus: `instrumentType`, `symbolName`, den GDTF-Scheinwerfertyp `gdtfName` und DMX-`mode`, `dmxFootprint`, `useGdtfGeometry` und `bounds`. Der optionale Parameter `params` listet Plug-in-Parameternamen auf (siehe `getObjectParameters`), die als typisierte Rohwerte ausgegeben werden sollen.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `uuid` | string |  | Referenz über UUID (bevorzugt). Siehe [Objektreferenzen](Common.md#objektreferenzen). |
| `name` | string |  | Referenz über Namen. |
| `index` | integer |  | Referenz über internen Index. |
| `params` | array of string |  | Namen der Plug-in-Parameter, die mit typisierten Werten ausgegeben werden sollen. Siehe [Plug-in-Parameter](Common.md#plug-in-parameter). |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `instrumentType` | Spotlight-Instrumententyp (Parameter `Inst Type`). |
| `symbolName` | Name des Beleuchtungssymbols (Parameter `Symbol Name`). |
| `gdtfName` | GDTF-Fixture-Typ, wie von `listGDTFs` gemeldet. |
| `mode` | DMX-Modusname, wie von `listGDTFs` gemeldet. |
| `dmxFootprint` | Anzahl der DMX-Kanäle (Parameter `Num Channels`). |
| `useGdtfGeometry` | Gibt an, ob das 3D-Modell des GDTF-Fixture-Typs gezeichnet wird. |
| `bounds` | Begrenzungsrahmen des Geräts als [Rechteck](Common.md#rechtecke) in Welteinheiten. |
| `params` | Nur wenn `params` angegeben wurde: Objekt mit dem typisierten Wert jedes angefragten Parameters, den das Gerät besitzt. Unbekannte Namen werden ausgelassen. |


### setLightingDevice

Bearbeitet ein Beleuchtungsgerät.

> **Auswirkung:** Bearbeitung · **Sicherheit:** mittel · **Rückgängig:** ein Schritt „MCP: setLightingDevice“ · **In runToolBatch:** ja

**Details**

Bearbeitet ein Beleuchtungsgerät anhand von UUID, Namen oder Index: `gdtfName` (ein Scheinwerfertyp in der Zeichnung) mit `mode` weist einen GDTF-Scheinwerfertyp zu (und aktiviert nach erfolgreicher Zuweisung sein 3D-Modell, sofern `useGdtfGeometry` nicht false ist); außerdem lassen sich `useGdtfGeometry`, `instrumentType` und rohe `params` festlegen. Das Gerät wird neu generiert; `applied` meldet für jede Einstellung, ob sie geschrieben wurde.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `uuid` | string |  | Referenz über UUID (bevorzugt). Siehe [Objektreferenzen](Common.md#objektreferenzen). |
| `name` | string |  | Referenz über Namen. |
| `index` | integer |  | Referenz über internen Index. |
| `gdtfName` | string |  | Ein Scheinwerfertyp in der Zeichnung. |
| `mode` | string |  | DMX-Modus des Fixture-Typs, exakt einschließlich Groß-/Kleinschreibung. Wird nur zusammen mit `gdtfName` geschrieben. Wenn nicht angegeben, leer oder keine Zeichenfolge, wird der erste Modus verwendet. |
| `useGdtfGeometry` | boolean |  | 3D-Modell des GDTF-Fixture-Typs zeichnen. Standard `true`, nachdem `gdtfName` angewendet wurde; wird bei Angabe auch ohne `gdtfName` geschrieben. Muss ein JSON-Boolean sein; jeder andere Wert wird als `true` geschrieben. |
| `instrumentType` | string |  | Spotlight-Instrumententyp (Parameter `Inst Type` des Geräts). |
| `params` | object |  | Rohe Plug-in-Parameter { "ParamName": value } (siehe `getObjectParameters`). |

**Ergebnis**

Nur `applied` (siehe [Angewendete Einstellungen](Common.md#angewendete-einstellungen)); es gibt keine Objektreferenz. `applied` ist immer vorhanden, auch wenn es leer ist. Die Schlüssel entsprechen denen von `createLightingDevice`: `gdtf` und `mode`, `useGdtfGeometry`, `instrumentType` und `params`. Ein Schlüssel ist nur vorhanden, wenn die zugehörige Einstellung angegeben wurde, außer: Bei `gdtfName` umfasst `gdtf` auch `mode`, und es gibt keinen Schlüssel `mode` (`mode` erscheint immer mit `false` nur ohne `gdtfName`); `useGdtfGeometry` ist auch vorhanden, nachdem `gdtfName` angewendet wurde; `params` nur, wenn es ein Objekt ist. Ein `useGdtfGeometry`, das kein Boolean ist, gilt als `true`; ein `instrumentType`, das keine Zeichenfolge ist, schreibt leeren Text; beide melden `true`.

Fehler: `object not found`; `not a lighting device`. Das Gerät wird zuerst anhand von `uuid`, dann `name` und anschließend `index` gesucht. Ein fehlgeschlagener Aufruf wird zurückgerollt (`rolledBack`).

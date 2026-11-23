[English](../../MCP/v2027.2/ObjectsConnectCAD.md) • **Deutsch** • [日本語](../../MCP.ja/v2027.2/ObjectsConnectCAD.md)

# ObjectsConnectCAD — ConnectCAD-Schaltplangeräte

> **Server:** Vectorworks MCP · **Version:** Vectorworks 2027 Update 2

[Zurück zum Inhaltsverzeichnis](README.md)

Werkzeuge für ConnectCAD-Schaltplangeräte, ihre Anschlüsse und Gerätetypen sowie die verwendeten Signal- und Steckverbindertypen.

## Inhaltsverzeichnis

- [Überblick](#überblick)
- [ConnectCAD](#connectcad)
  - [listConnectCADSignals](#listconnectcadsignals)
  - [listConnectCADConnectors](#listconnectcadconnectors)
  - [validateConnectCADDevice](#validateconnectcaddevice)
  - [createConnectCADDevice](#createconnectcaddevice)
  - [createConnectCADDevices](#createconnectcaddevices)
  - [getConnectCADDevice](#getconnectcaddevice)
  - [addConnectCADSocket](#addconnectcadsocket)
  - [setConnectCADSocket](#setconnectcadsocket)
  - [createConnectCADDeviceType](#createconnectcaddevicetype)
  - [getConnectCADDeviceType](#getconnectcaddevicetype)

## Überblick

Dieser Ordner enthält 1 Werkzeuggruppe mit insgesamt 10 Werkzeugen.

| Gruppe | Gruppen-ID | Standardmäßig aktiv | Sicherheitsstufe | Werkzeuge | Zusammenfassung |
|---|---|---|---|---|---|
| [ConnectCAD](#connectcad) | `connectcad` | Nein | mittel | 10 | ConnectCAD-Schaltplangeräte, Anschlüsse und Gerätetypen, erstellt anhand von JSON-Gerätebeschreibungen. |

## ConnectCAD

> **Gruppe:** `ConnectCAD` · **Gruppen-ID:** `connectcad` · **Standardmäßig aktiv:** Nein · **Sicherheitsstufe:** mittel · **Werkzeuge:** 10

**ConnectCAD-Schaltplangeräte, Anschlüsse und Gerätetypen, erstellt anhand von JSON-Gerätebeschreibungen.**

ConnectCAD-Schaltplangeräte ohne Skripte erstellen und anzeigen: ein Gerät mit allen Anschlüssen anhand einer JSON-Gerätebeschreibung, Anschlüsse zu einem Gerät hinzufügen oder bearbeiten, Gerätetyp-Symbole (Datensatz „Device Definition“) sowie die zu verwendenden Signal- und Steckverbindertypen. Gerätebeschreibung (ein JSON-Objekt): name, tag, description, make, model, category, width_r (`non-rack` | `half-rack` | `full-rack`), width, height, depth (mm; die Höhe eines Rack-Geräts entspricht einer ganzen Rackeinheit von 44.45 mm), power (W), weight (kg), is_modular (bool), n_slots (int, &gt; 0 nur bei modularen Geräten); name, tag, make, model, width_r, is_modular und n_slots sind erforderlich; „socket groups“: [ { qty (1-50), type, name, signal, connector, orientation, pinout: [ { pinID, name, sourceID } ], extra_data } ].

**Anschlusstypen:** IN, OUT, IO (jeweils ein Anschluss) und LOOP / IOloop (ein Paar „&lt;name&gt;“ + „&lt;name&gt;\_LP“); Ausrichtungen L, R, X (Durchschleifen); LOOP und IOloop nur L oder R; FUSE und BUS sind keine Anschlüsse. Bei qty &gt; 1 werden „&lt;name&gt; 1“ bis „&lt;name&gt; n“ erstellt (Standardnummerierung von ConnectCAD); Anschlussnamen müssen im Gerät eindeutig sein, dürfen kein „+“ enthalten und nicht mit `_LP` enden. Signale und Steckverbinder müssen aus `listConnectCADSignals` / `listConnectCADConnectors` stammen; ein Pinout listet die Pins seines Steckverbinders mit im Gerät eindeutigen `pinID`-Werten auf. Beschreibungen werden zuerst validiert; eine ungültige Beschreibung erstellt nichts. Jede Änderung wird als eigener benannter, rückgängig machbarer Vectorworks-Vorgang ausgeführt.

| Werkzeug | Auswirkung | Sicherheit | Zusammenfassung |
|---|---|---|---|
| [`listConnectCADSignals`](#listconnectcadsignals) | Nur lesend | niedrig | Listet die ConnectCAD-Signaltypen auf. |
| [`listConnectCADConnectors`](#listconnectcadconnectors) | Nur lesend | niedrig | Listet die ConnectCAD-Steckverbindertypen und deren Pins auf. |
| [`validateConnectCADDevice`](#validateconnectcaddevice) | Nur lesend | niedrig | Prüft eine Gerätebeschreibung, ohne etwas zu erstellen. |
| [`createConnectCADDevice`](#createconnectcaddevice) | Bearbeitung | mittel | Erstellt ein Schaltplangerät mit allen Anschlüssen anhand einer Gerätebeschreibung. |
| [`createConnectCADDevices`](#createconnectcaddevices) | Bearbeitung | mittel | Erstellt mehrere Schaltplangeräte hintereinander in einem Vorgang. |
| [`getConnectCADDevice`](#getconnectcaddevice) | Nur lesend | niedrig | Liest ein ConnectCAD-Gerät und seine Anschlüsse aus. |
| [`addConnectCADSocket`](#addconnectcadsocket) | Bearbeitung | mittel | Fügt einem Gerät einen Anschluss hinzu. |
| [`setConnectCADSocket`](#setconnectcadsocket) | Bearbeitung | mittel | Bearbeitet einen Anschluss. |
| [`createConnectCADDeviceType`](#createconnectcaddevicetype) | Bearbeitung | mittel | Erstellt das Gerätetyp-Symbol eines Geräts. |
| [`getConnectCADDeviceType`](#getconnectcaddevicetype) | Nur lesend | niedrig | Liest den Datensatz „Device Definition“ eines Gerätetyp-Symbols aus. |

### listConnectCADSignals

Listet die ConnectCAD-Signaltypen auf.

> **Auswirkung:** Nur lesend · **Sicherheit:** niedrig · **Rückgängig:** keiner · **In runToolBatch:** zulässig

**Details**

Listet die ConnectCAD-Signaltypen auf: `name` (als Anschluss-`signal` verwenden), `category`, `description`, `defaultConnector` und die bevorzugten `connectors`. Optionale Filter: `category` und `search` (Teile, ohne Beachtung der Groß-/Kleinschreibung). Seitennavigation über `limit` (Standardwert 500) und `offset`; `countOnly` gibt nur die Anzahl zurück.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `category` | string |  | Filter: behält Signale, deren Kategorie diesen Text enthält (ohne Beachtung der Groß-/Kleinschreibung). |
| `search` | string |  | Textfilter: Behält Einträge bei, die diesen Text enthalten (ohne Beachtung der Groß-/Kleinschreibung). |
| `limit` | integer |  | Seitennavigation: maximale Anzahl zurückzugebender Elemente (mindestens 1). Siehe [Seitennavigation](Common.md#seitennavigation). |
| `offset` | integer |  | Seitennavigation: Anzahl der zu überspringenden Elemente (Standardwert 0). |
| `countOnly` | boolean |  | Seitennavigation: Gibt nur die Anzahl, nicht die Elemente zurück. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `signals` | Array der Signaltypen (bei `countOnly` ausgelassen): `name`, `category`, `description`, `defaultConnector` und `connectors` (bevorzugte Steckernamen). |


### listConnectCADConnectors

Listet die ConnectCAD-Steckverbindertypen und deren Pins auf.

> **Auswirkung:** Nur lesend · **Sicherheit:** niedrig · **Rückgängig:** keiner · **In runToolBatch:** zulässig

**Details**

Listet die ConnectCAD-Steckverbindertypen auf: `name` (als Anschluss-`connector` verwenden), `localizedName`, `category` und `pins` (die Pinnamen in Reihenfolge für ein `pinout` einer Anschlussgruppe). Optional ist `search`. Seitennavigation über `limit` (Standardwert 500) und `offset`; `countOnly` gibt nur die Anzahl zurück.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `search` | string |  | Textfilter: Behält Einträge bei, die diesen Text enthalten (ohne Beachtung der Groß-/Kleinschreibung). |
| `limit` | integer |  | Seitennavigation: maximale Anzahl zurückzugebender Elemente (mindestens 1). Siehe [Seitennavigation](Common.md#seitennavigation). |
| `offset` | integer |  | Seitennavigation: Anzahl der zu überspringenden Elemente (Standardwert 0). |
| `countOnly` | boolean |  | Seitennavigation: Gibt nur die Anzahl, nicht die Elemente zurück. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `connectors` | Array der Steckertypen (bei `countOnly` ausgelassen): `name`, `localizedName`, `category` und `pins` (Pin-Namen in Reihenfolge). |


### validateConnectCADDevice

Prüft eine Gerätebeschreibung, ohne etwas zu erstellen.

> **Auswirkung:** Nur lesend · **Sicherheit:** niedrig · **Rückgängig:** keiner · **In runToolBatch:** zulässig

**Details**

Prüft eine Gerätebeschreibung, ohne etwas zu erstellen: `isValid`, `errors` (was das Gerät ungültig machen oder zum Fehlschlagen des Plug-ins führen würde) und `warnings` (Daten, die nur in einem Gerätetyp gespeichert werden: category, pinout, extra_data, uuid, source).

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `device` | object or string | Ja | Gerätebeschreibung (siehe Gruppenbeschreibung) als JSON-Objekt oder JSON-Text. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `isValid` | `true`, wenn `errors` leer ist. |
| `errors` | Array von Texten (immer vorhanden): Gründe, aus denen das Gerät ungültig wäre oder das Plug-in fehlschlagen könnte. |
| `warnings` | Array von Texten (immer vorhanden): Daten, die nur im Gerätetyp gespeichert werden. |


### createConnectCADDevice

Erstellt ein Schaltplangerät mit allen Anschlüssen anhand einer Gerätebeschreibung.

> **Auswirkung:** Bearbeitung · **Sicherheit:** mittel · **Rückgängig:** ein Schritt „MCP: createConnectCADDevice“ · **In runToolBatch:** ja

**Details**

Erstellt ein ConnectCAD-Schaltplangerät mit allen Anschlüssen anhand einer Gerätebeschreibung auf der aktiven Ebene; sein Einfügepunkt liegt bei `position`. Wenn `createDeviceType` true ist, wird auch das Gerätetyp-Symbol „&lt;make&gt; &lt;model&gt;“ erstellt, dessen Datensatz „Device Definition“ die vollständige Beschreibung enthält. Gibt das Gerät zurück (`uuid`, `deviceName`, `tag`, `make`, `model`, `rackWidth`, `rackUnits`, `bounds`, Anschlüsse mit `uuid`, `name`, `type`, `signal`, `connector`, `orientation`), außerdem `warnings` und `deviceType`.

Eine ungültige Beschreibung erstellt nichts und gibt `errors` zurück.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `device` | object or string | Ja | Gerätebeschreibung (siehe Gruppenbeschreibung) als JSON-Objekt oder JSON-Text. |
| `position` | [Punkt](Common.md#punkte) |  | Einfügepunkt. |
| `createDeviceType` | boolean |  | `true`: zusätzlich das Symbol des Gerätetyps `&lt;make&gt; &lt;model&gt;` erstellen (Standard `false`). |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `warnings` | Array von Texten, nur bei Warnungen (entspricht den Warnungen von `validateConnectCADDevice`). |
| `deviceType` | Nur bei `createDeviceType` `true`: Ergebnis von [createConnectCADDeviceType](#createconnectcaddevicetype) (`deviceTypeName`, `isCreated`, `isFullDataStored`, `warnings`, `errors`). |


### createConnectCADDevices

Erstellt mehrere Schaltplangeräte hintereinander in einem Vorgang.

> **Auswirkung:** Bearbeitung · **Sicherheit:** mittel · **Rückgängig:** ein Schritt „MCP: createConnectCADDevices“ · **In runToolBatch:** ja

**Details**

Erstellt mehrere ConnectCAD-Geräte anhand eines Arrays mit Gerätebeschreibungen in einem Vorgang, von links nach rechts in einer Reihe, deren Oberkanten auf `origin` liegen; `gap` (Zeichnungseinheiten) gibt den Abstand dazwischen an. `createDeviceTypes` erstellt zusätzlich die Gerätetypen. Alle Beschreibungen werden zuerst validiert: Enthält eine davon Fehler, wird nichts erstellt und `invalid` listet sie nach Index auf.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `devices` | array of object or string | Ja | Jedes Element: Gerätebeschreibung (siehe Gruppenbeschreibung) als JSON-Objekt oder JSON-Text. |
| `origin` | [Punkt](Common.md#punkte) |  | Linke Kante des ersten Geräts und obere Kante aller Geräte (Standard 0, 0). |
| `gap` | number |  | Zeichnungseinheiten. |
| `createDeviceTypes` | boolean |  | `true`: zusätzlich die Symbole der Gerätetypen erstellen (Standard `false`). |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `devices` | Array mit einem Eintrag je Beschreibung in der angegebenen Reihenfolge. Jeder Eintrag entspricht dem Ergebnis von [createConnectCADDevice](#createconnectcaddevice) (Gerät mit `bounds` nach dem Verschieben, `warnings`, `deviceType`) oder enthält `err` und `errors` des nicht erstellten Geräts. |
| `partial` | `true` nur, wenn ein Gerät nicht erstellt wurde. Das Ergebnis enthält dann zusätzlich `err` und der Aufruf wird zurückgerollt: bereits erstellte Geräte werden wieder entfernt, sodass die `uuid`-Werte in `devices` nicht mehr existieren (siehe `rolledBack`). In der Zeichnung bleibt nichts zurück. |


### getConnectCADDevice

Liest ein ConnectCAD-Gerät und seine Anschlüsse aus.

> **Auswirkung:** Nur lesend · **Sicherheit:** niedrig · **Rückgängig:** keiner · **In runToolBatch:** zulässig

**Details**

Liest ein ConnectCAD-Gerät anhand von UUID, Namen oder Index aus: `deviceName`, `tag`, `description`, `make`, `model`, `rackWidth`, `rackUnits`, `isModular`, `slotCount`, `bounds` und dessen Anschlüsse (`uuid`, `name`, `type`, `signal`, `connector`, `orientation`).

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `uuid` | string |  | Referenz über UUID (bevorzugt). Siehe [Objektreferenzen](Common.md#objektreferenzen). |
| `name` | string |  | Referenz über Namen. |
| `index` | integer |  | Referenz über internen Index. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `deviceName` | ConnectCAD-Gerätename (das `name` der Beschreibung). `name` der Referenz ist der Vectorworks-Objektname. |
| `tag`, `description`, `make`, `model` | Text of the device. |
| `rackWidth` | Text: `non-rack`, `half-rack` oder `full-rack`. |
| `rackUnits` | Text: Höhe in Rack-Einheiten oder `---`, wenn die Höhe keine ganze Rack-Einheitenzahl ist oder das Gerät kein Rackgerät ist. |
| `isModular`, `slotCount` | Whether the device is modular, and its number of slots. |
| `bounds` | [Rechteck](Common.md#rechtecke) des Geräts. |
| `sockets` | Array der Anschlüsse: `uuid`, `name`, `type`, `signal`, `connector`, `orientation`. |


### addConnectCADSocket

Fügt einem Gerät einen Anschluss hinzu.

> **Auswirkung:** Bearbeitung · **Sicherheit:** mittel · **Rückgängig:** ein Schritt „MCP: addConnectCADSocket“ · **In runToolBatch:** ja

**Details**

Fügt einem ConnectCAD-Gerät (UUID, Name oder Index) einen Anschluss hinzu: `socketName`, `type` IN | OUT | IO, `signal`, `connector` und `orientation` L | R. Er wird unter den Anschlüssen dieser Seite platziert, und das Gerät wird vergrößert. Schleifen und X-Anschlüsse können nur beim Erstellen des Geräts angelegt werden (`createConnectCADDevice`).

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `uuid` | string |  | Referenz über UUID (bevorzugt). Siehe [Objektreferenzen](Common.md#objektreferenzen). |
| `name` | string |  | Referenz über Namen. |
| `index` | integer |  | Referenz über internen Index. |
| `socketName` | string | Ja | Name des neuen Anschlusses: nicht leer, ohne `+`, nicht mit `_LP` endend und nicht bereits von einem anderen Anschluss des Geräts verwendet. |
| `type` | string | Ja | Einer aus: `IN`, `OUT`, `IO`. |
| `signal` | string | Ja | Ein ConnectCAD-Signaltyp (siehe `listConnectCADSignals`). |
| `connector` | string | Ja | Ein ConnectCAD-Verbindertyp (siehe `listConnectCADConnectors`). |
| `orientation` | string | Ja | `L` oder `R`. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `uuid` | UUID des neuen Anschlusses. |
| `name`, `type`, `signal`, `connector`, `orientation` | The values of the socket, as `getConnectCADDevice` lists them. |


### setConnectCADSocket

Bearbeitet einen Anschluss.

> **Auswirkung:** Bearbeitung · **Sicherheit:** mittel · **Rückgängig:** ein Schritt „MCP: setConnectCADSocket“ · **In runToolBatch:** ja

**Details**

Bearbeitet einen ConnectCAD-Anschluss anhand seiner UUID: `socketName`, `type` (IN | OUT | IO), `signal` und `connector` (aus den ConnectCAD-Listen). Ungültige Werte werden nicht geschrieben; `applied` meldet für jede Einstellung, ob sie geschrieben wurde. Der Anschluss und sein Gerät werden neu generiert.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `uuid` | string | Ja | Referenz über UUID (bevorzugt). Siehe [Objektreferenzen](Common.md#objektreferenzen). |
| `socketName` | string |  | Neuer Name des Anschlusses (siehe Hinweis oben). |
| `type` | string |  | Einer von: `IN`, `OUT`, `IO`. |
| `signal` | string |  | Ein ConnectCAD-Signaltyp (siehe `listConnectCADSignals`). |
| `connector` | string |  | Aus den ConnectCAD-Listen. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `applied` | Für jedes angegebene Feld aus `socketName`, `type`, `signal` und `connector` ein Eintrag: `true`, wenn der Wert geschrieben wurde, andernfalls `false`, wenn er abgelehnt wurde oder keine Zeichenfolge ist. |


### createConnectCADDeviceType

Erstellt das Gerätetyp-Symbol eines Geräts.

> **Auswirkung:** Bearbeitung · **Sicherheit:** mittel · **Rückgängig:** ein Schritt „MCP: createConnectCADDeviceType“ · **In runToolBatch:** ja

**Details**

Erstellt das Gerätetyp-Symbol „&lt;make&gt; &lt;model&gt;“ mit seinem ConnectCAD-Datensatz „Device Definition“ anhand eines Geräts (UUID, Name oder Index). Mit `device` (der Beschreibung, anhand derer das Gerät erstellt wurde) enthält der Datensatz die vollständige Beschreibung (pinout, extra_data, uuid, source, category). Ein Gerätetyp mit diesem Hersteller und Modell, der bereits in der Zeichnung vorhanden ist, bleibt erhalten; ein Gerätetyp aus den ConnectCAD-Bibliotheken wird stattdessen importiert (die Beschreibung wird dann nicht geschrieben).

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `uuid` | string |  | Referenz über UUID (bevorzugt). Siehe [Objektreferenzen](Common.md#objektreferenzen). |
| `name` | string |  | Referenz über Namen. |
| `index` | integer |  | Referenz über internen Index. |
| `device` | object or string |  | Gerätebeschreibung (siehe Gruppenbeschreibung) als JSON-Objekt oder JSON-Text. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `deviceTypeName` | Name `&lt;make&gt; &lt;model&gt;` (leer, wenn Hersteller oder Modell fehlt). |
| `isCreated` | `true`, wenn das Symbol jetzt erstellt wurde; `false`, wenn ein Symbol dieses Namens bereits in der Zeichnung vorhanden war. |
| `isFullDataStored` | `true` nur, wenn die Beschreibung in den Datensatz Device Definition geschrieben wurde. |
| `warnings` | Array von Texten, nur bei Warnungen. |
| `errors` | Array von Texten, nur bei Fehlern. |


### getConnectCADDeviceType

Liest den Datensatz „Device Definition“ eines Gerätetyp-Symbols aus.

> **Auswirkung:** Nur lesend · **Sicherheit:** niedrig · **Rückgängig:** keiner · **In runToolBatch:** zulässig

**Details**

Liest den ConnectCAD-Datensatz „Device Definition“ einer Gerätetyp-Symboldefinition (UUID oder Name) aus: `category`, `type`, `make`, `model`, `rackMounting`, `slotCount` und die analysierten `socketGroups`.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `uuid` | string |  | Referenz über UUID (bevorzugt). Siehe [Objektreferenzen](Common.md#objektreferenzen). |
| `name` | string |  | Referenz über den Namen: Name der Symboldefinition des Gerätetyps. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `category`, `make`, `model` | Text of the Device Definition record. |
| `type` | Text des Datensatzfelds `Type`. Er ersetzt den numerischen `type` der Objektreferenz. |
| `rackMounting` | Text: `non-rack`, `half-rack` oder `full-rack`. |
| `slotCount` | Anzahl der Einschübe als Text. |
| `socketGroups` | Array: geparste `socket groups` des Datensatzes; `[]`, wenn keine vorhanden sind. |

[English](../../MCP/v2027.2/IFC.md) • **Deutsch** • [日本語](../../MCP.ja/v2027.2/IFC.md)

# IFC — IFC-Daten und Data-Manager-Zuordnungen

> **Server:** Vectorworks MCP · **Version:** Vectorworks 2027 Update 2

[Zurück zum Inhaltsverzeichnis](README.md)

Schreibgeschützter Zugriff auf IFC-Daten (Industry Foundation Classes) der Zeichnung: IFC-Entität und Eigenschaftensätze von Objekten, Definitionen von Eigenschaftensätzen sowie IFC-Data-Manager-Zuordnungen des Dokuments.

## Inhaltsverzeichnis

- [Überblick](#überblick)
- [IFC](#ifc)
  - [getObjectIFCData](#getobjectifcdata)
  - [getIFCPsetDefinition](#getifcpsetdefinition)
  - [listIFCPsets](#listifcpsets)
  - [listIFCCustomPsets](#listifccustompsets)
- [IFC Data Mapping](#ifc-data-mapping)
  - [listIFCMappingObjects](#listifcmappingobjects)
  - [getIFCMapping](#getifcmapping)

## Überblick

Dieser Ordner enthält 2 Werkzeuggruppen mit insgesamt 6 Werkzeugen.

| Gruppe | Gruppen-ID | Standardmäßig aktiv | Sicherheitsstufe | Werkzeuge | Zusammenfassung |
|---|---|---|---|---|---|
| [IFC](#ifc) | `ifc` | Ja | low | 4 | Schreibgeschützte IFC-Daten: IFC-Entität und Eigenschaftensätze von Objekten sowie Eigenschaftensatzdefinitionen des Dokuments. |
| [IFC Data Mapping](#ifc-data-mapping) | `ifc-data-mapping` | Nein | low | 2 | Liest IFC-Data-Manager-Zuordnungsdefinitionen des aktiven Dokuments aus. |

## IFC

> **Gruppe:** `IFC` · **Gruppen-ID:** `ifc` · **Standardmäßig aktiv:** Ja · **Sicherheitsstufe:** low · **Werkzeuge:** 4

**Schreibgeschützte IFC-Daten: IFC-Entität und Eigenschaftensätze von Objekten sowie Eigenschaftensatzdefinitionen des Dokuments.**

Schreibgeschützter Zugriff auf IFC-Daten ausschließlich über die IFC-Unterstützungsbibliothek: Objekt-Entitätszuweisung, Eigenschaftensätze, Entitäten und Eigenschaftswerte sowie benutzerdefinierte Eigenschaftensatzdefinitionen. IFC-Werte stammen aus dem Data Manager; diese Gruppe kann sie nicht ändern. Diese Werkzeuge zeigen keine rohen internen IFC-Datensätze direkt an und bearbeiten sie nicht; verwenden Sie sie für IFC-Aufgaben anstelle der allgemeinen Objekt-/Ressourcendatensatzwerkzeuge.

Wenn IFC-Unterstützung nicht verfügbar ist, geben die Werkzeuge einen ausdrücklichen Fehler zurück. getObjectIFCData meldet die IFC-Daten eines Objekts so, wie sie beim IFC-Export berechnet werden. listIFCCustomPsets listet die benutzerdefinierten Eigenschaftensätze des aktiven Dokuments auf und ist die einzige vollständige Prüfung, ob ein benutzerdefinierter Satz vorhanden ist; getIFCPsetDefinition prüft eine einzelne geladene Definition und listIFCPsets deckt einen Entitätstyp ab.

Data-Manager-Zuordnungsdefinitionen befinden sich in der inaktiven Gruppe 'IFC Data Mapping'; verwenden Sie diese nur, wenn der Benutzer nach Datenzuordnungen fragt. Ein fehlgeschlagenes Auslesen ist ein `err`-Ergebnis und bedeutet niemals, dass die Daten nicht vorhanden sind.

| Werkzeug | Auswirkung | Sicherheit | Zusammenfassung |
|---|---|---|---|
| [`getObjectIFCData`](#getobjectifcdata) | Nur lesend | low | Liest die IFC-Daten eines Objekts so aus, wie sie beim IFC-Export berechnet werden. |
| [`getIFCPsetDefinition`](#getifcpsetdefinition) | Nur lesend | low | Liest eine IFC-Eigenschaftensatzdefinition anhand ihres Namens aus. |
| [`listIFCPsets`](#listifcpsets) | Nur lesend | low | Listet die IFC-Eigenschaftensätze auf, die für einen IFC-Entitätstyp gelten. |
| [`listIFCCustomPsets`](#listifccustompsets) | Nur lesend | low | Listet die benutzerdefinierten IFC-Eigenschaftensatzdefinitionen des Dokuments auf. |

### getObjectIFCData

Liest die IFC-Daten eines Objekts so aus, wie sie beim IFC-Export berechnet werden.

> **Auswirkung:** Nur lesend · **Sicherheit:** low · **Rückgängig:** keiner · **In runToolBatch:** zulässig

**Details**

Liest die IFC-Daten des durch `uuid` angegebenen Objekts so aus, wie sie beim IFC-Export anhand der angefügten IFC-Datensätze und der Data-Manager-Zuordnung berechnet werden (einschließlich Werten aus Plug-in-Parametern, Datensätzen, Stilen und Formeln): `hasIFC`, `entity`, `schema`, IFC-`guid`, Entitäts-`attributes` und die exportierten Eigenschaftensätze (`psets`) mit `custom` sowie ihren Eigenschaften (Name, Werttyp, IFC-Typ und gegebenenfalls Wert).

Exporteinstellungen, MVD-Filterung und Ebenen-/Geschosszuordnung werden nicht angewendet. Auch die zusätzlichen Teile, die der IFC-Export für Tür-/Fensterteile, Symboltypen, Treppen und Wandkomponenten schreibt, werden nicht nachgebildet. Ein Eigenschaftensatz wird nur aufgeführt, wenn der Export ihn schreiben würde. Verwenden Sie den gemeldeten `type`/`ifcType`; leiten Sie Typen niemals aus dem Entitätsnamen ab (zum Beispiel IfcSlab).

Das Ergebnis enthält nur den aktuellen Zustand und kann daher nicht zeigen, dass sich ein Wert oder Typ geändert hat.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `uuid` | string | Ja | Referenz anhand der UUID (bevorzugt). Siehe [Objektreferenzen](Common.md#objektreferenzen). |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `object` | Objektreferenz (siehe [Objektreferenzen](Common.md#objektreferenzen)). |
| `hasIFC` | `true`, wenn das Objekt gemäß IFC-Export eine IFC-Entität hat. |
| `scope` | Fester Text, der den Umfang der Daten beschreibt. |
| `attributes` | Attribute der Entität als Eigenschaftenliste (siehe unten); Attribute mit Verweisen auf andere IFC-Instanzen werden ausgelassen. Leer, wenn `hasIFC` `false` ist. |
| `psets` | Exportierte Eigenschaftensätze als Liste; jeder enthält `name`, `custom` und `properties`. `properties` ist eine Eigenschaftenliste (siehe unten). Leer, wenn `hasIFC` `false` ist. |
| `readErrors` | Derzeit immer eine leere Liste. Ein fehlgeschlagener Lesevorgang liefert `err`. |
| `entity` | Name der IFC-Entität. Nur wenn `hasIFC` `true` ist. |
| `schema` | Aktives IFC-Schema: `IFC2x2`, `IFC2x3`, `IFC4` oder `IFC4x3`. Nur wenn `hasIFC` `true` ist. `getDocumentInfo` meldet das IFC4-Schema als `IFC2x4`. |
| `guid` | IFC-GUID. Nur wenn das Objekt eine besitzt. |


### getIFCPsetDefinition

Liest eine IFC-Eigenschaftensatzdefinition anhand ihres Namens aus.

> **Auswirkung:** Nur lesend · **Sicherheit:** low · **Rückgängig:** keiner · **In runToolBatch:** zulässig

**Details**

Liest eine IFC-Eigenschaftensatzdefinition anhand von `name` aus. Gibt zurück, ob sie definiert und benutzerdefiniert ist, sowie ihre Eigenschaftsnamen. Eine fehlende Definition wird ausdrücklich gemeldet und nicht als leeres Ergebnis ausgegeben. `scope` gibt an, wo gesucht wurde: `defined` false bedeutet, dass die IFC-Unterstützungsbibliothek keine Standard- oder benutzerdefinierte Definition dieses Namens enthält; es wird nicht in Datensatzformaten oder Objektdaten gesucht.

Ein ähnlich benannter Eigenschaftensatz oder ein Datensatzformat ist davon verschieden. Um zu prüfen, ob das Dokument einen benutzerdefinierten Eigenschaftensatz enthält, verwenden Sie listIFCCustomPsets.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `name` | string | Ja | Name des Eigenschaftensatzes, zum Beispiel `Pset_WallCommon`. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `name` | Angefragter Name. |
| `scope` | Fester Text, der angibt, wo gesucht wurde. |
| `defined` | `true`, wenn die IFC-Unterstützungsbibliothek eine Definition mit diesem Namen enthält. |
| `custom` | Nur wenn `defined` `true` ist: `true` bei einem benutzerdefinierten Eigenschaftensatz. |
| `propertyNames` | Nur wenn `defined` `true` ist: Namen der Eigenschaften als Liste von Zeichenfolgen. |


### listIFCPsets

Listet die IFC-Eigenschaftensätze auf, die für einen IFC-Entitätstyp gelten.

> **Auswirkung:** Nur lesend · **Sicherheit:** low · **Rückgängig:** keiner · **In runToolBatch:** zulässig

**Details**

Listet die IFC-Eigenschaftensätze auf, die für einen Entitätstyp gelten. `entity` hat standardmäßig den Wert `IfcBuildingElementProxy`. Mit `customOnly` werden ausschließlich benutzerdefinierte Eigenschaftensätze angezeigt. Zurückgegeben werden nur Sätze, die für `entity` gelten, aus dem IFC-Schema und der Data-Manager-Zuordnung dieser Entität; es handelt sich nicht um eine Liste der Eigenschaftensätze des Dokuments. Benutzerdefinierte Sätze des Dokuments erhalten Sie mit listIFCCustomPsets.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `customOnly` | boolean |  | Nur benutzerdefinierte Eigenschaftensätze zurückgeben. Standard: `false`. |
| `entity` | string |  | IFC-Entitätstyp, zum Beispiel `IfcWall`. Standard: `IfcBuildingElementProxy`. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `entity` | Verwendete Entität: Argument `entity` oder `IfcBuildingElementProxy`, wenn es fehlt oder keine Zeichenfolge ist. |
| `customOnly` | Verwendeter Wert. |
| `psets` | Zutreffende Eigenschaftensätze als Liste mit `name` und `custom`. |


### listIFCCustomPsets

Listet die benutzerdefinierten IFC-Eigenschaftensatzdefinitionen des Dokuments auf.

> **Auswirkung:** Nur lesend · **Sicherheit:** low · **Rückgängig:** keiner · **In runToolBatch:** zulässig

**Details**

Listet die benutzerdefinierten IFC-Eigenschaftensatzdefinitionen des aktiven Dokuments samt IFC-Typ jeder Eigenschaft und Angabe auf, ob der Satz aktiviert ist. Fehlt ein Satz in einem erfolgreichen Ergebnis, ist er im Dokument nicht definiert; ein `err`-Ergebnis bedeutet, dass seine Existenz nicht festgestellt werden kann. Keine Argumente erforderlich.

**Parameter**

Dieses Werkzeug benötigt keine Parameter.

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `scope` | Fester Text: `custom property-set definitions of the active document`. |
| `customPsets` | Benutzerdefinierte Eigenschaftensätze als Liste mit `name`, `enabled` und `properties`. `properties` ist eine Liste mit `name`, `ifcType` und `unit`. `unit` ist nur vorhanden, wenn die Eigenschaft eine Einheit hat: `Length`, `Area`, `SolidAngle`, `Mass`, `Time`, `Temperature`, `Luminosity`, `Power`, `ThermalTransmittance`, `Dimension`, `Volume` oder `Angle`. |

Fehler: `IFC support is unavailable in this Vectorworks session` und `the custom property sets of the active document could not be read; presence cannot be determined` (zum Beispiel, wenn die IFC-Daten nicht an das aktive Dokument gebunden sind).


## IFC Data Mapping

> **Gruppe:** `IFC Data Mapping` · **Gruppen-ID:** `ifc-data-mapping` · **Standardmäßig aktiv:** Nein · **Sicherheitsstufe:** low · **Werkzeuge:** 2

**Liest IFC-Data-Manager-Zuordnungsdefinitionen des aktiven Dokuments aus.**

Liest IFC-Data-Manager-Zuordnungsdefinitionen des aktiven Dokuments aus: welche Objekte zugeordnet sind, ihre Bedingungen, IFC-Einträge und Eigenschaftensätze sowie die Formel, die jeden Wert bereitstellt. Verwenden Sie diese Werkzeuge nur, wenn der Benutzer nach Datenzuordnungen oder dem Data Manager fragt; für IFC-Werte eines Objekts verwenden Sie getObjectIFCData in der Gruppe IFC.

| Werkzeug | Auswirkung | Sicherheit | Zusammenfassung |
|---|---|---|---|
| [`listIFCMappingObjects`](#listifcmappingobjects) | Nur lesend | low | Listet die Zuordnungsobjekte der aktiven Data-Manager-Zuordnung auf. |
| [`getIFCMapping`](#getifcmapping) | Nur lesend | low | Liest die Data-Manager-Zuordnung eines Zuordnungsobjekts aus. |

### listIFCMappingObjects

Listet die Zuordnungsobjekte der aktiven Data-Manager-Zuordnung auf.

> **Auswirkung:** Nur lesend · **Sicherheit:** low · **Rückgängig:** keiner · **In runToolBatch:** zulässig

**Details**

Listet die Zuordnungsobjekte der aktiven Data-Manager-Zuordnung mit `name`, `enabled`, `condition` und `category` auf; die Ausgabe wird mit `limit` (Standard 200) und `offset` seitenweise abgerufen. `count` enthält die Gesamtzahl, und `truncated` gibt an, ob weitere Einträge folgen. Übergeben Sie einen Namen an getIFCMapping, um die zugehörigen Einträge abzurufen.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `limit` | integer |  | Seitennavigation: maximal zurückzugebende Anzahl (mindestens 1). Siehe [Seitennavigation](Common.md#seitennavigation). |
| `offset` | integer |  | Seitennavigation: Anzahl der zu überspringenden Elemente (Standard 0). |
| `countOnly` | boolean |  | Seitennavigation: Gibt nur die Anzahlen zurück, nicht die Elemente. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `index` | Position des Objekts in der Zuordnung. |
| `name` | Objektname. Übergeben Sie ihn als `objectName` an `getIFCMapping`. |
| `enabled` | `true`, wenn das Objekt aktiviert ist. |
| `condition` | Bedingung des Objekts. Nur vorhanden, wenn eine Bedingung festgelegt ist. |
| `category` | Nur vorhanden, wenn für das Objekt eine Kategorie gespeichert ist: `classBasedLegacy`, `symbolDefinition`, `plugInThirdPartyLegacy`, `plugInBuiltInLegacy`, `ifcEntity`, `criteriaBased`, `parametricObjects`, `modelHierarchy`, `zones`, `systems`, `groups` oder `unknown`. |


### getIFCMapping

Liest die Data-Manager-Zuordnung eines Zuordnungsobjekts aus.

> **Auswirkung:** Nur lesend · **Sicherheit:** low · **Rückgängig:** keiner · **In runToolBatch:** zulässig

**Details**

Liest die Data-Manager-Zuordnung des Zuordnungsobjekts `objectName` aus (wie von listIFCMappingObjects zurückgegeben): seine Bedingung und IFC-Einträge, jeweils mit `type` (primary, secondary oder unknown), Aktivierungsstatus und Feldern (Werttyp, Zuordnungsformel, aktiviert, optional, leer) sowie Eigenschaftensätzen mit ihren Bedingungen und Feldern. Ein unbekannter Name gibt einen Fehler zurück.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `objectName` | string | Ja | Wie von listIFCMappingObjects zurückgegeben. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `objectName` | Angefragter Name. |
| `enabled` | `true`, wenn das Zuordnungsobjekt aktiviert ist. |
| `condition` | Bedingung des Zuordnungsobjekts. Nur vorhanden, wenn eine Bedingung festgelegt ist. |
| `entries` | IFC-Einträge des Objekts. Jeder Eintrag enthält die unten aufgeführten Schlüssel. |

| Eintragsschlüssel | Beschreibung |
|---|---|
| `name` | Name des Eintrags. |
| `type` | `primary`, `secondary` oder `unknown`. |
| `enabled` | `true`, wenn der Eintrag aktiviert ist. |
| `fields` | Felder des Eintrags. |
| `psets` | Eigenschaftensätze des Eintrags als Liste mit `name`, `enabled`, `fields` und `condition`. `condition` ist nur vorhanden, wenn für den Eigenschaftensatz eine Bedingung festgelegt ist. |

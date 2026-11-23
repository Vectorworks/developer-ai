[English](../../PythonAPI/v2027.2/ObjectsConnectCAD.md) • **Deutsch** • [日本語](../../PythonAPI.ja/v2027.2/ObjectsConnectCAD.md)

# ObjectsConnectCAD — ConnectCAD-Geräte und -Anschlüsse

> **Python-Modul:** `api` · **Version:** Vectorworks 2027 Update 2

[Zurück zum Index](README.md)

Die ConnectCAD-Klassen (sie erfordern ConnectCAD). `ConnectCADDeviceObject` ist ein schematisches Gerät ("Device") mit seinen Anschlüssen, das aus einer JSON-Gerätebeschreibung erzeugt wird; es kann auch ein Gerätetyp-Symbol erzeugen, das die vollständige Beschreibung speichert. `ConnectCADSocketObject` ist ein Anschlusspunkt eines Geräts ("Socket": IN, OUT oder IO; Loop-Anschlüsse bestehen aus Anschlusspaaren). `ConnectCADLibrary` listet die Signal- und Verbindertypen auf, prüft Gerätebeschreibungen und liest die Datenbank „Device Definition“ von Gerätetypen.

Der allgemeine Parameterzugriff wird von [`ParametricObject`](ObjectPrimitives.md#parametricobject) bereitgestellt.

## Inhaltsverzeichnis

- [Überblick](#überblick)
- [Klassen](#klassen)
  - [ConnectCADLibrary](#connectcadlibrary)
    - [ConnectCADLibrary.Signal](#connectcadlibrarysignal)
    - [ConnectCADLibrary.Connector](#connectcadlibraryconnector)
    - [ConnectCADLibrary.Validation](#connectcadlibraryvalidation)
    - [ConnectCADLibrary.DeviceDefinition](#connectcadlibrarydevicedefinition)
  - [ConnectCADSocketObject](#connectcadsocketobject)
  - [ConnectCADDeviceObject](#connectcaddeviceobject)
    - [ConnectCADDeviceObject.CreateResult](#connectcaddeviceobjectcreateresult)
    - [ConnectCADDeviceObject.AddSocketResult](#connectcaddeviceobjectaddsocketresult)
    - [ConnectCADDeviceObject.DeviceTypeResult](#connectcaddeviceobjectdevicetyperesult)

## Überblick

| Name | Art | Erbt von | Zusammenfassung |
|---|---|---|---|
| [`ConnectCADLibrary`](#connectcadlibrary) | Klasse |  | ConnectCAD-Daten, die von seinen Geräten gemeinsam genutzt werden: Signal- und Verbindertypen, Prüfung von Gerätebeschreibungen (JSON) und die Datenbank „Device Definition“ von... |
| [`ConnectCADLibrary.Signal`](#connectcadlibrarysignal) | Klasse (verschachtelt) |  | Ein ConnectCAD-Signaltyp mit seiner Kategorie und seinen bevorzugten Verbindern. |
| [`ConnectCADLibrary.Connector`](#connectcadlibraryconnector) | Klasse (verschachtelt) |  | Ein ConnectCAD-Verbindertyp. |
| [`ConnectCADLibrary.Validation`](#connectcadlibraryvalidation) | Klasse (verschachtelt) |  | Ergebnis von ValidateDevice: Fehler (das Gerät wäre fehlerhaft) und Warnungen (Daten, die nur in einem Gerätetyp erhalten bleiben). |
| [`ConnectCADLibrary.DeviceDefinition`](#connectcadlibrarydevicedefinition) | Klasse (verschachtelt) |  | Datenbank „Device Definition“ einer Gerätetyp-Symboldefinition. |
| [`ConnectCADSocketObject`](#connectcadsocketobject) | Klasse | [`ParametricObject`](ObjectPrimitives.md#parametricobject) | ConnectCAD-Anschluss (universeller Name "Socket"): ein Anschlusspunkt eines schematischen Geräts innerhalb seiner Profilgruppe. |
| [`ConnectCADDeviceObject`](#connectcaddeviceobject) | Klasse | [`ParametricObject`](ObjectPrimitives.md#parametricobject) | Schematisches ConnectCAD-Gerät (universeller Name "Device"): ein benannter Kasten mit Anschlüssen in seiner Profilgruppe. |
| [`ConnectCADDeviceObject.CreateResult`](#connectcaddeviceobjectcreateresult) | Klasse (verschachtelt) |  | Ergebnis von CreateFromJSON: das Gerät (null, wenn es nicht erzeugt wurde), Fehler und Warnungen. |
| [`ConnectCADDeviceObject.AddSocketResult`](#connectcaddeviceobjectaddsocketresult) | Klasse (verschachtelt) |  | Ergebnis von AddSocket: der Anschluss (null, wenn er nicht hinzugefügt wurde) und Fehler. |
| [`ConnectCADDeviceObject.DeviceTypeResult`](#connectcaddeviceobjectdevicetyperesult) | Klasse (verschachtelt) |  | Ergebnis von CreateDeviceType: die Gerätetyp-Symboldefinition, ob sie neu ist und ob ihre Datenbank die vollständige Beschreibung enthält. |

## Klassen

### ConnectCADLibrary

> **Vollständiger Name:** `api.ConnectCADLibrary` · **Erbt von:** `api.Object`

ConnectCAD-Daten, die von seinen Geräten gemeinsam genutzt werden: Signal- und Verbindertypen, Prüfung von Gerätebeschreibungen (JSON) und die Datenbank „Device Definition“ von Gerätetyp-Symbolen.

Eine Gerätebeschreibung ist ein JSON-Objekt in dem Format, das CC_DeviceFromJSON von ConnectCAD liest: { "name", "tag", "description", "make", "model", "category", "width_r": "non-rack" | "half-rack" | "full-rack", "width", "height", "depth" (mm), "power" (W), "weight" (kg), "is_modular" (bool), "n_slots" (int), "socket groups": [ { "qty", "type", "name", "signal", "connector", "orientation", "pinout": [ { "pinID", "name", "sourceID" } ], "extra_data": { ... }, "uuid", "source" } ] } Erforderlich: name, tag, make, model, width_r, is_modular, n_slots (> 0 nur bei modularen Geräten); die Höhe eines Rackgeräts wird in ganzen Höheneinheiten angegeben (n x 44.45 mm). Anschlussgruppentypen: IN, OUT, IO (je ein Anschluss) und LOOP / IOloop (ein Paar "<name>" + "<name>_LP": IN + OUT / IO + IO). Ausrichtungen: L, R, X (Durchführung); Loop-Anschlüsse nur L oder R. FUSE und BUS sind Bestandteile der internen Verdrahtung eines Gerätetyps, keine Anschlüsse. qty 1..50 erzeugt "<name> 1".."<name> n". Signale und Verbinder stammen aus GetSignals und GetConnectors; eine Anschlussbelegung listet die Kontakte ihres Verbinders auf, wobei pinIDs innerhalb des Geräts eindeutig sein muss. Erfordert das Plug-in ConnectCAD und die Lizenz; ohne sie ist IsAvailable gleich `False` und die Listen sind leer.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `ConnectCADLibrary()` | Zustandsloses Objekt; jede Methode ist statisch und kann direkt an der Klasse aufgerufen werden. |

**Methoden**

*Allgemein*

| Methode | Beschreibung |
|---|---|
| `IsAvailable() -> bool` *statisch* | Ob das Plug-in ConnectCAD installiert ist (zum Erzeugen von Geräten ist außerdem die Lizenz erforderlich). |

*Signaltypen*

| Methode | Beschreibung |
|---|---|
| `GetSignals() -> list[ConnectCADLibrary.Signal]` *statisch* | Die ConnectCAD-Signaldateien aus den Programm-, Arbeitsgruppen- und Benutzerordnern, wie von ConnectCAD zusammengeführt; aufgelistet werden nur die Signale, die ConnectCAD in dieser Sitzung kennt. |
| `GetConnectors() -> list[ConnectCADLibrary.Connector]` *statisch* | Verbindertypen mit ihren Kontakten. |
| `ValidateDevice(deviceJson: str) -> ConnectCADLibrary.Validation` *statisch* | Prüft eine Gerätebeschreibung (ein JSON-Objekt) anhand der Anforderungen von CC_DeviceFromJSON und des Anschlussobjekts ("Socket"). |
| `GetDeviceDefinition(symbolDefinition: Handle) -> ConnectCADLibrary.DeviceDefinition` *statisch* | Der Datensatz „Device Definition“ einer Gerätetyp-Symboldefinition mit `symbolDefinition`, category, type, make, model, rackMounting, slotCount und socketGroups; `symbolDefinition` ist `None`, wenn kein Datensatz vorhanden ist. |

#### ConnectCADLibrary.Signal

> **Vollständiger Name:** `api.ConnectCADLibrary.Signal` · **Erbt von:** `api.Object`

Ein ConnectCAD-Signaltyp.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `Signal()` | Standardwert (Felder mit ihren Standardwerten). |
| `Signal(name, category, description, defaultConnector, connectors)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `name` | `str` | Universeller Name, z. B. "HDMI". |
| `category` | `str` | Z. B. "Video". |
| `description` | `str` | Beschreibung des Signaltyps. |
| `defaultConnector` | `str` | Standard-Verbindertyp des Signals. |
| `connectors` | `list[str]` | Bevorzugte Verbinder (alle in GetConnectors enthalten). |

#### ConnectCADLibrary.Connector

> **Vollständiger Name:** `api.ConnectCADLibrary.Connector` · **Erbt von:** `api.Object`

Ein ConnectCAD-Verbindertyp.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `Connector()` | Standardwert (Felder mit ihren Standardwerten). |
| `Connector(name, localizedName, category, pins)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `name` | `str` | Universeller Name, z. B. "XLR3F". |
| `localizedName` | `str` | Lokalisierter Anzeigename. |
| `category` | `str` | Lokalisierter Ordner. |
| `pins` | `list[str]` | Kontaktnamen in ihrer Reihenfolge für "pinout" einer Anschlussgruppe. |

#### ConnectCADLibrary.Validation

> **Vollständiger Name:** `api.ConnectCADLibrary.Validation` · **Erbt von:** `api.Object`

Ergebnis von ValidateDevice.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `Validation()` | Standardwert (Felder mit ihren Standardwerten). |
| `Validation(errors, warnings, isValid)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `errors` | `list[str]` | Das Gerät wäre fehlerhaft oder das Plug-in würde fehlschlagen. |
| `warnings` | `list[str]` | Daten, die nur in einem Gerätetyp erhalten bleiben. |
| `isValid` | `bool` | Ob die Beschreibung gültig ist. |

#### ConnectCADLibrary.DeviceDefinition

> **Vollständiger Name:** `api.ConnectCADLibrary.DeviceDefinition` · **Erbt von:** `api.Object`

Datenbank „Device Definition“ einer Gerätetyp-Symboldefinition.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `DeviceDefinition()` | Standardwert (Felder mit ihren Standardwerten). |
| `DeviceDefinition(symbolDefinition, category, type, make, model, rackMounting, slotCount, socketGroups)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `symbolDefinition` | `Handle` | Gerätetyp-Symboldefinition. |
| `category` | `str` | Gerätekategorie. |
| `type` | `str` | Gerätetyp. |
| `make` | `str` | Hersteller. |
| `model` | `str` | Modell. |
| `rackMounting` | `str` | Kein Rackeinbau, halbe Rackbreite, volle Rackbreite. |
| `slotCount` | `str` | Anzahl der Steckplätze (modulare Geräte). |
| `socketGroups` | `str` | JSON: { "socket groups": [ ... ] }. |

### ConnectCADSocketObject

> **Vollständiger Name:** `api.ConnectCADSocketObject` · **Erbt von:** [`ParametricObject`](ObjectPrimitives.md#parametricobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

ConnectCAD-Anschluss (universeller Name "Socket"): ein Anschlusspunkt eines schematischen Geräts innerhalb seiner Profilgruppe. Sein Typ ist IN, OUT oder IO; ein Loop-Anschluss ist ein Anschlusspaar "<name>" und "<name>_LP". Die Darstellung richtet sich nach Typ und Ausrichtung (Verbindersymbol "skt_con_<type>" oder bei X "skt_con_classic_<type>"). Die Schreibmethoden prüfen den Wert (Typ IN/OUT/IO, Signal- und Verbindertypen von ConnectCAD) und berechnen den Anschluss und sein Gerät neu. Registrieren Sie das Gerät vor dem Ändern eines Anschlusses für das Rückgängigmachen (`Document.AddBothSwapObject`).

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `ConnectCADSocketObject(h: Handle)` | Verweist auf den vorhandenen ConnectCAD-Anschluss `h`; vor der Verwendung `IsValid()` prüfen. |

**Methoden**

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | True, wenn `h` auf ein Objekt des von dieser Klasse dargestellten Typs verweist. |
| `Duplicate() -> ConnectCADSocketObject` | Dupliziert den ConnectCAD-Anschluss in der Zeichnung und gibt die Kopie zurück. |
| `GetDevice() -> Handle` | Das Gerät, zu dem der Anschluss gehört; null, wenn sich der Anschluss nicht in einem Gerät befindet. |
| `GetSocketName() -> str \| None` | Gibt den Anschlussnamen zurück. |
| `SetSocketName(name: str) -> bool` | Darf nicht leer sein, '+' (Nummerierungsversatz) enthalten, auf "_LP" (Loop-Ausgang) enden oder von einem anderen Anschluss des Geräts verwendet werden. Die Anschlüsse eines Loop-Anschlusses können nicht umbenannt werden. |
| `GetTag() -> str \| None` | Gibt die Kennung zurück. |
| `GetSocketType() -> str \| None` | IN, OUT oder IO. |
| `SetSocketType(type: str) -> bool` | Setzt den Anschlusstyp. IN, OUT oder IO. |
| `GetSignal() -> str \| None` | Gibt das Signal zurück. |
| `SetSignal(signal: str) -> bool` | Ein Signaltyp von `ConnectCADLibrary.GetSignals`. |
| `GetConnector() -> str \| None` | Gibt den Verbinder zurück. |
| `SetConnector(connector: str) -> bool` | Ein Verbindertyp von `ConnectCADLibrary.GetConnectors`. |
| `GetOrientation() -> str \| None` | L, R oder X; wird beim Erzeugen des Geräts gesetzt (das Anschlusssymbol hängt davon ab). |
| `IsLoopOutput() -> bool` | Ob dieser Anschluss der Ausgang "<name>_LP" eines Loop-Anschlusses ist. |

Geerbt: alle Elemente von [`ParametricObject`](ObjectPrimitives.md#parametricobject), [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

### ConnectCADDeviceObject

> **Vollständiger Name:** `api.ConnectCADDeviceObject` · **Erbt von:** [`ParametricObject`](ObjectPrimitives.md#parametricobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Schematisches ConnectCAD-Gerät (universeller Name "Device"): ein benannter Kasten mit Anschlüssen in seiner Profilgruppe.

CreateFromJSON erzeugt ein Gerät mit seinen Anschlüssen aus einer Gerätebeschreibung (JSON-Format siehe ConnectCADLibrary), nachdem diese mit `ConnectCADLibrary.ValidateDevice` geprüft wurde; bei einer ungültigen Beschreibung wird nichts erzeugt. Geräte besitzen Name, Kennung, Beschreibung, Hersteller, Modell, Rackbreite / Höheneinheiten, Modularität / Steckplätze, Leistung und Gewicht; category, pinout, extra_data, uuid und source sind nur im Gerätetyp enthalten (CreateDeviceType).

Rückgängigmachen: CreateFromJSON registriert das neue Gerät selbst. Registrieren Sie das Gerät vor AddSocket oder vor Änderungen an Anschlüssen für das Rückgängigmachen (`Document.AddBothSwapObject`). Erfordert das Plug-in ConnectCAD und die Lizenz.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `ConnectCADDeviceObject(h: Handle)` | Verweist auf das vorhandene ConnectCAD-Gerät `h`; vor der Verwendung `IsValid()` prüfen. |

**Methoden**

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | True, wenn `h` auf ein Objekt des von dieser Klasse dargestellten Typs verweist. |
| `CreateFromJSON(deviceJson: str, position: Math.Point2D) -> ConnectCADDeviceObject.CreateResult` *statisch* | Erzeugt auf der aktiven Ebene ein Gerät mit seinen Anschlüssen aus einer Gerätebeschreibung (ein JSON-Objekt), mit dem Einfügepunkt an `position`. Wenn die Beschreibung Fehler enthält, wird nichts erzeugt. |
| `Duplicate() -> ConnectCADDeviceObject` | Dupliziert das ConnectCAD-Gerät in der Zeichnung und gibt die Kopie zurück. |
| `GetDeviceName() -> str \| None` | Gibt den Gerätenamen zurück. |
| `GetTag() -> str \| None` | Gibt die Kennung zurück. |
| `GetDescription() -> str \| None` | Gibt die Beschreibung zurück. |
| `GetMake() -> str \| None` | Gibt den Hersteller zurück. |
| `GetModel() -> str \| None` | Gibt das Modell zurück. |
| `GetRackWidth() -> str \| None` | Kein Rackeinbau, halbe Rackbreite oder volle Rackbreite. |
| `GetRackUnits() -> str \| None` | Aus der Höhe abgeleitete Höheneinheiten ("---", wenn es keine ganzen Einheiten sind oder das Gerät kein Rackgerät ist). |
| `IsModular() -> bool \| None` | True, wenn das Gerät modular ist (Steckplätze für Karten besitzt). |
| `GetSlotCount() -> int \| None` | Anzahl der Steckplatzeinträge. |
| `GetSockets() -> list[ConnectCADSocketObject]` | Die Anschlüsse des Geräts in der Zeichenreihenfolge; ein Loop-Anschluss besteht aus zwei Anschlüssen ("<name>" und "<name>_LP"). |
| `AddSocket(name: str, type: str, signal: str, connector: str, orientation: str) -> ConnectCADDeviceObject.AddSocketResult` | Fügt auf der Seite L oder R unter den vorhandenen Anschlüssen dieser Seite einen IN-, OUT- oder IO-Anschluss hinzu und vergrößert das Gerät. Das Ergebnis enthält den neuen `socket` und `errors`; `socket` ist `None`, wenn der Anschluss nicht hinzugefügt wurde. Loop-Anschlüsse und X-Anschlüsse können nur zusammen mit dem Gerät (`CreateFromJSON`) erzeugt werden. |
| `CreateDeviceType(deviceJson: str = '') -> ConnectCADDeviceObject.DeviceTypeResult` | Erzeugt aus diesem Gerät die Gerätetyp-Symboldefinition "<make> <model>" mit einer Datenbank "ConnectCAD Device Definition" (ConnectCAD CC_DeviceType). Mit `deviceJson` (der Beschreibung, aus der das Gerät erzeugt wurde) bewahrt die Datenbank die vollständige Beschreibung: pinout, extra_data, uuid, source und category. Ein Gerätetyp mit diesem Hersteller und Modell, der bereits in der Zeichnung vorhanden ist, bleibt unverändert; ein solcher aus den ConnectCAD-Bibliotheken wird importiert, statt einen neuen zu erzeugen. |

Geerbt: alle Elemente von [`ParametricObject`](ObjectPrimitives.md#parametricobject), [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

#### ConnectCADDeviceObject.CreateResult

> **Vollständiger Name:** `api.ConnectCADDeviceObject.CreateResult` · **Erbt von:** `api.Object`

Ergebnis von CreateFromJSON.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `CreateResult()` | Standardwert (Felder mit ihren Standardwerten). |
| `CreateResult(device, errors, warnings)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `device` | `Handle` | Null, wenn nichts erzeugt wurde. |
| `errors` | `list[str]` | Warum das Gerät nicht erzeugt wurde. |
| `warnings` | `list[str]` | Daten, die nur in einem Gerätetyp erhalten bleiben. |

#### ConnectCADDeviceObject.AddSocketResult

> **Vollständiger Name:** `api.ConnectCADDeviceObject.AddSocketResult` · **Erbt von:** `api.Object`

Ergebnis von AddSocket.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `AddSocketResult()` | Standardwert (Felder mit ihren Standardwerten). |
| `AddSocketResult(socket, errors)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `socket` | `Handle` | Null, wenn kein Anschluss hinzugefügt wurde. |
| `errors` | `list[str]` | Fehlermeldungen. |

#### ConnectCADDeviceObject.DeviceTypeResult

> **Vollständiger Name:** `api.ConnectCADDeviceObject.DeviceTypeResult` · **Erbt von:** `api.Object`

Ergebnis von CreateDeviceType.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `DeviceTypeResult()` | Standardwert (Felder mit ihren Standardwerten). |
| `DeviceTypeResult(symbolDefinition, name, isCreated, isFullDataStored, errors, warnings)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `symbolDefinition` | `Handle` | Die Gerätetyp-Symboldefinition; null bei einem Fehler. |
| `name` | `str` | "<make> <model>". |
| `isCreated` | `bool` | `False`: Ein Gerätetyp mit diesem Hersteller und Modell war bereits in der Zeichnung vorhanden und bleibt erhalten. |
| `isFullDataStored` | `bool` | Die Gerätebeschreibung (pinout, extra_data, category, ...) befindet sich in seiner Datenbank. |
| `errors` | `list[str]` | Fehlermeldungen. |
| `warnings` | `list[str]` | Warnmeldungen. |

---

[Zurück zum Index](README.md) · [Nach oben](#objectsconnectcad--connectcad-geräte-und--anschlüsse)

[English](../../MCP/v2027.2/OIPAccess.md) • **Deutsch** • [日本語](../../MCP.ja/v2027.2/OIPAccess.md)

# OIPAccess — Objekt-Info-Palette

> **Server:** Vectorworks MCP · **Version:** Vectorworks 2027 Update 2

[Zurück zum Index](README.md)

Werkzeuge zum Lesen und Bedienen der Objekt-Info-Palette für die aktuelle Auswahl wie ein Benutzer.

## Inhaltsverzeichnis

- [Überblick](#überblick)
- [Object Info](#object-info)
  - [getOIPControls](#getoipcontrols)
  - [setOIPValues](#setoipvalues)
  - [pressOIPButton](#pressoipbutton)

## Überblick

Dieser Ordner enthält 1 Werkzeuggruppe mit insgesamt 3 Werkzeugen.

| Gruppe | Gruppen-ID | Standardmäßig aktiv | Risikostufe | Anzahl der Werkzeuge | Zusammenfassung |
|---|---|---|---|---|---|
| [Object Info](#object-info) | `object-info` | Nein | mittel | 3 | Liest und bedient die Objekt-Info-Palette für die aktuelle Auswahl wie ein Benutzer. |

## Object Info

> **Gruppe:** `Object Info` · **Gruppen-ID:** `object-info` · **Standardmäßig aktiv:** Nein · **Risikostufe:** mittel · **Werkzeuge:** 3

**Liest und bedient die Objekt-Info-Palette für die aktuelle Auswahl wie ein Benutzer.**

Die Objekt-Info-Palette wie ein Benutzer bedienen: Für die aktuelle Auswahl zeigt sie den Reiter „Form“ (Klasse, Konstruktionsebene, Größe, Parameter von Plug-in-Objekten usw.), den Reiter „Daten“ (Datensätze und andere angehängte Daten) und den Reiter „Rendern“ (Texturen) als Steuerelemente an – Eingabefelder, Kontrollkästchen, Auswahllisten, Optionsfelder und Schaltflächen. Die Palette muss nicht sichtbar sein.

Verwenden Sie diese Gruppe für Eigenschaften, die in der Palette angezeigt und von keinem dedizierten Werkzeug abgedeckt werden, für die Parameter von Plug-in-Objekten so, wie die Palette sie anzeigt (einschließlich der Steuerelemente und Schaltflächen, die ein Plug-in dort hinzufügt), für Datensatzfelder im Reiter „Daten“ und Texturen im Reiter „Rendern“ oder wenn der Benutzer die Objekt-Info-Palette verwenden möchte. Bevorzugen Sie die dedizierten Werkzeuge anderer Gruppen, wenn diese die Änderung abdecken – z. B. setObjectParameter (oder `params` von createPluginObject beim Erstellen) für Plug-in-Parameter, editObject für Name, Klasse und Transformationen, setObjectAttributes für Stift und Füllung, applyResource für Texturen: Jeder Aufruf dieser Werkzeuge ist ein eigener Rückgängig-Schritt „MCP: <tool>“, wird bei einem Fehler zurückgenommen und kann in runToolBatch ausgeführt werden.

Arbeitsablauf:

1. Wählen Sie die Objekte mit selectObjects (Gruppe Selection) aus; eine Änderung gilt für die gesamte Auswahl.
2. getOIPControls listet die Steuerelemente eines `pane` auf: shape (Standard), data oder render.
3. setOIPValues legt Werte fest und pressOIPButton betätigt eine Schaltfläche. Geben Sie ein Steuerelement über `label` (das erste sichtbare Steuerelement mit dieser Bezeichnung, ohne Beachtung der Groß-/Kleinschreibung; ein abschließendes „:“ und Leerzeichen werden ignoriert) oder über `controlId` aus getOIPControls an – genau eine der beiden Angaben. Jede Änderung kann die Palette neu aufbauen und die Steuerungs-IDs ändern; bevorzugen Sie deshalb Bezeichnungen.
4. Lesen Sie die Steuerelemente nach Änderungen erneut mit getOIPControls aus.

Werte werden so eingegeben, wie sie ein Benutzer eintippt: Eine einfache Zahl wird in den Dokumenteinheiten (getUnits) angegeben, nicht in den Welteinheiten und Radiant, die andere Gruppen verwenden; fügen Sie daher zur Eindeutigkeit eine Einheit hinzu (z. B. „200mm“). Text, den Vectorworks nicht lesen kann, kann eine Warnmeldung auslösen, die wie ein Dialog auf eine Benutzereingabe wartet. Plug-in-Objekte werden sofort aktualisiert.

Rückgängig: Jede Änderung in der Palette ist ein eigener Vectorworks-Rückgängig-Schritt. Vectorworks benennt ihn wie eine Benutzereingabe, nicht „MCP: <tool>“. setOIPValues und pressOIPButton können nicht in runToolBatch ausgeführt werden; eine fehlgeschlagene Einstellung nimmt frühere Einstellungen nicht zurück.

Dialoge: Eine Schaltfläche oder Auswahl kann einen modalen Dialog oder eine Warnmeldung öffnen. Der Aufruf wartet dann, bis der Benutzer ihn schließt; währenddessen beantwortet Vectorworks keine anderen MCP-Aufrufe und beim MCP-Client kann eine Zeitüberschreitung auftreten. Eine Schaltflächenbezeichnung oder ein Auswahlname mit abschließendem „...“ öffnet einen Dialog (`opensDialog` in getOIPControls) und erfordert `allowDialog`: true (Standardwert false). Übergeben Sie den Wert nur, nachdem Sie dem Benutzer mitgeteilt haben, dass sich der Dialog öffnet und dort geschlossen werden muss.

| Werkzeug | Wirkung | Risiko | Zusammenfassung |
|---|---|---|---|
| [`getOIPControls`](#getoipcontrols) | Nur lesend | niedrig | Listet die Steuerelemente eines Reiters der Objekt-Info-Palette auf. |
| [`setOIPValues`](#setoipvalues) | Interaktiv | mittel | Legt Steuerelementwerte in der Objekt-Info-Palette wie ein Benutzer fest. |
| [`pressOIPButton`](#pressoipbutton) | Interaktiv | mittel | Betätigt eine Schaltfläche der Objekt-Info-Palette. |

### getOIPControls

Listet die Steuerelemente eines Reiters der Objekt-Info-Palette auf.

> **Wirkung:** Nur lesend · **Risiko:** niedrig · **Rückgängig:** keiner · **In runToolBatch:** zulässig

**Einzelheiten**

Listet die Steuerelemente auf, die ein Reiter der Objekt-Info-Palette für die aktuelle Auswahl anzeigt; der Reiter wird zuvor aktualisiert, sodass die Liste auch direkt nach selectObjects der Auswahl entspricht. `pane`: shape (Standard), data oder render. `search` behält Steuerelemente bei, deren Bezeichnung den Suchtext enthält (ohne Beachtung der Groß-/Kleinschreibung); `includeHidden` (Standardwert false) listet auch ausgeblendete Steuerelemente auf; `maxChoices` (0 oder größer, Standardwert 50) begrenzt die aufgeführten `choices` eines Steuerelements (`choiceCount` bleibt die Gesamtzahl); `limit` (Standardwert 100) und `offset` blättern durch die Liste; `countOnly` (Standardwert false) gibt `count` und die anderen Seitennavigationsschlüssel, jedoch kein `controls` zurück.

Gibt `pane`, `available` (true), `selectionCount`, `count` (die Anzahl der auf `search` passenden Steuerelemente), `controls` (diese Seite) und die Seitennavigationsschlüssel zurück (`truncated` ist true, wenn weitere Einträge folgen). Ein Reiter ohne Steuerelemente, z. B. wenn nichts ausgewählt ist, ist kein Fehler: `available` ist false, `count` 0, `controls` leer und es wird ein `hint` zurückgegeben. Jedes Steuerelement hat `controlId`, `type` (editText, staticText, checkBox, radioGroup, pullDown, searchablePullDown, button, classPullDown, layerPullDown oder other), `label`, `value` (als Text), `enabled`, `readOnly` und `indeterminate` (die ausgewählten Objekte unterscheiden sich); `visible` bei includeHidden, `parentId`, wenn es ein übergeordnetes Steuerelement hat, `checked` für ein Kontrollkästchen, das nicht indeterminate ist, `choices`, `choiceCount` und `selectedChoice` (0-basiert) für radioGroup und die vier pullDown-Typen, `opensDialog`: true für eine Schaltfläche, deren Bezeichnung einen Dialog öffnet, sowie `coreTypeId` für den Typ other.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `pane` | string |  | Einer von: `shape`, `data`, `render`. |
| `search` | string |  | Textfilter: behält Einträge bei, die diesen Text enthalten (ohne Beachtung der Groß-/Kleinschreibung). |
| `includeHidden` | boolean |  | Auch ausgeblendete Steuerelemente auflisten; jedes enthält dann `visible`. Standard `false`. |
| `maxChoices` | integer |  | 0 oder größer, Standardwert 50. |
| `limit` | integer |  | Seitennavigation: die maximale Anzahl zurückzugebender Elemente (mindestens 1). Siehe [Seitennavigation](Common.md#seitennavigation). |
| `offset` | integer |  | Seitennavigation: die Anzahl zu überspringender Elemente (Standardwert 0). |
| `countOnly` | boolean |  | Seitennavigation: Gibt nur die Anzahlen, nicht die Elemente zurück. |

### setOIPValues

Legt Steuerelementwerte in der Objekt-Info-Palette wie ein Benutzer fest.

> **Wirkung:** Interaktiv · **Risiko:** mittel · **Rückgängig:** von Vectorworks wie Benutzereingabe aufgezeichnet · **In runToolBatch:** nein

**Einzelheiten**

Legt Steuerelementwerte in der Objekt-Info-Palette der Reihe nach wie ein Benutzer fest. `settings`: 1 bis 50 Einträge mit { `label` oder `controlId`, `value`, `pane` (optional; Standardwert ist das `pane` des Aufrufs, das wiederum standardmäßig shape ist) }; `allowDialog` (Standardwert false). `value` je nach Steuerelementtyp: editText – der einzugebende Text oder eine Zahl (wird wie angegeben eingegeben); checkBox – ein boolescher Wert oder on/off, yes/no, 1/0 oder toggle; radioGroup und die vier pullDown-Typen – ein Auswahlname oder ein 0-basierter Index; searchablePullDown listet seine Elemente nicht auf, daher erfordert ein Index dafür `allowDialog`: true (das Element könnte einen Dialog öffnen).

Jede Einstellung wird vor der Änderung geprüft: Der Aufruf wird ohne Änderungen abgelehnt, wenn ein Steuerelement unbekannt, ausgeblendet, deaktiviert oder schreibgeschützt ist, wenn es sich um staticText oder einen anderen Steuerelementtyp, eine Schaltfläche (verwenden Sie pressOIPButton) oder einen nicht passenden Wert handelt, oder wenn eine Auswahl ohne `allowDialog`: true einen Dialog öffnet. Ein Steuerelement, das erst durch eine frühere Einstellung angezeigt oder aktiviert würde, wird deshalb ebenfalls abgelehnt: Legen Sie es in einem späteren Aufruf fest.

Anschließend werden die Einstellungen der Reihe nach angewendet: Jedes Steuerelement wird unmittelbar vor dem Festlegen erneut gesucht (eine frühere Einstellung kann die Palette neu aufbauen), sein neuer Wert wird zurückgelesen und der Aufruf endet beim ersten Fehler. Zurückgegeben werden `pane`, `results` [{ index, label, controlId, ok, value (wie zurückgelesen) oder err }], `appliedCount`, `allApplied` und `notAttemptedCount`. Ein Fehler bei der ersten Einstellung fügt ein `err` auf oberster Ebene hinzu; bei einem späteren Fehler bleiben die früheren Einstellungen angewendet (`allApplied` false, kein `err` auf oberster Ebene).

Es gibt keinen Rückgängig-Schritt „MCP: setOIPValues“ und kein Zurücksetzen: Jede angewendete Einstellung ist ein eigener Vectorworks-Rückgängig-Schritt.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `pane` | string |  | Einer von: `shape`, `data`, `render`. |
| `settings` | array of object | Ja | 1 bis 50 Elemente. |
| `settings[].label` | string |  | Beschriftung des Steuerelements: das erste sichtbare Steuerelement mit dieser Beschriftung (ohne Beachtung der Groß-/Kleinschreibung; führende und abschließende Leerzeichen sowie ein abschließender Doppelpunkt werden ignoriert, Leerzeichen innerhalb der Beschriftung zählen). Genau eines von `label` und `controlId` ist erforderlich. |
| `settings[].controlId` | integer |  | `controlId` aus getOIPControls; findet auch ein ausgeblendetes Steuerelement, das dann abgelehnt wird. Genau eines von `label` und `controlId` ist erforderlich. |
| `settings[].value` | string or number or boolean | Ja | Der neue Wert; wie er gelesen wird, hängt vom Steuerelementtyp ab (siehe Hinweis oben). |
| `settings[].pane` | string |  | Einer von: `shape`, `data`, `render`. |
| `allowDialog` | boolean |  | Standard `false`. Erforderlich für eine Auswahl, die ein Dialogfeld öffnet (Text endet mit `...` oder `…`), und für ein Element, das in einem durchsuchbaren `searchablePullDown` anhand des Index gewählt wird. |

### pressOIPButton

Betätigt eine Schaltfläche der Objekt-Info-Palette.

> **Wirkung:** Interaktiv · **Risiko:** mittel · **Rückgängig:** von Vectorworks wie Benutzereingabe aufgezeichnet · **In runToolBatch:** nein

**Einzelheiten**

Betätigt wie ein Benutzer eine Schaltfläche der Objekt-Info-Palette: `label` oder `controlId` bezeichnet sie im `pane` (Standardwert shape). Der Aufruf wird ohne Betätigung abgelehnt, wenn der Reiter keine Steuerelemente hat, das Steuerelement unbekannt, ausgeblendet, deaktiviert oder keine Schaltfläche ist oder die Schaltfläche einen Dialog öffnet (ihre Bezeichnung endet mit „...“: `opensDialog` in getOIPControls) und `allowDialog` nicht true ist. Teilen Sie dem Benutzer in diesem Fall mit, dass der Dialog geöffnet wird und dort geschlossen werden muss, und rufen Sie das Werkzeug erneut mit `allowDialog`: true auf.

Gibt `pane`, `label`, `controlId` und `pressed`: true zurück. Das Betätigen kann die Palette neu aufbauen: Lesen Sie die Steuerelemente danach erneut aus.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `pane` | string |  | Einer von: `shape`, `data`, `render`. |
| `label` | string |  | Beschriftung der Schaltfläche: das erste sichtbare Steuerelement mit dieser Beschriftung (ohne Beachtung der Groß-/Kleinschreibung; führende und abschließende Leerzeichen sowie ein abschließender Doppelpunkt werden ignoriert, Leerzeichen innerhalb der Beschriftung zählen). Genau eines von `label` und `controlId` ist erforderlich. |
| `controlId` | integer |  | `controlId` aus getOIPControls; findet auch ein ausgeblendetes Steuerelement, das dann abgelehnt wird. Genau eines von `label` und `controlId` ist erforderlich. |
| `allowDialog` | boolean |  | Standard `false`. Erforderlich, wenn die Beschriftung der Schaltfläche mit `...` oder `…` endet. |

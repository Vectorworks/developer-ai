[English](../../MCP/v2027.2/MenuAccess.md) • **Deutsch** • [日本語](../../MCP.ja/v2027.2/MenuAccess.md)

# MenuAccess — Menübefehle

> **Server:** Vectorworks MCP · **Version:** Vectorworks 2027 Update 2

[Zurück zum Inhaltsverzeichnis](README.md)

Werkzeuge zum Auslesen der Vectorworks-Menüs, Prüfen, ob ein Befehl ausgeführt werden kann, und Ausführen von Menübefehlen, als hätte der Benutzer sie ausgewählt.

## Inhaltsverzeichnis

- [Überblick](#überblick)
- [Menus](#menus)
  - [findMenuCommands](#findmenucommands)
  - [getMenus](#getmenus)
  - [getMenuStatus](#getmenustatus)
  - [runMenuCommand](#runmenucommand)

## Überblick

Dieser Ordner enthält 1 Werkzeuggruppe mit insgesamt 4 Werkzeugen.

| Gruppe | Gruppen-ID | Standardmäßig aktiv | Risikostufe | Werkzeuge | Zusammenfassung |
|---|---|---|---|---|---|
| [Menus](#menus) | `menus` | Nein | high | 4 | Menübefehle suchen, die Menüleiste auslesen, prüfen, ob ein Befehl jetzt ausgeführt werden kann, und ihn ausführen. |

## Menus

> **Gruppe:** `Menus` · **Gruppen-ID:** `menus` · **Standardmäßig aktiv:** Nein · **Risikostufe:** high · **Werkzeuge:** 4

**Menübefehle suchen, die Menüleiste auslesen, prüfen, ob ein Befehl jetzt ausgeführt werden kann, und ihn ausführen.**

Liest Vectorworks-Menüs aus und führt deren Befehle aus: die installierten Menübefehle, Menüs der Menüleiste des aktuellen Arbeitsbereichs mit Untermenüs, Befehlen und Elementgruppen, den Aktivierungs- oder Markierungsstatus eines Befehls oder Elements einer Elementgruppe sowie runMenuCommand, das einen Befehl oder ein Element einer Elementgruppe so ausführt, als hätte der Benutzer es ausgewählt. Verwenden Sie diese Gruppe, um herauszufinden, ob und wo Vectorworks einen Befehl für eine Aufgabe anbietet (um den Benutzer dorthin zu führen), was ein Befehl bewirkt, ob er im aktuellen Zustand ausgeführt werden kann (z. B. bei geöffnetem Dokument oder einer Auswahl) oder markiert ist (z. B. eine Ansichtsoption), und welche aktuellen Elemente Elementgruppen wie zuletzt verwendete Dateien, Standardansichten oder geöffnete Dokumente enthalten. findMenuCommands, getMenus und getMenuStatus lesen ausschließlich Daten aus: Die Zeichnung wird nicht geändert (kein Rückgängig-Schritt). runMenuCommand birgt ein hohes Risiko: Ein Menübefehl kann Daten ändern oder entfernen und Dialogfelder öffnen; fragen Sie vor jedem Aufruf den Benutzer.

Verwenden Sie für Änderungen, die von anderen Gruppen abgedeckt werden, bevorzugt die dafür vorgesehenen Werkzeuge.

Namen: Ein Befehl hat einen `universalName` (seine stabile Identität; integrierte Befehle verwenden eine negative Zahl wie "-28"), einen `name` (den englischen Namen; bei Plug-in-Befehlen ist er gleich dem universalName) und einen `displayName` (den lokalisierten Titel in den Menüs). Die Werkzeuge akzeptieren jeden dieser Namen ohne Beachtung der Groß-/Kleinschreibung und mit oder ohne nachgestellte "..."; bevorzugt wird universalName. Menütitel und Eintragstexte sind lokalisiert und entsprechen der Anzeige für den Benutzer.

Installiert und im Arbeitsbereich: findMenuCommands listet jeden installierten Befehl auf; `inWorkspace` gibt an, ob die Menüs des aktuellen Arbeitsbereichs ihn enthalten. Nur Befehle im Arbeitsbereich können aktiviert werden; nur Elementgruppen im Arbeitsbereich haben Elemente.

**Elementgruppen:** Eine Elementgruppe ist ein Befehl, der eine Gruppe von Menüelementen bereitstellt (zuletzt verwendete Dateien, Standardansichten usw.). Ein Element wird anhand des universalName seiner Elementgruppe und seines bei 0 beginnenden Index oder seines Textes benannt. Eine Elementgruppe ist regulär (feste Elemente), dynamisch (Elemente, die mit der Menüleiste erstellt werden) oder variabel (Elemente, die sich während der Ausführung von Vectorworks ändern). Elementtexte und Markierungen entsprechen dem letzten Aktualisierungsstand der Menüs in Vectorworks. Die Aktualisierung erfolgt beim Öffnen der Menüs durch den Benutzer, daher können sie veraltet sein; `enabled` ist immer aktuell. Auf dem Mac haben Elemente von Elementgruppen kein `checked`.

Arbeitsablauf:

1. Mit findMenuCommands `search` nach möglichen Befehlen suchen.
2. Mit getMenus `search` oder `menu` deren Position in den Menüs anzeigen; getMenus `chunk` listet die Elemente einer Elementgruppe auf.
3. Mit getMenuStatus prüfen, ob ein Befehl oder Element einer Elementgruppe jetzt ausgeführt werden kann und warum nicht.
4. runMenuCommand führt den Befehl aus, nachdem der Benutzer zugestimmt hat.

| Werkzeug | Auswirkung | Risiko | Zusammenfassung |
|---|---|---|---|
| [`findMenuCommands`](#findmenucommands) | Nur lesend | low | Sucht installierte Menübefehle anhand von Text und Arbeitsbereich. |
| [`getMenus`](#getmenus) | Nur lesend | low | Liest die Menüleiste des aktuellen Arbeitsbereichs, ein Menü oder die Elemente einer Elementgruppe aus. |
| [`getMenuStatus`](#getmenustatus) | Nur lesend | low | Gibt an, ob ein Menübefehl oder Element einer Elementgruppe jetzt ausgeführt werden kann und warum nicht. |
| [`runMenuCommand`](#runmenucommand) | Interaktiv, destruktiv | high | Führt einen Menübefehl oder ein Element einer Elementgruppe so aus, als hätte der Benutzer es ausgewählt. |

### findMenuCommands

Sucht installierte Menübefehle anhand von Text und Arbeitsbereich.

> **Auswirkung:** Nur lesend · **Risiko:** low · **Rückgängig:** keiner · **In runToolBatch:** zulässig

**Details**

Sucht installierte Menübefehle. `search` behält Befehle, deren universalName, name, displayName, category oder helpText den Text enthält (Groß-/Kleinschreibung wird ignoriert). `filter`: all (Standard: jeder installierte Befehl), inWorkspace (in den Menüs des aktuellen Arbeitsbereichs) oder enabled (Vectorworks könnte den Befehl jetzt ausführen; bei einer Elementgruppe mindestens eines ihrer Elemente). Mit `name` wird ein einzelner Befehl anhand von universalName, name oder displayName gesucht (Groß-/Kleinschreibung wird ignoriert, nachgestellte "..." optional; bei Gleichstand wird ein Befehl im Arbeitsbereich bevorzugt); nicht zusammen mit `search` oder `filter`.

`limit` (Standard 50) und `offset` rufen die Liste seitenweise ab; `countOnly` (Standard false) gibt die Seitennavigationsschlüssel ohne `commands` zurück. Gibt `commands` (diese Seite), `count` (alle Treffer), `returned`, `offset`, `limit`, `truncated` und bei weiteren Treffern `nextOffset` sowie `filter` zurück – oder `name`, wenn `name` angegeben ist. Ein `name`, zu dem kein Befehl existiert, ist kein Fehler: `count` ist 0 und es wird ein `hint` zurückgegeben.

Jeder Befehl enthält `universalName`, `name`, `displayName`, `category` (seine Kategorie im Arbeitsbereich-Editor), `helpText`, `kind` (internal, scriptPlugin, extensionPlugin oder unknown), `isChunk`, `inWorkspace`, `enabled` und `shortcut`, falls der Arbeitsbereich einen zuweist.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `name` | string |  | Sucht einen Befehl anhand von universalName, name oder displayName (ohne Beachtung der Groß-/Kleinschreibung). Ein abschließendes "..." darf nur beim displayName weggelassen oder hinzugefügt werden; universalName und name müssen bis auf Groß-/Kleinschreibung übereinstimmen. Nicht zusammen mit `search` oder `filter` verwenden. |
| `search` | string |  | Textfilter: Behält Einträge, die diesen Text enthalten (Groß-/Kleinschreibung wird ignoriert). |
| `filter` | string |  | Einer von: `all`, `inWorkspace`, `enabled`. |
| `limit` | integer |  | Seitennavigation: maximal zurückzugebende Anzahl (mindestens 1). Siehe [Seitennavigation](Common.md#seitennavigation). |
| `offset` | integer |  | Seitennavigation: Anzahl der zu überspringenden Elemente (Standard 0). |
| `countOnly` | boolean |  | Seitennavigation: Gibt nur die Anzahlen zurück, nicht die Elemente. |

### getMenus

Liest die Menüleiste des aktuellen Arbeitsbereichs, ein Menü oder die Elemente einer Elementgruppe aus.

> **Auswirkung:** Nur lesend · **Risiko:** low · **Rückgängig:** keiner · **In runToolBatch:** zulässig

**Details**

Liest die Menüleiste des aktuellen Arbeitsbereichs aus; es wird nichts ausgeführt.

**Ohne Argumente:** `menus`, die Titel der Menüs von links nach rechts. `menu` (ein Titel aus `menus`, Groß-/Kleinschreibung wird ignoriert) listet die Einträge des Menüs in Tiefensuche auf: Auf einen Untermenüeintrag folgen die Einträge des Untermenüs und auf eine Elementgruppe ihre aktuellen Elemente; Trennlinien werden ausgelassen. `search` behält Einträge, deren Text oder universalName den Suchtext enthält (Groß-/Kleinschreibung wird ignoriert), entweder in allen Menüs oder nur in `menu`. `chunk` (universalName, name oder displayName einer Elementgruppe im Arbeitsbereich; nicht zusammen mit `menu` oder `search`) listet die aktuellen Elemente dieser Elementgruppe auf. `limit` (Standard 100) und `offset` rufen die Liste seitenweise ab; `countOnly` (Standard false) gibt nur die Seitennavigationsschlüssel zurück. Gibt `menus`, `entries` oder `items` (diese Seite) mit `count`, `returned`, `offset`, `limit`, `truncated` und `nextOffset` zurück, wenn weitere Einträge folgen; außerdem `menu`, wenn `menu` angegeben ist, und `chunk` (den Befehl wie in findMenuCommands) für eine Elementgruppe. Ein Eintrag enthält `type` (command, chunkItem oder submenu), `menuPath` (Titel der Menüs, die ihn enthalten, von der Menüleiste abwärts, z. B. ["File", "Export"]) und `text`; ein Befehl oder Element einer Elementgruppe hat zusätzlich `universalName`, `enabled` und `checked`, ein Element einer Elementgruppe außerdem `chunkKind` (regular, dynamic oder variable) und `chunkItemIndex`, und jeder Eintrag gegebenenfalls `shortcut`. Ein Element einer `chunk` hat `index` (seine bei 0 beginnende Position in der Elementgruppe; Positionen von Trennlinien werden übersprungen), `text`, `enabled` und `checked`. Auf dem Mac haben Elemente von Elementgruppen kein `checked`.

**Fehler:** `menu` ist kein Menü der Menüleiste; für `chunk` gibt es keinen benannten Befehl, es handelt sich nicht um eine Elementgruppe oder sie ist nicht im Arbeitsbereich vorhanden.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `menu` | string |  | Ein Titel aus `menus`; Groß-/Kleinschreibung wird ignoriert. |
| `search` | string |  | Textfilter: Behält Einträge, die diesen Text enthalten (Groß-/Kleinschreibung wird ignoriert). |
| `chunk` | string |  | universalName, name oder displayName einer Elementgruppe im Arbeitsbereich; nicht zusammen mit `menu` oder `search`. |
| `limit` | integer |  | Seitennavigation: maximal zurückzugebende Anzahl (mindestens 1). Siehe [Seitennavigation](Common.md#seitennavigation). |
| `offset` | integer |  | Seitennavigation: Anzahl der zu überspringenden Elemente (Standard 0). |
| `countOnly` | boolean |  | Seitennavigation: Gibt nur die Anzahlen zurück, nicht die Elemente. |

### getMenuStatus

Gibt an, ob ein Menübefehl oder Element einer Elementgruppe jetzt ausgeführt werden kann und warum nicht.

> **Auswirkung:** Nur lesend · **Risiko:** low · **Rückgängig:** keiner · **In runToolBatch:** zulässig

**Details**

Gibt an, ob Vectorworks einen Menübefehl oder ein Element einer Elementgruppe jetzt ausführen könnte und warum nicht; es wird nichts ausgeführt. `name`: universalName (bevorzugt), name oder displayName des Befehls oder der Elementgruppe. Bei einer Elementgruppe bezeichnet `chunkItemIndex` (ein `index` oder `chunkItemIndex` aus getMenus) oder `chunkItemText` (Groß-/Kleinschreibung wird ignoriert) das Element; bei einer Elementgruppe mit nur einem Element ist keines von beiden erforderlich. Gibt `name`, `status`, `enabled` (true, wenn bereit), `reason`, `command` (wie in findMenuCommands), sofern ein Befehl diesen Namen hat, sowie bei ready oder disabled `checked` zurück (ob das Menü ein Häkchen anzeigt; nicht für Elemente einer Elementgruppe auf dem Mac); bei einem Element einer Elementgruppe auch `chunkItemIndex` und `chunkItemText`.

`status`: ready; disabled (benötigt einen anderen Zustand, z. B. ein geöffnetes Dokument oder eine Auswahl); notInWorkspace (installiert, aber nicht in den Menüs des aktuellen Arbeitsbereichs); notFound; chunkItemRequired (eine Elementgruppe mit mehreren Elementen: ein Element angeben); chunkItemNotFound (kein solches Element oder der Befehl ist keine Elementgruppe); unavailable (kein Befehl kann jetzt ausgeführt werden: die Menüleiste ist nicht eingerichtet oder ein Plug-in-Objekt wird neu generiert).

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `name` | string | Ja | universalName (bevorzugt), name oder displayName des Befehls oder der Elementgruppe. |
| `chunkItemIndex` | integer |  | Ein `index` oder `chunkItemIndex` aus getMenus. |
| `chunkItemText` | string |  | Groß-/Kleinschreibung wird ignoriert. |

### runMenuCommand

Führt einen Menübefehl oder ein Element einer Elementgruppe so aus, als hätte der Benutzer es ausgewählt.

> **Auswirkung:** Interaktiv, destruktiv · **Risiko:** high · **Rückgängig:** vom Menübefehl aufgezeichnet · **In runToolBatch:** nein

**Details**

Führt einen Vectorworks-Menübefehl oder ein Element einer Elementgruppe so aus, als hätte der Benutzer es in der Menüleiste ausgewählt.

**Hohes Risiko:** Teilen Sie dem Benutzer mit, welchen Befehl Sie ausführen und was er bewirkt; führen Sie ihn erst nach Zustimmung aus. `name`: universalName (bevorzugt), name oder displayName des Befehls oder der Elementgruppe wie in getMenuStatus; bei einer Elementgruppe bezeichnet `chunkItemIndex` oder `chunkItemText` das Element (bei einer Elementgruppe mit nur einem Element ist keines davon erforderlich). Der Befehl wird nur ausgeführt, wenn getMenuStatus ready melden würde; andernfalls geschieht nichts und das Ergebnis enthält `err`, `ran` false sowie die Schlüssel aus getMenuStatus (`status`, `reason`, `command`, ...).

**Dialogfelder:** Der Aufruf wird erst zurückgegeben, wenn der Benutzer die vom Befehl geöffneten Dialogfelder und Warnmeldungen geschlossen hat; währenddessen wird kein anderer Aufruf beantwortet. Ein Befehl oder Element einer Elementgruppe, dessen Titel mit "..." endet, öffnet ein Dialogfeld. SDK-Plug-in-Befehle (kind extensionPlugin) können auch ohne "..." ein Dialogfeld öffnen. Sie werden abgelehnt, sofern `allowDialog` nicht true ist. Übergeben Sie diesen Wert erst, nachdem Sie dem Benutzer mitgeteilt haben, dass ein Dialogfeld geöffnet wird und er es in Vectorworks schließen muss. Jeder Befehl kann weiterhin eine Warnmeldung anzeigen (z. B. wenn die Lizenz eine Funktion nicht umfasst).

**Vor der Ausführung abgelehnt:** Befehle, die Dokumente öffnen, speichern, drucken, schließen oder wechseln oder Vectorworks beenden (Neu, Öffnen, zuletzt verwendete Dateien, Startbildschirm, Schließen, Speichern, Alle speichern, Zurücksetzen, Vorherige Version exportieren, Drucken, Beenden, geöffnete Dokumente im Menü Fenster usw.); Aktualisieren einer Project-Sharing-Datei; Rückgängig und Wiederholen; Ausschneiden und Kopieren (sie ersetzen den Inhalt der Zwischenablage des Benutzers); erneutes Ausführen zuletzt verwendeter Befehle; Skript ausführen; Plug-in-Manager; Wechseln des Arbeitsbereichs; VectorScript- und Python-Plug-in-Befehle (kind scriptPlugin); sowie ein bereiter Befehl, während eine Werkzeugaktion läuft oder ein Rückgängig-Ereignis geöffnet ist.

**Rückgängig:** Der Befehl zeichnet wie in Vectorworks seinen eigenen Rückgängig-Schritt auf und nicht „MCP: runMenuCommand“; ein fehlgeschlagener Aufruf wird nicht zurückgerollt, und das Werkzeug kann nicht in runToolBatch ausgeführt werden. Gibt `ran` true, `command`, bei einem Element einer Elementgruppe `chunkItemIndex` und `chunkItemText`, `undoSteps` (Namen der vom Befehl hinzugefügten Rückgängig-Schritte, neueste zuerst; leer, wenn keine hinzugefügt wurden), `documentBefore` und `documentAfter` (Dateinamen des aktiven Dokuments; `documentAfter` ist null, wenn kein Dokument geöffnet ist) samt `documentChanged`, `activeTool` (universalName des danach aktiven Werkzeugs) samt `activeToolChanged`, `waitingForInput` (true, wenn der Befehl einen Rückgängig-Schritt offen ließ oder das aktive Werkzeug änderte: möglicherweise wartet Vectorworks auf Eingaben, z. B. Mausklicks eines temporären Werkzeugs; weisen Sie den Benutzer an, dies dort abzuschließen oder abzubrechen und bis dahin keine weiteren Änderungen vorzunehmen) und einen `hint` bei geändertem Dokument oder ausstehender Eingabe zurück. Wenn sich das Dokument geändert hat, wird `undoSteps` ausgelassen und nachfolgende Aufrufe beziehen sich auf das neue aktive Dokument. Lesen Sie anschließend Menüs, Auswahl und Objekte erneut aus.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `name` | string | Ja | universalName (bevorzugt), name oder displayName des Befehls oder der Elementgruppe, wie in getMenuStatus. |
| `chunkItemIndex` | integer |  | Ein `index` oder `chunkItemIndex` aus getMenus (0 oder höher). Nicht zusammen mit `chunkItemText` verwenden. |
| `chunkItemText` | string |  | Text des Elements, ohne Beachtung der Groß-/Kleinschreibung; ein abschließendes "..." darf weggelassen werden. Nicht zusammen mit `chunkItemIndex` verwenden. |
| `allowDialog` | boolean |  | Muss auf `true` gesetzt werden, um einen Befehl auszuführen, der einen Dialog öffnet oder öffnen könnte: Sein Titel endet mit "..." oder "…", oder sein Typ ist `extensionPlugin`. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `name` | Übergebener Wert für `name`. |
| `ran` | `true`. |
| `command` | Befehl, wie von findMenuCommands zurückgegeben. |
| `chunkItemIndex`, `chunkItemText` | Nur bei einem Element einer Elementgruppe: das ausgeführte Element. |
| `documentBefore` | Dateiname des aktiven Dokuments vor der Ausführung (bei einem ungespeicherten Dokument dessen unbenannter Name). |
| `documentAfter` | Dateiname des aktiven Dokuments danach (bei einem ungespeicherten Dokument dessen unbenannter Name); `null`, wenn kein Dokument geöffnet ist. |
| `documentChanged` | `true`, wenn das aktive Dokument nicht mehr dem vorherigen entspricht: ein anderes Dokument, keines (`documentAfter` ist `null`), dieselbe Datei erneut geöffnet oder dasselbe Dokument unter einem anderen Dateipfad (z. B. nach dem Speichern unter einem neuen Namen). |
| `undoSteps` | Namen der vom Befehl hinzugefügten Rückgängig-Schritte, neueste zuerst (leer, wenn keine hinzugefügt wurden). Wird ausgelassen, wenn sich das Dokument geändert hat oder die Rückgängig-Schritte nicht gelesen werden können. |
| `activeTool` | universalName des danach aktiven Werkzeugs; `null`, wenn keines aktiv ist. |
| `activeToolChanged` | `true`, wenn die Ausführung das aktive Werkzeug geändert hat. |
| `waitingForInput` | `true`, wenn der Befehl ein Rückgängig-Ereignis offen ließ oder das aktive Werkzeug änderte. |
| `hint` | Nur vorhanden, wenn es etwas mitzuteilen gibt: geändertes Dokument oder ausstehende Eingabe. |

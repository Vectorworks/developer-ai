[English](../MCP/README.md) • **Deutsch** • [日本語](../MCP.ja/README.md)

# Vectorworks-MCP-Server

## Was ist MCP?

Das Model Context Protocol (MCP) ist ein offenes Protokoll, über das KI-Anwendungen externe Funktionen und Kontext nutzen können. Ein MCP-Server beschreibt seine verfügbaren Funktionen. Ein MCP-Client kann diese entdecken und über ein einheitliches Protokoll Anfragen stellen.

## Lokaler HTTP-Server von Vectorworks

Der Vectorworks-MCP-Server verbindet MCP-Clients mit den in Vectorworks verfügbaren Funktionen. Diese sind in Funktionsgruppen organisiert und ermöglichen mithilfe der Vectorworks-APIs das Untersuchen und Bearbeiten von Dokumentdaten. Dazu gehören unter anderem Dokumentkontext, Zeichnungsobjekte und Geometrie, Ressourcen, der Zugriff auf die Benutzeroberfläche, Skripte und produktspezifische Arbeitsabläufe. Der vollständige Funktionskatalog ist separat dokumentiert; diese README listet die einzelnen Tools bewusst nicht auf.

Der MCP-Server wird lokal auf dem Rechner des Benutzers ausgeführt und kommuniziert über HTTP mit MCP-Clients. So kann sich ein kompatibler Client mit der Vectorworks-Instanz verbinden, ohne dass die Integration über einen gehosteten MCP-Dienst geleitet wird.

| Version | Referenz |
| --- | --- |
| Vectorworks 2027 Update 2 | [v2027.2](v2027.2/README.md) |

## Server starten und verbinden

Wählen Sie in den Standard-Arbeitsumgebungen (außer Viewer) **Extras > MCP-Server > MCP-Server starten...**. In einer benutzerdefinierten Arbeitsumgebung können die Befehle an anderer Stelle liegen oder fehlen. Der Dialog **MCP-Server starten** enthält:

- **Werkzeugmodus**: **Alle Werkzeuge aktivieren** (Standard), **Alle Werkzeuge ohne Skriptwerkzeuge aktivieren** oder **Nur Skriptwerkzeuge aktivieren**. Siehe [Werkzeuggruppen und Aktivierung](v2027.2/Common.md#werkzeuggruppen-und-aktivierung).
- **Serverport**: 1 bis 65535, Standardwert 8765. Ist der Port belegt, versucht der Server bis zu 9 weitere Ports (höchstens 65535); im Dialog wird die URL mit dem verwendeten Port angezeigt.
- **Server starten** und **Server stoppen** sowie **URL kopieren**, womit die Server-URL, zum Beispiel `http://localhost:8765`, kopiert wird.
- Links zur Dokumentation für KI-Skripte und zur MCP-Tool-Dokumentation sowie die Versionsangabe.

Der Modus und der Port lassen sich nur ändern, wenn der Server gestoppt ist. Sie werden nach einem erfolgreichen Start gespeichert. **Schließen** schließt den Dialog; ein laufender Server bleibt aktiv. **Server stoppen** oder **Extras > MCP-Server > MCP-Server stoppen** beendet ihn.

Fügen Sie die URL in Ihrem MCP-Client als HTTP-MCP-Server hinzu und öffnen Sie eine Zeichnung in Vectorworks: Ohne geöffnete Zeichnung geben die Werkzeuge `no active Vectorworks document` zurück. Der Server:

- lauscht ausschließlich auf `127.0.0.1` und verarbeitet jeweils eine Verbindung;
- verwendet JSON-RPC 2.0 über HTTP mit der MCP-Protokollversion `2024-11-05` und den Methoden `initialize`, `ping`, `tools/list` und `tools/call`; Anfragen müssen mit `POST` (beliebiger Pfad) und `Content-Type: application/json` gesendet werden;
- beantwortet `GET /` mit `{service, version, protocol}`, andere `GET`-Anfragen mit 404 und andere Methoden mit 405;
- weist mit 403 Anfragen zurück, deren `Host` nicht `127.0.0.1:<port>` oder `localhost:<port>` ist, deren `Origin` (falls angegeben) nicht `http://` oder `https://` gefolgt von `localhost` oder `127.0.0.1` und optional `:<port>` entspricht (alles Weitere, etwa `null`, `[::1]` oder ein Pfad, wird zurückgewiesen), oder die mehr als einen `Host`- oder `Origin`-Header enthalten. Ein `POST` mit mehr als einem `Content-Type`-Header oder einem anderen Wert als `application/json` wird mit 415 abgelehnt;
- verwendet keine Authentifizierung: Jedes Programm auf diesem Rechner kann die angebotenen Werkzeuge aufrufen. Wählen Sie **Alle Werkzeuge ohne Skriptwerkzeuge aktivieren**, um Skriptausführungen auszuschließen, und stoppen Sie den Server, wenn Sie ihn nicht benötigen;
- beantwortet Benachrichtigungen wie `notifications/initialized` mit HTTP 200 und leerem Inhalt und meldet `capabilities.tools.listChanged: true`. Akzeptiert der Client `text/event-stream`, wird die Antwort auf `activateToolGroups` als Ereignisstrom gesendet, der vor dem Ergebnis `notifications/tools/list_changed` enthält.
## Festgelegte Skripte mit KI-Unterstützung

KI kann Sie auch beim Entwickeln („Vibe-Coding“) eines fest definierten Skripts für wiederkehrende Aufgaben unterstützen. Statt bei jedem Durchlauf die KI dynamisch Aktionen auswählen zu lassen, können Sie das generierte Skript prüfen und testen und anschließend wiederverwenden – ohne dass die KI während der Ausführung Entscheidungen trifft.

So entsteht ein deterministischer Arbeitsablauf: Das Skript folgt einer vordefinierten Logik; die Ergebnisse hängen von den Eingaben und dem Dokumentzustand ab. Informationen zur Entwicklung dieser Skripte und zum dafür verwendbaren KI-Kontext finden Sie in der [Python-API-Dokumentation](../PythonAPI.de/README.md).

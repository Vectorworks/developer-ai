[English](README.md) • **Deutsch** • [日本語](README.ja.md)

# KI-gestützte Entwicklung für Vectorworks

KI kann Sie auf zwei sich ergänzende Arten bei der Arbeit mit Vectorworks-Zeichnungen unterstützen:

- **Fest definierte Skripte – Python-API:** Mit KI können Sie ein Skript entwickeln, das die in Vectorworks ausgeführten Vorgänge festlegt. Nach Prüfung und Tests lässt sich das Skript für einen vorhersehbaren Arbeitsablauf wiederverwenden.
- **MCP-Verbindung – Skripte und Zeichnungswerkzeuge:** Verbinden Sie einen KI-Client direkt mit Vectorworks. Er kann Python-Skripte erstellen, speichern und ausführen oder mithilfe von MCP-Tools mit der Zeichnung arbeiten. Bei der direkten Verwendung der Tools statt eines vordefinierten Skripts wählt die KI die Aktionen anhand Ihrer Anfrage und des Zeichnungskontexts aus; die Abfolge kann daher variieren.

## Python-API

Verwenden Sie die Python-API, um fest definierte Skripte für Vectorworks zu erstellen. KI-Tools können Sie beim Schreiben von Skripten unterstützen, die Sie prüfen, testen und ausführen können. So entsteht ein klar definierter Arbeitsablauf, dessen Ergebnisse vom Skript, seinen Eingaben und dem Dokumentzustand abhängen.

Weitere Informationen zur API und zum KI-Kontext für die Skriptentwicklung finden Sie in der [Python-API-Dokumentation](PythonAPI.de/README.md).

## MCP-Server

Der Vectorworks-MCP-Server ermöglicht kompatiblen KI-Clients über das [Model Context Protocol (MCP)](https://modelcontextprotocol.io) eine direkte Verbindung zu Vectorworks. MCP ist ein offenes Protokoll, über das KI-Anwendungen externe Funktionen und Kontext nutzen können. Die Verbindung unterstützt sowohl die Entwicklung und Ausführung von Skripten als auch die direkte Bearbeitung von Zeichnungen mit einer breiten Auswahl an MCP-Tools.

Vorteile:

- **Lokal ausgeführt:** Der Server läuft auf Ihrem Rechner und kommuniziert über HTTP mit MCP-Clients. So kann sich ein Client mit Ihrer laufenden Vectorworks-Instanz verbinden, ohne dass die Integration über einen gehosteten MCP-Dienst geleitet wird.
- **Skriptunterstützung:** Ein KI-Client kann die Python-API verwenden, um Skripte direkt in Vectorworks zu erstellen, zu speichern und auszuführen.
- **Arbeit mit Zeichnungen:** MCP-Tools decken Dokumentkontext, Zeichnungsobjekte und Geometrie, Ressourcen, den Zugriff auf die Benutzeroberfläche sowie produkt- und fachbereichsspezifische Arbeitsabläufe ab. Bei der direkten Verwendung dieser Tools wählt die KI Aktionen anhand der Anfrage und des verfügbaren Kontexts aus, statt einem fest definierten Skript zu folgen.

Weitere Informationen zur Verbindung und den verfügbaren Tools finden Sie in der [Dokumentation zum MCP-Server](MCP.de/README.md).

## MCP-Einrichtung für externe KI-Clients

Anleitungen zur Installation und Einrichtung der MCP-Unterstützung in GitHub Copilot, Claude Desktop und Claude Code finden Sie in der [Tools-README](Tools/READ_ME.de.md).

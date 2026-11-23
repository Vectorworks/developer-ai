[English](../PythonAPI/README.md) • **Deutsch** • [日本語](../PythonAPI.ja/README.md)

# Python-API-Dokumentation

Verwenden Sie den jeweiligen <u>**AI-CONTEXT.md**</u> als Kontext, damit ein KI-Tool mit dieser API Code generieren und Skripte entwickeln kann (sogenanntes „Vibe-Coding“).

Referenzdokumentation des Vectorworks-Python-Moduls `api`, nach Vectorworks-Version:

| Version | Referenz | KI-Kontext |
| --- | --- | --- |
| Vectorworks 2027 Update 2 | [v2027.2](v2027.2/README.md) | [AI-CONTEXT.md](../PythonAPI/v2027.2/AI-CONTEXT.md) |

## MCP-Verbindung

Der [Vectorworks-MCP-Server](../MCP.de/README.md) ermöglicht einem kompatiblen KI-Client die Verbindung zu Vectorworks, um Python-Skripte direkt in der Anwendung zu erstellen, zu speichern und auszuführen. Über diese Verbindung kann der Client die Python-API nachschlagen und Skripte während der Entwicklung und beim Testen ausführen.

Dieselbe Verbindung ermöglicht es Ihnen auch, ohne vordefiniertes Skript mit einer großen Auswahl an MCP-Tools an Ihrer Zeichnung zu arbeiten. In diesem nichtdeterministischen Arbeitsablauf wählt die KI anhand Ihrer Anfrage und des aktuellen Zeichnungszustands die zu verwendenden Tools aus; die Abfolge der Aktionen kann daher variieren. Skriptentwicklung und direkte Interaktion mit den Tools können getrennt oder gemeinsam in einem Arbeitsablauf eingesetzt werden.

[English](../../MCP/v2027.2/Attributes.md) • **Deutsch** • [日本語](../../MCP.ja/v2027.2/Attributes.md)

# Attributes — Linienendmarkierungen und Schlagschatten

> **Server:** Vectorworks MCP · **Version:** Vectorworks 2027 Update 2

[Zurück zum Index](README.md)

Die Werteformate für Linienendmarkierungen und Schlagschatten. Sie werden von Tools gemeinsam verwendet, die die grafischen Attribute von Klassen und Objekten sowie die Standardattribute des Dokuments lesen und schreiben.

## Inhaltsverzeichnis

- [Übersicht](#übersicht)
- [Linienendmarkierungen](#linienendmarkierungen)
- [Schlagschatten](#schlagschatten)

## Übersicht

| Format | Verwendet in | Zusammenfassung |
|---|---|---|
| [Linienendmarkierungen](#linienendmarkierungen) | [`editClass`](DocumentAccess.md#editclass), [`setObjectAttributes`](ObjectPrimitives.md#setobjectattributes) | Pfeilspitzen, Striche und andere Markierungen am Anfang und Ende von Linien, Bögen, Polylinien und Polygonen sowie bei Plug-in-Objekten, die Markierungen unterstützen. |
| [Schlagschatten](#schlagschatten) | [`editClass`](DocumentAccess.md#editclass), [`setObjectAttributes`](ObjectPrimitives.md#setobjectattributes) | Der Schlagschatten, der hinter einem Objekt gezeichnet wird. |

Beide Formate sind **partiell**: Nur die angegebenen Elemente werden geändert, die übrigen behalten ihre Werte. Ein Wert, der dem aktuellen Wert entspricht, wird ignoriert. So kann eine gelesene Markierung oder ein gelesener Schlagschatten mit nur einem geänderten Element zurückgesendet werden.

## Linienendmarkierungen

Eine Linienendmarkierung ist ein Objekt mit den folgenden optionalen Elementen:

| Element | Typ | Beschreibung |
|---|---|---|
| `shape` | string | Die Form der Markierung. Zulässige Werte: `arrow`, `concaveCurvedArrow`, `circle`, `dimSlash`, `dimCross`, `lasso`, `hexagon`, `vShaped`, `cone`, `taperedVShaped`, `sShaped`, `rectangle`, `doubleLine`. |
| `fill` | string | `lineColor` füllt die Markierung mit der Linienfarbe, `white` mit Weiß, `none` lässt sie offen. Zulässige Werte: `lineColor`, `white`, `none`. |
| `base` | string | Die Form der Markierungsbasis. Zulässige Werte: `flat`, `open`, `angle`, `arc`. |
| `halfTick` | string | Zeichnet die gesamte Markierung oder nur ihre linke oder rechte Hälfte. Zulässige Werte: `full`, `left`, `right`. |
| `tail` | boolean | Fügt den Markierungsschaft hinzu. |
| `angle` | integer | Der Öffnungswinkel in ganzen Grad. Er wird als vorzeichenbehaftete 8-Bit-Zahl gespeichert; daher wird 200 zu -56. |
| `length` | number | Die Länge in Seiteneinheiten (Zoll). |
| `width` | number | Die Breite in Seiteneinheiten (Zoll). |
| `thickness` | number | Die Linienstärke der Markierung in `thicknessUnits`. Bei einer geänderten Linienstärke wird `thicknessBasis` auf `custom` gesetzt. Gespeichert wird sie als ganze Mil im Bereich von 0 bis 255 (etwa 6,5 mm oder 18,4 Punkte): Der Wert wird auf ganze Mil gerundet; größere Werte werden umgebrochen (300 mils werden zu 44 mils). |
| `thicknessBasis` | string | Gibt an, woher die Linienstärke stammt: Linienstärke des Objekts, Bemaßungslinienstärke oder benutzerdefinierte `thickness`. Zulässige Werte: `lineThickness`, `dimThickness`, `custom`. |
| `thicknessUnits` | string | Die Einheiten von `thickness`. Zulässige Werte: `mils`, `points`, `millimeters`. |
| `visible` | boolean | Zeigt die Markierung an. Klassen speichern diesen Wert nicht: `editClass` ignoriert ihn, und `getClasses` gibt für eine Klassenmarkierung immer `true` zurück. Bei Objekten wird er mit der Markierung gespeichert; daher setzen `beginning` und `end` ihn ebenfalls. `markers.beginningVisible` und `markers.endVisible` setzen ihn separat. |

**Beispiel**: ein offener Pfeil am Ende einer Linie, etwas verlängert.

```json
{
  "uuid": "<uuid>",
  "markers": {
    "end": {"shape": "arrow", "fill": "none", "length": 0.2, "angle": 20},
    "endVisible": true
  }
}
```

**Verwendung dieses Formats**

| Werkzeug | Argument |
|---|---|
| [`editClass`](DocumentAccess.md#editclass) | `beginningMarker` |
| [`editClass`](DocumentAccess.md#editclass) | `endMarker` |
| [`setObjectAttributes`](ObjectPrimitives.md#setobjectattributes) | `markers.beginning` |
| [`setObjectAttributes`](ObjectPrimitives.md#setobjectattributes) | `markers.end` |
| [`setPreferences`](DocumentAccess.md#setpreferences) | `values.beginningMarker` (mit `category` `defaultAttributes`) |
| [`setPreferences`](DocumentAccess.md#setpreferences) | `values.endMarker` (mit `category` `defaultAttributes`) |

Mit [`setObjectAttributes`](ObjectPrimitives.md#setobjectattributes) akzeptiert `markers` außerdem `beginningVisible` und `endVisible` (zum Ein- oder Ausblenden der jeweiligen Markierung) sowie `byClass` (verwendet die Markierungen der Klasse). [`getObjectAttributes`](ObjectPrimitives.md#getobjectattributes) und [`getClasses`](DocumentAccess.md#getclasses) (`detailed`) lesen Markierungen im selben Format. [`getPreferences`](DocumentAccess.md#getpreferences) (`defaultAttributes`) gibt `beginningMarker`, `endMarker` (jeweils mit ihrem tatsächlichen `visible`-Wert) und `markersByClass` zurück. [`setPreferences`](DocumentAccess.md#setpreferences) schreibt `beginningMarker` und `endMarker` als partielle Markierungen, die vom aktuellen Standardmarker des Dokuments ausgehen, sowie `markersByClass`, das nur bei `true` wirksam wird. Das Schreiben von `beginningMarker` oder `endMarker` schaltet `markersByClass` aus; wenn beide angegeben sind, wird `markersByClass` danach angewendet und hat Vorrang.

## Schlagschatten

Ein Schlagschatten ist ein Objekt mit den folgenden optionalen Elementen:

| Element | Typ | Beschreibung |
|---|---|---|
| `enabled` | boolean | Zeichnet den Schlagschatten. |
| `units` | string | Einheiten für `offset` und `blurRadius`: Seiteneinheiten (Zoll) (`page`) oder Welteinheiten (`world`). Zulässige Werte: `page`, `world`. |
| `offset` | number | Der Abstand des Schattens zum Objekt in `units`. |
| `blurRadius` | number | Der Weichzeichnungsradius in `units`. |
| `angle` | number | Die Richtung des Schattens in Grad. |
| `colorIndex` | integer | Die Schattenfarbe als Index in der Farbtabelle des Dokuments. |
| `color` | [Farbe](Common.md#farben) | Die Schattenfarbe als RGB-Wert (siehe [Farben](Common.md#farben)). Wenn sich `color` und `colorIndex` ändern, hat `colorIndex` Vorrang. |
| `opacity` | integer | Die Deckkraft von 0 bis 100. |
| `byClass` | boolean | Nur Objekte: verwendet den Schlagschatten der Objektklasse. |
| `delete` | boolean | Nur Objekte: entfernt den Schlagschatten des Objekts selbst. |

**Beispiel**: ein weicher schwarzer Schatten mit halber Deckkraft und einem Abstand von 0,05 Seiteneinheiten (Zoll) zum Objekt.

```json
{
  "uuid": "<uuid>",
  "dropShadow": {
    "enabled": true,
    "units": "page",
    "offset": 0.05,
    "angle": -45,
    "blurRadius": 0.03,
    "opacity": 50,
    "color": {"r": 0, "g": 0, "b": 0}
  }
}
```

**Verwendung dieses Formats**

| Werkzeug | Argument |
|---|---|
| [`editClass`](DocumentAccess.md#editclass) | `dropShadow` |
| [`setObjectAttributes`](ObjectPrimitives.md#setobjectattributes) | `dropShadow` |

[`setObjectAttributes`](ObjectPrimitives.md#setobjectattributes) akzeptiert für `dropShadow` auch `true` oder `false`, um den Schlagschatten eines Objekts ein- oder auszuschalten. [`getObjectAttributes`](ObjectPrimitives.md#getobjectattributes) und [`getClasses`](DocumentAccess.md#getclasses) (`detailed`) lesen Schlagschatten im selben Format.

**English** • [Deutsch](../../MCP.de/v2027.2/Attributes.md) • [日本語](../../MCP.ja/v2027.2/Attributes.md)

# Attributes — line end markers and drop shadows

> **Server:** Vectorworks MCP · **Version:** Vectorworks 2027 Update 2

[Back to the index](README.md)

The value formats of line end markers and drop shadows. They are shared by the tools that read and write the graphical attributes of classes and objects, and the default attributes of the document.

## Table of contents

- [Overview](#overview)
- [Line end markers](#line-end-markers)
- [Drop shadow](#drop-shadow)

## Overview

| Format | Used in | Summary |
|---|---|---|
| [Line end markers](#line-end-markers) | [`editClass`](DocumentAccess.md#editclass), [`setObjectAttributes`](ObjectPrimitives.md#setobjectattributes), [`setPreferences`](DocumentAccess.md#setpreferences) | The arrowheads, ticks and other markers at the start and end of lines, arcs, polylines and polygons, and of the plug-in objects that accept markers. |
| [Drop shadow](#drop-shadow) | [`editClass`](DocumentAccess.md#editclass), [`setObjectAttributes`](ObjectPrimitives.md#setobjectattributes) | The drop shadow drawn behind an object. |

Both formats are **partial**: only the members given are changed, the others keep their values. Where there is no stored marker or drop shadow to start from, the members left out start with the defaults listed under each format. A value that is not an object changes no member, but it is still written (except for a non-boolean, non-object `dropShadow` in `setObjectAttributes`): `applied` reports the write, and for `setObjectAttributes` and `setPreferences` a non-object marker writes the current marker back and so switches `byClass` / `markersByClass` off, like any marker write. Leave the member out to keep it as it is.

A marker or drop shadow that was read can be sent back with one member edited, because a member that still has the value it was read with is not applied again:

- A `thickness` equal to the current thickness does not set `thicknessBasis` to `custom`.
- A `thicknessBasis` equal to the current one is ignored, so it cannot undo a changed `thickness`.
- Of `color` and `colorIndex`, the form that equals the current color is ignored. When both change, `colorIndex` wins.

A wrong value is not an error. A number of the wrong JSON type is ignored and the member keeps its value. A boolean of the wrong type (`tail`, `visible`, `enabled`) becomes `false`. An unknown or non-string name is handled as described for each member.

## Line end markers

A line end marker is an object with these members, all optional:

| Member | Type | Description |
|---|---|---|
| `shape` | string | The shape of the marker. One of: `arrow`, `concaveCurvedArrow`, `circle`, `dimSlash`, `dimCross`, `lasso`, `hexagon`, `vShaped`, `cone`, `taperedVShaped`, `sShaped`, `rectangle`, `doubleLine`. An unknown name keeps the current shape. |
| `fill` | string | `lineColor` fills the marker with the line color, `white` with white, `none` leaves it open. One of: `lineColor`, `white`, `none`. Any other text sets `lineColor`. |
| `base` | string | The shape of the marker base. One of: `flat`, `open`, `angle`, `arc`. Any other text sets `flat`. |
| `halfTick` | string | Draw the whole marker, or only its left or right half. One of: `full`, `left`, `right`. An unknown name keeps the current value. |
| `tail` | boolean | Add the marker tail. |
| `angle` | integer | The opening angle, in whole degrees. It is stored as a signed 8-bit number, so 200 becomes -56. |
| `length` | number | The length, in page inches. |
| `width` | number | The width, in page inches. |
| `thickness` | number | The line thickness of the marker, in `thicknessUnits`. A changed thickness sets `thicknessBasis` to `custom`. It is stored as whole mils from 0 to 255 (about 6.5 mm or 18.4 points): the value is rounded to whole mils, and a larger value wraps around (300 mils becomes 44 mils). |
| `thicknessBasis` | string | Where the thickness comes from: the line thickness of the object, the dimension line thickness, or the custom `thickness`. One of: `lineThickness`, `dimThickness`, `custom`. An unknown name keeps the current value. |
| `thicknessUnits` | string | The units of `thickness`. One of: `mils`, `points`, `millimeters`. An unknown name keeps the current value. |
| `visible` | boolean | Show the marker. Classes do not store it: `editClass` ignores it and `getClasses` always reports `true` for a class marker. For an object it is stored with the marker, so `beginning` and `end` set it too; `markers.beginningVisible` and `markers.endVisible` set it separately. |

With no stored marker to start from, the members left out start with: `shape` `arrow`, `fill` `lineColor`, `base` `flat`, `halfTick` `full`, `tail` `false`, `angle` 15, `length` 0.125, `width` 0.125, `thickness` 0, `thicknessBasis` `lineThickness`, `thicknessUnits` `mils`, `visible` `false`.

Vectorworks corrects a marker when it is written: `arrow`, `concaveCurvedArrow` and `cone` always get `width` 0, and some shapes reset `base`, `tail`, `fill` or `angle`. A `cone` with `fill` `lineColor` (the default) is stored as an `arrow` with `fill` `none`, so give `cone` with `fill` `white` or `none`. Read the marker back to see the stored values.

**Example**: an open arrow at the end of a line, made a little longer.

```json
{
  "uuid": "<uuid>",
  "markers": {
    "end": {"shape": "arrow", "fill": "none", "length": 0.2, "angle": 20},
    "endVisible": true
  }
}
```

**Where this format is used**

| Tool | Argument |
|---|---|
| [`editClass`](DocumentAccess.md#editclass) | `beginningMarker` |
| [`editClass`](DocumentAccess.md#editclass) | `endMarker` |
| [`setObjectAttributes`](ObjectPrimitives.md#setobjectattributes) | `markers.beginning` |
| [`setObjectAttributes`](ObjectPrimitives.md#setobjectattributes) | `markers.end` |
| [`setPreferences`](DocumentAccess.md#setpreferences) | `values.beginningMarker` (with `category` `defaultAttributes`) |
| [`setPreferences`](DocumentAccess.md#setpreferences) | `values.endMarker` (with `category` `defaultAttributes`) |

**Reading and writing markers**

With [`setObjectAttributes`](ObjectPrimitives.md#setobjectattributes), `markers` also takes `beginningVisible` and `endVisible` (show or hide a marker without changing its other members) and `byClass` (use the markers of the class). The members are applied in this order: `beginning`, `end`, `beginningVisible`, `endVisible`, `byClass`.

- Only lines, arcs, polylines, polygons and the plug-in objects that accept markers can take markers. A circle or any other object refuses them: `applied` reports `false`.
- A marker that is written starts from the current marker of the object. With no marker to read, it starts from the defaults above, so it stays hidden unless `visible` is `true`, or the matching `beginningVisible` or `endVisible` is `true` in the same call.
- Writing `beginning` or `end` switches `byClass` off for the object. `byClass` takes effect only as `true`, and it is applied last, so it wins when both are given. `byClass: false` does nothing.
- `beginningVisible` and `endVisible` need a marker that can be read, which includes a marker written earlier in the same call. When there is none, `applied` reports `false`.
- `applied` has the keys `beginningMarker`, `endMarker`, `beginningMarkerVisible`, `endMarkerVisible` and `markersByClass` for the members given. `markersByClass` appears only when `byClass` is `true`.

[`getObjectAttributes`](ObjectPrimitives.md#getobjectattributes) returns `markers` with `beginning`, `end`, `beginningVisible` and `endVisible`, each only when the object has a marker that can be read, and always `byClass`. [`getClasses`](DocumentAccess.md#getclasses) (`detailed`) returns the markers of a class in the same format. [`getPreferences`](DocumentAccess.md#getpreferences) (`defaultAttributes`) returns `beginningMarker`, `endMarker` (with their real `visible` flag) and `markersByClass`. [`setPreferences`](DocumentAccess.md#setpreferences) writes `beginningMarker` and `endMarker` as partial markers that start from the current default marker, and `markersByClass`, which takes effect only as `true`. Writing `beginningMarker` or `endMarker` switches `markersByClass` off; `markersByClass` is applied after them, so it wins when both are given.

## Drop shadow

A drop shadow is an object with these members, all optional:

| Member | Type | Description |
|---|---|---|
| `enabled` | boolean | Draw the drop shadow. |
| `units` | string | The units of `offset` and `blurRadius`: page inches (`page`) or world units (`world`). One of: `page`, `world`. Any other text sets `page`. |
| `offset` | number | The distance of the shadow from the object, in `units`. |
| `blurRadius` | number | The blur radius, in `units`. |
| `angle` | number | The direction of the shadow, in degrees. |
| `colorIndex` | integer | The shadow color as an index into the document color table. |
| `color` | [color](Common.md#colors) | The shadow color as RGB (see [Colors](Common.md#colors)). When both `color` and `colorIndex` change, `colorIndex` wins. |
| `opacity` | integer | The opacity, 0 to 100. The value is not range-checked: it is stored as an unsigned 8-bit number, so 256 becomes 0 and -1 becomes 255. |
| `byClass` | boolean | Objects only: `true` uses the drop shadow of the class of the object, `false` stops using it. |
| `delete` | boolean | Objects only: remove the drop shadow of the object itself. |

When the object has no drop shadow of its own, the members left out start from the Vectorworks default drop shadow: `enabled` `false`, `units` `page`, `offset` 0.1, `blurRadius` 0.05, `angle` 315, `colorIndex` the index of black in the document, `opacity` 75.

**Example**: a soft black shadow at half opacity, 0.05 page inches from the object.

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

**Where this format is used**

| Tool | Argument |
|---|---|
| [`editClass`](DocumentAccess.md#editclass) | `dropShadow` |
| [`setObjectAttributes`](ObjectPrimitives.md#setobjectattributes) | `dropShadow` |

[`setObjectAttributes`](ObjectPrimitives.md#setobjectattributes) also accepts `true` or `false` for `dropShadow` to switch the drop shadow of an object on or off.

With an object, `byClass` is applied first, then either `delete` or the other members. With `delete` set to `true`, the drop shadow data of the object is removed and none of the other members is applied. `applied` has `dropShadow` for the write of the members (or of `true` or `false`), `dropShadowByClass` when `byClass` is given, and `dropShadowDeleted` when `delete` is `true`. Without `delete`, the members are always written, also when `byClass` is the only member given; they are then written with their current values, and `applied` has `dropShadow`.

[`getObjectAttributes`](ObjectPrimitives.md#getobjectattributes) always returns all members and `byClass`; an object without a drop shadow of its own (also after `delete`) reports the default values above. [`getClasses`](DocumentAccess.md#getclasses) (`detailed`) returns the drop shadow of a class in the same format. [`getPreferences`](DocumentAccess.md#getpreferences) (`defaultAttributes`) returns the drop shadow of the document as `documentDropShadow` in this format. It is read-only: [`setPreferences`](DocumentAccess.md#setpreferences) does not write it.

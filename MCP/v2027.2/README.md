**English** • [Deutsch](../../MCP.de/v2027.2/README.md) • [日本語](../../MCP.ja/v2027.2/README.md)

# Vectorworks MCP server — tool reference for Vectorworks 2027 Update 2

This reference documents the tools of the Vectorworks MCP server: what each tool does, the arguments it takes and what it returns. The 154 tools are organized in 18 tool groups, plus the 3 always available meta-tools of the Core group. There is one page per area, with a table of contents at the top of every page and the same layout for every group and tool.

For what MCP is and how the server runs, see [Vectorworks MCP Server](../README.md).

## Table of contents

- [Getting started](#getting-started)
- [Conventions](#conventions)
- [Tool tree](#tool-tree)
- [Contents by category](#contents-by-category)
  - [Shared conventions and formats](#shared-conventions-and-formats)
  - [Document and selection](#document-and-selection)
  - [Objects and geometry](#objects-and-geometry)
  - [Annotation](#annotation)
  - [Industry objects](#industry-objects)
  - [Resources and data](#resources-and-data)
  - [Automation and user interface](#automation-and-user-interface)
- [Index A–Z](#index-az)
- [Page layout](#page-layout)
- [Statistics](#statistics)

## Getting started

1. In Vectorworks, choose **Tools > MCP Server > Start MCP Server...** (in the default workspaces except Viewer), select the tools mode and the port (default 8765), and click **Start Server**. The dialog shows the server URL, for example `http://localhost:8765`; **Copy URL** copies it. If the port is busy, the server tries up to 9 more ports and the dialog shows the one in use. Add the URL as an HTTP MCP server in your MCP client, and open a drawing in Vectorworks: without an open drawing the tools return `no active Vectorworks document`. See [Start and Connect](../README.md#start-and-connect) for the dialog and the server.
2. The tool list (`tools/list`) shows the tools of the active groups only: the [Core](Common.md#core-group) meta-tools and the groups active by default, [Document](DocumentAccess.md#document), [Selection](DocumentAccess.md#selection), [IFC](IFC.md#ifc), [Objects](ObjectPrimitives.md#objects). The tools mode that you chose decides which groups the server offers: **Enable all tools** (the default) offers every group, **Enable all without scripting tools** every group except [Scripting](Scripting.md#scripting), and **Enable scripting tools only** only the Core meta-tools and the Scripting group, which is active at once. See [Tool groups and activation](Common.md#tool-groups-and-activation).
3. Call [`listToolGroups`](Common.md#listtoolgroups) to see every group, and [`activateToolGroups`](Common.md#activatetoolgroups) to switch on the groups you need, such as [Architecture](ObjectsArchitect.md#architecture). Then refresh the tool list.
4. Call the tools. Each successful call that changes the drawing is one undo step (`MCP: <tool>`; scripts `MCP: script`) that one Edit > Undo reverts; the interactive tools and menu commands record their own undo steps, as user input does. Use [`runToolBatch`](Common.md#runtoolbatch) to make several edit calls one undo step; it refuses the tools that record their own undo steps (`activateTool`, `setToolMode`, `setToolModes`, `sendToolPointer`, `sendToolAction`, `setOIPValues`, `pressOIPButton` and `runMenuCommand`), the script runs `runPythonScript` and `runScript`, the meta-tools and the tools of inactive groups. See [Undo](Common.md#undo).

For example, activate the Architecture group and draw a wall:

```json
{
  "name": "activateToolGroups",
  "arguments": {"groups": ["architecture"]}
}
```

```json
{
  "name": "createWall",
  "arguments": {
    "start": {"x": 0, "y": 0},
    "end": {"x": 5000, "y": 0},
    "thickness": 200
  }
}
```

`createWall` returns the [object reference](Common.md#object-references) of the new wall, whose `uuid` the next calls use. Lengths are in the units of the drawing (millimeters in this example).

## Conventions

The [Common](Common.md) page describes the conventions that every tool follows; [Attributes](Attributes.md) describes the line end marker and drop shadow formats.

| Topic | Convention |
|---|---|
| [Tool groups and activation](Common.md#tool-groups-and-activation) | Only the tools of active groups are listed. `activateToolGroups` switches groups on until the server is stopped, for every client. |
| [Results and errors](Common.md#results-and-errors) | Every tool returns one JSON object; a failure returns `{ "err": "..." }`. |
| [Object references](Common.md#object-references) | Objects are passed as `uuid` (preferred), `name` or `index`, and returned with `uuid`, `type`, `typeName` and `name`. |
| [Points, rectangles and colors](Common.md#points-rectangles-and-colors) | `{ x, y }`, `{ left, top, right, bottom }` and `{ r, g, b }` with channels 0 to 255. |
| [Units and angles](Common.md#units-and-angles) | Lengths in world units (the units of the drawing), angles in radians, unless a tool says otherwise. |
| [Creation options](Common.md#creation-options) | Most create tools accept `class`, `useClassAttributes`, `name` and `select`. |
| [Applied settings](Common.md#applied-settings) | Tools that write several settings report each one in `applied`. |
| [Plug-in parameters](Common.md#plug-in-parameters) | Parameters of plug-in objects are read and written by universal name, with `params`. |
| [Paging](Common.md#paging) | Long lists take `limit`, `offset` and `countOnly` and report `count`, `truncated` and `nextOffset`. |
| [Effects and risk levels](Common.md#effects-and-risk-levels) | Each tool is read-only, an edit, interactive or a script run, with a risk level low, medium or high. |
| [Undo](Common.md#undo) | Each edit call is one undo step `MCP: <tool>` (scripts `MCP: script`); a failed edit call is reverted and reports `rolledBack`. Interactive tools record their own undo steps. |
| [Line end markers and drop shadows](Attributes.md) | Partial objects: only the members given are changed. |

## Tool tree

The pages of this reference and the tool groups they document, in the order of the tool folders. Groups marked *active* are active by default.

```text
Vectorworks MCP server
├── Attributes                    → Attributes.md       line end markers, drop shadows
├── Common                        → Common.md           conventions
│   └── Core                      (3 tools, always active)
├── DocumentAccess                → DocumentAccess.md
│   ├── Document                  (17 tools, active)
│   └── Selection                 (3 tools, active)
├── IFC                           → IFC.md
│   ├── IFC                       (4 tools, active)
│   └── IFC Data Mapping          (2 tools)
├── MenuAccess                    → MenuAccess.md
│   └── Menus                     (4 tools)
├── ObjectPrimitives              → ObjectPrimitives.md
│   ├── Draw2D                    (15 tools)
│   └── Objects                   (12 tools, active)
├── Objects3D                     → Objects3D.md
│   └── 3D Modeling               (16 tools)
├── ObjectsAnnotation             → ObjectsAnnotation.md
│   ├── Annotation                (8 tools)
│   └── Dimensioning              (8 tools)
├── ObjectsArchitect              → ObjectsArchitect.md
│   └── Architecture              (9 tools)
├── ObjectsConnectCAD             → ObjectsConnectCAD.md
│   └── ConnectCAD                (10 tools)
├── ObjectsLandmark               → ObjectsLandmark.md
│   └── Landmark                  (10 tools)
├── ObjectsSpotlight              → ObjectsSpotlight.md
│   └── Spotlight                 (5 tools)
├── OIPAccess                     → OIPAccess.md
│   └── Object Info               (3 tools)
├── Resources                     → Resources.md
│   └── Resources                 (11 tools)
├── Scripting                     → Scripting.md
│   └── Scripting                 (7 tools)
└── ToolAccess                    → ToolAccess.md
    └── InteractiveTools          (10 tools)
```

## Contents by category

Every page, group and tool, by subject. Each tool links to its description.

### Shared conventions and formats

How every tool is called and what the shared value formats look like.

- **[Common](Common.md)** — The conventions that every tool of the Vectorworks MCP server follows: calls and results, object references, points and colors, units, creation options, applied settings, plug-in parameters, paging, effects, risk levels and undo.
  - **[Core](Common.md#core-group)** (`core`, 3 tools, always active) — Discover and activate tool groups, and run several tool calls as one undo step.
    - [`listToolGroups`](Common.md#listtoolgroups) — List all tool groups, active and inactive, with their activation state and, optionally, their tools.
    - [`activateToolGroups`](Common.md#activatetoolgroups) — Activate tool groups so that their tools appear in the tool list, until the server is stopped.
    - [`runToolBatch`](Common.md#runtoolbatch) — Run several tool calls as one undo step, all or nothing.
  - Conventions: [Calling a tool](Common.md#calling-a-tool) · [Results and errors](Common.md#results-and-errors) · [Object references](Common.md#object-references) · [Points, rectangles and colors](Common.md#points-rectangles-and-colors) · [Units and angles](Common.md#units-and-angles) · [Creation options](Common.md#creation-options) · [Applied settings](Common.md#applied-settings) · [Plug-in parameters](Common.md#plug-in-parameters) · [Paging](Common.md#paging) · [Effects and risk levels](Common.md#effects-and-risk-levels) · [Undo](Common.md#undo)
- **[Attributes](Attributes.md)** — The value formats of line end markers and drop shadows. They are shared by the tools that read and write the graphical attributes of classes and objects.
  - Formats: [Line end markers](Attributes.md#line-end-markers) · [Drop shadow](Attributes.md#drop-shadow)

### Document and selection

The drawing as a whole: layers, stories, classes, units, view, preferences and the selection.

- **[DocumentAccess](DocumentAccess.md)** — Tools for the active drawing as a whole and for the current selection: the document summary, layers, stories, classes, units, the view and the document preferences, and bulk edits of the selected objects.
  - **[Document](DocumentAccess.md#document)** (`document`, 17 tools, active by default) — The active drawing: document summary, layers, stories, classes, units, view and document preferences.
    - [`getDocumentInfo`](DocumentAccess.md#getdocumentinfo) — Returns a summary of the active document: file, counts, page bounds, view center and user origin.
    - [`getLayers`](DocumentAccess.md#getlayers) — Lists the layers with their kind, visibility, scale, elevation, object count and bounds.
    - [`createLayer`](DocumentAccess.md#createlayer) — Creates a design layer or a sheet layer.
    - [`editLayer`](DocumentAccess.md#editlayer) — Changes the properties of a layer: name, visibility, scale, elevation, thickness and more.
    - [`getStories`](DocumentAccess.md#getstories) — Lists the stories (building floors) with their levels, lowest first.
    - [`createStory`](DocumentAccess.md#createstory) — Creates one or more stories with their levels.
    - [`editStory`](DocumentAccess.md#editstory) — Changes a story, the level types of the document or its default story levels.
    - [`getClasses`](DocumentAccess.md#getclasses) — Lists the classes of the document and names the special classes.
    - [`createClass`](DocumentAccess.md#createclass) — Creates a class, or returns the existing class of that name.
    - [`editClass`](DocumentAccess.md#editclass) — Changes a class: description, visibility, pen, fill, markers, drop shadow and more.
    - [`setActiveContext`](DocumentAccess.md#setactivecontext) — Sets the active layer and class and how the other layers and classes are shown.
    - [`getUnits`](DocumentAccess.md#getunits) — Returns the primary and secondary unit settings of the document.
    - [`setUnits`](DocumentAccess.md#setunits) — Changes the primary or secondary unit settings of the document.
    - [`convertUnits`](DocumentAccess.md#convertunits) — Converts lengths between world units and document units.
    - [`setView`](DocumentAccess.md#setview) — Moves the view, sets the zoom, moves the user origin or redraws the page.
    - [`getPreferences`](DocumentAccess.md#getpreferences) — Reads one category of document preferences.
    - [`setPreferences`](DocumentAccess.md#setpreferences) — Writes document preferences of one category.
  - **[Selection](DocumentAccess.md#selection)** (`selection`, 3 tools, active by default) — List the current selection and move, rotate, scale, duplicate, group, delete or re-class it in bulk.
    - [`getSelection`](DocumentAccess.md#getselection) — Lists the selected objects on every layer and the bounds of the selection.
    - [`selectObjects`](DocumentAccess.md#selectobjects) — Selects or deselects objects by criteria or by UUID, or all or none.
    - [`editSelection`](DocumentAccess.md#editselection) — Moves, rotates, scales, duplicates, groups, deletes or re-classes the selection.

### Objects and geometry

Any object, 2D primitives, text and 3D geometry.

- **[ObjectPrimitives](ObjectPrimitives.md)** — Tools for any object of the drawing (finding, inspecting, styling, transforming, plug-in parameters and records) and for creating, editing, measuring and combining 2D primitives and text.
  - **[Draw2D](ObjectPrimitives.md#draw2d)** (`draw2d`, 15 tools, inactive by default) — Create, edit, measure and combine 2D primitives, and create, read and edit text objects.
    - [`createLine`](ObjectPrimitives.md#createline) — Creates a straight line between two points.
    - [`createRectangle`](ObjectPrimitives.md#createrectangle) — Creates a rectangle, optionally rotated and with rounded corners.
    - [`createCircle`](ObjectPrimitives.md#createcircle) — Creates a circle from a center and radius, or through three points.
    - [`createArc`](ObjectPrimitives.md#createarc) — Creates a circular arc from a center, radius and angles, or through three points.
    - [`createPolygon`](ObjectPrimitives.md#createpolygon) — Creates a polygon from points, or a regular polygon.
    - [`createPolyline`](ObjectPrimitives.md#createpolyline) — Creates a polyline from vertices of any vertex type, or a rounded shape.
    - [`createLocus`](ObjectPrimitives.md#createlocus) — Creates a 2D locus (reference point).
    - [`getGeometry`](ObjectPrimitives.md#getgeometry) — Reads the type-specific geometry of a 2D primitive.
    - [`setGeometry`](ObjectPrimitives.md#setgeometry) — Edits the geometry of a 2D primitive.
    - [`editVertices`](ObjectPrimitives.md#editvertices) — Adds, inserts, changes, deletes, reverses or replaces the vertices of a polygon or polyline.
    - [`queryGeometry`](ObjectPrimitives.md#querygeometry) — Answers geometric questions about a 2D primitive: closest point, distance, containment, intersections, tangents and measurements along curves.
    - [`combineShapes`](ObjectPrimitives.md#combineshapes) — Combines two 2D shapes with a Boolean operation: union, intersection, difference or symmetric difference.
    - [`createText`](ObjectPrimitives.md#createtext) — Creates a text object.
    - [`getText`](ObjectPrimitives.md#gettext) — Reads a text object: its content, character formatting, style and layout.
    - [`editText`](ObjectPrimitives.md#edittext) — Edits the content and formatting of a text object.
  - **[Objects](ObjectPrimitives.md#objects)** (`objects`, 12 tools, active by default) — Find, inspect and edit any object: attributes, transforms, containers, plug-in parameters and records.
    - [`findObjects`](ObjectPrimitives.md#findobjects) — Finds the objects that match a criteria string.
    - [`getObjectsAtPoint`](ObjectPrimitives.md#getobjectsatpoint) — Finds the objects at a point.
    - [`getObjectInfo`](ObjectPrimitives.md#getobjectinfo) — Returns the identity, class, layer, bounds, state and container of an object.
    - [`getObjectAttributes`](ObjectPrimitives.md#getobjectattributes) — Returns the graphical attributes of an object.
    - [`setObjectAttributes`](ObjectPrimitives.md#setobjectattributes) — Sets graphical attributes of an object: pen, fill, opacity, markers, drop shadow and more.
    - [`copyAttributes`](ObjectPrimitives.md#copyattributes) — Copies the graphical attributes of one object onto other objects.
    - [`editObject`](ObjectPrimitives.md#editobject) — Moves, rotates, scales, mirrors, duplicates, regroups, converts, resets or deletes an object, or changes its name and class.
    - [`getObjectParameters`](ObjectPrimitives.md#getobjectparameters) — Reads the parameters of a plug-in object.
    - [`getObjectRecords`](ObjectPrimitives.md#getobjectrecords) — Reads the data records attached to an object.
    - [`setObjectParameter`](ObjectPrimitives.md#setobjectparameter) — Writes one or more parameters of a plug-in object.
    - [`getPluginDefinition`](ObjectPrimitives.md#getplugindefinition) — Describes an installed plug-in object: its kind, parameters and pop-up choices.
    - [`createPluginObject`](ObjectPrimitives.md#createpluginobject) — Creates a plug-in object that has no dedicated create tool.
- **[Objects3D](Objects3D.md)** — Tools to create, read and edit 3D geometry: solids, 3D polygons, meshes, NURBS curves and surfaces, and surface models.
  - **[3D Modeling](Objects3D.md#3d-modeling)** (`3d-modeling`, 16 tools, inactive by default) — Create, read and edit solids, 3D polygons, meshes, NURBS curves and surfaces, and surface models.
    - [`createExtrude`](Objects3D.md#createextrude) — Creates an extrude, a multiple extrude or a tapered extrude.
    - [`createSolidPrimitive`](Objects3D.md#createsolidprimitive) — Creates a sphere, ellipsoid, hemisphere, cone, box, cylinder or torus.
    - [`createSweep`](Objects3D.md#createsweep) — Creates a sweep: 2D profiles revolved about an axis.
    - [`combineSolids`](Objects3D.md#combinesolids) — Combines two solids into a Generic Solid by union, intersection or difference.
    - [`createShell`](Objects3D.md#createshell) — Creates a shell by thickening a NURBS surface or hollowing a solid.
    - [`convertSolid`](Objects3D.md#convertsolid) — Creates a copy of a solid converted to a Generic Solid or a mesh.
    - [`getSolid`](Objects3D.md#getsolid) — Reads a solid: its kind, 3D bounds, parameters and Generic Solid history.
    - [`editSolid`](Objects3D.md#editsolid) — Moves, rotates, scales, re-orients or resizes a solid.
    - [`create3DPolygon`](Objects3D.md#create3dpolygon) — Creates a 3D polygon from 3D points, from 2D points at a height, or from a rectangle.
    - [`createMesh`](Objects3D.md#createmesh) — Creates a mesh from vertices and faces, from polygons or from a group of 3D polygons.
    - [`createNurbsCurve`](Objects3D.md#createnurbscurve) — Creates a NURBS curve from control points or fit points.
    - [`createNurbsSurface`](Objects3D.md#createnurbssurface) — Creates a NURBS surface from its control net.
    - [`createSurfaceModel`](Objects3D.md#createsurfacemodel) — Creates a loft, rail sweep, revolve or extrude-along-path surface model from existing objects.
    - [`get3DGeometry`](Objects3D.md#get3dgeometry) — Reads a 3D polygon, mesh, NURBS curve or NURBS surface.
    - [`edit3DGeometry`](Objects3D.md#edit3dgeometry) — Edits a 3D polygon, mesh, NURBS curve or NURBS surface.
    - [`convertTo3D`](Objects3D.md#convertto3d) — Converts a copy of an object to 3D polygons, a mesh or a Generic Solid.

### Annotation

Data tags, title blocks and dimensions.

- **[ObjectsAnnotation](ObjectsAnnotation.md)** — Tools for annotations: data tags, title block borders and the title block project data, and dimensions with center marks.
  - **[Annotation](ObjectsAnnotation.md#annotation)** (`annotation`, 8 tools, inactive by default) — Data tags, title block borders and the title block project data of the document.
    - [`createDataTag`](ObjectsAnnotation.md#createdatatag) — Creates a data tag, optionally attached to an object.
    - [`createTitleBlock`](ObjectsAnnotation.md#createtitleblock) — Creates a title block border.
    - [`getAnnotationObject`](ObjectsAnnotation.md#getannotationobject) — Reads a data tag or a title block border.
    - [`setAnnotationObject`](ObjectsAnnotation.md#setannotationobject) — Edits a data tag or a title block border.
    - [`tagObject`](ObjectsAnnotation.md#tagobject) — Attaches a data tag to an object, or detaches it.
    - [`getObjectTags`](ObjectsAnnotation.md#getobjecttags) — Lists the data tags attached to an object.
    - [`getProjectData`](ObjectsAnnotation.md#getprojectdata) — Reads the title block project data of the document.
    - [`setProjectData`](ObjectsAnnotation.md#setprojectdata) — Writes the title block project data of the document.
  - **[Dimensioning](ObjectsAnnotation.md#dimensioning)** (`dimensioning`, 8 tools, inactive by default) — Linear, angular, arc length and radial dimensions, and center marks.
    - [`createLinearDimension`](ObjectsAnnotation.md#createlineardimension) — Creates a constrained, horizontal, vertical, unconstrained or ordinate linear dimension.
    - [`createAngularDimension`](ObjectsAnnotation.md#createangulardimension) — Creates an angular dimension.
    - [`createArcLengthDimension`](ObjectsAnnotation.md#createarclengthdimension) — Creates an arc length dimension.
    - [`createRadialDimension`](ObjectsAnnotation.md#createradialdimension) — Creates a radial or diametrical dimension.
    - [`createCenterMark`](ObjectsAnnotation.md#createcentermark) — Creates a center mark for a circular feature.
    - [`getDimension`](ObjectsAnnotation.md#getdimension) — Reads a dimension: its kind, measured points, value and text settings.
    - [`setDimension`](ObjectsAnnotation.md#setdimension) — Edits a dimension.
    - [`getObjectDimensions`](ObjectsAnnotation.md#getobjectdimensions) — Lists the dimensions associated with an object.

### Industry objects

Architecture, landscape, entertainment lighting and AV system objects.

- **[ObjectsArchitect](ObjectsArchitect.md)** — Tools for BIM building elements: walls, slabs, roofs, doors, windows, columns and stairs.
  - **[Architecture](ObjectsArchitect.md#architecture)** (`architecture`, 9 tools, inactive by default) — BIM building elements: walls, slabs, roofs, doors, windows, columns and stairs.
    - [`createWall`](ObjectsArchitect.md#createwall) — Creates a straight or round wall.
    - [`createSlab`](ObjectsArchitect.md#createslab) — Creates a slab from a 2D boundary object.
    - [`createRoof`](ObjectsArchitect.md#createroof) — Creates a polygonal roof.
    - [`createDoor`](ObjectsArchitect.md#createdoor) — Creates a free-standing door.
    - [`createWindow`](ObjectsArchitect.md#createwindow) — Creates a free-standing window.
    - [`createColumn`](ObjectsArchitect.md#createcolumn) — Creates a column.
    - [`createStair`](ObjectsArchitect.md#createstair) — Creates a stair.
    - [`getArchitectureObject`](ObjectsArchitect.md#getarchitectureobject) — Reads the properties of a wall, slab, roof, door, window, column or stair.
    - [`setArchitectureObject`](ObjectsArchitect.md#setarchitectureobject) — Edits a wall, slab, roof, door, window, column or stair.
- **[ObjectsLandmark](ObjectsLandmark.md)** — Tools for site and landscape objects: plants, hardscapes, landscape areas, site models, site modifiers, stakes, property lines and existing trees.
  - **[Landmark](ObjectsLandmark.md#landmark)** (`landmark`, 10 tools, inactive by default) — Plants, hardscapes, landscape areas, site models, site modifiers, stakes, property lines and existing trees.
    - [`createPlant`](ObjectsLandmark.md#createplant) — Creates a plant at a point or along a path.
    - [`createHardscape`](ObjectsLandmark.md#createhardscape) — Creates a hardscape from a 2D path object.
    - [`createLandscapeArea`](ObjectsLandmark.md#createlandscapearea) — Creates a landscape area from a 2D path object.
    - [`createSiteModifier`](ObjectsLandmark.md#createsitemodifier) — Creates a site modifier from a 2D path object.
    - [`createPropertyLine`](ObjectsLandmark.md#createpropertyline) — Creates a property line from a closed 2D path object.
    - [`createSiteModel`](ObjectsLandmark.md#createsitemodel) — Creates an empty site model.
    - [`createStake`](ObjectsLandmark.md#createstake) — Creates a stake (elevation point).
    - [`createExistingTree`](ObjectsLandmark.md#createexistingtree) — Creates an existing tree.
    - [`getLandmarkObject`](ObjectsLandmark.md#getlandmarkobject) — Reads the properties of a site or landscape object.
    - [`setLandmarkObject`](ObjectsLandmark.md#setlandmarkobject) — Edits a site or landscape object.
- **[ObjectsSpotlight](ObjectsSpotlight.md)** — Tools for Spotlight lighting devices and the GDTF fixture types (General Device Type Format) they use.
  - **[Spotlight](ObjectsSpotlight.md#spotlight)** (`spotlight`, 5 tools, inactive by default) — Spotlight lighting devices and the GDTF fixture types they use.
    - [`listGDTFs`](ObjectsSpotlight.md#listgdtfs) — Lists the available GDTF fixture types and their DMX modes.
    - [`importGDTF`](ObjectsSpotlight.md#importgdtf) — Imports a .gdtf file into the drawing as a GDTF fixture type.
    - [`createLightingDevice`](ObjectsSpotlight.md#createlightingdevice) — Creates a lighting device, optionally with a GDTF fixture type.
    - [`getLightingDevice`](ObjectsSpotlight.md#getlightingdevice) — Reads a lighting device.
    - [`setLightingDevice`](ObjectsSpotlight.md#setlightingdevice) — Edits a lighting device.
- **[ObjectsConnectCAD](ObjectsConnectCAD.md)** — Tools for ConnectCAD schematic devices, their sockets and their device types, and the signal and connector types they use.
  - **[ConnectCAD](ObjectsConnectCAD.md#connectcad)** (`connectcad`, 10 tools, inactive by default) — ConnectCAD schematic devices, sockets and device types, built from JSON device descriptions.
    - [`listConnectCADSignals`](ObjectsConnectCAD.md#listconnectcadsignals) — Lists the ConnectCAD signal types.
    - [`listConnectCADConnectors`](ObjectsConnectCAD.md#listconnectcadconnectors) — Lists the ConnectCAD connector types and their pins.
    - [`validateConnectCADDevice`](ObjectsConnectCAD.md#validateconnectcaddevice) — Checks a device description without creating anything.
    - [`createConnectCADDevice`](ObjectsConnectCAD.md#createconnectcaddevice) — Creates a schematic device with all its sockets from a device description.
    - [`createConnectCADDevices`](ObjectsConnectCAD.md#createconnectcaddevices) — Creates several schematic devices in a row in one operation.
    - [`getConnectCADDevice`](ObjectsConnectCAD.md#getconnectcaddevice) — Reads a ConnectCAD device and its sockets.
    - [`addConnectCADSocket`](ObjectsConnectCAD.md#addconnectcadsocket) — Adds a socket to a device.
    - [`setConnectCADSocket`](ObjectsConnectCAD.md#setconnectcadsocket) — Edits a socket.
    - [`createConnectCADDeviceType`](ObjectsConnectCAD.md#createconnectcaddevicetype) — Creates the device-type symbol of a device.
    - [`getConnectCADDeviceType`](ObjectsConnectCAD.md#getconnectcaddevicetype) — Reads the Device Definition record of a device-type symbol.

### Resources and data

Resources, worksheets and IFC data.

- **[Resources](Resources.md)** — Tools for the resources of the drawing and of external content (libraries, files, other documents), and for worksheets.
  - **[Resources](Resources.md#resources)** (`resources`, 11 tools, inactive by default) — List, import, create, inspect, edit and apply resources; read and edit worksheets.
    - [`getResourceTypes`](Resources.md#getresourcetypes) — Lists the resource types and the standard content folders.
    - [`getResources`](Resources.md#getresources) — Lists the resources of one type from the drawing, a library, a file or another document.
    - [`getResource`](Resources.md#getresource) — Reads one resource of the drawing.
    - [`importResource`](Resources.md#importresource) — Imports an external resource into the drawing.
    - [`editResource`](Resources.md#editresource) — Renames, describes, moves, duplicates or deletes a resource.
    - [`createResource`](Resources.md#createresource) — Creates an empty resource.
    - [`getResourceDetails`](Resources.md#getresourcedetails) — Reads what a resource holds: hatch levels, gradient stops, line type dashes and more.
    - [`setResourceDetails`](Resources.md#setresourcedetails) — Changes what a resource holds.
    - [`applyResource`](Resources.md#applyresource) — Applies a texture, style or data visualization to an object.
    - [`getWorksheet`](Resources.md#getworksheet) — Reads a worksheet: its size, cells, formats and database rows.
    - [`editWorksheet`](Resources.md#editworksheet) — Changes a worksheet with a list of actions.
- **[IFC](IFC.md)** — Read-only access to the IFC (Industry Foundation Classes) data of the drawing: the IFC entity and property sets of objects, property-set definitions, and the IFC Data Manager mappings of the document.
  - **[IFC](IFC.md#ifc)** (`ifc`, 4 tools, active by default) — Read-only IFC data: the IFC entity and property sets of objects, the IFC property-set definitions (standard and custom) and the custom property sets of the document.
    - [`getObjectIFCData`](IFC.md#getobjectifcdata) — Reads the IFC data of an object as IFC export computes it.
    - [`getIFCPsetDefinition`](IFC.md#getifcpsetdefinition) — Reads one IFC property-set definition by name.
    - [`listIFCPsets`](IFC.md#listifcpsets) — Lists the IFC property sets applicable to an IFC entity type.
    - [`listIFCCustomPsets`](IFC.md#listifccustompsets) — Lists the custom IFC property-set definitions of the document.
  - **[IFC Data Mapping](IFC.md#ifc-data-mapping)** (`ifc-data-mapping`, 2 tools, inactive by default) — Read the IFC Data Manager mapping definitions of the active document.
    - [`listIFCMappingObjects`](IFC.md#listifcmappingobjects) — Lists the mapping objects of the active Data Manager mapping.
    - [`getIFCMapping`](IFC.md#getifcmapping) — Reads the Data Manager mapping of one mapping object.

### Automation and user interface

Scripts, interactive tools, the Object Info palette and menu commands.

- **[Scripting](Scripting.md)** — Tools to run Python scripts in Vectorworks, read and save Python script resources, and look up the Python `api` module that scripts use.
  - **[Scripting](Scripting.md#scripting)** (`scripting`, 7 tools, inactive by default) — Run Python scripts, read and save Python script resources, and look up the Python `api` module.
    - [`listScripts`](Scripting.md#listscripts) — Lists the script resources of the document.
    - [`getScript`](Scripting.md#getscript) — Reads a script resource without running it.
    - [`saveScript`](Scripting.md#savescript) — Creates or updates a Python script resource without running it.
    - [`describePythonApi`](Scripting.md#describepythonapi) — Returns the help text of the Python `api` module or one of its names.
    - [`getPythonApiGuide`](Scripting.md#getpythonapiguide) — Returns one section of the guide for writing Python scripts.
    - [`runPythonScript`](Scripting.md#runpythonscript) — Runs Python code in Vectorworks.
    - [`runScript`](Scripting.md#runscript) — Runs a saved Python script resource.
- **[ToolAccess](ToolAccess.md)** — Tools that operate the interactive Vectorworks tools of the tool palettes like a user: activate a tool, set its modes and click in the drawing.
  - **[InteractiveTools](ToolAccess.md#interactivetools)** (`interactivetools`, 10 tools, inactive by default) — Operate the interactive Vectorworks tools of the tool palettes like a user.
    - [`getTools`](ToolAccess.md#gettools) — Lists the Vectorworks tools.
    - [`getTool`](ToolAccess.md#gettool) — Returns one tool with its declared mode buttons.
    - [`getActiveTool`](ToolAccess.md#getactivetool) — Returns the state of the active tool.
    - [`activateTool`](ToolAccess.md#activatetool) — Activates a tool.
    - [`getToolModes`](ToolAccess.md#gettoolmodes) — Reads the live mode bar of the active tool.
    - [`setToolMode`](ToolAccess.md#settoolmode) — Changes one mode of the active tool.
    - [`setToolModes`](ToolAccess.md#settoolmodes) — Sets several modes of the active tool.
    - [`sendToolPointer`](ToolAccess.md#sendtoolpointer) — Clicks, double-clicks, hovers or drags in the drawing with the active tool.
    - [`sendToolAction`](ToolAccess.md#sendtoolaction) — Finishes or cancels the action of the active tool, or removes its last point.
    - [`convertToolCoordinates`](ToolAccess.md#converttoolcoordinates) — Converts points between model space and the view of the active pane.
- **[OIPAccess](OIPAccess.md)** — Tools that read and operate the Object Info palette for the current selection, like a user.
  - **[Object Info](OIPAccess.md#object-info)** (`object-info`, 3 tools, inactive by default) — Read and operate the Object Info palette for the current selection, like a user.
    - [`getOIPControls`](OIPAccess.md#getoipcontrols) — Lists the controls of one pane of the Object Info palette.
    - [`setOIPValues`](OIPAccess.md#setoipvalues) — Sets controls of the Object Info palette, as a user does.
    - [`pressOIPButton`](OIPAccess.md#pressoipbutton) — Presses a button of the Object Info palette.
- **[MenuAccess](MenuAccess.md)** — Tools that read the Vectorworks menus, check whether a command can run, and run menu commands as if the user chose them.
  - **[Menus](MenuAccess.md#menus)** (`menus`, 4 tools, inactive by default) — Find menu commands, read the menu bar, check whether a command can run now, and run it.
    - [`findMenuCommands`](MenuAccess.md#findmenucommands) — Finds installed menu commands by text and by workspace.
    - [`getMenus`](MenuAccess.md#getmenus) — Reads the menu bar of the current workspace, one menu, or the items of a chunk.
    - [`getMenuStatus`](MenuAccess.md#getmenustatus) — Tells whether a menu command or chunk item can run now, and why not.
    - [`runMenuCommand`](MenuAccess.md#runmenucommand) — Runs a menu command or chunk item as if the user chose it.

## Index A–Z

[A](#index-a) · [C](#index-c) · [D](#index-d) · [E](#index-e) · [F](#index-f) · [G](#index-g) · [I](#index-i) · [L](#index-l) · [P](#index-p) · [Q](#index-q) · [R](#index-r) · [S](#index-s) · [T](#index-t) · [V](#index-v)

### Index A

| Tool | Group | Page | Summary |
|---|---|---|---|
| [`activateTool`](ToolAccess.md#activatetool) | [InteractiveTools](ToolAccess.md#interactivetools) | [ToolAccess](ToolAccess.md) | Activates a tool. |
| [`activateToolGroups`](Common.md#activatetoolgroups) | [Core](Common.md#core-group) | [Common](Common.md) | Activate tool groups so that their tools appear in the tool list, until the server is stopped. |
| [`addConnectCADSocket`](ObjectsConnectCAD.md#addconnectcadsocket) | [ConnectCAD](ObjectsConnectCAD.md#connectcad) | [ObjectsConnectCAD](ObjectsConnectCAD.md) | Adds a socket to a device. |
| [`applyResource`](Resources.md#applyresource) | [Resources](Resources.md#resources) | [Resources](Resources.md) | Applies a texture, style or data visualization to an object. |

### Index C

| Tool | Group | Page | Summary |
|---|---|---|---|
| [`combineShapes`](ObjectPrimitives.md#combineshapes) | [Draw2D](ObjectPrimitives.md#draw2d) | [ObjectPrimitives](ObjectPrimitives.md) | Combines two 2D shapes with a Boolean operation: union, intersection, difference or symmetric difference. |
| [`combineSolids`](Objects3D.md#combinesolids) | [3D Modeling](Objects3D.md#3d-modeling) | [Objects3D](Objects3D.md) | Combines two solids into a Generic Solid by union, intersection or difference. |
| [`convertSolid`](Objects3D.md#convertsolid) | [3D Modeling](Objects3D.md#3d-modeling) | [Objects3D](Objects3D.md) | Creates a copy of a solid converted to a Generic Solid or a mesh. |
| [`convertTo3D`](Objects3D.md#convertto3d) | [3D Modeling](Objects3D.md#3d-modeling) | [Objects3D](Objects3D.md) | Converts a copy of an object to 3D polygons, a mesh or a Generic Solid. |
| [`convertToolCoordinates`](ToolAccess.md#converttoolcoordinates) | [InteractiveTools](ToolAccess.md#interactivetools) | [ToolAccess](ToolAccess.md) | Converts points between model space and the view of the active pane. |
| [`convertUnits`](DocumentAccess.md#convertunits) | [Document](DocumentAccess.md#document) | [DocumentAccess](DocumentAccess.md) | Converts lengths between world units and document units. |
| [`copyAttributes`](ObjectPrimitives.md#copyattributes) | [Objects](ObjectPrimitives.md#objects) | [ObjectPrimitives](ObjectPrimitives.md) | Copies the graphical attributes of one object onto other objects. |
| [`create3DPolygon`](Objects3D.md#create3dpolygon) | [3D Modeling](Objects3D.md#3d-modeling) | [Objects3D](Objects3D.md) | Creates a 3D polygon from 3D points, from 2D points at a height, or from a rectangle. |
| [`createAngularDimension`](ObjectsAnnotation.md#createangulardimension) | [Dimensioning](ObjectsAnnotation.md#dimensioning) | [ObjectsAnnotation](ObjectsAnnotation.md) | Creates an angular dimension. |
| [`createArc`](ObjectPrimitives.md#createarc) | [Draw2D](ObjectPrimitives.md#draw2d) | [ObjectPrimitives](ObjectPrimitives.md) | Creates a circular arc from a center, radius and angles, or through three points. |
| [`createArcLengthDimension`](ObjectsAnnotation.md#createarclengthdimension) | [Dimensioning](ObjectsAnnotation.md#dimensioning) | [ObjectsAnnotation](ObjectsAnnotation.md) | Creates an arc length dimension. |
| [`createCenterMark`](ObjectsAnnotation.md#createcentermark) | [Dimensioning](ObjectsAnnotation.md#dimensioning) | [ObjectsAnnotation](ObjectsAnnotation.md) | Creates a center mark for a circular feature. |
| [`createCircle`](ObjectPrimitives.md#createcircle) | [Draw2D](ObjectPrimitives.md#draw2d) | [ObjectPrimitives](ObjectPrimitives.md) | Creates a circle from a center and radius, or through three points. |
| [`createClass`](DocumentAccess.md#createclass) | [Document](DocumentAccess.md#document) | [DocumentAccess](DocumentAccess.md) | Creates a class, or returns the existing class of that name. |
| [`createColumn`](ObjectsArchitect.md#createcolumn) | [Architecture](ObjectsArchitect.md#architecture) | [ObjectsArchitect](ObjectsArchitect.md) | Creates a column. |
| [`createConnectCADDevice`](ObjectsConnectCAD.md#createconnectcaddevice) | [ConnectCAD](ObjectsConnectCAD.md#connectcad) | [ObjectsConnectCAD](ObjectsConnectCAD.md) | Creates a schematic device with all its sockets from a device description. |
| [`createConnectCADDevices`](ObjectsConnectCAD.md#createconnectcaddevices) | [ConnectCAD](ObjectsConnectCAD.md#connectcad) | [ObjectsConnectCAD](ObjectsConnectCAD.md) | Creates several schematic devices in a row in one operation. |
| [`createConnectCADDeviceType`](ObjectsConnectCAD.md#createconnectcaddevicetype) | [ConnectCAD](ObjectsConnectCAD.md#connectcad) | [ObjectsConnectCAD](ObjectsConnectCAD.md) | Creates the device-type symbol of a device. |
| [`createDataTag`](ObjectsAnnotation.md#createdatatag) | [Annotation](ObjectsAnnotation.md#annotation) | [ObjectsAnnotation](ObjectsAnnotation.md) | Creates a data tag, optionally attached to an object. |
| [`createDoor`](ObjectsArchitect.md#createdoor) | [Architecture](ObjectsArchitect.md#architecture) | [ObjectsArchitect](ObjectsArchitect.md) | Creates a free-standing door. |
| [`createExistingTree`](ObjectsLandmark.md#createexistingtree) | [Landmark](ObjectsLandmark.md#landmark) | [ObjectsLandmark](ObjectsLandmark.md) | Creates an existing tree. |
| [`createExtrude`](Objects3D.md#createextrude) | [3D Modeling](Objects3D.md#3d-modeling) | [Objects3D](Objects3D.md) | Creates an extrude, a multiple extrude or a tapered extrude. |
| [`createHardscape`](ObjectsLandmark.md#createhardscape) | [Landmark](ObjectsLandmark.md#landmark) | [ObjectsLandmark](ObjectsLandmark.md) | Creates a hardscape from a 2D path object. |
| [`createLandscapeArea`](ObjectsLandmark.md#createlandscapearea) | [Landmark](ObjectsLandmark.md#landmark) | [ObjectsLandmark](ObjectsLandmark.md) | Creates a landscape area from a 2D path object. |
| [`createLayer`](DocumentAccess.md#createlayer) | [Document](DocumentAccess.md#document) | [DocumentAccess](DocumentAccess.md) | Creates a design layer or a sheet layer. |
| [`createLightingDevice`](ObjectsSpotlight.md#createlightingdevice) | [Spotlight](ObjectsSpotlight.md#spotlight) | [ObjectsSpotlight](ObjectsSpotlight.md) | Creates a lighting device, optionally with a GDTF fixture type. |
| [`createLine`](ObjectPrimitives.md#createline) | [Draw2D](ObjectPrimitives.md#draw2d) | [ObjectPrimitives](ObjectPrimitives.md) | Creates a straight line between two points. |
| [`createLinearDimension`](ObjectsAnnotation.md#createlineardimension) | [Dimensioning](ObjectsAnnotation.md#dimensioning) | [ObjectsAnnotation](ObjectsAnnotation.md) | Creates a constrained, horizontal, vertical, unconstrained or ordinate linear dimension. |
| [`createLocus`](ObjectPrimitives.md#createlocus) | [Draw2D](ObjectPrimitives.md#draw2d) | [ObjectPrimitives](ObjectPrimitives.md) | Creates a 2D locus (reference point). |
| [`createMesh`](Objects3D.md#createmesh) | [3D Modeling](Objects3D.md#3d-modeling) | [Objects3D](Objects3D.md) | Creates a mesh from vertices and faces, from polygons or from a group of 3D polygons. |
| [`createNurbsCurve`](Objects3D.md#createnurbscurve) | [3D Modeling](Objects3D.md#3d-modeling) | [Objects3D](Objects3D.md) | Creates a NURBS curve from control points or fit points. |
| [`createNurbsSurface`](Objects3D.md#createnurbssurface) | [3D Modeling](Objects3D.md#3d-modeling) | [Objects3D](Objects3D.md) | Creates a NURBS surface from its control net. |
| [`createPlant`](ObjectsLandmark.md#createplant) | [Landmark](ObjectsLandmark.md#landmark) | [ObjectsLandmark](ObjectsLandmark.md) | Creates a plant at a point or along a path. |
| [`createPluginObject`](ObjectPrimitives.md#createpluginobject) | [Objects](ObjectPrimitives.md#objects) | [ObjectPrimitives](ObjectPrimitives.md) | Creates a plug-in object that has no dedicated create tool. |
| [`createPolygon`](ObjectPrimitives.md#createpolygon) | [Draw2D](ObjectPrimitives.md#draw2d) | [ObjectPrimitives](ObjectPrimitives.md) | Creates a polygon from points, or a regular polygon. |
| [`createPolyline`](ObjectPrimitives.md#createpolyline) | [Draw2D](ObjectPrimitives.md#draw2d) | [ObjectPrimitives](ObjectPrimitives.md) | Creates a polyline from vertices of any vertex type, or a rounded shape. |
| [`createPropertyLine`](ObjectsLandmark.md#createpropertyline) | [Landmark](ObjectsLandmark.md#landmark) | [ObjectsLandmark](ObjectsLandmark.md) | Creates a property line from a closed 2D path object. |
| [`createRadialDimension`](ObjectsAnnotation.md#createradialdimension) | [Dimensioning](ObjectsAnnotation.md#dimensioning) | [ObjectsAnnotation](ObjectsAnnotation.md) | Creates a radial or diametrical dimension. |
| [`createRectangle`](ObjectPrimitives.md#createrectangle) | [Draw2D](ObjectPrimitives.md#draw2d) | [ObjectPrimitives](ObjectPrimitives.md) | Creates a rectangle, optionally rotated and with rounded corners. |
| [`createResource`](Resources.md#createresource) | [Resources](Resources.md#resources) | [Resources](Resources.md) | Creates an empty resource. |
| [`createRoof`](ObjectsArchitect.md#createroof) | [Architecture](ObjectsArchitect.md#architecture) | [ObjectsArchitect](ObjectsArchitect.md) | Creates a polygonal roof. |
| [`createShell`](Objects3D.md#createshell) | [3D Modeling](Objects3D.md#3d-modeling) | [Objects3D](Objects3D.md) | Creates a shell by thickening a NURBS surface or hollowing a solid. |
| [`createSiteModel`](ObjectsLandmark.md#createsitemodel) | [Landmark](ObjectsLandmark.md#landmark) | [ObjectsLandmark](ObjectsLandmark.md) | Creates an empty site model. |
| [`createSiteModifier`](ObjectsLandmark.md#createsitemodifier) | [Landmark](ObjectsLandmark.md#landmark) | [ObjectsLandmark](ObjectsLandmark.md) | Creates a site modifier from a 2D path object. |
| [`createSlab`](ObjectsArchitect.md#createslab) | [Architecture](ObjectsArchitect.md#architecture) | [ObjectsArchitect](ObjectsArchitect.md) | Creates a slab from a 2D boundary object. |
| [`createSolidPrimitive`](Objects3D.md#createsolidprimitive) | [3D Modeling](Objects3D.md#3d-modeling) | [Objects3D](Objects3D.md) | Creates a sphere, ellipsoid, hemisphere, cone, box, cylinder or torus. |
| [`createStair`](ObjectsArchitect.md#createstair) | [Architecture](ObjectsArchitect.md#architecture) | [ObjectsArchitect](ObjectsArchitect.md) | Creates a stair. |
| [`createStake`](ObjectsLandmark.md#createstake) | [Landmark](ObjectsLandmark.md#landmark) | [ObjectsLandmark](ObjectsLandmark.md) | Creates a stake (elevation point). |
| [`createStory`](DocumentAccess.md#createstory) | [Document](DocumentAccess.md#document) | [DocumentAccess](DocumentAccess.md) | Creates one or more stories with their levels. |
| [`createSurfaceModel`](Objects3D.md#createsurfacemodel) | [3D Modeling](Objects3D.md#3d-modeling) | [Objects3D](Objects3D.md) | Creates a loft, rail sweep, revolve or extrude-along-path surface model from existing objects. |
| [`createSweep`](Objects3D.md#createsweep) | [3D Modeling](Objects3D.md#3d-modeling) | [Objects3D](Objects3D.md) | Creates a sweep: 2D profiles revolved about an axis. |
| [`createText`](ObjectPrimitives.md#createtext) | [Draw2D](ObjectPrimitives.md#draw2d) | [ObjectPrimitives](ObjectPrimitives.md) | Creates a text object. |
| [`createTitleBlock`](ObjectsAnnotation.md#createtitleblock) | [Annotation](ObjectsAnnotation.md#annotation) | [ObjectsAnnotation](ObjectsAnnotation.md) | Creates a title block border. |
| [`createWall`](ObjectsArchitect.md#createwall) | [Architecture](ObjectsArchitect.md#architecture) | [ObjectsArchitect](ObjectsArchitect.md) | Creates a straight or round wall. |
| [`createWindow`](ObjectsArchitect.md#createwindow) | [Architecture](ObjectsArchitect.md#architecture) | [ObjectsArchitect](ObjectsArchitect.md) | Creates a free-standing window. |

### Index D

| Tool | Group | Page | Summary |
|---|---|---|---|
| [`describePythonApi`](Scripting.md#describepythonapi) | [Scripting](Scripting.md#scripting) | [Scripting](Scripting.md) | Returns the help text of the Python `api` module or one of its names. |

### Index E

| Tool | Group | Page | Summary |
|---|---|---|---|
| [`edit3DGeometry`](Objects3D.md#edit3dgeometry) | [3D Modeling](Objects3D.md#3d-modeling) | [Objects3D](Objects3D.md) | Edits a 3D polygon, mesh, NURBS curve or NURBS surface. |
| [`editClass`](DocumentAccess.md#editclass) | [Document](DocumentAccess.md#document) | [DocumentAccess](DocumentAccess.md) | Changes a class: description, visibility, pen, fill, markers, drop shadow and more. |
| [`editLayer`](DocumentAccess.md#editlayer) | [Document](DocumentAccess.md#document) | [DocumentAccess](DocumentAccess.md) | Changes the properties of a layer: name, visibility, scale, elevation, thickness and more. |
| [`editObject`](ObjectPrimitives.md#editobject) | [Objects](ObjectPrimitives.md#objects) | [ObjectPrimitives](ObjectPrimitives.md) | Moves, rotates, scales, mirrors, duplicates, regroups, converts, resets or deletes an object, or changes its name and class. |
| [`editResource`](Resources.md#editresource) | [Resources](Resources.md#resources) | [Resources](Resources.md) | Renames, describes, moves, duplicates or deletes a resource. |
| [`editSelection`](DocumentAccess.md#editselection) | [Selection](DocumentAccess.md#selection) | [DocumentAccess](DocumentAccess.md) | Moves, rotates, scales, duplicates, groups, deletes or re-classes the selection. |
| [`editSolid`](Objects3D.md#editsolid) | [3D Modeling](Objects3D.md#3d-modeling) | [Objects3D](Objects3D.md) | Moves, rotates, scales, re-orients or resizes a solid. |
| [`editStory`](DocumentAccess.md#editstory) | [Document](DocumentAccess.md#document) | [DocumentAccess](DocumentAccess.md) | Changes a story, the level types of the document or its default story levels. |
| [`editText`](ObjectPrimitives.md#edittext) | [Draw2D](ObjectPrimitives.md#draw2d) | [ObjectPrimitives](ObjectPrimitives.md) | Edits the content and formatting of a text object. |
| [`editVertices`](ObjectPrimitives.md#editvertices) | [Draw2D](ObjectPrimitives.md#draw2d) | [ObjectPrimitives](ObjectPrimitives.md) | Adds, inserts, changes, deletes, reverses or replaces the vertices of a polygon or polyline. |
| [`editWorksheet`](Resources.md#editworksheet) | [Resources](Resources.md#resources) | [Resources](Resources.md) | Changes a worksheet with a list of actions. |

### Index F

| Tool | Group | Page | Summary |
|---|---|---|---|
| [`findMenuCommands`](MenuAccess.md#findmenucommands) | [Menus](MenuAccess.md#menus) | [MenuAccess](MenuAccess.md) | Finds installed menu commands by text and by workspace. |
| [`findObjects`](ObjectPrimitives.md#findobjects) | [Objects](ObjectPrimitives.md#objects) | [ObjectPrimitives](ObjectPrimitives.md) | Finds the objects that match a criteria string. |

### Index G

| Tool | Group | Page | Summary |
|---|---|---|---|
| [`get3DGeometry`](Objects3D.md#get3dgeometry) | [3D Modeling](Objects3D.md#3d-modeling) | [Objects3D](Objects3D.md) | Reads a 3D polygon, mesh, NURBS curve or NURBS surface. |
| [`getActiveTool`](ToolAccess.md#getactivetool) | [InteractiveTools](ToolAccess.md#interactivetools) | [ToolAccess](ToolAccess.md) | Returns the state of the active tool. |
| [`getAnnotationObject`](ObjectsAnnotation.md#getannotationobject) | [Annotation](ObjectsAnnotation.md#annotation) | [ObjectsAnnotation](ObjectsAnnotation.md) | Reads a data tag or a title block border. |
| [`getArchitectureObject`](ObjectsArchitect.md#getarchitectureobject) | [Architecture](ObjectsArchitect.md#architecture) | [ObjectsArchitect](ObjectsArchitect.md) | Reads the properties of a wall, slab, roof, door, window, column or stair. |
| [`getClasses`](DocumentAccess.md#getclasses) | [Document](DocumentAccess.md#document) | [DocumentAccess](DocumentAccess.md) | Lists the classes of the document and names the special classes. |
| [`getConnectCADDevice`](ObjectsConnectCAD.md#getconnectcaddevice) | [ConnectCAD](ObjectsConnectCAD.md#connectcad) | [ObjectsConnectCAD](ObjectsConnectCAD.md) | Reads a ConnectCAD device and its sockets. |
| [`getConnectCADDeviceType`](ObjectsConnectCAD.md#getconnectcaddevicetype) | [ConnectCAD](ObjectsConnectCAD.md#connectcad) | [ObjectsConnectCAD](ObjectsConnectCAD.md) | Reads the Device Definition record of a device-type symbol. |
| [`getDimension`](ObjectsAnnotation.md#getdimension) | [Dimensioning](ObjectsAnnotation.md#dimensioning) | [ObjectsAnnotation](ObjectsAnnotation.md) | Reads a dimension: its kind, measured points, value and text settings. |
| [`getDocumentInfo`](DocumentAccess.md#getdocumentinfo) | [Document](DocumentAccess.md#document) | [DocumentAccess](DocumentAccess.md) | Returns a summary of the active document: file, counts, page bounds, view center and user origin. |
| [`getGeometry`](ObjectPrimitives.md#getgeometry) | [Draw2D](ObjectPrimitives.md#draw2d) | [ObjectPrimitives](ObjectPrimitives.md) | Reads the type-specific geometry of a 2D primitive. |
| [`getIFCMapping`](IFC.md#getifcmapping) | [IFC Data Mapping](IFC.md#ifc-data-mapping) | [IFC](IFC.md) | Reads the Data Manager mapping of one mapping object. |
| [`getIFCPsetDefinition`](IFC.md#getifcpsetdefinition) | [IFC](IFC.md#ifc) | [IFC](IFC.md) | Reads one IFC property-set definition by name. |
| [`getLandmarkObject`](ObjectsLandmark.md#getlandmarkobject) | [Landmark](ObjectsLandmark.md#landmark) | [ObjectsLandmark](ObjectsLandmark.md) | Reads the properties of a site or landscape object. |
| [`getLayers`](DocumentAccess.md#getlayers) | [Document](DocumentAccess.md#document) | [DocumentAccess](DocumentAccess.md) | Lists the layers with their kind, visibility, scale, elevation, object count and bounds. |
| [`getLightingDevice`](ObjectsSpotlight.md#getlightingdevice) | [Spotlight](ObjectsSpotlight.md#spotlight) | [ObjectsSpotlight](ObjectsSpotlight.md) | Reads a lighting device. |
| [`getMenus`](MenuAccess.md#getmenus) | [Menus](MenuAccess.md#menus) | [MenuAccess](MenuAccess.md) | Reads the menu bar of the current workspace, one menu, or the items of a chunk. |
| [`getMenuStatus`](MenuAccess.md#getmenustatus) | [Menus](MenuAccess.md#menus) | [MenuAccess](MenuAccess.md) | Tells whether a menu command or chunk item can run now, and why not. |
| [`getObjectAttributes`](ObjectPrimitives.md#getobjectattributes) | [Objects](ObjectPrimitives.md#objects) | [ObjectPrimitives](ObjectPrimitives.md) | Returns the graphical attributes of an object. |
| [`getObjectDimensions`](ObjectsAnnotation.md#getobjectdimensions) | [Dimensioning](ObjectsAnnotation.md#dimensioning) | [ObjectsAnnotation](ObjectsAnnotation.md) | Lists the dimensions associated with an object. |
| [`getObjectIFCData`](IFC.md#getobjectifcdata) | [IFC](IFC.md#ifc) | [IFC](IFC.md) | Reads the IFC data of an object as IFC export computes it. |
| [`getObjectInfo`](ObjectPrimitives.md#getobjectinfo) | [Objects](ObjectPrimitives.md#objects) | [ObjectPrimitives](ObjectPrimitives.md) | Returns the identity, class, layer, bounds, state and container of an object. |
| [`getObjectParameters`](ObjectPrimitives.md#getobjectparameters) | [Objects](ObjectPrimitives.md#objects) | [ObjectPrimitives](ObjectPrimitives.md) | Reads the parameters of a plug-in object. |
| [`getObjectRecords`](ObjectPrimitives.md#getobjectrecords) | [Objects](ObjectPrimitives.md#objects) | [ObjectPrimitives](ObjectPrimitives.md) | Reads the data records attached to an object. |
| [`getObjectsAtPoint`](ObjectPrimitives.md#getobjectsatpoint) | [Objects](ObjectPrimitives.md#objects) | [ObjectPrimitives](ObjectPrimitives.md) | Finds the objects at a point. |
| [`getObjectTags`](ObjectsAnnotation.md#getobjecttags) | [Annotation](ObjectsAnnotation.md#annotation) | [ObjectsAnnotation](ObjectsAnnotation.md) | Lists the data tags attached to an object. |
| [`getOIPControls`](OIPAccess.md#getoipcontrols) | [Object Info](OIPAccess.md#object-info) | [OIPAccess](OIPAccess.md) | Lists the controls of one pane of the Object Info palette. |
| [`getPluginDefinition`](ObjectPrimitives.md#getplugindefinition) | [Objects](ObjectPrimitives.md#objects) | [ObjectPrimitives](ObjectPrimitives.md) | Describes an installed plug-in object: its kind, parameters and pop-up choices. |
| [`getPreferences`](DocumentAccess.md#getpreferences) | [Document](DocumentAccess.md#document) | [DocumentAccess](DocumentAccess.md) | Reads one category of document preferences. |
| [`getProjectData`](ObjectsAnnotation.md#getprojectdata) | [Annotation](ObjectsAnnotation.md#annotation) | [ObjectsAnnotation](ObjectsAnnotation.md) | Reads the title block project data of the document. |
| [`getPythonApiGuide`](Scripting.md#getpythonapiguide) | [Scripting](Scripting.md#scripting) | [Scripting](Scripting.md) | Returns one section of the guide for writing Python scripts. |
| [`getResource`](Resources.md#getresource) | [Resources](Resources.md#resources) | [Resources](Resources.md) | Reads one resource of the drawing. |
| [`getResourceDetails`](Resources.md#getresourcedetails) | [Resources](Resources.md#resources) | [Resources](Resources.md) | Reads what a resource holds: hatch levels, gradient stops, line type dashes and more. |
| [`getResources`](Resources.md#getresources) | [Resources](Resources.md#resources) | [Resources](Resources.md) | Lists the resources of one type from the drawing, a library, a file or another document. |
| [`getResourceTypes`](Resources.md#getresourcetypes) | [Resources](Resources.md#resources) | [Resources](Resources.md) | Lists the resource types and the standard content folders. |
| [`getScript`](Scripting.md#getscript) | [Scripting](Scripting.md#scripting) | [Scripting](Scripting.md) | Reads a script resource without running it. |
| [`getSelection`](DocumentAccess.md#getselection) | [Selection](DocumentAccess.md#selection) | [DocumentAccess](DocumentAccess.md) | Lists the selected objects on every layer and the bounds of the selection. |
| [`getSolid`](Objects3D.md#getsolid) | [3D Modeling](Objects3D.md#3d-modeling) | [Objects3D](Objects3D.md) | Reads a solid: its kind, 3D bounds, parameters and Generic Solid history. |
| [`getStories`](DocumentAccess.md#getstories) | [Document](DocumentAccess.md#document) | [DocumentAccess](DocumentAccess.md) | Lists the stories (building floors) with their levels, lowest first. |
| [`getText`](ObjectPrimitives.md#gettext) | [Draw2D](ObjectPrimitives.md#draw2d) | [ObjectPrimitives](ObjectPrimitives.md) | Reads a text object: its content, character formatting, style and layout. |
| [`getTool`](ToolAccess.md#gettool) | [InteractiveTools](ToolAccess.md#interactivetools) | [ToolAccess](ToolAccess.md) | Returns one tool with its declared mode buttons. |
| [`getToolModes`](ToolAccess.md#gettoolmodes) | [InteractiveTools](ToolAccess.md#interactivetools) | [ToolAccess](ToolAccess.md) | Reads the live mode bar of the active tool. |
| [`getTools`](ToolAccess.md#gettools) | [InteractiveTools](ToolAccess.md#interactivetools) | [ToolAccess](ToolAccess.md) | Lists the Vectorworks tools. |
| [`getUnits`](DocumentAccess.md#getunits) | [Document](DocumentAccess.md#document) | [DocumentAccess](DocumentAccess.md) | Returns the primary and secondary unit settings of the document. |
| [`getWorksheet`](Resources.md#getworksheet) | [Resources](Resources.md#resources) | [Resources](Resources.md) | Reads a worksheet: its size, cells, formats and database rows. |

### Index I

| Tool | Group | Page | Summary |
|---|---|---|---|
| [`importGDTF`](ObjectsSpotlight.md#importgdtf) | [Spotlight](ObjectsSpotlight.md#spotlight) | [ObjectsSpotlight](ObjectsSpotlight.md) | Imports a .gdtf file into the drawing as a GDTF fixture type. |
| [`importResource`](Resources.md#importresource) | [Resources](Resources.md#resources) | [Resources](Resources.md) | Imports an external resource into the drawing. |

### Index L

| Tool | Group | Page | Summary |
|---|---|---|---|
| [`listConnectCADConnectors`](ObjectsConnectCAD.md#listconnectcadconnectors) | [ConnectCAD](ObjectsConnectCAD.md#connectcad) | [ObjectsConnectCAD](ObjectsConnectCAD.md) | Lists the ConnectCAD connector types and their pins. |
| [`listConnectCADSignals`](ObjectsConnectCAD.md#listconnectcadsignals) | [ConnectCAD](ObjectsConnectCAD.md#connectcad) | [ObjectsConnectCAD](ObjectsConnectCAD.md) | Lists the ConnectCAD signal types. |
| [`listGDTFs`](ObjectsSpotlight.md#listgdtfs) | [Spotlight](ObjectsSpotlight.md#spotlight) | [ObjectsSpotlight](ObjectsSpotlight.md) | Lists the available GDTF fixture types and their DMX modes. |
| [`listIFCCustomPsets`](IFC.md#listifccustompsets) | [IFC](IFC.md#ifc) | [IFC](IFC.md) | Lists the custom IFC property-set definitions of the document. |
| [`listIFCMappingObjects`](IFC.md#listifcmappingobjects) | [IFC Data Mapping](IFC.md#ifc-data-mapping) | [IFC](IFC.md) | Lists the mapping objects of the active Data Manager mapping. |
| [`listIFCPsets`](IFC.md#listifcpsets) | [IFC](IFC.md#ifc) | [IFC](IFC.md) | Lists the IFC property sets applicable to an IFC entity type. |
| [`listScripts`](Scripting.md#listscripts) | [Scripting](Scripting.md#scripting) | [Scripting](Scripting.md) | Lists the script resources of the document. |
| [`listToolGroups`](Common.md#listtoolgroups) | [Core](Common.md#core-group) | [Common](Common.md) | List all tool groups, active and inactive, with their activation state and, optionally, their tools. |

### Index P

| Tool | Group | Page | Summary |
|---|---|---|---|
| [`pressOIPButton`](OIPAccess.md#pressoipbutton) | [Object Info](OIPAccess.md#object-info) | [OIPAccess](OIPAccess.md) | Presses a button of the Object Info palette. |

### Index Q

| Tool | Group | Page | Summary |
|---|---|---|---|
| [`queryGeometry`](ObjectPrimitives.md#querygeometry) | [Draw2D](ObjectPrimitives.md#draw2d) | [ObjectPrimitives](ObjectPrimitives.md) | Answers geometric questions about a 2D primitive: closest point, distance, containment, intersections, tangents and measurements along curves. |

### Index R

| Tool | Group | Page | Summary |
|---|---|---|---|
| [`runMenuCommand`](MenuAccess.md#runmenucommand) | [Menus](MenuAccess.md#menus) | [MenuAccess](MenuAccess.md) | Runs a menu command or chunk item as if the user chose it. |
| [`runPythonScript`](Scripting.md#runpythonscript) | [Scripting](Scripting.md#scripting) | [Scripting](Scripting.md) | Runs Python code in Vectorworks. |
| [`runScript`](Scripting.md#runscript) | [Scripting](Scripting.md#scripting) | [Scripting](Scripting.md) | Runs a saved Python script resource. |
| [`runToolBatch`](Common.md#runtoolbatch) | [Core](Common.md#core-group) | [Common](Common.md) | Run several tool calls as one undo step, all or nothing. |

### Index S

| Tool | Group | Page | Summary |
|---|---|---|---|
| [`saveScript`](Scripting.md#savescript) | [Scripting](Scripting.md#scripting) | [Scripting](Scripting.md) | Creates or updates a Python script resource without running it. |
| [`selectObjects`](DocumentAccess.md#selectobjects) | [Selection](DocumentAccess.md#selection) | [DocumentAccess](DocumentAccess.md) | Selects or deselects objects by criteria or by UUID, or all or none. |
| [`sendToolAction`](ToolAccess.md#sendtoolaction) | [InteractiveTools](ToolAccess.md#interactivetools) | [ToolAccess](ToolAccess.md) | Finishes or cancels the action of the active tool, or removes its last point. |
| [`sendToolPointer`](ToolAccess.md#sendtoolpointer) | [InteractiveTools](ToolAccess.md#interactivetools) | [ToolAccess](ToolAccess.md) | Clicks, double-clicks, hovers or drags in the drawing with the active tool. |
| [`setActiveContext`](DocumentAccess.md#setactivecontext) | [Document](DocumentAccess.md#document) | [DocumentAccess](DocumentAccess.md) | Sets the active layer and class and how the other layers and classes are shown. |
| [`setAnnotationObject`](ObjectsAnnotation.md#setannotationobject) | [Annotation](ObjectsAnnotation.md#annotation) | [ObjectsAnnotation](ObjectsAnnotation.md) | Edits a data tag or a title block border. |
| [`setArchitectureObject`](ObjectsArchitect.md#setarchitectureobject) | [Architecture](ObjectsArchitect.md#architecture) | [ObjectsArchitect](ObjectsArchitect.md) | Edits a wall, slab, roof, door, window, column or stair. |
| [`setConnectCADSocket`](ObjectsConnectCAD.md#setconnectcadsocket) | [ConnectCAD](ObjectsConnectCAD.md#connectcad) | [ObjectsConnectCAD](ObjectsConnectCAD.md) | Edits a socket. |
| [`setDimension`](ObjectsAnnotation.md#setdimension) | [Dimensioning](ObjectsAnnotation.md#dimensioning) | [ObjectsAnnotation](ObjectsAnnotation.md) | Edits a dimension. |
| [`setGeometry`](ObjectPrimitives.md#setgeometry) | [Draw2D](ObjectPrimitives.md#draw2d) | [ObjectPrimitives](ObjectPrimitives.md) | Edits the geometry of a 2D primitive. |
| [`setLandmarkObject`](ObjectsLandmark.md#setlandmarkobject) | [Landmark](ObjectsLandmark.md#landmark) | [ObjectsLandmark](ObjectsLandmark.md) | Edits a site or landscape object. |
| [`setLightingDevice`](ObjectsSpotlight.md#setlightingdevice) | [Spotlight](ObjectsSpotlight.md#spotlight) | [ObjectsSpotlight](ObjectsSpotlight.md) | Edits a lighting device. |
| [`setObjectAttributes`](ObjectPrimitives.md#setobjectattributes) | [Objects](ObjectPrimitives.md#objects) | [ObjectPrimitives](ObjectPrimitives.md) | Sets graphical attributes of an object: pen, fill, opacity, markers, drop shadow and more. |
| [`setObjectParameter`](ObjectPrimitives.md#setobjectparameter) | [Objects](ObjectPrimitives.md#objects) | [ObjectPrimitives](ObjectPrimitives.md) | Writes one or more parameters of a plug-in object. |
| [`setOIPValues`](OIPAccess.md#setoipvalues) | [Object Info](OIPAccess.md#object-info) | [OIPAccess](OIPAccess.md) | Sets controls of the Object Info palette, as a user does. |
| [`setPreferences`](DocumentAccess.md#setpreferences) | [Document](DocumentAccess.md#document) | [DocumentAccess](DocumentAccess.md) | Writes document preferences of one category. |
| [`setProjectData`](ObjectsAnnotation.md#setprojectdata) | [Annotation](ObjectsAnnotation.md#annotation) | [ObjectsAnnotation](ObjectsAnnotation.md) | Writes the title block project data of the document. |
| [`setResourceDetails`](Resources.md#setresourcedetails) | [Resources](Resources.md#resources) | [Resources](Resources.md) | Changes what a resource holds. |
| [`setToolMode`](ToolAccess.md#settoolmode) | [InteractiveTools](ToolAccess.md#interactivetools) | [ToolAccess](ToolAccess.md) | Changes one mode of the active tool. |
| [`setToolModes`](ToolAccess.md#settoolmodes) | [InteractiveTools](ToolAccess.md#interactivetools) | [ToolAccess](ToolAccess.md) | Sets several modes of the active tool. |
| [`setUnits`](DocumentAccess.md#setunits) | [Document](DocumentAccess.md#document) | [DocumentAccess](DocumentAccess.md) | Changes the primary or secondary unit settings of the document. |
| [`setView`](DocumentAccess.md#setview) | [Document](DocumentAccess.md#document) | [DocumentAccess](DocumentAccess.md) | Moves the view, sets the zoom, moves the user origin or redraws the page. |

### Index T

| Tool | Group | Page | Summary |
|---|---|---|---|
| [`tagObject`](ObjectsAnnotation.md#tagobject) | [Annotation](ObjectsAnnotation.md#annotation) | [ObjectsAnnotation](ObjectsAnnotation.md) | Attaches a data tag to an object, or detaches it. |

### Index V

| Tool | Group | Page | Summary |
|---|---|---|---|
| [`validateConnectCADDevice`](ObjectsConnectCAD.md#validateconnectcaddevice) | [ConnectCAD](ObjectsConnectCAD.md#connectcad) | [ObjectsConnectCAD](ObjectsConnectCAD.md) | Checks a device description without creating anything. |

## Page layout

Every page of a tool folder follows the same layout:

1. **Title** — the folder and its subject, the server and the Vectorworks version, and a link back to this index.
2. **Table of contents** — every group and every tool of the page.
3. **Overview** — one row per group: group ID, whether it is active by default, risk level, number of tools and a one-line summary.
4. **Groups** — for each group: its group ID, activation and risk level, a summary, the description that the server reports, and a table of its tools with effect, risk level and summary.
5. **Tools** — for each tool: a one-line summary; its effect, risk level, undo behavior and whether it can run inside `runToolBatch`; the **Details** that the server reports; and the **Parameters** table (name, type, required, description). Members of object parameters are listed as `parameter.member`, members of array items as `parameter[].member`. Where known, the **Result** section lists the result keys, **Errors** lists the failures, and a **Note** adds behavior that the description does not state.

Shared formats link to [Common](Common.md) and [Attributes](Attributes.md), for example [point](Common.md#points), [color](Common.md#colors) or [marker](Attributes.md#line-end-markers).

## Statistics

| Page | Groups | Tools | Parameters | Read-only | Edit | Interactive | Script run |
|---|---|---|---|---|---|---|---|
| [DocumentAccess](DocumentAccess.md) | 2 | 20 | 129 | 8 | 12 | 0 | 0 |
| [IFC](IFC.md) | 2 | 6 | 8 | 6 | 0 | 0 | 0 |
| [MenuAccess](MenuAccess.md) | 1 | 4 | 19 | 3 | 0 | 1 | 0 |
| [ObjectPrimitives](ObjectPrimitives.md) | 2 | 27 | 273 | 10 | 17 | 0 | 0 |
| [Objects3D](Objects3D.md) | 1 | 16 | 193 | 2 | 14 | 0 | 0 |
| [ObjectsAnnotation](ObjectsAnnotation.md) | 2 | 16 | 338 | 5 | 11 | 0 | 0 |
| [ObjectsArchitect](ObjectsArchitect.md) | 1 | 9 | 127 | 1 | 8 | 0 | 0 |
| [ObjectsConnectCAD](ObjectsConnectCAD.md) | 1 | 10 | 39 | 5 | 5 | 0 | 0 |
| [ObjectsLandmark](ObjectsLandmark.md) | 1 | 10 | 190 | 1 | 9 | 0 | 0 |
| [ObjectsSpotlight](ObjectsSpotlight.md) | 1 | 5 | 30 | 2 | 3 | 0 | 0 |
| [OIPAccess](OIPAccess.md) | 1 | 3 | 14 | 1 | 0 | 2 | 0 |
| [Resources](Resources.md) | 1 | 11 | 122 | 5 | 6 | 0 | 0 |
| [Scripting](Scripting.md) | 1 | 7 | 11 | 4 | 1 | 0 | 2 |
| [ToolAccess](ToolAccess.md) | 1 | 10 | 44 | 5 | 0 | 5 | 0 |
| **Total** | **18** | **154** | **1537** | **58** | **86** | **8** | **2** |

Parameters counts the top-level parameters of the tools; members of object parameters and of array items (`parameter.member`, `parameter[].member`) are not counted. Interactive includes the menu command tool. The [Core](Common.md#core-group) group adds 3 always available meta-tools (read-only `listToolGroups`, session setting `activateToolGroups`, batch edit `runToolBatch`) with 5 top-level parameters.

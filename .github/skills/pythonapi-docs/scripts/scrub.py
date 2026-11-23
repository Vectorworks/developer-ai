"""Removes implementation vocabulary from descriptions: the reference is published for Python users."""

import re

# Exact rewrites of single sentences (applied first, on translated text).
PHRASES = [
    # undo
    (' Wraps the SDK SetUndoMethod (CB_SetUndoMethod) callback.', ''),
    (' (SetUndoMethod does not support it), so nothing is requested for it', ''),
    ('Returns `False`, without calling Vectorworks (UndoAndRemove stops debug builds when no event exists), when no event '
     'is being built.', 'Returns `False` when no event is being built.'),
    ('Otherwise it returns `True`: the SDK UndoAndRemove has no result, so it cannot tell whether the event could be '
     'reverted (it cannot if it was not started with isRevertible).',
     'Otherwise it returns `True`, also when the event could not be reverted (it cannot if it was not started with '
     '`revertible`).'),
    ('Does nothing and returns `False` while a script runs that CScriptRunner executes with EScriptUndo::Caller.',
     'Does nothing and returns `False` while the undo of the running script is managed by the application that runs it.'),
    ('an SDK call that records undo', 'an API call that records undo'),
    ('Deprecated: `Delete()` / DeleteObject already insert the undo primitive, so this is rarely needed.',
     'Deprecated: `Delete()` already records the deletion for undo, so this is rarely needed.'),
    # plug-in styles
    ('the style takes it "by style" (gSDK->GetPluginStyleParameterType `kPluginStyleParameter_ByStyle`), "by catalog" '
     '(ByCatalog, or a parameter of the catalog the style uses, gSDK->IsCatalogParameter), or "mixed" (ByMixed, a state '
     'of the style dialogs that is treated as set by the style). `False` for a parameter that the object takes "by '
     'instance" (ByInstance, AllwaysByInstance),',
     'the style takes it "by style", "by catalog" (also a parameter of the catalog the style uses), or "mixed" (a state '
     'of the style dialogs that is treated as set by the style). `False` for a parameter that the object takes "by '
     'instance",'),
    # objects and resources
    ('of any kind, implemented in a script or in the SDK', 'of any kind, defined by a script or by a compiled plug-in'),
    (', the modern SiteModifierEx2 implementation from the Landmark plug-in', ' of the Landmark plug-in'),
    ('which the SDK inserts into the active container', 'which are inserted into the active container'),
    ('Established SDK behavior: reposition the first existing image, or create one on the active layer if absent.',
     'It repositions the first existing image, or creates one on the active layer if absent.'),
    (' backed by dedicated SDK functions', ''),
    (' backed by the SDK slab functions', ''),
    (', as gSDK->GetRoofEdge reports it', ''),
    ('Existing CSG nodes are wrapped/duplicated.', 'Existing CSG solids are used as they are or duplicated.'),
    ('Getters return optional (empty on invalid wrapper or missing parameter).',
     'Getters return `None` for an invalid object or a missing parameter.'),
    ('Setters return bool (`True` on success, `False` on invalid wrapper or missing parameter).',
     'Setters return `True` on success and `False` for an invalid object or a missing parameter.'),
    ('Keep the wrapper returned by `Create()`, or explicitly wrap a known center-mark group.',
     'Keep the object returned by `Create()`, or construct one from the handle of a known center-mark group.'),
    ('do not wrap them as', 'do not use them as'),
    ('Older stair objects are not wrapped', 'Older stair objects are not supported'),
    ('Each subclass header documents the useful parameter names in a "Full parameter reference" block-comment.',
     'Each subclass lists the useful parameter names in its "Full parameter reference".'),
    ('Each subclass header documents the complete list of available parameter names in a "Full parameter reference" '
     'block-comment.', 'Each subclass lists all available parameter names in its "Full parameter reference".'),
    ('The Window, Door, Column and Stair headers document the available parameter names in a "Full parameter reference" '
     'block-comment;', 'The Window, Door, Column and Stair classes list the available parameter names in their "Full '
     'parameter reference";'),
    # math
    ('(the API counterpart of the core ViewPt; ViewCoord is 16 bit)', '(16-bit coordinates)'),
    # user interface automation
    ('; SDK group number is fIndex + 1', ' (0-based)'),
    ('; SDK chunk index is fIndex + 1', ' (0-based)'),
    ('Switchboard type id of the core widget (diagnostics)', 'Internal type id of the control (for diagnostics)'),
    ('(see EAreaUnits)', '(see `LandscapeAreaObject.AreaUnits`)'),
    ('(see EConfig below)', '(see `SiteModifierObject.Config` below)'),
    ('to the left of a->b', 'to the left of the line from `a` to `b`'),
    ('Lightweight and non-owning, like', 'Lightweight, like'),
    ('Move-only: it owns the underlying Vectorworks resource list and disposes it on destruction',
     'It cannot be copied: it holds a Vectorworks resource list and releases it when the Python object is deleted'),
    ('Releases the underlying Vectorworks resource list', 'Releases the Vectorworks resource list'),
    ('Called automatically by the destructor', 'Called automatically when the Python object is deleted'),
    ('with a raw switchboard change info (0 for a plain value change; see Switchboard.DataTypes.X.h for the `kBox`..Changed '
     '/ `kList`..Changed constants of composite controls). The value must already be in the platform OIP.',
     'with a raw change info (0 for a plain value change; composite controls use their own change codes). The value must '
     'already be set in the Object Info palette.'),
    (' (popups; see the sash operation table in MCPProviderImpl.cpp)', ' (popups)'),
    ('Built into the core as a classic tool definition', 'Built into Vectorworks (classic tool)'),
    ('Built into the core as a VCOM IExtensionTool implementation', 'Built into Vectorworks (extension tool)'),
    ('External VCOM IExtensionTool implementation from a plug-in module (SDK)', 'Tool of an external plug-in module'),
    ('VCOM IExtensionMenu implementation from a plug-in module (SDK)', 'Menu command of an external plug-in module'),
    ('How a tool is implemented', 'How a tool is provided'),
    ('How a menu command is implemented', 'How a menu command is provided'),
    ('Every input goes through the same core entry points as real mouse and keyboard input',
     'Every input is processed exactly like real mouse and keyboard input'),
    # wrappers
    ('Like every wrapper of this API it is a lightweight, non-owning view', 'Like every object class of this API it is a lightweight view'),
    ('The wrapper is a non-owning view of the drawing object', 'An instance is a lightweight view of the drawing object'),
    ('A wrapper does not own the object; it only reads and writes attributes of the wrapped handle',
     'An instance does not own the object; it only reads and writes the attributes of the object'),
    ('The list mirrors the internal Vectorworks node type codes', 'The list mirrors the Vectorworks object type codes'),
    # object, tool and user interface names of the Vectorworks help
    ('the Constrained Dimension tool', 'the Constrained Linear Dimension tool'),
    ('the Unconstrained Dimension tool', 'the Unconstrained Linear Dimension tool'),
    ('Covers native CSG nodes, including Boolean solids and history-free Generic Solids.',
     'Covers native solid objects, including solid additions, subtractions and intersections and history-free generic '
     'solids.'),
    ('Creates a new roof container.', 'Creates a new roof object.'),
    ('in a window / door assembly', 'in a door and window assembly'),
    ('a legacy floor slab node (`kSlabNode` of the floor kind) of older files',
     'a floor object (`kSlabNode` of the floor kind, created with the Floor command)'),
    ('a legacy floor slab node (`kSlabNode`) of older files is a slab without a record',
     'a floor object (`kSlabNode` of the floor kind) is a native slab without a record'),
    ('PadwEdge (=Retaining Pad)', 'PadwEdge (=Pad with Retaining Edge)'),
    ('Pad (Config = "Pad") and Retaining Pad (Config = "PadwEdge")',
     'Planar Pad (Config = "Pad") and Pad with Retaining Edge (Config = "PadwEdge")'),
    ('(retaining pad only)', '(pad with retaining edge only)'),
    ('pad with retaining edges (walls) of a fixed height', 'pad with a retaining edge'),
    ('It can be a solid area or a pathway', 'It can be a boundary hardscape or a pathway hardscape'),
    ('Building material (`kBuildingMaterialNode`)', 'Material (building material, `kBuildingMaterialNode`)'),
    ('internal index of a building material', 'internal index of a material'),
    ('instances of it are Symbol objects', 'placed in the drawing as symbol instances'),
    ('Generic parametric (plug-in) object', 'Generic plug-in (parametric) object'),
    ('a Vectorworks "parametric" object (an instance of a plug-in registered by the Landscape / Vectorworks Landmark '
     'module)', 'a Vectorworks plug-in object (an instance of a plug-in registered by the Landscape / Vectorworks '
     'Landmark module; also called a parametric object in the API)'),
    ('Vectorworks "parametric" objects (instances of a plug-in)',
     'Vectorworks plug-in objects (also called parametric objects in the API)'),
    ('or a parametric annotation', 'or an annotation plug-in object'),
    ('handles that are not parametric', 'handles that are not plug-in objects'),
    ('Applies to parametric objects only (Slab, Window, Door, Column, Stair). For Wall / Roof and a legacy floor slab '
     'node the parametric accessors', 'Applies to plug-in objects only (slabs, windows, doors, columns, stairs). For a '
     'wall, a roof or a floor object the parametric accessors'),
    ('(Plant, Landscape Area, Site Model, Site Modifier, Stake, Hardscape, Property Line, Existing Tree)',
     '(plant, landscape area, site model, site modifier, stake, hardscape, property line, existing tree)'),
    ('(Wall, Slab, Roof, Window, Door, Column, Stair)', '(wall, slab, roof, window, door, column, stair)'),
    ('(Data Tag, Title Block Border)', '(data tag, title block border)'),
    ('An unstyled Data Tag has no text layout and an unstyled Title Block Border has',
     'An unstyled data tag has no text layout and an unstyled title block border has'),
    ('reshapes a Site Model surface', 'reshapes a site model surface'),
    ('the entire Site Modifier parameter set', 'the entire site modifier parameter set'),
    ('ConnectCAD Socket (universal name', 'ConnectCAD socket (universal name'),
    ('ConnectCAD schematic Device (universal name', 'ConnectCAD schematic device (universal name'),
    ('a named box with Socket objects', 'a named box with socket objects'),
    ('(or a multi-cell fixture)', '(or a multi-cell lighting device)'),
    ('Stateless view over the mode bar of the active tool',
     'Stateless view over the Tool bar (mode bar) of the active tool'),
    ('the reusable templates in the resource browser', 'the reusable templates in the Resource Manager'),
]

# Regular expressions applied to the whole text (they may span code spans).
RAW = [
    (r'\s*\(the equivalent of VWFC [^)]*\)', ''),
    (r'\s*\(as in VWFC \w+\)', ''),
    (r'\s*\(the API counterpart of the core \w+\)', ''),
    (r'\s*\(gSDK->[^)]*\)', ''),
    (r"\s*\(Core's [^)]*\)", ''),
    (r'\s*\(friend `[^`]+` operator\w*\([^()]*\)\)', ''),
    (r'^friend `[^`]+` operator\w*\([^()]*\)$', ''),
    (r'\s*\(ov[A-Z]\w+\)', ''),
    (r' as ov[A-Z]\w+', ''),
    (r'\s*Handles are non-owning\.?', ''),
    (r'\s*\(`kUndo\w+`\)', ''),
    (r'`kUndo\w+`; ', ''),
    (r'\s*\(`kInternalID_\w+`\)', ''),
    (r'\(`kSlabStyle` resource\)', '(a slab style resource)'),
    (r'\(`kField(\w+)`\)', lambda m: '(%s)' % m.group(1).lower()),
    (r'`kStyle`\* flags', '`TextObject.kStyle...` flags'),
    (r'`kCustom`\* flags', '`TextObject.kCustom...` flags'),
    (r'\s*Wraps the SDK [^.|]*\.', ''),
    (r'\s*Wraps CB_\w+(?: / CB_\w+)*\.', ''),
    (r'\s*Mirrors the `kUndo`\.\.\. selectors of the SDK SetUndoMethod callback\.', ''),
    (r'\s*Use these from MCP tools\.', ''),
    (r'`?\bisRevertible\b`?', '`revertible`'),
    # node constants without the k...Node form
    (r'\(rBoxNode\)', '(`ObjectType.RoundedRectangle`)'),
    (r'\(qPoly\)', '(`ObjectType.Polygon3D`)'),
    (r'\(dimHeaderNode\)', '(`ObjectType.Dimension`)'),
]

# Regular expressions applied outside code spans only.
PROSE = [
    (r'\bVectorWorks\b', 'Vectorworks'),
    (r'\bplain double\b', 'plain number'),
    # wrappers
    (r'\bnon-owning handle wrapper\b', 'lightweight view of the drawing object'),
    (r'\blightweight, non-owning view\b', 'lightweight view'),
    (r'\b([Aa]n) invalid wrapper\b', r'\1 invalid object'),
    (r'\binvalid wrapper\b', 'invalid object'),
    (r'\bWrapper of (one|a|an|the) ', lambda m: m.group(1).capitalize() + ' '),
    (r'\bwrapper of (one|a|an|the) ', r'\1 '),
    (r'\bResource wrapper\b', 'Resource'),
    (r'\bsource wrappers\b', 'source objects'),
    (r'\bsource wrapper\b', 'source object'),
    (r'\bwrappers\b', 'classes'),
    (r'\bWrappers\b', 'Classes'),
    (r'\b([Tt]his) wrapper becomes\b', r'\1 object becomes'),
    (r'\b([Tt]his) wrapper\b', r'\1 class'),
    (r'\bspecific wrapper\b', 'specific class'),
    (r'\bThe wrapper inherits\b', 'The class inherits'),
    (r'\b([Tt]he) wrapper\b', r'\1 object'),
    (r'\bwrapper\b', 'object'),
    (r'\bWrapper\b', 'Object'),
    (r'\b([Tt]he) wrapped (\w+)', r'\1 \2'),
    # node types
    (r'\s*\(node type\)', ''),
    (r'\ba node type\b', 'an object type'),
    (r'\b([Oo]bject) node type', r'\1 type'),
    (r'\bnode type', 'object type'),
    (r'\blegacy floor slab node\b', 'floor object'),
    # the application core
    (r'\bCore-backed\s+', ''),
    (r"\bCore's\b", 'the'),
    (r'\bthe core color representation\b', 'the Vectorworks color representation'),
    (r'\bRead-only Core analysis\b', 'Read-only analysis'),
    (r'\b[Tt]he core (identifies|keeps|creates|fixes|registers|expects)\b', r'Vectorworks \1'),
    (r'\bCore (uses|validates|may|cannot)\b', r'Vectorworks \1'),
    (r'\bto Core\b', 'to Vectorworks'),
    (r'\bthe core folder specifiers\b', 'the Vectorworks folder specifiers'),
    (r'\b(by|into) the core\b', r'\1 Vectorworks'),
    # C++ vocabulary
    (r'\benums\b', 'enumerations'),
    (r'\benum\b', 'enumeration'),
    # object, tool and user interface names of the Vectorworks help (lower case in running text)
    (r'\bround wall(s?)\b', r'curved wall\1'),
    (r'\brender material resources\b', 'texture resources'),
    (r'\bRender material\b', 'Texture'),
    (r'\brender material\b', 'texture'),
    (r'^Renderworks style(s?)\b', r'Render style\1'),
    (r'\bRenderworks style(s?)\b', r'render style\1'),
    (r'(^|[.!?]\s+)Generic Solid(s?)\b', r'\1Generic solid\2'),
    (r'\bGeneric Solid(s?)\b', r'generic solid\1'),
    (r'\blighting symbol(s?)\b', r'lighting device symbol\1'),
    (r'\btitle block style(s?)\b', r'title block border style\1'),
    (r'\btitle block object(s?)\b', r'title block border object\1'),
    (r'\bevery title block\b(?! border)', 'every title block border'),
    (r'\ba title block without a style\b', 'a title block border without a style'),
    (r'\btitle block content\b', 'title block border content'),
    (r'^(Plant|Landscape Area|Site Model|Site Modifier|Stake|Hardscape|Property Line|Existing Tree|Data Tag'
     r'|Title Block Border|Lighting Device|Window|Door|Column|Stair) parametric object\b',
     lambda m: m.group(1)[0] + m.group(1)[1:].lower() + ' plug-in object'),
    (r'\b([Pp])arametric plug-in object(s?)\b', r'\1lug-in object\2'),
    (r'\bparametric plug-in\b', 'plug-in object'),
    (r'\bplug-in parametric(s?)\b', r'plug-in object\1'),
    (r'\b([Pp])arametric object(s?)\b(?! in the API)', r'\1lug-in object\2'),
    (r'\bparametrics\b', 'plug-in objects'),
    (r'\bthe native Wall / Roof objects\b', 'the native wall and roof objects'),
    (r'\bCreates a (Window|Door) at\b', lambda m: 'Creates a %s at' % m.group(1).lower()),
    (r'(?<!\()\b[Mm]ode bar(s?)\b', r'Tool bar\1'),
    (r'\bObject Info Palette\b', 'Object Info palette'),
    (r'\bdrawing pane\b', 'view pane'),
    (r'\b(Organization|Change Story Elevation|Edit Story|New Story|Level Types) dialog\b(?! box)', r'\1 dialog box'),
    (r'\bOrganization dialog box > Stories >', 'Organization dialog box > Stories tab >'),
    (r'\bstory dialogs of the\b', 'story dialog boxes of the'),
    (r'\bthe (?:tool )?preferences dialog\b(?! box)', 'the tool preferences dialog box'),
]

# Paragraphs that only make sense to C++ developers.
DROP = [
    re.compile(r'^Common object variables \(read-only unless noted'),
]

_RAW = [(re.compile(p), r) for p, r in RAW]
_PROSE = [(re.compile(p), r) for p, r in PROSE]
NODE_RE = re.compile(r'`?\bk(\w+?)Node\b`?')


class Scrubber:
    def __init__(self, object_types):
        self.object_types = set(object_types)

    def node(self, m):
        name = m.group(1)
        for cand in (name, re.sub(r'Def$', 'Definition', name)):
            if cand in self.object_types:
                return '`ObjectType.%s`' % cand
        return '`ObjectType`'

    def __call__(self, text):
        if not text:
            return text
        for rx in DROP:
            if rx.search(text):
                return ''
        for old, new in PHRASES:
            if old in text:
                text = text.replace(old, new)
            elif old[:1].isalpha():
                # comments often start lower case; sentence() capitalizes them later
                alt = old[0].swapcase() + old[1:]
                if alt in text:
                    text = text.replace(alt, (new[0].swapcase() + new[1:]) if new[:1].isalpha() else new)
        for rx, rep in _RAW:
            text = rx.sub(rep, text)
        text = NODE_RE.sub(self.node, text)
        parts = re.split(r'(`[^`]*`)', text)
        for k in range(0, len(parts), 2):
            seg = parts[k]
            for rx, rep in _PROSE:
                seg = rx.sub(rep, seg)
            parts[k] = seg
        return ''.join(parts)
